# Puesto 30 · Tema 7 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`.
Entrada: `30-T07-refutacion.md` y `30-T07-preguntas.md`. **Se amplió contenido nuevo** (dos lagunas):
procede 5 bis. Copia previa: `30t07-antes-remate.md` en el scratchpad.

## Fuentes releídas antes de aplicar (25-09-2026)

| Fuente | Qué |
|---|---|
| *DaVinci Resolve 21 Reference Manual* (PDF de julio de 2026, metadatos 09-07-2026), cap. 58 «Speed Effects», pp. 1253-1266 | Leído entero; extracto con marcas `[[pNNNN]]` guardado en `fuentes/canal-sur/montador/resolve21-extractos/speed.txt` (página PDF = página impresa) |
| Resolve 21, extracto `titles.txt`, p. 1214 | Guías *Social Media* |
| UBU, *Guía para elaborar Material Multimedia Accesible* (txt) | Pp. impresas 4, 5, 6 y 7 |
| une.org (ficha de la UNE 153010) | 403: no se pudo leer; por eso se quita lo no sostenido, no se confirma |

## Correcciones y ampliaciones (todas confirmadas en la fuente)

| # | Origen | Dónde | Qué se cambió |
|---|---|---|---|
| 1 | Exactitud 1 | § 4 «Las zonas de seguridad» | «guías de 1:1, 4:5 y 9:16» → «guías *Social Media* de **«1:1, 4:5, 9:16, 1.91:1, 16:9»**» (literal, p. 1214) |
| 2 | Exactitud 2 | Aplicación práctica, paso 4 | Añadido «(criterio tomado, por oficio, de la síntesis de la UNE 153010, que es norma de subtitulado para personas sordas, no de traducción)» |
| 3 | Exactitud 3 | Siglas | «Asociación Española de Normalización (UNE es la sigla de sus normas)» → «UNE, la sigla con la que se numeran las normas españolas, que la guía de la Universidad de Burgos cita como publicadas por AENOR (la guía no desarrolla esta otra sigla)» |
| 4 | Exactitud 3 | Tabla de normativa | Fuera «(hoy Asociación Española de Normalización)» |
| 5 | Exactitud 3 | § 5 «Los criterios» y «Lo que este tema no da» | Fuera «es de pago»; queda «no se ha leído» |
| 6 | Cobertura 1 (preg. 11 y 12) | § 5 «Los criterios del subtitulado» | Rótulo de páginas (pp. 4-5 visuales, p. 6 tiempo). Filas nuevas literales: pausas y tipografía (p. 4), información contextual (p. 4 y p. 6), mayúsculas, cursiva, números, paréntesis (p. 5), efectos sonoros (p. 6, en redonda). Párrafo que declara la incoherencia de la guía (mayúsculas p. 5 frente a p. 6). Tabla de las ocho combinaciones de color por orden de legibilidad (p. 5), su uso para personajes y el orden color-etiquetas-guiones (pp. 6-7) |
| 7 | Cobertura 2 (preg. 7) | § 3, epígrafe nuevo «Los efectos de tiempo» (antes de «Los efectos y la información») | Definición (p. 1254); tabla de velocidad constante, marcha atrás, congelado y velocidad variable (pp. 1254-1264); flechas amarillas y azules (p. 1258); audio y *Pitch Correction* (pp. 1254-1256); *Retime Process* y sus tres opciones literales *Nearest*, *Frame Blend*, *Optical Flow* (p. 1265); límites del flujo óptico y modos de estimación (pp. 1265-1266); cuenta propia del 50 % a 25 i/s |
| 8 | — | «Qué se puede preguntar» | Añadidos efectos de tiempo e interpolación, y colores, cursivas y mayúsculas de la síntesis |
| 9 | — | Trazabilidad | Resolve: añadido cap. 58, pp. 1254-1266; UBU: pp. 4 a 7 |
| 10 | — | Ficha | Extensión: 12.500 → 13.500 palabras (13.651 medidas) |

La refutación no se equivocó. Precisión: la información contextual entre paréntesis está en la p. 4,
no en la 5 como decía; las pausas y la tipografía, en la p. 4, como decía.

## Lentes

- `indice.py`: 13.651 palabras, 50 epígrafes; índice regenerado con «Los efectos de tiempo». El tema
  no está en `portadas.tsv` (el script avisa «sin portada»): la extensión de la ficha se cambió a mano.
- `negritas.py` (extractos de Resolve con `speed.txt`, UBU, Adobe): 173 cotejadas, 45 «no están»,
  todas de fuentes no pasadas (Libro, BT.2408, REBT, lo copiado del común); ninguna de las nuevas.
- `refutar_prosa.py`: 0 hallazgos.
- Sin normas jurídicas nuevas: no proceden `refutar_exactitud.py` ni `refutar_modo.py`.

Antecedentes releídos: «Ese orden» sigue a la tabla de colores; «La guía no es del todo coherente»
sigue a la tabla de criterios; «El flujo óptico tiene su límite» y «El mismo proceso» siguen a la
tabla del *Retime Process*.

## Ficheros tocados

El tema, este informe y el extracto nuevo `fuentes/canal-sur/montador/resolve21-extractos/speed.txt`.
`fuentes/canal-sur/BOE-A-2023-11022.md` figura modificado en `git status`, pero no por este remate.

## Adenda (relanzamiento de la fase 5, 25-09-2026)

El remate ya estaba hecho (arriba) y revisado en la fase 5 bis (`30-T07-final.md`, con cuatro ajustes
sobre pasajes nuevos). No se reaplica nada para no pisar esos ajustes. Comprobado que siguen en el
tema: «Los efectos de tiempo», las guías *Social Media* con 1.91:1, *Optical Flow*, y fuera «hoy
Asociación Española». `indice.py`: 13.660 palabras, 50 epígrafes, sin cambios en el índice.
`refutar_prosa.py`: 0 hallazgos. Ficheros tocados: sólo este informe.
