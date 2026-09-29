# Grafista (15) · Tema 8 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/08-formatos-tecnicos-resolucion-codecs-alfa-zonas-seguras-colorimetria-hdr-entrega.md`
(1.519 líneas, unas 17.900 palabras). Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026
(fecha del sistema). No corrijo: sólo informo. Ficheros tocados: este informe y `15-T08-preguntas.md`.

Alcance de la exactitud: lo que no figura en «Copiado del común» ni en «Copiado de RTVE sin cambios» de
`15-T08-redaccion.md`. La cobertura mira el tema entero.

## 1. Lo cotejado en la fuente (sin hallazgo)

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| Epígrafe 1: 720 y 360 muestras de la BT.601-7; «entrelazada» | `fuentes/normas-tecnicas/UIT-R_BT.601-7.txt` (punto 6 de la tabla; l. 112) | Bien |
| Epígrafe 2: definición de 4:4:4, 4:2:2 y 4:2:0 | `bt2100.txt`, l. 925-940 | Literal |
| Epígrafe 2: rango completo de la BT.2100-3 (0; 1.023/4.095) | `bt2100.txt`, tabla 9 | Bien |
| Epígrafe 3: ST 2110-20 (§ 7.4.1 llave con «ALPHA» sin TCS; § 7.5 valor ALPHA; § 7.6 regla del receptor) | `SMPTE_ST-2110-20-2022.txt`, l. 900-965 | Literal y bien situado |
| Epígrafe 5: primarios y blanco (BT.709-6, BT.2020-2; 630/532/467 nm de la BT.2100-3) | `bt709.txt`, `bt2020.txt`, `bt2100.txt` | Bien |
| Epígrafe 5: coeficientes 0,299/0,587/0,114; 0,2126/0,7152/0,0722; 0,2627/0,6780/0,0593 | BT.601-7, BT.709-6, BT.2020-2 | Bien; suman 1 |
| Epígrafe 5: notas (2) y (3) de la tabla 4 de la BT.2020-2 (CL/NCL) | `bt2020.txt`, l. 598-603 | Literales, completas |
| Epígrafe 5: NCL por defecto e intensidad constante | `bt2100.txt`, l. 814-816 | Literal |
| Epígrafe 5: BT.2408-9 § 9 (imagen fija, CICP = UIT-T H.273, cuatro señales, PNG/TIFF/AVIF/HEIF, rango) y § 5.1 («BT.2020 container») | `bt2408.txt`, l. 934-940 y 2684-2734 | Literales; H.273 es UIT-T; bien |
| Epígrafe 6: § 9 de la BT.2408-9 (Graphics White 75 % HLG / 58 % PQ; display-light / scene-light) y edición 03/2026 | `bt2408.txt`, l. 11 y 2685-2691 | Literal |
| Epígrafe 4: cuentas de la R 95 y la ST 2046-1 (1080: líneas 80-1083 y 96-1067; 2160: 3572 × 2008 y 3456 × 1944; 720: 1152 × 648) | Cálculo | Bien |
| Epígrafe 1 y 2, aplicación práctica: 6.220.800, 8.294.400, 33.177.600 bytes; 207 MB/s; 12,4 GB/min; 330 × 60 ÷ 8 = 2.475 MB | Cálculo | Bien |

Apple, Vizrt, Blender, Resolve 21 y la ST 2046-1 no están en el repositorio (sólo en el scratchpad de la
sesión de verificación): no se han podido volver a leer. Las citas son coherentes entre sí y con lo que
declara la verificación; no hay indicio de error.

## 2. Hallazgos

### Graves

Ninguno.

### Menores

1. **Epígrafe 2, «El muestreo cromático», párrafo de la cuarta cifra (error 9).** «Un archivo de vídeo con
   muestreo cromático 4:4:4:4 significa que tiene una señal de vídeo RGB sin submuestreo de color más
   información del canal alfa.» La notación no implica RGB: el propio tema cita a la BT.2100-3, que define
   el 4:4:4 respecto de «**the Y' or I component**», es decir, también en Y'CbCr; y Apple habla de
   «**4:4:4:4 image sources**», sin fijar el modelo. Propuesta: «una señal sin submuestreo de color (RGB o
   YCbCr) más el canal alfa».
2. **Epígrafe 5, «Luminancia constante y no constante» (error 5).** «la señal ICtCp de su tabla 7»: ICtCp
   no se presenta en las siglas ni en el texto. Añadirla a los nombres de «Los términos técnicos» o
   desarrollarla (intensidad, y las dos diferencias de color *tritan* y *protan*, si se confirma en la
   BT.2100-3) o quedarse en «la señal de intensidad constante de su tabla 7».
3. **Portada, «Extensión» (error 3).** Dice «17.200 palabras aproximadamente»; el tema tiene unas 17.900
   (17.929 según la verificación).
4. **«Trazabilidad», párrafo de entrada y columna «Lectura».** Dice que vienen de temas cerrados las
   fuentes «de los epígrafes 1, 2 y 3», pero también lo son las de los epígrafes 4 y 7 (R 95, R 103,
   R 128, AS-11, *Quality Control*, fichas SMPTE); y las filas «Tomado del tema…» no dan la fecha de
   lectura que el encargo pide declarar. Basta con «epígrafes 1 a 7» y la fecha de lectura del tema de
   origen en cada fila.
5. **Epígrafe 4, «El grafista y las zonas seguras», tabla.** El rótulo «(cálculo sobre la R 95)» cubre una
   fila marcada «1.280 × 720 (SMPTE)», que sale de la ST 2046-1. Cambiar el rótulo a «(cálculo sobre la
   R 95 y, en 720, la ST 2046-1)».

Observación, no hallazgo: en «Cuentas que se piden», la fila del ProRes 4444 no repite que los 330 Mb/s
de Apple son a 29,97 fps; el epígrafe 2 sí lo dice. Podría añadirse «(a 29,97 fps)».

## 3. Cobertura del enunciado

Las siete materias del enunciado (resolución, códecs, alfa, *safe areas*, colorimetría, HDR/SDR y
entrega para emisión) tienen epígrafe propio, en su orden, con teoría, cifras y aplicación práctica.
Preguntas (`15-T08-preguntas.md`): 13 enteras, 0 a medias, 2 no.

### Lagunas

1. **sRGB frente a BT.709 (pregunta 12).** El grafista diseña en programas que trabajan en sRGB, y la
   relación con la BT.709 (mismos primarios y blanco D65; distinta curva de transferencia) es pregunta
   natural de test y de la prueba práctica. El tema la declara no comprobada. Ampliar con fuente
   publicada (IEC 61966-2-1 o documentación de fabricante que la cite) en «Del programa de diseño a la
   señal de vídeo»; si no se confirma, se mantiene el hueco declarado.
2. **Tasas del resto de la familia ProRes (pregunta 6).** El tema da sólo 4444 y 4444 XQ y declara que no
   da las demás, aunque salen del mismo documento de Apple ya leído. Una línea con las tasas de 422 HQ,
   422, LT y Proxy a 1080/29,97 (del mismo documento) cierra la laguna sin nueva fuente.

## 4. Lentes

No pasadas de nuevo: el tema no cita norma jurídica salvo el Contrato-programa (ya pasado por
`refutar_exactitud.py` y `refutar_modo.py` en la verificación, 0 hallazgos). Cero graves: el tema está
bien en lo esencial.
