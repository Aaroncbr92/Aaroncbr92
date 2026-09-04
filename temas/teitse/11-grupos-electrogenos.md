# Tema 11 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Sistemas de generación: grupos electrógenos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 11 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. **Ninguna cita literal propia**: lo que se afirma del reglamento está citado en los temas 8 y 10, con su apartado identificado |
| **La coletilla del enunciado** | **«Condiciones de trabajo»**, no «características» ni «tipos». **Un grupo da AUTONOMÍA y no da CONTINUIDAD**: tarda en arrancar, y ese hueco lo cubre el tema 12 |
| **Extensión** | **2.915 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el reglamento electrotécnico para baja tensión
(**REBT**) y sus instrucciones (**ITC-BT-28**, **ITC-BT-40**); el kilovoltamperio (**kVA**) y el
kilovatio (**kW**); el hercio (**Hz**) y las revoluciones por minuto (**r.p.m.**); el sistema de
alimentación ininterrumpida (**SAI**), del tema 12; el reglamento de instalaciones petrolíferas y su
instrucción de almacenamiento en instalaciones de consumo (**MI-IP 03**); y el decibelio ponderado A
(**dBA**), unidad de nivel sonoro.

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 11):
> «Sistemas de generación de energía: grupos electrógenos. Condiciones de trabajo.»

**El enunciado tiene una coletilla que hay que leer con atención: «CONDICIONES DE TRABAJO».** **No dice
«características» ni «tipos»: dice condiciones de trabajo**, y **eso es lo que un examen de esta
ocupación buscará**: **en qué régimen puede trabajar un grupo, cuánto tiempo, con qué carga y con qué
requisitos de emplazamiento.**

**Y la idea que hay que tener antes de nada, y que este temario repite porque es la que más se
confunde**: **un grupo electrógeno da AUTONOMÍA y no da CONTINUIDAD.** **Tarda en arrancar y en tomar
carga.** **Lo que cubre ese hueco es la batería del tema 12.** **Los dos juntos son un sistema; cada
uno por su cuenta, no.**

<!-- indice -->

## Índice

- [1. Qué es y de qué partes consta](#1-qué-es-y-de-qué-partes-consta)
- [2. Las condiciones de trabajo](#2-las-condiciones-de-trabajo)
- [3. El emplazamiento: lo que el reglamento exige](#3-el-emplazamiento-lo-que-el-reglamento-exige)
- [4. El régimen del grupo respecto a la red](#4-el-régimen-del-grupo-respecto-a-la-red)
- [5. La secuencia de funcionamiento](#5-la-secuencia-de-funcionamiento)
- [6. El mantenimiento y las pruebas](#6-el-mantenimiento-y-las-pruebas)
- [7. El grupo en una casa que emite](#7-el-grupo-en-una-casa-que-emite)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Qué es y de qué partes consta

**Un grupo electrógeno es un conjunto MOTOR-ALTERNADOR que convierte la energía química de un
combustible en energía eléctrica.**

| Parte | Qué hace |
|---|---|
| **MOTOR térmico** | **Gasóleo o gas**; da el par y la velocidad |
| **ALTERNADOR** | **Convierte el giro en tensión alterna**; es la máquina síncrona del tema 2 |
| **Regulador de VELOCIDAD** | **Mantiene las revoluciones, y con ellas la FRECUENCIA** |
| **Regulador de TENSIÓN** | **Ajusta la excitación del alternador**; mantiene la tensión |
| **Cuadro de control y mando** | **Arranque, medidas, alarmas, parada** |
| **Sistema de arranque** | **Batería, motor de arranque y cargador** |
| **Depósito de combustible** | **Diario y, en su caso, depósito nodriza** |
| **Sistema de refrigeración** | **Radiador y ventilador, o intercambiador** |
| **Sistema de escape** | **Silencioso y conducto al exterior** |
| **Bancada y antivibratorios** | **Soporte y aislamiento de vibración** |

**Y la relación que hay que saber y que explica el regulador de velocidad**: **la FRECUENCIA de la
tensión que genera un alternador depende de su VELOCIDAD DE GIRO y de su número de pares de polos.**
**Mantener 50 hercios es mantener las revoluciones**, y **por eso un grupo con el regulador
desajustado da mala frecuencia y no un mal voltaje.**

**Los dos parámetros que se ajustan por separado y que hay que no confundir:**

| Se ajusta | Con qué | Qué controla |
|---|---|---|
| **La FRECUENCIA** | **El regulador de velocidad del MOTOR** | Revoluciones por minuto |
| **La TENSIÓN** | **El regulador de EXCITACIÓN del alternador** | Campo magnético del rotor |

## 2. Las condiciones de trabajo

**Ésta es la parte que el enunciado pide expresamente**, y **son cuatro cosas distintas que se dan
juntas y se confunden.**

**Primero, el RÉGIMEN de servicio.** **Un grupo no da la misma potencia según cuánto vaya a trabajar**,
y **la designación normalizada distingue varios regímenes:**

| Régimen | Para qué |
|---|---|
| **De EMERGENCIA o de socorro** | **Sólo cuando falla la red**, un número limitado de horas al año y sin sobrecarga admisible |
| **PRINCIPAL, con carga variable** | **Funcionamiento continuado como fuente principal**, con una carga media limitada y sobrecarga admisible durante un tiempo |
| **CONTINUO** | **Carga constante y horas ilimitadas**; **es el régimen más exigente y el de menor potencia declarada** |

**Y la regla que sale de la tabla y que hay que saber decir**: **la misma máquina declara MÁS potencia
cuanto MENOS va a trabajar.** **Un grupo de emergencia y uno continuo del mismo tamaño no dan la misma
cifra**, y **comparar dos ofertas sin mirar el régimen es comparar dos cosas distintas.**

**Segundo, la POTENCIA y el factor de potencia.** **La potencia de un grupo se declara en
kilovoltamperios y en kilovatios**, y **la relación entre las dos es el factor de potencia de
referencia.** **Un grupo dimensionado en kilovatios para una carga con factor de potencia peor del de
referencia se queda corto en corriente**, y **es un error de dimensionado frecuente.**

**Tercero, las CONDICIONES AMBIENTALES.** **Las potencias se declaran para unas condiciones de
referencia**, y **hay que corregirlas:**

| Factor | Efecto |
|---|---|
| **ALTITUD** | **Menos densidad de aire, menos potencia del motor** |
| **TEMPERATURA ambiente** | **Más temperatura, menos potencia y menos capacidad de refrigeración** |
| **HUMEDAD** | Efecto menor, pero contemplado |

**El temario no da los coeficientes y lo declara**: **son dato de fabricante y de norma de producto.**
**Lo que hay que saber es que existen y que un grupo instalado en altura o en una sala caliente
entrega menos de lo que dice su placa.**

**Cuarto, el ESCALÓN DE CARGA.** **Un grupo no admite que se le eche toda la carga de golpe**, y **la
razón es física**: **al conectar una carga grande, el motor se frena, la frecuencia cae y el regulador
tarda en recuperarla.** **Por eso las cargas se meten POR ESCALONES**, y **los arranques de motores
grandes se hacen con arrancador progresivo o variador para no exigir la punta al grupo.** **Ésa es la
conexión directa con el tema 2.**

## 3. El emplazamiento: lo que el reglamento exige

**Las condiciones que la instrucción de instalaciones generadoras impone al local, citadas ya en el
tema 10 y aquí desarrolladas:**

| Exigencia | Qué implica en obra |
|---|---|
| **Local de uso EXCLUSIVO** | **No se comparte con almacén ni con otras instalaciones** |
| **Protección contra incendios** | **Cumple las disposiciones reguladoras que le correspondan** |
| **VENTILACIÓN suficiente**, cualquiera que sea la potencia | **Entrada de aire de combustión y de refrigeración, y salida de aire caliente**, dimensionadas |
| **Conductos de escape de material INCOMBUSTIBLE** | **Y evacuando DIRECTAMENTE al exterior**, o a un sistema de aprovechamiento energético |
| **Depósitos y canalizaciones** | **Cumplen ADEMÁS sus propios reglamentos** |

**La ventilación es la exigencia que más se subestima y merece explicación**: **un grupo necesita aire
para tres cosas distintas** —**la combustión, la refrigeración del motor y la refrigeración del
alternador y del propio local**—, y **el caudal que hace falta es muy superior al que la intuición
sugiere.** **Una sala con rejilla pequeña hace que el grupo se caliente y se pare por temperatura
justo cuando más falta hace.**

**Y el escape merece su párrafo**: **el conducto tiene que ser incombustible, estar aislado
térmicamente donde pueda tocarse, llevar compensador de dilatación —porque se dilata mucho al
calentarse— y salir donde los gases no vuelvan a entrar por la toma de aire.** **Un escape que
descarga junto a la entrada de ventilación hace que el grupo respire su propio humo.**

**El RUIDO, que en una casa que emite es un asunto de primer orden y no de comodidad**: **un grupo es
una de las fuentes de ruido y vibración más intensas de un edificio**, y **lo que hay que resolver son
las TRES vías por las que se transmite:**

| Vía | Cómo se corta |
|---|---|
| **Por el AIRE** | **Cabina insonorizada, silencioso de escape, atenuadores en las rejillas** |
| **Por la ESTRUCTURA** | **Antivibratorios bajo la bancada** y **conexiones flexibles** en escape, combustible y refrigerante |
| **Por los CONDUCTOS** | **Manguitos flexibles**: un conducto rígido lleva la vibración a todo el edificio |

**Y la advertencia de proyecto que este temario declara como oficio**: **la vía estructural es la que se
olvida y la que arruina una grabación.** **Un grupo perfectamente insonorizado que apoya rígido sobre
la losa hace vibrar los estudios que tiene encima**, y **eso no lo arregla ninguna cabina.**

## 4. El régimen del grupo respecto a la red

**Es la clasificación del tema 10 aplicada aquí**, y **la que decide cómo se conmuta:**

| Clase de instalación generadora | Qué permite | Cómo conmuta |
|---|---|---|
| **AISLADA** | **Ninguna conexión con la red** | No hay conmutación con red |
| **ASISTIDA** | **Conexión, pero NUNCA en paralelo** | **Sistema de conmutación de todos los activos y el neutro**; **transferencia sin corte sólo con los requisitos del tema 10** |
| **INTERCONECTADA** | **Trabajo normal EN PARALELO** | Sincronización permanente |

**El grupo de socorro de un centro de trabajo es ASISTIDO**, y **de ahí salen las tres exigencias que
un técnico tiene que comprobar:**

1. **La conmutación corta TODOS los conductores activos Y EL NEUTRO.** **No basta con conmutar
   fases.**
2. **El acoplamiento simultáneo tiene que ser IMPOSIBLE**, y **eso es enclavamiento mecánico además
   del eléctrico, como en el tema 3.**
3. **Si se quiere transferencia sin corte, hay requisitos adicionales**: **potencia superior a
   100 kVA, punto único, desconexión del neutro de tierra en la interconexión, protecciones de tensión
   y frecuencia, antivertido y un máximo de CINCO SEGUNDOS de interconexión.** **Están citados en el
   tema 10.**

**Y el papel del grupo en los servicios de seguridad, que enlaza con el tema 8**: **el grupo es una de
las fuentes propias de energía que la instrucción de pública concurrencia admite**, y **su categoría
de conmutación es, típicamente, de CORTE MEDIANO** —disponible en 15 segundos como máximo—. **Nunca
«sin corte» ni «corte muy breve»**, porque **tiene que arrancar.**

**El umbral de arranque también es reglamentario y está citado en el tema 8**: **la fuente propia
arranca al faltar la tensión de la distribuidora o cuando ésta desciende por debajo del 70 % de su
valor nominal.**

## 5. La secuencia de funcionamiento

**Lo que ocurre desde que falla la red hasta que vuelve, paso a paso**, que es **lo que hay que saber
explicar y lo que se programa en el cuadro de control:**

| Fase | Qué pasa |
|---|---|
| **1 · Detección del fallo** | **Falta de tensión o tensión por debajo del umbral**, durante un tiempo de confirmación |
| **2 · Apertura del interruptor de red** | **Se aísla la instalación de la red** |
| **3 · Arranque del motor** | **Por batería**; con un número limitado de intentos |
| **4 · Estabilización** | **Espera a que tensión y frecuencia estén dentro de límites** |
| **5 · Cierre del interruptor de grupo** | **La instalación queda alimentada** |
| **6 · Toma de carga por escalones** | **Si el automatismo lo prevé** |
| **7 · Vuelta de la red** | **Se confirma durante un tiempo, para evitar retornos inestables** |
| **8 · Retransferencia** | **Con corte o sin corte, según el sistema** |
| **9 · REFRIGERACIÓN y parada** | **El motor sigue girando EN VACÍO unos minutos antes de pararse** |

**Las dos fases que la gente no espera y que hay que saber justificar:**

- **La 7.** **La red vuelve a menudo de forma inestable**, con microcortes. **Retransferir al primer
  parpadeo puede dejar la instalación sin nada.** **Por eso se confirma la red durante un tiempo antes
  de volver.**
- **La 9.** **Un motor térmico que se para inmediatamente después de trabajar a plena carga acumula
  calor sin circulación de refrigerante.** **El giro en vacío evacua ese calor**, y **saltárselo acorta
  la vida del motor.**

## 6. El mantenimiento y las pruebas

**Lo que hay que hacer para que el grupo esté cuando haga falta**, y **enlaza con el tema 9:**

| Tarea | Por qué |
|---|---|
| **Nivel y estado del COMBUSTIBLE** | **El gasóleo se degrada y cría microorganismos** si está mucho tiempo parado |
| **Nivel de refrigerante y de aceite** | Lo evidente |
| **BATERÍA de arranque y su cargador** | **Es la causa número uno de que un grupo no arranque** |
| **Precalentamiento del motor** | Facilita el arranque en frío |
| **Prueba periódica de ARRANQUE** | Que arranque |
| **Prueba periódica CON CARGA** | **Que aguante** |
| **Prueba de TRANSFERENCIA completa** | **Que la conmutación funcione** |
| **Estado de antivibratorios, manguitos y escape** | Envejecen |

**Y la advertencia que este temario subraya y que ya apareció en el tema 9**: **una prueba de arranque
EN VACÍO no demuestra casi nada.** **Un grupo que arranca y gira sin carga no prueba que el alternador
regule, que la conmutación transfiera ni que la refrigeración baste.** **Y hay más**: **hacer trabajar
un motor diésel largo rato en vacío o a carga muy baja produce carbonilla y lo estropea.**

**Lo que hay que probar, entonces, y con qué**: **la prueba correcta es con carga**, y **si la carga
real no se puede arriesgar, con un BANCO DE CARGAS resistivo.** **Es la única forma de comprobar la
potencia sin apagar la casa.**

**Y la prueba que nadie hace y que es la única que prueba lo importante**: **la de TRANSFERENCIA
completa, con la instalación real.** **Exige una ventana pactada y aceptar un riesgo controlado**, y
**es exactamente el mismo argumento del tema 9: una redundancia que no se ha provocado nunca no se
sabe si funciona.**

## 7. El grupo en una casa que emite

**Las tres decisiones propias que este temario aporta y que ningún manual de grupos trae:**

1. **Qué cuelga del grupo y qué no.** **Un grupo dimensionado para toda la casa es carísimo y trabaja
   siempre descargado.** **Lo correcto es un CUADRO DE SOCORRO con lo que de verdad no puede caerse**
   —control central, emisión, servidores, refrigeración de las salas técnicas, alumbrado de seguridad
   y ascensores— **y deslastre automático de lo demás.**
2. **La refrigeración de las salas técnicas VA en el grupo.** **Es el olvido clásico**: se salva el
   equipamiento y se deja fuera el aire acondicionado, **y una sala de servidores sin refrigeración se
   apaga sola en minutos.** **La continuidad eléctrica sin continuidad térmica no sirve.**
3. **La autonomía se decide por el ESCENARIO, no por una cifra redonda.** **Cuántas horas hay que
   aguantar depende de si el corte previsible es de minutos o de horas, y de en cuánto tiempo se puede
   traer combustible.** **Y el depósito, a partir de cierto tamaño, deja de ser un accesorio del grupo
   y pasa a ser una instalación petrolífera con su propio reglamento.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal nueva**: lo que este tema afirma del reglamento está **citado literalmente en los temas 8 y 10** de este mismo específico, y **aquí se remite** |

**Cinco declaraciones expresas:**

1. **Este tema NO tiene cita literal propia**, y **lo dice.** **Las condiciones del local del generador,
   la clasificación de instalaciones generadoras, los requisitos de la transferencia sin corte, las
   categorías de conmutación y el umbral del 70 % están citados o resumidos en los temas 8 y 10**,
   **con su apartado identificado**, y **aquí se aplican al grupo electrógeno.**
2. **Este tema NO da ninguna potencia, ningún coeficiente de corrección por altitud o temperatura,
   ningún escalón de carga admisible, ninguna autonomía y ningún nivel de ruido.** **Son dato de
   fabricante y de norma de producto**, y **una cifra que no se ha leído en su fuente no se escribe.**
3. **Los regímenes de servicio se describen por lo que permiten y NO se les asignan las siglas ni los
   porcentajes de la norma internacional que los define**, que **no se ha consultado.**
4. **El reglamento de instalaciones petrolíferas se nombra por lo que regula —el depósito de
   combustible del grupo— y no se cita**: **está volcado y citado en el temario de Ingeniería Técnica
   · Industrial de este mismo proyecto**, y **aquí sólo se remite.**
5. **La reglamentación de ruido y vibraciones no está en el enunciado de este punto y no se ha
   consultado.** **Lo que el tema dice sobre las tres vías de transmisión es oficio de
   instalaciones**, y **no se le atribuye ningún límite ni ninguna norma.**

**El resto del tema va como oficio y así se declara**: la lectura de la coletilla «condiciones de
trabajo» como clave del punto, la distinción entre autonomía y continuidad, la separación entre el
regulador de velocidad y el de excitación, la regla de que la misma máquina declara más potencia cuanto
menos trabaja, el aviso sobre dimensionar en kilovatios con un factor de potencia peor, la explicación
del escalón de carga por la caída de frecuencia, la explicación de los tres aires que necesita un
grupo, el aviso sobre el escape junto a la toma de aire, las tres vías de transmisión del ruido con la
advertencia sobre la estructural, la secuencia de nueve fases con la justificación de la confirmación
de red y del giro en vacío, la advertencia sobre las pruebas en vacío y el banco de cargas, y las tres
decisiones propias de una casa que emite. **Nada de eso lo dice la norma con esas palabras**, y el tema
no lo presenta como si lo dijera.
