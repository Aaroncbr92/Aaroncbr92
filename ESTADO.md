# Estado

Fichero de estado del apartado 11 del manual: qué es este temario, dónde vive
cada cosa, qué está hecho y qué falta. Se actualiza al final de cada sesión,
para que otra pueda seguir sin reconstruir nada.

**Última actualización:** 2026-08-30

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
- [x] **`banco/`: 505 preguntas reales** —476 del bloque común y 29 del tema de
      prevención del específico—, **todas con su respuesta oficial**.
      Sustituye a las preguntas inventadas del apartado 7 del manual.
- [x] **El volumen, listo para el opositor** (`informes/mejoras-formato-2026-08-30.md`):
      sin una sola referencia a ficheros del proyecto, con **encabezado y pie**
      —portada limpia—, **índice a tres niveles con número de página y clicable**
      en PDF y en Word, **marcadores** en el PDF, cuerpo justificado y preguntas
      sin la línea de procedencia.
- [x] **Las 505 preguntas tienen respuesta oficial.** Las tres plantillas cuyo PDF
      no lleva tabla de caracteres se leen **celda a celda**
      (`herramientas/plantilla_ocr.py`), contrastadas contra la imagen y contra
      preguntas repetidas. **El cuaderno de pendientes queda vacío.**
- [x] **Segunda prueba de cobertura**, sobre las **111 preguntas** que la pasada de
      verificación añadió y que nunca habían pasado el apartado 7 del manual
      (`informes/cobertura-nuevas-2026-08-30.md`): **102 se contestaban** y **9 no**.
      Las nueve lagunas, cerradas contra la fuente —**los artículos 10, 11 y 22 y el
      teletrabajo fuera de horario en el tema 5**; **la respuesta de la Guía a «¿y si la
      víctima es un hombre?» en el 6**; y **el múltiplex, el productor independiente y
      los artículos 145, 146.3 y 150 en el 7**—. **Con esto, las preguntas del banco se
      contestan todas con el tema delante.**
- [x] **Pasada de verificación sobre el banco**, leyendo las preguntas una a una
      (`informes/verificacion-banco-2026-08-30.md`): el salto de página fundía
      **83 preguntas** con la de al lado, cinco cuadernillos ilegibles no
      aportaban **93 más** y nada daba error, y **113 estaban en el cajón
      equivocado**. Las correcciones viven en `banco/reclasificadas.tsv`, que
      `banco.py` aplica al regenerar y cuyas filas huérfanas avisa.
- [x] `herramientas/word.py`: el mismo volumen en **.docx con estilos de Word con
      nombre** y **sin una sola línea de formato a mano**, para poder darle el formato
      en Word y devolverlo. Lo que vuelva en `word/styles.xml` se traslada al CSS de
      `libro.py`. `--temas 1` saca solo un tema.
- [x] `herramientas/boe.py --fecha AAAAMMDD`: lee la ley como estaba ese día.
- [x] Las tres lentes de refutación, automatizadas y reutilizables en cualquier
      tema: `refutar_exactitud.py`, `refutar_modo.py` y `refutar_prosa.py`.
- [x] **`boe.py` avisa de la vacatio**: si un bloque existe en el texto publicado pero su
      entrada en vigor es posterior a la fecha leída, el volcado deja **el rótulo con el
      aviso y la fecha**, y el resumen los enumera. Antes los omitía en silencio y el rastro
      quedaba solo en el `.tsv`: en la Ley 13/2022 eran **quince bloques**, dos de ellos
      preguntados en el examen.
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
- [x] **Los nueve temas llevan portada e índice, y los nueve esquemas llevan índice**,
      generados con `herramientas/indice.py` y **regenerables**: un índice escrito a mano se queda viejo al
      primer epígrafe que se añade, y un índice viejo no da error, lleva a otro sitio. La
      portada dice bloque del programa, fuente, identificador, redacción que se estudia,
      extensión medida y dónde están el esquema y los informes. **El script comprueba que las
      rutas que cita existen**, y así se descubrió que **los temas 2 y 3 citaban un informe de
      refutación que nunca se había escrito**: reconstruido en
      `informes/refutacion-temas-02-03.md`, marcado como reconstrucción.
      El **esquema no lleva portada** —la ficha de la norma está en su tema y repetirla sería
      ruido—, y el **índice va justo antes del primer epígrafe**, para no enterrar la
      entradilla bajo veinte líneas de enlaces.
- [x] **Corregido cómo se miden las palabras.** Todas las cifras de extensión publicadas hasta
      el 2026-08-30 salían de `wc -w` **en locale C**, que **cuenta de menos en texto
      acentuado**: el esquema del tema 8 no eran 3.856 palabras sino **3.966**, y el del
      específico de PRL no 2.802 sino **2.937**. Las líneas se contaban además **con las
      vacías**. Corregidas en los informes, con la causa dicha. `indice.py` mide con separación
      de palabras Unicode, así que las portadas ya nacen bien.
- [x] **Las cuatro lentes ignoran la portada y el índice** (`herramientas/tema.py`, una sola
      función compartida). Sin eso, el envoltorio metía **ocho falsos «no literales» y una
      cifra huérfana por tema**: ruido que acaba enseñando a no mirar la lista.
- [x] **Cuaderno de pendientes vaciado (2026-08-30).** Los ocho hallazgos que había están
      cerrados: **cuatro investigados y aplicados** —la entrada en vigor de la DF cuarta de la
      Ley 13/2022, la fecha de cese del artículo 155, el número de senadores y el interruptor
      diferencial— y **cuatro que no eran trabajo pendiente** sino erratas comprobadas de
      plantillas y decisiones ya tomadas, mal archivadas bajo el epígrafe «Aplicados». El
      fichero se ha reorganizado en cuatro secciones y **conserva todo el histórico**.
      **Dos de las cuatro resoluciones fueron en contra de lo que la propia anotación decía**:
      la de la Ley 8/2009 la daba por irrelevante para el examen y sí lo era, y la del
      diferencial acusaba a la plantilla oficial de un error que no había.
- [x] **Bloque común cerrado: los 8 temas del general y el de PRL del específico**, que sirve
      para las tres ocupaciones como **P18 / D7 / I11**. Con eso está hecho todo lo que rinde
      por tres.
- [x] **`refutar_documento.py` cose las palabras que el PDF parte al final del renglón.**
      Cambiaba el guion por un espacio y una cita literal salía marcada como «no literal»; y la
      clase de caracteres era el rango `U+2010..U+2015`, que **no incluye el guion normal**, así
      que el primer arreglo no movió ni una cifra. Corregido: **26 falsos «no literales»** menos
      en el tema de PRL, y ninguno en el tema 6, que es el otro que usa esta lente.
- [x] **Fuentes del tema de PRL del específico** en `fuentes/prl-especifico/`: Guía Técnica de
      pantallas del INSST (junio 2021), documento del INSST sobre TME de la extremidad superior,
      NTP 536, NTP 1090 y 1091, informe de Seguridad Vial Laboral de la CNSST y la ficha de
      doctrina del Tribunal Supremo sobre in itinere y en misión, con sus transcripciones.
- [x] **Las lentes ven los artículos «bis»**: el patrón de la fuente estaba anclado en
      `Artículo (\d+)$` y **«Artículo 32 bis» no acaba en dígito**, así que no entraba en el
      diccionario, **no se comprobaba nunca** y además su texto en el tema se contrastaba
      contra el artículo 32, que dice otra cosa. Corregido en `refutar_exactitud.py` y
      `refutar_modo.py`, con las claves hechas cadenas.
- [x] **Una remisión dentro de una frase ya no abre epígrafe**: «conoce las actuaciones de los
      **artículos 7, 8, 9 y 11**» abría bloque y toda la explicación posterior se comprobaba
      contra el artículo 7. Ahora el marcador que **abre epígrafe** manda sobre su párrafo y el
      que va **dentro de una frase** se queda solo con su frase. El primer intento —descartar
      todos los marcadores de dentro de frase— dejó **catorce artículos del tema 7 sin mirar**,
      y se detectó porque **la cifra de negritas comprobadas bajó al «arreglarlo»**.
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
- [ ] **Fase B: los tres temarios específicos.** Documentación es el más corto (6 temas),
      Producción (Asistencia) el más largo (17) e Información y Contenidos el más entrelazado
      con el general (10). El orden y el tratamiento de los temas sin norma detrás, en `PLAN.md`.

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
| General 7 · Ley 13/2022 | sí | sí | sí | sí | sí | sí, con 11 salvedades declaradas | 34 de 34 enteras |
| General 8 · Ley 31/1995 | sí | sí | sí | sí | sí | sí, con 3 falsos positivos declarados | 49 de 52 enteras, 2 a medias |
| PRL del específico (P18/D7/I11) | sí | sí | sí | sí | sí | sí, limpia | 35 de 40 enteras, 1 con matiz, 5 fuera de tema |

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

- **2026-08-29 · Qué se hace cuando parte de la norma aún no estaba en vigor al corte.** La
  Ley 13/2022 escalona su entrada en vigor en ocho reglas (DF novena) y **quince bloques no
  eran exigibles el 21/12/2022**, entre ellos los artículos 102 y 115, que el tribunal
  preguntó en 2024. Se estudia **la ley entera**: la fecha de corte congela **el texto**, que
  en esta ley no ha cambiado ni una palabra desde su publicación, y lo diferido era la
  **exigibilidad**. El programa lo respalda al citar el «texto inicial». En el volcado al
  corte esos bloques llevan **aviso expreso**, y el tema explica la distinción.
