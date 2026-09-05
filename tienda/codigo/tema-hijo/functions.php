<?php
/**
 * Tema hijo de Twenty Twenty-Five para TOAC.
 *
 * Instalación:
 *   wp-content/themes/toac/
 *     ├── style.css       (con la cabecera Template: twentytwentyfive)
 *     └── functions.php   (este fichero)
 */

defined( 'ABSPATH' ) || exit;

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'toac', get_stylesheet_uri(), array(), '1.0.0' );
} );

/** Cuatro por fila en el catálogo: veinticinco volúmenes caben en siete filas. */
add_filter( 'loop_shop_columns', fn() => 4 );
add_filter( 'loop_shop_per_page', fn() => 28, 20 );

/**
 * Fuera la ficha de «Valoraciones» mientras no haya reseñas reales.
 * Una pestaña vacía dice «aquí no ha comprado nadie».
 */
add_filter( 'woocommerce_product_tabs', function ( $pestanas ) {
	global $product;
	if ( $product && ! $product->get_review_count() ) {
		unset( $pestanas['reviews'] );
	}
	return $pestanas;
} );

/**
 * En un temario, «Añadir al carrito» no dice nada. «Comprar y descargar» sí.
 */
add_filter( 'woocommerce_product_single_add_to_cart_text', fn() => 'Comprar y descargar' );
add_filter( 'woocommerce_product_add_to_cart_text', function ( $texto, $producto = null ) {
	return get_post_meta( $producto ? $producto->get_id() : 0, '_toac_slug', true )
		? 'Ver temario' : $texto;
}, 10, 2 );

/**
 * Entrega inmediata: los pedidos que sólo llevan temarios pasan solos de
 * «procesando» a «completado». Sin esto, el cliente paga y espera a que
 * alguien mueva el pedido a mano.
 */
add_action( 'woocommerce_payment_complete', function ( $pedido_id ) {
	$pedido = wc_get_order( $pedido_id );
	if ( ! $pedido ) {
		return;
	}
	foreach ( $pedido->get_items() as $linea ) {
		if ( ! get_post_meta( $linea->get_product_id(), '_toac_slug', true ) ) {
			return; // Lleva algo que no es un temario: que lo revise una persona.
		}
	}
	$pedido->update_status( 'completed', 'Sólo temarios: entrega automática.' );
} );

/**
 * En el correo de compra, el enlace directo a «Mis temarios».
 * Es la primera pregunta que hace todo el mundo: «¿y ahora dónde lo bajo?».
 */
add_action( 'woocommerce_email_before_order_table', function ( $pedido, $admin ) {
	if ( $admin || ! $pedido->get_customer_id() ) {
		return;
	}
	printf(
		'<p style="padding:14px;background:#f2f5fa;border-radius:6px">'
		. 'Tu temario ya está disponible en <a href="%s"><strong>Mis temarios</strong></a>, '
		. 'dentro de tu cuenta. Las actualizaciones futuras del temario están incluidas: '
		. 'vuelve a descargarlo cuando quieras y obtendrás la última versión.</p>',
		esc_url( wc_get_account_endpoint_url( 'mis-temarios' ) )
	);
}, 10, 2 );

/**
 * Casilla obligatoria de renuncia al desistimiento.
 * Sin ella, un comprador puede descargar el temario y pedir la devolución
 * dentro de los catorce días. Ver tienda/04-PAGOS.md §4.5.
 */
add_action( 'woocommerce_review_order_before_submit', function () {
	woocommerce_form_field( 'toac_renuncia', array(
		'type'     => 'checkbox',
		'class'    => array( 'form-row', 'toac-renuncia' ),
		'label'    => 'Solicito la descarga inmediata y reconozco que, una vez descargado '
			. 'el temario, pierdo el derecho de desistimiento de catorce días.',
		'required' => true,
	), WC()->checkout->get_value( 'toac_renuncia' ) );
} );

add_action( 'woocommerce_checkout_process', function () {
	if ( empty( $_POST['toac_renuncia'] ) ) {
		wc_add_notice( 'Para completar la compra hay que aceptar la descarga inmediata.', 'error' );
	}
} );

/** Queda registrado en el pedido: es la prueba si algún día hay reclamación. */
add_action( 'woocommerce_checkout_update_order_meta', function ( $pedido_id ) {
	if ( ! empty( $_POST['toac_renuncia'] ) ) {
		update_post_meta( $pedido_id, '_toac_renuncia_desistimiento', current_time( 'mysql' ) );
	}
} );

/**
 * Descuento del pack: 15 % cuando el carrito lleva el temario general y al
 * menos un específico.
 *
 * Se hace con una comisión negativa y no con un producto «pack» aparte a
 * propósito: un pack como producto obligaría a que un producto entregase dos
 * ficheros, y eso rompe la regla de «un producto, un volumen» de la que vive
 * toda la entrega de descargas. Así el descuento es una regla del carrito y el
 * modelo de datos no se entera.
 */
add_action( 'woocommerce_cart_calculate_fees', function ( $carrito ) {
	if ( is_admin() && ! wp_doing_ajax() ) {
		return;
	}
	$general    = false;
	$especifico = false;
	$base       = 0.0;

	foreach ( $carrito->get_cart() as $linea ) {
		$slug = get_post_meta( $linea['product_id'], '_toac_slug', true );
		if ( ! $slug ) {
			continue;
		}
		$base += (float) $linea['line_subtotal'];
		if ( 'general' === $slug ) {
			$general = true;
		} else {
			$especifico = true;
		}
	}

	if ( $general && $especifico && $base > 0 ) {
		$carrito->add_fee( 'Descuento pack general + específico (15 %)', -1 * round( $base * 0.15, 2 ) );
	}
}, 20 );

/**
 * Y el aviso en la ficha del específico, que es donde sirve de algo:
 * decirlo en el carrito es tarde.
 */
add_action( 'woocommerce_single_product_summary', function () {
	global $product;
	$slug = get_post_meta( $product->get_id(), '_toac_slug', true );
	if ( ! $slug || 'general' === $slug ) {
		return;
	}
	$generales = wc_get_products( array(
		'limit'      => 1,
		'meta_key'   => '_toac_slug',
		'meta_value' => 'general',
	) );
	if ( ! $generales ) {
		return;
	}
	printf(
		'<p class="toac-pack">Con el <a href="%s">temario general</a>, el pack sale un <strong>15 %% más barato</strong>. '
		. 'Los dos bloques entran en el examen.</p>',
		esc_url( get_permalink( $generales[0]->get_id() ) )
	);
}, 23 );
