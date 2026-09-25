# Puesto 08 · Tema 7 · Fase 5 bis · Revisión de lo rematado

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Leídos: `ENCARGO.md`, enunciado del puesto 08, `08-T07-remate.md` (lista de 12 pasajes). Sólo se han revisado esos pasajes.

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Copia local | Qué se comprobó |
|---|---|---|
| Sony, *PXW-X400 Operating Instructions*, 2015 | `fuentes/fabricantes/Sony_PXW-X400_operating-instructions.txt` | «MPEG-2 Long GOP»; MPEG HD422 CBR 50 Mbps 422P@HL; HD420 HQ VBR 35 Mbps (max) MP@HL; XAVC-L 50 VBR 50 Mbps (max) H.264; página 144 (marcador «11. Appendix / 144» antes de «General», siguiente página 145) |
| Sony, *PXW-Z200 Help Guide* | `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt` | Lista de formatos y cadencias del MPEG HD (1080P 29.97/25/23.98, 1080i 59.94/50, 720P 59.94/50), en p. 336; el manual no nombra MPEG-2 |
| Avid, *Avid DNxHD Technology*, 2012 | `fuentes/fabricantes/Avid_DNxHD_white-paper-2012.txt` | Citas de definición, variantes y tabla de calidad; tabla de resoluciones 1080i/50 y 1080p/25; nota «* = Sub-sampled to 1440x1080» |
| Panasonic, *AVC-Intra FAQ*, pregunta 10 | `fuentes/fabricantes/Panasonic_AVC-Intra_FAQ.txt` | 16/32 min y 20/40 min por tarjeta de 16 GB; cuenta 1.280 s y «una cuarta parte menos» (16 ÷ 21,33 = 0,75) |
| DPC, «Fixity and checksums» | `fuentes/normas-tecnicas/DPC_fixity-and-checksums.txt` | Nivel 2: «Check fixity on all ingests», «Use write-blockers…», «Virus-check high risk content.»; nota «Write-blocking» y sus dos salvedades; «recommending four levels» |
| SD Association, libro blanco *Video Speed Class*, 2016 | `fuentes/fabricantes/SDA_Video-Speed-Class_white-paper-2016.pdf` | Figure 1 renderizada (p. 4): la tabla del tema casa fila a fila; citas de p. 4 y p. 5 (V30/C10, «match the SD memory card…», «A guide … owner’s manuals.») comprobadas por página con PyMuPDF |
| Library of Congress, fdd000389 (ProRes) | `fuentes/normas-tecnicas/LOC_fdd000389_ProRes422.txt` | Desarrollo de VBR («variable bit rate (VBR)») |

## Hallazgos

1. **Salvedad omitida (error 6), corregida.** Pasaje 6, párrafo de DNxHD a 25 cuadros: «Para 1080p/25 añade la 36 … Las cinco citadas son 4:2:2». La tabla de Avid da además, en 1080p/25, la **365x** (10 bits, 4:4:4, 367 Mb/s). Nueva redacción: «Para 1080p/25 repite esas cuatro y añade la 365x (10 bits, 4:4:4, 367 Mb/s) y la 36, a 36 Mb/s. Todas son 4:2:2 salvo la 365x.» Comprobado en la fuente: en 1080i/50 sólo hay las cuatro citadas; en 1080p/25, esas cuatro más 365x y 36.
2. **CBR (pasaje 2), sin cambio en el tema.** El remate lo daba como «desarrollo de oficio». Queda confirmado en fuente local: SMPTE ST 377-1, glosario, «CBR: Constant Bit Rate.» (`fuentes/archivos/SMPTE_ST377-1_MXF.txt`, l. 427). No se añade al tema porque este declara no haber leído el texto de las normas SMPTE; si se quiere, puede citarse en «Trazabilidad».

Todo lo demás de los 12 pasajes casa con su fuente: citas en negrita literales, cifras, páginas, cálculos (128 GB a 200 y 500 Mb/s; 200 Mb/s = 25 MB/s → V30/U3; 500 Mb/s = 62,5 MB/s → V90) y salvedades («se deduce del nombre y del fabricante»; «leído sobre la imagen»).

## Antecedentes

Releídos: «el mismo documento» (DNxHD, SDA), «la tabla de calidad», «esas cuatro» (nuevo: remite a las cuatro de 1080i/50), «la guía citada» (paso 3 → DPC en el paso 1), «la lista de la X400», «Dos salvedades del mismo documento». Todos tienen su antecedente.

## Comprobaciones

`refutar_prosa.py`: 0 hallazgos. El índice no cambia (no se tocaron rótulos).

## Ficheros tocados

El tema (un párrafo) y este informe.
