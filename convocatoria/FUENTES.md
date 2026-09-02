# Fuentes del programa: identificadores y acceso

Localizado y comprobado desde esta sesión el 2026-08-29. Los identificadores no
se deducen: se han resuelto contra el BOE, y el acceso se ha probado uno a uno.

## Temario general

| # | Fuente | Identificador | Acceso |
|---|---|---|---|
| 1 | Constitución Española | `BOE-A-1978-31229` | consolidado, API |
| 2 | Ley 17/2006, radio y televisión de titularidad estatal | `BOE-A-2006-9958` | consolidado, API |
| 3 | Ley 5/2017 (modifica la 17/2006) | `BOE-A-2017-11091` | consolidado, API |
| 4 | Ley 8/2009, financiación de la CRTVE | `BOE-A-2009-13988` | consolidado, API |
| 5 | III Convenio Colectivo CRTVE | `BOE-A-2020-16744` | PDF, 117 págs. |
| 5 | Corrección de errores del III Convenio | `BOE-A-2021-1334` | PDF |
| 5 | Acuerdo de modificación del Convenio (2022) | `BOE-A-2022-20256` | PDF |
| 6 | II Plan de Igualdad RTVE (2022-2026) | PDF en rtve.es | descargado y transcrito en `fuentes/igualdad/` |
| 6 | Guía de Igualdad RTVE 2020 | PDF en rtve.es | descargado y transcrito en `fuentes/igualdad/` |
| 7 | Ley 13/2022, General de Comunicación Audiovisual | `BOE-A-2022-11311` | consolidado, API |
| 8 | Ley 31/1995, de Prevención de Riesgos Laborales | `BOE-A-1995-24292` | consolidado, API |

## Temario específico

| Dónde | Fuente | Identificador | Acceso |
|---|---|---|---|
| Producción 2 | TRLPI, RDLeg. 1/1996 | `BOE-A-1996-8930` | consolidado, API |
| Producción 17 | LOPDGDD 3/2018 | `BOE-A-2018-16673` | consolidado, API |
| Información 4 | Código de autorregulación de derechos del menor de RTVE | PDF en rtve.es | descarga bien |
| Información 5 | RDL 4/2018 | `BOE-A-2018-8577` | consolidado, API |
| Información 6 | Manual de estilo de RTVE | manualdeestilo.rtve.es | **descargado** (ocho capítulos, ~48.000 palabras) |
| Información 7 | Directiva UE 2018/1808 | DOUE L 303, vía BOE | descarga bien |
| Información 8 | Resolución del PE de 25/11/2020 | CELEX 52020IP0320 | descarga bien |
| Información 9 | Informe mundial UNESCO 2021/2022 | unesdoc.unesco.org | **403 de verdad**; se usa el micrositio oficial del informe |
| Información 10 | Carta ética mundial para periodistas (FIP) | PDF en ifj.org | descarga bien |

**Esta tabla dijo durante días que las dos daban 403 «del servidor, no del
proxy». Sólo una lo daba, y la conclusión era la equivocada.**

- **El Manual de estilo se descarga bien**, y está entero en
  `fuentes/informacion/`. Su 403 **no venía del servidor**: el programa da la
  dirección en `http://` y la política de salida de este entorno sólo deja pasar
  `https`. Cambiar el esquema bastó. Estuvo dado por imposible desde la primera
  revisión de fuentes.
- **El informe de la UNESCO sí está bloqueado de verdad**: `unesdoc.unesco.org`
  responde con un desafío de JavaScript de Cloudflare, que un cliente sin
  navegador no resuelve. Se probaron cinco caminos y ninguno abre. **El tema 9 se
  escribe contra el micrositio oficial del propio informe**, que publica sus
  capítulos en página web, y **declara las dos preguntas que ese micrositio no
  sostiene**.

De ahí sale la regla que dejó este bloque: **un 403 no dice quién bloquea.**
Antes de anotar una fuente como cerrada hay que separar el bloqueo del servidor
del de la red por la que se sale.

## El programa cita una foto de las normas que ya no es la vigente

Comprobado precepto a precepto con `herramientas/boe.py`. No es una objeción
teórica: cambia la respuesta.

- **Constitución.** El programa cita la actualización de 27/09/2011. Desde
  entonces se ha reformado dos veces: el **artículo 49** (17/02/2024) y el
  **artículo 69** (20/05/2026, `BOE-A-2026-10881`), donde el apartado 3 pasa de
  «cada isla o agrupación de ellas, con Cabildo o Consejo Insular» a «cada isla
  con Cabildo o Consejo Insular», e Ibiza y Formentera dejan de ser una sola
  circunscripción.
- **Ley 17/2006.** El programa cita la actualización de 08/07/2022. Después
  llegó el **Real Decreto-ley 5/2024**, convalidado por Resolución de 30 de
  octubre de 2024, que reescribió entre otros el artículo 11: el Consejo de
  Administración pasa a elegirse **once por el Congreso y cuatro por el Senado**.
  Y hay materia consolidada aún posterior, de 16/07/2026, en el artículo 33 bis.
- **Ley 31/1995** (última consolidación 09/04/2026) y **LOPDGDD 3/2018**
  (27/12/2025) también son posteriores a lo que cita el programa.
- **Ley 8/2009**, **Ley 13/2022** y el **TRLPI** sí coinciden con la foto que
  cita el programa.

**Decidido el 2026-08-29**: se escribe con la redacción vigente, y donde difiera
de la que cita el programa va una nota corta con qué cambió y cuándo. Cada tema
declara la fecha en que se leyó la fuente, porque la redacción vigente de hoy no
es necesariamente la de dentro de tres meses.
