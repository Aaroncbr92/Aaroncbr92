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
| `herramientas/indice.py` | Genera la **portada** y el **índice** de cada tema, y comprueba que las rutas que citan existen. Se vuelve a pasar cuantas veces haga falta. |
| `herramientas/libro.py` | Arma el **bloque general en un volumen imprimible**: ficha, cuerpo, esquema y preguntas reales de cada tema, y las respuestas al final. |
| `herramientas/pdf.py` | Convierte ese volumen en PDF con el Chromium del entorno. |
| `esquemas/` | Un esqueleto de repaso por tema. Estilo telegrama, con el artículo delante de cada línea. |
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

# volumen imprimible del bloque general
python3 herramientas/libro.py && python3 herramientas/pdf.py

# bancos de preguntas
python3 herramientas/banco.py                           # bloque común
python3 herramientas/banco_especifico.py                # Producción (Asistencia)
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
