# Tema 17 del específico de Ingeniería Superior · Telecomunicación · Sistemas radiantes, parámetros de antena y propagación

Las siglas y símbolos de este tema, presentados de entrada: la potencia isótropa radiada equivalente
(**PIRE**) y la radiada aparente respecto a un dipolo (**PRA**); el decibelio (**dB**), el decibelio
sobre un milivatio (**dBm**), el decibelio sobre el isótropo (**dBi**) y sobre el dipolo (**dBd**); la
relación de onda estacionaria (**ROE**); el coeficiente de reflexión y las pérdidas de retorno; el
ancho de haz a media potencia; la relación delante-detrás; la frecuencia muy alta (**VHF**), la ultraalta
(**UHF**), la superalta (**SHF**) y la extremadamente alta (**EHF**); el hercio (**Hz**) con sus
múltiplos **kHz**, **MHz** y **GHz**; y la longitud de onda (**λ**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 19):
> «Sistemas radiantes. Parámetros básicos. Tipos de antenas. Sistemas y tecnologías de
> radiocomunicaciones. Modos de propagación de ondas eléctricas.»

**Hay que decir de entrada cómo se reparte este punto con el 25 del mismo anexo**, porque **los dos
hablan de antenas y el reparto va declarado**: **el punto 25 —«Antenas y transmisores de
radiodifusión»— es IDÉNTICO, palabra por palabra —sólo cambia un signo de puntuación tras la primera
frase—, al punto 18 del anexo de Ingeniería Técnica ·
Telecomunicación**, y **su tema se comparte con aquella ocupación**, como se comparte el de prevención.
**Allí van las líneas de transmisión, las guías de onda, los transmisores de amplitud y de frecuencia,
la onda corta y la medida de distorsiones.**

**Aquí, en el punto 19, van los PARÁMETROS y la PROPAGACIÓN**: **qué mide cada magnitud de una antena,
qué tipos hay y cómo viaja la onda.** **Es el punto teórico y el 25 es el de la instalación de
radiodifusión.**

**Y la idea que ordena el punto**: **una antena no amplifica nada.** **La ganancia de una antena es
CONCENTRACIÓN, no amplificación**: **reparte la misma potencia en menos ángulo.** **Quien entienda eso
no se equivoca en ninguna pregunta de este tema.**

<!-- indice -->
<!-- /indice -->

## 1. Qué es una antena

**La definición funcional**: **el dispositivo que convierte una onda guiada en una onda radiada, y al
revés.** **Es la frontera entre el cable y el espacio.**

**Y las dos propiedades que se derivan de esa definición y que hay que saber:**

1. **Una antena es RECÍPROCA.** **Su comportamiento al transmitir y al recibir es el mismo**:
   **la misma ganancia, el mismo diagrama y la misma polarización.** **Por eso se puede estudiar como
   emisora y aplicar lo aprendido a la recepción.**
2. **Una antena está ADAPTADA o no lo está.** **Si su impedancia no casa con la de la línea, parte de
   la potencia se refleja y vuelve**, y **eso no calienta el aire: calienta el transmisor.**

## 2. Los parámetros básicos

**Los que el enunciado pide expresamente, con qué mide cada uno:**

| Parámetro | Qué mide |
|---|---|
| **DIAGRAMA o PATRÓN DE RADIACIÓN** | **La DISTRIBUCIÓN ESPACIAL de la potencia radiada**: cuánto radia en cada dirección |
| **DIRECTIVIDAD** | **Cuánto concentra** respecto a un radiador isótropo |
| **GANANCIA** | **La directividad multiplicada por el rendimiento**: lo que de verdad sale |
| **ANCHO DE HAZ** | **El ángulo dentro del cual la potencia no baja de la mitad** |
| **RELACIÓN DELANTE-DETRÁS** | **Cuánto menos radia hacia atrás que hacia delante** |
| **LÓBULOS SECUNDARIOS** | **Lo que radia fuera del haz principal**: interferencia potencial |
| **POLARIZACIÓN** | **La orientación del campo eléctrico**: vertical, horizontal, circular |
| **IMPEDANCIA de entrada** | **Lo que la antena presenta a la línea** |
| **ANCHO DE BANDA** | **En qué margen de frecuencias mantiene sus prestaciones** |
| **RENDIMIENTO** | **Cuánta potencia entregada acaba radiada** |

**La pregunta directa del cuadernillo es la primera fila**: **el patrón de radiación representa la
DISTRIBUCIÓN ESPACIAL DE LA POTENCIA RADIADA.** **No la impedancia característica, que es otro
parámetro; ni la polarización, que es la orientación del campo; ni la eficiencia comparada con un
dipolo, que es la ganancia expresada en decibelios sobre el dipolo.** **Las tres opciones falsas son
parámetros de antena reales colocados en el sitio de otro.**

**Las dos referencias de ganancia y por qué hay dos**, que es una confusión clásica:

| Referencia | Respecto a qué |
|---|---|
| **Decibelios sobre el ISÓTROPO** | **Un radiador teórico que radia igual en todas direcciones** |
| **Decibelios sobre el DIPOLO** | **Un dipolo de media onda**, que ya tiene ganancia propia |

**Y la regla**: **la misma antena tiene un número mayor expresado sobre el isótropo que sobre el
dipolo**, porque **el dipolo no es isótropo: ya concentra.** **Comparar dos antenas con referencias
distintas es el error de catálogo más frecuente.**

**La POLARIZACIÓN, con la regla que la hace útil**: **transmisor y receptor tienen que estar
polarizados igual.** **Una antena horizontal recibe muy mal una emisión vertical**, y **esa pérdida no
la arregla ninguna ganancia.** **La polarización circular resuelve el problema cuando la orientación
del receptor no se puede controlar**, a costa de una pérdida fija frente a la coincidencia perfecta.

## 3. El cálculo de la potencia radiada

**La magnitud que resume el conjunto transmisor, línea y antena**: **la potencia isótropa radiada
equivalente.** **Qué significa**: **la potencia que habría que dar a un radiador isótropo para producir
en la dirección de máxima radiación el mismo efecto que produce este sistema.**

**Cómo se calcula, en decibelios, que es como se pregunta:**

**Potencia isótropa radiada equivalente = potencia del transmisor − pérdidas + ganancia de la antena**

**Y la razón de que se trabaje en decibelios**: **porque convierte multiplicaciones en sumas.** **Una
cadena de ganancias y pérdidas se resuelve sumando y restando**, y **eso es lo que un examen pide
hacer.**

**El ejemplo que el cuadernillo de esta ocupación plantea, resuelto paso a paso**: **un emisor de −10
decibelios sobre milivatio, una antena de 30 decibelios sobre el isótropo y 1 decibelio de pérdidas en
el cableado dan −10 − 1 + 30 = 19 decibelios sobre milivatio.**

**Las tres cosas que hay que vigilar en esa cuenta, porque son donde se falla:**

1. **Las PÉRDIDAS se restan y la ganancia se SUMA.** **Parece obvio y es el error que las opciones
   falsas explotan**: **hay una opción que suma la pérdida y otra que la olvida.**
2. **Las unidades tienen que ser COHERENTES.** **El resultado se expresa en la misma referencia de
   potencia que la entrada** —aquí, decibelios sobre milivatio—, y **la ganancia en decibelios sobre
   el isótropo se suma sin convertir porque es una relación, no una potencia.**
3. **El signo de la potencia de entrada puede ser NEGATIVO y no pasa nada.** **Un valor negativo en
   decibelios sobre milivatio sólo significa menos de un milivatio**, y **la aritmética es la misma.**

**Y la observación de oficio que cierra el epígrafe**: **la potencia radiada no es lo que interesa al
final: interesa lo que LLEGA.** **La cuenta completa de un enlace resta además las pérdidas del camino
y suma la ganancia de la antena receptora**, y **eso es el balance de enlace del tema 9.**

## 4. Los tipos de antena

**Ordenados por su principio, que es como se recuerdan:**

| Familia | Cómo funciona | Dónde se usa |
|---|---|---|
| **DIPOLO y monopolo** | **Elementos resonantes de longitud relacionada con la onda** | **La antena elemental**; base de casi todo |
| **AGRUPACIONES o arrays** | **Varios elementos combinados en fase** | **Concentrar y dar forma al haz**: sistemas radiantes de difusión |
| **De ELEMENTOS PARÁSITOS** | **Un elemento activo y varios que reflejan y dirigen** | **Recepción doméstica y enlaces**: directividad barata |
| **LOGARÍTMICO-PERIÓDICAS** | **Elementos de tamaño escalado** | **Gran ancho de banda**: medida y vigilancia |
| **De APERTURA** | **Una superficie que radia**: bocinas y reflectores | **Frecuencias altas**: satélite y radioenlaces |
| **PARABÓLICAS** | **Un reflector que concentra en un foco** | **Mucha ganancia y haz muy estrecho** |
| **Impresas o de parche** | **Sobre circuito impreso** | **Equipos compactos y agrupaciones planas** |
| **Panel para difusión** | **Agrupación de dipolos ante un reflector** | **Sistemas radiantes de televisión y radio** |

**Y las dos reglas que relacionan tamaño, frecuencia y ganancia:**

1. **El tamaño de una antena está ligado a la LONGITUD DE ONDA.** **A frecuencia baja, la longitud de
   onda es larga y la antena es grande; a frecuencia alta, pequeña.** **Por eso las antenas de onda
   media son torres y las de satélite caben en una mano.**
2. **La ganancia sale del TAMAÑO ELÉCTRICO.** **A igual frecuencia, más superficie es más ganancia y
   haz más estrecho**, y **haz más estrecho significa apuntar mejor.** **Ganancia y tolerancia de
   apuntamiento van en direcciones opuestas.**

**El SISTEMA RADIANTE, que es lo que el enunciado nombra en primer lugar**: **el conjunto de antenas,
su estructura de soporte, la red de distribución que reparte la potencia entre ellas y sus
accesorios.** **Su función es dar el diagrama que la cobertura necesita**, y **para eso se combinan
varios paneles con las fases y las potencias adecuadas.**

**Y el RADOMO, que el cuadernillo pregunta**: **es una CUBIERTA PROTECTORA para antenas.** **No es un
tipo de modulación, ni un sistema de radar, ni un instrumento de medida.** **Su función es proteger de
la lluvia, el hielo, el viento y los pájaros**, y **su exigencia es ser transparente a la onda**: **un
radomo mal elegido o mojado introduce pérdidas y desadapta.**

## 5. La propagación

**Los modos que el enunciado pide, con qué los caracteriza:**

| Modo | Cómo viaja | Dónde manda |
|---|---|---|
| **ONDA DE SUPERFICIE** | **Pegada al suelo, siguiendo su curvatura** | **Frecuencias bajas**: onda larga y media |
| **ONDA ESPACIAL o directa** | **Línea de vista, con su reflexión en el suelo** | **Frecuencias altas**: televisión, radioenlaces |
| **ONDA IONOSFÉRICA** | **REFLEJADA en la ionosfera** | **Onda corta**: alcance intercontinental |
| **Por DISPERSIÓN troposférica** | Difusión en irregularidades de la baja atmósfera | Enlaces largos sin vista |
| **Por SATÉLITE** | **Atravesando la atmósfera** | Tema 9 |

**Los fenómenos que le pasan a una onda por el camino, que es la parte que un examen pregunta suelta:**

| Fenómeno | Qué es |
|---|---|
| **REFLEXIÓN** | **La onda rebota en una superficie grande y lisa**, cambiando de dirección con ángulo simétrico |
| **REFRACCIÓN** | **Cambia de dirección al pasar de un medio a otro** con distinta velocidad |
| **DIFRACCIÓN** | **La onda bordea un obstáculo y cambia de dirección al encontrarlo**, llegando detrás de él |
| **DISPERSIÓN** | **Se reparte en muchas direcciones** al chocar con muchos objetos pequeños |
| **ABSORCIÓN** | **El medio se queda con parte de la energía**: lluvia, gases, vegetación |
| **MULTITRAYECTO** | **La misma señal llega por varios caminos** con retardos distintos |

**La pregunta directa del cuadernillo es la tercera fila**: **el fenómeno por el que una onda
electromagnética CAMBIA DE DIRECCIÓN AL ENCONTRAR UN OBSTÁCULO es la DIFRACCIÓN.** **No la reflexión,
que es el rebote en una superficie; ni la absorción, que no cambia la dirección sino que quita energía;
ni la polarización, que no es un fenómeno de propagación sino una propiedad de la onda.**

**Y la lectura de oficio de la difracción, que explica media cobertura terrestre**: **la difracción es
lo que permite recibir señal detrás de una colina o de un edificio.** **Sin ella, la cobertura
terrestre sería estrictamente línea de vista**, y **cuanto MÁS BAJA es la frecuencia, más se difracta y
mejor se sortean los obstáculos.** **Por eso las bandas bajas cubren mejor terreno irregular y las
altas exigen visión directa.**

## 6. Las bandas de frecuencia

**La escalera que hay que llevar aprendida, porque se pregunta suelta y cada escalón multiplica por
diez:**

| Denominación | Margen |
|---|---|
| **Frecuencias medias** | **De 300 a 3.000 kilohercios** |
| **Frecuencias altas** | **De 3 a 30 megahercios** |
| **Frecuencias MUY ALTAS** | **De 30 a 300 megahercios** |
| **Frecuencias ULTRAALTAS** | **De 300 a 3.000 megahercios** |
| **Frecuencias SUPERALTAS** | **De 3 a 30 gigahercios** |
| **Frecuencias EXTREMADAMENTE ALTAS** | **De 30 a 300 gigahercios** |

**La pregunta directa**: **las señales de frecuencias muy altas van de 30 a 300 megahercios.** **No de
300 a 3.000, que son las ultraaltas; ni de 3 a 30 gigahercios, que son las superaltas.**

**Y la regla que evita memorizar la tabla**: **cada banda va de una década a la siguiente y el punto de
apoyo es que las muy altas empiezan en 30 megahercios.** **Desde ahí, hacia arriba y hacia abajo, todo
se deduce multiplicando o dividiendo por diez.**

**Y lo que hay que saber decir de cada tramo, en una línea**: **cuanto más baja la frecuencia, más
alcance, más difracción, menos capacidad y antenas más grandes; cuanto más alta, más capacidad, más
directividad, más atenuación por lluvia y necesidad de línea de vista.** **Toda la ingeniería de
radiocomunicaciones es elegir un punto en ese intercambio.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **El reparto entre este punto y el 25 del mismo anexo va declarado en la cabecera**: **el 25 es
   idéntico palabra por palabra —con un solo signo de puntuación distinto— al punto 18 del anexo de
   Ingeniería Técnica · Telecomunicación, y su
   tema se COMPARTE con aquella ocupación.** **Aquí van los parámetros, los tipos y la propagación;
   allí, las líneas, las guías, los transmisores y la medida.** **No se solapan y no se recorta
   contenido.**
2. **Este tema NO da ninguna ganancia concreta, ningún ancho de haz, ninguna relación de onda
   estacionaria admisible, ninguna longitud de antena y ninguna atenuación por kilómetro.** **Son dato
   de recomendación y de fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.**
3. **Las cifras del epígrafe 6 son la escalera de décadas del vocabulario radioeléctrico común**, y
   **la plantilla oficial de esta ocupación confirma en su pregunta 33 el tramo de las frecuencias muy
   altas.** **El temario declara esa procedencia y no atribuye la tabla a ninguna recomendación.**
4. **Las cuatro respuestas que la plantilla confirma —el patrón de radiación como distribución
   espacial de la potencia, el radomo como cubierta protectora, la difracción como el cambio de
   dirección al encontrar un obstáculo y el resultado de 19 decibelios sobre milivatio del cálculo de
   potencia radiada— se recogen con su razonamiento**, en **las preguntas 35, 42, 87 y 31.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **los
   transmisores, las líneas y las guías de onda, al tema 23, que se comparte**; **el balance de enlace
   y el satélite, al tema 9**; **la difusión terrestre y su planificación, al tema 7**; **y la
   modulación, al tema 3.**

**El resto del tema va como oficio y así se declara**: la idea de que la ganancia de una antena es
concentración y no amplificación, las dos propiedades de reciprocidad y de adaptación con el aviso de
que la potencia reflejada calienta el transmisor, la explicación de por qué hay dos referencias de
ganancia y de que la misma antena da un número mayor sobre el isótropo, la regla de la coincidencia de
polarización, la fórmula de la potencia radiada con la razón de trabajar en decibelios y las tres cosas
que hay que vigilar al calcularla, las dos reglas que relacionan tamaño, frecuencia y ganancia con la
observación de que ganancia y tolerancia de apuntamiento van en direcciones opuestas, la exigencia de
que un radomo sea transparente a la onda, la lectura de la difracción como lo que explica media
cobertura terrestre y de que se difracta más cuanto más baja es la frecuencia, la regla mnemotécnica de
la escalera de décadas y el resumen del intercambio entre alcance y capacidad. **Nada de eso está en un
boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si
lo estuviera.
