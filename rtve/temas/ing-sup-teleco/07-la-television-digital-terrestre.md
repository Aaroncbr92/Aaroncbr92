# Tema 7 del específico de Ingeniería Superior · Telecomunicación · La televisión digital terrestre

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 7 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son los estándares europeos de difusión terrestre, **no consultados**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Todo cuelga de una idea** | **El intervalo de guarda.** De él salen la inmunidad a los ecos, la red de frecuencia única, el dividendo digital y el efecto de acantilado |
| **Extensión** | **2.587 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la televisión digital terrestre (**TDT**);
la difusión de vídeo digital (**DVB**) en sus variantes terrestre (**DVB-T** y **DVB-T2**); la
multiplexación ortogonal por división en frecuencia (**OFDM**), en su variante codificada (**COFDM**);
la modulación en cuadratura (**QAM**) y por desplazamiento de fase en cuadratura (**QPSK**); la
corrección de errores hacia delante (**FEC**); el intervalo de guarda (**IG**); la red de frecuencia
única (**SFN**, *single frequency network*) y la de frecuencia múltiple (**MFN**); el megahercio
(**MHz**) y el gigahercio (**GHz**); el megabit por segundo (**Mbit/s**); la frecuencia muy alta
(**VHF**) y la ultraalta (**UHF**); el microsegundo (**µs**); y la potencia isótropa radiada
equivalente (**PIRE**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 7):
> «El servicio de televisión digital terrestre (TDT). Características, estándares, sistemas de
> transmisión y distribución primaria de televisión digital.»

**Es el punto de la difusión por ondas terrestres**, y **hay que decir de entrada qué lo separa del 6**:
**aquél estudia qué se emite —cómo se codifica y se multiplexa el contenido—; éste estudia CÓMO SE
RADIA ese múltiplex y cómo llega a la antena de una casa.**

**Y la idea que ordena el punto entero**: **la difusión terrestre trabaja en el peor canal que existe.**
**El satélite tiene línea de vista y el cable no tiene interferencias; el terrestre tiene edificios,
montañas, reflexiones, otros emisores y receptores baratos.** **Todo lo que este tema describe
—modulación de muchas portadoras, intervalo de guarda, corrección de errores, redes de frecuencia
única— existe para ganar esa pelea.**

<!-- indice -->

## Índice

- [1. La cadena de la difusión terrestre](#1-la-cadena-de-la-difusión-terrestre)
- [2. La codificación de canal](#2-la-codificación-de-canal)
- [3. La modulación de muchas portadoras](#3-la-modulación-de-muchas-portadoras)
- [4. Las redes de frecuencia única](#4-las-redes-de-frecuencia-única)
- [5. Las bandas y la planificación](#5-las-bandas-y-la-planificación)
- [6. La recepción](#6-la-recepción)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. La cadena de la difusión terrestre

**De la señal al televisor, con lo que hace cada eslabón:**

| Eslabón | Qué hace |
|---|---|
| **Codificación y multiplexado** | **Forma el flujo de transporte con varios programas**: es el tema 6 |
| **DISTRIBUCIÓN PRIMARIA** | **Lleva ese múltiplex desde el centro de producción hasta los centros emisores** |
| **CODIFICACIÓN DE CANAL** | **Añade redundancia y desordena los datos** para que el canal no los destruya |
| **MODULACIÓN** | **Reparte los datos entre miles de portadoras** |
| **AMPLIFICACIÓN y RADIACIÓN** | **Sube la potencia y la entrega al sistema radiante**: es el tema 23 |
| **RECEPCIÓN** | **Antena, sintonizador, demodulador y descodificador** en casa del espectador |

**Y la distinción que el enunciado nombra expresamente y que hay que fijar**:

| | **DISTRIBUCIÓN PRIMARIA** | **DIFUSIÓN** |
|---|---|---|
| **Qué transporta** | **El múltiplex ya formado**, desde donde se produce hasta donde se emite | **La señal radiada al espectador** |
| **Por qué medio** | **Fibra, radioenlace o satélite**, punto a punto o punto a multipunto | **Ondas terrestres** |
| **Quién la ve** | **Nadie**: es una red de transporte | **Todo el mundo** |
| **Qué prima** | **Fiabilidad y disponibilidad**: si cae, se cae la emisión de una región entera | **Cobertura** |

**La distribución primaria es la parte invisible y la que más se olvida en un examen**, y **conviene
decir qué la caracteriza**: **es una red de transporte con exigencia de disponibilidad muy alta y
normalmente redundante por caminos distintos**, porque **un fallo no afecta a un espectador: afecta a
todos los de una zona.**

## 2. La codificación de canal

**Lo que se le hace a los datos antes de modularlos**, y **hay que saber que son tres cosas distintas
con tres propósitos distintos:**

| Operación | Qué hace | Contra qué protege |
|---|---|---|
| **ALEATORIZACIÓN o dispersión de energía** | **Mezcla los datos con una secuencia conocida** | **Contra rachas de bits iguales**, que concentrarían energía en frecuencias sueltas |
| **CORRECCIÓN DE ERRORES hacia delante** | **Añade redundancia calculada** | **Contra el ruido**: el receptor arregla errores sin pedir repetición |
| **ENTRELAZADO** | **Desordena los datos en el tiempo y en la frecuencia** | **Contra los errores EN RÁFAGA** |

**El entrelazado merece explicación porque es el más contraintuitivo y el que más se pregunta**: **un
código corrector arregla bien errores dispersos y mal errores agrupados.** **El canal terrestre produce
errores agrupados** —un desvanecimiento, una interferencia de impulso—. **Lo que hace el entrelazado es
repartir los bits de cada bloque a lo largo del tiempo antes de emitirlos**, de modo que **una ráfaga
que destruye un tramo continuo de la emisión sólo estropea unos pocos bits de cada bloque**, y **cada
bloque puede arreglarse solo.** **El entrelazado no corrige nada: convierte errores que no se pueden
corregir en errores que sí.**

**Y el concepto de TASA DE CÓDIGO, que hay que saber leer**: **dice cuántos bits de cada bloque son de
información y cuántos de redundancia.** **Cuanta más redundancia, más robusta la emisión y menos
capacidad útil**, y **elegirla es la decisión de planificación del epígrafe 5.**

## 3. La modulación de muchas portadoras

**Es el corazón técnico del punto.** **En vez de una portadora rapidísima, MILES de portadoras lentas y
ortogonales entre sí**, cada una modulada en cuadratura de amplitud o por desplazamiento de fase.

**Las tres consecuencias, y las tres hay que saber razonarlas:**

1. **Cada símbolo dura muchísimo.** **Repartir la misma tasa entre miles de portadoras hace que el símbolo
   de cada una sea larguísimo comparado con los retardos del canal.**
2. **Eso permite el INTERVALO DE GUARDA.** **Antes de cada símbolo se emite una copia de su final**,
   y **el receptor descarta ese trozo.** **Cualquier eco que llegue dentro del intervalo de guarda cae
   en la parte descartada y NO produce interferencia entre símbolos.**
3. **Un desvanecimiento selectivo no mata la señal.** **Si el canal hunde una banda estrecha, sólo se
   pierden las portadoras de esa banda**, y **la corrección de errores reconstruye lo que llevaban.**

**Y de ahí sale la respuesta a la pregunta más contraintuitiva del punto, que hay que saber razonar**:
**si una antena recibe la señal directa MÁS un reflejo de un edificio cercano, la imagen se ve
NÍTIDA.**

**Por qué**, en tres pasos: **en analógico ese reflejo producía la doble imagen fantasma, porque la
señal llegaba dos veces desplazada y las dos se pintaban.** **En digital con intervalo de guarda, un
eco de un edificio cercano llega con un retardo pequeñísimo comparado con el intervalo**, así que **cae
dentro de la guarda y el receptor lo descarta**; **y no sólo no molesta: la energía del eco SUMA a la
de la señal directa**, porque el receptor las combina. **La doble imagen es un artefacto analógico**, y
**quien conteste eso está aplicando la intuición de la televisión anterior.**

**El límite de esa propiedad, que también hay que saber**: **un eco que llegue más tarde que el
intervalo de guarda sí interfiere**, y **entonces la señal se degrada bruscamente.** **La difusión
digital no se degrada poco a poco como la analógica: aguanta perfecta hasta un punto y ahí cae de
golpe.** **Es el efecto de acantilado**, y **es lo que hace que la planificación de coberturas sea más
exigente, no menos.**

## 4. Las redes de frecuencia única

**La consecuencia de planificación más importante del intervalo de guarda**, y **el concepto que
distingue la difusión digital de la analógica:**

| | **Red de frecuencia MÚLTIPLE** | **Red de frecuencia ÚNICA** |
|---|---|---|
| **Cómo es** | **Cada emisor de una zona usa un canal distinto** | **TODOS los emisores usan el MISMO canal** |
| **Por qué se podía o no** | **En analógico era obligatorio**: dos emisores en el mismo canal se destruyen | **En digital es posible**: un emisor vecino se comporta como un eco |
| **Qué exige** | Un canal por emisor y bandas de guarda | **Sincronización estrictísima**: misma frecuencia, mismo instante y mismo contenido |
| **Qué ahorra** | Nada | **ESPECTRO**: es lo que permitió el dividendo digital |
| **Qué complica** | La planificación de frecuencias | **La planificación de retardos**: hay que meter a todos los emisores dentro del intervalo de guarda del receptor |

**Y la frase que resume el epígrafe**: **en una red de frecuencia única, un emisor lejano no es una
interferencia: es un eco**, y **se trata como tal.** **Mientras llegue dentro del intervalo de guarda,
suma; si llega fuera, interfiere.** **Por eso el intervalo de guarda se elige por la DISTANCIA entre
emisores**, y **por eso una red de frecuencia única grande necesita guardas largas, que cuestan
capacidad.**

**El intercambio que hay que saber enunciar**: **capacidad, robustez y tamaño de red son tres cosas que
se reparten un presupuesto fijo.** **Más portadoras y guarda larga permiten una red mayor pero dejan
menos capacidad; una constelación de orden alto da más capacidad pero exige mejor relación señal a
ruido.** **No hay ajuste bueno en abstracto: hay el que corresponde a una cobertura y a un objetivo de
servicios.**

## 5. Las bandas y la planificación

**Dónde vive la televisión terrestre:**

| Banda | Qué es | Qué le pasa a la señal |
|---|---|---|
| **De frecuencias muy altas** | **De 30 a 300 megahercios** | **Alcance mayor y antenas grandes** |
| **De frecuencias ultraaltas** | **De 300 a 3.000 megahercios** | **La banda de la televisión terrestre**: antenas manejables y buena capacidad |

**Y la escalera de bandas completa, que un examen pregunta suelta y hay que llevar aprendida**: **cada
escalón multiplica por diez.** **De 3 a 30 megahercios, ondas decamétricas; de 30 a 300, muy altas; de
300 a 3.000, ultraaltas; de 3 a 30 gigahercios, superaltas; de 30 a 300, extremadamente altas.**
**Quien fije el punto de partida y el factor diez no necesita memorizar la tabla.**

**Los conceptos de planificación que hay que manejar**, sin cifras:

| Concepto | Qué es |
|---|---|
| **CANAL** | **La rejilla de frecuencias en que se reparte la banda**: el múltiplex ocupa un canal |
| **COBERTURA** | **El porcentaje de ubicaciones y de tiempo en que el servicio se recibe con calidad** |
| **RELACIÓN DE PROTECCIÓN** | **Cuánta señal deseada hace falta frente a una interferente** |
| **DIVIDENDO DIGITAL** | **El espectro que la difusión libera al pasar a digital**, reasignado a otros servicios |
| **POTENCIA RADIADA** | **Lo que sale al espacio**, materia del tema 23 |

**Y la observación de servicio que cierra el epígrafe**: **la televisión terrestre es el único medio de
difusión que llega a todo el mundo sin contrato, sin conexión y sin identificación.** **Ésa es la razón
de servicio público que sostiene la obligación de cobertura**, y **es lo que la diferencia del envío
bajo demanda por red, por bien que éste funcione.**

## 6. La recepción

**Lo que hay del otro lado y por qué falla:**

| Elemento | Qué hace | Qué falla |
|---|---|---|
| **ANTENA** | **Capta y da directividad** | **Mal orientada, degradada o de banda equivocada** |
| **Amplificador de mástil** | **Compensa las pérdidas de la instalación** | **Saturado por una señal fuerte**, produce intermodulación |
| **Red de distribución del edificio** | **Reparte a las tomas** | **Derivadores desadaptados, tomas mal terminadas** |
| **SINTONIZADOR y demodulador** | **Selecciona el canal y recupera los datos** | Sensibilidad y selectividad limitadas |
| **DESCODIFICADOR** | **Descomprime y presenta** | Formato no soportado |

**Y los tres síntomas que un técnico tiene que saber interpretar, porque son la parte práctica del
punto:**

1. **Imagen a bloques o congelada de golpe.** **Relación señal a ruido en el límite**: no es
   «poca señal» necesariamente, puede ser exceso e intermodulación.
2. **Un múltiplex se ve y otro no.** **Problema selectivo en frecuencia**: antena de banda equivocada,
   respuesta del amplificador o interferencia en un canal.
3. **Se ve bien y a ratos no.** **Interferencia intermitente o multitrayecto variable**: es lo que
   producen el tráfico, la vegetación con viento o un emisor que entra en propagación anómala.

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma con su identificador y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí**, con **un matiz que hay
que dar**: **el enunciado de este punto habla de «estándares», y los estándares de difusión digital son
normas europeas de un organismo de normalización, no del Boletín Oficial del Estado.** **Este proyecto
no las ha consultado**, y **por eso el temario no atribuye a ninguna de ellas ningún parámetro
concreto.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ningún número de portadoras, ninguna duración de símbolo, ningún valor de
   intervalo de guarda, ninguna tasa de código, ningún orden de constelación y ninguna capacidad de
   múltiplex.** **Son dato de la norma de difusión, que no se ha consultado**, y **una cifra que no se
   ha leído en su fuente no se escribe.** **Lo que el temario da es qué decide cada parámetro y en qué
   sentido.**
2. **Los límites de las bandas del epígrafe 5 se dan como la escalera de décadas del vocabulario
   radioeléctrico común** —de 30 a 300 megahercios, de 300 a 3.000, y así—, y **la plantilla oficial
   de esta ocupación confirma en su pregunta 33 el tramo de la banda de frecuencias muy altas.** **El
   temario declara esa procedencia** y **no atribuye la tabla a ninguna recomendación.**
3. **La respuesta sobre el reflejo del edificio se razona por el intervalo de guarda**, y **la
   plantilla oficial la confirma en la pregunta 12.** **El temario explica POR QUÉ**, que es lo que un
   opositor necesita, **y no se limita a dar la letra.**
4. **Este tema NO describe la planificación del espectro en España, ni el reparto de múltiplex, ni
   ninguna concesión.** **Eso es materia del marco regulatorio, que es el tema 1**, y **de la Ley
   13/2022 General de Comunicación Audiovisual**, **citada en el tema 7 del bloque general de este
   proyecto**, y **aquí se remite.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la
   codificación y el multiplexado del contenido, al tema 6**; **la modulación en general, al tema 3**;
   **las antenas, los transmisores y la potencia radiada, a los temas 17 y 23**; **y la difusión por
   satélite, al tema 9.**

**El resto del tema va como oficio y así se declara**: la separación entre este punto y el 6 —qué se
emite frente a cómo se radia—, la idea de que la difusión terrestre trabaja en el peor canal que
existe, la caracterización de la distribución primaria como red de transporte de disponibilidad muy
alta, la explicación del entrelazado como lo que convierte errores incorregibles en corregibles, las
tres consecuencias de la modulación de muchas portadoras, el razonamiento completo de por qué un
reflejo cercano no produce doble imagen en digital, la explicación del efecto de acantilado y de por
qué hace la planificación más exigente y no menos, la lectura de que en una red de frecuencia única un
emisor vecino es un eco, el intercambio entre capacidad, robustez y tamaño de red, la regla de la
escalera de décadas de las bandas, la observación de servicio público sobre la recepción sin contrato y
los tres síntomas de recepción con su interpretación. **Nada de eso está en un boletín oficial ni en
ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
