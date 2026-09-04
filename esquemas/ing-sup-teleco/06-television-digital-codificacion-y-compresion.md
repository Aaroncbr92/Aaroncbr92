# Esquema · Tema 6 del específico de Ingeniería Superior · Telecomunicación · Televisión digital: codificación y compresión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de televisión digital ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el
grupo de imágenes (**GOP**, *group of pictures*); la transformada del coseno discreta (**DCT**); el bit
por segundo con su múltiplo **Mbit/s**; y el submuestreo **4:2:2**, que se lee en el tema 5.

**Cabecera.** Enunciado: punto 6 del anexo · **cinco preguntas** · **sin norma**: el punto no nombra
ninguna del boletín y el tema va como oficio.

**La idea que lo ordena** · `[of]` · **Una señal de alta definición sin comprimir pide más de mil
megabits por segundo y un canal de difusión no tiene ni una décima parte.** **La compresión no es una
mejora: es la condición de existencia de la televisión digital.**

<!-- indice -->

## Índice

- [La digitalización](#la-digitalización)
- [Los tres mecanismos de la compresión de vídeo](#los-tres-mecanismos-de-la-compresión-de-vídeo)
- [Cuadros y grupo de imágenes](#cuadros-y-grupo-de-imágenes)
- [Las generaciones](#las-generaciones)
- [Audio, códec y contenedor](#audio-códec-y-contenedor)
- [Contribución, distribución y difusión](#contribución-distribución-y-difusión)
- [Servicios y acceso condicional](#servicios-y-acceso-condicional)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La digitalización

| Operación | Qué decide |
|---|---|
| **muestreo** | **la frecuencia, y con ella el ancho de banda que se conserva** |
| **cuantificación** | **la profundidad de bits, y con ella el ruido de cuantificación** |
| **codificación** | **el formato del dato** |

- **lo que separa esto del tema 2** · `[of]` · **Una señal de televisión no muestrea «la señal»:
  muestrea CADA COMPONENTE con su propia frecuencia.** **De ahí sale la notación de submuestreo del
  tema 5.**

## Los tres mecanismos de la compresión de vídeo

| Mecanismo | Qué explota |
|---|---|
| **transformada y cuantificación** | **que la energía de un bloque se concentra en pocas frecuencias** |
| **predicción** | **que un bloque se parece a otro: al de al lado o al de otro cuadro** |
| **codificación entrópica** | **que unos símbolos son mucho más frecuentes que otros** |

- **dónde se pierde información** · `[of]` · **En la cuantificación de los coeficientes**: **los de
  frecuencia alta, que el ojo aprecia menos, se cuantifican más grueso o se anulan.**
- **EL BLOQUE DE LA TRANSFORMADA** · `[exam]` · **En la codificación clásica de televisión digital es
  de OCHO POR OCHO PÍXELES.** **No dieciséis por dieciséis, que es el MACROBLOQUE**; ni cuatro por
  cuatro ni treinta y dos por treinta y dos, que son de generaciones posteriores. **Confundir bloque
  de transformada con macrobloque es lo que la pregunta busca.**

## Cuadros y grupo de imágenes

| Tipo de cuadro | Cómo se codifica |
|---|---|
| **intracodificado** | **solo, sin mirar a ningún otro**: es el punto de entrada |
| **predicho** | **mirando a un cuadro anterior** |
| **bipredicho** | **mirando a uno anterior Y a uno posterior** |

- **qué es el grupo de imágenes** · `[exam]` · **La secuencia que va de un cuadro intracodificado al
  siguiente.** **Su nombre en inglés significa literalmente «grupo de imágenes»**, y **las tres
  opciones falsas de esa pregunta desarrollan las mismas iniciales con palabras de informática que no
  tienen nada que ver.**
- **cuanto más largo, más eficiente y menos accesible** · `[of]` · **Sólo se entra en el flujo por un
  cuadro intracodificado**, y **eso alarga la sintonización y complica el corte de montaje.**
- **cerrado o abierto** · `[of]` · **Cerrado, ningún cuadro mira fuera del grupo: permite cortar
  limpio.** **Abierto, los últimos miran al grupo siguiente: comprime algo mejor.**
- **LA RESPUESTA QUE PARECE UN NÚMERO Y NO LO ES** · `[exam]` · **Un códec intracuadro NO TIENE grupo
  de imágenes.** **No es de dos, de cuatro ni de ocho: no aplica**, porque **cada cuadro se codifica
  solo.**

| Familia de códec | Cómo comprime | Dónde |
|---|---|---|
| **de producción** | **cada cuadro solo, compresión ligera** | **cámara, edición, postproducción** |
| **de contribución** | **grupo corto, calidad alta** | **enlaces entre centros** |
| **de difusión** | **grupo largo, predicción entre cuadros** | **emisión al espectador** |
| **de archivo** | **sin pérdida o casi** | **conservación** |

- **la pregunta de la compresión temporal** · `[exam]` · **De un juego de opciones con tres códecs de
  producción y uno de grabación de noticias con grupo largo, el que usa compresión temporal es este
  último.** **Los de familia de producción, por definición, no la usan.**

## Las generaciones

| Generación | Qué aporta |
|---|---|
| **la de la primera televisión digital** | **transformada de bloque, vector de movimiento, grupo de imágenes** |
| **la siguiente** | **bloques de tamaño variable, más modos de predicción, mejor entropía**: **la mitad de tasa a igual calidad** |
| **la de la ultraalta definición** | **otra vez la mitad**, a costa de mucho más cálculo |

- **LA LECTURA QUE LA PREGUNTA BUSCA** · `[exam]` · **La ventaja de una generación sobre la anterior es
  MENOR TASA DE BITS PARA LA MISMA CALIDAD DE IMAGEN.** **No más calidad de audio, no más
  compatibilidad con equipos antiguos y desde luego no un proceso de codificación más sencillo**: cada
  generación es **más** compleja de codificar, no menos.

## Audio, códec y contenedor

| Mecanismo del audio | Qué explota |
|---|---|
| **enmascaramiento** | **que un sonido fuerte tapa a otro débil cercano en frecuencia o en el tiempo** |
| **banco de filtros** | **repartir en bandas para cuantificar cada una según lo que se oye** |
| **codificación conjunta** | **que los canales comparten información** |

- **la confusión de siempre** · `[of]` · **El códec es el algoritmo; el contenedor, el envoltorio de
  fichero.** **Un mismo contenedor lleva códecs distintos y un mismo códec va en contenedores
  distintos.**
- **el contenedor de intercambio profesional** · `[of]` · **Envuelve vídeo, audio y datos con sus
  metadatos**, y **tiene variantes de empaquetado.** **La variante importa al intercambiar con otra
  casa, y es lo primero que se pacta en un pliego de entrega.**

## Contribución, distribución y difusión

| Etapa | De dónde a dónde | Qué prima |
|---|---|---|
| **contribución** | **del acontecimiento al centro de producción** | **calidad y baja latencia** |
| **distribución** | **del centro a los emisores o a otros operadores** | **fiabilidad y calidad alta** |
| **difusión** | **del emisor al espectador** | **eficiencia: cabe lo que cabe** |

- **LA REGLA QUE LAS ORDENA** · `[of]` · **La compresión aumenta según se avanza en la cadena.**
  **Contribuir con calidad de difusión es el error caro**, porque **la degradación de la primera etapa
  la arrastran todas las demás.**

| Nivel de flujo | Qué es |
|---|---|
| **elemental** | **la salida de un codificador** |
| **de programa** | **varios elementales de un programa, para medios sin errores** |
| **de transporte** | **varios programas en paquetes de longitud fija, para medios con errores** |

- **por qué paquetes cortos y fijos** · `[of]` · **Porque el canal se equivoca.** **Un paquete corto
  limita el daño y permite resincronizar deprisa**, y **la longitud fija hace trivial encontrar el
  principio del siguiente.**
- **las tablas** · `[of]` · **Una dice qué programas hay y dónde está la descripción de cada uno**;
  **otra, de qué flujos se compone cada programa**; **encima, la información de servicio con nombres y
  guía.** **Sin ellas el múltiplex es una tubería que nadie sabe interpretar.**

## Servicios y acceso condicional

| Pieza del acceso condicional | Qué hace |
|---|---|
| **aleatorización** | **el flujo se emite revuelto con una clave que cambia continuamente** |
| **mensajes de control** | **llevan la clave, cifrada a su vez** |
| **mensajes de gestión** | **dicen qué abonado puede descifrar qué** |
| **interfaz común** | **un receptor sirve para varios sistemas cambiando el módulo** |

- **LA DISTINCIÓN QUE SE CONFUNDE SIEMPRE** · `[of]` · **El acceso condicional protege la EMISIÓN; la
  gestión de derechos protege el CONTENIDO ya entregado.** **Uno impide ver sin pagar; el otro impide
  copiar y redistribuir lo ya recibido.**
- **por qué el interactivo puro era una simulación** · `[of]` · **Sin canal de vuelta, el receptor
  tenía todos los datos y sólo elegía cuál mostrar.** **Lo volvió interactivo la banda ancha del propio
  televisor**, y **eso lo convirtió en híbrido: la imagen por la antena y los datos por la red.**
- **la tendencia que más cambia el oficio y menos se ve** · `[of]` · **Más calidad por píxel antes que
  más píxeles.** **Duplicar la resolución multiplica por cuatro los píxeles y se nota poco a distancia
  normal; ampliar el rango dinámico y la gama de color se nota siempre.** **Eso es materia del tema
  8.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 5 | Cuál de cuatro códecs usa compresión temporal | **El de grabación de noticias con grupo largo** ✔ **·** los otros tres son intracuadro |
| 7 | Ventaja principal de una generación de codificación sobre la anterior | **Menor tasa de bits para la misma calidad de imagen** ✔ |
| 10 | Qué significa la sigla del grupo de imágenes | **Grupo de imágenes** ✔ **·** las tres falsas desarrollan las mismas iniciales con palabras ajenas |
| 65 | Tamaño del bloque de la transformada en los cuadros intracodificados de la codificación clásica | **Ocho por ocho píxeles** ✔ **·** dieciséis por dieciséis es el macrobloque |
| 89 | Grupo de imágenes de una señal con compresión intracuadro | **No tiene** ✔ **·** el concepto no aplica |
