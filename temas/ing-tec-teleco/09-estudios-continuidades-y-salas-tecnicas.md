# Tema 9 del específico de Ingeniería Técnica · Telecomunicación · Estudios, continuidades y salas técnicas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · puntos 11, 12 y 13 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la arquitectura de las salas de una televisión, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Tres puntos a cero** | **El mayor bloque sin preguntas de la ocupación.** Lo que piden es saber DIBUJAR una instalación, y **eso es lo que un examen escrito no sabe preguntar bien** |
| **Extensión** | **1.836 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la interfaz digital serie (**SDI**) del tema 3; el
protocolo de internet (**IP**); el sistema de alimentación ininterrumpida (**SAI**); la calefacción,
ventilación y aire acondicionado (**HVAC**, como lo abrevia el sector); el protocolo de tiempo de
precisión (**PTP**) del tema 7; y el multiplexado digital de iluminación (**DMX512**) del tema 8.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, puntos 11, 12 y 13):
> «11. Estudios de televisión: Equipamiento. Diagrama a bloques. Interconexión. Sincronización y
> Referencia.»
>
> «12. Continuidades: Equipamiento. Diagrama a bloques. Interconexión. Sincronización y Referencia»
>
> «13. Controles técnicos y salas técnicas: Equipamiento. Diagrama a bloques. Interconexión.»

**Cero preguntas.** **Estos tres puntos del anexo no han dado ni una en el cuadernillo**, y **los temas
se escriben igual, contra el programa.**

**Este tema reúne los tres porque sus enunciados son la misma frase con el nombre de la sala
cambiado**: **«equipamiento, diagrama a bloques, interconexión, sincronización y referencia».**
**Separarlos daría tres temas que se repetirían entre sí**, que es lo que el método de este proyecto
prohíbe.

**Y hay una razón para no despachar los tres deprisa**: **son la mitad práctica del oficio.** **Lo que
estos puntos piden es saber DIBUJAR una instalación**, y **eso es exactamente lo que un examen escrito
no sabe preguntar bien.** **Que no haya caído nada no significa que no vaya a caer: significa que el
redactor del examen no encontró la manera.**

<!-- indice -->

## Índice

- [1. Lo que las tres salas tienen en común](#1-lo-que-las-tres-salas-tienen-en-común)
- [2. El estudio y su control](#2-el-estudio-y-su-control)
- [3. La continuidad](#3-la-continuidad)
- [4. Los controles y las salas técnicas](#4-los-controles-y-las-salas-técnicas)
- [5. La sincronización y la referencia](#5-la-sincronización-y-la-referencia)
- [6. Lo que el examen ha preguntado](#6-lo-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Lo que las tres salas tienen en común

**El enunciado repite cinco palabras tres veces, y ésas cinco son el esqueleto de cualquiera de las
tres:**

| Palabra del enunciado | Qué hay que saber decir |
|---|---|
| **Equipamiento** | **Qué aparatos hay y para qué está cada uno** |
| **Diagrama a bloques** | **Cómo se dibujan y en qué orden va la señal** |
| **Interconexión** | **Qué conecta con qué, y por qué medio** |
| **Sincronización** | **De dónde sale el tiempo** |
| **Referencia** | **Contra qué se mide y se ajusta** |

**Y las cinco capas que atraviesan cualquier sala técnica, que es el orden en que se diseña:**

| Capa | Qué resuelve |
|---|---|
| **Alimentación** | **Corriente, con respaldo y con protección diferencial** |
| **Climatización** | **Sacar el calor que el equipo genera** |
| **Señal** | **Vídeo y audio, por matriz o por red** |
| **Sincronización** | **La referencia común de tiempo** |
| **Control y datos** | **La red que configura, supervisa y ordena** |

**El principio de diseño que ordena las cinco y que un examen puede pedir**: **cada capa se diseña
para que su fallo no arrastre a las demás.** **Una sala bien hecha aguanta un corte de red de datos
sin perder la señal, y un fallo de climatización sin perder la alimentación.**

## 2. El estudio y su control

**Un estudio de televisión son dos espacios**, y **el enunciado los da por sabidos:**

| Espacio | Qué hay |
|---|---|
| **El plató** | **Cámaras, iluminación, escenografía, sonido de escena, monitores de retorno** |
| **El control** | **Realización, sonido, iluminación y, a veces, grafismo** |

**El diagrama a bloques de un control de realización, en el orden en que va la señal:**

1. **Las cámaras entran por sus unidades de control**, que es donde se ajustan.
2. **Las señales pasan por una matriz** o por la red del tema 7.
3. **El mezclador elige el programa** y aplica transiciones y efectos.
4. **El grafismo se incrusta**, antes o después del mezclador según el diseño.
5. **La salida de programa va a emisión, a grabación y a los retornos de plató.**

**Y las tres señales que salen del control hacia el plató, que es lo que un ingeniero tiene que
prever:**

| Señal de vuelta | Para qué |
|---|---|
| **Retorno de programa** | **Que en plató se vea lo que sale** |
| **Retorno de cámara** | **Que el operador vea su propia señal ajustada** |
| **Intercomunicación y orden** | **Que el realizador hable con cada puesto** |

**El error de diseño más frecuente en un estudio, y conviene saberlo enunciar**: **olvidar el retorno
y la intercomunicación.** **La señal de ida se dibuja siempre; la de vuelta se olvida**, y **sin ella
el plató no funciona aunque la imagen sea perfecta.**

**Las unidades de control de cámara merecen un párrafo propio**: **son la mitad del control que no se
ve.** **Ahí se ajusta el diafragma, el negro, el equilibrio de blancos y la matriz de color de cada
cámara**, y **de ahí sale que las cuatro cámaras de un plató parezcan la misma cámara.** **Es el
trabajo de un técnico dedicado, no del realizador.**

## 3. La continuidad

**Qué es en términos de instalación**: **la sala desde la que sale el canal.** **Su trabajo es que la
emisión no se interrumpa nunca**, y **su diseño está gobernado por eso.**

**El diagrama a bloques de una continuidad:**

1. **Las fuentes**: servidores de emisión, estudios, señales exteriores, cartón de reserva.
2. **La matriz o la conmutación de emisión.**
3. **El mezclador de continuidad**, que hace las transiciones entre piezas.
4. **La inserción de identidad**: mosca, cortinillas y sobreimpresiones.
5. **El procesado final**: control de sonoridad del tema 12 y legalización de niveles.
6. **La salida a difusión**, duplicada.

**Los tres principios que la distinguen de un estudio:**

| Principio | Qué obliga |
|---|---|
| **Redundancia en toda la cadena** | **Dos de todo lo que puede fallar, y conmutación automática** |
| **Cartón de reserva** | **Algo que emitir si todo lo demás cae**: nunca negro |
| **Supervisión permanente** | **Alarmas de ausencia de vídeo, de audio y de nivel** |

**Y la diferencia de mentalidad que un ingeniero tiene que entender**: **en un estudio, un fallo
estropea una grabación.** **En continuidad, un fallo se ve en toda España.** **Por eso una continuidad
se diseña suponiendo que las cosas van a fallar**, y no suponiendo que van a funcionar.

**El detector de ausencia de señal es la pieza más humilde y más importante**: **vigila la salida y,
si detecta negro o silencio durante más de unos segundos, conmuta automáticamente a la cadena de
respaldo.** **No mejora nada cuando todo va bien; es lo único que sirve cuando algo va mal.**

## 4. Los controles y las salas técnicas

**Qué son y qué las diferencia de las dos anteriores**: **no producen ni emiten.** **Encaminan, miden,
procesan y guardan.**

| Sala | Qué contiene |
|---|---|
| **Control central** | **La matriz principal, la referencia, la supervisión de toda la casa** |
| **Sala de equipos** | **Los bastidores: servidores, procesadores, conversores, alimentación** |
| **Sala de intercambios** | **Las señales que entran y salen del centro**: satélite, fibra, agencias |
| **Sala de medida** | **Instrumentos y puesto de comprobación** |

**Los cuatro criterios de una sala de equipos bien hecha, que es lo preguntable de este punto:**

1. **Bastidores accesibles por delante y por detrás**, con pasillo de servicio suficiente.
2. **Reparto de calor por pasillo frío y pasillo caliente**, no por temperatura media de la sala.
3. **Canalizaciones separadas para alimentación y para señal**, y cruces perpendiculares donde
   coincidan.
4. **Etiquetado de todos los latiguillos en los dos extremos**, y documentación actualizada.

**El cuarto parece administrativo y es técnico**: **una instalación sin etiquetar no se puede reparar
deprisa**, y **la reparación deprisa es exactamente lo que se pide a las tres de la madrugada.**

**Y la observación que ordena el epígrafe**: **las salas técnicas son las que nadie visita y las que
deciden si la casa funciona.** **Su diseño es el trabajo más propio de esta ocupación**, y es el que
el examen no ha sabido preguntar.

## 5. La sincronización y la referencia

**El enunciado de los puntos 11 y 12 termina con estas dos palabras**, y **son las que unen las tres
salas:**

| Concepto | Qué es |
|---|---|
| **Sincronización** | **Que todas las fuentes empiecen cada cuadro en el mismo instante** |
| **Referencia** | **La señal común contra la que todos se alinean** |

**Por qué hace falta**: **conmutar entre dos fuentes que no están sincronizadas produce un salto en la
imagen.** **Con las fuentes bloqueadas a la misma referencia, la conmutación es limpia.**

**La cadena de referencia de una casa, de arriba abajo:**

1. **Un generador maestro, con respaldo y conmutación automática.**
2. **Una distribución hasta cada sala.**
3. **En cada equipo, una entrada de referencia y el ajuste de fase que lo alinea.**

**Y las dos maneras de tratar una fuente que llega sin referencia**, que es el problema diario:

| Solución | Qué hace | Qué cuesta |
|---|---|---|
| **Sincronizador de cuadro** | **Guarda un cuadro y lo lee al ritmo de la casa** | **Un cuadro de retardo** |
| **Bloquear la fuente remota a la misma referencia** | **Que llegue ya alineada** | **Requiere referencia común en los dos extremos** |

**En una instalación sobre red, la referencia es el protocolo de tiempo de precisión del tema 7**, y
**el principio no cambia**: **sigue habiendo un maestro, sigue habiendo distribución y sigue habiendo
que comprobar que llega a todas partes.**

## 6. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **tres puntos del anexo y cero preguntas.** **Lo razonablemente preguntable
es el diagrama a bloques de un control de realización, los tres principios de una continuidad y la
cadena de referencia.** **Con eso se cubre lo que un examen escrito puede preguntar de una materia que
es de dibujo y de obra.**

**Y una advertencia sobre el reparto**: **si el examen siguiente decide preguntar por aquí, tiene tres
puntos del anexo para hacerlo.** **Es el mayor bloque a cero de la ocupación.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **no tiene ninguna respuesta oficial que
sostener**, porque los tres puntos no han dado preguntas.

**Tres declaraciones expresas:**

1. **Este temario no describe las instalaciones de RTVE**, cuyos planos y documentación no se han
   consultado. **Lo que contiene es la arquitectura habitual de un estudio, una continuidad y un
   control central**, escrita a partir del propio enunciado del anexo.
2. **Los criterios de diseño de sala de equipos, los principios de una continuidad y la cadena de
   referencia son oficio de ingeniería de instalaciones audiovisuales**, presentados como tal.
   **Ninguna norma se ha consultado para ellos.**
3. **La sincronización sobre red remite al tema 7 de esta misma ocupación**, donde se desarrolla con
   su protocolo. **Aquí se enuncia sin repetirla.**

**El tema entero va como oficio y así se declara**, porque **sus tres puntos del anexo no tienen norma
detrás ni preguntas que contestar**: se ha escrito contra el programa, que es lo que el manual de este
proyecto manda hacer con un punto sin banco.
