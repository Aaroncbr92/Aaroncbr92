#!/usr/bin/env python3
"""Refutación por prosa y forma: relleno, repeticiones y siglas sin presentar."""
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio
import unicodedata
from collections import Counter

# «en síntesis» es relleno cuando conecta y **término técnico cuando
# nombra una mezcla de colores**: la síntesis aditiva y la sustractiva son
# la materia de los temas de color, y sin la salvedad el aviso salta en
# todos ellos y **entierra el relleno que sí lo es**.
# **Conectores que una sigla no toma.** «Instituto Nacional de Seguridad y
# Salud en el Trabajo» da INSST y no INDSYSET: la sigla se forma con las
# iniciales de las palabras con contenido y salta las preposiciones y los
# artículos. Sin esta lista, la comprobación semántica de más abajo no
# reconocería ninguna presentación real.
# Lo pone `main()` al leer la línea de órdenes.
ESTRICTO = False

CONECTORES_SIGLA = {"de", "del", "la", "el", "los", "las", "y", "e", "en", "a",
                    "al", "para", "por", "con", "un", "una", "sobre", "o", "u",
                    "of", "the", "and", "for"}


def forman_sigla(texto, sigla):
    """¿Las iniciales de `texto` forman `sigla`?

    Se compara sin tildes y saltando los conectores, y basta con que la sigla
    salga **dentro** de la cadena de iniciales: el nombre largo suele venir
    precedido de texto que no forma parte de él.
    """
    palabras = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", texto)
    if not palabras:
        return False
    iniciales = "".join(quita_tildes(p)[0].upper()
                        for p in palabras if p.lower() not in CONECTORES_SIGLA)
    return bool(iniciales) and quita_tildes(sigla).upper() in iniciales


def presentada(tema, i, sigla, estricto=False):
    """¿Está presentada la sigla que empieza en la posición `i`?

    En modo normal basta con **un paréntesis en los 130 caracteres de delante**,
    que es la regla holgada de siempre. En modo estricto ese paréntesis tiene
    además que **tener algo que ver con la sigla**, que es el punto ciego que
    `PENDIENTES.md` tenía anotado: en «RIP (v1 y v2), OSPF, EIGRP» el paréntesis
    de la primera sigla daba por presentada la tercera.
    """
    antes = tema[max(0, i - 130):i]

    # Presentación por detrás: «UGT (Unión General de Trabajadores)». Hay que
    # **saltar el cierre de negrita y las comillas**, porque la forma de la casa
    # es «**UGT** (…)» y los dos asteriscos se colaban entre la sigla y el
    # paréntesis, de modo que la presentación más limpia del proyecto salía
    # marcada como ausente.
    if re.match(r"[*»\s]{0,4}\(", tema[i + len(sigla):i + len(sigla) + 8]):
        return True

    if "(" not in antes:
        return False
    if not estricto:
        return True

    # A partir de aquí, sólo el modo estricto.
    #
    # 1. La sigla va DENTRO de un paréntesis todavía abierto. Se busca
    #    recorriendo hacia atrás y **no comparando cuentas**: la ventana de 130
    #    caracteres puede haber cortado la apertura de un paréntesis anterior y
    #    dejar dentro su cierre, con lo que las cuentas cuadran y el abierto de
    #    verdad no se ve.
    prof = 0
    for c in reversed(antes):
        if c == ")":
            prof += 1
        elif c == "(":
            if prof == 0:
                return True
            prof -= 1

    cierres = list(re.finditer(r"\(([^()]*)\)", antes))
    if cierres:
        ult = cierres[-1]
        dentro = ult.group(1)
        # 2. la sigla está escrita dentro del paréntesis
        if re.search(r"\b%s\b" % re.escape(sigla), dentro):
            return True
        # 3. lo de dentro del paréntesis forma la sigla, o lo hace lo que va
        #    justo delante: «UGT (Unión General…)» y «Unión General… (UGT)»
        if forman_sigla(dentro, sigla):
            return True
        if forman_sigla(antes[max(0, ult.start() - 90):ult.start()], sigla):
            return True

    # 4. **Familia por prefijo.** Presentado «(UV)», las bandas UVA, UVB y UVC
    #    no necesitan presentación propia. Sin esta salvedad el modo estricto
    #    marca las tres en cuanto el tema nombra el ultravioleta.
    for otra in re.findall(r"\b([A-Z]{2,6})\b", antes):
        if otra != sigla and len(otra) >= 2 and sigla.startswith(otra):
            return True

    # 5. **Enumeración de siglas.** «Las puertas lógicas —AND, OR, NOT, NAND—»
    #    presenta la lista entera por su encabezamiento. Si entre esta sigla y
    #    otra anterior sólo hay separadores de lista, va presentada con ella.
    cola = re.sub(r"[*«»_`]", "", antes).rstrip()
    if re.search(r"\b[A-Z]{2,6}\b\s*(?:,|;|—|-|\s+y|\s+e|\s+o|\s+u)\s*$", cola):
        return True

    return False


RELLENO = [r"como hemos visto", r"como ya se ha dicho",
           r"en s[íi]ntesis(?!\s+(aditiva|sustractiva|substractiva|crom[áa]tica))",
           r"cabe destacar", r"es importante se[ñn]alar", r"conviene recordar",
           r"en definitiva", r"por [úu]ltimo,? cabe", r"no hay que olvidar",
           r"resulta evidente", r"a modo de resumen", r"dicho esto"]


def quita_tildes(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").upper()


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def main():
    # **`--siglas-estrictas` no cuenta como hallazgo, y es a propósito.** La
    # regla estricta deja unos ciento noventa avisos sobre el corpus entero y
    # **la mayoría son marcas y modelos** —XDCAM, XLR, LEMO, AKG, BNC— que no
    # son siglas de nada. Contarlos convertiría la lente en una que nadie corre
    # (manual, apartado 10). Va como modo opcional para auditar las siglas de un
    # volumen nuevo, donde la lista sí es corta y se repasa a ojo.
    global ESTRICTO
    argv = [a for a in sys.argv if a != "--siglas-estrictas"]
    ESTRICTO = len(argv) != len(sys.argv)
    sys.argv = argv
    # fuera la portada y el índice: son envoltorio, no afirmaciones del tema
    tema = sin_envoltorio(open(sys.argv[1], encoding="utf-8").read())
    # **Un esquema se mira contra su tema.** El esquema es un telegrama y su
    # estilo son los rótulos en mayúsculas —«LA REGLA QUE LO ORDENA TODO»—, de
    # modo que la salvedad de «la palabra que también sale en minúscula no es
    # sigla» no le sirve: en un texto tan corto la palabra puede no salir
    # nunca en minúscula aunque sea castellana corriente. El tema del que el
    # esquema resume dice esas mismas palabras en prosa normal, así que se le
    # presta su vocabulario. Sin esto la lente devuelve decenas de avisos que
    # no son siglas y **entierra los que sí lo son** (manual, apartado 10),
    # que es el único motivo por el que se mira la lista.
    gemelo = ""
    ruta = os.path.abspath(sys.argv[1])
    if os.sep + "esquemas" + os.sep in ruta:
        par = ruta.replace(os.sep + "esquemas" + os.sep, os.sep + "temas" + os.sep, 1)
        if os.path.exists(par):
            gemelo = sin_envoltorio(open(par, encoding="utf-8").read())
    hallazgos = 0

    print("## Tejido conectivo y relleno")
    # **el relleno que está dentro de una cita literal no es relleno del tema:
    # es de la norma citada**, y quitarlo sería dejar de citar. El artículo 2
    # del Real Decreto 299/2016 dice «en definitiva, podrían suponer riesgos
    # para la seguridad», y sin esta salvedad la lente pide corregir el BOE.
    # Se anulan los renglones de cita —los que empiezan por «>»— sustituyéndolos
    # por espacios, para no mover las posiciones del resto.
    sin_citas = "\n".join(" " * len(l) if l.lstrip().startswith(">") else l
                          for l in tema.splitlines())
    # **Una muletilla ENTRECOMILLADA se está citando, no usando.** Los informes
    # del proyecto nombran las expresiones que esta misma lente busca —«como
    # hemos visto», «en síntesis»— para explicar qué mira, y sin esta salvedad
    # la lente se marca a sí misma: el documento que la documenta no la pasa.
    # Es el mismo criterio que ya se aplica a las frases repetidas y a las
    # citas en bloque. Se sustituye por espacios para no mover posiciones.
    sin_citas = re.sub(r"«[^»]{0,120}»",
                       lambda m: " " * len(m.group(0)), sin_citas)
    for pat in RELLENO:
        for m in re.finditer(pat, sin_citas, re.I):
            print("  · %s" % re.sub(r"\s+", " ", tema[max(0, m.start()-60):m.end()+60]))
            hallazgos += 1
    print("  (ninguno)" if not hallazgos else "")

    print()
    print("## Frases repetidas entre epígrafes")
    # una frase que se repite **dentro de comillas latinas las dos veces** no
    # es relleno del tema: es la fuente que se repite a sí misma. La
    # Constitución dice de los partidos y de los sindicatos, con las mismas
    # palabras, que «su estructura interna y funcionamiento deberán ser
    # democráticos», y recortar una de las dos citas para callar el aviso
    # sería recortar la norma. Se miran sólo los trozos que quedan fuera de
    # las comillas.
    def fuera_de_comillas(texto):
        # ni los renglones citados con «>» ni los rótulos de epígrafe son prosa
        # del tema: el enunciado de la convocatoria se transcribe una vez por
        # ocupación cuando el tema sirve a varias, y el título de un epígrafe
        # vuelve a salir en su encabezado. Contarlos como repetición es contar
        # dos veces lo mismo.
        texto = "\n".join(l for l in texto.splitlines()
                          if not l.lstrip().startswith((">", "#")))
        return re.sub(r"«[^»]*»", " ", texto)
    frases = [limpia(f) for f in re.split(r"(?<=[.;:])\s", fuera_de_comillas(tema))]
    frases = [f for f in frases if len(f.split()) >= 8]
    repes = [(f, c) for f, c in Counter(frases).items() if c > 1]
    for f, c in sorted(repes, key=lambda x: -x[1]):
        print("  · x%d  %s" % (c, f[:120]))
        hallazgos += 1
    if not repes:
        print("  (ninguna)")

    print()
    print("## Siglas sin presentar la primera vez"
          + (" (modo estricto: NO cuenta como hallazgo)" if ESTRICTO else ""))
    # Lo que va entre acentos graves no es prosa: es código, un nombre de
    # función, un identificador. Un tema de hoja de cálculo lo tiene a
    # docenas —`BUSCARV`, `SUMAR.SI`, `#¡DIV/0!`— y todos ellos van en
    # mayúsculas, así que sin excluirlos la lista de siglas sale llena de
    # avisos que no son siglas y **entierra los que sí lo son**, que es el
    # único motivo por el que se mira esta lista. Se sustituye por espacios
    # en lugar de borrarse para no juntar palabras vecinas.
    tema = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), tema)
    # los números romanos de los títulos no son siglas
    ROMANOS = re.compile(r"^[IVXLC]+$")
    CONOCIDAS = ("BOE", "RTVE", "TVE", "RNE", "PDF", "HTML", "URL", "TV")
    # palabras escritas en mayúsculas que no son siglas. Unas son castellanas
    # y van en mayúsculas por énfasis —el examen las usa a docenas: «¿Cuál NO
    # es válido?»—; otras son palabras inglesas que el oficio escribe así
    # aunque no abrevien nada: RAW es «crudo», LOG es «logarítmico».
    PALABRAS = ("NO", "SI", "UNA", "UNO", "TODO", "TODAS", "SOLO", "NUNCA",
                "SIEMPRE", "MENOS", "MAS", "CIERTA", "FALSA",
                "ANUAL", "SALVO", "ANTES", "DESPUES", "MENOR", "MAYOR",
                "TRES", "DOS", "ES", "PUEDE", "SOLAMENTE",
                # más palabras castellanas que los temas escriben en
                # mayúsculas por énfasis. Sin ellas la lista de siglas se
                # llena de avisos que no lo son y **entierra los que sí**,
                # que es el único motivo de mirarla (manual, apartado 10)
                "BAJO", "BUENA", "BUENO", "DE", "LA", "EL", "MISMA", "MISMO",
                "PASO", "REDUCE", "SIN", "TRAMPA", "CON", "COLOR", "TONO",
                "AFECTA", "PRODUCE", "CONSIGUE", "MEZCLA", "SIEMPRE", "NADA",
                "TODOS", "TODO", "UNICA", "UNICO", "DENTRO", "FUERA",
                "ANCHO", "ALTO", "LARGO", "CORTO", "MAS", "MENOS", "IGUAL",
                "SOLO", "CUANDO", "DONDE", "COMO", "QUE",
                "CORTA", "CORTO", "EN", "FILTRO", "MEJOR", "MUY", "PUESTA",
                "SON", "TIEMPO", "TIPO", "UN", "SI", "NI", "AL", "SU",
                "GEOMETRIA", "ANTES", "AHORA", "AQUI", "ESE", "ESTA",
                # y las que los **esquemas** ponen en mayúsculas por ser su
                # estilo: el telegrama rotula cada línea —«LA REGLA QUE LO
                # ORDENA TODO», «AVISO DE ESTUDIO»— y esas palabras son
                # castellano corriente. Sin ellas la lista de siglas de un
                # esquema sale llena de avisos que no lo son y **entierra
                # los que sí**, que es el único motivo de mirarla
                "AJUSTE", "AMIGO", "APORTA", "AVISO", "AYUDA", "BUSCA", "CARO",
                "CLAVE", "CRUZA", "CUENTA", "DECIDE", "DICEN", "DOBLE", "ERROR",
                "ESCALA", "FALSO", "FIJA", "FIJAN", "FONDO", "FRASE", "FRENTE",
                "GENERA", "IDEA", "JUNTOS", "LLEVAR", "MAL", "MARCA", "MARGEN",
                "METEN", "MIENTE", "OFICIO", "OJO", "OLVIDA", "ORDENA", "ORO",
                "PESAN", "PIEZA", "PUENTE", "QUEDAN", "RASGOS", "RAZONA", "REAL",
                "REALES", "REGLA", "RESIDE", "SABER", "SALEN", "SOBRA", "SONORA",
                "ENLAZA", "MUERDE", "OYE", "CUESTA", "CAMBIA", "DEPENDE", "DECIDEN",
                "SIRVE", "SIRVEN", "APARECE", "APARECEN", "EXIGE", "EXIGEN", "MIDE",
                "MIDEN", "SUENA", "SUENAN", "TOCA", "PIDE", "PIDEN", "ABRE",
                "CIERRA", "SUBE", "BAJA", "ENTRA", "SALE", "LLEGA", "QUEDA",
                "IMPORTA", "AHORRA", "PIERDE", "GANA", "JUNTA", "SEPARA", "RESUELVE",
                "AVISA", "TRADUCE",
                "SUELO", "TABLA", "VALE", "VEN", "VERDAD", "VIENE", "VIVA",
                "COSA", "USA", "EXACTA", "FALSAS", "SUB", "NEAR",
                "DEL", "PASIVA", "ACTIVA", "PASIVO", "ACTIVO", "LOS", "LAS",
                "UNA", "MAYOR", "MENOR", "IGUALES", "DISTINTO", "DISTINTA",
                "UMBRAL", "UNIDAD", "GRUPO", "BANDA", "CANAL", "NIVEL",
                "AUDICION", "MINIMO", "MAXIMO", "CUADERNILLO", "AUDIO",
                "VIDEO", "IMAGEN", "SONIDO", "SENAL", "OIDO", "EQUIPO",
                "OTRO", "OTRA", "OTROS", "OTRAS", "SUMA", "RESTA", "ALTA",
                "ALTO", "BAJA", "COLOR", "DURA", "DIFUSA", "PEQUENO",
                "GRANDE", "DEMASIADA", "DOS", "CUATRO", "CINCO", "SEIS",
                "OSCURO", "OSCURA", "CLARO", "CLARA", "CERCA", "LEJOS",
                "ZONAS", "ZONA", "SOMBRAS", "LUCES", "BORDES", "NEGRO",
                "BLANCO", "GANANCIA", "RUIDO", "PASOS", "MITAD", "MEDIA",
                "PLANO", "SE", "ESCENA", "SECUENCIA", "CORTE", "TOMA",
                "EJE", "ANGULO", "TIEMPO", "ESPACIO", "LUGAR", "SENTIDO",
                "TOMAS", "VA", "VAN", "HAY", "SON", "ERA", "FUE", "SEA",
                "RAW", "LOG", "LUT", "MIX")
    # rótulos de botones y de menús, tal como están serigrafiados en el
    # aparato. No abrevian nada: son el nombre que el operador lee y pulsa, y
    # el tema los escribe en mayúsculas justamente para que se reconozcan en
    # el panel. Y nombres de marca y de modelo, que tampoco son siglas.
    ROTULOS = ("CUT", "AUTO", "WIPE", "NAM", "FAM", "CLEAN", "EDIT", "PREVIO",
               "SHOW", "KEY", "FILL", "SIZE", "CROP", "MENU", "PGM", "PVW",
               "ATEM", "MOTU", "XVS", "AV", "HS",
               # órdenes y rótulos de los programas de edición y de los
               # mandos de repetición, que el examen escribe en mayúsculas
               # porque así están rotulados. Tampoco abrevian nada
               "MATCH", "FRAME", "AUDIO", "MIXER", "SET", "PAN", "LEVEL",
               "GLOBAL", "IN", "OUT", "EQ", "TAKE", "PRV", "CAM", "AUX",
               "LINK", "GANG", "TWICE", "DUAL", "PLAYLIST", "TIMELINE",
               "TBAR", "VGA", "VDR", "REC", "MODE",
               # rótulos de la rueda de filtros y del anillo de zoom de una
               # cámara, y sufijos de referencia de objetivo: tampoco
               # abrevian nada
               "CLEAR", "TELE", "BERD", "IE", "ND", "PL", "EF", "B4",
               "STRETCH", "STRECH", "GAMMA", "BLACK", "LEVEL", "DEPEND",
               "FREQUENCY", "KNEE", "FRENCH", "FLAG")
    # «SI(C2 = 1» no es una sigla: es una llamada a función. Un paréntesis
    # pegado al nombre lo delata, y sin esta salvedad un tema de hoja de
    # cálculo llena la lista de falsos avisos aunque el nombre vaya dentro de
    # una cita literal, donde no se le pueden poner acentos graves sin tocar
    # la cita.
    llamadas = set(re.findall(r"\b([A-Z]{2,6})\(", tema))
    # «CC.AA.» y «NO-DO» son una sola abreviatura, no dos. Con `\b` a secas la
    # lente las parte y avisa de «AA» y de «DO», que no son siglas de nada y
    # **entierran los avisos que sí lo son**. Se descartan los trozos que sólo
    # aparecen pegados a otro grupo de mayúsculas por un punto o un guion.
    trozos = set()
    for m in re.finditer(r"\b[A-Z]{2,6}(?:[.-][A-Z]{2,6})+\.?", tema):
        partes = re.findall(r"[A-Z]{2,6}", m.group(0))
        trozos.update(partes)
    enteras = set(re.findall(r"(?<![A-Z.-])\b([A-Z]{2,6})\b(?![.-][A-Z])", tema))
    # una palabra que en el mismo tema aparece también en minúscula o
    # capitalizada **no es una sigla**: es la misma palabra puesta en
    # mayúsculas por énfasis. El examen y los temas de este proyecto lo hacen
    # a docenas —«la CUARTA pared», «lo que VIENEN después»— y sin esta
    # salvedad la lista de siglas se llena de castellano y **entierra los
    # avisos que sí lo son**, que es el único motivo por el que se mira.
    # Una sigla de verdad —SMPTE, RAID, OETF— no sale nunca en minúscula.
    minusculas = set()
    for m in re.finditer(r"\b([A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,6})\b", tema + " " + gemelo):
        pal = m.group(1)
        if pal.isupper():
            continue
        minusculas.add(quita_tildes(pal).upper())
    # **lo que el tema no nombra, el esquema no puede presentar.** El esquema
    # resume su tema: una sigla de la materia sale en los dos. Una palabra en
    # mayúsculas que **no aparece en el tema de ninguna forma** —ni en
    # mayúsculas ni en minúsculas— es un rótulo del telegrama, castellano
    # puesto en mayúsculas por estilo: «QUÉ PASA SI NO SE CRUZAN», «EL PRECIO».
    # Avisar de esas **entierra las siglas que sí lo son** (manual, apartado
    # 10). La salvedad sólo vale cuando hay tema gemelo, es decir, sólo para
    # los esquemas: en un tema no hay contra qué contrastar y se mira todo.
    del_tema = set()
    if gemelo:
        for m in re.finditer(r"\b([A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,6})\b", gemelo):
            del_tema.add(quita_tildes(m.group(1)))
    for sigla in sorted(set(re.findall(r"\b([A-Z]{2,6})\b", tema))):
        if quita_tildes(sigla) in minusculas:
            continue
        if gemelo and quita_tildes(sigla) not in del_tema:
            continue
        if sigla in trozos and sigla not in enteras:
            continue
        if ROMANOS.match(sigla) or sigla in CONOCIDAS or sigla in llamadas:
            continue
        if sigla in PALABRAS or sigla in ROTULOS:
            continue
        # «BT.601-7», «EN 300 744», «ST 2110»: la serie de una norma no es una
        # sigla que el tema tenga que presentar, es la mitad de su nombre. Se
        # reconoce porque **todas** sus apariciones llevan pegado un número.
        apariciones = list(re.finditer(r"\b%s\b" % re.escape(sigla), tema))
        if apariciones and all(
                re.match(r"[.\s-]\s?\d", tema[m.end():m.end() + 3] or " ")
                for m in apariciones):
            continue
        # una sigla que sólo sale dentro de una cita literal no es del tema:
        # es de la fuente citada, y no se le puede meter la presentación
        # dentro de las comillas sin dejar de ser literal.
        lineas = tema.splitlines()
        fuera_de_cita = [l for l in lineas
                         if re.search(r"\b%s\b" % re.escape(sigla), l)
                         and not l.lstrip().startswith(">")]
        if apariciones and not fuera_de_cita:
            continue
        # buscar la sigla como palabra, no como trozo: `find` la encuentra dentro
        # de otra palabra —«RD» dentro de «BORDER», «SI» dentro de «MÚSICA»— y
        # entonces se comprueba la presentación en un sitio del tema donde la
        # sigla no está, de modo que un aviso correcto se vuelve incorregible
        m = re.search(r"\b%s\b" % re.escape(sigla), tema)
        i = m.start() if m else -1
        # «Directiva 2007/65/CE» no es una sigla del tema: es el nombre de la norma
        while i > 0 and tema[i - 1] == "/":
            m = re.search(r"\b%s\b" % re.escape(sigla), tema[i + 1:])
            i = i + 1 + m.start() if m else -1
        if i < 0:
            continue
        antes = tema[max(0, i - 130):i]
        if not presentada(tema, i, sigla, ESTRICTO):
            print("  · %-6s primera aparición: ...%s%s..."
                  % (sigla, re.sub(r"\s+", " ", antes[-70:]), sigla))
            if not ESTRICTO:
                hallazgos += 1

    # **Negritas rotas y negritas anidadas.** Ninguna otra lente mira cómo se
    # RENDERIZA el texto, y hay un defecto que sólo se ve al renderizarlo:
    # sustituir una palabra en mayúsculas por la misma en negrita, dentro de un
    # párrafo que ya iba entero en negrita, produce `**texto **palabra**
    # texto**`. El formato no sabe representar eso y **invierte el énfasis**:
    # sale en redonda justo lo que se quería destacar. Se descubrió reparando en
    # bloque el énfasis por mayúsculas y **se reparaban ochenta y seis
    # apariciones a mano**, así que la comprobación vive aquí desde entonces.
    #
    # Cómo se detecta, y por qué así: se parte cada párrafo por `**`, de modo
    # que **los índices impares son los tramos en negrita**. Un tramo que
    # empieza o acaba con espacio o con salto de línea no es una negrita: es el
    # hueco entre dos cierres mal emparejados. Y un número PAR de asteriscos
    # dobles en un párrafo significa que uno se quedó sin pareja.
    #
    # Se mira sobre el fichero entero y no sobre `tema`, porque la portada y el
    # índice también se renderizan.
    crudo = open(sys.argv[1], encoding="utf-8").read()
    # **Lo que va entre acentos graves NO se renderiza como negrita**, y este
    # proyecto escribe dentro de ellos justamente el ejemplo del defecto que se
    # busca: `**texto **palabra** texto**`. Sin esta salvedad, el informe que
    # explica el fallo se marca a sí mismo.
    #
    # Se neutralizan **sólo los asteriscos** de dentro, y no el tramo entero:
    # borrar el tramo dejaría un hueco pegado a la negrita vecina —«**`banco.py`
    # avisa de X**» pasaría a empezar por espacios— y **la lente se llenaría de
    # anidamientos que no existen**, que es el fallo que esta comprobación
    # existe para no cometer.
    crudo = re.sub(r"`[^`\n]*`",
                   lambda m: m.group(0).replace("*", "\u2217"), crudo)
    rotas = []
    for parrafo in crudo.split("\n\n"):
        trozos = parrafo.split("**")
        if len(trozos) % 2 == 0:
            rotas.append(("paridad", re.sub(r"\s+", " ", parrafo)[:70]))
            continue
        for k in range(1, len(trozos), 2):
            tramo = trozos[k]
            if tramo[:1] in " \n" or tramo[-1:] in " \n":
                rotas.append(("anidada", re.sub(r"\s+", " ", tramo)[:70]))
    print()
    print("## Negritas rotas o anidadas")
    if not rotas:
        print("  (ninguna)")
    for clase, muestra in rotas:
        print("  · %-8s %s" % (clase, muestra))
        hallazgos += 1

    print()
    print("hallazgos de prosa: %d" % hallazgos)


if __name__ == "__main__":
    main()
