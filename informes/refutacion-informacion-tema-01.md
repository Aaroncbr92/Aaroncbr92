# Refutación del tema 1 del específico de Información y Contenidos

**Ciento veintiuna preguntas y ninguna norma que las gobierne.** La refutación de este tema no podía
consistir en contrastar un texto contra su fuente, porque no hay **una** fuente: consistió en
**buscar ciento veintiuna veces**, anotar **qué se encontró y qué no**, y **comprobar una a una las
citas literales** que el tema pone entre comillas.

## Qué lente sirve aquí, y cuál no

**Las lentes por artículo no sirven.** `refutar_exactitud.py` y `refutar_modo.py` trocean el tema por
artículos y contrastan cada trozo con su precepto. Este tema **no está organizado por artículos** —lo
está por materias— y sus fuentes son, en su mayoría, órdenes de una sola disposición. Ejecutadas
sobre él devuelven **«0 negritas comprobadas, 0 no literales»**, que es exactamente el fallo del
apartado 10 del manual: **una lente que devuelve cero se lee como un tema impecable y en realidad es
un tema sin mirar**. Por eso se dice aquí, en vez de imprimir el cero.

**La de documento y la de prosa sí sirven, y son las que se corrieron.**

## Lente de documento

Contra **las veintitrés fuentes reunidas** en `fuentes/informacion/`: **379 negritas comprobadas**,
**264 no literales** y **1 cifra huérfana**.

**Las 264 no literales son la prosa del propio tema**, que en este proyecto va en negrita: los
titulares de epígrafe, las advertencias y las respuestas oficiales que el tema enuncia con sus
palabras. Es la proporción normal en un tema de este tipo —el tema 6 de Documentación dio 349 de
447—, y **lo que importa no es el número, sino que las citas literales sí lo sean**. Eso se comprobó
aparte, y va abajo.

**La única cifra huérfana es un falso positivo**: el «77» de «La tasa de paro (31, nº 77)», que es
**el número de la pregunta en el cuadernillo**, no un dato. La lente no distingue una cosa de otra.

**Cuatro cifras huérfanas que sí lo eran se corrigieron**, y merece la pena contarlo porque son el
tipo de fallo que nadie ve:

| Cifra | Dónde | Qué pasaba | Qué se hizo |
|---|---|---|---|
| **838** | «RD 838/2024» | Se citaba el real decreto de cese **sin haberlo descargado**: salía en el listado del buscador y de ahí a la página | Se descargó y se guardó con los demás |
| **141** | «BOE núm. 141, de 11 de junio de 2024» | El precepto volcado con `boe.py` **no trae la referencia de publicación**, sólo el texto del artículo | Se añadió la ficha de publicación de la ley |
| **19** | «Ley 20/2022, de 19 de octubre» | La ley se citaba en la trazabilidad **sin estar en el corpus** | Se descargó su ficha |

**La regla que sale de aquí**: **volcar un precepto no es volcar la norma**. `boe.py precepto` da el
artículo y su cadena de redacciones, que es lo que hace falta para estudiar; **no da el número del
boletín ni la fecha de publicación**, que es justo lo que preguntaba una de las preguntas de este
tema. Quien cite una fecha de publicación tiene que traerse **también** la ficha del documento.

## Lente de prosa

**Cero hallazgos**, después de una corrección. La primera pasada dio **veinte siglas sin presentar**,
y al mirarlas una a una resultó que **ninguna era un falso positivo**: eran siglas de partidos
(PSOE, PP, PSC, ERC, PNV, EH), de organismos (ONU, UEFA, FMI), de estadística (IPC, NFT, FTSE MIB) y
—las más interesantes— **los códigos de departamento de las órdenes ministeriales**: CLT, CUD, CIN y
TER.

**Ese último grupo enseña algo que el tema no sabía que tenía que contar.** El número de una orden
—«Orden CLT/1124/2024»— lleva dentro **el código del ministerio que la firma**, y en este tema
aparecen cuatro porque el Ministerio de Cultura **cambió de código** entre 2023 y 2024: las órdenes
de 2023 son **CUD** y las de 2024, **CLT**. Un lector que busque «Orden CUD» en 2024 no encuentra
nada. Eso está ahora presentado en la cabecera del tema.

## La comprobación que ninguna lente hace: las citas literales

**Las citas de este tema van en bloque de cita, no en negrita**, y la lente de documento sólo mira
negritas. Así que se comprobaron **a mano y con una comprobación programada aparte**: cada fragmento
entre comillas del tema, normalizado, buscado en el texto completo de las fuentes.

- **Diez bloques de cita**, todos literales: la disposición final de la ley de amnistía, su artículo
  2.c), el artículo 1.3.a) de la ley de animales, la frase del INE sobre la tasa de paro, las cuatro
  concesiones de premios, las dos frases de la orden que suprime el Premio de Tauromaquia y la
  definición de fines de la Fundación Princesa de Asturias.
- **Las citas en línea** se comprobaron contra las fuentes **y contra los propios cuadernillos**,
  porque muchas son enunciados y títulos de obras que sólo están ahí. Dos no cuadraban y se
  arreglaron:
  - **«L'hymne à l'amour»**. El tema escribía el título francés bien; **el cuadernillo lo imprime
    "L'hymme à l'amour"**, con erre de más. Corregir la grafía dentro de las comillas habría sido
    **reescribir el examen**. Se cita como está y se advierte de la grafía.
  - **«Amar en tiempos revueltos»**. El tema afirmaba que «Amar es para siempre» continúa esa serie
    anterior. **Eso no salía de ninguna fuente: salía de saberlo.** Se quitó, y en su lugar el tema
    explica por qué la pregunta de «la serie más longeva» es discutible **sin afirmar de qué serie
    viene cuál**.

**La segunda es la corrección que importa**, porque es un caso puro del apartado 1 del manual: un
dato verdadero, escrito de memoria, colado dentro de un tema que presume de citar. La lente de
documento no lo habría cogido nunca —no era una negrita— y la de prosa tampoco. **Lo cogió una
comprobación hecha a propósito para este tema**, y por eso queda escrita aquí.

## La discrepancia con la plantilla

**La tasa de paro del segundo trimestre de 2024.** La respuesta oficial es **11,4 %**; el INE publica
**11,27 %** en la nota de prensa de la EPA de ese trimestre, de 26 de julio de 2024.

**Se aplicó el apartado 5 del manual —el que detecta se equivoca— y la sospecha no se sostuvo**:

1. **¿Es el trimestre correcto?** Sí: la nota se titula «Encuesta de población activa (EPA). Segundo
   trimestre 2024».
2. **¿Está la cifra bien leída?** Sí, y la propia nota la comprueba sola: «**11,27 % este trimestre,
   1,02 puntos menos que en el anterior**», y 11,27 + 1,02 = 12,29, que es la tasa del primer
   trimestre.
3. **¿Pregunta el enunciado por otra tasa?** No dice de quién es la tasa. En España, «la tasa de
   paro» de un trimestre es la de la EPA.
4. **¿Hay alguna serie que dé 11,4 %?** Podría darlo una serie mensual desestacionalizada distinta
   de la EPA trimestral. **Eso es una conjetura y no una fuente**, y como conjetura se escribe.

**Decisión**: el tema **enseña el 11,27 % del INE** y deja constancia de que la respuesta oficial es
otra. No se corrige la plantilla —no se puede— pero tampoco se escribe en un temario un dato que su
fuente desmiente.

**Es la primera vez en el proyecto que una fuente estadística, y no una norma, desmiente una
respuesta oficial.** Las tres erratas de plantilla anotadas hasta ahora en `PENDIENTES.md` eran de
derecho: un título de la Constitución, un artículo de la Ley 17/2006 y una escala de la Ley 31/1995.

## Los dos enunciados descolocados

**No cambian la respuesta, pero hacen ilegible el papel.** El «Proyecto Viena» (cuadernillo 33,
nº 45) y el Premio Novela Café Gijón (33, nº 43) imprimen **las cuatro letras seguidas —«a) b) c)
d)»— y después los cuatro textos**, y el segundo además parte las frases por la mitad, de modo que en
el papel se lee «Ganadora, cuándo' de María Elena Morán». **Las opciones van en orden de aparición**,
y así se dice en el tema y se imprimirá con las respuestas del volumen.

## Lo que queda sin comprobar, y por qué

**Ciento una preguntas**, listadas en el epígrafe 9 del tema y razonadas grupo a grupo en el informe
de cobertura. **No es lo mismo no encontrar que no buscar**, y aquí se buscó: la búsqueda por título
en el BOE se corrió sobre todo lo que podía estar publicado —premios, nombramientos, leyes citadas—
y lo que apareció está verificado. Lo que no aparece es porque **no lo publica ningún organismo
español**: son informes privados, premios extranjeros y hechos de prensa internacional.
