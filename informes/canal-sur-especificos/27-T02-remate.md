# Remate · Oficial Técnico Electricista (27) · Tema 2 · REBT: documentación, puesta en servicio, inspecciones y mantenimiento

Fase 5. Tema:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/02-reglamento-electrotecnico-para-baja-tension-documentacion-puesta-en-servicio-inspecciones-y-mantenimiento.md`.
Entrada: `27-T02-refutacion.md` (0 graves, 4 menores, 1 laguna) y `27-T02-preguntas.md` (13 enteras,
1 a medias, 1 no). Fuentes releídas el 05-10-2026 (reloj del sistema; el encargo dice 24-09-2026;
el consolidado del REBT no cambia entre ambas fechas: última actualización, 18-12-2025).

Ficheros tocados: el tema y este informe.

## Correcciones, comprobadas en la fuente antes de aplicarlas

| Id | Epígrafe | Comprobación | Aplicada |
|---|---|---|---|
| M1 | 1.5 (listado ITC-BT-02, nota (*)) | Volcado BOE-A-2002-18099, nota (*) del listado de la ITC-BT-02: literal como dice la refutación | Sí |
| M2 | 4.4 (ITC-BT-18, apartado 9) | Volcado, ITC-BT-18, 9: la frase sigue al 24/50 V | Sí |
| M3 | 1.1 (STS 17-02-2004) | `boe.py precepto BOE-A-2002-18099 ib-3 --fecha 20040501`: nota «se anula, por ser contrario a derecho, el inciso 4.2.c.2, en tanto que incluye a los Ingenieros industriales, por Sentencia del TS de 17 de febrero de 2004» | Sí |
| M4 | 2.4 (ITC-BT-04, 4 c) | Sin fuente para «la más preguntable y la más incumplida» (no hay exámenes anteriores) | Sí, quitada |
| L1 | 4.3 (ITC-BT-19, 2.9) | Volcado, ITC-BT-19, 2.9: el párrafo sigue a «…a la cual están unidos habitualmente.» | Sí, **ampliación** |

Ninguna corrección del informe resultó errónea.

## Pasajes cambiados

1. **1.1**, tras la tabla de reformas. Antes: «declaró nulo un inciso de la ITC-BT-03 (el 4.2.c.2 de
   la redacción de entonces)». Ahora: «anuló, por ser contrario a derecho, un inciso de la ITC-BT-03
   de la redacción de entonces: **el inciso 4.2.c.2, en tanto que incluye a los Ingenieros
   industriales**. Fue, por tanto, una anulación parcial.»
2. **1.5**, notas del listado de la ITC-BT-02. Sustituido el resumen de la exención por la nota (*)
   literal en negrita (**siempre que el correspondiente proyecto de instalación haya sido firmado
   electrónicamente o visado … o la memoria técnica ha sido firmada electrónicamente antes de la
   fecha de aplicabilidad.**), más una frase en redonda: la licencia de obras sólo cuenta para las
   que no requieren proyecto y la firma ha de ser electrónica. Se mantiene el **plazo máximo de dos
   años** («Las exentas disponen de…»: antecedente presente).
3. **2.4**, tras la cita de 4 a)-c) de la ITC-BT-04: «La c) es la más preguntable y la más
   incumplida» → «La c) pide atención».
4. **4.3**, lista de condiciones de la medida de aislamiento: nuevo guion «Las masas unidas al
   neutro: **Si las masas de los aparatos receptores están unidas al conductor neutro, se suprimirán
   estas conexiones durante la medida, restableciéndose una vez terminada ésta.**» (contesta la
   pregunta 12).
5. **4.4**, cita del apartado 9 de la ITC-BT-18: añadida a la cita la frase **Si las condiciones de
   la instalación son tales que pueden dar lugar a tensiones de contacto superiores a los valores
   señalados anteriormente, se asegurará la rápida eliminación de la falta mediante dispositivos de
   corte adecuados a la corriente de servicio.**

Releídos los cinco pasajes: «la nota (*)», «la c)», «estas conexiones» y «los
valores señalados anteriormente» tienen su antecedente delante.

## Lentes

- `indice.py`: 16.227 palabras, 43 epígrafes; ningún epígrafe nuevo, índice sin cambios.
- `negritas.py` (REBT + Decreto 59/2005): 270 negritas; 3 «no están»: dos son rótulos de la
  plantilla («Enunciado del programa», «Qué se puede preguntar.») y la tercera es la nota de la STS
  (M3), que sólo figura en la redacción histórica de la ITC-BT-03 (comprobada con `--fecha
  20040501`), no en el volcado vigente. Las 11 «atribuidas a otro artículo» son falsos positivos
  de anclaje (preceptos del Reglamento citados en su epígrafe correcto), sin cambio respecto a la
  verificación.
- `refutar_exactitud.py`: los «no literales» son cortes de línea y paréntesis de ITC (el «art.» que
  ve la herramienta es el apartado de la ITC); ninguno en los pasajes cambiados.
- `refutar_modo.py`: 0 hallazgos.

## Resultado

Pregunta 12: ahora entera. Pregunta 14: ahora entera. Amplió contenido nuevo: sí (L1, y la frase
de M2). Procede la fase 5 bis sobre los pasajes 2, 4 y 5.
