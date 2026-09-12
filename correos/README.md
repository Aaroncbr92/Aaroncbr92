# Correos

Ingreso de personal laboral fijo, Grupo Profesional IV (Personal Operativo). La
sección de la web que sale de aquí es **`www.opotemarios.es/correos`**.

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
| `convocatoria/PROGRAMA.md` | Los 12 temas, transcritos literales del ANEXO III |
| `convocatoria/EXAMEN.md` | La prueba, los méritos y los dos listones de aprobado |
| `convocatoria/FUENTES.md` | Qué tiene norma detrás y qué no. **Se lee antes de escribir nada** |
| `convocatoria/bases/` | El Primer Desarrollo de las Bases: PDF oficial y volcado de texto |
| `temas/` `esquemas/` `fuentes/` `banco/` `informes/` | Lo de siempre |

## De un vistazo

- **12 temas**, y **nueve no tienen fuente todavía**: el documento de referencia
  de Correos no se ha podido descargar desde aquí.
- **La convocatoria de 2026 no está publicada.** Lo que hay es la anterior.
- **90 preguntas de temario y 10 psicotécnicas**, sin penalizar el error, y
  **40 de los 100 puntos son méritos**, no temario.
- **El listón no es el mismo**: 55 aciertos en Reparto y Clasificación, 60 en
  Atención al Cliente.

## Cómo se trabaja

Las herramientas son las del repositorio, compartidas con las demás oposiciones
y explicadas en el `README.md` de la raíz. Resuelven las rutas contra esta
carpeta, así que basta con estar dentro de ella:

```
cd correos
python3 ../herramientas/boe.py precepto BOE-A-2015-10565 a13
python3 ../herramientas/indice.py temas/...
```

O nombrarla desde la raíz del repositorio: `OPO=correos python3 herramientas/...`.

Todavía **no hay `bloques.py`**, que es el catálogo de volúmenes. Hasta que haya
temas que armar no hace falta: sin él, `libro.py`, `pdf.py` y `word.py` se paran
diciendo qué falta, y las demás herramientas funcionan.
