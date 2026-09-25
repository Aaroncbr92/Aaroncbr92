# Puesto 28 · Operador/a de Sonido · Tema 1 · Fase 5, remate

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/01-fundamentos-de-sonido.md`. Entrada:
`28-T01-refutacion.md` (2 hallazgos de exactitud, 6 lagunas) y `28-T01-preguntas.md`.

**Resultado: el remate AMPLÍA contenido nuevo** (cinco epígrafes o bloques con fuentes nuevas). Toca
fase 5 bis sobre los pasajes listados abajo. De unas 7.100 a unas 9.300 palabras.

## Fuentes nuevas (todas leídas el 25-09-2026)

| Fuente | Copia local | Qué sostiene |
|---|---|---|
| OpenStax, *University Physics Vol. 1*, 17.2 «Sound Waves» y 17.3 «Speed of Sound» (LibreTexts) | `fuentes/canal-sur/sonido/academicos/openstax-17-2.txt`, `openstax-17-3.txt` | Onda longitudinal; compresiones y enrarecimientos; sólidos transversal y longitudinal; 331/343 m/s; tabla de velocidades |
| OpenStax, *Psychology 2e* (2020), 5.4 «Hearing» | `openstax-psych-5-4.txt` | Células ciliadas; pistas monoaurales y biaurales; diferencias interaurales de nivel y tiempo |
| UNSW Physclips, «Timbre and envelope» | `physclips-timbre-envelope.txt` | Timbre y envolvente; ADSR; transitorios; clave al revés |
| B. Shinn-Cunningham, «Auditory Precedence Effect», *Encyclopedia of Computational Neuroscience*, Springer 2013 | `shinn-cunningham-2013-precedence.pdf/.txt` | Definición del efecto de precedencia; «Law of the first wavefront»; 1–5 ms y decenas de ms |
| Guía de aplicación del DB HR, anejo 1 «Conceptos previos» (codigotecnico.org) | `guia-dbhr-anejo1.pdf/.txt` | 344 m/s; ladrillo ×9; aislamiento frente a acondicionamiento; ley de masa; estanquidad; ruido de impactos |
| Protocolo de vigilancia sanitaria de trabajadores expuestos a ruido (CISNS, Sanidad 2022), 2.1.3-2.1.4 | ya en `fuentes/protocolos-vigilancia/ruido.txt` | Recorrido por el oído; tonotopía; 3.000 y 6.000 Hz |
| DPA «Polarity, phase and delay» (web releída) | — | Salvedad condensador/dinámico (hallazgo 1) |

Las copias en `.txt` de las páginas web se hicieron con curl y limpieza de etiquetas, y todas las
negritas nuevas se cotejaron contra ellas con `negritas.py` (literales).

## Hallazgos de exactitud

1. **Salvedad DPA (patilla 2)**: comprobada en la web de DPA; **aplicada** con la cita literal
   completa, incluido «(not necessarily measurement microphones)».
2. **Contrafase por retardo**: comprobado por cálculo; **aplicado**. Nuevo texto: «un retardo sólo da
   180° a unas frecuencias concretas: la de medio periodo y sus múltiplos impares (con 1 ms, 500,
   1.500, 2.500 Hz…), que son los huecos del filtro en peine del epígrafe siguiente».

## Lagunas: todas ampliadas

| Pregunta | Dónde | Pasaje |
|---|---|---|
| 1 (onda longitudinal) | «Qué es el sonido y qué lo describe» | Párrafo nuevo con tres citas OpenStax 17.2 |
| 3 (velocidad según medio) | «La relación entre longitud de onda y frecuencia» | Dos párrafos y tabla (OpenStax 17.3, guía DB HR) |
| 11 (envolvente) | Tabla «Las tres cualidades» (fila Timbre) + epígrafe nuevo «El timbre y la envolvente» | Physclips |
| 12 (fisiología) | Epígrafe nuevo «El camino del sonido por el oído» | Protocolo + OpenStax *Psychology* |
| 13 (localización, precedencia) | Epígrafe nuevo «Dónde está el sonido: localización y efecto de precedencia» | OpenStax *Psychology* + Shinn-Cunningham |
| 15 (aislamiento) | Epígrafe nuevo «Aislar no es acondicionar» | Guía DB HR |

Con el tema rematado, las 15 preguntas quedan enteras (la 8 ya no induce a error).

Menores de cobertura no ampliados (difracción y distancia crítica por su nombre): sin fuente leída;
se declaran en «Lo que este tema no da».

## Otros pasajes cambiados

- Portada: «Fuente» (nuevas fuentes) y «Extensión» (9.300).
- Siglas: se presenta **DB HR**.
- «Qué se puede preguntar»: añadidos onda longitudinal, medio, envolvente, cóclea, localización y
  precedencia, aislar/acondicionar y ley de masa.
- «Lo que este tema no da»: se quitan los huecos ya cubiertos (fisiología del oído, localización,
  precedencia, velocidad por medio); se dejan la fisiología de la voz, las frecuencias de cada pista
  biaural, la cifra de los 50 ms como oficio, la fórmula de velocidad por temperatura, difracción,
  distancia crítica e índices del DB HR.
- «Trazabilidad»: seis filas nuevas; oficio y cálculo ampliados (efecto Haas como nombre de oficio;
  proporciones de velocidad).
- Índice regenerado con `indice.py`.

Relectura de antecedentes: «la misma fuente», «el mismo protocolo», «la guía», «la propia guía»
tienen delante su antecedente en cada pasaje.

## Donde el informe o las fuentes obligaron a matizar

- La primera tabla de velocidades se había redactado con 343 m/s para el aire; la tabla de OpenStax
  da 331 m/s (gases a 0 °C). Se corrigió y se rehicieron las proporciones (×4,5 agua dulce, ×18 acero).
- Physclips: el «suena a órgano de pedales» es una impresión del autor («to me», «if anything»); se
  dice así.
- La guía DB HR define aislamiento con «Se entiende por aislamiento al conjunto…»: la cita empieza en
  «conjunto».

## Lentes

- `indice.py`: 43 epígrafes, índice al día (avisa «sin portada: es un esquema» porque el tema no está
  en `herramientas/portadas.tsv`; no es de este remate).
- `refutar_prosa.py`: 0 hallazgos (el primer pase dio «HR» sin presentar; corregido).
- `negritas.py` con el RD 2032/2009 y las fuentes locales: todas las negritas nuevas literales; las
  28 no encontradas son citas web ya verificadas (DPA, Rane, RTW), rótulos y dos de Shinn-Cunningham
  que sólo difieren en ligadura «ﬁ» y comillas tipográficas.
- `refutar_exactitud.py` y `refutar_modo.py` con el RD: 0 hallazgos.

## Aviso fuera del tema (no tocado)

El tema 10 (`10-sonorizacion.md`, «Lo que este tema no da») dice que el efecto de precedencia y la
velocidad exacta están «sin fuente leída» y remite al tema 1 como oficio; ahora el tema 1 los da con
fuente. Conviene ajustar esa remisión en el remate del tema 10.

## Otros ficheros tocados

El tema 1 y este informe. Fuentes nuevas en `fuentes/canal-sur/sonido/academicos/`.
