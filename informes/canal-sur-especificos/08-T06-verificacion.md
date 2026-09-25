# Puesto 08 · Tema 6 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/06-captacion-de-sonido.md`.
Leídos sólo `ENCARGO.md`, el enunciado del puesto 08 y el informe de redacción de T06.

## Fuentes releídas (todas el 24-09-2026)

- `fuentes/normas-tecnicas/EBU_R68-2000.txt` (entera, 98 líneas).
- `fuentes/normas-tecnicas/EBU_R128-2023.txt`: historial, considerandos a)-f), puntos g)-n), notas 1 y 2.
- `fuentes/normas-tecnicas/EBU_Tech3341.txt`: portada, § 2.4 (1 LU = 1 dB), parámetros M/S/I.
- `fuentes/normas-tecnicas/EBU_Tech3343-2023.txt`: pp. 12-13 (margen para el público), § 3.5.1, § 8.1, p. 43 (pico verdadero, −2 dBTP).
- `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt`: pp. 13-14, 16, 99, 136-139, 260-261, 298, 336-338 (páginas por la marca de pie de página).
- `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 3.2.2 (p. 46), 3.17.1 y 3.17.1.3 (pp. 59-60), 5.3.3 (p. 81), p. 82 y 5.4, 6.4 (p. 92), 8.3.2 (p. 117), 8.6.1 (p. 122).
- `fuentes/normas-tecnicas/AES-normas-de-audio.md` (AES14).
- RTVE: `temas/informacion-grafica/06-el-sonido-en-eng.md` y `temas/montaje-equipos/06-sonido-microfonos-y-altavoces.md`.

## Copiado del común

Ninguno (según la redacción); nada que saltar.

## Copiado de RTVE (verificado)

Lo adaptado coincide en lo sustancial con los dos temas RTVE; es oficio sin norma y así se declara.
Añadidos del redactor comprobados: «o pila» en el condensador (Z200, p. 136, «battery-operated
microphone»); pinza para el corbata; ruido de manejo (oficio). Sin cambios.

## Hallazgos y correcciones (15)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | «En la práctica de otros países se usa −20 dBFS» | Sin fuente: quitado. Queda sólo que la Z200 trae −20 dB de fábrica y que su origen no consta; ídem en «Lo que este tema no da» |
| 2 | 6 | R 68, nota 1 (16 bits) cortada | Añadido «depending on the performance of the A/D and D/A converters» |
| 3 | 6 | Picos «hasta 6 dB» sobre el medidor | R 68: 3 dB; 6 dB sólo ocasionalmente contando errores de operación. Reescrito |
| 4 | 6 | Tech 3343 § 8.1: −18 LUFS / +5 LU | Añadida la condición (tono en fase en los dos canales) y la razón (ponderación en frecuencia) |
| 5 | 6 | R 128 m): tolerancia ±0,3 dB | Añadido «for signals with a bandwidth limited to 20 kHz» (texto y tabla de recomendaciones) |
| 6 | 6 | R 128 c): QPPM | Añadido «usado para leer picos» (when used to read peaks in the usual way) |
| 7 | 9 | −2 dBTP «para sistemas de emisión» | La Tech 3343 dice sistemas de reducción de datos (MPEG-1 Layer 2, Dolby AC-3). Corregido |
| 8 | 8 | Z200 «entrar en» cámara lenta suelta el TC | Fuente (p. 298): «if you start shooting in Slow & Quick Motion mode». Corregido a «empezar a grabar» |
| 9 | 8 | [CH1-4 Input Select] «pp. 260-261» | Los cuatro están en p. 260. Corregido |
| 10 | 4 | Libro de estilo «pedía» barras | Fuente: «Es conveniente mantener la norma…». Corregido a «recomendaba», con la cita completa |
| 11 | 9 | «cámara de mano», «profesional de mano» | El manual dice «Solid-State Memory Camcorder»; ni «de mano» ni «profesional». Reescrito como «videocámara (de 2024)» |
| 12 | 9 | «Un LU es un decibelio de sonoridad», sin fuente | Añadida la cita de la Tech 3341 § 2.4 «1 LU is equivalent to 1 dB» |
| 13 | 5 | SPL presentada y no usada; PCM (en cita de la Tech 3343) y BOJA sin presentar | SPL quitada; PCM y BOJA presentadas |
| 14 | — | Páginas que faltaban | 3.2.2, p. 46; 8.6.1, p. 122 (texto y trazabilidad) |
| 15 | — | Trazabilidad | R 128 «notas 1 y 2»; Tech 3341 con versión y título de portada («…supplement EBU R 128 loudness normalization»); Z200 p. 298 incluye la pérdida de enclavamiento |

## Confirmado sin cambios

R 68: opinión de 16 bits y BS.646, 9/8 dB bajo el PML, 18 dB, 1:8 (18,06 dB). R 128: título, V5
(nov. 2023), h) −23,0 LUFS ±1,0 LU, i) ±0,2 LU, k), m) −1 dBTP, n) y nota 2, LUFS = LKFS, ±0,5 LU de
2014 sólo en el historial. Tech 3341: M 0,4 s sin puerta, S 3 s, I con puerta. Tech 3343: § 8.1
entero, margen de 1 dB y 0,5 dB de sublectura, «welcome bonus», § 3.5.1 −24 LUFS. Z200: todos los
literales y valores de fábrica (LINE/MIC/MIC+48V, avisos p. 136, AUTO/MAN p. 16, p. 138, p. 139,
menú pp. 260-261, p. 99, TC p. 298, pp. 336-338). Libro de estilo: todos los literales y páginas.
Sin normas jurídicas: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Lentes

- `refutar_prosa.py`: 0 relleno, 0 repeticiones; sigla «PXW» = código de producto (sin cambio).
- `indice.py`: índice sin cambios (43 epígrafes), 9.535 palabras; portada puesta a 9.500.

## Otros ficheros tocados

Sólo el tema 6 y este informe.
