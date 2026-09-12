# Esquema · Tema 12 del específico de Ingeniería Superior · Telecomunicación · Producción II: sonido, iluminación, medida y auxiliares

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de equipamiento de estudio ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: el
conversor de frecuencia de muestreo (**SRC**); el protocolo estándar de control de iluminación escénica
(**DMX**); la interfaz digital serie (**SDI**); y el kilohercio (**kHz**).

**Cabecera.** Enunciado: punto 12 del anexo · **cuatro preguntas** · **sin norma del boletín**.

**La idea que lo ordena** · `[of]` · **Este punto es el del RACK y el del CONTROL**: **lo que no se ve
en pantalla y sin lo cual no hay pantalla.** **Las cuatro preguntas que ha dado son de reconocer la
herramienta correcta entre cuatro que suenan parecido.**

<!-- indice -->

## Índice

- [Las mesas de sonido](#las-mesas-de-sonido)
- [La iluminación y su control](#la-iluminación-y-su-control)
- [La medida de vídeo](#la-medida-de-vídeo)
- [Las señales de prueba](#las-señales-de-prueba)
- [El equipamiento auxiliar](#el-equipamiento-auxiliar)
- [La medida de audio](#la-medida-de-audio)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las mesas de sonido

| Bloque | Qué hace |
|---|---|
| **preamplificador** | **adapta el nivel de la fuente al de la mesa** |
| **ecualización y filtros** | **corrige la respuesta en frecuencia** |
| **dinámica** | **compresor, limitador y puerta de ruido** |
| **envíos y retornos** | **salidas paralelas para efectos y monitorado** |
| **buses y subgrupos** | **sumas parciales que se controlan juntas** |
| **matriz de salida** | **qué mezcla va a qué destino** |
| **monitorado** | **lo que oye el técnico, que no siempre es lo que sale** |

- **analógica frente a digital** · `[of]` · **La analógica tiene un camino físico por canal y un mando
  por función; la digital procesa números, guarda escenas y cambia la función del mando según la
  capa.** **La digital gana recuperando una configuración en segundos; la analógica, en que lo que se
  ve es lo que hay.**
- **el caso de la frecuencia de muestreo** · `[exam]` · **Si a una mesa digital le llega una señal
  muestreada a otra frecuencia, se usa un CONVERSOR de frecuencia de muestreo.** **Meterla por
  analógico es convertir dos veces sin necesidad; un atenuador toca el nivel y no la frecuencia; y
  decir que no se puede es falso.**
- **la regla de instalación** · `[of]` · **Una instalación de audio digital tiene UNA referencia de
  reloj y todo se engancha a ella.** **La conversión se usa para lo que viene de fuera; dentro de la
  casa se sincroniza, no se convierte.**

## La iluminación y su control

| Pieza | Qué hace |
|---|---|
| **luminarias** | **producen la luz**: descarga, incandescencia y hoy sobre todo diodos |
| **reguladores** | **controlan la potencia que llega a cada aparato** |
| **mesa de iluminación** | **guarda y lanza los estados de luz** |
| **luminarias robotizadas** | **mueven, enfocan y cambian color y forma** |
| **red de control** | **lleva las órdenes de la mesa a cada aparato** |

- **EL PROTOCOLO** · `[exam]` · **El protocolo estándar de control de iluminación escénica sirve para
  CONTROLAR LA ILUMINACIÓN y nada más.** **No controla servidores de emisión, ni la señalización de
  cámara, ni conmuta una matriz de vídeo.**
- **las tres cosas que hay que saber de él** · `[of]` · **1)** es **unidireccional y sin acuse**: la
  mesa manda y nadie contesta. **2)** se organiza en **universos de canales**, y **una luminaria
  robotizada gasta muchos**. **3)** hoy **viaja sobre red**, con la ventaja y el riesgo de compartir
  infraestructura con los datos.
- **las dos observaciones de oficio** · `[of]` · **1)** un regulador de fase **recorta la onda y ensucia
  la red**: produce armónicos que cargan el neutro. **2)** los diodos **han cambiado el problema, no lo
  han quitado**: su fuente conmutada también genera armónicos, y **su parpadeo puede batir con la
  cadencia de la cámara**, que es hoy el fallo más frecuente de una iluminación nueva mal elegida.

## La medida de vídeo

| Instrumento | Qué muestra | Para qué |
|---|---|---|
| **monitor de forma de onda** | **la señal en el tiempo, con su nivel** | **exposición: negro, blanco y recorte** |
| **vectorscopio** | **la CROMINANCIA en un plano polar**: matiz en el ángulo, saturación en el radio | **medir el color** |
| **rasterizador** | **lo mismo, calculado y presentado en un monitor de datos** | **la forma moderna de los dos anteriores** |
| **monitor de estado del enlace** | **errores de interfaz y datos auxiliares** | **diagnóstico de enlace** |
| **analizador de flujo** | **la estructura de un flujo de transporte o de red** | **emisión y red** |
| **generador de patrones** | **señales de prueba conocidas** | **ajuste y verificación** |

- **LA PREGUNTA DIRECTA** · `[exam]` · **La crominancia se mide con el VECTORSCOPIO.** **No con un
  «medidor de tensión de color», que no existe con ese nombre; ni con un analizador de espectro, que es
  de radiofrecuencia; ni con un monitor de forma de onda, que da nivel en el tiempo y no color en un
  plano polar.**
- **la regla que separa los dos clásicos** · `[of]` · **La forma de onda es para la LUZ y el
  vectorscopio para el COLOR.** **Se usan juntos y responden preguntas distintas.**

## Las señales de prueba

| Señal | Para qué |
|---|---|
| **barras de color** | **referencia de nivel y de color** |
| **rampa y escalera** | **linealidad del canal** |
| **múltiples ráfagas** | **respuesta en frecuencia** |
| **patológica** | **el caso PEOR para un enlace digital** |

- **QUÉ ES LA PATOLÓGICA** · `[exam]` · **Una señal construida a propósito para poner el enlace digital
  en su peor situación**, y **sirve para comprobar un canal digital de televisión en altas Y en bajas
  frecuencias.** **Tiene dos partes: una de máximo contenido de baja frecuencia —pocas transiciones,
  que estresa la recuperación de reloj— y otra de máximo de alta.**
- **las tres falsas** · `[exam]` · **No corrige retardos entre crominancia y luminancia**, **ni
  aberraciones cromáticas de las lentes** —eso es óptico y se hace con carta—, **ni comprueba la fase
  entre parejas de audio** —eso es el medidor de correlación, del tema 21—.
- **la lectura de oficio** · `[of]` · **Un enlace que pasa la patológica pasa cualquier cosa.** **Por
  eso es la prueba de aceptación de una instalación de vídeo digital**, y **por eso un enlace que va
  bien con imagen normal y falla con la patológica está al límite aunque parezca sano.**

## El equipamiento auxiliar

| Equipo | Qué hace |
|---|---|
| **distribuidor** | **una entrada, varias salidas idénticas, regeneradas** |
| **conversor de formato o de norma** | **cambia resolución, cadencia o barrido** |
| **embebedor y desembebedor** | **mete el audio dentro del vídeo y lo saca** |
| **conversor de interfaz** | **entre coaxial, fibra y red** |
| **sincronizador de cuadro** | **alinea una señal ajena a la referencia de la casa** |
| **regenerador y ecualizador** | **recupera una señal que ha viajado mucho** |
| **generador de retardo** | **alinea audio con vídeo** |

- **el embebedor** · `[of]` · **Es lo que permite que audio y vídeo viajen por un solo cable**: **mete
  el audio en el espacio de datos auxiliares del borrado**, que es lo del tema 5. **Embeber es cómodo y
  desembeber siempre cuesta un proceso.**
- **el sincronizador de cuadro** · `[of]` · **Es lo que hace utilizable una señal de fuera.** **Una
  señal ajena no está enganchada a la referencia de la casa**, y **sin sincronizar, al conmutarla
  salta.**
- **LA ARITMÉTICA DE DISTRIBUCIÓN** · `[exam]` · **Una señal de ultraalta definición repartida por
  cuadrantes son CUATRO enlaces independientes**, y **llevarla a TRES monitores pide CUATRO
  distribuidores de al menos TRES salidas cada uno.** **Cuadrantes por un lado y destinos por otro: un
  distribuidor por cuadrante, con tantas salidas como destinos.** **Quien piense en un solo distribuidor
  de cuatro salidas confunde los cuadrantes de la señal con los destinos.**

## La medida de audio

| Instrumento | Qué mide |
|---|---|
| **vúmetro** | **nivel con respuesta lenta** |
| **picómetro** | **nivel de pico: lo que puede saturar** |
| **medidor de sonoridad** | **cuán fuerte suena de verdad, integrado en el tiempo** |
| **medidor de correlación** | **si los dos canales están en fase o en contrafase** |
| **sonómetro** | **nivel acústico en la sala, no en la señal** |

- **por qué importa la fase** · `[of]` · **Dos canales en contrafase suenan bien en estéreo y
  DESAPARECEN al sumarlos a monofonía.** **Como parte del público oye en un solo altavoz, un problema
  de fase que nadie detecta en el control se convierte en un audio que se apaga en casa.** **Enlaza con
  el tema 21.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 51 | Para qué se usa la señal de prueba patológica | **Para comprobar un canal digital de televisión en altas y bajas frecuencias** ✔ |
| 53 | Distribuidores para llevar a tres monitores una señal de ultraalta definición por cuadrantes | **Cuatro distribuidores de al menos tres salidas cada uno** ✔ |
| 75 | Para qué se usa el protocolo estándar de control escénico | **Control de la iluminación** ✔ |
| 96 | Con qué equipo se mide la crominancia | **Vectorscopio** ✔ |
