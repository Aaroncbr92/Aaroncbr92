# Grafista (15) · Tema 2 · Revisión del remate (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/02-identidad-visual-corporativa-manual-de-marca.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema).
Alcance: sólo los pasajes listados en `15-T02-remate.md`. Ficheros tocados: el tema y este informe.

## Pasajes revisados, dato a dato

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| Siglas (OTT, DOI; fuera CSS, HD, UHD) | cuerpo del tema | OTT (ll. 182, 857) y DOI (l. 871) se usan; HD y UHD no aparecen; CSS sólo en una URL. Correcto |
| Ficha: Fuente y Extensión | `indice.py` | 10.063 palabras, 41 epígrafes: cuadra con «10.000 aproximadamente» |
| «La arquitectura de marca», último párrafo | Contrato-programa, BOJA 245/2023, puntos 52 (ll. 1409-1416) y 110 (ll. 2123-2125), cláusula tercera | Los tres literales, exactos. «El punto 52», «el documento», «los vuelve a nombrar» tienen antecedente |
| «Qué hace legible…»: párrafo de Google Fonts | `google-fonts-knowledge-glosario.txt` | Definiciones de *legibility* y *readability*, literales. La frase sobre de qué depende la lecturabilidad no tenía fuente: **marcada como oficio** |
| «Tres fuentes publicadas lo concretan» | tema | Recuento correcto: UCF (Frutiger), *Fonseca*, Android TV |
| Párrafo de Android TV | `android-tv-typography.txt`, ll. 27-32 | Dos literales exactos (incluido «from one other», errata del original) |
| «El contraste medible»: frase que presenta las viñetas | `wcag22.txt`, ll. 443-446, 1467-1472, 1631-1632, 1808-1810 | Las viñetas usan **tres** definiciones del glosario (*contrast ratio*, *relative luminance*, *large scale*), no dos: **corregido** a «Tres definiciones… (relación de contraste, luminancia relativa y texto grande)». Las dos salvedades, del 1.4.3: correcto |
| «El círculo cromático y las armonías» | `sessions-college-color-wheel.txt` | Todos los literales, exactos; los seis ejemplos coinciden. Rojo-verde: sale del ejemplo tetrádico y lo confirma la complementaria dividida (verde con rojo anaranjado y rojo violáceo); azul-naranja, del ejemplo complementario. «(tabla de «Las dos mezclas»)»: rojo-cian y azul-amarillo, correcto. «(epígrafe 4)» apunta a Legibilidad, donde está el contraste: correcto |
| «Las medidas de la letra», desde las medidas verticales | glosario de Google Fonts | Literales exactos. Ascendentes: el tema decía «los trazos de la minúscula»; la fuente dice **«parts of letterforms»**, sin limitarlo a la minúscula: **corregido** a «Las partes de la letra». «La primera con la segunda» sigue apuntando a la tabla de kerning, que va antes |
| «Normativa que el tema invoca» | Contrato-programa, puntos 45 (l. 1299) y 46 (l. 1315); Acuerdo de 19-XII-2023 (l. 12) | El cuerpo usa «Canal Sur Más» y «Canal Sur Media», que «Trazabilidad» atribuye a los puntos 45 y 46, pero la lista no los tenía: **añadidos** (puntos 45, 46, 52, 105, 110 y 112). Fecha del Acuerdo, correcta |
| «Lo que este tema no da» y párrafo de oficio | tema | Coherentes con lo cambiado; la autoría del círculo (Newton, 1666) se deja fuera con razón |
| «Trazabilidad», cuatro filas nuevas | volcados citados | URL, fechas de modificación y de lectura coinciden con las cabeceras de los volcados |

## Correcciones aplicadas (4)

1. Recuento: «Dos definiciones» → «Tres definiciones de las propias pautas (relación de contraste,
   luminancia relativa y texto grande) y las salvedades del criterio 1.4.3:».
2. Ascendentes: «Los trazos de la minúscula que suben» → «Las partes de la letra que suben» (fiel a la fuente).
3. Lecturabilidad: la enumeración de lo que la condiciona, marcada «(oficio)».
4. Normativa: añadidos los puntos 45 y 46 del Contrato-programa.

Lentes tras corregir: `indice.py` 10.063 palabras, 41 epígrafes; `refutar_prosa.py` 0 hallazgos.
Pendiente ajeno a este tema: `fuentes/canal-sur/grafista/README.md` no registra aún los volcados
`sessions-college-color-wheel.txt` ni `google-fonts-knowledge-glosario.txt` (no se ha tocado).
