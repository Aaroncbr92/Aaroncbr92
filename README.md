# Temarios de oposición

Producción de temario verificado contra fuente oficial, siguiendo el método de
`metodo/MANUAL.md`. La regla de la que sale todo lo demás:

> Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de
> afirmarlo, y lo que no se puede confirmar se quita.

## Tres oposiciones, un método

| Carpeta | Oposición | Sección de la web | Estado |
|---|---|---|---|
| `rtve/` | Personal laboral fijo de la Corporación RTVE | `opotemarios.es/RTVE` | **Terminada**: 25 volúmenes en PDF, Word y HTML |
| `correos/` | Personal laboral de Correos | `opotemarios.es/correos` | **Empezando** |
| `age/` | Cuerpo General Auxiliar de la Administración del Estado (C2) | `opotemarios.es/age` | **Empezando** |

Cada una vive entera en su carpeta: su convocatoria, sus temas, sus esquemas,
sus fuentes, su banco de preguntas y su catálogo de volúmenes. Lo que comparten
es lo de arriba: el método y las herramientas.

| Compartido | De cada oposición |
|---|---|
| `metodo/` · el manual y las cláusulas de encargo | `convocatoria/` · programa oficial, bases y exámenes |
| `herramientas/` · lectores del BOE, refutadores, armadores de volumen | `temas/` `esquemas/` `fuentes/` `banco/` `informes/` |
| `marca/` · el logotipo que llevan los volúmenes | `bloques.py` · el catálogo de volúmenes y la fecha de corte |
| | `portadas.tsv` · la ficha de cabecera de cada tema |
| | `ESTADO.md` `PENDIENTES.md` `PLAN.md` · dónde va cada una |

**El corte está donde está a propósito.** Lo común es *cómo* se comprueba un
dato y *cómo* se arma un volumen, que no depende de qué se estudie. Lo propio es
*qué* se estudia, y ahí no hay nada reaprovechable entre un temario de RTVE y
uno de Correos. Una herramienta que supiera de las tres tendría dentro tres
catálogos y habría que leerlos todos para tocar uno.

## Sobre qué oposición se trabaja

Ninguna herramienta tiene oposición por defecto. Se dice de una de estas dos
maneras:

```
cd rtve && python3 ../herramientas/libro.py general     # estando dentro
OPO=rtve python3 herramientas/libro.py general          # nombrándola
```

Y si no se dice, la herramienta se para y enseña las que hay. Es a propósito:
equivocarse de oposición no da error, escribe el banco de preguntas de una
encima del de otra y el fallo aparece semanas después, dentro de un volumen.
Una carpeta es una oposición cuando lleva un `OPOSICION.md`; lo demás lo resuelve
`herramientas/raiz.py`.

## Las herramientas

| Ruta | Qué es |
|---|---|
| `metodo/MANUAL.md` | El método. Se lee entero antes de tocar un tema. |
| `metodo/ENCARGOS.md` | Cláusulas de encargo y catálogo de errores, para pegar en cada fase. |
| `herramientas/raiz.py` | Sobre qué oposición se trabaja. De aquí saca cada herramienta dónde están los datos. |
| `herramientas/boe.py` | Lector de legislación consolidada del BOE. |
| `herramientas/doue.py` | Lector de normas de la Unión Europea publicadas por el BOE, con sus correcciones de errores. El texto no está consolidado, y lo dice. |
| `herramientas/refutar_*.py` | Las cinco lentes de refutación: exactitud, modo verbal y salvedades, prosa, citas literales y contraste contra documento sin articulado. |
| `herramientas/despintar.py` | Quita la negrita a lo que no es cita literal de ninguna fuente, o la rebaja a cursiva con `--cursiva`. La negrita es una promesa de literalidad; ésta retira las que el texto no cumple. |
| `herramientas/indice.py` | Genera la **portada** y el **índice** de cada tema, y comprueba que las rutas que citan existen. Se vuelve a pasar cuantas veces haga falta. |
| `herramientas/boe_buscar.py` | Busca una norma por su título en el BOE. Manda las casillas de sección, sin las cuales el buscador contesta «no se han encontrado documentos» y una búsqueda con respuesta se anota como camino cerrado. |
| `herramientas/libro.py` | Arma **cada bloque en un volumen imprimible**: ficha, cuerpo, esquema y preguntas reales de cada tema, y las respuestas al final, con los avisos de plantilla y de enunciado. Los bloques los pone la oposición, en su `bloques.py`. |
| `herramientas/pdf.py` | Convierte ese volumen en PDF con el Chromium del entorno, con índice paginado. |
| `herramientas/word.py` | El mismo volumen en `.docx`, con estilos de Word. |
| `herramientas/extraer_examen.py` | Reconstruye el texto de un cuadernillo desde su PDF. Prueba **dos modos** —línea a línea y agrupando por altura, para los que maquetan las opciones en tres columnas— y se queda con el que deja menos letras huérfanas. Sin él, 21 cuadernillos daban opciones vacías y uno se contaminaba con 252 fragmentos duplicados. |
| `herramientas/banco.py` | Arma el banco de preguntas del **bloque común**, clasificando por materia. |
| `herramientas/banco_especifico.py` | El del **bloque específico**, aplicando un reparto escrito a mano y avisando de lo que falta por repartir. |

## La herramienta del BOE

Resuelve las tres trampas del apartado 2 del manual: la cadena de redacciones,
las reformas cruzadas y los identificadores irregulares.

```
herramientas/boe.py indice   BOE-A-2006-9958            # índice real de bloques
herramientas/boe.py buscar   BOE-A-2006-9958 "artículo 43"
herramientas/boe.py precepto BOE-A-2006-9958 a11        # cadena + redacción vigente
herramientas/doue.py DOUE-L-2016-80807 fuentes/         # un reglamento europeo
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

## Dar de alta otra oposición

1. Una carpeta con su `OPOSICION.md` —la ficha, y la marca por la que las
   herramientas la reconocen—.
2. Dentro, `convocatoria/` con las bases y el **programa oficial literal**, que
   es lo primero que hay que tener: sin él no se sabe ni cuántos temas son.
3. `temas/`, `esquemas/`, `fuentes/`, `banco/` e `informes/`, que se van
   llenando.
4. `portadas.tsv` con la ficha de cada tema, y `bloques.py` con su catálogo de
   volúmenes, **cuando haya temas que armar**. Antes no hace falta: sin
   `bloques.py` las demás herramientas funcionan y sólo se paran las tres que
   arman volúmenes, diciendo qué falta.

No hay que tocar ninguna herramienta.
