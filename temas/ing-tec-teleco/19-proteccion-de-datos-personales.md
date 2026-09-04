# Tema 19 del específico de Ingeniería Técnica · Telecomunicación · Protección de datos personales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 23 |
| **Sirve para** | **Ing. Técnica Telecomunicación** y **Ing. Superior Telecomunicación** |
| **Punto compartido con Ing. Superior** | **Este mismo enunciado es el punto 28 del anexo de Ingeniería Superior · Telecomunicación**, palabra por palabra, así que **el tema se comparte y sirve a las dos ocupaciones** |
| **Fuente** | **Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales**, y **Reglamento (UE) 2016/679** |
| **Identificador** | `BOE-A-2018-16673` · BOE núm. 294, de 06/12/2018 · y `DOUE-L-2016-80807` |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan **los apartados 1 a 3 del artículo 22** y **los apartados 2 y 3 del artículo 89** de la ley, y **el artículo 32.1** y **el 25.2** del reglamento |
| **Cero preguntas, y aun así** | **Este punto decide dónde se puede colgar una cámara, dónde no se puede poner un micrófono, cuánto se guarda una grabación y qué hay que meter en el pliego** |
| **Extensión** | **2.968 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la Ley Orgánica de Protección de Datos Personales y
garantía de los derechos digitales (**LOPDGDD**), que es la Ley Orgánica 3/2018; el Reglamento General
de Protección de Datos (**RGPD**), que es el Reglamento (UE) 2016/679; la Agencia Española de
Protección de Datos (**AEPD**); la evaluación de impacto relativa a la protección de datos (**EIPD**);
y el delegado de protección de datos (**DPD**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 23):
> «Ley orgánica 3/2018, de 5 de diciembre, de protección de datos personales y garantía de los
> derechos digitales (BOE núm. 294, de 06 de diciembre de 2018. Texto consolidado. Última
> modificación publicada el 27/05/2021)»

**Este tema sirve a DOS ocupaciones**: **el enunciado de arriba es también, palabra por palabra, el
punto 28 del anexo de Ingeniería Superior · Telecomunicación**, así que **el tema se comparte con
aquella ocupación**, como se comparte el de prevención de riesgos laborales. **Nada de lo que sigue
está escrito para una sola de las dos.**

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo**, y **el tema se
escribe igual, contra el programa.**

**Y aquí no se despacha con un resumen, porque este punto no es papeleo para un ingeniero de
instalaciones**: **es el que decide dónde se puede colgar una cámara, dónde no se puede poner un
micrófono, cuánto tiempo se guarda una grabación y qué hay que meter en el pliego antes de comprar el
sistema.** **Las cuatro cosas se resuelven con artículos concretos**, y **este tema los cita
literalmente.**

<!-- indice -->

## Índice

- [1. Qué norma es cuál](#1-qué-norma-es-cuál)
- [2. La seguridad del tratamiento: el artículo del ingeniero](#2-la-seguridad-del-tratamiento-el-artículo-del-ingeniero)
- [3. Protección desde el diseño y por defecto](#3-protección-desde-el-diseño-y-por-defecto)
- [4. Videovigilancia: el artículo 22](#4-videovigilancia-el-artículo-22)
- [5. Cámaras y micrófonos en el centro de trabajo: el artículo 89](#5-cámaras-y-micrófonos-en-el-centro-de-trabajo-el-artículo-89)
- [6. Los otros derechos digitales del título X](#6-los-otros-derechos-digitales-del-título-x)
- [7. Las dos setenta y dos horas, que no son la misma](#7-las-dos-setenta-y-dos-horas-que-no-son-la-misma)
- [8. Lo que el examen ha preguntado](#8-lo-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Qué norma es cuál

**El enunciado sólo nombra la ley española, pero la materia se reparte entre dos normas** y **el
reparto hay que tenerlo claro antes de nada:**

| Norma | Qué es | Qué hace |
|---|---|---|
| **Reglamento (UE) 2016/679** | **Un reglamento europeo**: se aplica directamente, sin trasponer | **Pone los principios, los derechos y las obligaciones generales** |
| **Ley Orgánica 3/2018** | **Una ley orgánica española** | **Adapta el reglamento**, ejerce los márgenes que éste deja y **añade el título X de derechos digitales** |

**La regla que ordena las dos**: **lo general está en el reglamento europeo y lo español está en la
ley orgánica.** **Cuando una pregunta cita un plazo, un principio o un derecho del interesado, mira
primero al reglamento**; **cuando cita videovigilancia, trabajo o derechos digitales, mira a la ley
orgánica.**

## 2. La seguridad del tratamiento: el artículo del ingeniero

**Éste es el artículo que un ingeniero de telecomunicación tiene que saberse**, porque **es el que
convierte la protección de datos en requisitos técnicos de un pliego.**

**Artículo 32**, apartado 1, del reglamento europeo:

> «**Teniendo en cuenta el estado de la técnica, los costes de aplicación, y la naturaleza, el alcance,
> el contexto y los fines del tratamiento, así como riesgos de probabilidad y gravedad variables para
> los derechos y libertades de las personas físicas, el responsable y el encargado del tratamiento
> aplicarán medidas técnicas y organizativas apropiadas para garantizar un nivel de seguridad adecuado
> al riesgo, que en su caso incluya, entre otros:
> a) la seudonimización y el cifrado de datos personales;
> b) la capacidad de garantizar la confidencialidad, integridad, disponibilidad y resiliencia
> permanentes de los sistemas y servicios de tratamiento;
> c) la capacidad de restaurar la disponibilidad y el acceso a los datos personales de forma rápida en
> caso de incidente físico o técnico;
> d) un proceso de verificación, evaluación y valoración regulares de la eficacia de las medidas
> técnicas y organizativas para garantizar la seguridad del tratamiento.**»
>
> — Reglamento (UE) 2016/679, artículo 32.1, redacción vigente el 21 de diciembre de 2022.

---

**Lo que hay que leer en esas cuatro letras**, porque **es el temario del tema anterior escrito en
lenguaje jurídico:**

| Letra | Qué exige | Con qué se cumple en una instalación |
|---|---|---|
| **a)** | **Seudonimizar y cifrar** | **Cifrado en el disco de la grabadora y en el enlace que la exporta** |
| **b)** | **Confidencialidad, integridad, disponibilidad y RESILIENCIA permanentes** | **Redundancia: la resiliencia es una exigencia legal, no una comodidad** |
| **c)** | **Restaurar rápido tras un incidente físico o técnico** | **Copias de seguridad probadas y tiempo de restauración medido** |
| **d)** | **Verificar y evaluar con regularidad la eficacia** | **Auditoría periódica: no basta con instalarlo, hay que comprobarlo** |

**El dato que separa a quien ha leído el artículo de quien no**: **la letra b) enumera cuatro
propiedades y no tres.** **A la confidencialidad, la integridad y la disponibilidad el reglamento
añade la RESILIENCIA**, y **la añade con la palabra «permanentes».** **Una instalación que se cae y
tarda un día en volver no cumple ese artículo**, aunque nadie haya visto los datos.

**Y el criterio que gobierna todo el artículo, que es el que más se malinterpreta**: **el nivel de
seguridad no es fijo, es «adecuado al riesgo».** **La norma no dice qué hay que comprar**: **dice que
hay que justificar por qué eso basta**, teniendo en cuenta el estado de la técnica y el coste. **De ahí
que la memoria de un proyecto tenga que razonar las medidas y no sólo enumerarlas.**


## 3. Protección desde el diseño y por defecto

**El artículo 25 del reglamento europeo es el que llega antes que el ingeniero al proyecto**, porque
**obliga en el momento de decidir los medios, no en el de estrenarlos.**

**Artículo 25**, apartado 2:

> «**El responsable del tratamiento aplicará las medidas técnicas y organizativas apropiadas con miras a
> garantizar que, por defecto, solo sean objeto de tratamiento los datos personales que sean
> necesarios para cada uno de los fines específicos del tratamiento. Esta obligación se aplicará a la
> cantidad de datos personales recogidos, a la extensión de su tratamiento, a su plazo de conservación
> y a su accesibilidad. Tales medidas garantizarán en particular que, por defecto, los datos
> personales no sean accesibles, sin la intervención de la persona, a un número indeterminado de
> personas físicas.**»
>
> — Reglamento (UE) 2016/679, artículo 25.2, redacción vigente el 21 de diciembre de 2022.

---

**Las dos ideas que hay que separar**, porque **el título del artículo lleva dos y se confunden:**

| Idea | Cuándo actúa | Qué exige |
|---|---|---|
| **Desde el diseño** | **Al decidir los medios** —apartado 1— | **Meter las garantías en la arquitectura**, no encima de ella |
| **Por defecto** | **En la configuración de fábrica** —apartado 2— | **Que lo que sale de serie sea lo mínimo**, no lo máximo |

**Lo que eso significa en una instalación audiovisual, dicho sin rodeos**: **una grabadora que sale de
caja guardando un año y accesible a todo el personal incumple el apartado 2.** **El valor por defecto
tiene que ser el corto y el cerrado**, y **abrirlo debe ser una decisión de alguien.**

## 4. Videovigilancia: el artículo 22

**Es el artículo que se lleva a la obra.** **La Ley Orgánica 3/2018 le dedica un artículo entero**, y
**sus tres primeros apartados resuelven las tres preguntas que siempre se hacen: qué se puede grabar,
hasta dónde y cuánto tiempo.**

**Artículo 22**, apartados 1 a 3:

> «**1. Las personas físicas o jurídicas, públicas o privadas, podrán llevar a cabo el tratamiento de
> imágenes a través de sistemas de cámaras o videocámaras con la finalidad de preservar la seguridad de
> las personas y bienes, así como de sus instalaciones.
> 2. Solo podrán captarse imágenes de la vía pública en la medida en que resulte imprescindible para la
> finalidad mencionada en el apartado anterior.
> No obstante, será posible la captación de la vía pública en una extensión superior cuando fuese
> necesario para garantizar la seguridad de bienes o instalaciones estratégicos o de infraestructuras
> vinculadas al transporte, sin que en ningún caso pueda suponer la captación de imágenes del interior
> de un domicilio privado.
> 3. Los datos serán suprimidos en el plazo máximo de un mes desde su captación, salvo cuando hubieran
> de ser conservados para acreditar la comisión de actos que atenten contra la integridad de personas,
> bienes o instalaciones. En tal caso, las imágenes deberán ser puestas a disposición de la autoridad
> competente en un plazo máximo de setenta y dos horas desde que se tuviera conocimiento de la
> existencia de la grabación.**»
>
> — Ley Orgánica 3/2018, artículo 22, apartados 1 a 3 (`BOE-A-2018-16673`), redacción vigente el 21 de
> diciembre de 2022.

---

**Los cuatro números que salen de ahí y que son exactamente lo preguntable:**

| Dato | Valor |
|---|---|
| **Plazo máximo de supresión de las imágenes** | **Un mes desde la captación** |
| **Plazo para poner una grabación a disposición de la autoridad** | **Setenta y dos horas desde que se conoce que existe** |
| **Vía pública** | **Sólo lo imprescindible**, salvo instalación estratégica o de transporte |
| **Interior de un domicilio privado** | **Nunca**, en ningún caso |

**Y el apartado 4, que es el del cartel**: **el deber de informar del artículo 12 del reglamento
europeo se cumple colocando un dispositivo informativo en lugar suficientemente visible** que
identifique **al menos tres cosas**: **que hay tratamiento, quién es el responsable y que se pueden
ejercer los derechos de los artículos 15 a 22 del reglamento.** **Puede añadirse un código o una
dirección de internet**, pero **el responsable sigue obligado a tener disponible la información
completa.**

**El aviso de obra**: **el cartel es parte de la instalación, no de la burocracia posterior.** **Un
sistema entregado sin los dispositivos informativos colocados está incompleto**, y **quien lo firma
responde de ello.**

## 5. Cámaras y micrófonos en el centro de trabajo: el artículo 89

**Aquí está la diferencia que más papeletas resuelve**: **grabar en el trabajo no se rige por el
artículo 22, sino por el 89**, y **el propio artículo 22 lo remite así en su apartado 8.**

**Artículo 89**, apartados 2 y 3:

> «**2. En ningún caso se admitirá la instalación de sistemas de grabación de sonidos ni de
> videovigilancia en lugares destinados al descanso o esparcimiento de los trabajadores o los empleados
> públicos, tales como vestuarios, aseos, comedores y análogos.
> 3. La utilización de sistemas similares a los referidos en los apartados anteriores para la grabación
> de sonidos en el lugar de trabajo se admitirá únicamente cuando resulten relevantes los riesgos para
> la seguridad de las instalaciones, bienes y personas derivados de la actividad que se desarrolle en
> el centro de trabajo y siempre respetando el principio de proporcionalidad, el de intervención mínima
> y las garantías previstas en los apartados anteriores.**»
>
> — Ley Orgánica 3/2018, artículo 89, apartados 2 y 3 (`BOE-A-2018-16673`), redacción vigente el 21 de
> diciembre de 2022.

---

**Las tres reglas que hay que llevar aprendidas:**

| Regla | Qué dice |
|---|---|
| **Prohibición absoluta** | **Ni cámara ni micrófono en vestuarios, aseos, comedores y análogos.** **«En ningún caso»** |
| **Información previa** | **Al trabajador y, en su caso, a sus representantes**, de forma **expresa, clara y concisa** |
| **El sonido es más estricto que la imagen** | **Sólo si los riesgos son RELEVANTES**, y con **proporcionalidad e intervención mínima** |

**La asimetría entre imagen y sonido es lo más preguntable del artículo**: **grabar imagen para
controlar el cumplimiento laboral se admite con información previa**; **grabar sonido exige además que
haya riesgos relevantes para la seguridad.** **El legislador entendió que oír lo que alguien dice
invade más que verlo.**

**Y el caso propio de una instalación audiovisual, que conviene pensar antes de que ocurra**: **un
micrófono de plató o de control no es un sistema de grabación de sonidos en el lugar de trabajo
mientras sirva a la producción**; **lo es en cuanto se conserve y se use para controlar a quien
trabaja.** **La finalidad, y no el aparato, decide qué artículo se aplica.**

## 6. Los otros derechos digitales del título X

**El título de la ley dice «y garantía de los derechos digitales»**, y **ese título X es lo que la ley
española añade por su cuenta.** **Los cuatro que tocan a un centro de trabajo técnico:**

| Artículo | Derecho | Lo que hay que retener |
|---|---|---|
| **87** | **Intimidad y uso de dispositivos digitales** | **El empleador puede acceder sólo para controlar obligaciones laborales y la integridad del dispositivo**, y **los criterios de uso se elaboran con participación de los representantes** |
| **88** | **Desconexión digital** | **Se ejerce según la negociación colectiva**, y **el empleador elabora una política interna previa audiencia de los representantes** |
| **89** | **Cámaras y micrófonos en el trabajo** | **El del epígrafe anterior** |
| **90** | **Geolocalización** | **Información previa expresa, clara e inequívoca**, y **también sobre cómo ejercer los derechos** |

**El hilo común de los cuatro, que es lo que se pregunta cuando se pregunta**: **ninguno prohíbe la
herramienta; todos exigen informar antes y contar con los representantes de los trabajadores.**
**Quien busque en la ley una prohibición de vigilar no la encuentra**: **encuentra un procedimiento.**

**Y el que un ingeniero olvida**: **el artículo 88 menciona expresamente el trabajo a distancia.** **En
una corporación con guardias, retenes y avisos, la política de desconexión no es un adorno**: **decide
si un técnico está obligado a atender un aviso fuera de su turno.**

## 7. Las dos setenta y dos horas, que no son la misma

**Éste es el error que el temario quiere prevenir**, porque **el número se repite y las dos cosas no
tienen nada que ver:**

| Dónde | Qué cuentan las 72 horas | Norma |
|---|---|---|
| **Videovigilancia** | **Plazo para poner una grabación a disposición de la autoridad competente** desde que se sabe que existe | **Artículo 22.3 de la Ley Orgánica 3/2018** |
| **Brecha de seguridad** | **Plazo para notificar a la autoridad de control una violación de la seguridad** desde que se tiene constancia | **Artículo 33.1 del Reglamento (UE) 2016/679** |

**La segunda tiene además dos matices que se preguntan**: **no hay que notificar si es improbable que
la violación entrañe un riesgo para los derechos y libertades**, y **si se pasa de las setenta y dos
horas, la notificación debe ir acompañada de la indicación de los motivos del retraso.** **Es decir:
llegar tarde no exime de notificar, obliga a explicarse.**

**Y el plazo que no son setenta y dos horas y se confunde con ellas**: **el mes del artículo 22.3**,
que es **el máximo de conservación de las imágenes**, no un plazo de reacción.

## 8. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **este punto es de los que más rendimiento dan por hora, porque su materia
son plazos y prohibiciones cerradas.** **Lo razonablemente preguntable, por orden**: **el mes y las
setenta y dos horas del artículo 22**, **la prohibición absoluta de vestuarios y aseos del artículo
89.2**, **las cuatro letras del artículo 32.1 con su resiliencia**, **el «por defecto» del artículo
25.2** y **el reparto entre reglamento europeo y ley orgánica.** **Lo demás se lee.**

## 9. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales** (`BOE-A-2018-16673`), **en su redacción vigente el 21 de diciembre de 2022** | **Los apartados 1 a 3 del artículo 22** y **los apartados 2 y 3 del artículo 89**, citados literalmente |
| **Primero: norma de la Unión publicada en el Diario Oficial** | **Reglamento (UE) 2016/679** (`DOUE-L-2016-80807`), **en su redacción vigente el 21 de diciembre de 2022** | **El apartado 1 del artículo 32** y **el apartado 2 del artículo 25**, citados literalmente |

**Cinco declaraciones expresas:**

1. **La ley orgánica se ha leído en su texto consolidado**, que es **el que el propio enunciado del
   anexo manda estudiar**: el enunciado remite al consolidado con última modificación publicada el
   27/05/2021, **anterior a la fecha de corte**, de modo que **la redacción del anexo y la del corte
   coinciden.**
2. **El contenido de los apartados 4 y 8 del artículo 22 se resume, no se cita.** **El apartado 4 es
   el del dispositivo informativo** y **el apartado 8 es el que remite al artículo 89 cuando el
   tratamiento lo hace el empleador.** **Ambos están en la norma citada arriba.**
3. **Los artículos 87, 88 y 90 del título X se resumen en tabla y no se citan literalmente.** **Sus
   rúbricas y su contenido están en la misma norma**, y **el resumen no añade obligación alguna que
   ellos no digan.**
4. **El apartado 1 del artículo 33 del reglamento europeo se resume y no se cita**: de él salen **el
   plazo de setenta y dos horas**, **la salvedad de que sea improbable el riesgo** y **la obligación
   de indicar los motivos de la dilación.**
5. **Ninguna respuesta oficial descansa en este tema**, porque **el punto no ha dado preguntas en el
   cuadernillo.** **Las citas se han verificado igual contra las dos fuentes**, por el método.

**El resto del tema va como oficio y así se declara**: la lectura de las cuatro letras del artículo
32.1 como requisitos de pliego, el aviso de que la resiliencia es la cuarta propiedad y no una
comodidad, la advertencia sobre la grabadora que sale de caja guardando un año, el aviso de que el
cartel es parte de la instalación, la distinción entre el micrófono de producción y el micrófono de
control laboral, y la advertencia sobre las dos setenta y dos horas. **Nada de eso está en un boletín
oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
