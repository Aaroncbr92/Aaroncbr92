# Tema 16 del específico de Técnica de Equipos y Sistemas Electrónicos · Mantenimiento en televisión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica de Equipos y Sistemas Electrónicos · punto 19 |
| **Sirve para** | **Técnica de Equipos y Sistemas Electrónicos** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la explotación de una instalación de televisión, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Aviso de contenido** | **Ninguna de sus tres preguntas es de electrónica**: dos son de licencias de programas y una de criterio ante una avería en directo. **Es el punto donde esta ocupación deja de ser un oficio de banco de trabajo y pasa a ser un oficio de explotación**, y el examen lo ha entendido así |
| **Extensión** | **2.409 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el conjunto redundante de discos independientes
(**RAID**) y el sistema de alimentación ininterrumpida (**SAI**), los dos ya usados en temas
anteriores de esta ocupación.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 19):
> «MANTENIMIENTO EN TV: Mantenimiento de Estudios, Continuidades, Controles Técnicos y Salas Técnicas,
> Sistemas de Redacción, Postproducción (Video y Audio) y Sonorización. Equipos que forman el
> equipamiento audiovisual, operaciones a realizar, resolución de incidencias, actualizaciones a
> realizar, operación diaria de soporte o mantenimiento. Redundancia que debe existir en el
> equipamiento.»

**Tres preguntas.** **Y son las tres preguntas más raras de la ocupación**, porque **ninguna es de
electrónica**: **dos son de licencias de programas y una es de criterio ante una avería en directo.**

**Eso no es un accidente del examen: es lo que dice el enunciado.** **El punto 19 no habla de
componentes, habla de «resolución de incidencias», «actualizaciones a realizar» y «operación diaria de
soporte».** **Es el punto donde esta ocupación deja de ser un oficio de banco de trabajo y pasa a ser
un oficio de explotación**, y **el examen lo ha entendido así.**

**Ninguna de las tres lleva figura.** **Las tres se contestan razonando**, y **las tres tienen en común
que la respuesta correcta es la prudente.**

<!-- indice -->

## Índice

- [1. Qué se mantiene en una televisión](#1-qué-se-mantiene-en-una-televisión)
- [2. La redundancia](#2-la-redundancia)
- [3. El disco averiado en continuidad](#3-el-disco-averiado-en-continuidad)
- [4. Las licencias y las versiones](#4-las-licencias-y-las-versiones)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué se mantiene en una televisión

**El enunciado enumera siete áreas, y conviene saber qué hay en cada una porque cada una falla de una
manera:**

| Área | Qué contiene | Qué la caracteriza |
|---|---|---|
| **Estudios** | **Cámaras, iluminación, sonido de plató, comunicaciones** | **Muchos equipos móviles y mucho cableado que se manipula a diario** |
| **Continuidades** | **La cadena que llega a la antena: servidores de emisión, conmutación, retardo** | **No puede parar nunca: cada minuto es emisión** |
| **Controles técnicos y salas técnicas** | **Matrices, distribuidores, sincronismos, conversores, red** | **Es la columna vertebral: un fallo aquí afecta a todo lo demás** |
| **Sistemas de redacción** | **Los ordenadores y los programas donde se escribe y se edita la noticia** | **Fallan por informática, no por electrónica** |
| **Postproducción de vídeo y audio** | **Salas de edición y de mezcla** | **Trabajo por proyectos, con dependencia fuerte de versiones y licencias** |
| **Sonorización** | **Refuerzo de sonido de plató y de público** | **Comparte problemas con el tema 11: potencia, cables y realimentación** |

**Y la jerarquía que ordena las prioridades cuando fallan dos cosas a la vez**: **primero lo que está
en antena, después lo que va a estar en antena en las próximas horas, y al final lo que se puede
recuperar más tarde.** **Una sala de edición parada es un problema; una continuidad parada es un
incidente de emisión.**

## 2. La redundancia

**El enunciado la nombra expresamente —«Redundancia que debe existir en el equipamiento»—** y **es lo
que este punto tiene de propio frente al tema 15.**

**Los niveles de redundancia de una instalación de televisión, de menos a más:**

| Nivel | En qué consiste | Cuánto tarda en entrar |
|---|---|---|
| **Repuesto en almacén** | **Hay otra unidad, apagada, en la estantería** | **El tiempo de ir a por ella y configurarla** |
| **Reserva fría** | **Hay otra unidad instalada y apagada** | **El tiempo de encenderla y conmutar** |
| **Reserva caliente** | **Hay otra unidad instalada, encendida y sincronizada** | **El tiempo de accionar la conmutación** |
| **Redundancia interna del propio equipo** | **El equipo tiene dos fuentes, dos ventiladores o discos en RAID** | **Ninguno: sigue funcionando con la pieza rota dentro** |
| **Doble camino permanente** | **Las dos rutas van a la vez y el receptor toma de las dos** | **Ninguno: no hay conmutación**, como la norma de redundancia del tema 9 |

**Y la regla que hay que llevar entendida, porque es la que la pregunta 25 mide**: **la redundancia
existe para que la avería no se note.** **Si se ha invertido en redundancia y, cuando llega la avería,
se para el servicio de todas formas, la inversión no ha servido para nada.**

**Dónde está la redundancia en una cadena de emisión típica**: **doble alimentación desde dos cuadros
distintos, con sistema de alimentación ininterrumpida y grupo electrógeno detrás; doble camino de
señal por matrices distintas; doble servidor de emisión sincronizado; y doble enlace hacia el centro
emisor.** **La lista completa es larga**, y **lo que hay que retener es el criterio: se duplica lo que
no puede parar y se tiene repuesto de lo que sí.**

**El aviso que casi nadie recuerda**: **una redundancia que no se prueba no existe.** **Una segunda
fuente que lleva tres años sin dar corriente puede estar averiada y nadie lo sabrá hasta que caiga la
primera.** **Probar las conmutaciones y descargar los sistemas de alimentación ininterrumpida es tarea
del preventivo del tema 15.**

## 3. El disco averiado en continuidad

**La pregunta 25 del segundo cuadernillo plantea el caso completo**: **desde una continuidad se quiere
emitir un programa grabado, el sistema de almacenamiento único —que ya cuenta con redundancia
interna— informa de un fallo en uno de sus discos, y se pregunta cuál es el procedimiento más adecuado
para garantizar la emisión.**

**La respuesta oficial**: **continuar la emisión normalmente, ya que la redundancia interna garantiza
la disponibilidad de los datos.**

---

**Y es exactamente el epígrafe anterior aplicado**: **el sistema tiene redundancia interna, un disco ha
fallado, y la redundancia interna está haciendo justo aquello para lo que se compró.** **El cálculo
del tema 10 lo dice con números**: **un conjunto en RAID 5 sigue funcionando con un disco menos.**

**Las tres opciones falsas, y por qué cada una es peor que no hacer nada:**

| Opción | Qué provoca |
|---|---|
| **a) Detener la emisión para reparar el disco** | **Convierte una avería sin consecuencias en un corte de emisión.** **Es el error que la redundancia existe para evitar** |
| **c) Copiar de inmediato los programas críticos a otro sistema y emitir desde ahí** | **Una copia masiva carga el conjunto justo cuando está degradado**, y **cambiar la fuente de emisión en caliente es más arriesgado que seguir** |
| **d) Reiniciar el sistema de almacenamiento** | **Lo peor de las cuatro**: **corta la emisión y además somete al conjunto degradado a un arranque, que es el momento de mayor esfuerzo para los discos** |

**Lo que sí hay que hacer, y no es ninguna de las cuatro opciones porque la pregunta no lo ofrece**:
**sustituir el disco averiado por uno sano en cuanto se pueda, sin parar el servicio**, que es
precisamente lo que un conjunto redundante permite hacer, **y vigilar la reconstrucción.** **Emitir y
reparar no son incompatibles: ése es el sentido de la respuesta oficial.**

**El aviso técnico que conviene añadir, porque el examen no lo pregunta y el oficio lo sabe**: **un
conjunto degradado ha agotado su margen.** **Con un disco caído, un RAID 5 no tolera el siguiente
fallo**, y **la reconstrucción es el momento de mayor exigencia para los discos supervivientes.**
**Seguir emitiendo es lo correcto; olvidarse del disco caído, no.**

## 4. Las licencias y las versiones

**Dos de las tres preguntas del punto son de programas informáticos**, y **eso, en una ocupación de
electrónica, sorprende hasta que se lee el enunciado: «Sistemas de Redacción» y «Postproducción» están
en él con todas las letras.**

**La pregunta 15 del segundo cuadernillo va de licencias flotantes**: **las licencias flotantes se
comparten entre varios redactores, pero sólo un número limitado de usuarios pueden usarlas a la vez,
dependiendo de la cantidad de licencias adquiridas.** Ésa es la respuesta oficial.

---

**Los dos modelos de licencia, uno frente a otro:**

| | **Licencia nominal o por puesto** | **Licencia flotante** |
|---|---|---|
| **A qué se ata** | **A un equipo o a una persona** | **A un servidor que las presta** |
| **Quién puede usarla** | **Ese equipo o esa persona** | **Cualquiera de la red, mientras queden libres** |
| **Qué limita** | **Nada más: el que la tiene, la tiene** | **Cuántas se usan a la vez** |
| **Para qué encaja** | **Puestos dedicados que trabajan siempre** | **Muchos puestos que usan el programa a ratos** |

**Y por qué una redacción compra flotantes**: **hay ochenta redactores y sólo veinte editan a la vez.**
**Comprar ochenta licencias sería pagar sesenta que están paradas.** **Se compran veinticinco, y el
servidor las va prestando.**

**El inconveniente, que es el que el mantenimiento sufre**: **cuando se agotan, el usuario ochenta y
uno no entra.** **Y hay un modo particular de agotarlas que da mucha guerra: el redactor que deja el
programa abierto y se va.** **Su licencia sigue ocupada.** **De ahí que estos servidores tengan
liberación por inactividad, y que saber liberar una licencia colgada sea tarea corriente del soporte
diario que el enunciado nombra.**

**Las tres opciones falsas y su defecto**: **la a describe la licencia nominal; la b dice «sin
límite», que es justo lo contrario del modelo; y la d cambia el límite de usuarios por un requisito de
conexión a internet**, que **es característica de otro modelo de licenciamiento, el de suscripción, y
no de éste.**

**La pregunta 17 del segundo cuadernillo va de versiones**: **al llevar un proyecto de un programa de
postproducción de la versión de 2024 a una estación que sólo tiene la de 2022, el problema es que el
proyecto no se abrirá directamente, ya que las versiones anteriores no son compatibles con proyectos
de versiones más nuevas.** Ésa es la respuesta oficial.

---

**La regla que hay detrás se llama compatibilidad hacia atrás, y es asimétrica:**

| Dirección | Qué pasa |
|---|---|
| **Proyecto viejo abierto con programa nuevo** | **Suele funcionar**: el programa nuevo sabe leer lo que el viejo escribía, y a menudo ofrece convertirlo |
| **Proyecto nuevo abierto con programa viejo** | **No funciona**: el programa viejo no puede conocer un formato que se inventó después de él ✔ |

**Y el porqué es de sentido común y por eso se recuerda**: **un programa puede saber lo que se hizo
antes; ninguno puede saber lo que se hará después.**

**Las tres opciones falsas dicen tres cosas imposibles**: **la a promete compatibilidad total entre
versiones; la c inventa un cambio automático de licencia, que no tiene nada que ver con el formato del
proyecto; y la d supone que el programa viejo se actualizaría solo**, lo que **además sería un cambio
de versión no planificado, exactamente lo que el tema 15 desaconseja.**

**Cómo se resuelve el caso en la práctica, que es lo útil**: **exportando el proyecto desde la versión
nueva en un formato de intercambio que la vieja entienda**, o **igualando versiones entre las
estaciones.** **La segunda solución es la que el mantenimiento debe perseguir**: **un parque de salas de
edición con versiones distintas genera esta incidencia todas las semanas**, y **por eso la
actualización coordinada de todas las estaciones es una tarea de preventivo, no una decisión de cada
sala.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 15 (2.º llam.) | Cómo funciona una licencia flotante | c) Se comparten, con un límite de usos simultáneos ✔ |
| 17 (2.º llam.) | Problema al abrir un proyecto de 2024 en la versión de 2022 | b) No se abrirá: no hay compatibilidad hacia el futuro ✔ |
| 25 (2.º llam.) | Qué hacer con un disco averiado en un sistema redundante | b) Continuar la emisión: la redundancia interna garantiza los datos ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El rasgo que llama la atención y conviene decir**: **las tres preguntas del punto vienen del segundo
cuadernillo, el corto**, **y ninguna del primero.** **Es el único punto de la ocupación del que puede
decirse eso.**

**El aviso de estudio**: **este punto no se estudia con un manual de electrónica.** **Lo que mide es
criterio de explotación**: **qué se para y qué no se para, qué se duplica, cómo se organizan las
licencias y por qué las versiones no van hacia atrás.** **Es el punto donde más rinde haber trabajado
en una instalación y donde menos rinde saber teoría de circuitos.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Este temario no describe la instalación de RTVE.** **Las áreas del epígrafe 1, los niveles de
   redundancia del epígrafe 2 y la lista de qué se duplica en una cadena de emisión son la
   arquitectura habitual de una televisión**, escrita como guía de estudio a partir del propio
   enunciado del anexo. **No proceden de ninguna documentación de la corporación**, y **el temario no
   afirma que la instalación de RTVE esté montada así.**
2. **Ninguna de las tres preguntas depende de esa arquitectura**: **las tres se contestan con el
   razonamiento que queda escrito en los epígrafes 3 y 4.**
3. **Los modelos de licencia del epígrafe 4 se describen de forma genérica.** **No se nombra ningún
   programa concreto, ningún fabricante y ninguna condición contractual de ningún producto**, y
   **tampoco lo hace el enunciado de la pregunta, que habla de «una aplicación de edición de
   noticias» sin nombrarla.**
4. **La asimetría de la compatibilidad entre versiones del epígrafe 4 se presenta como regla
   general del sector, no como característica de ningún producto.** **La respuesta oficial la
   enuncia en esos mismos términos generales**, y el temario la razona sin atribuirla a nadie.
5. **El comportamiento de un conjunto RAID 5 con un disco caído del epígrafe 3 es el mismo que el
   tema 10 de esta ocupación calcula**, y **allí consta ya que la cuenta se hace y no se toma de
   ninguna fuente.**

**El resto del tema va como oficio y así se declara**: la jerarquía de prioridades ante dos averías
simultáneas, el aviso de que una redundancia que no se prueba no existe, la clasificación razonada de
las opciones falsas de las tres preguntas, el problema de las licencias colgadas y la recomendación de
igualar versiones entre salas. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
