#!/usr/bin/env bash
#
# Comprueba desde fuera, como lo haría un desconocido, que la tienda está bien
# cerrada. Se ejecuta EN TU MÁQUINA y no necesita SSH.
#
#   bash tienda/despliegue/comprobar.sh
#
# Lo lanza `desplegar.sh` al terminar, pero conviene volver a pasarlo cada vez
# que se toque un plugin, la caché o el .htaccess.

set -uo pipefail   # sin -e: aquí queremos ver TODAS las que fallan, no la primera

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=config.sh
source "${AQUI}/config.sh"

BASE="https://${DOMINIO}"
OK=0; MAL=0

# --- utilidades --------------------------------------------------------------

codigo() { curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$1"; }
tipo()   { curl -s -o /dev/null -w '%{content_type}' --max-time 20 "$1"; }
cuerpo() { curl -sL --max-time 20 "$1"; }

bien() { printf '  \033[32m✓\033[0m %s\n' "$1"; OK=$((OK+1)); }
mal()  { printf '  \033[31m✗\033[0m %s\n' "$1"; printf '      %s\n' "$2"; MAL=$((MAL+1)); }

# Espera uno de varios códigos.
espera() {  # descripción url códigos-separados-por-espacio
	local desc="$1" url="$2" esperados="$3"
	local c; c=$(codigo "${url}")
	if [[ " ${esperados} " == *" ${c} "* ]]; then bien "${desc}"
	else mal "${desc}" "devuelve ${c}, se esperaba uno de: ${esperados} — ${url}"; fi
}

# --- 1 · Que nadie llegue a un fichero ---------------------------------------
# Es el grupo que, si falla, obliga a parar. Todo lo demás es secundario.

printf '\n\033[1mLos ficheros\033[0m\n'

for ruta in \
	"/temarios_privados/libros/libro-sonido.pdf" \
	"/temarios_privados/muestras/muestra-sonido.pdf" \
	"/temarios_privados/" \
	"/wp-content/uploads/libro-sonido.pdf" \
	"/wp-content/uploads/woocommerce_uploads/libro-sonido.pdf" \
	"/libro-sonido.pdf"
do
	espera "sin acceso a ${ruta}" "${BASE}${ruta}" "403 404"
done

# Y el más importante de todos: que no salga un PDF por ahí.
t=$(tipo "${BASE}/temarios_privados/libros/libro-sonido.pdf")
if [[ "${t}" == *pdf* ]]; then
	mal "el volumen completo NO debe servirse" "está saliendo como ${t}. PARA Y ARRÉGLALO."
else
	bien "ninguna de esas rutas devuelve un PDF"
fi

# --- 2 · La descarga, sin sesión ---------------------------------------------

printf '\n\033[1mLa descarga\033[0m\n'

espera "/descarga/sonido sin sesión no entrega"      "${BASE}/descarga/sonido/"          "301 302 403"
espera "/descarga/sonido con token inventado, 403"   "${BASE}/descarga/sonido/?t=xxx.yy" "301 302 403"
espera "/muestra-pdf/sonido sin token, 403"          "${BASE}/muestra-pdf/sonido/"       "403"

t=$(tipo "${BASE}/descarga/sonido/")
if [[ "${t}" == *pdf* ]]; then
	mal "descarga abierta sin sesión" "devuelve ${t}. PARA Y ARRÉGLALO."
else
	bien "la descarga sin sesión no devuelve un PDF"
fi

# --- 3 · La tienda ------------------------------------------------------------

printf '\n\033[1mLa tienda\033[0m\n'

espera "portada"                "${BASE}/"                  "200"
espera "catálogo"               "${BASE}/tienda/"           "200"
espera "mi cuenta"              "${BASE}/mi-cuenta/"        "200"
espera "visor de la muestra"    "${BASE}/muestra/sonido/"   "200"

if cuerpo "${BASE}/muestra/sonido/" | grep -q "muestra-pdf/sonido"; then
	bien "el visor apunta a la muestra con su token"
else
	mal "el visor no carga la muestra" "revisa que PDF.js esté en wp-content/uploads/pdfjs/"
fi

if cuerpo "${BASE}/tienda/" | grep -qi "Actualizado el"; then
	bien "el catálogo enseña la fecha de actualización"
else
	mal "no veo la fecha de actualización en el catálogo" \
	    "¿está activo el tema hijo y rellenado _toac_actualizado?"
fi

for p in aviso-legal privacidad cookies condiciones-venta contacto; do
	espera "página /${p}" "${BASE}/${p}/" "200"
done

# --- 4 · Superficie cerrada ---------------------------------------------------

printf '\n\033[1mLo que debe estar cerrado\033[0m\n'

espera "xmlrpc desactivado"           "${BASE}/xmlrpc.php"               "403 404 405"
espera "listado de usuarios por REST" "${BASE}/wp-json/wp/v2/users"      "401 403 404"
espera "sin índice de mu-plugins"     "${BASE}/wp-content/mu-plugins/"   "403 404"
espera "sin índice de uploads"        "${BASE}/wp-content/uploads/"      "403 404"

c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "${BASE}/?author=1")
if [[ "${c}" == 30* ]]; then bien "enumeración de autores redirigida"
else mal "enumeración de autores" "devuelve ${c}, se esperaba una redirección"; fi

if curl -sI --max-time 20 "${BASE}/" | grep -qi "x-content-type-options"; then
	bien "cabeceras de seguridad presentes"
else
	mal "faltan cabeceras de seguridad" "¿está toac-blindaje.php en mu-plugins?"
fi

espera "http redirige a https" "http://${DOMINIO}/" "301 302 307 308"

# --- Resumen ------------------------------------------------------------------

printf '\n'
if (( MAL == 0 )); then
	printf '\033[32m%d comprobaciones, todas pasan.\033[0m\n' "${OK}"
	exit 0
fi
printf '\033[31m%d de %d comprobaciones fallan.\033[0m\n' "${MAL}" "$((OK+MAL))"
printf 'Las del apartado «Los ficheros» y «La descarga» son las que obligan a parar.\n'
exit 1
