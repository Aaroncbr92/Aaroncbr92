# Tema 30 del específico de Gestión · Excel avanzado

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión · punto 30 |
| **Sirve para** | **Gestión** |
| **Fuente** | Documentación de producto de Microsoft para **Excel 2019** (cuarto nivel de la jerarquía de fuentes) |
| **Identificador** | 9 páginas de `support.microsoft.com/es-es/office/…` |
| **Redacción que se estudia** | **Las páginas tal como estaban el 03/09/2026.** Microsoft publica documentación viva, no versiones fechadas |
| **Aviso sobre las fuentes** | **Ninguna pregunta cae aquí**, y es el más llamativo de los tres puntos sin preguntas: el temario de **Gestión Administrativa**, examinado el mismo año, **sí preguntó por ofimática** y bastante. El tema anota la única diferencia de versión que afecta a la materia: **las matrices dinámicas no existen en Excel 2019** |
| **Extensión** | **4.252 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: Visual Basic para Aplicaciones (**VBA**), el
procesamiento analítico en línea (**OLAP**, del inglés *online analytical processing*), el
coeficiente de determinación (**R²**) y el Boletín Oficial del Estado (**BOE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Gestión, punto 30):
> «Excel avanzado (versión Microsoft Excel 2019): Funciones y fórmulas avanzadas. Anidación de
> funciones. Tablas de datos. Tablas dinámicas: elementos de una tabla dinámica; campos calculados:
> segmentación de datos. Macros: Concepto, grabación y ejecución. Análisis de datos: estadística
> descriptiva; media móvil; regresión.»

*El enunciado fija una versión de producto: Excel 2019.* Eso hace de la documentación del
fabricante la fuente exigible, que es el *cuarto nivel* de la jerarquía del proyecto. Aquí se cita
la documentación de soporte de Microsoft, y con la misma advertencia que ya quedó escrita para el
temario de Gestión Administrativa: *son las páginas de hoy, no las de 2019*, porque Microsoft
publica documentación viva y no versiones fechadas. Se ha comprobado que las páginas usadas
declaran expresamente que se aplican a **Excel 2019**, y donde eso no pueda afirmarse, el tema lo
dirá.

<!-- indice -->

## Índice

- [1. Fórmulas y referencias](#1-fórmulas-y-referencias)
- [2. Funciones avanzadas](#2-funciones-avanzadas)
- [3. Anidación de funciones](#3-anidación-de-funciones)
- [4. Tablas de datos y análisis de hipótesis](#4-tablas-de-datos-y-análisis-de-hipótesis)
- [5. Tablas dinámicas](#5-tablas-dinámicas)
  - [5.1. Elementos de una tabla dinámica](#51-elementos-de-una-tabla-dinámica)
  - [5.2. Campos y elementos calculados](#52-campos-y-elementos-calculados)
  - [5.3. Segmentación de datos](#53-segmentación-de-datos)
- [6. Macros](#6-macros)
- [7. Análisis de datos](#7-análisis-de-datos)
  - [7.1. Estadística descriptiva](#71-estadística-descriptiva)
  - [7.2. Media móvil](#72-media-móvil)
  - [7.3. Regresión](#73-regresión)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Fórmulas y referencias

Una **fórmula** empieza siempre por el signo igual y puede combinar valores, referencias a celdas,
operadores y funciones. Una **función** es una fórmula predefinida con un nombre y unos argumentos.

Los *tipos de referencia*, que son el cimiento de todo lo demás porque determinan qué pasa al
copiar una fórmula:

| Referencia | Escritura | Al copiar la fórmula |
|---|---|---|
| **Relativa** | `A1` | Fila y columna *se ajustan* |
| **Absoluta** | `$A$1` | **No cambia** nada |
| *Mixta de columna* | `$A1` | La columna se fija, la fila se ajusta |
| *Mixta de fila* | `A$1` | La fila se fija, la columna se ajusta |

La tecla **F4** recorre los cuatro estados. *La referencia mixta es la que se domina tarde y la que
resuelve las tablas de doble entrada*: una tabla de multiplicar, o una tabla de cuotas por tipo y
plazo, se construye con una sola fórmula si se fijan la columna en un factor y la fila en el otro.

Otros elementos que conviene tener presentes: los **rangos** con dos puntos —`A1:B10`—, los
**nombres definidos** que dan un alias a un rango, las *referencias 3D* entre hojas
—`Hoja1:Hoja3!A1`— y las *referencias estructuradas* de tabla —`Tabla1[Importe]`—, que se ajustan
solas cuando la tabla crece.

Y los errores que Excel devuelve, porque leerlos ahorra tiempo: `#¡DIV/0!` división por cero,
`#¿NOMBRE?` nombre no reconocido, `#¡VALOR!` tipo de argumento incorrecto, `#¡REF!` referencia
destruida, `#N/A` valor no disponible —el típico de una búsqueda sin resultado—, `#¡NUM!` número no
válido y `#¡NULO!` intersección vacía de dos rangos.

---

## 2. Funciones avanzadas

Microsoft agrupa las funciones **por categoría**, y las que este punto exige pertenecen a cuatro
de ellas: **búsqueda y referencia**, **estadísticas**, **lógicas** y **financieras**.

**Búsqueda y referencia.** Son las que resuelven el problema de traer un dato de otra tabla:

- `BUSCARV`, que busca un valor **en la primera columna** de una tabla y devuelve un dato de la
  columna que se le indique. Su cuarto argumento decide todo: `FALSO` para coincidencia exacta,
  `VERDADERO` para aproximada. *La coincidencia aproximada exige que la primera columna esté
  ordenada* y es la causa habitual de resultados silenciosamente equivocados.
- `BUSCARH`, la misma operación por filas.
- `INDICE` y `COINCIDIR`, que combinadas hacen lo mismo que `BUSCARV` *sin la limitación de buscar
  sólo en la primera columna* y sin romperse si se insertan columnas. Es la pareja que usa quien ha
  sufrido lo bastante con `BUSCARV`.
- `DESREF`, `INDIRECTO`, `ELEGIR` y `TRANSPONER`.

*Una advertencia de nomenclatura*: la documentación de Microsoft en español no siempre llama
`BUSCARV` a esta función. La página consultada la titula **«Función CONSULTAV»** y menciona el
nombre `BUSCARV` en su cuerpo: son la misma función con dos denominaciones según la variante de
español de la interfaz. En un examen escrito en España lo esperable es `BUSCARV`.

**Lógicas**: `SI`, `Y`, `O`, `NO`, `SI.ERROR`, `SI.CONJUNTO`. La documentación describe `SI` con
precisión, y su ejemplo se lee solo: **«En este ejemplo, la fórmula de la celda D2 dice: SI(C2 = 1;
entonces devolver Sí; en caso contrario devolver No)»**, y añade que **«También se pueden anidar varias funciones SI para
realizar varias comparaciones.»**

*Estadísticas y de agregación condicional*: `SUMAR.SI`, `SUMAR.SI.CONJUNTO`, `CONTAR.SI`,
`CONTAR.SI.CONJUNTO`, `PROMEDIO.SI`, `PROMEDIO.SI.CONJUNTO`. La diferencia entre la forma simple y
la del conjunto es el número de criterios: *una sola condición frente a varias a la vez*. Y una
trampa de orden de argumentos que se paga cara: en `SUMAR.SI` el rango de suma va **al final**,
mientras que en `SUMAR.SI.CONJUNTO` va **al principio**.

**Financieras**, que enlazan con el punto 28: `PAGO` para la cuota de un préstamo, `VA` para el
valor actual, `VF` para el valor final, `TASA`, `NPER`, `VNA` para el valor actual neto y `TIR`
para la tasa interna de rentabilidad.

*De texto y fecha*, para preparar datos antes de analizarlos: `IZQUIERDA`, `DERECHA`, `EXTRAE`,
`HALLAR`, `ENCONTRAR`, `CONCATENAR`, `TEXTO`, `ESPACIOS`, `HOY`, `AHORA`, `SIFECHA`, `DIAS.LAB`.

Y las *fórmulas matriciales*, que operan sobre rangos enteros y que en Excel 2019 se introducen
con `Ctrl + Mayús + Intro` —de ahí el nombre coloquial de *fórmulas control-mayúsculas-entrar*—. *Las matrices dinámicas
que se propagan solas no existen en Excel 2019*: llegaron con Microsoft 365, y ésa es una de las
pocas diferencias de versión que conviene tener presente al estudiar con documentación viva.

---

## 3. Anidación de funciones

**Anidar** es usar una función como argumento de otra. La función interior se evalúa primero y su
resultado se convierte en argumento de la exterior. Los paréntesis se cierran de dentro hacia
fuera, y Excel los colorea por parejas para ayudar.

Los tres casos que hay que saber construir:

- *`SI` anidados*, para clasificar en más de dos categorías. Cada `SI` va en el argumento de «valor
  si falso» del anterior, y las condiciones deben escribirse en *orden excluyente*: si la primera
  ya captura un caso, los siguientes ya no lo ven.
- *`SI.ERROR` envolviendo una búsqueda*, para que un `#N/A` no ensucie la hoja:
  `SI.ERROR(BUSCARV(...); "No encontrado")`. Es la anidación más útil de todas.
- *`INDICE` con `COINCIDIR` dentro*, donde `COINCIDIR` devuelve la posición y `INDICE` el valor de
  esa posición.

Los límites de Excel 2019: *hasta 64 niveles* de anidación y *hasta 255 argumentos* por función.
Pero el límite práctico llega mucho antes: *una fórmula con más de tres o cuatro niveles ya no se
puede depurar*. La alternativa profesional es partirla en columnas auxiliares o usar nombres
definidos, que además documenta el cálculo.

Para depurar una anidación, dos herramientas: **F9** sobre un fragmento seleccionado de la barra de
fórmulas, que muestra el resultado parcial, y *Fórmulas › Evaluar fórmula*, que recorre el cálculo
paso a paso.

---

## 4. Tablas de datos y análisis de hipótesis

Cuidado con el nombre, porque Excel usa la palabra «tabla» para tres cosas distintas: la **tabla**
—un rango con formato y referencias estructuradas—, la **tabla dinámica** del epígrafe 5 y la
**tabla de datos** de este epígrafe, que es una herramienta de simulación.

La documentación la define así: **«Una tabla de datos es un rango de celdas en el que puede cambiar
los valores de algunas de las celdas y encontrar diferentes respuestas a un problema.»** Y sitúa la
herramienta en su familia: **«En Microsoft Excel, las tablas de datos forman parte de un conjunto de
comandos conocidos como herramientas de análisis de hipótesis. Al construir y analizar tablas de
datos, está realizando análisis de hipótesis.»**

Qué es el análisis de hipótesis: **«el proceso de cambiar valores en celdas para ver cómo afectan
esos cambios al resultado de fórmulas de la hoja de cálculo»**. La propia documentación da el
ejemplo que mejor lo explica: **«puede usar una tabla de datos para variar la tasa de interés y la
duración del período de un préstamo con el fin de evaluar los posibles importes de los pagos
mensuales»** —que es, exactamente, el cuadro de amortización del punto 28 explorado en dos
dimensiones—.

Las *tres herramientas de análisis de hipótesis* de Excel y la diferencia entre ellas:

| Herramienta | Qué hace | Cuántas variables |
|---|---|---|
| **Escenarios** | Guarda **conjuntos de valores** con nombre y permite alternarlos | Hasta 32 valores por escenario |
| *Buscar objetivo* | Va *hacia atrás*: se fija el resultado que se quiere y Excel calcula el valor de entrada que lo produce | **Una** |
| **Tabla de datos** | Calcula *muchos resultados a la vez* para una o dos entradas variables | **Una o dos** |

La **tabla de datos de una variable** coloca los valores de entrada en una columna o en una fila, y
la fórmula en la esquina; la de **dos variables** coloca una serie en la fila superior, otra en la
columna izquierda, y *la fórmula en la celda de la esquina*, donde se cruzan. Se genera con
*Datos › Análisis de hipótesis › Tabla de datos*, indicando la celda de entrada de fila y la de
columna.

Dos rasgos que se preguntan: la tabla de datos genera una *fórmula matricial `TABLA`* cuyos
resultados *no se pueden borrar ni editar por separado* —hay que eliminar el bloque entero—, y su
recálculo es costoso, por lo que puede desactivarse con la opción de cálculo *«Automático excepto
para tablas de datos»*.

---

## 5. Tablas dinámicas

La documentación la define en una frase que conviene retener entera: **«Una tabla dinámica es una
herramienta avanzada para calcular, resumir y analizar datos que le permite ver comparaciones,
patrones y tendencias en ellos.»**

Es la herramienta central del punto y la que más rendimiento da: *resume miles de filas en un
informe de unas pocas, sin escribir una sola fórmula y sin alterar los datos de origen*.

Sus requisitos de datos de origen, que explican la mitad de los problemas: la documentación advierte
que **«Los datos deben organizarse en columnas con una sola fila de encabezado»**. A eso se añaden
las reglas de oficio: sin filas ni columnas totalmente vacías, sin celdas combinadas, sin subtotales
intercalados y con un solo tipo de dato por columna. *Una tabla dinámica bien hecha empieza por
unos datos bien puestos.*

Se crea con **Insertar › Tabla dinámica**, y hay que decidir dónde colocarla: **«Seleccione Nueva
hoja de cálculo para colocar la tabla dinámica en una hoja de cálculo nueva o en una hoja de cálculo
existente»**.

### 5.1. Elementos de una tabla dinámica

La **lista de campos** tiene cuatro áreas, y saber qué hace cada una es todo el manejo de la
herramienta:

| Área | Qué contiene | Qué produce |
|---|---|---|
| **Filas** | Campos de agrupación | Una **fila** por cada valor distinto |
| **Columnas** | Campos de agrupación | Una **columna** por cada valor distinto |
| **Valores** | Campos que se resumen | Las **cifras** del informe |
| **Filtros** | Campos por los que se acota | Un desplegable que filtra **todo** el informe |

Más los elementos que aparecen en el propio informe: los **subtotales**, los **totales generales**,
el *diseño del informe* —compacto, esquema o tabular—, la **agrupación** de campos —por fechas en
meses, trimestres y años, o por intervalos numéricos— y el **gráfico dinámico** asociado.

**La función de resumen** del área de Valores se elige, y su valor por defecto depende del tipo de
dato. La documentación lo dice con precisión: **«Excel usa la función de resumen Suma para calcular
los campos de valores que contienen datos numéricos, y la función de resumen Contar para calcular
los campos de datos que contienen texto. Puede elegir otra función de resumen, como Promedio, Máx o
Mín, para analizar y personalizar sus datos.»**

Junto a las funciones de resumen están los **cálculos personalizados** —«% del total general», «% de
la fila», «diferencia respecto de», «total acumulado»—, que cambian **cómo se muestra** un valor sin
cambiar el dato.

Y una advertencia práctica: la tabla dinámica *no se actualiza sola* cuando cambian los datos de
origen. Hay que **actualizarla**, y si el origen ha crecido en filas, **cambiar el origen de datos**
o —mejor— haber construido la dinámica sobre una **tabla**, que crece sola.

### 5.2. Campos y elementos calculados

Cuando las funciones de resumen no bastan, la documentación abre la puerta a las fórmulas propias:
**«Si las funciones de resumen y los cálculos personalizados no proporcionan los resultados que
quiere, puede crear sus propias fórmulas en los campos y elementos calculados.»**

Son *dos cosas distintas*, y la diferencia es la parte del epígrafe que hay que llevar exacta:

| | **Campo calculado** | **Elemento calculado** |
|---|---|---|
| Qué añade | Un *campo nuevo* a la tabla dinámica | Un *elemento nuevo dentro de un campo* existente |
| Sobre qué opera | Sobre **la suma** de los datos subyacentes | Sobre **los registros individuales** |
| Ejemplo de la documentación | `=Ventas * 1,2` | `=Lácteos * 115 %` |

La documentación explica la diferencia con un ejemplo que no deja lugar a dudas: **«Las fórmulas
para los campos calculados operan sobre la suma de los datos subyacentes para cualquier campo de la
fórmula. Por ejemplo, la fórmula de campo calculado =Ventas * 1,2 multiplica por 1,2 la suma de las
ventas de cada tipo y la región, no multiplica cada venta individual por 1,2 y luego suma los
importes multiplicados.»** Frente a ello: **«Las fórmulas para los elementos calculados operan en
los registros individuales. Por ejemplo, la fórmula de elemento calculado =Lácteos * 115 %
multiplica cada venta individual de lácteos un 115 %, tras lo cual los importes multiplicados se
resumen conjuntamente en el área de valores.»**

*Con sumas y multiplicaciones por una constante el resultado coincide; con divisiones, promedios o
porcentajes, no.* Un campo calculado que divida ventas entre unidades divide *las sumas* —lo que
da el precio medio ponderado, que suele ser lo correcto—, y un elemento calculado dividiría registro
a registro y después sumaría los cocientes, que no significa nada. Ésa es la razón práctica de
distinguirlos.

Se crean en *Analizar tabla dinámica › Cálculos › Campos, elementos y conjuntos*. Y una limitación
que conviene saber: *los campos y elementos calculados no están disponibles cuando el origen es
OLAP*, porque allí los cálculos se definen en el propio cubo.

### 5.3. Segmentación de datos

La documentación la define por lo que hace: **«Las segmentaciones de datos proporcionan botones en
los que puede hacer clic para filtrar tablas o tablas dinámicas.»** Y añade la ventaja que la
distingue del filtro de siempre: **«Además del filtrado rápido, las segmentaciones también indican
el estado de filtrado actual, lo que facilita la comprensión de lo que se muestra exactamente en ese
momento.»**

Ahí está toda la diferencia con el área de **Filtros** del epígrafe 5.1: *un filtro desplegable
esconde lo que está filtrando; una segmentación lo enseña*. En un informe que va a leer otra
persona, eso deja de ser una comodidad y pasa a ser una garantía de que no se malinterpreta.

Su otra virtud es que *una misma segmentación puede gobernar varias tablas dinámicas a la vez*, si
comparten el origen: la documentación describe cómo **«Hacer que una segmentación de datos esté
disponible en otra tabla dinámica»**, seleccionando *«las casillas de verificación de las tablas
dinámicas en la que quiere que la segmentación de datos esté disponible»*. Es lo que convierte un
conjunto de tablas sueltas en un *cuadro de mando*: se pulsa un botón y se mueve todo el informe a
la vez.

La figura hermana es la **escala de tiempo**, una segmentación especializada en campos de fecha, con
niveles de año, trimestre, mes y día.

---

## 6. Macros

**Concepto.** La documentación de Microsoft lo define así: **«Si tiene tareas en Microsoft Excel que
repite repetidamente, puede grabar una macro para automatizar esas tareas. Una macro es una acción o
un conjunto de acciones que se puede ejecutar todas las veces que desee. Cuando se crea una macro,
se graban los clics del mouse y las pulsaciones de las teclas. Después de crear una macro, puede
modificarla para realizar cambios menores en su funcionamiento.»**

Tres cosas en esa definición: una macro es **una acción o un conjunto de acciones**, se **graba**
registrando clics y pulsaciones, y se puede **modificar** después.

**Antes de grabar.** Hay un paso previo que se olvida y bloquea todo lo demás: **«Las macros y las
herramientas de VBA se pueden encontrar en la pestaña Desarrollador, que está oculta de forma
predeterminada, por lo que el primer paso consiste en habilitarla.»**

**Grabación.** **«En el grupo Código de la pestaña Programador y seleccione Grabar macro.»** Y en el
cuadro de diálogo: **«Escriba un nombre para la macro en el cuadro Nombre de macro, escriba una
tecla de método abreviado en el cuadro de tecla de método abreviado y una descripción en el cuadro
Descripción. Seleccione Aceptar para iniciar la grabación.»** A partir de ahí, todo lo que se haga
queda registrado hasta que se detiene la grabación.

Dos decisiones del cuadro de diálogo que la documentación no destaca y que cambian el resultado:
*dónde se guarda la macro* —en este libro, en un libro nuevo o en el *Libro de macros personal*,
que la hace disponible en todos los libros— y si se graba con *referencias relativas o absolutas*,
que decide si la macro actúa siempre sobre las mismas celdas o sobre las que estén seleccionadas al
ejecutarla.

**Edición.** **«Al modificar una macro, puede aprender un poco acerca del lenguaje de programación
Visual Basic.»** Y el camino: **«Para editar una macro, en el grupo Código de la pestaña Programador,
seleccione Macros, seleccione el nombre de la macro y presione Editar. Esta acción hará que se
inicie el Editor de Visual Basic.»**

**Ejecución.** Cuatro vías: desde *Programador › Macros*, con la **tecla de método abreviado**
asignada al grabarla, desde un *botón o forma* de la hoja con la macro asignada, o desde un botón
añadido a la barra de herramientas de acceso rápido.

*Guardado y seguridad.* Un libro con macros *no se puede guardar en el formato `.xlsx`*: hay que
usar el formato *habilitado para macros, `.xlsm`*. Y al abrirlo, Excel muestra una advertencia de
seguridad que exige *habilitar el contenido*, porque una macro es código ejecutable y ésa es
precisamente la vía por la que se han distribuido históricamente los ataques por documento ofimático.

---

## 7. Análisis de datos

Las tres herramientas que el enunciado nombra están en el complemento **Herramientas para análisis**,
que *no viene activado*: se añade desde *Archivo › Opciones › Complementos › Complementos de
Excel* y aparece después en *Datos › Análisis de datos*.

### 7.1. Estadística descriptiva

**«La herramienta de análisis Estadística descriptiva genera un informe estadístico de una sola
variable para los datos del rango de entrada, y proporciona información sobre la tendencia central y
dispersión de los datos.»**

Dos cosas de esa definición: es **de una sola variable** —para dos, hay otras herramientas— y
devuelve a la vez *centralización y dispersión*, que son los dos bloques del punto 29. El informe
que produce incluye media, error típico, mediana, moda, desviación estándar, varianza de la muestra,
curtosis, coeficiente de asimetría, rango, mínimo, máximo, suma, cuenta y, si se pide, el nivel de
confianza para la media.

Conviene notar que la herramienta devuelve *«varianza de la muestra»*, es decir, la que divide por
*N − 1*: es la **cuasivarianza** del punto 29, no la varianza de la población. Quien necesite la
otra debe usar la función `VAR.P` en vez de fiarse del informe.

### 7.2. Media móvil

**«La herramienta de análisis Media móvil proyecta valores en el período de pronósticos, basándose
en el valor promedio de la variable calculada durante un número específico de períodos anteriores.»**

Y la razón de usarla, que la propia documentación explica: **«Una media móvil proporciona
información de tendencias que se vería enmascarada por una simple media de todos los datos
históricos. Utilice esta herramienta para pronosticar ventas, inventario u otras tendencias.»**

El parámetro que hay que decidir es el **intervalo**: **«N es el número de períodos anteriores que
se incluyen en la media móvil.»** Un intervalo pequeño sigue de cerca a los datos y conserva el
ruido; uno grande alisa más y reacciona más tarde a los cambios. *Elegir el intervalo es elegir
cuánto ruido se sacrifica a cambio de cuánto retraso*, y no hay un valor correcto: depende de la
serie.

### 7.3. Regresión

**«La herramienta de análisis Regresión efectúa el análisis de regresión lineal utilizando el método
de "mínimos cuadrados" para ajustar una línea a un conjunto de observaciones. Puede analizar la
forma en que los valores de una o más variables independientes afectan a una variable
dependiente.»**

Dos precisiones de esa frase: el método es el de **mínimos cuadrados**, y admite **una o más
variables independientes**, es decir, hace también *regresión múltiple*. La documentación añade el
detalle de implementación: por debajo, la herramienta se apoya en la función de hoja de cálculo
`LINEST`.

Su informe devuelve el *coeficiente de determinación R²* —qué proporción de la variabilidad de la
variable dependiente explica el modelo—, el R² ajustado, el error típico, la tabla de análisis de la
varianza y, para cada variable, su **coeficiente**, su error típico, su estadístico *t* y su valor
*p*.

Y la advertencia que ninguna herramienta da y que hay que llevar puesta: *una regresión mide
asociación, no causa*. Un R² alto no demuestra que una variable cause la otra; puede haber una
tercera que explique a las dos, o la relación puede ser casual.

---

## 8. Los datos que el examen ha preguntado

*Ninguna de las 81 preguntas del específico de Gestión de 2024 cayó en este punto.* Es uno de los
tres puntos del temario —con el 16 y el 23— que el examen no tocó.

Es, además, el más llamativo de los tres, porque *el temario de Gestión Administrativa, que se
examinó el mismo año, sí preguntó por ofimática*, y bastante: sus puntos 8 a 12 son todos de
producto —Windows 10, la red, Office 2019 y Teams— y sus preguntas cayeron. Que el temario de
Gestión incluya un punto entero de Excel avanzado y no se pregunte por él en una convocatoria *no
permite deducir que no se pregunte en la siguiente*: es materia del anexo y hay que llevarla.

Si hubiera que apostar por dónde caería, son cinco datos: la *diferencia entre campo calculado y
elemento calculado*, las *cuatro áreas* de la lista de campos, el hecho de que la *pestaña
Desarrollador esté oculta* por defecto, el formato **`.xlsm`** para libros con macros y que las
tres herramientas de análisis exijan *activar el complemento*.

---

## 9. Trazabilidad

Documentación de soporte de Microsoft, toda ella en `support.microsoft.com/es-es/office/…` y
descargada el 3 de septiembre de 2026:

- **Crear una tabla dinámica para analizar datos de una hoja de cálculo**, en
  `…a9a84538-bfe9-40a9-a8e9-f99134456576`. De ahí salen la definición de tabla dinámica, el
  requisito de la fila única de encabezado y las funciones de resumen por defecto.
- **Calcular valores en un informe de tabla dinámica**, en `…11f41417-da80-435c-a5c6-b0185e59da77`.
  De ahí sale la distinción entre campo y elemento calculado.
- **Usar segmentaciones para filtrar datos**, en `…249f966b-a9d5-4b0f-b31a-12651785d29d`.
- **Inicio rápido: Crear una macro**, en `…741130ca-080d-49f5-9471-1e5fb3d581a8`. De ahí
  salen la definición de macro y los pasos de grabación y edición.
- **Usar las herramientas para análisis para realizar análisis de datos complejos**, en
  `…6c67ccf0-f4a9-487c-8dec-bdb5a2cefab6`. De ahí salen las tres herramientas del epígrafe 7.
- **Calcular varios resultados con una tabla de datos**, en `…e95e2487-6ca6-4413-ad12-77542a5ea50b`.
- **Funciones de Excel por categoría**, en `…5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb`.
- **Función SI**, en `…69aed7c9-4e8a-4755-a9bc-aa8bbff73be2`.
- **Función CONSULTAV**, en `…0bbc8083-26fe-4963-8ab8-93a18ad188a1`.

*Las dos advertencias que ya quedaron escritas para la documentación de producto del temario de
Gestión Administrativa valen igual aquí*, y se repiten porque son las que delimitan lo que estas
fuentes pueden sostener:

*Primera: son las páginas de hoy, no las de 2019.* Microsoft publica documentación viva. A favor
de citarlas juega que la página de tablas dinámicas declara expresamente aplicarse a **«Excel 2019
Excel 2016»** junto a las versiones más recientes, y que lo que aquí se cita —qué es un campo
calculado, cómo se graba una macro, qué hace la herramienta de regresión— no ha cambiado entre 2019
y hoy.

*Segunda: donde la versión importa, el tema lo dice.* Se ha señalado expresamente el único punto
en que Excel 2019 se separa de las versiones actuales y afecta a la materia del enunciado: *las
matrices dinámicas no existen en 2019*, de modo que las fórmulas matriciales se introducen con
`Ctrl + Mayús + Intro`.

Va como conocimiento de producto no citado de estas páginas, y así se declara: los *tipos de
referencia* y la tecla `F4`; la lista de **errores** de Excel; el detalle de las **funciones** por
categoría más allá de la mera clasificación; el orden de argumentos de `SUMAR.SI` frente a
`SUMAR.SI.CONJUNTO`; los *límites de 64 niveles y 255 argumentos*; las tres herramientas de
análisis de hipótesis y sus diferencias; las opciones de *dónde guardar una macro* y de
*referencias relativas o absolutas* al grabarla; el formato **`.xlsm`**; y la ruta de activación
del complemento **Herramientas para análisis**.

Y el enlace con el resto del proyecto: las *medidas de centralización y dispersión* que la
herramienta de estadística descriptiva calcula son las del punto 29 —incluida la advertencia sobre
la *varianza de la muestra*—, y las **funciones financieras** `PAGO`, `VNA` y `TIR` calculan lo que
el punto 28 desarrolla a mano.
