# Tema 2 del específico de Sonido · Principios físicos del sonido y la audición

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Sonido · punto 1.3 y 1.5 |
| **Sirve para** | **Sonido** |
| **Fuente** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** |
| **Identificador** | `BOE-A-2010-927` · BOE núm. 21, de 24/01/2010 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. De él sale **que el pascal es la unidad legal de presión**, que es la respuesta a la pregunta 89 |
| **Extensión** | **2.686 palabras** |

<!-- /portada -->

Las siglas y unidades de este tema, presentadas de entrada: el pascal (**Pa**), unidad legal de
presión; el decibelio (**dB**), el belio (**B**) y el neper (**Np**), que son unidades logarítmicas
aceptadas para su uso con el Sistema Internacional; el decibelio de nivel de presión sonora (**dB
SPL**, *sound pressure level*); el hercio (**Hz**) y el kilohercio (**kHz**); las curvas de criterio
de ruido de fondo (**NC**, *noise criteria*, y **NR**, *noise rating*); y el nivel de una magnitud
respecto a una referencia, que es lo que un decibelio siempre expresa.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, puntos 1.3 y 1.5):
> «CONOCIMIENTOS BÁSICOS. Principios básicos sobre sonido: (Ondas, frecuencias, longitud de onda,
> periodo, enmascaramiento, etc.). La voz y la audición: fisiología básica.»

**Seis preguntas.** **Y el tema que sostiene a los otros dieciséis**: **todo lo que este temario dice
después —el micrófono, la sala, el compresor, el medidor de sonoridad— se mide en las unidades que
aquí se fijan.**

**Con una particularidad que este proyecto no esperaba encontrar**: **dos de las seis respuestas están
en el Boletín Oficial del Estado.** **El pascal y el decibelio son unidades legales de medida, y el
real decreto que las establece dice de ellas más de lo que la pregunta pide.**

<!-- indice -->

## Índice

- [1. Qué es el sonido y qué lo describe](#1-qué-es-el-sonido-y-qué-lo-describe)
- [2. La unidad de presión sonora es LEGAL](#2-la-unidad-de-presión-sonora-es-legal)
- [3. El decibelio, y por qué SIEMPRE necesita una referencia](#3-el-decibelio-y-por-qué-siempre-necesita-una-referencia)
- [4. La aritmética del decibelio](#4-la-aritmética-del-decibelio)
- [5. El ruido rosa y el ruido blanco](#5-el-ruido-rosa-y-el-ruido-blanco)
- [6. Cómo oímos: las curvas isofónicas](#6-cómo-oímos-las-curvas-isofónicas)
- [7. El margen audible y el enmascaramiento](#7-el-margen-audible-y-el-enmascaramiento)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Qué es el sonido y qué lo describe

**El sonido es una onda de presión que se propaga por un medio material.** **No hay sonido en el
vacío**, y **la onda no transporta materia: transporta una perturbación.**

**Las magnitudes que describen esa onda, y cómo se relacionan:**

| Magnitud | Qué es | Unidad |
|---|---|---|
| **Frecuencia** | **Cuántos ciclos por segundo** | **Hercio (Hz)** |
| **Periodo** | **Cuánto dura un ciclo**: es el inverso de la frecuencia | **Segundo (s)** |
| **Longitud de onda** | **Cuánto avanza la onda en un ciclo** | **Metro (m)** |
| **Amplitud** | **Cuánta presión** alcanza el pico | **Pascal (Pa)** |

**La relación que las une, y que hay que tener a mano en todo el temario**: **la longitud de onda es
la velocidad del sonido dividida entre la frecuencia.** **Con 340 metros por segundo, un tono de 340
hercios mide un metro; uno de 34 hercios, diez metros; y uno de 3.400, diez centímetros.**

**De ahí salen dos consecuencias que reaparecen en los temas de acústica y de micrófonos**: **los
graves son largos** —por eso atraviesan tabiques y no se dejan absorber por materiales finos— **y los
agudos son cortos** —por eso son direccionales y los detiene cualquier obstáculo—.

## 2. La unidad de presión sonora es LEGAL

**La unidad de presión de sonido en el Sistema Internacional se denomina pascal.** Ésa es la respuesta
oficial a la pregunta 89.

**Y no es convención de sector: está en el Boletín Oficial del Estado.** **El Real Decreto 2032/2009,
de 30 de diciembre, por el que se establecen las unidades legales de medida, la recoge en su cuadro de
unidades derivadas coherentes**, con las celdas separadas por puntos porque un cuadro no admite otro
entrecomillado y cada celda va literal:

> «presión, tensión» · «pascal» · «Pa» · «N/m2»

**Un pascal es un newton por metro cuadrado.** **Y el orden de magnitud es lo que hace falta entender:
el umbral de audición está en 20 micropascales** —veinte millonésimas de pascal— **y el umbral de
dolor, en torno a 20 pascales.** **Un millón de veces más.**

**Ese margen de un millón a uno es la razón de que el sonido no se mida en pascales sino en
decibelios**, y **las tres opciones falsas de la pregunta son tres unidades que miden otra cosa:**

| Opción | Qué mide de verdad |
|---|---|
| **Newton** | **Fuerza**, no presión: le falta dividir por la superficie |
| **Milibar** | **Presión**, sí, pero **no es unidad del Sistema Internacional**: el propio real decreto la recoge entre las ajenas al SI aceptadas, y **un bar son 100.000 pascales** |
| **W/cm²** | **Intensidad**: potencia por unidad de superficie, que es otra magnitud |

## 3. El decibelio, y por qué SIEMPRE necesita una referencia

**El decibelio también está en el real decreto**, en su cuadro de unidades ajenas al Sistema
Internacional cuyo uso se acepta, junto al belio y al neper. **Y la norma dice de él exactamente lo
que la pregunta 65 mide.**

**El apartado 4 del real decreto, en cita literal:**

> «La tabla 8 cita también las unidades de las magnitudes logarítmicas, el neper, el belio y el
> decibelio. Estas son unidades adimensionales y se emplean para proporcionar información sobre la
> naturaleza logarítmica del cociente de magnitudes.»

**Y su nota (i), que es la frase que ordena todo el uso del decibelio en audio:**

> «Cuando se usan estas unidades, es importante indicar cuál es la naturaleza de la magnitud en
> cuestión y el valor de referencia empleado.»

---

**De esa frase se sigue la regla que hay que llevarse del tema entero**: **un decibelio a secas no
significa nada.** **Un decibelio es siempre la relación entre una magnitud y una referencia**, y
**cambiar la referencia cambia el número.**

| Escala | Referencia | Dónde se usa |
|---|---|---|
| **dB SPL** | **20 micropascales**, el umbral de audición | **Presión sonora en el aire** |
| **dBu** | **0,775 voltios** | **Nivel de línea profesional** |
| **dBV** | **1 voltio** | **Nivel de línea de consumo** |
| **dBFS** | **La escala digital completa**: 0 es el máximo y todo lo demás es negativo | **Audio digital** |
| **dBm** | **1 milivatio** sobre una impedancia dada | **Potencia** |

**Y la pregunta 65**: **en la escala de decibelios se emplean como valores de referencia, en el aire, a
una temperatura de 20 grados centígrados.** Ésa es la respuesta oficial.

**Por qué la temperatura importa**: **porque la velocidad del sonido y la impedancia acústica del aire
dependen de ella.** **El valor de referencia de 20 micropascales está definido para aire a 20 grados
y a presión atmosférica normal**, y **fuera de esas condiciones la equivalencia entre presión y nivel
cambia.** **Es el mismo motivo por el que un instrumento de viento se desafina cuando el local está
frío.**

## 4. La aritmética del decibelio

**Dos preguntas del cuadernillo son cuentas de decibelios**, y **las dos se hacen con una sola tabla
en la cabeza.**

**Para magnitudes de AMPLITUD —tensión, presión sonora— la fórmula es 20 por el logaritmo decimal del
cociente.** **Para magnitudes de POTENCIA, es 10 por ese logaritmo.** **Ésa es la distinción que más
se falla.**

| Relación de amplitud | Diferencia en dB |
|---|---|
| **× 2** | **+6 dB** |
| **× 4** | **+12 dB** |
| **× 10** | **+20 dB** |
| **× 1,41** —raíz de dos— | **+3 dB** |

**La pregunta 90**: **la diferencia en decibelios entre una señal de 1 voltio y una de 2 voltios es de
6 dB.** Ésa es la respuesta oficial. **Veinte por el logaritmo decimal de dos son aproximadamente
seis.**

**La trampa está en la opción a), 3 dB**, **que es la respuesta correcta si la magnitud fuera
POTENCIA.** **Doblar la potencia son 3 dB; doblar la amplitud son 6.** **El enunciado dice
«amplitud», y por eso son 6.**

**La pregunta 94, que es la misma cuenta al revés**: **si el micrófono A capta 80 dB SPL y el B capta
74 dB SPL, la señal de A es aproximadamente 2 veces más fuerte en amplitud que la de B.** Ésa es la
respuesta oficial. **La diferencia es de 6 dB, y 6 dB de amplitud son un factor de dos.**

**Las tres opciones falsas —4, 6 y 8 veces— son las que salen de aplicar mal la escala**: **quien
divida 80 entre 74, quien tome los 6 dB como «seis veces» o quien use la fórmula de potencia acaba en
una de ellas.**

## 5. El ruido rosa y el ruido blanco

**En el ruido rosa la energía disminuye a medida que aumenta la frecuencia.** Ésa es la respuesta
oficial a la pregunta 50.

**Los dos ruidos de referencia, y qué los separa:**

| Ruido | Cómo reparte la energía | Cómo suena |
|---|---|---|
| **Blanco** | **La misma energía por HERCIO**: es plano por frecuencia | **Agudo, siseante** |
| **Rosa** ✔ | **La misma energía por OCTAVA**: cae 3 dB por octava | **Equilibrado, como una cascada** |

**Por qué el rosa cae y aun así se considera «plano»**: **porque cada octava tiene el doble de
hercios que la anterior.** **La octava de 100 a 200 Hz contiene 100 hercios; la de 1.000 a 2.000
contiene 1.000.** **Para que las dos tengan la misma energía total, la energía POR HERCIO tiene que
caer a la mitad**, y **eso son 3 dB por octava.**

**De ahí que el ruido rosa sea el que se usa para medir y ecualizar salas**: **el oído percibe por
octavas, y un analizador por bandas de octava lo ve horizontal.**

**Las tres opciones falsas:**

1. **«Caída de 6 dB por octava»** **es la del ruido marrón o browniano**, no la del rosa. **La cifra
   del rosa es 3.**
2. **«Es lineal porque tiene la misma energía en todas sus bandas»** **describe al ruido BLANCO** con
   la palabra «bandas» mal usada.
3. **«Se utiliza para enmascarar sonidos en entornos de trabajo»** **es un uso real** —del ruido de
   enmascaramiento en oficinas— **pero no es lo que el ruido rosa ES.** **La opción describe una
   aplicación, no una definición.**

## 6. Cómo oímos: las curvas isofónicas

**El conjunto de curvas que representan la sensibilidad del oído a diferentes frecuencias para todo el
margen audible son las curvas isofónicas.** Ésa es la respuesta oficial a la pregunta 55.

**Qué dicen**: **que el oído no es plano.** **Para que un tono de 50 hercios se perciba tan fuerte
como uno de 1.000, el de 50 tiene que sonar bastante más alto en presión.** **Cada curva une los
puntos que se perciben igual de fuertes**, y **la unidad de esa percepción es el fon.**

**Las tres consecuencias de oficio, que es lo que las hace útiles y no una curiosidad:**

1. **La sensibilidad cambia con el NIVEL.** **A volumen bajo el oído pierde graves y agudos; a volumen
   alto se aplana.** **Por eso una mezcla que suena bien fuerte se queda sin fondo al bajarla**, y por
   eso existe el botón *loudness* de los equipos domésticos.
2. **El oído es más sensible entre 2 y 5 kilohercios**, que **es la banda de la inteligibilidad de la
   voz.** **Ahí un decibelio de más se nota mucho más que en cualquier otro sitio.**
3. **Por eso las escalas de medida llevan ponderación**: **la curva A del sonómetro imita la respuesta
   del oído a nivel bajo**, y **es la que usa la normativa de ruido laboral.**

**Las tres opciones falsas son curvas reales de acústica y ninguna es ésta:**

| Opción | Qué es de verdad |
|---|---|
| **Curvas NC** | **Criterio de ruido de fondo**: fijan cuánto ruido se tolera en un recinto, por bandas de octava |
| **Curvas NR** | **Lo mismo, en la versión de la Organización Internacional de Normalización** |
| **Curva de Wegel** | **Una representación histórica del campo auditivo**, ligada a los mismos trabajos, pero **no es el conjunto de curvas que la pregunta describe** |

**La palabra que decide es «sensibilidad del oído»**: **NC y NR no describen el oído, describen cuánto
ruido admite una sala.**

## 7. El margen audible y el enmascaramiento

**El enunciado del anexo nombra el enmascaramiento y el examen no lo pregunta**, pero **el tema lo
desarrolla porque el programa lo pide y porque es lo que explica media docena de decisiones de
mezcla.**

**El margen audible del oído humano se sitúa convencionalmente entre 20 hercios y 20 kilohercios**, y
**se estrecha con la edad por el extremo agudo.**

**El enmascaramiento es el fenómeno por el que un sonido hace inaudible a otro.** **Sus tres reglas:**

1. **Un sonido enmascara mejor a los de frecuencia PRÓXIMA**, y **más hacia arriba que hacia abajo**:
   **un grave potente tapa a los medios; un agudo no tapa a los graves.**
2. **El enmascaramiento crece con el nivel del enmascarador.**
3. **Hay enmascaramiento TEMPORAL además del simultáneo**: **un sonido fuerte tapa a lo que viene
   inmediatamente después, y en menor medida a lo inmediatamente anterior.**

**Y es la base de la compresión con pérdida del tema 9**: **un códec que descarta lo que el oído no va
a oír necesita saber exactamente qué enmascara qué.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 50 | Qué es el ruido rosa | d) La energía disminuye al aumentar la frecuencia ✔ |
| 55 | Curvas de sensibilidad del oído por frecuencia | a) Curvas isofónicas ✔ |
| 65 | Temperatura de referencia de la escala de decibelios en el aire | c) 20 grados centígrados ✔ |
| 89 | Unidad de presión sonora del Sistema Internacional | d) Pascal ✔ **·** en el BOE |
| 90 | Diferencia en dB entre 1 y 2 voltios | b) 6 dB ✔ |
| 94 | Relación de amplitud entre 80 y 74 dB SPL | d) 2 veces ✔ |

**Las seis respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de estudio del tema**: **dos de las seis son la misma cuenta** —la 90 y la 94, las dos de
la relación entre decibelios y amplitud—. **Quien tenga clara la tabla del epígrafe 4 acierta las
dos, y con ella acierta también las de sonoridad del tema 14 y las de sensibilidad de altavoz del
tema 10.** **Es la tabla más rentable de la ocupación.**

## 9. Trazabilidad

**Este tema cita una norma del BOE.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** (`BOE-A-2010-927`), **en su redacción vigente el 21 de diciembre de 2022**: la fila del pascal, el apartado 4 sobre las unidades logarítmicas y su nota (i) | Preguntas 89 y, en parte, 65 |

**Cuatro declaraciones expresas:**

1. **La fila del pascal se cita celda a celda**, porque **un cuadro no admite entrecomillado corrido
   sin dejar de ser literal.** **El apartado 4 y la nota (i), en cambio, son citas corridas y van como
   tales.**
2. **El real decreto sostiene que el decibelio exige declarar su referencia; no sostiene la
   temperatura de 20 grados de la pregunta 65.** **Esa cifra es la condición en que están definidos
   los valores de referencia acústicos**, y **es convención de la acústica, no del real decreto.**
   **El temario separa las dos cosas en lugar de dar por normativo lo que no lo es.**
3. **El margen audible de 20 Hz a 20 kHz y las tres reglas del enmascaramiento son conocimiento
   asentado de la psicoacústica**, y **este proyecto no ha volcado ninguna fuente de esa disciplina.**
   **El tema los presenta como conocimiento común de la materia.**
4. **La curva de Wegel de la pregunta 55 no se ha podido contrastar en fuente.** **Lo que el tema
   sostiene es que las curvas isofónicas son la respuesta correcta y que NC y NR describen ruido de
   fondo de recinto y no sensibilidad del oído**, que **es lo que hace la pregunta contestable.**

**El resto del tema va como oficio y así se declara**: la relación entre frecuencia y longitud de
onda, la aritmética del decibelio y su doble fórmula, la diferencia entre ruido blanco y rosa y los
3 dB por octava, y las consecuencias de oficio de las curvas isofónicas. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
