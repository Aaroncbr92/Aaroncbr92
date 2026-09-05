<?php
/**
 * Plugin Name: TOAC · Entrar con Google
 * Description: Inicio de sesión y alta con cuenta de Google (OAuth 2.0 + PKCE) sin depender de plugins de terceros.
 * Version:     1.0.0
 * License:     GPL-2.0-or-later
 *
 * Constantes necesarias en wp-config.php:
 *   TOAC_GOOGLE_ID       ID de cliente de OAuth
 *   TOAC_GOOGLE_SECRETO   Secreto de cliente
 *
 * URI de redirección a registrar en Google Cloud Console:
 *   https://TU-DOMINIO/?toac_google=callback
 */

defined( 'ABSPATH' ) || exit;

final class TOAC_Google_SSO {

	const AUTORIZAR = 'https://accounts.google.com/o/oauth2/v2/auth';
	const TOKEN     = 'https://oauth2.googleapis.com/token';
	const EMISORES  = array( 'accounts.google.com', 'https://accounts.google.com' );

	public static function arranca() {
		if ( ! defined( 'TOAC_GOOGLE_ID' ) || ! TOAC_GOOGLE_ID ) {
			return; // Sin credenciales el plugin no pinta nada y no estorba.
		}
		$yo = new self();

		add_action( 'init', array( $yo, 'atiende' ) );

		// El botón, en los tres sitios donde alguien puede querer entrar.
		add_action( 'woocommerce_login_form_start',    array( $yo, 'boton' ) );
		add_action( 'woocommerce_register_form_start', array( $yo, 'boton' ) );
		add_action( 'login_form',                      array( $yo, 'boton' ) );
		add_action( 'login_enqueue_scripts',           array( $yo, 'estilo_en_wp_login' ) );
	}

	private function url_de_retorno() {
		return home_url( '/?toac_google=callback' );
	}

	/* ---------------------------------------------------------------- *
	 *  El botón
	 * ---------------------------------------------------------------- */

	public function boton() {
		// El destino tras entrar: de dónde venía, o su panel.
		$destino = isset( $_GET['redirect_to'] )
			? esc_url_raw( wp_unslash( $_GET['redirect_to'] ) )
			: ( function_exists( 'wc_get_page_permalink' ) ? wc_get_page_permalink( 'myaccount' ) : home_url() );

		$url = wp_nonce_url(
			add_query_arg( array(
				'toac_google' => 'start',
				'destino'     => rawurlencode( $destino ),
			), home_url( '/' ) ),
			'toac_google_start'
		);
		?>
		<div class="toac-google">
			<a class="toac-google__boton" href="<?php echo esc_url( $url ); ?>" rel="nofollow">
				<svg width="18" height="18" viewBox="0 0 48 48" aria-hidden="true" focusable="false">
					<path fill="#4285F4" d="M45.1 24.5c0-1.6-.1-3.2-.4-4.7H24v8.9h11.8c-.5 2.8-2 5.1-4.4 6.7v5.5h7.1c4.2-3.8 6.6-9.5 6.6-16.4z"/>
					<path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.2 15.5 46 24 46z"/>
					<path fill="#FBBC05" d="M11.8 28.3c-.4-1.3-.7-2.7-.7-4.3s.3-2.9.7-4.3v-5.7H4.5A22 22 0 0 0 2 24c0 3.6.9 6.9 2.5 9.9l7.3-5.6z"/>
					<path fill="#EA4335" d="M24 10.7c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.1 29.9 2 24 2 15.5 2 8.1 6.8 4.5 14.1l7.3 5.7c1.7-5.2 6.5-9.1 12.2-9.1z"/>
				</svg>
				<span>Continuar con Google</span>
			</a>
			<p class="toac-google__nota">Es la forma recomendada: sin contraseña que recordar.</p>
		</div>
		<?php
	}

	public function estilo_en_wp_login() {
		echo '<style>.toac-google__boton{display:flex;gap:.6rem;align-items:center;justify-content:center;'
			. 'padding:.7rem 1rem;border:1px solid #dadce0;border-radius:6px;background:#fff;color:#3c4043;'
			. 'font-weight:600;text-decoration:none;margin-bottom:1rem}'
			. '.toac-google__nota{font-size:.8rem;color:#5f6368;text-align:center;margin:0 0 1rem}</style>';
	}

	/* ---------------------------------------------------------------- *
	 *  El ciclo
	 * ---------------------------------------------------------------- */

	public function atiende() {
		$paso = isset( $_GET['toac_google'] ) ? sanitize_key( wp_unslash( $_GET['toac_google'] ) ) : '';

		if ( 'start' === $paso ) {
			$this->empieza();
		} elseif ( 'callback' === $paso ) {
			$this->vuelve();
		}
	}

	/**
	 * Manda al usuario a Google.
	 *
	 * Dos protecciones, y las dos hacen falta:
	 *  - «state» ata la vuelta a esta petición concreta: sin él, cualquiera
	 *    puede provocar que inicies sesión en la cuenta que él elija (CSRF de
	 *    inicio de sesión).
	 *  - PKCE ata el canje del código al navegador que lo pidió: aunque el
	 *    código se filtre por el historial o por un «Referer», no sirve.
	 */
	private function empieza() {
		if ( ! isset( $_GET['_wpnonce'] ) || ! wp_verify_nonce( wp_unslash( $_GET['_wpnonce'] ), 'toac_google_start' ) ) {
			wp_die( 'Petición caducada. Vuelve a la página de acceso e inténtalo otra vez.' );
		}

		$state    = bin2hex( random_bytes( 16 ) );
		$verifier = rtrim( strtr( base64_encode( random_bytes( 48 ) ), '+/', '-_' ), '=' );
		$reto     = rtrim( strtr( base64_encode( hash( 'sha256', $verifier, true ) ), '+/', '-_' ), '=' );

		$destino = isset( $_GET['destino'] ) ? rawurldecode( wp_unslash( $_GET['destino'] ) ) : '';

		set_transient( 'toac_g_' . $state, array(
			'verifier' => $verifier,
			'destino'  => $destino,
		), 10 * MINUTE_IN_SECONDS );

		$url = add_query_arg( array(
			'client_id'             => rawurlencode( TOAC_GOOGLE_ID ),
			'redirect_uri'          => rawurlencode( $this->url_de_retorno() ),
			'response_type'         => 'code',
			'scope'                 => rawurlencode( 'openid email profile' ),
			'state'                 => $state,
			'code_challenge'        => $reto,
			'code_challenge_method' => 'S256',
			'prompt'                => 'select_account',
			'access_type'           => 'online', // No queremos refresh token: no vamos a actuar en su nombre.
		), self::AUTORIZAR );

		wp_redirect( $url );   // Destino externo: wp_safe_redirect lo bloquearía.
		exit;
	}

	private function panel() {
		return function_exists( 'wc_get_page_permalink' )
			? wc_get_page_permalink( 'myaccount' )
			: admin_url( 'profile.php' );
	}

	private function vuelve() {
		if ( is_user_logged_in() ) {
			wp_safe_redirect( $this->panel() );
			exit;
		}

		// El usuario ha cancelado en la pantalla de Google: no es un error.
		if ( isset( $_GET['error'] ) ) {
			$this->falla( 'No se ha completado el acceso con Google.' );
		}

		$state  = isset( $_GET['state'] ) ? sanitize_text_field( wp_unslash( $_GET['state'] ) ) : '';
		$codigo = isset( $_GET['code'] )  ? sanitize_text_field( wp_unslash( $_GET['code'] ) )  : '';

		$guardado = $state ? get_transient( 'toac_g_' . $state ) : false;
		if ( ! $guardado || ! $codigo ) {
			$this->falla( 'La sesión de acceso ha caducado. Inténtalo de nuevo.' );
		}
		delete_transient( 'toac_g_' . $state ); // De un solo uso, siempre.

		$datos = $this->canjea( $codigo, $guardado['verifier'] );
		if ( is_wp_error( $datos ) ) {
			error_log( '[TOAC SSO] ' . $datos->get_error_message() );
			$this->falla( 'No hemos podido verificar tu cuenta de Google. Prueba otra vez en unos minutos.' );
		}

		$usuario_id = $this->usuario_para( $datos );
		if ( is_wp_error( $usuario_id ) ) {
			$this->falla( $usuario_id->get_error_message() );
		}

		wp_set_current_user( $usuario_id );
		wp_set_auth_cookie( $usuario_id, true );
		do_action( 'wp_login', get_userdata( $usuario_id )->user_login, get_userdata( $usuario_id ) );

		$destino = $guardado['destino'] ?: $this->panel();
		wp_safe_redirect( $destino );   // safe: sólo admite destinos de este dominio.
		exit;
	}

	/**
	 * Canjea el código por el id_token y devuelve sus datos ya validados.
	 *
	 * No se verifica la firma del id_token, y es correcto no hacerlo: el token
	 * llega en la respuesta directa del extremo de Google sobre TLS, no por el
	 * navegador. Es la excepción que contempla el propio OpenID Connect Core
	 * (§3.1.3.7, nota). Si algún día el token llegase por el canal frontal,
	 * habría que verificar la firma contra el JWKS de Google.
	 */
	private function canjea( $codigo, $verifier ) {
		$respuesta = wp_remote_post( self::TOKEN, array(
			'timeout' => 15,
			'body'    => array(
				'code'          => $codigo,
				'client_id'     => TOAC_GOOGLE_ID,
				'client_secret' => TOAC_GOOGLE_SECRETO,
				'redirect_uri'  => $this->url_de_retorno(),
				'grant_type'    => 'authorization_code',
				'code_verifier' => $verifier,
			),
		) );

		if ( is_wp_error( $respuesta ) ) {
			return $respuesta;
		}
		if ( 200 !== wp_remote_retrieve_response_code( $respuesta ) ) {
			return new WP_Error( 'toac_token', 'Google respondió ' . wp_remote_retrieve_response_code( $respuesta )
				. ': ' . wp_remote_retrieve_body( $respuesta ) );
		}

		$cuerpo = json_decode( wp_remote_retrieve_body( $respuesta ), true );
		if ( empty( $cuerpo['id_token'] ) ) {
			return new WP_Error( 'toac_token', 'Respuesta sin id_token.' );
		}

		$partes = explode( '.', $cuerpo['id_token'] );
		if ( 3 !== count( $partes ) ) {
			return new WP_Error( 'toac_token', 'id_token con formato inesperado.' );
		}
		$carga = json_decode( base64_decode( strtr( $partes[1], '-_', '+/' ) ), true );
		if ( ! is_array( $carga ) ) {
			return new WP_Error( 'toac_token', 'id_token ilegible.' );
		}

		// Las tres comprobaciones que sí siguen siendo obligatorias.
		if ( ! in_array( $carga['iss'] ?? '', self::EMISORES, true ) ) {
			return new WP_Error( 'toac_token', 'Emisor inesperado.' );
		}
		if ( ( $carga['aud'] ?? '' ) !== TOAC_GOOGLE_ID ) {
			return new WP_Error( 'toac_token', 'El token es para otra aplicación.' );
		}
		if ( ( (int) ( $carga['exp'] ?? 0 ) ) < time() ) {
			return new WP_Error( 'toac_token', 'Token caducado.' );
		}
		return $carga;
	}

	/**
	 * Encuentra, enlaza o crea el usuario de WordPress.
	 */
	private function usuario_para( $g ) {
		$sub    = $g['sub'] ?? '';
		$correo = sanitize_email( $g['email'] ?? '' );

		if ( ! $sub || ! $correo ) {
			return new WP_Error( 'toac_sso', 'Google no ha devuelto un correo utilizable.' );
		}
		// Sin correo verificado no se enlaza nada: es la puerta por la que se
		// entraría en la cuenta de otro.
		if ( empty( $g['email_verified'] ) ) {
			return new WP_Error( 'toac_sso', 'Tu correo de Google no está verificado. '
				. 'Verifícalo en tu cuenta de Google y vuelve a intentarlo.' );
		}

		// 1. Ya enlazado: el camino normal a partir de la segunda vez.
		$enlazados = get_users( array(
			'meta_key'   => 'toac_google_sub',
			'meta_value' => $sub,
			'number'     => 1,
			'fields'     => 'ID',
		) );
		if ( $enlazados ) {
			return (int) $enlazados[0];
		}

		// 2. Existe una cuenta con ese correo: se enlaza.
		$existente = get_user_by( 'email', $correo );
		if ( $existente ) {
			// Excepción deliberada: una cuenta con permisos de administración no
			// se enlaza sola. Si algún día el correo cambiara de manos, esto
			// evita que el enlace automático regale el escritorio.
			if ( user_can( $existente, 'manage_options' ) ) {
				return new WP_Error( 'toac_sso', 'Esa cuenta tiene permisos de administración: '
					. 'entra con usuario y contraseña y enlaza Google desde tu perfil.' );
			}
			update_user_meta( $existente->ID, 'toac_google_sub', $sub );
			return (int) $existente->ID;
		}

		// 3. Cuenta nueva.
		$base   = sanitize_user( current( explode( '@', $correo ) ), true );
		$acceso = $base;
		$n      = 1;
		while ( username_exists( $acceso ) ) {
			$acceso = $base . ++$n;
		}

		$id = wp_insert_user( array(
			'user_login'   => $acceso,
			'user_email'   => $correo,
			'user_pass'    => wp_generate_password( 32, true, true ),
			'display_name' => sanitize_text_field( $g['name'] ?? $acceso ),
			'first_name'   => sanitize_text_field( $g['given_name'] ?? '' ),
			'last_name'    => sanitize_text_field( $g['family_name'] ?? '' ),
			'role'         => 'customer',
		) );
		if ( is_wp_error( $id ) ) {
			return $id;
		}

		update_user_meta( $id, 'toac_google_sub', $sub );
		update_user_meta( $id, 'toac_alta_por', 'google' );

		return (int) $id;
	}

	private function falla( $mensaje ) {
		if ( function_exists( 'wc_add_notice' ) ) {
			wc_add_notice( $mensaje, 'error' );
			wp_safe_redirect( $this->panel() );
			exit;
		}
		wp_die( esc_html( $mensaje ) );
	}
}

add_action( 'plugins_loaded', array( 'TOAC_Google_SSO', 'arranca' ) );
