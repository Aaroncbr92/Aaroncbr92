# Esquema · Tema 11 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Sistemas de generación: grupos electrógenos

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = exigencia del reglamento, citada en
los temas 8 y 10 y aquí aplicada · `[of]` = oficio de instalaciones · `[plan]` = enunciado del anexo.
**Siglas**: el reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones
(**ITC-BT-28**, **ITC-BT-40**); el kilovoltamperio (**kVA**) y el kilovatio (**kW**); el hercio
(**Hz**) y las revoluciones por minuto (**r.p.m.**); el sistema de alimentación ininterrumpida
(**SAI**); la instrucción de almacenamiento en instalaciones de consumo (**MI-IP 03**); y el decibelio
ponderado A (**dBA**).

**Cabecera.** Enunciado: punto 11 del anexo · **la coletilla que hay que leer con atención**:
**«CONDICIONES DE TRABAJO»** —**no dice «características» ni «tipos»**—, y **eso es lo que un examen
buscará**: **en qué régimen puede trabajar un grupo, cuánto tiempo, con qué carga y con qué
emplazamiento** · **la idea que más se confunde**: **un grupo da AUTONOMÍA y no da CONTINUIDAD**;
**tarda en arrancar y en tomar carga**, y **lo que cubre ese hueco es la batería del tema 12** · **los
dos juntos son un sistema; cada uno por su cuenta, no.**

<!-- indice -->

## Índice

- [Qué es y de qué partes consta](#qué-es-y-de-qué-partes-consta)
- [Las condiciones de trabajo](#las-condiciones-de-trabajo)
- [El emplazamiento](#el-emplazamiento)
- [El régimen respecto a la red](#el-régimen-respecto-a-la-red)
- [La secuencia de funcionamiento](#la-secuencia-de-funcionamiento)
- [Mantenimiento y pruebas](#mantenimiento-y-pruebas)
- [El grupo en una casa que emite](#el-grupo-en-una-casa-que-emite)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## Qué es y de qué partes consta

| Parte | Qué hace |
|---|---|
| **MOTOR térmico** | **Gasóleo o gas**; da el par y la velocidad |
| **ALTERNADOR** | **Convierte el giro en tensión alterna**: la máquina síncrona del tema 2 |
| **Regulador de VELOCIDAD** | **Mantiene las revoluciones, y con ellas la FRECUENCIA** |
| **Regulador de TENSIÓN** | **Ajusta la excitación del alternador** |
| **Cuadro de control y mando** | **Arranque, medidas, alarmas, parada** |
| **Sistema de arranque** | **Batería, motor de arranque y cargador** |
| **Depósito de combustible** | **Diario y, en su caso, nodriza** |
| **Refrigeración** | **Radiador y ventilador, o intercambiador** |
| **Escape** | **Silencioso y conducto al exterior** |
| **Bancada y antivibratorios** | **Soporte y aislamiento de vibración** |

- **LA RELACIÓN QUE EXPLICA EL REGULADOR DE VELOCIDAD** · `[of]` · **la FRECUENCIA depende de la
  VELOCIDAD DE GIRO y del número de pares de polos** · **mantener 50 hercios es mantener las
  revoluciones**, y **un grupo con el regulador desajustado da mala FRECUENCIA, no mal voltaje.**

| Se ajusta | Con qué | Qué controla |
|---|---|---|
| **La FRECUENCIA** | **El regulador de velocidad del MOTOR** | Revoluciones por minuto |
| **La TENSIÓN** | **El regulador de EXCITACIÓN del alternador** | Campo magnético del rotor |

## Las condiciones de trabajo

| Régimen | Para qué |
|---|---|
| **EMERGENCIA o socorro** | **Sólo cuando falla la red**, horas limitadas al año y **sin sobrecarga admisible** |
| **PRINCIPAL, con carga variable** | **Continuado como fuente principal**, carga media limitada y sobrecarga durante un tiempo |
| **CONTINUO** | **Carga constante y horas ilimitadas**: **el más exigente y el de menor potencia declarada** |

- **LA REGLA QUE SALE DE LA TABLA** · `[of]` · **la misma máquina declara MÁS potencia cuanto MENOS va
  a trabajar** · **comparar dos ofertas sin mirar el régimen es comparar dos cosas distintas.**
- **POTENCIA Y FACTOR DE POTENCIA** · `[of]` · **se declara en kilovoltamperios y en kilovatios**, y
  **la relación es el factor de potencia de referencia** · **dimensionar en kilovatios para una carga
  con factor peor que el de referencia se queda corto en corriente.**

| Condición ambiental | Efecto |
|---|---|
| **ALTITUD** | **Menos densidad de aire, menos potencia del motor** |
| **TEMPERATURA** | **Más temperatura, menos potencia y menos refrigeración** |
| **HUMEDAD** | Efecto menor, pero contemplado |

- **EL ESCALÓN DE CARGA** · `[of]` · **un grupo no admite toda la carga de golpe** · **al conectar una
  carga grande el motor se frena, la frecuencia cae y el regulador tarda en recuperarla** · **por eso
  se mete POR ESCALONES**, y **los motores grandes arrancan con arrancador progresivo o variador para
  no exigirle la punta.** (Tema 2.)

## El emplazamiento

| Exigencia | Qué implica en obra |
|---|---|
| **Local de uso EXCLUSIVO** | **No se comparte con almacén ni con otras instalaciones** |
| **Protección contra incendios** | **Cumple las disposiciones que le correspondan** |
| **VENTILACIÓN suficiente**, sea cual sea la potencia | **Entrada de aire de combustión y refrigeración, y salida de aire caliente** |
| **Escape INCOMBUSTIBLE** | **Y evacuando DIRECTAMENTE al exterior**, o a aprovechamiento energético |
| **Depósitos y canalizaciones** | **Cumplen ADEMÁS sus propios reglamentos** |

- **LA EXIGENCIA MÁS SUBESTIMADA** · `[of]` · **un grupo necesita aire para TRES cosas**: **la
  combustión, la refrigeración del motor y la del alternador y el local** · **el caudal necesario es
  muy superior al que la intuición sugiere** · **una sala con rejilla pequeña hace que el grupo se pare
  por temperatura justo cuando más falta hace.**
- **EL ESCAPE MERECE PÁRRAFO** · `[of]` · **incombustible, aislado térmicamente donde pueda tocarse,
  con compensador de dilatación** —**se dilata mucho al calentarse**— **y saliendo donde los gases no
  vuelvan por la toma de aire** · **un escape junto a la entrada de ventilación hace que el grupo
  respire su propio humo.**

| Vía del ruido | Cómo se corta |
|---|---|
| **Por el AIRE** | **Cabina insonorizada, silencioso de escape, atenuadores en rejillas** |
| **Por la ESTRUCTURA** | **Antivibratorios bajo la bancada** y **conexiones flexibles** |
| **Por los CONDUCTOS** | **Manguitos flexibles**: uno rígido lleva la vibración a todo el edificio |

- **LA ADVERTENCIA DE PROYECTO** · `[of]` · **la vía estructural es la que se olvida y la que arruina
  una grabación** · **un grupo perfectamente insonorizado que apoya rígido sobre la losa hace vibrar
  los estudios de encima**, y **eso no lo arregla ninguna cabina.**

## El régimen respecto a la red

| Clase | Qué permite | Cómo conmuta |
|---|---|---|
| **AISLADA** | **Ninguna conexión con la red** | No hay conmutación con red |
| **ASISTIDA** | **Conexión, pero NUNCA en paralelo** | **Conmutación de todos los activos y el neutro**; **sin corte sólo con los requisitos del tema 10** |
| **INTERCONECTADA** | **Trabajo normal EN PARALELO** | Sincronización permanente |

- **EL GRUPO DE SOCORRO ES ASISTIDO** · `[BOE]` · **la conmutación corta TODOS los activos Y EL
  NEUTRO** —**no basta con conmutar fases**— · **el acoplamiento simultáneo tiene que ser IMPOSIBLE**:
  **enclavamiento mecánico además del eléctrico** (tema 3) · **para transferencia sin corte, potencia
  superior a 100 kVA, punto único, neutro desconectado de tierra en la interconexión, protecciones de
  tensión y frecuencia, antivertido y un máximo de CINCO SEGUNDOS.**
- **SU PAPEL EN LOS SERVICIOS DE SEGURIDAD** · `[BOE]` · **es una de las fuentes propias admitidas** y
  **su categoría es típicamente de CORTE MEDIANO** —15 segundos como máximo— · **nunca «sin corte» ni
  «corte muy breve»**, porque **tiene que arrancar** · **arranca al faltar la tensión o al bajar del
  70 % de su valor nominal.** (Tema 8.)

## La secuencia de funcionamiento

| Fase | Qué pasa |
|---|---|
| **1 · Detección del fallo** | **Falta de tensión o tensión bajo umbral**, con tiempo de confirmación |
| **2 · Apertura del interruptor de red** | **Se aísla la instalación** |
| **3 · Arranque del motor** | **Por batería**; intentos limitados |
| **4 · Estabilización** | **Tensión y frecuencia dentro de límites** |
| **5 · Cierre del interruptor de grupo** | **La instalación queda alimentada** |
| **6 · Toma de carga por escalones** | **Si el automatismo lo prevé** |
| **7 · Vuelta de la red** | **Se confirma durante un tiempo** |
| **8 · Retransferencia** | **Con corte o sin corte, según el sistema** |
| **9 · REFRIGERACIÓN y parada** | **El motor gira EN VACÍO unos minutos antes de pararse** |

- **LAS DOS FASES QUE NADIE ESPERA** · `[of]` · **la 7**: **la red vuelve a menudo inestable, con
  microcortes**, y **retransferir al primer parpadeo puede dejar la instalación sin nada** · **la 9**:
  **un motor que se para justo tras trabajar a plena carga acumula calor sin circulación de
  refrigerante**, y **saltarse el giro en vacío acorta su vida.**

## Mantenimiento y pruebas

| Tarea | Por qué |
|---|---|
| **Nivel y estado del COMBUSTIBLE** | **El gasóleo se degrada y cría microorganismos** si está mucho parado |
| **Refrigerante y aceite** | Lo evidente |
| **BATERÍA de arranque y su cargador** | **La causa número uno de que un grupo no arranque** |
| **Precalentamiento** | Facilita el arranque en frío |
| **Prueba de ARRANQUE** | Que arranque |
| **Prueba CON CARGA** | **Que aguante** |
| **Prueba de TRANSFERENCIA completa** | **Que la conmutación funcione** |
| **Antivibratorios, manguitos, escape** | Envejecen |

- **LA ADVERTENCIA QUE SE REPITE DESDE EL TEMA 9** · `[of]` · **una prueba en vacío no demuestra casi
  nada**: **no prueba que el alternador regule, que la conmutación transfiera ni que la refrigeración
  baste** · **y encima**, **hacer trabajar un diésel largo rato en vacío o a carga muy baja produce
  carbonilla y lo estropea.**
- **CON QUÉ SE PRUEBA** · `[of]` · **con carga**, y **si la real no se puede arriesgar, con un BANCO DE
  CARGAS resistivo** · **la que nadie hace es la de TRANSFERENCIA completa con la instalación real**:
  **exige ventana pactada y riesgo controlado** · **una redundancia que no se ha provocado nunca no se
  sabe si funciona.**

## El grupo en una casa que emite

- **QUÉ CUELGA DEL GRUPO Y QUÉ NO** · `[of]` · **uno dimensionado para toda la casa es carísimo y
  trabaja siempre descargado** · **lo correcto es un CUADRO DE SOCORRO** —control central, emisión,
  servidores, refrigeración de salas técnicas, alumbrado de seguridad, ascensores— **con deslastre
  automático de lo demás.**
- **EL OLVIDO CLÁSICO** · `[of]` · **la refrigeración de las salas técnicas VA en el grupo** · **se
  salva el equipamiento y se deja fuera el aire acondicionado**, y **una sala de servidores sin
  refrigeración se apaga sola en minutos** · **la continuidad eléctrica sin continuidad térmica no
  sirve.**
- **LA AUTONOMÍA SE DECIDE POR EL ESCENARIO** · `[of]` · **no por una cifra redonda**: **depende de si
  el corte previsible es de minutos o de horas y de en cuánto se puede traer combustible** · **y el
  depósito, a partir de cierto tamaño, deja de ser accesorio del grupo y pasa a ser una instalación
  petrolífera con su propio reglamento.**

## Aviso de estudio

- **ESTE TEMA NO TIENE CITA LITERAL PROPIA** · `[of]` · **lo que afirma del reglamento está citado en
  los temas 8 y 10, con su apartado identificado**, y **aquí se aplica al grupo.**
- **LO QUE NO SE DA** · `[of]` · **ninguna potencia, ningún coeficiente por altitud o temperatura,
  ningún escalón admisible, ninguna autonomía y ningún nivel de ruido** · **los regímenes se describen
  por lo que permiten y NO se les asignan las siglas ni los porcentajes de la norma internacional que
  los define, que no se ha consultado.**
