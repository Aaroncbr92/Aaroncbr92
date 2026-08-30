#!/usr/bin/env python3
"""Convierte el volumen HTML en PDF con el Chromium del entorno.

Chromium no aplica las reglas `@page` de numeración, así que la cabecera y el
pie se le pasan aparte, como plantillas suyas. Lo demás —saltos de página,
huérfanas y viudas, tablas que no se parten— sí sale del CSS del documento.

Uso:  pdf.py [entrada.html] [salida.pdf]
"""
import os
import sys

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PIE = """<div style="width:100%;font:8pt Helvetica,Arial,sans-serif;color:#777;
 padding:0 18mm;display:flex;justify-content:space-between;">
 <span>Temario general · Oposiciones RTVE · redacción a 21/12/2022</span>
 <span class="pageNumber"></span></div>"""
VACIO = "<div></div>"


def main():
    entrada = sys.argv[1] if len(sys.argv) > 1 else "libro-general.html"
    salida = sys.argv[2] if len(sys.argv) > 2 else "libro-general.pdf"
    ruta = os.path.join(RAIZ, entrada)
    destino = os.path.join(RAIZ, salida)

    with sync_playwright() as p:
        navegador = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pagina = navegador.new_page()
        pagina.goto("file://" + ruta, wait_until="load")
        pagina.pdf(path=destino, format="A4", print_background=True,
                   display_header_footer=True, header_template=VACIO, footer_template=PIE,
                   margin={"top": "16mm", "bottom": "18mm", "left": "18mm", "right": "18mm"})
        navegador.close()

    print("· %s · %.1f MB" % (salida, os.path.getsize(destino) / 1e6))


if __name__ == "__main__":
    main()
