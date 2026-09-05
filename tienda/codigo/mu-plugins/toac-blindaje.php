<?php
/**
 * Plugin Name: TOAC · Blindaje del área privada
 * Description: Cierra el panel de cliente y la superficie que WordPress deja abierta por defecto.
 * Version:     1.0.0
 * License:     GPL-2.0-or-later
 */

defined( 'ABSPATH' ) || exit;

final class TOAC_Blindaje {

	public static function arranca() {
		$yo = new self();

		add_action( 'template_redirect',   array( $yo, 'nada_de_cache_en_lo_privado' ), 0 );
		add_action( 'template_redirect',   array( $yo, 'panel_solo_con_sesion' ) );
		add_action( 'admin_init',          array( $yo, 'clientes_fuera_del_escritorio' ) );
		add_filter( 'show_admin_bar',      array( $yo, 'sin_barra_para_clientes' ) );
		add_filter( 'rest_endpoints',      array( $yo, 'sin_listado_de_usuarios' ) );
		add_action( 'template_redirect',   array( $yo, 'sin_enumeracion_por_autor' ) );
		add_filter( 'xmlrpc_enabled',      '__return_false' );
		add_filter( 'wp_headers',          array( $yo, 'cabeceras' ) );
		add_action( 'wp_login_failed',     array( $yo, 'frena_fuerza_bruta' ) );
		add_filter( 'authenticate',        array( $yo, 'comprueba_freno' ), 30, 3 );
		add_filter( 'login_errors',        array( $yo, 'error_generico' ) );
	}

	/** Lo privado no se cachea. Es el fallo que sirve la sesión de uno a otro. */
	public function nada_de_cache_en_lo_privado() {
		if ( ! function_exists( 'is_account_page' ) ) {
			return;
		}
		$privado = is_account_page() || is_cart() || is_checkout()
			|| get_query_var( 'toac_descarga' ) || get_query_var( 'toac_muestra_pdf' );

		if ( $privado ) {
			if ( ! defined( 'DONOTCACHEPAGE' ) ) {
				define( 'DONOTCACHEPAGE', true );
			}
			nocache_headers();
			// LiteSpeed Cache atiende a esta acción además de a sus exclusiones.
			do_action( 'litespeed_control_set_nocache', 'zona privada TOAC' );
		}
	}

	/** El panel de cliente, ni siquiera un instante, sin sesión iniciada. */
	public function panel_solo_con_sesion() {
		if ( ! function_exists( 'is_account_page' ) || ! is_account_page() ) {
			return;
		}
		if ( is_user_logged_in() ) {
			return;
		}
		// La portada de «Mi cuenta» es el formulario de acceso: esa sí pasa.
		// Cualquier subpágina (pedidos, mis temarios, direcciones), no.
		//
		// Se pregunta a WooCommerce por el endpoint actual en vez de mirar la
		// URL: el slug de la página de cuenta lo elige quien instala, y
		// comparar contra «mi-cuenta» a mano deja de funcionar en cuanto
		// alguien la llama de otra forma.
		$endpoint = ( WC()->query ) ? WC()->query->get_current_endpoint() : '';
		if ( $endpoint ) {
			wp_safe_redirect( wc_get_page_permalink( 'myaccount' ) );
			exit;
		}
	}

	/** Un cliente no tiene nada que hacer en wp-admin. */
	public function clientes_fuera_del_escritorio() {
		if ( wp_doing_ajax() || wp_doing_cron() || ! function_exists( 'wc_get_page_permalink' ) ) {
			return;
		}
		if ( current_user_can( 'edit_posts' ) || current_user_can( 'manage_woocommerce' ) ) {
			return;
		}
		wp_safe_redirect( wc_get_page_permalink( 'myaccount' ) );
		exit;
	}

	public function sin_barra_para_clientes( $mostrar ) {
		return current_user_can( 'edit_posts' ) ? $mostrar : false;
	}

	/** La API REST publica la lista de usuarios; aquí no. */
	public function sin_listado_de_usuarios( $rutas ) {
		if ( is_user_logged_in() && current_user_can( 'list_users' ) ) {
			return $rutas;
		}
		unset( $rutas['/wp/v2/users'], $rutas['/wp/v2/users/(?P<id>[\d]+)'] );
		return $rutas;
	}

	/** /?author=1 revela el nombre de acceso del administrador. */
	public function sin_enumeracion_por_autor() {
		if ( ! is_admin() && isset( $_GET['author'] ) ) {
			wp_safe_redirect( home_url(), 301 );
			exit;
		}
	}

	public function cabeceras( $cabeceras ) {
		$cabeceras['X-Content-Type-Options'] = 'nosniff';
		$cabeceras['X-Frame-Options']        = 'SAMEORIGIN';
		$cabeceras['Referrer-Policy']        = 'strict-origin-when-cross-origin';
		$cabeceras['Permissions-Policy']     = 'geolocation=(), microphone=(), camera=(), interest-cohort=()';
		return $cabeceras;
	}

	/* --- Freno a la fuerza bruta ------------------------------------- *
	 *  No sustituye a un cortafuegos: es el mínimo para que un intento
	 *  automatizado no salga gratis mientras Cloudflare hace lo suyo.
	 * ---------------------------------------------------------------- */

	private function llave() {
		return 'toac_freno_' . md5( (string) ( $_SERVER['REMOTE_ADDR'] ?? '' ) );
	}

	public function frena_fuerza_bruta() {
		$intentos = (int) get_transient( $this->llave() );
		set_transient( $this->llave(), $intentos + 1, 15 * MINUTE_IN_SECONDS );
	}

	public function comprueba_freno( $usuario, $acceso, $clave ) {
		if ( (int) get_transient( $this->llave() ) >= 6 ) {
			return new WP_Error( 'toac_freno',
				'Demasiados intentos fallidos. Espera quince minutos o entra con Google.' );
		}
		return $usuario;
	}

	/** «Contraseña incorrecta» confirma que ese usuario existe. */
	public function error_generico( $error ) {
		return 'Los datos no son correctos.';
	}
}

add_action( 'plugins_loaded', array( 'TOAC_Blindaje', 'arranca' ) );
