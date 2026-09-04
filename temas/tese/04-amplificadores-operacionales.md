# Tema 4 del específico de Técnica de Equipos y Sistemas Electrónicos · Amplificadores operacionales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica de Equipos y Sistemas Electrónicos · punto 4 |
| **Sirve para** | **Técnica de Equipos y Sistemas Electrónicos** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el amplificador operacional, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Tres de las cinco preguntas dependen de un esquema.** El temario no los describe: aporta **las tres reglas que resuelven cualquier circuito con operacional**, que es lo que permite atacar el que salga |
| **Extensión** | **2.103 palabras** |

<!-- /portada -->

Los términos y siglas de este tema, presentados de entrada: el amplificador operacional (**AO**, u
**op-amp** en la documentación en inglés); sus dos entradas, la inversora (**−**) y la no inversora
(**+**); la ganancia en lazo abierto (**A**) y la realimentación (*feedback*); los montajes básicos
—seguidor o adaptador de impedancia (*buffer*), inversor, no inversor, sumador, restador,
comparador, integrador y derivador—; la velocidad de subida (*slew rate*); y la corriente continua
(**DC**), que el tema 1 ya presentó.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 4):
> «AMPLIFICADORES OPERACIONALES: El amplificador diferencial. La fuente de corriente constante.
> Principales características de los amplificadores operacionales. Tipos de amplificadores
> operacionales. Circuitos prácticos con amplificadores operacionales.»

**Cinco preguntas.** **Y el componente que más aparece en un equipo de audio y vídeo profesional**:
**cada entrada balanceada, cada salida de línea, cada filtro activo y cada circuito de medida lleva
uno.**

**Tres de las cinco preguntas dependen de un esquema.** **Y las cinco se contestan con las tres reglas
del epígrafe 2, que son las que hacen legible cualquier circuito con un operacional dentro.**

<!-- indice -->

## Índice

- [1. Qué es y qué mide la pregunta 46](#1-qué-es-y-qué-mide-la-pregunta-46)
- [2. Las tres reglas que resuelven cualquier circuito](#2-las-tres-reglas-que-resuelven-cualquier-circuito)
- [3. El seguidor y la pregunta 5 del segundo llamamiento](#3-el-seguidor-y-la-pregunta-5-del-segundo-llamamiento)
- [4. Las tres preguntas que dependen de un esquema](#4-las-tres-preguntas-que-dependen-de-un-esquema)
- [5. Lo que el enunciado pide y el examen no pregunta](#5-lo-que-el-enunciado-pide-y-el-examen-no-pregunta)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Qué es y qué mide la pregunta 46

**Un amplificador operacional es un amplificador DIFERENCIAL de mucha ganancia**: **amplifica la
DIFERENCIA entre sus dos entradas, y la amplifica muchísimo.**

**Desde el punto de vista teórico, una propiedad de un amplificador operacional es la alta impedancia
de entrada.** Ésa es la respuesta oficial a la pregunta 46.

**Las cuatro propiedades del operacional IDEAL, que son las que el examen presupone:**

| Propiedad | Valor ideal | Por qué importa |
|---|---|---|
| **Ganancia en lazo abierto** | **Infinita** | **Es lo que permite que la realimentación mande** |
| **Impedancia de entrada** ✔ | **Infinita** | **No carga a lo que tiene delante**: no le roba señal |
| **Impedancia de salida** | **Cero** | **Entrega la tensión que sea sin caer** |
| **Ancho de banda** | **Infinito** | **Ideal: en la práctica es el límite real** |

**Y las tres opciones falsas de la pregunta son las tres inversiones de esa tabla**: **«muy baja
ganancia», «baja impedancia de entrada» y «alta impedancia en la salida».** **La pregunta se contesta
sabiendo que el operacional ideal es lo contrario de todo eso.**

**Por qué esas propiedades**: **un operacional está pensado para NO alterar lo que mide y para
entregar sin esfuerzo lo que da.** **Es el componente que permite encadenar etapas sin que cada una
estropee a la siguiente.**

## 2. Las tres reglas que resuelven cualquier circuito

**Ésta es la parte del tema que hay que llevarse**, porque **con ella se leen los tres esquemas que el
examen muestra y no describe.**

**Cuando un operacional trabaja con realimentación NEGATIVA y no está saturado:**

1. **Las dos entradas están a la MISMA tensión.** **Es el llamado cortocircuito virtual: la
   realimentación hace lo que haga falta para igualarlas.**
2. **Por las entradas NO entra corriente.** **Su impedancia de entrada es altísima.**
3. **La salida hace lo que sea necesario para que se cumplan las dos primeras.**

**Con esas tres reglas salen las ganancias de los montajes básicos:**

| Montaje | Ganancia | Para qué se usa |
|---|---|---|
| **Seguidor** (*buffer*) | **1**: la salida copia a la entrada | **Adaptar impedancias**: aislar sin amplificar |
| **No inversor** | **1 + Rf/R1** | **Amplificar sin invertir**: la ganancia nunca baja de 1 |
| **Inversor** | **−Rf/R1** | **Amplificar invirtiendo**: puede tener ganancia menor que 1 |
| **Sumador** | **Suma ponderada** de varias entradas | **Mezclar**: es el bus de una mesa de audio |
| **Restador** o diferencial | **Amplifica la diferencia** | **Entrada balanceada**: el tema 11 del temario de Sonido |
| **Comparador** | **Sin realimentación**: la salida se va a un extremo u otro | **Decidir**: convierte analógico en digital |

**Y el aviso que separa las dos mitades de la tabla**: **las tres reglas del principio SÓLO valen con
realimentación negativa.** **Un comparador no la tiene, así que sus entradas NO están a la misma
tensión y su salida está siempre saturada.** **Es el error de análisis más frecuente.**

## 3. El seguidor y la pregunta 5 del segundo llamamiento

**Se mide con un voltímetro un amplificador operacional configurado como seguidor y se obtienen 3
voltios a la entrada y 2 a la salida.** **La conclusión oficial es que está dañado: la salida debería
ser 3 voltios.** Ésa es la respuesta oficial.

**El razonamiento es la primera regla del epígrafe 2 aplicada al montaje más simple**: **en un
seguidor, la salida está conectada directamente a la entrada inversora.** **La realimentación iguala
las dos entradas, así que la salida tiene que valer exactamente lo mismo que la entrada no
inversora.** **Tres voltios dentro son tres voltios fuera.**

**Y las tres opciones falsas merecen mirarse porque cada una es un error de método distinto:**

| Opción | Por qué se cae |
|---|---|
| **«Funciona correctamente»** | **No**: un seguidor con ganancia distinta de 1 no funciona |
| **«No se puede verificar con un multímetro, se necesita un osciloscopio»** | **Falso**: con tensiones continuas el multímetro basta. **El osciloscopio hace falta para ver FORMA, no para medir un valor estable** |
| **«Está saturado»** | **La saturación llevaría la salida a un extremo** —cerca de la tensión de alimentación—, **no a 2 voltios con 3 a la entrada** |

**Ésta es, de las cinco, la única que no depende de ver el esquema**: **el montaje lo describe el
propio enunciado.**

## 4. Las tres preguntas que dependen de un esquema

**La pregunta 43** pide **el valor de la tensión de salida cuando la de entrada son 2,5 voltios**, y
**la respuesta oficial es 2,5 voltios.**

**La regla de familia**: **cuando la salida coincide EXACTAMENTE con la entrada, el montaje es un
seguidor**, o **un no inversor cuya red de realimentación tiene ganancia unidad.** **De las cuatro
opciones, la que repite el dato del enunciado es siempre candidata seria en un circuito con
operacional**, precisamente **porque el seguidor es el montaje más común.**

**La pregunta 65** pide **el valor de tensión a la salida del circuito**, y **la respuesta oficial es 6
voltios.**

**La regla de familia, en tres comprobaciones:**

1. **Localizar por qué entrada entra la señal.** **Si entra por la no inversora, la ganancia es
   positiva y vale 1 + Rf/R1; si entra por la inversora, es negativa y vale −Rf/R1.**
2. **Si el circuito no tiene señal de entrada sino sólo alimentación y resistencias, es un divisor de
   tensión seguido de un operacional**: **la salida es la del divisor multiplicada por la ganancia.**
3. **Y un resultado que sea la mitad exacta de la tensión de alimentación delata un divisor de dos
   resistencias iguales.**

**La pregunta 33** aplica a la entrada **una señal cuadrada** y pregunta **qué señal se obtiene a la
salida.** **La respuesta oficial es una señal triangular.**

**Y ésta se razona entera sin ver el esquema, que es lo que la hace la mejor del punto:**

| Montaje | Qué le hace a una señal cuadrada | Por qué |
|---|---|---|
| **Integrador** ✔ | **La convierte en TRIANGULAR** | **Integrar una constante da una rampa.** Una cuadrada son constantes alternas: sube y baja en rampas |
| **Derivador** | **La convierte en picos** estrechos | **Derivar una constante da cero**; sólo los flancos producen algo |
| **Amplificador** | **La deja cuadrada**, más grande | **No cambia la forma** |
| **Filtro paso bajo** | **La redondea** | **Recorta los armónicos altos** |

**De las cuatro opciones que la pregunta ofrece —cuadrada, senoidal, componente continua y
triangular—, la triangular es la única que corresponde a un montaje canónico con operacional**, y
**los otros tres resultados no salen de ningún circuito de este punto.**

**Ninguna de estas reglas sustituye a ver el esquema**, y **el tema lo dice.** **Pero la 33 muestra que
saber qué le hace cada montaje a una forma de onda vale casi tanto como verla.**

## 5. Lo que el enunciado pide y el examen no pregunta

**El enunciado nombra expresamente «la fuente de corriente constante» y «tipos de amplificadores
operacionales», y de eso no hay ninguna pregunta.** **El tema los cubre porque el programa lo pide.**

**La fuente de corriente constante**: **es un circuito que entrega la MISMA corriente sea cual sea la
carga**, dentro de un margen. **Es lo contrario de una fuente de tensión.** **Dentro de un
operacional, la fuente de corriente constante es la que polariza el par diferencial de entrada**, y en
un equipo se usa para alimentar sensores, para cargar condensadores linealmente y para excitar
diodos.

**Los tipos de operacional que un técnico distingue:**

| Tipo | Qué lo caracteriza | Dónde |
|---|---|---|
| **De propósito general** | **Barato y suficiente** | **La mayoría de los circuitos** |
| **De bajo ruido** | **Ruido de entrada mínimo** | **Previos de micrófono**: el tema 10 |
| **De alta velocidad** | **Mucha velocidad de subida y ancho de banda** | **Vídeo y señales rápidas** |
| **De precisión** | **Muy poca tensión de desviación y poca deriva** | **Instrumentación y medida**: el tema 13 |
| **De instrumentación** | **Tres operacionales en uno**, con entrada diferencial de alta impedancia | **Medida de señales pequeñas sobre ruido** |

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 33 | Qué señal se obtiene ante una entrada cuadrada | d) Una señal triangular ✔ **·** sólo con la plantilla |
| 43 | Tensión de salida con 2,5 V a la entrada | d) 2,5 V ✔ **·** sólo con la plantilla |
| 46 | Propiedad teórica de un amplificador operacional | c) Alta impedancia de entrada ✔ |
| 65 | Valor de tensión a la salida del circuito | a) 6 V ✔ **·** sólo con la plantilla |
| 5 (2.º llam.) | Qué se concluye de un seguidor con 3 V dentro y 2 fuera | b) Está dañado, la salida debería ser 3 V ✔ |

**Las cinco respuestas oficiales son correctas.**

**Tres de las cinco descansan sólo en la plantilla**: **las tres que dependen de un esquema.**

**Y el aviso de estudio**: **las tres reglas del epígrafe 2 son lo más rentable de este punto y de
buena parte del temario.** **Con ellas y con la tabla de montajes se entiende cualquier circuito con
operacional que el examen ponga delante**, aunque **no siempre se pueda dar el número exacto sin
verlo.**

## 7. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los amplificadores operacionales y sus montajes, y
**va como oficio**, salvo tres afirmaciones que descansan en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Tres afirmaciones**: los resultados de tres circuitos que el temario no puede reproducir | Preguntas 33, 43 y 65 |

**Tres declaraciones expresas:**

1. **Las preguntas 33, 43 y 65 dependen de un esquema que el temario no ha visto.** **Lo que aporta en
   su lugar son las tres reglas del cortocircuito virtual, la tabla de ganancias por montaje y la
   tabla de lo que cada montaje le hace a una forma de onda.** **En el caso de la 33 esas reglas
   bastan para llegar a la respuesta**; **en los otros dos casos, no.** **El tema distingue una cosa de
   la otra en lugar de presentarlas igual.**
2. **Las propiedades del operacional ideal del epígrafe 1 son un MODELO teórico**, y **el propio
   enunciado de la pregunta 46 lo dice: «desde el punto de vista teórico».** **Un operacional real
   tiene ganancia finita, impedancia de entrada muy alta pero no infinita y algo de impedancia de
   salida.** **El tema lo declara para que el modelo no se confunda con el componente.**
3. **La clasificación de tipos de operacional del epígrafe 5 es de uso comercial**, no normalizada, y
   **el tema la presenta como tal.** **Ninguna pregunta depende de ella.**

**El resto del tema va como oficio y así se declara**: las tres reglas del cortocircuito virtual y su
límite, las ganancias de los montajes básicos, por qué un comparador no las cumple, lo que cada
montaje le hace a una señal cuadrada y qué es una fuente de corriente constante. **Nada de eso está en
un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
