#!/usr/bin/env python3
"""Arma el bloque general en un volumen imprimible.

Un tema en pantalla y un tema impreso no se ordenan igual. En pantalla se salta
con el índice; en papel hay que decidir un orden y sostenerlo. El de aquí:

  1. Portada del volumen y aviso de uso, con la **fecha de corte** delante,
     porque es lo que decide qué redacción vale.
  2. Índice general.
  3. Cada tema, en el **orden del programa oficial** —no en el orden en que se
     escribieron—, y dentro de cada uno: **ficha, índice, cuerpo, esquema y
     preguntas reales**. El esquema **detrás** del cuerpo y no delante: es para
     repasar, y puesto antes invita a leer el esqueleto y saltarse la carne.
  4. Las **respuestas, al final del volumen**. Si van junto a la pregunta no hay
     autoevaluación posible; y separadas caben las advertencias sobre las
     plantillas oficiales que están mal, que en la misma página serían ruido.

El mismo armazón sirve para los cuatro bloques —el general y los específicos de
Producción (Asistencia), Documentación e Información y Contenidos—, que se
diferencian en qué temas llevan, de qué carpeta salen y qué avisos hay que
imprimir con las respuestas. Todo eso está en
`BLOQUES`, y **no se duplica el código**: un volumen escrito dos veces se
desincroniza a la primera corrección.

Uso:  libro.py <bloque> [salida.html]
      El bloque es una clave de BLOQUES: general, produccion-asistencia,
      gestion-administrativa, gestion, realizacion, documentacion, informacion.
      python3 herramientas/libro.py general     && python3 herramientas/pdf.py libro-general.html
      python3 herramientas/libro.py informacion && python3 herramientas/pdf.py libro-informacion.html
"""
import glob
import html
import os
import re
import sys
from datetime import date

from markdown_it import MarkdownIt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORTE = "21 de diciembre de 2022"

# Los cuatro bloques. Cada uno dice **de dónde salen sus temas**, **cómo se
# presenta el volumen** y **qué avisos van con las respuestas**. Cuando entre
# otra ocupación tipo, se añade una entrada aquí y no se toca nada más —los tres
# específicos que hay se dieron de alta así, sin tocar el armazón—.
#
# Un tema **puede no tener banco**: en Información y Contenidos, el del Real
# Decreto-ley 4/2018 y el de la Carta ética de la FIP no tienen ni una pregunta
# de examen. Se escribe `None` y el volumen los imprime sin juego, igual que el
# tema 2 del general, que comparte el suyo con el 3.
#
# En el general, los temas 2 y 3 comparten banco de preguntas, así que el juego
# va detrás del 3, que es el corto y el que depende del 2.
#
# «avisos» recoge lo que hay que imprimir junto a la respuesta de una pregunta
# concreta. En el general son **erratas de la plantilla oficial**: respuestas
# dadas por buenas que la norma desmiente. En el específico no hay ninguna
# errata de respuesta, pero sí **enunciados defectuosos**, que engañan igual y
# se avisan igual. Un volumen que copia la plantilla sin avisar enseña mal justo
# lo que el opositor va a memorizar.

ERRATAS_GENERAL = {
    "81_preguntas_produccion · nº 32":
        "La plantilla da <b>b) Título segundo</b>. Es <b>a) Título primero</b>: los derechos y "
        "deberes fundamentales son el Título I (arts. 10 a 55); el Título II es el de la Corona.",
    "77_preguntas_produccion_asist · nº 51":
        "La plantilla da <b>a) Tres</b>. Son <b>b) Dos</b>: los tres los designa el Consejo "
        "Económico y Social (art. 23.2 de la Ley 17/2006).",
    "62_preguntas_realizacion_asist_2_llamamiento · nº 77":
        "La plantilla da <b>c) 4</b>. Son <b>b) 3</b>: el art. 35.2 de la Ley 31/1995 asigna "
        "3 Delegados de 101 a 500 trabajadores; el 4 es el tramo de 501 a 1.000.",
}

AVISOS_PRODUCCION_ASISTENCIA = {
    "77_preguntas_produccion_asist · nº 78":
        "<b>El enunciado tiene los términos invertidos.</b> Pide la tecnología de «superponer una "
        "imagen real sobre el entorno virtual», y la realidad aumentada superpone <b>lo virtual "
        "sobre lo real</b>. La respuesta oficial es la única posible entre las cuatro opciones; "
        "quien intente razonar el enunciado al pie de la letra se bloquea.",
    "78_preguntas_produccion_asist_2_llamamiento · nº 29":
        "<b>El enunciado mezcla cine y televisión.</b> Pide lo que «la DCI 4K estandariza para "
        "televisión», y la iniciativa de cine digital estandariza <b>cine</b>: su 4K es "
        "<b>4 096 × 2 160</b>. El 4K de televisión es <b>3 840 × 2 160</b>, que es lo que el "
        "propio enunciado remata pidiendo, «en UHD 16:9».",
    "77_preguntas_produccion_asist · nº 61":
        "<b>El distractor c) no es falso.</b> La Recomendación UIT-R BT.2100-1 incluye <b>24</b> "
        "y 24/1,001 entre sus frecuencias de trama de televisión. Lo que decide la pregunta es la "
        "palabra <b>«tradicionalmente»</b>: las 24 imágenes por segundo vienen del cine "
        "fotoquímico.",
    "77_preguntas_produccion_asist · nº 81":
        "<b>El enunciado fecha mal una ley y cita otra derogada.</b> La ley de televisión privada "
        "es la <b>Ley 10/1988, de 3 de mayo</b> —el día y el mes del enunciado coinciden; el año, "
        "no—; y la <b>Ley 7/2010</b> está derogada por la disposición derogatoria única de la "
        "Ley 13/2022.",
    "77_preguntas_produccion_asist · nº 44":
        "<b>La opción correcta dice «marca comercial alemana».</b> Lo alemán está comprobado: el "
        "informe de ensayo de seguridad fotobiológica del Titan Tube identifica al solicitante "
        "como <b>Astera LED Technology GmbH, de Múnich</b>.",
}

AVISOS_DOCUMENTACION = {
    "09_preguntas_documentacion · nº 11":
        "<b>La opción correcta empieza un día tarde.</b> El Real Decreto 1673/2010 se publicó en el "
        "«BOE» núm. 295, de <b>4 de diciembre de 2010</b>, y entró en vigor «en el instante de su "
        "publicación»: el estado de alarma corrió desde <b>el 4</b>, no desde el 5. La fecha final "
        "sí es literal —el Real Decreto 1717/2010 lo prorroga «hasta las 24 horas del día 15 de "
        "enero de 2011»—, y la opción sigue siendo la única posible de las cuatro.",
    "09_preguntas_documentacion · nº 47":
        "<b>El enunciado desarrolla las siglas y la norma no.</b> La norma ECMA-319, que es la que "
        "define el formato, se titula «Data Interchange on 12,7 mm 384-Track <b>Magnetic Tape "
        "Cartridges</b> – Ultrium-1 Format» y usa las siglas sin explicarlas. El desarrollo entre "
        "paréntesis es del tribunal; lo que la norma sí dice es que es <b>cinta magnética</b>.",
}


AVISOS_INFORMACION = {
    "31_preguntas_iyc · nº 77":
        "<b>La respuesta oficial y el INE no dicen lo mismo.</b> La plantilla da <b>11,4 %</b>; la "
        "nota de prensa de la EPA del segundo trimestre de 2024, de 26 de julio, publica "
        "<b>11,27 %</b>, y se comprueba sola: «11,27 % este trimestre, 1,02 puntos menos que en el "
        "anterior», y 11,27 + 1,02 = 12,29, la tasa del primer trimestre. <b>De las cuatro "
        "opciones, la de la plantilla sigue siendo la única cercana</b>; el temario enseña la "
        "cifra del INE y deja dicho que la oficial es otra.",
    "33_preguntas_iyc_2_llamamiento · nº 6":
        "<b>El enunciado nombra mal el organismo.</b> Dice «Centro de Investigaciones Científicas "
        "(CIS)». El CIS es el <b>Centro de Investigaciones Sociológicas</b>; el de Investigaciones "
        "Científicas es el <b>CSIC</b>, otro organismo con otra adscripción. No cambia la "
        "respuesta —las siglas sólo pueden ser el Sociológico—.",
    "31_preguntas_iyc · nº 20":
        "<b>El enunciado llama al documento por el título de otro.</b> Dice «Código de "
        "Autorregulación sobre contenidos televisivos e infancia», que es el <b>acuerdo sectorial "
        "de 9 de diciembre de 2004</b>. El documento del Anexo 2 es el <b>de RTVE, de 23 de julio "
        "de 2010</b>, que cita a aquél como «el más directo precedente de las presentes normas». "
        "<b>La respuesta no depende de cuál se lea</b>: la cifra está en el de RTVE con esas "
        "mismas palabras.",
    "31_preguntas_iyc · nº 57":
        "<b>Mismo defecto que en la otra pregunta del tema</b>: el enunciado usa el título del "
        "acuerdo sectorial de 2004 para preguntar por el código de RTVE de 2010. La respuesta se "
        "verifica en el documento que el programa manda estudiar.",
    "33_preguntas_iyc_2_llamamiento · nº 63":
        "<b>La cifra de la respuesta no está en la directiva</b>, y el programa la fecha mal. La "
        "norma dice <b>20 % del período</b>; los 144 minutos son esa proporción sobre doce horas, "
        "así que quien busque «144» en el texto no lo encontrará. Y el Anexo 2 fecha la directiva "
        "el <b>28 de noviembre de 2018</b>, que es la fecha del <b>Diario Oficial</b>: la "
        "directiva es de <b>14 de noviembre</b>.",
    "33_preguntas_iyc_2_llamamiento · nº 82":
        "<b>La respuesta era correcta en 2024 y hoy no lo sería.</b> La plantilla da <b>siete</b> "
        "países de la Unión sin el euro, y así era cuando se examinó; <b>la página oficial de hoy "
        "dice seis</b>, porque la zona del euro ha crecido desde entonces. Se estudia la de 2024 "
        "y se sabe por qué cambia.",
}


# El tema de prevención lo comparten las tres ocupaciones, así que su aviso
# también. Se escribe una vez y se mezcla en los tres bloques: escrito tres veces,
# a la primera corrección habría tres redacciones distintas del mismo aviso.
# Y el tema es uno solo, aunque el programa le ponga tres números: es el 18 de
# Producción, el 7 de Documentación y el 11 de Información y Contenidos. Vive en
# `temas/prl/`, fuera de las tres carpetas, y por eso lleva la suya escrita
# delante: un tema con «/» en el nombre trae su carpeta puesta, y los demás salen
# de la del bloque. Tres copias del mismo fichero se habrían separado a la primera
# corrección.
TEMA_PRL = ("prl/prl-especifico", "prl-especifico")

AVISOS_PRODUCCION = {
    "81_preguntas_produccion · nº 88":
        "<b>Ninguna de las cuatro opciones es correcta.</b> La plantilla da la <b>d)</b> "
        "—informar solo por encima del <b>30 %</b> y obtener <b>siempre</b> aprobación "
        "expresa—, y la ley que la propia pregunta cita dice lo contrario en sus dos mitades. "
        "El <b>artículo 215.2.b) de la Ley 9/2017</b> obliga a que <b>«en todo caso, el "
        "contratista deberá comunicar por escrito»</b> su intención de subcontratar, "
        "<b>sin umbral alguno</b>; y el <b>215.2.d)</b> reserva la <b>autorización expresa</b> a "
        "los contratos <b>secretos o reservados</b> y a los que exigen medidas de seguridad "
        "especiales. El <b>30 %</b> y los <b>5 millones de euros</b> de las opciones c) y d) salen "
        "de un artículo distinto, el <b>217.2</b>, y de una obligación que <b>no es del "
        "contratista sino de la Administración</b>: cuándo tiene que comprobar que el "
        "contratista paga a sus subcontratistas. <b>La pregunta toma dos cifras de un artículo y "
        "las coloca en otro.</b>",
    "81_preguntas_produccion · nº 75":
        "<b>La respuesta oficial está mal enunciada, aunque es la única marcable.</b> Dice "
        "que la ley garantiza que los datos personales <b>«solo»</b> se recojan con el "
        "consentimiento del titular, y el <b>artículo 6 del Reglamento (UE) 2016/679</b> prevé "
        "<b>seis bases de licitud</b>, de las que el consentimiento es una. La propia <b>Ley "
        "Orgánica 3/2018</b> lo presupone cuando su artículo <b>72.1.b)</b> tipifica el "
        "tratamiento «sin que concurra <b>alguna de</b> las condiciones de licitud». "
        "<b>Marcar la c)</b>: las otras tres son falsas de plano. Lo que sobra de su enunciado es "
        "la palabra <b>«solo»</b>.",
}



AVISOS_PRL = {
    "77_preguntas_produccion_asist · nº 77":
        "<b>La opción buena nombra algo que la norma no dice.</b> La plantilla da <b>b) «Para la "
        "salud y la seguridad informática»</b>, y el <b>artículo 3.1 del RD 488/1997</b> obliga a "
        "que el uso de las pantallas «no suponga riesgos para su seguridad o salud»: <b>la "
        "«seguridad informática» no aparece ni en el real decreto ni en su Guía Técnica</b>. Con "
        "el tema delante se acierta igual, pero por otra razón que la que el enunciado sugiere: "
        "la norma nombra <b>seguridad y salud</b>, y <b>b) es la única opción que nombra las "
        "dos</b> —la a), «para la salud», se queda corta—.",
}

AVISOS_REALIZACION = {
    "60_preguntas_realizacion_asist · nº 46":
        "<b>La respuesta oficial no describe ninguna sensorización.</b> La plantilla da "
        "<b>c) «unos postes de croma colocados en el techo»</b>, que es un montaje de croma: "
        "<b>no mide la posición de la cámara</b>, que es lo que el enunciado pregunta. La que sí "
        "la describe es la <b>a)</b>, «sensores que permiten establecer la posición de la cámara "
        "mediante la lectura de pequeñas marcas de referencia», y es la familia a la que el "
        "<b>free-d</b> pertenece: la ficha del <b>Mo-Sys StarTracker Max</b> documenta que el "
        "seguimiento se hace con <b>marcas retrorreflectantes en techo, pared o suelo</b> y que "
        "<b>FreeD</b> es uno de los formatos en que esos datos se entregan al motor de "
        "representación. <b>La respuesta buena es la a).</b>",
    "62_preguntas_realizacion_asist_2_llamamiento · nº 47":
        "<b>Ninguna de las cuatro opciones define la unidad de control de cámara.</b> Describen "
        "<b>el sensor</b>, <b>la unidad central de proceso</b> de un ordenador, <b>la caja de "
        "plató</b> y <b>la cebra</b> del visor. La marcada —la c)— es la única defendible, "
        "leyendo que el cable de cada cámara llega a la CCU a través de un conector de la pared "
        "del plató; <b>al pie de la letra contradice a la pregunta 65 del primer llamamiento</b>, "
        "que coloca correctamente la caja de plató <b>antes</b> de la CCU. Es una pregunta mal "
        "construida, no una errata de plantilla.",
}

AVISOS_MONTAJE_EQUIPOS = {
    "58_preguntas_mont_equip_audio · nº 63":
        "<b>El nombre correcto del aparato no está entre las opciones.</b> El instrumento que "
        "mide niveles de presión sonora se llama en español <b>sonómetro</b>, y la plantilla da "
        "<b>b) «fonómetro»</b>, que es como lo llaman algunos manuales traducidos. Es la única "
        "opción defendible: <b>«sonímetro» y «presómetro» no existen</b>, y el <b>otoscopio</b> "
        "sí existe pero <b>mira el oído y no mide sonido</b>. Se contesta por descarte, no por "
        "el nombre.",
    "58_preguntas_mont_equip_audio · nº 9":
        "<b>El enunciado confunde dos magnitudes.</b> Pregunta por el <b>«rango dinámico»</b> del "
        "oído humano y la respuesta oficial da un <b>margen de frecuencias</b>: <b>de 20 Hz a "
        "20.000 Hz</b>. El <b>rango dinámico se mide en decibelios</b>, no en hercios; lo que la "
        "opción marcada da es el <b>margen de frecuencias audibles</b>, que es correcto como "
        "dato. <b>La respuesta es la única marcable</b>: el defecto está en el enunciado.",
    "58_preguntas_mont_equip_audio · nº 43":
        "<b>Esta pregunta es idéntica a la 26 del mismo cuadernillo</b>, con la misma respuesta "
        "—<b>«centro o base plana»</b> no es parte del carro de una grúa— y un distractor "
        "distinto. <b>Es la única repetición literal del cuadernillo</b>, y conviene saberla "
        "porque <b>vale dos preguntas de noventa y seis</b>.",
}

AVISOS_EDICION_MONTAJE = {
    "11_preguntas_emypa · nº 61":
        "<b>Esta pregunta es la misma que la 57 del mismo cuadernillo.</b> Los dos enunciados se "
        "diferencian en tres letras —«la tasa de grabación original» y «la tasa fps de grabación "
        "original»—, tienen <b>las mismas cuatro opciones en el mismo orden</b> y <b>la misma "
        "respuesta</b>. <b>Es la única repetición de este cuadernillo</b>, y conviene saberla "
        "porque <b>vale dos preguntas de noventa y seis</b>.",
    "11_preguntas_emypa · nº 5":
        "<b>El enunciado escribe «NFL» donde la literatura escribe «NCL».</b> Los dos sistemas de "
        "luma se llaman <b>constante</b> (<i>constant luminance</i>, CL) y <b>no constante</b> "
        "(<i>non-constant luminance</i>, NCL). <b>No es otra cosa: es una errata del enunciado</b>, "
        "y no cambia cuál es la opción correcta.",
    "11_preguntas_emypa · nº 50":
        "<b>Una de las opciones falsas nombra algo que no existe.</b> La a) dice «monitor con "
        "<i>Hybrid</i> Dynamic Range», y <b>no hay tal categoría</b>: la palabra <i>hybrid</i> "
        "pertenece a <b>HLG</b>, <i>hybrid log-gamma</i>, que es <b>una curva de HDR y no un tipo "
        "de monitor</b>. La respuesta oficial —un monitor con <i>High Dynamic Range</i>— es "
        "correcta.",
}

AVISOS_INFORMACION_GRAFICA = {
    "29_preguntas_igyciys · nº 39":
        "<b>Una de las opciones falsas da las cifras correctas con la unidad equivocada.</b> La d) "
        "dice <b>«de 20 µm a 20.000 µm»</b>, y el micrómetro es <b>una longitud, no una "
        "frecuencia</b>. Las cifras del margen audible son las de la respuesta buena \u2014de 20 Hz "
        "a 20.000 Hz\u2014, pero <b>en hercios</b>. Es la clase de distractor que castiga leer "
        "s\u00f3lo el n\u00famero: <b>hay que mirar la unidad</b>.",
    "29_preguntas_igyciys · nº 32":
        "<b>Una de las opciones falsas es literalmente cierta y no responde a lo que se "
        "pregunta.</b> La d) dice que <b>«el filtro ND no afecta a la profundidad de campo»</b>, y "
        "es verdad: <b>un filtro de densidad neutra no la cambia por s\u00ed mismo</b>. Lo que hace "
        "es <b>permitir un diafragma m\u00e1s abierto</b>, y <b>es el diafragma el que la cambia</b>. "
        "El enunciado no pregunta si el filtro cambia la profundidad: pregunta <b>qu\u00e9 filtro "
        "usar para conseguir la menor profundidad con exposici\u00f3n correcta</b>, y la respuesta a "
        "eso es <b>el de mayor densidad disponible</b>.",
    "29_preguntas_igyciys · nº 71":
        "<b>Esta pregunta depende enteramente de una imagen.</b> El enunciado dice «esta imagen "
        "corresponde a una» y ofrece cuatro se\u00f1ales de prueba. <b>Una imagen no se puede "
        "reproducir en un temario escrito ni contrastar con una fuente</b>, as\u00ed que <b>la "
        "respuesta descansa en la plantilla oficial</b>. Lo que el tema aporta es <b>qu\u00e9 dibuja "
        "cada se\u00f1al de prueba en un monitor de forma de onda</b>: <b>la rampa o diente de "
        "sierra dibuja una diagonal recta</b>, y ninguna de las otras tres opciones dibuja eso. "
        "<b>Y la cuarta opci\u00f3n no existe</b>: el <i>bokeh</i> es el aspecto del desenfoque de un "
        "objetivo y <b>no se corrige con una se\u00f1al de prueba</b>.",
    "29_preguntas_igyciys · nº 36":
        "<b>Esta pregunta depende de un plano de planificaci\u00f3n con cuatro posiciones de "
        "c\u00e1mara marcadas</b>, que un temario escrito no puede reproducir. <b>La respuesta "
        "descansa en la plantilla oficial.</b> Lo que el tema aporta es <b>la condici\u00f3n "
        "geom\u00e9trica</b> que una trayectoria tiene que cumplir para admitir un travelling "
        "compensado: <b>el desplazamiento tiene que ser en la direcci\u00f3n del eje \u00f3ptico "
        "respecto del personaje</b>, acerc\u00e1ndose o alej\u00e1ndose en l\u00ednea recta. Una "
        "trayectoria que pase de lado <b>no permite compensar con el zoom</b>, porque <b>el zoom "
        "s\u00f3lo corrige el tama\u00f1o, no el \u00e1ngulo</b>.",
}

AVISOS_SONIDO = {
    "85_preguntas_sonido · nº 44":
        "<b>La pregunta tiene dos opciones id\u00e9nticas.</b> La c) y la d) dicen exactamente lo "
        "mismo, palabra por palabra. <b>La respuesta oficial sigue siendo correcta</b> —Dante es un "
        "transporte de audio para red local, no un algoritmo de codificaci\u00f3n para una llamada "
        "por internet—, pero <b>el enunciado est\u00e1 mal construido</b> y as\u00ed se declara.",
    "85_preguntas_sonido · nº 36":
        "<b>La f\u00f3rmula s\u00f3lo da milisegundos si la frecuencia de muestreo va en "
        "hercios</b>, y <b>el enunciado la escribe en kilohercios</b>. Con 128 muestras a 48.000 Hz "
        "salen 2,67 ms; metiendo 48 kHz tal cual saldr\u00eda un n\u00famero mil veces mayor. <b>La "
        "opci\u00f3n marcada es la \u00fanica de las cuatro con la estructura correcta</b> y se "
        "marca igual.",
    "85_preguntas_sonido · nº 46":
        "<b>El enunciado pide «lo m\u00e1s aproximado» y hace falta.</b> Tres altavoces de 8 ohmios "
        "en paralelo dan <b>2,67 ohmios</b>, y la opci\u00f3n marcada es <b>2,5</b>. Es la m\u00e1s "
        "pr\u00f3xima de las cuatro —de 2,5 a 2,67 hay 0,17; de 4,5 a 2,67 hay 1,83—, y por eso es "
        "la correcta.",
    "85_preguntas_sonido · nº 82":
        "<b>La respuesta oficial es la mejor de las cuatro y no es exacta.</b> Un mult\u00edmetro "
        "corriente <b>mide resistencia en continua, no impedancia</b>: para medir impedancia hace "
        "falta un puente o un analizador. <b>Las otras tres opciones no miden nada de eso</b>, as\u00ed "
        "que se marca igual.",
}

AVISOS_TESE = {
    "70_preguntas_tese_a · nº 5":
        "<b>Esta pregunta se contesta con el Bolet\u00edn Oficial del Estado en la mano.</b> El "
        "art\u00edculo 2 del <b>Real Decreto 299/2016</b> enumera los efectos de los campos "
        "electromagn\u00e9ticos y <b>tres de las cuatro opciones est\u00e1n literalmente en \u00e9l</b>: "
        "corrientes de contacto, calentamiento de los tejidos y corrientes en las extremidades. <b>La "
        "ionizaci\u00f3n no aparece</b>, y el propio real decreto lo confirma sin decirlo: regula los "
        "campos <b>de 0 Hz a 300 GHz</b>, que es toda la regi\u00f3n no ionizante.",
    "70_preguntas_tese_a · nº 96":
        "<b>La cifra no est\u00e1 en la norma de prevenci\u00f3n: est\u00e1 en el reglamento "
        "electrot\u00e9cnico.</b> El <b>Real Decreto 614/2001</b>, en la definici\u00f3n 5 de su anexo "
        "I, remite la alta y la baja tensi\u00f3n «a los reglamentos electrot\u00e9cnicos», y es el "
        "<b>art\u00edculo 2.1 del Real Decreto 842/2002</b> el que fija la baja tensi\u00f3n hasta "
        "<b>1.000 voltios en alterna y 1.500 en continua</b>. Por encima empieza la alta. <b>Quien "
        "busque el n\u00famero en la norma de prevenci\u00f3n no lo encontrar\u00e1.</b>",
}

AVISOS_REALIZACION_TV = {
    "66_preguntas_realizacion_a · nº 33":
        "<b>La pregunta tiene tres respuestas igualmente correctas.</b> <i>Ben-Hur</i>, "
        "<i>Titanic</i> y <i>El señor de los anillos: el retorno del rey</i> comparten el récord "
        "de <b>once Óscar</b>, y <b>tres de las cuatro opciones son esas tres películas</b>. La "
        "plantilla da <b>b) <i>Ben-Hur</i></b>, y hay que marcarla <b>sabiendo que está marcada "
        "por la plantilla y no por el enunciado</b>. <b>Es impugnable.</b> <b>No es una errata de "
        "plantilla</b>: <i>Ben-Hur</i> es una respuesta correcta, sólo que no es la única.",
    "66_preguntas_realizacion_a · nº 67":
        "<b>El enunciado y la respuesta oficial no encajan.</b> Se pregunta qué <b>NO</b> se "
        "incluye en un magazine y la respuesta marcada afirma que <b>cualquier temática puede "
        "incluirse</b>. Es <b>materialmente cierta</b> —el magazine no excluye temas— y <b>no "
        "contesta a lo que se pregunta</b>. Se marca igual: es la clase de pregunta que se "
        "acierta reconociendo la intención del redactor, no la lógica del enunciado.",
    "68_preguntas_realizacion_b · nº 37":
        "<b>La formulación es discutible.</b> Que la sensación de relieve <b>aumente</b> con la "
        "distancia puede sostenerse al revés si se atiende a la estereoscopia, que <b>desaparece "
        "con la distancia</b>. Lo que hace defendible la respuesta oficial es que <b>en una "
        "imagen plana</b> el relieve descansa en los <b>indicios monoculares</b>, más abundantes "
        "cuanta más profundidad tiene la escena. <b>La respuesta descansa en la plantilla.</b>",
    "66_preguntas_realizacion_a · nº 11":
        "<b>El criterio de reparto no se ha podido establecer.</b> La plantilla deja <b>sin moto "
        "al grupo perseguidor</b> y cubre <b>dos veces el pelotón</b>, mientras que la opción "
        "<b>a)</b> reparte <b>una unidad por grupo</b>. El temario expone el criterio que "
        "sostiene la respuesta oficial —el helicóptero cubre un tramo, la moto de cola recoge a "
        "los descolgados del puerto— y <b>declara que ninguna fuente consultable dirime entre "
        "las dos</b>.",
}

AVISOS_GESTION_ADMINISTRATIVA = {
    "23_preguntas_gea · nº 21":
        "<b>La plantilla da 33 días de indemnización por despido objetivo, con tope de 12 "
        "mensualidades.</b> El <b>artículo 53.1.b) del Estatuto de los Trabajadores</b> dice "
        "<b>veinte días por año de servicio, con un máximo de doce mensualidades</b>. Los treinta "
        "y tres días son del <b>despido improcedente</b> (art. 56.1), y allí el tope no es doce "
        "sino <b>veinticuatro</b>. La opción escogida <b>mezcla la cuantía de un despido con el "
        "tope del otro</b>, y ninguna de las otras tres salva la pregunta: la c) acierta los "
        "veinte días y los estropea diciendo que no hay límite.",
    "23_preguntas_gea · nº 42":
        "<b>La plantilla da 48 horas para comunicar altas y bajas.</b> El <b>artículo 32.3 del RD "
        "84/1996</b> no contempla ese plazo, y además <b>no hay un plazo, hay dos</b>: el "
        "<b>alta</b> se solicita <b>antes</b> del comienzo de la prestación —sin poder "
        "anticiparse más de <b>sesenta días naturales</b>—, y la <b>baja</b>, dentro de los "
        "<b>tres días naturales</b> siguientes al cese. La única opción que roza algo real es la "
        "de setenta y dos horas, y sólo para las bajas.",
    "23_preguntas_gea · nº 17":
        "<b>La plantilla dice que las cuentas anuales son tres documentos.</b> La <b>norma de "
        "elaboración 1.ª</b> del Plan General de Contabilidad dice que son <b>cinco</b> —balance, "
        "cuenta de pérdidas y ganancias, estado de cambios en el patrimonio neto, estado de flujos "
        "de efectivo y memoria— y que dos de ellos sólo decaen en el modelo abreviado. <b>Y la "
        "prueba está en este mismo examen</b>: la pregunta <b>93</b> da por buena esa enumeración "
        "de cinco, y la <b>68</b> da por no obligatorios el estado de cambios y el de flujos, lo "
        "que sólo tiene sentido si la regla son cinco.",
    "23_preguntas_gea · nº 37":
        "<b>La plantilla da 2.400 €, que es el capital de partida.</b> Con interés simple, "
        "C = 2.400 · (1 + 0,10 · 10) = 2.400 · 2 = <b>4.800 €</b>, que es la opción d). <b>Lo que "
        "hace creíble el error conviene saberlo</b>: al 10 % durante diez años los intereses "
        "simples valen exactamente lo mismo que el capital, así que quien calcula los intereses y "
        "se detiene ahí encuentra su resultado entre las opciones.",
    "23_preguntas_gea · nº 90":
        "<b>La opción buena enseña la regla al revés.</b> Da por bueno que los actos "
        "administrativos «pueden ser orales, salvo que una norma exija forma escrita», y el "
        "<b>artículo 36.1 de la Ley 39/2015</b> dice lo contrario: <b>se producirán por escrito a "
        "través de medios electrónicos</b>, salvo que su naturaleza exija otra forma. <b>Aun así "
        "es la única marcable</b>, porque la alternativa dice «siempre por escrito» y ese "
        "«siempre» también es falso.",
    "23_preguntas_gea · nº 13":
        "<b>La respuesta es correcta y su norma no está en el temario.</b> El porcentaje de "
        "retención lo fijan la Ley 35/2006 y el RD 439/2007, que el Anexo 2 no cita. Lo que sí "
        "queda cerrado con norma es la falsedad de las otras tres: el <b>artículo 26.4 del "
        "Estatuto</b> declara <b>nulo</b> todo pacto que traslade la carga fiscal, así que no "
        "puede depender del convenio; y la base del cálculo es la retribución total, no el salario "
        "base.",
    "23_preguntas_gea · nº 26":
        "<b>Los quince días de preaviso al dimitir no están en ninguna norma.</b> El artículo "
        "49.1.d) del Estatuto remite «al preaviso que señalen los convenios colectivos o la "
        "costumbre del lugar», y el <b>III Convenio Colectivo de RTVE tampoco lo fija</b>: "
        "comprobados los dos. Son <b>costumbre</b>, y coinciden con el plazo que el artículo "
        "53.1.c) impone <b>al empresario</b> en el despido objetivo.",
    "23_preguntas_gea · nº 76":
        "<b>Correcta con un matiz.</b> Acierta en que los miembros de un canal privado no añaden a "
        "otros ni cambian permisos. Se queda corta en quién sí: la documentación de Microsoft dice "
        "que es <b>el propietario del canal privado</b> —quien lo creó—, y que <b>por defecto "
        "también un miembro del equipo puede crear canales privados</b>, no sólo un propietario "
        "del equipo.",
    "23_preguntas_gea · nº 94":
        "<b>Tres de las cuatro opciones nombran contratos derogados.</b> El <b>RDL 32/2021</b>, en "
        "vigor desde el 30 de marzo de 2022, suprimió el contrato de <b>obra o servicio</b>, el de "
        "<b>prácticas</b> y el de <b>formación y aprendizaje</b>. La plantilla escoge el que "
        "cumplía esa función <b>hasta esa fecha</b>, nueve meses antes del examen.",
}

SIN_PREGUNTAS_GESTION = {1, 2, 10, 16, 23, 30}
# en Realización (Asistencia) sólo un tema se queda sin banco: el 13, la
# asistencia en grabación, que es justamente el que describe el oficio que da
# nombre a la ocupación. Ni uno de los dos llamamientos le dedicó una pregunta
SIN_PREGUNTAS_REALIZACION = {13}

AVISOS_GESTION = {
    "15_preguntas_gestion · nº 32":
        "<b>La plantilla da «BAI» al indicador del resultado de explotación que <i>no</i> tiene en "
        "cuenta los intereses ni los costes financieros, y el BAI es el único de los cuatro que "
        "<i>sí</i> los computa.</b> Lo dice el propio modelo de cuenta de pérdidas y ganancias del "
        "Plan General de Contabilidad, que construye el BAI como <b>A.3) RESULTADO ANTES DE "
        "IMPUESTOS (A.1+A.2)</b>, donde A.1) es el resultado de explotación y A.2) el resultado "
        "financiero, cuya partida 13 es, literalmente, <b>Gastos financieros</b>. El nombre exacto "
        "de lo que el enunciado describe es <b>BAII</b> o <i>EBIT</i>, que <b>no estaba entre las "
        "opciones</b>; de las cuatro ofrecidas, la única que se sitúa por encima de los intereses "
        "es el <b>EBITDA</b>, la b), y es la que hay que marcar.",
    "15_preguntas_gestion · nº 83":
        "<b>Enunciado roto: ninguna de las cuatro opciones responde a lo que pregunta.</b> Pide el "
        "plazo de prescripción de las faltas <b>muy graves</b> y las opciones hablan de la "
        "publicación en el BOE. El <b>artículo 60.2 del Estatuto de los Trabajadores</b> da "
        "<b>sesenta días</b> desde que la empresa conoce la falta y <b>seis meses</b> desde que se "
        "cometió; los <b>veinte días</b> de la respuesta oficial son el plazo de las faltas "
        "<b>graves</b>. Comprobado en el Estatuto <b>y</b> en el III Convenio Colectivo, que dice "
        "lo mismo, y con la página del cuadernillo vuelta a leer para descartar un error de "
        "transcripción.",
}


BLOQUES = {
    "general": dict(
        carpeta="general",
        rotulo="Temario general",
        ocupacion=None,
        titulo="Temario general",
        subtitulo="Los ocho temas comunes a las siete ocupaciones tipo:<br>"
                  "Producción (Asistencia), Producción, Gestión Administrativa,<br>"
                  "Gestión, Realización (Asistencia), Documentación<br>"
                  "e Información y Contenidos",
        pie="Oposiciones RTVE – Temario General",
        avisos=ERRATAS_GENERAL,
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[
            ("01-constitucion-espanola", "g1"),
            ("02-ley-17-2006", None),
            ("03-ley-5-2017", "g2-g3"),
            ("04-ley-8-2009", "g4"),
            ("05-convenio-colectivo", "g5"),
            ("06-igualdad", "g6"),
            ("07-ley-13-2022", "g7"),
            ("08-ley-31-1995", "g8"),
        ],
        aviso_respuestas="<b>Tres respuestas oficiales están mal</b> y van avisadas debajo de su "
                         "tabla: el volumen enseña la norma, no la plantilla.",
        aviso_portada="<p><b>Tres respuestas oficiales de 2024 están mal.</b> Van marcadas una a "
                      "una en el apéndice, con el precepto que las desmiente. El temario enseña "
                      "la norma, no la plantilla.</p>",
    ),
    "produccion-asistencia": dict(
        carpeta="produccion-asistencia",
        rotulo="Temario específico · Producción (Asistencia)",
        ocupacion="Producción (Asistencia)",
        titulo="Temario específico",
        subtitulo="Los dieciocho temas de <b>Producción (Asistencia)</b>",
        pie="Oposiciones RTVE – Producción (Asistencia)",
        avisos=dict(AVISOS_PRODUCCION_ASISTENCIA, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "produccion-asistencia-%02d" % n) for n, base in [
            (1, "la-produccion"), (2, "propiedad-intelectual"), (3, "el-guion"),
            (4, "el-desglose"), (5, "localizacion"), (6, "plan-y-orden-de-trabajo"),
            (7, "equipos-humanos"), (8, "formatos-y-soportes"),
            (9, "escenografia-e-iluminacion"), (10, "imagen-y-sonido"),
            (11, "transmision-de-senal"), (12, "el-estudio"),
            (13, "equipos-de-exteriores"), (14, "documentacion-internacional"),
            (15, "organismos"), (16, "gestion-de-servicios"),
            (17, "proteccion-de-datos"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque está mal</b>, pero "
                         "<b>seis enunciados sí lo están</b> —uno con los términos invertidos, "
                         "otro que mezcla cine y televisión, otro con una ley mal fechada, y en "
                         "el tema 18 uno cuya opción buena nombra una «seguridad informática» "
                         "que la norma no conoce—: van avisados debajo de su tabla.",
        aviso_portada="<p><b>Ninguna respuesta oficial de este bloque está mal, pero seis "
                      "enunciados sí.</b> Uno invierte los términos, otro mezcla cine y "
                      "televisión, otro fecha mal una ley y cita otra derogada, en otro el "
                      "distractor descartado <i>no es falso</i>, y en otro la opción buena "
                      "nombra un riesgo que la norma no nombra. Van marcados uno a uno en el "
                      "apéndice. El temario contesta lo que corrige el tribunal <b>y dice dónde "
                      "está la costura</b>.</p>",
    ),
    "gestion-administrativa": dict(
        carpeta="gestion-administrativa",
        rotulo="Temario específico · Gestión Administrativa",
        ocupacion="Gestión Administrativa",
        titulo="Temario específico",
        subtitulo="Los trece temas de <b>Gestión Administrativa</b>",
        pie="Oposiciones RTVE – Gestión Administrativa",
        avisos=dict(AVISOS_GESTION_ADMINISTRATIVA, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "gestion-administrativa-%02d" % n) for n, base in [
            (1, "gestion-administrativa"), (2, "contrato-de-trabajo"),
            (3, "seguridad-social"), (4, "nominas"), (5, "contabilidad"),
            (6, "matematica-financiera"), (7, "probabilidad-y-estadistica"),
            (8, "ofimatica"), (9, "windows-10"), (10, "la-red-internet"),
            (11, "office-2019"), (12, "microsoft-teams"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Cuatro respuestas oficiales de este bloque están mal</b> —la "
                         "indemnización del despido objetivo, el plazo de las altas y bajas, los "
                         "documentos de las cuentas anuales y una capitalización simple—, y van "
                         "marcadas una a una con lo que las desmiente. <b>El temario enseña la "
                         "norma y la cuenta, no la plantilla.</b>",
        aviso_portada="<p><b>Es la ocupación con más respuestas oficiales equivocadas del "
                      "proyecto: cuatro.</b> Una la desmiente un artículo del Estatuto de los "
                      "Trabajadores; otra, un reglamento de la Seguridad Social; otra, <b>el "
                      "propio examen</b>, que contesta la misma regla de dos maneras distintas; y "
                      "la cuarta, <b>una multiplicación</b>. Van marcadas una a una en el "
                      "apéndice.</p>"
                      "<p><b>Y es la primera con temas que no se verifican, se demuestran</b>: la "
                      "matemática financiera y la estadística no están en el BOE, así que sus "
                      "cuentas van rehechas en el propio tema, con el procedimiento a la vista. "
                      "<b>Los cinco temas de informática se apoyan en la documentación del "
                      "fabricante</b>, que es el cuarto nivel de la jerarquía de fuentes, y dicen "
                      "qué es lo que con ella no se puede asegurar.</p>",
    ),
    "gestion": dict(
        carpeta="gestion",
        rotulo="Temario específico · Gestión",
        ocupacion="Gestión",
        titulo="Temario específico",
        subtitulo="Los treinta y un temas de <b>Gestión</b>",
        pie="Oposiciones RTVE – Gestión",
        avisos=dict(AVISOS_GESTION, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        # seis puntos del temario no tienen ni una pregunta en los cuadernillos
        # de 2024 —el 1, el 2, el 10, el 16, el 23 y el 30—, así que su banco no
        # existe y en su lugar va None. Se desarrollan igual: el examen siguiente
        # no tiene por qué repetir el reparto del anterior
        temas=[("%02d-%s" % (n, base),
                "gestion-%02d" % n if n not in SIN_PREGUNTAS_GESTION else None)
               for n, base in [
            (1, "estatuto-de-los-trabajadores"), (2, "trabajo-por-cuenta-ajena"),
            (3, "convenios-colectivos"), (4, "contrato-de-trabajo"),
            (5, "modificacion-de-condiciones"), (6, "tiempo-de-trabajo"),
            (7, "el-salario"), (8, "derechos-y-deberes"), (9, "proteccion-de-datos"),
            (10, "el-presupuesto"), (11, "modelo-contable"), (12, "proceso-contable"),
            (13, "el-patrimonio"), (14, "gastos-ingresos-tesoreria"),
            (15, "inmovilizado-material"), (16, "inmovilizado-intangible"),
            (17, "costes-de-produccion"), (18, "tesoreria"),
            (19, "informacion-financiera"), (20, "iva"),
            (21, "planificacion-y-control"), (22, "seguridad-social"),
            (23, "retribucion-de-recursos-humanos"), (24, "nomina"),
            (25, "la-empresa-como-organizacion"), (26, "gestion-por-competencias"),
            (27, "produccion-en-television"), (28, "matematica-financiera"),
            (29, "estadistica-descriptiva"), (30, "excel-avanzado"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Una respuesta oficial de este bloque está mal</b> —el indicador que "
                         "no computa los intereses— y <b>una pregunta está rota</b>: la de la "
                         "prescripción de las faltas muy graves, donde <b>ninguna</b> de las "
                         "cuatro opciones responde. Las dos van marcadas con lo que las "
                         "desmiente. <b>El temario enseña la norma, no la plantilla.</b>",
        aviso_portada="<p><b>Es el temario más largo del proyecto y el más entrelazado con el "
                      "resto.</b> Treinta puntos propios más el de prevención, y sus fronteras "
                      "tocan a los otros bloques: su punto 9 es la protección de datos, su punto "
                      "27 es el proceso de producción en televisión y sus puntos 11 a 16 "
                      "comparten el Plan General de Contabilidad con Gestión Administrativa.</p>"
                      "<p><b>Sus dos puntos con más peso son el 24 y el 25</b>, con siete y seis "
                      "preguntas de las ochenta y una, y en los dos las respuestas oficiales son "
                      "correctas. <b>Tres puntos no han caído nunca</b> —el 16, el 23 y el 30— y "
                      "van desarrollados igual, porque el examen siguiente no tiene por qué "
                      "repetir el reparto del anterior.</p>"
                      "<p><b>Y ocho de sus puntos no descansan en ninguna norma.</b> El control "
                      "de gestión, la organización, las competencias, la matemática financiera y "
                      "la estadística no están en el BOE: sus cuentas van rehechas con el "
                      "procedimiento a la vista y sus modelos van atribuidos al autor que los "
                      "formuló. El punto 30 se apoya en la documentación de Microsoft para "
                      "<b>Excel 2019</b>, que es el cuarto nivel de la jerarquía de fuentes, y "
                      "dice qué es lo que con ella no se puede asegurar.</p>",
    ),
    "produccion": dict(
        carpeta="produccion",
        rotulo="Temario específico · Producción",
        ocupacion="Producción",
        titulo="Temario específico",
        subtitulo="Los diecisiete temas de <b>Producción</b>",
        pie="Oposiciones RTVE – Producción",
        avisos=dict(AVISOS_PRODUCCION, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "produccion-%02d" % n) for n, base in [
            (1, "la-produccion"), (2, "propiedad-intelectual"),
            (3, "escaleta-guion-desglose"), (4, "generos-y-formatos"),
            (5, "equipos-humanos"), (6, "captacion-de-imagen-y-sonido"),
            (7, "el-estudio-de-television"), (8, "produccion-en-exteriores"),
            (9, "escenografia-e-iluminacion"), (10, "medios-artisticos"),
            (11, "tratamiento-de-imagen-y-sonido"), (12, "transporte-de-la-senal"),
            (13, "control-central"), (14, "el-presupuesto"),
            (15, "organismos"), (16, "aspectos-juridicos"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Una respuesta oficial de este bloque no existe</b> \u2014la de la "
                         "subcontrataci\u00f3n en los contratos p\u00fablicos, donde <b>ninguna de "
                         "las cuatro opciones dice lo que dice la ley</b>\u2014 y <b>otra est\u00e1 "
                         "mal enunciada</b>: la que da el consentimiento por \u00fanica base para "
                         "tratar datos. Las dos van marcadas con el art\u00edculo que las desmiente. "
                         "<b>El temario ense\u00f1a la norma, no la plantilla.</b>",
        aviso_portada="<p><b>El punto 16 de su anexo es el m\u00e1s preguntado de todo el "
                      "proyecto: siete preguntas de noventa salen de un solo punto</b>, y es "
                      "tambi\u00e9n donde est\u00e1n las dos costuras de este examen. <b>La pregunta "
                      "de la subcontrataci\u00f3n no tiene ninguna opci\u00f3n correcta</b>: la "
                      "marcada contradice el \u00aben todo caso\u00bb del art\u00edculo 215 de la Ley "
                      "de Contratos del Sector P\u00fablico, y sus dos cifras \u2014el 30 % y los "
                      "cinco millones\u2014 vienen de otro art\u00edculo que mide otra cosa. Va "
                      "demostrado con los dos art\u00edculos delante.</p>"
                      "<p><b>Y es el bloque con m\u00e1s preguntas contestadas con documento "
                      "propio</b>: la ficha del fabricante que documenta las cuatro se\u00f1ales "
                      "sincronizadas de una mochila, la nota de prensa que fecha la creaci\u00f3n de "
                      "FORTA, la p\u00e1gina en que una asociaci\u00f3n se define a s\u00ed misma con "
                      "las palabras del enunciado. <b>Donde no hay documento, el tema lo dice</b>, "
                      "y son cuatro veces contadas.</p>",
    ),
    "montaje-equipos": dict(
        carpeta="montaje-equipos",
        rotulo="Temario específico · Montaje de Equipos Audiovisuales",
        ocupacion="Montaje de Equipos Audiovisuales",
        titulo="Temario específico",
        subtitulo="Los diez temas de <b>Montaje de Equipos Audiovisuales</b>",
        pie="Oposiciones RTVE – Montaje de Equipos Audiovisuales",
        avisos=dict(AVISOS_MONTAJE_EQUIPOS, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "montaje-equipos-%02d" % n) for n, base in [
            (1, "instalaciones-y-unidades-moviles"),
            (2, "profesionales-y-operativa"),
            (3, "camaras-tipos-y-manejo"),
            (4, "cabezas-y-soportes"),
            (5, "conectores-y-cables"),
            (6, "sonido-microfonos-y-altavoces"),
            (7, "maquinaria-movimiento-camaras"),
            (8, "la-cabeza-caliente"),
            (9, "montaje-en-estudios-y-exteriores"),
            (10, "asistencia-a-la-operacion-de-camara"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque se puede dar por mal "
                         "contestada</b>, pero <b>dos preguntas están defectuosas</b> \u2014una "
                         "pide el \u00abrango din\u00e1mico\u00bb del o\u00eddo y responde con un "
                         "margen de frecuencias, y otra llama \u00abfon\u00f3metro\u00bb al "
                         "son\u00f3metro porque el nombre correcto no est\u00e1 entre las "
                         "opciones\u2014, y <b>una se repite literalmente</b>. Van avisadas debajo "
                         "de su tabla.",
        aviso_portada="<p><b>Este es el bloque de oficio del proyecto</b>: casi ninguna de sus "
                      "noventa y seis preguntas se contesta abriendo una norma. Se contestan "
                      "sabiendo <b>qu\u00e9 pieza pertenece a qu\u00e9 m\u00e1quina</b> \u2014la copa "
                      "es del tr\u00edpode y no de la cabeza, el iluminador es la antena y el disco "
                      "s\u00f3lo refleja\u2014 y <b>qu\u00e9 cable lleva corriente y cu\u00e1l no</b>. "
                      "El temario los ense\u00f1a con su despiece delante.</p>"
                      "<p><b>Diecisiete preguntas salen de un solo punto</b>, el de conectores y "
                      "cables: casi una de cada cinco. Y <b>siete m\u00e1s son electricidad "
                      "b\u00e1sica</b>, porque el programa dice \u00abbaja tensi\u00f3n\u00bb y el "
                      "tribunal lo ha tomado al pie de la letra: ah\u00ed s\u00ed hay norma, y va "
                      "citada \u2014el reglamento electrot\u00e9cnico, su ITC-BT-24 y el real decreto "
                      "del riesgo el\u00e9ctrico\u2014. <b>Diez datos de cat\u00e1logo descansan s\u00f3lo "
                      "en la plantilla</b>, y cada uno lo dice en su tema.</p>",
    ),
    "edicion-montaje": dict(
        carpeta="edicion-montaje",
        rotulo="Temario específico · Edición, Montaje y Procesos Audiovisuales",
        ocupacion="Edición, Montaje y Procesos Audiovisuales",
        titulo="Temario específico",
        subtitulo="Los diez temas de <b>Edición, Montaje y Procesos Audiovisuales</b>",
        pie="Oposiciones RTVE – Edición, Montaje y Procesos Audiovisuales",
        avisos=dict(AVISOS_EDICION_MONTAJE, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "edicion-montaje-%02d" % n) for n, base in [
            (1, "electronica-e-informatica"),
            (2, "colorimetria"),
            (3, "conceptos-basicos-de-sonido"),
            (4, "tratamiento-digital-de-la-senal"),
            (5, "soportes-formatos-e-ingesta"),
            (6, "equipos-de-medida-y-control"),
            (7, "avid-media-composer"),
            (8, "evs-directo-y-retransmisiones"),
            (9, "incrustaciones-grafismo-y-postproduccion"),
            (10, "lenguaje-audiovisual-y-montaje"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque se puede dar por mal "
                         "contestada</b>, pero <b>una pregunta se repite entera</b> \u2014la 57 y "
                         "la 61 son la misma\u2014 y <b>dos enunciados est\u00e1n defectuosos</b>: "
                         "uno escribe \u00abNFL\u00bb por NCL y otro ofrece como opci\u00f3n un "
                         "tipo de monitor que no existe. Van avisados debajo de su tabla.",
        aviso_portada="<p><b>Este bloque tiene dos caras y conviene saberlo antes de empezar.</b> "
                      "Una es <b>te\u00f3rica y se estudia leyendo</b>: colorimetr\u00eda, "
                      "tratamiento digital de la se\u00f1al y teor\u00eda del montaje suman "
                      "treinta y siete preguntas, y casi todas se contestan con norma t\u00e9cnica "
                      "delante \u2014las recomendaciones de la Uni\u00f3n Internacional de "
                      "Telecomunicaciones, que aqu\u00ed van citadas cuadro por cuadro\u2014 o "
                      "con vocabulario de oficio asentado.</p>"
                      "<p>La otra es <b>pr\u00e1ctica y no se estudia leyendo</b>: <b>veintiocho "
                      "preguntas salen del manejo de tres programas comerciales</b> \u2014el "
                      "montador de Avid, el sistema de repetici\u00f3n en directo y la "
                      "composici\u00f3n de Adobe\u2014, y <b>su documentaci\u00f3n no se ha "
                      "podido consultar</b>. El temario lo dice en lugar de fingir lo contrario, y "
                      "hace con ellas lo \u00fanico honrado: <b>levantar la arquitectura del "
                      "programa y el porqu\u00e9 de cada respuesta</b>, que es lo que convierte una "
                      "lista de atajos en algo recordable. <b>Treinta y cinco afirmaciones "
                      "descansan s\u00f3lo en la plantilla, y cada una lo declara en su tema.</b></p>",
    ),
    "informacion-grafica": dict(
        carpeta="informacion-grafica",
        rotulo="Temario específico · Información Gráfica y Captación de Imagen y Sonido",
        ocupacion="Información Gráfica y Captación de Imagen y Sonido",
        titulo="Temario específico",
        subtitulo="Los once temas de <b>Información Gráfica y Captación de Imagen y Sonido</b>",
        pie="Oposiciones RTVE – Información Gráfica y Captación de Imagen y Sonido",
        avisos=dict(AVISOS_INFORMACION_GRAFICA, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), banco) for n, base, banco in [
            (1, "luz-color-y-percepcion", "informacion-grafica-01"),
            (2, "senales-y-formatos", "informacion-grafica-02"),
            (3, "la-camara-y-el-sensor", "informacion-grafica-03"),
            (4, "objetivos-filtros-y-accesorios", "informacion-grafica-04"),
            (5, "soportes-y-estabilizacion", "informacion-grafica-05"),
            (6, "el-sonido-en-eng", "informacion-grafica-06"),
            (7, "la-iluminacion-en-eng", "informacion-grafica-07"),
            (8, "control-de-camara-y-ajuste", "informacion-grafica-08"),
            (9, "envios-directos-y-robotizadas", "informacion-grafica-09"),
            (10, "lenguaje-audiovisual", "informacion-grafica-10"),
            # el punto 11 no tiene ni una pregunta en el cuadernillo
            (11, "teoria-de-la-informacion-audiovisual", None),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Las noventa y cuatro respuestas oficiales de este bloque son "
                         "correctas</b>: no hay ni una errata de plantilla. Pero <b>dos preguntas "
                         "dependen de una imagen que un temario escrito no puede reproducir</b> y "
                         "<b>dos m\u00e1s tienen una opci\u00f3n falsa mal construida</b> \u2014una da "
                         "las cifras correctas con la unidad equivocada y otra es literalmente "
                         "cierta sin responder a lo que se pregunta\u2014. Van avisadas debajo de su "
                         "tabla.",
        aviso_portada="<p><b>Este es el bloque m\u00e1s f\u00edsico del proyecto.</b> "
                      "Treinta y cinco de sus preguntas son \u00f3ptica, colorimetr\u00eda, "
                      "fotometr\u00eda y fisiolog\u00eda de la visi\u00f3n, y <b>casi todas se "
                      "contestan con cuatro o cinco leyes que se aplican una y otra vez</b>: la "
                      "relaci\u00f3n entre longitud de onda, frecuencia y desviaci\u00f3n; la ley "
                      "inversa del cuadrado; los tres factores de la profundidad de campo; la "
                      "escala de n\u00fameros f y la de mireds, que van las dos <b>al rev\u00e9s</b> de "
                      "lo que parece. El temario las levanta como leyes y no como datos, <b>porque "
                      "as\u00ed una sola vale por cuatro preguntas</b>.</p>"
                      "<p><b>Y trae la pregunta mejor construida de todo el proyecto</b>: la que "
                      "pide qu\u00e9 hace la OETF, <b>con las cuatro opciones sacadas del mismo "
                      "p\u00e1rrafo de la Recomendaci\u00f3n UIT-R BT.2100</b> \u2014las tres falsas son "
                      "las definiciones de las otras dos funciones\u2014. Aqu\u00ed va citada "
                      "literalmente, con el p\u00e1rrafo entero delante. <b>Siete afirmaciones "
                      "descansan s\u00f3lo en la plantilla</b>, y cada una lo declara en su tema; "
                      "<b>dos de ellas porque dependen de una imagen</b>, y el temario dice qu\u00e9 "
                      "aporta en su lugar. <b>Y un punto entero del programa no tiene ni una "
                      "pregunta</b>: se escribe contra el programa, y lo dice.</p>",
    ),
    "sonido": dict(
        carpeta="sonido",
        rotulo="Temario espec\u00edfico \u00b7 Sonido",
        ocupacion="Sonido",
        titulo="Temario espec\u00edfico",
        subtitulo="Los diecisiete temas de <b>Sonido</b>",
        pie="Oposiciones RTVE \u2013 Sonido",
        avisos=dict(AVISOS_SONIDO, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), banco) for n, base, banco in [
            (1, "electricidad-y-electronica-basicas", "sonido-01"),
            (2, "principios-fisicos-del-sonido-y-la-audicion", "sonido-02"),
            # el punto 1.6 no tiene ni una pregunta en el cuadernillo
            (3, "musica-instrumentos-e-historia", None),
            (4, "acustica-arquitectonica", "sonido-04"),
            (5, "microfonos-soportes-y-accesorios", "sonido-05"),
            (6, "senales-de-contribucion", "sonido-06"),
            (7, "mezcla-y-tratamiento-del-sonido", "sonido-07"),
            (8, "postproduccion-efectos-y-daw", "sonido-08"),
            (9, "grabacion-de-sonido", "sonido-09"),
            (10, "sonorizacion-altavoces-y-amplificadores", "sonido-10"),
            (11, "lineas-y-conexiones", "sonido-11"),
            (12, "el-sonido-en-la-radio-y-la-television", "sonido-12"),
            (13, "radiofrecuencia", "sonido-13"),
            (14, "medicion-y-sonoridad", "sonido-14"),
            (15, "audio-multicanal", "sonido-15"),
            (16, "audio-sobre-ip", "sonido-16"),
            (17, "audio-sobre-protocolos-digitales", "sonido-17"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Las ochenta y seis respuestas oficiales de este bloque son "
                         "correctas</b>, con cuatro salvedades que van marcadas con lo que las "
                         "explica: <b>una pregunta con dos opciones id\u00e9nticas</b>, <b>una "
                         "f\u00f3rmula cuyas unidades no encajan con su enunciado</b>, <b>un "
                         "resultado aproximado que el enunciado pide como tal</b> y <b>un "
                         "instrumento que no mide exactamente lo que la respuesta afirma</b>. "
                         "<b>Cuatro preguntas dependen de un dato que un temario escrito no puede "
                         "verificar</b> \u2014un modelo de cat\u00e1logo, un gesto de la mano y dos "
                         "cifras de especificaci\u00f3n comercial\u2014: van declaradas una a una, y "
                         "de cada una se aporta <b>la regla de su familia</b>.",
        aviso_portada="<p><b>Es la ocupaci\u00f3n con m\u00e1s puestos convocados de las que quedaban "
                      "por cubrir</b>: <b>ciento dos plazas</b>, noventa y tres de ellas con "
                      "examen, y <b>ochenta y seis preguntas</b> de un llamamiento con su "
                      "plantilla completa.</p>"
                      "<p><b>Su anexo reparte el examen de forma muy desigual</b>: el audio sobre "
                      "redes se lleva <b>nueve preguntas</b>, los micr\u00f3fonos y las l\u00edneas "
                      "ocho cada uno y la medici\u00f3n de sonoridad seis, mientras que la "
                      "ac\u00fastica arquitect\u00f3nica se lleva una y <b>la m\u00fasica, ninguna</b>.</p>"
                      "<p><b>Ese punto sin preguntas se ha escrito igual</b>, contra el programa: "
                      "un punto con cero preguntas en un llamamiento puede tener cuatro en el "
                      "siguiente, y <b>quien s\u00f3lo estudia lo preguntado estudia el examen "
                      "pasado</b>.</p>"
                      "<p>Y hay un punto que merece un aviso propio: <b>el enunciado m\u00e1s largo "
                      "de todo el anexo tiene UNA sola pregunta, y es sobre un gesto de la "
                      "mano</b>. Es la respuesta peor documentada del bloque, porque los gestos "
                      "del control son convenio de casa y no hay fuente p\u00fablica que los fije. "
                      "<b>El temario lo declara</b> en lugar de inventar una.</p>",
    ),
    "tese": dict(
        carpeta="tese",
        rotulo="Temario espec\u00edfico \u00b7 T\u00e9cnica de Equipos y Sistemas Electr\u00f3nicos",
        ocupacion="T\u00e9cnica de Equipos y Sistemas Electr\u00f3nicos",
        titulo="Temario espec\u00edfico",
        subtitulo="Los diecisiete temas de <b>T\u00e9cnica de Equipos y Sistemas Electr\u00f3nicos</b>",
        pie="Oposiciones RTVE \u2013 T\u00e9cnica de Equipos y Sistemas Electr\u00f3nicos",
        avisos=dict(AVISOS_TESE, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "tese-%02d" % n) for n, base in [
            (1, "conceptos-basicos-de-electricidad"),
            (2, "componentes-electronicos"),
            (3, "electronica-de-potencia"),
            (4, "amplificadores-operacionales"),
            (5, "electronica-digital"),
            (6, "circuitos-integrados-y-secuenciales"),
            (7, "memorias-logica-programable-y-microprocesadores"),
            (8, "la-senal-audiovisual"),
            (9, "la-senal-ip"),
            (10, "equipos-utilizados-en-television-y-radio"),
            (11, "control-de-iluminacion-escenica"),
            (12, "comunicaciones-y-redes"),
            (13, "equipos-de-medida-y-control"),
            (14, "medidas-de-la-senal-de-video-audio-y-radiofrecuencia"),
            (15, "mantenimiento-preventivo-y-correctivo"),
            (16, "mantenimiento-en-television"),
            (17, "seguridad-en-instalaciones-tecnicas"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Las ciento catorce respuestas oficiales de este bloque son "
                         "correctas.</b> Ninguna es err\u00f3nea y ninguna es impugnable. Lo que "
                         "s\u00ed hay que saber antes de empezar es que <b>unas treinta preguntas "
                         "dependen de una figura</b> \u2014un esquema de circuito, un s\u00edmbolo, una "
                         "pantalla de instrumento, una fotograf\u00eda de conectores\u2014, <b>la "
                         "proporci\u00f3n m\u00e1s alta de todo el proyecto</b>. Un temario escrito no "
                         "puede reproducirlas: <b>este las declara una a una y, en lugar de "
                         "describir lo que no ha visto, aporta la regla de la familia</b> que hace "
                         "legible cualquier pregunta de esa clase.",
        aviso_portada="<p><b>Noventa y siete plazas convocadas</b>, ochenta y nueve de ellas con "
                      "examen, y <b>ciento catorce preguntas</b> de dos cuadernillos con sus dos "
                      "plantillas completas.</p>"
                      "<p><b>Los dos cuadernillos son de tama\u00f1o muy distinto</b>: uno de noventa "
                      "y seis preguntas y otro que sus propias instrucciones describen como «30 "
                      "preguntas (25 principales m\u00e1s 5 de reserva)». <b>No es un fallo de "
                      "extracci\u00f3n: es un examen m\u00e1s corto</b>, y se ha le\u00eddo entero.</p>"
                      "<p><b>Su anexo reparte el examen de forma muy desigual</b>: el inventario "
                      "de equipos de televisi\u00f3n y radio se lleva <b>diecinueve preguntas</b>, "
                      "las redes trece y los componentes doce, mientras que el control de "
                      "iluminaci\u00f3n escenica se lleva una y las memorias y microprocesadores, "
                      "otra entre dos puntos del programa.</p>"
                      "<p>Y hay una diferencia de fondo con el resto del proyecto: <b>diecis\u00e9is "
                      "de sus diecisiete temas van enteros como oficio</b>, sin ninguna norma "
                      "detr\u00e1s. <b>El \u00fanico con respaldo en el Bolet\u00edn Oficial del Estado es el "
                      "de seguridad en instalaciones t\u00e9cnicas</b>, y ah\u00ed el temario cita "
                      "literalmente las tres normas que resuelven sus preguntas.</p>",
    ),
    "realizacion-tv": dict(
        carpeta="realizacion-tv",
        rotulo="Temario específico · Realización Televisión",
        ocupacion="Realización Televisión",
        titulo="Temario específico",
        subtitulo="Los veintidós temas de <b>Realización Televisión</b>",
        pie="Oposiciones RTVE – Realización Televisión",
        avisos=dict(AVISOS_REALIZACION_TV, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "realizacion-tv-%02d" % n) for n, base in [
            (1, "la-musica"), (2, "las-artes-escenicas"), (3, "la-literatura"),
            (4, "artes-plasticas-y-fotografia"), (5, "el-cine"), (6, "la-television"),
            (7, "generos-y-formatos"), (8, "el-guion"),
            (9, "organizacion-de-la-produccion"), (10, "funciones-del-realizador"),
            (11, "la-senal-y-su-control"), (12, "formatos-y-procesos-de-registro"),
            (13, "lenguaje-tecnico-y-narrativo"),
            (14, "la-camara-accesorios-y-posibilidades"), (15, "el-mezclador"),
            (16, "la-iluminacion"), (17, "el-sonido"),
            (18, "produccion-de-programas-directos-y-grabados"),
            (19, "la-puesta-en-escena"), (20, "postproduccion"),
            (21, "produccion-y-realizacion-online-transmedia"),
            (22, "derechos-de-autor-y-propiedad-intelectual"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Las doscientas veintinueve respuestas oficiales de este bloque son "
                         "correctas</b>, salvo dos preguntas defectuosas que van marcadas con lo "
                         "que las desmiente: <b>una con tres opciones igualmente correctas</b> "
                         "—el récord de Óscar— y <b>una cuyo enunciado y respuesta no encajan</b> "
                         "—la del magazine—. <b>Trece preguntas dependen de una imagen que un "
                         "temario escrito no puede reproducir</b>: van declaradas una a una, y de "
                         "cada una se aporta <b>la regla de su familia</b> en lugar de describir "
                         "lo que no se ha visto.",
        aviso_portada="<p><b>Es la ocupación de grado del área de realización</b>, distinta de "
                      "Realización (Asistencia), y trae <b>doscientas veintinueve preguntas del "
                      "bloque específico</b>, de dos llamamientos con sus dos plantillas "
                      "completas.</p>"
                      "<p><b>Su anexo reparte el examen de forma muy desigual</b>: la producción "
                      "de programas directos y grabados se lleva <b>veintitrés preguntas</b> —el "
                      "banco más grande del proyecto en un solo punto de programa—, el guion "
                      "veintidós, el lenguaje narrativo veinte y el sonido dieciocho, mientras "
                      "que la literatura se lleva dos y los derechos de autor, tres.</p>"
                      "<p><b>Y es la ocupación con más preguntas dependientes de una imagen de "
                      "todo el proyecto: trece.</b> Piden leer una planta de decorado, un "
                      "esquema de posiciones, una captura de pantalla o una fotografía. <b>El "
                      "temario no las describe, porque no las tiene delante</b>: declara cada "
                      "una y aporta en su lugar la regla que hace legible cualquier pregunta de "
                      "esa familia.</p>",
    ),
    "realizacion": dict(
        carpeta="realizacion",
        rotulo="Temario específico · Realización (Asistencia)",
        ocupacion="Realización (Asistencia)",
        titulo="Temario específico",
        subtitulo="Los veintiún temas de <b>Realización (Asistencia)</b>",
        pie="Oposiciones RTVE – Realización (Asistencia)",
        avisos=dict(AVISOS_REALIZACION, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base),
                "realizacion-%02d" % n if n not in SIN_PREGUNTAS_REALIZACION else None)
               for n, base in [
            (1, "generos-y-formatos"), (2, "el-guion"),
            (3, "organizacion-de-la-produccion"), (4, "decorados-planos-y-perspectivas"),
            (5, "la-tecnologia-en-la-realizacion"), (6, "lenguaje-tecnico-y-narrativo"),
            (7, "la-camara-accesorios-y-posibilidades"), (8, "la-iluminacion"),
            (9, "el-sonido"), (10, "el-mezclador-de-video"),
            (11, "el-estudio-controles-y-plato"), (12, "las-unidades-moviles"),
            (13, "la-asistencia-en-grabacion"), (14, "la-retransmision"),
            (15, "la-emision-pantallas-servidores-y-grafismo"),
            (16, "realidad-aumentada-y-produccion-online"),
            (17, "la-asistencia-en-plato-regiduria"), (18, "canales-online"),
            (19, "la-puesta-en-escena"), (20, "postproduccion"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Una respuesta oficial de este bloque está mal</b> —la del sistema "
                         "free-d, cuya opción marcada describe un montaje de croma y no una "
                         "sensorización— y <b>una pregunta está mal construida</b>: la de la "
                         "unidad de control de cámara, donde <b>ninguna</b> de las cuatro "
                         "opciones la define. Las dos van marcadas con lo que las desmiente. "
                         "<b>El temario enseña la norma y la ficha del fabricante, no la "
                         "plantilla.</b>",
        aviso_portada="<p><b>Es la ocupación más grande del proceso 1/2022: 129 puestos, 104 de "
                      "ellos con examen</b>, y trae <b>doscientas nueve preguntas del bloque "
                      "específico</b> —el mayor del proyecto hasta Realización Televisión—, de dos "
                      "llamamientos con sus dos plantillas completas.</p>"
                      "<p><b>Su anexo no numera temas, sino ocho bloques con cuarenta y dos "
                      "subpuntos de tamaños muy desiguales</b>, y este libro explica en el "
                      "programa cómo se convierten en veintiún temas. <b>Dos bloques concentran "
                      "el examen</b>: el mezclador de vídeo, con treinta y cinco preguntas, y la "
                      "tecnología de la realización, con treinta y cuatro.</p>"
                      "<p><b>Y es la única ocupación cuyo punto de prevención añade la exposición "
                      "a altos niveles de sonido</b>, que va desarrollada sobre el Real Decreto "
                      "286/2006 en el apartado 4 del tema de prevención. Las otras cinco "
                      "ocupaciones que comparten ese tema pueden saltárselo, y allí se dice.</p>",
    ),
    "documentacion": dict(
        carpeta="documentacion",
        rotulo="Temario específico · Documentación",
        ocupacion="Documentación",
        titulo="Temario específico",
        subtitulo="Los siete temas de <b>Documentación</b>",
        pie="Oposiciones RTVE – Documentación",
        avisos=dict(AVISOS_DOCUMENTACION, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "documentacion-%02d" % n) for n, base in [
            (1, "historia-de-rtve"), (2, "documentacion-y-tecnologias"),
            (3, "internet"), (4, "inteligencia-artificial"),
            (5, "centros-de-documentacion"), (6, "cultura-y-actualidad"),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque está mal</b>, pero "
                         "<b>tres enunciados cojean</b> —uno fecha el estado de alarma un día "
                         "tarde, otro desarrolla unas siglas que la norma no desarrolla, y en el "
                         "tema 7 uno da por buena una «seguridad informática» que la norma no "
                         "nombra—: van avisados debajo de su tabla.",
        aviso_portada="<p><b>Ninguna respuesta oficial de este bloque está mal.</b> Lo que sí "
                      "hay es <b>desigualdad de fuentes</b>, y el temario la dice: hay un tema "
                      "con las diez preguntas verificadas en documento y otro con cuarenta "
                      "preguntas de las que <b>quince</b> tienen documento y <b>veinticinco</b> "
                      "se apoyan sólo en la plantilla. Cada respuesta lleva <b>el nivel de su "
                      "fuente</b> escrito al lado.</p>",
    ),
    "informacion": dict(
        carpeta="informacion",
        rotulo="Temario específico · Información y Contenidos",
        ocupacion="Información y Contenidos",
        titulo="Temario específico",
        subtitulo="Los once temas de <b>Información y Contenidos</b>",
        pie="Oposiciones RTVE – Información y Contenidos",
        avisos=dict(AVISOS_INFORMACION, **AVISOS_PRL),
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), banco) for n, base, banco in [
            (1, "actualidad", "informacion-01"),
            (2, "union-europea", "informacion-02"),
            (3, "instituciones", "informacion-03"),
            (4, "codigo-menores", "informacion-04"),
            (5, "rdl-4-2018", None),
            (6, "manual-de-estilo", "informacion-06"),
            (7, "directiva-2018-1808", "informacion-07"),
            (8, "resolucion-parlamento-europeo", "informacion-08"),
            (9, "informe-unesco", "informacion-09"),
            (10, "carta-etica-fip", None),
        ]] + [TEMA_PRL],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque se puede dar por mal "
                         "contestada</b>, pero <b>una discrepa de su fuente estadística</b> y "
                         "<b>cinco enunciados están defectuosos</b> —uno nombra mal un "
                         "organismo, dos nombran mal el documento, otro apoya la respuesta en una "
                         "cifra que la norma no escribe, y en el tema 11 otro da por buena una "
                         "«seguridad informática» que la norma no nombra—: van avisados debajo de "
                         "su tabla.",
        aviso_portada="<p><b>Este bloque tiene dos temas sin una sola pregunta de examen</b> —el "
                      "del Real Decreto-ley 4/2018 y el de la Carta ética de la FIP—, y se "
                      "escriben igual, contra la norma y el documento, porque el programa los "
                      "manda. <b>Y tiene el tema más preguntado del proyecto</b>: ciento "
                      "veintiuna preguntas de actualidad, que no se estudian en una norma sino "
                      "que se comprueban dato a dato. <b>Cada respuesta lleva el nivel de su "
                      "fuente al lado</b>, y las que sólo se apoyan en la plantilla lo dicen. "
                      "<b>Ocho enunciados salen descolocados en el papel</b> —las cuatro letras "
                      "seguidas y después los textos—: es de la maquetación de los cuadernillos, "
                      "no cambia ninguna respuesta, y aquí las opciones van en su orden.</p>",
    ),
}

# La portada dice «Ocho temas», no «8 temas»: en una portada las cifras bajas se
# escriben con letra. Con dos bloques hay que generarlo, y no hace falta más que
# los números que este temario puede tener.
LETRA = {2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete",
         8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 13: "Trece",
         17: "Diecisiete", 18: "Dieciocho", 31: "Treinta y un"}


def con_letra(n):
    return LETRA.get(n, str(n))


md = MarkdownIt("commonmark").enable("table").enable("strikethrough")


def ruta_tema(carpeta, base):
    """Dónde vive un tema. Casi siempre, en la carpeta de su bloque; el de
    prevención, en la suya, porque lo comparten los tres bloques específicos y
    se escribe una sola vez."""
    return base if "/" in base else "%s/%s" % (carpeta, base)


def lee(ruta):
    return open(os.path.join(RAIZ, ruta), encoding="utf-8").read()


def sin_marcas(texto):
    """Quita las marcas HTML del generador de índices, no su contenido."""
    return texto.replace("<!-- portada -->", "").replace("<!-- /portada -->", "") \
                .replace("<!-- indice -->", "").replace("<!-- /indice -->", "")


def baja_titulos(texto, saltos=1):
    """Baja los encabezados N niveles: en el volumen el # es el tema."""
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * (len(m.group(1)) + saltos) + " ", texto)


def numera(texto, raiz):
    """Numera los epígrafes del tema y devuelve (texto, entradas del índice).

    Los temas traen la numeración escrita a mano y solo a veces: «1. Elaboración»
    la lleva y «Artículo 1. Estado, soberanía» no. Para que el índice y el cuerpo
    digan lo mismo se **quita la que venga escrita y se genera entera**, con el
    número del tema como raíz: 1, 1.1, 1.1.1. Cada epígrafe se queda además con
    un ancla, que es lo que hace el índice navegable y lo que luego permite saber
    en qué página ha caído.
    """
    cuenta = [0, 0, 0]
    entradas = []
    fuera = []
    for linea in texto.split("\n"):
        m = re.match(r"^(#{2,4}) (.+?)\s*$", linea)
        if not m:
            fuera.append(linea)
            continue
        nivel = len(m.group(1)) - 1          # h2 -> 1, h3 -> 2, h4 -> 3
        titulo = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", m.group(2))
        cuenta[nivel - 1] += 1
        for i in range(nivel, 3):
            cuenta[i] = 0
        numero = ".".join(str(x) for x in [raiz] + cuenta[:nivel] if True)
        ancla = "e" + numero.replace(".", "-")
        entradas.append((nivel, numero, titulo, ancla))
        fuera.append('%s <a id="%s"></a>%s %s' % (m.group(1), ancla, numero, titulo))
    return "\n".join(fuera), entradas


def preguntas(banco):
    """[(id, enunciado, respuesta)] del fichero del banco."""
    fuera = []
    for bloque in re.split(r"\n---\n", lee("banco/%s.md" % banco)):
        m = re.search(r"\*\*([^*]+?) · nº (\d+) · respuesta: ([^*]+)\*\*", bloque)
        if not m:
            continue
        ident = "%s · nº %s" % (m.group(1).strip(), m.group(2))
        cuerpo = re.search(r"```\n(.*?)```", bloque, re.S)
        if not cuerpo:
            continue
        fuera.append((ident, cuerpo.group(1).strip(), m.group(3).strip()))
    return fuera


CIERRA = re.compile(r"[.:;?!)]\s*$")


def ordena_opciones(enunciado):
    """Separa el enunciado de sus opciones: (enunciado, opciones, sin_texto).

    Al extraer el PDF las letras de opción quedan sueltas en su renglón. A veces
    cada una va justo encima de su texto; en otros cuadernillos salen **las
    cuatro seguidas y detrás los cuatro textos**, y además cada texto puede
    ocupar varios renglones. Pegar cada letra con el renglón siguiente juntaba
    «a) b)» y mandaba las respuestas al enunciado.

    Se lleva una cola de letras pendientes: un renglón **continúa** la opción
    abierta mientras esa opción no haya cerrado frase, y **abre** la siguiente
    cuando sí. De 504 preguntas, 502 salen con sus cuatro opciones. En las dos
    que no —opciones que el cuadernillo corta sin punto final— se devuelven las
    letras que se quedaron sin texto en vez de repartir a ojo, porque adivinar
    qué texto va con qué letra es enseñar mal justo lo que se va a memorizar.
    """
    lineas = [l.strip() for l in enunciado.split("\n") if l.strip()]
    if lineas and re.match(r"^\d+[.,\-]", lineas[0]):
        lineas[0] = re.sub(r"^\d+[.,\-]+\s*", "", lineas[0])
    cabeza, pendientes, opciones, abierta = [], [], [], False
    for linea in lineas:
        # el OCR dibuja la «c)» de doce preguntas como «Cc)», y con la letra sin
        # reconocer esa opción se fundía con la anterior
        if linea.startswith("Cc)") and [x[0] for x in opciones] == ["a", "b"]:
            linea = linea[1:]
        suelta = re.fullmatch(r"([a-d])\)", linea)
        pegada = re.match(r"^([a-d])\)\s+(.*)$", linea)
        if suelta:
            pendientes.append(suelta.group(1))
            abierta = False
            continue
        if pegada and not pendientes:
            opciones.append("%s) %s" % pegada.groups())
        elif abierta and opciones:
            opciones[-1] += " " + linea
        elif pendientes:
            opciones.append("%s) %s" % (pendientes.pop(0), linea))
        elif opciones:
            opciones[-1] += " " + linea
        else:
            cabeza.append(linea)
            continue
        abierta = not CIERRA.search(linea)
    return " ".join(cabeza).strip(), opciones, pendientes


def linea_indice(nivel, numero, titulo, ancla):
    """Un renglón del índice: número, título, línea de puntos y hueco de página.

    El hueco lo rellena `pdf.py` en una segunda pasada, cuando ya sabe en qué
    página ha caído cada ancla: el motor que compone el PDF no sabe contar
    páginas desde el documento, así que hay que componerlo, mirarlo y volver a
    componerlo.
    """
    return ('<div class="ii n%d"><a href="#%s"><span class="it">%s %s</span>'
            '<span class="pun"></span><span class="ip" data-ref="%s"></span></a></div>'
            % (nivel, ancla, numero, html.escape(titulo), ancla))


def pinta_pregunta(n, enunciado):
    cabeza, opciones, sin_texto = ordena_opciones(enunciado)
    cuerpo = "<b>%s</b>" % html.escape(cabeza) if cabeza else ""
    for o in opciones:
        cuerpo += '<div class="opcion">%s</div>' % html.escape(o)
    if sin_texto:
        cuerpo += ('<div class="suelta">El cuadernillo corta estas opciones sin punto '
                   'final, así que la transcripción no marca dónde acaba cada una y '
                   '<b>%s se queda sin texto</b>. Se imprime como salió: repartirlo a ojo '
                   'sería inventar.</div>'
                   % ", ".join("la %s)" % l for l in sin_texto))
    return ('<div class="pregunta"><div class="pnum">%d</div>'
            '<div class="ptexto">%s</div></div>' % (n, cuerpo))


CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.5 "Georgia","Times New Roman",serif; color:#111; margin:0;
       hyphens:auto; -webkit-hyphens:auto; text-align:justify; }
h1,h2,h3,h4,h5,th,td,.pnum,.rotulo { text-align:left; }
.portada-vol, .portada-vol h1, .portada-vol .rotulo, .portada-vol .sub,
.portada-vol .meta { text-align:center; }
h1,h2,h3,h4,h5 { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; line-height:1.25;
                 page-break-after:avoid; break-after:avoid; }
h1 { font-size:20pt; margin:0 0 .2em; }
h2 { font-size:14pt; margin:1.6em 0 .5em; padding-bottom:.15em; border-bottom:1.5px solid #111; }
h3 { font-size:11.5pt; margin:1.2em 0 .35em; }
h4 { font-size:10.5pt; margin:1em 0 .3em; font-style:italic; }
p, li { orphans:3; widows:3; }
ul,ol { padding-left:1.3em; margin:.4em 0; }
li { margin:.15em 0; }
table { border-collapse:collapse; width:100%; margin:.7em 0; font-size:9pt;
        page-break-inside:avoid; break-inside:avoid; }
th,td { border:.5px solid #999; padding:3px 5px; text-align:left; vertical-align:top; }
th { background:#e4e4e4; }
/* la primera fila de toda tabla va en gris, lleve cabecera o no */
table tr:first-child > td { background:#e4e4e4; }
code { font-family:"SF Mono",Menlo,Consolas,monospace; font-size:8.5pt; background:#f2f2f2;
       padding:0 2px; }
blockquote { margin:.8em 0; padding:.5em .9em; border-left:3px solid #888; background:#f7f7f7;
             font-size:9.5pt; }
blockquote p { margin:.3em 0; }
hr { border:0; border-top:.5px solid #bbb; margin:1.4em 0; }

.portada-vol { height:245mm; display:flex; flex-direction:column; justify-content:center;
               text-align:center; page-break-after:always; }
.portada-vol h1 { font-size:30pt; border:0; margin-bottom:.1em; }
.portada-vol .sub { font-size:13pt; color:#444; margin-bottom:2.5em; }
.portada-vol .meta { font-size:10pt; color:#333; line-height:2; }
.aviso { page-break-after:always; }
.aviso .caja { border:1.5px solid #111; padding:12px 16px; margin:1.2em 0; }
.indice-gral { page-break-after:always; }
.indice-gral a { color:inherit; text-decoration:none; display:block; }
.ii { display:block; margin:0; }
.ii a { display:flex; align-items:baseline; }
.ii .it { flex:0 1 auto; }
.ii .pun { flex:1 1 auto; border-bottom:1px dotted #bbb; margin:0 .4em .18em .4em;
           min-width:1.2em; }
.ii .ip { flex:0 0 auto; font-variant-numeric:tabular-nums; color:#333; }
.ii.n0 { font-weight:bold; font-size:11pt; margin:.75em 0 .15em; page-break-after:avoid; }
.ii.n1 { font-size:9.8pt; margin-left:1.1em; }
.ii.n2 { font-size:9.2pt; margin-left:2.4em; color:#444; }
.ii.n3 { font-size:8.8pt; margin-left:3.7em; color:#666; }

.tema { page-break-before:always; }
.tema > h1 { border-bottom:3px solid #111; padding-bottom:.25em; margin-bottom:.8em; }
.rotulo { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; font-size:8.5pt;
          letter-spacing:.12em; text-transform:uppercase; color:#666; margin:0 0 .3em; }
.ficha table { font-size:8.5pt; }
.ficha th, .ficha td { border:0; border-bottom:.5px solid #ddd; }
.parte { page-break-before:always; }
.parte h2 { border-bottom:3px double #111; font-size:16pt; }
.esquema { font-size:9.5pt; }
.esquema h2 { font-size:12pt; }
.esquema h3 { font-size:10pt; }

.pregunta { display:flex; gap:8px; margin:.55em 0; page-break-inside:avoid;
            break-inside:avoid; font-size:9.5pt; }
.pnum { flex:0 0 26px; font-family:Helvetica,Arial,sans-serif; font-weight:bold;
        font-size:9pt; color:#fff; background:#111; height:20px; text-align:center;
        line-height:20px; }
.ptexto { flex:1; }
.suelta { border-left:3px solid #999; padding:3px 8px; margin-top:4px; font-size:8pt;
          color:#555; font-style:italic; text-align:left; }
.errata { border-left:3px solid #111; background:#f0f0f0; padding:5px 9px; margin:6px 0;
          font-size:9pt; }
/* el solucionario alterna: fila de números en gris, fila de letras en blanco */
table.claves { font-size:10pt; margin:.4em 0 1.2em; }
table.claves th, table.claves td { text-align:center; width:10%; }
table.claves th { background:#e4e4e4; font-weight:bold; }
table.claves td { background:#fff; font-weight:bold; }
.opcion { margin-left:1.1em; text-indent:-1.1em; }
@media screen { body { max-width:190mm; margin:0 auto; padding:16mm 10mm; background:#fff; } }
"""


def main():
    argv = sys.argv[1:]
    clave = argv[0] if argv and argv[0] in BLOQUES else "general"
    argv = argv[1:] if argv and argv[0] in BLOQUES else argv
    B = BLOQUES[clave]
    salida = argv[0] if argv else "libro-%s.html" % clave
    TEMAS = [list(x) for x in B["temas"]]

    partes, indice_gral, total_preg = [], [], 0
    for i, (base, banco) in enumerate(B["temas"], 1):
        crudo = sin_marcas(lee("temas/%s.md" % ruta_tema(B["carpeta"], base)))
        titulo = re.search(r"(?m)^# (.+)$", crudo).group(1)
        cuerpo = re.sub(r"(?m)^# .+$\n", "", crudo, count=1)
        # fuera el índice del propio tema: el volumen lleva el suyo
        cuerpo = re.sub(r"## Índice\n.*?(?=\n## )", "", cuerpo, flags=re.S)
        ficha, resto = "", cuerpo
        mt = re.match(r"\s*(\|.*?\|)\n\n", cuerpo, re.S)
        if mt:
            ficha = md.render(mt.group(1))
            resto = cuerpo[mt.end():]

        esquema = sin_marcas(lee("esquemas/%s.md" % ruta_tema(B["carpeta"], base)))
        esquema = re.sub(r"(?m)^# .+$\n", "", esquema, count=1)
        esquema = re.sub(r"## Índice\n.*?(?=\n## )", "", esquema, flags=re.S)

        resto, entradas = numera(resto, i)
        indice_gral.append((i, titulo, entradas))

        bloque = ['<section class="tema" id="tema-%d">' % i]
        bloque.append('<p class="rotulo">%s</p>' % html.escape(B["rotulo"]))
        bloque.append("<h1>TEMA %d – %s</h1>"
                      % (i, html.escape(titulo.split("·", 1)[-1].strip())))
        if ficha:
            bloque.append('<div class="ficha">%s</div>' % ficha)
        bloque.append(md.render(baja_titulos(resto, 0)))
        bloque.append('<section class="parte esquema"><h2>Esquema de repaso · tema %d</h2>%s</section>'
                      % (i, md.render(esquema)))
        if banco:
            ps = preguntas(banco)
            total_preg += len(ps)
            rot = ("Preguntas reales de examen · temas 2 y 3" if banco == "g2-g3"
                   else "Preguntas reales de examen · tema %d" % i)
            bloque.append('<section class="parte"><h2>%s</h2>' % rot)
            bloque.append("<p><i>%d preguntas de los cuadernillos de 2024. "
                          "Las respuestas, al final del volumen.</i></p>" % len(ps))
            bloque.append("".join(pinta_pregunta(n, e)
                                  for n, (_, e, _) in enumerate(ps, 1)))
            bloque.append("</section>")
            TEMAS[i - 1] = [base, banco, ps]
        bloque.append("</section>")
        partes.append("\n".join(bloque))

    # ── apéndice de respuestas ────────────────────────────────────────────────
    resp = ['<section class="tema"><p class="rotulo">Apéndice</p>'
            '<h1>Respuestas oficiales</h1>',
            "<p>La respuesta es la de la <b>plantilla oficial</b> del examen, y el número "
            "es el que la pregunta lleva impreso en su tema. "
            + B["aviso_respuestas"] + "</p>"]
    for i, t in enumerate(TEMAS, 1):
        if len(t) < 3:
            continue
        base, banco, ps = t
        rot = "Temas 2 y 3" if banco == "g2-g3" else "Tema %d" % i
        resp.append("<h2>%s</h2>" % rot)
        # la respuesta se busca por el número con el que la pregunta está impresa;
        # el cuadernillo del que salió ya no se imprime, que al opositor no le dice nada
        sueltas = [(n, r) for n, (_, _, r) in enumerate(ps, 1)]
        erratas = [(n, B["avisos"][ident]) for n, (ident, _, _) in enumerate(ps, 1)
                   if ident in B["avisos"]]
        filas, POR_FILA = [], 10
        for a in range(0, len(sueltas), POR_FILA):
            trozo = sueltas[a:a + POR_FILA]
            filas.append("<tr>%s</tr><tr>%s</tr>"
                         % ("".join("<th>%d</th>" % n for n, _ in trozo),
                            "".join("<td>%s</td>" % html.escape(r) for _, r in trozo)))
        resp.append('<table class="claves">%s</table>' % "".join(filas))
        for n, texto in erratas:
            resp.append('<div class="%s"><b>%s %d:</b> %s</div>'
                        % (B["clase_aviso"], B["rotulo_aviso"], n, texto))
    resp.append("</section>")

    ig = []
    for i, t, entradas in indice_gral:
        ig.append(linea_indice(0, "TEMA %d –" % i, t.split("·", 1)[-1].strip(),
                               "tema-%d" % i))
        for nivel, numero, titulo, ancla in entradas:
            ig.append(linea_indice(nivel, numero, titulo, ancla))

    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<!-- pie: {B["pie"]} -->
<title>{B["titulo"]} · Oposiciones RTVE</title><style>{CSS}</style></head><body>
<section class="portada-vol">
  <p class="rotulo">Oposiciones RTVE · convocatorias 1/2022 y 3/2022</p>
  <h1>{B["titulo"]}</h1>
  <p class="sub">{B["subtitulo"]}</p>
  <div class="meta">
    Redacción vigente a <b>{CORTE}</b><br>
    {con_letra(len(TEMAS))} temas · {con_letra(len(TEMAS)).lower()} esquemas de repaso · <b>{total_preg}</b> preguntas reales de examen<br>
    Generado el {date.today().strftime('%d/%m/%Y')}
  </div>
</section>

<section class="aviso">
<h1>Cómo usar este volumen</h1>
<div class="caja">
<p><b>La redacción que vale es la del {CORTE}</b>, que es la fecha de corte que
imponen las bases: «las pruebas se realizarán sobre su texto vigente a fecha de la primera
publicación de las Bases Generales». Lo que cambió después está en el tema, en apartados
marcados como <i>notas de actualización</i>, y <b>no es materia examinable</b>.</p>
</div>
<p><b>Cada tema trae tres partes.</b> El <b>cuerpo</b>, para leer; el <b>esquema</b>, para
repasar, que va detrás y no delante a propósito; y las <b>preguntas reales</b> de los
cuadernillos de 2024, para comprobar si el tema se sostiene. <b>Las respuestas están al final
del volumen</b>, no junto a la pregunta: con la respuesta a la vista no hay autoevaluación.</p>
{B["aviso_portada"]}
<p><b>Las preguntas se imprimen tal como salieron del examen</b>, sin más limpieza que
quitarles el pie de página. Son transcripciones de los cuadernillos oficiales y traen sus
costuras: alguna arrastra una letra mal reconocida. <b>Están leídas una a una</b> y colocadas
en el tema que les toca, comprobando cada una contra la norma.</p>
<p><b>Nada de aquí se ha escrito de memoria.</b> Cada dato se ha leído en el texto consolidado
del BOE en su redacción a la fecha de corte, o en la fuente oficial que se cita en la
trazabilidad de cada tema.</p>
</section>

<section class="indice-gral"><h1>Índice general</h1><ol>{''.join(ig)}</ol></section>

{''.join(partes)}
{''.join(resp)}
</body></html>"""

    # si una errata deja de casar con su pregunta, desaparece del apéndice sin
    # decir nada: el volumen volvería a dar por buena una plantilla que está mal
    sueltas = set(B["avisos"]) - {i for t in TEMAS if len(t) > 2 for i, _, _ in t[2]}
    if sueltas:
        print("  ! erratas sin pregunta a la que pegarse: %s" % ", ".join(sorted(sueltas)))

    ruta = os.path.join(RAIZ, salida)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("· %s · %d KB · %d temas · %d preguntas"
          % (salida, len(doc) // 1024, len(TEMAS), total_preg))


if __name__ == "__main__":
    main()
