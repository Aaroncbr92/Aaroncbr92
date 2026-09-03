# Esquema · Tema 13 del específico de Producción · Control central

Telegrama. **Cada línea lleva delante de dónde sale**: `[oficio]` = organización técnica de un centro
de producción, declarada como tal en el tema · `[LGCA]` = Ley 13/2022, artículo 156.2, **citada de
enlace** con el tema 16.

**Siglas**: el protocolo de internet (**IP**).

**Cabecera.** Enunciado: «CONTROL CENTRAL. Coordinación de señales y comunicaciones.
Emisión/Continuidad. Distribución de imágenes» · **3 preguntas** · ninguna descansa en la plantilla ·
**las tres tienen la misma construcción: opciones que se diferencian POR UNA ACOTACIÓN**.

<!-- indice -->

## Índice

- [Qué es el control central](#qué-es-el-control-central)
- [La matriz](#la-matriz)
- [La sincronización](#la-sincronización)
- [El embebedor](#el-embebedor)
- [Los tres circuitos de comunicación](#los-tres-circuitos-de-comunicación)
- [La señal N-1](#la-señal-n-1)
- [Emisión y continuidad](#emisión-y-continuidad)
- [Distribución](#distribución)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es el control central

- **PREGUNTA 3** · **Desde el control central se coordinan TODAS las señales de audio y vídeo que se
  pueden manejar en una estación de televisión.** **La palabra que decide es *TODAS*.**
- **Las tres falsas ACOTAN la competencia y por eso son falsas**: «solamente las **exteriores** que
  llegan» → deja fuera **estudios, servidores, salas de edición** · «solamente las **emisiones en
  directo**» → deja fuera **lo grabado, el intercambio y la contribución** · «solamente **intercambio
  y directos**» → **las internas otra vez**.
- `[oficio]` · **Sus siete funciones**: **encaminar** (cualquier origen a cualquier destino) ·
  **sincronizar** · **adaptar** (formatos, embeber y desembeber, niveles) · **vigilar** (medir cada
  señal antes de que entre en un programa) · **reservar** (circuitos y conexiones exteriores) ·
  **registrar** · **comunicar** (intercomunicador, pilotos, retornos).

## La matriz

- `[oficio]` · **Rejilla de entradas y salidas donde CUALQUIER entrada puede ir a CUALQUIER salida**, y
  una entrada **a varias salidas a la vez**.
- **Vocabulario**: **entrada** (*source*) · **salida** (*destination*) · **nivel** —vídeo, audio y
  datos se conmutan en niveles que **pueden ir juntos o por separado**— · **panel de control** ·
  **SALVADO** (*salvo*): **el bloqueo de una salida para que nadie la cambie por error durante una
  emisión**.
- **LA REGLA DE ORO DEL CONTROL CENTRAL: una señal que va al aire SE PROTEGE.** Eso hace el salvado, y
  **es lo que evita que una conmutación equivocada tire una emisión**.

## La sincronización

- `[oficio]` · **Dos señales sólo se conmutan limpiamente si sus imágenes empiezan EN EL MISMO
  INSTANTE.** Por eso todo el centro trabaja contra **UNA MISMA REFERENCIA**, generada en un sitio y
  repartida.
- **Dos referencias**: ***BLACK BURST*** —vídeo negro completo con sus sincronismos: la clásica— y
  ***TRI-LEVEL SYNC*** —impulso de tres niveles, definido **para alta definición**—.
- **Lo que llega de fuera NO está en fase con la casa**: hay que **retenerlo en memoria y volver a
  leerlo en el momento correcto**. Lo hace el **SINCRONIZADOR DE CUADRO**, y **su precio es EL
  RETARDO**: la señal sale uno o varios cuadros después de entrar.

## El embebedor

- `[oficio]` · **AUDIO EMBEBIDO** = las pistas de audio metidas **dentro de la señal digital de
  vídeo**, en los espacios que deja libres entre líneas y entre cuadros. **Embeber** = meterlas ·
  **desembeber** = sacarlas. **En la práctica el mismo aparato hace las dos cosas.**
- **PREGUNTA 25** · **La función del embebedor es EXTRAER O INSERTAR AUDIOS EN UNA SEÑAL DE VÍDEO.**
- **Las tres falsas describen tres aparatos REALES del mismo control**: «multiplexar desde satélite» →
  **demultiplexor de transporte** · «multiplexar desde codificadores IP» → **multiplexor de
  transporte** · «enrutar hacia los controles de realización» → **la MATRIZ**.
- **Lo que lo separa de los tres: NO mueve señales entre sitios, mueve AUDIO DENTRO DE UNA SEÑAL.** Es
  **operación de formato, no de encaminamiento**.
- **Por qué importa**: una señal de fuera puede traer su audio **en pistas que no coinciden con las de
  la casa**. **El embebedor las reordena**, y sin ese paso **el programa sale con el sonido en el canal
  equivocado**.

## Los tres circuitos de comunicación

| Circuito | Quién habla | Quién oye |
|---|---|---|
| **Intercomunicación** (*intercom*) | El equipo técnico entre sí | El equipo técnico, por auricular |
| **Órdenes** | **El realizador** | Cámaras, regiduría, control |
| **RETORNOS** | El control | **QUIEN ESTÁ DELANTE DE LA CÁMARA**, por pinganillo o monitor |

- **El tercero es el que da problemas, porque QUIEN LO RECIBE ESTÁ HABLANDO AL MISMO TIEMPO.**

## La señal N-1

- `[oficio]` · **El N-1 es la mezcla del programa MENOS la señal de la persona a la que se le envía.**
- **EL PROBLEMA QUE RESUELVE**: si a un redactor en directo se le devuelve el programa **con su propia
  voz dentro**, la oirá **con el retardo del enlace** —unos cientos de milisegundos— **y no podrá
  hablar**. **El eco de la propia voz retrasada bloquea el habla, y no se vence con voluntad.**
- **PREGUNTA 37** · **Se le envía el retorno de audio del programa EXCEPTUANDO SU PROPIA VOZ.**
- **Las cuatro opciones empiezan igual y se diferencian en QUÉ QUITAN Y QUÉ DEJAN**: a) incluye lo que
  él dice → **es justo el problema** · c) mete su voz **y las órdenes del realizador**, que son **otro
  circuito** · d) quita las órdenes **pero lo deja oyéndose a sí mismo**.
- **PRECISIÓN DE OFICIO: CADA ENVÍO TIENE SU PROPIA N-1.** Tres conexiones exteriores = **tres mezclas
  distintas**. **Por eso una mesa de directo se dimensiona por el número de ENVÍOS, no sólo de
  entradas.**
- **Las órdenes del realizador van por otro camino** y se mezclan con el retorno **sólo si así se
  decide**, con el nivel del programa bajado mientras se habla.

## Emisión y continuidad

- `[oficio]` · **La continuidad NO hace programas: hace lo que va ENTRE los programas** y **garantiza
  que el canal no se quede en negro**: identidad del canal (mosca, caretas, cortinillas) ·
  autopromociones · publicidad **en sus bloques con su duración vendida** · entradas y salidas ·
  **avisos de servicio** (señalización de contenido, subtitulado, cambios de programación).
- **Cómo se emite hoy**: **lista de emisión** minuto a minuto cargada en un **servidor de emisión**,
  con automatización que lo dispara **y un operador que vigila y corrige**.
- `[LGCA 156.2]` · **Lo emitido hay que conservarlo** → tema 16.

## Distribución

- `[oficio]` · **Un centro público reparte en varias direcciones a la vez**: red de difusión terrestre
  (centro emisor → TDT) · satélite y cable por circuitos contratados · plataformas e internet **con la
  codificación de cada destino** · **otras cadenas** (intercambio de noticias) · **el archivo**.
- **Figura del intercambio que hay que nombrar**: la **SEÑAL *POOL***, la que **una sola cadena o
  productora realiza y distribuye a todas las demás**, típicamente en actos institucionales **donde no
  caben veinte equipos**.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 3 | Qué se coordina desde el control central | a) Todas las señales de audio y vídeo de la estación ✔ |
| 25 | Función de un embebedor | b) Extraer o insertar audios en una señal de vídeo ✔ |
| 37 | Qué significa el envío del N-1 al redactor | b) El programa exceptuando su propia voz ✔ |

**Las tres oficiales son correctas.** · **La 3 opone «todas» a tres «solamente»; la 25 opone una
operación de formato a tres de encaminamiento; la 37 opone cuatro combinaciones de qué se quita y qué
se deja. LEER DESPACIO LA MITAD FINAL DE CADA OPCIÓN resuelve las tres.** · **Aviso**: el **N-1** se
pregunta también en Realización (Asistencia). **Entenderlo, no memorizarlo: la mezcla del programa
menos la voz de quien la recibe.**
