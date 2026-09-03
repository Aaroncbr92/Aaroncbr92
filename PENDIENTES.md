# Cuaderno de pendientes

Cualquier sesión anota aquí lo que detecte, aunque no lo corrija en el momento.
Lo aplicado se tacha con su fecha, **no se borra**: el histórico es lo que deja
ver si un mismo error se repite en varios temarios.

Cada entrada, cinco campos:

- **Dónde**: tema y epígrafe.
- **Qué dice** hoy.
- **Qué debería decir**, ya redactado para pegar.
- **Fuente**: el precepto en su redacción vigente, citado literal. Si no se ha
  comprobado, se dice.
- **Gravedad**: cambia la respuesta / induce a error / menor.

---

## Abiertos

### 2026-09-03 · Los informes tampoco pasan la lente de prosa — abierto

- **Dónde**: `informes/`.
- **Qué pasa**: el mismo problema que tenían los esquemas y por la misma razón: **la lente nunca se
  les había pasado**. El barrido devuelve **95 informes con aviso de los 141**, del orden de
  trescientas setenta siglas sin presentar.
- **Qué debería decir**: los cuatro informes nuevos de Sonido y de Técnica de Equipos ya abren con
  una línea de siglas, y **ése es el patrón a extender**.
- **Por qué no se cierra hoy, dicho sin adornos**: **los informes son documentación interna del
  proyecto y no van dentro de los libros**, así que **no llegan al opositor**. Los esquemas sí van
  impresos, y por eso se han cerrado primero.
- **Por dónde se arregla**: igual que en los esquemas —heredando la presentación del tema al que
  cada informe acompaña—, con la diferencia de que **un informe no tiene tema gemelo con el mismo
  nombre**, así que la correspondencia hay que darla a mano.
- **Gravedad**: menor.
- **Estado**: **abierto.**

---

## Cerrados

### 2026-09-03 · La lente de prosa nunca se había pasado a los esquemas — cerrado el mismo día

- **Dónde**: los 207 esquemas de `esquemas/`.
- **Qué pasaba**: `refutar_prosa` se venía pasando **sólo a los temas**. Al pasarla por primera vez a
  los esquemas devolvió **141 ficheros con aviso**.
- **Lo primero fue corregir la lente**, porque la mayor parte de esos avisos no eran siglas sino el
  propio estilo del telegrama: **contrastar cada esquema contra su tema gemelo** —de donde toma su
  vocabulario—, **descartar las mayúsculas que el tema no nombra** —un rótulo que el esquema inventa
  no puede ser una sigla de la materia— y **una lista de palabras castellanas** que el telegrama
  escribe en mayúsculas por estilo. Con eso el barrido bajó a **105 esquemas y 438 avisos, ya todos
  siglas de verdad**.
- **Aplicado**: **109 esquemas llevan ahora una línea de siglas de entrada**. **De las 438
  apariciones, 259 se heredaron literalmente del párrafo «Las siglas de este tema» de su tema
  gemelo** y **105 más del cuerpo del tema**, con la extracción revisada una a una y **treinta
  recortes corregidos a mano** porque salían partidos por la mitad. **Las 74 restantes se
  escribieron a mano** contra el tema.
- **Y lo que no se ha inventado**: donde el tema declara que no ha verificado una forma larga
  —VINTEN, JDR Pan Bar, ORAD, Brainstorm IPF, THX, DTS, PXW, ACN, IMG, TDP, UHF, VHF—, **el esquema
  lo repite en lugar de rellenarlo**.
- **Dos títulos de esquema se reescribieron**, porque llevaban la sigla por delante de su
  presentación: el del real decreto-ley 4/2018 y el de la Carta ética de la Federación Internacional
  de Periodistas.
- **Estado**: **cerrado. Los 207 temas y los 207 esquemas quedan a cero.**


### 2026-09-03 · `banco/reclasificadas.tsv` mandaba una pregunta a dos sitios — cerrado el mismo día

- **Dónde**: `banco/reclasificadas.tsv`, pregunta 96 de `70_preguntas_tese_a`.
- **Qué decía**: **dos filas contradictorias** para la misma pregunta. Una la mandaba a
  `prl-especifico` y la otra la sacaba del general por ser materia del punto 20 del específico de
  Técnica de Equipos.
- **Por qué importa**: el fichero lo aplica `herramientas/banco.py` **después de clasificar**, y con
  dos destinos el resultado depende de cuál gane, que no es una decisión que deba tomar el orden de
  las líneas.
- **Aplicado**: se borra la fila `prl-especifico` y sobrevive la correcta. La pregunta está en
  `banco/especifico-tese.tsv`, tema 17.
- **Gravedad**: menor, sin efecto en el producto: el reparto final era el correcto.

### 2026-09-03 · El guion de reindexado borraba los subepígrafes del índice — cerrado el mismo día

- **Dónde**: el guion auxiliar que reconstruye el bloque `<!-- indice -->`.
- **Qué pasaba**: recogía **sólo los encabezados de segundo nivel**. Al reindexar
  `temas/prl/prl-especifico.md`, que es el único tema del proyecto con subepígrafes en el índice,
  **borró sus 63 entradas de tercer nivel sin avisar**.
- **Aplicado**: el guion recoge ahora los de segundo y tercer nivel, con sangría. Índice restaurado
  y ampliado a 75 entradas.
- **Gravedad**: **induce a error** mientras dura: un índice paginado al que le faltan dos tercios de
  sus entradas es peor que no tenerlo.


_Los ocho que había se cerraron el 2026-08-30. La pasada de verificación del banco abrió
**uno**, al final de este cuaderno: tres plantillas oficiales que el OCR no lee enteras. La
segunda prueba de cobertura, ese mismo día, encontró **nueve lagunas** en los temas 5, 6 y 7
y **las cerró todas** contra la fuente: no queda trabajo pendiente de ellas
(`informes/cobertura-nuevas-2026-08-30.md`)._

### 2026-08-30 · Un dato que estaba en el esquema y no en el tema — cerrado el mismo día

- **Dónde**: tema 6 del general, epígrafe 17, y `esquemas/general/06-igualdad.md`.
- **Qué pasaba**: el esquema decía «**si la víctima es un hombre, no es violencia de género ni
  entra en la LO 1/2004**» y **el cuerpo del tema no lo decía**. El esquema se escribe **desde**
  el tema, así que ese dato entró por la puerta de atrás y nunca volvió al cuerpo.
- **Por qué importa como método**: un esquema por delante del tema es un aviso de que el ciclo
  se saltó un paso. Y lo destapó una pregunta del banco, no una lente: **ninguna de las cuatro
  lentes compara el tema con su propio esquema**.
- **Aplicado**: el tema recoge ahora la respuesta de la Guía **en cita literal**, con el
  distractor —«violencia contra el hombre o varón si la agresora es una mujer que mantiene
  relaciones sentimentales con la víctima»—, y el esquema se ha completado con él.
- **Lo que queda como idea, no como trabajo**: una quinta lente que compare cada tema con su
  esquema y avise de lo que está en uno y no en el otro. No se hace ahora porque con nueve
  temas se comprueba a mano; con treinta y tres, no.


### 2026-09-03 · Realización Televisión: la pregunta 33 no es una errata de plantilla — precisado el mismo día

- **Dónde**: `temas/realizacion-tv/05-el-cine.md`, sus dos informes, el esquema, `banco/README.md` y
  el aviso de `herramientas/libro.py`.
- **Qué decía**: que la pregunta 33 del primer llamamiento —el récord de Óscar— era **«la undécima
  errata del proyecto»**.
- **Por qué estaba mal**: **el proyecto cuenta las «erratas de plantilla» como respuestas oficiales
  EQUIVOCADAS**, y van diez. **La respuesta de esta pregunta no es equivocada**: *Ben-Hur* tiene once
  Óscar y es una respuesta correcta. **Lo que falla es el enunciado**, que pide «la película con
  mayor número» cuando **hay tres empatadas y tres de las cuatro opciones son esas tres**. Meterla en
  la cuenta de erratas de plantilla habría inflado una cifra que el proyecto usa para medirse.
- **Aplicado**: se la llama **«la undécima costura documentada del proyecto»** —el término que el
  propio README usa para el conjunto— y **en los cinco sitios se dice expresamente que NO es errata
  de plantilla y que la cuenta de erratas sigue en diez**.
- **Gravedad**: menor en cuanto al contenido —la instrucción al opositor no cambia: marcar la
  plantilla e impugnar— y **no menor en cuanto al método**: **una cifra que se usa para medir el
  proyecto no puede crecer por asimilación.**

---
---

## Erratas comprobadas en plantillas oficiales de 2024

No son trabajo pendiente: son **avisos permanentes**. Las tres están verificadas por los dos
extremos —el emparejamiento de la plantilla y el precepto en su redacción vigente— y en las tres
**el tema enseña la norma, no la plantilla**. Se dejan aquí para que quien estudie por las
plantillas sepa dónde le van a enseñar mal.

### 2026-08-29 · Errata en una plantilla oficial de respuestas

- **Dónde**: `convocatoria/examenes/82_plantilla_de_respuestas_produccion.txt`,
  pregunta 32 del cuadernillo de Producción.
- **Qué dice**: la pregunta «¿Qué Título de la Constitución recoge los derechos y
  libertades de los ciudadanos españoles?» tiene como respuesta oficial **b)
  Título segundo**.
- **Qué debería decir**: **a) Título primero**. Los derechos y deberes
  fundamentales son el **Título I** (artículos 10 a 55); el Título II es el de la
  Corona.
- **Fuente**: texto consolidado de la Constitución, `BOE-A-1978-31229`, rúbrica
  del Título I: «De los derechos y deberes fundamentales».
- **Comprobado que no es un desajuste de nuestra lectura**: en esa misma plantilla,
  la pregunta 34 —«¿cómo se denomina el enlace de subida de una señal a satélite?»—
  responde «b) Uplink», que es correcto, así que la numeración está alineada. El
  error es de la plantilla.
- **Gravedad**: no afecta al tema, pero conviene saberlo antes de estudiar por las
  plantillas. **No se corrige el tema para que cuadre con la plantilla.**

### 2026-08-29 · Segunda errata en una plantilla oficial de respuestas

- **Dónde**: `convocatoria/examenes/79_plantilla_de_respuestas_produccion_asist.txt`,
  pregunta 51 del cuadernillo de Producción (Asistencia) de octubre de 2024.
- **Qué dice**: a la pregunta «¿cuántos miembros del Consejo Asesor son designados
  por el Consejo de Consumidores y Usuarios?» responde **a) Tres**.
- **Qué debería decir**: **b) Dos**. Los **tres** son los que designa el **Consejo
  Económico y Social**.
- **Fuente**: artículo 23.2 de la Ley 17/2006, redacción vigente a 21/12/2022,
  letras a) y b), leídas en el texto consolidado `BOE-A-2006-9958`.
- **Comprobado que no es un desajuste de nuestra lectura**: en esa misma plantilla,
  la pregunta 1 responde «b» al artículo 44 de la Constitución —el acceso a la
  cultura, que es correcto—, la 50 responde «c» a la hoja de script y la 39
  responde «d» al reparto seis y cuatro de la Ley 5/2017. La numeración está
  alineada; el error es de la plantilla.
- **Gravedad**: induce a error. Quien estudie por las plantillas aprenderá mal el
  artículo 23. **El tema no se ha cambiado para que cuadre con ella**, y lo dice
  expresamente en el epígrafe del Consejo Asesor.

### 2026-08-30 · Tercera errata en una plantilla oficial de respuestas

- **Dónde**: `convocatoria/examenes/63_plantilla_de_respuestas_realizacion_asist_2_llamamiento.txt`,
  pregunta 77 del cuadernillo de Realización (Asistencia), 2.º llamamiento, 07/11/2024.
- **Qué dice**: a «¿cuántos delegados de prevención debe haber en una empresa de **251 a 500
  trabajadores**?» —opciones a) 2, b) 3, c) 4, d) 5— responde **c) 4**.
- **Qué debería decir**: **b) 3**.
- **Fuente**: **artículo 35.2 de la Ley 31/1995**, redacción única desde el 10/02/1996, leída en
  el volcado del texto consolidado `BOE-A-1995-24292` a la fecha de corte: «*De 101 a 500
  trabajadores: 3 Delegados de Prevención*». El **4** es el del tramo siguiente, **de 501 a
  1.000**.
- **Comprobado que no es un desajuste de nuestra lectura**: la plantilla trae **120 números y
  120 letras** en el mismo orden, y las **otras seis preguntas de la escala** que hay en el
  banco cuadran todas con la ley (50-100 → 2; 501-1.000 → 4, dos veces; 1.001-2.000 → 5;
  2.500 → 6; más de 4.000 → 8). La única que se sale es ésta.
- **Gravedad**: cambia la respuesta. **El tema 8 enseña la escala como está en la ley** y no se
  ha tocado para cuadrar con la plantilla.

---

## Decisiones tomadas, sin trabajo pendiente

Casos en que **la respuesta oficial pide algo que la fuente no dice**. Se ha decidido **no tocar
el tema**, porque escribir lo que la fuente no sostiene es exactamente lo que el apartado 1 del
manual prohíbe. Se dejan anotados por si en una convocatoria futura el tribunal insiste.

**Con una excepción, que se marca porque enseña más que los aciertos**: uno de los casos que
había aquí —el interruptor diferencial— **resultó estar bien en la plantilla y mal en esta
anotación**. Se resolvió el 2026-08-30 y está aplicado en el tema; la entrada se conserva con su
cierre para que quede el histórico del error propio.

### 2026-08-30 · Dos preguntas del banco g8 que la Ley 31/1995 no contesta por sí sola

- **Dónde**: tema 8 del general, artículos 15.1.d) y 29.
- **Qué dice hoy**: el tema recoge los dos preceptos **literales**, y con ellos las preguntas se
  aciertan por eliminación.
- **Qué debería decir**: lo mismo. **No se amplía**, porque lo que piden las respuestas oficiales
  no está en la ley:
  - `81_preguntas_produccion nº 1` da por buena «*organizar el trabajo de forma que se garantice
    una adecuada distribución de las tareas, evitando la monotonía y la sobrecarga física y
    psíquica*». La ley solo dice, en el **art. 15.1.d)**, «*atenuar el trabajo monótono y
    repetitivo y reducir los efectos del mismo en la salud*».
  - `13_preguntas_fx nº 88` da por buena «**participar en la formación preventiva**» como
    obligación del trabajador. El **art. 29.2** enumera **seis** obligaciones y ésa no está: la
    formación es **deber del empresario de garantizarla** (**art. 19**).
- **Fuente**: artículos 15.1.d), 19 y 29 de la Ley 31/1995, redacción vigente al corte.
- **Gravedad**: menor. Queda anotado por si en una convocatoria futura el tribunal insiste, que
  entonces habría que decidir si se recoge la formulación del tribunal advirtiendo de que no es
  la de la ley.

### 2026-08-30 · Dos opciones oficiales del bloque de PRL que la fuente no sostiene

**a) «Seguridad informática» como riesgo de las pantallas de visualización.**

- **Dónde**: tema de PRL del específico, rúbrica 2.
- **Qué dice hoy**: que el **artículo 3.1 del RD 488/1997** obliga a que el uso de estos equipos
  **«no suponga riesgos para su seguridad o salud»** del trabajador.
- **Qué dice el examen**: `77_preguntas_produccion_asist nº 77` da por buena la opción **b)
  «Para la salud y la seguridad informática»**.
- **Fuente**: artículo 3.1 del RD 488/1997, redacción única desde 1997, leída en el volcado a la
  fecha de corte. **La «seguridad informática» no aparece en el real decreto ni en su Guía
  Técnica.** La opción está bien transcrita y la plantilla —**96 números y 96 letras
  alineados**— da **b**.
- **Qué se ha hecho**: **nada en el tema**. Con el tema delante se acierta igualmente, porque la
  norma nombra **seguridad Y salud** y **b) es la única opción que nombra las dos**; la a), «para
  la salud», es incompleta. Incorporar la «seguridad informática» como riesgo de las pantallas
  sería inventar.
- **Gravedad**: menor. Se acierta, pero por una razón distinta de la que el enunciado sugiere.
- **AVISADO el 2026-09-02**, al meter el tema de prevención en los tres volúmenes específicos.
  Seguía sin tocarse el tema —la «seguridad informática» no se inventa—, pero **el aviso ya se
  imprime** junto a la respuesta, en `AVISOS_PRL` de `herramientas/libro.py`. Está escrito una
  sola vez y se mezcla en los tres bloques: **el tema es uno, y su aviso también**.

**b) El interruptor diferencial como protección contra contactos directos.**

- **Dónde**: tema de PRL del específico, rúbrica 4, epígrafe de riesgo eléctrico.
- **Qué dice hoy**: las definiciones del **anexo I del RD 614/2001** —**contacto directo**, con
  elementos en tensión; **contacto indirecto**, con masas puestas accidentalmente en tensión— y
  los umbrales del **RD 842/2002**. **No menciona el interruptor diferencial.**
- **Qué dice el examen**: `52_preguntas_luminotecnia nº 28` da por buena **a) «Sistema de
  protección contra contactos directos»**.
- **Fuente**: **no comprobada en una norma que nombre el diferencial**. El RD 614/2001 no lo
  cita; la reglamentación electrotécnica lo trata como protección frente a **contactos
  indirectos**, y la alta sensibilidad como **protección adicional** frente a los directos.
- **Qué se ha hecho**: **no se incorpora al tema**. La pregunta viene del cuadernillo de
  **Luminotecnia**, ocupación que no preparamos, y afirmarla exigiría una fuente que sostenga lo
  que dice.
- **Gravedad**: menor mientras no caiga en las tres ocupaciones que preparamos. Si cayera, hay
  que buscar la fuente antes de escribir nada.

- **RESUELTO el 2026-08-30, y en contra de esta misma anotación.** La fuente existe y estaba
  a un nivel más abajo del que se miró: la **ITC-BT-24 del RD 842/2002**, «Instalaciones
  interiores o receptoras. Protección contra los contactos directos e indirectos», **coloca el
  diferencial en los dos capítulos**. Su apartado **3.5** está **dentro del capítulo 3,
  «PROTECCIÓN CONTRA CONTACTOS DIRECTOS»**, y dice: «*Esta medida de protección está destinada
  solamente a **complementar** otras medidas de protección **contra los contactos directos**. El
  empleo de dispositivos de corriente diferencial-residual, cuyo valor de corriente diferencial
  asignada de funcionamiento sea **inferior o igual a 30 mA**, se reconoce como medida de
  protección complementaria en caso de fallo de otra medida de protección contra los contactos
  directos o en caso de imprudencia de los usuarios*». Y aparece otra vez en el apartado **4.1**,
  «Protección por corte automático de la alimentación», que es **protección contra contactos
  indirectos**.
  **La plantilla oficial no estaba equivocada**: en la letra del reglamento, el diferencial es
  protección **complementaria** frente a contactos **directos**. **Aplicado en
  `temas/prl/prl-especifico.md`**, epígrafe 4.8, con las dos citas y el umbral de 30 mA; y el
  extracto guardado en `fuentes/corte-20221221/BOE-A-2002-18099.preceptos.md`.
  **La lección es la del apartado 5 del manual**: *el que detecta se equivoca*. Sospeché de la
  plantilla y la plantilla tenía razón; me faltaba bajar de la ley al reglamento y del
  reglamento a su instrucción técnica.

---

## Aplicados

### 2026-08-29 · Cuándo entró en vigor la modificación de la Ley 8/2009 por la Ley 13/2022

- **Dónde**: tema 4 del general, artículo 2.1 de la Ley 8/2009, y tema 7, disposición final
  cuarta de la Ley 13/2022.
- **Qué dice hoy**: el tema 4 recoge, entre los recursos de financiación de RTVE, la
  aportación de **los prestadores del servicio de intercambio de vídeos a través de
  plataforma**, que introdujo la Ley 13/2022.
- **La discordancia**: la **disposición final novena de la Ley 13/2022** dice que **«la
  disposición final cuarta entrará en vigor en el ejercicio 2023»**, es decir **después** de
  la fecha de corte. Pero el **texto consolidado de la Ley 8/2009 que publica el propio BOE**
  data la nueva redacción del artículo 2.1 **desde el 9 de julio de 2022**, atribuyéndola a
  la Ley 13/2022. Dos fuentes oficiales, dos fechas.
- **Qué debería decir**: probablemente lo que dice —la lectura razonable es que el BOE
  consolida **el texto** con la regla general y reserva a 2023 los **efectos económicos** de
  la aportación—, pero **no está comprobado**. Si aparece una resolución o nota del BOE que
  lo aclare, se cita.
- **Fuente**: DF novena de `BOE-A-2022-11311`, leída literal; y el volcado de
  `BOE-A-2009-13988` a 21/12/2022, que marca la redacción como vigente desde 20220709.
- **Gravedad**: menor para el examen —ninguna pregunta del banco depende de la fecha—, pero
  afecta a qué redacción del artículo 2 de la Ley 8/2009 es la examinable.
- **RESUELTO el 2026-08-30.** **La discordancia sigue existiendo entre las dos fuentes
  oficiales, pero ya no decide nada**, porque **el tribunal examinó la redacción reformada**:
  las preguntas **54 de Producción** y **88 de Producción (Asistencia)** de octubre de 2024
  citan el **artículo 6** de la Ley 8/2009 nombrando a **«los prestadores del servicio de
  intercambio de vídeos a través de plataforma»**, que es literalmente lo que introdujo la
  disposición final cuarta de la Ley 13/2022. Comprobado además que el **texto consolidado de
  la Ley 8/2009 no lleva ninguna nota de «téngase en cuenta»** sobre el aplazamiento: el BOE
  data los artículos 2 y 6 desde el **09/07/2022** sin salvedad. **Aplicado en `temas/general/04-ley-8-2009.md`**,
  con la discordancia explicada y el argumento del examen.
  **Corrección de lo que esta misma entrada decía**: la gravedad estaba mal fijada. Se anotó
  «ninguna pregunta del banco depende de la fecha» y **sí dependen dos**.

### 2026-08-29 · Fecha final de la aplicación del artículo 155 en Cataluña

- **Dónde**: tema 1 del general, epígrafe 10.3, nota sobre el artículo 155.
- **Qué dice hoy**: que la plantilla oficial del examen de Información y
  Contenidos de 2024 da como período «del 27 de octubre de 2017 al 2 de junio de
  2018», y que la fecha final se recoge por la plantilla y no por fuente oficial.
- **Qué debería decir**: lo mismo, más la referencia del BOE que publique el cese
  de las medidas, si existe.
- **Fuente**: el inicio sí está verificado —Resolución de 27 de octubre de 2017 de
  la Presidencia del Senado, `BOE-A-2017-12327`, y Reales Decretos 942/2017 a
  945/2017—. **La fecha de cese no se ha comprobado**: se buscó en los sumarios
  del BOE de 1, 2, 4 y 5 de junio de 2018 y no aparece.
- **Gravedad**: menor. El dato se da atribuido a la plantilla, no como afirmación
  propia.
- **RESUELTO el 2026-08-30.** **No hay publicación en el BOE porque no puede haberla**, y ésa
  era la pregunta de verdad. La mecánica, comprobada en tres fuentes:
  - Cada real decreto de ejecución dispone que **«mantendrá su vigencia en tanto continúe en
    vigor el Acuerdo del Pleno del Senado de 27 de octubre de 2017»** (RD 944/2017, disposición
    final, leída en `BOE-A-2017-12329`).
  - El Acuerdo del Senado dedica su **apartado E.9, «Duración y revisión de las medidas»**, a
    prever **«la posibilidad de plantear modificaciones o actualizaciones de las medidas, así
    como de anticipar su cese si cesasen las causas que lo motivan»**. **No fija fecha de
    terminación.**
  - El cese se produjo **con la toma de posesión del nuevo Govern**, que se publica en el
    **DOGC**, no en el BOE.
  - Y la fecha tiene ahora **fuente oficial de la Generalitat**: la *Revista Catalana de Dret
    Públic* de la **Escola d'Administració Pública de Catalunya** dice **«Entre els dies 27
    d'octubre de 2017 i 2 de juny de 2018 es va aplicar l'anomenat mecanisme de coerció federal
    de l'article 155»** y precisa que **«l'aplicació de l'article 155 CE acabava quan el nou
    Govern de Catalunya prengués possessió»**.
  **Aplicado en `temas/general/01-constitucion-espanola.md`**: la fecha ya no se recoge «por la
  plantilla», y el tema explica por qué buscarla en el BOE no da nada.

### 2026-08-29 · Número total de Senadores en cada legislatura

- **Dónde**: tema 1 del general, epígrafe 5.1, artículo 69.
- **Qué dice hoy**: que la Constitución no fija el número total y que depende de
  las designaciones autonómicas, sin dar cifra.
- **Qué debería decir**: lo mismo, y añadir la cifra vigente en la legislatura en
  curso cuando se pueda citar de fuente oficial (Senado o Junta Electoral
  Central). En el examen de Información y Contenidos de 2024 la plantilla da
  **266**.
- **Fuente**: **no comprobada**. El artículo 69 sí está verificado; la cifra
  concreta, no.
- **Gravedad**: menor, y además es dato de actualidad, que solo cuenta en
  Información y Contenidos.
- **RESUELTO el 2026-08-30.** La cifra tiene fuente oficial: **el propio Senado**, en
  «Composición del Senado», da **266 senadores en la XV legislatura** —la que estaba en curso
  en los exámenes de 2024—, de los que **208 son elegidos** y **58 designados** por los
  parlamentos autonómicos. Comprobada la suma con el reparto que publica: Andalucía 9,
  Cataluña 8, Madrid 7, Comunitat Valenciana 6, Canarias, Castilla-La Mancha, Castilla y León,
  Galicia y País Vasco 3, Aragón, Asturias, Extremadura, Illes Balears y Murcia 2, y Cantabria,
  La Rioja y Navarra 1 → **58**. **La plantilla del examen acertaba.**
  **Aplicado en `temas/general/01-constitucion-espanola.md`**, artículo 69.


---

## Abiertos (reabierto el 2026-08-30)

_**Cerrado el mismo día.** El único pendiente que quedaba, el de las tres plantillas
ilegibles, se resolvió leyéndolas celda a celda. **No queda ninguno abierto.**_

### 2026-08-30 · Tres plantillas oficiales que el OCR no sabe leer entera — RESUELTO

- **Dónde**: `convocatoria/examenes/16_plantilla_de_respuestas_gestion.pdf`,
  `18_plantilla_de_respuestas_gestion_abogado_a.pdf` y
  `26_plantilla_de_respuestas_iluminacion.pdf`.
- **Qué pasa**: los tres PDF llevan la fuente incrustada **sin tabla de caracteres**, igual
  que sus cuadernillos. Los cuadernillos se han recuperado rasterizando y pasando Tesseract;
  **las plantillas no**. Son tablas de dos columnas —número y letra—: Tesseract lee bien la
  primera página (`1 C`, `2 a`, `3 b`…) y **a partir de la segunda devuelve solo la columna de
  números**. Probados los modos de segmentación 3, 4, 6, 11 y 12; ninguno recupera las letras.
  Y lo poco que lee trae números mal leídos: el **5 sale como `9`**.
- **Qué se ha hecho**: **no guardar ese OCR**. Una plantilla leída a medias desplaza las
  respuestas sin avisar —es el mismo fallo que obligó a reescribir `plantilla()`— y es peor que
  no tener ninguna. Las **67 preguntas** de esos tres cuadernillos entran en el banco marcadas
  como **«sin plantilla»**, y el volumen imprimible lo explica en el apéndice de respuestas.
- **Qué faltaría**: recortar la página por columnas **antes** de pasarle Tesseract, y validar
  el resultado contra el número de preguntas del cuadernillo antes de darlo por bueno.
- **Gravedad**: menor. No hay ningún dato equivocado en el banco; hay 65 preguntas cuya
  respuesta oficial no se puede citar. El enunciado sí está, y con el tema delante se contestan.
- **RESUELTO el 2026-08-30**, y por donde no se había mirado: **el problema no era el
  lector, era la unidad de lectura**. Dando la hoja entera, ningún modo de segmentación
  saca la columna de letras. Leyendo **celda a celda** sale entera, y con tres apoyos que
  no requieren adivinar nada: la **geometría exacta** la dan los bordes de la tabla, que en
  el PDF son dibujos vectoriales; los **códigos de la fuente** ya distinguen las cuatro
  letras, aunque no sepan nombrarlas —y son consistentes **por página**, no por documento,
  porque cada página incrusta la suya—; y al OCR solo le queda **decir cuál es cuál**, por
  mayoría de varias celdas.
  **Contrastado por fuera**: **50 de 50** contra las dos primeras páginas de la plantilla de
  Iluminación leídas a ojo, y las **dos preguntas repetidas** en cuadernillos de plantilla
  legible dan la misma respuesta aunque las opciones vayan en distinto orden.
  Aplicado en `herramientas/plantilla_ocr.py`. **Las 505 preguntas del banco tienen ahora
  su respuesta oficial.**
  **La lección**: se dio por agotado un camino tras probar cuatro modos del mismo lector,
  cuando lo que había que cambiar no era el modo sino **qué se le daba a leer**.

---

## Cuatro siglas sin presentar en el tema 7 del bloque general — cerrado el 2026-09-02

- **Detectado el 2026-09-02**, al corregir la lente de prosa. Buscaba la primera aparición de
  cada sigla **como trozo y no como palabra**, de modo que la encontraba dentro de otra
  —«SI» dentro de «MÚSICA», «RD» dentro de «BORDER»— y comprobaba la presentación en un punto
  del tema donde la sigla no está. Corregida la lente con límites de palabra, **aparecieron
  avisos que antes quedaban tapados**.
- **Qué queda**: en `temas/general/07-ley-13-2022.md` hay **cuatro siglas realmente sin
  presentar** —la de la comisión que informa los reglamentos, la de la federación de fútbol, la
  de la copa femenina de tenis y la de la interfaz por la que se volcó la norma—. Los demás
  avisos de los otros temas son **falsos positivos**: palabras en mayúsculas usadas como
  énfasis, y trozos de «CC.AA.» y «NO-DO».
- **Aplicado el 2026-09-02**, aprovechando que el volumen general **había que reimprimirlo de
  todos modos**: al repartir el bloque de Información y Contenidos volvieron dos preguntas al
  banco del III Convenio, y el general pasó de **479 a 481** preguntas. Desaparecida la razón
  para aplazarlo, se aplicó:
  - **CNMC**: la ley **nunca usa la sigla** —escribe siempre «Comisión Nacional de los Mercados
    y la Competencia»—, así que la sigla es del tema y se presenta en su primera aparición, la
    del artículo 54 de los contratos-programa.
  - **API**: «Volcada la norma entera desde la **interfaz de programación (API)** de legislación
    consolidada».
  - **RFEF** y **FED**: aquí no se podía presentar dentro de la frase, porque **las dos van
    dentro de la cita literal del artículo 146.3** —«Primera División femenina RFEF», «Copa
    Davis y Copa FED»— y **la ley no las desarrolla**. Se presentan **antes de la cita**, con esa
    advertencia: la de la Real Federación Española de Fútbol y la de la antigua Copa Federación
    de tenis. Meter el desarrollo dentro de las comillas habría sido reescribir la ley.
- **Regenerados los tres formatos** del volumen general en la misma pasada: 254 páginas.
- **Gravedad**: menor, y era menor. No había ningún dato equivocado; había cuatro siglas que el
  lector tenía que deducir del contexto.

---

## Una respuesta oficial que su fuente estadística no sostiene — abierto el 2026-09-02

- **Dónde**: banco `informacion-01`, pregunta 77 del cuadernillo `31_preguntas_iyc`, y el
  epígrafe de economía del tema 1 del específico de **Información y Contenidos**.
- **Qué dice la plantilla**: la tasa de paro del **segundo trimestre de 2024** fue **11,4 %**.
- **Qué dice la fuente**: el **INE**, en la nota de prensa de la **EPA del segundo trimestre de
  2024** —26 de julio de 2024—, publica **11,27 %**.
- **Qué se ha hecho**: se aplicó el apartado 5 del manual —*el que detecta se equivoca*— y la
  sospecha **no se sostuvo**. Es el trimestre correcto: la nota se titula «Encuesta de población
  activa (EPA). Segundo trimestre 2024». La cifra se comprueba sola: «**11,27 % este trimestre,
  1,02 puntos menos que en el anterior**», y 11,27 + 1,02 = 12,29, que es la tasa del primero. Y
  el enunciado **no dice de quién es la tasa**: en España, «la tasa de paro» de un trimestre es
  la de la EPA.
- **Qué queda pendiente**: encontrar **de dónde sale el 11,4 %**. Podría darlo una serie mensual
  desestacionalizada distinta de la EPA trimestral, pero **eso es una conjetura y no una
  fuente**, y como conjetura queda escrita. Mientras no aparezca esa serie, **esto no se anota
  como errata de plantilla**: se anota como discrepancia.
- **Decisión mientras tanto**: el tema **enseña el 11,27 % del INE** y deja dicho que la
  respuesta oficial es otra; el volumen lo avisa debajo de la tabla de respuestas. De las cuatro
  opciones, la de la plantilla sigue siendo la única cercana, así que **el opositor la marca
  igual**.
- **Gravedad**: induce a error si se estudia la cifra de memoria. **Es la primera vez en el
  proyecto que una fuente estadística, y no una norma, discute una respuesta oficial**: las tres
  erratas de plantilla anotadas más arriba son todas de derecho.

---

## La respuesta oficial que define un indicador por lo contrario de lo que es — abierto y cerrado el 2026-09-03

- **Dónde**: banco `gestion-19`, pregunta 32 del cuadernillo `15_preguntas_gestion`, y el epígrafe
  6 del tema 19 del específico de **Gestión**.
- **Qué dice la plantilla**: el indicador del resultado de explotación **«sin tener en cuenta
  justamente los intereses y los costes financieros»** es el **BAI**.
- **Qué dice la fuente**: el **modelo normal de cuenta de pérdidas y ganancias** del Plan General de
  Contabilidad —Real Decreto 1514/2007, tercera parte— construye ese escalón como
  **«A.3) RESULTADO ANTES DE IMPUESTOS (A.1+A.2)»**, donde **A.1)** es el **«RESULTADO DE
  EXPLOTACIÓN»** y **A.2)** el **«RESULTADO FINANCIERO (12+13+14+15+16)»**, cuya partida 13 es
  literalmente **«Gastos financieros»**. El BAI es, por definición del modelo, **el escalón
  inmediatamente posterior a restar los intereses**: es el único de las cuatro opciones que **sí**
  los computa.
- **Qué se ha hecho**: se aplicó el apartado 5 del manual —*el que detecta se equivoca*— y la
  sospecha **se sostuvo**, con la particularidad de que la refutación **no necesita doctrina**: la
  contradicción está dentro del propio modelo normalizado.
- **Cuál es la respuesta**: el nombre exacto de lo que el enunciado describe es **BAII**, o *EBIT*,
  y **no estaba entre las opciones**. De las cuatro ofrecidas, la única que se sitúa por encima de
  los intereses en la escalera de resultados es el **EBITDA**, la **b)**, y es la que hay que
  marcar. El *margen bruto* se queda por encima del resultado de explotación y *«Resultado Viable»*
  no existe.
- **Decisión**: el tema enseña la escalera completa y marca la pregunta; el volumen la avisa debajo
  de la tabla de respuestas.
- **Gravedad**: **cambia la respuesta**. Es la **octava errata de plantilla** del proyecto y la
  primera que se refuta con un **modelo normalizado de cuentas anuales** en lugar de con un
  artículo.

---

## Una pregunta cuyas cuatro opciones no responden a su enunciado — abierto y cerrado el 2026-09-03

- **Dónde**: banco `gestion-08`, pregunta 83 del cuadernillo `15_preguntas_gestion`, y el epígrafe
  de régimen disciplinario del tema 8 del específico de **Gestión**.
- **Qué pregunta**: el plazo de prescripción de las faltas **muy graves**.
- **Qué ofrecen sus opciones**: plazos referidos a la **publicación en el BOE**, ajenos al
  artículo 60 del Estatuto de los Trabajadores.
- **Qué dice la fuente**: **artículo 60.2 del Estatuto**, **sesenta días** desde que la empresa
  conoce la falta y **seis meses** desde que se cometió. Los **veinte días** de la respuesta oficial
  son el plazo de las faltas **graves**. Comprobado además en el **III Convenio Colectivo de la
  Corporación RTVE**, que dice lo mismo.
- **Qué se ha hecho para descartar un error propio**: se volvió a leer **la página del cuadernillo
  escaneado** por si la transcripción hubiera perdido texto. No lo había perdido: el enunciado es
  el que es.
- **Decisión**: no se marca como errata de plantilla sino como **enunciado roto**, que es distinto:
  aquí no hay una opción correcta que la plantilla haya errado; **no hay ninguna**. El tema lo dice
  y el volumen lo avisa.
- **Gravedad**: **cambia la respuesta**, y es incorregible marcando otra opción.

---

## Dos preguntas que examinan de una ley que su propio anexo no cita — abierto el 2026-09-03

- **Dónde**: cuadernillo `15_preguntas_gestion`, preguntas **nº 6** y **nº 89**.
- **Qué pasa**: las dos se contestan con la **Ley Orgánica 7/2021**, y el **Anexo 2 de Gestión no
  la cita en ninguno de sus treinta y un puntos**.
- **Por qué se anota y no se corrige**: **no es una errata**. Las dos preguntas tienen respuesta
  correcta y la plantilla la da bien. Lo que falla es la correspondencia entre el programa y el
  examen, que no es cosa del temario sino de quien lo redactó.
- **Qué se hace mientras tanto**: se deja constancia aquí y en el informe de cobertura del bloque.
  **No se amplía el temario con una ley que el anexo no manda estudiar**, porque eso sería
  sustituir al examinador; pero el opositor merece saber que ocurrió.
- **Gravedad**: menor para el temario, **relevante para quien se examine**. Es el tercer caso del
  proyecto en que el examen se sale de su propio programa.

---

## La respuesta oficial que llama sensorización a un montaje de croma — abierto y cerrado el 2026-09-03

- **Dónde**: banco `realizacion-16`, pregunta **46** del cuadernillo
  `60_preguntas_realizacion_asist`, y el epígrafe de escenografía virtual del tema 16 del
  específico de **Realización (Asistencia)**.
- **Qué pregunta**: qué tipo de **sensorización** corresponde al sistema **free-d**.
- **Qué responde la plantilla**: la **c)**, «unos postes de croma colocados en el techo, fuera de
  plano, para favorecer el movimiento escénico y evitar la inclusión de sombras».
- **Por qué está mal**: eso **no es una sensorización**, es un montaje de croma. **No mide la
  posición de la cámara**, que es lo que el enunciado pregunta. La que sí la describe es la **a)**,
  «sensores que permiten establecer la posición de la cámara mediante la lectura de pequeñas marcas
  de referencia».
- **Fuente**: la ficha del **Mo-Sys StarTracker Max**, guardada en `fuentes/fabricantes/`, documenta
  que el seguimiento se hace con «*ceiling, wall or floor mounted retro-reflective stickers*» y que
  «**FreeD**» es uno de los formatos en que esos datos se entregan al motor de representación; y que
  «Mo-Sys *invented 'simple-to-use' marker-based optical camera tracking*».
- **Límite declarado**: **la especificación del propio free-d no se ha podido consultar.** Lo que la
  ficha prueba es **la familia a la que pertenece**, no su articulado. **La conclusión no depende de
  esa especificación**: se sostiene por el contenido de la propia opción marcada, que no describe
  sensorización de ninguna clase.
- **Gravedad**: **cambia la respuesta.** Es la **novena errata de plantilla** del proyecto y la
  primera de materia técnica audiovisual: las ocho anteriores eran de derecho y de contabilidad.

---

## Una pregunta de contratación pública cuyas cuatro opciones contradicen la ley que cita — abierto y cerrado el 2026-09-03

- **Dónde**: banco `produccion-16`, pregunta **88** del cuadernillo `81_preguntas_produccion`, y el
  epígrafe de subcontratación del tema 16 del específico de **Producción**.
- **Qué pregunta**: cuál de cuatro afirmaciones sobre la subcontratación en los contratos públicos
  es correcta **según la Ley 9/2017**.
- **Qué responde la plantilla**: la **d)**, que hay que informar a la Administración **«solo cuando
  ésta supere el 30 % del importe total»** y que **«siempre»** hay que obtener **aprobación
  expresa**.
- **Por qué está mal, en sus dos mitades**:
  - **Artículo 215.2.b)**: «**En todo caso, el contratista deberá comunicar por escrito**, tras la
    adjudicación del contrato y, a más tardar, cuando inicie la ejecución de este, al órgano de
    contratación **la intención de celebrar los subcontratos**…». **No hay umbral.**
  - **Artículo 215.2.d)**: la autorización expresa se exige **sólo** «en los contratos de carácter
    **secreto o reservado**, o en aquellos cuya ejecución deba ir acompañada de **medidas de
    seguridad especiales**…».
- **De dónde salen las cifras**: del **artículo 217.2**, que impone a **las Administraciones
  Públicas** —no al contratista— comprobar los pagos a subcontratistas «en los contratos de obras y
  en los contratos de servicios cuyo valor estimado **supere los 5 millones de euros** y en los que
  el importe de la subcontratación sea igual o superior al **30 por ciento** del precio del
  contrato». **La pregunta toma dos números de un artículo y los coloca en otro.**
- **Y las otras tres tampoco**: la a) inventa un requisito de carencia de medios que el 215.1 no
  exige; la b) inventa un límite general del 50 % —el único 50 % del artículo es **la penalidad**
  del 215.3.a)—; la c) inventa una prohibición por importe que la ley no establece.
- **Qué se ha hecho para descartar un error propio**: se volcaron los **tres artículos enteros** del
  texto consolidado del BOE en su redacción vigente al 21/12/2022 y se comparó **frase por frase**
  con cada opción. **El conflicto no es de interpretación, es de literalidad**: «en todo caso» y
  «sólo cuando supere el 30 %» no pueden ser la misma regla.
- **Decisión**: se marca como **enunciado roto**, no como errata con respuesta alternativa: **no hay
  ninguna opción correcta**. El tema manda **marcar la d)** en un examen, que es la de la plantilla,
  **sabiendo que se marca por la plantilla y no por la ley**, y escribe al lado la regla verdadera.
- **Gravedad**: **cambia la respuesta**, y es incorregible marcando otra opción. Es la **décima
  errata de plantilla** del proyecto y la segunda de la clase «no hay respuesta correcta».

---

## Una respuesta oficial que sobra en una palabra — abierto y cerrado el 2026-09-03

- **Dónde**: banco `produccion-16`, pregunta **75** del cuadernillo `81_preguntas_produccion`, y el
  epígrafe del mapa de la protección de datos del tema 16 del específico de **Producción**.
- **Qué pregunta**: cuál de cuatro afirmaciones sobre la Ley de Protección de Datos es correcta.
- **Qué responde la plantilla**: la **c)**, que la ley «garantiza que los datos personales **solo**
  se recojan con el consentimiento explícito e informado del titular».
- **Por qué su enunciado no se sostiene**: el **artículo 6 del Reglamento (UE) 2016/679** prevé
  **seis bases de licitud** —consentimiento, ejecución de un contrato, obligación legal, intereses
  vitales, misión de interés público e interés legítimo—, y el consentimiento es una de ellas. La
  propia **Ley Orgánica 3/2018** lo presupone: su **artículo 72.1.b)** tipifica el tratamiento «sin
  que concurra **alguna de** las condiciones de licitud del tratamiento establecidas en el artículo
  6». **Si el consentimiento fuera la única base, ese artículo no diría «alguna de».**
- **Por qué NO se marca como errata**: **las otras tres opciones son falsas de plano** —la necesidad
  económica no es base de licitud, la ley no prohíbe recopilar datos, y la mayoría de edad no
  levanta ninguna obligación—. **Hay respuesta, y está mal escrita**: es distinto de la 88, donde no
  hay ninguna.
- **Qué hace el temario**: manda **marcar la c)** y explica **qué palabra sobra de su enunciado**,
  que es la que distingue estudiar de memorizar.
- **Gravedad**: **induce a error** en el estudio, no en el examen. Quien memorice la opción tal como
  está escrita aprenderá mal el régimen de bases de licitud, que es materia de tres preguntas de
  este mismo bloque.
