# Grafista (15) · Tema 8 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/08-formatos-tecnicos-resolucion-codecs-alfa-zonas-seguras-colorimetria-hdr-entrega.md`
(17.929 palabras tras la verificación; 63 epígrafes). Fecha del encargo: 24-09-2026; fuentes leídas el
29-09-2026 (fecha del sistema). Ficheros tocados: sólo el tema y este informe. Copia previa del tema en el
scratchpad de la sesión (`t08v/08-antes.md`).

## 1. Lo copiado: sólo cotejo de literalidad

Cotejo automático bloque a bloque (párrafos y filas de tabla, sin negritas ni acentos graves) contra
Montador/a 04, Realizador/a 12 y 14 y los temas de RTVE `diseno-grafico/02`, `10`, `11` y
`edicion-montaje/02`. No se re-verificó el contenido.

- «Copiado del común» (30 pasajes): literales. Los que no casan al 100 % lo hacen sólo en los ajustes que
  declara la redacción (remisiones «§ N» → «epígrafe N», «(tema 14)» suprimido, primera frase del
  subepígrafe del grafismo en HDR, «citada en el epígrafe 2», fila 0001F y cierre del control de calidad).
  Además, el párrafo del AFD (ítem 0001F, epígrafe 1, «La relación de aspecto y sus arreglos») es literal
  de Realizador/a 14 con «(§ 8)» → «(epígrafe 7)» y la frase de remisión cambiada; no estaba en la lista,
  pero es copiado cerrado: no se re-verificó.
- «Copiado de RTVE sin cambios»: literales. Salvedad: en el epígrafe 5, la frase de `diseno-grafico/10` § 2
  acaba en «…no lo lleva» y el tema le añade «: el PNG no admite el modo CMYK, y el PSD, el JPG y el TIFF
  sí (oficio)». Esa cola es nueva; se cotejó con la tabla «¿Admite CMYK?» del mismo tema de RTVE y casa.
- Primer bullet de «Los errores de entrega con el alfa»: rótulo «Entregar sin alfa:» + frase de RTVE + frase
  de R12, literales; los otros tres bullets son nuevos y se verificaron (abajo).

## 2. Lo verificado en su fuente

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| Epígrafe 2: muestreo (citas de la BT.2100-3), bits (BT.709-6 punto 4.5, BT.2020-2, BT.2100-3 tabla 9), niveles (BT.709-6 puntos 4.6 y 4.7), rango estrecho y completo | `montador/itu/bt709.txt`, `bt2020.txt`, `bt2100.txt` | Literales y bien atribuidos. Corregida la descripción de la notación del muestreo (error 9, ver 3.1) |
| Epígrafe 2: Viz Engine (Downscale Luma, Allow Super White, Allow Chroma Clipping) | Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output» (docs.vizrt.com, descargada el 29-09-2026) | Literales; «Default mode is Active/Inactive» confirmados. Corregida la frase que presentaba la opción de la llave como conversión general de la salida (3.2) |
| Epígrafe 2: ProRes 4444 y 4444 XQ, 330 y 500 Mb/s, alfa hasta 16 bits, «only ProRes codecs that support alpha» | Apple, *Apple ProRes*, «April 2022» (apple.com, descargado el 29-09-2026) | Literales (la elisión «[…]» es correcta). Cuentas: 330 × 60 ÷ 8 = 2.475 MB; bien |
| Epígrafe 2: DNxHD sin «alpha» | `fuentes/fabricantes/Avid_DNxHD_white-paper-2012.txt` | 0 apariciones de «alpha»; bien |
| Epígrafe 1: cálculos de tamaño de fotograma | Cálculo | 6.220.800, 8.294.400, 33.177.600 bytes; 207 MB/s y 12,4 GB/min a 25 fps; bien |
| Epígrafe 3: alfa directo y premultiplicado | *DaVinci Resolve 21 Reference Manual* («July 2026»), cap. 77, volcado del scratchpad | Citas literales; páginas bien: definiciones y «not multiplied» en p. 1726, «Most computer-generated…» en p. 1727, reglas y *bright fringe* en p. 1728 (la errata «Unpremultipled» es del original) |
| Epígrafe 3: glosario de Blender | *Blender 5.2 LTS Manual*, Glossary (docs.blender.org/manual/en/5.2, descargado el 29-09-2026) | Literales |
| Epígrafe 3: relleno y llave de Vizrt | *Viz Engine Administrator Guide* 5.2 «Dual Channel Mode» y 5.4 «Video Output» | Literales (Contains Alpha, Invert Luma, Watchdog Key Opaque, H-delay) |
| Epígrafe 3: ATEM | `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt`, líneas 419-420 y 1564-1565 | Literales |
| Epígrafe 3: ST 2110-20 y la señal de llave | `fuentes/normas-tecnicas/SMPTE_ST-2110-20-2022.txt`, §§ 7.4.1, 7.5 y 7.6 | Error 4 corregido (3.3) |
| Epígrafe 4: SMPTE ST 2046-1:2009 entera (introducción, §§ 1, 4.3-4.5, 5, 5.1-5.4, notas, bibliografía) | PDF de pub.smpte.org, descargado y pasado a texto el 29-09-2026; ficha de la biblioteca: «active», única «Publication (2009-11-23)» | Todas las citas literales y con su apartado correcto; aprobación «November 23, 2009». Cuentas: 1786 × 1004, 1728 × 972, 1190 × 670, 1152 × 648 (márgenes 64 y 36), 670 × 536, 648 × 518, 670 × 446, 648 × 432; bien. Marcado como oficio lo del recorte de los tubos (3.4) |
| Epígrafe 4: comparación EBU/SMPTE | R95 (vía R12) y ST 2046-1 | Cuentas de líneas (80-1083 = 1004; 96-1067 = 972) y 2160 (3572 × 2008; 3456 × 1944): bien |
| Epígrafe 5: primarios y blanco | BT.709-6 puntos 1.3 y 1.4; BT.2020-2 tabla 3; BT.2100-3 tabla 2 (630, 532, 467 nm) | Literales |
| Epígrafe 5: coeficientes de luminancia | BT.709-6 punto 3.2; BT.2020-2 tabla 4; `UIT-R_BT.601-7.txt` (0,299/0,587/0,114) | Bien; suman 1 |
| Epígrafe 5: CL y NCL | BT.2020-2, notas de la tabla 4; BT.2100-3, texto previo a la tabla 6 | Errores 6 corregidos (3.5 y 3.6) |
| Epígrafe 5: BT.2408-9 § 5.1 («BT.2020 container») y § 9 (imagen fija, CICP, H.273) | `montador/itu/bt2408.txt` | Literales; H.273 es Recomendación UIT-T; bien |
| Epígrafe 5: gamma y BT.1886 | BT.709-6, nota (1) y punto 3.1 | Bien |
| Epígrafe 6: perfiles de HDR (primer párrafo, nuevo) | *DaVinci Resolve 21 Reference Manual*, lista de «five principal approaches» y apartados de HDR10+, HDR Vivid y HLG | Los cinco nombres y las dos citas, literales; la frase de los metadatos se marca como oficio (3.7) |
| Epígrafe 6: tabla «Lo que el grafista hace con eso» | BT.2408-9 §§ 5.1, 5.2 y 9, tabla 1 | Coherente con las citas |
| Epígrafe 7 y aplicación práctica | Oficio y cálculo; 0021B citado de R14 | Cuentas bien; referencia de secciones corregida (3.8) |
| Remisiones internas (error 1) | Todo el tema | «epígrafe N» y «tema N» apuntan bien (temas 2, 5, 6, 9, 10 y 13 casan con el enunciado) |

## 3. Correcciones aplicadas (comprobadas en la fuente antes de aplicarlas)

1. **Muestreo (error 9).** «tres o cuatro cifras, y cada una cuenta muestras en un bloque de cuatro por
   dos» no es exacto: la primera cifra es el ancho del bloque y la cuarta, el alfa. Reescrito (oficio):
   primera = ancho, las otras dos = muestras de color en la primera y en la segunda fila, cuarta = alfa.
2. **Viz Engine (error 9).** «Un motor de grafismo de directo hace esa conversión en su salida» no lo
   sostiene la cita, que es de la señal de llave. Ahora: rango completo/estrecho como oficio, y «en Viz
   Engine, la señal de llave tiene una opción que hace esa conversión».
3. **ST 2110-20 (error 4).** «exime a las señales de llave de declarar la curva» → la norma **obliga** a
   la llave a declarar «ALPHA» y **le prohíbe** declarar TCS: se añade «the Key stream shall signal the
   colorimetry value “ALPHA”, and shall not signal a TCS value.» (§ 7.4.1) y se sitúa la regla del
   receptor en el § 7.6. TCS: «SDR, PQ o HLG, entre otros valores» (la norma da más: LINEAR,
   BT2100LINPQ, ST2115LOGS3…).
4. **Zonas seguras (error 9).** «televisores de tubo, que recortaban los bordes» se marca como oficio y
   se apoya en la cita de la ST 2046-1 («were based on analog transmission and CRT displays», de la
   RP 218 y la RP 27.3).
5. **BT.2020-2, luminancia constante (error 6).** La cita se cortaba antes de «or where there is an
   expectation of improved coding efficiency for delivery»; completada.
6. **BT.2100-3 (error 6).** El tema daba a entender que la BT.2100 elige entre CL y NCL; en ella la
   alternativa no es la luminancia constante sino la intensidad constante (ICtCp, tabla 7). Añadido, con
   la frase siguiente de la fuente («The Constant Intensity (CI) format is newly introduced… unless all
   parties agree.»).
7. **Perfiles de HDR.** «lo que los separa son los metadatos» no es cita: marcado «(oficio)».
8. **BT.2408-9, secciones.** La aplicación práctica usa la bajada a SDR por luz de pantalla (§ 5.2): «§§
   5.1 y 9» → «§§ 5.1, 5.2 y 9». En «Trazabilidad», la fila de la BT.2408-9 pasa a «§§ 2.1, 5.1, 5.2, 7.1 y
   9» (las citas del epígrafe 6 incluyen la bajada y las idas y vueltas).
9. **Siglas (error 5).** «sRGB» aparecía sin presentar: añadido a la lista de nombres que sólo se nombran.
10. **Trazabilidad.** ST 2110-20 con sus §§ y la relectura de hoy; BT.2100-3 con la intensidad constante;
    Resolve con HDR Vivid y la lista de los cinco perfiles releída hoy.

Nada se ha quitado: todo lo demás se confirmó en su fuente.

## 4. Lentes

- `negritas.py` contra las UIT (BT.601-7, 709-6, 2020-2, 2100-3, 2408-9), ST 2110-20, LOC, Contrato-programa,
  R 95, ATEM, Avid, Panasonic, Sony Z200, catálogos SMPTE, AS-11, R 128, ST 2046-1, Apple, Vizrt, Blender y
  Resolve 21: 205 negritas; 42 «NO ESTÁ», todas de pasajes copiados de fuentes que no están en el
  repositorio (R 103, hoja y catálogo QC de la EBU, guías Sony, FAQ de AVC-Intra con elisiones, LOC con
  elisiones) o con «[…]» (Apple y *Graphics White* de la BT.2408-9, cotejadas a mano: literales).
- `refutar_prosa.py`: 1 hallazgo, falso positivo (HDR en el título; se presenta en «Los términos técnicos»).
- `refutar_exactitud.py` y `refutar_modo.py` con el Contrato-programa: 0 hallazgos (el tema no cita
  artículos de norma jurídica; sólo el RD 16/2023 dentro de la cita del punto 101).
- `indice.py`: índice regenerado, 63 epígrafes.

## 5. Para el coordinador

- Extensión: 17.929 palabras, muy por encima de los demás temas del puesto (lo avisó la redacción, con su
  propuesta de recorte).
- Las fuentes externas descargadas hoy (ST 2046-1, Apple, Vizrt, Blender) están sólo en el scratchpad de
  la sesión, no en `fuentes/`.
