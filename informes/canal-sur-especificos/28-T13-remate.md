# Puesto 28 · Operador/a de Sonido · Tema 13 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md`. Fecha de
trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Entrada: `28-T13-refutacion.md` y
`28-T13-preguntas.md`. Ficheros tocados: el tema y este informe. Copia previa del tema en el
scratchpad de la sesión (`t13/tema13.antes-remate.md`).

**Resultado: SÍ se amplió contenido nuevo** (goniómetro, requisitos de la Tech 3341 § 2.2, dialnorm).
Procede la fase 5 bis sobre los pasajes marcados «nuevo».

## Fuentes releídas (todas el 25-09-2026)

UIT-R BS.1770-5 (anexo 1, etapas y tabla 3); EBU Tech 3205-E (§ 2, marca «Test»; § 3.10, retorno);
EBU Tech 3341-2023 (§ 2.2); EBU Tech 3343-2023 (§ 6 y § 6.1); **nueva**: RTW, «Focus: The Audio
Vectorscope», Mike Kahsnitz, 2-VIII-2019 (rtw.com/en/blog/focus-the-audio-vectorscope.html),
leída en HTML; citas comprobadas contra el HTML crudo (las comillas de «inverted» y «ball of wool»
son literales).

## Correcciones de la refutación: todas confirmadas en la fuente y aplicadas

| # | Hallazgo | Comprobación en la fuente | Pasaje cambiado |
|---|---|---|---|
| G1 | [9] «La fase también cambia lo que marca el medidor de sonoridad» | BS.1770-5, anexo 1: «mean square calculation for each channel» antes de «channel-weighted summation». Confirmado: la polaridad entre canales no altera la lectura | «Fase y sonoridad: el tono en los dos canales», primer párrafo reescrito: la lectura depende de cuántos canales llevan el tono; la contrafase se ve en correlador, goniómetro o suma a mono. Título y remisiones (línea «Lo que marca el tono… se ve en») se mantienen: siguen siendo exactos. «Aplicación práctica» no remitía a la sonoridad; sin cambio |
| M2 | [6] Salvedad de la marca «Test» | 3205-E: «9 dB below the maximum amplitude of programme signals transmitted on international sound-programme circuits permitted according to C.C.I.T.T. Recommendations». Confirmado | «Los medidores clásicos», párrafo del PPM: añadido en redonda el complemento y presentada la sigla C.C.I.T.T. (hoy UIT-T) |
| M3 | [6] Celda de la tabla sin «modo normal» | 3205-E § 3.10: «2.8 ±0.3 s in the normal mode, and in 3.8 ±0.5 s in the slow mode». Confirmado | Tabla de medidores, fila PPM: «En modo normal…; (3,8 s en modo lento)» |
| M4 | [8] LFE atribuido a la tabla 3 | BS.1770-5: tabla 3 sólo L, R, C, Ls, Rs; «The low frequency effects (LFE) channel is not included in the measurement» en la descripción del anexo 1. Confirmado | «El peso de cada canal»: frase de entrada y fila LFE precisan la procedencia |

## Lagunas: se amplió el tema (pasajes nuevos)

1. **Goniómetro / vectorscopio** (pregunta 14). Fuente encontrada (RTW, fabricante). Nuevo párrafo y
   tabla en «La correlación de fase», en lugar de la frase «no se ha documentado en una fuente
   leída»: qué muestra, figura de Lissajous girada 45°, AGC (sigla presentada), línea vertical =
   mono, horizontal = polaridad invertida, 45° a un lado = un solo canal, «ball of wool» = mezcla
   normal, y causas de la inversión (cableado, botón INV). Quitada la línea del goniómetro en «Lo
   que este tema no da» y del listado de oficio de «Trazabilidad»; añadida fila RTW en
   «Trazabilidad»; portada («Fuente») y «Qué se puede preguntar» actualizados.
2. **Tech 3341 § 2.2** (pregunta 11). «Las tres lecturas», párrafo de requisitos: integrada a
   «at least 1 Hz»; funciones mínimas «start/pause/continue…» y puesta a cero conjunta de I y LRA.
   Filas de la Tech 3341 en las dos tablas de fuentes actualizadas.
3. **Dialnorm** (pregunta 15). «Los metadatos de sonoridad», párrafo nuevo al principio: nombres de
   los metadatos AC-3 (dialnorm, dynrng, coeficientes de mezcla descendente), qué describe dialnorm
   (sonoridad del programa entero; del diálogo sólo con normalización anclada en el diálogo) y que
   con la R 128 debe indicar −23 LUFS (§ 6.1). Fila de la Tech 3343 en «Trazabilidad» ampliada.

Otros: «Trazabilidad», lista de cálculo: añadida «la misma lectura con un canal en contrafase».
Ficha: extensión de 8.000 a 8.600 palabras (recuento de `indice.py`: 8.608).

Con el tema rematado, las preguntas 11, 13, 14 y 15 pasan a **enteras** (15/15).

## Relectura de antecedentes

Releídos todos los pasajes cambiados: «ponerlas a cero» remite a la integrada y el LRA de la cita
anterior; «el parámetro» remite a dialnorm; «esas etapas» a las dos etapas citadas de la BS.1770;
«el mismo fabricante» y «según RTW» tienen delante a RTW. Sin antecedentes rotos.

## Lentes

Tema técnico sin norma legal: `indice.py` (índice regenerado, 30 epígrafes, 8.608 palabras) y
`refutar_prosa.py` (0 hallazgos; sin siglas sin presentar ni negritas rotas). Comprobación de
literalidad por script de las 15 citas nuevas en negrita: todas literales.
