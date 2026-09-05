#!/usr/bin/env python3
"""Saca de cada volumen el PDF de muestra que se enseña antes de comprar.

La muestra es **portada + índice completo + las primeras páginas del cuerpo**.
El índice entero se enseña a propósito: es lo que convence: quien duda quiere
comprobar que están sus temas, no leer gratis el primero.

**Dónde acaba el índice no se adivina.** Se lee del propio PDF: `pdf.py` deja
escritos los marcadores del panel de navegación, y la página del primero es la
primera del cuerpo. Todo lo anterior es portada e índice. Si un volumen no
trajera marcadores —no debería pasar—, se avisa y se cae a un número fijo.

Cada página de la muestra se sella con una diagonal y un pie que dicen lo que
es, y al final se añade una página de cierre con el recuento del volumen
completo. Eso resuelve el caso incómodo: la muestra que se reenvía por ahí sin
contexto sigue diciendo de dónde sale y cuánto falta.

Lo que protege la muestra no es el sellado: es **que sólo contiene esas
páginas**. Lo demás no ha salido del servidor. Ver `tienda/03-PDFS.md`.

**Cuidado con el peso.** Sellar una página deja su flujo de contenido *sin
comprimir*: la muestra de Sonido pasaba de 358 KB a 1.665 KB, cinco veces más,
por eso y sólo por eso. Hay que volver a comprimir cada página después de
sellarla. Se hace abajo, y no se puede quitar: una muestra de megabyte y medio
es una muestra que en un móvil nadie espera a que cargue.

Uso:
    herramientas/muestra.py                      # los veinticinco volúmenes
    herramientas/muestra.py libro-sonido.pdf     # uno
    herramientas/muestra.py --paginas 20         # más cuerpo en la muestra
"""
import argparse
import io
import os
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "muestras")

# El nombre de cada volumen sale de `libro.py`, que ya lo tiene escrito una vez.
# No se copia aquí: dos listas de veinticinco nombres se desincronizan a la
# primera ocupación nueva. Si `libro.py` no se puede importar —le faltaría una
# dependencia—, la muestra se genera igual con el identificador por nombre.
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from libro import BLOQUES
except Exception:
    BLOQUES = {}

# Páginas de cuerpo que se enseñan, además de la portada y del índice entero.
CUERPO_POR_DEFECTO = 12

# Si un volumen viniera sin marcadores, hasta dónde cortar a ciegas.
CORTE_A_CIEGAS = 16

TINTA = HexColor("#5a6b86")
MARCA = "TOAC · Temarios de Oposiciones"


def primera_pagina_del_cuerpo(lector):
    """Página (base 0) a la que apunta el primer marcador del PDF.

    Es donde acaba el índice. Devuelve None si el PDF no trae marcadores.
    """
    try:
        marcadores = lector.outline
    except Exception:
        return None

    def primero(nodo):
        # El árbol de marcadores mezcla listas (los hijos) y destinos.
        if isinstance(nodo, list):
            for hijo in nodo:
                encontrado = primero(hijo)
                if encontrado is not None:
                    return encontrado
            return None
        try:
            return lector.get_destination_page_number(nodo)
        except Exception:
            return None

    return primero(marcadores)


def nombre_del_volumen(slug):
    """«sonido» → «Temario específico · Sonido»."""
    bloque = BLOQUES.get(slug)
    if not bloque:
        return slug.replace("-", " ").capitalize()
    if bloque.get("ocupacion"):
        return f"{bloque['titulo']} · {bloque['ocupacion']}"
    return bloque["titulo"]


def sello(ancho, alto, pie):
    """Capa que se dibuja encima de cada página de la muestra."""
    lienzo_bytes = io.BytesIO()
    lienzo = canvas.Canvas(lienzo_bytes, pagesize=(ancho, alto))

    # La diagonal, muy clara: tiene que dejar leer el texto de debajo.
    lienzo.saveState()
    lienzo.setFillColor(HexColor("#c9d2e0"))
    lienzo.setFont("Helvetica-Bold", 58)
    lienzo.translate(ancho / 2, alto / 2)
    lienzo.rotate(35)
    try:
        lienzo.setFillAlpha(0.22)
    except AttributeError:
        pass  # reportlab antiguo: se queda con el color claro y ya.
    lienzo.drawCentredString(0, 0, "MUESTRA")
    lienzo.restoreState()

    # El pie, que es el que lleva la información útil.
    lienzo.setFillColor(TINTA)
    lienzo.setFont("Helvetica", 7)
    lienzo.drawCentredString(ancho / 2, 16, pie)

    lienzo.save()
    lienzo_bytes.seek(0)
    return PdfReader(lienzo_bytes).pages[0]


def cierre(ancho, alto, titulo, paginas, url):
    """Última página de la muestra: qué es esto y dónde está el completo."""
    lienzo_bytes = io.BytesIO()
    lienzo = canvas.Canvas(lienzo_bytes, pagesize=(ancho, alto))

    y = alto - 170
    lienzo.setFillColor(TINTA)
    lienzo.setFont("Helvetica-Bold", 19)
    lienzo.drawCentredString(ancho / 2, y, "Hasta aquí la muestra")

    lienzo.setFont("Helvetica", 11)
    for linea in (
        f"{titulo}",
        f"El volumen completo tiene {paginas} páginas.",
        "",
        "Cada dato está verificado contra su fuente oficial,",
        "y el temario se actualiza cuando la norma cambia.",
        "Las actualizaciones van incluidas en la compra.",
    ):
        y -= 22
        lienzo.drawCentredString(ancho / 2, y, linea)

    y -= 44
    lienzo.setFont("Helvetica-Bold", 11)
    lienzo.drawCentredString(ancho / 2, y, url)

    lienzo.setFont("Helvetica", 7.5)
    lienzo.drawCentredString(ancho / 2, 34, MARCA)

    lienzo.save()
    lienzo_bytes.seek(0)
    return PdfReader(lienzo_bytes).pages[0]


def una(ruta, cuerpo, url):
    nombre = os.path.basename(ruta)
    slug = nombre[len("libro-"):-len(".pdf")]

    lector = PdfReader(ruta)
    total = len(lector.pages)

    inicio_cuerpo = primera_pagina_del_cuerpo(lector)
    if inicio_cuerpo is None:
        print(f"  aviso: {nombre} no trae marcadores; se corta en {CORTE_A_CIEGAS} páginas")
        hasta = CORTE_A_CIEGAS
    else:
        hasta = inicio_cuerpo + cuerpo

    hasta = min(hasta, total)

    titulo = nombre_del_volumen(slug)
    pie = (f"Muestra de «{titulo}» · {MARCA} · "
           f"El volumen completo tiene {total} páginas · {url}")

    escritor = PdfWriter()
    for i in range(hasta):
        pagina = lector.pages[i]
        ancho = float(pagina.mediabox.width)
        alto = float(pagina.mediabox.height)

        # Los enlaces del índice apuntan a páginas que aquí no están: se
        # quitan, para que ningún clic acabe en el vacío.
        if "/Annots" in pagina:
            del pagina["/Annots"]

        # La portada no se ensucia: es la cara del producto.
        if i > 0:
            pagina.merge_page(sello(ancho, alto, pie))

        escritor.add_page(pagina)

    primera = lector.pages[0]
    escritor.add_page(cierre(float(primera.mediabox.width),
                             float(primera.mediabox.height),
                             titulo, total, url))

    # Y ahora sí, comprimir: `compress_content_streams` exige que la página ya
    # cuelgue del escritor, así que no se puede hacer dentro del bucle de arriba.
    # Ver el aviso de peso del encabezado.
    for pagina in escritor.pages:
        pagina.compress_content_streams()

    # La muestra no lleva metadatos del original ni marcadores al resto.
    escritor.add_metadata({
        "/Title": f"Muestra · {titulo}",
        "/Author": MARCA,
        "/Subject": "Muestra sin valor para el estudio",
    })

    os.makedirs(SALIDA, exist_ok=True)
    destino = os.path.join(SALIDA, f"muestra-{slug}.pdf")
    with open(destino, "wb") as f:
        escritor.write(f)

    peso = os.path.getsize(destino) / 1024
    print(f"  {nombre}: {hasta} de {total} páginas + cierre "
          f"→ muestras/muestra-{slug}.pdf ({peso:.0f} KB)")
    return destino


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("volumenes", nargs="*",
                        help="libro-*.pdf. Sin argumentos, todos.")
    parser.add_argument("--paginas", type=int, default=CUERPO_POR_DEFECTO,
                        help=f"páginas de cuerpo en la muestra (por defecto {CUERPO_POR_DEFECTO})")
    parser.add_argument("--url", default="temarios.example",
                        help="dominio de la tienda, para el pie y el cierre")
    args = parser.parse_args()

    rutas = args.volumenes
    if not rutas:
        rutas = sorted(os.path.join(RAIZ, n) for n in os.listdir(RAIZ)
                       if n.startswith("libro-") and n.endswith(".pdf"))
    if not rutas:
        sys.exit("No hay ningún libro-*.pdf. ¿Estás en la raíz del repositorio?")

    print(f"Muestras de {len(rutas)} volúmenes, {args.paginas} páginas de cuerpo cada una:")
    for ruta in rutas:
        if not os.path.exists(ruta):
            print(f"  aviso: no existe {ruta}")
            continue
        una(ruta, args.paginas, args.url)

    print(f"\nEn {SALIDA}. Se suben a ~/temarios_privados/muestras/ "
          f"(fase 3 de tienda/02-IMPLANTACION.md).")


if __name__ == "__main__":
    main()
