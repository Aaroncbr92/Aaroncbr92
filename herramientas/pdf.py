#!/usr/bin/env python3
"""Convierte el volumen HTML en PDF, con encabezado, pie e índice paginado.

El motor que compone el PDF **no sabe contar páginas desde el documento**: no hay
manera de escribir en el índice «este epígrafe está en la página 47» antes de
componerlo. Así que se compone dos veces:

1. **Primera pasada.** Sale un PDF cuyo índice ya lleva los enlaces, pero con el
   hueco de la página vacío.
2. **Se mira ese PDF** y se apunta en qué página ha caído cada enlace, leyendo
   los destinos que el propio PDF guarda.
3. **Segunda pasada**, con los números ya escritos en el índice. Como el índice
   crece al llenarse, puede desplazar lo que viene detrás, así que se repite
   hasta que los números **dejan de moverse**. Suelen bastar dos vueltas.

Al PDF terminado se le añaden el **encabezado y el pie** —dibujados encima,
salvo en la portada— y los **marcadores** del panel de navegación del lector.

Uso:  pdf.py [entrada.html] [salida.pdf]
"""
import io
import os
import re
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from pypdf.generic import Fit
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENCABEZADO = "TOAC – Temarios de Oposiciones"
PIE_DERECHA = "Oposiciones RTVE – Temario General"
TINTA = HexColor("#5a6b86")
A4 = (595.28, 841.89)
VUELTAS = 4


def compon(navegador, html, destino):
    pagina = navegador.new_page()
    pagina.goto("file://" + html, wait_until="load")
    pagina.pdf(path=destino, format="A4", print_background=True,
               margin={"top": "18mm", "bottom": "20mm", "left": "18mm", "right": "18mm"})
    pagina.close()


def paginas_de_anclas(pdf):
    """{ancla: nº de página}, leído del propio PDF.

    Chromium guarda cada ancla del documento como un **destino con nombre**, y
    ese nombre es el del ancla. Así que no hay que adivinar nada: se pregunta al
    PDF en qué página está cada destino. Eso sí, hay que preguntárselo **al PDF
    tal como sale de Chromium**: al reescribirlo para dibujarle el pie, la tabla
    de destinos se pierde si no se clona el documento entero.
    """
    lector = PdfReader(pdf)
    fuera = {}
    for nombre, destino in lector.named_destinations.items():
        try:
            # las claves llegan con la barra del nombre PDF delante: «/tema-1»
            fuera[nombre.lstrip("/")] = lector.get_page_number(destino.page) + 1
        except Exception:
            pass
    return fuera


def numera_indice(html, paginas):
    """Escribe el número de página en cada hueco del índice."""
    def pon(m):
        ancla = m.group(1)
        return '<span class="ip" data-ref="%s">%s</span>' % (ancla, paginas.get(ancla, ""))
    return re.sub(r'<span class="ip" data-ref="([^"]+)">[^<]*</span>', pon, html)


def adorna(entrada, portada_limpia=True):
    """Dibuja encabezado y pie encima de cada página, menos en la portada.

    Se clona el documento entero en vez de ir añadiendo páginas sueltas: así se
    conservan los **destinos y los enlaces**, que es lo que hace que el índice
    se pueda pinchar. Y el adorno se dibuja en **una sola capa** de tantas
    páginas como el volumen, no en una por página: hacerlo página a página
    multiplicaba los recursos y engordaba el fichero de 2 a 17 MB.
    """
    escritor = PdfWriter(clone_from=entrada)
    total = len(escritor.pages)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    for n in range(1, total + 1):
        if not (portada_limpia and n == 1):
            c.setFillColor(TINTA)
            c.setFont("Times-Roman", 9)
            c.drawRightString(A4[0] - 51, A4[1] - 38, ENCABEZADO)
            c.setFont("Times-Roman", 8.5)
            c.drawString(51, 34, "Página %d de %d" % (n, total))
            c.drawRightString(A4[0] - 51, 34, PIE_DERECHA)
        c.showPage()
    c.save()
    buf.seek(0)

    capa = PdfReader(buf)
    for n, pagina in enumerate(escritor.pages):
        pagina.merge_page(capa.pages[n])
        # fusionar deja el contenido de la página sin comprimir, y son 250
        # páginas: sin esto el volumen pasa de 2 a 17 MB
        pagina.compress_content_streams()
    return escritor


def marcadores(escritor, indice):
    """El árbol de navegación del lector, con los temas y sus epígrafes."""
    padres = {}
    for nivel, numero, titulo, pagina in indice:
        if pagina is None or pagina > len(escritor.pages):
            continue
        padre = padres.get(nivel - 1) if nivel else None
        m = escritor.add_outline_item("%s %s" % (numero, titulo),
                                      pagina - 1, parent=padre, fit=Fit.fit_horizontally())
        padres[nivel] = m
        for k in list(padres):
            if k > nivel:
                del padres[k]


def indice_del_html(html):
    return [(int(m.group(1)), m.group(2), m.group(3),
             re.sub(r"<[^>]+>", "", m.group(4)).strip())
            for m in re.finditer(
                r'<div class="ii n(\d)"><a href="#([^"]+)"><span class="it">'
                r'(\S+) ([^<]*)</span>', html)]


def main():
    entrada = sys.argv[1] if len(sys.argv) > 1 else "libro-general.html"
    salida = sys.argv[2] if len(sys.argv) > 2 else "libro-general.pdf"
    fuente = open(os.path.join(RAIZ, entrada), encoding="utf-8").read()
    anclas = re.findall(r'<div class="ii n\d"><a href="#([^"]+)"', fuente)
    trabajo = os.path.join(RAIZ, entrada[:-5] + "-paginado.html")
    crudo = os.path.join(RAIZ, salida[:-4] + "-crudo.pdf")
    destino = os.path.join(RAIZ, salida)

    with sync_playwright() as p:
        navegador = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        html, previas, vueltas = fuente, None, 0
        while vueltas < VUELTAS:
            vueltas += 1
            open(trabajo, "w", encoding="utf-8").write(html)
            compon(navegador, trabajo, crudo)
            paginas = paginas_de_anclas(crudo)
            if paginas == previas:
                break
            previas = paginas
            html = numera_indice(fuente, paginas)
        navegador.close()

    escritor = adorna(crudo)
    marcadores(escritor, [(nivel, num, tit, paginas.get(anc))
                          for nivel, anc, num, tit in indice_del_html(html)])
    paginas_totales = len(escritor.pages)
    # clonar el documento duplica objetos idénticos; sin esto el fichero engorda
    # de 2 a 17 MB solo por dibujarle el pie
    escritor.compress_identical_objects()
    with open(destino, "wb") as fh:
        escritor.write(fh)
    os.remove(crudo)
    os.remove(trabajo)

    sin = [a for a in re.findall(r'data-ref="([^"]+)"', html) if a not in paginas]
    print("· %s · %.1f MB · %d páginas · índice paginado en %d vuelta(s)"
          % (salida, os.path.getsize(destino) / 1e6, paginas_totales, vueltas))
    if sin:
        print("  ! %d entradas del índice se han quedado sin número de página: %s"
              % (len(sin), ", ".join(sin[:6])))


if __name__ == "__main__":
    main()
