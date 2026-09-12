# Tema 28 del específico de Gestión · Matemática financiera

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión · punto 28 |
| **Sirve para** | **Gestión** |
| **Fuente** | **Sin norma.** Matemática financiera |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **no hay norma que fechar** |
| **Aviso sobre las fuentes** | **Sus 4 respuestas oficiales son correctas y las cuatro se comprueban rehaciendo la operación**, que es lo que el tema hace. En este tema **ninguna cifra calculada va en negrita**: la negrita promete literalidad y una cuenta propia no la tiene. Los distractores del examen son magnitudes reales del enunciado, y una de ellas es el resultado **sin convertir la unidad** |
| **Extensión** | **3.499 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el valor actual neto (**VAN**), la tasa interna de
rentabilidad (**TIR**), la tasa anual equivalente (**TAE**) y el Boletín Oficial del Estado
(**BOE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Gestión, punto 28):
> «Matemática financiera. Capitalización simple y compuesta. Operaciones a corto plazo: Descuento
> simple comercial, descuento de efectos comerciales. Rentas constantes, variables y fraccionadas.
> Amortizaciones de préstamos y empréstitos.»

*Este punto no descansa en ninguna norma*: es matemática. Sus fórmulas no se citan de un boletín,
se demuestran; y sus resultados se comprueban rehaciendo la operación. Por esa razón, **en este
tema no hay una sola cifra en negrita que proceda de un cálculo propio**: la negrita se reserva
para los nombres de las magnitudes, y los números van en texto llano con la operación a la vista
para que el lector la repita.

<!-- indice -->

## Índice

- [1. Los conceptos de partida](#1-los-conceptos-de-partida)
- [2. Capitalización simple](#2-capitalización-simple)
- [3. Capitalización compuesta](#3-capitalización-compuesta)
- [4. Tantos equivalentes](#4-tantos-equivalentes)
- [5. Descuento simple comercial](#5-descuento-simple-comercial)
- [6. El descuento de efectos comerciales](#6-el-descuento-de-efectos-comerciales)
- [7. Las rentas](#7-las-rentas)
- [8. Amortización de préstamos](#8-amortización-de-préstamos)
- [9. Empréstitos](#9-empréstitos)
- [10. Criterios de selección de inversiones](#10-criterios-de-selección-de-inversiones)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. Los conceptos de partida

La matemática financiera se apoya en un único principio: **un euro hoy no vale lo mismo que un euro
dentro de un año**. De ahí salen todas las fórmulas.

El vocabulario, que hay que fijar antes de nada:

- **Capital inicial** *C₀*, o **principal**: la cantidad de partida.
- **Capital final** *Cₙ*, o **montante**: la cantidad al término de la operación.
- **Interés** *I*: la diferencia entre los dos, *I = Cₙ − C₀*. Es el precio del tiempo.
- **Tanto o tipo de interés** *i*: el interés por unidad de capital y de tiempo. **Se expresa en
  tanto por uno en las fórmulas**: un 6 % es 0,06.
- **Rédito** *r*: el interés total por unidad de capital de la operación entera, sin referirlo al
  tiempo. Es *r = I / C₀*.
- **Tiempo** *n*: la duración, **expresada en las mismas unidades que el tipo**. Ésta es la fuente
  del noventa por ciento de los errores: si el tipo es anual, *n* va en años; si es semestral, en
  semestres.
- **Capitalizar** es llevar un capital hacia el futuro; **descontar** o **actualizar**, traerlo
  hacia el presente. Son la misma operación en sentidos opuestos.

La distinción que ordena el resto del tema:

| | **Capitalización simple** | **Capitalización compuesta** |
|---|---|---|
| Qué pasa con los intereses | Se calculan siempre sobre el **capital inicial** y no se acumulan | Se **acumulan al capital** al final de cada periodo y generan a su vez intereses |
| Cómo crece el capital | De forma **lineal** | De forma **exponencial** |
| Dónde se usa | Operaciones a **corto plazo**, menos de un año | Operaciones a **largo plazo**, más de un año |

---

## 2. Capitalización simple

Los intereses de cada periodo se calculan sobre el capital inicial y **no se incorporan** a él.

- **Interés total**: *I = C₀ · i · n*
- **Capital final**: *Cₙ = C₀ · (1 + i · n)*

Los dos casos prácticos que se preguntan:

**Hallar el interés.** Un capital de 18.000 € al 6 % anual durante 3 meses. Tres meses son 3/12 de
año, es decir 0,25 años: *I = 18.000 · 0,06 · 0,25 = 270 €*.

**Hallar el tiempo.** ¿Cuánto tarda un capital en triplicarse al 2,5 % simple semestral? De
*Cₙ = C₀ · (1 + i · n)* con *Cₙ = 3 · C₀*, sale *3 = 1 + 0,025 · n*, luego *n = 2 / 0,025 = 80*.
Ochenta **semestres**, porque el tipo era semestral; y ochenta semestres son cuarenta años.

**Ahí está la trampa habitual**: la fórmula devuelve el tiempo en la unidad del tipo, y la respuesta
suele pedirse en otra. Quien resuelve bien y no convierte, marca la opción equivocada, que en el
examen estaba puesta a propósito.

---

## 3. Capitalización compuesta

Los intereses se acumulan al capital al final de cada periodo:

- **Capital final**: *Cₙ = C₀ · (1 + i)ⁿ*
- **Capital inicial**, despejando: *C₀ = Cₙ / (1 + i)ⁿ*
- **Interés total**: *I = C₀ · [(1 + i)ⁿ − 1]*
- **Tiempo**: *n = log(Cₙ / C₀) / log(1 + i)*
- **Tipo**: *i = (Cₙ / C₀)^(1/n) − 1*

Comparadas para un mismo capital, tipo y plazo:

- Para **n = 1**, simple y compuesta dan **exactamente lo mismo**: sólo hay un periodo y no ha
  habido ocasión de acumular.
- Para **n < 1** —fracciones de periodo—, la **simple da más**.
- Para **n > 1**, la **compuesta da más**, y la diferencia crece con el plazo.

---

## 4. Tantos equivalentes

Dos tipos referidos a periodos distintos son **equivalentes** si producen el mismo capital final
sobre el mismo capital inicial en el mismo tiempo. La regla cambia según el régimen, y confundirlas
es el segundo error clásico:

- **En capitalización simple**, los tantos equivalentes son **proporcionales**: el tanto de un
  periodo *k* veces menor es *i / k*. Un 6 % anual equivale a 3 % semestral, 1,5 % trimestral y
  0,5 % mensual.
- **En capitalización compuesta**, los tantos equivalentes **no** son proporcionales, sino que se
  obtienen con raíces: *i₍ₖ₎ = (1 + i)^(1/k) − 1*. Un 6 % anual equivale a 1,4674 % trimestral, no
  a 1,5 %.

De ahí la utilidad del **rédito** para operaciones a corto: el rédito trimestral de una operación
al 6 % anual simple es 0,06 / 4 = 0,015, y se expresa en tanto por uno, no en porcentaje. Es lo que
preguntó la pregunta 10, y sus distractores estaban construidos con el interés en euros —270— y con
el año comercial —360—, no con réditos.

Y el concepto que la normativa bancaria impone para comparar productos: la **tasa anual
equivalente**, que expresa en términos anuales y en régimen compuesto el coste o rendimiento
efectivo de una operación, incluyendo comisiones y la periodicidad real de los pagos. Dos productos
sólo son comparables por su tasa anual equivalente, nunca por su tipo nominal.

---

## 5. Descuento simple comercial

**Descontar** es anticipar el cobro de un capital futuro a cambio de una deducción. Es la operación
inversa a capitalizar y la propia de las operaciones a corto plazo.

Dos modalidades, y hay que distinguirlas:

| | **Descuento comercial** | **Descuento racional o matemático** |
|---|---|---|
| Sobre qué se calcula el descuento | Sobre el **nominal**, el valor futuro | Sobre el **efectivo**, el valor actual |
| Fórmula del descuento | *Dc = N · i · n* | *Dr = N · i · n / (1 + i · n)* |
| Cuál es mayor | **El comercial**, siempre | El racional |
| Quién lo usa | **La banca**, en el descuento de efectos | El cálculo teóricamente correcto |

Donde *N* es el **nominal** —la cantidad que figura en el efecto—, *i* el tipo de descuento y *n* el
tiempo que falta hasta el vencimiento, **expresado en la misma unidad que el tipo**: si el tipo es
anual, *n = días / 365*.

El **efectivo** *E* es lo que realmente se recibe: *E = N − Dc*, o lo que es lo mismo,
*E = N · (1 − i · n)*.

Que el descuento comercial se calcule sobre el nominal y no sobre el efectivo es lo que lo hace más
caro y lo que explica que sea el que usa la banca: **se cobra interés sobre una cantidad mayor que
la que se entrega**.

---

## 6. El descuento de efectos comerciales

Es la aplicación práctica del epígrafe anterior, y la operación que enlaza este punto con el 18.

Una empresa lleva al banco una letra o un pagaré que vence dentro de *n* tiempo y el banco le
adelanta su importe menos tres partidas:

1. **El descuento comercial** propiamente dicho: *Dc = N · i · n*.
2. **La comisión**, normalmente un porcentaje sobre el nominal —de ahí que se llame *comisión
   referida al nominal*—, con un mínimo por efecto.
3. **Los gastos** fijos de gestión: correo, timbre, gastos de devolución si los hay.

De donde el **efectivo** que la empresa recibe es *E = N − Dc − comisión − gastos*, y el **descuento
total** o **descuento bancario** es la suma de las deducciones:

> **Descuento bancario = (N · i · n) + comisión**

Ésa es la fórmula que preguntó la pregunta 82, con la comisión expresada como *Cs* y ya referida al
nominal. Las tres opciones falsas mezclaban los factores: una multiplicaba la comisión por el tipo y
el tiempo, otra dividía por el tiempo y la tercera restaba la comisión en vez de sumarla.

**El descuento no transmite el riesgo**: si el librado no paga al vencimiento, el banco carga a la
empresa el nominal más los gastos de devolución. Es la cláusula *salvo buen fin* del punto 18, y por
eso el Plan General de Contabilidad abre una cuenta de deuda —la (5208)— y no una de venta.

Y la magnitud que resume el coste real de la operación: el **coste efectivo**, que se obtiene
comparando lo que se recibe con lo que se devuelve y expresándolo en términos anuales. Siempre es
mayor que el tipo de descuento nominal, precisamente porque el descuento se calcula sobre el
nominal y las comisiones no devengan tiempo.

---

## 7. Las rentas

Una **renta** es una sucesión de capitales que vencen en momentos distintos. Sus elementos: los
**términos** —cada capital—, el **periodo** —el tiempo entre dos términos consecutivos—, la
**duración** y el **tanto de valoración**.

**Clasificación**, que es lo que el enunciado pide:

- **Por la cuantía de sus términos**: **constantes**, si todos son iguales; **variables**, si no.
  Entre las variables, las que tienen fórmula cerrada son las que varían en **progresión
  aritmética** —cada término suma una cantidad fija al anterior— y en **progresión geométrica**
  —cada término multiplica al anterior por una razón fija—.
- **Por el vencimiento dentro del periodo**: **pospagables**, si el término vence al final del
  periodo —es el caso normal—, y **prepagables**, si vence al principio. La relación entre ambas es
  directa: el valor de una renta prepagable es el de la pospagable **multiplicado por (1 + i)**.
- **Por su duración**: **temporales**, con un número finito de términos, y **perpetuas**, sin
  término final.
- **Por el momento de valoración**: **inmediatas**, **diferidas** —la valoración se hace antes de que
  empiece— y **anticipadas** —después de que haya terminado—.
- **Por la relación entre el periodo de la renta y el del tanto**: **enteras**, si coinciden;
  **fraccionadas**, si el periodo de la renta es menor que el del tanto —una renta mensual valorada
  con un tanto anual—.

Las **rentas fraccionadas**, que el enunciado destaca, se resuelven de la única manera correcta:
**convirtiendo el tanto al periodo de la renta con la equivalencia compuesta** del epígrafe 4, nunca
dividiéndolo. Un tanto anual del 6 % para una renta mensual no es 0,5 % mensual, sino
(1 + 0,06)^(1/12) − 1.

Las dos fórmulas de la renta constante, unitaria, pospagable, inmediata y temporal de *n* términos:

- **Valor actual**: *a = (1 − (1 + i)^(−n)) / i*
- **Valor final**: *s = ((1 + i)ⁿ − 1) / i*

Y la de la **renta perpetua** pospagable, que es la que más se usa en valoración: *a = 1 / i*. Para
una renta de término *c*, basta multiplicar: *a = c / i*.

---

## 8. Amortización de préstamos

**Amortizar** un préstamo es devolverlo. Cada cuota o **término amortizativo** se descompone
siempre en dos partes:

> **Cuota = intereses del periodo + cuota de amortización**

donde los **intereses** se calculan sobre el **capital vivo o pendiente** al inicio del periodo, y
la **cuota de amortización** es lo que efectivamente reduce la deuda. El **cuadro de amortización**
es la tabla que recoge, periodo a periodo, cuota, intereses, amortización y capital pendiente.

Los sistemas, que hay que saber distinguir por lo que hace cada uno:

| Sistema | Cómo es la cuota | Cómo son los intereses | Cómo es la amortización |
|---|---|---|---|
| **Francés** o de cuota constante | **Constante** durante toda la vida | **Decrecientes** | **Crecientes** |
| **Italiano** o de amortización constante | **Decreciente** | Decrecientes | **Constante** |
| **Americano** | Sólo intereses cada periodo y el capital **íntegro al final** | Constantes | Cero hasta el vencimiento |
| **Alemán** o de intereses anticipados | Los intereses se pagan **al principio** de cada periodo | — | Constante |
| **Con carencia** | Durante la carencia se pagan sólo intereses, o nada | — | Empieza después |

**El sistema francés es el de las hipotecas** y el que hay que tener más claro, porque su
comportamiento sorprende: **al principio casi toda la cuota son intereses y casi nada amortiza**, y
la proporción se invierte con el tiempo. La cuota se obtiene de la renta constante del epígrafe 7:
el capital prestado es el valor actual de las cuotas, luego *C = c · a*, y de ahí *c = C / a*.

En el **sistema americano** conviene notar que **el capital vivo no baja nunca** hasta el último
periodo, de modo que los intereses totales son los más altos de los cinco sistemas. Suele ir
acompañado de un **fondo de amortización** —un *sinking fund*— en el que el deudor va acumulando
para poder devolver el principal al vencimiento.

---

## 9. Empréstitos

Un **empréstito** es un préstamo **dividido en muchos títulos de igual valor nominal**, colocados
entre un gran número de prestamistas. Es la forma en que se endeudan el Estado y las grandes
empresas cuando ninguna entidad puede o quiere prestar la totalidad.

Su vocabulario propio:

- **Emisor**: quien pide el dinero y emite los títulos.
- **Obligacionista**: cada prestamista, titular de uno o varios títulos.
- **Valor nominal**: el importe sobre el que se calculan los intereses o **cupones**.
- **Valor de emisión**: lo que paga el suscriptor. **A la par** si coincide con el nominal, **bajo
  la par** o con **prima de emisión** si es menor, **sobre la par** si es mayor.
- **Valor de reembolso**: lo que se devuelve. Si supera al nominal, la diferencia es la **prima de
  reembolso**.
- **Cupón**: el interés periódico. Un título **cupón cero** no paga intereses periódicos y compensa
  con la diferencia entre emisión y reembolso.
- **Amortización por sorteo**: en cada periodo se sortea qué títulos se reembolsan, que es la forma
  clásica de amortizar un empréstito escalonadamente.

La diferencia esencial con el préstamo: en el préstamo hay **un solo acreedor** y el capital vivo es
un importe; en el empréstito hay **muchos**, y el capital vivo se cuenta en **número de títulos en
circulación**.

---

## 10. Criterios de selección de inversiones

Es la aplicación de todo lo anterior a la decisión de invertir.

**El valor actual neto.** Se descuentan todos los flujos de caja futuros que la inversión promete y
se les resta el desembolso inicial:

> **VAN = −A + Σ Qₜ / (1 + k)ᵗ**

donde *A* es el desembolso inicial, *Qₜ* el flujo neto de caja del año *t* y *k* la tasa de
descuento o coste de capital.

Su lectura es directa: **la inversión interesa si el VAN es positivo**, porque significa que el
valor actual de lo que se va a cobrar supera a lo que hay que poner. Si es cero, es indiferente; si
es negativo, se rechaza. Entre varias inversiones, se prefiere la de mayor VAN.

**Y en su enunciado está la respuesta de la pregunta 48**: el valor actual neto se obtiene
**restando el coste inicial de la inversión al valor presente de los flujos de efectivo**. Las tres
opciones falsas proponen sumarlo, multiplicarlo por la tasa o dividir por el valor presente:
ninguna de las tres da una magnitud con sentido financiero.

**La tasa interna de rentabilidad** es la tasa de descuento que hace el VAN igual a cero. Se
interpreta como el rendimiento propio del proyecto, y la regla es aceptar la inversión si la tasa
interna **supera al coste de capital**. Su ventaja es que se expresa en porcentaje y se compara
fácilmente; sus inconvenientes, que puede no existir o ser múltiple cuando los flujos cambian de
signo más de una vez, y que **puede ordenar mal** proyectos de tamaños muy distintos, donde el valor
actual neto ordena bien.

**El plazo de recuperación** o *payback* es el tiempo que tarda la inversión en devolver el
desembolso. Es intuitivo y muy usado, pero tiene dos defectos que hay que conocer: **ignora lo que
ocurre después** de recuperar el desembolso y, en su versión simple, **no descuenta los flujos**.

---

## 11. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Qué hay que saber | Oficial |
|---|---|---|---|
| 10 | Rédito trimestral equivalente al 6 % anual simple | Tantos equivalentes proporcionales en régimen simple | a) 0,015 ✔ |
| 48 | Cómo se calcula el VAN | Definición del valor actual neto | a) Restar el coste inicial al valor presente de los flujos ✔ |
| 82 | Fórmula del descuento comercial con comisión | Descuento bancario = nominal × tipo × tiempo + comisión | b) Dc = (N × i × n) + Cs ✔ |
| 99 | Años para triplicar un capital al 2,5 % simple semestral | Despejar *n* y convertir semestres en años | d) 40 años ✔ |

**Las cuatro respuestas oficiales son correctas**, y las cuatro se comprueban rehaciendo la
operación, que es lo que se ha hecho aquí:

- **Pregunta 10.** En régimen simple los tantos equivalentes son proporcionales, luego el rédito
  trimestral es 0,06 / 4 = 0,015. Los distractores son el interés en euros —18.000 · 0,06 · 0,25 =
  270, opción b)— y el 360 del año comercial, opción d). La opción c), 0,02, sería el rédito
  cuatrimestral. Es decir: **las cuatro opciones son magnitudes reales del enunciado**, y sólo una
  responde a lo preguntado, que era un rédito.
- **Pregunta 99.** De 3 = 1 + 0,025 · n sale n = 80 semestres, que son 40 años. La opción a), 80
  años, es exactamente el resultado **sin convertir la unidad**; la b), 24 años, y la c), 35, no
  corresponden a ningún paso del cálculo. Es la pregunta que castiga con más precisión el error de
  unidades.
- **Pregunta 82.** Conviene una precisión terminológica que la pregunta no hace: en sentido
  estricto, el **descuento comercial** es sólo *N · i · n*, y lo que resulta de sumarle la comisión
  es el **descuento bancario** o descuento total. El enunciado da entre sus datos la comisión de
  servicio, de modo que pregunta por el total; y de las cuatro opciones, la b) es la única que suma
  la comisión al descuento en lugar de multiplicarla o dividirla. **La respuesta oficial es la
  correcta**; lo que hay que retener es que las comisiones **se suman**, porque no dependen del
  tiempo.
- **Pregunta 48.** Es de definición pura y no requiere cálculo.

Y una observación sobre el conjunto: **de los cuatro apartados que el enunciado del punto enumera,
el examen preguntó por dos** —capitalización simple y descuento— y **añadió uno que el enunciado no
menciona**, el valor actual neto, que pertenece a la selección de inversiones. Ni las rentas ni la
amortización de préstamos y empréstitos cayeron, siendo la parte más extensa del punto.

---

## 12. Trazabilidad

**Este tema no cita ninguna norma, porque su materia no está en ninguna.** Es matemática financiera:
sus fórmulas no proceden de un boletín oficial sino de la definición de las operaciones, y se
comprueban rehaciendo el cálculo, no consultando una fuente.

Va como desarrollo propio, y así se declara:

- Todas las **fórmulas** del tema: capitalización simple y compuesta, tantos equivalentes, descuento
  comercial y racional, valor actual y final de las rentas, cuota del sistema francés, valor actual
  neto y tasa interna de rentabilidad.
- Los **cinco sistemas de amortización** con esos nombres —francés, italiano, americano, alemán y
  con carencia—, que son la denominación habitual en la literatura española y no una clasificación
  legal.
- El vocabulario de **empréstitos** y la **amortización por sorteo**.
- **Todos los cálculos numéricos del tema**, incluidos los de las preguntas 10, 82 y 99, que son
  aritmética propia y por eso van sin negrita, con la operación escrita para que el lector la
  repita.
- La precisión terminológica sobre **descuento comercial** frente a **descuento bancario** del
  epígrafe 11, que es doctrina y no una corrección a la plantilla: la respuesta oficial es la que
  hay que marcar.

Dos enlaces con partes del proyecto que sí tienen norma detrás: el **descuento de efectos** se
contabiliza con las cuentas (4311) y (5208) del Plan General de Contabilidad, tal como se desarrolla
en el punto 18; y la **tasa anual equivalente** está definida en la normativa del Banco de España
sobre transparencia bancaria, que no es materia de este temario y por eso aquí sólo se nombra.
