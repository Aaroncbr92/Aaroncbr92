# Tema 6 del específico de Ingeniería Superior · Telecomunicación · Televisión digital: digitalización, codificación y compresión

Las siglas y símbolos de este tema, presentados de entrada: el grupo de imágenes (**GOP**, *group of
pictures*); la transformada discreta del coseno (**DCT**); el megabit por segundo (**Mbit/s**); el
flujo elemental (**ES**), el flujo de programa (**PS**) y el flujo de transporte (**TS**); la tabla de
asociación de programas (**PAT**) y la de mapa de programa (**PMT**); la información específica de
programa (**PSI**) y la información de servicio (**SI**); la guía electrónica de programación (**EPG**);
el acceso condicional (**CA**) y su interfaz común (**CI**); la gestión de derechos digitales
(**DRM**); la televisión híbrida de difusión y banda ancha (**HbbTV**); y el formato de intercambio de
material (**MXF**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 6):
> «Televisión digital. Digitalización, estándares de codificación y compresión de video y de audio.
> Sistemas de contribución, distribución y difusión. Tipos de servicios soportados. Servicios
> interactivos y acceso condicional. Evolución y tendencias.»

**Es el punto más largo del enunciado de toda la ocupación y hay que trocearlo para estudiarlo.**
**Cuatro asuntos encadenados**: **cómo se digitaliza y se comprime**, **por dónde viaja**, **qué
servicios lleva** y **cómo se protege el acceso.**

**Y la idea que ordena el punto entero**: **la televisión digital no es televisión analógica
digitalizada: es una CADENA DE DATOS.** **Lo que viaja no es una imagen, son paquetes**, y **eso
permite meter varios programas en el mismo canal, añadir servicios que no son imagen y cobrar por
ellos.** **Todo lo que este tema describe sale de ahí.**

<!-- indice -->
<!-- /indice -->

## 1. La digitalización

**Tres operaciones en orden, y hay que saber que cada una pierde algo distinto:**

| Operación | Qué hace | Qué decide |
|---|---|---|
| **MUESTREO** | **Tomar valores a intervalos regulares** | **La frecuencia de muestreo, y con ella el ancho de banda que se conserva** |
| **CUANTIFICACIÓN** | **Asignar a cada muestra uno de un número finito de niveles** | **La profundidad de bits, y con ella el ruido de cuantificación** |
| **CODIFICACIÓN** | **Representar cada nivel con un código binario** | **El formato del dato** |

**Y la observación que separa este epígrafe del tema 2**: **la digitalización de una señal de
televisión no muestrea «la señal»: muestrea CADA COMPONENTE**, con **su propia frecuencia**, y **de ahí
sale la notación de submuestreo del tema 5.**

**Lo que ocupa una señal digitalizada sin comprimir es lo que hace imprescindible el epígrafe
siguiente**: **una señal de alta definición sin comprimir pide más de mil megabits por segundo**, y
**un canal de difusión no tiene ni una décima parte.** **La compresión no es una mejora: es la
condición de existencia de la televisión digital.**

## 2. La compresión de vídeo

**Los tres mecanismos que se combinan, en el orden en que actúan:**

| Mecanismo | Qué explota |
|---|---|
| **TRANSFORMADA y cuantificación** | **Que la energía de un bloque de imagen se concentra en pocas frecuencias** |
| **PREDICCIÓN** | **Que un bloque se parece a otro**: al de al lado —intra— o al de otro cuadro —inter— |
| **CODIFICACIÓN ENTRÓPICA** | **Que unos símbolos son mucho más frecuentes que otros** |

**El primero merece detalle porque es el que un examen pregunta con números**: **la imagen se parte en
BLOQUES y a cada bloque se le aplica una transformada** que convierte los valores de píxel en
coeficientes de frecuencia. **Después se cuantifican esos coeficientes**, y **ahí es donde se pierde
información**: los de frecuencia alta, que el ojo aprecia menos, se cuantifican más grueso o se anulan.

**El tamaño del bloque de la transformada del coseno en la codificación clásica de televisión digital
—la de segunda generación, la que sostiene la difusión— es de OCHO POR OCHO PÍXELES.** **No dieciséis
por dieciséis, que es el tamaño del MACROBLOQUE**, ni cuatro por cuatro ni treinta y dos por treinta y
dos, que son tamaños de generaciones posteriores. **Confundir el bloque de transformada con el
macrobloque es el error que esa pregunta busca.**

**Los tipos de cuadro y el grupo de imágenes**, que es el concepto central del punto:

| Tipo de cuadro | Cómo se codifica |
|---|---|
| **Intracodificado** | **Solo, sin mirar a ningún otro**: es el punto de entrada |
| **Predicho** | **Mirando a un cuadro anterior** |
| **Bipredicho** | **Mirando a un cuadro anterior Y a uno posterior** |

**El GRUPO DE IMÁGENES es la secuencia que va de un cuadro intracodificado al siguiente**, y **hay que
saber tres cosas de él:**

1. **Cuanto más largo, más eficiente y menos accesible.** **Un grupo largo comprime mucho porque hay
   pocos cuadros completos**, pero **sólo se puede entrar en el flujo por un cuadro intracodificado**,
   y **eso alarga el tiempo de sintonización y complica el corte de montaje.**
2. **Puede ser CERRADO o ABIERTO.** **Cerrado, ningún cuadro del grupo mira fuera de él; abierto, los
   últimos pueden mirar al grupo siguiente.** **El cerrado permite cortar limpio; el abierto comprime
   algo mejor.**
3. **Un códec INTRACUADRO NO TIENE grupo de imágenes.** **No es que lo tenga de dos, de cuatro o de
   ocho**: **es que no aplica**, porque **cada cuadro se codifica solo.** **Ésa es la respuesta, y las
   tres cifras de las otras opciones están puestas para que parezca que hay que elegir un número.**

**Las familias de códec por su uso, que es lo que decide un flujo de trabajo:**

| Familia | Cómo comprime | Dónde se usa |
|---|---|---|
| **De producción, INTRACUADRO** | **Cada cuadro solo**, con compresión ligera | **Cámara, edición y postproducción** |
| **De contribución** | **Grupo corto**, calidad alta | **Enlaces entre centros** |
| **De difusión, con GRUPO LARGO** | **Predicción entre cuadros**, muy eficiente | **Emisión al espectador** |
| **De archivo** | **Sin pérdida o casi**, o con grupo largo si el archivo es de consulta | **Conservación** |

**Y el dato que un examen pide reconocer**: **de los códecs que un centro maneja, los de familia de
producción —los de tipo intracuadro— NO usan compresión temporal**, y **los de familia de emisión
sí.** **Un códec de cámara con submuestreo 4:2:2 y grupo largo existe y se usa en grabación de
noticias**, y **es el ejemplo que suele aparecer como respuesta cuando se pregunta cuál usa compresión
temporal frente a tres intracuadro.**

**La evolución de las generaciones de codificación**, sin nombrar ninguna por su denominación
comercial:

| Generación | Qué aporta |
|---|---|
| **La de la primera televisión digital** | **Transformada de bloque, predicción con vector de movimiento y grupo de imágenes** |
| **La siguiente** | **Bloques de tamaño variable, más modos de predicción y codificación entrópica mejor**: **la mitad de tasa para la misma calidad** |
| **La de la ultraalta definición** | **Otra vez la mitad**, a costa de mucha más potencia de cálculo |

**Y la lectura que hay que dar de esa tabla, porque es lo que la pregunta busca**: **la ventaja
principal de una generación sobre la anterior NO es más calidad de audio, ni más compatibilidad con
equipos antiguos, ni un proceso de codificación más sencillo** —es justo lo contrario, cada generación
es más compleja de codificar—: **es MENOR TASA DE BITS PARA LA MISMA CALIDAD DE IMAGEN.**

## 3. La compresión de audio

**El mismo principio con otro sistema perceptivo:**

| Mecanismo | Qué explota |
|---|---|
| **ENMASCARAMIENTO** | **Que un sonido fuerte tapa a otro débil cercano en frecuencia o en el tiempo** |
| **Banco de FILTROS** | **Repartir la señal en bandas para cuantificar cada una según lo que se oye** |
| **Codificación conjunta de canales** | **Que los canales de un estéreo o de un multicanal comparten información** |

**Y los dos conceptos que hay que separar y que se confunden siempre:**

| | **CÓDEC** | **CONTENEDOR** |
|---|---|---|
| **Qué es** | **El algoritmo que comprime y descomprime** | **El formato de fichero que envuelve uno o varios flujos** |
| **Qué decide** | **La calidad y la tasa** | **Qué cabe dentro, cómo se sincroniza y qué metadatos lleva** |
| **Ejemplo de confusión** | Un mismo contenedor puede llevar códecs distintos, y un mismo códec ir en contenedores distintos | |

**El contenedor de intercambio profesional merece una línea**, porque **es el que ordena el material de
una casa que emite**: **envuelve vídeo, audio y datos con sus metadatos**, y **tiene variantes de
empaquetado según lo que se busque** —un fichero autocontenido y sencillo de manejar, o material y
metadatos repartidos—. **La variante importa al intercambiar con otra casa**, y **es lo primero que se
pacta en un pliego de entrega.**

## 4. Contribución, distribución y difusión

**Tres etapas de la cadena, y hay que no confundirlas nunca**, porque **cada una tiene calidad, retardo
y coste distintos:**

| Etapa | De dónde a dónde | Qué prima |
|---|---|---|
| **CONTRIBUCIÓN** | **Del lugar del acontecimiento al centro de producción** | **CALIDAD y baja latencia**: el material se va a seguir tratando |
| **DISTRIBUCIÓN** | **Del centro de producción a los centros emisores o a otros operadores** | **Fiabilidad y calidad alta** |
| **DIFUSIÓN** | **Del centro emisor al espectador** | **EFICIENCIA**: cabe lo que cabe en el canal |

**Y la regla que las ordena**: **la compresión aumenta según se avanza en la cadena.** **En
contribución se comprime poco porque el material aún se va a editar y a recodificar; en difusión se
comprime al límite porque ya no se va a tocar más.** **Invertir eso —contribuir con una calidad de
difusión— es el error caro**, porque **la degradación de la primera etapa la arrastran todas las
demás.**

**El FLUJO DE TRANSPORTE, que es como viaja todo eso**, con sus tres niveles:

| Nivel | Qué es |
|---|---|
| **Flujo ELEMENTAL** | **La salida del codificador**: un vídeo, un audio, unos datos |
| **Flujo de PROGRAMA** | **Varios elementales de un mismo programa**, para medios sin errores |
| **Flujo de TRANSPORTE** | **Varios programas multiplexados en paquetes de longitud fija**, pensado para medios con errores |

**Por qué el de transporte usa paquetes cortos y de longitud fija, que es la pregunta conceptual**:
**porque va por un canal que se equivoca.** **Un paquete corto limita el daño de un error y permite
resincronizar deprisa**, y **la longitud fija hace trivial encontrar el principio del siguiente.**

**Las tablas que lo hacen navegable**, que hay que saber para qué sirven: **una tabla dice qué
programas hay en el múltiplex y dónde está la descripción de cada uno**, **otra dice de qué flujos se
compone cada programa**, y **encima de eso van las tablas de información de servicio que dan los
nombres, la guía de programación y los datos de red.** **Sin ellas el múltiplex es una tubería de
paquetes que nadie sabe interpretar.**

## 5. Los servicios y el acceso condicional

**Qué se puede llevar además de la imagen y el sonido:**

| Servicio | Qué es |
|---|---|
| **Guía electrónica de programación** | **Qué hay ahora y qué habrá luego**, con sus descripciones |
| **Subtitulado y audiodescripción** | **Accesibilidad**, que es exigencia legal y no una prestación opcional |
| **Múltiples pistas de audio** | Versión original, lengua cooficial, comentario |
| **Teletexto y sus sucesores** | Datos en pantalla |
| **Servicios INTERACTIVOS** | **Aplicaciones que corren en el receptor**, hoy con vuelta por banda ancha |
| **Televisión híbrida** | **La difusión y la conexión de banda ancha combinadas en el mismo receptor** |

**Y la observación sobre los interactivos que explica su historia**: **el interactivo puro, sin canal de
vuelta, era una simulación**: el receptor tenía todos los datos y sólo elegía cuál mostrar. **Lo que lo
volvió interactivo de verdad fue la conexión de banda ancha del propio televisor**, y **eso convirtió
el servicio en un híbrido: la imagen por la antena y los datos por la red.**

**El ACCESO CONDICIONAL**, que el enunciado nombra expresamente:

| Pieza | Qué hace |
|---|---|
| **ALEATORIZACIÓN** | **El flujo se emite revuelto** con una clave que cambia continuamente |
| **Mensajes de CONTROL** | **Llevan la clave, cifrada a su vez** |
| **Mensajes de GESTIÓN** | **Dicen qué abonado puede descifrar qué**, y se dirigen a cada tarjeta o receptor |
| **Módulo e INTERFAZ COMÚN** | **Permite que un receptor sirva para varios sistemas de acceso**, cambiando el módulo |

**Y la distinción que hay que dejar clara, porque se confunde constantemente**: **el acceso condicional
protege la EMISIÓN; la gestión de derechos digitales protege el CONTENIDO ya entregado.** **Uno impide
ver lo que se emite sin pagar; el otro impide copiar y redistribuir lo que ya se ha recibido.** **Son
dos problemas distintos y dos tecnologías distintas.**

## 6. Evolución y tendencias

**El enunciado lo pide, y un temario tiene que decirlo sin caducar**: **las tendencias se estudian por
su MECANISMO, no por su lista de productos.**

| Tendencia de fondo | Qué la mueve |
|---|---|
| **Más eficiencia de codificación** | **Cada generación libera espacio en el canal**, y ese espacio se llena con más servicios o más calidad |
| **De la difusión al ENVÍO BAJO DEMANDA** | **La red de banda ancha llega a donde llegaba la antena**, y el consumo deja de ser simultáneo |
| **De la señal al FICHERO y del fichero al FLUJO** | **La cadena de producción se vuelve informática**, que es lo que sostiene los temas 18, 19 y 20 |
| **Más calidad por píxel antes que más píxeles** | **El rango dinámico y la gama de color aportan más que la resolución** a igual tasa |
| **Accesibilidad y personalización** | **Más pistas, más subtítulos, audio adaptado** |

**Y la lectura que este temario declara como suya**: **la cuarta es la que más cambia el oficio y la que
menos se ve.** **Duplicar la resolución multiplica por cuatro los píxeles y se nota poco a la distancia
de visión normal; ampliar el rango dinámico y la gama de color se nota siempre.** **Por eso la
ultraalta definición se define por más cosas que el número de píxeles**, y **eso es materia del tema
8.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO nombra ningún códec, ningún estándar de codificación y ningún contenedor por su
   denominación**, aunque **el enunciado hable de «estándares».** **La razón es de método**: **cada
   uno de esos nombres es una norma con su número y su año**, y **este proyecto no atribuye a una
   norma nada que no haya leído en ella.** **Lo que el temario da son las FAMILIAS, sus mecanismos y
   el criterio para elegirlas**, que es lo que no caduca. **Los estándares que el anexo sí nombra —los
   de alta y ultraalta definición y los de difusión— se estudian en los temas 7, 8 y 9.**
2. **Los ocho por ocho píxeles del bloque de transformada son la respuesta que la plantilla oficial
   de esta ocupación confirma en su pregunta 65**, y **el temario declara esa procedencia**: **no
   proceden de la norma que lo fija, que no se ha consultado.** **La advertencia de no confundirlo con
   el macrobloque de dieciséis por dieciséis es lectura de este temario.**
3. **Este tema NO da ninguna tasa de bits, ninguna longitud de grupo de imágenes, ningún tamaño de
   paquete del flujo de transporte y ningún porcentaje de reducción entre generaciones.** **La
   afirmación de que cada generación consigue «la mitad de tasa para la misma calidad» se da como
   ORDEN DE MAGNITUD del oficio y así se declara**, no como un valor medido.
4. **La exigencia legal de accesibilidad se nombra como tal y NO se cita**: **está en la Ley 13/2022
   General de Comunicación Audiovisual**, que **este proyecto tiene volcada y citada en el tema 7 del
   bloque general**, y **aquí se remite.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la difusión
   terrestre, al tema 7**; **la de satélite, al tema 9**; **los estándares de alta y ultraalta
   definición, al tema 8**; **la compresión de audio y sus formatos, al tema 21**; **y el material
   como fichero y como flujo, a los temas 18 y 19.**

**El resto del tema va como oficio y así se declara**: la idea de que la televisión digital es una
cadena de datos y no televisión analógica digitalizada, la observación de que se muestrea cada
componente y no «la señal», la lectura de que la compresión es la condición de existencia de la
televisión digital, la advertencia de no confundir el bloque de transformada con el macrobloque, las
tres cosas que hay que saber del grupo de imágenes y en particular que un códec intracuadro no lo
tiene, la tabla de familias de códec por su uso, la lectura de que la ventaja de una generación es
menor tasa a igual calidad y no las otras tres cosas, la distinción entre códec y contenedor, la regla
de que la compresión aumenta según se avanza en la cadena y de que contribuir con calidad de difusión
es el error caro, la explicación de por qué el flujo de transporte usa paquetes cortos y fijos, la
observación sobre lo que volvió interactivo de verdad al interactivo, la distinción entre acceso
condicional y gestión de derechos, y la lectura de que la calidad por píxel cambia más el oficio que el
número de píxeles. **Nada de eso está en un boletín oficial ni en ninguna fuente consultada para este
proyecto**, y el tema no lo presenta como si lo estuviera.
