# Puesto 28 · Operador/a de Sonido · Tema 13 · Fase 5 bis, revisión del remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md`. Fecha de
trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Alcance: sólo los pasajes que cambió el
remate (`28-T13-remate.md`), identificados con `diff` contra la copia previa al remate. Ficheros
tocados: el tema y este informe.

## Fuentes releídas (todas el 25-09-2026)

UIT-R BS.1770-5 (anexo 1: etapas, descripción de la figura 1, tabla 3); EBU Tech 3205-E (§ 1 marca
«Test»; § 3.10 retorno); EBU Tech 3341-2023 (§ 2.1 y § 2.2); EBU Tech 3343-2023 (§ 6, § 6.1, § 8.1);
RTW, «Focus: The Audio Vectorscope» (HTML crudo); **nueva**: UIT, «ITU's History», página 3
(itu.int/en/history/Pages/ITUsHistory-page-3.aspx).

## Pasajes confirmados sin cambio

- LFE: cita literal (descripción de la figura 1 del anexo 1; la lista de etapas también lo excluye). Tabla 3 sólo L, R, C, Ls, Rs. Correcto.
- Tabla de medidores, fila PPM: 10 ms en modo normal; 2,8 s normal y 3,8 s lento (§ 3.10). Correcto.
- Marca «Test», «9 dB below the maximum amplitude» y su complemento: correcto.
- Fase y sonoridad: «mean square calculation for each channel» y «channel-weighted summation», literales; el cálculo (polaridad no altera la lectura) se sigue de esas etapas.
- Vectorscopio: las seis citas, literales contra el HTML crudo (comillas de «inverted» y «ball of wool» incluidas); 45° a izquierda/derecha y causas (cableado, botón INV), confirmadas.
- Tech 3341 § 2.2: «at least 10 Hz», «at least 1 Hz», «start/pause/continue…», puesta a cero conjunta: confirmados.
- Dialnorm (Tech 3343 § 6): cita de los tres parámetros y de «genuinely describes…», literales; caso del diálogo como ancla, confirmado.

## Correcciones aplicadas (comprobadas en la fuente)

| # | Error | Hallazgo | Corrección |
|---|---|---|---|
| 1 | 9 | «C.C.I.T.T., hoy UIT-T» y el desarrollo en español de la sigla no constaban en ninguna fuente leída | Buscada la fuente: la página histórica de la UIT da «International Telephone and Telegraph Consultative Committee (CCITT)», de 1956. Queda «Comité Consultivo Internacional Telefónico y Telegráfico de la UIT (C.C.I.T.T.; en inglés, …)»; quitado «hoy UIT-T» (no confirmado). Fila nueva en «Trazabilidad» y mención en la portada |
| 2 | 8 | «Otros requisitos del medidor (Tech 3341, § 2.2)» abarcaba también el máximo de M y S, que está en el § 2.1 | Párrafo partido: § 2.2 para actualización y funciones; «ya en su § 2.1» para los máximos |
| 3 | antecedente | «ponerlas a cero» sin antecedente femenino plural (la cita en inglés no lo da) | «poner a cero a la vez la integrada y el LRA»; «pasar de "en marcha" a "en espera" y a la inversa» (la fuente dice *switch between*) |
| 4 | literal | Comillas rectas en 'running', 'stand-by', 'Momentary Loudness', 'Short-term Loudness' dentro de negrita; la fuente usa ‘ ’ | Cambiadas a ‘ ’ |
| 5 | 8/6 | Dialnorm a −23 LUFS citado como § 6: está en § 6.1, que además admite otro valor en tres casos | Añadido «(§ 6.1)» y las tres excepciones (archivo, directo externo, metadatos fieles de extremo a extremo); fila de la Tech 3343 en «Trazabilidad» ajustada |
| 6 | 9 | «su anchura informa de la anchura de la base estéreo»: RTW dice que el movimiento y la dispersión *may give information* | «su movimiento y su dispersión pueden informar, entre otras cosas, de…» |
| 7 | 9 | «Las figuras horizontales avisan de problemas de compatibilidad mono»: RTW, canales muy distintos que *could result in* problemas | Reformulado con «pueden» |
| 8 | 9 | «Lleva un control automático de ganancia»: la fuente lo dice del vectorscopio de RTW, no de todo goniómetro | «El vectorscopio de RTW lleva…» |
| 9 | 6 | Tras afirmar que la polaridad no altera la lectura, la cita de la Tech 3343 con «(in phase)» parecía contradecirlo | Frase de enlace: la Tech 3343, al dar la lectura del tono de alineación, lo pide en fase en los dos canales |

## Relectura de antecedentes

«La misma Tech 3341», «la misma § 6.1», «el parámetro» (dialnorm), «esas etapas» (BS.1770),
«según RTW» y «el vectorscopio de RTW»: todos con antecedente delante. Sin antecedentes rotos.

## Lentes

`indice.py`: 30 epígrafes, 8.745 palabras (ficha: 8.700 aproximadamente). `refutar_prosa.py`: 0
hallazgos (siglas presentadas, negritas sanas).

**Resultado: 9 correcciones, ninguna de fondo técnico; el tema queda cerrado.**
