# Puesto 08 · Tema 2 · Fase 5 bis · Revisión de lo rematado

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/02-lenguaje-visual.md`.
Alcance: sólo los pasajes listados en `08-T02-remate.md` (el remate amplió). Resultado: **4
correcciones**, todas comprobadas en la fuente; el resto, confirmado.

## Fuentes releídas (todas el 24-09-2026)

- Libro de estilo de Canal Sur TV y Canal 2 Andalucía, 1.ª ed., 2004 (volcado `.txt`): índice
  (9, 9.2), 3.17.1.2-3.17.1.3 (p. 60), 5.3.2 (p. 81), cierre de 6.3 (p. 92), 8.3.2 (p. 117),
  9.2.12.3-9.2.12.4 (p. 130).
- EBU R 95 v1.1 (junio de 2017), texto completo (introducción, recomendación, notas 1-6, figuras 1-6).
- Recomendación UIT-R BT.709-6 (06/2015), versión española (`fuentes/normas-tecnicas/`), apartado 2.
- Sony, *PXW-FS5/FS5K Operating Guide* 4-581-849-11(1), p. 132 (MARKER).
- ITE, *Multimedia. Aplicaciones didácticas*, «Lenguaje de imagen: El movimiento»
  (www.ite.educacion.es/formacion/materiales/84/cd/curso/lenguaje4.htm), descargada de nuevo.

## Correcciones aplicadas

| Nº | Error | Pasaje | Comprobación y cambio |
|---|---|---|---|
| F1 | 8 (ubicación mal dicha) | Viñeta de sucesos, «Imagen y realidad», «Documentos que el tema cita» | El Libro no tiene un «capítulo sobre malos tratos»: 9.2 «Malos tratos» es un apartado del capítulo 9 «Asuntos comprometidos» (índice, p. 19 del volcado). Se dice «apartado 9.2» en los tres sitios |
| F2 | 9 (literal no casa con la fuente guardada) | «La relación de aspecto y las zonas seguras» | La versión española de BT.709-6, 2.2 y 2.5, dice «**1920**» y «**1:1 (píxeles cuadrados)**»; el tema citaba «1 920» y «1:1 (square pixels)» en inglés. Se pasan al literal español y se precisa «líneas activas por imagen» (2.4) |
| F3 | Coherencia | «Documentos que el tema cita» | Título de BT.709-6 en su versión española, la que se cita: *Valores de los parámetros de la norma de TVAD para la producción y el intercambio internacional de programas* |
| F4 | 5 | Siglas de entrada | TVAD (del título) se presenta: televisión de alta definición |

## Confirmado sin cambios

- «La variedad» (3.17.1.2, p. 60), «La mirada» con «No obstante, es necesario alentar la
  cercanía del personaje.», «Sin escorzo» completa (3.17.1.3, p. 60): literales.
- Postura del directo (8.3.2, p. 117): literal; la p. 117 empieza antes de 8.3.2.
- 9.2.12.3 (p. 130): «El sistema es poco recomendable…» y «También es arriesgado…», literales.
- Linealidad: párrafo sin número en p. 92, tras 6.3.4 y antes de 6.4. Correcto.
- «sobre todo las panorámicas» y «edición convencional» (5.3.2): literales.
- EBU R 95: recomendación (tres viñetas), nota 5 (3,5 % y 5 %), formatos de las figuras 1-6
  (576i, 720p, 1080i/1080psf, 1080p, 2160p, 4320p), fecha y versión: correctos. La resta 93 % / 90 %
  va declarada como resta.
- FS5, p. 132: ASPECT, SAFETY ZONE 80 %/90 %, CENTER; marcas no grabadas.
- ITE: definiciones de panorámica descriptiva, de acompañamiento y de relación, barrido y
  «El travelling también puede ser descriptivo, de acompañamiento o de relación.», literales; cita
  de los *Cuadernos* de la Generalitat Valenciana en la página. «De seguimiento», declarado oficio.
- Antecedentes: «esa fuente» y «La misma fuente» (ITE), «el epígrafe anterior» (zonas seguras,
  inmediatamente antes de las guías del visor), «Las tres normas casan», «Por eso el periodista…»
  (sigue a la cercanía): todos con su antecedente delante.
- Siglas nuevas UIT-R, ND, LCD, *dolly*, *slider*: presentadas; CSTV, TC y C-1 ya no se usan.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 51 epígrafes, 11.351 palabras.

## Otros ficheros tocados

Ninguno salvo el tema y este informe. (Los cambios sin commit en los temas 01, 05, 09 y 15 no son míos.)
