# Puesto 08 · Tema 7 · Fase 5 · Remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Leídos: `ENCARGO.md`, enunciado del puesto 08, `08-T07-refutacion.md`, `08-T07-preguntas.md`.

**Resultado: el remate AMPLÍA contenido nuevo** (L1 y L2, más las tasas de DNxHD a 25 cuadros). Procede la fase 5 bis.

## Fuentes releídas o nuevas (todas el 24-09-2026)

| Fuente | Copia local | Para |
|---|---|---|
| Avid, *Avid DNxHD Technology*, 2012 | `fuentes/fabricantes/Avid_DNxHD_white-paper-2012.txt` | G1: tabla «encoding quality» (bits, muestreo, «Bandwidth») y tabla «family of mastering resolutions» (1080i/50, 1080p/25; nota «* = Sub-sampled to 1440x1080») |
| DPC, «Fixity and checksums» | `fuentes/normas-tecnicas/DPC_fixity-and-checksums.txt` | M1: nota «Write-blocking» |
| Panasonic, *AVC-Intra FAQ*, pregunta 10 | `fuentes/fabricantes/Panasonic_AVC-Intra_FAQ.txt` | M2 |
| Sony, *PXW-Z200 Help Guide*, p. 336 | `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt` | L1: cadencias del MPEG HD |
| Sony, *PXW-X400 Operating Instructions*, 4-587-873-13(1), 2015, «Specifications», p. 144 | `fuentes/fabricantes/Sony_PXW-X400_operating-instructions.txt` (ya en el repositorio, lo trajo el remate de T01) | L1 |
| **Nueva**: SD Association, *Video Speed Class: The new capture protocol of SD 5.0*, libro blanco, febrero de 2016, pp. 4-5 | `fuentes/fabricantes/SDA_Video-Speed-Class_white-paper-2016.pdf` y `.txt` (descargado de sdcard.org/wp-content/uploads/2020/11/…; texto con `documento.py`) | L2. La tabla (Figure 1) es imagen: leída sobre la página 4 renderizada |

Intentos fallidos para L2: la página «Speed Class» de sdcard.org (403 con curl; con WebFetch, sin cifras), «Speed Class Standards for Video Recording» (tabla en imagen, no extraída) y «Bus Speed» (sólo velocidades de bus, no sirve).

## Correcciones de la refutación

- **G1 (DNxHD) — confirmada y aplicada.** La tabla de calidad da 36/100/145/220/440 Mb/s, 8 bits (36, 100, 145), «8- and 10-bit» (220), «10 bit» (444), 4:2:2 y 4:4:4 en la 444. Detalle: la tabla agrupa 220 y 220x en una columna. El texto dice «six userselectable bit rates» (guion perdido en el salto de línea): no lo cito en negrita, lo digo en redonda.
- **M1 (bloqueo de escritura) — confirmada y aplicada.** Además, en el paso 3 «pide» → «recomienda», por coherencia (la guía «recommending four levels»).
- **M2 (capacidad) — confirmada y aplicada.** Nota: la refutación decía «un 25 %». Cuenta: 1.280 s = 21,3 min; 16 es un 25 % menos que 21,3, pero 21,3 es un 33 % más que 16. Se escribe «una cuarta parte menos».

## Lagunas ampliadas

- **L1 (pregunta 7)**: el manual de la Z200 no explica el MPEG HD; se toma de la X400 («MPEG-2 Long GOP»; «MPEG HD422 mode: CBR, 50 Mbps, MPEG-2 422P@HL»; HD420 HQ VBR 35 Mbps máx.). Se declara que identificar el de la Z200 con el de la X400 es deducción por nombre y fabricante. No se afirma «XDCAM HD422»: el nombre no consta en las fuentes leídas.
- **L2 (pregunta 9)**: tabla de escritura mínima (2, 4, 6, 10, 30, 60, 90 MB/s) por familia; salvedad V30/C10 (p. 5); regla de ajustar a lo que pide el equipo (p. 5); cuenta de Mb/s a MB/s (cálculo).

## Pasajes cambiados

1. Portada: «Fuente» (añade X400 y el libro blanco de la SD Association); «Extensión» 11.000 → 12.000 palabras (`indice.py`: 12.110).
2. Siglas: añade VBR (desarrollo leído en la ficha de ProRes de la LOC) y CBR (desarrollo de oficio, por simetría); rótulos 422P@HL y MP@HL, sin desarrollar (no leídos).
3. «Qué se puede preguntar»: añade el MPEG HD 422 y los MB/s de cada clase.
4. «Cómo se lee el nombre de un formato»: párrafo nuevo sobre el MPEG HD (L1).
5. «La tasa y la capacidad»: párrafo reescrito (M2), con la cifra de 23,98p y la causa marcada como oficio.
6. «Avid DNxHD (SMPTE VC-3)»: frase de entrada, tabla con una columna nueva y párrafo nuevo sobre 1080i/50 y 1080p/25 (G1).
7. «Cuadro resumen», fila DNxHD: «De 36 a 440 Mb/s según variante; el tipo de compresión no lo desarrolla el documento de Avid leído».
8. «Las clases de velocidad»: se quita «La página no da las cifras…» y se añaden la tabla, las citas, las dos salvedades y el ejemplo de elección (L2).
9. «La ingesta de una tarjeta», pasos 1 y 3 (M1).
10. «Documentos técnicos que el tema cita»: filas de Avid, Panasonic y DPC ampliadas; filas nuevas del libro blanco SDA y de la X400.
11. «Lo que este tema no da»: se quita el hueco de los MB/s; sigue el de las VPG, y se añade que la especificación SD no se ha leído.
12. «Trazabilidad»: filas nuevas del libro blanco SDA y de la X400; en la lista de oficio, la elección de tarjeta «salvo lo que cita la SD Association», y en la de cálculo, el paso de Mb/s a MB/s.

He releído cada pasaje: «el mismo documento», «la lista», «la tabla del manual» tienen su antecedente.

## Comprobaciones

- Todas las citas nuevas en negrita casan con la copia local (espacios, apóstrofo y comillas normalizados). «Minimum Sequential Write Speed» está sólo en la imagen: va en redonda con «leído sobre la imagen».
- `refutar_prosa.py`: 0 hallazgos después de añadir las siglas (antes, HL y VBR). `indice.py`: índice regenerado, 54 epígrafes. Tema técnico sin norma: no se pasan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema; este informe; nuevos `fuentes/fabricantes/SDA_Video-Speed-Class_white-paper-2016.pdf` y `.txt`.
