# Esquema · Tema 19 del específico de Ingeniería Técnica · Telecomunicación · Protección de datos personales

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = Ley Orgánica 3/2018, citada
literalmente en el tema · `[DOUE]` = Reglamento (UE) 2016/679, citado literalmente en el tema · `[of]`
= oficio de instalaciones. **Siglas**: la Ley Orgánica de Protección de Datos Personales y garantía de
los derechos digitales (**LOPDGDD**); el Reglamento General de Protección de Datos (**RGPD**); la
Agencia Española de Protección de Datos (**AEPD**); la evaluación de impacto relativa a la protección
de datos (**EIPD**); y el delegado de protección de datos (**DPD**).

**Cabecera.** Enunciado: punto 23 del anexo · **cero preguntas** · **y aun así no se despacha**: este
punto **decide dónde se puede colgar una cámara, dónde no se puede poner un micrófono, cuánto se
guarda una grabación y qué hay que meter en el pliego antes de comprar el sistema.**

<!-- indice -->

## Índice

- [Qué norma es cuál](#qué-norma-es-cuál)
- [La seguridad del tratamiento](#la-seguridad-del-tratamiento)
- [Desde el diseño y por defecto](#desde-el-diseño-y-por-defecto)
- [Videovigilancia](#videovigilancia)
- [Cámaras y micrófonos en el trabajo](#cámaras-y-micrófonos-en-el-trabajo)
- [Los otros derechos digitales](#los-otros-derechos-digitales)
- [Las dos setenta y dos horas](#las-dos-setenta-y-dos-horas)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué norma es cuál

| Norma | Qué es | Qué hace |
|---|---|---|
| **Reglamento (UE) 2016/679** · `[DOUE]` | **Reglamento europeo**: se aplica directamente | **Principios, derechos y obligaciones generales** |
| **Ley Orgánica 3/2018** · `[BOE]` | **Ley orgánica española** | **Adapta el reglamento y añade el título X de derechos digitales** |

- **LA REGLA QUE LAS ORDENA** · `[of]` · **Plazo, principio o derecho del interesado: mira al reglamento
  europeo.** **Videovigilancia, trabajo o derechos digitales: mira a la ley orgánica.**

## La seguridad del tratamiento

- **EL ARTÍCULO DEL INGENIERO** · `[DOUE]` · **Artículo 32.1: medidas técnicas y organizativas
  apropiadas para garantizar un nivel de seguridad ADECUADO AL RIESGO**, teniendo en cuenta **el estado
  de la técnica, los costes, la naturaleza, el alcance, el contexto y los fines.**

| Letra | Qué exige | Con qué se cumple en una instalación |
|---|---|---|
| **a)** | **Seudonimización y cifrado** | **Cifrado en el disco de la grabadora y en el enlace que la exporta** |
| **b)** | **Confidencialidad, integridad, disponibilidad y RESILIENCIA permanentes** | **Redundancia: la resiliencia es exigencia legal, no comodidad** |
| **c)** | **Restaurar rápido tras incidente físico o técnico** | **Copias probadas y tiempo de restauración medido** |
| **d)** | **Verificar y evaluar con regularidad la eficacia** | **Auditoría periódica: no basta con instalarlo** |

- **LO QUE SEPARA A QUIEN HA LEÍDO EL ARTÍCULO** · `[of]` · **La letra b) enumera CUATRO propiedades, no
  tres**: **añade la RESILIENCIA**, y con la palabra «permanentes». **Una instalación que se cae y tarda
  un día en volver no cumple ese artículo**, aunque nadie haya visto los datos.
- **EL CRITERIO QUE MÁS SE MALINTERPRETA** · `[of]` · **El nivel de seguridad no es fijo: es «adecuado
  al riesgo».** **La norma no dice qué comprar: dice que hay que JUSTIFICAR por qué eso basta.** **De
  ahí que la memoria de un proyecto razone las medidas y no sólo las enumere.**

## Desde el diseño y por defecto

- **EL ARTÍCULO QUE LLEGA ANTES QUE EL INGENIERO AL PROYECTO** · `[DOUE]` · **Artículo 25**: obliga **en
  el momento de decidir los medios**, no en el de estrenarlos.

| Idea | Cuándo actúa | Qué exige |
|---|---|---|
| **Desde el diseño** | **Al decidir los medios** —apartado 1— | **Meter las garantías en la arquitectura, no encima** |
| **Por defecto** | **En la configuración de fábrica** —apartado 2— | **Que lo que sale de serie sea lo mínimo, no lo máximo** |

- **A QUÉ SE APLICA EL «POR DEFECTO»** · `[DOUE]` · **A la cantidad de datos recogidos, la extensión del
  tratamiento, el plazo de conservación y la accesibilidad**, y **a que no sean accesibles, sin
  intervención de una persona, a un número indeterminado de personas físicas.**
- **QUÉ SIGNIFICA EN OBRA** · `[of]` · **Una grabadora que sale de caja guardando un año y accesible a
  todo el personal incumple ese apartado.** **El valor por defecto ha de ser el corto y el cerrado**, y
  **abrirlo debe ser una decisión de alguien.**

## Videovigilancia

| Dato del artículo 22 · `[BOE]` | Valor |
|---|---|
| **Plazo máximo de supresión de las imágenes** | **Un mes desde la captación** |
| **Plazo para ponerlas a disposición de la autoridad** | **Setenta y dos horas desde que se conoce que existen** |
| **Vía pública** | **Sólo lo imprescindible**, salvo instalación estratégica o de transporte |
| **Interior de un domicilio privado** | **Nunca, en ningún caso** |

- **EL APARTADO 4, EL DEL CARTEL** · `[BOE]` · **El deber de informar se cumple con un dispositivo
  informativo en lugar suficientemente visible** que identifique **al menos tres cosas**: **que hay
  tratamiento, quién es el responsable y que se pueden ejercer los derechos de los artículos 15 a 22.**
  **Puede añadirse un código o una dirección de internet**, pero **el responsable sigue obligado a tener
  disponible la información completa.**
- **EL AVISO DE OBRA** · `[of]` · **El cartel es parte de la INSTALACIÓN, no de la burocracia
  posterior.** **Un sistema entregado sin los dispositivos informativos colocados está incompleto**, y
  **quien lo firma responde de ello.**

## Cámaras y micrófonos en el trabajo

- **LA DIFERENCIA QUE MÁS PAPELETAS RESUELVE** · `[BOE]` · **Grabar en el trabajo NO se rige por el
  artículo 22, sino por el 89**, y **el propio artículo 22 lo remite así en su apartado 8.**

| Regla del artículo 89 · `[BOE]` | Qué dice |
|---|---|
| **Prohibición absoluta** | **Ni cámara ni micrófono en vestuarios, aseos, comedores y análogos.** **«En ningún caso»** |
| **Información previa** | **Al trabajador y, en su caso, a sus representantes**, de forma **expresa, clara y concisa** |
| **El sonido es más estricto que la imagen** | **Sólo si los riesgos son RELEVANTES**, con **proporcionalidad e intervención mínima** |

- **LA ASIMETRÍA ES LO MÁS PREGUNTABLE** · `[of]` · **Grabar imagen para controlar el cumplimiento
  laboral se admite con información previa; grabar SONIDO exige además riesgos relevantes para la
  seguridad.** **El legislador entendió que oír lo que alguien dice invade más que verlo.**
- **EL CASO PROPIO DE UNA INSTALACIÓN AUDIOVISUAL** · `[of]` · **Un micrófono de plató o de control no
  es un sistema de grabación de sonidos en el lugar de trabajo mientras sirva a la producción**; **lo es
  en cuanto se conserve y se use para controlar a quien trabaja.** **La FINALIDAD, y no el aparato,
  decide qué artículo se aplica.**

## Los otros derechos digitales

| Artículo · `[BOE]` | Derecho | Qué retener |
|---|---|---|
| **87** | **Intimidad y uso de dispositivos digitales** | **Acceso sólo para controlar obligaciones laborales y la integridad del dispositivo**, y **criterios de uso elaborados con participación de los representantes** |
| **88** | **Desconexión digital** | **Según la negociación colectiva**, y **política interna previa audiencia de los representantes** |
| **89** | **Cámaras y micrófonos en el trabajo** | **El del epígrafe anterior** |
| **90** | **Geolocalización** | **Información previa expresa, clara e inequívoca**, y también sobre cómo ejercer los derechos |

- **EL HILO COMÚN** · `[of]` · **Ninguno prohíbe la herramienta; todos exigen INFORMAR ANTES y contar
  con los representantes.** **Quien busque en la ley una prohibición de vigilar no la encuentra:
  encuentra un procedimiento.**
- **EL QUE UN INGENIERO OLVIDA** · `[of]` · **El artículo 88 menciona expresamente el trabajo a
  distancia.** **En una corporación con guardias, retenes y avisos, la política de desconexión decide si
  un técnico está obligado a atender un aviso fuera de su turno.**

## Las dos setenta y dos horas

| Dónde | Qué cuentan | Norma |
|---|---|---|
| **Videovigilancia** | **Plazo para poner una grabación a disposición de la autoridad** | **Artículo 22.3 de la ley orgánica** · `[BOE]` |
| **Brecha de seguridad** | **Plazo para notificar una violación de la seguridad a la autoridad de control** | **Artículo 33.1 del reglamento europeo** · `[DOUE]` |

- **LOS DOS MATICES DE LA SEGUNDA** · `[DOUE]` · **No hay que notificar si es improbable que la
  violación entrañe un riesgo para los derechos y libertades**, y **si se pasa de las setenta y dos
  horas la notificación debe indicar los motivos de la dilación.** **Llegar tarde no exime de
  notificar: obliga a explicarse.**
- **EL PLAZO QUE SE CONFUNDE CON ELLAS** · `[of]` · **El MES del artículo 22.3**, que es **el máximo de
  conservación de las imágenes**, no un plazo de reacción.

## Lo que se ha preguntado

- **NINGUNA PREGUNTA.**
- **LO RAZONABLEMENTE PREGUNTABLE, POR ORDEN** · `[of]` · **El mes y las setenta y dos horas del
  artículo 22** · **la prohibición absoluta de vestuarios y aseos del artículo 89.2** · **las cuatro
  letras del artículo 32.1 con su resiliencia** · **el «por defecto» del artículo 25.2** · **el reparto
  entre reglamento europeo y ley orgánica.** **Lo demás se lee.**
