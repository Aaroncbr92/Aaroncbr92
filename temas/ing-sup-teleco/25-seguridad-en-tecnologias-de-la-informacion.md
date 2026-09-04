# Tema 25 del específico de Ingeniería Superior · Telecomunicación · Seguridad en tecnologías de la información

Las siglas de este tema, presentadas de entrada: la Organización Internacional de Normalización
(**ISO**) y la Comisión Electrotécnica Internacional (**IEC**), que publican conjuntamente la familia
**ISO/IEC 27000**; el sistema de gestión de la seguridad de la información (**SGSI**); la biblioteca
de infraestructura de tecnologías de la información (**ITIL**), en sus versiones 3 y 4; el Esquema
Nacional de Seguridad (**ENS**), que es el Real Decreto 311/2022, de 3 de mayo; el Reglamento General
de Protección de Datos (**RGPD**); la red perimetral o zona desmilitarizada (**DMZ**); y la red
privada virtual (**VPN**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 27):
> «Seguridad en tecnologías de la información. Normativas ISO/IEC 27000‐series. Biblioteca de
> Infraestructura de Tecnologías de Información (ITIL versiones 3 y 4).»

**Cero preguntas.** **Este punto no ha dado ni una en el cuadernillo de esta ocupación**, y **el tema
se escribe igual, contra el programa y no contra el examen.**

**Y hay que decir de entrada cómo se relaciona este punto con los de otras ocupaciones de este mismo
proyecto**, porque **la diferencia está en una palabra y no es menor**: **el punto 22 del anexo de
Ingeniería Técnica · Telecomunicación dice «Normativa ISO/IEC 27001» y éste dice «Normativas ISO/IEC
27000‐series».** **Aquél apunta a la norma certificable; éste, a la familia entera.** **No son el mismo
enunciado y por eso no comparten tema**, aunque **la materia se solape y el estudio de una sirva para
la otra.**

**Y la advertencia de método que gobierna todo el tema, dicha antes de empezar y no escondida al
final**: **ni las normas de esa familia ni la biblioteca de gestión de servicios son textos publicados
en un boletín oficial.** **Son publicaciones de pago de organismos privados de normalización**, y
**este proyecto no tiene su texto.** **Por eso este tema no cita de ellas ni una cláusula, ni un
requisito, ni un número de control**, y **lo que dice de ellas lo dice como conocimiento común de la
materia, declarado como tal.** **Lo único que aquí se cita literalmente es la norma española que sí
está en el boletín y que sí regula esta materia para una corporación pública: el Esquema Nacional de
Seguridad.**

<!-- indice -->
<!-- /indice -->

## 1. Qué se protege

**La seguridad de la información no protege máquinas: protege propiedades de la información y de los
servicios.** **Cuáles son esas propiedades lo dice, para el sector público español, el primer artículo
del Esquema Nacional de Seguridad, y conviene leerlo porque enumera más de las tres de manual:**

**Artículo 1**, apartado 2:

> «El ENS está constituido por los principios básicos y requisitos mínimos necesarios para una
> protección adecuada de la información tratada y los servicios prestados por las entidades de su
> ámbito de aplicación, **con objeto de asegurar el acceso, la confidencialidad, la integridad, la
> trazabilidad, la autenticidad, la disponibilidad y la conservación de los datos, la información y
> los servicios** utilizados por medios electrónicos que gestionen en el ejercicio de sus
> competencias.»

---

**Las siete, con lo que significa cada una:**

| Propiedad | Qué garantiza |
|---|---|
| **Acceso** | **que quien tiene derecho pueda llegar a la información** |
| **Confidencialidad** | **que no llegue a ella quien no está autorizado** |
| **Integridad** | **que no se altere sin autorización** |
| **Trazabilidad** | **que se pueda saber quién hizo qué y cuándo** |
| **Autenticidad** | **que quien dice ser algo lo sea, y que el dato venga de donde dice** |
| **Disponibilidad** | **que esté accesible cuando hace falta** |
| **Conservación** | **que siga estando dentro de años, y siga pudiendo leerse** |

**La observación que ordena la lista para esta ocupación**: **en una casa que emite, la propiedad
crítica no es la confidencialidad, es la disponibilidad.** **Un incidente que revele un documento es
grave y se gestiona; uno que deje la señal en negro lo ve el país entero y no admite gestión.** **Un
ingeniero de telecomunicación que llegue a una corporación audiovisual con el orden de prioridades de
una oficina se equivocará en la primera decisión que tome.**

**Y el matiz sobre la última propiedad, que es la que más se olvida y la más propia de un archivo
audiovisual**: **conservar no es guardar.** **Un fichero que sobrevive treinta años en una cinta que
ya no tiene lector no se ha conservado: se ha perdido con orden.** **La conservación exige migrar de
soporte y de formato antes de que el soporte o el formato mueran**, y **eso es una obligación de
seguridad, no una tarea de archivo.**

## 2. La familia de normas de gestión de la seguridad

**Lo primero, entender qué clase de cosa es esa familia**: **no es una lista de medidas técnicas, es
un modelo de gestión.** **Su tesis es que la seguridad no se compra, se gestiona**, y **que lo que
distingue a una organización segura de otra que no lo es no son sus cortafuegos sino su manera de
decidir dónde ponerlos.**

**Los tres papeles que se reparten las normas más citadas de la familia, que es lo que hay que saber
distinguir:**

| Norma | Qué papel desempeña |
|---|---|
| **La 27000** | **el vocabulario y la visión de conjunto de toda la familia** |
| **La 27001** | **los requisitos del sistema de gestión: es la certificable** |
| **La 27002** | **el catálogo de buenas prácticas y controles: no se certifica** |

**La distinción que se pregunta siempre**: **una organización se certifica en la de requisitos, no en
la de buenas prácticas.** **Una dice qué hay que tener; la otra, cómo conseguirlo.** **Y hay más
normas en la familia —de gestión del riesgo, de auditoría, de sectores concretos—, pero este temario
no las enumera, porque enumerar de memoria una familia de normas que no se ha leído es exactamente
lo que este método prohíbe.**

**Qué es un sistema de gestión de la seguridad de la información, dicho en una línea**: **el conjunto
de políticas, procedimientos, responsabilidades y controles con los que una organización planifica su
seguridad, la aplica, la mide y la corrige**, siguiendo el ciclo de **planificar, hacer, verificar y
actuar** que comparten todos los sistemas de gestión.

**Y la idea que hace útil todo el modelo**: **la seguridad se gestiona por riesgos y no por lista de
la compra.** **Se inventarían los activos, se valoran las amenazas y las vulnerabilidades, se estima
el impacto, se decide qué riesgo se acepta y cuál se trata**, y **sólo entonces se eligen los
controles.** **Comprar equipamiento de seguridad antes de ese análisis es gastar sin saber en qué, y
deja fuera precisamente el riesgo que nadie miró.**

**Las cuatro maneras de tratar un riesgo:**

| Tratamiento | En qué consiste |
|---|---|
| **Mitigar** | **poner controles que reduzcan la probabilidad o el impacto** |
| **Transferir** | **pasarlo a un tercero: un seguro, un proveedor con su compromiso** |
| **Evitar** | **dejar de hacer la actividad que lo genera** |
| **Aceptar** | **asumirlo tal como está** |

**La cuarta es la que más se olvida y la única que exige firma**: **aceptar un riesgo es una decisión
de dirección y no del técnico que lo detectó.** **Un riesgo aceptado por quien no tiene autoridad para
aceptarlo no está aceptado: está oculto.**

## 3. La biblioteca de gestión de servicios

**Qué es, con precisión**: **un cuerpo de buenas prácticas para gestionar servicios de tecnologías de
la información.** **No es una norma certificable para la organización**: **quienes se certifican son
las personas.**

**Y por qué el programa la pone junto a la seguridad, que es la pregunta razonable**: **porque casi
todo lo que rompe la seguridad de una instalación entra por un fallo de gestión de servicio.** **Un
cambio sin autorizar, una configuración sin registrar, un incidente que nadie escala.** **La seguridad
se apoya en la gestión del servicio y no al revés.**

**La versión 3 organiza el trabajo en un ciclo de vida del servicio con cinco fases**, y **la manera de
retenerlas es que van en el orden en que un servicio nace y vive:**

| Fase | De qué se ocupa |
|---|---|
| **Estrategia** | **qué servicios se prestan y con qué recursos** |
| **Diseño** | **cómo tienen que ser: nivel de servicio, capacidad, disponibilidad, continuidad, seguridad** |
| **Transición** | **cómo se pasa un servicio nuevo o cambiado a producción, sin romper lo que había** |
| **Operación** | **el día a día: incidentes, problemas, peticiones, accesos** |
| **Mejora continua** | **medir y corregir, y atraviesa a las otras cuatro** |

**Las tres distinciones que un examen pide siempre de esta materia:**

| Concepto | Qué persigue | Cuándo se cierra |
|---|---|---|
| **Incidente** | **devolver el servicio cuanto antes** | **cuando el servicio vuelve, aunque sea con un apaño** |
| **Problema** | **encontrar y eliminar la causa que produce los incidentes** | **cuando la causa desaparece** |
| **Cambio** | **autorizar y coordinar una modificación del entorno** | **cuando la modificación está hecha y comprobada** |

**El matiz que ordena las dos primeras y que es la razón de que sean procesos distintos**: **quien
atiende una urgencia no puede a la vez investigar despacio.** **Separarlos no es burocracia: es que
son dos oficios con dos relojes.**

**Y qué cambia en la versión 4, que el enunciado también nombra**: **desaparece la estructura rígida
de fases y entra un sistema de valor del servicio, articulado en torno a unos principios rectores y a
un conjunto de prácticas**, con **el acento puesto en el valor que se entrega y en no estorbar al que
produce.** **La gestión del cambio pasa a llamarse habilitación del cambio, y el nombre no es
cosmético**: **dice que el papel del proceso es facilitar el cambio con control, no frenarlo.**

**Este temario no da el número de principios ni el número de prácticas de esa versión**, porque **la
publicación no se ha consultado** y **una cifra que no se ha leído en su fuente no se escribe.**

## 4. La norma española que sí está en el boletín

**Aquí acaba lo que se dice como oficio y empieza lo que se cita.** **Una corporación pública española
no gestiona su seguridad sólo con normas privadas: está sujeta al Esquema Nacional de Seguridad**,
aprobado por **el Real Decreto 311/2022, de 3 de mayo**, que **se cita en su redacción vigente el 21 de
diciembre de 2022.**

**A quién se aplica lo dice su segundo artículo, y tiene dos apartados que interesan a un ingeniero
que redacta pliegos:**

**Artículo 2**, apartados 1 y 3:

> «1. **El presente real decreto es de aplicación a todo el sector público**, en los términos en que
> este se define por el artículo 2 de la Ley 40/2015, de 1 de octubre, y de acuerdo con lo previsto en
> el artículo 156.2 de la misma.
> [...]
> 3. **Este real decreto también se aplica a los sistemas de información de las entidades del sector
> privado**, incluida la obligación de contar con la política de seguridad a que se refiere el
> artículo 12, **cuando, de acuerdo con la normativa aplicable y en virtud de una relación
> contractual, presten servicios o provean soluciones a las entidades del sector público** para el
> ejercicio por estas de sus competencias y potestades administrativas.»

---

**La consecuencia práctica, que es lo que un ingeniero tiene que llevarse**: **el esquema no se queda
dentro de la casa.** **Alcanza al proveedor que presta el servicio, y el propio artículo manda que los
pliegos incluyan los requisitos necesarios para asegurar la conformidad de los sistemas en que se
sustenten esos servicios, extendiendo la cautela a la cadena de suministro en la medida en que el
análisis de riesgos lo exija.** **Quien redacta un pliego de un sistema de emisión está escribiendo,
lo sepa o no, una cláusula de seguridad.**

**Los principios básicos son siete y están enumerados en un solo artículo, lo que los convierte en la
lista más preguntable de la norma:**

**Artículo 5**:

> «El objeto último de la seguridad de la información es garantizar que una organización podrá cumplir
> sus objetivos, desarrollar sus funciones y ejercer sus competencias utilizando sistemas de
> información. Por ello, en materia de seguridad de la información deberán tenerse en cuenta los
> siguientes principios básicos:
> **a) Seguridad como proceso integral.
> b) Gestión de la seguridad basada en los riesgos.
> c) Prevención, detección, respuesta y conservación.
> d) Existencia de líneas de defensa.
> e) Vigilancia continua.
> f) Reevaluación periódica.
> g) Diferenciación de responsabilidades.**»

---

**Dos de esos principios tienen artículo propio y son los que más dicen a un ingeniero de
instalaciones.**

**El de las líneas de defensa es la doctrina de la defensa en profundidad puesta en norma:**

**Artículo 9**:

> «1. El sistema de información ha de disponer de una estrategia de protección constituida por
> **múltiples capas de seguridad, dispuesta de forma que, cuando una de las capas sea comprometida**,
> permita:
> a) Desarrollar una reacción adecuada frente a los incidentes que no han podido evitarse, reduciendo
> la probabilidad de que el sistema sea comprometido en su conjunto.
> b) Minimizar el impacto final sobre el mismo.
> 2. **Las líneas de defensa han de estar constituidas por medidas de naturaleza organizativa, física
> y lógica.**»

---

**La frase que hay que retener de ahí es la del apartado 2**: **las capas no son sólo técnicas.** **Un
cortafuegos, una puerta con control de acceso y un procedimiento firmado son tres líneas de defensa de
tres naturalezas distintas**, y **una instalación que sólo tiene las lógicas no tiene defensa en
profundidad: tiene una capa gruesa.**

**Y el de la diferenciación de responsabilidades es el que más se incumple:**

**Artículo 11**, apartados 1 y 2:

> «1. En los sistemas de información se diferenciará **el responsable de la información, el
> responsable del servicio, el responsable de la seguridad y el responsable del sistema**.
> 2. **La responsabilidad de la seguridad de los sistemas de información estará diferenciada de la
> responsabilidad sobre la explotación** de los sistemas de información concernidos.»

---

**Por qué esa separación es una regla de seguridad y no de organigrama**: **quien explota un sistema
tiene el incentivo de que funcione, y quien responde de su seguridad tiene el de que no se rompa.**
**Cuando las dos responsabilidades caen en la misma persona, la primera gana siempre**, porque **la
avería se ve hoy y la brecha se ve dentro de un año.** **La norma lo previene separando los papeles,
no confiando en la virtud de quien los ocupa.**

**Y el enganche con la protección de datos, que la propia norma declara**: **su tercer artículo remite,
cuando el sistema trata datos personales, al reglamento europeo y a la ley orgánica española, y ordena
que prevalezcan las medidas que resulten del análisis de riesgos y de la evaluación de impacto si
resultan más exigentes que las suyas.** **La materia se estudia en el tema 26 de este mismo volumen.**

## 5. Lo propio de una instalación de emisión

**Aquí está lo que un ingeniero de telecomunicación aporta y un informático de gestión no tiene por qué
saber**: **cómo se aplica todo lo anterior a una casa cuyo servicio es una señal que no puede parar.**

**Las redes que conviven y por qué se separan:**

| Red | Qué transporta | Cuánto se expone |
|---|---|---|
| **De señal** | **vídeo y audio en tiempo real, y su reloj** | **cerrada: no toca la red pública** |
| **De control y automatización** | **órdenes a los equipos y la escaleta de emisión** | **cerrada, con accesos contados** |
| **De producción** | **ficheros, edición, catálogo** | **cerrada con salidas controladas** |
| **De gestión** | **correo, navegación, administración** | **expuesta** |

**La regla de diseño**: **el tráfico va de la expuesta hacia las cerradas sólo por puntos controlados,
y nunca al revés sin control.** **Es la red perimetral aplicada a una televisión.**

**Los riesgos propios de esta clase de instalación, que ningún manual de seguridad de oficina
recoge:**

| Riesgo | Por qué es propio de aquí |
|---|---|
| **El equipo audiovisual que no se puede parchear** | **un mezclador o un servidor de emisión tiene sistema operativo, y parar la emisión para actualizarlo no es una decisión técnica sino editorial** |
| **La credencial de fábrica** | **mucho equipamiento de instalación se entrega con usuario y contraseña conocidos y se pone en servicio sin cambiarlos** |
| **El acceso remoto del suministrador** | **el soporte del fabricante suele exigir una puerta permanente: hay que acotarla, registrarla y poder cerrarla** |
| **La automatización de emisión** | **es el sistema con más capacidad de daño de toda la casa y suele ser el menos vigilado**: quien lo controla decide lo que sale en antena |
| **El reloj de la instalación** | **una red de medios sincronizada por protocolo depende de su reloj: atacar el reloj es tumbar la producción sin tocar un solo flujo** |

**La tensión que define este punto para un ingeniero de instalaciones**: **la política de seguridad
corporativa está escrita pensando en ordenadores de oficina**, y **aplicarla al pie de la letra a un
equipo de emisión puede tumbar el canal.** **Lo que se espera de un ingeniero no es saltársela sino
escribir la excepción**: **con su análisis de riesgo, sus controles compensatorios y la firma de quien
acepta lo que queda.** **Eso es exactamente lo que los dos modelos de gestión de este tema piden, y es
también lo que el esquema exige al diferenciar responsabilidades.**

**Y la continuidad, que es donde la seguridad y la explotación se juntan**: **el plan de continuidad de
una casa que emite tiene que contemplar el caso en que los sistemas informáticos caigan y haya que
emitir de todos modos.** **Una cadena de emisión reducida, con material en soporte y gobernada a mano,
es la última línea de defensa**, y **es la que casi nunca se ensaya.** **Un plan que no se ha ensayado
no es un plan: es un documento.**

## 6. Lo que el examen ha preguntado

**Ninguna pregunta.** **El cuadernillo de esta ocupación no ha tocado este punto.**

**Lo razonablemente preguntable, para orientar el repaso**: **las propiedades que se protegen y cuáles
añade el esquema español a las tres clásicas**; **cuál de las normas de la familia es la certificable y
cuál el catálogo de buenas prácticas**; **las cuatro maneras de tratar un riesgo y cuál exige firma**;
**las cinco fases del ciclo de vida del servicio de la versión 3 y el cambio de enfoque de la versión
4**; **la distinción entre incidente, problema y cambio**; y **los siete principios básicos del
esquema, que van todos en un solo artículo.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad** (`BOE-A-2022-7191`), **en su redacción vigente el 21 de diciembre de 2022** | **El apartado 2 del artículo 1**, **los apartados 1 y 3 del artículo 2**, **el artículo 5 entero**, **el artículo 9 entero** y **los apartados 1 y 2 del artículo 11**, citados literalmente |

**Seis declaraciones expresas:**

1. **Este punto no ha dado ninguna pregunta**, de modo que **no hay ninguna respuesta oficial que
   sostener y ninguna que se pueda invocar.** **El tema se escribe contra el enunciado del programa.**
2. **Las normas de la familia ISO/IEC 27000 no se han consultado**: **son publicaciones de pago de
   organismos privados de normalización y este proyecto no tiene su texto.** **Lo que de ellas se dice
   —el reparto de papeles entre las tres más citadas, el ciclo de mejora, la gestión por riesgos y las
   cuatro maneras de tratarlos— se presenta como conocimiento común de la materia y no como cita.**
   **El temario no da ningún número de cláusula, ningún requisito literal, ningún número de controles
   y ninguna enumeración de las demás normas de la familia.**
3. **La biblioteca de gestión de servicios tampoco se ha consultado**, por la misma razón. **Sus cinco
   fases y el reparto entre incidente, problema y cambio se presentan igualmente como conocimiento
   común**, y **están verificados contra respuesta oficial en el tema 20 del específico de Técnica
   Informática, escrito en este mismo proyecto.** **De la versión 4 no se da ni el número de principios
   rectores ni el de prácticas**, porque **no se han leído en su fuente.**
4. **El Esquema Nacional de Seguridad es la única fuente que este tema cita literalmente**, y **sus
   cinco tramos van con su artículo y su apartado.** **Lo que de él no va entre comillas va resumido**:
   **el resto del apartado 3 del artículo 2 —los pliegos y la cadena de suministro— y el artículo 3
   entero**, y **el resumen no añade obligación que la norma no diga.** **El estudio completo de este
   real decreto está en el tema 23 del específico de Técnica Informática.**
5. **Este tema no da ninguna cifra técnica**: **ningún plazo, ningún nivel, ninguna categoría de
   sistema, ningún número de medidas del anexo del esquema y ningún parámetro de configuración.**
   **Los niveles y categorías del esquema existen y están en su articulado y sus anexos**, pero **no se
   recogen aquí porque este punto del programa no los pide y porque su desarrollo está en el tema que
   se acaba de citar.**
6. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la
   protección de datos personales, al tema 26**; **las redes, su segmentación y su control, al tema
   20**; **el reloj repartido y la producción sobre red, al tema 19**; **el almacenamiento, la
   redundancia y las copias, al tema 18**; y **la automatización de emisión y las salas, a los temas
   13 y 14.**

**El resto del tema va como oficio y así se declara**: la observación de que en una casa que emite la
propiedad crítica es la disponibilidad y no la confidencialidad, el matiz de que conservar no es
guardar y de que un fichero en un soporte sin lector se ha perdido con orden, la tesis de que la
seguridad no se compra sino que se gestiona, el aviso de que aceptar un riesgo exige la firma de quien
tiene autoridad y de que un riesgo aceptado por quien no la tiene está oculto, la razón por la que el
programa pone la gestión de servicios junto a la seguridad, el matiz de que incidente y problema son
dos oficios con dos relojes, la lectura de que el cambio de nombre de la gestión del cambio en la
versión 4 no es cosmético, la consecuencia de que quien redacta un pliego está escribiendo una
cláusula de seguridad, la observación de que una instalación con sólo capas lógicas no tiene defensa en
profundidad sino una capa gruesa, la explicación de por qué la separación entre explotación y seguridad
es una regla de seguridad y no de organigrama, la tabla de redes de una casa que emite con su regla de
diseño, los cinco riesgos propios de esta clase de instalación —incluido el del reloj—, la tensión
entre la política corporativa y el equipo de emisión con la salida de escribir la excepción firmada, y
el aviso de que un plan de continuidad que no se ensaya es un documento. **Nada de eso está en un
boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si
lo estuviera.
