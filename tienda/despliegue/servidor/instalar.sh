#!/usr/bin/env bash
#
# Se ejecuta EN EL SERVIDOR de Hostinger. No se llama a mano: lo lanza
# `desplegar.sh` por SSH.
#
#   instalar.sh <ruta_wp> <ruta_privada> <dominio> <correo_admin>
#
# Idempotente: cada paso comprueba antes de actuar. Se puede repetir.

set -euo pipefail

RUTA_WP="${1:?falta la ruta de WordPress}"
RUTA_PRIVADA="${2:?falta la ruta privada}"
DOMINIO="${3:?falta el dominio}"
CORREO="${4:?falta el correo del administrador}"

verde() { printf '  \033[32m✓\033[0m %s\n' "$*"; }
aviso() { printf '  \033[33m!\033[0m %s\n' "$*"; }
gris()  { printf '    \033[90m%s\033[0m\n' "$*"; }

cd "${RUTA_WP}"

# --- WP-CLI ------------------------------------------------------------------
# Hostinger suele traerlo. Si no está, se baja al vuelo y se usa desde /tmp.

if command -v wp >/dev/null 2>&1; then
	WP="wp"
elif [[ -x /tmp/wp-cli.phar ]]; then
	WP="php /tmp/wp-cli.phar"
else
	curl -sS -o /tmp/wp-cli.phar \
		https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
	chmod +x /tmp/wp-cli.phar
	WP="php /tmp/wp-cli.phar"
fi
$WP --info >/dev/null || { echo "WP-CLI no arranca"; exit 1; }
verde "WP-CLI: $($WP cli version 2>/dev/null | head -1)"

ADMIN=$($WP user list --role=administrator --field=ID --number=1 2>/dev/null | head -1)
[[ -n "${ADMIN}" ]] || { echo "No encuentro ningún administrador"; exit 1; }

# --- 1 · wp-config.php --------------------------------------------------------

echo
echo "1 · wp-config.php"

# Copia antes de tocar. Es un fichero que si se rompe deja la web muerta.
if [[ ! -f wp-config.php.antes-de-toac ]]; then
	cp wp-config.php wp-config.php.antes-de-toac
	verde "copia de seguridad en wp-config.php.antes-de-toac"
fi

constante() {  # nombre valor [--raw]
	local nombre="$1" valor="$2"; shift 2
	if $WP config has "${nombre}" --type=constant 2>/dev/null; then
		gris "${nombre} ya estaba, se respeta"
	else
		$WP config set "${nombre}" "${valor}" --type=constant "$@" >/dev/null
		verde "${nombre}"
	fi
}

constante TOAC_DIR_LIBROS   "${RUTA_PRIVADA}/libros"
constante TOAC_DIR_MUESTRAS "${RUTA_PRIVADA}/muestras"
constante TOAC_DIR_SELLADOS "${RUTA_PRIVADA}/sellados"
constante TOAC_ENVIO        "auto"

# La clave de firma se genera aquí y no se escribe en ningún otro sitio.
# Cambiarla invalida todos los enlaces emitidos: es el botón de emergencia.
if ! $WP config has TOAC_CLAVE_FIRMA --type=constant 2>/dev/null; then
	CLAVE=$(openssl rand -hex 32 2>/dev/null || head -c32 /dev/urandom | od -An -tx1 | tr -d ' \n')
	$WP config set TOAC_CLAVE_FIRMA "${CLAVE}" --type=constant >/dev/null
	verde "TOAC_CLAVE_FIRMA generada (64 hex, no se muestra)"
fi

# El sellado se deja APAGADO: necesita FPDI, y FPDI libre no lee PDF 1.7,
# que es lo que escribe pdf.py. Ver tienda/03-PDFS.md §3.5.
constante TOAC_SELLAR false --raw

constante DISALLOW_FILE_EDIT true  --raw
constante FORCE_SSL_ADMIN    true  --raw
constante WP_DEBUG_DISPLAY   false --raw
constante WP_POST_REVISIONS  5     --raw

# Marcadores de posición: se rellenan cuando Google dé las credenciales.
constante TOAC_GOOGLE_ID      ""
constante TOAC_GOOGLE_SECRETO ""

# --- 2 · Ajustes de WordPress -------------------------------------------------

echo
echo "2 · Ajustes de WordPress"

$WP option update home    "https://${DOMINIO}" >/dev/null
$WP option update siteurl "https://${DOMINIO}" >/dev/null
$WP option update admin_email "${CORREO}"      >/dev/null
$WP option update blogdescription "Temarios verificados para las oposiciones de RTVE" >/dev/null
$WP option update timezone_string "Europe/Madrid" >/dev/null
$WP option update default_comment_status closed   >/dev/null
$WP option update users_can_register 1            >/dev/null
$WP option update default_role customer           >/dev/null 2>&1 || true
$WP rewrite structure '/%postname%/' --hard >/dev/null
verde "URL, zona horaria, enlaces permanentes y registro abierto"

# --- 3 · WooCommerce ----------------------------------------------------------

echo
echo "3 · WooCommerce"

if ! $WP plugin is-installed woocommerce 2>/dev/null; then
	$WP plugin install woocommerce --activate >/dev/null
	verde "WooCommerce instalado y activado"
else
	$WP plugin activate woocommerce >/dev/null 2>&1 || true
	verde "WooCommerce ya estaba (v$($WP plugin get woocommerce --field=version))"
fi

# Las páginas de la tienda (Tienda, Carrito, Pago, Mi cuenta).
$WP wc tool run install_pages --user="${ADMIN}" >/dev/null 2>&1 \
	&& verde "páginas de la tienda creadas" \
	|| aviso "no he podido crear las páginas de la tienda; revísalo en WooCommerce → Estado → Herramientas"

ajuste() { $WP option update "$1" "$2" >/dev/null; }

ajuste woocommerce_default_country               "ES"
ajuste woocommerce_currency                      "EUR"
ajuste woocommerce_price_thousand_sep            "."
ajuste woocommerce_price_decimal_sep             ","
ajuste woocommerce_currency_pos                  "right_space"

# Sin cuenta no hay panel privado, y sin panel privado no hay entrega.
ajuste woocommerce_enable_guest_checkout                  "no"
ajuste woocommerce_enable_signup_and_login_from_checkout  "yes"
ajuste woocommerce_enable_checkout_login_reminder         "yes"
ajuste woocommerce_enable_myaccount_registration          "yes"

# Cinturón: aunque las descargas las sirve el plugin propio, si algún día un
# producto se marca descargable por descuido, que no salga sin sesión.
ajuste woocommerce_downloads_require_login  "yes"
ajuste woocommerce_file_download_method     "force"

# Aquí no se envía nada.
ajuste woocommerce_ship_to_countries        "disabled"
ajuste woocommerce_calc_shipping            "no"

# Impuestos: el público español espera ver el precio final.
ajuste woocommerce_calc_taxes           "yes"
ajuste woocommerce_prices_include_tax   "yes"
ajuste woocommerce_tax_based_on         "billing"
verde "moneda, cuentas obligatorias, sin envíos, precios con impuestos"

# --- 4 · Tema hijo ------------------------------------------------------------

echo
echo "4 · Tema"

if ! $WP theme is-installed twentytwentyfive 2>/dev/null; then
	$WP theme install twentytwentyfive >/dev/null
fi
if [[ -f wp-content/themes/toac/style.css ]]; then
	$WP theme activate toac >/dev/null && verde "tema hijo TOAC activado"
else
	aviso "no encuentro el tema hijo en wp-content/themes/toac"
fi

# --- 5 · PDF.js ---------------------------------------------------------------

echo
echo "5 · Visor de muestras (PDF.js)"

DESTINO="wp-content/uploads/pdfjs"
if [[ -f "${DESTINO}/web/viewer.html" ]]; then
	verde "PDF.js ya estaba"
else
	# Se resuelve la última versión publicada en vez de fijar una a mano: un
	# número escrito hoy deja de existir en cuanto Mozilla retira la release.
	URL=$(curl -sS https://api.github.com/repos/mozilla/pdf.js/releases/latest \
		| grep -o 'https://[^"]*-dist\.zip' | head -1 || true)
	if [[ -n "${URL}" ]] && curl -sSL -o /tmp/pdfjs.zip "${URL}"; then
		mkdir -p "${DESTINO}"
		unzip -oq /tmp/pdfjs.zip -d "${DESTINO}"
		rm -f /tmp/pdfjs.zip
		verde "PDF.js instalado desde ${URL##*/}"
	else
		aviso "no he podido bajar PDF.js. Bájalo a mano de github.com/mozilla/pdf.js/releases"
		aviso "y descomprímelo en ${RUTA_WP}/${DESTINO}"
	fi
fi

# El recorte de la barra: fuera descargar, imprimir y abrir en otra pestaña.
if [[ -f "${DESTINO}/web/viewer.css" ]] && ! grep -q "TOAC" "${DESTINO}/web/viewer.css"; then
	{
		echo ""
		echo "/* --- TOAC: recorte de la barra del visor --- */"
		echo "#download,#secondaryDownload,#print,#secondaryPrint,#openFile,"
		echo "#secondaryOpenFile,#viewBookmark,#secondaryViewBookmark,"
		echo "#documentProperties{display:none !important}"
	} >> "${DESTINO}/web/viewer.css"
	verde "barra del visor recortada"
fi

# --- 6 · Caché ----------------------------------------------------------------

echo
echo "6 · Caché"

if ! $WP plugin is-installed litespeed-cache 2>/dev/null; then
	$WP plugin install litespeed-cache --activate >/dev/null && verde "LiteSpeed Cache instalado"
else
	verde "LiteSpeed Cache ya estaba"
fi

# La protección de verdad la hace toac-blindaje.php en tiempo de ejecución:
# llama a `litespeed_control_set_nocache` en cuenta, carrito, pago, descarga y
# muestra. Esto de aquí es sólo el cinturón, y hay que verificarlo a ojo.
$WP litespeed-option set cache-exc "/carrito
/finalizar-compra
/mi-cuenta
/descarga
/muestra" >/dev/null 2>&1 \
	&& verde "exclusiones de caché puestas" \
	|| aviso "no he podido poner las exclusiones de caché por línea de comandos.
    Ponlas a mano: LiteSpeed Cache → Caché → Excluir → carrito, finalizar-compra,
    mi-cuenta, descarga y muestra. (El plugin propio ya lo fuerza en ejecución,
    así que esto es redundancia, no la única defensa.)"

# --- 7 · Páginas legales ------------------------------------------------------

echo
echo "7 · Páginas legales (esqueleto, sin tus datos)"

crea_pagina() {  # slug titulo contenido
	if $WP post list --post_type=page --field=post_name 2>/dev/null | grep -qx "$1"; then
		gris "«$2» ya existía"
		return
	fi
	$WP post create --post_type=page --post_status=publish \
		--post_name="$1" --post_title="$2" --post_content="$3" >/dev/null
	verde "«$2»"
}

PENDIENTE='<p><strong>PENDIENTE DE COMPLETAR.</strong> Esta página necesita tus datos identificativos antes de abrir la tienda. Lo que tiene que decir está en <code>tienda/05-LANZAMIENTO.md</code>, apartado 5.1.</p>'

crea_pagina "aviso-legal"        "Aviso legal"              "${PENDIENTE}<p>Titular, NIF, domicilio y correo de contacto.</p>"
crea_pagina "privacidad"         "Política de privacidad"   "${PENDIENTE}<p>Responsable, datos tratados, base jurídica, plazos y cesionarios: Stripe, Google y el proveedor de correo. Y el registro de descargas.</p>"
crea_pagina "cookies"            "Política de cookies"      "${PENDIENTE}"
crea_pagina "condiciones-venta"  "Condiciones de venta"     "${PENDIENTE}<p>Incluye la renuncia expresa al desistimiento del artículo 103.m) del Real Decreto Legislativo 1/2007.</p>"
crea_pagina "contacto"           "Contacto"                 "${PENDIENTE}"

# --- 8 · El catálogo ----------------------------------------------------------

echo
echo "8 · Catálogo"

if [[ -f /tmp/toac-productos.csv && -f /tmp/toac-importar.php ]]; then
	$WP eval-file /tmp/toac-importar.php /tmp/toac-productos.csv
else
	aviso "no encuentro el CSV del catálogo en /tmp"
fi

# --- 9 · Cierre ---------------------------------------------------------------

echo
echo "9 · Cierre"

$WP rewrite flush --hard >/dev/null
$WP cache flush >/dev/null 2>&1 || true
$WP transient delete --all >/dev/null 2>&1 || true
verde "enlaces permanentes y cachés al día"

rm -f /tmp/toac-productos.csv /tmp/toac-importar.php /tmp/toac-instalar.sh
