# III Convenio Colectivo de la Corporación RTVE

**Un convenio colectivo no es legislación consolidada.** El BOE no publica texto
refundido de los convenios, así que **no existe versión consolidada oficial** y
`herramientas/boe.py` —que trabaja contra la API de legislación consolidada— no sirve
aquí. La redacción en vigor hay que reconstruirla superponiendo los documentos
publicados.

## Los tres documentos

| Fichero | Identificador | Publicación | Qué es |
|---|---|---|---|
| `BOE-A-2020-16744.txt` | BOE-A-2020-16744 | BOE 332, de **22/12/2020** | Resolución de 15/12/2020 de la Dirección General de Trabajo, con el **texto del convenio** y los **anexos 1 a 6** |
| `BOE-A-2021-1334.txt` | BOE-A-2021-1334 | **29/01/2021** | Corrección de errores: añade el **anexo 7** |
| `BOE-A-2022-20256.txt` | BOE-A-2022-20256 | **05/12/2022** | Acuerdo de modificación parcial suscrito el 10/11/2022: reescribe los artículos **12, 13, 16, 17, 18, 21, 27, 30, 63 y 102**, sustituye la **DT octava**, añade la **DT décima** y el **anexo 8** |

Los tres son anteriores a la fecha de corte de las bases (**21/12/2022**), de modo que el
texto reconstruido es el examinable.

## `CONVENIO.md` — el articulado reconstruido

Lo genera `herramientas/convenio_dump.py`. Toma de 2022 los diez artículos que ese
acuerdo reescribió y de 2020 el resto, y **anota en cada artículo de qué documento viene
su redacción**. Tiene la forma que esperan las lentes de refutación
(`## [id] Artículo N`), de modo que el tema se puede contrastar con ellas.

Se regenera con:

```
python3 herramientas/convenio_dump.py > fuentes/convenio/CONVENIO.md
```

**Solo contiene el articulado del convenio, hasta el anexo 1.** El anexo 4 vuelve a
numerar desde el artículo 1, y mezclarlo haría contrastar las negritas del tema contra el
artículo equivocado, que es peor que no contrastar nada.

## Dos cosas que cuestan una pregunta si se pasan por alto

1. **El acuerdo de 2022 intercambia los artículos 16 y 17.** A la fecha de corte,
   **art. 16 = reingreso de excedentes** y **art. 17 = promoción y cambio de ocupación
   tipo**; en el texto de 2020 era al revés.
2. **El artículo 63.5 cambió de porcentajes.** En 2020, prácticas al **70 % / 80 %**;
   desde 2022, **contrato formativo en alternancia al 60 % / 75 %** y **contrato para la
   práctica profesional al 70 %**. Los porcentajes antiguos no desaparecen: se trasladan
   a la **disposición transitoria décima** para quienes ya estuvieran contratados.

## Y una que no está en el texto

**Partes del convenio solo existen como imagen en el BOE**: la tabla de niveles económicos
del artículo 65 y los **anexos 1, 2 y 3 completos**. No aparecen en el HTML y, por tanto,
tampoco en estas transcripciones, y **su ausencia no da ningún aviso**: el texto continúa
con normalidad después del rótulo del anexo. Están descargadas y en parte transcritas en
`imagenes/`.
