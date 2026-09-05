#!/usr/bin/env bash
# Los seis datos que hay que rellenar antes de desplegar. Nada más.
#
# Dónde encontrarlos, en el hPanel de Hostinger:
#   SSH_HOST, SSH_USER, SSH_PUERTO  →  Avanzado → Acceso SSH
#   RUTA_WP                         →  suele ser /home/<SSH_USER>/public_html
#   DOMINIO                         →  el que apunta a esa carpeta, sin https://
#   CORREO_ADMIN                    →  una dirección que leas de verdad

SSH_HOST="temarios.example"
SSH_USER="uXXXXXXX"
SSH_PUERTO="65002"

DOMINIO="temarios.example"
RUTA_WP="/home/uXXXXXXX/public_html"
CORREO_ADMIN="tu-correo@ejemplo.com"

# --- De aquí para abajo no suele hacer falta tocar nada ----------------------

# Dónde viven los PDF. FUERA de RUTA_WP: es la línea de la que depende que
# ninguna URL llegue a un fichero.
RUTA_PRIVADA="/home/${SSH_USER}/temarios_privados"

# Precio del pack: descuento que aplica el tema hijo. Informativo aquí.
# Los precios de cada volumen se cambian en herramientas/catalogo.py.

# Páginas de cuerpo que enseña cada muestra, además de portada e índice.
PAGINAS_MUESTRA=12
