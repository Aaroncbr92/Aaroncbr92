# Puesto 28 · Operador/a de Sonido · Tema 9 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`
(de 10.963 a 11.635 palabras; 60 epígrafes). Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en
24-09-2026). Entradas: `28-T09-refutacion.md` y `28-T09-preguntas.md`. Ficheros tocados: el tema y
este informe. **Amplía contenido nuevo** (dos lagunas): procede la fase 5 bis sobre los pasajes 6 a 8
y la fila nueva de Trazabilidad.

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Para qué |
|---|---|
| EBU R 128 s1 V3 (PDF de tech.ebu.ch, `r128s1.pdf`) | Hallazgo 3: punto c), «in special cases… on purpose» |
| EBU Tech 3343-2023 (`fuentes/normas-tecnicas/`) | Hallazgo 4: «offline loudness meters» sólo en § 3.1 (l. 434); «simple corrective static gain calculation» en § 3.2 (l. 540) |
| iZotope, *RX 11 Manual*, «Spectral De-noise» (docs.izotope.com/rx11/en/spectral-de-noise.html) | Hallazgo 5: *Artifact Control*, valores bajos (sustracción espectral, *musical noise*) y altos (puerta de banda ancha, *bursts of noise*) |
| Avid, *Pro Tools Reference Guide* 2025.12 (PDF de resources.avid.com, creado el 30-11-2025) | Lagunas L1 y L2: cap. 13 (p. 298-299), cap. 22 (p. 628-629), cap. 52 (p. 1464-1465), cap. 56 (p. 1593-1594) |
| Tema 6 del puesto | Hallazgo 2: no habla de enclavar relojes ni de resincronizar |

## Correcciones (todas comprobadas; ninguna rechazada)

| # | Error | Pasaje | Antes | Después |
|---|---|---|---|---|
| 1 | 3 | «La sonoridad del programa terminado» | «al menos 0,5 dB (de −1,8 a −2,3 dBTP)» | «al menos 0,7 dB (de −1,8 a −2,5 dBTP)»; cálculo: −2,5 + 1,5 = −1,0 |
| 2 | 1 | «Posición, velocidad y muestra», deriva | «…se enclavan los relojes o se vuelve a sincronizar de vez en cuando (tema 6).» | «en doble sistema (tema 6), además de código común se enclavan los relojes o se vuelve a sincronizar de vez en cuando (oficio).» |
| 3 | 6 | «Lo que fija la R 128 s1», fila c) | «Se puede normalizar por debajo de −23 «on purpose…»» | «**«In special cases»** (en casos especiales) se puede normalizar por debajo de −23 «on purpose…»» |
| 4 | 8 | «La sonoridad del programa terminado», tabla de recomendaciones y Trazabilidad | Ganancia estática y medidores fuera de línea atribuidos a «§ 3.1 y § 3.2» | Medidores fuera de línea, § 3.1; corrección por ganancia estática, § 3.2 (en los tres sitios) |
| 5 | 9 | «Los artefactos» | «de dos maneras que el manual nombra»; «La puerta de banda ancha deja «bursts of noise…»» | «el manual nombra dos artefactos, uno en cada extremo del mismo ajuste»; «Y si, para evitarlo, el proceso se apoya más en la puerta de banda ancha, tiene menos ruido musical pero suena a puerta y deja «bursts of noise…». Es un compromiso entre los dos artefactos, que el módulo regula con un control propio (*Artifact Control*).» |

## Ampliaciones (lagunas; no se recorta ninguna pregunta)

| # | Laguna | Pasaje nuevo o cambiado |
|---|---|---|
| 6 | L2 (pregunta 9) | Epígrafe nuevo «Los tipos de pista de una estación de trabajo» en «Pistas», antes de «Las pistas de un programa terminado»: enumeración literal de la guía, tabla de ocho tipos con su uso en cita (audio, auxiliar, máster, VCA, MIDI, instrumento, carpeta, vídeo), formatos mono/estéreo/multicanal (3 a 8 canales, Ultimate y Studio) y aplicación a una sesión de postproducción, marcada como oficio |
| 7 | L1 (pregunta 15) | Epígrafe nuevo «Reducir la resolución y cambiar la frecuencia» en «Entrega», tras «El máster»: definición de *dither* y su compromiso, *noise shaping* (≈ 4 kHz), cuándo se usa y cuándo no, último proceso en la pista máster, truncado si no se pone en *Bounce Mix*, *dither* automático en exportación de fragmentos e importación, cinco calidades de SRC (Low a Tweak Head), orden SRC a 24 bits y después reducción con *dither*; caso práctico de 48 kHz/24 bits a 44,1 kHz/16 bits |
| 8 | L1 | «Un caso práctico: la entrega de una cuña de radio», paso 3: «Si piden 16 bits, con *dither* al final de la cadena (epígrafe «Reducir la resolución y cambiar la frecuencia»).» |
| 9 | — | Periféricos: portada (Fuente, Redacción que se estudia, Extensión 11.600), siglas (VCA, MIDI; Avid entre los fabricantes; SRC se presenta en su epígrafe), «Qué se puede preguntar», «Lo que este tema no da» (lo leído de Pro Tools; tipos de *dither* sin leer), fila nueva de Trazabilidad (Avid) y lista de oficio |

Matiz aplicado al redactar la ampliación: la guía dice que al exportar fragmentos se aplica
*dither* «with or without Noise Shaping» (cap. 22) y en otro lugar «preset, noise-shaped dither»
(cap. 52); el tema dice sólo que se aplica *dither*, sin fijar el conformado.

## Relectura de antecedentes

«Esos artefactos» (pasaje 7) tiene delante «quantization artifacts»; «su guía de referencia»
(pasaje 6) sigue a «Pro Tools, de Avid»; «el epígrafe «Reducir…»» y «epígrafe «Entrega»» existen
con ese título; «(tema 6)» del pasaje 2 queda pegado al doble sistema, que es lo que el tema 6 trata.

## Lentes

Tema técnico sin norma legal: `indice.py` (índice regenerado, 60 epígrafes, 11.635 palabras; el
tema no está en `portadas.tsv`, la Extensión se ajustó a mano) y `refutar_prosa.py` antes y después:
0 hallazgos en ambos.

## Respuestas tras el remate

Pregunta 9: entera («Los tipos de pista…», fila auxiliar). Pregunta 14: entera (0,7 dB). Pregunta
15: entera («Reducir la resolución…»). Resultado: 15 enteras.
