#!/usr/bin/env bash
#
# Monta la tienda entera en Hostinger. Se ejecuta EN TU MÁQUINA, desde la raíz
# del repositorio, con el `config.sh` de al lado ya rellenado.
#
#   bash tienda/despliegue/desplegar.sh --simulacro   # enseña lo que haría
#   bash tienda/despliegue/desplegar.sh               # lo hace
#
# Es idempotente: se puede volver a pasar las veces que haga falta. No borra
# nada, no pisa un producto que ya exista y hace copia de `wp-config.php`
# antes de tocarlo.
#
# Lo que NO hace, porque no lo puede hacer ningún script:
#   · activar tu cuenta de Stripe (te pide identidad e IBAN);
#   · crear el proyecto de OAuth en Google Cloud (va contra tu cuenta);
#   · comprar el dominio ni el certificado;
#   · redactar el aviso legal con tu NIF.
# Esos cuatro quedan listados al final, con lo que hay que hacer en cada uno.

set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "${AQUI}/../.." && pwd)"
SIMULACRO=0
[[ "${1:-}" == "--simulacro" ]] && SIMULACRO=1

# shellcheck source=config.sh
source "${AQUI}/config.sh"

# --- Presentación ------------------------------------------------------------

rojo()  { printf '\033[31m%s\033[0m\n' "$*"; }
verde() { printf '\033[32m%s\033[0m\n' "$*"; }
gris()  { printf '\033[90m%s\033[0m\n' "$*"; }
paso()  { printf '\n\033[1m▸ %s\033[0m\n' "$*"; }

morir() { rojo "✗ $*"; exit 1; }

SSH="ssh -p ${SSH_PUERTO} ${SSH_USER}@${SSH_HOST}"

remoto() {
	if (( SIMULACRO )); then gris "    [remoto] $*"; return 0; fi
	# shellcheck disable=SC2086
	$SSH "$@"
}

# Varios orígenes y un destino, como scp: el ÚLTIMO argumento es el destino.
# (La primera versión tomaba $1 y $2 a secas, y con un comodín de tres ficheros
#  se comía el destino y copiaba un plugin encima de otro. Lo cazó el simulacro.)
subir() {
	local destino="${!#}"
	local origenes=( "${@:1:$#-1}" )
	if (( SIMULACRO )); then
		local o
		for o in "${origenes[@]}"; do gris "    [subir]  ${o} → ${destino}"; done
		return 0
	fi
	scp -q -P "${SSH_PUERTO}" -r "${origenes[@]}" "${SSH_USER}@${SSH_HOST}:${destino}"
}

# --- 0 · Comprobaciones antes de tocar nada ----------------------------------

paso "0 · Comprobaciones previas"

[[ "${SSH_USER}" == "uXXXXXXX" ]] && morir "Rellena tienda/despliegue/config.sh primero."
[[ -f "${RAIZ}/libro-general.pdf" ]] || morir "Ejecuta esto desde la raíz del repositorio."

command -v python3 >/dev/null || morir "Hace falta python3 para generar muestras y catálogo."

# Las tres librerías que usan muestra.py y catalogo.py. Se comprueban aquí y no
# a mitad del despliegue, cuando ya se han subido 55 MB por la red.
FALTAN=$(python3 -c 'import importlib.util as u; print(" ".join(q for m,q in (("pypdf","pypdf"),("reportlab","reportlab"),("markdown_it","markdown-it-py")) if u.find_spec(m) is None))' 2>/dev/null)
if [[ -n "${FALTAN// /}" ]]; then
	morir "Faltan librerías de Python. Instálalas con:

     python3 -m pip install ${FALTAN}"
fi
verde "  ✓ python3, con pypdf, reportlab y markdown-it-py"

for orden in ssh scp; do
	if ! command -v "${orden}" >/dev/null; then
		(( SIMULACRO )) && gris "  (falta ${orden}; en simulacro da igual)" \
		                || morir "Hace falta ${orden}."
	fi
done

if (( ! SIMULACRO )); then
	$SSH "true" 2>/dev/null || morir "No conecto por SSH. Comprueba host, usuario y puerto en config.sh,
   y que tu clave pública esté dada de alta en hPanel → Avanzado → Acceso SSH."
	verde "  ✓ SSH conecta"

	remoto "test -d '${RUTA_WP}/wp-admin'" \
		|| morir "No veo WordPress en ${RUTA_WP}. Instálalo desde el hPanel (fase 2) y vuelve."
	verde "  ✓ WordPress está en ${RUTA_WP}"
else
	gris "  (simulacro: no se conecta a nada)"
fi

# --- 1 · Generar muestras y catálogo, aquí -----------------------------------

paso "1 · Muestras y catálogo (en tu máquina)"

if (( SIMULACRO )); then
	gris "    python3 herramientas/muestra.py --paginas ${PAGINAS_MUESTRA} --url ${DOMINIO}"
	gris "    python3 herramientas/catalogo.py --url ${DOMINIO}"
else
	python3 "${RAIZ}/herramientas/muestra.py"  --paginas "${PAGINAS_MUESTRA}" --url "${DOMINIO}" | tail -2
	python3 "${RAIZ}/herramientas/catalogo.py" --url "${DOMINIO}"                                | tail -2
	verde "  ✓ 25 muestras y el catálogo, al día"
fi

# --- 2 · Carpetas privadas ---------------------------------------------------

paso "2 · Carpetas fuera de public_html"

remoto "mkdir -p '${RUTA_PRIVADA}/libros' '${RUTA_PRIVADA}/muestras' '${RUTA_PRIVADA}/sellados' \
        && chmod 750 '${RUTA_PRIVADA}' '${RUTA_PRIVADA}'/*"
subir "${AQUI}/../codigo/servidor/temarios-privados.htaccess" "${RUTA_PRIVADA}/.htaccess"
verde "  ✓ ${RUTA_PRIVADA}"

# --- 3 · Los ficheros --------------------------------------------------------

paso "3 · Subiendo los volúmenes y las muestras (unos 55 MB la primera vez)"

if command -v rsync >/dev/null && (( ! SIMULACRO )); then
	rsync -az --info=progress2 -e "ssh -p ${SSH_PUERTO}" \
		"${RAIZ}"/libro-*.pdf "${SSH_USER}@${SSH_HOST}:${RUTA_PRIVADA}/libros/"
	rsync -az -e "ssh -p ${SSH_PUERTO}" \
		"${RAIZ}"/muestras/muestra-*.pdf "${SSH_USER}@${SSH_HOST}:${RUTA_PRIVADA}/muestras/"
else
	subir "${RAIZ}"/libro-*.pdf            "${RUTA_PRIVADA}/libros/"
	subir "${RAIZ}"/muestras/muestra-*.pdf "${RUTA_PRIVADA}/muestras/"
fi
verde "  ✓ 25 volúmenes y 25 muestras"

# --- 4 · Código --------------------------------------------------------------

paso "4 · Plugins propios, tema hijo y .htaccess"

remoto "mkdir -p '${RUTA_WP}/wp-content/mu-plugins' '${RUTA_WP}/wp-content/themes/toac'"
subir "${AQUI}/../codigo/mu-plugins/"*.php        "${RUTA_WP}/wp-content/mu-plugins/"
subir "${AQUI}/../codigo/tema-hijo/"*             "${RUTA_WP}/wp-content/themes/toac/"
subir "${AQUI}/../codigo/servidor/uploads.htaccess" "${RUTA_WP}/wp-content/uploads/.htaccess"
subir "${AQUI}/../catalogo/productos.csv"         "/tmp/toac-productos.csv"
subir "${AQUI}/servidor/instalar.sh"              "/tmp/toac-instalar.sh"
subir "${AQUI}/servidor/importar-catalogo.php"    "/tmp/toac-importar.php"
verde "  ✓ código en su sitio"

# --- 5 · El instalador, en el servidor ---------------------------------------

paso "5 · Configurando WordPress y WooCommerce (esto tarda unos minutos)"

if (( SIMULACRO )); then
	gris "    [remoto] bash /tmp/toac-instalar.sh '${RUTA_WP}' '${RUTA_PRIVADA}' '${DOMINIO}' '${CORREO_ADMIN}'"
else
	# shellcheck disable=SC2029
	$SSH "bash /tmp/toac-instalar.sh '${RUTA_WP}' '${RUTA_PRIVADA}' '${DOMINIO}' '${CORREO_ADMIN}'"
fi

# --- 6 · Comprobar ------------------------------------------------------------

paso "6 · Comprobaciones"

if (( SIMULACRO )); then
	gris "    bash ${AQUI}/comprobar.sh"
else
	bash "${AQUI}/comprobar.sh" || rojo "  ↑ Alguna comprobación no pasa. Míralas antes de abrir."
fi

# --- 7 · Lo que queda, y es tuyo ---------------------------------------------

cat <<FIN

$(printf '\033[1m')Hecho lo que se puede hacer solo. Queda esto, que no puede hacer un script:$(printf '\033[0m')

  1. STRIPE — https://dashboard.stripe.com
     Activa la cuenta (te pedirá NIF e IBAN: es verificación de identidad).
     Luego, en tu web: Plugins → WooCommerce Stripe Gateway → Conectar.
     Webhook a  https://${DOMINIO}/?wc-api=wc_stripe
     con los eventos de tienda/04-PAGOS.md §4.2, y pega el secreto whsec_…
     Empieza en MODO DE PRUEBAS y pasa las cuatro tarjetas de esa misma sección.

  2. GOOGLE — https://console.cloud.google.com
     Proyecto nuevo → Pantalla de consentimiento (necesita los enlaces a tu
     aviso legal y a tu privacidad, que ya están creados) → Credenciales →
     ID de cliente de OAuth → Aplicación web.
       Origen:      https://${DOMINIO}
       Redirección: https://${DOMINIO}/?toac_google=callback
     Y luego, en el servidor:
       ssh -p ${SSH_PUERTO} ${SSH_USER}@${SSH_HOST}
       cd ${RUTA_WP} && wp config set TOAC_GOOGLE_ID 'tu-id' --type=constant
       cd ${RUTA_WP} && wp config set TOAC_GOOGLE_SECRETO 'tu-secreto' --type=constant

  3. TEXTOS LEGALES
     Las cinco páginas están creadas con su esqueleto, pero VACÍAS de tus datos.
     Rellena NIF, domicilio y correo. Lista de qué tiene que decir cada una en
     tienda/05-LANZAMIENTO.md §5.1.

  4. LOGOTIPO
     marca/toac.svg sigue pendiente. La cabecera y las muestras lo necesitan.

Cuando estén los cuatro, la lista de diecisiete comprobaciones previas a abrir
está en tienda/05-LANZAMIENTO.md §5.3.
FIN
