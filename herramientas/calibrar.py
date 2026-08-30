#!/usr/bin/env python3
"""Reparto de preguntas por materia en los exámenes transcritos.

Clasificación por palabras clave, con la primera regla que casa. Es una
aproximación: sirve para ver dónde apretar, no para dar por buena una cifra.
Las preguntas sin clasificar se listan enteras para mirarlas a mano.
"""
import re
import sys
import unicodedata

MATERIAS = [
    ("G8 · Prevención de riesgos (Ley 31/1995)", [
        r"31/1995", r"riesgos laborales", r"pantallas de visualizaci", r"in itinere",
        r"in misi[oó]n", r"incendi", r"extintor", r"musculoesquel", r"delegad[oa]s? de prevenci",
        r"evaluaci[oó]n de riesgos", r"equipo de protecci[oó]n", r"servicio de prevenci"]),
    ("G6 · Igualdad (II Plan y Guía de RTVE)", [
        r"plan de igualdad", r"gu[ií]a de igualdad", r"perspectiva de g[eé]nero",
        r"acoso sexual", r"brecha salarial", r"lenguaje inclusiv", r"violencia de g[eé]nero"]),
    ("G4 · Financiación (Ley 8/2009)", [
        r"8/2009", r"fondo de reserva", r"aportaci[oó]n .{0,30}operadores",
        r"tasa .{0,30}reserva de dominio", r"financiaci[oó]n de la corporaci"]),
    ("G7 · Comunicación audiovisual (Ley 13/2022)", [
        r"13/2022", r"general de comunicaci[oó]n audiovisual", r"prestador(es)? del servicio",
        r"servicio de intercambio de v[ií]deos", r"cnmc", r"comisi[oó]n nacional de los mercados"]),
    ("G5 · III Convenio Colectivo", [
        r"convenio colectivo", r"grupo profesional", r"ocupaci[oó]n tipo", r"[aá]mbito ocupacional",
        r"comisi[oó]n de empleo", r"excedencia", r"vacaciones", r"jornada .{0,25}anual",
        r"antig[uü]edad", r"permiso retribuido", r"comit[eé] de valoraci"]),
    ("G2/G3 · Ley 17/2006 y Ley 5/2017", [
        r"17/2006", r"5/2017", r"consejo de administraci[oó]n", r"corporaci[oó]n rtve",
        r"mandato.?marco", r"contrato.?programa", r"consejo asesor", r"consejos? de informativos",
        r"administrador provisional", r"radio y (la )?televisi[oó]n de titularidad estatal",
        r"presidencia de la corporaci"]),
    ("G1 · Constitución", [
        r"constituci[oó]n", r"\bce\b", r"tribunal constitucional", r"defensor del pueblo",
        r"cortes generales", r"congreso de los diputados", r"\bsenado\b", r"corona",
        r"poder judicial", r"tribunal de cuentas", r"estatuto de autonom",
        r"derechos fundamentales", r"consejo general del poder judicial"]),
]

ESPECIFICO = [
    ("E · Actualidad y cultura", [
        r"\b20(2[3-9])\b", r"premio nacional", r"nobel", r"elecciones", r"presidente de",
        r"guerra", r"gobierno de", r"ol[ií]mpic", r"campeonato", r"pel[ií]cula", r"novela"]),
    ("E · Unión Europea e instituciones internacionales", [
        r"uni[oó]n europea", r"parlamento europeo", r"comisi[oó]n europea", r"consejo europeo",
        r"onu", r"unesco", r"otan", r"fmi", r"tribunal penal internacional", r"directiva"]),
    ("E · Materia propia del puesto", []),
]


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).lower()


# tras el separador puede no haber espacio («101.-Seleccione»), así que en vez de
# exigirlo se exige que lo que siga no sea un dígito, que es lo que distingue la
# marca de una cifra como «1.000»
MARCA = r"(?m)^\s*(\d{1,3})\s*[.,\-–]{1,2}\s*(?=[^\d\s])"
OPCIONES = re.compile(r"(?m)^\s*a\)").search


def preguntas(texto):
    """Trocea el cuadernillo en preguntas por su numeración.

    El salto de página (\x0c) no lleva salto de línea detrás, así que el pie y
    la cabecera de la página siguiente quedan pegados al número de la pregunta
    que abre esa página: «2º Llamamiento\x0c2º Llamamiento\x0c1.-». La marca
    dejaba entonces de estar a principio de línea, la pregunta no se reconocía
    y su texto se acumulaba dentro de la anterior: 83 preguntas de cuatro
    cuadernillos, cada una fundida con su vecina y ninguna de las dos
    contestable. Convertir el salto de página en salto de línea las recupera.
    """
    texto = texto.replace("\x0c", "\n")
    marcas = list(re.finditer(MARCA, texto))
    # los números que aparecen dentro de las respuestas también casan, así que
    # solo se acepta la marca que continúa la numeración: 1, 2, 3...
    # el OCR se come algún número, así que se tolera un salto de uno
    buenas, esperado = [], 1
    for m in marcas:
        n = int(m.group(1))
        if n in (esperado, esperado + 1):
            buenas.append((n, m.start()))
            esperado = n + 1
    buenas = recupera_la_primera(texto, marcas, buenas)
    fuera = []
    for i, (n, ini) in enumerate(buenas):
        fin = buenas[i + 1][1] if i + 1 < len(buenas) else len(texto)
        fuera.append((n, texto[ini:fin]))
    return fuera


def recupera_la_primera(texto, marcas, buenas):
    """Rescata la pregunta 1 cuando el OCR le lee mal el número.

    En el cuadernillo de Documentación la 1 sale como «4.», no continuaba la
    serie y se descartaba entera; no se pegaba a ninguna, se perdía. Si la
    serie arranca en la 2 y justo antes hay una marca con su juego de
    opciones, esa marca es la 1. Lo confirma la plantilla: en ese examen la 1
    es «d», y la opción d de ese bloque es la definición de perspectiva de
    género del II Plan de Igualdad de RTVE.
    """
    if not buenas or buenas[0][0] != 2:
        return buenas
    previas = [m for m in marcas if m.start() < buenas[0][1]]
    if not previas or not OPCIONES(texto[previas[-1].start():buenas[0][1]]):
        return buenas
    return [(1, previas[-1].start())] + buenas


def clasifica(cuerpo, reglas):
    c = limpia(cuerpo)
    for nombre, patrones in reglas:
        for p in patrones:
            if re.search(p, c):
                return nombre
    return None


def informe(ruta, etiqueta):
    texto = open(ruta, encoding="utf-8").read()
    qs = preguntas(texto)
    cuenta, sin = {}, []
    for n, cuerpo in qs:
        m = clasifica(cuerpo, MATERIAS)
        if m is None:
            m = clasifica(cuerpo, ESPECIFICO[:2])
        if m is None:
            m = "E · Materia propia del puesto"
            sin.append((n, re.sub(r"\s+", " ", cuerpo)[:150]))
        cuenta[m] = cuenta.get(m, 0) + 1
    print("## %s" % etiqueta)
    print()
    print("Preguntas localizadas: %d" % len(qs))
    print()
    total = sum(cuenta.values()) or 1
    for m, c in sorted(cuenta.items(), key=lambda x: -x[1]):
        print("| %-46s | %3d | %4.1f %% |" % (m, c, 100.0 * c / total))
    print()
    return cuenta, sin


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        ruta, _, etiqueta = arg.partition("=")
        informe(ruta, etiqueta or ruta)
