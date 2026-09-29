# Realizador/a (puesto 33) · Investigación del bloque B-control-directo (temas 4, 6, 9, 11, 12, 18)

Fase 1. Fecha de trabajo: 24-09-2026 (fecha del encargo); las fuentes web se descargaron y leyeron el
29-09-2026 (fecha del sistema), y así se declara al lado de cada una. Sólo lo que falta sobre lo
reutilizable ya localizado (RTVE y temas cerrados de Canal Sur); el redactor copia esos ficheros
aparte. Aquí van los huecos, con la fuente y la cita literal pegadas. Traducción entre paréntesis,
en redonda.

Además de lo que el encargo da como reutilizable, hay en el repositorio **pasajes ya cerrados y
verificados** de otros puestos de Canal Sur que cubren huecos de este bloque (se señalan en cada
tema con su ruta; son del común de Canal Sur o de puesto anterior, copiables literal):

- `temas/canal-sur-especificos/34-redactor-a/09-presentacion-locucion-comunicacion-oral.md`, § 6 «Uso del prompter» (Autocue) y § 7 «Comunicación con control».
- `temas/canal-sur-especificos/08-camara-operador/02-lenguaje-visual.md`, pasaje de la EBU R 95 v1.1 (zonas seguras de acción 3,5 % y de grafismo 5 %).
- `temas/canal-sur-especificos/08-camara-operador/04-soportes-y-accesorios.md` (el teleprompter cambia el equilibrio de la columna).

---

## Tema 4 · Organización del control de realización

Falta sobre RTVE: **prompter** e **iluminación del control** (sólo mencionados en RTVE).

### 4.1 Prompter (documentación del fabricante Autocue)

Fuente: Autocue, *Prompting A-Z: An Introduction To Prompting*, https://www.autocue.com/education/prompting-101/ (leída el 29-09-2026). Glosario del fabricante, no norma.

- **«Beamsplitter — The glass that sits at the front of a teleprompter. Also known as a mirror or teleprompter glass. The beamsplitter reflects the text from the monitor for the presenter to read, while using a special coating that allows a percentage of light through to the camera without the text being visible. At Autocue we use broadcast standard 70:30 glass that produces a clear mirror image and allows optimal light to the camera.»** (el cristal divisor refleja el texto del monitor hacia el presentador y deja pasar parte de la luz a la cámara; Autocue usa cristal 70:30). Ojo: «broadcast standard 70:30» es expresión del fabricante; no se ha localizado norma que lo fije.
- Autocue, *How a prompter works*, https://www.autocue.com/education/tutorials/how-a-prompter-works/ (29-09-2026): **«Autocue beamsplitters let 70% of the light to pass through the glass and reflect 30% back to the presenter.»** y **«Remember when you reflect a video in a beamsplitter it needs to be inverted – flipped – in the monitor, so it appears the right way round for the reader.»** (la imagen se invierte en el monitor para que se lea al derecho en el reflejo).
- **«Blank screen — This function enables you to remove the script from the teleprompter screen at the touch of a button. Usually used to hide the script when a camera pans around a studio.»**
- **«Cue marker — A marker on the edge of the prompt output, guiding the presenter’s eye to the optimum reading position (…) We recommend positioning the cue marker around 1/4 down from the top»** (marca de lectura, a un cuarto desde arriba, recomendación del fabricante).
- **«Foot controller — A foot pedal used to control the speed and position of the script. Often found under news desks for presenters to use to operate their own script.»**
- **«Hand controller — Used to control the speed and position of the script. Dedicated prompt operators usually use wired controllers with a scroll wheel to easily adapt to the speed of the reader. Wireless remote controllers can be used by presenters to operate their own script.»**
- **«Newsroom / Newsroom Computer System / NRCS / NCS — A broadcast system for news production. The NRCS manages the journalists’ content and outputs a run order to the prompting software.»** (la redacción digital manda la escaleta al software del prompter: enlace con servidores/automatización del control).
- **«Drop — A prompting software term, used to describe dropping a story to the end of the run order – eg. when more time is needed for breaking news»**; **«Cloak / Uncloak — When you cloak a story in the run order it hides the story from the prompt output.»** (útil para tema 6: cambios de escaleta en directo).
- **«Slugline — A story title that is visible on the prompt output but not read by the presenter.»**
- **«Talent feedback monitor — A monitor used to show the programme output to the presenter. These are often fitted below the teleprompter monitor to help the presenter maintain a good eyeline with the camera.»**
- **«Tally light — A light added to a teleprompter to show which camera is live. This mirrors the camera tally which is obscured by the prompter hood.»** (el tally del prompter repite el de la cámara, que la capucha tapa).
- **«Top — (…) Pressing the top button on a controller will automatically return the prompt output to the start of the script.»**

Quién opera el prompter en la RTVA (operador propio, presentador con pedal, ayudante): **no consta en documento publicado leído**. No afirmar.

### 4.2 Iluminación desde el control: la mesa y el DMX512

Fuente: ANSI E1.11-2024, *Entertainment Technology—USITT DMX512-A—Asynchronous Serial Digital Data Transmission Standard for Controlling Lighting Equipment and Accessories*, ESTA, aprobada por el ANSI Board of Standards Review el 25-04-2024, https://tsp.esta.org/tsp/documents/docs/ANSI%20E1.11%20-%202024.pdf (descargada y leída el 29-09-2026).

- Portada: **«Approved by the ANSI Board of Standards Review on 25 April 2024»**. Es la redacción vigente (la 2008 R2018 queda sustituida).
- 1.1 Scope: **«This Standard describes a method of digital data transmission between controllers and controlled equipment (…) and accessories, including dimmers. It covers electrical characteristics, data format, data protocol, and connector types.»** y **«Cable requirements and premises wiring are not within the scope of this Standard.»**
- 1.2: **«The media is driven using ANSI/TIA/EIA-485A-1998 (…) balanced data transmission techniques. Physical connection at devices is via 5-pin XLR connectors or by “hard-wiring” to terminals.»**; **«Data on the primary data link is sent in packets of up to 513 slots. The first slot is a START Code, which defines the information in the subsequent slots in the packet.»**
- 3.36: **«A single Universe contains a maximum of 513 Slots, starting at slot 0. Slot 0 is the START Code. Slots 1 through 512 are data slots.»**
- 3.45: **«Universe: a DMX512 data link originating from a single DMX512 source. Control of up to 512 DMX512 data slots comprises a single universe.»**
- 8.6: **«Each data link shall support up to 512 data slots. Multiple links shall be used where larger numbers of slots are required.»**
- 1.3: **«This is not intended to support a venue wide network that can carry data for lighting, sound, and scenery mechanization, for example, all on the same wire.»**
- Velocidad: la tabla de temporización da **250 kbit/s** (valor en la tabla del apartado de temporización; la extracción la parte en líneas, no se cita como frase literal).

Ya en el repositorio (tema técnico RTVE): DMX512 citado en `temas/realizacion/08-la-iluminacion.md` e `temas/ing-tec-teleco/08-equipamiento-de-television.md` («Protocolo más extendido para iluminación: DMX512»). Dónde se sitúa la mesa de luces en los controles de Canal Sur (dentro del control de realización o en sala aparte): **no consta**.

### 4.3 Qué hay en un control de realización y cómo se intercomunica: el título oficial de FP (norma estatal)

Fuente: Real Decreto 1680/2011, de 18 de noviembre, por el que se establece el título de Técnico Superior en Realización de proyectos audiovisuales y espectáculos y se fijan sus enseñanzas mínimas (BOE núm. 302, de 16-XII-2011, BOE-A-2011-19599), texto del diario oficial en https://www.boe.es/diario_boe/txt.php?id=BOE-A-2011-19599 (leído el 29-09-2026). No está en consolidado (`boe.py` da 404). **Vigencia comprobada** en «Referencias posteriores» de la ficha BOE: lo modifica el **Real Decreto 500/2024, de 21 de mayo** (BOE-A-2024-10685), que **«se suprimen los siguientes módulos profesionales: Formación y Orientación Laboral, Empresa e iniciativa emprendedora y Formación en centros de trabajo»** (art. 7.Uno.a) y añade el anexo III de profesorado; y el RD 1085/2020 deroga un anexo. **Los módulos 0905 y 0910 que se citan abajo no los toca el RD 500/2024** (comprobado en su texto: sólo aparecen en la tabla de profesorado). No citar la duración en horas (el RD 500/2024 trae una tabla de adaptación horaria; no se ha comprobado la de estos módulos). Es norma educativa: describe lo que se enseña al técnico, no la organización de la RTVA. Útil porque da, con rango de norma, la lista de equipos y puestos del control.

- Módulo 0910 «Medios técnicos audiovisuales y escénicos», resultado 4: **«Determina la configuración de medios técnicos del control de realización, adecuándola a diversas estrategias multicámara en programas de televisión y justificando sus características funcionales y operativas.»** Criterios:
  - a) **«Se ha justificado el diagrama de equipos y conexiones del control de realización y el plató de televisión, de unidades móviles y del control de continuidad.»**
  - b) **«Se han evaluado las características de diversos mezcladores de vídeo y sus capacidades en cuanto a operaciones de selección de líneas de entrada, sincronización, buses primarios y auxiliares, transiciones, incrustaciones, DSK y efectos digitales.»**
  - c) **«Se han definido las necesidades de líneas de entrada a la mesa de audio y los envíos de esta hacia diferentes destinos en control y estudio, en diversos programas televisivos.»**
  - d) **«Se ha diseñado el esquema de intercomunicación entre los puestos de realización, cámaras, regiduría, mesa de audio, reproducción y grabación de vídeo, control de cámaras, control de iluminación, grafismo y conexiones exteriores.»** ← la mejor enumeración normativa de los puestos del control (tema 4, «comunicaciones»).
  - e) **«Se ha justificado la elección de soportes y formatos de registro de vídeo y audio, y de tecnologías del tipo audio sigue vídeo y vídeo y audio embebido.»**
  - f) **«Se han evaluado las especificaciones de las cámaras y de sus unidades de control, y se han justificado las operaciones de ajuste de imagen en diversos programas grabados y emisiones en directo.»**
  - g) **«Se han determinado las capacidades técnicas de sistemas de escenografía virtual y su vinculación con las cámaras y el mezclador de imagen.»**
- Mismo módulo, contenidos: **«Cualidades técnicas y operativas generales de mezcladores de vídeo, generadores de sincronismos, matrices o patch–pannel, preselectores de vídeo, cámaras y unidades de control de cámaras, reproductores y grabadores de vídeo, tituladoras, sistemas de autocúe y sistemas de escenografía virtual.»** (así, «autocúe» y «patch–pannel», con esa grafía en el BOE). Y, criterio 1.d: **«Se ha determinado la idoneidad de diversas configuraciones de mesas de luces y dimmers a proyectos televisivos, escénicos y de espectáculos, en función del material de iluminación involucrado y de las intenciones expresivas y dramáticas.»**
- Módulo 0905 «Procesos de realización en televisión», resultado 6: **«Realiza operaciones técnicas de apoyo a la realización, mediante la utilización de los equipos auxiliares ubicados en el control de realización del estudio de televisión, describiendo sus características funcionales y operativas.»** Criterios útiles: a) **«…las opciones de configuración de los equipos auxiliares, servidores y sistemas virtuales de redacción y edición que envían señales de vídeo y audio al control de realización.»**; b) **«Se ha determinado la configuración idónea de monitorizado en multipantalla, para la realización de un programa de televisión.»**; c) **«Se han prefijado los enrutamientos de señales de vídeo y audio en matrices de conmutación, switcher o preselectores hacia grabadores auxiliares y pantallas, según las características y requerimientos del programa.»**; d) **«Se han configurado las opciones gráficas y de almacenamiento de textos del titulador, comprobando que su señal se incrusta adecuadamente.»**
- Resultado 5, criterio b): **«Se han ajustado los parámetros de partida de las unidades de control de cámaras, equilibrando sus señales con la ayuda del monitor de imagen, el monitor de forma de onda, el vectorscopio y el rasterizador, siguiendo criterios expresivos y estéticos.»** (CCU).

### 4.4 Lo que no se pudo confirmar (tema 4)

- Disposición física, número y equipamiento de los controles de realización de Canal Sur (San Juan de Aznalfarache, Málaga, etc.): sin documento publicado leído.
- Marca de prompter, mezclador, CCU o grafismo que usa Canal Sur: sin documento publicado leído.
- Si la mesa de iluminación está en el control de realización o en sala propia: depende de la instalación; sólo oficio.

---

## Tema 6 · Realización multicámara en directo

Falta sobre RTVE y el tema 34-10: **órdenes del realizador** y **gestión de incidencias**.

### 6.1 Lo que la norma de FP dice que hace quien realiza en multicámara (RD 1680/2011, módulo 0905)

Misma fuente y vigencia que en 4.3.

- Resultado 3: **«Realiza programas de televisión en multicámara, valorando la implicación de todos los recursos humanos y técnicos que intervienen en el proceso y dirigiendo sus actuaciones según los requerimientos del proyecto.»** Criterios:
  - a) **«Se ha establecido un sistema para garantizar la coordinación de todos los intervinientes en la realización de un programa en multicámara grabado o emitido en directo: informadores, presentadores, equipos de realización, cámaras, sonido, iluminación, caracterización, escenografía, personal artístico y otros.»**
  - b) **«Se han previsto y evitado los enfilamientos no deseados en los segundos términos de la composición de todos los encuadres que componen el programa.»**
  - c) **«Se ha previsto y evitado la irrupción de cámaras y elementos impropios en todos los encuadres.»**
  - d) **«Se han identificado y evitado todos los elementos de escenografía, iluminación, vestuario, peluquería y maquillaje susceptibles de generar efectos indeseados en los encuadres.»** (prevención de errores)
  - e) **«Se han solicitado planos, encuadres y movimientos al equipo de cámaras, piezas de vídeo al equipo de vídeo, fuentes de audio al equipo de sonido y acciones a la asistencia a la realización en estudio, previniendo las solicitudes con suficiente antelación.»** ← base normativa de las **órdenes** y de la **anticipación** («preparado» antes de «entra»).
  - f) **«Se ha dirigido el equipo humano técnico y artístico, dando instrucciones para la consecución de los objetivos del programa, validando las tomas y ordenando las repeticiones en el caso de grabados.»**
  - g) **«Se han dado instrucciones para la grabación del programa o se ha informado de la entrada en emisión.»**
  - h) **«Se ha realizado el programa de televisión, seleccionando secuencialmente las diversas fuentes de imagen y de sonido que salen al aire para ser grabadas o emitidas.»**
- Resultado 2 (la asistencia en control, **llamadas**): b) **«Se ha informado con anticipación de la naturaleza del total o colas de cada pieza de vídeo y de la duración, pies y coleos reseñados en los minutados, relatando durante su reproducción el tiempo restante y advirtiendo sobre cambios de plano y congelados finales.»**; a) **«Se ha informado con anticipación sobre la fuente de procedencia y número de las sucesivas piezas de vídeo, interpretando correctamente la escaleta del programa.»**; e) **«Se ha gestionado el sistema de grabación y reproducción de repeticiones en retransmisiones deportivas.»**
- Resultado 1.f (señales que se graban, útil para incidencias): **«Se han determinado las señales de la realización televisiva que van a ser grabadas: master, señal sin incrustaciones y cámaras dobladas o masterizadas.»**
- Resultado 4 (plató, ensayos): d) **«Se ha establecido un procedimiento de coordinación de los distintos equipos técnicos que operan en el estudio, para implementar la fluidez de la grabación del programa o la emisión en directo.»**; e) **«Se han determinado las instrucciones de asistencia a la realización en estudio que hay que comunicar a los equipos de cámara, sonido, iluminación y efectos especiales durante la realización del programa.»**; f) **«Se ha establecido un sistema para la comprobación de las ubicaciones de las cámaras y sus movimientos, así como los tiempos de desplazamiento entre sets y su viabilidad.»**
- Contenidos del módulo: **«Comunicación y órdenes en el control de realización.»**, **«Técnicas de montaje en vivo en la realización televisiva.»**, **«Métodos de anticipación de vídeos en la asistencia a la realización en control.»**
- Módulo 0904 «Planificación de la realización en televisión» (contenidos): **«Comunicaciones y órdenes para la continuidad en emisiones de televisión.»**

### 6.2 Órdenes: vocabulario

No se ha localizado **ningún documento publicado (norma, manual universitario accesible o fabricante) con el repertorio de órdenes del realizador en español** («preparado/a cámara 2», «entra 2», «fuera rótulo», «dentro vídeo», cuenta atrás). Ya en el repositorio, como costumbre de oficio o material RTVE: `temas/realizacion/13-la-asistencia-en-grabacion.md` (tabla «Cantar el guion»: «entra vídeo», «cámara 3 preparada», «rótulo en cinco») y `temas/realizacion/17-la-asistencia-en-plato-regiduria.md` (código de señas, cuenta atrás con los dedos, «cantar los tiempos»). Recomendación al redactor: exponer la **estructura aviso‑ejecución** con apoyo en el criterio 3.e del RD 1680/2011 («previniendo las solicitudes con suficiente antelación») y dar las fórmulas concretas como oficio. Se buscó en inglés (Austin Community College, *Set Commands*): es vocabulario de rodaje de cine («Roll Sound», «Speed», «Action», «Cut»), no de control de televisión; **no sirve**.

### 6.3 Incidencias y cambios de escaleta en directo: lo que añade el Libro de estilo de Canal Sur

Fuente: Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía, 1.ª ed., marzo de 2004 (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`, leído el 29-09-2026). Documento publicado de la casa, de 2004.

- 4.4.4 «Competencias» (pasos del Departamento de Producción), punto 4 (errores): **«Las situaciones similares previas, especialmente si no son habituales, han de revisarse para eludir errores o para soslayar las diﬁcultades que hubo y se resolvieron. Si hemos de cometer errores, al menos que no sean idénticos.»**
- Punto 6: **«…las propuestas e intercambios de información entre periodistas, técnicos y productores deben hacerse con ﬂuidez: nunca se formularán de viva voz, sino por un medio del que quede constancia, sobre todo en asuntos de envergadura. El acuerdo ﬁnal es obligatorio para todos.»**
- 8.1 «El periodista comunicador», punto 6: **«Los términos de cada aparición en directo deben ser pactados entre todos los profesionales involucrados: productor, cámara, técnicos de enlace, presentador en plató, equipo de edición, realizador... que deben estar al tanto de los detalles y asumir por completo los de su competencia. (…) Siempre se intentará plasmar todos los extremos en la escaleta.»**; punto 7: **«Identiﬁcar y conocer los riesgos en la preparación o en el transcurso de un directo y procurar soslayarlos para no incurrir en errores. La experiencia anterior es un método excelente para no repetirlos o para tratar de evitarlos.»** (el punto 6 ya está en 34-10, línea ~202: tomarlo de allí).
- 6.5.1: **«…cuando haya imperfecciones técnicas moderadas, la información —competencia del editor— tendrá preeminencia sobre la técnica —atribución del realizador—.»** (criterio para decidir ante un fallo: si se emite con defecto técnico moderado).
- 6.5.2: **«En la realización informativa, la urgencia acaba imponiéndose a cualquier otra consideración aunque no puede hacerlo hasta el punto de anular un aceptable nivel de calidad.»**

Estos pasajes del LE ya están copiados en temas cerrados (08-08, 30-09, 30-14, 34-03, 34-07, 32-03, 28-08: `grep` de «Si hemos de cometer» o «responsable máximo de la corrección»); el redactor puede copiarlos de allí.

### 6.4 Cambios de escaleta en el prompter (fabricante)

Autocue (4.1): **«Drop — (…) dropping a story to the end of the run order – eg. when more time is needed for breaking news»**; **«Cloak / Uncloak — When you cloak a story in the run order it hides the story from the prompt output.»**; **«Blank screen — (…) Usually used to hide the script when a camera pans around a studio.»**

### 6.5 Lo que no se pudo confirmar (tema 6)

- Protocolo escrito de incidencias en emisión de Canal Sur (a quién se avisa, negro de seguridad, carta de ajuste, «estamos teniendo problemas técnicos»): sin documento publicado leído.
- Repertorio normalizado de órdenes: no existe documento público localizado (6.2).

---

## Tema 9 · Mezclador y recursos de realización

Falta sobre RTVE: **criterios de uso narrativo**.

### 9.1 Ya cerrado y verificado en Canal Sur (copiable literal)

- `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/01-lenguaje-y-montaje-audiovisual.md`, tabla de transiciones (líneas ~368-371): fundido y encadenado con cita de F. J. Mateu Torres, *Fundamentos teóricos de la edición y el montaje audiovisual*, Editorial UMH, 2024 (manual universitario): **«es una transición empleada para acentuar el paso del tiempo —elipsis—…»**; **«"el fundido separa las secuencias, mientras que el encadenado y el corte las conectan"»**. Y la fila de «Informativo» (línea ~889: «El corte manda sobre el encadenado», oficio).
- `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`, § 6 «Transiciones» (Adobe y Blackmagic: **«Transitions (…) are often used to indicate a change in time or location when changing scenes.»**; tabla de transiciones corrientes con su uso, marcado como oficio).

### 9.2 La norma de FP pone los usos narrativos en el temario del realizador

RD 1680/2011, módulo 0905, contenidos: **«Realización de transiciones. Usos expresivos y narrativos.»**, **«Incrustación de la señal.»**, **«Gráficos en la realización de televisión.»**; resultado 5.e: **«Se han ajustado y prefijado en el mezclador las transiciones, cortinillas, efectos digitales e incrustaciones mediante croma, luminancia o DSK, que se utilizarán en el programa de televisión.»**; 5.c: **«Se han configurado las entradas de vídeo a los buses del mezclador, mediante la adecuada ordenación de cámaras, líneas de vídeo, señales exteriores, gráficos y otras.»**; 5.d: **«Se han configurado las salidas del mezclador y los destinos de las señales de programa, previo y auxiliares.»**

### 9.3 Criterio de la casa sobre efectos y croma (Libro de estilo, 2004)

- 3.10 (cierres de informativo): **«…el realizador puede arbitrar numerosas variantes estéticas (vidiwall, croma...).»**
- 6.5.2: **«La imagen y su manufacturación están siempre al servicio de la eﬁcacia, la accesibilidad y la claridad de la comunicación»**; y la mención de **«conexiones en directo, uso normalizado de satélites, presencia de otros centros de producción, infografías, ‘vidi wall’, pantallas de plasma... cuyo uso precisa cierto sentido estético y de una capacidad notable para aprovechar y armonizar los recursos disponibles.»**
- 8.6.1 (vestuario), puntos 4 y 9: **«Los colores fuertes tampoco son aconsejables. Se saturan e impregnan de ‘croma’ el cuello y el mentón.»**; **«Los departamentos de Estilismo y Realización deberán tener muy en cuenta los condicionantes técnicos de cromas, transparencias o bien de la grabación o emisión desde un plató con decorado virtual.»** (ya en `32-productor-a/07-produccion-de-programas-en-estudio.md`).

### 9.4 No confirmado (tema 9)

- Criterios escritos de Canal Sur sobre cortinillas/DVE en informativos: sólo lo citado del LE; el resto, oficio.
- Afirmación del tema RTVE 15 de que Vizrt es «el más extendido en televisión»: sin fuente en el tema; no copiar como dato.

---

## Tema 11 · Sonido para realización

Falta sobre RTVE y 28-08: **coordinación de microfonía** (breve en RTVE) y **sincronía imagen‑sonido** (lip sync).

### 11.1 Ya cerrado y verificado en Canal Sur (copiable literal)

- Coordinación de microfonía inalámbrica: `temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`, § «Coordinación de frecuencias» (qué es coordinar, una frecuencia por micrófono, banda/grupo/canal, separación mínima, intermodulación, procedimiento) y § «Durante el programa». Bandas legales en España y el límite de 694 MHz, también allí.
- Captación por formato y el reparto de canales en informativos: `28-operador-a-de-sonido/06-captacion-de-sonido.md`.
- Sincronía por reloj común (PTP, ST 2110): `28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`, § «Sincronía entre flujos y con la imagen».
- Quién manda en el control y cómo se pacta el directo con sonido: `28-08`, § «Coordinación con realización» (ya previsto por el encargo).

### 11.2 Sincronía labial: EBU R 37 (nuevo)

Fuente: EBU Recommendation R37-2007, *The relative timing of the sound and vision components of a television signal*, Ginebra, febrero de 2007, https://tech.ebu.ch/docs/r/r037.pdf (descargada y leída el 29-09-2026). Es la versión en la web de la EBU; no se ha encontrado revisión posterior.

- **«In television, a discrepancy between the instant at which an action is seen to take place and the instant at which the corresponding sound is heard can be subjectively disturbing.»**
- **«The value of the relative delay that is just perceptible depends on several factors, notably the programme content and the viewing distance. Experience suggests that particular care needs to be taken in HD production.»**
- Base de los valores: **«subjective tests of the relative delays at which failure of the synchronism between lip movements and speech becomes perceptible to 50% of observers»**.
- Recomendación: **«Member organisations should take action to minimise any differences (such as those that may exist within camera channels) in the relative timing of the sound and vision components of a television signal. Preferably, this should be applied by automatic correction techniques, at each point at which significant differences are apparent.»**
- Por etapa: **«The accuracy of A/V synchronisation at each stage should lie within the range of Audio 5 ms early (sound before picture) to 15 ms late (sound after picture).»**
- Medida: **«The flash consists of a peak white field for one full frame duration, and the blip consisting of a 1 kHz tone carried at alignment level for the same period.»**
- **«Throughout the programme chain, the audio and video data should be maintained coincident “on the tape” (or in the file or data stream) and not advanced or retarded to account for down-stream processing delays.»**
- Tabla 1, de extremo a extremo en la salida a emisión: **sonido adelantado ≤ 40 ms; sonido retrasado ≤ 60 ms** (**«Sound before picture ≤ 40 ms / Sound after picture ≤ 60 ms»**).
- Palabras clave de la propia R 37: **«Lipsync, AV Synchronization, Timing, Delay, Clapperboard, VT Clock, Slate»**.

Relación con la realización (oficio): el retardo de pantallas y de RA (tema RTVE 15 § 2 y 16 § 5) obliga a retrasar el audio para que no vaya por delante; la R 37 da el margen.

UIT: existe la Recomendación UIT-R BT.1359-1 (1998), *Relative timing of sound and vision for broadcasting* (https://www.itu.int/rec/R-REC-BT.1359-1-199811-I/en, sólo ficha vista); **no se ha leído su texto**: no citar valores de ella.

### 11.3 Coordinación de microfonía desde la realización (norma FP)

RD 1680/2011, módulo 0905, 3.e (ya citado): **«…fuentes de audio al equipo de sonido (…), previniendo las solicitudes con suficiente antelación.»**; contenidos: **«Dinámica del uso de los elementos sonoros en la realización de televisión.»**; módulo 0910, 4.c: **«Se han definido las necesidades de líneas de entrada a la mesa de audio y los envíos de esta hacia diferentes destinos en control y estudio, en diversos programas televisivos.»**. LE 8.6.1.2 (roce de tejidos): **«Telas brillantes, satenes y sedas producen brillo y reﬂejan color. El roce de estos tejidos produce además ruidos que los micrófonos registran.»**; 8.6.1.6: **«Los adornos exagerados (collares, pendientes, broches) (…) pueden producir ruidos extraños. Lo mismo puede ocurrir con bolígrafos o plumas estilográﬁcas.»**

---

## Tema 12 · Grafismo

Falta sobre RTVE: **elementos de continuidad visual** (poco) y lo propio de Canal Sur en rotulación.

### 12.1 Ya cerrado y verificado en Canal Sur (copiable literal)

- Zonas seguras EBU R 95 v1.1 (acción 3,5 %, grafismo 5 %): `08-camara-operador/02-lenguaje-visual.md` y `30-operador-a-montador-a-de-video/07-postproduccion.md` § 4 «Las zonas de seguridad».
- Rotulación en el LE (**«El rótulo que acompaña es también información. Reúne brevedad, impacto y síntesis.»**, 3.6.1; subtítulos resumidos en totales en lengua extranjera, 3.7.1; reglas de rotulación de fechas 13.8.1 y signos 13.1.1.3): `30-07` § 4 «Lo que pide el Libro de Estilo», `30-05`, `34-07`.

### 12.2 Plantillas de grafismo y aspecto uniforme (fabricante Vizrt)

Fuente: Vizrt, *Viz Pilot Edge User Guide* 3.5, «Introduction», https://docs.vizrt.com/viz-pilot-edge-guide/3.5/Introduction.html (leída el 29-09-2026).

- **«Viz Pilot Edge is a graphics creation tool designed for newsrooms to help journalists and producers to independently create and preview graphics using on-brand, show-aligned templates, making visual storytelling faster and easier.»** (plantillas con la marca y el estilo del programa: la continuidad visual se garantiza por plantilla).
- **«Template Builder is used by design teams to create customized templates via scene import from Viz Artist, supports scripting (Typescript), and live data integrations.»**
- Flujo: **«Fill templates with content and store them as data elements.»**, **«Move data elements into the newsroom rundown.»**, **«Scenes are made in Viz Artist and imported into Template Builder, where templates are made.»**, **«The template is saved in the Viz Pilot system and is available to newsroom and control room systems for playout.»**
- Reparto (lectura propia de lo anterior): diseño hace escenas y plantillas; redacción rellena; el control lanza. Enlaza con 30-13 (automatización, MOS).

### 12.3 Coherencia visual de la casa (Libro de estilo, 2004)

- 6.4 El raccord: **«…el ‘raccord’, esto es, la continuidad y uniformidad visual de los planos con sentido lógico.»** y punto 1 **«Técnico. No deben permitirse diferencias de color, brillo, contraste, tono, luz, altura de planos, calidad de la imagen...»** (edición; ya en temas 30).
- 7.4 (desconexiones territoriales): **«La continuidad del formato y el discurso son básicos para mantener la coherencia y evitar repeticiones.»** y **«Las desconexiones, como meta del trabajo informativo local, están obligadas a aplicar un criterio de coherencia estética y conceptual con la edición general en la que se integran y de la que son tributarias.»** ← el único texto publicado de la casa que exige coherencia estética entre emisiones (útil para «elementos de continuidad visual»).
- 6.5: **«Los informativos de CSTV y Canal 2 Andalucía tendrán siempre un marco periodístico, técnico y formal uniforme aunque cada realizador debe implicarse en su desarrollo y puede, y debe, aportar ideas propias y soluciones como responsable del producto audiovisual.»**

### 12.4 Norma FP (grafismo y continuidad)

RD 1680/2011, módulo 0904, contenidos: **«Determinación del material de grafismo en programas de televisión.»**, **«Escenografía virtual.»**, **«Los elementos de puntuación en la continuidad de televisión.»**; módulo 0905, contenidos: **«Gestión, ajustes previos y lanzamiento de rótulos en la realización de televisión.»**, **«Técnicas de operación de tituladoras y aplicaciones de rotulación en el control de realización.»**; 6.e: **«Se han generado los rótulos y claquetas identificativas necesarias en el titulador, para la realización de un programa de televisión, gestionando su almacenamiento y controlando su salida hacia el mezclador de vídeo.»**; 4.b: **«Se han comprobado y fijado las características y posiciones de los elementos de atrezo y elementos móviles que puedan comprometer la continuidad visual en la realización del programa de televisión.»**

### 12.5 No confirmado (tema 12)

- Manual de identidad gráfica de Canal Sur (mosca, tipografías, colores, cortinillas): no publicado / no localizado.
- Sistema de grafismo que usa Canal Sur: sin documento publicado leído.

---

## Tema 18 · Seguridad, comunicación y coordinación bajo presión

Falta sobre 32-14 (que ya da estrés operativo con NTP 318 y 443, emergencias, evacuación, comunicación de incidencias): **la comunicación en el equipo** y **la coordinación técnico‑artística**.

### 18.1 Comunicación e información como prevención del estrés: NTP 438 (INSST)

Fuente: INSST, NTP 438, *Prevención del estrés: intervención sobre la organización*, redactores Félix Martín Daza y Clotilde Nogareda Cuixart, Centro Nacional de Condiciones de Trabajo; el PDF dice **«Año: 1995»** (WebFetch la fechó en 1998; manda el PDF). https://www.insst.es/documents/94886/326962/ntp_438.pdf (descargado y leído el 29-09-2026). Advertencia del propio PDF: **«Las NTP son guías de buenas prácticas. Sus indicaciones no son obligatorias salvo que estén recogidas en una disposición normativa vigente. A efectos de valorar la pertinencia de las recomendaciones contenidas en una NTP concreta es conveniente tener en cuenta su fecha de edición.»**

- **«El hecho de que no esté claramente definido qué se espera de un trabajador, que su papel sea confuso o que no exista una fluida comunicación es uno de los más importantes estresores, debido a que el trabajador, al no saber exactamente qué tiene que hacer, de qué manera, qué áreas son de su responsabilidad, se traduce en una sensación de incertidumbre y amenaza.»**
- Preguntas que plantea: **«¿se le mandan cosas contrapuestas o contradictorias?, ¿se le mandan distintas cosas al mismo tiempo?»** (aplicable a órdenes simultáneas en el control).
- **«Los problemas que se pueden dar por una deficiente información y comunicación, la ambigüedad y el conflicto de rol que de ello se derivan, son unos de los más potentes estresores.»**
- Variables a revisar: **«Precisión de las informaciones.»**, **«Coherencia entre ellas.»**, **«Coincidencia (hacía un mismo objetivo) de las decisiones tomadas a partir de las informaciones.»** (así, «hacía», en el PDF), **«Lenguaje adecuado al destinatario.»**, **«Frecuencia de comunicación adaptada a las necesidades.»**, **«Procedimientos adecuados de recogida, tratamiento y transmisión de la información.»**
- **«Un buen sistema de información debe permitir a cada uno captar precisamente lo que se espera de él (tareas u objetivos a cumplir) y conocer los resultados del trabajo realizado.»**
- Tipos: horizontal / vertical (descendente y ascendente). Descendente, objetivo: **«Coordinar a los miembros de una organización para conseguir sus objetivos.»**; **«La sencillez y la claridad del contenido facilita la asimilación del mensaje.»** Horizontal: **«Este tipo de comunicación hace posible la coordinación de actividades y la resolución de conflictos»**. Riesgo ascendente: **«…la inhibición de comunicación por parte de los subordinados, sobre todo, cuando la pirámide jerárquica es muy apuntada»**.
- Poder: la organización necesita **«del ejercicio del poder para unificar las posibles desviaciones a las normas que las conductas individuales pueden ocasionar y para dar rápida respuesta a situaciones imprevistas o no contempladas normativamente.»**

### 18.2 Barreras de la comunicación: NTP 685 (INSST, 2003)

Fuente: INSST, NTP 685, *La comunicación en las organizaciones*, redactores Jaime Llacuna Morera y Laura Pujol Franco, CNCT, **«Año: 2003»**, https://www.insst.es/documents/94886/7852705/ntp_685.pdf (29-09-2026). Misma advertencia sobre el valor de las NTP.

- **«…la principales barreras son las siguientes:»** (así en el PDF) Psicológicas: **«Emociones.»**, **«Valores.»**, **«Hábitos de conducta.»**, **«Percepciones.»**; Físicas: **«Ruidos.»**; Semántica: **«Símbolos (palabras, imágenes, acciones) con distintos significados.»**; Otros: **«Interrumpir.»**, **«Cambiar de tema.»**, **«Tangencializaciones.»**, **«No escuchar.»**, **«Interpretaciones.»**, **«Responder a una pregunta con otra pregunta.»**, **«Rotulaciones.»**
- Formal/informal: la formal **«Se origina en la estructura formal de la organización y fluye a través de los canales organizacionales.»**; **«Preferentemente toda la comunicación formal de la empresa debe efectuarse por escrito»** (cuadra con el LE 4.4.4, punto 6, citado en 6.3: «por un medio del que quede constancia»).
- Aplicación (oficio, no de la NTP): en el intercom, el ruido es barrera física; la jerga no compartida, semántica; interrumpir órdenes, «otros».

### 18.3 Coordinación técnico‑artística (norma FP y LE)

- RD 1680/2011, art. 5 (competencias profesionales, personales y sociales; no lo modifica el RD 500/2024, que toca los arts. 2, 10, 12 y 15), letra e): **«Coordinar y dirigir el trabajo del personal técnico y artístico durante los ensayos, registro, emisión, postproducción o representación escénica, asegurando la aplicación del plan de trabajo y reforzando la labor del director, del realizador audiovisual y del director del espectáculo o evento.»**; d) **«Coordinar la disponibilidad de los recursos técnicos, materiales y escénicos durante los ensayos, registro, emisión o representación escénica, asegurando la aplicación del plan de trabajo.»** Y el 0905 3.a (en 6.1).
- LE 6.5: **«La puesta en antena de un informativo diario exige un gran esfuerzo de coordinación y concentración de un equipo numeroso y heterogéneo vinculado por la tecnología.»**; 6.5.1 **«El realizador actúa por delegación en profesionales que asumen funciones concretas y criterios particulares en cada fase de elaboración de la noticia. (…) su función se ciñe a la coordinación y supervisión de la parte ﬁnal del mismo.»**; 6.5.2 **«Tiene capacidad y autoridad para tomar, en cualquier momento, decisiones concretas referentes al modo, la forma y el diseño del informativo, con la salvedad de que deberá ceñirse a criterios de producción y a la supremacía del sentido informativo.»** y **«El realizador también tiene la responsabilidad de la organización eﬁcaz de los recursos que permita la dotación técnica.»** (6.5 probablemente ya en 08-08 o 34-03: copiar de allí).

### 18.4 Seguridad

Todo en 32-14 (plató, cableado, iluminación, altura, público, emergencias, evacuación, riesgo grave e inminente, comunicación de incidencias al responsable preventivo). Nada que añadir.

### 18.5 No confirmado (tema 18)

- Protocolos internos de la RTVA de comunicación en emergencias durante una emisión (quién interrumpe, quién decide): sin documento publicado leído.
- Técnicas tipo «comunicación en bucle cerrado» (repetir la orden recibida): no se ha localizado fuente de broadcast; no incluir.

---

## Trazabilidad (fuentes leídas en esta fase)

| Fuente | Fecha de lectura | Temas |
|---|---|---|
| Autocue, *Prompting A-Z* y *How a prompter works* (web del fabricante) | 29-09-2026 | 4, 6 |
| ANSI E1.11-2024, USITT DMX512-A (ESTA, PDF) | 29-09-2026 | 4 |
| RD 1680/2011 (BOE-A-2011-19599, texto del diario) y ficha de referencias posteriores; RD 500/2024 (BOE-A-2024-10685), art. 7 y anexo XLI | 29-09-2026 | 4, 6, 9, 11, 12, 18 |
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), 3.6.1, 3.10, 4.4.4 (pts. 4 y 6), 6.4, 6.5, 7.4, 8.1 (pts. 6 y 7), 8.6.1 | 29-09-2026 | 6, 9, 11, 12, 18 |
| EBU R37-2007 (PDF) | 29-09-2026 | 11 |
| Vizrt, *Viz Pilot Edge User Guide* 3.5, Introduction | 29-09-2026 | 12 |
| INSST NTP 438 (año 1995 según PDF) y NTP 685 (2003) | 29-09-2026 | 18 |

Ficheros tocados: sólo este informe. Descargas de trabajo en el scratchpad (no en el repositorio).
