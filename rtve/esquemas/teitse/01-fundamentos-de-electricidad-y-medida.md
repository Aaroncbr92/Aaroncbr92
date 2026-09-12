# Esquema · Tema 1 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Fundamentos de electricidad y medida

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = norma citada literalmente en el tema ·
`[of]` = oficio eléctrico · `[plan]` = enunciado del anexo. **Siglas y símbolos**: el reglamento
electrotécnico para baja tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**);
el voltio (**V**), el amperio (**A**), el ohmio (**Ω**), el vatio (**W**) y el voltamperio (**VA**); el
hercio (**Hz**); la corriente alterna (**CA**) y la corriente continua (**CC**); el valor eficaz
(**RMS**, *root mean square*); y la Asociación Española de Normalización (**UNE**).

**Cabecera.** Enunciado: punto 1 del anexo, **fundamentos** · **el reparto que hay que decir primero**:
**este punto NOMBRA transformadores y motores y el punto 2 los DESARROLLA** —**aquí se presentan y se
remite**— · **el aviso que ordena la ocupación entera**: **los dos últimos puntos del específico son el
reglamento y sus instrucciones**, así que **casi toda la física de aquí acaba teniendo un artículo
detrás.**

<!-- indice -->

## Índice

- [Las tres magnitudes y la ley de Ohm](#las-tres-magnitudes-y-la-ley-de-ohm)
- [Potencia, energía y factor de potencia](#potencia-energía-y-factor-de-potencia)
- [Continua y alterna](#continua-y-alterna)
- [El sistema trifásico](#el-sistema-trifásico)
- [La medida](#la-medida)
- [Las dos máquinas: dónde se estudian](#las-dos-máquinas-dónde-se-estudian)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## Las tres magnitudes y la ley de Ohm

| Magnitud | Qué es | Símbolo | Unidad |
|---|---|---|---|
| **Tensión** | **El trabajo para mover una carga entre dos puntos**: la causa | **U** o **V** | **Voltio** |
| **Intensidad** | **Carga que atraviesa una sección por unidad de tiempo**: el efecto | **I** | **Amperio** |
| **Resistencia** | **La oposición al paso de la corriente** | **R** | **Ohmio** |

- **LAS TRES FORMAS DE LA LEY** · `[of]` · **U = R · I** (caída en un tramo) · **I = U / R** (corriente
  de un receptor) · **R = U / I** (resistencia deducida de una medida). **Un examen pide cualquiera.**
- **LA LECTURA QUE DECIDE UN CÁLCULO** · `[of]` · **La tensión es dato —la de la red— y la resistencia
  es lo que se elige.** **Lo que resulta es la CORRIENTE**, y **la corriente dimensiona cable e
  interruptor.** **Un cálculo de instalación no empieza en la ley de Ohm: ACABA en ella.**
- **LA RESISTENCIA DE UN CONDUCTOR** · `[of]` · **R = ρ · L / S** · **ρ** resistividad del material,
  **dependiente de la temperatura** · **L** longitud · **S** sección.
- **LAS TRES CONSECUENCIAS, QUE SON EL FUNDAMENTO DEL PUNTO 5** · `[of]` · **crece con la LONGITUD**
  (línea larga cae más) · **baja con la SECCIÓN** (cable grueso cae menos) · **depende del MATERIAL**
  (**el cobre conduce mejor que el aluminio** y **a igual corriente el aluminio pide más sección**).
- **LA CUARTA, QUE NO SE LEE EN LA FÓRMULA** · `[of]` · **la resistividad SUBE con la temperatura** ·
  **un conductor cargado se calienta, y al calentarse conduce peor y se calienta más** · **ésa es la
  razón física de que las intensidades admisibles dependan de la instalación y del ambiente.**

## Potencia, energía y factor de potencia

- **CONTINUA** · `[of]` · **P = U · I**, en vatios.

| Potencia | Qué es | Unidad | Monofásica |
|---|---|---|---|
| **ACTIVA, P** | **La que se transforma en trabajo o calor** | **Vatio** | **P = U · I · cos φ** |
| **REACTIVA, Q** | **La que va y vuelve** para magnetizar y cargar | **var** | **Q = U · I · sen φ** |
| **APARENTE, S** | **La que la instalación tiene que poder transportar** | **Voltamperio** | **S = U · I** |

- **TRIFÁSICA** · `[of]` · **P = √3 · U · I · cos φ**, con **U** entre fases.
- **QUÉ ES EL FACTOR DE POTENCIA** · `[of]` · **el cociente entre activa y aparente** · **un cos φ bajo
  significa que por el cable circula MÁS corriente de la que hace falta para el trabajo que se hace.**
- **LAS CUATRO CONSECUENCIAS** · `[of]` · **más corriente** (**I = P / (U · cos φ)**) · **más caída y
  más pérdidas** · **más sección y más aparamenta** · **penalización en factura.**
- **LO QUE LO CORRIGE** · `[of]` · **la batería de condensadores**, **lo más cerca posible de la carga
  que causa el problema** · **la carga inductiva típica es el MOTOR**, y eso enlaza con el tema 2.
- **ENERGÍA** · `[of]` · **E = P · t**, en kilovatios hora · **la potencia se contrata; la energía se
  gasta.**

## Continua y alterna

| | **Continua** | **Alterna** |
|---|---|---|
| **Sentido** | **Siempre el mismo** | **Se invierte cada semiperiodo** |
| **Valor** | **Constante** | **Senoidal** |
| **De dónde sale** | **Pilas, baterías, rectificadores, paneles** | **Alternadores** |
| **Transformable** | **No directamente** | **Sí, con TRANSFORMADOR** |
| **Dónde manda** | **Electrónica, baterías, tracción, alimentación ininterrumpida** | **Generación, transporte y distribución** |

- **POR QUÉ LA RED ES ALTERNA** · `[of]` · **se eleva y se reduce con un transformador, sin partes
  móviles y con rendimiento altísimo** · **elevar la tensión transporta la misma potencia con menos
  corriente** porque **las pérdidas van con el CUADRADO de la corriente** · **ésa es toda la
  justificación de que exista una red de alta tensión, y del punto 6 del anexo.**
- **LAS MAGNITUDES DE UNA SEÑAL ALTERNA** · `[of]` · **pico** · **pico a pico** · **medio** (**en una
  senoide completa es CERO**) · **EFICAZ** (**el de una continua de igual efecto calorífico**) ·
  **periodo T** · **frecuencia f = 1 / T.**
- **LA REGLA QUE HAY QUE DECIR EN VOZ ALTA** · `[of]` · **cuando se dice que la red es de 230 voltios,
  son 230 EFICACES** · **el eficaz es el máximo dividido por raíz de dos**, así que **hay picos de unos
  325** · **importa porque los aislamientos se dimensionan por el PICO, no por el eficaz.**
- **LA CITA DEL TEMA** · `[BOE]` · **Artículo 4.2 del REBT: las tensiones nominales usuales en alterna
  serán a) 230 V entre fases para las trifásicas de tres conductores y b) 230 V entre fase y neutro y
  400 V entre fases para las trifásicas de 4 conductores** · **artículo 4.4: la frecuencia empleada en
  la red será de 50 Hz.**
- **LO QUE LA NORMA NO DICE** · `[of]` · **la relación entre 230 y 400 es la RAÍZ DE TRES**, y **es
  geometría de vectores desfasados 120 grados** · **el reglamento da las dos cifras y no las relaciona.**

## El sistema trifásico

- **DEFINICIÓN** · `[of]` · **tres tensiones alternas de igual amplitud y frecuencia, desfasadas 120
  grados.**
- **LAS TRES RAZONES DE USARLO** · `[of]` · **más potencia con menos cobre** que tres monofásicos ·
  **potencia instantánea CONSTANTE**, y de ahí **un par de motor uniforme** · **permite un campo
  magnético giratorio**, que **hace girar un asíncrono sin artificio de arranque** (tema 2).

| Conexión | Cómo se une | Tensiones | Corrientes |
|---|---|---|---|
| **ESTRELLA** | **Un extremo de cada devanado a un común, el NEUTRO** | **La de línea es raíz de tres veces la de fase** | **La de línea es igual a la de fase** |
| **TRIÁNGULO** | **Cada devanado entre dos fases**, en serie cerrada | **La de línea es igual a la de fase** | **La de línea es raíz de tres veces la de fase** |

- **LA REGLA QUE EVITA CONFUNDIRLAS** · `[of]` · **la raíz de tres está SIEMPRE y cambia de sitio**:
  **en estrella, en la TENSIÓN**; **en triángulo, en la CORRIENTE.**
- **LA CONSECUENCIA QUE SOSTIENE EL ARRANQUE DEL TEMA 2** · `[of]` · **el mismo motor en estrella
  recibe por devanado una tensión raíz de tres veces menor que en triángulo** y **absorbe una potencia
  TRES veces menor.**
- **EL NEUTRO** · `[of]` · **conductor unido al punto común de la estrella** · **da dos tensiones en la
  misma red** —230 y 400— · **y por él circula el DESEQUILIBRIO**: **una instalación muy desequilibrada
  carga el neutro.**

## La medida

| Instrumento | Conexión | Resistencia interna | Por qué |
|---|---|---|---|
| **VOLTÍMETRO** | **En PARALELO** | **MUY ALTA**, idealmente infinita | **Para no derivar corriente** |
| **AMPERÍMETRO** | **En SERIE**, abriendo el circuito | **MUY BAJA**, idealmente cero | **Para no añadir caída** |

- **EL ERROR MÁS GRAVE CON UN POLÍMETRO** · `[of]` · **amperímetro en paralelo sobre una tensión es un
  CORTOCIRCUITO a través del instrumento** · **se funde su fusible**, y **con una fuente potente detrás
  lo que sale es un arco.**
- **LA PINZA AMPERIMÉTRICA, HERRAMIENTA CARACTERÍSTICA** · `[of]` · **mide sin abrir el circuito** ·
  **aísla al operador**, porque **mide por el campo magnético** · **abraza UN solo conductor**: **si
  abraza los dos, la suma es cero.**
- **LA APLICACIÓN DE ESE ÚLTIMO RASGO** · `[of]` · **abrazar fase y neutro juntos debería dar CERO** ·
  **si no da cero hay corriente que se va por otro camino**: **una FUGA** · **es la medida con la que se
  busca la derivación que hace saltar un diferencial.**

| Tecnología de pinza | Qué mide |
|---|---|
| **De transformador de corriente** | **Sólo ALTERNA**: necesita campo variable |
| **De efecto Hall** | **ALTERNA Y CONTINUA** |

- **LA TRAMPA CLÁSICA DE LA LECTURA EN ALTERNA** · `[of]` · **un polímetro convencional mide el valor
  medio rectificado y lo escala suponiendo senoide perfecta** · **ante una corriente deformada
  —variador, fuente conmutada, balasto electrónico— la lectura es FALSA por defecto** · **hay que usar
  VERDADERO VALOR EFICAZ**, y **en una instalación moderna es la única lectura fiable.**

| Instrumento | Qué mide |
|---|---|
| **Polímetro** | **Tensión, corriente, resistencia, continuidad** |
| **Telurómetro** | **La resistencia de una puesta a tierra** |
| **Megóhmetro** | **La resistencia de AISLAMIENTO**, con tensión de ensayo elevada |
| **Analizador de redes** | **Potencias, factor de potencia, armónicos y calidad de onda** |
| **Comprobador de instalaciones** | **Bucle de defecto, disparo del diferencial, continuidad, aislamiento** |

- **LA REGLA DE SEGURIDAD QUE PRECEDE A TODA MEDIDA** · `[of]` · **saber qué se va a medir y con qué
  categoría de medida está clasificado el instrumento** · **un polímetro de categoría insuficiente en
  cabecera es un accidente esperando el transitorio.** (Tema 14.)

## Las dos máquinas: dónde se estudian

| Máquina | Qué hace | Dónde |
|---|---|---|
| **Transformador** | **Cambia la tensión de una alterna sin cambiar su frecuencia** | **Tema 2**, epígrafes 1 a 4 |
| **Motor** | **Convierte energía eléctrica en mecánica de rotación** | **Tema 2**, epígrafes 5 a 8 |

| Ley | Qué dice | Qué explica |
|---|---|---|
| **Inducción electromagnética** | **Un flujo magnético VARIABLE induce tensión** | **El transformador**, y **por qué no funciona en continua** |
| **Fuerza sobre un conductor** | **Un conductor con corriente en un campo sufre una fuerza** | **El par de un motor** |

- **LA FRONTERA QUE EXPLICA LA PRIMERA LEY** · `[of]` · **el transformador necesita flujo variable y
  una continua no lo da** · **de ahí que la continua no se transforme directamente y que toda la red de
  transporte sea alterna.**

## Aviso de estudio

- **LO QUE ESTE TEMA NO DA** · `[of]` · **ninguna tabla de intensidades admisibles, ninguna
  resistividad y ninguna caída máxima** · **están en las instrucciones**, y **se estudian en los temas
  5 y 15.**
- **LA NORMA QUE SE NOMBRA Y NO SE CONSULTA** · `[of]` · **la UNE 20.460-6-61**, que la instrucción de
  verificaciones nombra como metodología, **y las categorías de medida**, que son de norma de producto.
