# Grafista (15) · Tema 8 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/08-formatos-tecnicos-resolucion-codecs-alfa-zonas-seguras-colorimetria-hdr-entrega.md`.
Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha del sistema). Ficheros tocados: el
tema y este informe. Copia previa del tema en el scratchpad de la sesión (`15t08-antes-remate.md`).

**Resultado: se amplió contenido nuevo (dos lagunas cerradas). Procede la fase 5 bis.**

## Hallazgos del informe de refutación

| N.º | Comprobación en la fuente | Aplicado |
|---|---|---|
| 1 · 4:4:4:4 no implica RGB | Apple, *Apple ProRes* (abril de 2022), «Alpha Channel Support»: «The sampling nomenclature for such Y’CBCRA or RGBA images is 4:4:4:4». El informe acierta | Sí: «una señal sin submuestreo de color, en RGB o en YCbCr, más el canal alfa», con la cita literal de Apple |
| 2 · ICtCp sin presentar | BT.2100-3 (`fuentes/canal-sur/montador/itu/bt2100.txt`), tabla 7 «Constant Intensity ICTCP signal format», «I = 0.5L' + 0.5M'», nota 7a «The newly introduced I, CT and CP symbols». La BT.2100-3 **no** usa «tritan» ni «protan»: no se ponen | Sí: se desarrolla en el texto (intensidad I, diferencias de color CT y CP) y se añade a los términos de entrada |
| 3 · Extensión | `indice.py`: 18.248 palabras tras el remate | Sí: «18.200 palabras aproximadamente» |
| 4 · Trazabilidad | Trazabilidad de los temas de origen: Realizador/a 14 (Contrato-programa, QC, ST 2094-40: 29-09-2026), Realizador/a 12 (R 95, ATEM: 29-09-2026), Montador/a 4 (24 y 25-09-2026), Montador/a 2 (R 103: 24-09-2026, por Cámara 9), Cámara 7 (Sony, Avid, Panasonic, LOC: 24-09-2026) | Sí: «epígrafes 1 a 7» y fecha de lectura del origen en cada fila «Tomado…» |
| 5 · Rótulo de la tabla de zonas | La fila 720 sale de la ST 2046-1 | Sí: «(cálculo sobre la R 95 y, en 720, sobre la ST 2046-1)» |
| Observación · 29,97 fps en «Cuentas» | Apple: «at 1920 x 1080 and 29.97 fps» | Sí |

## Lagunas (ampliación)

1. **sRGB frente a BT.709 (pregunta 12).** La IEC 61966-2-1 no se ha podido leer. Se amplía con fuentes
   publicadas que la citan: W3C PNG 3.ª ed. (24-06-2025), § 11.3.2.5 y tabla 17 (cromaticidades
   31270/32900, 64000/33000, 30000/60000, 15000/6000; gamma 45455; referencia [SRGB] = IEC 61966-2-1);
   W3C WCAG 2.2 (12-12-2024), «relative luminance» (0.2126/0.7152/0.0722; umbral 0.04045, 12.92,
   exponente 2.4; «Formula taken from [SRGB]»); glosario del manual de Blender 5.2 («uses the Rec.709
   Primaries and a D65 white point»; «approximate 2.2 gamma»). Cotejado con la BT.709-6 (punto 1.2,
   1,099 L^0,45 − 0,099; 4,500 L). La pregunta 12 queda contestada entera.
2. **Tasas del resto de ProRes (pregunta 6).** Del mismo documento de Apple: 422 HQ 220, 422 147, LT 102,
   Proxy 45 Mb/s a 1080/29,97; «66 percent», «roughly 70 percent»; «the only ProRes codecs that support
   alpha channels». La pregunta 6 queda contestada entera (b).

## Pasajes cambiados (para la fase 5 bis)

1. Términos de entrada: añadidos CI e ICtCp (I, CT, CP); sRGB presentado (IEC 61966-2-1) en lugar de
   «sólo se nombra»; siglas IEC, W3C y WCAG.
2. Portada, «Extensión».
3. Epígrafe 2, «El muestreo cromático», párrafo de la cuarta cifra.
4. Epígrafe 2, «Apple ProRes»: tabla nueva de la familia y dos citas.
5. Epígrafe 4, «El grafista y las zonas seguras», rótulo de la tabla.
6. Epígrafe 5, «Luminancia constante y no constante»: desarrollo de ICtCp.
7. Epígrafe 5, «Del programa de diseño a la señal de vídeo»: bloque nuevo sobre el sRGB (cuatro
   puntos y resumen). El punto del rango es deducción de la fórmula de las WCAG y se dice así.
8. «Cuentas que se piden», fila del ProRes 4444.
9. «Normas y documentos técnicos que el tema cita»: W3C (PNG y WCAG 2.2).
10. «Lo que este tema no da»: la IEC 61966-2-1, no leída directamente; perfil por defecto de cada programa.
11. «Trazabilidad»: párrafo de entrada, fechas de origen en las filas «Tomado…», filas nuevas (PNG 3,
    WCAG 2.2, BT.2100-3 tabla 7), Apple y Blender ampliadas.

Antecedentes releídos: «(véase "Primarios y blanco de referencia")» y «(véase "La gamma")» remiten a
apartados del mismo epígrafe 5; «el mismo documento» (ProRes) tiene delante *Apple ProRes*; «su tabla 7»
tiene delante la BT.2100-3.

Nota: las fuentes de Apple, PNG 3, WCAG 2.2 y Blender están sólo en el scratchpad de la sesión
(`t08v/Apple_ProRes.txt`, `png3.txt`, `g15a/wcag22.txt`, `t08v/…blender…glossary…txt`), no en `fuentes/`.

## Lentes

- `indice.py`: 18.248 palabras, 63 epígrafes, sin error.
- `refutar_prosa.py`: 2 avisos, ninguno real: «CBCR» está dentro de la cita literal de Apple (Y'CbCr ya
  presentado) y «HDR» en el título, antes de las siglas (preexistente).
- `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`: no proceden (no se ha tocado cita de norma
  jurídica).
