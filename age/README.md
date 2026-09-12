# Auxiliar de la AGE

Cuerpo General Auxiliar de la Administración del Estado, subgrupo C2, código
1146, ingreso libre. La sección de la web que sale de aquí es
**`www.opotemarios.es/age`**.

El método y las herramientas son los del repositorio. Lo de esta carpeta son
**sus datos**.

> Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de
> afirmarlo, y lo que no se puede confirmar se quita.

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `OPOSICION.md` | La ficha de la oposición, y la marca de raíz de trabajo |
| `ESTADO.md` | Qué hay hecho, qué falta, dónde vive cada cosa |
| `PENDIENTES.md` | Cuaderno de hallazgos |
| `PLAN.md` | El orden de trabajo y por qué es ése |
| `convocatoria/PROGRAMA.md` | Los 28 puntos del programa, transcritos literales del ANEXO I |
| `convocatoria/EXAMEN.md` | Plazas, estructura del ejercicio y lo que eso decide sobre el temario |
| `convocatoria/FUENTES.md` | La norma detrás de cada punto, con su identificador resuelto contra el BOE |
| `convocatoria/bases/` | La convocatoria entera: PDF oficial y volcado de texto |
| `temas/` `esquemas/` `fuentes/` `banco/` `informes/` | Lo de siempre |

## De un vistazo

- **28 puntos**, 16 del bloque I y 12 del bloque II.
- **1.700 plazas**, 156 reservadas a personas con discapacidad.
- **El bloque II vale más del doble por tema** y seis de sus doce puntos son
  Windows 11 y Microsoft 365. Ver `convocatoria/EXAMEN.md`.
- **Sin fecha de corte en las bases.** Se escribe con la redacción vigente el
  día en que se escribe, y cada tema declara cuándo se leyó.

## Cómo se trabaja

Las herramientas son las del repositorio, compartidas con las demás oposiciones
y explicadas en el `README.md` de la raíz. Resuelven las rutas contra esta
carpeta, así que basta con estar dentro de ella:

```
cd age
python3 ../herramientas/boe.py precepto BOE-A-2015-10565 a13
python3 ../herramientas/indice.py temas/...
```

O nombrarla desde la raíz del repositorio: `OPO=age python3 herramientas/...`.

Todavía **no hay `bloques.py`**, que es el catálogo de volúmenes. Hasta que haya
temas que armar no hace falta: sin él, `libro.py`, `pdf.py` y `word.py` se paran
diciendo qué falta, y las demás herramientas funcionan.
