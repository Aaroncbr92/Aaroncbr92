# Puesto 08 · Tema 7 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Leídos sólo `ENCARGO.md`, el enunciado del puesto 08 y el informe de redacción de T07.

## Fuentes releídas (todas el 24-09-2026)

- `fuentes/fabricantes/Sony_PXW-Z200_help-guide.pdf`: las páginas se han comprobado en el PDF, página a página
  (pymupdf), no en el `.txt`, cuyo orden de extracción mezcla páginas. Leídas completas pp. 31, 67, 68, 95-99,
  151, 153, 160-163, 196, 202, 242, 251-252, 298, 310-311, 336.
- `Sony_ILCE-1_help-guide_extractos.txt` («Notes on memory card», «File Format (movie)»);
  `Sony_ILCE-7SM3_formatos-fichero.txt` (entero); `Avid_DNxHD_white-paper-2012.txt` (pp. 3-4 y lista SMPTE);
  `Panasonic_AVC-Intra_FAQ.txt` (preguntas 1, 2, 4, 10, 12, 13).
- `fuentes/normas-tecnicas/`: `LOC_fdd000013_MXF.txt`, `LOC_fdd000389_ProRes422.txt` (fecha de revisión
  2024-05-09 en las dos), `DPC_fixity-and-checksums.txt` (tabla de niveles), `UIT-R_BT.709-6.txt` (2.1-2.5),
  `UIT-R_BT.2020-2.txt` (cuadro 1).
- `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 5.3.3 (p. 81) y p. 82.
- Web, con WebFetch: SD Association, «Speed Class» (las cuatro frases coinciden; la página sólo nombra
  «10MB/sec» de pasada, sin tabla por clase: el hueco declarado se mantiene); INCIBE, 29/09/2021 (la frase
  de la regla 3-2-1 coincide, «se refiere a disponer» … «diferente a los demás»).
- RTVE: `temas/edicion-montaje/05-soportes-formatos-e-ingesta.md` (§§ 7-8) y
  `temas/realizacion-tv/12-formatos-y-procesos-de-registro.md` (§§ 8, 10, 12).

Método: un cotejo automático de las 165 citas en negrita «…» contra las copias locales (espacios
normalizados). Sólo fallaron las web (SDA, INCIBE, releídas a mano) y la lista SMPTE de Avid (un tabulador
en la copia; el texto coincide).

## Copiado del común

Ninguno (según la redacción); nada que saltar.

## Copiado de RTVE (verificado)

Lo adaptado (XDCAM, tabla esencia/códec/contenedor, formatos de proyecto, SxS/P2/XDCAM, LTC/VITC, tres formas
de ingesta, RAID, LTO) coincide con los dos temas de RTVE y se declara oficio. Aritmética del código de
tiempo rehecha: 125.850 − 70.948 = 54.902 cuadros = 00:36:36:02. Cuentas de capacidad rehechas (85, 34 y
21 min).

## Hallazgos y correcciones (13)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | «cámara de mano» Sony PXW-Z200 | El manual dice «Solid-State Memory Camcorder». Ahora «videocámara» (igual que se corrigió en T06) |
| 2 | 6 | Cadencias de la Z200 con asterisco sin explicar | Añadida la nota de p. 336: «119.88P and 100P cannot be used when Slow & Quick Motion is turned on.» |
| 3 | 9 | ProRes «pensado para editar, no para emitir» | La misma ficha LOC dice que el MXF se añadió «as an option for broadcast delivery». Ahora «pensado para la posproducción», con la cita de la LOC |
| 4 | 3/9 | DNxHD: «el número de cada variante es su tasa a 1080i30» | Avid sólo lo dice de la 220x, la 220 (por remisión) y la 145; la 444, 100 y 36 no traen tasa. Restringido |
| 5 | 6 | Nombre de clip de la Z200 | [Title Prefix] y [Number Set] son «PXW-Z200 only» y sólo se configuran en MXF; «0001 to 9999» es el campo [Number Set]; [Series] salta al número más alto de la tarjeta si es mayor. Añadido |
| 6 | 6 | Sincronizar el código | La función es «(PXW-Z200 only)» (p. 298). Añadido |
| 7 | 4 | Libro de estilo «fijaba» / «pedía» barras | Fuente: «Es conveniente…» (una noticia por cinta y 30 s de barras) y «deben separarse» (dos noticias). Epígrafe «Lo que recomendaba el Libro de estilo», texto y «Qué se puede preguntar» corregidos; índice actualizado |
| 8 | — | Cita del Libro de estilo 5.3.3 con «puede ser recomendable es el TC» | Es literal del original; se deja y se avisa fuera de la cita |
| 9 | literal | DPC, cita de Bailey con «”» de cierre sin abrir | Quitado |
| 10 | 9 | «Virus-check high risk content», «para material que llega de fuera» | Glosa sin fuente. Ahora: las dos medidas son del segundo de los cuatro niveles (tabla DPC) |
| 11 | 6 | «Do not attach a label…»; «la tarjeta se identifica por fuera» | Añadida la razón del fabricante («You may not be able to remove the memory card.») y que el manual sí contempla escribir en el espacio de notas («Do not press down hard when writing in the memo space…») |
| 12 | 6 | LOC: P2 «can output MXF OP-Atom files» | La frase sigue «with DVC Pro encodings»: cita completada (DVC Pro, declarado como nombre de formato) |
| 13 | 6 | «El RAID protege del fallo de un disco» | El RAID 6 (en la tabla, doble paridad) aguanta dos. Añadido |

## Confirmado sin cambios

Z200: todas las páginas citadas casan en el PDF (31, 67, 68, 95, 96, 97, 98, 99, 151, 153, 160, 161, 162,
163, 196, 202, 242, 251, 252, 298, 310-311, 336); valores de fábrica ([Preset], [Rec Run], [DF], [Fix]);
trozo de *proxy* de 30 s, 1 y 2 min; aviso de 5 minutos; 9999/600 clips; 13/24 h; carpeta
/PRIVATE/M4ROOT/SUB (MP4, SDXC). UIT-R BT.709-6 2.2 y 2.4; BT.2020-2 cuadro 1. LOC MXF (ST 377-1, 378,
390, R122) y ProRes (ramas, rasgos, MXF en FCP 10.3, PSNR citando el libro blanco de Apple). Avid (VC-3,
SMPTE 2019-4, MXF, variantes; MOV confirmado: «QuickTime-wrapped versions»). Panasonic (preguntas 1, 2, 4,
10, 12, 13). Sony ILCE-1 e ILCE-7SM3 (todas). DPC (todas). Libro de estilo: páginas 81 y 82.

## Lentes

Sin normas jurídicas: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.
- `refutar_prosa.py`: 0 relleno, 0 repeticiones, 0 negritas rotas; tras las correcciones salieron RGB (ya
  estaba) y DVC; RGB presentada en siglas, DVC Pro añadido a los nombres de formato. Queda en 0.
- `indice.py`: 54 epígrafes, 10.963 palabras; portada puesta a 11.000.

## Ficheros tocados

Sólo el tema 7 y este informe.
