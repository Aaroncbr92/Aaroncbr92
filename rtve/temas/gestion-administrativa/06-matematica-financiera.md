# Tema 6 del específico de Gestión Administrativa · Matemática financiera básica

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 6 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | **Ninguna**: la matemática financiera no está en el BOE ni en una norma de un organismo de normalización |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: las fórmulas no tienen redacción vigente |
| **Aviso sobre las fuentes** | **Es el primer tema del proyecto sin fuente que citar, y no por falta de búsqueda**: aquí no se verifica, se demuestra. La garantía que sustituye a la cita es que **todas las operaciones del tema se han recalculado**, incluidas las cinco numéricas del examen, con la cuenta escrita al lado. **Una de ellas no cuadra con su respuesta oficial**: la plantilla da 2.400 € de capital final donde la multiplicación da **4.800 €** |
| **Extensión** | **2.413 palabras** |

<!-- /portada -->

**Las siglas y los símbolos de este tema, presentados de entrada**: el capital inicial (**C₀**), el
capital final o montante (**Cₙ**), el tipo de interés (**i**), el número de periodos (**n**), los
intereses (**I**), el valor actual neto (**VAN**) y el Boletín Oficial del Estado (**BOE**), que
aquí sólo aparece en la trazabilidad.

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 6):**
> «Matemática financiera básica. Capitalización simple y compuesta. Rentas constantes, variables y
> fraccionadas. Amortización de préstamos.»

<!-- indice -->

## Índice

- [Antes de empezar: aquí no se cita, se demuestra](#antes-de-empezar-aquí-no-se-cita-se-demuestra)
- [1. Capitalización simple](#1-capitalización-simple)
  - [1.1. Tres ejemplos, que son los del examen](#11-tres-ejemplos-que-son-los-del-examen)
  - [1.2. El rédito equivalente de un periodo fraccionado](#12-el-rédito-equivalente-de-un-periodo-fraccionado)
- [2. Capitalización compuesta](#2-capitalización-compuesta)
- [3. Las rentas](#3-las-rentas)
  - [3.1. Por la cuantía de los términos](#31-por-la-cuantía-de-los-términos)
  - [3.2. Por la frecuencia](#32-por-la-frecuencia)
  - [3.3. Por el momento del vencimiento y por la duración](#33-por-el-momento-del-vencimiento-y-por-la-duración)
- [4. Amortización de préstamos](#4-amortización-de-préstamos)
  - [4.1. Los sistemas](#41-los-sistemas)
  - [4.2. Cuadro de amortización](#42-cuadro-de-amortización)
- [5. Otras operaciones que el examen roza](#5-otras-operaciones-que-el-examen-roza)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
  - [6.1. La errata que se refuta con una multiplicación](#61-la-errata-que-se-refuta-con-una-multiplicación)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## Antes de empezar: aquí no se cita, se demuestra

**Es el primer tema del proyecto sin ninguna fuente que citar, y no por falta de búsqueda.** La
matemática financiera no está en el BOE ni en una norma de un organismo de normalización: **es
matemática**. Sus resultados no se verifican leyendo un artículo, **se comprueban rehaciendo la
operación**.

**Eso cambia el método de verificación, no su exigencia.** En los temas de norma, una respuesta se da
por buena cuando coincide con el precepto; aquí, cuando **la cuenta sale**. Y sale o no sale: no hay
lugar para la interpretación.

**Lo que este tema aporta como garantía es que todas las operaciones que aparecen en él —incluidas
las diez del examen— se han recalculado una a una.** Y una de ellas no cuadra con su respuesta
oficial. Está en el epígrafe 6.

---

## 1. Capitalización simple

**En capitalización simple los intereses no se acumulan al capital**: cada periodo genera intereses
sobre el mismo capital inicial, y esos intereses se retiran o se apartan.

**Las fórmulas**, con el tipo en tanto por uno y el tiempo en la misma unidad que el tipo:

- Intereses: **I = C₀ · i · n**
- Capital final: **Cₙ = C₀ · (1 + i · n)**
- Capital inicial despejado: **C₀ = Cₙ / (1 + i · n)**

**Dos observaciones que evitan la mayoría de los fallos:**

1. **El tiempo y el tipo tienen que ir en la misma unidad.** Un 6 % anual con un plazo de tres meses
   exige o bien pasar el plazo a años —3/12— o bien pasar el tipo a trimestral —6 %/4—. Mezclarlos es
   el error más común.
2. **«Capital final» no es «intereses».** El capital final incluye el capital inicial; los intereses,
   no. **Ésta es la distinción que el examen convierte en trampa**, y se explica en el epígrafe 6.

### 1.1. Tres ejemplos, que son los del examen

**Ejemplo A.** 5.000 € al 6 % simple anual durante 3 años.

> I = 5.000 · 0,06 · 3 = **900 €**
> C₃ = 5.000 + 900 = **5.900 €**

**Ejemplo B.** Un capital colocado 10 años al 20 % simple anual da un montante de 3.600 €. ¿Cuál era?

> C₀ = 3.600 / (1 + 0,20 · 10) = 3.600 / 3 = **1.200 €**
>
> Comprobación: 1.200 · 0,20 · 10 = 2.400 € de intereses; 1.200 + 2.400 = 3.600 €. Cuadra.

**Ejemplo C.** 2.400 € al 10 % simple anual durante 10 años.

> I = 2.400 · 0,10 · 10 = **2.400 €**
> C₁₀ = 2.400 · (1 + 0,10 · 10) = 2.400 · 2 = **4.800 €**

**Fíjese en lo que ocurre en el ejemplo C**: al 10 % durante 10 años, **los intereses simples igualan
exactamente al capital**. Quien calcule los intereses y se detenga ahí obtiene 2.400 €, que es el
capital de partida, y creerá haber terminado. **El capital final es el doble: 4.800 €.**

### 1.2. El rédito equivalente de un periodo fraccionado

Cuando el plazo es una fracción del año, el **rédito del periodo** es el tipo anual multiplicado por
la fracción. Para tres meses al 6 % anual:

> i(trimestral) = 0,06 · 3/12 = 0,06 / 4 = 0,015

Es decir, un 1,5 %. Y sobre 18.000 € da 18.000 · 0,015 = 270 € de intereses. Las dos cifras son
ciertas y responden a preguntas distintas: **el rédito es el tanto; los intereses son el importe**, y
un enunciado que pida «el rédito trimestral equivalente» pide el primero.

*(Los números de este ejemplo son cuenta propia, no cita: por eso van sin negrita. La regla del
proyecto es que la negrita promete literalidad.)*

---

## 2. Capitalización compuesta

**En capitalización compuesta los intereses se acumulan al capital y generan a su vez intereses.**
Ésa es la única diferencia con la simple, y es la que hace que el crecimiento sea exponencial en vez
de lineal.

- Capital final: **Cₙ = C₀ · (1 + i)ⁿ**
- Capital inicial: **C₀ = Cₙ / (1 + i)ⁿ**
- Intereses: **I = Cₙ − C₀ = C₀ · [(1 + i)ⁿ − 1]**

**Ejemplo, el del examen.** 100 € al 10 % durante 3 años, acumulando los intereses:

> C₃ = 100 · 1,10³ = 100 · 1,331 = **133,10 €**

**Y la comparación que conviene tener hecha**: los mismos 100 € en capitalización simple darían
100 · (1 + 0,10 · 3) = 130 €. La diferencia, 3,10 €, es el interés que los intereses han generado. Con tres años se nota poco; con veinte, la diferencia es de más del doble.

**Cómo distinguir cuál pide un enunciado.** Si dice «los intereses **se van acumulando**», «se
capitalizan», «interés compuesto» o «se reinvierten», es compuesta. Si dice «interés simple» o los
intereses «se retiran cada año», es simple. Cuando no dice nada, la convención es **simple para
plazos inferiores al año y compuesta para superiores**, pero el enunciado de un test suele decirlo.

---

## 3. Las rentas

Una **renta** es una sucesión de capitales que vencen en momentos sucesivos. Se clasifican por tres
criterios, y el examen pregunta por dos de ellos.

### 3.1. Por la cuantía de los términos

- **Renta constante**: **todos los términos son iguales** y vencen a **intervalos iguales**. Las dos
  condiciones a la vez: pagos iguales **y** periodicidad regular.
- **Renta variable**: los términos cambian de un periodo a otro. Pueden variar **en progresión
  aritmética** —cada término suma una cantidad fija al anterior— o **en progresión geométrica** —cada
  uno multiplica al anterior por una razón—.

**Cuidado con una confusión de vocabulario que el examen aprovecha.** En el lenguaje de la inversión,
«renta fija» y «renta variable» designan **tipos de activo** —bonos frente a acciones—, y ahí
«variable» quiere decir *cuyo rendimiento depende del mercado*. En matemática financiera, **una renta
variable es simplemente una renta cuyos términos no son iguales**. Son dos conceptos distintos con
nombres parecidos, y el enunciado del examen usa el primero.

### 3.2. Por la frecuencia

- **Renta entera**: sus términos vencen con la misma periodicidad que se capitaliza.
- **Renta fraccionada**: sus términos vencen **más de una vez** en cada periodo de capitalización
  —mensualidades con capitalización anual, por ejemplo—.

### 3.3. Por el momento del vencimiento y por la duración

- **Pospagable** (vencimiento al final de cada periodo) o **prepagable** (al principio).
- **Temporal** (número finito de términos) o **perpetua**.
- **Inmediata**, **diferida** o **anticipada**, según dónde se sitúe la valoración.

---

## 4. Amortización de préstamos

**Amortizar un préstamo es devolver el capital prestado**, con sus intereses, mediante pagos
repartidos en el tiempo. **No es aumentar la deuda ni pagar sólo intereses**: es **reducir
progresivamente el capital pendiente hasta extinguirlo**.

En cada pago hay que distinguir **dos componentes**:

- La **cuota de interés**: el interés del periodo sobre el **capital vivo** al comienzo de ese
  periodo.
- La **cuota de amortización**: la parte que **reduce el capital pendiente**.

La suma de ambas es el **término amortizativo** o cuota total.

### 4.1. Los sistemas

**Sistema francés** (cuota total constante). El término amortizativo es el mismo todos los periodos.
Dentro de él, **la cuota de interés decrece y la de amortización crece**, porque el capital vivo baja.
Es el sistema de la inmensa mayoría de los préstamos hipotecarios.

**Sistema de cuota de amortización constante** (o lineal, o italiano). **Lo que se repite es la parte
que amortiza capital**, que vale siempre **C₀ / n**. Como el capital vivo decrece de forma uniforme,
**la cuota de interés decrece y la cuota total también**.

> **Ejemplo, el del examen.** Préstamo de 10.000 €, 5 años, cuotas de amortización constantes.
> Cuota de amortización de cualquier año, incluido el segundo:
> **10.000 / 5 = 2.000 €**
>
> El tipo de interés —el 10 % del enunciado— **no interviene en esta cifra**: interviene en la cuota
> de interés, que el año 2 sería el 10 % de los 8.000 € que quedan vivos, es decir 800 €. **La
> pregunta pide la cuota de amortización, no la de interés ni la total.**

**Sistema americano.** Durante toda la vida del préstamo **se pagan sólo los intereses**, y **el
capital se devuelve íntegro al final**, en un único pago. De ahí que a lo largo del préstamo el
capital vivo no baje: sólo baja de golpe, al vencimiento.

### 4.2. Cuadro de amortización

El cuadro recoge, periodo a periodo, cinco columnas: **término amortizativo, cuota de interés, cuota
de amortización, total amortizado y capital vivo**. Cierra bien cuando **el total amortizado del
último periodo iguala al capital prestado** y el capital vivo queda en cero.

---

## 5. Otras operaciones que el examen roza

**Operaciones simples y compuestas.** Son **simples** la capitalización simple, el descuento simple y
el descuento comercial. Son **compuestas** —porque en ellas los intereses se capitalizan— la
capitalización compuesta, **la constitución de capitales** y la amortización de préstamos.

**La constitución de un capital** es la operación inversa de la amortización: en vez de devolver un
capital recibido, **se van entregando términos periódicos para reunir un capital al final**, y esas
entregas generan intereses que se acumulan.

**El descuento** es anticipar el cobro de un capital futuro a cambio de una rebaja. En el **descuento
comercial** la rebaja se calcula sobre el **nominal**; en el **racional o matemático**, sobre el
**efectivo**. El primero da siempre un descuento mayor.

---

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Cuenta | Veredicto |
|---|---|---|---|
| 2 | 100 € al 10 % compuesto, 3 años | 100 · 1,10³ = 133,10 € | Correcta |
| 9 | Capital inicial: 10 años, 20 % simple, montante 3.600 € | 3.600 / 3 = 1.200 € | Correcta |
| 12 | Qué es una renta variable | Concepto | Correcta en el sentido financiero, no en el actuarial |
| 23 | 5.000 € al 6 % simple, 3 años | 5.000 · 1,18 = 5.900 € | Correcta |
| 37 | 2.400 € al 10 % simple, 10 años | 2.400 · 2 = 4.800 € | **La respuesta oficial da 2.400 €** |
| 38 | Qué es amortizar un préstamo | Concepto | Correcta |
| 43 | Cuota de amortización constante, año 2 | 10.000 / 5 = 2.000 € | Correcta |
| 47 | Qué pasa al final en el sistema americano | Concepto | Correcta |
| 69 | Cuál es una operación compuesta | Concepto | Correcta: constitución de capitales |
| 86 | Qué es una renta constante | Concepto | Correcta |

### 6.1. La errata que se refuta con una multiplicación

**La pregunta 37 pide el capital final de 2.400 € invertidos 10 años al 10 % de interés simple. Las
opciones son 2.400 €, 1.200 €, 600 € y 4.800 €. La plantilla da por buena la primera.**

**La cuenta es de una línea:**

> C₁₀ = C₀ · (1 + i · n) = 2.400 · (1 + 0,10 · 10) = 2.400 · 2 = **4.800 €**

**La respuesta correcta es la d).** La opción a) que la plantilla escoge, 2.400 €, es **el capital de
partida**: la única forma de llegar a ella es no capitalizar nada.

**Y aquí está lo que hace creíble el error.** Al 10 % durante 10 años, **los intereses simples valen
exactamente lo mismo que el capital**: 2.400 · 0,10 · 10 = 2.400 €. Quien calcula los intereses y da
esa cifra por respuesta **encuentra su resultado entre las opciones** y no sospecha. La coincidencia
numérica convierte un error de concepto en una respuesta aparentemente verificada.

Se aplicó el apartado 5 del manual —*el que detecta se equivoca*— y la sospecha se sostuvo:

1. **¿Está bien leído el enunciado?** Se volvió a leer **rasterizando la página del cuadernillo y
   pasándole reconocimiento óptico**, para no fiarse de la transcripción: dice «interés simple» y
   pide «el capital final que tendremos», con esas cuatro opciones.
2. **¿Podría «capital final» significar «intereses»?** No. El capital final es el montante; los
   intereses son la diferencia entre el montante y el capital inicial. Y si el enunciado hubiera
   querido los intereses, la respuesta seguiría siendo 2.400 €, pero **la pregunta no dice eso**.
3. **¿Sería compuesto en vez de simple?** El enunciado dice «en una operación de interés simple». Y
   aun en compuesto, 2.400 · 1,10¹⁰ = 6.224,68 €, que **no está entre las opciones**.
4. **¿Hay algún convenio que dé 2.400 €?** Ninguno: cualquier régimen de capitalización con tipo
   positivo produce un montante **mayor** que el capital inicial.

**El temario enseña los 4.800 €** y deja constancia de que la respuesta oficial es otra. **Es la
séptima errata de plantilla del proyecto y la primera que no necesita ninguna fuente para
refutarse**: basta con hacer la multiplicación.

---

## 7. Trazabilidad

**Este tema no tiene fuente que citar, y no es un descuido.** La matemática financiera no se publica
en un boletín oficial: se demuestra. Las fórmulas de capitalización simple y compuesta, la
clasificación de las rentas y los tres sistemas de amortización son **material común de la disciplina**,
no el contenido de una norma, y el tema los expone como tales.

**Lo que sí se ha hecho, y es la garantía que sustituye a la cita**: recalcular **todas** las
operaciones que aparecen en el tema, incluidas las cinco numéricas del examen. Los resultados
—133,10 €, 1.200 €, 5.900 €, 4.800 € y 2.000 €— se obtuvieron con la operación escrita al lado, de
modo que cualquiera puede rehacerlas.

- **Cuadernillo `23_preguntas_gea`**, preguntas 2, 9, 12, 23, 37, 38, 43, 47, 69 y 86, con su
  plantilla oficial. El enunciado de la pregunta 37 se releyó **sobre la imagen de la página**, no
  sobre la transcripción.
