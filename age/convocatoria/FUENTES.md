# Fuentes del programa: identificadores y acceso

Resueltos **contra el buscador del BOE** el **12 de septiembre de 2026**, uno a
uno, con `herramientas/boe_buscar.py`. Ninguno se ha deducido de la numeración
de la norma: el identificador se ha leído en el resultado de la búsqueda por
título. Es la regla del apartado 2 del manual, y aquí ya ha evitado un error:
buscar el Estatuto Básico del Empleado Público devuelve **primero su corrección
de errores** (`BOE-A-2015-12525`) y sólo después el texto refundido
(`BOE-A-2015-11719`). Quien copie el primer resultado se lleva la norma
equivocada.

## Bloque I · Organización pública

| Punto | Fuente | Identificador | Acceso |
|---|---|---|---|
| 1, 2, 3, 4, 5, 9 | Constitución Española | `BOE-A-1978-31229` | consolidado, API |
| 2 | Ley Orgánica 2/1979, del Tribunal Constitucional | `BOE-A-1979-23709` | consolidado, API |
| 4 | Ley Orgánica 6/1985, del Poder Judicial | `BOE-A-1985-12666` | consolidado, API |
| 5 | Ley 50/1997, del Gobierno | `BOE-A-1997-25336` | consolidado, API |
| 6 | Agenda 2030 y Objetivos de Desarrollo Sostenible | Resolución 70/1 de la Asamblea General de la ONU | **no es BOE**: fuente por localizar y declarar |
| 7 | Ley 19/2013, de transparencia, acceso a la información pública y buen gobierno | `BOE-A-2013-12887` | consolidado, API |
| 8 | Ley 40/2015, de Régimen Jurídico del Sector Público (título I y título II) | `BOE-A-2015-10566` | consolidado, API |
| 9 | Ley 7/1985, Reguladora de las Bases del Régimen Local | `BOE-A-1985-5392` | consolidado, API |
| 10 | Organización de la Unión Europea | Tratado de la Unión Europea y TFUE | **no es BOE**: se lee del DOUE, con `herramientas/doue.py` |
| 11 | Ley 39/2015, del Procedimiento Administrativo Común | `BOE-A-2015-10565` | consolidado, API |
| 11 | Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa | `BOE-A-1998-16718` | consolidado, API |
| 12 | Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales | `BOE-A-2018-16673` | consolidado, API |
| 12 | Reglamento (UE) 2016/679, general de protección de datos | `DOUE-L-2016-80807` | `doue.py`; **no consolidado**, y se dice |
| 13, 14 | Texto refundido de la Ley del Estatuto Básico del Empleado Público | `BOE-A-2015-11719` | consolidado, API |
| 13, 14 | Corrección de errores del anterior | `BOE-A-2015-12525` | **no confundir con la norma** |
| 15 | Ley 47/2003, General Presupuestaria | `BOE-A-2003-21614` | consolidado, API |
| 16 | Ley Orgánica 3/2007, para la igualdad efectiva de mujeres y hombres | `BOE-A-2007-6115` | consolidado, API |
| 16 | Ley Orgánica 1/2004, de Medidas de Protección Integral contra la Violencia de Género | `BOE-A-2004-21760` | consolidado, API |
| 16 | Ley 4/2023, para la igualdad real y efectiva de las personas trans y garantía de los derechos LGTBI | `BOE-A-2023-5366` | consolidado, API |
| 16 | Texto refundido de la Ley General de derechos de las personas con discapacidad | `BOE-A-2013-12632` | consolidado, API |
| 16 | Ley 39/2006, de Promoción de la Autonomía Personal y Atención a la dependencia | `BOE-A-2006-21990` | consolidado, API |

## Bloque II · Actividad administrativa y ofimática

**Aquí está el problema de este temario, y conviene verlo antes de escribir una
línea.** De los doce puntos, **sólo tres y medio tienen norma detrás**:

| Punto | Fuente | Identificador | Acceso |
|---|---|---|---|
| 1, 2 | Ley 39/2015 (derechos de las personas en sus relaciones con la Administración, arts. 13 y 53) | `BOE-A-2015-10565` | consolidado, API |
| 1 | Texto refundido de la Ley General de derechos de las personas con discapacidad | `BOE-A-2013-12632` | consolidado, API |
| 3 | Ley 39/2015 (registro electrónico y archivo) y Ley 40/2015 | `BOE-A-2015-10565` · `BOE-A-2015-10566` | consolidado, API |
| 4 | Ley 39/2015 (título de administración electrónica) y el Punto de Acceso General | `BOE-A-2015-10565` | consolidado, API |
| 5, 12 | Informática básica e Internet | — | **sin norma**: manual identificado con edición y página |
| 6, 7, 8, 9, 10, 11 | Windows 11 y Microsoft 365 de escritorio | — | **sin norma**: documentación del fabricante, con fecha de consulta |

**Seis de los doce puntos son producto de una empresa**, y la convocatoria fija
la versión: Windows 11 y Microsoft 365 versión de escritorio. Ahí no hay
precepto que citar, y **se aplica lo que ya hizo este proyecto en los quince
temas sin norma de RTVE**: se sustituye el precepto por una fuente citable y
estable —la documentación del propio fabricante, identificada y con fecha de
consulta— y se mantiene intacta la otra mitad de la regla, que lo que no se
puede sostener en una fuente se quita.

**Y esos seis puntos son la mitad de la nota.** Ver `EXAMEN.md`.

## Lo que falta por resolver

- **La Agenda 2030** (bloque I, punto 6) no está en el BOE. Hay que decidir y
  declarar la fuente: la Resolución 70/1 de la Asamblea General de Naciones
  Unidas es el documento, y su traducción oficial al español es la que habrá que
  citar, con su signatura.
- **La organización de la Unión Europea** (bloque I, punto 10) se lee de los
  Tratados. `herramientas/doue.py` los baja del BOE, y **el texto no está
  consolidado**: la herramienta lo dice y el tema tendrá que decirlo también.
- **Ninguna documentación de Microsoft está todavía volcada.** Sin ella los seis
  puntos de ofimática no se pueden escribir con este método.
