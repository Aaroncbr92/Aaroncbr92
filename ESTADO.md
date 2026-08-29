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
- [x] `herramientas/boe.py --fecha AAAAMMDD`: lee la ley como estaba ese día.
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
- [ ] Buscar exámenes de convocatorias anteriores a 2024, si los hay publicados.
- [ ] **Manual de estilo de RTVE** y **informe UNESCO 2021/2022**: conseguirlos
      por otra vía.
- [ ] Comprobar si hay acuerdos del Convenio Colectivo posteriores a 2022.
- [ ] Primer tema piloto por el ciclo completo.

## Qué comprobación pasa por qué material

El apartado 10 del manual: un hueco de cobertura no da error, así que se
escribe. Se rellena desde los ficheros de `informes/`, no de memoria.

| Tema | Investigar | Redactar | Verificar | Refutar 1 | Rematar | Refutar 2 | Preguntas |
|---|---|---|---|---|---|---|---|
| _(sin temas todavía)_ | | | | | | | |
