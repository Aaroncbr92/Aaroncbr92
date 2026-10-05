# Tema 14 del específico de Oficial Técnico Electricista · Medidas eléctricas e instrumentación: multímetro, pinza amperimétrica, telurómetro, medidor de aislamiento, analizador de redes y termografía básica

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 14 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Real Decreto 842/2002, de 2 de agosto, Reglamento electrotécnico para baja tensión: ITC-BT-03 (apéndice I), ITC-BT-05, ITC-BT-18, ITC-BT-19 (apartado 2.9) e ITC-BT-24. Real Decreto 614/2001, de 8 de junio, anexos I, II, IV y V. Guía técnica del INSST sobre riesgo eléctrico (2020). Documentación técnica de fabricantes de instrumentos (Fluke, Chauvin Arnoux-AEMC, Circutor, FLIR). Lo demás es oficio, y así se declara |
| **Redacción que se estudia** | La vigente el 24/09/2026. Del REBT: ITC-BT-03 en la redacción del Real Decreto 770/2025 (vigente desde el 04/09/2025; el apéndice I.2, que es el que se cita, no cambió); ITC-BT-05 en la del Real Decreto 1053/2014 (desde el 30/06/2015); ITC-BT-18 en la del Real Decreto 560/2010 (desde el 23/05/2010); ITC-BT-19 e ITC-BT-24, redacción única de 2002 (desde el 18/09/2003). El Real Decreto 614/2001 tiene una sola redacción |
| **Extensión** | Unas 9.000 palabras |

<!-- /portada -->

Siglas y símbolos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**); Instituto Nacional de
Seguridad y Salud en el Trabajo (**INSST**); Asociación Española de Normalización (**UNE**), norma
europea (**EN**) y Comisión Electrotécnica Internacional (**IEC**); categoría de medida de un
instrumento (**CAT I** a **CAT IV**); verdadero valor eficaz (**TRMS**, *true root mean square*);
interruptor diferencial (**ID**; en la documentación de los fabricantes, **RCD**, *residual current
device*); muy baja tensión de seguridad y de protección (**MBTS** y **MBTP**); conductor de
protección (**PE**); esquemas de conexión a tierra (**TT**, **TN**, **IT**); sistema de alimentación
ininterrumpida (**SAI**); centro de proceso de datos (**CPD**). Magnitudes: corriente
diferencial-residual asignada (**IΔn**), corriente que asegura el funcionamiento del dispositivo
(**Ia**), resistencia de tierra de las masas (**RA**), tensión de contacto límite convencional
(**U** o **UL**), impedancia del bucle de defecto (**Zs**), tensión entre fase y tierra (**U0**),
resistividad del terreno (**ρ**), factor de potencia y coseno de fi (**cos φ**), emisividad
(**ε**). Unidades: voltio (**V**), amperio (**A**), miliamperio (**mA**), ohmio (**Ω**),
megaohmio (**MΩ**), ohmio por metro (**Ω·m**), milisegundo (**ms**), grado Celsius (**°C**),
milikelvin (**mK**), hercio y kilohercio (**Hz**, **kHz**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 14):
>
> Medidas eléctricas e instrumentación: multímetro, pinza amperimétrica, telurómetro, medidor de
> aislamiento, analizador de redes y termografía básica.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: quién puede hacer mediciones según el Real Decreto 614/2001 y si una
medición es o no un trabajo en tensión; qué instrumentos exige la ITC-BT-03 a una empresa
instaladora básica y cuáles añade la especialista; qué es la categoría de medida de un instrumento
y cuál corresponde a la cabecera de una instalación; cómo se conectan voltímetro y amperímetro y por
qué; qué es un instrumento de verdadero valor eficaz y cuándo hace falta; qué pinza mide continua;
cómo se busca una fuga con la pinza; qué resistencia de tierra admite un diferencial de 30 o de
300 mA en un esquema TT; dónde está el borne de medida de la tierra; cómo se hace el método de
caída de potencial, la regla del 62 % y la comprobación de que la pica de tensión está bien
puesta; cuándo y con qué periodicidad se revisa la tierra según la ITC-BT-18; qué pasa si se mide
sin separar el electrodo; qué hace y qué no la pinza de tierra; los valores de la tabla 3 de la
ITC-BT-19 (250 V/0,25 MΩ, 500 V/0,5 MΩ, 1000 V/1 MΩ), la regla de los 100 metros, la polaridad del
generador y qué se hace con los circuitos electrónicos; el ensayo de rigidez (2U + 1000 V, mínimo
1.500 V, 1 minuto); qué exige el anexo IV del Real Decreto 614/2001 cuando se usa una fuente de
tensión exterior; qué mide un analizador de redes y para qué se deja registrando; y en termografía,
por qué se hace en carga, qué es la emisividad, qué falsea una lectura y cómo se organiza un
programa de inspección. En la prueba práctica: elegir el instrumento para una tarea, describir una
medida de tierra o de aislamiento paso a paso, interpretar una lectura (una resistencia de
aislamiento baja, una corriente de neutro alta, un punto caliente), calcular la tierra máxima de un
TT o comprobar un diferencial con el comprobador de instalaciones.

<!-- indice -->

<!-- /indice -->

## 1. Medidas eléctricas e instrumentación

### 1.1 Qué es medir y quién puede hacerlo

El Real Decreto 614/2001, de riesgo eléctrico, define la actividad en su anexo I, apartado 10:
**Mediciones, ensayos y verificaciones: actividades concebidas para comprobar el cumplimiento de las
especificaciones o condiciones técnicas y de seguridad necesarias para el adecuado funcionamiento de
una instalación eléctrica, incluyéndose las dirigidas a comprobar su estado eléctrico, mecánico o
térmico, eficacia de protecciones, circuitos de seguridad o maniobra, etc.**

La definición cubre todo el enunciado de este tema: el estado eléctrico (multímetro, pinza,
analizador de redes), la eficacia de protecciones (telurómetro, medidor de aislamiento, comprobador
de diferenciales) y el estado térmico (termografía).

Dos consecuencias jurídicas que un tribunal puede preguntar:

1. **Una medición no es un trabajo en tensión.** La definición de trabajo en tensión del mismo
   anexo (apartado 8) termina así: **No se consideran como trabajos en tensión las maniobras y las
   mediciones, ensayos y verificaciones definidas a continuación.** Tienen su propio régimen, el
   del anexo IV.
2. **Sólo las hace un trabajador autorizado.** Anexo IV, A.1: **Las maniobras locales y las
   mediciones, ensayos y verificaciones sólo podrán ser realizadas por trabajadores autorizados. En
   el caso de las mediciones, ensayos y verificaciones en instalaciones de alta tensión, deberán ser
   trabajadores cualificados, pudiendo ser auxiliados por trabajadores autorizados, bajo su
   supervisión y control.**

Las dos figuras, en el anexo I del mismo real decreto:

| Figura | Definición (anexo I) |
|---|---|
| Trabajador autorizado (apartado 13) | **trabajador que ha sido autorizado por el empresario para realizar determinados trabajos con riesgo eléctrico, en base a su capacidad para hacerlos de forma correcta, según los procedimientos establecidos en este Real Decreto.** |
| Trabajador cualificado (apartado 14) | **trabajador autorizado que posee conocimientos especializados en materia de instalaciones eléctricas, debido a su formación acreditada, profesional o universitaria, o a su experiencia certificada de dos o más años.** |

La regla, resumida: en baja tensión basta el autorizado; en alta tensión mide el cualificado, y el
autorizado sólo puede auxiliarle bajo su supervisión. La autorización la da el empresario; no es
un carné oficial.

El resto del apartado A del anexo IV fija las condiciones de cualquier medición:

- A.2: **El método de trabajo empleado y los equipos y materiales de trabajo y de protección
  utilizados deberán proteger al trabajador frente al riesgo de contacto eléctrico, arco eléctrico,
  explosión o proyección de materiales.** Entre los equipos, la letra b) nombra **Los útiles
  aislantes o aislados (herramientas, pinzas, puntas de prueba, etc.).**
- A.3: los equipos se elegirán **teniendo en cuenta las características del trabajo y, en
  particular, la tensión de servicio, y se utilizarán, mantendrán y revisarán siguiendo las
  instrucciones de su fabricante.** Por eso el manual del instrumento no es papel de la caja:
  la norma remite a él.
- A.4: **Los trabajadores deberán disponer de un apoyo sólido y estable, que les permita tener las
  manos libres, y de una iluminación que les permita realizar su trabajo en condiciones de
  visibilidad adecuadas.**
- A.5: **La zona de trabajo deberá señalizarse y/o delimitarse adecuadamente, siempre que exista la
  posibilidad de que otros trabajadores o personas ajenas penetren en dicha zona y accedan a
  elementos en tensión.** En una sala técnica con personal de producción entrando y saliendo, es
  lo normal.
- A.6: al aire libre, las medidas preventivas tendrán en cuenta **las posibles condiciones
  ambientales desfavorables**. Afecta a la medida de tierras y a la revisión de un centro emisor.

Y para medir hay que abrir: el anexo V, B.1.2, dice que **La apertura de celdas, armarios y demás
envolventes de material eléctrico estará restringida a trabajadores autorizados**. Quitar la tapa
de un cuadro para una termografía ya es una operación reservada.

La guía técnica del INSST, al comentar el anexo IV, añade criterios que no son norma pero sí la
interpretación del organismo técnico: para cada prueba **que suponga un grado relevante de
complejidad se debería planificar un procedimiento que garantice su realización de manera segura**,
y pone el ejemplo contrario: **en principio no sería necesario planificar un procedimiento para
realizar medidas triviales de tensión o de intensidad en un sencillo circuito eléctrico en baja
tensión**. Ese procedimiento debería incluir, al menos, **Delimitación y señalización de la zona de
trabajo**, **Aspectos relacionados con la puesta a tierra** y **Forma de utilizar los equipos de
pruebas**.

### 1.2 Los instrumentos que el REBT exige

El REBT no regula cómo se mide, salvo el aislamiento (epígrafe 5); pero sí dice con qué
instrumentos tiene que contar una empresa instaladora. Es la lista que mejor responde a la
pregunta «qué instrumentos debe conocer un electricista». ITC-BT-03, apéndice I, apartado 2.1.2,
para la categoría básica:

> **– Telurómetro;**
> **– Medidor de aislamiento, según ITC MIE-BT 19;**
> **– Multímetro o tenaza, para las siguientes magnitudes:**
> **Tensión alterna y continua hasta 500 V;**
> **Intensidad alterna y continua hasta 20 A;**
> **Resistencia;**
> **– Medidor de corrientes de fuga, con resolución mejor o igual que 1 mA;**
> **– Detector de tensión;**
> **– Analizador registrador de potencia y energía para corriente alterna trifásica, con capacidad
> de medida de las siguientes magnitudes: potencia activa; tensión alterna; intensidad alterna;
> factor de potencia;**
> **– Equipo verificador de la sensibilidad de disparo de los interruptores diferenciales, capaz de
> verificar la característica intensidad-tiempo;**
> **– Equipo verificador de la continuidad de conductores;**
> **– Medidor de impedancia de bucle, con sistema de medición independiente o con compensación del
> valor de la resistencia de los cables de prueba y con una resolución mejor o igual que 0,1 Ω;**
> **– Herramientas comunes y equipo auxiliar;**
> **– Luxómetro con rango de medida adecuado para el alumbrado de emergencia**
>
> — Real Decreto 842/2002, ITC-BT-03, apéndice I, apartado 2.1.2.

La categoría especialista (apartado 2.2) añade, **según proceda**: **– Analizador de redes, de
armónicos y de perturbaciones de red;** **– electrodos para la medida del aislamiento de los
suelos;** **– aparato comprobador del dispositivo de vigilancia del nivel de aislamiento de los
quirófanos;**

(La referencia «ITC MIE-BT 19» usa la numeración del reglamento anterior a 2002; la medida de
aislamiento vigente está en la ITC-BT-19, apartado 2.9, y se cita así en todo el tema.)

Cómo se reparte esa lista en este tema:

| Instrumento de la ITC-BT-03 | Epígrafe |
|---|---|
| Multímetro o tenaza; detector de tensión | 2 |
| Tenaza (pinza); medidor de corrientes de fuga | 3 |
| Telurómetro | 4 |
| Medidor de aislamiento | 5 |
| Analizador registrador de potencia y energía; analizador de redes, de armónicos y de perturbaciones | 6 |
| Verificador de diferenciales, de continuidad y medidor de impedancia de bucle | 1.5 |
| Luxómetro | Tema 6 (alumbrado de emergencia) |

Dos observaciones de lectura. La primera: la cámara termográfica **no** está en la lista; la
termografía es una técnica de mantenimiento, no una exigencia del REBT (epígrafe 7). La segunda:
la lista fija mínimos para una empresa instaladora; no dice qué instrumentos tiene un servicio de
mantenimiento propio como el de la RTVA, y ningún documento publicado de la RTVA o de CSRTV lo
dice.

### 1.3 Medir en tensión o sin tensión

La primera decisión de cualquier medida no es el instrumento, sino el estado de la instalación.
Antes de medir hay que decidir si se mide en tensión o sin tensión, y si es sin tensión, hay que
aplicar las cinco reglas de oro. La comprobación de ausencia de tensión es, ella misma, una medida
en tensión.

| Medida | Estado de la instalación |
|---|---|
| Aislamiento con megóhmetro | Sin tensión y descargada |
| Termografía y análisis de red | En carga y en su régimen normal |

La razón: el aislamiento se mide inyectando una tensión propia y compararía mal con la de la red;
el punto caliente y el armónico sólo existen cuando circula corriente. Una termografía hecha con la
instalación parada no vale para nada, y es un error frecuente en un mantenimiento mal planificado.

El cuadro completo de los instrumentos del tema (oficio, salvo donde se cita la norma):

| Medida | Estado | Por qué |
|---|---|---|
| Tensión con multímetro | En tensión | Es lo que se mide |
| Corriente con pinza | En tensión y en carga | Sin carga no circula corriente |
| Resistencia y continuidad con multímetro o verificador | Sin tensión | El instrumento inyecta su propia corriente; la tensión de red lo daña o falsea la lectura |
| Resistencia de tierra con telurómetro | Electrodo separado del resto (epígrafe 4) | El telurómetro inyecta su propia corriente |
| Aislamiento | Sin tensión, separada de la alimentación (ITC-BT-19, 2.9) | El medidor inyecta su propia tensión continua |
| Disparo de diferencial con comprobador | En tensión | El comprobador provoca una fuga real desde la red |
| Analizador de redes y termografía | En carga y régimen normal | Lo que se busca sólo aparece con corriente |

La ausencia de tensión se comprueba con un detector concebido para ello. La guía del INSST cita
como norma posible para baja tensión **la norma UNE-EN 61243-3, para detectores de tensión para
baja tensión bipolares**, y recuerda que, antes de usarlo, **es importante comprobar su tensión o
gama de tensiones nominales de funcionamiento, así como el estado de las puntas de prueba y de las
pilas o baterías**. Y que la verificación se haga **en todos los conductores de la instalación,
especialmente en cada una de las fases y en el conductor neutro, en caso de existir**; también
recomienda verificarla **en todas las masas accesibles susceptibles de quedar eventualmente en
tensión**.

El método de comprobación en tres pasos, recomendado por la documentación de Fluke: **Primero,
compruebe un circuito con tensión conocido. Segundo, compruebe el circuito deseado. Tercero,
compruebe nuevamente el circuito con tensión. Esto verifica que su multímetro funcionó
correctamente antes y después de la medición.** Una lectura de «cero voltios» sólo vale si se sabe
que el instrumento funciona; por eso se prueba antes y después.

### 1.4 La seguridad del propio instrumento: categorías de medida

Antes de medir hay que saber qué se va a medir y con qué categoría de medida está clasificado el
instrumento. Un polímetro de categoría insuficiente conectado en la cabecera de una instalación es
un accidente esperando el transitorio.

La categoría de medida es una clasificación de la norma de producto IEC 61010 (en España, UNE-EN
61010), que el tema no ha leído; lo que sigue está tomado de la documentación técnica de Fluke
(*El ABC de la seguridad en las mediciones eléctricas*, 2003), y se presenta como tal.

La idea: un transitorio de gran energía, como un rayo, **será atenuado o amortiguado a medida que
recorre la impedancia (resistencia de CA) del sistema**. Cuanto más cerca del origen de la
instalación, más energía puede tener el transitorio que llegue al instrumento. Por eso **Un número
más alto de CAT se refiere a un entorno eléctrico de mayor energía disponible y transitorios de más
energía.**

| Categoría | Dónde (según Fluke) |
|---|---|
| CAT IV | **«origen de la instalación»; es decir, en dónde se efectúa la conexión de baja tensión a la alimentación del servicio de energía eléctrica**: contadores, protección general, acometida |
| CAT III | **Equipos en instalaciones fijas, tales como equipos de conmutación y distribución y motores polifásicos**; cuadros de distribución, alumbrado de grandes edificios |
| CAT II | **Cargas conectadas a tomacorrientes monofásicos**: aparatos, herramientas portátiles, tomas de corriente y circuitos largos |
| CAT I | **Electrónica**: **Equipos electrónicos protegidos** |

Tres reglas prácticas de la misma fuente:

1. **cuanto más cerca se encuentre usted de la fuente de energía, más alto debe ser el número de
   la categoría**.
2. **Dentro de una categoría, una mayor tensión nominal indica una mayor calificación para soportar
   transitorios**; pero la categoría manda sobre la tensión: el error es elegir **un multímetro
   CAT II de 1000 V nominales pensando que es superior a un multímetro CAT III de 600 V**.
3. Las puntas también cuentan: **deberán estar certificadas en una categoría y tensión tan alta o
   mayor que la del multímetro**.

Aplicado a los edificios de un centro de producción (lectura de oficio): la caja general de
protección, el cuadro general y la entrada del centro de transformación son terreno de CAT IV; los
cuadros secundarios de planta, de climatización o de una sala técnica, de CAT III; las tomas de
corriente de un plató o de un rack, de CAT II; y la electrónica interna de un equipo, de CAT I. El
instrumento de un electricista de mantenimiento se elige por el sitio más exigente en el que vaya a
medir.

La documentación de Fluke recuerda además por qué la entrada de corriente de un multímetro lleva
fusible: la impedancia de entrada de un borne de 10 A es del orden de **0,01 ohmios**, frente a
**10 MΩ** en los bornes de tensión; si las puntas se dejan en el borne de corriente y se aplican a
una tensión, **la baja impedancia de entrada se convierte en un cortocircuito**. De ahí su
consejo: **Nunca reemplace un fusible quemado con un fusible incorrecto. Utilice sólo los fusibles
para alta energía especificados por el fabricante.**

### 1.5 El comprobador de instalaciones: continuidad, bucle y diferenciales

La ITC-BT-03 exige tres equipos que en el mercado suelen ir reunidos en un solo aparato, el
comprobador multifunción o de instalaciones: el **Equipo verificador de la continuidad de
conductores**, el **Medidor de impedancia de bucle** y el **Equipo verificador de la sensibilidad
de disparo de los interruptores diferenciales, capaz de verificar la característica
intensidad-tiempo**. Cada uno comprueba una condición del REBT.

**Continuidad de los conductores de protección.** Se mide sin tensión, con baja resistencia, entre
el borne de tierra del cuadro y la masa de cada receptor o el contacto de tierra de cada toma.
Comprueba que la masa está realmente unida al PE: la protección contra contactos indirectos
depende de ello (tema 5). El valor admisible depende de la longitud y la sección; el REBT no da una
cifra de continuidad, y el tema tampoco.

**Impedancia de bucle.** En un esquema TN, la condición de corte automático de la ITC-BT-24,
4.1.1, es **Zs x Ia ≤ U0**: la impedancia del bucle de defecto tiene que ser lo bastante baja para
que la corriente de defecto haga actuar la protección en el tiempo de la tabla 1 (0,4 s para U0 =
230 V). El medidor de impedancia de bucle mide Zs; la ITC-BT-03 le pide resolución de 0,1 Ω y
compensación de la resistencia de los cables de prueba, porque en un bucle de pocas décimas de
ohmio el cable del instrumento falsearía la lectura.

**Diferenciales.** El botón de prueba del diferencial comprueba el mecanismo, no la instalación ni
la tierra (tema 3). El comprobador hace algo distinto: provoca desde la red una fuga real hacia el
PE y mide. El manual del comprobador de diferenciales CDB de Circutor describe las cuatro medidas
típicas:

| Medida | Qué hace el comprobador (Circutor, manual CDB) |
|---|---|
| Tensión de contacto | Hace circular una fracción de la corriente asignada (**0,45x I∆N**) **a través de la toma de tierra sin sincronización de RCD, y comprobar que no se desconecte el RCD**, y de ahí calcula la tensión de contacto que aparecería con IΔn y la impedancia del bucle de protección |
| Tiempo de disparo a IΔn | Mide el tiempo de disparo con la corriente asignada; el rango del aparato es de **600 ms para el RCD de uso general y en un rango de 1000 ms para el RCD selectivo** |
| Tiempo de disparo a 5·IΔn | Sólo para diferenciales de 6, 10 y 30 mA; el impulso **dura como máximo 60 ms** |
| Corriente de disparo (rampa) | **la corriente de prueba I∆ empieza en 0.30 I∆N y va aumentando hasta 1.40 I∆N**: da la sensibilidad real |

Y el criterio de aceptación de la rampa, en el mismo manual: **Durante la prueba con señal alterna
todos los RCD's deben actuar a una corriente igual o inferior a I∆ N. En la prueba con corriente
pulsante, los RCD de tipo A deben disparar con corrientes de hasta 1.4 I∆N**. El comprobador
interrumpe la prueba si la tensión de contacto pasa del límite elegido (**25 V o 50 V**), que es la
salvaguarda del operador frente a una tierra mala.

Los tiempos máximos de disparo que debe cumplir cada clase de diferencial son de su norma de
producto (UNE-EN 61008-1 y 61009-1, que la ITC-BT-02 lista y el tema no ha leído); no se dan aquí.
Lo que sí da el REBT es el límite del diferencial selectivo en un TT (ITC-BT-24, 4.1.2): **con un
tiempo de funcionamiento como máximo igual a 1 s**.

Una consecuencia práctica (oficio): la prueba con comprobador hace disparar el diferencial, y con
él todo lo que cuelga de él. En una sala técnica o en un CPD se hace en una ventana pactada con
producción, con los equipos críticos alimentados por la otra rama (temas 8 y 17).

## 2. Multímetro

### 2.1 Qué mide y qué exige el REBT

| Instrumento | Qué mide |
|---|---|
| Polímetro o multímetro | Tensión, corriente, resistencia, continuidad y a veces frecuencia y capacidad |

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Polímetro o multímetro | Tensión, corriente, resistencia, continuidad | Verdadero valor eficaz ante cargas no lineales, y categoría de medida suficiente |

El mínimo reglamentario para una empresa instaladora es el de la ITC-BT-03 (epígrafe 1.2): un
**Multímetro o tenaza** que mida **Tensión alterna y continua hasta 500 V**, **Intensidad alterna
y continua hasta 20 A** y **Resistencia**. Dos lecturas de esa línea: «o tenaza» admite que la
intensidad se mida con pinza en vez de abriendo el circuito; y «continua» obliga a que, si es
tenaza, mida también continua, lo que excluye la pinza de transformador de corriente (epígrafe
3.2).

Las funciones de un multímetro en el trabajo de mantenimiento (oficio):

| Función | Uso típico del electricista | Estado del circuito |
|---|---|---|
| Tensión alterna | Tensión de red en un cuadro o en una toma; tensión entre neutro y tierra | En tensión |
| Tensión continua | Baterías del SAI y del grupo, fuentes de 24 V de mando, cargadores | En tensión |
| Intensidad | Consumo de un circuito pequeño o de mando (abriendo el circuito) | En tensión, en serie |
| Resistencia | Bobina de un contactor o un relé, resistencia de un calefactor | Sin tensión |
| Continuidad (zumbador) | Identificar un conductor, comprobar un fusible o un hilo cortado | Sin tensión |

### 2.2 Voltímetro y amperímetro: cómo se conectan

| Instrumento | Cómo se conecta | Qué resistencia interna tiene | Por qué |
|---|---|---|---|
| Voltímetro | En paralelo con el elemento a medir | Muy alta, idealmente infinita | Para no derivar corriente y no alterar el circuito |
| Amperímetro | En serie, abriendo el circuito | Muy baja, idealmente cero | Para no añadir caída de tensión |

Y el error que la regla previene, que es el más grave que se comete con un polímetro: conectar un
amperímetro en paralelo sobre una tensión es un cortocircuito a través del instrumento. La escala
de corriente de un polímetro tiene una resistencia mínima y un fusible; ése es el fusible que se
funde, y con una fuente potente detrás lo que se produce es un arco.

Las cifras de un instrumento real lo confirman: según Fluke, el borne de 10 A tiene una impedancia
de entrada de 0,01 ohmios y los de tensión, de 10 MΩ (epígrafe 1.4). Por eso, en el trabajo de
mantenimiento, la corriente de los circuitos de potencia se mide con pinza (epígrafe 3) y el
multímetro se reserva, para corriente, a circuitos de mando y de pequeña intensidad.

Tres reglas de manejo (oficio): seleccionar la función y el rango antes de conectar, y no cambiar
de función con las puntas aplicadas; al terminar una medida de corriente, devolver las puntas a los
bornes de tensión; y en tensión continua, respetar la polaridad o leer el signo.

### 2.3 Verdadero valor eficaz

El valor que muestra un instrumento en alterna, y aquí está la trampa clásica: un polímetro
convencional mide el valor medio rectificado y lo escala suponiendo una senoide perfecta. Ante una
corriente deformada —la de un variador, una fuente conmutada o un balasto electrónico— la lectura
es falsa por defecto. Lo que hay que usar es un instrumento de verdadero valor eficaz, y en una
instalación moderna, con electrónica en casi todo, ésa es la única lectura fiable.

En un centro de producción audiovisual la mayor parte de la carga es electrónica —fuentes
conmutadas de equipos de vídeo, audio e informática, alimentación de luminarias LED, SAI,
variadores de la climatización—, de modo que la corriente casi nunca es senoidal. El valor eficaz
es el que calienta el cable y el que dispara la protección (tema 1, epígrafe 3.2;
tema 3, sobrecargas); un instrumento que lo subestima lleva a dar por buena una línea cargada de
más. El instrumento TRMS lleva esa indicación en la carátula (*True RMS*); es la primera
característica que se comprueba al elegir multímetro o pinza para mantenimiento.

### 2.4 Resistencia, continuidad y ausencia de tensión

La resistencia y la continuidad se miden sin tensión, porque el instrumento usa su propia pila.
Dos avisos de oficio: una lectura de resistencia en un circuito con otros elementos en paralelo da
el paralelo, no el elemento (se desconecta un extremo para medir sólo lo que interesa); y un
condensador cargado o una tensión residual falsean la lectura y pueden dañar el instrumento (se
descarga antes, como manda el Real Decreto 614/2001 en su anexo II, B.3, para los condensadores
**que permitan una acumulación peligrosa de energía**).

¿Sirve el multímetro para comprobar la ausencia de tensión, la tercera de las cinco reglas de oro?
El REBT exige a la empresa instaladora un **Detector de tensión** distinto del multímetro (ITC-BT-03,
epígrafe 1.2), y la guía del INSST pide que el verificador se elija **entre los modelos diseñados
para tal fin** (epígrafe 1.3). La práctica segura es usar el detector bipolar, con el método de los
tres pasos; un multímetro en una función equivocada (resistencia, corriente) o con la pila agotada
puede mostrar cero con tensión presente. La consignación completa es del tema 15.

## 3. Pinza amperimétrica

### 3.1 Principio y ventajas

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Pinza amperimétrica | Corriente sin abrir el circuito | De efecto Hall si hay que medir continua |

La pinza resuelve el problema del epígrafe 2.2: medir la corriente de un circuito de potencia sin
abrirlo y sin meter el instrumento en serie. Sus tres rasgos:

| Rasgo | Qué aporta |
|---|---|
| Mide sin abrir el circuito | No hay que cortar nada ni dejar la instalación sin servicio |
| Aísla al operador del circuito | La medida se hace por el campo magnético del conductor |
| Abraza un solo conductor | Si abraza los dos, la suma es cero y no mide nada |

La mayoría de las pinzas de mantenimiento son además multímetros: llevan bornes para puntas de
prueba y miden tensión, resistencia y continuidad. Por eso la ITC-BT-03 admite **Multímetro o
tenaza** en la misma línea (epígrafe 2.1). Las puntas de una pinza tienen la misma exigencia de
categoría que las de un multímetro (epígrafe 1.4).

Cómo se mide bien (oficio): la mordaza bien cerrada y limpia; el conductor centrado en la
mordaza; lejos de otros conductores con corriente alta, cuyo campo se suma a la lectura; y, en un
cuadro, con la tapa interior que deja accesibles sólo los conductores aislados. Abrazar un
conductor aislado no es tocar una parte activa, pero meter la mordaza en un cuadro abierto sí exige
las precauciones del anexo IV del Real Decreto 614/2001 (epígrafe 1.1).

### 3.2 Tecnologías: alterna y continua

| Tecnología | Qué mide |
|---|---|
| De transformador de corriente | Sólo alterna: necesita un campo variable |
| De efecto Hall | Alterna y continua |

En el trabajo de un electricista de mantenimiento la continua aparece en las baterías de los SAI,
en las de arranque de los grupos, en los cargadores y en las instalaciones fotovoltaicas de
autoconsumo (temas 7 y 18). Para medir la corriente de carga o de descarga de una batería hace
falta una pinza de efecto Hall; una de transformador de corriente marcará cero aunque circulen
cientos de amperios. Y, como en el multímetro, la pinza tiene que ser de verdadero valor eficaz para
leer bien la corriente de cargas electrónicas (epígrafe 2.3).

### 3.3 La búsqueda de fugas

El último rasgo tiene una aplicación directa y muy útil: abrazar a la vez fase y neutro de un
circuito debería dar cero. Si no da cero, hay una corriente que se va por otro camino, es decir,
una corriente de fuga. Ésa es la medida con la que se busca una derivación que hace saltar un
diferencial.

El REBT define la **CORRIENTE DE FUGA EN UNA INSTALACIÓN** en la ITC-BT-01: **Corriente que, en
ausencia de fallos, se transmite a la tierra o a elementos conductores del circuito.** Y pone el
límite en la ITC-BT-19, apartado 2.9: **Las corrientes de fuga no serán superiores para el conjunto
de la instalación o para cada uno de los circuitos en que ésta pueda dividirse a efectos de su
protección, a la sensibilidad que presenten los interruptores diferenciales instalados como
protección contra los contactos indirectos.**

Para medir esas corrientes no basta una pinza normal: la fuga de un circuito de equipos es de
miliamperios, y una pinza de 400 o 1000 A no los resuelve. La ITC-BT-03 exige un instrumento
propio: **Medidor de corrientes de fuga, con resolución mejor o igual que 1 mA**. Es la pinza de
fugas, de mordaza mayor y muy sensible.

Cómo se busca una fuga (oficio):

1. En la cabecera del circuito, con el circuito en servicio, se abrazan juntos todos los
   conductores activos —fase y neutro en monofásico; las tres fases y el neutro en trifásico—, nunca
   el PE. La lectura es la fuga del circuito.
2. Si es alta, se baja por el circuito: se mide en cada derivación hasta encontrar la que la lleva.
3. Alternativa: abrazar sólo el conductor de protección de una masa, que lleva la fuga de ese
   receptor a tierra.
4. Se compara la fuga con la sensibilidad del diferencial que protege el circuito. La regla de la
   ITC-BT-19 citada arriba es el límite; en la práctica, una fuga permanente que se acerca a la
   sensibilidad hace que el diferencial salte al conectar una carga más.

En una sala técnica la fuga suele ser la suma de muchas fugas pequeñas y legítimas de los filtros
de las fuentes conmutadas, no un defecto (tema 3, epígrafe 3.5; tema 8, epígrafe 5.3). La pinza de
fugas permite decidir si hay que buscar una avería o repartir los equipos entre más circuitos.

### 3.4 Equilibrado de fases y corriente de neutro

Con la pinza se comprueba el reparto de cargas de un cuadro trifásico, que es el paso 4 del
procedimiento de equilibrado del tema 1 (epígrafe 8.4): con la instalación en servicio y en un
momento de carga representativo, se mide la corriente de cada fase y la del neutro en la cabecera.

Cómo se leen esas cuatro lecturas (oficio, apoyado en el tema 1, 8.2 y 8.3, y en el tema 8,
10.2):

| Lectura | Qué indica |
|---|---|
| Tres fases parecidas y neutro casi nulo | Cuadro equilibrado con cargas lineales |
| Fases distintas y neutro con corriente | Desequilibrio: hay que pasar circuitos de la fase cargada a la menos cargada (tema 1, 8.4) |
| Fases parecidas y neutro con corriente alta, a veces mayor que las fases | Armónicos múltiplos de tres de cargas no lineales: no se arregla moviendo circuitos |
| Una fase mucho más alta que su protección prevista | Sobrecarga: revisar la protección y la sección (temas 3 y 4) |

Para distinguir la tercera fila de la segunda, la pinza no basta: hace falta ver el contenido de
armónicos, y eso es del analizador de redes (epígrafe 6). Y la pinza mide un instante; el
analizador registra la evolución.

### 3.5 Los transformadores de intensidad

La pinza es, por dentro, un transformador de intensidad; los cuadros grandes llevan
transformadores de intensidad fijos para los contadores y los analizadores fijos. El Real Decreto
614/2001 tiene una regla para ellos, en su anexo II, apartado B.4.1, dentro de las disposiciones
sobre **Trabajos en transformadores y en máquinas en alta tensión**: **Se prohíbe la apertura de
los circuitos conectados al secundario estando el primario en tensión, salvo que sea necesario por
alguna causa, en cuyo caso deberán cortocircuitarse los bornes del secundario.**

Salvedad: el apartado está escrito para alta tensión. La razón física vale para cualquier
transformador de intensidad (oficio): con el secundario abierto, la corriente del primario no
encuentra la que la compensaba y en el secundario aparece una tensión peligrosa. Por eso, en baja
tensión, antes de desconectar un contador o un analizador alimentado por transformadores de
intensidad, se cortocircuitan los bornes del secundario.

## 4. Telurómetro

### 4.1 Qué se mide y qué valor se exige

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Telurómetro | Resistencia de puesta a tierra | Exige separar el electrodo del resto |

Qué se mide: la resistencia entre el electrodo y el terreno lejano, es decir, la oposición que el
terreno ofrece a que una corriente de defecto se disipe.

La ITC-BT-18, apartado 9, no fija un número de ohmios: fija lo que la resistencia tiene que
conseguir. **El electrodo se dimensionará de forma que su resistencia de tierra, en cualquier
circunstancia previsible, no sea superior al valor especificado para ella, en cada caso.** Y ese
valor **será tal que cualquier masa no pueda dar lugar a tensiones de contacto superiores a:**
**– 24 V en local o emplazamiento conductor** **– 50 V en los demás casos.**

En un esquema TT (los esquemas, tema 5), la condición se escribe en la ITC-BT-24, apartado
4.1.2: **RA x Ia ≤ U**, donde **RA es la suma de las resistencias de la toma de tierra y de los
conductores de protección de masas**, Ia es, con diferencial, **la corriente diferencial-residual
asignada**, y **U es la tensión de contacto límite convencional (50, 24V u otras, según los
casos)**.

El valor admisible de resistencia de tierra, por tanto, no es un número universal: depende de la
sensibilidad del diferencial que tiene que actuar y de la tensión de contacto admisible. Despejando
RA ≤ U / Ia (aritmética, no cifra de la norma):

| Diferencial (IΔn) | RA máxima con U = 50 V | RA máxima con U = 24 V |
|---|---|---|
| 30 mA | 50 / 0,03 ≈ 1.667 Ω | 24 / 0,03 = 800 Ω |
| 300 mA | 50 / 0,3 ≈ 167 Ω | 24 / 0,3 = 80 Ω |
| 1 A | 50 Ω | 24 Ω |

Una tierra alta con un diferencial muy sensible puede ser aceptable; la misma tierra con un
diferencial de 300 mA, no. Y una lectura que cumple la fórmula no es una buena tierra por sí sola:
la fórmula da el máximo para que actúe la protección contra contactos indirectos; la tierra
también sirve de referencia a los descargadores contra sobretensiones y a los equipos (temas 3 y
8), y para eso un valor de cientos de ohmios no ayuda. Ningún precepto leído fija un valor
«recomendado» de resistencia de tierra para un edificio; el tema no lo da.

### 4.2 El borne de medida

La medida está prevista en la propia instalación. ITC-BT-18, apartado 3.3: **Debe preverse sobre
los conductores de tierra y en lugar accesible, un dispositivo que permita medir la resistencia de
la toma de tierra correspondiente. Este dispositivo puede estar combinado con el borne principal de
tierra, debe ser desmontable necesariamente por medio de un útil, tiene que ser mecánicamente seguro
y debe asegurar la continuidad eléctrica.**

Abrir ese dispositivo es lo que separa el electrodo del resto de la instalación. Mientras está
abierto, las masas del edificio se quedan sin tierra: en un esquema TT el diferencial ya no
protegería contra un contacto indirecto. La medida se hace rápido, con la zona controlada, y el
borne se cierra y se comprueba al terminar (oficio).

### 4.3 El método de caída de potencial

| Paso | Qué se hace |
|---|---|
| 1 | Separar el electrodo del resto de la instalación, abriendo el dispositivo de medida del apartado 3.3 de la ITC-BT-18 |
| 2 | Clavar dos picas auxiliares alineadas con el electrodo: una de corriente, lejos, y una de tensión, entre medias |
| 3 | Inyectar una corriente conocida entre el electrodo y la pica de corriente |
| 4 | Medir la tensión entre el electrodo y la pica de tensión |
| 5 | Dividir tensión entre corriente: eso es la resistencia |

El telurómetro hace los pasos 3 a 5 por sí solo: genera su corriente y muestra directamente la
resistencia. Sus bornes suelen rotularse con las letras que usa la documentación de Chauvin
Arnoux-AEMC: X para el electrodo bajo prueba, Y para la pica de potencial (tensión) y Z para la de
corriente.

Y la regla que hace válida la medida, que es lo que un examen premia: la pica de tensión tiene que
estar en la zona de potencial nulo, es decir, fuera de la influencia del electrodo y fuera de la de
la pica de corriente. La comprobación práctica es mover la pica de tensión y ver si la lectura
cambia: si al desplazarla la lectura se mantiene, la medida es buena; si cambia, las picas están
demasiado cerca.

La guía de medida de tierras de Chauvin Arnoux-AEMC concreta esa regla en el llamado método del
62 %:

- La meseta de lecturas estables (el *plateau*) **es a menudo llamada el "área 62%"**: con
  electrodo y pica de corriente lo bastante separados, **las medidas se contrarestan cuando Y es
  colocado a un 62% de la distancia desde X** a la pica de corriente (así en la fuente, que escribe
  «desde X a Y» por errata).
- La comprobación: se toman lecturas con la pica de tensión al 62 % y desplazada un 10 % a cada
  lado (al 52 % y al 72 % de la distancia). Si las tres quedan dentro de la tolerancia que fije el
  operador (la guía cita **±2%, ±5%, ±10%, etc.**), la lectura del 62 % vale.
- El límite del método: **Este método es aplicable sólo cuando los tres electrodos están en línea
  recta y la tierra es un sólo electrodo, tubo, o placa**.
- La distancia a la pica de corriente: **No se puede dar una distancia específica entre X y Z**,
  porque depende del tamaño del electrodo y del terreno; la guía da tablas orientativas en pies para
  una pica de una pulgada, que no se reproducen aquí.

Si las lecturas no se estabilizan, la pica de corriente está demasiado cerca: se aleja y se repite.

### 4.4 Los dos avisos de método

1. Si no se separa el electrodo, no se mide el electrodo. Lo que se mide es el paralelo de ese
   electrodo con todo lo que esté unido a él —las tuberías, las armaduras, otros electrodos
   enlazados—, y eso da un valor menor y falso.
2. La resistencia de tierra varía con la humedad del terreno. Una medida en primavera después de
   llover y otra en agosto no dan lo mismo, y el valor que hay que garantizar es el del caso más
   desfavorable. El REBT lo recoge en la ITC-BT-18, apartado 12, **REVISIÓN DE LAS TOMAS DE
   TIERRA**:

> **Por la importancia que ofrece, desde el punto de vista de la seguridad cualquier instalación de
> toma de tierra, deberá ser obligatoriamente comprobada por el Director de la Obra o Empresa
> instaladora en el momento de dar de alta la instalación para su puesta en marcha o en
> funcionamiento.**
>
> **Personal técnicamente competente efectuará la comprobación de la instalación de puesta a
> tierra, al menos anualmente, en la época en la que el terreno esté mas seco. Para ello, se medirá
> la resistencia de tierra, y se repararán con carácter urgente los defectos que se encuentren.**
>
> **En los lugares en que el terreno no sea favorable a la buena conservación de los electrodos,
> éstos y los conductores de enlace entre ellos hasta el punto de puesta a tierra, se pondrán al
> descubierto para su examen, al menos una vez cada cinco años.**
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 12 («mas», sin tilde, así en el BOE).

Las tres cifras que hay que retener: comprobación al dar de alta la instalación; **al menos
anualmente**, en la época más seca; y electrodos al descubierto **al menos una vez cada cinco
años** donde el terreno los conserve mal. En Andalucía, la época más seca es el verano; una medida
hecha en invierno lluvioso da un valor optimista (lectura de oficio).

La guía de AEMC explica por qué: la resistividad del terreno **cambia con las estaciones** y
depende sobre todo de su contenido de agua y sales disueltas; también de la temperatura.

### 4.5 La pinza de tierra

La alternativa sin picas: la medida con pinza de tierra, que inyecta y mide sobre el propio
conductor. Su ventaja es que no hay que clavar nada ni separar el electrodo; su límite es que
necesita un bucle, es decir, otro camino de retorno a tierra, y por eso no vale en un electrodo
único y aislado.

La documentación de AEMC describe el principio de sus pinzas de tierra: el aparato aplica una
tensión al conductor de tierra a través de un transformador y mide la corriente que circula; si el
resto de tomas en paralelo tiene una resistencia conjunta mucho menor que la medida, el cociente
tensión/corriente es la resistencia de la toma que se pinza. El instrumento trabaja a **2.4kHz**
y filtra la corriente a frecuencia de red. Y una advertencia práctica de la misma guía, para sus
modelos: antes de medir la resistencia se mide la corriente que circula por el conductor de
tierra, y **Si la corriente de tierra excede 5A, las medidas de resistencia de tierra no son
posibles**; esa corriente ya es en sí un hallazgo que hay que anotar.

Lo que la lectura incluye: según la misma guía, no sólo la pica, sino también las conexiones y
uniones del camino hasta el punto de retorno. Una lectura alta puede ser una pica mala, un
conductor de tierra abierto o una unión de alta resistencia.

Cuándo usar cada método (oficio):

| Situación | Método |
|---|---|
| Electrodo único de un edificio, se puede abrir el borne de medida y hay terreno para las picas | Caída de potencial (62 %) |
| Muchas tomas en paralelo (red de picas, apoyos, sistemas enlazados) y no se puede desconectar | Pinza de tierra |
| Recinto urbano sin terreno libre para clavar picas | Pinza de tierra, si hay bucle; si no, el método de picas con las precauciones del terreno disponible |

### 4.6 La resistividad del terreno

La resistencia de un electrodo depende del electrodo y del terreno. La ITC-BT-18, apartado 9: **La
resistencia de un electrodo depende de sus dimensiones, de su forma y de la resistividad del
terreno en el que se establece. Esta resistividad varía frecuentemente de un punto a otro del
terreno, y varía también con la profundidad.**

La misma instrucción da las fórmulas de su tabla 5 para estimar la resistencia: placa enterrada
**R = 0,8 ρ/P**, pica vertical **R = ρ/L** y conductor enterrado horizontalmente **R = 2 ρ/L**
(ρ, resistividad en Ω·m; P, perímetro de la placa en m; L, longitud de la pica o del conductor en
m). Y prevé usarlas al revés: **la medida de resistencia de tierra de este electrodo puede permitir,
aplicando las fórmulas dadas en la tabla 5, estimar el valor medio local de la resistividad del
terreno.**

Ejemplo (aritmética): una pica vertical de 2 m da con el telurómetro 50 Ω. Con R = ρ/L, ρ ≈ 50 ×
2 = 100 Ω·m. Ese valor sirve para prever cuántas picas o qué longitud harían falta para bajar la
tierra: con la misma fórmula, una pica de 4 m en ese terreno daría unos 25 Ω.

Las tablas 3 y 4 de la ITC-BT-18 dan resistividades de terrenos **a título de orientación** (por
ejemplo, terrenos cultivables y fértiles, terraplenes compactos y húmedos, valor medio **50**
Ω·m; suelos pedregosos desnudos, arenas secas permeables, **3.000** Ω·m).

La resistividad también se mide directamente, con un telurómetro de cuatro bornes, por el método de
Wenner que describe la guía de AEMC: cuatro electrodos en línea a la misma distancia A; se inyecta
corriente por los exteriores y se mide la tensión entre los interiores. Si la separación es mucho
mayor que la profundidad de clavado (la guía pone la condición **A > 20 B**), la resistividad es
**ρ = 2π AR**, y representa el terreno hasta una profundidad aproximadamente igual a A. (La guía
trabaja en centímetros y Ω·cm; con A en metros, ρ sale en Ω·m.) Es la medida previa al proyecto de
una tierra nueva, por ejemplo la de un centro emisor en terreno rocoso (tema 8, 6.2).

## 5. Medidor de aislamiento

### 5.1 Qué mide y qué valores exige el REBT

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Medidor de aislamiento (megóhmetro) | Resistencia de aislamiento, con tensión continua de ensayo | La instalación, sin tensión y separada de su alimentación; los receptores, según la medida (epígrafe 5.2) |

El medidor de aislamiento aplica una tensión continua elevada entre los conductores, o entre ellos y
tierra, y mide la corriente que atraviesa el aislamiento; el cociente es la resistencia de
aislamiento, del orden de megaohmios. Es la medida que detecta un cable dañado, humedad en una
caja, un empalme mal hecho o un receptor derivado antes de que hagan saltar el diferencial.

La medida es la única que el REBT regula en detalle. ITC-BT-19, apartado 2.9: **Las instalaciones
deberán presentar una resistencia de aislamiento al menos igual a los valores indicados en la tabla
siguiente:**

| Tensión nominal de la instalación | Tensión de ensayo en corriente continua (V) | Resistencia de aislamiento (MΩ) |
|---|---|---|
| **Muy Baja Tensión de Seguridad (MBTS)** / **Muy Baja Tensión de protección (MBTP)** | **250** | **≥ 0,25** |
| **Inferior o igual a 500 V, excepto caso anterior** | **500** | **≥ 0,5** |
| **Superior a 500 V** | **1000** | **≥ 1,0** |

(ITC-BT-19, tabla 3; con la **Nota: Para instalaciones a MBTS y MBTP, véase la ITC-BT-36**.)

Una instalación de 230/400 V está en la fila central: se ensaya a 500 V en continua y tiene que
dar al menos 0,5 MΩ.

**La regla de la longitud.** Los valores de la tabla valen para un tramo limitado: **Este
aislamiento se entiende para una instalación en la cual la longitud del conjunto de canalizaciones
y cualquiera que sea el número de conductores que las componen no exceda de 100 metros.** Si es
mayor y puede fraccionarse **en partes de aproximadamente 100 metros de longitud, bien por
seccionamiento, desconexión, retirada de fusibles o apertura de interruptores**, cada parte debe
cumplir; y **Cuando no sea posible efectuar el fraccionamiento citado, se admite que el valor de
la resistencia de aislamiento de toda la instalación sea, con relación al mínimo que le
corresponda, inversamente proporcional a la longitud total, en hectómetros, de las canalizaciones.**

Ejemplo (aritmética): una instalación de 230/400 V con 300 m de canalización que no se puede
fraccionar debe dar al menos 0,5 / 3 ≈ 0,17 MΩ.

**El generador.** **El aislamiento se medirá con relación a tierra y entre conductores, mediante un
generador de corriente continua capaz de suministrar las tensiones de ensayo especificadas en la
tabla anterior con una corriente de 1 mA para una carga igual a la mínima resistencia de
aislamiento especificada para cada tensión.** Es la exigencia de producto que hace válido un
medidor: que mantenga la tensión de ensayo justo en el límite de aceptación.

### 5.2 Cómo se mide

La ITC-BT-19, apartado 2.9, describe el procedimiento. Las condiciones generales:

> **Durante la medida, los conductores, incluido el conductor neutro o compensador, estarán
> aislados de tierra, así como de la fuente de alimentación de energía a la cual están unidos
> habitualmente. Si las masas de los aparatos receptores están unidas al conductor neutro, se
> suprimirán estas conexiones durante la medida, restableciéndose una vez terminada ésta.**

Las dos medidas, que no se hacen igual:

| | Con relación a tierra | Entre conductores |
|---|---|---|
| Receptores | **dejando, en principio, todos los receptores conectados y sus mandos en posición «paro»** | **después de haber desconectado todos los receptores** |
| Interruptores y fusibles | **los dispositivos de interrupción se pondrán en posición de "cerrado" y los cortacircuitos instalados como en servicio normal** | **en la misma posición que la señalada anteriormente** |
| Conexión | **Todos los conductores se conectarán entre sí incluyendo el conductor neutro o compensador, en el origen de la instalación que se verifica y a este punto se conectará el polo negativo del generador**; tierra, al **polo positivo** | **sucesivamente entre los conductores tomados dos a dos, comprendiendo el conductor neutro o compensador** |

Y la comprobación previa a la medida a tierra: **asegurándose que no existe falta de continuidad
eléctrica en la parte de la instalación que se verifica**. Un interruptor abierto aguas abajo deja
un tramo sin medir, y la lectura buena engaña.

Lectura de la tabla (oficio): la medida a tierra se hace con todo cerrado y los receptores
conectados porque se quiere comprobar todo lo que está unido a la instalación; la medida entre
conductores se hace con los receptores fuera porque un receptor conectado entre dos conductores es,
para el medidor, una resistencia baja que no es defecto. Un error frecuente en la prueba práctica es
decir que «el megóhmetro se usa siempre con los receptores desconectados»: el REBT dice lo contrario
para la medida a tierra.

### 5.3 Los circuitos con electrónica

> **Cuando la instalación tenga circuitos con dispositivos electrónicos, en dichos circuitos los
> conductores de fases y el neutro estarán unidos entre sí durante las medidas.**
>
> — Real Decreto 842/2002, ITC-BT-19, apartado 2.9.

Es la regla que más importa en un centro de producción. Unidos fase y neutro, la tensión de ensayo
queda entre los conductores activos, todos al mismo potencial, y tierra: no aparece entre fase y
neutro, que es donde están conectadas las entradas de las fuentes, los filtros y los descargadores
de los equipos (oficio). Medir entre fase y neutro a 500 V con un rack conectado puede dañar
equipos y, además, daría una lectura baja que no es un defecto del cable. En la práctica de
mantenimiento de una sala técnica (oficio), los equipos sensibles se desconectan antes de cualquier
medida de aislamiento, aunque la norma permita dejarlos en la medida a tierra.

Lo mismo vale para los descargadores contra sobretensiones del cuadro (tema 3, epígrafe 9): están
conectados entre los conductores activos y tierra y conducen a partir de una tensión; la
documentación del fabricante dice si hay que desconectarlos antes del ensayo (oficio; ningún
precepto leído lo regula).

### 5.4 Si la lectura sale baja

El REBT admite una instalación con aislamiento bajo si el defecto está en los receptores y no en la
instalación:

> **Cuando la resistencia de aislamiento obtenida resultara inferior al valor mínimo que le
> corresponda, se admitirá que la instalación es, no obstante correcta, si se cumplen las
> siguientes condiciones:**
> **– Cada aparato receptor presenta una resistencia de aislamiento por lo menos igual al valor
> señalado por la Norma UNE que le concierna o en su defecto 0,5 MΩ.**
> **– Desconectados los aparatos receptores, la instalación presenta la resistencia de aislamiento
> que le corresponda.**

De ahí el método de búsqueda (oficio): si la medida a tierra da bajo, se desconectan los receptores
y se repite; si sube, el defecto está en un receptor, que se busca uno a uno; si sigue bajo, está en
la instalación, y se fracciona por circuitos, abriendo interruptores, hasta aislar el tramo. La
humedad es la causa más común de una lectura baja que se recupera al secar: la medida se anota con
las condiciones del día.

### 5.5 La rigidez dieléctrica

Es un ensayo distinto, de tensión alterna y no de medida de resistencia:

> **Por lo que respecta a la rigidez dieléctrica de una instalación, ha de ser tal, que
> desconectados los aparatos de utilización (receptores), resista durante 1 minuto una prueba de
> tensión de 2U + 1000 voltios a frecuencia industrial, siendo U la tensión máxima de servicio
> expresada en voltios y con un mínimo de 1.500 voltios.**

Con U = 400 V, la prueba es de 2 × 400 + 1000 = 1.800 V durante un minuto (aritmética). Se hace
**para cada uno de los conductores incluido el neutro o compensador, con relación a tierra y entre
conductores, salvo para aquellos materiales en los que se justifique que haya sido realizado dicho
ensayo previamente por el fabricante**, y con una salvedad: **Este ensayo no se realizará en
instalaciones correspondientes a locales que presenten riesgo de incendio o explosión.**

La tabla que conviene no confundir:

| | Resistencia de aislamiento | Rigidez dieléctrica |
|---|---|---|
| Tensión | Continua: 250, 500 o 1000 V | Alterna a frecuencia industrial: 2U + 1000 V, mínimo 1.500 V |
| Qué se mide | La resistencia, en MΩ | Que resista, durante 1 minuto |
| Receptores | Conectados a tierra; desconectados entre conductores | Desconectados |
| Excepción | — | No en locales con riesgo de incendio o explosión |

### 5.6 La seguridad del ensayo y el histórico

El medidor de aislamiento es una fuente de tensión exterior, y el Real Decreto 614/2001 tiene una
regla para eso en su anexo IV, apartado B.2, 2.ª: **Cuando sea necesario utilizar una fuente de
tensión exterior se tomarán precauciones para asegurar que:**

> **a) La instalación no puede ser realimentada por otra fuente de tensión distinta de la prevista.**
> **b) Los puntos de corte tienen un aislamiento suficiente para resistir la aplicación simultánea de
> la tensión de ensayo por un lado y la tensión de servicio por el otro.**
> **c) Se adecuarán las medidas de prevención tomadas frente al riesgo eléctrico, cortocircuito o
> arco eléctrico al nivel de tensión utilizado.**

La letra a) es la que más pesa en un edificio con grupo electrógeno, SAI o autoconsumo: un circuito
consignado del lado de la red puede seguir alimentado desde otra fuente (tema 7). La b) recuerda que
el interruptor abierto tiene a un lado la red y al otro el medidor.

Y una precaución que la guía del INSST añade al terminar: **Cuando se realizan pruebas de
aislamiento en una instalación, es necesario tener en cuenta que puede quedar cargada a la tensión
suministrada por el equipo utilizado en las pruebas, debido a las capacidades existentes entre los
conductores y entre estos y tierra.** Por eso hay que **proceder a su descarga una vez concluidas
las operaciones**, mediante puesta a tierra y en cortocircuito. Un cable largo ensayado a 500 o
1000 V se descarga antes de tocarlo.

Como en la termografía y el análisis de red, en mantenimiento la medida de aislamiento vale sobre
todo por su evolución. Se compara consigo misma a lo largo del tiempo, y por eso lo que la hace útil
no es la medida: es el histórico. La evolución del aislamiento de cada devanado a masa, medida
siempre en las mismas condiciones, es una de las medidas que anticipan la avería de un motor; y una
caída progresiva en un circuito avisa antes de que la fuga alcance la sensibilidad del diferencial
(tema 13).

## 6. Analizador de redes

### 6.1 Qué exige el REBT

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Analizador de redes | Potencias, factor de potencia, armónicos, huecos y calidad de onda | Se deja registrando días |

El REBT distingue dos niveles de instrumento en la ITC-BT-03 (epígrafe 1.2):

| Categoría de la empresa instaladora | Instrumento | Qué debe medir |
|---|---|---|
| Básica | **Analizador registrador de potencia y energía para corriente alterna trifásica** | **potencia activa; tensión alterna; intensidad alterna; factor de potencia** |
| Especialista, **según proceda** | **Analizador de redes, de armónicos y de perturbaciones de red** | Lo anterior y, además, armónicos y perturbaciones |

La diferencia es la que separa un registrador de consumos de un analizador de calidad de suministro.
Para un centro de producción audiovisual, con carga electrónica en casi todo, la segunda es la que
explica los problemas (lectura de aplicación).

### 6.2 Qué mide y para qué sirve

Lo que el analizador da a un electricista de mantenimiento, con el tema donde se estudia la
magnitud (aplicación de oficio):

| Medida | Para qué | Dónde se estudia |
|---|---|---|
| Tensión de cada fase y su evolución | Comprobar que la tensión de suministro está dentro de lo admisible y detectar caídas en horas de carga | Tema 1, epígrafes 1.2 y 7 |
| Intensidad de cada fase y del neutro | Equilibrado de cargas; corriente de neutro | Tema 1, epígrafe 8 |
| Potencia activa, reactiva y aparente; energía | Consumos por cuadro o por sala; base de la monitorización energética | Temas 1 (4 y 5) y 16 |
| Factor de potencia y cos φ | Ver si hace falta compensar y si la batería de condensadores trabaja | Tema 1, epígrafe 6 |
| Armónicos | Explicar un neutro caliente, un transformador que se calienta o un factor de potencia bajo que los condensadores no corrigen | Tema 1, 8.3; tema 8, 10.2 |
| Huecos y cortes breves | Explicar reinicios de equipos sin disparo de protecciones; dimensionar la respuesta del SAI | Temas 7 y 8 |
| Máximos de demanda | Saber si un cuadro, un SAI o un grupo admiten más carga | Tema 7 |

Una lectura que sólo da el analizador: con carga electrónica, el factor de potencia (P / S) y el
cos φ dejan de coincidir, porque la corriente deformada aumenta la potencia aparente sin aportar
activa, y los condensadores corrigen el desfase, no la deformación (tema 1, 6.1). Un analizador que
da los dos valores dice cuál de los dos problemas hay; un registrador sencillo que sólo da uno, no.

### 6.3 Conexión y registro

Cómo se conecta un analizador portátil a un cuadro trifásico (oficio):

1. Con el cuadro en servicio y las precauciones del anexo IV del Real Decreto 614/2001 (epígrafe
   1.1): las conexiones de tensión se hacen en un punto protegido, con las puntas o pinzas de
   cocodrilo del fabricante y con la categoría de medida adecuada al punto (epígrafe 1.4).
2. Tensiones: las tres fases y el neutro, en el orden de fases correcto, y la referencia de tierra
   si el aparato la usa.
3. Corrientes: una pinza por fase y otra por el neutro, cada una en su fase correspondiente y
   orientada en el sentido de la energía (de la red hacia la carga). Una pinza cambiada de fase o
   puesta al revés da potencias y factores de potencia absurdos, a veces potencia negativa; es el
   error más común, y se detecta comprobando el diagrama vectorial o las potencias de cada fase antes
   de dejar el equipo registrando.
4. Registro: un periodo representativo del uso real —una semana con la programación normal de
   producción, por ejemplo— y no sólo un instante. Los problemas de una casa de radio y televisión
   dependen del horario: un plató encendido, un directo, la climatización de verano.
5. Descarga y análisis: máximos, mínimos, medias y eventos, comparados con el registro anterior del
   mismo cuadro.

Ningún precepto leído fija cómo se conecta un analizador ni cuánto tiempo se registra; lo anterior
es práctica de oficio y la documentación de cada fabricante.

Además del portátil, los cuadros generales y de salas técnicas pueden llevar analizadores fijos,
alimentados por transformadores de intensidad (con la precaución del epígrafe 3.5) y conectados al
sistema de gestión técnica del edificio, que guarda los históricos y avisa cuando una magnitud se
sale de su margen (tema 12).

## 7. Termografía básica

### 7.1 Qué es y qué detecta

| Equipo | Qué mide | Cuidado propio |
|---|---|---|
| Cámara termográfica | Puntos calientes | Mide con la instalación en carga |

La cámara termográfica mide sin contacto la radiación infrarroja que emite una superficie y la
convierte en una imagen de temperaturas. La guía de FLIR para mantenimiento predictivo explica por
qué sirve en una instalación eléctrica: **las instalaciones eléctricas y mecánicas suelen calentarse
antes de fallar**. Una conexión floja o corroída tiene más resistencia; por ella pasa la misma
corriente, y disipa más calor (efecto Joule, tema 1, 2.4).

Lo que la misma guía enumera como fallos detectables en baja tensión:

> **• Conexiones de alta resistencia**
> **• Conexiones corroídas**
> **• Daños internos en los fusibles**
> **• Fallos internos en los disyuntores**
> **• Malas conexiones y daños internos**

Y añade que con ella se ven también **desequilibrios de carga**; una de sus imágenes muestra que
**la carga no está uniformemente distribuida entre las cajas de fusibles**.

Su gran ventaja es la seguridad y la continuidad: **Una de las múltiples ventajas de la termografía
es la capacidad para llevar a cabo inspecciones mientras los sistemas eléctricos están cargados.**
No hay que cortar nada, que es lo que pide una instalación que no puede parar.

### 7.2 En carga

Es el requisito del que depende todo lo demás. El punto caliente sólo existe cuando circula
corriente: una conexión floja sin carga está a temperatura ambiente. Una termografía hecha con la
instalación parada no vale para nada (epígrafe 1.3). La guía de FLIR pide la inspección de
referencia **durante el funcionamiento normal**, y muestra el caso contrario: una imagen extraña en
la que **Los cables no están cargados** y lo que se ve son reflejos.

Consecuencia de planificación (oficio): en un centro de producción, la termografía de un cuadro de
plató o de iluminación se hace con el plató en uso o con la carga encendida, no en la madrugada de
mantenimiento cuando todo está apagado; y la de la climatización, en la época en que trabaja. Si
hay que forzar la carga, se pacta con producción (tema 17).

Y abrir el cuadro: la cámara tiene que ver los bornes, y eso suele exigir retirar tapas. **La
apertura de celdas, armarios y demás envolventes de material eléctrico estará restringida a
trabajadores autorizados** (Real Decreto 614/2001, anexo V, B.1.2). Con el cuadro abierto y en
tensión, el operador está en la situación de una medición del anexo IV: distancia, apoyo estable,
zona señalizada y equipos de protección según la evaluación (epígrafe 1.1). Mirar a través del
cristal de la puerta no sirve: **La ventana refleja radiación térmica, de forma que, para la cámara
termográfica, la ventana actúa como un espejo.**

### 7.3 Lo que falsea una lectura

La guía de FLIR enumera los factores que más influyen en la temperatura que lee la cámara:

| Factor | Qué dice la guía de FLIR | Cómo afecta en un cuadro (lectura de aplicación) |
|---|---|---|
| Conductividad térmica | **el aislamiento se suele calentar lentamente, mientras que los metales se suelen calentar rápidamente** | El borne de cobre y el aislante del cable de al lado no muestran la misma temperatura aunque compartan el calor |
| Emisividad | **La emisividad se define como la capacidad que tiene un cuerpo para emitir infrarrojos.** **Es muy importante establecer la emisividad correcta en la cámara o, de lo contrario, las mediciones de temperatura no serán correctas.** | Pletinas y bornes de metal brillante emiten poco y la cámara les da una temperatura falsa |
| Reflexión | **Algunos materiales reflejan la radiación térmica del mismo modo que un espejo refleja la luz visible. Entre estos están los metales no oxidados, especialmente si se han pulido.** | El calor del propio operador o de una luminaria reflejado en una pletina parece un punto caliente |
| Condiciones meteorológicas | **Una elevada temperatura ambiente puede ocultar puntos calientes al calentar todo el objeto**; el sol, el viento y la lluvia alteran la superficie | Cuadros de exterior, centros emisores, unidades móviles |
| Calefacción y ventilación | **Los flujos de aire frío de ventiladores o sistemas de aire acondicionado** pueden enfriar la superficie **mientras los componentes situados por debajo de la superficie permanecen calientes** | Una sala técnica muy climatizada puede esconder un defecto |

El ejemplo de la guía sobre la emisividad: con la emisividad correcta de la piel humana (**0,97**),
la cámara lee **36,7 °C**; con una emisividad incorrecta (**0,15**), **98,3 °C**.

Cómo se corrige, según la misma guía:

- La emisividad: con los ajustes predefinidos de la cámara o una tabla de emisividades; o con
  **"cinta de calibración"**, un trozo de cinta de emisividad conocida, **por lo general, cercana a
  1**, que se pega en la superficie, se deja unos minutos hasta que toma su temperatura, se mide, y
  se ajusta la emisividad hasta que la lectura de la superficie coincide con la de la cinta.
- La reflexión: introduciendo en la cámara la temperatura reflejada, y eligiendo **cuidadosamente
  el ángulo desde el que la cámara termográfica apunta al objeto**. El indicio de un falso punto
  caliente: **desaparece cuando se cambia ligeramente la ubicación de la cámara**; los verdaderos
  **suelen mostrar un patrón homogéneo, a diferencia de las reflexiones**.

En la práctica (oficio), la medida más fiable en un cuadro no es la temperatura absoluta de una
pletina brillante, sino la comparación entre elementos iguales en condiciones iguales: las tres
fases de un mismo interruptor, los bornes de entrada y de salida de un mismo aparato, dos cables
iguales con carga parecida. Un borne más caliente que sus vecinos con la misma corriente es
sospechoso aunque la cámara no dé su temperatura exacta.

Y los puntos fríos: la guía advierte de que **fusibles fundidos** y **sistemas de refrigeración con
un flujo de refrigerante limitado** provocan **puntos fríos, en lugar de puntos calientes**. Un
fusible frío entre dos calientes en una base trifásica es una fase sin corriente.

### 7.4 La cámara

Las tres características que la guía de FLIR manda evaluar, con sus cifras de referencia (de 2011,
según la propia guía, y de un fabricante; son orientativas, no normativas):

| Característica | Qué es | Referencia de la guía |
|---|---|---|
| Resolución | Número de puntos de medida de la imagen | Modelos básicos de **60 x 60 píxeles**; avanzados de **640 x 480 píxeles**, que **tiene 307.200 puntos de medición en una imagen** |
| Sensibilidad térmica | **La sensibilidad térmica define la magnitud de una diferencia de temperatura que la cámara puede detectar.** | Las más avanzadas, **0,03 °C (30 mK)** |
| Precisión | Margen de error de la temperatura medida | **El estándar del sector actual para la precisión es de ±2% / ±2 °C.** |

La resolución importa más de lo que parece: un borne pequeño visto de lejos ocupa pocos píxeles y
se mezcla con lo que le rodea. La guía da el ejemplo de un mismo objeto medido a **63,9 °C** con
640 x 480 píxeles y a **42,7 °C** con 320 x 240. Con una cámara de baja resolución hay que
acercarse, y en un cuadro en tensión acercarse tiene un límite (epígrafe 7.2).

### 7.5 Cómo se organiza una inspección termográfica

La guía de FLIR propone cuatro pasos:

| Paso | Qué se hace (guía de FLIR) |
|---|---|
| 1. Definir la tarea | **Enumere todo el equipamiento que desee supervisar**; asignar prioridades según los registros de mantenimiento y las consecuencias del fallo: **El equipamiento esencial se debe supervisar con más frecuencia y atención** |
| 2. Inspección inicial | Termografías de referencia de todo el equipo, **durante el funcionamiento normal**, documentando **la configuración de emisividad y reflexión de cada pieza del equipamiento, así como una descripción de la ubicación exacta de cada termografía**; con ellas se fija **un umbral de alarma de temperatura** |
| 3. Inspección | Recorrido según la programación, con la alarma de cada equipo; **Si la alarma se activa, esta pieza del equipamiento deberá ser analizada en mayor profundidad** |
| 4. Análisis e informe | Analizar las imágenes, resumir en un informe y seguir **el rendimiento térmico de su equipamiento en el tiempo** |

Aplicado a la casa (oficio): los primeros de la lista son los cuadros generales, los de SAI y
grupo, los de las salas técnicas, continuidad y CPD, y los de los centros emisores, porque su fallo
corta la emisión (temas 7, 8 y 17). Cada hallazgo termina en una orden de trabajo con su prioridad
(tema 13), y la reparación —reapretar un borne, cambiar un aparato— se hace con la instalación
consignada (tema 15). Después se repite la termografía en carga para comprobar que el punto caliente
ha desaparecido.

Ningún documento leído para este tema da criterios numéricos de gravedad (cuántos grados de
diferencia entre fases obligan a actuar y con qué urgencia); existen en normas y guías de
asociaciones que el tema no ha leído, y no se dan aquí.
