# Temarios de oposición · RTVE

Producción de temario verificado contra fuente oficial, siguiendo el método de
`metodo/MANUAL.md`. La regla de la que sale todo lo demás:

> Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de
> afirmarlo, y lo que no se puede confirmar se quita.

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `metodo/MANUAL.md` | El método. Se lee entero antes de tocar un tema. |
| `metodo/ENCARGOS.md` | Cláusulas de encargo y catálogo de errores, para pegar en cada fase. |
| `herramientas/boe.py` | Lector de legislación consolidada del BOE. |
| `herramientas/doue.py` | Lector de normas de la Unión Europea publicadas por el BOE, con sus correcciones de errores. El texto no está consolidado, y lo dice. |
| `herramientas/refutar_*.py` | Las cuatro lentes de refutación: exactitud, modo verbal y salvedades, prosa, y contraste contra documento sin articulado. |
| `herramientas/despintar.py` | Quita la negrita a lo que no es cita literal de ninguna fuente, o la rebaja a cursiva con `--cursiva`. La negrita es una promesa de literalidad; ésta retira las que el texto no cumple. |
| `herramientas/indice.py` | Genera la **portada** y el **índice** de cada tema, y comprueba que las rutas que citan existen. Se vuelve a pasar cuantas veces haga falta. |
| `herramientas/boe_buscar.py` | Busca una norma por su título en el BOE. Manda las casillas de sección, sin las cuales el buscador contesta «no se han encontrado documentos» y una búsqueda con respuesta se anota como camino cerrado. |
| `herramientas/libro.py` | Arma **cada bloque en un volumen imprimible**: ficha, cuerpo, esquema y preguntas reales de cada tema, y las respuestas al final, con los avisos de plantilla y de enunciado. Los bloques están en `BLOQUES`, uno por entrada. |
| `herramientas/pdf.py` | Convierte ese volumen en PDF con el Chromium del entorno, con índice paginado. |
| `herramientas/word.py` | El mismo volumen en `.docx`, con estilos de Word. |
| `esquemas/` | Un esqueleto de repaso por tema. Estilo telegrama, con el artículo delante de cada línea. |
| `herramientas/extraer_examen.py` | Reconstruye el texto de un cuadernillo desde su PDF. Prueba **dos modos** —línea a línea y agrupando por altura, para los que maquetan las opciones en tres columnas— y se queda con el que deja menos letras huérfanas. Sin él, 21 cuadernillos daban opciones vacías y uno se contaminaba con 252 fragmentos duplicados. |
| `herramientas/banco.py` | Arma el banco de preguntas del **bloque común**, clasificando por materia. |
| `herramientas/banco_especifico.py` | El del **bloque específico**, aplicando un reparto escrito a mano y avisando de lo que falta por repartir. |
| `banco/` | Preguntas reales de convocatorias anteriores con su respuesta oficial. |
| `ESTADO.md` | Qué hay hecho, qué falta, dónde vive cada cosa. |
| `PENDIENTES.md` | Cuaderno de hallazgos, se anote o no se corrija en el momento. |
| `convocatoria/` | Programa oficial literal y exámenes de convocatorias anteriores. |
| `temas/` | Un fichero por tema. |
| `informes/` | Un fichero por agente y fase. Nada se queda solo en el chat. |

## La herramienta del BOE

Resuelve las tres trampas del apartado 2 del manual: la cadena de redacciones,
las reformas cruzadas y los identificadores irregulares.

```
herramientas/boe.py indice   BOE-A-2006-9958            # índice real de bloques
herramientas/boe.py buscar   BOE-A-2006-9958 "artículo 43"
herramientas/boe.py precepto BOE-A-2006-9958 a11        # cadena + redacción vigente
herramientas/doue.py DOUE-L-2016-80807 fuentes/          # un reglamento europeo

# portada e índice de todos los temas, regenerables
python3 herramientas/indice.py                          # todos
python3 herramientas/indice.py temas/general/07-*.md    # uno

# volúmenes imprimibles, uno por bloque
python3 herramientas/libro.py general     && python3 herramientas/pdf.py libro-general.html
python3 herramientas/libro.py informacion && python3 herramientas/pdf.py libro-informacion.html
python3 herramientas/word.py informacion                # el mismo, en .docx

# bancos de preguntas
python3 herramientas/banco.py                           # bloque común
python3 herramientas/banco_especifico.py informacion    # uno por ocupación tipo
```

Lo que hace por ti en cada precepto:

- enseña **todas** las redacciones con su fecha de vigencia y de publicación, y
  elige la última vigencia ya cumplida;
- avisa de **posible reforma cruzada** cuando la redacción con la vigencia más
  alta no es también la publicada más tarde;
- saca aparte las **notas del BOE** que hablan de inconstitucionalidad, nulidad,
  falta de convalidación o derogación;
- no deduce identificadores: los resuelve contra el índice publicado. En la Ley
  17/2006, el artículo 43 es el bloque `a4-2`. Por analogía no se acierta.

## Los volúmenes

**Catorce, uno por bloque**, cada uno en PDF, Word y HTML. El general sirve a las
trece ocupaciones; los trece específicos cierran con **el mismo tema de
prevención de riesgos laborales**, que es un solo fichero.

| Volumen | Ocupación tipo | Temas | Preguntas | Páginas |
|---|---|---:|---:|---:|
| `libro-general` | Las trece | 8 | 503 | 259 |
| `libro-produccion-asistencia` | Producción (Asistencia) | 18 | 170 | 280 |
| `libro-produccion` | Producción | 17 | 113 | 232 |
| `libro-realizacion` | Realización (Asistencia) | 21 | 253 | 303 |
| `libro-realizacion-tv` | **Realización Televisión** | **23** | **276** | **363** |
| `libro-documentacion` | Documentación | 7 | 129 | 154 |
| `libro-informacion` | Información y Contenidos | 11 | 225 | 214 |
| `libro-gestion-administrativa` | Gestión Administrativa | 13 | 122 | 180 |
| `libro-gestion` | Gestión | 31 | 128 | 321 |
| `libro-montaje-equipos` | Montaje de Equipos Audiovisuales | 11 | 122 | 165 |
| `libro-edicion-montaje` | Edición, Montaje y Procesos Audiovisuales | 11 | 133 | 193 |
| `libro-informacion-grafica` | Información Gráfica y Captación de Imagen y Sonido | 12 | 141 | 218 |
| `libro-sonido` | **Sonido** | 18 | 133 | 206 |
| `libro-tese` | **Técnica de Equipos y Sistemas Electrónicos** | 18 | 161 | 230 |
| `libro-tecnica-informatica` | **Técnica Informática** | 24 | 137 | 255 |

**Realización Televisión es el volumen más grande del proyecto**: 363 páginas,
veintidós temas propios más el de prevención y **229 preguntas del bloque
específico**, de dos llamamientos con sus dos plantillas completas.

**Y Técnica de Equipos y Sistemas Electrónicos es el más gráfico**: **treinta de
sus 114 preguntas dependen de una imagen**, la proporción más alta del proyecto.
El temario **no describe lo que no ha visto**: declara cada una y aporta la regla
de su familia.

**Y Técnica Informática es el contrario exacto**: **ninguna de sus 90 preguntas
del específico depende de una imagen**, y es **el único volumen del proyecto que
contesta el examen entero sin remitir ni una vez a la plantilla**. Todo lo que se
pregunta está escrito, y por tanto todo se puede comprobar.

**Diez respuestas oficiales de 2024 están mal, y van marcadas una a una** con el
precepto, el modelo de cuentas o la ficha de fabricante que las desmiente. El
temario enseña la norma, no la plantilla, **y dice dónde está la costura**.
