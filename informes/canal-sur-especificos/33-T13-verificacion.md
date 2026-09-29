# Realizador/a (puesto 33) · Tema 13 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/33-realizador-a/13-postproduccion-montaje-edicion-efectos-grafismo-mezcla-calidad.md`
(15.910 palabras tras la verificación; índice regenerado con `indice.py`). Fecha de trabajo: 24-09-2026
(encargo); todas las fuentes, leídas el 29-09-2026 (fecha del sistema). Copia previa en el scratchpad
(`13-antes-verif.md`).

## Lo copiado: sólo literalidad

Comprobado con un guion (`v13check.py`, scratchpad) que reaplica cada directiva de `t13r/part*.md`
sobre el fichero de origen **actual** y busca el resultado en el tema: los 44 bloques (COPY del común,
RTVE sin cambios y ADAPT) están literales, antes y después de las correcciones. El tema es además
idéntico a la salida de `t13r/build.py` salvo el índice. No se re-verificó el contenido de lo listado bajo
«Copiado del común» ni de «Copiado de RTVE sin cambios».

En los 23 pasajes adaptados del común se verificó sólo la cadena cambiada: todas las remisiones nuevas
tienen destino real (tema 4: ficha del Grafista y circuito de rótulos; tema 7: «Quién dirige el montaje…»,
«De la grabación al montaje…», «La pieza terminada…», coleos y pies en el parte; tema 9: tres señales y
croma; tema 11: capas de la banda sonora y «Sistema único o doble sistema», y declara que la R 128 sólo
la nombra; tema 12: plantillas de directo, R 95, JPG/TGA, BT.2408, «Archivo»/«Reconstrucción»; tema 14:
rangos de la R 103, submuestreo, curvas HDR; tema 16; epígrafes internos «El *render*», «El códec con
que se monta», «Incrustar», «Las transiciones corrientes», «Offline y online»). Sin hallazgos.

## Verificado contra la fuente (lo nuevo y lo adaptado de RTVE)

- RD 1680/2011 (`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`, consolidado): módulo 0907, RA 2, 3 y
  5 (enunciados), RA 2.e-h, 3.b-f, 5.c, e, f, h y contenidos del control de calidad; 0906 RA 3.e; 0905
  RA 1.f; BOE núm. 302, de 16-12-2011. Literales. RD 500/2024 (`BOE-A-2024-10685.txt`, art. 7 y anexo
  XLI): modifica el anexo I (suprime FOL, EIE y FCT; añade módulos) y el anexo III; no toca el texto de
  0905-0907. Correcto lo que dice la portada.
- X Convenio (BOJA 240, 10-12-2014): Realizador 5351000 p. 196; Ayudante 5353000 p. 111; Encargado
  5212204 p. 127; Operador Montador 5212206 p. 190; Editor de Continuidad 5302010 p. 125. Literales y
  páginas correctas.
- Libro de Estilo 3.17.1.5: código de tiempo idéntico y planos compatibles (p. 61), manipulación del
  máster (p. 62). Literales (el volcado usa la ligadura «ﬁ»; por eso `negritas.py` no las halla).
- Tesis de Todd (Georgia Tech, nov. 1989, M. Arch.): cita de los cinco niveles p. 8; métrico pp. 10-11;
  rítmico p. 13; tonal p. 15; sobretonal p. 17; intelectual y león p. 20 (numeración impresa, como
  pedía la redacción). Citas literales.
- Avid *Media Composer User's Guide* R8 (1999): pp. 522, 523, 526, 531, 540, 543 y 431 (Match Frame y
  Reverse), comprobadas con la cabecera de página del volcado.
- EVS IPDirector 6.2 Control Panel, p. 30 impresa (40 de la web): literal.
- UER *Quality Control* (01-09-2015): las nueve citas, literales. Catálogo qc.ebu.io (API v1, `qcapi.txt`):
  las nueve definiciones, literales y con su nombre (0010B, 0021B, 0051B, 0044B, 0078B, 0012B, 0026F,
  0248B, 0001F).
- UIT-R BT.1702-3 (11/2023): todas las citas literales (recomienda 1, anexo 1, directrices 1 y 2, notas
  1, 3 y 5, adjunto 1). Estado «In force» releído hoy en itu.int. Cuenta a 25 imágenes/s: 360 ms = 9
  cuadros; un destello cada 4 cuadros = 6,25/s > 3. Correcta.
- Supuesto 3: −24,5 + 1,5 = −23 LUFS; −1,8 + 1,5 = −0,3 dBTP; exceso sobre −1 dBTP = 0,7 dB. Correcto.

## Correcciones aplicadas (7)

| # | Dónde | Error | Qué había → qué queda |
|---|---|---|---|
| 1 | Qué se puede preguntar | 9 | Prometía «cómo se numeran sus clips», que la redacción quitó por extensión → quitado |
| 2 | § 1, Eisenstein | 9 | «cineasta y teórico soviético»; *Film Form* «recopilación de sus escritos» → «cineasta ruso» (así lo presenta la tesis: «Russian filmmaker») y «edición de Jay Leyda, Nueva York, 1949» (bibliografía de la tesis) |
| 3 | § 1, método métrico | 9 | «Acortar los planos … da tensión» → la tesis dice *varying* y «from serene to chaotic»: «Variar la duración … da grados de tensión, de la calma al caos» |
| 4 | § 2, *trim* | 9 | Atribuía al modo *Trim* en general la sustitución de monitores, y por «el último cuadro … el primero»; Avid p. 523 lo dice del *Big Trim* y de *outgoing and incoming frames* → corregido |
| 5 | § 2, coleo (adaptado de RTVE) | 9/6 | Sólo «después del último fotograma útil»; el RD 1680/2011, 0905 RA 1.b, minuta **«coleo de entrada, coleo de salida»**, y el tema 7 lo define antes y después → definido en los dos extremos con esa cita; «sin coleo» → «sin coleo de salida». Añadido «RA 1.b» en «Normativa» |
| 6 | § 6, control de calidad | 9 | «trabaja desde hace años» y «depende de la máquina» → «El programa de control de calidad de la UER ha reunido…»; «depende del procesado y de la fiabilidad de las comprobaciones automáticas» (lo que dice la hoja) |
| 7 | Trazabilidad | fecha | Convenio: todas las páginas releídas hoy → 29-09-2026 |

Antecedentes releídos en los pasajes cambiados: «ese modo»/«su presentación grande» remite al modo
*Trim* de la frase anterior; «El de salida» tiene delante «coleo de salida». Bien.

## Lentes

- `negritas.py` (RD, Convenio, LE, Todd, Avid, hoja QC, API QC, BT.1702-3, EVS y los cinco temas de
  origen): 175 negritas, 2 no halladas, ambas del LE 3.17.1.5 por la ligadura; comprobadas a mano.
- `refutar_exactitud.py` y `refutar_modo.py` con el RD: 0 hallazgos (el RD se cita por módulo y
  criterio, no por artículo; los criterios no llevan «podrá»/«deberá» ni salvedades).
- `refutar_prosa.py`: 1, «UX» en «MediaCentral | Cloud UX», nombre comercial presentado como tal. Se deja.
- `indice.py`: índice y extensión regenerados.

## Lo que no se pudo confirmar

- Que «acaba a capón» signifique «sin coleo al final»: sólo lo da la respuesta oficial de un examen de
  RTVE; queda como oficio, declarado.
- Las fechas de lectura de las fuentes que el tema toma del común (Resolve 21, Premiere, DNxHD,
  MediaCentral, R 128, Tech 3343): no releídas, por ser copia literal del común.

Ficheros tocados: el tema y este informe. Trabajo en el scratchpad (`13-antes-verif.md`, `v13check.py`,
`v13-*.txt`).
