# Esquema · Tema 5 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Cálculo de líneas: longitudes y secciones

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = instrucción técnica citada
literalmente en el tema · `[of]` = oficio de cálculo · `[plan]` = enunciado del anexo. **Siglas y
símbolos**: el reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones
(**ITC-BT-10**, **ITC-BT-15**, **ITC-BT-19**, **ITC-BT-44**, **ITC-BT-47**); la caída de tensión (**e**
o **ΔU**); la conductividad (**γ**) y la resistividad (**ρ**); la intensidad de diseño (**IB**), la
asignada de la protección (**In**) y la máxima admisible del conductor (**Iz**); el factor de potencia
(**cos φ**); el milímetro cuadrado (**mm²**); y el metro (**m**).

**Cabecera.** Enunciado: punto 5 del anexo, **siete palabras**, **el más corto y el más OPERATIVO** ·
**la idea antes de ningún número**: **una sección se calcula por DOS criterios y se elige la MAYOR de
las dos.**

| Criterio | Qué garantiza | De qué depende |
|---|---|---|
| **CALENTAMIENTO** | **Que el cable no se destruya por temperatura** | **De la corriente y de cómo está instalado** |
| **CAÍDA DE TENSIÓN** | **Que al receptor le llegue tensión suficiente** | **De la corriente Y DE LA LONGITUD** |

- **LA CONSECUENCIA QUE RESPONDE AL ENUNCIADO** · `[of]` · **la longitud NO influye en el calentamiento
  y SÍ en la caída** · **por eso el anexo dice «longitudes y secciones» en la misma frase**: **en
  líneas cortas manda el calentamiento y en líneas largas manda la caída.**

<!-- indice -->

## Índice

- [El criterio de calentamiento](#el-criterio-de-calentamiento)
- [El criterio de caída de tensión](#el-criterio-de-caída-de-tensión)
- [Las fórmulas](#las-fórmulas)
- [Cómo se calcula una línea, paso a paso](#cómo-se-calcula-una-línea-paso-a-paso)
- [Los casos que cambian el cálculo](#los-casos-que-cambian-el-cálculo)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## El criterio de calentamiento

- **LA CONDICIÓN** · `[of]` · **IB ≤ In ≤ Iz.**

| Término | Qué es |
|---|---|
| **IB** | **La corriente de DISEÑO**: la que va a circular de verdad |
| **In** | **La asignada de la PROTECCIÓN** puesta en su origen |
| **Iz** | **La máxima ADMISIBLE del conductor** en sus condiciones de instalación |

- **LAS DOS DESIGUALDADES DICEN COSAS DISTINTAS** · `[of]` · **IB ≤ In**: **la protección no puede
  dispararse con la corriente normal de servicio** · **In ≤ Iz**: **la protección tiene que actuar
  ANTES de que el cable se dañe** —**ésa es la que protege el cable**, y **la que se incumple cuando
  alguien sube el calibre porque «saltaba».**
- **LO QUE UN EXAMEN PERSIGUE** · `[of]` · **la intensidad admisible NO es propiedad del cable solo**:
  **es del cable EN SU INSTALACIÓN.**

| Factor | Cómo influye |
|---|---|
| **Sección** | **A más sección, más corriente**, no proporcionalmente |
| **Material** | **Cobre admite más que aluminio a igual sección** |
| **AISLAMIENTO** | **A más temperatura admisible, más corriente** |
| **MODO DE INSTALACIÓN** | **Al aire, en tubo, empotrado, enterrado, en bandeja** |
| **TEMPERATURA AMBIENTE** | **A más temperatura, menos corriente** |
| **AGRUPAMIENTO** | **Cuantos más circuitos juntos, menos cada uno** |

- **EL AVISO SOBRE LOS DOS ÚLTIMOS** · `[of]` · **son de CORRECCIÓN y son los que más se olvidan** ·
  **la tabla da un valor para condiciones de referencia y sobre él se aplican los coeficientes** · **un
  haz de ocho circuitos en un tubo a cuarenta grados admite bastante menos que el mismo cable solo y al
  aire a veinticinco.**

## El criterio de caída de tensión

| Consecuencia de una caída excesiva | Por qué |
|---|---|
| **El receptor recibe menos tensión** | Y **no da su potencia** |
| **Un motor pierde PAR** | El par va con el cuadrado de la tensión |
| **Una lámpara de descarga puede no arrancar** | Necesita una tensión mínima |
| **Se pierde energía en calor en el cable** | Dinero que se paga y no se usa |

- **LA CITA MÁS PREGUNTABLE DEL PUNTO** · `[BOE]` · **ITC-BT-19, apartado 2.2.2: la sección se
  determinará de forma que la caída entre el origen de la instalación interior y cualquier punto de
  utilización sea, salvo lo prescrito en las instrucciones particulares, menor del 3 % de la tensión
  nominal para cualquier circuito interior de viviendas, y para otras instalaciones interiores o
  receptoras, del 3 % para alumbrado y del 5 % para los demás usos · esta caída se calculará
  considerando alimentados todos los aparatos de utilización susceptibles de funcionar
  simultáneamente.**

| Caso | Caída máxima |
|---|---|
| **Circuito interior de VIVIENDAS** | **3 %** |
| **Otras instalaciones: ALUMBRADO** | **3 %** |
| **Otras instalaciones: LOS DEMÁS USOS** | **5 %** |

- **EL CASO DE UNA INDUSTRIA O DE UNA CASA QUE EMITE** · `[BOE]` · **ITC-BT-19, apartado 2.2.2: para
  instalaciones industriales que se alimenten directamente en alta tensión mediante un transformador de
  distribución propio, se considerará que la instalación interior de baja tensión tiene su origen en la
  salida del transformador · en este caso las caídas máximas admisibles serán del 4,5 % para alumbrado
  y del 6,5 % para los demás usos.**
- **LAS DOS COSAS QUE HAY QUE LEER AHÍ** · `[of]` · **los porcentajes SUBEN: 4,5 y 6,5** · **y suben
  porque el ORIGEN se mueve**: **con centro de transformación propio el origen es la salida del
  transformador**, y **eso mete en el cómputo un tramo que antes quedaba fuera** · **no es más
  tolerancia: es la misma tolerancia contada desde más atrás.**
- **LA COMPENSACIÓN QUE LA PRIMERA CITA PERMITE** · `[BOE]` · **la caída puede compensarse entre la de
  la instalación interior y la de las derivaciones individuales**, de forma que **la total quede por
  debajo de la suma de los dos límites.**
- **LA PALABRA QUE DECIDE CUÁNTOS AMPERIOS ENTRAN EN LA FÓRMULA** · `[of]` · **SIMULTANEIDAD** · **es
  lo que separa un cálculo honesto de uno que sale barato.**

## Las fórmulas

| Sistema | Caída | Sección despejada |
|---|---|---|
| **MONOFÁSICO** | **e = 2 · L · I · cos φ / (γ · S)** | **S = 2 · L · I · cos φ / (γ · e)** |
| **TRIFÁSICO** | **e = √3 · L · I · cos φ / (γ · S)** | **S = √3 · L · I · cos φ / (γ · e)** |

- **LA ÚNICA DIFERENCIA ENTRE LAS DOS, EXPLICADA** · `[of]` · **el 2 del monofásico es el CAMINO DE
  IDA Y VUELTA** —**la corriente va por la fase y vuelve por el neutro, y las dos caen**— · **la raíz de
  tres del trifásico sale de la composición vectorial de las tres fases** · **quien entienda eso no las
  confunde.**
- **LAS CUATRO LECTURAS DIRECTAS** · `[of]` · **la sección es PROPORCIONAL a la longitud** —**el doble
  de metros, el doble de sección**— · **PROPORCIONAL a la corriente** · **INVERSAMENTE proporcional a
  la caída admitida** —**admitir la mitad de caída duplica la sección**— · **a igual potencia el
  trifásico pide MENOS cobre**, y **ésa es la razón económica de repartir cargas en trifásica.**
- **EL AVISO QUE SEPARA UN CÁLCULO BUENO DE UNO OPTIMISTA** · `[of]` · **la conductividad depende de la
  TEMPERATURA** y **la del cable en servicio no es la de veinte grados** · **calcular a temperatura
  ambiente da una sección MENOR de la necesaria**: **lo prudente es la temperatura máxima de servicio
  del aislamiento.**

## Cómo se calcula una línea, paso a paso

| Paso | Qué se hace |
|---|---|
| **1 · Potencia prevista** | **Sumar cargas** y **aplicar simultaneidad y utilización** |
| **2 · Corriente de diseño** | **IB**, de la potencia, la tensión y el factor de potencia |
| **3 · Sección por CALENTAMIENTO** | **Tabla con el modo de instalación** + **coeficientes de corrección** |
| **4 · Sección por CAÍDA** | **Fórmula, longitud real y límite que corresponda** |
| **5 · La MAYOR de las dos** | Y **normalizar a la sección comercial inmediatamente superior** |
| **6 · Conductor de PROTECCIÓN** | **Su sección se deduce de la de fase**, según tabla |
| **7 · Comprobar el CORTOCIRCUITO** | **Que el cable soporta la energía hasta que la protección corta** |
| **8 · Elegir la PROTECCIÓN** | **IB ≤ In ≤ Iz**, curva y poder de corte |

- **LOS DOS QUE MÁS SE SALTAN** · `[of]` · **el conductor de protección no se elige «igual que la fase»
  por costumbre**: **hay relación reglamentada por sección de fase**, y **para secciones grandes puede
  ser menor** · **la comprobación de cortocircuito garantiza que el CABLE aguanta hasta que la
  protección actúa**: **un cable protegido contra sobrecarga puede no estarlo contra cortocircuito si
  el aparato tarda demasiado.**

| Factor del paso 1 | Qué corrige |
|---|---|
| **De UTILIZACIÓN** | **Que un receptor no siempre trabaja a su máxima potencia** |
| **De SIMULTANEIDAD** | **Que no todos funcionan a la vez** |

## Los casos que cambian el cálculo

| Caso | Qué cambia |
|---|---|
| **MOTORES** | **La línea de un solo motor se dimensiona para una corriente MAYOR que la nominal**, por la punta de arranque; en grupo, con criterio propio |
| **Lámparas de DESCARGA** | **La carga se calcula por encima de la potencia nominal**, por los equipos auxiliares |
| **ARMÓNICOS** | **El neutro puede llevar más que las fases**: su sección debe ser **como mínimo igual a la de fase** en interiores, salvo justificación por cálculo |

- **POR QUÉ EL TERCERO ES CONTRAINTUITIVO** · `[of]` · **en trifásico equilibrado con cargas LINEALES
  las tres corrientes se anulan en el neutro** · **con cargas NO LINEALES —fuentes conmutadas,
  alumbrado electrónico, variadores— aparecen armónicos de orden tres y múltiplos**, y **ésos NO se
  anulan: se SUMAN en el neutro.**
- **EL CASO DE UNA CASA QUE EMITE ES EXACTAMENTE ÉSE** · `[of]` · **vídeo, informática y alumbrado de
  plató son fuentes conmutadas** · **dimensionar el neutro como si las cargas fueran resistivas es el
  error de proyecto más caro y menos visible**, porque **en muchos esquemas el neutro no lleva
  protección y su sobrecalentamiento no dispara nada.**

## Aviso de estudio

- **LOS ÚNICOS NÚMEROS DEL TEMA** · `[BOE]` · **los cinco porcentajes de caída** —**3, 3, 5, 4,5 y
  6,5**—, **citados literalmente.**
- **LO QUE NO SE REPRODUCE** · `[of]` · **ninguna tabla de intensidades admisibles, ningún coeficiente
  de corrección, ninguna conductividad, ningún factor de simultaneidad y ninguna relación de sección
  del conductor de protección** · **el tema dice qué contiene cada tabla, dónde está y en qué sentido
  influye cada variable.**
