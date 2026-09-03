# Esquema · Tema 14 del específico de Ingeniería Técnica · Telecomunicación · Antenas, transmisores y propagación

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de radiocomunicación · `[exam]`
= opciones del propio cuadernillo. **Siglas**: la modulación de amplitud (**AM**) y la de frecuencia
(**FM**); la onda corta (**OC**); la relación de onda estacionaria (**ROE**); el decibelio respecto a
un radiador isótropo (**dBi**) y respecto a un dipolo (**dBd**); la potencia radiada aparente
(**PRA**) y la isótropa equivalente (**PIRE**); la radiofrecuencia (**RF**); el gigahercio (**GHz**) y
el megahercio (**MHz**); las bandas de satélite por su letra (**banda C**, **banda Ku**, **banda
Ka**); y las clases de amplificador, también por letra (**clase A**, **clase B**, **clase AB**,
**clase C**, **clase D**).

**Cabecera.** Enunciado: punto 18 del anexo, **con diez asuntos** · **3 preguntas** · **reparto**: 1 de
bandas de satélite, 1 de clases de amplificador, 1 de un componente elemental · **de antenas, guías de
onda, onda corta y medida de distorsiones no ha caído ninguna** · **aviso**: **la pregunta 75 no encaja
en ningún punto del anexo** y se clasifica aquí por proximidad, declarándolo.

<!-- indice -->

## Índice

- [Las bandas de satélite](#las-bandas-de-satélite)
- [Las clases de amplificador](#las-clases-de-amplificador)
- [El componente de la pregunta 75](#el-componente-de-la-pregunta-75)
- [Antenas y ganancia](#antenas-y-ganancia)
- [Líneas y guías de onda](#líneas-y-guías-de-onda)
- [Los transmisores](#los-transmisores)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las bandas de satélite

| Banda | Ascendente | Descendente | Rasgo |
|---|---|---|---|
| **C** | **6 GHz** | **4 GHz** | **Poco afectada por la lluvia; antenas grandes** |
| **Ku** | **14 GHz** ✔ | **12 GHz** | **Antenas pequeñas; la lluvia atenúa** |
| **Ka** | **30 GHz** | **20 GHz** | **Antenas muy pequeñas; la lluvia atenúa mucho** |

- **PREGUNTA 68** · `[exam]` · **La banda Ku sube a 14 GHz y baja a 12 GHz.**
- **LAS DOS REGLAS QUE LA HACEN MEMORIZABLE** · `[of]` · **El ascendente es SIEMPRE mayor que el
  descendente**, porque **la estación terrena tiene potencia y espacio de sobra y el satélite no**: se
  le pone la frecuencia más difícil al extremo que puede permitírselo · **al subir de banda, las
  antenas se hacen pequeñas y la lluvia empieza a molestar.**
- **LA FALSA QUE DELATA** · `[exam]` · **2,5 y 2,2 gigahercios son de otros servicios**, no de
  comunicación por satélite fija.
- **EL FENÓMENO QUE DECIDE UN ENLACE** · `[of]` · **La atenuación por lluvia**: **despreciable en C,
  obliga a dejar margen en Ku, puede cortar en Ka.** **Una contribución seria va en Ku con margen
  sobrado, o en C donde la fiabilidad manda sobre el tamaño de antena.**

## Las clases de amplificador

- **EL CRITERIO QUE LAS DEFINE** · `[of]` · **Cuánta parte del ciclo de la señal conduce el elemento
  activo.**

| Clase | Cuánto conduce | Rendimiento | Distorsión | Dónde |
|---|---|---|---|---|
| **A** | **El ciclo entero** | **Bajo: 25-50 %** | **Mínima** | **Audio de precisión, pequeña señal** |
| **B** | **Medio ciclo** | **Medio: hasta 78 %** | **Cruce por cero** | **Salida en contrafase** |
| **AB** | **Algo más de medio** | **Entre las dos** | **Corrige el cruce** | **La mayoría del audio de potencia** |
| **C** | **Menos de medio ciclo** | **Alto: más del 80 %** ✔ | **Mucha: armónicos** ✔ | **Radiofrecuencia con portadora sintonizada** |
| **D** | **Conmuta: no es lineal** | **Muy alto: más del 90 %** | **La del filtrado de salida** | **Audio de potencia moderno y radiofrecuencia** |

- **PREGUNTA 73** · `[exam]` · **La clase C se caracteriza por alto rendimiento y gran generación de
  armónicos.**
- **SI DISTORSIONA TANTO, ¿PARA QUÉ SIRVE?** · `[of]` · **En radiofrecuencia la salida va a un circuito
  resonante sintonizado**: **ese circuito filtra los armónicos y devuelve una sinusoide limpia.** **La
  distorsión se genera y se elimina, y el rendimiento se queda.**
- **POR QUÉ NO SIRVE PARA AUDIO** · `[of]` · **Una señal de audio ocupa banda ancha y no se puede
  filtrar así.** **Eso hace falsa la opción de la «absoluta linealidad para amplificadores de
  estudio».**
- **LAS OTRAS DOS FALSAS** · `[exam]` · **El bajo rendimiento es de la clase A**, y **la temperatura
  elevada en ausencia de señal también**: **la clase A consume igual con señal y sin ella**; **la C en
  reposo no conduce y no calienta.**

## El componente de la pregunta 75

- **PREGUNTA 75** · `[exam]` · **Un reóstato es un resistor variable.**
- **LO QUE HAY QUE DECIR** · `[of]` · **Es electrónica elemental y no pertenece a ningún punto de este
  anexo.** **Se clasifica aquí por proximidad con instrumentos y componentes de radiofrecuencia**, y se
  declara en vez de inventarle un encaje.

| Componente | Qué es | Terminales |
|---|---|---|
| **Reóstato** | **Resistor variable para regular CORRIENTE** ✔ | **Dos** |
| **Potenciómetro** | **El mismo componente como divisor de TENSIÓN** | **Tres** |

- **LA DISTINCIÓN ÚTIL** · `[of]` · **Son físicamente el mismo elemento con dos conexiones distintas**:
  **la palabra dice cómo está conectado, no cómo está fabricado.** **Un reóstato de potencia se
  construye con hilo bobinado para disipar calor.**
- **LAS FALSAS SON COMPONENTES REALES** · `[exam]` · **Condensador variable, aparato de medida, control
  de temperatura.** **La palabra que decide es «resistor».**

## Antenas y ganancia

- **QUÉ ES LA GANANCIA, CON PRECISIÓN** · `[of]` · **Una antena NO amplifica: CONCENTRA.** **Manda hacia
  una dirección la potencia que un radiador ideal repartiría por igual en todas.**

| Referencia | Qué significa |
|---|---|
| **Decibelio respecto a radiador isótropo** | **Comparada con una fuente que radia igual en todas direcciones** |
| **Decibelio respecto a dipolo** | **Comparada con un dipolo de media onda** |

- **LA CONVERSIÓN QUE EL EXAMEN PUEDE PEDIR** · `[of]` · **La ganancia respecto al dipolo es 2,15
  decibelios menor que la respecto al radiador isótropo**, porque **el propio dipolo tiene esa
  ganancia.**

| Servicio | Antena típica |
|---|---|
| **Amplitud modulada** | **Mástil radiante: la torre es la antena** |
| **Frecuencia modulada** | **Dipolos o paneles apilados, hacia el horizonte** |
| **Televisión terrestre** | **Paneles o dipolos en cortina, sobre torre** |
| **Enlaces terrestres** | **Parabólicas pequeñas, muy directivas** |
| **Satélite** | **Parabólicas, alimentador en foco o desplazado** |

- **LOS CUATRO PARÁMETROS DE CUALQUIER ANTENA** · `[of]` · **Ganancia, diagrama de radiación e
  impedancia de entrada**, y **el que decide si se puede usar: el ancho de banda.**

## Líneas y guías de onda

| Medio | Hasta qué frecuencia | Rasgo |
|---|---|---|
| **Línea coaxial** | **Hasta unos pocos gigahercios** | **Flexible y fácil de tender; pierde con la frecuencia** |
| **Guía de onda** | **Por encima, en microondas** | **Rígida, con muy poca pérdida, voluminosa** |

- **POR QUÉ HAY QUE CAMBIAR DE MEDIO** · `[of]` · **Las pérdidas del coaxial crecen con la frecuencia**,
  sobre todo por el dieléctrico, **hasta que llevar la señal cuesta más de lo que vale.** **La guía no
  tiene dieléctrico ni conductor central: es un tubo por el que la onda se propaga.**

| Relación de onda estacionaria | Qué significa |
|---|---|
| **1 a 1** | **Adaptación perfecta: no vuelve nada** |
| **1,5 a 1** | **Aceptable en la mayoría de las instalaciones** |
| **2 a 1 o más** | **Hay un problema: conector, cable o antena** |

- **POR QUÉ IMPORTA EN UN TRANSMISOR DE POTENCIA** · `[of]` · **La potencia que vuelve se disipa en la
  etapa de salida.** **Un transmisor moderno se protege reduciendo potencia o cortando**, y **una
  relación alta es la avería más frecuente de un centro emisor**, casi siempre por **agua en un
  conector o un latiguillo dañado.**

## Los transmisores

| | **Modulación de amplitud** | **Modulación de frecuencia** |
|---|---|---|
| **Qué varía con el audio** | **La amplitud de la portadora** | **La frecuencia de la portadora** |
| **Banda que ocupa** | **Estrecha** | **Ancha** |
| **Calidad de audio** | **Limitada** | **Alta, con estéreo** |
| **Ruido** | **Le afecta directamente** | **Lo rechaza: el ruido es de amplitud** |
| **Alcance** | **Mucho, de noche por reflexión ionosférica** | **Línea de vista, poco más del horizonte** |

- **POR QUÉ UNA RECHAZA EL RUIDO Y LA OTRA NO** · `[of]` · **El ruido eléctrico se suma en AMPLITUD.**
  **Un receptor de frecuencia modulada limita la amplitud antes de demodular y con ella se lleva el
  ruido**; **uno de amplitud no puede hacerlo sin llevarse la señal.**
- **LA ONDA CORTA DEL ENUNCIADO** · `[of]` · **Aprovecha la reflexión ionosférica para alcanzar miles de
  kilómetros con potencia moderada.** **Su alcance cambia con la hora, la estación y el ciclo solar**,
  y por eso **las emisiones internacionales cambiaban de frecuencia según el momento del día.** **Es el
  servicio que internet ha vaciado**, y sigue en el temario porque sigue existiendo.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 68 | Frecuencias de los satélites de banda Ku | **Ascendente 14 GHz, descendente 12 GHz** ✔ |
| 73 | Qué caracteriza a un amplificador de clase C | **Alto rendimiento y muchos armónicos** ✔ |
| 75 | Qué es un reóstato | **Un resistor variable** ✔ **·** ajena al punto |
