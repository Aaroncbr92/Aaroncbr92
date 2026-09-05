#!/usr/bin/env bash
#
# Deja lista la conexión con Hostinger. Se ejecuta EN TU ORDENADOR, una sola
# vez, antes del primer despliegue.
#
#   bash tienda/despliegue/preparar-ssh.sh
#
# Lo que hace:
#   1. Busca una clave SSH tuya. Si no tienes, la crea.
#   2. Te enseña la clave PÚBLICA para que la pegues en el hPanel.
#   3. Prueba la conexión y te dice qué falla si falla.
#
# LA CLAVE PRIVADA NO SALE DE TU ORDENADOR. Nunca. Ni aquí ni en el despliegue.
# Lo único que se copia a ningún sitio es la pública, que para eso es pública.

set -uo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=config.sh
source "${AQUI}/config.sh"

verde() { printf '  \033[32m✓\033[0m %s\n' "$*"; }
aviso() { printf '  \033[33m!\033[0m %s\n' "$*"; }
rojo()  { printf '  \033[31m✗\033[0m %s\n' "$*"; }
paso()  { printf '\n\033[1m▸ %s\033[0m\n' "$*"; }

if [[ "${SSH_USER}" == "uXXXXXXX" ]]; then
	rojo "Rellena antes tienda/despliegue/config.sh."
	echo "     Los datos están en hPanel → Avanzado → Acceso SSH."
	exit 1
fi

# --- 1 · La clave ------------------------------------------------------------

paso "1 · Tu clave SSH"

CLAVE=""
for candidata in ~/.ssh/id_ed25519 ~/.ssh/id_rsa; do
	if [[ -f "${candidata}" ]]; then CLAVE="${candidata}"; break; fi
done

if [[ -z "${CLAVE}" ]]; then
	aviso "no tienes ninguna clave. La creo ahora."
	echo "     (Te va a pedir una contraseña para la clave: puedes dejarla vacía"
	echo "      pulsando Intro dos veces, o poner una y usar el agente ssh.)"
	echo
	ssh-keygen -t ed25519 -C "${CORREO_ADMIN}" -f ~/.ssh/id_ed25519
	CLAVE=~/.ssh/id_ed25519
	verde "clave creada en ${CLAVE}"
else
	verde "ya tienes una: ${CLAVE}"
fi

# --- 2 · Darla de alta en Hostinger ------------------------------------------

paso "2 · Pégala en el hPanel"

cat <<FIN

  Ve a:  hPanel → Avanzado → Acceso SSH → Claves SSH → Añadir nueva

  Y pega EXACTAMENTE esto (es la clave PÚBLICA; se puede enseñar sin riesgo,
  para eso está: sólo sirve para reconocerte, no para suplantarte):

FIN
printf '\033[36m'
cat "${CLAVE}.pub"
printf '\033[0m\n'
cat <<FIN
  Lo que NO se enseña nunca es ${CLAVE} (sin el .pub). Esa se queda aquí.

FIN

read -r -p "  ¿Ya la has pegado en el hPanel? [Intro para seguir] " _

# --- 3 · Probar ---------------------------------------------------------------

paso "3 · Probando la conexión"

SALIDA=$(ssh -p "${SSH_PUERTO}" -o BatchMode=yes -o ConnectTimeout=15 \
	"${SSH_USER}@${SSH_HOST}" "echo CONECTA; pwd; ls -d ${RUTA_WP}/wp-admin 2>/dev/null" 2>&1)

if grep -q CONECTA <<<"${SALIDA}"; then
	verde "SSH conecta"

	if grep -q "wp-admin" <<<"${SALIDA}"; then
		verde "WordPress está en ${RUTA_WP}"
		echo
		printf '\033[32m  Todo listo. El siguiente paso es:\033[0m\n\n'
		echo "    bash tienda/despliegue/desplegar.sh --simulacro"
		echo "    bash tienda/despliegue/desplegar.sh"
		exit 0
	fi

	rojo "conecta, pero no veo WordPress en ${RUTA_WP}"
	echo "     Mira cuál es la ruta buena con:"
	echo "       ssh -p ${SSH_PUERTO} ${SSH_USER}@${SSH_HOST} 'ls ~'"
	echo "     y corrige RUTA_WP en config.sh. Si aún no has instalado"
	echo "     WordPress, hazlo desde el hPanel (fase 2 de ../02-IMPLANTACION.md)."
	exit 1
fi

rojo "no conecta"
echo
echo "  Lo que ha contestado el servidor:"
sed 's/^/     /' <<<"${SALIDA}"
echo
echo "  Lo que suele ser:"
echo "   · La clave aún no está dada de alta, o tarda un par de minutos en valer."
echo "   · El puerto no es el 22. El tuyo sale en hPanel → Avanzado → Acceso SSH"
echo "     (ahora mismo config.sh dice ${SSH_PUERTO})."
echo "   · El acceso SSH está desactivado en el hPanel. Actívalo ahí."
echo "   · El host no es el dominio sino una IP. También sale en esa pantalla."
echo
echo "  Corrige config.sh y vuelve a pasar este mismo script."
exit 1
