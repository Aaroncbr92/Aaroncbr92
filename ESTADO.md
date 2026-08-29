# Estado

Fichero de estado del apartado 11 del manual: qué es este temario, dónde vive
cada cosa, qué está hecho y qué falta. Se actualiza al final de cada sesión,
para que otra pueda seguir sin reconstruir nada.

**Última actualización:** 2026-08-29

## Qué es esto

Tres temarios de oposición de RTVE, por ocupación tipo: **Producción
(Asistencia)**, **Documentación** e **Información y Contenidos**. El programa
sale del ANEXO 2 de las bases, transcrito literal en `convocatoria/`.

Los tres comparten el mismo temario general y el mismo tema de prevención de
riesgos laborales, así que son **42 cuerpos de tema**, no 60. El reparto y el
orden están en `PLAN.md`.

**Convocatoria identificada**: son los anexos 2 de las **bases específicas de la
convocatoria 1/2022** (turno libre, adaptadas tras el acuerdo transaccional de la
Audiencia Nacional en los autos 154/2023) y de la **3/2022** (promoción interna y
cambio de ocupación tipo). El temario es el mismo en las dos. Las bases completas
están en `convocatoria/bases/` y los exámenes de octubre de 2024 en
`convocatoria/examenes/`.

**La prueba**: test de un mínimo de 80 preguntas más un 20 % de reserva, cuatro
opciones, acierto +1, error −1/3, blanco 0. En octubre de 2024 fueron 100
preguntas y 180 minutos en Información y Contenidos, y 80 preguntas y 120 minutos
en Documentación y en Producción (Asistencia).

## Hecho

- [x] Método y cláusulas de encargo en `metodo/`.
- [x] `herramientas/boe.py`: lector de legislación consolidada del BOE.
- [x] Programa transcrito literal: `convocatoria/PROGRAMA-GENERAL.md` y los tres
      `PROGRAMA-*.md` de específico.
- [x] Comprobado que el temario general es idéntico en los tres anexos, y que el
      tema de PRL también.
- [x] Identificadores del BOE de todas las fuentes del programa, localizados
      contra el BOE y no deducidos, en `convocatoria/FUENTES.md`.
- [x] Acceso probado fuente a fuente. Dos no se descargan (Manual de estilo de
      RTVE y el informe de la UNESCO): bloqueo del servidor, no del proxy.
- [x] Comprobado que el programa cita una foto de las normas anterior a la
      vigente, y en qué se nota (`convocatoria/FUENTES.md`).
- [x] `PLAN.md`: orden de trabajo y tratamiento de los temas sin norma detrás.
- [x] **Bases completas**: las específicas de las seis convocatorias que nos
      tocan y las generales de la 1/2022, con su transcripción, en
      `convocatoria/bases/`.
- [x] **87 exámenes de octubre de 2024 con sus plantillas de respuestas**,
      transcritos, en `convocatoria/examenes/`. El de Documentación es un
      escaneo y se pasó por OCR.
- [x] Calibración: reparto de preguntas por materia en las tres ocupaciones, en
      `informes/calibracion-examenes-2024.md`.
- [x] **Exámenes de convocatorias anteriores** en `convocatoria/examenes-antiguos/`:
      la convocatoria 1/2020 (pruebas de diciembre de 2021 y enero de 2022, con
      plantillas) y la de 2007, más sueltos de 1999, 2002, 2009, 2010 y 2011.
      Transcritos, con OCR los que hacía falta.
- [x] Comprobado que **las preguntas se repiten**: entre ocupaciones de la misma
      convocatoria y entre convocatorias, a veces palabra por palabra
      (`informes/preguntas-repetidas.md`).
- [x] **`banco/`: 465 preguntas reales del bloque común con su respuesta oficial**
      (447 de 465). Sustituye a las preguntas inventadas del apartado 7 del
      manual.
- [x] `herramientas/boe.py --fecha AAAAMMDD`: lee la ley como estaba ese día.
- [x] Las tres lentes de refutación, automatizadas y reutilizables en cualquier
      tema: `refutar_exactitud.py`, `refutar_modo.py` y `refutar_prosa.py`.
- [x] `herramientas/refutar_documento.py`: cuarta lente, para temas cuya fuente **no es
      articulado** (un plan, una guía, un manual). Contrasta cada negrita y **cada cifra**
      contra el texto completo de las fuentes. Hace falta porque las lentes por artículo
      devuelven «0 comprobadas, 0 hallazgos» sobre un documento sin artículos, que se lee
      como un tema impecable y es un tema sin revisar.
- [x] `herramientas/convenio_dump.py`: reconstruye el articulado del convenio en
      vigor superponiendo el acuerdo de 2022 sobre el texto de 2020, con la forma
      que esperan las lentes. Hace falta porque **el convenio no es legislación
      consolidada**: el BOE no publica texto refundido y `boe.py` no sirve.
- [x] **Comprobados todos los acuerdos del Convenio Colectivo**, por el bloque de
      «referencias posteriores» de su ficha en el BOE. **Anteriores al corte son cuatro, no
      tres**: faltaba `BOE-A-2021-8252` (18/05/2021), que sustituye entero el anexo 7.
      Posteriores al corte hay otros cuatro (2023 ×2, 2024 y 2025), anotados como nota de
      actualización en el tema; el de agosto de 2023 toca los artículos 42, 50, 52, 57, 72
      y 91, así que **cualquier material posterior a esa fecha da cifras que no son las del
      examen**.
- [x] **Descubierto que partes del convenio solo existen como imagen** en el BOE:
      la tabla de niveles del artículo 65 y los anexos 1, 2 y 3 completos. No están
      en el HTML ni en la transcripción de texto, y su ausencia no da ningún aviso.
      Descargadas y **transcritas las cinco** en `fuentes/convenio/imagenes/`: la tabla
      del artículo 65 y los anexos 1, 2 y 3.
- [x] Ley 17/2006 y Ley 5/2017 volcadas a `fuentes/`, en la redacción de hoy y en
      la del corte 21/12/2022. Entre una y otra cambian **11 bloques** de la Ley
      17/2006: arts. 4, 10, 11, 12, 15, 16, 20 y 24 y tres disposiciones
      transitorias.

## Decisiones tomadas

- **2026-08-29 · Qué redacción se estudia. Corregida el mismo día al leer las
  bases.** El cuerpo del tema se escribe con la redacción **vigente el 21 de
  diciembre de 2022**, que es la fecha de corte que imponen las bases (punto 6:
  «las pruebas se realizarán sobre su texto vigente a fecha de la primera
  publicación de las Bases Generales»). Donde la redacción de hoy sea distinta va
  una **nota de actualización** al final del epígrafe, marcada como tal y fuera
  del cuerpo examinable.
  La primera decisión de esta sesión fue la contraria —cuerpo con la redacción
  vigente hoy— y se tomó sin tener las bases delante. Las bases mandan.
  Excepción: en **Información y Contenidos**, los apartados 1, 2 y 3 del temario
  específico (actualidad, Unión Europea, instituciones) **sí** cuentan hechos
  posteriores al corte.

## Falta

- [ ] Los **anexos 5 y 6 de las Bases Generales** (baremos de méritos). La versión
      descargada no los trae. No afectan al temario.

- [ ] **Manual de estilo de RTVE** y **informe UNESCO 2021/2022**: conseguirlos
      por otra vía.
- [ ] Tema 7 del general: **Ley 13/2022** general de comunicación audiovisual.
- [ ] Tema 8 del general: **Ley 31/1995** de prevención de riesgos laborales.

## Qué comprobación pasa por qué material

El apartado 10 del manual: un hueco de cobertura no da error, así que se
escribe. Se rellena desde los ficheros de `informes/`, no de memoria.

| Tema | Investigar | Redactar | Verificar | Refutar 1 | Rematar | Refutar 2 | Preguntas |
|---|---|---|---|---|---|---|---|
| General 1 · Constitución | sí | sí | sí | sí | sí | sí, limpia | 87 de 89 enteras |
| General 2 · Ley 17/2006 | sí | sí | sí | sí | sí | sí, limpia | 32 de 32 enteras |
| General 3 · Ley 5/2017 | sí | sí | sí | sí | sí | sí, limpia | incluidas en las 32 |
| General 4 · Ley 8/2009 | sí | sí | sí | sí | sí | sí, limpia | 23 de 23 enteras |
| General 5 · III Convenio Colectivo | sí | sí | sí | sí | sí | sí, limpia | 84 de 84 enteras |
| General 6 · Igualdad | sí | sí | sí | sí | sí | sí, limpia | 39 de 39 enteras |

**El tema 1 está cerrado**, con su esquema en `esquemas/general/`. La lista del
apartado 13 del manual, repasada punto por punto, está al final de
`informes/refutacion-tema-01.md`.

Lo del tema 1: investigado sobre el volcado del texto consolidado a la fecha de
corte; verificado con 28 comprobaciones de cifra contra el articulado y el
recuento de las enumeraciones; refutado con tres lentes distintas —exactitud
normativa, cobertura y prosa—, que sacaron **diez hallazgos reales** más
(`informes/refutacion-tema-01.md`); rematado revisando antecedentes; y la
**segunda refutación vuelve sin ningún hallazgo real**.

## Decisión de esta sesión

- **2026-08-29 · Cómo se verifica un tema cuya fuente no es legislación
  consolidada.** El III Convenio Colectivo no tiene texto refundido oficial: son
  tres documentos del BOE que hay que superponer. En vez de renunciar a las lentes
  o de darlas por pasadas, se construyó la fuente (`convenio_dump.py`) y se
  ejecutaron las tres sobre ella. Al hacerlo aparecieron **dos puntos ciegos en las
  propias lentes** —no reconocían la abreviatura «Art.» ni los rótulos de rango
  «Artículos 53 a 56»—, que dejaban artículos enteros sin comprobar devolviendo un
  resultado limpio. Corregidos y **repasados los cuatro temas ya cerrados**, lo que
  destapó un hallazgo real en el tema 2 (artículo 36: la presentación consolidada
  se suma a la individual, no la sustituye). Está contado en
  `informes/refutacion-tema-05.md`.
- **El tema 3 no pasa por la lente por artículo y se dice.** La Ley 5/2017 tiene
  «Artículo único» y el tema cita artículos de otra norma, así que la lente
  devuelve «0 comprobadas, 0 no literales», que **no es un aprobado**. Se verificó
  a mano y con un contraste contra el texto completo, y así consta en el informe.

- **2026-08-29 · Qué se hace cuando la fuente no está en el BOE.** El tema 6 son dos PDF
  publicados en `rtve.es`: sin identificador, sin texto consolidado y sin redacciones
  fechadas, de modo que **no se puede demostrar qué decían en una fecha pasada**. Se aplican
  tres reglas: **se versionan los PDF además de su transcripción**, para que quede la versión
  con la que se ha estudiado; se **verifica con `refutar_documento.py`** en vez de dar por
  buenas las lentes por artículo; y **se dice en el tema** que si RTVE sustituyera el fichero
  no quedaría rastro del anterior. Lo mismo valdrá para el Manual de estilo y el Código de
  autorregulación del menor de los temarios específicos.
