# Cobertura · Ingeniería Superior · Telecomunicación, los veintisiete temas del específico

**Siglas de este informe**: la Corporación de Radio y Televisión Española (**RTVE**); la interfaz
digital serie (**SDI**); el protocolo de internet (**IP**); la prevención de riesgos laborales
(**PRL**); el conjunto redundante de discos independientes (**RAID**); la cinta lineal abierta
(**LTO**); el protocolo de tiempo de precisión (**PTP**); las especificaciones de red abierta para
medios (**NMOS**); la Organización Internacional de Normalización (**ISO**) y la Comisión
Electrotécnica Internacional (**IEC**), que publican juntas la familia **ISO/IEC 27000**; y la Ley
General de Comunicación Audiovisual (**LGCA**).

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y donde
el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

**Un solo cuadernillo sostiene este bloque**: `44_preguntas_ing_sup_teleco`, que sus instrucciones
describen como **96 preguntas —80 principales más 16 de reserva—**, con su plantilla completa,
fechada el **05/02/2025**. De ellas, **86 son del específico y 10 del bloque común**: la 26, la 30, la
38, la 52, la 56, la 72, la 85 y la 88 de la Constitución, y la 27 y la 49 del III Convenio
Colectivo. **Las 86 están repartidas y no queda ninguna sin clasificar.**

**Una particularidad que conviene decir de entrada**: **ninguna de las noventa y seis preguntas es de
prevención de riesgos laborales.** **Es el único cuadernillo del proyecto en que ese bloque no ha dado
ni una**, y **el tema compartido de prevención se incluye igual, porque el punto 29 del anexo lo
pide.**

**Y una sobre la clasificación**: **la pregunta 38 no la coge ninguna palabra clave del clasificador
general** —«Las Fuerzas Armadas están constituidas por…», sin nombrar la Constitución ni ningún
artículo—, así que **va a mano en `banco/reclasificadas.tsv`**, al tema 1 del general, **con su motivo
escrito.**

**Una advertencia sobre la fuente**: **el PDF del cuadernillo trae la fuente incrustada sin tabla de
caracteres**, de modo que su texto se extrae como glifos numerados y no como letras. **El texto se ha
leído de la transcripción por reconocimiento óptico que está al lado.** **La plantilla, en cambio, sí
se lee por coordenadas**: se ha extraído emparejando el número de la izquierda con la letra de su
misma fila, y **sus 96 respuestas salen enteras, sin huecos, sin duplicados y sin una sola
anotación.**

## Por qué veintisiete temas y no veintinueve

**El anexo tiene veintinueve puntos.** **El 29 es el de prevención de riesgos laborales**, que este
proyecto escribe una sola vez y comparten veinte ocupaciones. **De los veintiocho restantes salen
veintiséis temas, y la única unión está razonada:**

| Temas unidos | Puntos del anexo | Por qué |
|---|---|---|
| **Tema 13** | **13, 14 y 15** | **Los tres enunciados son la misma frase con el nombre de la sala cambiado**: estudio, continuidades y controles técnicos, cada uno con «equipamiento, diagrama a bloques, interconexión y sincronización» |

**El criterio es el del método**: **separarlos daría tres temas que se repetirían entre sí**, y **eso
es lo que el proyecto prohíbe.**

## Los siete temas compartidos con Ingeniería Técnica · Telecomunicación

**Siete puntos de este anexo son, palabra por palabra, siete puntos del anexo de Ingeniería Técnica ·
Telecomunicación**, y **la comprobación se ha hecho carácter a carácter sobre los dos ficheros de
bases, normalizando sólo los espacios y los guiones que el PDF reparte como quiere:**

| Punto de este anexo | Punto del de Ing. Técnica | Tema que se comparte |
|---|---|---|
| **1** | **1** | **Marco regulatorio de las telecomunicaciones** |
| **2** | **2** | **La señal y la conversión analógico-digital** |
| **22** | **19** | **Comunicaciones y redes** |
| **24** | **17** | **Radio digital** |
| **25** | **18** | **Antenas, transmisores y propagación** |
| **26** | **20** | **Ingeniería de implantación** |
| **28** | **23** | **Protección de datos personales** |

**Y una precisión que hay que dar en lugar de afirmar una identidad exacta que no lo es**: **en el
punto 25 sólo cambia un signo de puntuación** —donde un anexo pone punto, el otro pone dos puntos—.
**Las palabras son las mismas y en el mismo orden**, y **el temario lo dice así.**

**La consecuencia de método, y es la que importa**: **el tema se escribe UNA sola vez y sirve a las
dos ocupaciones**, como el de prevención. **Escribir dos temas casi iguales es garantizar que se
separen a la primera corrección**, que es exactamente lo que este proyecto evita compartiendo el
fichero.

**Y la consecuencia de mantenimiento**: **al entrar esta ocupación, la CABECERA de esos siete temas
había que reescribirla, no sólo su cuerpo.** **Un cuerpo correcto con una cabecera vieja publica una
afirmación falsa en los dos volúmenes a la vez.** **Los siete declaran ahora, en su ficha y en su
primer párrafo, que sirven a las dos ocupaciones.**

## El reparto

| Tema | Puntos del anexo | Materia | Preguntas |
|---|---|---|---:|
| 1 | 1 | Marco regulatorio de las telecomunicaciones *(compartido)* | **0** |
| 2 | 2 | La señal y la conversión analógico-digital *(compartido)* | **0** |
| 3 | 3 | La transmisión: canal, modulación y multiplexado | 3 |
| 4 | 4 | Medios de transmisión, conectores y compresión | 6 |
| 5 | 5 | La señal de televisión | 3 |
| 6 | 6 | Televisión digital: codificación y compresión | 5 |
| 7 | 7 | La televisión digital terrestre | 1 |
| 8 | 8 | Alta y ultraalta definición: estándares | **11** |
| 9 | 9 | Comunicaciones y radiodifusión por satélite | 1 |
| 10 | 10 | Voz, imagen, multimedia y difusión en flujo | 1 |
| 11 | 11 | Producción I: cámaras, conmutación, grabación y edición | 4 |
| 12 | 12 | Producción II: sonido, iluminación, medida y auxiliares | 4 |
| 13 | 13, 14 y 15 | Las salas: estudio, continuidad y controles técnicos | 5 |
| 14 | 16 | Sistemas de redacción e informativos | **0** |
| 15 | 17 | Postproducción de vídeo y audio | 1 |
| 16 | 18 | Grafismo electrónico y escenografía virtual | **0** |
| 17 | 19 | Sistemas radiantes y radiocomunicaciones | 5 |
| 18 | 20 | Almacenamiento de datos y servidores | 4 |
| 19 | 21 | Producción audiovisual sobre infraestructura de red | **11** |
| 20 | 22 | Comunicaciones y redes *(compartido)* | **13** |
| 21 | 23 | Sonido | 7 |
| 22 | 24 | Radio digital *(compartido)* | **0** |
| 23 | 25 | Antenas y transmisores de radiodifusión *(compartido)* | **0** |
| 24 | 26 | Ingeniería de implantación *(compartido)* | 1 |
| 25 | 27 | Seguridad en tecnologías de la información | **0** |
| 26 | 28 | Protección de datos personales *(compartido)* | **0** |
| **PRL** | **29** | **Prevención en el temario específico** | **compartido** |

## El desequilibrio

**Por arriba**: **tres puntos se llevan 35 de las 86 preguntas**, el **41 %** del examen específico.
**Las comunicaciones y redes, trece**; **la producción sobre infraestructura de red, once**; **la alta
y ultraalta definición, otras once.**

**Por abajo**: **ocho de los veintinueve puntos del anexo no se llevan ninguna**: el 1, el 2, el 16,
el 18, el 24, el 25, el 27 y el 28, más el 29 de prevención, que no ha dado ni una en este
cuadernillo.

**La lectura de estudio que sale de ahí**: **quien domine el direccionamiento y los protocolos de red,
la familia de normas de producción sobre red con su reloj repartido, y el rango dinámico y la gama de
color de la ultraalta definición tiene contestado más del 40 % del examen.** **Y son las tres materias
sobre las que se está contratando ahora mismo en las casas de televisión**, lo que las hace rentables
dos veces.

## Los ocho puntos a cero, y por qué se escriben igual

| Tema | Por qué se escribe igual |
|---|---|
| **1 · Marco regulatorio** | **Compartido.** En la otra ocupación dio dos preguntas, y su tema está verificado allí |
| **2 · La señal y su conversión** | **Compartido.** En la otra ocupación dio tres preguntas, y con dos reglas se contestan las tres |
| **14 · Sistemas de redacción e informativos** | **Es la pieza más integrada de una casa y la más difícil de cambiar**: habla con el almacenamiento, la edición, el grafismo, la emisión y el archivo |
| **16 · Grafismo y escenografía virtual** | **La calidad de una incrustación la decide el submuestreo de color, no el programa**, y eso es una decisión de ingeniería, no de diseño |
| **22 · Radio digital** | **Compartido.** Tampoco cayó en la otra ocupación: es el único punto de los dos anexos dedicado enteramente a la radio, en una corporación que tiene la mitad de su nombre ahí |
| **23 · Antenas y transmisores de radiodifusión** | **Compartido.** En la otra ocupación dio tres preguntas. Aquí el punto 19 se lleva los parámetros y la propagación, y éste las líneas, las guías, los transmisores y la medida |
| **25 · Seguridad en tecnologías de la información** | **Su enunciado NO es el mismo que el de la otra ocupación**: aquél dice «Normativa ISO/IEC 27001» y éste «Normativas ISO/IEC 27000-series». Por eso el tema no se comparte |
| **26 · Protección de datos personales** | **Compartido.** Decide dónde se puede colgar una cámara, dónde no un micrófono, cuánto se guarda una grabación y qué va en el pliego |

**El principio del método es el mismo de siempre**: **el temario se escribe contra el PROGRAMA, no
contra el examen.** **Que un punto no haya caído no dice que no vaya a caer.**

## El único punto de este específico con norma del boletín

**El punto 23 —Sonido— cierra su enunciado con «Regulación básica de la radiodifusión sonora en
España»**, y **eso es el título IV de la Ley 13/2022, de 7 de julio, General de Comunicación
Audiovisual.** **Es el único punto de todo el temario específico de esta ocupación que se apoya en una
norma publicada en el Boletín Oficial del Estado**, y **su tema la cita literalmente**: **los apartados
3 y 4 del artículo 76, el 77.1, el 78.2, el 80.4 y el 83.3.**

**El punto 27 tiene además una norma que su enunciado no nombra**: **el Esquema Nacional de Seguridad,
aprobado por el Real Decreto 311/2022**, que **sí está en el boletín y sí obliga a una corporación
pública.** **Su tema lo cita literalmente** —el artículo 1.2, el 2.1 y 2.3, el 5, el 9 y el 11.1 y
11.2— **mientras declara que las normas privadas que el enunciado sí nombra están tras muro de pago y
no se han consultado.**

## Las cinco preguntas que dependen de una figura

| Nº | De qué depende |
|---|---|
| **15** | **Una fotografía de un conversor** |
| **22** | **Una fotografía de un panel de conexiones** |
| **37** | **Un esquema de puestos técnicos y estaciones de trabajo** |
| **68** | **Una fotografía de un conector de fibra óptica** |
| **76** | **Una fotografía de un conector de bus serie** |

**Lo que este temario hace con ellas, y va declarado una a una en el apéndice de respuestas**: **no
describe lo que no ha visto.** **La respuesta descansa en la plantilla oficial**, y **lo que el tema
aporta es la REGLA DE LA FAMILIA**: cómo se reconoce un conector de fibra por su cuerpo, un multipolar
por su carcasa y uno de bus por su sección. **La del esquema es la excepción**: **la palabra que la
resuelve está en el texto** —«cualquiera de las estaciones»—, **y el tema la razona sin necesitar el
dibujo.**

## La pregunta con una opción ilegible

**La 91**, sobre el transporte que admite una de las interfaces de descubrimiento y control de medios,
**trae su tercera opción corrompida en la transcripción óptica.** **No es un error del examen: es de
la transcripción**, y **va declarado.** **La respuesta oficial no se ve afectada**, y el tema la razona
por lo que esa interfaz hace.

## Conclusión

**Los veintisiete temas cubren los veintinueve puntos del anexo** —diecinueve propios, siete
compartidos con Ingeniería Técnica · Telecomunicación y el de prevención—, **las ochenta y seis
preguntas del específico están repartidas y contestadas**, **las cinco que dependen de una figura y la
que llega con una opción ilegible van declaradas una a una**, y **ninguna respuesta oficial de este
bloque está mal.** **El bloque está al 100 %.**
