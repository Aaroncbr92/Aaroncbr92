#!/usr/bin/env python3
"""Caza las cifras imposibles que el reconocedor mete en el volcado de Correos.

**El problema que resuelve, y es el peor de todo este volumen.** La tipografía del
documento de referencia dibuja el **9 con el cuello recto**, y `tesseract` lo lee
como un **4**. Así, «Directiva 97/67/CE, de 1997» sale del volcado como «Directiva
47/67/CE, de 1447», y «Ley 9/2017» como «Ley 94/2017».

**Ninguna de las cinco lentes del proyecto puede ver eso.** `refutar_documento`
comprueba que cada cifra del tema aparezca en la fuente; si el tema copia «1447» del
volcado, la cifra **está** en la fuente y la lente da el visto bueno. **La fuente
corrupta valida la copia corrupta.** Es el fallo que no da error del apartado 10 del
manual, en su forma más pura.

**Lo que hace esta herramienta.** Recorre el volcado y señala toda cifra que no puede
existir: un año fuera de un rango razonable, y una referencia de norma «N/AAAA» cuyo
año no es un año. No corrige nada —**corregir a ciegas sería cambiar un invento por
otro**—: imprime la cifra con su página y su renglón **para ir a mirarla a la
página original**, que es la única comprobación que vale.

**No lo caza todo, y hay que saberlo.** Un «1964» leído como «1464» lo caza, porque
1464 cae fuera de rango. Un «1999» leído como «1949» **no**, porque 1949 es un año
posible. Esta herramienta quita las imposibles; **las verosímiles siguen exigiendo
leer la página.** Y tampoco caza lo que es un número corriente mal leído: el tema 2
decía **«164 metas»** donde el documento imprime **169**, y 164 es un número posible.
Eso sólo lo caza saber el dato.

Uso:
    python3 herramientas/correos_cifras.py fuentes/correos-referencia/tema-*.txt
"""
import re
import sys

# **Dos rangos, y hacen falta los dos.** Una NORMA española citada por este
# documento es moderna: ningún «N/AAAA» tiene un año anterior al siglo XIX.
# Un AÑO suelto, en cambio, puede ser antiguo de verdad: el tema 1 cuenta la
# historia del correo y menciona **1505**, cuando se nombró al primer Correo
# Mayor. Poner el suelo en 1700 marcaba ese 1505 como imposible, que es
# justamente el falso positivo que enseña a no leer la lista.
PRIMER_ANO_NORMA = 1800
PRIMER_ANO_SUELTO = 1400
ULTIMO_ANO = 2030


def revisa(fichero):
    pagina = "?"
    hallazgos = []
    for n, linea in enumerate(open(fichero, encoding="utf-8"), 1):
        m = re.match(r"\[\[ página (\d+) de", linea)
        if m:
            pagina = m.group(1)
            continue
        # referencias de norma: «Ley 9/2017», «Real Decreto 1829/1999»
        for mm in re.finditer(r"\b(\d{1,4})/(\d{4})\b", linea):
            # **Un reglamento europeo se numera al revés que una ley española**:
            # «Reglamento (UE) 2018/1108» es año/número, no número/año. Sin esta
            # salvedad la herramienta marca como imposible toda la normativa
            # comunitaria, que es justo el ruido que enseña a no leer la lista.
            if 1950 <= int(mm.group(1)) <= ULTIMO_ANO:
                continue
            ano = int(mm.group(2))
            if not (PRIMER_ANO_NORMA <= ano <= ULTIMO_ANO):
                hallazgos.append((pagina, n, mm.group(0), "el año de la norma no es un año"))
        # **Años sueltos, vengan como vengan.** La primera versión de esta
        # herramienta sólo miraba «de AAAA», y por ese hueco se colaron en el
        # tema 2 «no se constituyó hasta 1478» y «el Estatuto de los Trabajadores
        # en el año 1480». El año no siempre lleva delante la preposición.
        for mm in re.finditer(r"(?<![\d/])(\d{4})(?![\d/])", linea):
            ano = int(mm.group(1))
            if not (PRIMER_ANO_SUELTO <= ano <= ULTIMO_ANO):
                hallazgos.append((pagina, n, mm.group(0), "año imposible"))
            elif ano < 1800:
                hallazgos.append((pagina, n, mm.group(0),
                                  "podría ser histórico de verdad: comprobar"))
        # **Un cuatro de más.** El reconocedor no sólo confunde el nueve con el
        # cuatro: a veces **añade** un cuatro y deja el nueve. Así «1 de enero de
        # 1986» salió del volcado como «14986». Un año no tiene cinco cifras, y
        # si al quitarle un cuatro queda un año moderno, es este defecto.
        for mm in re.finditer(r"(?<![\d/])(\d{5})(?![\d/])", linea):
            bruto = mm.group(1)
            if "4" not in bruto:
                continue
            for i, c in enumerate(bruto):
                if c != "4":
                    continue
                resto = bruto[:i] + bruto[i + 1:]
                if 1900 <= int(resto) <= ULTIMO_ANO:
                    hallazgos.append((pagina, n, bruto,
                                      "cinco cifras: ¿%s con un cuatro de más?" % resto))
                    break
    return hallazgos


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = 0
    for f in sys.argv[1:]:
        h = revisa(f)
        if not h:
            continue
        print("== %s" % f.split("/")[-1])
        for pagina, linea, texto, por_que in h:
            print("   pág %-4s renglón %-6d %-22s %s" % (pagina, linea, texto, por_que))
        total += len(h)
    print("\ncifras imposibles: %d" % total)


if __name__ == "__main__":
    main()
