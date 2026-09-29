# Grafista (15) · Tema 8 · Fase 5 bis (revisión de lo cambiado por el remate)

Tema: `temas/canal-sur-especificos/15-grafista/08-formatos-tecnicos-resolucion-codecs-alfa-zonas-seguras-colorimetria-hdr-entrega.md`.
Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha del sistema). Ficheros tocados: el tema y
este informe. Copia previa en el scratchpad (`15t08-antes-5bis.md`). Revisados sólo los 11 pasajes de
`15-T08-remate.md` (diff contra `15t08-antes-remate.md`).

## Comprobado sin cambios

| Pasaje | Fuente releída (29-09-2026) | Resultado |
|---|---|---|
| 3 · 4:4:4:4 | Apple, *Apple ProRes* (abril 2022), «Alpha Channel Support» | Cita literal exacta |
| 4 · Tasas ProRes | Mismo documento, «Family Overview» y «Note» | 500/330/220/147/102/45 Mbps a 1920x1080 y 29.97 fps, «66 percent», «roughly 70 percent», «only ProRes codecs that support alpha channels»: exactos |
| 5 · Rótulo zonas | Tabla del propio tema (ST 2046-1, 90 % en 720) | 1.152 × 648 cuadra |
| 6 · ICtCp | BT.2100-3, tabla 7, notas 7a; párrafo previo a tablas 6-7 (CI) | «I = 0.5L' + 0.5M'», CT/CP «colour difference signals», nota 7a: exactos |
| 7 · sRGB | PNG 3.ª ed. (W3C Rec. 24-06-2025) § 11.3.2.5 y tabla 17; WCAG 2.2 (12-12-2024) «relative luminance»; Blender 5.2 glosario; BT.709-6 (puntos 1.2, 1.3 y pesos 0.2126/0.7152/0.0722) | Valores y citas exactos |
| 8 · Cuentas ProRes 4444 | Apple | 330 Mbps a 29.97 fps |
| 1, 9, 10, 11 · Siglas, normas citadas, «no da», trazabilidad | — | Coherentes |

Antecedentes: «el mismo documento», «su tabla 7», «Las mismas WCAG 2.2», «(véase "La gamma")», «(véase
"Primarios y blanco de referencia")» tienen delante su referente (apartados existentes en el epígrafe 5).

## Corregido

1. **Contradicción (error 3)**, epígrafe 2 «Apple ProRes»: seguía «Las dos únicas tasas de este documento
   que el tema da son las de esas dos variantes» justo antes de la tabla nueva con seis. Se reescribe
   («Sus tasas objetivo… El mismo documento da también las del resto»).
2. **Tabla ProRes, columna Muestreo**: 4444 y 4444 XQ figuraban como 4:4:4:4, pero Apple da su tasa
   «for 4:4:4 sources» y el alfa es «optional». Queda «4:4:4 (4:4:4:4 con alfa)».
3. **IEC 61966-2-1 (error 9)**: ni la PNG ni las WCAG dan ese número; su referencia [SRGB] da el título
   («Part 2-1: … Default RGB colour space - sRGB») y enlaza webstore.iec.ch/publication/6169. Se leyó esa
   ficha (29-09-2026): «IEC 61966-2-1:1999». Se confirma y se añade el año, con fila nueva en Trazabilidad y
   matiz en «Lo que este tema no da» (sólo ficha de catálogo).
4. **Afirmación sin fuente (error 9)**: «trabajan por defecto la pantalla del ordenador, la web y buena parte
   de las imágenes» no constaba. Se sustituye por la nota 3 de las WCAG 2.2, literal: «Almost all systems
   used today to view web content assume sRGB encoding.» Trazabilidad de WCAG ampliada a la nota 3.
5. **Precisión técnica**: la fórmula de las WCAG va del valor codificado a la luz lineal; la de la BT.709-6,
   de la luz a la señal. Se dice, para que la comparación no parezca de curvas homólogas.
6. **Etiqueta**: «mismos colores posibles que el HD» es deducción (primarios comunes), no oficio; se marca así.
7. Entrada de siglas: «RGB estándar de la informática» → «RGB por defecto», como el título de la norma.
8. Extensión: `indice.py` da 18.340 palabras → «18.300 aproximadamente».

## Lentes

- `indice.py`: 18.340 palabras, 63 epígrafes, sin error.
- `refutar_prosa.py`: 2 avisos preexistentes, no reales (CBCR dentro de cita de Apple; HDR en el título).
- `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`: no proceden (sin norma jurídica).

Nota: Apple, PNG 3 y Blender siguen sólo en el scratchpad de la sesión, no en `fuentes/`; las WCAG 2.2
están en `fuentes/canal-sur/grafista/wcag22.txt`; la BT.2100-3 y BT.709-6 en `fuentes/canal-sur/montador/itu/`.

**Resultado: tema cerrado tras la 5 bis.**
