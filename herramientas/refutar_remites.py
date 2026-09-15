#!/usr/bin/env python3
"""Sexta lente: el remite de cada pregunta, contra el epígrafe al que remite.

**Un remite es una afirmación**, y del mismo género que las que persiguen las
otras cinco lentes: dice que *este* epígrafe de *este* tema contesta *esta*
pregunta. Escrito a mano en `banco/especifico-correos.tsv` y luego impreso
debajo del enunciado, **nadie volvería a comprobarlo**, y un remite que apunta a
un epígrafe que se renumeró —o que nunca dijo lo que la pregunta mide— es peor
que ninguno: manda a estudiar al sitio equivocado con la autoridad del libro.

La lente comprueba tres cosas, de menos a más fina:

  1. **Que el epígrafe existe.** Se numeran los epígrafes del tema igual que lo
     hace `libro.py` y se busca el número del remite. Si no está, se canta. Esto
     es lo que salva de los renumerados: añadir un epígrafe a mitad del tema
     corre todos los de abajo, y **ningún otro sitio se entera**.
  2. **Que la raíz del remite es el tema donde está repartida la pregunta.**
     Remitir la pregunta del tema 7 al epígrafe 3.2 es un dedo, no un criterio.
  3. **Que el cuerpo de ese epígrafe habla de lo que la pregunta mide.** Se
     toman las palabras con carga del enunciado y de la opción correcta y se
     miran contra el cuerpo del epígrafe **y el de sus subepígrafes**. Por
     debajo de un mínimo se canta, **como sospecha y no como sentencia**: hay
     preguntas cuya opción correcta es «las respuestas A y B son correctas» y
     ahí no hay vocabulario que compartir. Lo que la lente dice es *ve a mirar
     ésta*, que es su oficio.
  4. **Que no haya OTRO TEMA que hable mucho más de ella.** Este es el que
     importa y nació de un fallo real: tres preguntas sobre «Mi Oficina» y
     sobre `correos.es` estaban repartidas al tema 4 y remitidas a un epígrafe
     suyo que **pasaba de largo el umbral por palabras sueltas**, cuando quien
     las contesta es un epígrafe del tema 3. Las tres comprobaciones anteriores
     daban el visto bueno porque **sólo miran dentro del tema donde la pregunta
     ya está**. Ésta puntúa **todos los epígrafes de los doce temas** y canta
     cuando el mejor de otro tema **le saca bastante** al remitido: no dice que
     el remite esté mal, dice **que la pregunta puede estar en el tema
     equivocado**, que es un defecto mayor y que ninguna otra lente ve.

**Una casilla vacía no es un hallazgo**: es una pregunta que todavía no se ha
remitido, y se cuenta aparte para que se vea cuánto queda. **Una que empieza por
`!`** declara que el tema no la contesta; se comprueba que traiga motivo y no se
le busca epígrafe, porque no lo tiene.

Uso:  python3 herramientas/refutar_remites.py
"""
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
import banco_correos                                            # noqa: E402
import libro                                                    # noqa: E402

# por debajo de esto la lente pide que se mire la pregunta a mano
MINIMO = 3

# cuántas palabras de ventaja necesita un epígrafe de OTRO tema para que la
# lente sospeche que la pregunta está repartida donde no toca. Con menos, la
# ventaja es ruido: dos temas vecinos comparten vocabulario por fuerza
VENTAJA = 4

VACIAS = set("""algun alguna algunas alguno algunos ante antes aquel aquella aquello aqui asi aun
aunque bien cada casi como con contra cual cuales cuando cuanto desde donde dos ella ellas ello
ellos entre era eran esa esas ese eso esos esta estan estas este esto estos fue fueron hace hacia
han hasta las les los mas mientras mismo mucho muy nada otra otras otro otros para pero poco por
porque que quien segun ser siempre sin sobre solo son sus tal tambien tan tanto tiene tienen toda
todas todo todos tras una unas uno unos señale siguientes siguiente correcta incorrecta
afirmaciones afirmacion respuestas respuesta relacion opciones opcion cuantos cuantas entre
siguiente cual""".split())


def pela(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def fichas(s):
    return {w for w in pela(re.sub(r"[^\w\s]", " ", s)).split()
            if len(w) > 3 and w not in VACIAS}


def ficheros():
    """{'01': 'temas/correos/01-...md'} por el número con que empieza el nombre."""
    fuera = {}
    for f in sorted(os.listdir(os.path.join(RAIZ, "temas/correos"))):
        m = re.match(r"(\d\d)-", f)
        if m:
            fuera[m.group(1)] = "temas/correos/" + f
    return fuera


def cuerpos(tema, ruta):
    """{numero de epígrafe: (titulo, cuerpo con el de sus subepígrafes)}."""
    texto, _ = libro.numera(libro.lee(ruta), int(tema))
    bloques = []
    for linea in texto.split("\n"):
        m = re.match(r'^#{2,4} <a id="[^"]+"></a>([\d.]+) (.+)$', linea)
        if m:
            bloques.append([m.group(1), m.group(2), []])
        elif bloques:
            bloques[-1][2].append(linea)
    fuera = {}
    for num, tit, lineas in bloques:
        # el cuerpo de un epígrafe incluye el de los suyos: remitir al padre no
        # es impreciso cuando la respuesta está en uno de sus hijos
        propio = "\n".join(lineas)
        hijos = "\n".join("\n".join(l) for n, _, l in bloques
                          if n.startswith(num + "."))
        fuera[num] = (tit, propio + "\n" + hijos)
    return fuera


def main():
    filas = banco_correos.acta()
    rutas = ficheros()
    cache = {}
    sinremite, declarados, flojos, rotos, forasteras = [], 0, [], [], []
    comprobados = 0
    for t in sorted(rutas):
        cache[t] = cuerpos(t, rutas[t])
    vocabulario = {(t, num): fichas(cuerpo)
                   for t, mapa in cache.items() for num, (_, cuerpo) in mapa.items()}

    for base, modelo in banco_correos.MODELOS:
        ruta = os.path.join(banco_correos.DIR, "examen-%s.md" % modelo)
        for n, enun, ops, letra, _anul in banco_correos.preguntas(ruta):
            fila = filas.get((base, n))
            if fila is None or fila[0] == "--":
                continue
            tema, _motivo, epi = fila
            sig = "%s nº %d" % ("ATC" if "ATC" in base else "REP", n)
            epi = epi.strip()
            if not epi:
                sinremite.append(sig)
                continue
            if epi.startswith("!"):
                if not epi[1:].strip():
                    rotos.append((sig, "declara que el tema no la contesta y no dice por qué"))
                else:
                    declarados += 1
                continue
            mapa = cache[tema]
            comprobados += 1
            if not epi.startswith(str(int(tema)) + "."):
                rotos.append((sig, "el remite %s no es del tema %s" % (epi, tema)))
                continue
            if epi not in mapa:
                rotos.append((sig, "el epígrafe %s no existe en el tema %s" % (epi, tema)))
                continue
            correcta = next((t for L, t in ops if L == letra), "")
            clave = fichas(enun + " " + correcta)
            vistas = clave & fichas(mapa[epi][1])
            if len(vistas) < MINIMO:
                flojos.append((sig, epi, mapa[epi][0], sorted(vistas)))
            # ¿hay un epígrafe de otro tema que hable mucho más de esta pregunta?
            mejor, suyo = None, len(vistas)
            for (t, num), voc in vocabulario.items():
                if t == tema:
                    continue
                cuantas = len(clave & voc)
                if mejor is None or cuantas > mejor[2]:
                    mejor = (t, num, cuantas)
            if mejor and mejor[2] - suyo >= VENTAJA:
                forasteras.append((sig, tema, epi, suyo, mejor[0], mejor[1], mejor[2],
                                   cache[mejor[0]][mejor[1]][0]))

    print("## Remites que no se sostienen")
    if rotos:
        for sig, por in rotos:
            print("  ! %-12s %s" % (sig, por))
    else:
        print("  (ninguno)")

    print()
    print("## Remites flojos: el epígrafe existe y apenas comparte palabras con la pregunta")
    if flojos:
        for sig, epi, tit, vistas in flojos:
            print("  · %-12s %-9s %-44s %s" % (sig, epi, tit[:44], " ".join(vistas)))
    else:
        print("  (ninguno)")

    print()
    print("## Preguntas que otro tema contesta mejor que el suyo")
    if forasteras:
        for sig, tema, epi, suyo, t2, num2, cuantas, tit2 in forasteras:
            print("  ? %-12s tema %s · %-8s (%d) ←→ tema %s · %-8s (%d) %s"
                  % (sig, tema, epi, suyo, t2, num2, cuantas, tit2[:38]))
    else:
        print("  (ninguna)")

    print()
    print("remites comprobados: %d ; rotos: %d ; flojos: %d ; en otro tema: %d ; "
          "declarados sin epígrafe: %d ; sin remitir todavía: %d"
          % (comprobados, len(rotos), len(flojos), len(forasteras), declarados,
             len(sinremite)))
    return 1 if rotos else 0


if __name__ == "__main__":
    sys.exit(main())
