# Puesto 28 · Operador/a de Sonido · Tema 3 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/03-microfonia.md` (unas 11.400 palabras según
`indice.py`; 7 rúbricas en el orden del enunciado, 36 epígrafes `###`).

Material usado: `informes/canal-sur-especificos/28-investigacion-A-fundamentos.md` (§ 3.1 y 3.2;
§ 2.4 sólo para remitir al tema 2); RTVE `temas/sonido/05` y `temas/sonido/13` (§ 5); tema cerrado
de Canal Sur `08-camara-operador/06-captacion-de-sonido.md` (cierre: `08-T06-final.md`).

## Fuentes leídas en esta fase (todas el 25-09-2026)

La investigación A sólo daba tipos de transductor y sensibilidad. Para patrones, colocación,
estéreo, inalámbricos y accesorios, y para confirmar las cifras del RTVE, se leyeron con curl
(extractos en el scratchpad de la sesión, `t03/`) estas páginas de DPA *Mic University*:
«Listen to your polar pattern»; «How to specify the directivity of a shotgun mic»; «Directional vs.
Omnidirectional microphones»; «Stereo recording techniques and setups»; «Immersive/object-based
audio recording techniques»; «Introduction to immersive audio: The basics»; «Miniature mics in
broadcast»; «How mic placement affects the recorded sound of the voice»; «Proper hand placement on
a vocal mic»; «The audio consequences of using wind, rain and virus protection on microphones»; «A
guide to pro wireless audio», partes 1-6; «Your first wireless system»; «Troubleshooting wireless
systems»; y el menú del catálogo. Además, los extractos DPA-SPEC, DPA-CD y DPA-PH de la
investigación. Todas las citas inglesas del tema se cotejaron por programa con esos textos: 190
citas, todas literales tras normalizar comillas y espacios (se corrigió una: el símbolo Ω de la
fuente es U+2126).

## Correcciones al RTVE (manda la fuente)

- **Mínimos de captación**: el RTVE 05 da 126° (super) y 110° (hiper) sin fuente. DPA da
  «approximately ±135°» y «approximately ±115°». El tema da los de DPA como aproximados y declara el
  hueco de los valores teóricos de manual.
- **ORTF**: el RTVE da 177 mm y 110,55° (cifras de la plantilla de su examen). DPA: «spaced 17 cm (7
  in) and angled ±110°»; su barra estéreo marca 110° para ORTF igual que 90° para XY («90° angle
  (±45°)»). El tema da 17 cm y 110° totales y explica la lectura; **aviso al verificador**: el «±110°»
  literal de DPA es ambiguo.
- **Pareja espaciada**: el RTVE dice «separados metros»; DPA calcula un AB de 40 cm. Tabla de
  familias adaptada.
- **Receptores y antenas** (RTVE 13 § 5): «las antenas se acercan al escenario y no los receptores»
  contradice a DPA («best to place the receiver close to the antenna and route the AF signal in the
  long wires»). No se copió; el tema da la regla de DPA.
- **Ambisónico**: la serie 4/9/16 del RTVE no tiene fuente leída; se quita. DPA da 8-64 cápsulas en
  orden superior.

## Qué se quitó por propio de RTVE o sin fuente

- Todas las referencias a preguntas y respuestas oficiales (12, 16, 20, 34, 62, 63, 64, 78 del 05;
  41, 71, 87 del 13) y los epígrafes «Los datos que el examen ha preguntado».
- RTVE 05 § 4 entero (modelos de catálogo AKG D112, SM58, MD441, MKH 416): sin fuente; hueco
  declarado.
- RTVE 05: rosca de 3/8 y 5/8 de pulgada; «rotar la escena» y «realidad virtual» del ambisónico; la
  explicación de que el ORTF «suena natural en una toma de orquesta».
- RTVE 13 § 1-4 (bandas de radiodifusión, FM estéreo, DAB+, modulaciones): fuera de este enunciado;
  lo que toque va al tema 12 (radiofrecuencia).

## Copiado del común

Pasajes literales del tema 6 del específico de Cámara Operador (cerrado: `08-T06-final.md`). No se
re-verifican. Comprobado por script: cada párrafo y cada fila de tabla es subcadena del tema 6.

1. «El micrófono, un transductor»: frase de entrada y tabla de los dos transductores (sin el
   párrafo de los tres adjetivos ni el de los aparatos que no transducen).
2. «Los micrófonos por su transductor»: tabla de cuatro tipos.
3. «Los micrófonos por su forma y su uso»: tabla de cinco formas y la frase «Electret, condensador
   y lavalier son tipos de micrófono…».
4. «Los patrones de primer orden»: párrafo «Los micrófonos con igual sensibilidad en cualquier
   dirección son los omnidireccionales…» (sin la frase de la Sony Z200).
5. «Cuándo conviene cada patrón»: frase «El patrón polar de un micrófono dice de qué direcciones
   recoge…», tabla de seis patrones con la columna «Cuándo se usa en ENG», párrafo «El hipercardioide
   se usa principalmente…», tabla «Lo que no hace un patrón estrecho» y párrafo «Un patrón estrecho
   castiga el movimiento…».
6. «El efecto de proximidad»: los párrafos de las definiciones de DPA, la tabla de cuatro
   condiciones y el párrafo «La causa: …» (con sus citas de DPA ya verificadas en Cámara).
7. «El micrófono de corbata y la diadema»: párrafo «El micrófono de corbata tiene su propio ruido…»
   con la cita del Libro de estilo (8.6.1) y la colocación de oficio.
8. «Lo que dice el Libro de estilo de Canal Sur»: frase de entrada y las tres viñetas (3.17.1,
   3.17.1.3, 8.3.2).
9. «Los soportes y para qué sirve cada uno»: tabla de seis soportes y la frase «El micrófono nunca
   va rígido sobre el soporte…» (sin las frases de la Sony Z200).
10. «Qué es un sistema inalámbrico»: párrafo «Un sistema inalámbrico son dos aparatos…».
11. «Bandas, grupos y canales»: tabla banda/grupo/canal, párrafo «El grupo es la clave…» y párrafo
    «Por eso, en un inalámbrico doble…».
12. «Contra el viento»: frase «En exterior el viento es el primer enemigo…» (sin la del filtro de la
    Z200).

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra; **sólo se ha quitado la negrita** (en el RTVE era
énfasis y aquí negrita = literal de fuente) y la marca ✔. Ninguno cita norma. Comprobado por
script: cada párrafo o fila, sin `**`, es subcadena del RTVE 05.

1. «El diagrama polar»: «El diagrama polar de un micrófono dice cuánto capta según de dónde venga
   el sonido, con el eje de captación en 0 grados.» (§ 1)
2. «El efecto de proximidad»: párrafo «El razonamiento es directo: … Sin gradiente no hay efecto de
   proximidad.» (§ 2)
3. «El efecto de proximidad»: párrafo «Y el uso creativo, que conviene conocer… para poder acercarse
   sin que el grave se desborde.» (§ 2)
4. «La regla: el patrón se elige por lo que hay que rechazar»: las cuatro filas de la tabla de
   descarte y su cabecera, y el párrafo «La regla de familia que se lleva de aquí…». (§ 3)
5. «El micrófono ambisónico»: tabla W, X, Y, Z. (§ 6; contrastada además con DPA)
6. «Contra el golpe de voz: el antipop»: párrafo «Y la distinción que más confunde: … un peluche no
   sirve para una locución.» (§ 7)

**Adaptado de RTVE (sí se verifica):** la frase de entrada de la mesa de locutores (reescrita sin
la pregunta); «De ahí la regla que se pregunta…» (resume las preguntas 12 del RTVE); «El monitor en
el mínimo del micrófono» (ángulos cambiados a los de DPA); la tabla de las tres familias estéreo
(XY/Blumlein/MS; DIN añadido; «separados metros» quitado); la tabla del RTVE 13 § 5 no se copió.

## Nuevo (se verifica entero)

- Tipos: cita de la membrana; separación de 20-50 µm e interfase; alimentación (DPA-CD, DPA-PH);
  «El transductor no es la directividad» y la tabla presión/gradiente; los tres tópicos; capa
  límite, lápiz, diafragma grande, miniatura y electret.
- Patrones: medida del diagrama; tabla de siete patrones con −3/−6 dB, mínimos y polaridad del
  lóbulo trasero; tabla DSF/DF/DI/ángulo de aceptación (con 10 × log DF comprobado); patrón con la
  frecuencia y efecto cortina; el cañón; la recomendación de probar un omni; proximidad «boomy» y
  graves a más de 30 cm.
- Sensibilidad entera (salvo la remisión al tema 1): definición, 94 dB, mV/Pa ↔ dBV/Pa (tabla de
  cálculo), tolerancia, ganancia, voz de 150 dB (cuenta 56 dB ≈ 630 veces), ruido propio, SPL
  máximo, rango dinámico (ejemplo 15/135 → 120 dB), carga 5-10 veces **con la salvedad de DPA**
  («only a problem with very poor mixer designs»).
- Colocación: distancia y factor de distancia; acople de omni y direccional; *cupping*; logotipos;
  posiciones del corbata y realce de 2-4 kHz; parejas estéreo con cifras DPA; MS; ambisónico.
- Soportes: jirafa, pértiga, cuello de cisne, barra estéreo; soporte como reflector; seguridad.
- Inalámbricos: todo salvo los tres pasajes del común (emisores, analógico/digital, latencia y su
  equivalente en metros, WMAS, bandas UHF europeas, procedimiento de grupos, recepción, petaca,
  pilas).
- Accesorios: viento, lluvia, antipop, suspensión, accesorios del miniatura, funda higiénica.

## Huecos declarados (en el tema, «Lo que este tema no da»)

Equipos de CSRTV; texto de IEC 60268-4 e IEC 61938; CNAF, antenas, coordinación e intermodulación
(tema 12); micrófono de cinta; modelos de catálogo; valores teóricos de los mínimos; serie de
cápsulas de orden superior.

## Lentes

`indice.py`: índice generado (45 epígrafes). `refutar_prosa.py`: 1 hallazgo (sigla HF en una cita
sin presentar), corregido presentando HF y LF en las siglas; segunda pasada, 0. Sin lentes de norma
(el tema no cita norma).

## Otros ficheros tocados

Ninguno del repositorio fuera del tema y este informe. En el scratchpad de la sesión, un script de
extracción pasó por error sobre todos los `.html` del directorio raíz del scratchpad y regeneró sus
`.txt` (quedándose sólo con el `<main>`); son ficheros de trabajo, no del repositorio, pero otro
agente que los reutilice debe regenerarlos.

## Preguntas tipo test de comprobación (10)

| # | Rúbrica | Pregunta | Respuesta | ¿La contesta el tema? |
|---|---|---|---|---|
| 1 | Tipos | La diferencia entre un micrófono dinámico y uno de condensador está en: a) su patrón polar b) su principio de transducción c) su conector d) su efecto de proximidad | b) | Entera: «El transductor no es la directividad» (cita DPA: «nothing to do with the directional characteristics») |
| 2 | Patrones polares | Un hipercardioide es prácticamente sordo: a) a 90° b) justo detrás, a 180° c) hacia ±115° del eje, a los lados de su lóbulo trasero d) en ninguna dirección | c) | Entera: «Los patrones de primer orden» (DPA ±115°; super ±135°; cardioide 180°; polaridad invertida del lóbulo trasero) |
| 3 | Patrones polares | ¿Qué micrófono no presenta efecto de proximidad? a) bidireccional b) cardioide c) supercardioide d) omnidireccional | d) | Entera: «El efecto de proximidad» (y el ocho es el que más lo acusa) |
| 4 | Sensibilidad | La sensibilidad en campo libre de un micrófono se da para una presión de: a) 20 µPa b) 1 Pa, es decir, 94 dB SPL c) 1 Pa, es decir, 120 dB SPL d) 1 V | b) | Entera: «Qué es y cómo se expresa» (en el eje y a 1 kHz) |
| 5 | Sensibilidad (práctica) | Un micrófono de 10 mV/Pa tiene una sensibilidad de: a) −20 dBV/Pa b) −40 dBV/Pa c) −60 dBV/Pa d) +10 dBV/Pa | b) | Entera: tabla de conversión y ejemplo de DPA |
| 6 | Colocación (práctica) | En una tertulia de radio con los locutores sentados unos al lado de otros y otros enfrente, el micrófono más recomendable para cada uno es: a) omnidireccional b) bidireccional c) cardioide d) supercardioide | c) | Entera: «La regla: el patrón se elige por lo que hay que rechazar» (tabla de descarte) |
| 7 | Colocación | La disposición ORTF usa: a) dos omnidireccionales separados 40 cm b) dos cardioides separados 17 cm y con 110° entre ellos c) un cardioide y un ocho coincidentes d) dos ochos coincidentes a 90° | b) | Entera: «Las parejas estéreo» (con AB, MS y Blumlein para las falsas) |
| 8 | Soportes | La suspensión elástica sirve para: a) reducir el ruido del viento b) aislar el micrófono de las vibraciones del soporte c) evitar el golpe de las oclusivas d) fijar el corbata a la ropa | b) | Entera: «Los soportes y para qué sirve cada uno» y «Contra la vibración» |
| 9 | Inalámbricos (práctica) | Dos micrófonos inalámbricos en el mismo montaje deben ir: a) en grupos lo más separados posible b) en el mismo grupo y en canales distintos c) en el mismo canal d) el grupo no influye | b) | Entera: «Bandas, grupos y canales» (intermodulación y procedimiento DPA) |
| 10 | Accesorios (práctica) | Para grabar a un reportero con un corbata en la calle con viento, lo adecuado es: a) un antipop b) una peluca para miniatura y, si hace falta, el corte de graves c) una bolsa de plástico gruesa ceñida d) un cono de nariz | b) | Entera: «Contra el viento» (27 dB(A) del ejemplo, corte de graves) y «Contra el golpe de voz» (el antipop no sirve en la calle) |

Comprobación adicional de lo que las diez dejan fuera: latencia de un inalámbrico digital (2-3 ms,
7-8 ms; analógico 0 ms), diversidad, petaca a 5 cm del cuerpo, *cupping*, corbata en el pecho y
realce de 2-4 kHz, ruido propio y SPL máximo con THD < 1 %, carga de 5-10 veces, factor de distancia
del cardioide (1,73), cañón descrito por DI. Todas se contestan con el tema. Las diez, repartidas
por las siete rúbricas (tipos 1; patrones 2; sensibilidad 2; colocación 2; soportes 1; inalámbricos
1; accesorios 1; cuatro de aplicación práctica), se contestan enteras; no ha hecho falta ampliar.
