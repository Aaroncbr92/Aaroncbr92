# Puesto 28 · Operador/a de Sonido · Tema 6 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/06-captacion-de-sonido.md`.
Fecha de lectura de todas las fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026).

## Fuentes releídas

| Fuente | Cómo | Fecha |
|---|---|---|
| Shure, C. Lyons, *Audio Systems Guide for Video and Film Production* (©2013/©2014) | PDF original de content-files.shure.com, pasado a texto con `documento.py` | 25-09-2026 |
| Shure, T. Vear, *Selection and Operation of Wireless Microphone Systems* (©2014) | `fuentes/canal-sur/sonido/shure-selection.txt` | 25-09-2026 |
| EBU Tech 3343-2023 | `fuentes/normas-tecnicas/EBU_Tech3343-2023.txt` y su PDF (página del recuadro) | 25-09-2026 |
| EBU Tech 3326 Rev. 4 (nov. 2014) | PDF de tech.ebu.ch, pasado a texto | 25-09-2026 |
| EBU Tech 3347 Rev. 1 (oct. 2012) | PDF de tech.ebu.ch, pasado a texto | 25-09-2026 |
| Clear-Com, *Interruptible Fold Back, AKA IFB* (3/16/2021) | Página web del fabricante | 25-09-2026 |
| EBU R 128-2023 y EBU R 68-2000 | `fuentes/normas-tecnicas/` (sólo los puntos citados) | 25-09-2026 |
| BOJA núm. 186, anexo I | `convocatoria/canal-sur/2026-bases-boja-186.txt`, filas del puesto | 25-09-2026 |

## Pasajes exentos (comprobación sólo de literalidad)

- **Copiado del común** (Cámara 06, 03 y 10), puntos 1-8: cada párrafo y fila es subcadena exacta
  del tema de Cámara (script, sin saltos de línea); el 6 lo es hasta «…posible.»**, como declaró el
  redactor. Las citas del Libro de estilo, de DPA y de Tech 3343 («greater headroom») de los puntos
  9-13 también están literales en Cámara. No se re-verifican.
- **Copiado de RTVE sin cambios**, puntos 1-7: todos los párrafos, filas y puntos listados son
  subcadena del RTVE correspondiente quitando `**` y ✔. No se re-verifican.

## Verificado y confirmado

- 40 citas en negrita de Shure, Tech 3343, Tech 3326, Tech 3347 y Clear-Com cotejadas por script: todas
  literales (dos, «voice-activated» y «Latency is an issue.», partidas por salto de línea o de página;
  comprobadas a mano).
- Tech 3343: § 3.5.1 (goles, −24 LUFS, golf), § 3.5.2 (público, música, +3/−5 LU, 1-2 dB), § 3.1
  («greater headroom»). Tech 3326 § 1.2 (tipos de contribución). Tech 3347 § 1.2 («Intercom use
  cases», «3. commentary feed»). Títulos, revisiones y fechas de las tres.
- R 128: ±1,0 LU cuando el objetivo no es alcanzable en la práctica («for example, live programmes»).
- Shure: contexto de cada cita (entrevista en movimiento, dos corbatas para conversación larga, regla
  de 3 a 1 con su ejemplo de 1 → 3 pies, doble corbata del «news anchor», nivel y pista de seguridad).
  Cálculos: 30 → 90 cm; 20 pies ≈ 6,1 m.
- Clear-Com: definición del IFB y sus tres elementos; IFB en deportes; fecha 16-03-2021.
- Remisiones a los temas 3, 5, 7, 8, 9, 10, 11, 12, 13, 15 y 16: cada uno trata lo remitido (grep).

## Correcciones aplicadas (11)

1. **Grupos de frecuencias (error 9)**: «dos emisores… pueden interferirse… porque sus armónicos y sus
   productos de intermodulación caen encima del otro» no lo dice ninguna fuente, y Shure dice otra
   cosa: dos sistemas interfieren con **un tercero**, y el problema aparece con tres o más. Sustituido
   por la cita de Shure (guía de Lyons) y la de los **«pre-selected frequency groups»** (guía de Vear).
   El tema 12 lleva la misma frase (epígrafe «Banda, grupo y canal»): no lo he tocado; conviene
   corregirlo en su verificación.
2. **Tono de 1 kHz atribuido a la R 68 (error 9/8)**: la R 68 no habla de 1 kHz; fija el nivel 18 dB
   bajo el máximo. El 1 kHz lo da Tech 3343 § 8.1. Reescrito y añadido a tabla y Trazabilidad.
3. **«only by ear» en § 3.1 (error 8)**: la frase es un recuadro de la p. 10, junto al § 2.4.
   Corregido en el texto, en la tabla y en Trazabilidad.
4. **Procesador de sonoridad**: añadido § 2.4; la glosa de «loudness sausage» se ajusta a la fuente
   (contraste y dinámica), en vez de «mata lo que el público aporta».
5. **«aconseja» subir la escucha (error 4)**: la fuente dice «one strategy could be»; ahora «propone,
   como estrategia posible».
6. **Golf (error 6)**: añadida la condición de la fuente, comentario nivelado en torno a −23 LUFS.
7. **Cañón y preguntas del público (error 6)**: añadida la salvedad de Shure («it can work if the
   audio is only for the video if the room is not too noisy»).
8. **Visita previa**: la cita estaba mal encajada (los *in-ear* e intercom son lo que se va a usar, no
   lo instalado); reescrita. El *walkaround* es de inalámbricos: explicado.
9. **Cerrar micrófonos**: Shure lo da «To minimize pickup or room noise and reverberation», no contra
   el sonido «a lata»; añadido. **Aviso de alcance de Shure**: añadido su contexto (deporte escolar).
10. **Jack Foley (error 9)**: el origen del nombre no se ha podido confirmar en fuente; quitado.
11. **Cierre**: «Ninguna norma legal regula la captación de sonido» (afirmación sin fuente) → «El tema no
    invoca ninguna norma legal». «Sede de Sevilla y centros territoriales» → reparto real del anexo I
    (8 Sevilla, 3 Málaga, 2 Córdoba, Granada y Jaén, 1 Algeciras, Almería, Cádiz y Jerez). Trazabilidad:
    fuentes releídas en original, filas nuevas de Shure (Vear) y R 68. Extensión de la ficha: 8.600.

## No corregido, a la vista

- La afirmación de oficio de «La música en un informativo» (sala pequeña) sigue sin fuente, declarada
  como oficio; la dejo por eso.

## Lentes

Tema técnico sin norma legal: `refutar_prosa.py` 0 hallazgos; `indice.py` 8.611 palabras, 45 epígrafes.
Pasajes cambiados releídos: cada «la misma guía», «Es la intermodulación» y «su recuadro» tiene su
antecedente.

## Otros ficheros tocados

Ninguno fuera del tema y este informe (descargas en el scratchpad).
