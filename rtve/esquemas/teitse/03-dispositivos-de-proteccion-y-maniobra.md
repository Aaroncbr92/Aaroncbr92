# Esquema · Tema 3 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Dispositivos de protección y maniobra

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = instrucción técnica citada
literalmente en el tema · `[of]` = oficio eléctrico · `[plan]` = enunciado del anexo. **Siglas**: el
reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones (**ITC-BT-08**,
**ITC-BT-18**, **ITC-BT-22**, **ITC-BT-23**, **ITC-BT-24**); el interruptor diferencial (**ID**); el
miliamperio (**mA**) y el amperio (**A**); el kiloamperio (**kA**); la muy baja tensión de seguridad
(**MBTS**); los esquemas de conexión del neutro (**TN**, **TT** e **IT**); el grado de protección
(**IP**), con **IP XXB**, **IP4X** e **IP XXD**; las clases de diferencial (**AC**, **A**, **B** y
**S**); y la Asociación Española de Normalización (**UNE**).

**Cabecera.** Enunciado: punto 3 del anexo, **la SEGURIDAD eléctrica de la instalación** · **el punto
con más instrucción técnica detrás de todo el anexo**: **cuatro** —esquemas de neutro, puesta a tierra,
sobreintensidades, contactos—, **las cuatro volcadas y citadas.**

| Qué se protege | De qué | Con qué |
|---|---|---|
| **La INSTALACIÓN** | **Sobrecargas y cortocircuitos** | **Magnetotérmicos y fusibles** |
| **Las PERSONAS** | **Contactos directos e indirectos** | **Diferenciales, tierra, aislamiento, envolventes** |

- **EL ERROR CONCEPTUAL DEL PUNTO** · `[of]` · **un magnetotérmico no protege a nadie de una
  electrocución** —**treinta miliamperios que matan no lo hacen saltar**— **y un diferencial no protege
  el cable de una sobrecarga** · **los dos hacen falta y ninguno sustituye al otro.**

<!-- indice -->

## Índice

- [Sobreintensidades](#sobreintensidades)
- [El magnetotérmico](#el-magnetotérmico)
- [La protección diferencial](#la-protección-diferencial)
- [Esquemas de conexión del neutro](#esquemas-de-conexión-del-neutro)
- [La puesta a tierra](#la-puesta-a-tierra)
- [Contactos directos e indirectos](#contactos-directos-e-indirectos)
- [Aparatos de maniobra](#aparatos-de-maniobra)
- [Automatismos y cuadros](#automatismos-y-cuadros)
- [Conmutación sin paso por cero](#conmutación-sin-paso-por-cero)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## Sobreintensidades

- **LA CITA QUE ABRE EL PUNTO** · `[BOE]` · **ITC-BT-22, apartado 1.1: todo circuito estará protegido
  contra los efectos de las sobreintensidades que puedan presentarse en el mismo, para lo cual la
  interrupción se realizará en un tiempo conveniente o estará dimensionado para las previsibles ·
  causas: sobrecargas debidas a los aparatos de utilización o defectos de aislamiento de gran
  impedancia, cortocircuitos y descargas eléctricas atmosféricas.**

| Causa | Qué es | Quién la corta |
|---|---|---|
| **SOBRECARGA** | **Corriente superior a la nominal en circuito SANO** | **El disparo TÉRMICO**, o un fusible |
| **CORTOCIRCUITO** | **Contacto entre activos**, impedancia casi nula | **El disparo MAGNÉTICO**, instantáneo |
| **Descarga atmosférica** | **Sobretensión transitoria por la línea** | **Los protectores de la ITC-BT-23** |

- **LA DIFERENCIA FÍSICA QUE EXPLICA LOS DOS DISPAROS** · `[of]` · **una sobrecarga es de dos a diez
  veces la nominal y se aguanta un rato; un cortocircuito es de cientos o miles y hay que cortarlo en
  milisegundos** · **un solo mecanismo no hace las dos cosas bien.**
- **LO QUE LA NORMA ADMITE COMO DISPOSITIVO** · `[BOE]` · **ITC-BT-22, apartado 1.1.a): interruptor
  automático de corte omnipolar con curva térmica de corte, o cortacircuitos fusibles calibrados de
  características de funcionamiento adecuadas.**
- **LA REGLA QUE AHORRA APARAMENTA** · `[BOE]` · **en el origen de todo circuito, dispositivo contra
  cortocircuitos con capacidad de corte acorde a la intensidad de ese punto** · **pero en circuitos
  derivados de uno principal cada derivado lleva su protección contra SOBRECARGAS y un solo general
  asegura la de CORTOCIRCUITOS de todos.**
- **LA LECTURA QUE HAY QUE AÑADIR** · `[of]` · **el cortocircuito se puede proteger aguas arriba porque
  su valor lo fija la RED; la sobrecarga no, porque depende de lo que se enchufe.** **Es la base de la
  selectividad y del filiado.**

## El magnetotérmico

| Mecanismo | Cómo | Qué protege |
|---|---|---|
| **TÉRMICO** | **Lámina bimetálica que se curva al calentarse** | **La sobrecarga**: más rápido cuanto mayor el exceso |
| **MAGNÉTICO** | **Bobina que atrae un núcleo sobre un umbral** | **El cortocircuito**: milisegundos |

| Dato del frontal | Qué es |
|---|---|
| **Calibre** | **La corriente que aguanta indefinidamente sin disparar** |
| **CURVA** | **A cuántas veces el calibre actúa lo MAGNÉTICO** |
| **PODER DE CORTE** | **La corriente de cortocircuito máxima que corta sin destruirse** |
| **Polos** | Unipolar más neutro, bipolar, tripolar, tetrapolar |

| Curva | Sensibilidad | Para qué |
|---|---|---|
| **B** | **La que antes dispara** | **Líneas largas y cargas resistivas** |
| **C** | **Intermedia** | **Uso general**: alumbrado y fuerza |
| **D** | **La que más tolera** | **Punta de arranque fuerte**: motores, transformadores |

- **LO QUE EL TEMA NO DA Y DECLARA** · `[of]` · **los múltiplos exactos de cada curva son dato de norma
  de producto y de fabricante** · **lo que hay que saber es el ORDEN.**
- **EL DATO QUE MÁS SE OLVIDA Y CAUSA EL ACCIDENTE** · `[of]` · **si la corriente de cortocircuito
  posible supera el poder de corte del aparato, el aparato NO corta: se destruye y el arco continúa** ·
  **el poder de corte necesario crece cuanto más cerca del transformador**, y **por eso la cabecera
  lleva más que las últimas derivaciones.**

## La protección diferencial

- **CÓMO FUNCIONA, EN UNA FRASE** · `[of]` · **compara lo que entra por las fases con lo que vuelve por
  el neutro**: **si la suma no es cero, la diferencia se está yendo por otro camino** —una persona, una
  masa, la humedad— **y abre.**

| Sensibilidad | Valor asignado | Para qué |
|---|---|---|
| **ALTA** | **30 mA o menos** | **PROTECCIÓN DE PERSONAS**, complementaria contra contactos directos |
| **Media** | **300 mA** | **Incendios** de origen eléctrico y contactos indirectos |
| **Baja** | **Amperios** | Selectividad en cabecera |

- **LA CITA QUE MÁS SE MALINTERPRETA** · `[BOE]` · **ITC-BT-24, apartado 3.5: el empleo de dispositivos
  de corriente diferencial-residual de valor asignado inferior o igual a 30 mA se reconoce como medida
  de protección COMPLEMENTARIA en caso de fallo de otra medida contra los contactos directos o en caso
  de imprudencia de los usuarios.**
- **LO QUE LA PALABRA COMPLEMENTARIA SIGNIFICA** · `[BOE]` · **no constituye por sí misma una medida
  completa y requiere una de las de los apartados 3.1 a 3.4** —aislamiento, envolventes, obstáculos,
  alejamiento— · `[of]` · **un diferencial no autoriza a dejar un conductor accesible.**
- **FRENTE A LOS INDIRECTOS ES OTRA COSA** · `[of]` · **ahí el diferencial SÍ es la medida principal.**

| Clase | Qué detecta |
|---|---|
| **AC** | **Sólo defectos alternos senoidales** |
| **A** | **Alternas senoidales Y continuas PULSANTES** |
| **B** | **Además, continuas lisas** |
| **Selectivo S** | **Retardado**, para selectividad con los de aguas abajo |

- **LA LECTURA QUE UN EXAMEN BUSCA** · `[of]` · **una instalación llena de electrónica —variadores,
  fuentes conmutadas, alumbrado electrónico— produce defectos que un AC puede NO ver** · **por eso se
  han generalizado las de clase A**, y **una casa que emite es exactamente ese caso.**
- **AVISO DE MANTENIMIENTO** · `[of]` · **el botón de prueba hay que accionarlo periódicamente** · **un
  diferencial que lleva años sin disparar puede estar agarrotado** · **el botón comprueba el MECANISMO,
  no la instalación.** (Tema 9.)

## Esquemas de conexión del neutro

| Letra | Posición | Qué significa |
|---|---|---|
| **T** | Primera | **Un punto de la ALIMENTACIÓN directamente a tierra** |
| **I** | Primera | **Alimentación aislada**, o a través de impedancia |
| **T** | Segunda | **Masas DIRECTAMENTE a tierra** |
| **N** | Segunda | **Masas al punto de la alimentación puesto a tierra** |
| **S** | Tercera | **Neutro y protección SEPARADOS** |
| **C** | Tercera | **Neutro y protección COMBINADOS** |

| Esquema | Cómo es | Corriente de defecto fase-masa | Qué protege |
|---|---|---|---|
| **TN** | **Alimentación a tierra y masas a ese mismo punto** | **Es un CORTOCIRCUITO**: bucle metálico | **Los de sobreintensidad**, si el bucle es bajo |
| **TT** | **Masas a tierra SEPARADA** | **Menor**: el bucle pasa por dos tomas de tierra | **El DIFERENCIAL**, imprescindible |
| **IT** | **Alimentación AISLADA, masas a tierra** | **Muy pequeña en el PRIMER defecto** | **Controlador permanente de aislamiento**; el segundo sí se corta |

- **POR QUÉ IMPORTA EN ESPAÑA** · `[of]` · **el TT es el de las instalaciones alimentadas desde la red
  pública**: **de ahí que el diferencial sea obligatorio y no opcional.**
- **POR QUÉ EL IT MERECE UNA LÍNEA** · `[of]` · **es el único esquema en el que un PRIMER defecto no
  obliga a cortar**: **se detecta, se avisa y se repara sin apagar** · **es lo que se busca donde una
  interrupción es peor que el defecto**, y **una continuidad de emisión es de esa familia.**

## La puesta a tierra

- **LA DEFINICIÓN** · `[BOE]` · **ITC-BT-18, apartado 2: unión eléctrica directa, sin fusibles ni
  protección alguna, de una parte del circuito eléctrico o de una parte conductora no perteneciente al
  mismo mediante una toma de tierra con un electrodo o grupos de electrodos enterrados en el suelo.**
- **LAS CINCO PALABRAS QUE HAY QUE SUBRAYAR** · `[of]` · **«sin fusibles ni protección alguna»** · **un
  conductor de protección con fusible podría quedar interrumpido sin que nadie se entere** · **la
  tierra es un camino permanente, incondicional y comprobable.**
- **PARA QUÉ SIRVE** · `[BOE]` · **limitar la tensión que las masas puedan presentar respecto a
  tierra**, **asegurar la actuación de las protecciones** y **eliminar o disminuir el riesgo de avería.**

| Parte, desde el terreno | Qué es |
|---|---|
| **Electrodo o TOMA DE TIERRA** | **Lo enterrado**: picas, placas, conductores desnudos, mallas, armaduras |
| **Conductor de tierra** | **Del electrodo al borne principal**, no enterrado |
| **BORNE de puesta a tierra** | **Punto de reunión, con dispositivo de separación para poder MEDIR** |
| **Conductores de PROTECCIÓN** | **Del borne a cada masa** |
| **Conductores de EQUIPOTENCIALIDAD** | **Unen masas y elementos conductores ajenos** |

- **EL DETALLE QUE UN EXAMEN PERSIGUE** · `[of]` · **el dispositivo de separación del borne** · **sin
  poder separar el electrodo no se mide su resistencia aislada.** (Tema 9.)
- **LA RESISTENCIA DE TIERRA NO ES UNA CIFRA FIJA** · `[BOE]` · **depende de la sensibilidad de la
  protección que debe actuar y de la tensión de contacto admisible** · **la tensión límite convencional
  es de 50 voltios eficaces**, y **de 24 en los casos que la propia instrucción señala.**
- **LA MEDIDA MÁS BARATA Y PEOR ENTENDIDA** · `[of]` · **la equipotencialidad**: **unir todas las masas
  de una zona hace que, si aparece tensión, TODO suba a la vez** · **la seguridad no está en que no
  haya tensión: está en que no haya DIFERENCIA de tensión.**

## Contactos directos e indirectos

| | **DIRECTO** | **INDIRECTO** |
|---|---|---|
| **Qué se toca** | **Una parte ACTIVA** | **Una MASA en tensión por fallo de aislamiento** |
| **Es fallo de** | **La instalación como barrera** | **El aislamiento de un equipo** |
| **Se previene con** | **Aislamiento, envolventes, obstáculos, alejamiento** + **diferencial de 30 mA** | **Corte automático, clase II, locales no conductores, equipotencialidad local, separación eléctrica** |

- **LA QUE PROTEGE DE LOS DOS A LA VEZ** · `[of]` · **la muy baja tensión de seguridad** · **si la
  tensión no puede ser peligrosa, no importa qué se toque.**
- **LOS GRADOS DE ENVOLVENTE** · `[BOE]` · **partes activas en envolventes o tras barreras con mínimo
  IP XXB** · **superficies superiores horizontales fácilmente accesibles, mínimo IP4X o IP XXD.**
- **LA LECTURA QUE UN EXAMEN PREMIA** · `[of]` · **la cara SUPERIOR de un cuadro pide más grado que sus
  laterales** · **sobre una superficie horizontal caen cosas**: **un destornillador dejado encima es
  exactamente el riesgo que ese grado previene.**
- **LA CONDICIÓN QUE SEPARA UN CUADRO DE UNA CAJA** · `[BOE]` · **suprimir barreras o abrir envolventes
  sólo debe ser posible con llave o herramienta, o tras quitar la tensión, o con una segunda barrera
  detrás** · `[of]` · **una tapa que se abre con la mano y deja activos a la vista incumple.**

## Aparatos de maniobra

| Aparato | Puede | NO puede |
|---|---|---|
| **SECCIONADOR** | **Separación VISIBLE y segura**, en vacío | **NO corta corriente** |
| **INTERRUPTOR** | **Abrir y cerrar corrientes NORMALES** | **No corta un cortocircuito** |
| **INTERRUPTOR-SECCIONADOR** | **Las dos cosas** | — |
| **CONTACTOR** | **Maniobrar A DISTANCIA y con mucha frecuencia** | **No protege** |
| **INTERRUPTOR AUTOMÁTICO** | **Cortar corrientes de defecto** y maniobrar | — |
| **FUSIBLE** | **Cortar un cortocircuito fundiéndose** | **No se rearma; no maniobra** |

- **LAS DOS REGLAS QUE RESUMEN LA TABLA** · `[of]` · **un seccionador NO se maniobra en carga**:
  **abrirlo con corriente produce un arco que no está diseñado para extinguir** —**el accidente clásico
  del cuadro de un centro de transformación**—, y **la maniobra correcta es cortar con el interruptor y
  seccionar con el seccionador** · **maniobrar y proteger son dos funciones**: **un contactor abre mil
  veces al día y no protege; un magnetotérmico protege y no está hecho para eso.**

| Parte del contactor | Qué es |
|---|---|
| **Bobina** | **El electroimán que lo cierra**; va en el circuito de MANDO |
| **Contactos PRINCIPALES** | **Los que llevan la corriente de la carga** |
| **Contactos AUXILIARES** | **Los que informan y enclavan** |

## Automatismos y cuadros

| Circuito | Qué lleva | Cómo se dibuja |
|---|---|---|
| **POTENCIA** | **La corriente de la carga** | **Trazo grueso**, pocas líneas |
| **MANDO** | **La corriente que gobierna las bobinas** | **Trazo fino**, muchos contactos |

| Esquema elemental | Qué hace |
|---|---|
| **Marcha-paro con REALIMENTACIÓN** | **Un pulsador cierra el contactor y un auxiliar suyo lo mantiene**; el paro en serie lo abre |
| **INVERSIÓN DE GIRO** | **Dos contactores que permutan dos fases**, con **enclavamiento** |

| Enclavamiento | Cómo | Qué garantiza |
|---|---|---|
| **ELÉCTRICO** | **Auxiliar normalmente cerrado de cada uno en serie con la bobina del otro** | **Que la lógica no dé la orden de cerrar los dos** |
| **MECÁNICO** | **Pieza física que impide el cierre simultáneo** | **Que no cierren aunque la lógica falle o un contacto se pegue** |

- **POR QUÉ HACEN FALTA LOS DOS** · `[of]` · **el eléctrico protege del error de MANDO; el mecánico, del
  fallo del APARATO** · **un auxiliar soldado deja sin efecto el eléctrico** · **en la inversión de giro
  y en el estrella-triángulo del tema 2, cerrar los dos a la vez es un cortocircuito entre fases.**

| Regla de montaje de cuadro | Por qué |
|---|---|
| **Separar potencia y mando** | **Evita acoplamientos y facilita el mantenimiento** |
| **Identificar TODO** | **Un cuadro sin marcar no se puede mantener** (tema 13) |
| **Colores normalizados** | **Azul el neutro; amarillo-verde el de protección** |
| **Reserva de espacio y carril** | **Una instalación siempre crece** |
| **Esquema DENTRO y actualizado** | **Es el documento de quien venga después** |
| **Grado de protección acorde al sitio** | Materia del tema 4 |

- **LA REGLA DE COLOR QUE ES EXCLUSIVA** · `[of]` · **el amarillo-verde está RESERVADO al conductor de
  protección y no vale para nada más.**

## Conmutación sin paso por cero

- **EL PROBLEMA** · `[of]` · **pasar la carga de una fuente a otra —red a grupo, red a alimentación
  ininterrumpida, línea a línea— con una conmutación convencional CORTA un instante** · **para un
  alumbrado es un parpadeo; para un directo o un servidor, una caída.**
- **QUÉ ES** · `[of]` · **transferir la carga SIN que la tensión se anule en la salida**: **sin que el
  receptor llegue a quedarse sin alimentación.**
- **LAS DOS CONDICIONES** · `[of]` · **fuentes SINCRONIZADAS** —**misma tensión, misma frecuencia y
  mismo ángulo de fase**, en ventana estrecha— · **solapamiento controlado**: **la segunda se conecta
  antes de que la primera se desconecte**, un tiempo mínimo.
- **EL PELIGRO QUE ESAS CONDICIONES EVITAN** · `[of]` · **paralelar dos fuentes fuera de fase es unir
  dos tensiones distintas a través de casi nada** · **la corriente sólo la limita la impedancia de las
  fuentes y del cableado**: **cortocircuito, con daño mecánico en las máquinas.**

| Tipo | Qué hace | Corte |
|---|---|---|
| **Manual con enclavamiento** | **Tres posiciones: red, cero, grupo** | **Largo**; el cero existe para que no se unan |
| **Automático de corte** | **Detecta el fallo y transfiere** | **Breve**, de segundos |
| **SOLAPADA sincronizada** | **Transfiere con las dos fuentes en fase** | **Sin corte** |
| **Estático** | **Semiconductores en vez de contactos** | **Prácticamente sin corte** |

- **LA LECTURA QUE CIERRA EL PUNTO** · `[of]` · **el grupo resuelve la AUTONOMÍA y la alimentación
  ininterrumpida resuelve la CONTINUIDAD, y no son lo mismo** · **el grupo tarda en arrancar y en tomar
  carga; el sistema de alimentación ininterrumpida cubre ese hueco** · **la conmutación sin paso por
  cero hace que el paso de uno a otro no se note.** (Temas 11 y 12.)

## Aviso de estudio

- **LA LENTE NO PUEDE ANCLAR ESTAS CITAS** · `[of]` · **las instrucciones NO numeran por artículos sino
  por apartados del tipo 1.1 o 3.5** · **las tres citas de este tema se han comprobado como subcadena
  literal contra el volcado**, y **el informe de refutación de la ocupación da la cuenta.**
- **LO QUE ESTE TEMA NO DA** · `[of]` · **ningún múltiplo de curva, ningún poder de corte, ningún
  calibre, ninguna sección de conductor de protección y ningún valor de resistencia de tierra** ·
  **los dos valores que sí se dan son los de las instrucciones citadas**: **los 30 mA** y **los 50
  voltios eficaces, con los 24 de los casos señalados.**
