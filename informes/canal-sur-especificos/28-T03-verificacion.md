# Puesto 28 · Operador/a de Sonido · Tema 3 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/03-microfonia.md`.

## Pasajes copiados: sólo comprobación de literalidad

Script de cotejo por párrafo y por fila de tabla (sin `**` ni ✔, espacios normalizados) contra el
tema 6 de Cámara Operador y contra RTVE `sonido/05`; los tres puntos del Libro de estilo, con `diff`.

- **Copiado del común** (12 pasajes): todos literales. No se re-verifican.
- **Copiado de RTVE sin cambios** (6 pasajes): todos literales. No se re-verifican.
- Lo adaptado de RTVE (mesa de locutores, regla del ocho, monitor en el mínimo, tablas de familias
  y disposiciones estéreo) se verificó como nuevo.

## Fuentes releídas (todas el 25-09-2026, descargadas de nuevo con curl)

DPA *Mic University*: «10+ statements on condenser microphones versus dynamic mics»; «Know the
basics about phantom power»; «How to read microphone specifications»; «Directional vs.
Omnidirectional microphones»; «Listen to your polar pattern»; «How to specify the directivity of a
shotgun mic»; «Miniature mics in broadcast»; «How mic placement affects the recorded sound of the
voice»; «Proper hand placement on a vocal mic»; «Stereo recording techniques and setups»;
«Immersive/object-based audio recording techniques»; «Introduction to immersive audio: The basics»;
«The audio consequences of using wind, rain and virus protection on microphones»; «A guide to pro
wireless audio», partes 1-6; «Your first wireless system»; «Troubleshooting wireless systems»; menú
del catálogo. No se usaron los `.txt` del redactor (su informe avisa de que se regeneraron mal).

Resultado: las 164 citas inglesas en negrita que no son del común están, literales, en la página que
«Trazabilidad» les asigna. Tablas de −3/−6 dB, DSF/DF/DI/ángulo (con 10 × log DF), ángulos del
modelo 2017, cifras estéreo (15 dB, 1,1 ms, 0,5 ms/6 dB, 17/20/30/40 cm), bandas europeas, WMAS,
códec, latencias, 99 %, 4 m, 3-5 m, 10 mW, 27 dB(A), 20-30 dB, <10 µm: conformes. Cálculos rehechos
(94 dB, tabla mV/Pa, 7,9-12,6 mV, 56 dB ≈ 630 veces, 120 dB, 1-2 kΩ, 1,152 Mbit/s, 1 m y 2 m de
recorrido): correctos. Remisiones a los temas 1, 2, 6, 7, 10, 12, 14 y 16: existen o están en el
enunciado. Aviso del redactor sobre el ORTF: la lectura de 110° totales se sostiene (la barra marca
«90° and 110° offset» y el XY de 90° es ±45°).

## Hallazgos y correcciones aplicadas

1. **Error 9 (afirmación sin fuente).** «Antenas del receptor separadas: al menos un cuarto de onda».
   DPA (*Troubleshooting*, 2.05): **«at least 1/2 wavelength … At 600 MHz, this is approximately 25
   cm»**. Corregido a media longitud de onda (25 cm a 600 MHz), y se mantienen los 30 cm de la guía
   básica.
2. **Error 6 (salvedad omitida).** Presión y gradiente: DPA dice que en rigor **«Only the
   figure-of-eight should be called a pressure gradient microphone»**, aunque lo común es llamar
   gradiente a todos. Añadido tras la tabla.
3. **Error 9.** «De esa diferencia salen casi todas las propiedades… viento, golpe de voz, distorsión»:
   DPA atribuye la sensibilidad al viento y al golpe de voz a las membranas más flexibles de los
   direccionales, no al principio de gradiente. Reescrito atribuyendo cada propiedad a su causa.
4. **Error 6.** SPL máximo: DPA da además el SPL máximo de pico al 10 % de THD. Añadido.
5. **Error 6.** Carga del micrófono: el tema limitaba el problema a mesas mal diseñadas; DPA añade
   que **«making passive splits»** da el mismo problema. Añadido.
6. **Error 9 (atribución).** «La petaca hacia delante» estaba en la lista de oficio, pero es de DPA
   (parte 6: **«facing forward»**; guía básica: petaca a la espalda tapada por el cuerpo). Se cita y
   se quita del oficio. Trazabilidad ampliada (partes 1-6, guía básica, *Troubleshooting*,
   especificaciones, «10+ statements»).
7. **Error 5 (siglas).** **PA** (en dos citas) y **QPSK** no se presentaban. Presentadas.
8. Oficio no declarado: por qué la capa límite evita el filtro en peine. Añadido a la lista de oficio.
   Extensión de la ficha: 11.600 palabras.

Nota: no se añadió la salvedad del realce de agudos del cono de nariz, porque DPA se contradice (en
la página del viento **«with a high-frequency boost on axis»**; en la de estéreo, **«without»**).

Pasajes cambiados releídos: todos los «esa diferencia», «añade» y «la salvedad» tienen su
antecedente.

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py`, 0 hallazgos; `indice.py`, índice al día (11.573
palabras, 45 epígrafes; avisa «sin portada» porque no tiene fila en `portadas.tsv`, no tocado).

## Otros ficheros tocados

Sólo el tema y este informe (y ficheros de trabajo en el scratchpad, `v03/`).
