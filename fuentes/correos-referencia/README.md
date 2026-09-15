# El «documento de referencia» de Correos

**Qué es.** El Anexo III de la convocatoria —el programa— no describe contenidos:
enumera doce títulos y remite, para el contenido, a un documento que publica la
propia Correos. **Ese documento es la fuente de la que salieron las preguntas del
examen de 2023**, y sin él este temario no tendría nada detrás.

**Son 1.334 páginas en doce PDF**, uno por tema, publicados entre noviembre de 2022
y febrero de 2023.

## Y la nota con que Correos lo publicó

**Junto al enlace de descarga, Correos publicó una nota informativa que dice qué es este documento y
qué no es**, y **esa nota no está dentro del documento**: por eso no aparece en el volcado de sus mil
trescientas treinta y cuatro páginas. Está volcada aparte, en
`nota-documento-referencia.txt`, y dice dos cosas que gobiernan lo que este temario puede
afirmar: que **«en ningún caso reviste carácter de manual o temario oficial de las pruebas»**, que
**«está actualizado a fecha 31 de octubre de 2022»** y que **su carácter es «meramente enunciativo y
no limitativo»** de las fuentes que el aspirante puede usar.

**El portal de Correos ya no la sirve**, igual que ya no sirve los PDF, así que **se contrastó el
2026-09-15 contra dos reproducciones independientes de diciembre de 2022 que coinciden palabra por
palabra**. La procedencia entera está escrita en la ficha de fuentes de la convocatoria.

## Por qué aquí sólo está el volcado

**Los doce PDF pesan 547 megabytes (**MB**).** El mayor que este repositorio versiona
son 15 MB, y el historial entero ronda los 612 MB: meterlos lo doblaría. Así que **se versiona
el volcado `.txt`, que es lo que se lee, lo que se cita y contra lo que corren las
lentes**, y los PDF se vuelven a bajar con la tabla de abajo. Es la misma regla
que el repositorio ya aplica a los ochenta y siete cuadernillos de RTVE.

**Los cuadernillos del examen sí van versionados**, en
`convocatoria/correos/examenes/`: pesan poco y hay que poder contrastar cada
enunciado contra su página.

## Cómo se vuelven a bajar

Todos cuelgan del mismo sitio, con el prefijo
`https://www.solidaridadpostal.com/docs/noticias/`:

| Tema | Fichero en origen | Páginas |
|---:|---|---:|
| 1 | `627_Tema_1._Pag_1-80-Ref.pdf` | 80 |
| 2 | `626_20230221-Tema_2._Pag_81-161.pdf` | 81 |
| 3 | `628_Tema_3._Pag_163-294.pdf` | 132 |
| 4 | `629_TEMA_4_Productos_pag_295_a_390.pdf` | 96 |
| 5 | `630_TEMA_5_pag_391_a_438_movilR.pdf` | 48 |
| 6 | `631_TEMA_6_pag_439-471_movilR.pdf` | 33 |
| 7 | `632_TEMA_7_pag_485-790_NavegadorOR.pdf` | 306 |
| 8 | `633_Tema_8_pag_779-878_0r.pdf` | 100 |
| 9 | `634_tema_9._Pag_891-1098_O.pdf` | 208 |
| 10 | `635_tema_10._Pag_1087-1150-O.pdf` | 64 |
| 11 | `636_tema_11._Pag_1151-1194_O.pdf` | 44 |
| 12 | `637_tema_12._Pag_1195-1348_O.pdf` | 142 |

```sh
curl -sSL -A "Mozilla/5.0" -o fuentes/correos-referencia/tema-01.pdf \
  "https://www.solidaridadpostal.com/docs/noticias/627_Tema_1._Pag_1-80-Ref.pdf"
```

**Y una advertencia de procedencia que hay que decir**: estos doce ficheros se han
bajado de **la sección sindical que los replica**, no del portal de Correos, porque
**el portal ya no los sirve**: la convocatoria de 2023 está cerrada y su material
retirado. **Los nombres de fichero y la paginación son los del original** —«Pag
1-80», «Pag 1195-1348»— y encajan sin hueco de un tema al siguiente, que es lo que
permite afirmar que la serie está completa. Aun así, **no son fuente primaria
servida por el organismo**, y eso queda escrito.

## Cómo se ha volcado

Con `herramientas/correos_dump.py`, página a página:

- **225 páginas de las 1.334 traen capa de texto** y se toman tal cual.
- **Las otras 1.109 van como dibujo vectorial** —sus letras son trazos, no
  caracteres— y se han **reconocido ópticamente a 300 puntos por pulgada** con
  `tesseract -l spa --psm 3`.

**Cada página va rotulada con su número y con el origen del texto**, `texto` u
`ocr`. No es decoración: un tema que cite este documento tiene que poder decir de
qué página sale cada cita, y quien repase un pasaje reconocido necesita saber que
lo es antes de fiarse.

**Por qué 300 y no más**: se midieron 350, 300 y 250 puntos por pulgada sobre la
misma página. **Entre 350 y 300 no cambia ni un carácter** y el reconocimiento
tarda la mitad; 250 empieza a perder. 300 es donde deja de valer la pena subir.

**Por qué `--psm 3` y no `--psm 6`**: el documento alterna páginas a una columna
con páginas a dos. **La segmentación de bloque uniforme pega los renglones de las
dos columnas en una sola línea** y destroza las frases; la automática detecta las
columnas.

## Lo que este volcado NO es

**No es el documento.** El reconocimiento se equivoca, y se equivoca más en las
tablas, en los rótulos sobre fondo de color y en las cifras sueltas. Dos defectos
ya vistos en la primera lectura: **la «o» minúscula suelta sale como «O»
mayúscula**, y una portada devuelve **«Blanq,ueo»** por «Blanqueo».

**Y hay un defecto sistemático que obliga a desconfiar de TODAS las cifras: el
nueve.** La tipografía de este documento dibuja el **9** con un cuello abierto que el
reconocedor confunde con un **4**, y a veces lo desdobla en dos dígitos. Cuatro casos
del tema 1, **comprobados a la vista uno a uno sobre su página**:

| El volcado dice | El documento dice | Página del tema 1 |
|---|---|---:|
| Directiva **47**/67/CE, de 15 de diciembre de **1447** | Directiva **97**/67/CE, de **1997** | 8 |
| Real Decreto 1829/**1499** | Real Decreto 1829/**1999** | 12 |
| Ley **94**/2017, de Contratos del Sector Público | Ley **9**/2017 | 14 |
| Ley **49**/2017, la misma norma dos páginas después | Ley **9**/2017 | 15 |

**No son tropiezos aislados: es el nueve de esta fuente.** El documento compone las
cifras en una tipografía geométrica cuyo **9 tiene el cuello recto**, y el reconocedor
lo toma por un **4**; a veces, además, lo desdobla en dos dígitos.

**Y lo peor es que producen números verosímiles**: «Ley 49/2017» parece una ley, «1499»
y «1447» parecen años. Un temario que copie del volcado sin mirar la página **enseña
fechas y números de norma inventados por un reconocedor**, y no hay lente que lo
detecte, porque la cifra falsa está en la fuente que la lente usa para comprobar.

**Regla, y es la misma que el proyecto aplicó a las plantillas ilegibles y a la
página 59 del consenso de sensibilidad química múltiple**: todo dato que un tema
tome de una página marcada `ocr` **se comprueba a la vista sobre la página original
antes de escribirlo**. **Con las cifras, sin excepción.**
