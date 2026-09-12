# Tema 7 del específico de Sonido · Mezcla y tratamiento del sonido

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Sonido · punto 5 |
| **Sirve para** | **Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los procesadores de dinámica y de espectro, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Extensión** | **2.406 palabras** |

<!-- /portada -->

Los términos de este tema, presentados de entrada: el margen entre el nivel de trabajo y la saturación
(*headroom*); el umbral (*threshold*), la relación de compresión (*ratio*), el ataque, la relajación
(*release*), el codo (*knee*) y la recuperación de ganancia (*make-up*) de un compresor; el factor de
selectividad de un filtro (**Q**); el filtro de ranura (*notch*); el amplificador controlado por
tensión (**VCA**, *voltage-controlled amplifier*); el transistor de efecto campo (**FET**,
*field-effect transistor*); el decibelio de nivel de presión sonora (**dB SPL**), que el tema 2 ya
presentó; el compresor de válvula de ganancia variable (*Vari-Mu*); y la escucha previa al fader (**PFL**), que el tema 10 y el temario de Realización
también usan.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 5):
> «MEZCLA Y TRATAMIENTO DEL SONIDO. Mezcladores de audio: Tipos, características y funcionalidad.
> Equipos de tratamiento del sonido: Ecualizadores, Filtros, Sistemas de reducción de ruido,
> compresores.»

**Siete preguntas.** **Y el punto que más se parece al trabajo diario**: **cuatro de sus siete van de
dinámica —compresores y limitadores— y tres de ecualización.**

**El aviso de estudio, dicho de entrada**: **este punto no tiene ni un dato que memorizar.** **Todo se
razona si se entienden dos figuras: la curva de un compresor y la campana de un ecualizador.**

<!-- indice -->

## Índice

- [1. El headroom](#1-el-headroom)
- [2. La dinámica: qué hace un compresor](#2-la-dinámica-qué-hace-un-compresor)
- [3. El limitador](#3-el-limitador)
- [4. Las tecnologías de compresor](#4-las-tecnologías-de-compresor)
- [5. Los ecualizadores](#5-los-ecualizadores)
- [6. El factor Q y el filtro notch](#6-el-factor-q-y-el-filtro-notch)
- [7. Los sistemas de reducción de ruido](#7-los-sistemas-de-reducción-de-ruido)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. El headroom

**El nivel de diferencia entre el nivel nominal y el punto de saturación que se debe tener en una
mezcla de audio es el headroom.** Ésa es la respuesta oficial a la pregunta 21.

**Qué es y por qué existe**: **el nivel nominal es dónde se trabaja; la saturación es dónde el sistema
se rompe.** **La distancia entre los dos es el margen que queda para lo imprevisto**: un grito, un
golpe de caja, una entrada mal medida.

**Y la cifra depende del sistema, que es lo que hay que tener claro:**

| Sistema | Nivel nominal | Saturación | Headroom típico |
|---|---|---|---|
| **Analógico profesional** | **+4 dBu** | **Donde la electrónica recorta**, con margen amplio | **De 18 a 24 dB** |
| **Digital** | **Lo que se elija** | **0 dBFS**: un techo absoluto | **El que se deje bajando el nivel nominal** |

**La diferencia que más cuesta interiorizar**: **en analógico, pasarse un poco distorsiona
progresivamente; en digital, pasarse un poco RECORTA.** **El 0 dBFS no es una recomendación: es el
número más grande que cabe.** **Por eso una mezcla digital se trabaja con el nominal bien por debajo
del techo.**

**Las tres opciones falsas nombran tres conceptos reales y ninguno es éste:**

| Opción | Qué es de verdad |
|---|---|
| **Masterización** | **La fase final de una producción**: no es una distancia entre niveles |
| **Nivel de presión sonora** | **Lo que hay en el aire**, en dB SPL: no es un margen |
| **Rango dinámico** | **La distancia entre el ruido de fondo y la saturación.** **Es la falsa mejor puesta**: el headroom mide desde el nominal hacia arriba; el rango dinámico, desde el suelo de ruido |

## 2. La dinámica: qué hace un compresor

**Un compresor reduce la diferencia entre lo más fuerte y lo más flojo.** **Sus mandos, y qué hace
cada uno:**

| Mando | Qué hace |
|---|---|
| **Umbral** | **A partir de qué nivel empieza a actuar** |
| **Relación** | **Cuánto reduce lo que pasa del umbral**: 4:1 significa que cuatro decibelios de más a la entrada se convierten en uno a la salida |
| **Ataque** | **Cuánto tarda en empezar a reducir** |
| **Relajación** | **Cuánto tarda en soltar** |
| **Codo** | **Si la reducción entra de golpe (*hard knee*) o progresivamente (*soft knee*)** |
| **Recuperación de ganancia** | **Sube todo lo que queda**, para compensar lo que la compresión ha bajado |

**La pregunta 22**: **el ajuste make-up de un compresor recupera ganancia.** Ésa es la respuesta
oficial.

**Por qué hace falta**: **un compresor sólo BAJA.** **Después de comprimir, el material tiene menos
nivel de pico que antes**, y **si se dejara así el compresor sonaría siempre «peor» que el original.**
**El make-up devuelve al conjunto el nivel que la reducción le quitó**, y **ése es el efecto que se
percibe como «más fuerte y más denso»: no lo hace la compresión, lo hace la ganancia de después.**

**Las tres opciones falsas nombran otros tres mandos o conceptos**: **la posición en la cadena, un
filtrado de agudos y el codo.** **El codo es la que más se acerca y es un mando distinto: el make-up
está al final de la cadena interna del compresor, después de la reducción.**

## 3. El limitador

**El compresor que actúa sólo atenuando los niveles de entrada superiores a un umbral, dejando pasar
inalteradas las señales de nivel inferior, es el compresor limitador.** Ésa es la respuesta oficial a
la pregunta 40.

**Qué lo define**: **una relación de compresión muy alta —10:1 o mayor, y en el límite infinita— y un
ataque muy rápido.** **Por debajo del umbral no toca nada; por encima, no deja pasar.** **Un limitador
es un techo.**

**Y para qué se usa, que explica por qué se pregunta:**

| Uso | Por qué |
|---|---|
| **Proteger una etapa de potencia** | **Que no le lleguen picos que la rompan** |
| **Proteger un transmisor** | **Que no se sobremodule**: es obligación técnica en radiodifusión |
| **Cerrar una masterización** | **Subir el nivel medio sin pasar de 0 dBFS**: es el limitador de pico |

**Las tres opciones falsas —«lineal», «de ganancia constante» y «Rumble»— no nombran tipos de
compresor.** ***Rumble* es el ruido de baja frecuencia de un giradiscos**, y **el filtro que lo quita
se llama así**: **es un falso amigo bien puesto.**

## 4. Las tecnologías de compresor

**La pregunta 56**: **de los tipos de compresor enumerados, el que tiene una velocidad superior de
respuesta es el VCA.** Ésa es la respuesta oficial.

| Tecnología | Cómo controla la ganancia | Velocidad | Carácter |
|---|---|---|---|
| **VCA** ✔ | **Un amplificador controlado por tensión** | **La más rápida y la más precisa** | **Limpio, transparente, controlable** |
| **Óptico** | **Una lámpara y una célula fotosensible** | **Lenta**, y con una relajación en dos tiempos | **Muy musical en voz** |
| **Vari-Mu** | **Una válvula cuya ganancia varía con la polarización** | **Lenta** | **Denso, «pegado»**: el sonido clásico |
| ***FET*** | **Un transistor de efecto campo** | **Muy rápida** | **Agresivo**: el de las cajas de batería |

**La opción b), «clase A», es la que hay que descartar por categoría, no por velocidad**: **la clase A
no es una tecnología de compresión, es una clase de amplificador** —la del tema 1—. **Un compresor
puede tener su etapa de salida en clase A y ser óptico, o de válvula, o de VCA.**

**Y la regla que ordena la tabla**: **la velocidad y el carácter van reñidos.** **El VCA es el que
mejor obedece y el que menos se nota; el óptico y el de válvula se notan, y eso es exactamente por lo
que se eligen.**

## 5. Los ecualizadores

**La pregunta 23 es negativa**: **de los que enumera, el que NO es un tipo de ecualizador es
multibanda.** Ésa es la respuesta oficial.

| Tipo | Qué se puede tocar |
|---|---|
| **Gráfico** | **Sólo la ganancia** de cada banda: la frecuencia y el ancho vienen fijos |
| **Paramétrico** | **Frecuencia, ganancia Y ancho de banda**: los tres parámetros |
| **Semiparamétrico** | **Frecuencia y ganancia**, con el ancho fijo |
| **«Multibanda»** ✔ | **No es un tipo de ecualizador**: es un adjetivo que se aplica a los COMPRESORES |

**Por qué la falsa está bien puesta**: **el compresor multibanda existe y es corriente** —parte el
espectro en bandas y comprime cada una por separado—. **La palabra es real; el aparato al que se
aplica es otro.** **Y para más confusión, todo ecualizador gráfico es, literalmente, de muchas
bandas.** **Lo que la pregunta mide es saber que «multibanda» no es una CATEGORÍA de ecualizador.**

## 6. El factor Q y el filtro notch

**La pregunta 91**: **en un ecualizador paramétrico, un factor Q de 1,41 corresponde aproximadamente a
1 octava.** Ésa es la respuesta oficial.

**Qué es el Q**: **la frecuencia central dividida entre el ancho de banda.** **A más Q, más estrecha
la campana.** **Y la relación con las octavas es la que hay que tener:**

| Q | Ancho aproximado |
|---|---|
| **0,7** | **2 octavas**: muy ancho, para dar carácter |
| **1,41** ✔ | **1 octava**: el ajuste corriente de trabajo |
| **2,9** | **1/2 octava** |
| **4,3** | **1/3 de octava**: el ancho de un ecualizador gráfico de tercio |
| **Más de 10** | **Quirúrgico**: es el terreno del notch |

**La opción a) —«el Q sólo existe en los ecualizadores gráficos»— es falsa por partida doble**: **en
un gráfico el Q está FIJO y no se toca, y es precisamente en el paramétrico donde el Q se ajusta.**
**Dice lo contrario de lo que ocurre.**

**La pregunta 45**: **un filtro notch se utiliza idealmente para evitar un acople con una megafonía.**
Ésa es la respuesta oficial.

**Qué es un notch**: **un filtro de ranura, de Q altísimo, que quita una franja de frecuencia muy
estrecha y no toca lo de al lado.**

**Por qué sirve contra el acoplamiento**: **la realimentación de un sistema de megafonía se dispara
siempre a UNA frecuencia concreta** —aquella en la que la ganancia del lazo llega a uno primero—.
**Quitando dos o tres decibelios exactamente ahí, el lazo deja de oscilar y el resto del sonido no se
entera.** **Con un ecualizador de campana ancha habría que quitar mucho más y se oiría.**

**Las tres opciones falsas y por qué caen:**

1. **«Evitar diafonía entre canales»** **es un problema de aislamiento eléctrico o de cableado**, no de
   frecuencia: **no hay una frecuencia que quitar.**
2. **«Atenuar toda la banda de medias de un bombo»** **pide justo lo contrario que un notch**: **toda
   una banda es un filtro ancho.**
3. **«Quitar las pes de una voz»** **es trabajo de un antipop o de un filtro de corte de graves**: **el
   golpe de aire de una oclusiva no es una frecuencia estrecha.**

## 7. Los sistemas de reducción de ruido

**El enunciado del anexo los nombra y el examen no los pregunta.** **El tema los cubre porque el
programa los pide.**

| Familia | Cómo funciona | Dónde se usó o se usa |
|---|---|---|
| **De doble extremo** (*companding*) | **Comprime al grabar y expande al reproducir**: exige el mismo sistema en los dos extremos | **Los sistemas de cinta analógica** |
| **Puerta de ruido** | **Cierra el canal cuando la señal baja del umbral** | **Directo y grabación multipista**: es el de uso diario |
| **Expansor** | **Como la puerta, pero progresivo** en vez de todo o nada | **Cuando cerrar del todo se nota** |
| **Reducción espectral** | **Aprende el perfil del ruido y lo resta banda a banda** | **Postproducción y restauración** |
| **Filtro de corte** | **Quita lo que está fuera de la banda útil**: *rumble* abajo, siseo arriba | **Siempre, y es el primero que hay que probar** |

**Y la regla del oficio que ordena la tabla**: **el mejor sistema de reducción de ruido es no
grabarlo.** **Un micrófono bien elegido y bien colocado, en el tema 5, ahorra más ruido que cualquier
proceso posterior.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 21 | Diferencia entre nivel nominal y saturación | d) Headroom ✔ |
| 22 | Qué hace el ajuste make-up de un compresor | c) Recupera ganancia ✔ |
| 23 | Cuál NO es un tipo de ecualizador | c) Multibanda ✔ |
| 40 | Compresor que sólo atenúa por encima del umbral | c) Compresor limitador ✔ |
| 45 | Para qué se usa un filtro notch | a) Para evitar un acople con una megafonía ✔ |
| 56 | Qué compresor responde más rápido | d) VCA ✔ |
| 91 | Octavas de un factor Q de 1,41 | c) 1 octava ✔ |

**Las siete respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Un aviso de reparto**: **una de las siete es negativa** —la 23—, **y es la única del tema que no se
contesta razonando sino sabiendo que «multibanda» califica a los compresores.**

## 9. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los mezcladores y los equipos de tratamiento del
sonido, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las siete **van como oficio** |

**Tres declaraciones expresas:**

1. **Las cifras de headroom del epígrafe 1 son órdenes de magnitud del sector, no valores
   normalizados.** **Los 18 a 24 decibelios de un sistema analógico profesional varían con el equipo y
   con la casa**, y **lo que la pregunta mide es el concepto, no la cifra.**
2. **La correspondencia entre factor Q y octavas del epígrafe 6 es una relación matemática
   aproximada**, y **los manuales la tabulan con pequeñas diferencias según cómo definan el ancho de
   banda.** **Con la definición corriente —el ancho a 3 decibelios— el resultado coincide con la
   respuesta oficial.**
3. **Las cuatro tecnologías de compresor del epígrafe 4 son una clasificación asentada del sector, no
   normalizada.** **Sus caracteres sonoros son descripciones de uso**, y **el tema los presenta como
   tales.** **Lo que sí es objetivo, y es lo que la pregunta mide, es que el VCA es el más rápido de
   los cuatro.**

**El resto del tema va como oficio y así se declara**: la definición de headroom y su diferencia con
el rango dinámico, los seis mandos de un compresor, qué convierte a un compresor en limitador, los
tres tipos de ecualizador y por qué «multibanda» no es uno de ellos, el mecanismo del notch contra el
acoplamiento y la tabla de sistemas de reducción de ruido. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
