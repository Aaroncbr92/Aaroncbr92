# Tema 4 del específico de Ingeniería Superior · Telecomunicación · Medios de transmisión, conectores y compresión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 4 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los medios, los conectores y la compresión, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Cuatro preguntas con fotografía** | **El cuadernillo pide identificar conectores y paneles a partir de una imagen.** El temario declara cada una y da en su lugar **la regla de su familia**: no describe lo que no ha visto |
| **Extensión** | **3.033 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el par trenzado no apantallado (**UTP**) y
apantallado (**STP** y **FTP**); la fibra monomodo (**SM**, *single mode*) y multimodo (**MM**); el
decibelio por kilómetro (**dB/km**); el nanómetro (**nm**) y el micrómetro (**µm**); el gigabit por
segundo (**Gbit/s**); el conector de bayoneta (**BNC**) y su versión de alta densidad (**HD-BNC**); la
interfaz digital en serie (**SDI**) con sus grados **HD-SDI**, **3G-SDI**, **6G-SDI** y **12G-SDI**; la
interfaz multimedia de alta definición (**HDMI**); la interfaz visual digital (**DVI**); el puerto de
pantalla (**DP**, *DisplayPort*); el bus serie universal (**USB**); el conector de férula de 2,5
milímetros (**ST**), de encaje (**SC**) y compacto (**LC**), con sus pulidos plano (**PC**) y en
ángulo (**APC**); el módulo enchufable de factor de forma pequeño (**SFP**) y su versión cuádruple de
28 gigabits (**QSFP28**); y la relación de compresión (**CR**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 4):
> «Medios de Transmisión. Clasificación. Características. Aplicaciones. Compresión. Tipos.
> Equipamientos.»

**El enunciado junta dos cosas que no tienen nada que ver y hay que decirlo**: **los medios de
transmisión son física; la compresión es tratamiento de la señal.** **Lo único que las une es que las
dos deciden cuánta información cabe por un enlace.**

**Y la regla que ordena la primera mitad, dicha una vez**: **un medio de transmisión se elige por
CUATRO cosas y en este orden**: **el ancho de banda o régimen que tiene que llevar**, **la distancia**,
**el entorno electromagnético y mecánico** y **el coste de la instalación, no el del cable.** **Invertir
el orden es como se compra mal**, y **el cuarto factor es el que más se subestima: tirar un cable
cuesta mucho más que el cable.**

<!-- indice -->

## Índice

- [1. La clasificación de los medios](#1-la-clasificación-de-los-medios)
- [2. Los medios guiados, uno a uno](#2-los-medios-guiados-uno-a-uno)
- [3. Los conectores](#3-los-conectores)
- [4. Los sistemas de transmisión de señal en un centro](#4-los-sistemas-de-transmisión-de-señal-en-un-centro)
- [5. La compresión](#5-la-compresión)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. La clasificación de los medios

**Dos familias, y la frontera es si la energía va confinada o no:**

| Familia | Qué es | Ejemplos |
|---|---|---|
| **GUIADOS** | **La energía viaja confinada en un soporte físico** | **Par trenzado, coaxial, fibra óptica, guía de onda** |
| **NO GUIADOS** | **La energía se radia y se propaga por el espacio** | **Radioenlace, satélite, óptica en espacio libre** |

**Y el criterio que decide entre las dos, que es de oficio y no de física**: **el medio guiado se
controla y el no guiado se comparte.** **Un cable no se lo puede quitar nadie y su comportamiento no
cambia con el tiempo; un enlace radio depende del espectro, del clima y de quién más esté
transmitiendo.** **Por eso lo crítico va por cable siempre que se pueda**, y **lo no guiado se usa
donde el cable no llega o no se puede tender.**

## 2. Los medios guiados, uno a uno

**El PAR TRENZADO**, con lo que hay que saber:

| Rasgo | Qué es |
|---|---|
| **Por qué se trenza** | **Para que el ruido afecte igual a los dos hilos y se cancele** en el receptor diferencial |
| **Apantallamiento** | **Sin pantalla, con pantalla global o con pantalla por par**: se elige por el entorno |
| **Categorías** | **Cuanto más alta, más ancho de banda garantizado** |
| **Límite práctico** | **La distancia**: el enlace de red normalizado tiene un tope de longitud |
| **Dónde manda** | **Redes de datos y de control**, y **audio digital y analógico simétrico** |

**El COAXIAL**, que es el medio histórico de esta casa:

| Rasgo | Qué es |
|---|---|
| **Cómo es** | **Un conductor central, un dieléctrico, una malla y una cubierta** |
| **Por qué funciona** | **La malla es a la vez retorno y pantalla**: el campo queda dentro |
| **Su magnitud clave** | **La IMPEDANCIA característica**: 75 ohmios en vídeo y 50 en radiofrecuencia |
| **Su límite** | **La atenuación crece con la frecuencia**, así que **cuanto mayor es el régimen, más corto es el tramo** |
| **Dónde manda** | **Vídeo digital en serie, radiofrecuencia, distribución de sincronismos** |

**La consecuencia de la cuarta fila es la que ordena un centro de producción y hay que saber decirla**:
**el mismo cable coaxial que lleva una señal de definición estándar cientos de metros no lleva una de
doce gigabits ni la décima parte.** **Al subir de grado de interfaz, la longitud admisible se desploma**,
y **eso —no el precio del cable— es lo que empuja a la fibra y a la red.**

**La FIBRA ÓPTICA**, con la distinción que más se pregunta:

| | **MONOMODO** | **MULTIMODO** |
|---|---|---|
| **Núcleo** | **Muy fino** | **Bastante más grueso** |
| **Cómo viaja la luz** | **Un solo modo**: un solo camino | **Varios modos**: varios caminos a la vez |
| **Dispersión modal** | **No la tiene** | **La tiene**: los modos llegan desfasados y ensanchan el pulso |
| **ATENUACIÓN** | **Menor** | **Mayor** |
| **Distancia** | **Larga y muy larga** | **Corta**: dentro de un edificio o de un centro |
| **Fuente y coste del equipo** | **Láser**, más caro | **Diodo o láser de superficie**, más barato |

**Y la regla que resuelve la pregunta clásica**: **para larga distancia se usa MONOMODO, y la razón es
su MENOR ATENUACIÓN** —y la ausencia de dispersión modal—, **no que su recubrimiento sea más robusto
ni que lleve varias longitudes de onda.** **Llevar varias longitudes de onda a la vez es multiplexado
por división en longitud de onda, y se hace precisamente sobre monomodo**, así que **la opción que
atribuye eso al multimodo invierte los términos.**

**La GUÍA DE ONDA**, que se estudia en el tema 23 y aquí sólo se nombra: **conducto metálico hueco por
el que se propaga la onda a frecuencias muy altas**, **con pérdidas muy bajas y sin conductor central.**

## 3. Los conectores

**El enunciado dice «equipamientos», y en un centro de producción el equipamiento empieza por el
conector.** **La regla de oficio del epígrafe**: **un conector se elige por la señal, por la densidad
que hace falta y por si se va a manipular.**

| Conector | Para qué | Rasgo que lo define |
|---|---|---|
| **BNC** | **Vídeo digital en serie y radiofrecuencia** | **Bayoneta**: se conecta con un cuarto de vuelta |
| **HD-BNC** | **Lo mismo, en alta densidad** | **Más pequeño**: **en el mismo espacio caben más conectores** |
| **DIN 1.0/2.3** | Alta densidad en interior de equipo | Aún más pequeño |
| **Conector `XLR` de tres contactos** | **Audio analógico simétrico y audio digital** | **Con pestillo**, y con contacto de masa que entra primero |
| **Jack de 6,35 y 3,5** | Audio | Insertable en caliente |
| **RJ45** | **Red de datos** | Ocho contactos, con lengüeta |
| **Fibra: ST, SC, LC** | **Óptica** | **ST de bayoneta, SC de encaje, LC compacto**: el LC es el de alta densidad |
| **Multipolar tipo Harting** | **Instalaciones fijas y unidades móviles**: fuerza y señal en un solo cuerpo | **Carcasa rectangular con inserto de muchos contactos** |
| **Multipolar circular tipo Lemo** | **Cámaras y equipos de campo** | **Cuerpo circular, cierre de empuje y tracción, guiado por chavetero** |
| **HDMI, DVI y** ***DisplayPort*** | **Monitorado e informática** | **De consumo o de informática, no de emisión** |
| **USB en sus tipos A, B, C y mini** | **Datos y periféricos** | **El C es reversible; los demás no** |
| **Módulos enchufables `SFP` y `QSFP`** | **Alojan el transceptor óptico o eléctrico en el propio equipo** | **Enchufables en caliente**: se cambia el módulo, no el equipo |

**Las tres cosas que hay que saber decir de esta tabla, porque son las que un examen busca:**

1. **La ventaja del conector de alta densidad NO es eléctrica, es MECÁNICA.** **No es que sea
   específico de alta o de ultra alta definición, ni que lleve varias señales**: **es que ocupa menos
   y permite poner más conectores en el mismo panel.** **Las tres opciones falsas de esa pregunta
   atribuyen al tamaño una propiedad de la señal.**
2. **Un módulo enchufable no es un conector: es un TRANSCEPTOR.** **Lo que se elige con él es la
   óptica, la longitud de onda y el alcance**, y **el mismo equipo sirve para cobre o para fibra según
   el módulo que se le ponga.** **Su tasa binaria máxima es lo que lo clasifica**, y **la del módulo
   cuádruple de veintiocho gigabits es de cien gigabits por segundo**: cuatro carriles de veinticinco.
3. **En un pliego, el conector se especifica con el cable.** **Un conector para coaxial de setenta y
   cinco ohmios no es el mismo que para cincuenta aunque encaje**, y **un desajuste de impedancia
   produce reflexiones que un equipo de medida ve y un ojo no.**

**Y el aviso de método sobre las preguntas de este cuadernillo que muestran una fotografía**: **este
temario no describe lo que no ha visto.** **Cuatro de las preguntas de esta ocupación piden identificar
un conector, un panel o un esquema a partir de una imagen**, y **el temario declara cada una y aporta
en su lugar la REGLA DE SU FAMILIA**: **cómo se reconoce un conector de fibra por su cuerpo, un
multipolar por su carcasa y un conector de bus por su sección.** **Lo que no se hace es afirmar qué se
ve en una fotografía que no se ha mirado.**

## 4. Los sistemas de transmisión de señal en un centro

**La aplicación que el enunciado pide**, y **lo que un centro de producción usa de verdad:**

| Sistema | Qué lleva | Dónde |
|---|---|---|
| **Vídeo digital en serie por coaxial** | **Una señal por cable, sin comprimir** | **La instalación clásica** |
| **Fibra punto a punto** | **La misma señal, más lejos y sin ruido** | **Entre edificios, plató y control, exteriores** |
| **TRIAX** | **Señal, retorno, comunicaciones y ALIMENTACIÓN de la cámara por un solo cable** | **Cadenas de cámara** |
| **Fibra híbrida de cámara** | **Lo mismo que el triax, con fibras y conductores de fuerza en un cuerpo** | **Cadenas de cámara modernas** |
| **Red de paquetes** | **Muchas señales por el mismo enlace** | **Lo que desarrollan los temas 19 y 20** |
| **Enlace inalámbrico** | **Cámara sin cordón umbilical** | **Exteriores y estudios grandes** |

**Y las dos observaciones que hay que hacer, porque son las que explican por dónde va el oficio:**

1. **El triax y la fibra híbrida no son cables de señal: son cordones umbilicales.** **Llevan la señal
   en los dos sentidos, el retorno de imagen, las comunicaciones, el mando y la corriente**, y **por
   eso una cámara de estudio se conecta con UN cable y no con seis.**
2. **La red de paquetes cambia la topología, no sólo el cable.** **Con vídeo digital en serie una
   señal va de un punto a otro y para llevarla a tres sitios hace falta un distribuidor; con red,
   cualquier equipo puede suscribirse a cualquier flujo.** **Eso es lo que hace del tema 19 un cambio
   de arquitectura y no un cambio de medio.**

## 5. La compresión

**La segunda mitad del enunciado, y hay que empezar por lo que es y no es:** **comprimir es representar
la misma información con menos bits aprovechando lo que sobra.**

**Las dos familias, con la frontera que un examen persigue:**

| Familia | Qué hace | Qué se recupera |
|---|---|---|
| **SIN PÉRDIDA** | **Sólo quita redundancia estadística** | **EXACTAMENTE lo original, bit a bit** |
| **CON PÉRDIDA** | **Quita además lo que el ojo o el oído no aprecian** | **Algo parecido**, y **la degradación se acumula en cada recodificación** |

**Los tipos de redundancia que se aprovechan, que es como se clasifica de verdad:**

| Redundancia | Qué explota |
|---|---|
| **ESPACIAL o intracuadro** | **Que los píxeles vecinos se parecen**, dentro de una misma imagen |
| **TEMPORAL o intercuadro** | **Que un cuadro se parece al anterior** |
| **ESTADÍSTICA** | **Que unos símbolos son más frecuentes que otros**: codificación de longitud variable |
| **PSICOVISUAL y PSICOACÚSTICA** | **Que el sistema perceptivo no distingue todo lo que se le da** |

**Y la distinción que decide un flujo de trabajo y que un examen pregunta directamente**: **hay códecs
que comprimen SÓLO dentro del cuadro y códecs que comprimen ENTRE cuadros.**

| | **Intracuadro** | **Intercuadro o de grupo de imágenes** |
|---|---|---|
| **Qué comprime** | **Cada cuadro por separado** | **Un cuadro contra sus vecinos** |
| **Grupo de imágenes** | **NO TIENE**: cada cuadro es independiente | **Sí**, con cuadros de referencia y cuadros predichos |
| **Corte de montaje** | **En cualquier cuadro** | **Sólo limpio en los de referencia**; en los demás hay que recomponer |
| **Eficiencia** | **Menor** | **Mucho mayor a igual calidad** |
| **Dónde manda** | **Producción y postproducción** | **Contribución, distribución y emisión** |

**La regla de examen que sale de esa tabla, y es de las que se preguntan tal cual**: **una señal con
compresión intracuadro NO TIENE grupo de imágenes.** **No es que lo tenga de dos, de cuatro o de
ocho: es que el concepto no aplica**, porque **cada cuadro se codifica solo.**

**Y la regla de oficio que ordena el flujo de trabajo de una casa que emite**: **se comprime poco y
dentro del cuadro mientras el material se trabaja, y se comprime mucho y entre cuadros cuando el
material ya no se va a tocar.** **Cada recodificación degrada**, así que **el número de
recodificaciones de una cadena importa tanto como la calidad de cada una.**

**Y lo que decide la elección de un códec, en cinco preguntas:**

| Pregunta | Qué decide |
|---|---|
| **¿Se va a editar?** | **Intracuadro**, para poder cortar donde haga falta |
| **¿Se va a TRANSPORTAR por un enlace estrecho?** | **Intercuadro**, que es lo eficiente |
| **¿Cuántas veces se va a recodificar?** | **Cada vuelta cuesta calidad** |
| **¿Qué tiene que poder leerlo?** | **La compatibilidad manda sobre la eficiencia** |
| **¿Cuánta latencia se admite?** | **Un códec eficiente mira cuadros futuros y por tanto espera** |

**La última merece explicación porque es la que sorprende**: **la eficiencia se paga en RETARDO.**
**Un códec que predice un cuadro a partir del anterior y del siguiente necesita tener el siguiente**,
y **eso obliga a almacenar y a esperar.** **Por eso una comunicación en directo con vuelta —una
entrevista a distancia— usa códecs menos eficientes que una emisión en un sentido.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna categoría de par trenzado con su ancho de banda, ninguna longitud máxima
   de enlace, ninguna atenuación por kilómetro, ningún diámetro de núcleo de fibra y ninguna longitud
   de onda.** **Son dato de norma de cable y de fabricante**, y **una cifra que no se ha leído en su
   fuente no se escribe.** **Lo que el temario da es en qué sentido influye cada variable.**
2. **Las dos únicas cifras del epígrafe 2 —los setenta y cinco ohmios del coaxial de vídeo y los
   cincuenta del de radiofrecuencia— se dan como valores de uso común del oficio**, y **el temario no
   los atribuye a ninguna norma**, que **no se ha consultado.**
3. **Los cien gigabits por segundo del módulo cuádruple de veintiocho gigabits son la respuesta que la
   plantilla oficial de esta ocupación confirma en su pregunta 36**, y **el temario declara esa
   procedencia**: **no proceden de la especificación del módulo, que no se ha consultado.**
4. **CUATRO preguntas de este cuadernillo dependen de una IMAGEN** —la 15, un conversor; la 22, un
   panel de conexiones; la 68, un conector de fibra; y la 76, un conector de bus—, **y una quinta, la
   37, de un esquema.** **Este temario NO describe ninguna de esas imágenes**, porque **no las ha
   mirado.** **Lo que aporta es la regla de reconocimiento de cada familia**, y **el banco de este
   tema las deja marcadas.**
5. **Este tema NO nombra ningún códec comercial, ningún fabricante de cable y ningún modelo de
   conector por su referencia.** **Los tipos de conector se nombran por su designación de uso**, que
   es como se piden en un pliego.

**El resto del tema va como oficio y así se declara**: la observación de que el enunciado junta física
y tratamiento de señal, las cuatro cosas por las que se elige un medio y el aviso de que tender el
cable cuesta más que el cable, el criterio de que el medio guiado se controla y el no guiado se
comparte, la explicación de por qué se trenza un par, la lectura de que la longitud admisible de un
coaxial se desploma al subir de grado de interfaz, la regla de que el monomodo se usa por su menor
atenuación y la advertencia sobre la opción que invierte los términos, las tres cosas que hay que saber
de la tabla de conectores —con la advertencia de que la ventaja del alta densidad es mecánica y no
eléctrica—, la distinción entre conector y transceptor, la observación sobre la impedancia en un
pliego, la lectura del triax y la fibra híbrida como cordones umbilicales, la observación de que la red
cambia la topología y no sólo el cable, la regla de que una compresión intracuadro no tiene grupo de
imágenes, la regla de flujo de trabajo sobre cuándo comprimir poco y cuándo mucho, y las cinco
preguntas para elegir códec con la explicación de que la eficiencia se paga en retardo. **Nada de eso
está en un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo
presenta como si lo estuviera.
