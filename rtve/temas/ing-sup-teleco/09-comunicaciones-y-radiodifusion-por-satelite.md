# Tema 9 del específico de Ingeniería Superior · Telecomunicación · Comunicaciones y radiodifusión por satélite

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 9 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son los estándares de difusión por satélite, **no consultados**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **El orden que hay que llevar** | **L, C, Ku, Ka**, de lo robusto y voluminoso a lo capaz y frágil. **A más frecuencia, más capacidad y más atenuación por lluvia** |
| **Extensión** | **2.207 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la órbita geoestacionaria (**GEO**), la
media (**MEO**) y la baja (**LEO**); la difusión de vídeo digital por satélite (**DVB-S** y **DVB-S2**,
con su extensión **DVB-S2X**); la modulación por desplazamiento de fase (**PSK**), en sus órdenes
(**QPSK**, **8PSK**, **16APSK** y **32APSK**); la corrección de errores hacia delante (**FEC**); la
potencia isótropa radiada equivalente (**PIRE**); la relación entre ganancia y temperatura de ruido
(**G/T**); la densidad de flujo de potencia (**PFD**); el gigahercio (**GHz**) y el megahercio
(**MHz**); el megabit por segundo (**Mbit/s**); la unidad móvil por satélite (**SNG**, *satellite news
gathering*); y el bloque de bajo ruido (**LNB**, *low noise block*).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 9):
> «Comunicaciones por satélite. Radiodifusión por satélite. Sistemas de televisión digital por
> satélite. Estándares DVB para la difusión por satélite. Tipos de servicios proporcionados.»

**Es el punto del enlace que sube y baja**, y **conviene decir de entrada por qué sigue existiendo
cuando hay fibra en casi todas partes**: **el satélite es el único medio que cubre un territorio entero
de una vez y el único que llega a donde no hay infraestructura.** **Un enlace terrestre cuesta lo que
cuesta el trayecto; un enlace por satélite cuesta lo mismo para uno que para un país entero.** **Ésa es
su economía y explica sus dos usos: la difusión y el enlace desde donde no hay nada.**

**Y la idea que ordena el punto**: **un satélite de comunicaciones es un REPETIDOR muy alto.** **Recibe
en una frecuencia, amplifica, cambia de frecuencia y retransmite.** **Todo lo demás —órbita, bandas,
huella, modulación— sale de que ese repetidor está a decenas de miles de kilómetros y no se puede
tocar.**

<!-- indice -->

## Índice

- [1. Las órbitas](#1-las-órbitas)
- [2. Las bandas](#2-las-bandas)
- [3. El enlace](#3-el-enlace)
- [4. La televisión por satélite](#4-la-televisión-por-satélite)
- [5. Los servicios](#5-los-servicios)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Las órbitas

| Órbita | Cómo se ve desde el suelo | Para qué |
|---|---|---|
| **GEOESTACIONARIA** | **FIJA en el cielo**: gira con la Tierra sobre el ecuador | **Difusión y enlaces fijos**: la antena se apunta y se olvida |
| **MEDIA** | Se mueve; hacen falta varios satélites | Navegación y algunas comunicaciones |
| **BAJA** | **Pasa deprisa**: hacen falta constelaciones y seguimiento | **Baja latencia**: datos y observación |

**Las tres consecuencias de la órbita geoestacionaria, que son las que hay que saber razonar:**

1. **La antena no se mueve.** **Es lo que hace posible una parabólica doméstica**, y **es toda la razón
   de que la difusión por satélite sea geoestacionaria.**
2. **La LATENCIA es alta y no se puede bajar.** **La señal recorre dos veces la distancia hasta la
   órbita**, y **eso impone un retardo que ninguna tecnología reduce**: **es física, no ingeniería.**
   **Por eso una conexión en directo por satélite tiene esa pausa característica**, y **por eso los
   enlaces de baja órbita interesan para datos interactivos.**
3. **Una posición orbital es un RECURSO ESCASO.** **Los satélites geoestacionarios comparten un solo
   anillo**, y **su separación angular y su reparto de frecuencias están coordinados
   internacionalmente.**

## 2. Las bandas

**La escalera de bandas de satélite, ordenada de menor a mayor frecuencia**, que es como se pregunta:

| Banda | Rasgo | Uso característico |
|---|---|---|
| **L** | **La más baja de las cuatro**: poca atenuación por lluvia, poca capacidad | **Móvil, navegación, radio por satélite** |
| **C** | Robusta frente a la lluvia; **antenas grandes** | **Contribución y difusión en zonas de lluvia intensa** |
| **Ku** | **El compromiso**: antenas pequeñas y buena capacidad | **Difusión doméstica y unidades móviles** |
| **Ka** | **La MÁS ALTA de las cuatro**: mucha capacidad, antenas muy pequeñas | **Banda ancha por satélite y servicios de mucha capacidad** |

**La regla que resuelve la pregunta y que hay que llevar aprendida**: **de esas cuatro, la de mayor
frecuencia es la Ka.** **El orden es L, C, Ku, Ka**, y **la manera de no olvidarlo es que va de lo
robusto y voluminoso a lo capaz y frágil.**

**Y el intercambio que ese orden esconde, que es la lectura de oficio**: **a más frecuencia, más
capacidad y antenas más pequeñas, pero MÁS ATENUACIÓN POR LLUVIA.** **Una banda alta se corta en un
chaparrón donde una baja aguanta**, y **por eso los enlaces de contribución críticos han preferido
históricamente bandas bajas**, y **por eso los sistemas modernos llevan control de potencia y
modulación adaptativa para pelear la lluvia.**

## 3. El enlace

**Las dos mitades y por qué no son simétricas:**

| Mitad | De dónde a dónde | Qué la caracteriza |
|---|---|---|
| **ASCENDENTE** | **De la estación terrena al satélite** | **Potencia y antena grandes**, que están en tierra y se pueden pagar |
| **DESCENDENTE** | **Del satélite al receptor** | **Potencia limitada**: la del satélite, que es lo escaso |

**Y de ahí sale la asimetría de todo el sistema**: **el eslabón débil es siempre la bajada**, porque
**la potencia a bordo es limitada y el receptor doméstico es pequeño y barato.** **Todo el diseño de la
difusión por satélite consiste en gastar bien esa potencia.**

**Los parámetros del balance de enlace, que hay que saber nombrar y decir qué miden:**

| Parámetro | Qué mide |
|---|---|
| **Potencia isótropa radiada equivalente** | **Lo que el transmisor entrega al espacio en la dirección buena** |
| **Pérdidas de espacio libre** | **Lo que se pierde sólo por la distancia**: crecen con la frecuencia |
| **Atenuación atmosférica y por lluvia** | **Lo que absorbe el camino**, y es lo que varía |
| **Relación entre ganancia y temperatura de ruido** | **La calidad del receptor**: cuánta ganancia tiene por cada grado de ruido |
| **Margen de enlace** | **Lo que sobra sobre el mínimo**: es lo que se come la lluvia |

**Y la regla de proyecto**: **un enlace se dimensiona para el peor caso admitido, no para el día
bueno.** **La disponibilidad se expresa como el porcentaje del tiempo en que el servicio se mantiene**,
y **subirla un escalón cuesta mucho margen.**

**La HUELLA o cobertura**, que es lo que un satélite dibuja en el suelo: **el mapa de niveles de señal
que produce cada haz.** **Un haz ancho cubre mucho con poca potencia por metro cuadrado; un haz
estrecho concentra**, y **los satélites modernos usan muchísimos haces estrechos** para reutilizar
frecuencias y multiplicar la capacidad, **igual que una red móvil reutiliza canales entre celdas.**

## 4. La televisión por satélite

**La estación transmisora, con sus piezas:**

| Pieza | Qué hace |
|---|---|
| **Codificadores y multiplexor** | **Forman el flujo de transporte**: tema 6 |
| **MODULADOR** | **Modula en fase, con la corrección de errores del sistema** |
| **Conversor elevador y amplificador de alta potencia** | **Sube a la banda de subida y da potencia** |
| **ANTENA de la estación terrena** | **Parabólica grande, muy directiva** |

**La recepción doméstica:**

| Pieza | Qué hace |
|---|---|
| **PARABÓLICA** | **Concentra la energía en el foco** |
| **BLOQUE DE BAJO RUIDO** | **Amplifica con muy poco ruido propio y BAJA la frecuencia** a una banda intermedia |
| **Cable y repartidores** | **Llevan esa banda intermedia hasta el receptor** |
| **Receptor** | **Sintoniza, demodula y descodifica** |

**Y las dos cosas que hay que saber decir del bloque de bajo ruido, porque es la pieza clave**: **baja
la frecuencia ANTES de meter la señal en el cable**, porque **una banda de gigahercios no viaja por un
coaxial doméstico**; y **su RUIDO PROPIO manda sobre todo lo demás**, porque **está en el primer
eslabón de la cadena**, y **el ruido que introduce el primer amplificador se amplifica con la señal en
todos los siguientes.**

**Los estándares de difusión por satélite**, con la procedencia declarada: **el enunciado los nombra
por su familia** —los estándares de difusión de vídeo digital para satélite— **y este proyecto no ha
consultado ninguno**, así que **el temario dice lo que la familia hace y cómo evoluciona, sin
atribuirle ninguna cifra ni ningún parámetro concreto:**

| Generación | Qué aporta |
|---|---|
| **La primera** | **Modulación de fase de orden bajo y corrección de errores clásica** |
| **La segunda** | **Constelaciones de orden más alto, corrección de errores mucho mejor y MODULACIÓN ADAPTATIVA** |
| **Su extensión** | **Aún más órdenes de modulación y afinado del reparto**, para exprimir el transpondedor |

**Y la idea que explica el salto entre la primera y la segunda, y que hay que saber enunciar**: **la
MODULACIÓN Y CODIFICACIÓN ADAPTATIVAS.** **En vez de emitir siempre con el ajuste que aguanta el peor
receptor, el sistema ajusta la robustez para cada destino según cómo esté su enlace.** **Eso convierte
el margen que antes se desperdiciaba en capacidad**, y **es lo que más rendimiento ha ganado en
satélite.**

## 5. Los servicios

**Qué se hace con un satélite en una casa que emite:**

| Servicio | Qué es |
|---|---|
| **DIFUSIÓN directa al hogar** | **La televisión por satélite**, con su acceso condicional |
| **DISTRIBUCIÓN a cabeceras** | **Llevar el múltiplex a los operadores de cable y a los centros emisores**: es distribución primaria |
| **CONTRIBUCIÓN ocasional** | **Enlace desde el lugar de la noticia**, con unidad móvil por satélite |
| **Contribución permanente** | **Un canal alquilado de forma continua** entre dos sedes |
| **Datos y banda ancha** | **Acceso a red donde no llega la fibra** |
| **Recogida de material** | **Recepción de agencias e intercambios internacionales** |

**Y las dos observaciones que un ingeniero de esta casa tiene que llevar hechas:**

1. **La contribución ocasional se contrata por tiempo y por capacidad.** **Un enlace por satélite para
   un directo no se «enciende»: se reserva, se coordina con el operador del satélite y se alinea**, y
   **eso tiene un calendario que hay que meter en la planificación de la producción.**
2. **El satélite es la redundancia natural de la fibra, y al revés.** **Los dos medios fallan por
   causas independientes** —una excavadora frente a una tormenta—, **y por eso un enlace crítico se
   monta con uno de cada.** **Poner dos fibras por la misma zanja no es redundancia.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Las normas que este punto nombra no son legislación y no están en el Boletín Oficial del Estado** |

**El aviso de método sobre este punto es el del tema 3**, con **el mismo matiz del tema 8**: **el
enunciado nombra una familia de estándares y este proyecto no ha consultado ninguno.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna altura de órbita, ninguna latencia en milisegundos, ningún límite de
   banda en gigahercios, ninguna potencia, ninguna ganancia y ninguna disponibilidad en porcentaje.**
   **Son dato de recomendación y de operador**, y **una cifra que no se ha leído en su fuente no se
   escribe.** **Lo que el temario da es el ORDEN de las bandas y en qué sentido influye cada
   variable.**
2. **El orden de las cuatro bandas —L, C, Ku, Ka— es el que la plantilla oficial de esta ocupación
   confirma en su pregunta 92**, al señalar la Ka como la de mayor frecuencia. **El temario declara
   esa procedencia** y **no atribuye a ninguna norma los límites de cada banda**, que **no da.**
3. **Los estándares de difusión por satélite se describen por GENERACIONES y por lo que cada una
   aporta**, y **el temario no les atribuye ningún orden de modulación concreto, ninguna tasa de
   código ni ninguna eficiencia espectral.** **No se han consultado.**
4. **Este tema NO describe ningún satélite concreto, ninguna posición orbital, ningún operador y
   ninguna huella real.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la
   codificación y el multiplexado, al tema 6**; **la distribución primaria, al tema 7**; **las antenas
   y el balance de potencia, a los temas 17 y 23**; **y el acceso condicional, al tema 6.**

**El resto del tema va como oficio y así se declara**: la explicación de por qué el satélite sigue
existiendo y de su economía plana con la distancia, la idea de que un satélite es un repetidor muy alto
que no se puede tocar, las tres consecuencias de la órbita geoestacionaria con la advertencia de que la
latencia es física y no ingeniería, la regla mnemotécnica del orden de las bandas y el intercambio
entre capacidad y lluvia que esconde, la explicación de por qué el eslabón débil es siempre la bajada,
la regla de dimensionar para el peor caso admitido, la lectura de los haces estrechos como reutilización
de frecuencias, las dos cosas que hay que saber del bloque de bajo ruido, la explicación de la
modulación adaptativa como conversión de margen en capacidad, y las dos observaciones sobre la
contratación de un enlace ocasional y sobre el satélite como redundancia natural de la fibra. **Nada de
eso está en un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo
presenta como si lo estuviera.
