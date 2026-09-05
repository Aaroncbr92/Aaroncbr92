#!/usr/bin/env python3
"""Arma el catálogo de la tienda leyéndolo de los propios volúmenes.

Ni un dato se escribe a mano. Cada fila sale de donde ya está:

- **el nombre**, de `BLOQUES` en `libro.py`;
- **temas, preguntas y fecha**, de la **portada del PDF**, que es lo que el
  comprador va a ver;
- **las páginas**, contándolas en el PDF;
- **las plazas**, del recuento del Anexo 1 en
  `convocatoria/1-2025-puestos-por-ocupacion.tsv`;
- **el precio**, de un tramo por número de páginas que se cambia en `TRAMOS`.

Se hace así por lo de siempre: un catálogo escrito aparte se desincroniza con
los volúmenes a la primera regeneración, y entonces la tienda promete
diecisiete temas donde hay dieciocho. Cuando cambie un volumen, se vuelve a
pasar esto y se reimporta.

Salida: `tienda/catalogo/productos.csv`, en el formato del importador de
WooCommerce (Herramientas → Importar → Productos WooCommerce (CSV)).

Uso:
    herramientas/catalogo.py
    herramientas/catalogo.py --url temarios.example
"""
import argparse
import csv
import os
import re
import sys

from pypdf import PdfReader

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from libro import BLOQUES          # noqa: E402  nombres de los volúmenes
from ordinales import cifra        # noqa: E402  «dieciocho» -> 18

PUESTOS_TSV = os.path.join(RAIZ, "convocatoria", "1-2025-puestos-por-ocupacion.tsv")
SALIDA = os.path.join(RAIZ, "tienda", "catalogo", "productos.csv")

# Precio por tramos de páginas. Es una propuesta: se discute en
# tienda/05-LANZAMIENTO.md §5.2 y se cambia aquí, no en la tienda.
TRAMOS = ((180, 44.0), (260, 54.0), (10**6, 64.0))
PRECIO_GENERAL = 34.0

# Qué filas del recuento de plazas cuenta cada volumen. La clave es el
# identificador del volumen; el valor, las parejas (ocupación, especialidad)
# que suman. La especialidad None significa «todas las de esa ocupación».
PLAZAS = {
    "produccion-asistencia":  [("PRODUCCION (ASISTENCIA)", None)],
    "produccion":             [("PRODUCCION", None)],
    "realizacion":            [("REALIZACION (ASISTENCIA)", None)],
    "realizacion-tv":         [("REALIZACION", "TV")],
    "documentacion":          [("DOCUMENTACION", None)],
    "informacion":            [("INFORMACION Y CONTENIDOS", None)],
    "gestion-administrativa": [("GESTION ADMINISTRATIVA", None)],
    "gestion":                [("GESTION", None)],
    "montaje-equipos":        [("MONTAJE EQUIPOS AUDIOVISUALES", None)],
    "edicion-montaje":        [("EDICION, MONTAJE Y PROCESOS AUDIOVISUALES", None)],
    "informacion-grafica":    [("INFORMACION GRAFICA Y CAPTACION DE IMAGEN Y SONIDO", None)],
    "sonido":                 [("SONIDO", None)],
    "tese":                   [("TECNICA EQUIPOS Y SIST. ELECTRONICO", None)],
    "tecnica-informatica":    [("TECNICA INFORMATICA", None)],
    "diseno-grafico":         [("DISEÑO GRAFICO", None)],
    "ing-tec-teleco":         [("INGENIERIA TECNICA", "TELECOMUNICACION")],
    "ing-tec-industrial":     [("INGENIERIA TECNICA", "INDUSTRIAL")],
    "ing-sup-teleco":         [("INGENIERIA SUPERIOR", "TELECOMUNICACION")],
    "imagen-personal":        [("IMAGEN PERSONAL", None)],
    "teitse":                 [("TECNICA EQUIPOS  INSTAL. Y SIST. ELECTRICOS", None)],
    "ambientacion-vestuario": [("AMBIENTACION VESTUARIO", None)],
    "profesor-orquesta":      [("PROFESOR DE ORQUESTA", None)],
    "enfermeria":             [("ENFERMERIA DE EMPRESA", None)],
    "medicina":               [("MEDICINA DE EMPRESA", None)],
    # El general no cuenta plazas: sirve a todas las ocupaciones, y poner ahí
    # las 872 de la convocatoria entera sería sugerir que basta con él.
    "general":                [],
}

COLUMNAS = [
    "SKU", "Name", "Type", "Published", "Visibility in catalog",
    "Short description", "Description",
    "Tax status", "In stock?", "Regular price", "Categories",
    "Virtual", "Downloadable",
    "Meta:_toac_slug", "Meta:_toac_actualizado", "Meta:_toac_paginas",
    "Meta:_toac_temas", "Meta:_toac_preguntas", "Meta:_toac_puestos",
]


def numero(texto):
    """«Dieciocho» o «18» -> 18. None si no se puede leer."""
    texto = texto.strip()
    if texto.isdigit():
        return int(texto)
    # «treinta y un temas»: `cifra` no conoce el apócope, se le da entero.
    return cifra(texto.replace(" un", " uno"))


def portada(ruta):
    """Temas, preguntas y fecha de generación, leídos de la portada del PDF."""
    lineas = PdfReader(ruta).pages[0].extract_text().split("\n")
    datos = {"temas": None, "preguntas": 0, "fecha": None}

    for linea in lineas:
        if "esquemas de repaso" in linea:
            # «Dieciocho temas · … · 134 preguntas reales de examen»
            m = re.match(r"\s*(.+?)\s+temas\b", linea)
            if m:
                datos["temas"] = numero(m.group(1))
            m = re.search(r"·\s*(\d+)\s+preguntas", linea)
            datos["preguntas"] = int(m.group(1)) if m else 0

        m = re.match(r"\s*Generado el (\d{2})/(\d{2})/(\d{4})", linea)
        if m:
            dia, mes, anio = m.groups()
            datos["fecha"] = f"{anio}-{mes}-{dia}"

    return datos


def paginas(ruta):
    return len(PdfReader(ruta).pages)


def plazas():
    """Recuento del Anexo 1, indexado por (ocupación, especialidad)."""
    filas = []
    with open(PUESTOS_TSV, encoding="utf-8") as f:
        for linea in f:
            if linea.startswith("#") or not linea.strip():
                continue
            partes = linea.rstrip("\n").split("\t")
            if len(partes) < 3:
                continue
            filas.append((partes[0].strip(), partes[1].strip(), int(partes[2])))
    return filas


def cuenta_plazas(slug, filas):
    reglas = PLAZAS.get(slug)
    if reglas is None:
        print(f"  aviso: {slug} no está en PLAZAS; va sin recuento de plazas")
        return ""
    total = 0
    for ocupacion, especialidad in reglas:
        encontrado = False
        for f_ocu, f_esp, f_num in filas:
            if f_ocu != ocupacion:
                continue
            if especialidad is not None and f_esp != especialidad:
                continue
            total += f_num
            encontrado = True
        if not encontrado:
            print(f"  aviso: {slug} apunta a «{ocupacion}»"
                  f"{'/' + especialidad if especialidad else ''}, que no está en el recuento")
    return total or ""


def precio(slug, n_paginas):
    if slug == "general":
        return PRECIO_GENERAL
    for tope, importe in TRAMOS:
        if n_paginas <= tope:
            return importe
    return TRAMOS[-1][1]


def nombre(slug):
    bloque = BLOQUES.get(slug)
    if not bloque:
        return slug.replace("-", " ").capitalize()
    if bloque.get("ocupacion"):
        return f"Temario específico · {bloque['ocupacion']}"
    return "Temario general · RTVE"


def descripcion(slug, datos, n_paginas, n_plazas, url):
    bloque = BLOQUES.get(slug, {})
    ocupacion = bloque.get("ocupacion")

    partes = []
    if ocupacion:
        partes.append(
            f"<p>Temario específico de <strong>{ocupacion}</strong> para las oposiciones "
            f"de RTVE, con los {datos['temas']} temas del programa oficial "
            f"(ANEXO 2 de las bases), en {n_paginas} páginas.</p>")
    else:
        partes.append(
            f"<p>Los {datos['temas']} temas del <strong>bloque común</strong>, "
            f"idénticos en todas las ocupaciones tipo, en {n_paginas} páginas.</p>")

    partes.append(
        "<p>Cada dato se ha leído en su fuente oficial antes de escribirlo: la "
        "legislación, en el texto consolidado del BOE, con la redacción vigente "
        "a la fecha de corte de la convocatoria. Lo que no se ha podido "
        "confirmar, no está.</p>")

    partes.append("<ul>")
    partes.append(f"<li>{datos['temas']} temas desarrollados y "
                  f"{datos['temas']} esquemas de repaso.</li>")
    if datos["preguntas"]:
        partes.append(f"<li>{datos['preguntas']} preguntas reales de convocatorias "
                      "anteriores, con su respuesta oficial.</li>")
    if n_plazas:
        partes.append(f"<li>{n_plazas} plazas de esta ocupación en la última "
                      "convocatoria.</li>")
    partes.append("<li>PDF con índice navegable. Actualizaciones incluidas.</li>")
    partes.append("</ul>")

    partes.append(
        f'<p>Puedes ver el índice completo y las primeras páginas antes de '
        f'comprar: <a href="https://{url}/muestra/{slug}/">ver la muestra</a>.</p>')

    return "".join(partes)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", default="temarios.example",
                        help="dominio de la tienda, para los enlaces de la muestra")
    parser.add_argument("--salida", default=SALIDA)
    args = parser.parse_args()

    filas_plazas = plazas()
    volumenes = sorted(n for n in os.listdir(RAIZ)
                       if n.startswith("libro-") and n.endswith(".pdf"))
    if not volumenes:
        sys.exit("No hay ningún libro-*.pdf. ¿Estás en la raíz del repositorio?")

    print(f"Catálogo de {len(volumenes)} volúmenes:")
    filas = []

    for fichero in volumenes:
        ruta = os.path.join(RAIZ, fichero)
        slug = fichero[len("libro-"):-len(".pdf")]

        datos = portada(ruta)
        n_paginas = paginas(ruta)
        n_plazas = cuenta_plazas(slug, filas_plazas)
        importe = precio(slug, n_paginas)

        if datos["temas"] is None:
            print(f"  aviso: no he sabido leer los temas de {fichero}")
        if datos["fecha"] is None:
            print(f"  aviso: {fichero} no dice cuándo se generó")

        filas.append({
            "SKU": f"TOAC-{slug.upper()}",
            "Name": nombre(slug),
            "Type": "simple",
            "Published": 1,
            "Visibility in catalog": "visible",
            "Short description":
                f"{datos['temas']} temas · {n_paginas} páginas · "
                + (f"{datos['preguntas']} preguntas reales de examen"
                   if datos["preguntas"] else "sin preguntas de examen"),
            "Description": descripcion(slug, datos, n_paginas, n_plazas, args.url),
            "Tax status": "taxable",
            "In stock?": 1,
            "Regular price": f"{importe:.2f}",
            "Categories": "Temario general" if slug == "general" else "Temarios específicos",
            # Virtual sí; descargable NO: la descarga la sirve toac-tienda.php,
            # no WooCommerce. Ver tienda/01-ARQUITECTURA.md §1.4.
            "Virtual": 1,
            "Downloadable": 0,
            "Meta:_toac_slug": slug,
            "Meta:_toac_actualizado": datos["fecha"] or "",
            "Meta:_toac_paginas": n_paginas,
            "Meta:_toac_temas": datos["temas"] or "",
            "Meta:_toac_preguntas": datos["preguntas"] or "",
            "Meta:_toac_puestos": n_plazas,
        })
        print(f"  {slug:24} {n_paginas:>4} pp · {str(datos['temas']):>3} temas · "
              f"{str(datos['preguntas'] or '—'):>4} preg · "
              f"{str(n_plazas or '—'):>4} plazas · {importe:6.2f} €")

    os.makedirs(os.path.dirname(args.salida), exist_ok=True)
    with open(args.salida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUMNAS)
        escritor.writeheader()
        escritor.writerows(filas)

    total = sum(float(f["Regular price"]) for f in filas)
    print(f"\n{len(filas)} productos en {os.path.relpath(args.salida, RAIZ)}. "
          f"Catálogo completo: {total:.2f} €.")


if __name__ == "__main__":
    main()
