# Esquema · Tema 16 del específico de Ingeniería Superior · Telecomunicación · Grafismo electrónico y escenografía virtual

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de grafismo y escenografía ·
`[plan]` = enunciado del propio anexo. **Siglas**: los submuestreos **4:2:2**, **4:2:0** y **4:4:4**,
que se leen en el tema 5.

**Cabecera.** Enunciado: punto 18 del anexo · **cero preguntas** · **sin norma del boletín** · **se
escribe igual, contra el programa.**

**La idea que lo ordena** · `[of]` · **La calidad de una incrustación la decide el SUBMUESTREO de
color, no el programa.** **Sobre material con la crominancia dividida por dos en las dos direcciones,
la máscara tiene la mitad de resolución en cada una**, y **eso se ve en los bordes como escalones que
ningún ajuste posterior arregla.**

<!-- indice -->

## Índice

- [La composición](#la-composición)
- [El grafismo](#el-grafismo)
- [La escenografía virtual](#la-escenografía-virtual)
- [La integración](#la-integración)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La composición

- **el concepto de partida** · `[of]` · **El CANAL ALFA**: **además del color, un cuarto canal que dice
  para cada píxel cuánto tapa a lo que hay debajo.**

| Tipo de incrustación | De dónde saca la transparencia |
|---|---|
| **clave de luminancia** | **del brillo de la propia imagen**: lo oscuro deja pasar |
| **clave lineal** | **de un canal alfa que viene aparte**: es la buena para grafismo |
| **clave de croma** | **del color**: un fondo de un color determinado se sustituye |

- **LA REGLA APRENDIDA** · `[of]` · **Un rótulo bien hecho se incrusta con clave LINEAL.** **La lineal
  respeta bordes suaves y transparencias parciales; la de luminancia recorta duro.** **Por eso el
  generador de rótulos entrega DOS señales: la imagen y su alfa.**

| Requisito de la incrustación por color | Por qué |
|---|---|
| **fondo saturado y uniforme** | **si el fondo varía, la máscara varía** |
| **iluminación del fondo separada de la del sujeto** | **para poder ajustar cada una** |
| **separación física entre sujeto y fondo** | **evita el derrame de color** |
| **submuestreo alto** | **4:2:2 como mínimo, 4:4:4 mejor** |
| **nada del color del fondo encima del sujeto** | **desaparece** |

## El grafismo

| Función | Qué es |
|---|---|
| **diseño** | **crear las plantillas: tipografía, color, animación, retícula** |
| **datos** | **rellenarlas, a mano o desde una fuente** |
| **reproducción** | **sacarlas en el instante justo, con su alfa** |
| **control** | **decidir qué sale y cuándo** |

| Elemento | Qué es |
|---|---|
| **la mosca** | **el identificador de canal, permanente** |
| **rótulo de identificación** | **quién habla: nombre y cargo** |
| **faldón** | **titulares y bandas de información** |
| **cintillo** | **texto que se desplaza** |
| **marcador** | **resultado y tiempo de una competición** |
| **infografía** | **datos representados: mapas, gráficos, comparativas** |
| **cortinilla y careta** | **transiciones e identidad de programa** |
| **realidad aumentada** | **elementos tridimensionales integrados en la escena real** |

| Parámetro que decide un ingeniero | Qué decide |
|---|---|
| **formato y espacio de color** | **que el grafismo case con la señal** |
| **zona segura de título** | **que el texto no se corte** |
| **legibilidad** | **cuerpo de letra y contraste para la peor pantalla** |
| **duración en pantalla** | **tiempo de lectura, no de gusto** |
| **latencia del sistema** | **cuánto tarda desde la orden hasta que sale** |

- **las dos reglas de oficio** · `[of]` · **1)** el grafismo se diseña **para la PEOR pantalla**: **un
  rótulo fino que se lee en un monitor de referencia desaparece en un televisor pequeño con brillo
  alto**, y **eso es lo que ve la mayoría del público.** **2)** la latencia **se mide y se compensa
  retardando la otra señal**, no adivinando.

## La escenografía virtual

| Pieza | Qué hace |
|---|---|
| **plató de croma** | **el fondo que se va a sustituir, iluminado uniforme** |
| **motor de renderizado en tiempo real** | **genera el decorado cuadro a cuadro** |
| **seguimiento de cámara** | **le dice al motor DÓNDE está la cámara y cómo mira** |

- **por qué la tercera es la clave** · `[of]` · **Sin seguimiento, el decorado virtual es un fondo
  plano.** **En cuanto la cámara se mueve o hace zum, el fondo tiene que moverse con la perspectiva
  correcta.**
- **los datos que el seguimiento entrega** · `[of]` · **giro horizontal, inclinación, balanceo, las
  tres coordenadas de posición, la focal y el enfoque.** **Con menos, la integración se rompe en cuanto
  la cámara deja de estar quieta.**
- **las dos exigencias temporales** · `[of]` · **1)** el decorado se genera **en tiempo real, un cuadro
  por cadencia sin fallar ninguno**; **2)** hay que **alinear los retardos**: **la señal de cámara se
  retarda lo mismo que tardan el motor y el seguimiento**, y **un desajuste de un solo cuadro se ve
  como si el decorado flotara.**

| | **Croma** | **Pared de paneles** |
|---|---|---|
| **Dónde se compone** | **en el control, después de la cámara** | **en el plató, delante de la cámara** |
| **Iluminación del sujeto** | **hay que imitarla** | **la da el propio fondo: reflejos y luz correctos** |
| **Lo que ve el intérprete** | **un fondo verde** | **el decorado** |
| **Derrame de color** | **el problema clásico** | **no existe** |
| **Su problema propio** | **máscara y submuestreo** | **batido entre la trama de paneles y el sensor, y el ángulo de visión** |

## La integración

| Con quién | Para qué |
|---|---|
| **sistema de redacción** | **el rótulo sale de la escaleta, no se teclea dos veces: tema 14** |
| **bases de datos externas** | **resultados, elecciones, meteorología: el dato entra solo** |
| **mezclador y automatización** | **quién dispara el gráfico: tema 13** |
| **postproducción** | **elementos con alfa para composiciones: tema 15** |
| **almacenamiento** | **plantillas, fuentes tipográficas y elementos: tema 18** |

- **las tres reglas de integración** · `[of]` · **1) un dato se teclea UNA vez**: si el nombre de un
  invitado se escribe en dos sitios, **algún día no coincidirán, y coincidirá en directo.** **2) las
  plantillas son del programa, no del operador**: **un grafismo hecho a mano cada día se desvía y la
  identidad del canal se deshace sin que nadie lo decida.** **3) lo automático necesita un CAMINO
  MANUAL**: **cuando la base de datos externa falla —y falla en una noche electoral—, tiene que poder
  teclearse.**

## Lo que se ha preguntado

**Ninguna pregunta.** **Lo razonablemente preguntable**: **los tres tipos de incrustación y por qué el
rótulo va con clave lineal**, **los requisitos de una incrustación por color**, **las tres piezas de la
escenografía virtual y por qué el seguimiento es la clave**, y **la diferencia entre componer en el
control y componer en el plató.**
