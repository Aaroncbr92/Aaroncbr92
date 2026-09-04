# Tema 16 del específico de Ingeniería Superior · Telecomunicación · Grafismo electrónico y escenografía virtual

Las siglas y símbolos de este tema, presentados de entrada: el canal de transparencia (**alfa**); la
incrustación por color (**croma**); la clave lineal y la clave de luminancia; el seguimiento de cámara
(**tracking**); la realidad aumentada (**RA**); la unidad de proceso gráfico (**GPU**); la imagen
generada por ordenador (**CGI**); el diodo emisor de luz (**LED**); la interfaz digital en serie
(**SDI**); el sistema de gestión de redacción (**NRCS**) y su protocolo hacia los dispositivos de
producción (**MOS**); el fotograma por segundo (**c/s**); y el milisegundo (**ms**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 18):
> «Elementos de producción (VIII): Grafismo electrónico. Equipos, sistemas, parámetros, funciones y
> procesos. Escenografía virtual.»

**Es el último de los ocho puntos de elementos de producción y el que más ha cambiado en veinte años**,
y **hay que decir en qué**: **el grafismo pasó de ser un generador de rótulos a ser un MOTOR DE
TIEMPO REAL**, y **con ese cambio se llevó por delante la frontera entre el decorado y la imagen.**

**Y la idea que ordena el punto**: **todo lo que este tema describe es lo mismo visto a distintas
escalas**: **componer una imagen sobre otra en el instante justo.** **Un rótulo, una incrustación por
color y un decorado virtual son el mismo problema —qué píxel viene de dónde— resuelto con más o menos
información.**

**Este punto NO ha dado ni una pregunta en el cuadernillo de esta ocupación**, y **eso se declara**:
**el cero de un punto no significa que no vaya a caer.**

<!-- indice -->
<!-- /indice -->

## 1. La composición: cómo se mezclan dos imágenes

**El concepto de partida y el que sostiene todo lo demás**: **el CANAL ALFA.** **Además de los tres
componentes de color, una imagen puede llevar un cuarto canal que dice, para cada píxel, CUÁNTO tapa a
lo que hay debajo.**

**Los tres tipos de incrustación que hay que distinguir:**

| Tipo | De dónde saca la transparencia |
|---|---|
| **Clave de LUMINANCIA** | **Del brillo de la propia imagen**: lo oscuro deja pasar |
| **Clave LINEAL** | **De un canal alfa que viene aparte**: es la buena para grafismo |
| **Clave de CROMA** | **Del color**: un fondo de un color determinado se sustituye |

**Y la regla que hay que llevar aprendida**: **un rótulo bien hecho se incrusta con clave LINEAL, no
con clave de luminancia.** **La lineal respeta los bordes suaves y las transparencias parciales; la de
luminancia recorta duro y ensucia los antialiasing.** **Por eso el generador de rótulos entrega dos
señales: la imagen y su alfa.**

**La incrustación por color, con lo que hay que saber de ella:**

| Requisito | Por qué |
|---|---|
| **Fondo de color SATURADO y UNIFORME** | **El sistema separa por color**: si el fondo varía, la máscara varía |
| **Iluminación del fondo SEPARADA de la del sujeto** | **Para poder ajustar cada una** |
| **SEPARACIÓN física entre sujeto y fondo** | **Evita el derrame de color** sobre el sujeto |
| **Submuestreo alto** | **4:2:2 como mínimo, 4:4:4 mejor**: es lo del tema 5 |
| **Sin ropa del color del fondo** | **Lo que sea del color del fondo desaparece** |

**Y el aviso que enlaza con el tema 5 y que un ingeniero tiene que dar**: **la calidad de una
incrustación la decide el SUBMUESTREO de color, no el programa.** **Sobre material 4:2:0 la máscara
tiene la mitad de resolución en las dos direcciones**, y **eso se ve en los bordes como escalones.**
**Ningún ajuste posterior lo arregla.**

## 2. El grafismo: equipos, funciones y procesos

**Qué hace un sistema de grafismo, en cuatro funciones:**

| Función | Qué es |
|---|---|
| **DISEÑO** | **Crear las plantillas**: tipografía, color, animación, retícula |
| **DATOS** | **Rellenar esas plantillas** con contenido, a mano o desde una fuente |
| **REPRODUCCIÓN** | **Sacarlas en el instante justo**, con su alfa |
| **CONTROL** | **Decidir qué sale y cuándo**: manual, desde la escaleta o desde una automatización |

**Los tipos de elemento gráfico, que es el vocabulario del punto:**

| Elemento | Qué es |
|---|---|
| **La mosca** | **El identificador de canal**, permanente |
| **RÓTULO de identificación** | **Quién habla**: nombre y cargo |
| **FALDÓN o banda inferior** | **Titulares y bandas de información** |
| **CINTILLO o teletipo** | **Texto que se desplaza** |
| **MARCADOR** | **Resultado y tiempo** de una competición |
| **INFOGRAFÍA** | **Datos representados**: mapas, gráficos, comparativas |
| **CORTINILLA y careta** | **Transiciones e identidad de programa** |
| **Realidad AUMENTADA** | **Elementos tridimensionales integrados en la escena real** |

**Los parámetros que decide un ingeniero, y que el enunciado pide expresamente:**

| Parámetro | Qué decide |
|---|---|
| **Formato y espacio de color** | **Que el grafismo case con la señal**: mismo formato, misma curva |
| **Zona SEGURA de título** | **Que el texto no se corte** en pantallas que recortan |
| **Legibilidad** | **Cuerpo de letra y contraste** suficientes para la peor pantalla |
| **Duración en pantalla** | **Tiempo de lectura**, no de gusto |
| **LATENCIA del sistema** | **Cuánto tarda desde la orden hasta que sale**, y si hay que compensarla |
| **Alfa asociada o separada** | Cómo entrega la transparencia |

**Y las dos reglas de oficio que un examen puede pedir razonadas:**

1. **El grafismo se diseña para la PEOR pantalla, no para el monitor de la sala.** **Un rótulo fino y
   de bajo contraste que se lee perfectamente en un monitor de referencia desaparece en un televisor
   pequeño con brillo alto**, y **eso es lo que ve la mayoría del público.**
2. **La latencia del grafismo hay que MEDIRLA y compensarla.** **Un sistema que tarda unos cuadros en
   sacar el rótulo desincroniza la entrada con lo que dice el presentador**, y **la compensación se
   hace retardando la otra señal, no adivinando.**

## 3. La escenografía virtual

**Qué es**: **sustituir el decorado por una imagen generada, manteniendo la coherencia con el
movimiento de la cámara.**

**Las tres piezas que la hacen posible, y hay que saber que sin la tercera no funciona:**

| Pieza | Qué hace |
|---|---|
| **PLATÓ de croma** | **El fondo que se va a sustituir**, iluminado uniforme |
| **MOTOR de renderizado en tiempo real** | **Genera el decorado virtual cuadro a cuadro** |
| **SEGUIMIENTO de cámara** | **Le dice al motor DÓNDE está la cámara y cómo mira** |

**Y por qué la tercera es la clave**: **sin seguimiento, el decorado virtual es un fondo plano.** **En
cuanto la cámara se mueve o hace zum, el fondo tiene que moverse con la perspectiva correcta**, y **eso
exige conocer en cada cuadro la posición, la orientación, la focal y el foco de la cámara.**

**Los datos que el seguimiento tiene que entregar, que es la respuesta técnica del epígrafe**: **giro
horizontal, inclinación, balanceo, las tres coordenadas de posición, la focal y el enfoque.** **Con
menos de eso, la integración se rompe en cuanto la cámara deja de estar quieta.**

**Las tecnologías de seguimiento, por dónde sacan esos datos:**

| Tecnología | Cómo funciona |
|---|---|
| **CODIFICADORES en el soporte** | **Sensores en la cabeza, el pedestal y la óptica**: miden lo que se mueve |
| **Marcas ÓPTICAS en el techo o en el fondo** | **Una cámara auxiliar reconoce marcas** y deduce la posición |
| **Reconocimiento del PROPIO ESCENARIO** | Sin marcas, por características de la imagen |
| **Sistemas INERCIALES y mixtos** | Combinan sensores para ganar robustez |

**Y las dos exigencias temporales que hacen difícil todo esto:**

1. **El decorado se genera EN TIEMPO REAL.** **Un cuadro por cadencia, sin fallar ninguno**, y **una
   caída de rendimiento se ve como un tirón.**
2. **Hay que ALINEAR los retardos.** **El motor tarda en renderizar y el seguimiento en medir**, así
   que **la señal de cámara se RETARDA lo mismo para que fondo y figura correspondan al mismo
   instante.** **Un desajuste de un solo cuadro se ve como si el decorado flotara.**

**Y la evolución que hay que nombrar, porque cambia el planteamiento**: **el fondo de paneles de diodos
emisores de luz.** **En vez de sustituir un croma en la mesa de mezclas, se PROYECTA el decorado
virtual en una pared de paneles detrás de los intérpretes**, y **la cámara lo graba de verdad.**

| | **Croma** | **Pared de paneles** |
|---|---|---|
| **Dónde se compone** | **En el control**, después de la cámara | **En el plató**, delante de la cámara |
| **Iluminación del sujeto** | **Hay que imitarla** para que case con el fondo | **La da el propio fondo**: reflejos y luz correctos |
| **Lo que ve el intérprete** | **Un fondo verde** | **El decorado** |
| **Derrame de color** | **Es el problema clásico** | **No existe** |
| **Su problema propio** | Máscara y submuestreo | **Batido entre la trama de paneles y el sensor**, y el ángulo de visión |

## 4. La integración con el resto de la casa

**Con quién habla el grafismo, que es lo que un ingeniero tiene que resolver:**

| Con quién | Para qué |
|---|---|
| **Sistema de REDACCIÓN** | **El rótulo sale de la escaleta**, no se teclea dos veces: tema 14 |
| **Bases de datos externas** | **Resultados, elecciones, meteorología, mercados**: el dato entra solo |
| **Mezclador y automatización** | **Quién dispara el gráfico**: tema 13 |
| **Postproducción** | **Elementos con alfa** para composiciones: tema 15 |
| **Almacenamiento** | Plantillas, fuentes tipográficas y elementos: tema 18 |

**Y las tres reglas de integración que este temario declara como oficio:**

1. **Un dato se teclea UNA vez.** **Si el nombre de un invitado se escribe en la escaleta y otra vez
   en el grafismo, algún día no coincidirán**, y **coincidirá en directo.**
2. **Las PLANTILLAS son del programa, no del operador.** **Un grafismo hecho a mano cada día se
   desvía**, y **la identidad visual del canal se deshace sin que nadie lo decida.**
3. **Lo automático necesita un CAMINO MANUAL.** **Cuando la base de datos externa falla —y falla en
   una noche electoral—, tiene que poder teclearse.** **Un sistema sin ese camino deja la pantalla en
   blanco.**

## 5. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este punto NO ha dado ni una pregunta en el cuadernillo de esta ocupación**, y **el tema lo dice
   en su cabecera.** **El informe de cobertura reúne los siete puntos que están en esa situación.**
2. **Este tema NO nombra ningún sistema de grafismo, ningún motor de tiempo real, ningún fabricante de
   paneles y ningún producto.** **Un nombre propio obliga a una fuente**, y **el punto pide equipos,
   sistemas, parámetros, funciones y procesos**, que **es lo que el tema desarrolla.**
3. **Este tema NO da ninguna cifra de zona segura, ningún cuerpo de letra mínimo, ninguna latencia en
   cuadros, ninguna cadencia de renderizado y ningún paso de panel.** **Son dato de recomendación y de
   fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.** **Lo que el temario da
   es qué parámetro hay que fijar y por qué.**
4. **La lista de datos que debe entregar un sistema de seguimiento de cámara —los tres giros, las tres
   posiciones, la focal y el enfoque— es OFICIO declarado**, y **el temario no la atribuye a ninguna
   especificación.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **el
   submuestreo de color, al tema 5**; **la conmutación y el mezclador, al tema 11**; **las salas y la
   automatización, al tema 13**; **la escaleta, al tema 14**; **la composición de postproducción, al
   tema 15**; **y el almacenamiento, al tema 18.**

**El resto del tema va como oficio y así se declara**: la lectura de que el grafismo pasó de generador
de rótulos a motor de tiempo real y de que con ello se llevó la frontera entre decorado e imagen, la
idea de que rótulo, croma y decorado virtual son el mismo problema a distintas escalas, la regla de que
un rótulo se incrusta con clave lineal y no de luminancia, los cinco requisitos de una incrustación por
color, el aviso de que la calidad de la máscara la decide el submuestreo y no el programa, los seis
parámetros que decide un ingeniero, las dos reglas sobre diseñar para la peor pantalla y sobre medir y
compensar la latencia, la explicación de por qué el seguimiento de cámara es la pieza clave y qué datos
tiene que entregar, las dos exigencias temporales del tiempo real y de la alineación de retardos, la
comparación entre croma y pared de paneles con sus problemas propios, y las tres reglas de integración
sobre teclear una vez, las plantillas del programa y el camino manual. **Nada de eso está en un boletín
oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como si lo
estuviera.
