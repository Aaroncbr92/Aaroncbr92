# Tema 12 del específico de Ingeniería Superior · Telecomunicación · Elementos de producción (II): sonido, iluminación, medida y equipamiento auxiliar

Las siglas y símbolos de este tema, presentados de entrada: el monitor de forma de onda (**WFM**,
*waveform monitor*); el vectorscopio; el multiplexado digital de audio (**MADI**); el audio digital de
la Sociedad de Audio y de la Unión Europea de Radiodifusión (**AES/EBU**, o **AES3**); el protocolo de
control de iluminación (**DMX**), en su versión sobre red (**Art-Net** y **sACN**); el diodo emisor de
luz (**LED**); el vatio (**W**) y el kilovatio (**kW**); el grado kelvin (**K**); el índice de
reproducción cromática (**IRC**); el decibelio (**dB**) con sus referencias (**dBu**, **dBFS** y
**LUFS**); el kilohercio (**kHz**); y la señal de prueba patológica (**patológica**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 12):
> «Elementos de producción (II): Mesas de Sonido. Mesas de iluminación, dimmers, iluminación
> robotizada. Equipos de medida y control (WFM, rasterizadores, medida de audio, etc.) Equipamiento
> auxiliar de vídeo (distribuidores, embebedores, etc.)»

**El enunciado junta cuatro familias que un plató necesita y que no se parecen entre sí**: **el sonido,
la luz, la medida y el equipamiento auxiliar de vídeo.** **Lo que las une es que ninguna produce
programa: las cuatro hacen posible producirlo.**

**Y la idea que ordena el punto**: **este es el equipamiento que sólo se nota cuando falla.** **Una
mesa de sonido, un regulador de luz, un distribuidor y un monitor de forma de onda no salen en pantalla
nunca**, y **sin embargo un fallo en cualquiera de ellos para un plató.** **Estudiarlos es estudiar el
mantenimiento de una casa que emite.**

<!-- indice -->
<!-- /indice -->

## 1. Las mesas de sonido

**Qué hace una mesa, en cinco funciones**: **amplificar y adaptar cada fuente, procesarla, mezclarla,
encaminarla y monitorizarla.**

**Su estructura, que es la que hay que saber describir:**

| Bloque | Qué hace |
|---|---|
| **PREAMPLIFICADOR de entrada** | **Adapta el nivel de la fuente al de la mesa**: micrófono, línea o digital |
| **ECUALIZACIÓN y filtros** | **Corrige la respuesta en frecuencia** |
| **DINÁMICA** | **Compresor, limitador y puerta de ruido** |
| **Envíos y retornos** | **Salidas paralelas** para efectos y para monitorado |
| **Buses y subgrupos** | **Sumas parciales** que se controlan juntas |
| **Matriz de salida** | **Qué mezcla va a qué destino**: emisión, grabación, sala, retornos |
| **MONITORADO y escucha** | Lo que oye el técnico, que no siempre es lo que sale |

**Las dos distinciones que un examen persigue:**

1. **Mesa ANALÓGICA frente a DIGITAL.** **La analógica tiene un camino físico por canal y un mando por
   función; la digital procesa números, tiene memorias de escena y un mando que cambia de función
   según la capa.** **La digital gana en recuperar una configuración en segundos; la analógica, en que
   lo que se ve es lo que hay.**
2. **Mesa de DIRECTO frente a mesa de POSTPRODUCCIÓN.** **La primera prioriza la maniobra inmediata y
   la fiabilidad; la segunda, la automatización y el número de pistas.**

**Y el problema de frecuencia de muestreo que esta ocupación pregunta**: **si una mesa digital trabaja
a una frecuencia de muestreo y le llega una señal digital muestreada a otra, hay que CONVERTIR LA
FRECUENCIA DE MUESTREO.** **El aparato que lo hace es un convertidor de frecuencia de muestreo**, y
**es lo que resuelve el caso.**

**Y hay que razonar por qué las otras salidas no valen**: **meterla por una entrada analógica supone
convertir a analógico y volver a digital, que es una pérdida de calidad innecesaria y además exige un
convertidor externo; un atenuador de paso no toca la frecuencia de muestreo, sólo el nivel; y decir que
no se puede es falso**, porque **la conversión de frecuencia de muestreo es un proceso corriente y está
integrado en las entradas de casi cualquier mesa moderna.**

**Y la regla de oficio que hay que añadir**: **una instalación de audio digital tiene UNA referencia de
reloj y todo lo demás se engancha a ella.** **La conversión de frecuencia se usa para lo que viene de
fuera; dentro de la casa se sincroniza, no se convierte**, porque **cada conversión es un proceso
más.**

## 2. La iluminación y su control

**Las piezas de una instalación de luz de plató:**

| Pieza | Qué hace |
|---|---|
| **LUMINARIAS** | **Producen la luz**: descarga, incandescencia y hoy sobre todo diodos |
| **REGULADORES o atenuadores** | **Controlan la potencia** que llega a cada luminaria |
| **MESA de iluminación** | **Guarda y lanza los estados de luz** |
| **Luminarias ROBOTIZADAS** | **Mueven, enfocan y cambian color y forma** por control remoto |
| **Red de CONTROL** | **Lleva las órdenes de la mesa a cada aparato** |

**El protocolo de control, que es la pregunta del epígrafe**: **el protocolo estándar de control de
iluminación escénica sirve para CONTROLAR LA ILUMINACIÓN**, y **nada más.** **No controla servidores de
emisión, ni la señalización de cámara, ni conmuta una matriz de vídeo.**

**Las tres cosas que hay que saber de él:**

1. **Es UNIDIRECCIONAL y sin acuse.** **La mesa manda y los aparatos obedecen; nadie contesta.** **Su
   extensión bidireccional existe aparte y sirve para configurar y diagnosticar.**
2. **Se organiza en UNIVERSOS de canales.** **Cada aparato ocupa tantos canales como funciones tenga**
   —intensidad, giro, inclinación, color, forma—, **y una luminaria robotizada gasta muchos.** **De
   ahí que una instalación grande necesite varios universos.**
3. **Hoy viaja sobre RED.** **Los protocolos que lo encapsulan sobre red de paquetes permiten llevar
   muchos universos por un solo cable**, con **la ventaja y el riesgo de compartir infraestructura con
   los datos.**

**Y las dos observaciones de oficio sobre los reguladores, que son las que tocan a un ingeniero:**

1. **Un regulador de fase recorta la onda y ENSUCIA la red.** **Produce armónicos que cargan el neutro
   y perturban a otros equipos**, y **por eso una instalación de plató se proyecta contando con
   ellos.**
2. **Las luminarias de diodos han cambiado el problema, no lo han quitado.** **Consumen mucho menos y
   no calientan igual**, pero **su fuente conmutada también genera armónicos**, y **su parpadeo puede
   batir con la cadencia de la cámara si su frecuencia de regulación no es adecuada.** **Ése es hoy el
   fallo más frecuente de una iluminación nueva mal elegida.**

## 3. Los equipos de medida de vídeo

**El instrumental que el enunciado nombra**, con **qué mide cada uno y —lo que más se pregunta— cuál
sirve para qué:**

| Instrumento | Qué muestra | Para qué se usa |
|---|---|---|
| **MONITOR DE FORMA DE ONDA** | **La señal en el tiempo**, con su nivel | **Exposición**: niveles de negro, blanco y recorte |
| **VECTORSCOPIO** | **La CROMINANCIA en un plano polar**: matiz en el ángulo, saturación en el radio | **Medir el color**: matiz, saturación y errores de matriz |
| **RASTERIZADOR** | **Lo mismo, calculado y presentado en un monitor de datos** | Es la forma moderna de los dos anteriores |
| **Monitor de estado del enlace** | **Errores de la interfaz, comprobaciones de redundancia, datos auxiliares** | **Diagnóstico de enlace** |
| **Analizador de flujo** | **La estructura de un flujo de transporte o de red** | Diagnóstico de emisión y de red |
| **Generador de PATRONES** | **Señales de prueba conocidas** | **Ajuste y verificación** |

**La pregunta directa que un examen hace de esta tabla**: **el equipo con el que se mide la
CROMINANCIA de una señal de vídeo es el VECTORSCOPIO.** **No un «medidor de tensión de color», que no
existe con ese nombre; ni un analizador de espectro, que es de radiofrecuencia; ni un monitor de forma
de onda, que muestra el nivel en el tiempo y no el color en un plano polar.**

**Y la regla que separa los dos instrumentos clásicos y que hay que llevar aprendida**: **la forma de
onda es para la LUZ y el vectorscopio para el COLOR.** **Se usan juntos y responden preguntas
distintas.**

**Las SEÑALES DE PRUEBA, que es la otra parte del epígrafe:**

| Señal | Para qué |
|---|---|
| **Barras de color** | **Referencia de nivel y de color**: la señal de ajuste clásica |
| **Rampa y escalera** | **Linealidad** del canal |
| **Multiburst** | **Respuesta en frecuencia** |
| **PATOLÓGICA** | **El caso PEOR para un enlace digital** |

**Y qué es exactamente la señal patológica, porque es la pregunta**: **una señal construida a propósito
para poner al enlace digital en su peor situación**, y **sirve para CHEQUEAR UN CANAL DIGITAL DE
TELEVISIÓN EN ALTAS Y EN BAJAS FRECUENCIAS.** **Tiene dos partes**: **una que produce el máximo
contenido de baja frecuencia —muy pocas transiciones, que estresa la recuperación de reloj y el
acoplamiento— y otra que produce el máximo de alta frecuencia.**

**Y por qué las otras tres opciones no son**: **no corrige retardos entre crominancia y luminancia
—eso es otra medida—, ni corrige aberraciones cromáticas de las lentes —eso es óptico y se hace con
carta—, ni comprueba la fase entre parejas de audio —eso lo hace un medidor de correlación, del tema
21—.**

**Y la lectura de oficio que hay que dar**: **un enlace que pasa la señal patológica pasa cualquier
cosa.** **Por eso es la prueba de aceptación de una instalación de vídeo digital**, y **por eso un
enlace que funciona con imagen normal y falla con la patológica está al límite aunque parezca sano.**

## 4. El equipamiento auxiliar de vídeo

**Lo que el enunciado llama auxiliar y que es la mitad de un rack:**

| Equipo | Qué hace |
|---|---|
| **DISTRIBUIDOR** | **Una entrada, varias salidas idénticas**, regeneradas |
| **CONVERSOR de formato o de norma** | **Cambia resolución, cadencia o barrido** |
| **EMBEBEDOR y DESEMBEBEDOR** | **Mete el audio dentro de la señal de vídeo y lo saca** |
| **CONVERSOR de interfaz** | **Entre coaxial, fibra y red** |
| **SINCRONIZADOR de cuadro** | **Alinea una señal ajena a la referencia de la casa** |
| **REGENERADOR y ecualizador de cable** | **Recupera una señal que ha viajado mucho** |
| **Generador de RETARDO** | **Alinea audio con vídeo** |

**Los dos que más se preguntan, con lo que hay que saber:**

1. **El EMBEBEDOR es lo que permite que audio y vídeo viajen por un solo cable.** **Mete el audio en
   el espacio de datos auxiliares del borrado**, que es lo que el tema 5 explicó. **Y su compañero
   saca el audio para tratarlo aparte.** **La regla de oficio**: **embeber es cómodo y desembeber
   siempre cuesta un proceso**, así que **conviene decidir pronto por dónde viaja cada audio.**
2. **El SINCRONIZADOR DE CUADRO es lo que hace utilizable una señal de fuera.** **Una señal que viene
   de otra casa no está enganchada a la referencia de ésta**, y **sin sincronizar, al conmutarla
   salta.** **Es la pieza que permite meter en un directo una señal ajena.**

**Y la aritmética de distribución que esta ocupación plantea como problema, con su razonamiento**: **si
en un estudio se maneja una señal de ultraalta definición REPARTIDA POR CUADRANTES —es decir, en cuatro
enlaces— y hay que llevarla a TRES monitores**, hacen falta **CUATRO distribuidores de al menos TRES
salidas cada uno.**

**La regla que lo resuelve, y hay que enunciarla porque es lo que un examen quiere**: **la señal son
cuatro enlaces independientes y cada uno hay que repartirlo a los mismos tres destinos**, así que
**cuadrantes por un lado y destinos por otro**: **un distribuidor por cuadrante, con tantas salidas
como destinos.** **Quien piense en un solo distribuidor de cuatro salidas está confundiendo los
cuadrantes de la señal con los destinos.**

## 5. La medida de audio

**Los instrumentos, y qué contesta cada uno:**

| Instrumento | Qué mide |
|---|---|
| **Vúmetro** | **Nivel con respuesta lenta**: se parece a la sensación de volumen |
| **Picómetro** | **Nivel de pico**: lo que puede saturar |
| **Medidor de SONORIDAD** | **Cuán fuerte suena de verdad**, integrado en el tiempo |
| **MEDIDOR DE CORRELACIÓN o de fase** | **Si los dos canales de un estéreo están en FASE o en contrafase** |
| **Analizador de espectro de audio** | Reparto de energía por frecuencia |
| **Sonómetro** | **Nivel acústico en la sala**, no en la señal |

**La pregunta directa**: **para detectar si una señal estéreo está en fase o en contrafase se usa el
MEDIDOR DE CORRELACIÓN.** **No un vúmetro ni un picómetro estéreo, que miden nivel y darían lo mismo
en fase que en contrafase; ni un sonómetro, que mide la sala.**

**Y por qué importa, que es la lectura de oficio**: **dos canales en contrafase suenan bien en estéreo
y DESAPARECEN al sumarlos a mono.** **Como una parte del público oye la emisión en mono, un problema de
fase que nadie detecta en el control se convierte en un audio que se apaga en casa.** **Por eso la
compatibilidad mono se comprueba siempre**, y **eso enlaza con el tema 21.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ningún nivel de referencia de audio, ninguna sonoridad objetivo, ninguna
   frecuencia de muestreo, ningún número de canales de un universo de control de iluminación, ninguna
   potencia de luminaria y ninguna temperatura de color.** **Son dato de recomendación y de
   fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.**
2. **Las cuatro respuestas que la plantilla oficial de esta ocupación confirma —la señal patológica
   como comprobación del canal digital en altas y bajas frecuencias, los cuatro distribuidores de tres
   salidas, el protocolo de control de iluminación y el vectorscopio para la crominancia— se recogen
   con su razonamiento**, y **el temario declara que la confirmación viene de la plantilla, en las
   preguntas 51, 53, 75 y 96.**
3. **El convertidor de frecuencia de muestreo se nombra por su función**, y **la respuesta a ese caso
   la confirma la plantilla en la pregunta 64**; **el temario añade por qué las otras tres salidas no
   valen.**
4. **Este tema NO nombra ningún fabricante, ningún modelo de mesa, de regulador ni de instrumento, y
   ningún protocolo por su versión.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **el audio,
   sus formatos y su transporte, al tema 21**; **la señal y sus datos auxiliares, al tema 5**; **las
   salas donde vive este equipamiento, al tema 13**; **el reparto de ultraalta definición por cuatro
   enlaces, al tema 8**; **y la instalación eléctrica que alimenta la iluminación, al tema 24.**

**El resto del tema va como oficio y así se declara**: la idea de que éste es el equipamiento que sólo
se nota cuando falla, la estructura de una mesa por bloques, las dos distinciones entre mesas, el
razonamiento del caso de frecuencia de muestreo con el descarte de las tres opciones falsas, la regla
de una sola referencia de reloj por instalación, las tres cosas que hay que saber del protocolo de
iluminación, las dos observaciones sobre los reguladores y sobre el parpadeo de los diodos, la regla de
que la forma de onda es para la luz y el vectorscopio para el color, la explicación de qué es y para
qué sirve la señal patológica con el descarte de las otras opciones, la lectura de que un enlace que
pasa la patológica pasa cualquier cosa, lo que hay que saber del embebedor y del sincronizador de
cuadro, el razonamiento de la aritmética de distribución por cuadrantes y la explicación de por qué
importa la fase para la compatibilidad mono. **Nada de eso está en un boletín oficial ni en ninguna
fuente consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
