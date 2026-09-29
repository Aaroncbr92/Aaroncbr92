# Realizador/a (puesto 33) · Tema 14 · Fase 5, remate

Tema: `temas/canal-sur-especificos/33-realizador-a/14-formatos-video-resolucion-compresion-hdr-codecs-entregables.md`.
Fecha de trabajo: 24-09-2026 (encargo); fuentes leídas el 29-09-2026 (fecha del sistema). Entradas:
`33-T14-refutacion.md` (1 hallazgo menor, 1 laguna) y `33-T14-preguntas.md`. Copia previa del tema en
el directorio temporal de la sesión (`33t14-antes-remate.md`).

**Resultado: se amplió contenido nuevo (laguna de la pregunta 11). Toca 5 bis sobre los pasajes 2 a 4.**

## Correcciones

| # | Comprobación en la fuente | Aplicada |
|---|---|---|
| Hallazgo 1 (§ 1, «Qué decide el realizador sobre el formato») | Ficha 5351000: las dos tareas citadas no hablan de configurar grabadores ni de exportar ficheros. El informe acierta | Sí: «(lectura de la ficha)» → «(oficio, a partir de la ficha)» |

## Laguna de la pregunta 11 (perfiles HDR con metadatos dinámicos)

Fuentes leídas el 29-09-2026:

- Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (julio de 2026), cap. 10, p. 262 (lista de
  los cinco perfiles) y pp. 267 y 280-291 (Dolby Vision, niveles de metadatos y entrega; «SMPTE
  ST.2084 and HDR10»; HDR10+; HDR Vivid; HLG; informe de niveles de luz). El extracto que ya había
  (`resolve21-extractos/hdr.txt`) terminaba en la p. 274; las pp. 280-291 se extrajeron del PDF y se
  guardan en `fuentes/canal-sur/montador/resolve21-extractos/hdr-entrega.txt`.
- SMPTE Document Library, ficha de la ST 2094-40 (pub.smpte.org/doc/st2094-40/), guardada en
  `fuentes/canal-sur/montador/smpte/catalogo-st2094-40.txt`: título «Dynamic Metadata for Color Volume
  Transform — Application #4», publicaciones 2016-08-24 y 2020-04-09, «stabilized».
- Informe BT.2408-9: la cita de MovieLabs (l. 1037, ref. 5026) trata del escalado BT.709→HDR10, no de
  los perfiles; no aporta a la laguna y no se usa.

Negritas nuevas: 28, cotejadas con `negritas.py` contra las tres fuentes; todas literales (la de Dolby
Vision con «[…]» se comprobó en sus dos trozos).

## Pasajes cambiados

1. § 1, final del primer párrafo: etiqueta «(oficio, a partir de la ficha)».
2. § 5, «Los metadatos de masterizado»: se quita la frase «Los nombres comerciales de perfiles HDR…
   no se desarrollan aquí: no hay fuente normativa leída que los defina».
3. § 5, **epígrafe nuevo «Los perfiles de HDR y sus metadatos»** (tras «Los metadatos de
   masterizado»): los cinco perfiles del manual; tabla HDR10 / HDR10+ / Dolby Vision / HLG (metadatos
   y comportamiento en una pantalla de pico menor); título de la ST 2094-40 y la clasificación
   estática/dinámica, declarada oficio; consecuencias de entrega para el realizador (XML o IMF de
   Dolby Vision, .json o HEVC Main10 de HDR10+, informe de MaxCLL/MaxFALL), declaradas oficio.
4. Ficha (Fuente y Extensión, 19.600 → 20.600), siglas (BDA; BBC y NHK como las escribe la fuente),
   «Qué se puede preguntar», «Normas y documentos técnicos», «Lo que este tema no da» (bullet de HDR10
   reescrito: no leídas las especificaciones de BDA, Samsung, Dolby, UWA ni el texto de la ST 2094-40;
   siglas MaxCLL/MaxFALL sin desarrollo en lo leído), «Trazabilidad» (dos filas nuevas y la
   declaración de oficio ampliada). Índice regenerado.

Relectura de antecedentes: «el programa» ambiguo (software/programa de TV) cambiado dos veces por
«DaVinci Resolve»; «la norma que el manual nombra» tiene delante la ST 2094 de la tabla. Pregunta 11:
ahora entera (Dolby Vision y HDR10+ llevan metadatos plano a plano).

## Lentes

- `indice.py`: 20.643 palabras, 75 epígrafes; índice con el epígrafe nuevo.
- `refutar_prosa.py`: 3 «siglas sin presentar» (HD, UHD, HDR) en el título, que reproduce el
  enunciado; previas, no tocadas.
- `negritas.py`: véase arriba. `refutar_exactitud.py` y `refutar_modo.py` no se corren: los pasajes
  cambiados no citan normas jurídicas.

Ficheros tocados: el tema, este informe, `fuentes/canal-sur/montador/resolve21-extractos/hdr-entrega.txt`
y `fuentes/canal-sur/montador/smpte/catalogo-st2094-40.txt`.
