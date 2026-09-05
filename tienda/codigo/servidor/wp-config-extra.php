<?php
/**
 * Añadido a wp-config.php.
 *
 * Va ENCIMA de la línea:  require_once ABSPATH . 'wp-settings.php';
 * Debajo de ella no se ejecuta a tiempo y las constantes llegan vacías.
 *
 * Sustituye uXXXXXXX por tu usuario de Hostinger (whoami por SSH).
 */

/* --- Dónde viven los PDF -------------------------------------------- *
 *  FUERA de public_html. Es la línea que hace que ninguna URL llegue a
 *  un fichero: no hay ruta bajo el dominio que lleve hasta aquí.
 * ------------------------------------------------------------------- */
define( 'TOAC_DIR_LIBROS',   '/home/uXXXXXXX/temarios_privados/libros' );
define( 'TOAC_DIR_MUESTRAS', '/home/uXXXXXXX/temarios_privados/muestras' );
define( 'TOAC_DIR_SELLADOS', '/home/uXXXXXXX/temarios_privados/sellados' );

/* --- Firma de los enlaces ------------------------------------------- *
 *  Genera una nueva con:  openssl rand -hex 32
 *  Si cambias esta clave, los enlaces ya emitidos dejan de valer al
 *  instante. Es la forma de cortar en seco una filtración.
 * ------------------------------------------------------------------- */
define( 'TOAC_CLAVE_FIRMA', 'PEGA-AQUI-64-CARACTERES-HEXADECIMALES' );

/* --- Cómo se entrega el fichero ------------------------------------- *
 *  'auto' detecta LiteSpeed, que es lo que corre en Hostinger.
 *  Valores: auto | litespeed | xsendfile | accel | php
 * ------------------------------------------------------------------- */
define( 'TOAC_ENVIO', 'auto' );

/* --- Sellado nominativo del PDF -------------------------------------- *
 *  Requiere FPDI y FPDF (ver tienda/03-PDFS.md §3.5).
 *  Si la biblioteca no está, se sirve el original sin sellar: una
 *  descarga pagada nunca falla por esto.
 * ------------------------------------------------------------------- */
define( 'TOAC_SELLAR', true );

/* --- Acceso con Google ----------------------------------------------- *
 *  De Google Cloud Console → Credenciales → ID de cliente de OAuth.
 * ------------------------------------------------------------------- */
define( 'TOAC_GOOGLE_ID',      'XXXXXXXXXXXX.apps.googleusercontent.com' );
define( 'TOAC_GOOGLE_SECRETO', 'GOCSPX-XXXXXXXXXXXXXXXXXXXX' );

/* --- Endurecimiento del propio WordPress ----------------------------- */
define( 'DISALLOW_FILE_EDIT',   true );  // Sin editor de temas: un administrador comprometido no escribe PHP.
define( 'DISALLOW_FILE_MODS',   false ); // Déjalo en false para poder actualizar desde el escritorio.
define( 'FORCE_SSL_ADMIN',      true );
define( 'WP_AUTO_UPDATE_CORE',  'minor' );
define( 'WP_DEBUG',             false );
define( 'WP_DEBUG_DISPLAY',     false ); // Un aviso de PHP en pantalla filtra rutas del servidor.
define( 'WP_DEBUG_LOG',         '/home/uXXXXXXX/logs/wp-errors.log' );
define( 'EMPTY_TRASH_DAYS',     14 );
define( 'WP_POST_REVISIONS',    5 );
