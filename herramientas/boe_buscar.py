#!/usr/bin/env python3
"""Busca documentos del BOE **por su título**, que es lo que faltaba.

`boe.py` sabe leer una norma cuando ya se conoce su identificador, y la API de
sumarios sabe dar el boletín de un día cuando ya se conoce la fecha. Entre las
dos quedaba fuera lo más frecuente en un temario de actualidad: **saber qué se
busca y no saber ni el identificador ni el día**. Un premio nacional, un
nombramiento, la ley que se aprobó «en junio»: todo eso está en el BOE y no se
llega a ello con ninguna de las dos herramientas anteriores.

El buscador del BOE lo resuelve, pero su formulario tiene dos trampas que dan
**cero resultados sin dar ningún error**, que es la peor forma de fallar:

  · Las **secciones son casillas**, `dato[0][1]` a `dato[0][5]` y `dato[0][T]`,
    y van todas marcadas por defecto. Si se manda la consulta sin ellas, el
    buscador responde «no se han encontrado documentos» —no «faltan campos»—,
    y una búsqueda que sí tenía respuesta se anota como camino cerrado.
  · Los **nombres de los campos no son los que se ven**: el título es
    `campo[1]=TITULOS` con el texto en `dato[1]`, y la fecha de publicación es
    `campo[6]=FPU` con `dato[6][0]` y `dato[6][1]` en formato ISO.

Uso:  boe_buscar.py "Premio Nacional de Poesía" 2024-01-01 2024-12-31
      boe_buscar.py "nombramiento Presidente del Tribunal Supremo"
"""
import html
import re
import subprocess
import sys

BUSCADOR = "https://www.boe.es/buscar/boe.php"
AGENTE = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/126.0 Safari/537.36")


def busca(titulo, desde=None, hasta=None, cuantos=40):
    """[(identificador, departamento, boletín, título)] de los que casan."""
    campos = ["--data-urlencode", "campo[0]=ORIS", "--data-urlencode", "operador[0]=and"]
    for s in ("1", "2", "3", "4", "5", "T"):
        campos += ["--data-urlencode", "dato[0][%s]=%s" % (s, s)]
    campos += ["--data-urlencode", "campo[1]=TITULOS",
               "--data-urlencode", "dato[1]=" + titulo,
               "--data-urlencode", "operador[1]=and"]
    if desde:
        campos += ["--data-urlencode", "campo[6]=FPU",
                   "--data-urlencode", "dato[6][0]=" + desde,
                   "--data-urlencode", "dato[6][1]=" + (hasta or desde),
                   "--data-urlencode", "operador[6]=and"]
    campos += ["--data-urlencode", "page_hits=%d" % cuantos,
               "--data-urlencode", "accion=Buscar"]
    crudo = subprocess.run(["curl", "-sS", "-A", AGENTE, "-G", BUSCADOR] + campos,
                           capture_output=True, text=True, timeout=90).stdout
    # cada resultado es un <li> con el departamento, la referencia del boletín y
    # el título; se recorta el marcado y se parte por la referencia, que es lo
    # único que aparece exactamente una vez por documento
    texto = html.unescape(re.sub(r"(?s)<[^>]+>", " ", crudo))
    texto = re.sub(r"\s+", " ", texto)
    # el nombre de la sección lleva punto dentro —«III. Otras disposiciones»—,
    # así que no se puede cortar por el primer punto: se toma de la lista fija
    SECCIONES = ("I. Disposiciones generales", "II. Autoridades y personal",
                 "III. Otras disposiciones", "IV. Administración de Justicia",
                 "V. Anuncios", "TC. Tribunal Constitucional")
    fuera = []
    for m in re.finditer(r"BOE (\d+) de (\d{2}/\d{2}/\d{4}) - (.*?) "
                         r"Ir al documento Ref\. (BOE-[A-Z]-\d{4}-\d+)", texto):
        resto = m.group(3).strip()
        seccion = next((s for s in SECCIONES if resto.startswith(s)), "")
        fuera.append((m.group(4), seccion, "BOE %s de %s" % (m.group(1), m.group(2)),
                      resto[len(seccion):].strip()))
    return fuera


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__.strip().splitlines()[-2].strip())
    filas = busca(sys.argv[1], *sys.argv[2:4])
    if not filas:
        print("sin resultados")
        return
    for ident, seccion, boletin, titulo in filas:
        print("%-18s %s · %s" % (ident, boletin, seccion))
        print("   %s" % titulo)


if __name__ == "__main__":
    main()
