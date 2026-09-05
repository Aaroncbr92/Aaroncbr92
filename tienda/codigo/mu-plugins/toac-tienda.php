<?php
/**
 * Plugin Name: TOAC · Tienda de temarios
 * Description: Catálogo con fecha de actualización, muestra en línea sin descarga, descarga firmada contra pedido pagado y panel «Mis temarios».
 * Version:     1.0.0
 * Author:      TOAC
 * License:     GPL-2.0-or-later
 *
 * Va en wp-content/mu-plugins/ a propósito: desde ahí no se puede desactivar
 * con un clic desde el escritorio. El control de acceso a los ficheros no debe
 * poder apagarse por error.
 *
 * Requiere en wp-config.php las constantes de servidor/wp-config-extra.php.
 */

defined( 'ABSPATH' ) || exit;

final class TOAC_Tienda {

	const VERSION = '1.0.0';

	/** Minutos que vive un enlace de descarga antes de dejar de servir. */
	const VIDA_TOKEN_DESCARGA = 10;

	/** Minutos que vive el enlace del PDF de muestra. */
	const VIDA_TOKEN_MUESTRA = 15;

	/** Descargas por usuario y producto al día. Frena la cuenta compartida. */
	const LIMITE_DIARIO = 8;

	/** Campos propios del producto: clave => etiqueta en el escritorio. */
	const CAMPOS = array(
		'_toac_slug'         => 'Identificador del volumen (p. ej. «sonido» para libro-sonido.pdf)',
		'_toac_actualizado'  => 'Fecha de última actualización (AAAA-MM-DD)',
		'_toac_paginas'      => 'Páginas',
		'_toac_temas'        => 'Temas',
		'_toac_preguntas'    => 'Preguntas reales incluidas',
		'_toac_puestos'      => 'Plazas de la ocupación en la convocatoria',
	);

	public static function arranca() {
		$yo = new self();

		add_action( 'init',                     array( $yo, 'reglas_de_url' ) );
		add_filter( 'query_vars',               array( $yo, 'variables_de_consulta' ) );
		add_action( 'template_redirect',        array( $yo, 'atiende_peticion' ) );
		add_action( 'init',                     array( $yo, 'crea_tabla_si_falta' ), 5 );

		// Escritorio: los campos propios del producto.
		add_action( 'woocommerce_product_options_general_product_data', array( $yo, 'campos_en_escritorio' ) );
		add_action( 'woocommerce_process_product_meta',                 array( $yo, 'guarda_campos' ) );

		// Escaparate: la fecha de actualización y la ficha técnica.
		add_action( 'woocommerce_after_shop_loop_item_title', array( $yo, 'sello_actualizado' ), 9 );
		add_action( 'woocommerce_single_product_summary',     array( $yo, 'ficha_tecnica' ), 21 );
		add_action( 'woocommerce_single_product_summary',     array( $yo, 'boton_muestra' ), 22 );
		add_filter( 'woocommerce_get_catalog_ordering_args',  array( $yo, 'orden_por_actualizacion' ) );
		add_filter( 'woocommerce_catalog_orderby',            array( $yo, 'opcion_de_orden' ) );

		// Panel de cliente. El endpoint se registra dentro de reglas_de_url(),
		// antes del flush: si se registrase en otra llamada a `init` posterior,
		// sus reglas no entrarían en el vaciado y «Mis temarios» daría 404 hasta
		// que alguien volviese a guardar los enlaces permanentes.
		add_filter( 'woocommerce_account_menu_items',           array( $yo, 'menu_mis_temarios' ) );
		add_action( 'woocommerce_account_mis-temarios_endpoint', array( $yo, 'pinta_mis_temarios' ) );
	}

	/* ---------------------------------------------------------------- *
	 *  Rutas
	 * ---------------------------------------------------------------- */

	public function reglas_de_url() {
		add_rewrite_endpoint( 'mis-temarios', EP_ROOT | EP_PAGES );

		add_rewrite_rule( '^descarga/([a-z0-9-]+)/?$', 'index.php?toac_descarga=$matches[1]', 'top' );
		add_rewrite_rule( '^muestra/([a-z0-9-]+)/?$',  'index.php?toac_muestra=$matches[1]',  'top' );
		add_rewrite_rule( '^muestra-pdf/([a-z0-9-]+)/?$', 'index.php?toac_muestra_pdf=$matches[1]', 'top' );

		// Sólo se vacían las reglas cuando cambia la versión, no en cada carga.
		if ( get_option( 'toac_version_reglas' ) !== self::VERSION ) {
			flush_rewrite_rules( false );
			update_option( 'toac_version_reglas', self::VERSION );
		}
	}

	public function variables_de_consulta( $vars ) {
		$vars[] = 'toac_descarga';
		$vars[] = 'toac_muestra';
		$vars[] = 'toac_muestra_pdf';
		return $vars;
	}

	public function atiende_peticion() {
		if ( $slug = get_query_var( 'toac_descarga' ) ) {
			$this->sirve_descarga( sanitize_title( $slug ) );
		}
		if ( $slug = get_query_var( 'toac_muestra' ) ) {
			$this->pinta_visor( sanitize_title( $slug ) );
		}
		if ( $slug = get_query_var( 'toac_muestra_pdf' ) ) {
			$this->sirve_muestra( sanitize_title( $slug ) );
		}
	}

	/* ---------------------------------------------------------------- *
	 *  Firma de enlaces
	 *
	 *  El token no lleva la ruta del fichero: lleva a qué producto se
	 *  refiere. Aunque alguien lo descifre, no aprende dónde está el PDF.
	 * ---------------------------------------------------------------- */

	private function clave() {
		if ( defined( 'TOAC_CLAVE_FIRMA' ) && TOAC_CLAVE_FIRMA ) {
			return TOAC_CLAVE_FIRMA;
		}
		// Respaldo: las sales que WordPress ya tiene. Mejor esto que nada.
		return wp_salt( 'secure_auth' );
	}

	private function firma( $tipo, $producto_id, $usuario_id, $minutos ) {
		$caduca = time() + ( $minutos * MINUTE_IN_SECONDS );
		$carga  = implode( '|', array( $tipo, (int) $producto_id, (int) $usuario_id, $caduca ) );
		$sello  = hash_hmac( 'sha256', $carga, $this->clave() );

		return rtrim( strtr( base64_encode( $carga ), '+/', '-_' ), '=' ) . '.' . $sello;
	}

	/**
	 * Devuelve array( producto_id, usuario_id ) o false. No emite nada.
	 */
	private function comprueba_firma( $token, $tipo_esperado ) {
		if ( ! is_string( $token ) || false === strpos( $token, '.' ) ) {
			return false;
		}
		list( $carga64, $sello ) = explode( '.', $token, 2 );

		$carga = base64_decode( strtr( $carga64, '-_', '+/' ), true );
		if ( false === $carga ) {
			return false;
		}
		// hash_equals compara en tiempo constante: no filtra por dónde falla.
		if ( ! hash_equals( hash_hmac( 'sha256', $carga, $this->clave() ), (string) $sello ) ) {
			return false;
		}

		$partes = explode( '|', $carga );
		if ( 4 !== count( $partes ) ) {
			return false;
		}
		list( $tipo, $producto_id, $usuario_id, $caduca ) = $partes;

		if ( $tipo !== $tipo_esperado || time() > (int) $caduca ) {
			return false;
		}
		return array( (int) $producto_id, (int) $usuario_id );
	}

	/* ---------------------------------------------------------------- *
	 *  Derecho de descarga
	 *
	 *  No se guarda en ninguna parte: se deriva de los pedidos pagados.
	 *  Un estado menos que pueda quedar desincronizado con la realidad.
	 * ---------------------------------------------------------------- */

	private function ha_comprado( $usuario_id, $producto_id ) {
		if ( ! $usuario_id || ! function_exists( 'wc_customer_bought_product' ) ) {
			return false;
		}
		$usuario = get_userdata( $usuario_id );
		if ( ! $usuario ) {
			return false;
		}
		// Comprueba contra los estados que WooCommerce considera pagados.
		return wc_customer_bought_product( $usuario->user_email, $usuario_id, $producto_id );
	}

	private function producto_por_slug( $slug ) {
		$consulta = new WP_Query( array(
			'post_type'      => 'product',
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
			'no_found_rows'  => true,
			'meta_query'     => array( array(
				'key'   => '_toac_slug',
				'value' => $slug,
			) ),
		) );
		return $consulta->posts ? (int) $consulta->posts[0] : 0;
	}

	/* ---------------------------------------------------------------- *
	 *  Descarga
	 * ---------------------------------------------------------------- */

	public function enlace_de_descarga( $producto_id, $usuario_id ) {
		$slug = get_post_meta( $producto_id, '_toac_slug', true );
		if ( ! $slug ) {
			return '';
		}
		return home_url( '/descarga/' . $slug . '/?t=' .
			rawurlencode( $this->firma( 'd', $producto_id, $usuario_id, self::VIDA_TOKEN_DESCARGA ) ) );
	}

	private function sirve_descarga( $slug ) {
		nocache_headers();

		if ( ! is_user_logged_in() ) {
			wp_safe_redirect( wc_get_page_permalink( 'myaccount' ) );
			exit;
		}

		$usuario_id = get_current_user_id();
		$firmado    = $this->comprueba_firma( wp_unslash( $_GET['t'] ?? '' ), 'd' );

		// El token caducado no es un error del usuario: se le devuelve a su panel
		// con un aviso, y desde allí pide otro enlace. Sin fricción.
		if ( ! $firmado ) {
			wp_safe_redirect( add_query_arg( 'toac_aviso', 'caducado',
				wc_get_account_endpoint_url( 'mis-temarios' ) ) );
			exit;
		}

		list( $producto_id, $token_usuario ) = $firmado;

		// El enlace firmado para otro es inservible aunque no haya caducado.
		if ( $token_usuario !== $usuario_id ) {
			$this->corta( 403, 'Este enlace se emitió para otra cuenta.' );
		}
		if ( $this->producto_por_slug( $slug ) !== $producto_id ) {
			$this->corta( 403, 'El enlace no corresponde a este temario.' );
		}
		if ( ! $this->ha_comprado( $usuario_id, $producto_id ) ) {
			$this->corta( 403, 'No consta una compra pagada de este temario en tu cuenta.' );
		}
		if ( $this->descargas_de_hoy( $usuario_id, $producto_id ) >= self::LIMITE_DIARIO ) {
			$this->corta( 429, sprintf(
				'Has alcanzado el límite de %d descargas diarias de este temario. Vuelve mañana o escríbenos.',
				self::LIMITE_DIARIO ) );
		}

		$origen = trailingslashit( TOAC_DIR_LIBROS ) . 'libro-' . $slug . '.pdf';
		if ( ! is_readable( $origen ) ) {
			// Falta el fichero en el servidor: es culpa nuestra, y hay que enterarse.
			error_log( '[TOAC] Falta el volumen: ' . $origen );
			$this->corta( 500, 'El fichero no está disponible ahora mismo. Ya estamos avisados.' );
		}

		$this->anota_descarga( $usuario_id, $producto_id );

		$fichero = $this->sella( $origen, $slug, $usuario_id, $producto_id );
		$nombre  = 'TOAC-' . $slug . '.pdf';

		$this->envia_fichero( $fichero, $nombre, 'attachment' );
	}

	/* ---------------------------------------------------------------- *
	 *  Muestra: visor sin descarga
	 * ---------------------------------------------------------------- */

	private function pinta_visor( $slug ) {
		$producto_id = $this->producto_por_slug( $slug );
		if ( ! $producto_id ) {
			$this->corta( 404, 'Ese temario no existe.' );
		}

		$pdf = home_url( '/muestra-pdf/' . $slug . '/?t=' .
			rawurlencode( $this->firma( 'm', $producto_id, 0, self::VIDA_TOKEN_MUESTRA ) ) );

		// PDF.js autoalojado, con la barra de herramientas recortada por CSS:
		// fuera descargar, imprimir y abrir en otra pestaña.
		$visor = content_url( '/uploads/pdfjs/web/viewer.html' )
			. '?file=' . rawurlencode( $pdf ) . '#pagemode=none';

		// Página autónoma a propósito: `get_header()` no pinta nada en un tema
		// de bloques, y el visor quiere el ancho entero de todas formas.
		nocache_headers();
		header( 'Content-Type: text/html; charset=utf-8' );
		header( 'X-Robots-Tag: noindex, follow' );
		?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="robots" content="noindex">
	<title><?php echo esc_html( 'Muestra · ' . get_the_title( $producto_id ) ); ?></title>
	<?php wp_head(); ?>
</head>
<body class="toac-visor-pagina">
	<main class="toac-visor">
		<h1>Muestra · <?php echo esc_html( get_the_title( $producto_id ) ); ?></h1>
		<p class="toac-visor__nota">
			Portada, índice completo y primeras páginas.
			El temario completo tiene
			<?php echo esc_html( get_post_meta( $producto_id, '_toac_paginas', true ) ); ?> páginas.
		</p>
		<iframe class="toac-visor__marco" src="<?php echo esc_url( $visor ); ?>"
			title="Previsualización del temario" referrerpolicy="same-origin"></iframe>
		<p>
			<a class="button" href="<?php echo esc_url( get_permalink( $producto_id ) ); ?>">
				Volver a la ficha del temario</a>
		</p>
	</main>
	<?php wp_footer(); ?>
</body>
</html>
		<?php
		exit;
	}

	private function sirve_muestra( $slug ) {
		nocache_headers();

		$firmado = $this->comprueba_firma( wp_unslash( $_GET['t'] ?? '' ), 'm' );
		if ( ! $firmado ) {
			$this->corta( 403, 'El enlace de la muestra ha caducado. Recarga la página.' );
		}
		list( $producto_id, ) = $firmado;

		if ( $this->producto_por_slug( $slug ) !== $producto_id ) {
			$this->corta( 403, 'El enlace no corresponde a esta muestra.' );
		}

		$fichero = trailingslashit( TOAC_DIR_MUESTRAS ) . 'muestra-' . $slug . '.pdf';
		if ( ! is_readable( $fichero ) ) {
			$this->corta( 404, 'No hay muestra de este temario todavía.' );
		}

		// inline: se ve dentro del visor, no se ofrece guardar.
		$this->envia_fichero( $fichero, 'muestra-' . $slug . '.pdf', 'inline' );
	}

	/* ---------------------------------------------------------------- *
	 *  Envío del fichero
	 * ---------------------------------------------------------------- */

	private function envia_fichero( $ruta, $nombre, $disposicion ) {
		// Nada de lo que haya salido antes debe acabar dentro del PDF.
		while ( ob_get_level() ) {
			ob_end_clean();
		}

		header( 'Content-Type: application/pdf' );
		header( 'Content-Disposition: ' . $disposicion . '; filename="' . rawurlencode( $nombre ) . '"' );
		header( 'X-Robots-Tag: noindex, nofollow', true );
		header( 'X-Content-Type-Options: nosniff' );
		header( 'Cache-Control: private, no-store, max-age=0' );

		$modo = defined( 'TOAC_ENVIO' ) ? TOAC_ENVIO : 'auto';
		if ( 'auto' === $modo ) {
			$modo = ( false !== stripos( $_SERVER['SERVER_SOFTWARE'] ?? '', 'litespeed' ) )
				? 'litespeed' : 'php';
		}

		// Con sendfile el servidor lee el disco él mismo: PHP no carga en memoria
		// 3,6 MB por cada descarga simultánea, que es lo que tumba un compartido.
		switch ( $modo ) {
			case 'litespeed':
				header( 'X-LiteSpeed-Send-File: ' . $ruta );
				exit;
			case 'xsendfile':
				header( 'X-Sendfile: ' . $ruta );
				exit;
			case 'accel':
				// Requiere un «internal location» en nginx apuntando a la carpeta.
				header( 'X-Accel-Redirect: /privado/' . basename( $ruta ) );
				exit;
		}

		// Respaldo en PHP puro: por trozos, para no agotar la memoria.
		header( 'Content-Length: ' . filesize( $ruta ) );
		header( 'Accept-Ranges: none' );

		if ( function_exists( 'set_time_limit' ) ) {
			@set_time_limit( 0 );
		}
		$mano = fopen( $ruta, 'rb' );
		while ( ! feof( $mano ) ) {
			echo fread( $mano, 512 * 1024 );
			flush();
			if ( connection_aborted() ) {
				break;
			}
		}
		fclose( $mano );
		exit;
	}

	/* ---------------------------------------------------------------- *
	 *  Sellado nominativo
	 *
	 *  Lo que de verdad frena que un temario acabe en un grupo de Telegram
	 *  no es el cifrado: es que lleve el correo de quien lo compró en el pie
	 *  de las 259 páginas. Se sella una vez por comprador y se guarda, para
	 *  no rehacerlo en cada descarga.
	 * ---------------------------------------------------------------- */

	private function sella( $origen, $slug, $usuario_id, $producto_id ) {
		if ( ! defined( 'TOAC_SELLAR' ) || ! TOAC_SELLAR ) {
			return $origen;
		}
		if ( ! class_exists( '\setasign\Fpdi\Fpdi' ) ) {
			return $origen; // Sin la biblioteca, se sirve el original. Nunca se falla.
		}

		if ( ! wp_mkdir_p( TOAC_DIR_SELLADOS ) ) {
			return $origen;
		}
		$destino = trailingslashit( TOAC_DIR_SELLADOS ) . $slug . '-' . $usuario_id . '.pdf';

		// Se rehace si el volumen se ha actualizado después del sellado.
		if ( is_readable( $destino ) && filemtime( $destino ) >= filemtime( $origen ) ) {
			return $destino;
		}

		$usuario = get_userdata( $usuario_id );
		$pie     = sprintf( 'Licencia personal de %s - %s - Pedido en %s - Prohibida su redistribucion',
			$usuario->display_name, $usuario->user_email, get_bloginfo( 'name' ) );

		// FPDF escribe en ISO-8859-1. Un «Muñoz» o un «José» sin convertir sale
		// roto en las 259 páginas del pie, que es justo donde nadie relee.
		if ( function_exists( 'iconv' ) ) {
			$convertido = iconv( 'UTF-8', 'ISO-8859-1//TRANSLIT', $pie );
			if ( false !== $convertido ) {
				$pie = $convertido;
			}
		}

		try {
			$pdf = new \setasign\Fpdi\Fpdi();
			$n   = $pdf->setSourceFile( $origen );

			for ( $i = 1; $i <= $n; $i++ ) {
				$plantilla = $pdf->importPage( $i );
				$medidas   = $pdf->getTemplateSize( $plantilla );

				$pdf->AddPage( $medidas['orientation'], array( $medidas['width'], $medidas['height'] ) );
				$pdf->useTemplate( $plantilla );

				$pdf->SetFont( 'Helvetica', '', 6.5 );
				$pdf->SetTextColor( 130, 140, 160 );
				$pdf->SetXY( 8, $medidas['height'] - 7 );
				$pdf->Cell( $medidas['width'] - 16, 4, $pie, 0, 0, 'C' );
			}
			$pdf->Output( 'F', $destino );
			return is_readable( $destino ) ? $destino : $origen;

		} catch ( \Throwable $e ) {
			// Que el sellado falle nunca puede impedir una descarga pagada.
			error_log( '[TOAC] Sellado fallido de ' . $slug . ': ' . $e->getMessage() );
			return $origen;
		}
	}

	/* ---------------------------------------------------------------- *
	 *  Registro de descargas
	 * ---------------------------------------------------------------- */

	public function crea_tabla_si_falta() {
		if ( get_option( 'toac_version_tabla' ) === self::VERSION ) {
			return;
		}
		global $wpdb;
		require_once ABSPATH . 'wp-admin/includes/upgrade.php';

		$tabla   = $wpdb->prefix . 'toac_descargas';
		$cotejo  = $wpdb->get_charset_collate();

		dbDelta( "CREATE TABLE {$tabla} (
			id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
			user_id BIGINT UNSIGNED NOT NULL,
			producto_id BIGINT UNSIGNED NOT NULL,
			ip VARCHAR(45) NOT NULL DEFAULT '',
			agente VARCHAR(255) NOT NULL DEFAULT '',
			fecha DATETIME NOT NULL,
			PRIMARY KEY (id),
			KEY usuario_producto_fecha (user_id, producto_id, fecha)
		) {$cotejo};" );

		update_option( 'toac_version_tabla', self::VERSION );
	}

	private function anota_descarga( $usuario_id, $producto_id ) {
		global $wpdb;
		$wpdb->insert( $wpdb->prefix . 'toac_descargas', array(
			'user_id'     => $usuario_id,
			'producto_id' => $producto_id,
			'ip'          => substr( (string) ( $_SERVER['REMOTE_ADDR'] ?? '' ), 0, 45 ),
			'agente'      => substr( (string) ( $_SERVER['HTTP_USER_AGENT'] ?? '' ), 0, 255 ),
			'fecha'       => current_time( 'mysql' ),
		) );
	}

	private function descargas_de_hoy( $usuario_id, $producto_id ) {
		global $wpdb;
		return (int) $wpdb->get_var( $wpdb->prepare(
			"SELECT COUNT(*) FROM {$wpdb->prefix}toac_descargas
			 WHERE user_id = %d AND producto_id = %d AND fecha > %s",
			$usuario_id, $producto_id,
			// `fecha` se guarda con current_time('mysql'), que es hora local del
			// sitio. gmdate() sobre una marca local la formatea sin volver a
			// aplicarle el desfase, que es justo lo que hace falta para comparar
			// las dos en la misma escala.
			gmdate( 'Y-m-d H:i:s', current_time( 'timestamp' ) - DAY_IN_SECONDS )
		) );
	}

	/* ---------------------------------------------------------------- *
	 *  Escritorio: campos propios
	 * ---------------------------------------------------------------- */

	public function campos_en_escritorio() {
		echo '<div class="options_group">';
		foreach ( self::CAMPOS as $clave => $etiqueta ) {
			woocommerce_wp_text_input( array(
				'id'          => $clave,
				'label'       => $etiqueta,
				'desc_tip'    => true,
				'description' => 'Campo propio de TOAC.',
			) );
		}
		echo '</div>';
	}

	public function guarda_campos( $producto_id ) {
		// WooCommerce ya ha comprobado el nonce y la capacidad antes de este hook.
		foreach ( array_keys( self::CAMPOS ) as $clave ) {
			if ( ! isset( $_POST[ $clave ] ) ) {
				continue;
			}
			$valor = sanitize_text_field( wp_unslash( $_POST[ $clave ] ) );

			if ( '_toac_actualizado' === $clave && $valor
				&& ! preg_match( '/^\d{4}-\d{2}-\d{2}$/', $valor ) ) {
				continue; // Una fecha mal escrita es peor que no ponerla.
			}
			update_post_meta( $producto_id, $clave, $valor );
		}
	}

	/* ---------------------------------------------------------------- *
	 *  Escaparate
	 * ---------------------------------------------------------------- */

	public function sello_actualizado() {
		global $product;
		$fecha = get_post_meta( $product->get_id(), '_toac_actualizado', true );
		if ( ! $fecha ) {
			return;
		}
		$marca = strtotime( $fecha );
		$dias  = (int) floor( ( current_time( 'timestamp' ) - $marca ) / DAY_IN_SECONDS );

		printf(
			'<p class="toac-sello %s"><span class="toac-sello__punto"></span>Actualizado el %s</p>',
			$dias <= 60 ? 'toac-sello--fresco' : '',
			esc_html( date_i18n( 'j \d\e F \d\e Y', $marca ) )
		);
	}

	public function ficha_tecnica() {
		global $product;
		$id = $product->get_id();

		$filas = array(
			'Páginas'                  => get_post_meta( $id, '_toac_paginas', true ),
			'Temas'                    => get_post_meta( $id, '_toac_temas', true ),
			'Preguntas reales'         => get_post_meta( $id, '_toac_preguntas', true ),
			'Plazas de la convocatoria' => get_post_meta( $id, '_toac_puestos', true ),
		);
		$filas = array_filter( $filas );
		if ( ! $filas ) {
			return;
		}

		echo '<table class="toac-ficha"><tbody>';
		foreach ( $filas as $etiqueta => $valor ) {
			printf( '<tr><th>%s</th><td>%s</td></tr>', esc_html( $etiqueta ), esc_html( $valor ) );
		}
		echo '</tbody></table>';
		echo '<p class="toac-ficha__nota">Formato PDF. Las actualizaciones del temario '
			. 'están incluidas: al descargarlo siempre obtienes la última versión.</p>';
	}

	public function boton_muestra() {
		global $product;
		$slug = get_post_meta( $product->get_id(), '_toac_slug', true );
		if ( ! $slug || ! is_readable( trailingslashit( TOAC_DIR_MUESTRAS ) . 'muestra-' . $slug . '.pdf' ) ) {
			return;
		}
		printf(
			'<p><a class="button toac-boton-muestra" href="%s">Ver muestra: índice y primeras páginas</a></p>',
			esc_url( home_url( '/muestra/' . $slug . '/' ) )
		);
	}

	public function opcion_de_orden( $opciones ) {
		$opciones['toac_actualizado'] = 'Actualizados primero';
		return $opciones;
	}

	public function orden_por_actualizacion( $args ) {
		if ( isset( $_GET['orderby'] ) && 'toac_actualizado' === $_GET['orderby'] ) {
			$args['meta_key'] = '_toac_actualizado';
			$args['orderby']  = 'meta_value';   // AAAA-MM-DD ordena bien como texto.
			$args['order']    = 'DESC';
		}
		return $args;
	}

	/* ---------------------------------------------------------------- *
	 *  Panel de cliente: «Mis temarios»
	 * ---------------------------------------------------------------- */

	public function menu_mis_temarios( $items ) {
		// Primero lo que el cliente viene a buscar; el panel, después.
		$nuevo = array( 'mis-temarios' => 'Mis temarios' );
		return array_slice( $items, 0, 1, true ) + $nuevo + array_slice( $items, 1, null, true );
	}

	public function pinta_mis_temarios() {
		$usuario_id = get_current_user_id();

		if ( isset( $_GET['toac_aviso'] ) && 'caducado' === $_GET['toac_aviso'] ) {
			wc_print_notice( 'El enlace de descarga había caducado, por seguridad. '
				. 'Aquí tienes uno nuevo.', 'notice' );
		}

		$productos = $this->temarios_del_usuario( $usuario_id );

		if ( ! $productos ) {
			echo '<p>Todavía no tienes ningún temario. <a href="'
				. esc_url( wc_get_page_permalink( 'shop' ) ) . '">Ver el catálogo</a>.</p>';
			return;
		}

		echo '<table class="toac-mis-temarios shop_table"><thead><tr>'
			. '<th>Temario</th><th>Actualizado</th><th>Descargas hoy</th><th></th>'
			. '</tr></thead><tbody>';

		foreach ( $productos as $producto_id ) {
			$fecha = get_post_meta( $producto_id, '_toac_actualizado', true );
			$hoy   = $this->descargas_de_hoy( $usuario_id, $producto_id );

			echo '<tr><td>' . esc_html( get_the_title( $producto_id ) ) . '</td>';
			echo '<td>' . ( $fecha ? esc_html( date_i18n( 'j M Y', strtotime( $fecha ) ) ) : '—' ) . '</td>';
			echo '<td>' . esc_html( $hoy . ' / ' . self::LIMITE_DIARIO ) . '</td><td>';

			if ( $hoy >= self::LIMITE_DIARIO ) {
				echo '<span class="toac-limite">Límite diario alcanzado</span>';
			} else {
				printf( '<a class="button" href="%s">Descargar PDF</a>',
					esc_url( $this->enlace_de_descarga( $producto_id, $usuario_id ) ) );
			}
			echo '</td></tr>';
		}
		echo '</tbody></table>';
		echo '<p class="toac-aviso-licencia">Cada PDF se entrega con licencia personal e '
			. 'intransferible y va sellado con tus datos.</p>';
	}

	private function temarios_del_usuario( $usuario_id ) {
		$pedidos = wc_get_orders( array(
			'customer_id' => $usuario_id,
			'status'      => wc_get_is_paid_statuses(),
			'limit'       => -1,
		) );

		$ids = array();
		foreach ( $pedidos as $pedido ) {
			foreach ( $pedido->get_items() as $linea ) {
				$id = $linea->get_product_id();
				if ( $id && get_post_meta( $id, '_toac_slug', true ) ) {
					$ids[ $id ] = $id;
				}
			}
		}
		return array_values( $ids );
	}

	/* ---------------------------------------------------------------- */

	private function corta( $codigo, $mensaje ) {
		status_header( $codigo );
		wp_die( esc_html( $mensaje ), 'Acceso no permitido', array( 'response' => $codigo ) );
	}
}

add_action( 'plugins_loaded', array( 'TOAC_Tienda', 'arranca' ) );
