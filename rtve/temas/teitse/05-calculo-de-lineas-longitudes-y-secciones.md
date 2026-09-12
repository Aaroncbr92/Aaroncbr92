# Tema 5 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Cálculo de líneas: longitudes y secciones

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 5 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se cita **el apartado 2.2.2 de la ITC-BT-19**, en sus dos párrafos de caída de tensión |
| **Aviso de estudio** | **Una sección se calcula por DOS criterios y se elige la MAYOR.** **La longitud NO influye en el calentamiento y SÍ en la caída**: por eso el enunciado dice «longitudes y secciones» en la misma frase |
| **Extensión** | **2.999 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones (**ITC-BT-14**, **ITC-BT-15**, **ITC-BT-19**, **ITC-BT-40**);
la caída de tensión (**e** o **ΔU**); la conductividad del material (**γ**) y su inversa, la
resistividad (**ρ**); la intensidad de diseño o de cálculo (**IB**), la intensidad asignada de la
protección (**In**) y la intensidad máxima admisible del conductor (**Iz**); el factor de potencia
(**cos φ**); el milímetro cuadrado (**mm²**); y el metro (**m**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 5):
> «Cálculos de longitudes y secciones de líneas eléctricas.»

**Es el punto más CORTO del enunciado y el más OPERATIVO del anexo**: **una línea de siete palabras que
describe lo que un técnico de esta ocupación hace todas las semanas.**

**Y la idea que ordena el punto entero, dicha antes de ningún número**: **una sección se calcula por
DOS criterios y se elige la MAYOR de las dos secciones que resulten.**

| Criterio | Qué garantiza | De qué depende |
|---|---|---|
| **CALENTAMIENTO** o intensidad máxima admisible | **Que el cable no se destruya por temperatura** | **De la corriente y de cómo está instalado** |
| **CAÍDA DE TENSIÓN** | **Que al receptor le llegue tensión suficiente** | **De la corriente Y DE LA LONGITUD** |

**Y la consecuencia que hay que saber enunciar, porque es la respuesta a la pregunta implícita del
enunciado**: **la longitud NO influye en el calentamiento y SÍ en la caída de tensión.** **Por eso el
enunciado del anexo dice «longitudes y secciones» en la misma frase**: **en líneas cortas manda el
calentamiento y en líneas largas manda la caída.**

<!-- indice -->

## Índice

- [1. El criterio de calentamiento](#1-el-criterio-de-calentamiento)
- [2. El criterio de caída de tensión](#2-el-criterio-de-caída-de-tensión)
- [3. Las fórmulas de caída de tensión](#3-las-fórmulas-de-caída-de-tensión)
- [4. Cómo se calcula una línea, paso a paso](#4-cómo-se-calcula-una-línea-paso-a-paso)
- [5. Los casos particulares que cambian el cálculo](#5-los-casos-particulares-que-cambian-el-cálculo)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. El criterio de calentamiento

**La condición que hay que cumplir, en la forma que se escribe:**

**IB ≤ In ≤ Iz**

| Término | Qué es |
|---|---|
| **IB** | **La corriente de DISEÑO**: la que va a circular de verdad por el circuito |
| **In** | **La corriente asignada de la PROTECCIÓN** que se pone en su origen |
| **Iz** | **La intensidad máxima ADMISIBLE del conductor**, en sus condiciones de instalación |

**Las dos desigualdades dicen dos cosas distintas y hay que saber separarlas:**

1. **IB ≤ In**: **la protección no puede dispararse con la corriente normal de servicio.**
2. **In ≤ Iz**: **la protección tiene que actuar ANTES de que el cable se dañe.** **Ésa es la que
   protege el cable**, y **la que se incumple cuando alguien sube el calibre del magnetotérmico
   porque «saltaba».**

**De qué depende Iz, que es lo que un examen persigue**: **la intensidad máxima admisible de un cable
NO es una propiedad del cable sola**: **es del cable EN SU INSTALACIÓN.**

| Factor | Cómo influye |
|---|---|
| **Sección** | **A más sección, más corriente**, pero no proporcionalmente |
| **Material del conductor** | **Cobre admite más que aluminio a igual sección** |
| **AISLAMIENTO** | **A más temperatura admisible, más corriente** |
| **MODO DE INSTALACIÓN** | **Al aire, en tubo, empotrado, enterrado, en bandeja perforada o no** |
| **TEMPERATURA AMBIENTE** | **A más temperatura, menos corriente** |
| **AGRUPAMIENTO** | **Cuantos más circuitos juntos, menos corriente cada uno** |

**Los dos últimos son factores de CORRECCIÓN y son los que más se olvidan**, y **el aviso de oficio que
hay que dar es éste**: **la tabla da un valor para unas condiciones de referencia, y sobre ese valor
se aplican los coeficientes.** **Un haz de ocho circuitos dentro de un mismo tubo en una sala de
máquinas a cuarenta grados admite bastante menos corriente que el mismo cable solo y al aire a
veinticinco.**

**El temario NO reproduce ninguna tabla de intensidades admisibles ni ningún coeficiente**, y **lo
declara**: **están en las tablas de la instrucción técnica correspondiente**, y **una cifra que no se
ha leído en su fuente no se escribe.** **Lo que hay que saber es qué entra en la tabla y en qué
sentido influye cada cosa.**

## 2. El criterio de caída de tensión

**La caída de tensión es la parte de la tensión de origen que se pierde en el propio conductor**, y
**hay que decir por qué importa, porque no es evidente:**

| Consecuencia de una caída excesiva | Por qué |
|---|---|
| **El receptor recibe menos tensión de la nominal** | Y **no da su potencia** |
| **Un motor pierde PAR** | El par depende del cuadrado de la tensión |
| **Una lámpara de descarga puede no arrancar** | Necesita una tensión mínima |
| **Se pierde energía en forma de calor en el cable** | Que es dinero que se paga y no se usa |

**Y aquí está la cita que fija los límites, que es el dato más preguntable del punto entero:**

> «**La sección de los conductores a utilizar se determinará de forma que la caída de tensión entre el
> origen de la instalación interior y cualquier punto de utilización sea, salvo lo prescrito en las
> Instrucciones particulares, menor del 3 % de la tensión nominal para cualquier circuito interior de
> viviendas, y para otras instalaciones interiores o receptoras, del 3 % para alumbrado y del 5 % para
> los demás usos. Esta caída de tensión se calculará considerando alimentados todos los aparatos de
> utilización susceptibles de funcionar simultáneamente.**»
>
> — Real Decreto 842/2002, **ITC-BT-19**, apartado 2.2.2 (`BOE-A-2002-18099`), redacción vigente el 21
> de diciembre de 2022.

---

**Los tres porcentajes que hay que saber de memoria y no confundir:**

| Caso | Caída máxima admisible |
|---|---|
| **Cualquier circuito interior de VIVIENDAS** | **3 %** |
| **Otras instalaciones interiores o receptoras: ALUMBRADO** | **3 %** |
| **Otras instalaciones interiores o receptoras: LOS DEMÁS USOS** | **5 %** |

**Y el caso propio de una instalación industrial o de una casa que emite, que la propia instrucción
distingue y hay que citar aparte:**

> «**Para instalaciones industriales que se alimenten directamente en alta tensión mediante un
> transformador de distribución propio, se considerará que la instalación interior de baja tensión
> tiene su origen en la salida del transformador. En este caso las caídas de tensión máximas
> admisibles serán del 4,5 % para alumbrado y del 6,5 % para los demás usos.**»
>
> — Real Decreto 842/2002, **ITC-BT-19**, apartado 2.2.2 (`BOE-A-2002-18099`), redacción vigente el 21
> de diciembre de 2022.

---

**Las dos cosas que hay que leer en esa segunda cita, y son las que un examen busca:**

1. **Los porcentajes SUBEN: 4,5 y 6,5 en vez de 3 y 5.**
2. **Y suben porque el ORIGEN se mueve.** **Cuando hay centro de transformación propio, el origen de
   la instalación interior es la salida del transformador**, y **eso incluye en el cómputo un tramo
   que en el caso general estaba fuera.** **No es una tolerancia mayor: es la misma tolerancia contada
   desde más atrás.**

**Y la regla de compensación que la primera cita permite**: **la caída de tensión puede compensarse
entre la de la instalación interior y la de las derivaciones individuales**, de forma que **la total
sea inferior a la suma de los dos límites.** **Es decir: si una derivación individual cae poco, la
instalación interior puede caer algo más**, siempre dentro del total.

**Y el criterio de SIMULTANEIDAD que la cita impone**: **el cálculo se hace «considerando alimentados
todos los aparatos susceptibles de funcionar simultáneamente».** **Ésa es la palabra que decide
cuántos amperios se meten en la fórmula**, y **la que separa un cálculo honesto de uno que sale
barato.**

## 3. Las fórmulas de caída de tensión

**Las dos fórmulas del oficio, que salen de la ley de Ohm y de la geometría del sistema trifásico:**

| Sistema | Caída de tensión |
|---|---|
| **MONOFÁSICO** | **e = 2 · L · I · cos φ / (γ · S)** |
| **TRIFÁSICO** | **e = √3 · L · I · cos φ / (γ · S)** |

| Símbolo | Qué es |
|---|---|
| **e** | **La caída de tensión, en voltios** |
| **L** | **La longitud de la línea**, en metros |
| **I** | **La corriente**, en amperios |
| **γ** | **La conductividad del material**, inversa de la resistividad |
| **S** | **La sección**, en milímetros cuadrados |

**Y el detalle que hay que saber explicar, porque es la única diferencia entre las dos fórmulas**:
**el 2 del monofásico es el CAMINO DE IDA Y VUELTA** —la corriente va por la fase y vuelve por el
neutro, y las dos caen—; **la raíz de tres del trifásico sale de la composición vectorial de las tres
fases.** **Quien entienda eso no confunde las dos.**

**Despejando la sección, que es como se usan de verdad:**

| Sistema | Sección necesaria |
|---|---|
| **MONOFÁSICO** | **S = 2 · L · I · cos φ / (γ · e)** |
| **TRIFÁSICO** | **S = √3 · L · I · cos φ / (γ · e)** |

**Las cuatro lecturas que se hacen directamente en esas fórmulas, y que son lo que un examen premia:**

1. **La sección es PROPORCIONAL a la longitud.** **El doble de metros pide el doble de sección**, si
   todo lo demás se mantiene.
2. **La sección es PROPORCIONAL a la corriente.**
3. **La sección es INVERSAMENTE proporcional a la caída admitida.** **Admitir la mitad de caída
   duplica la sección.**
4. **A igual potencia, el trifásico pide MENOS cobre que el monofásico.** **Ésa es la razón económica
   de repartir cargas en trifásica siempre que se pueda.**

**Y el aviso de método sobre la conductividad, que es de los que separan un cálculo bueno de uno
optimista**: **la conductividad depende de la TEMPERATURA**, y **la del cable en servicio no es la de
veinte grados.** **Calcular con la conductividad a temperatura ambiente da una sección menor de la
necesaria**, y **el criterio prudente es calcular a la temperatura máxima de servicio del
aislamiento.**

## 4. Cómo se calcula una línea, paso a paso

**El procedimiento completo, que es lo que el enunciado pide y lo que un examen puede pedir
enumerado:**

| Paso | Qué se hace |
|---|---|
| **1 · Potencia prevista** | **Sumar las cargas** y **aplicar los factores de simultaneidad y de utilización** que correspondan |
| **2 · Corriente de diseño** | **IB**, a partir de la potencia, la tensión y el factor de potencia |
| **3 · Sección por CALENTAMIENTO** | **Entrar en la tabla con el modo de instalación** y **aplicar los coeficientes de corrección** |
| **4 · Sección por CAÍDA DE TENSIÓN** | **Con la fórmula, la longitud real y el límite que corresponda** |
| **5 · Elegir la MAYOR de las dos** | Y **normalizarla a la sección comercial inmediatamente superior** |
| **6 · Comprobar el conductor de PROTECCIÓN** | **Su sección se deduce de la de fase**, según la tabla de la instrucción |
| **7 · Comprobar el cortocircuito** | **Que el cable soporta la energía que pasa hasta que la protección corta** |
| **8 · Elegir la PROTECCIÓN** | **Con IB ≤ In ≤ Iz**, su curva y su poder de corte |

**Los pasos 6 y 7 son los que más se saltan y los que un examen puede preguntar por eso:**

- **El conductor de protección no se elige «igual que la fase» por costumbre**: **hay una relación
  reglamentada que depende de la sección de fase**, y **para secciones grandes el de protección puede
  ser menor.**
- **La comprobación de cortocircuito es la que garantiza que el CABLE aguanta hasta que la protección
  actúa.** **Un cable protegido contra sobrecarga puede no estarlo contra un cortocircuito si el
  aparato tarda demasiado**, y **eso se comprueba comparando la energía que deja pasar la protección
  con la que el cable soporta.**

**Y el paso 1 merece una nota, porque es donde se decide todo lo demás**: **la potencia prevista no es
la suma aritmética de todo lo instalado.** **Se aplican dos factores distintos y hay que saber
separarlos:**

| Factor | Qué corrige |
|---|---|
| **De UTILIZACIÓN** | **Que un receptor no siempre trabaja a su potencia máxima** |
| **De SIMULTANEIDAD** | **Que no todos los receptores funcionan a la vez** |

**El temario no da valores de ninguno de los dos y lo declara**: **los que la reglamentación fija están
en las instrucciones técnicas de previsión de cargas y de derivaciones individuales**, y **los demás
son criterio de proyecto que hay que justificar.**

## 5. Los casos particulares que cambian el cálculo

**Tres situaciones en las que el cálculo general no vale y hay que saber reconocerlas:**

| Caso | Qué cambia |
|---|---|
| **MOTORES** | **La instrucción de receptores para motores obliga a dimensionar la línea de un solo motor para una corriente MAYOR que la nominal**, por la punta de arranque; y en un grupo de motores, para la suma con criterio propio |
| **Lámparas de DESCARGA** | **La instrucción obliga a calcular la carga por encima de la potencia nominal de las lámparas**, por el consumo de los equipos auxiliares |
| **Instalaciones con ARMÓNICOS** | **El neutro puede llevar más corriente que las fases**, y por eso la instrucción exige que su sección sea **como mínimo igual a la de las fases** en instalaciones interiores, salvo justificación por cálculo |

**El tercero merece explicación, porque es contraintuitivo y es lo más moderno del punto**: **en un
sistema trifásico equilibrado con cargas LINEALES, las tres corrientes se anulan en el neutro y por él
no circula casi nada.** **Con cargas NO LINEALES —fuentes conmutadas, alumbrado electrónico,
variadores— aparecen armónicos de orden tres y múltiplos, y esos NO se anulan: se SUMAN en el
neutro.** **De ahí que un neutro pueda ir más cargado que las fases**, y **de ahí la exigencia de la
instrucción.**

**Y el caso de una casa que emite es exactamente ése**: **una instalación llena de fuentes conmutadas
—equipos de vídeo, informática, alumbrado de plató electrónico— es una instalación con armónicos.**
**Dimensionar su neutro como si las cargas fueran resistivas es el error de proyecto más caro y menos
visible**, porque **el neutro no lleva protección en muchos esquemas y su sobrecalentamiento no
dispara nada.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **De la ITC-BT-19, apartado 2.2.2**, el párrafo de los límites generales de caída de tensión y el párrafo de las instalaciones industriales con transformador propio |

**El aviso de método sobre las citas de instrucción técnica es el del tema 3 y vale aquí**: **la lente
de exactitud ancla en «Artículo N» y una instrucción numera por apartados**, así que **estas citas se
comprueban con la lente de citas de bloque.**

**Cinco declaraciones expresas:**

1. **Este tema NO reproduce ninguna tabla de intensidades máximas admisibles, ningún coeficiente de
   corrección por temperatura o agrupamiento, ninguna conductividad, ningún factor de simultaneidad y
   ninguna relación de sección del conductor de protección.** **Están en las tablas de las
   instrucciones técnicas y en las normas que éstas invocan**, y **una cifra que no se ha leído en su
   fuente no se escribe.** **El temario dice qué contiene cada tabla, dónde está y en qué sentido
   influye cada variable.**
2. **Los ÚNICOS valores numéricos de este tema son los cinco porcentajes de caída de tensión que las
   dos citas contienen** —3, 3, 5, 4,5 y 6,5—, **y están citados literalmente.**
3. **Las fórmulas de caída de tensión y de sección son física elemental y así se declaran.** **El
   reglamento no las contiene**, y **el temario no se las atribuye.** **El 2 del monofásico y la raíz
   de tres del trifásico se explican por lo que son: el camino de ida y vuelta y la composición
   vectorial.**
4. **Los apartados que se resumen y no se citan van identificados uno a uno** —de la ITC-BT-19, el
   2.2.1, el 2.2.3 y el 2.2.2 en su párrafo del conductor neutro—. **Están en la norma citada
   arriba.**
5. **Las instrucciones que se nombran por lo que regulan y NO se citan** son **la ITC-BT-10**, de
   previsión de cargas, **la ITC-BT-15**, de derivaciones individuales, **la ITC-BT-44**, de
   receptores de alumbrado, y **la ITC-BT-47**, de receptores motores. **De ellas sólo se dice qué
   materia contienen**, y **no se les atribuye ninguna cifra.**

**El resto del tema va como oficio y así se declara**: la regla de calcular por dos criterios y quedarse
con la mayor sección, la lectura de que la longitud no influye en el calentamiento y sí en la caída, la
separación de las dos desigualdades de la condición de protección, el aviso de que la intensidad
admisible es del cable en su instalación y no del cable, la lista de consecuencias de una caída
excesiva, la lectura de que los porcentajes industriales suben porque el origen se mueve, la
explicación del 2 y de la raíz de tres, las cuatro lecturas directas de las fórmulas, el aviso sobre
la conductividad a temperatura de servicio, el procedimiento de ocho pasos, la advertencia sobre los
dos pasos que más se saltan, la separación entre factor de utilización y de simultaneidad, la
explicación de los armónicos de orden tres que se suman en el neutro y la lectura del caso de una casa
que emite. **Nada de eso lo dice la norma con esas palabras**, y el tema no lo presenta como si lo
dijera.
