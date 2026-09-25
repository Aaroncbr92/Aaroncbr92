# Puesto 28 · Operador/a de Sonido · Tema 13 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema verificado:
`temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md`.
Ficheros tocados: sólo el tema 13 y este informe. Las fuentes descargadas quedaron en el scratchpad
de la sesión, no en el repositorio.

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Cómo |
|---|---|
| EBU R 128-2023 (V5), Tech 3341-2023, Tech 3343-2023 (V4), R 68-2000 | Volcados de `fuentes/normas-tecnicas/`; descargados de nuevo de tech.ebu.ch: PDF idénticos (mismo MD5) |
| UIT-R BS.1770-5 (11/2023) | PDF de itu.int; estado en itu.int/rec/R-REC-BS.1770: -5 «In force», -4 (10/2015) a -0 (07/2006) «Superseded» |
| EBU Tech 3342-2023 (V4) y Tech 3205-E (2.ª ed., 1979) | PDF de tech.ebu.ch |
| RTW, «Focus: The Multi Correlator», Thomas Valter, publicado 2019-08-09 | Página web |
| Sound On Sound, H. Robjohns, «VU Meters…», «Published May 2024» | Página web |

Método: cada cita en negrita se buscó con script en el texto de su fuente y después se leyó en su
contexto (salvedades, sección); los datos en redonda se leyeron uno a uno.

## Pasajes copiados: sólo comprobación literal

- «Copiado del común» (11 pasajes, del tema 6 de Cámara): script sobre texto normalizado. Los 11
  son literales. Los fragmentos 8 y 9 son recortes de una cita más larga del común (literales).
- «Copiado de RTVE sin cambios» (6 pasajes, 9 bloques): sin `**` ni ✔, todos son subcadena del
  RTVE 14. Literales.
- No se re-verificaron. Observación sin corregir (está en la tabla copiada del común, punto 2): la fila
  n) se titula «Margen de sonoridad (LRA)», mientras el resto del tema dice «rango de sonoridad».
  No es un error de dato; se deja para quien cierre el tema 6 de Cámara.

## Correcciones aplicadas (error del catálogo entre corchetes)

1. [1] «Tras un códec puede hacer falta un techo más bajo (se ve en «Pico de muestra y pico
   verdadero»)»: el −2 dBTP está en «Por qué −1 dBTP y no 0». Remisión corregida.
2. [8] Escalas EBU +9/+18: la Tech 3341 las da en el **§ 2.7** («Scales and ranges»), no en el § 2.8
   («Display requirements»). Corregido en el texto y en la trazabilidad (secciones de la 3341
   rehechas: 2.1 nombres y máximos; 2.2 ventanas, puerta y 10 Hz; 2.3 puerta; 2.4 1 LU = 1 dB;
   2.7 escalas; 2.8 unidades).
3. [6] Escalas: la obligación rige **si el medidor muestra una escala** («may simply be numerical»).
   Añadida la salvedad y la escala por defecto («The 'EBU +9 scale' shall be used by default»).
4. [9/6] Pico verdadero, paso 1: la finalidad de la atenuación de 12,04 dB no era «dejar sitio a
   los valores por encima de la escala completa», sino margen para el procesado con aritmética de
   enteros, y la BS.1770 dice que el paso **«is not necessary»** en coma flotante. Corregido; el paso
   3 se rehace con las etapas del anexo 2 (filtro paso bajo, valor absoluto, compensación de 12,04
   dB, dBTP) y el paso 2 se apoya en cita («more accurately indicates the actual waveform…»).
5. [9] Cita del dBTP: la BS.1770 dice literalmente «The “dB TP”. Designation signifies…»; el tema la
   había retocado dentro de negrita. Sustituida por la cita literal **«in the units of dB TP»** y
   su significado en redonda.
6. [9] Vúmetro: «Su especificación sigue hoy en la norma CEI 60268-17 (1990)» no aparece en el texto
   accesible de Sound On Sound. Quitado el número de norma; queda lo que sí consta: especificación
   de 1940 que **«remains in use today»**. Ajustados «Lo que este tema no da» y trazabilidad (la
   referencia de los PPM queda como «Publicación 268-10 de la CEI», que es como la cita la 3205-E).
7. [6] Vúmetro: el +4 dBm = 0 VU es **con el atenuador del instrumento original a 0** (SOS). Añadido.
8. [6] PPM: los 10 ms y la caída a −12 en 2,8 s son del **modo normal**, y la caída es desde una
   lectura de +12. Añadido. La frase sin fuente «Un medidor de 10 ms no ve entero un transitorio
   más corto» se apoya ahora en la definición de la 3205-E (ráfaga de 5 kHz que marcaría +9
   **«results in an indication of +7»**). Tabla de medidores: «retorno lento» → «cae de +12 a −12
   en 2,8 s».
9. [9] «su portada dice … superseded by EBU R128»: es una nota de la página 2, no la portada.
   Corregido. Al releer, «Hoy es un documento histórico» tenía por antecedente la R 68 [1]: ahora
   dice «La Tech 3205-E es hoy…».
10. [9] Literalidad de citas: faltaban llamadas de referencia del original dentro de negrita —
    «ITU-R BS.1770 [3]», «BS.645 [2]», «EBU Tech 3344 [5]»— (el tema ya conservaba «Tech 3205-E
    [1]»). Añadidas.
11. [5] «dBm» salía (en cita) sin presentar: añadido a las siglas, con remisión a los temas 1 y 2.
12. Precisión: tabla de las etapas de la BS.1770, «(−70 y −10)» → «−70 LKFS y, después, 10 dB por
    debajo del nivel medido con el primero»; «El umbral relativo era de −8 LU hasta la versión 2»
    → «hasta que la versión 2 (2011) lo cambió a −10 LU».
13. Ficha: extensión 7.700 → 8.000 palabras (7.984 según `indice.py`). Trazabilidad: fecha de
    lectura directa, estado de versiones de la BS.1770, filas de la 3205-E y de SOS al día.

## Comprobado sin cambios

R 128: portada, historial V1–V5, considerandos a)–e), planteamiento, h)–p), notas 1 y 2,
definiciones, q)–v). BS.1770-5: alcance (anexos 1, 3 y 4), cuatro etapas, ponderación K y RLB,
tabla 3, LKFS, −3,01 LKFS, −0,691, límites (nota 1 y tonos puros), «subtracting 10», considerandos
del pico verdadero, 4× y 2×. Tech 3341: nombres, ventanas, puerta, 10 Hz, máximos, −23 LUFS = 0 LU,
unidades. Tech 3342: definición, ventana de 3 s, −70 LUFS y −20 LU, percentiles 10/95 y su razón.
Tech 3343: § 8.1, § 4.2, nota 3, § 6 (−27/−31 y descartar metadatos). R 68: 18 dB, 1:8 (18,06 dB).
RTW: cuatro citas, autor y fecha. SOS: 300 ms, correlación con el volumen percibido. Cálculos: −24 a
−22 LUFS; −23,2 a −22,8 LUFS; ±23 LU↔LUFS; tono −18 LUFS/+5 LU y ≈ −21 LUFS en un canal;
ejemplos de corrección de nivel. Remisiones a los temas 1, 3, 5, 8, 9 y 14: existen los epígrafes.

Diferencias de composición aceptadas (no son alteraciones): «·» entre líneas de la portada de la
R 128, «;» uniendo elementos de lista numerada (escalas y puerta de la 3341, etapas de la BS.1770),
llamadas de nota omitidas («time*», «18 dB²», «programme²»).

## Lentes

Tema técnico sin norma legal: `refutar_prosa.py` 0 hallazgos; `indice.py` 30 epígrafes, índice
sin cambios de rúbrica.
