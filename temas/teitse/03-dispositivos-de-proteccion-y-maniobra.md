# Tema 3 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Dispositivos de protección y maniobra

Las siglas y símbolos de este tema, presentados de entrada: el reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones (**ITC-BT-08**, **ITC-BT-18**, **ITC-BT-22**, **ITC-BT-23**,
**ITC-BT-24**); el interruptor diferencial (**ID**) y su corriente diferencial-residual asignada
(**IΔn**); el interruptor automático magnetotérmico (**PIA**, pequeño interruptor automático); el
miliamperio (**mA**) y el amperio (**A**); el poder de corte en kiloamperios (**kA**); la muy baja
tensión de seguridad (**MBTS**); el conductor de protección (**CP** o **PE**) y el conductor combinado
de neutro y protección (**CPN** o **PEN**); los esquemas de conexión del neutro (**TN**, **TT** e
**IT**); el grado de protección de una envolvente (**IP**), con sus códigos de ensayo (**IP XXB**,
**IP4X**, **IP XXD**); las clases de diferencial (**AC**, **A**, **B** y **S**); y la Asociación
Española de Normalización (**UNE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de la ocupación tipo de Técnica de
> Equipos, Instalaciones y Sistemas Eléctricos, punto 3):
> «Dispositivos de protección y maniobra: Protección diferencial. Puesta a tierra. Aparatos de
> maniobra y control y protección a baja tensión. Interruptores de maniobra. Automatismos y cuadros
> eléctricos. Conmutación sin paso por cero.»

**Es el punto de la SEGURIDAD ELÉCTRICA de la instalación**, y **el que más artículos de instrucción
técnica tiene detrás de todo el anexo.** **Cuatro instrucciones lo sostienen** —la de esquemas de
conexión del neutro, la de puesta a tierra, la de sobreintensidades y la de contactos—, **y las cuatro
están volcadas y se citan aquí.**

**La idea que ordena el punto entero y que hay que tener antes de abrir nada**: **una instalación
protege DOS cosas distintas, y con aparatos distintos.**

| Qué se protege | De qué | Con qué |
|---|---|---|
| **La INSTALACIÓN** | **Sobrecargas y cortocircuitos** | **Magnetotérmicos y fusibles** |
| **Las PERSONAS** | **Contactos directos e indirectos** | **Diferenciales, puesta a tierra, aislamiento y envolventes** |

**Confundir las dos es el error conceptual del punto**: **un magnetotérmico no protege a nadie de una
electrocución** —una corriente de treinta miliamperios que mata no lo hace saltar— **y un diferencial
no protege el cable de una sobrecarga.** **Los dos hacen falta y ninguno sustituye al otro.**

<!-- indice -->
<!-- /indice -->

## 1. Las sobreintensidades y quién las corta

**La instrucción de sobreintensidades es la que dice qué hay que proteger y de qué**, y **su primer
apartado es la cita que abre el punto:**

> «**Todo circuito estará protegido contra los efectos de las sobreintensidades que puedan presentarse
> en el mismo, para lo cual la interrupción de este circuito se realizará en un tiempo conveniente o
> estará dimensionado para las sobreintensidades previsibles.
> Las sobreintensidades pueden estar motivadas por:
> – Sobrecargas debidas a los aparatos de utilización o defectos de aislamiento de gran impedancia.
> – Cortocircuitos.
> – Descargas eléctricas atmosféricas**»
>
> — Real Decreto 842/2002, instrucción técnica complementaria **ITC-BT-22**, apartado 1.1
> (`BOE-A-2002-18099`), redacción vigente el 21 de diciembre de 2022.

---

**Tres causas y tres respuestas distintas**, y **conviene separarlas porque el aparato que las corta no
es el mismo:**

| Causa | Qué es | Quién la corta |
|---|---|---|
| **SOBRECARGA** | **Corriente superior a la nominal en un circuito sano**: demasiados receptores, o un motor forzado | **El disparo TÉRMICO** del magnetotérmico, o un fusible |
| **CORTOCIRCUITO** | **Contacto directo entre dos conductores activos**, con impedancia casi nula | **El disparo MAGNÉTICO**, instantáneo |
| **Descarga atmosférica** | **Sobretensión transitoria** que llega por la línea | **Los protectores contra sobretensiones**, de la ITC-BT-23 |

**Y la diferencia física entre las dos primeras, que es lo que explica que un mismo aparato tenga dos
disparos**: **una sobrecarga es de dos a diez veces la nominal y se puede aguantar un rato; un
cortocircuito es de cientos o miles de veces y hay que cortarlo en milisegundos.** **Un solo mecanismo
no puede hacer las dos cosas bien**, y **de ahí el magnetotérmico.**

**Lo que la instrucción admite como dispositivo, y hay que citarlo porque acota:**

> «**El dispositivo de protección podrá estar constituido por un interruptor automático de corte
> omnipolar con curva térmica de corte, o por cortacircuitos fusibles calibrados de características de
> funcionamiento adecuadas.**»
>
> — Real Decreto 842/2002, **ITC-BT-22**, apartado 1.1.a) (`BOE-A-2002-18099`), redacción vigente el
> 21 de diciembre de 2022.

---

**Y para el cortocircuito, la regla que se pregunta y que permite ahorrar aparamenta**: **en el origen
de todo circuito se establece un dispositivo contra cortocircuitos cuya capacidad de corte esté de
acuerdo con la intensidad de cortocircuito que pueda presentarse en ese punto**, pero **cuando se
trate de circuitos derivados de uno principal se admite que cada derivado tenga su protección contra
SOBRECARGAS y que un solo dispositivo general asegure la protección contra CORTOCIRCUITOS de todos
ellos.**

**Ésa es la base de la SELECTIVIDAD y del filiado**, y **la lectura de oficio que hay que añadir**:
**el cortocircuito se puede proteger aguas arriba porque su valor lo fija la red y no la carga; la
sobrecarga, no, porque depende de lo que se enchufe en cada circuito.**

## 2. El magnetotérmico

**Un aparato con DOS mecanismos de disparo y una maniobra manual:**

| Mecanismo | Cómo funciona | Qué protege |
|---|---|---|
| **TÉRMICO** | **Una lámina bimetálica que se curva al calentarse** con el paso de la corriente | **La sobrecarga**: actúa tanto más rápido cuanto mayor es el exceso |
| **MAGNÉTICO** | **Una bobina que atrae un núcleo** cuando la corriente supera un umbral | **El cortocircuito**: actúa en milisegundos |

**Los cuatro datos que definen a un magnetotérmico y que hay que saber leer en su frontal:**

| Dato | Qué es |
|---|---|
| **Calibre o intensidad nominal** | **La corriente que aguanta indefinidamente sin disparar** |
| **CURVA de disparo** | **A cuántas veces el calibre actúa la parte MAGNÉTICA** |
| **PODER DE CORTE** | **La corriente de cortocircuito máxima que es capaz de cortar sin destruirse**, en kiloamperios |
| **Número de polos** | Unipolar más neutro, bipolar, tripolar, tetrapolar |

**Las curvas, que es la tabla del epígrafe:**

| Curva | Disparo magnético, en veces el calibre | Para qué |
|---|---|---|
| **B** | **La más sensible** | **Líneas largas y cargas resistivas**; instalaciones con corriente de defecto baja |
| **C** | **Intermedia** | **El uso general**: alumbrado y fuerza corriente |
| **D** | **La menos sensible** | **Cargas con punta de arranque fuerte**: motores, transformadores |

**El temario no da los múltiplos exactos de cada curva y lo declara**: **son dato de norma de producto
y de fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.** **Lo que sí hay que
saber es el ORDEN: B es la que antes dispara y D la que más tolera.**

**El PODER DE CORTE es el dato que más se olvida y el que causa el accidente**, y **hay que decir por
qué**: **si la corriente de cortocircuito posible en un punto supera el poder de corte del aparato que
hay allí, el aparato no corta: se destruye y el arco continúa.** **El poder de corte necesario crece
cuanto más cerca se está del transformador**, y **por eso los aparatos de cabecera son de mayor poder
de corte que los de las últimas derivaciones.**

## 3. La protección diferencial

**El enunciado la nombra la primera y es el aparato característico de la protección de personas.**

**Cómo funciona, en una frase que hay que saber decir**: **compara la corriente que entra por las fases
con la que vuelve por el neutro**, y **si la suma no es cero, la diferencia se está yendo por otro
camino** —una persona, una masa, la humedad— **y el aparato abre.**

**La sensibilidad, que es lo que la clasifica:**

| Sensibilidad | Corriente diferencial asignada | Para qué |
|---|---|---|
| **ALTA sensibilidad** | **30 mA o menos** | **PROTECCIÓN DE PERSONAS**, incluida la complementaria contra contactos directos |
| **Media** | **300 mA** | **Protección contra incendios** de origen eléctrico y contra contactos indirectos |
| **Baja** | **Amperios** | Selectividad en cabecera |

**Y la cita que fija el valor y el papel exacto del aparato, que es lo que más se malinterpreta:**

> «**El empleo de dispositivos de corriente diferencial-residual, cuyo valor de corriente diferencial
> asignada de funcionamiento sea inferior o igual a 30 mA, se reconoce como medida de protección
> complementaria en caso de fallo de otra medida de protección contra los contactos directos o en caso
> de imprudencia de los usuarios.**»
>
> — Real Decreto 842/2002, **ITC-BT-24**, apartado 3.5 (`BOE-A-2002-18099`), redacción vigente el 21
> de diciembre de 2022.

---

**La palabra que hay que subrayar es COMPLEMENTARIA**, y **la propia instrucción lo remacha**: **la
utilización de estos dispositivos no constituye por sí misma una medida de protección completa y
requiere el empleo de una de las medidas de los apartados 3.1 a 3.4** —aislamiento, envolventes,
obstáculos o alejamiento—. **Un diferencial no autoriza a dejar un conductor accesible.**

**Frente a los contactos INDIRECTOS, en cambio, el diferencial sí es la medida principal**, y **eso
enlaza con el epígrafe siguiente.**

**Las clases de diferencial, que es lo que un técnico elige hoy y no hace veinte años:**

| Clase | Qué detecta |
|---|---|
| **AC** | **Sólo corrientes de defecto alternas senoidales** |
| **A** | **Alternas senoidales Y continuas PULSANTES** |
| **B** | **Además, corrientes continuas lisas** |
| **Superinmunizado o selectivo S** | **Retardado**, para dar selectividad con los de aguas abajo |

**La instrucción prevé expresamente la clase A cuando la corriente de defecto pueda no ser senoidal**,
y **la lectura de oficio que hay que dar es la que un examen buscaría**: **una instalación llena de
electrónica —variadores, fuentes conmutadas, alumbrado electrónico— produce corrientes de defecto que
un diferencial de clase AC puede no ver.** **Ésa es la razón por la que las clases A se han
generalizado**, y **una casa que emite es exactamente ese caso.**

**Y el aviso de mantenimiento, que es del tema 9 y aquí se anuncia**: **un diferencial tiene un botón
de prueba y hay que accionarlo periódicamente.** **Un diferencial que lleva años sin disparar puede
estar agarrotado**, y **el botón de prueba comprueba el mecanismo, no la instalación.**

## 4. Los esquemas de conexión del neutro

**No se puede elegir una protección sin saber en qué esquema se está**, y **la instrucción lo dice de
entrada**: **la coordinación entre el esquema de conexiones a tierra y las características de los
dispositivos de protección es obligada.**

**La nomenclatura, que es lo más preguntable del epígrafe:**

| Letra | Posición | Qué significa |
|---|---|---|
| **T** | **Primera** | **Conexión directa de un punto de la ALIMENTACIÓN a tierra** |
| **I** | **Primera** | **Aislamiento de todas las partes activas de la alimentación**, o conexión a través de una impedancia |
| **T** | **Segunda** | **Masas de la instalación conectadas DIRECTAMENTE a tierra** |
| **N** | **Segunda** | **Masas conectadas al punto de la alimentación puesto a tierra** |
| **S** | **Tercera** | **Neutro y protección por conductores SEPARADOS** |
| **C** | **Tercera** | **Neutro y protección COMBINADOS en un solo conductor** |

**Los tres esquemas, con lo que decide en cada uno la protección:**

| Esquema | Cómo es | Qué corriente da un defecto fase-masa | Qué protege |
|---|---|---|---|
| **TN** | **Alimentación a tierra y masas unidas a ese mismo punto** por conductores de protección | **Es una CORRIENTE DE CORTOCIRCUITO**: el bucle es todo metálico | **Los dispositivos de sobreintensidad** bastan, si el bucle es suficientemente bajo |
| **TT** | **Alimentación a tierra y masas a una tierra SEPARADA** | **Menor que un cortocircuito**, porque el bucle pasa por dos tomas de tierra | **El DIFERENCIAL**: es el esquema en que resulta imprescindible |
| **IT** | **Alimentación AISLADA de tierra, masas a tierra** | **Muy pequeña en el PRIMER defecto** | **Un controlador permanente de aislamiento avisa**; el segundo defecto sí hay que cortarlo |

**El TT es el esquema de las instalaciones alimentadas desde la red pública en España**, y **de ahí que
el diferencial sea aquí obligatorio y no opcional.**

**El IT merece una línea porque es el de los quirófanos y el de ciertas instalaciones críticas**, y
**la razón se dice en una frase**: **es el único esquema en el que un primer defecto NO obliga a
cortar el suministro.** **Se detecta, se avisa y se repara sin apagar.** **Eso es lo que se busca
donde una interrupción es peor que el defecto**, y **una continuidad de emisión es un caso de esa
familia.**

## 5. La puesta a tierra

**El enunciado la nombra la segunda y tiene su propia instrucción.** **La definición es la cita del
epígrafe:**

> «**La puesta o conexión a tierra es la unión eléctrica directa, sin fusibles ni protección alguna, de
> una parte del circuito eléctrico o de una parte conductora no perteneciente al mismo mediante una
> toma de tierra con un electrodo o grupos de electrodos enterrados en el suelo.**»
>
> — Real Decreto 842/2002, **ITC-BT-18**, apartado 2 (`BOE-A-2002-18099`), redacción vigente el 21 de
> diciembre de 2022.

---

**Las cinco palabras que hay que subrayar son «SIN FUSIBLES NI PROTECCIÓN ALGUNA»**, y **hay que saber
decir por qué**: **un conductor de protección con un fusible sería un conductor de protección que
puede quedar interrumpido sin que nadie se entere.** **La tierra tiene que ser un camino permanente,
incondicional y comprobable.**

**Para qué sirve, del objeto de la propia instrucción**: **limitar la tensión que las masas metálicas
puedan presentar respecto a tierra**, **asegurar la actuación de las protecciones** y **eliminar o
disminuir el riesgo de una avería.**

**Las partes de una instalación de puesta a tierra, en orden desde el terreno:**

| Parte | Qué es |
|---|---|
| **Electrodo o TOMA DE TIERRA** | **Lo enterrado**: picas, placas, conductores desnudos, mallas, armaduras del hormigón |
| **Conductor de tierra** | **Del electrodo al borne principal**, no enterrado |
| **BORNE o punto de puesta a tierra** | **El punto de reunión, con dispositivo de separación para poder MEDIR** |
| **Conductores de PROTECCIÓN** | **Del borne a cada masa** |
| **Conductores de EQUIPOTENCIALIDAD** | **Unen entre sí las masas y los elementos conductores ajenos** |

**El borne con dispositivo de separación es el detalle que un examen puede perseguir**, y **su razón es
de mantenimiento**: **sin poder separar el electrodo del resto no se puede medir su resistencia
aislada.** **Eso es del tema 9.**

**La resistencia de la toma de tierra**: **la instrucción dedica un apartado a ella y no fija un valor
único**, porque **el valor exigible depende de la sensibilidad de la protección que tiene que actuar y
de la tensión de contacto admisible.** **La tensión límite convencional de la instrucción de contactos
es de 50 voltios eficaces en condiciones normales**, y **de 24 voltios en los casos que la propia
norma señala.** **La relación entre esa tensión, la resistencia de tierra y la sensibilidad del
diferencial es la que decide el valor**, y **el temario no la reduce a una cifra fija.**

**Y la equipotencialidad, que es la medida más barata y la peor entendida**: **unir entre sí todas las
masas y elementos conductores de una zona hace que, si aparece una tensión, TODO suba a la vez** y
**no haya diferencia de potencial entre dos cosas que una persona pueda tocar a la vez.** **La
seguridad no está en que no haya tensión: está en que no haya DIFERENCIA de tensión.**

## 6. La protección contra contactos

**La instrucción distingue dos peligros y hay que separarlos bien:**

| | **Contacto DIRECTO** | **Contacto INDIRECTO** |
|---|---|---|
| **Qué se toca** | **Una parte ACTIVA**: un conductor con tensión de servicio | **Una MASA que se ha puesto en tensión por un fallo de aislamiento** |
| **Es un fallo de** | **La instalación como barrera** | **El aislamiento de un equipo** |
| **Se previene con** | **Aislamiento, envolventes, obstáculos, alejamiento** y, como complemento, **diferencial de 30 mA** | **Corte automático de la alimentación, clase II, locales no conductores, equipotencialidad local o separación eléctrica** |

**Y la medida que protege de los DOS a la vez, que es la que la instrucción pone primero**: **la muy
baja tensión de seguridad.** **Si la tensión no puede ser peligrosa, no importa qué se toque.**

**Los grados de protección de las envolventes**, que enlazan con el tema 4: **las partes activas deben
estar en el interior de envolventes o detrás de barreras con, como mínimo, el grado IP XXB**, y **las
superficies superiores horizontales fácilmente accesibles deben responder como mínimo al IP4X o
IP XXD.**

**La lectura de oficio de esa diferencia, que es de las que un examen premia**: **la cara superior de
un cuadro pide MÁS grado que sus laterales**, y **la razón es obvia en cuanto se dice: sobre una
superficie horizontal caen cosas.** **Un destornillador dejado encima de un cuadro es exactamente el
riesgo que ese IP4X previene.**

**Y la condición de apertura, que es la que separa un cuadro de una caja**: **cuando sea necesario
suprimir las barreras o abrir las envolventes, sólo debe ser posible con la ayuda de una llave o de
una herramienta, o después de quitar la tensión**, o **con una segunda barrera detrás.** **Una tapa
que se abre con la mano y deja partes activas a la vista incumple.**

## 7. Los aparatos de maniobra

**El enunciado nombra los interruptores de maniobra aparte de las protecciones**, y **la distinción es
la que ordena el epígrafe:**

| Aparato | Qué puede hacer | Qué NO puede hacer |
|---|---|---|
| **SECCIONADOR** | **Establecer una separación VISIBLE y segura**, en vacío | **NO corta corriente**: se maniobra sin carga |
| **INTERRUPTOR** | **Abrir y cerrar corrientes NORMALES de servicio** | **No corta un cortocircuito** |
| **INTERRUPTOR-SECCIONADOR** | **Las dos cosas**: corta en carga y da separación | — |
| **CONTACTOR** | **Abrir y cerrar corrientes de servicio A DISTANCIA y con mucha frecuencia** | **No protege** |
| **INTERRUPTOR AUTOMÁTICO** | **Cortar corrientes de defecto** y maniobrar | — |
| **FUSIBLE** | **Cortar un cortocircuito fundiéndose** | **No se rearma; no maniobra** |

**Las dos reglas de oficio que resumen la tabla:**

1. **Un seccionador no se maniobra en carga.** **Abrirlo con corriente produce un arco que no está
   diseñado para extinguir**, y **es el accidente clásico del cuadro de un centro de
   transformación.** **La maniobra correcta es: cortar con el interruptor, seccionar con el
   seccionador.**
2. **Maniobrar y proteger son dos funciones.** **Un contactor abre mil veces al día y no protege
   nada**; **un magnetotérmico protege y no está hecho para abrir mil veces al día.** **En un cuadro
   de motores están los dos, y cada uno hace lo suyo.**

**Y el vocabulario del contactor, que es la base del automatismo del epígrafe siguiente:**

| Parte del contactor | Qué es |
|---|---|
| **Bobina** | **El electroimán que lo cierra**; se alimenta del circuito de MANDO |
| **Contactos PRINCIPALES o de potencia** | **Los que llevan la corriente de la carga** |
| **Contactos AUXILIARES** | **Los que informan y enclavan**: normalmente abiertos y normalmente cerrados |

## 8. Automatismos y cuadros

**Todo automatismo eléctrico clásico separa DOS circuitos**, y **entenderlo es entender el punto:**

| Circuito | Qué lleva | Cómo se dibuja |
|---|---|---|
| **De POTENCIA o de fuerza** | **La corriente que alimenta la carga** | **Trazo grueso**; pocas líneas |
| **De MANDO o de control** | **La corriente que gobierna las bobinas** | **Trazo fino**; muchas líneas y contactos |

**Los dos esquemas elementales que hay que saber dibujar y leer:**

| Esquema | Qué hace |
|---|---|
| **Marcha-paro con REALIMENTACIÓN** | **Un pulsador de marcha cierra el contactor y un contacto auxiliar suyo lo mantiene cerrado**; un pulsador de paro en serie lo abre |
| **INVERSIÓN DE GIRO** | **Dos contactores que permutan dos fases**, con **enclavamiento** entre ambos |

**El ENCLAVAMIENTO es el concepto de seguridad del epígrafe**, y **hay que saber que hay dos y que se
usan los dos a la vez:**

| Tipo | Cómo se hace | Qué garantiza |
|---|---|---|
| **ELÉCTRICO** | **Un contacto auxiliar normalmente cerrado de cada contactor en serie con la bobina del otro** | **Que la lógica no pueda dar la orden de cerrar los dos** |
| **MECÁNICO** | **Una pieza física que impide el cierre simultáneo** | **Que no cierren los dos aunque la lógica falle o un contacto se pegue** |

**Y por qué hacen falta los dos, que es la respuesta que un examen busca**: **el eléctrico protege del
error de mando; el mecánico protege del fallo del aparato.** **Un contacto auxiliar soldado deja sin
efecto el enclavamiento eléctrico**, y **entonces sólo queda el mecánico.** **En la inversión de giro
y en el arranque estrella-triángulo del tema 2, cerrar los dos contactores a la vez es un
cortocircuito entre fases.**

**El cuadro eléctrico, y lo que un técnico de esta ocupación tiene que saber de su montaje:**

| Regla | Por qué |
|---|---|
| **Separación de potencia y mando** | **Evita acoplamientos y facilita el mantenimiento** |
| **Identificación de TODO**: bornes, conductores, aparatos | **Un cuadro sin marcar no se puede mantener**; enlaza con el tema 13 |
| **Colores normalizados de conductores** | **Azul el neutro; amarillo-verde el de protección**; los de fase, los restantes |
| **Reserva de espacio y de carril** | **Una instalación siempre crece** |
| **Esquema DENTRO del cuadro y actualizado** | **Es el documento que usa quien venga después** |
| **Grado IP adecuado al emplazamiento** | Materia del tema 4 |

**El amarillo-verde tiene una regla adicional que hay que decir**: **ese color está RESERVADO al
conductor de protección y no se puede usar para ninguna otra cosa.** **Es la única identificación de
color que es exclusiva.**

## 9. La conmutación sin paso por cero

**El enunciado la nombra expresamente y es el asunto más específico del punto**, **el que menos aparece
en un temario general de electricidad y el que más tiene que ver con una casa que emite.**

**El problema, planteado primero**: **cuando hay que pasar una carga de una fuente a otra —de red a
grupo, de red a un sistema de alimentación ininterrumpida, de una línea a otra— la conmutación
convencional CORTA un instante.** **Para un alumbrado eso es un parpadeo; para una emisión en directo
o para un servidor, es una caída.**

**Qué es la conmutación sin paso por cero**: **la transferencia de la carga de una fuente a otra SIN
que la tensión se anule en la salida**, es decir, **sin que el receptor llegue a quedarse sin
alimentación.**

**Las dos condiciones que la hacen posible, y hay que saber decirlas:**

1. **Las dos fuentes tienen que estar SINCRONIZADAS**: **misma tensión, misma frecuencia y mismo
   ángulo de fase**, dentro de una ventana estrecha.
2. **La transferencia se hace con un solapamiento controlado**: **la segunda fuente se conecta antes de que
   la primera se desconecte**, durante un tiempo mínimo.

**Y el peligro que esas condiciones evitan**: **conectar en paralelo dos fuentes que no están en fase
es unir dos tensiones distintas a través de casi nada.** **La corriente que circula sólo la limita la
impedancia de las fuentes y del cableado**, y **el resultado es un cortocircuito, con daño mecánico en
las máquinas.**

**Las familias de conmutador, ordenadas por lo que hacen:**

| Tipo | Qué hace | Corte |
|---|---|---|
| **Conmutador manual con enclavamiento** | **Tres posiciones: red, cero, grupo** | **Corte largo**; el cero existe para que no se puedan unir |
| **Conmutador automático de corte** | **Detecta el fallo y transfiere** | **Corte breve**, de segundos |
| **Conmutación SOLAPADA sincronizada** | **Transfiere sin corte** con las dos fuentes en fase | **Sin corte** |
| **Conmutador estático** | **Semiconductores en vez de contactos**: transfiere en milisegundos | **Prácticamente sin corte** |

**Y la lectura que cierra el punto y enlaza con los temas 11 y 12**: **un grupo electrógeno resuelve la
AUTONOMÍA y un sistema de alimentación ininterrumpida resuelve la CONTINUIDAD, y no son lo mismo.**
**El grupo tarda en arrancar y en tomar carga; el sistema de alimentación ininterrumpida cubre ese
hueco.** **La conmutación sin paso por cero es lo que hace que el paso de uno a otro no se note**, y
**en una instalación de emisión ése es exactamente el objetivo.**

## 10. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **De la ITC-BT-22**, el primer párrafo del apartado 1.1 con sus tres causas y el párrafo de dispositivos de la letra a) · **de la ITC-BT-24**, el párrafo de los 30 mA del apartado 3.5 · **de la ITC-BT-18**, la definición del apartado 2 |

**Un aviso de método que este tema tiene que dar, y que vale para toda esta ocupación**: **la lente de
exactitud de este proyecto ancla sus comprobaciones en marcadores del tipo «Artículo N», y las
instrucciones técnicas complementarias NO numeran por artículos, sino por apartados del tipo 1.1 o
3.5.** **Eso significa que la lente NO puede comprobar automáticamente las citas de instrucción
técnica**, y **el cero que devolvería sobre ellas no diría nada.** **Las tres citas de este tema se
han comprobado como subcadena literal contra el volcado de la norma**, y **el informe de refutación de
esta ocupación explica cómo y da la cuenta.** **La laguna de la herramienta queda anotada en
`PENDIENTES.md`.**

**Cinco declaraciones expresas:**

1. **Este tema NO da los múltiplos de disparo magnético de las curvas B, C y D**, ni **poderes de
   corte**, ni **calibres**, ni **secciones mínimas de conductor de protección**, ni **valores de
   resistencia de tierra.** **Son dato de norma de producto, de tabla de instrucción técnica o de
   fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.** **Lo que el temario da
   es el ORDEN y el criterio.**
2. **Los dos valores que sí se dan son los que las instrucciones citadas contienen**: **los 30 mA del
   diferencial de alta sensibilidad** y **la tensión límite convencional de 50 voltios eficaces, con
   los 24 voltios de los casos que la propia instrucción señala.**
3. **Los apartados que se resumen y no se citan van identificados uno a uno** —de la ITC-BT-08, el 1
   entero con sus tres esquemas; de la ITC-BT-18, el 1, el 3, el 8, el 9 y el 10; de la ITC-BT-22, el
   1.1.b); de la ITC-BT-24, el 2, el 3.1, el 3.2, el 3.5 y el 4—. **Todos están en la norma citada
   arriba.**
4. **La ITC-BT-23, de protección contra sobretensiones, se nombra por lo que regula y no se cita**:
   **el temario sólo dice que es donde están los protectores contra sobretensiones**, que es lo que
   la ITC-BT-22 dice de las descargas atmosféricas.
5. **Las normas que estas instrucciones invocan se nombran y no se han consultado**: **la serie UNE
   20.460 en sus partes 4-41, 4-43 y 4-473**, **la UNE 20.324 de grados de protección**, **la UNE
   20.481** y **la UNE 20.572-1.** **El temario sólo afirma de ellas lo que las instrucciones citadas
   dicen.**

**El resto del tema va como oficio y así se declara**: la tabla que separa la protección de la
instalación de la protección de las personas, la explicación física de por qué un solo mecanismo no
puede cubrir sobrecarga y cortocircuito, la lectura de que el cortocircuito se puede proteger aguas
arriba y la sobrecarga no, la advertencia sobre el poder de corte y su relación con la distancia al
transformador, la explicación del funcionamiento del diferencial por suma de corrientes, la lectura de
las clases de diferencial en una instalación con electrónica, el aviso sobre el botón de prueba, la
lectura de que el TT hace imprescindible el diferencial y de que el IT permite no cortar al primer
defecto, el subrayado de las palabras «sin fusibles ni protección alguna», la explicación del borne
con dispositivo de separación como condición para medir, la lectura de la equipotencialidad como
ausencia de DIFERENCIA de tensión, la explicación de por qué la cara superior de un cuadro pide más
grado de protección, las dos reglas del seccionador y del contactor, la razón de que hagan falta los
dos enclavamientos, las seis reglas de montaje de un cuadro y el planteamiento entero de la
conmutación sin paso por cero con sus dos condiciones y su peligro. **Nada de eso lo dice la norma con
esas palabras**, y el tema no lo presenta como si lo dijera.
