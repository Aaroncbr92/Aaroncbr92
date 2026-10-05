# Puesto 27 · Oficial Técnico Electricista · Tema 6 · Fase 5, remate

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/06-alumbrado-interior-exterior-y-de-emergencia.md`.
Entrada: `27-T06-refutacion.md` (0 graves, 3 menores, 3 lagunas y la pregunta 12) y `27-T06-preguntas.md`.
Fecha de trabajo y de lectura de las fuentes: 05-10-2026 (el encargo fija «hoy» en 24-09-2026).
Copia previa del tema en el scratchpad de la sesión (`27t06-antes-remate.md`).

**Resultado: se amplía contenido nuevo** (epígrafe 2.5 y la periodicidad de las pruebas de emergencia
en 5.2). De unas 12.560 a unas 15.700 palabras (`wc -w`); portada corregida a «Unas 15.000 palabras».

Ficheros tocados: el tema, este informe y un volcado nuevo de fuente,
`fuentes/canal-sur/DOUE-L-2019-81880.md` y `fuentes/canal-sur/DOUE-L-2020-80257.md` (corrección de
errores), sacados con `doue.py`. Nada más. (Los cambios que `git status` muestra en los temas 07 y 08
del puesto no son de este remate.)

## Fuentes nuevas leídas el 05-10-2026

| Fuente | Cómo | Para qué |
|---|---|---|
| Reglamento (UE) 2019/2020 (DOUE-L-2019-81880), con su corrección (DOUE-L-2020-80257) | `doue.py`; artículos 1, 2, 11 y anexo I | Definiciones de incandescencia, halógena, fluorescente, HID, sodio a alta presión, halogenuros metálicos, LED, CRI, CCT, mecanismo de control |
| Reglamento (UE) 2021/341 (DOUE-L-2021-80227), que modifica el anterior | `doue.py` al scratchpad; artículo 4 y anexo IV | Comprobar que no toca las definiciones citadas: en el artículo 2 sólo sustituye el punto 4; en el anexo I, sólo el punto 52. La ficha del BOE no lista otras modificaciones |
| RD 842/2002, ITC-BT-01 (clases 0, I, II, III; doble aislamiento; masas) e ITC-BT-30, 1.3 | `boe.py precepto` / `grep` del volcado; redacción única vigente | Laguna L3 |
| RD 1890/2008, artículo 3 (definiciones) | volcado del BOE | Laguna L1 |
| DB HE, anejo A (eficacia luminosa, iluminancia, Ra, equipo auxiliar, luminaria) y HE 3, 1.3 y tabla 3.1 | `DBHE.txt` de la verificación | L1, L2 y menores 1 y 2 |
| IDAE, Guía técnica de eficiencia energética en iluminación. Oficinas (Guía 010, junio de 2019) | PDF de idae.es pasado con `documento.py texto`; leídos 5.4 y capítulo 6 | Tonos de luz, valoración del Ra, código 840/930, datos orientativos de lámparas, balasto, arrancador, cebador |
| Zemper, página técnica de 04-11-2021 sobre mantenimiento del alumbrado de emergencia | `curl` y texto limpio | Pregunta 12 |

## Correcciones de la refutación

1. **Menor 1 (HE 3, 1.3) · aplicada.** Comprobado en el DB HE: la letra a) tiene dos supuestos y existen
   las letras c) y d). Pasaje cambiado en 3.1 (ámbito en intervenciones):
   > se aplica a todo el edificio en dos casos: cuando, con superficie útil final **«superior a 1000
   > m2»**, **«se renueve más del 25% de la superficie iluminada»**, y en los **«cambios de uso
   > característico»** (letra a). Si sólo se renueva o amplía una parte, se adecúa esa parte (letra b);
   > si la renovación afecta a zonas en las que son obligatorios los sistemas de control o regulación,
   > **«se dispondrá de estos sistemas»** (letra c); y un cambio de actividad en una zona que lleve a un
   > VEEI límite más bajo que el de la actividad inicial obliga a adecuar la instalación de esa zona
   > (letra d).
2. **Menor 2 (dos filas de zonas comunes) · aplicada.** Comprobado en la tabla 3.1-HE3: «Zonas comunes»
   (4,0, nota 4) y «Zonas comunes en edificios no residenciales» (6,0, sin nota); ninguna regla de
   prelación escrita. Párrafo nuevo en 3.1, tras la tabla, con la nota (4) literal y la frase: «El DB no
   escribe cuál prevalece para un pasillo de un edificio de oficinas o de producción [...]; la fila la
   elige y la justifica el proyecto. El tema no resuelve lo que la tabla deja abierto.» En 1.6, la fila
   de pasillos dice ahora «VEEI de una de las dos filas de zonas comunes de la tabla del DB HE 3
   (epígrafe 3.1)». La pregunta 15 queda contestada en lo que la fuente permite: el tema dice por qué
   no hay una única respuesta.
3. **Menor 3 (negrita del anexo IV.4) · aplicada.** Cotejado palabra por palabra con el BOE
   (RD 486/1997, anexo IV, apartado 4, letras a a e): literal. Puesto en negrita, con el mismo formato
   que la cita de los apartados 5 y 6.

## Lagunas: ampliación

**Epígrafe nuevo 2.5 «Magnitudes, fuentes de luz y clases de protección»** (unas 2.250 palabras), al
final de «2. Luminarias», con una frase de entrada bajo la rúbrica 2 que remite a él. Se puso al final
y no al frente para no renumerar los epígrafes 2.1 a 2.4, a los que remite el resto del tema. Contiene:

- **L1 · Magnitudes** (preguntas 7 y 8). Tabla con flujo, intensidad, iluminancia, luminancia, eficacia
  luminosa, rendimiento de la luminaria (RD 1890/2008, art. 3, y DB HE, anejo A, literales), temperatura
  de color correlacionada (Reglamento 2019/2020, anexo I) e índice de rendimiento de color (DB HE y
  Reglamento 2019/2020, art. 2.11). Cadena de magnitudes y ejemplo 1.000 lm / 10 m² = 100 lux, como
  oficio. Tonos cálido / neutro / frío de la guía del IDAE, con la discrepancia interna de la guía
  declarada (5.300 K en la tabla 4, 5.000 K en el capítulo 6); valoración del Ra; código 840/930.
- **L2 · Fuentes de luz** (preguntas 8 y 13). Tabla incandescente, halógena, fluorescente, HID y LED con
  la definición del Reglamento 2019/2020 y los datos orientativos de la guía del IDAE; sodio a alta
  presión y halogenuros metálicos definidos; sodio a baja presión según el IDAE. Lectura propia,
  declarada: las «lámparas de descarga» de las ITC-BT son las fluorescentes y las HID; el vapor de
  mercurio (36-59 lm/W) no llega a los 65 lm/W de la ITC-EA-04. Equipo auxiliar: definición del DB HE y
  función de balasto, arrancador, cebador, condensador y equipo electrónico según el IDAE, enlazada con
  la compensación a 0,9 y la resistencia de descarga de la ITC-BT-44.
- **L3 · Clases de protección** (pregunta 9). Definiciones literales de la ITC-BT-01 (clases 0, I, II,
  III y doble aislamiento) y lo que hacen con ellas la ITC-BT-44, la ITC-BT-09, la ITC-BT-30 (1.3) y la
  definición de masas.

**Pregunta 12 · ampliada en 5.2**, con el pasaje:
> Un fabricante de luminarias de emergencia, en documentación técnica publicada en 2021, atribuye a las
> normas UNE-EN 50172 (todos los sistemas) y UNE-EN 62034 (sistemas de ensayo automático) esta
> periodicidad: **«Test funcional: Al menos, una vez al mes»** y **«Test de autonomía: Al menos, una vez
> al año»**, con un libro de registro [...]. Esas dos normas UNE no se han leído: la periodicidad es la
> que el fabricante dice que fijan, no un precepto del REBT ni de ninguna otra norma del BOE.

La refutación pedía fuente publicada antes de dar cifras: es documentación de fabricante, que el
encargo admite como fuente técnica, y así se declara. La periodicidad de cambio de baterías no se ha
encontrado y sigue en «Lo que este tema no da».

## Otros pasajes cambiados

- **2.4**, primera frase: «Ninguna de las normas leídas» pasa a «Ninguna de las normas de instalación
  leídas», y se añade que el Reglamento (UE) 2019/2020 define el LED pero es norma de producto (su
  artículo 1 regula la «introducción en el mercado»). Sin el cambio, la frase quedaba falsa tras leer
  ese reglamento.
- **Portada**: Fuente (ITC-BT-01 y 30, Reglamento 2019/2020, guía del IDAE, fabricante), Redacción
  (Reglamento 2019/2020 con su corrección y la modificación de 2021/341), Extensión.
- **Siglas**: OLED, HID, CCT/Tc, IDAE; unidades lm, cd, K.
- **Qué se puede preguntar**: una frase sobre magnitudes, color, lámparas, equipos y clases.
- **Lo que este tema no da**: la viñeta de la periodicidad de las pruebas, reescrita; viñeta nueva sobre
  el carácter orientativo de los datos del IDAE y la serie UNE-EN 60598 no leída.
- **Normativa que el tema invoca**: REBT con ITC-BT-01 y 30; RD 1890/2008 con artículo 3; fila nueva
  del Reglamento (UE) 2019/2020; UNE-EN 50172 y 62034 en la nota de normas UNE.
- **Trazabilidad**: filas del REBT, RD 1890/2008 y DB HE ampliadas a 2.5; filas nuevas del Reglamento
  2019/2020, guía del IDAE y fabricante; lista de oficio ampliada.

## Para el 5 bis y para quien corrija la fuente

- **La fuente no cuadra con la lógica, y manda la fuente.** La ITC-BT-01, en su texto del BOE
  (redacción única, comprobada con `boe.py precepto`), define el material de clase III como aquel en
  que la protección **«no se basa en la alimentación a muy baja tensión»**. La negación contradice la
  idea de la clase. El tema la cita literal, lo dice y sólo afirma el límite de 50 V c.a. / 75 V c.c.
- La guía del IDAE trae errores que no se han copiado (espectro visible «308-780 nm»; etiquetado según
  el Reglamento Delegado 874/2012, ya derogado).

## Lentes

Comparadas antes y después del remate, con RD 842/2002, RD 1890/2008, RD 486/1997, RD 513/2017,
Reglamento 2019/2020, DB HE, DB SUA, guía del IDAE y página del fabricante como fuentes:

- `indice.py`: índice regenerado, 32 epígrafes, 2.5 incluido.
- `negritas.py`: 394 negritas cotejadas (319 antes); ninguna nueva que falte en la fuente. Dos avisos
  nuevos de «otro artículo», falsos: el anexo I del Reglamento 2019/2020 cuelga en el volcado del
  artículo 11, y «lámparas de descarga» es una expresión genérica.
- `refutar_exactitud.py`: 9 avisos nuevos de «no literal», todos falsos: citan apartados de ITC
  (ITC-BT-09, 30) o la guía del IDAE junto a un «artículo 2» del reglamento europeo; las nueve citas
  las encuentra `negritas.py` literales en su fuente.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: sin diferencias respecto de antes.

Releídos los pasajes cambiados: «la misma ITC» (2.5) tiene delante la ITC-BT-01; «esas dos normas
UNE» (5.2), las UNE-EN 50172 y 62034; «ese condensador» (2.5), el del equipo electromagnético recién
citado.
