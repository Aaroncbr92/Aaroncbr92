# Banco de preguntas del bloque común

**510 preguntas reales** —480 del temario general y 30 del tema de prevención del
específico— sacadas de los cuadernillos de la convocatoria 1/2022 (pruebas de
octubre y noviembre de 2024), **todas con la respuesta de la plantilla oficial**.

Se puede hacer porque el temario general es el mismo para las más de cincuenta
ocupaciones tipo convocadas, y porque las preguntas del bloque común se comparten
entre ocupaciones: está comprobado en `informes/preguntas-repetidas.md`.

| Fichero | Materia | Preguntas |
|---|---|---|
| `g1.md` | Constitución | 117 |
| `g2-g3.md` | Ley 17/2006 y Ley 5/2017 | 53 |
| `g4.md` | Ley 8/2009, financiación | 35 |
| `g5.md` | III Convenio Colectivo | 118 |
| `g6.md` | II Plan y Guía de Igualdad | 47 |
| `g7.md` | Ley 13/2022, General de Comunicación Audiovisual | 47 |
| `g8.md` | Ley 31/1995, prevención de riesgos | 63 |
| `prl-especifico.md` | Prevención en el temario **específico** (P18 · D7 · IyC11) | 30 |

Cinco de esas preguntas entraron el **2026-09-02**, al repartir a mano el bloque
específico: dos de la **Ley 31/1995** —el Comité de Seguridad y Salud y la
coordinación de actividades empresariales—, dos del **III Convenio** —las
comisiones de servicio y el artículo 107, que el examen llama «ley de
incompatibilidades»— y una del **PRL del específico** —el túnel carpiano—.

**Y esta tabla estaba mal, en dos filas que se compensaban.** Decía 114 en `g5.md`
cuando eran 116, y 48 en `g6.md` cuando eran 47: el **total de 505 salía bien** y
por eso nadie lo miró. Se descubrió al comparar los ficheros antes y después de
regenerarlos. La lección es del apartado 10 del manual: **un total correcto no
prueba que sus sumandos lo sean**, y la cifra que se publica hay que sacarla de
contar, no de copiar.

Se regenera con `herramientas/banco.py`. **Las correcciones no se hacen sobre
estos ficheros**, que se sobrescriben enteros: van en `reclasificadas.tsv`.

## Y el banco del bloque **específico**

**123 preguntas**, repartidas entre los diecisiete temas del Anexo 2 de Producción
(Asistencia) y **todas con su respuesta oficial**.

| Fichero | Tema | Preguntas |
|---|---|---|
| `produccion-01.md` | 1 · La producción: sistemas y métodos | 6 |
| `produccion-02.md` | 2 · Derechos de autor. Propiedad intelectual | 10 |
| `produccion-03.md` | 3 · El guion | 6 |
| `produccion-04.md` | 4 · El desglose | 2 |
| `produccion-05.md` | 5 · Localización | 3 |
| `produccion-06.md` | 6 · Organización, plan y orden de trabajo | 4 |
| `produccion-07.md` | 7 · Equipos humanos | 6 |
| `produccion-08.md` | 8 · Formatos y soportes | 6 |
| `produccion-09.md` | 9 · Escenografía e iluminación | **20** |
| `produccion-10.md` | 10 · Imagen y sonido | **17** |
| `produccion-11.md` | 11 · Medios de transmisión de señal | 10 |
| `produccion-12.md` | 12 · El estudio de televisión | 6 |
| `produccion-13.md` | 13 · Equipos técnicos de exteriores | 7 |
| `produccion-14.md` | 14 · Documentación internacional | 6 |
| `produccion-15.md` | 15 · Organismos | 6 |
| `produccion-16.md` | 16 · Gestión de servicios varios | 3 |
| `produccion-17.md` | 17 · Protección de datos | 5 |

Se regenera con `herramientas/banco_especifico.py`, y **el reparto se escribe a
mano** en `especifico-produccion.tsv`, una fila por pregunta y con el motivo al
lado. No se clasifica por palabras clave, y no por comodidad: las preguntas del
específico hablan de *beauty shot*, del cuaderno ATA o de SMPTE 2110, y muchas
podrían caer en dos temas a la vez. Una regla automática sobre eso no da un
reparto discutible, da **uno falso que nadie va a revisar**.

Y hay una razón más, que se vio al hacerlo: la pregunta «en una producción
interna, ¿qué derechos tiene la CRTVE?» **es de propiedad intelectual** —la
contesta el artículo 88 de la Ley— y **no nombra la ley ni ningún artículo**.
Ninguna palabra clave la habría cogido.

El script avisa de las **filas que ya no casan con ninguna pregunta**, no cuenta
como pendientes las que ya están repartidas a mano en `reclasificadas.tsv`, y
dice **cuántas preguntas específicas quedan sin repartir**: ahora mismo, **cero**.
