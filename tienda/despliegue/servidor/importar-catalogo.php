<?php
/**
 * Importa tienda/catalogo/productos.csv en WooCommerce.
 *
 * Se ejecuta con:  wp eval-file importar-catalogo.php <ruta-del-csv>
 *
 * Por qué no se usa el importador CSV de WooCommerce: es de interfaz, no de
 * línea de comandos, y su mapeo de columnas «Meta:» cambia entre versiones.
 * Aquí se crea el producto con la API de WooCommerce, que es estable.
 *
 * Idempotente y conservador: si ya existe un producto con ese SKU, actualiza
 * los datos que salen de los volúmenes —páginas, temas, preguntas, fecha— y
 * NO toca el precio ni la descripción, que a esas alturas ya las habrás
 * retocado a mano y sería muy desagradable perderlas.
 */

defined( 'ABSPATH' ) || exit;

$ruta = $args[0] ?? '';
if ( ! $ruta || ! is_readable( $ruta ) ) {
	WP_CLI::error( 'No encuentro el CSV: ' . $ruta );
}
if ( ! class_exists( 'WC_Product_Simple' ) ) {
	WP_CLI::error( 'WooCommerce no está activo.' );
}

$mano = fopen( $ruta, 'r' );
$cabecera = fgetcsv( $mano );
if ( ! $cabecera ) {
	WP_CLI::error( 'El CSV está vacío.' );
}

$nuevos = 0;
$actualizados = 0;
$intactos = 0;

while ( ( $fila = fgetcsv( $mano ) ) !== false ) {
	if ( count( $fila ) !== count( $cabecera ) ) {
		WP_CLI::warning( 'Fila con un número de columnas raro, la salto.' );
		continue;
	}
	$d = array_combine( $cabecera, $fila );

	$sku  = $d['SKU'];
	$slug = $d['Meta:_toac_slug'];

	// Los metadatos que salen de los volúmenes se refrescan siempre: son la
	// razón de ser de catalogo.py.
	$meta = array(
		'_toac_slug'        => $slug,
		'_toac_actualizado' => $d['Meta:_toac_actualizado'],
		'_toac_paginas'     => $d['Meta:_toac_paginas'],
		'_toac_temas'       => $d['Meta:_toac_temas'],
		'_toac_preguntas'   => $d['Meta:_toac_preguntas'],
		'_toac_puestos'     => $d['Meta:_toac_puestos'],
	);

	$id = wc_get_product_id_by_sku( $sku );

	if ( $id ) {
		$producto = wc_get_product( $id );
		$antes = array_map(
			static fn( $k ) => (string) get_post_meta( $id, $k, true ),
			array_keys( $meta )
		);

		foreach ( $meta as $clave => $valor ) {
			$producto->update_meta_data( $clave, $valor );
		}
		$producto->save();

		if ( $antes === array_values( array_map( 'strval', $meta ) ) ) {
			$intactos++;
		} else {
			$actualizados++;
			WP_CLI::log( sprintf( '  actualizado  %-24s %s pp · actualizado el %s',
				$slug, $meta['_toac_paginas'], $meta['_toac_actualizado'] ) );
		}
		continue;
	}

	// Producto nuevo.
	$producto = new WC_Product_Simple();
	$producto->set_name( $d['Name'] );
	$producto->set_sku( $sku );
	$producto->set_status( 'publish' );
	$producto->set_catalog_visibility( 'visible' );
	$producto->set_short_description( $d['Short description'] );
	$producto->set_description( $d['Description'] );
	$producto->set_regular_price( $d['Regular price'] );
	$producto->set_tax_status( 'taxable' );
	$producto->set_manage_stock( false );
	$producto->set_stock_status( 'instock' );

	// Virtual sí; descargable NO. La descarga la sirve toac-tienda.php contra
	// el pedido pagado, no WooCommerce. Ver tienda/01-ARQUITECTURA.md §1.4.
	$producto->set_virtual( true );
	$producto->set_downloadable( false );

	$categoria = get_term_by( 'name', $d['Categories'], 'product_cat' );
	if ( ! $categoria ) {
		$creada = wp_insert_term( $d['Categories'], 'product_cat' );
		if ( ! is_wp_error( $creada ) ) {
			$producto->set_category_ids( array( $creada['term_id'] ) );
		}
	} else {
		$producto->set_category_ids( array( $categoria->term_id ) );
	}

	foreach ( $meta as $clave => $valor ) {
		$producto->update_meta_data( $clave, $valor );
	}
	$producto->save();

	$nuevos++;
	WP_CLI::log( sprintf( '  creado       %-24s %6s € · %s pp',
		$slug, $d['Regular price'], $meta['_toac_paginas'] ) );
}
fclose( $mano );

WP_CLI::success( sprintf(
	'%d productos nuevos, %d actualizados, %d sin cambios. '
	. 'Los precios y las descripciones de los que ya existían no se han tocado.',
	$nuevos, $actualizados, $intactos ) );
