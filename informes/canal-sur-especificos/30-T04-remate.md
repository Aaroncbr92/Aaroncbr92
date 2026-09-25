# Puesto 30 · Tema 4 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`.
Entrada: `30-T04-refutacion.md` (1 grave, 4 menores, 1 laguna) y `30-T04-preguntas.md`.

## Fuentes releídas (25-09-2026, sólo el pasaje)

- SMPTE ST 259:2008 (alcance, «Typical loss amounts may be in the range of 20 dB to 30 dB»);
  ST 292-1:2018 (alcance, lín. 89-91, y 8.1.10, «up to 20 dB»); ST 424:2012 (alcance y 8.x, «up to
  30 dB … are typical»); ST 2082-1:2023 (alcance y lín. 882, «up to 40 dB … are typical»; todas admiten
  receptores para más o menos atenuación).
- UIT-R BT.2020-2 (lín. 129-136, LSDI y su definición; lín. 183, comillas tipográficas).
- SMPTE ST 2110-20:2022 (lín. 963, salvedad «KEY signal»).
- EBU R 123 (julio de 2009): §§ 1-3, tabla 1 (8a, 8b), notas generales, notas 1, 2 y 5, clave de
  abreviaturas, anexo 2.2.
- EBU Tech 3343-2023 (noviembre de 2023): § 4.2 (LFE, 5.0) y § 7.1 (*downmix* Lo/Ro).

## Correcciones de la refutación

| Nº | ¿Confirmada en la fuente? | Aplicada |
|---|---|---|
| 1 (grave) | Sí: ST 292-1 da «up to 20 dB», menos que la ST 259; en las cuatro son pérdidas típicas | Sí |
| 2 | Sí: «large screen digital imagery (LSDI)» y su definición | Sí, con la definición citada entera («…typically for public viewing») |
| 3 | Sí: “being there” | Sí |
| 4 | Sí: sigue «unless the sampling keyword indicates the signal is a KEY signal» | Sí, en redonda («salvo en las señales de clave»), con remisión al § 5, que ya cita la frase entera |
| 5 | Sí (oficio impreciso); 29,97 → 25 descarta unos 4,97 cuadros por segundo (cálculo) | Sí, en § 7 y en la fila del supuesto |

## Pasajes cambiados

1. § 11, «La interfaz digital serie (SDI)», párrafo tras la tabla: quitada la regla «cuanto más rápida
   la interfaz, más pérdida admite»; ahora: el alcance lo fija el fabricante del receptor; las normas
   dan pérdidas típicas: **«20 dB to 30 dB»** (ST 259), **«up to 20 dB»** (ST 292-1), **«up to 30 dB»**
   (ST 424), **«up to 40 dB»** (ST 2082-1); el HD-SDI da menos que el SD-SDI; se mantiene «a más
   velocidad, el mismo cable llega menos lejos (oficio)».
2. § 2, glosa de la cita de la BT.2020-2: LSDI es **«large screen digital imagery»**, con
   **«a system providing a display on a very large screen, typically for public viewing»**; comillas
   “being there”.
3. § 11, viñeta de la ST 2110-20: añadido «salvo en las señales de clave (§ 5)».
4. § 7, «La cadencia en el montaje», 1.ª viñeta: «pierde cuadros (unos cinco de cada treinta) o los
   mezcla, porque las dos cadencias no son múltiplo una de otra». Aplicación práctica, fila «Material
   del móvil»: «Las cadencias no son múltiplo una de otra».
5. **Ampliación (laguna, pregunta 12)**: nuevo epígrafe § 12 «Las pistas de audio: configuraciones y
   orden (EBU R 123)», antes de «La sonoridad de entrega»: mono/estéreo/multicanal con la clave de la
   R 123; el 5.1 (L, R, C, L Sur, R Sur y LFE) y el 5.0 (Tech 3343, § 4.2); por qué el orden debe ser
   inequívoco, la recomendación de hasta 16 canales y su salvedad de acuerdo previo; 48 kHz, 24 bits y
   alineación con la imagen; tabla con las asignaciones 8a y 8b y sus notas; nota 1 (estéreo como
   *downmix* o mezcla aparte); IT (definición SMPTE del anexo), AD y FL; *downmix* Lo/Ro por defecto
   (Tech 3343, § 7.1); qué comprueba el montador (oficio).
6. Accesorios: sigla LFE en la entrada; portada (Fuente: R 123 y Tech 3343; Extensión 14.200
   palabras); «Qué se puede preguntar»; filas nuevas en «Normas y documentos técnicos que el tema cita»
   y en «Trazabilidad»; en «Lo que este tema no da»: UIT-R BS.775, EBU R 48 y SMPTE 2035 no leídas, y
   no consta si la R 123 tiene revisión posterior a 2009; en la lista de oficio, las configuraciones y
   el «.1».

Relectura de antecedentes: «lo llama» (el canal de efectos de baja frecuencia, en la frase anterior),
«la misma recomendación» (BT.2020-2), «En las dos» (8a y 8b de la tabla), «nota 1» (de la R 123):
todos con su antecedente delante.

Con la ampliación, la pregunta 12 pasa a contestarse entera (a: cinco canales L, R, C, L Sur, R Sur
más LFE; el tema no afirma «rango completo», que no se leyó en fuente). La 13 también, tras el hallazgo 1.

## Lentes

- `indice.py`: 14.231 palabras, 62 epígrafes (uno más), índice regenerado.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py --todas` contra R 123, Tech 3343, ST 259/292-1/424/2082-1 y BT.2020: todas las
  negritas nuevas o cambiadas, «ok».

## Ficheros tocados

El tema y este informe. (El `git status` muestra modificado `fuentes/canal-sur/BOE-A-2023-11022.md`:
no es de este remate.)

Amplió contenido nuevo: **sí** (§ 12, pistas de audio): procede la fase 5 bis sobre el pasaje 5 y el 1.
