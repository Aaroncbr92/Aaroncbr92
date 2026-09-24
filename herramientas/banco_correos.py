#!/usr/bin/env python3
"""Arma el banco de preguntas del específico de Correos a partir del acta.

**Por qué no sirve `banco_especifico.py`.** Aquél lee los cuadernillos de RTVE,
que viven en `convocatoria/examenes`, se llaman `NN_preguntas_<ocupacion>.txt` y
traen la plantilla en un fichero aparte con el mismo sufijo. Los de Correos no
cumplen ninguna de las tres cosas: viven en `convocatoria/correos/examenes`, se
llaman `Cuestionario-<PUESTO>_<MODELO>_07052023.txt` y **ya están cruzados con su
plantilla** por `correos_examen.py`, que deja un `examen-<PUESTO>-<MODELO>.md`
con el enunciado, las cuatro opciones y una flecha en la correcta. Forzar el
otro script a entender esto habría sido meterle una tercera excepción con nombre
propio; se escribe éste, que lee lo que hay.

**Lo que este script sí comparte es la regla.** El reparto no lo decide ninguna
expresión regular: está escrito a mano, pregunta a pregunta, en
`banco/especifico-correos.tsv`, y aquí sólo se aplica. Y avisa de las dos cosas
que, si no se avisan, no dan ningún error:

  · **Filas huérfanas**: una fila del acta que ya no casa con ninguna pregunta.
  · **Preguntas sin fila**: las que están en el cuadernillo y no se han
    repartido. Ésa es la cuenta de lo que falta, y no aparece sola.

**Los modelos B no se leen.** Son el modelo A en otro orden —comprobado
enunciado a enunciado— y leerlos contaría cada pregunta dos veces sin dar
ningún error, que es exactamente la forma de duplicar un banco entero.

**Las anuladas se imprimen como anuladas.** La plantilla oficial escribe
«Anulada» en su celda: el enunciado sigue siendo material de estudio, pero su
respuesta no calibra nada y el volumen no debe fingir que sí.

Uso:  python3 herramientas/banco_correos.py
"""
import os
import re
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(RAIZ, "convocatoria/correos/examenes")
SALIDA = os.path.join(RAIZ, "banco")
ACTA = os.path.join(SALIDA, "especifico-correos.tsv")

# Cada puesto aporta su modelo A y nada más. El modelo B es el mismo examen
# barajado, y el acta lo dice con su recuento delante.
MODELOS = [("Cuestionario-ATC_A_07052023", "ATC-A"),
           ("Cuestionario-REP_A_07052023", "REP-A")]

TITULOS = {
    "01": "Correos · Tema 1 · Marco normativo postal y naturaleza jurídica",
    "02": "Correos · Tema 2 · Experiencia de personas, diversidad, prevención y sostenibilidad",
    "03": "Correos · Tema 3 · Productos y servicios: comunicación, paquetería y e-commerce",
    "04": "Correos · Tema 4 · Productos y servicios en oficinas, financieros, digitales y filatelia",
    "05": "Correos · Tema 5 · Nuevas líneas de negocio: logística, frío y patrimonio",
    "06": "Correos · Tema 6 · Herramientas: funciones y utilidad",
    "07": "Correos · Tema 7 · Procesos operativos I: admisión",
    "08": "Correos · Tema 8 · Procesos operativos II: tratamiento y transporte",
    "09": "Correos · Tema 9 · Procesos operativos III: distribución y entrega",
    "10": "Correos · Tema 10 · El cliente: atención, calidad y protocolos de venta",
    "11": "Correos · Tema 11 · Internacionalización y aduanas",
    "12": "Correos · Tema 12 · Normas de cumplimiento: datos, blanqueo, ética y ciberseguridad",
}


def acta():
    """{(origen, nº): (tema, motivo, epígrafe)} leído del acta de clasificación."""
    fuera = {}
    for linea in open(ACTA, encoding="utf-8"):
        if linea.startswith("#") or not linea.strip():
            continue
        c = (linea.rstrip("\n").split("\t") + ["", "", ""])[:5]
        if c[0] == "origen":
            continue
        fuera[(c[0], int(c[1]))] = (c[2], c[3], c[4])
    return fuera


def remite(epigrafe):
    """El renglón que va debajo de la pregunta, o cadena vacía.

    **Tres formas y ninguna más.** Un número de epígrafe remite al tema; un
    texto que empieza por `!` declara que el tema **no** la contesta y por qué,
    que es lo que hay que decir cuando es verdad; y una casilla vacía no imprime
    nada, porque todavía no se ha mirado y fingir que sí sería lo contrario de
    lo que este banco hace.
    """
    epigrafe = epigrafe.strip()
    if not epigrafe or epigrafe == "--":
        return ""
    if epigrafe.startswith("!"):
        return "El tema no la contesta: %s" % epigrafe[1:].strip()
    return "La contesta el epígrafe %s." % epigrafe


def preguntas(fichero):
    """[(nº, enunciado, [(letra, texto)], letra correcta o None, anulada)].

    Una pregunta psicotécnica **no trae opciones**: sus cuatro alternativas son
    dibujos y el volcado se queda con el enunciado. Se devuelven igual, con la
    lista vacía, para que el acta pueda declararlas y la cuenta cuadre; el banco
    no las escribe.
    """
    texto = open(fichero, encoding="utf-8").read()
    fuera = []
    for bloque in re.split(r"\n\n(?=\*\*\d+\.\*\* )", texto):
        m = re.match(r"\*\*(\d+)\.\*\* (.*?)(?=\n- \*\*A\.|\Z)", bloque, re.S)
        if not m:
            continue
        enunciado = " ".join(m.group(2).split())
        anulada = "**ANULADA**" in enunciado
        enunciado = enunciado.replace("· **ANULADA**", "").strip()
        opciones, letra = [], None
        for L, txt in re.findall(r"(?m)^- \*\*([A-D])\.\*\* (.*)$", bloque):
            txt = txt.rstrip()
            if txt.endswith("←"):
                letra = L
                txt = txt[:-1].rstrip()
            opciones.append((L, txt))
        fuera.append((int(m.group(1)), enunciado, opciones, letra, anulada))
    return fuera


def main():
    filas = acta()
    portema = defaultdict(list)
    usadas, sinfila, fuera_programa = set(), [], 0

    for base, modelo in MODELOS:
        # el fichero normalizado se llama `examen-ATC-A.md` / `examen-REP-A.md`
        ruta = os.path.join(DIR, "examen-%s.md" % modelo)
        for n, enunciado, opciones, letra, anulada in preguntas(ruta):
            clave = (base, n)
            if clave not in filas:
                sinfila.append(clave)
                continue
            tema = filas[clave][0]
            usadas.add(clave)
            if tema == "--":
                fuera_programa += 1
                continue
            # en minúscula, como el resto del banco: el compositor del volumen
            # reconoce la opción por «a)…d)» y con la mayúscula no la separa
            cuerpo = [enunciado] + ["%s) %s" % (L.lower(), t) for L, t in opciones]
            portema[tema].append((base, n, letra, anulada, "\n".join(cuerpo),
                                  remite(filas[clave][2])))

    total = 0
    for tema, items in sorted(portema.items()):
        anuladas = sum(1 for x in items if x[3])
        ruta = os.path.join(SALIDA, "correos-%s.md" % tema)
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n" % TITULOS[tema])
            fh.write("%d preguntas reales del examen del 7 de mayo de 2023 para el "
                     "ingreso de\npersonal laboral fijo en el Grupo Profesional IV. La "
                     "respuesta es la de la\nplantilla oficial; donde pone «anulada» es "
                     "que la propia plantilla la anuló.\n\n" % len(items))
            if anuladas:
                fh.write("**%d de estas preguntas están anuladas.** Su enunciado salió del "
                         "temario y\nsigue sirviendo para estudiar; su respuesta, no.\n\n"
                         % anuladas)
            for origen, n, letra, anul, cuerpo, rem in items:
                resp = "anulada" if anul else (letra.lower() if letra else "sin plantilla")
                fh.write("---\n\n**%s · nº %d · respuesta: %s**\n\n```\n%s\n```\n\n"
                         % (origen, n, resp, cuerpo))
                if rem:
                    fh.write("*%s*\n\n" % rem)
        print("%-84s %3d preguntas -> banco/correos-%s.md"
              % (TITULOS[tema], len(items), tema))
        total += len(items)

    print()
    print("del bloque específico: %d repartidas; %d declaradas fuera del programa; "
          "quedan %d sin clasificar" % (total, fuera_programa, len(sinfila)))
    for c in sinfila:
        print("  ? %s nº %d" % c)
    huerfanas = sorted(set(filas) - usadas)
    if huerfanas:
        print()
        print("! %d filas del acta no casan con ninguna pregunta:" % len(huerfanas))
        for h in huerfanas:
            print("  ! %s nº %d" % h)


if __name__ == "__main__":
    sys.exit(main())
