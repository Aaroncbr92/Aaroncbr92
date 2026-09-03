# Tema 7 del específico de Técnica Informática · Métrica V3, metodologías ágiles y SCRUM

Las siglas de este tema, presentadas de entrada: la Organización Internacional de Normalización y la
Comisión Electrotécnica Internacional (**ISO/IEC**), que publican conjuntamente las normas 12207 y
15504 que el enunciado nombra; el estudio de viabilidad del sistema (**EVS**), el análisis del sistema
de información (**ASI**), el diseño (**DSI**), la construcción (**CSI**) y la implantación y
aceptación (**IAS**), que son los cinco procesos de Métrica V3; y el lenguaje unificado de modelado
(**UML**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 9):
> «Procesos principales y estructura de Métrica V3. Aplicación en el desarrollo orientado a objetos.
> Metodologías agiles y SCRUM.»

**Dos preguntas.** **Y son las dos mitades del enunciado, una cada una**: **la metodología clásica de
la Administración y la ágil que la ha desplazado.**

**Este punto tiene un rasgo que conviene decir de entrada**: **es el único del temario que pregunta
por una metodología española**, y **la respuesta a esa pregunta está en el nombre del ministerio que
la publica.**

<!-- indice -->

## Índice

- [1. Métrica V3](#1-métrica-v3)
- [2. Las metodologías ágiles](#2-las-metodologías-ágiles)
- [3. SCRUM](#3-scrum)
- [4. Los datos que el examen ha preguntado](#4-los-datos-que-el-examen-ha-preguntado)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. Métrica V3

**La pregunta 56**: **la metodología propia del Ministerio de Hacienda y Función Pública en España que
se basa en normas como ISO/IEC 12207 y 15504 es Métrica V3.** Ésa es la respuesta oficial.

---

**Y la pregunta se contesta por la palabra «propia»**: **Agile, Scrum y Kanban no son de ningún
ministerio ni de ningún país.** **Sólo una de las cuatro opciones puede ser «propia del Ministerio de
Hacienda y Función Pública», y es la que tiene nombre en español.**

**Qué es Métrica V3, en una línea**: **la metodología de planificación, desarrollo y mantenimiento de
sistemas de información de la Administración General del Estado.**

**Sus cinco procesos, que son la «estructura» que el enunciado pide:**

| Proceso | Qué hace |
|---|---|
| **Planificación de Sistemas de Información** | **Decide qué sistemas necesita la organización**, antes de cualquier proyecto |
| **Desarrollo de Sistemas de Información** | **El grueso**: se subdivide en estudio de viabilidad, análisis, diseño, construcción e implantación |
| **Mantenimiento de Sistemas de Información** | **Qué se hace con el sistema una vez en marcha** |

**Y las cinco fases del proceso de desarrollo, que son las que el examen puede pedir por sus siglas:**

| Fase | Qué produce |
|---|---|
| **Estudio de viabilidad del sistema (EVS)** | **La decisión de hacerlo o no, y con qué alternativa** |
| **Análisis del sistema de información (ASI)** | **Qué tiene que hacer el sistema** |
| **Diseño del sistema de información (DSI)** | **Cómo lo va a hacer** |
| **Construcción del sistema de información (CSI)** | **El código y las pruebas** |
| **Implantación y aceptación del sistema (IAS)** | **La puesta en marcha y la aceptación formal** |

**Y lo que el enunciado llama «aplicación en el desarrollo orientado a objetos»**: **Métrica V3 admite
las dos orientaciones, la estructurada y la de objetos**, y **para la segunda utiliza notación
UML.** **No es una metodología atada a un paradigma.**

**Las dos normas que el enunciado nombra, para situarlas**: **la ISO/IEC 12207 define los procesos del
ciclo de vida del software** y **la 15504 define cómo evaluar la capacidad de esos procesos.**

## 2. Las metodologías ágiles

**El contraste que ordena la otra mitad del punto:**

| | **Clásica, en cascada** | **Ágil** |
|---|---|---|
| **Cuándo se define el alcance** | **Al principio, entero** | **Continuamente** |
| **Cuándo se entrega** | **Al final** | **En cada iteración** |
| **Qué se valora más** | **El plan y la documentación** | **El producto que funciona y la respuesta al cambio** |
| **Cómo se mide el avance** | **Por fases completadas** | **Por producto entregable** |

**Y la frase que resume el manifiesto ágil sin citarlo**: **no es que la documentación y el plan no
valgan; es que, cuando hay que elegir, pesa más el producto que funciona.**

## 3. SCRUM

**La pregunta 31**: **de las características enumeradas, la propia de un sprint es que su resultado
sea un producto que, potencialmente, se pueda entregar.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas se desmontan una a una con la definición del marco:**

| Opción | Por qué es falsa |
|---|---|
| **a) Los requisitos de un sprint son variables durante el mismo** | **Es justo lo contrario**: el alcance del sprint se cierra al empezarlo. **Lo variable es la pila del producto, no la del sprint** |
| **c) Duración fija de un mínimo de cuatro semanas** | **La duración es fija, sí, pero el mínimo no existe**: un sprint dura **como mucho un mes**, y son corrientes los de una o dos semanas |
| **d) Los desarrolladores se reúnen a diario con el propietario del producto y el maestro de scrum** | **La reunión diaria es de los desarrolladores**; los otros dos roles no tienen que estar |

**Los tres roles y los cuatro eventos, que es lo que hay que llevar aprendido:**

| Rol | De qué responde |
|---|---|
| **Propietario del producto** | **Del valor**: qué se hace y en qué orden |
| **Maestro de scrum** | **Del método**: que el marco se siga y se quiten los impedimentos |
| **Equipo de desarrollo** | **Del producto**: cómo se hace |

| Evento | Cuándo | Para qué |
|---|---|---|
| **Planificación del sprint** | **Al empezar** | **Elegir qué entra** |
| **Reunión diaria** | **Cada día**, unos quince minutos | **Sincronizar y ver impedimentos** |
| **Revisión del sprint** | **Al terminar** | **Enseñar lo hecho a quien lo va a usar** |
| **Retrospectiva** | **Al terminar, después de la revisión** | **Mejorar la forma de trabajar** |

**Y el concepto que la respuesta oficial usa y conviene entender**: **un incremento «potencialmente
entregable» no significa que se entregue.** **Significa que está terminado según la definición de
terminado del equipo**, y que **si alguien decidiera publicarlo, no habría que hacerle nada más.**

**Kanban, que la pregunta ofrece como distractor, merece una línea**: **no es un marco con sprints;
es un método de flujo continuo** que limita el trabajo en curso y hace visible el tablero. **Se puede
combinar con Scrum, y a esa combinación el sector la llama Scrumban.**

## 4. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 31 | Característica propia de un sprint | b) Su resultado es potencialmente entregable ✔ |
| 56 | Metodología propia del Ministerio de Hacienda basada en ISO/IEC 12207 y 15504 | c) MÉTRICA V3 ✔ |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **el punto tiene dos preguntas y las dos son de definición.** **Lo más
preguntable de lo que no ha caído son las cinco fases del proceso de desarrollo de Métrica V3 y los
tres roles de Scrum**, que son listas cortas y cerradas.

## 5. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La documentación de Métrica V3 no se ha consultado.** **Sus tres procesos y las cinco fases del
   de desarrollo, con sus siglas, son de uso corriente en la Administración**, y **la respuesta
   oficial de la pregunta 56 sólo pide el nombre de la metodología**, que el propio enunciado sitúa
   en su ministerio.
2. **Las normas ISO/IEC 12207 y 15504 no se han consultado**: su texto está tras un muro de pago.
   **Lo que el tema dice de ellas —que una define los procesos del ciclo de vida y la otra su
   evaluación— es de uso corriente**, y **ninguna respuesta depende de ese dato**: el enunciado las
   nombra sin preguntar por su contenido.
3. **La guía de Scrum no se ha consultado.** **Los tres roles, los cuatro eventos y el límite de un
   mes por sprint son de uso universal**, y **coinciden con la respuesta oficial de la pregunta 31 y
   con el desmontaje de sus opciones falsas.**
4. **El manifiesto ágil no se cita**: el epígrafe 2 lo resume con palabras propias y **así se dice.**

**El resto del tema va como oficio y así se declara**: el argumento de que sólo una de las cuatro
opciones puede ser «propia» de un ministerio, la tabla que contrasta la metodología en cascada con la
ágil, el desmontaje de las tres opciones falsas de la pregunta 31, la explicación de qué significa
«potencialmente entregable» y la nota sobre Kanban. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
