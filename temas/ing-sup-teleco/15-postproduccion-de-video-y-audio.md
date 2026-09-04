# Tema 15 del específico de Ingeniería Superior · Telecomunicación · Postproducción de vídeo y de audio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 17 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el flujo y el equipamiento de postproducción, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Lo que decide el punto** | **El ORDEN de las operaciones.** Etalonar un plano que después se cae es tiempo tirado, y conformar al final es lo que impide que el resultado dependa de la copia ligera |
| **Extensión** | **2.285 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la edición no lineal (**NLE**); la lista de
decisiones de montaje (**EDL**); el formato de intercambio de material (**MXF**) y el de proyecto
avanzado (**AAF**); la tabla de consulta de color (**LUT**); el alto rango dinámico (**HDR**) y el
estándar (**SDR**); la estación de trabajo de audio digital (**DAW**); la sonoridad integrada en
unidades relativas a escala completa (**LUFS**); el pico verdadero (**dBTP**); el decibelio a escala
completa (**dBFS**); la copia de trabajo ligera (**proxy**); el conformado; y el código de tiempo
(**TC**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 17):
> «Elementos de producción (VII): Postproducción video y audio. Equipamiento. Diagrama a bloques.
> Interconexión.»

**Es la sala donde el material se convierte en programa**, y **hay que decir de entrada qué la
distingue de la edición de informativos del tema 14**: **allí manda el reloj y aquí manda el
resultado.** **La misma operación —cortar dos planos— se hace en un minuto en informativos y en media
hora en postproducción, y las dos están bien.**

**Y la idea que ordena el punto**: **la postproducción es una CADENA DE PROCESOS con un orden que
importa.** **Montar, etalonar, mezclar y masterizar no son cuatro tareas independientes: son cuatro
etapas, y hacerlas fuera de orden obliga a repetirlas.**

<!-- indice -->

## Índice

- [1. El flujo de trabajo](#1-el-flujo-de-trabajo)
- [2. El equipamiento](#2-el-equipamiento)
- [3. El etalonaje y las conversiones de rango](#3-el-etalonaje-y-las-conversiones-de-rango)
- [4. La mezcla y el masterizado de audio](#4-la-mezcla-y-el-masterizado-de-audio)
- [5. La interconexión](#5-la-interconexión)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. El flujo de trabajo

**Las etapas, en el orden en que se hacen y con lo que produce cada una:**

| Etapa | Qué se hace | Qué produce |
|---|---|---|
| **1 · INGESTA y copias ligeras** | **Meter el material y generar la copia de montaje** | El proyecto poblado |
| **2 · MONTAJE** | **Decidir qué se ve y en qué orden** | **La lista de decisiones**, sobre copia ligera |
| **3 · CONFORMADO** | **Rehacer ese montaje sobre el material de alta calidad** | La secuencia en calidad de máster |
| **4 · ETALONAJE** | **Ajustar el color y el rango** | La imagen ya ajustada |
| **5 · GRAFISMO y efectos** | **Rótulos, composición, retoque** | Los elementos incrustados |
| **6 · MEZCLA de audio** | **Niveles, ecualización, dinámica, espacialización** | La banda sonora |
| **7 · MASTERIZADO y entrega** | **Ajustar a la norma de entrega y empaquetar** | **El máster y sus versiones** |

**Y las tres reglas del orden, que son lo que hay que saber razonar:**

1. **El montaje se cierra antes de etalonar.** **Etalonar un plano que después se cae es tiempo
   tirado**, y **un cambio de montaje después del etalonaje obliga a revisar los planos vecinos.**
2. **La mezcla se hace sobre imagen CERRADA.** **El audio se ajusta a lo que se ve**, y **un cambio de
   duración desplaza todo lo que va detrás.**
3. **El conformado va ANTES del acabado y no después.** **Etalonar sobre copia ligera y confiar en que
   el original responda igual es como se descubre, al final, que no responde.**

**Y la observación de oficio que explica por qué se trabaja así**: **la copia ligera existe para poder
montar sin mover el material pesado**, y **el conformado existe para que el resultado no dependa de esa
copia.** **Lo que ata las dos es el CÓDIGO DE TIEMPO**, y **si copia y original no lo comparten, el
conformado no cuadra.** **Ése es el fallo más caro de una postproducción mal preparada.**

## 2. El equipamiento

**La sala de postproducción de vídeo:**

| Equipo | Qué hace |
|---|---|
| **Estación de EDICIÓN** | El programa de montaje y su máquina |
| **ALMACENAMIENTO compartido** | **Que varios puestos trabajen sobre el mismo material**: tema 18 |
| **MONITOR DE REFERENCIA calibrado** | **Es lo que hace posible el etalonaje** |
| **Panel de ETALONAJE** | Mandos giratorios y bolas de control para el color |
| **Monitor de forma de onda y vectorscopio** | **La medida objetiva** que acompaña al ojo: tema 12 |
| **Superficie de control** | Mandos físicos para operaciones frecuentes |
| **Nodos de RENDERIZADO** | Calcular lo que no se reproduce al vuelo |

**La sala de postproducción de audio:**

| Equipo | Qué hace |
|---|---|
| **Estación de trabajo de audio** | El programa de mezcla y su máquina |
| **Superficie de control** | Faders y mandos físicos |
| **MONITORADO calibrado** | **Cajas y sala tratada acústicamente** |
| **MEDIDORES de nivel y de SONORIDAD** | **Lo que decide la entrega**: tema 12 |
| **Sala de LOCUCIÓN** | Grabación de voz |
| **Biblioteca de efectos y de músicas** | Con sus derechos documentados |

**Y las dos condiciones que un ingeniero tiene que garantizar y que no se ven en ninguna lista de
equipos:**

1. **La SALA.** **Un monitor de referencia en una sala con luz de ventana no sirve, y unas cajas en una
   sala sin tratar tampoco.** **La sala es parte del instrumento**: iluminación de ambiente controlada
   y neutra en vídeo, y acústica tratada en audio.
2. **La CALIBRACIÓN con fecha.** **Un monitor y una escucha se calibran periódicamente y se anota
   cuándo.** **Sin eso, dos salas de la misma casa entregan cosas distintas y nadie sabe cuál está
   bien.**

## 3. El etalonaje y las conversiones de rango

**Qué es etalonar**: **decidir cómo se ve la imagen**, en dos capas: **igualar** —que los planos de una
secuencia casen entre sí— y **crear** —darle una intención—.

**Las herramientas, de menos a más selectivas:**

| Herramienta | Qué hace |
|---|---|
| **Ajustes PRIMARIOS** | **Actúan sobre toda la imagen**: nivel, contraste, temperatura, saturación |
| **Ajustes SECUNDARIOS** | **Sobre una parte**: un rango de color, una zona, un objeto seguido |
| **Máscaras y seguimiento** | Delimitar dónde actúa cada ajuste |
| **Tablas de consulta** | **Conversiones de espacio y de curva**, y aspectos guardados |

**Y la parte que esta ocupación pregunta en su cuadernillo, que es la conversión entre rangos**: **pasar
material de alto rango dinámico a rango estándar exige una TABLA DE CONSULTA**, y **no se resuelve solo
por transcodificar.**

**El razonamiento del caso completo**, que es lo que hay que saber explicar: **si hay que entregar en
alta definición y con códec de emisión un material grabado en ultraalta definición, con alto rango
dinámico y con un códec de producción, hay tres operaciones y su orden importa**:

| Orden | Operación | Por qué ahí |
|---|---|---|
| **1** | **Aplicar la tabla de consulta**, de alto rango a rango estándar | **Se decide sobre el material con más información** |
| **2** | **Reducir la resolución** a alta definición | **Sobre material ya en el rango de destino** |
| **3** | **Transcodificar** al códec de entrega | **Al final**: es la operación que pierde, y no conviene arrastrar sus pérdidas |

**Y la opción que hay que saber descartar**: **decir que no hace falta tabla de consulta porque el
material de alto rango «tiene más información de color» confunde tener información con saber qué hacer
con ella.** **Un material de alto rango visto o codificado como rango estándar sin conversión sale
lavado y con los brillos comprimidos mal**, no mejor. **Y decir que la conversión no es técnicamente
posible es sencillamente falso.**

**Y el aviso de método sobre las tablas de consulta, que ya se dio en el tema 8 y aquí tiene su sitio
práctico**: **una conversión de rango es una decisión creativa disfrazada de operación técnica.** **Se
elige una tabla, se aprueba, se documenta y se aplica la misma a toda la producción**, porque **dos
tablas distintas en el mismo programa se ven.**

## 4. La mezcla y el masterizado de audio

**Las etapas de la mezcla:**

| Etapa | Qué se hace |
|---|---|
| **Edición y limpieza** | **Quitar ruidos, cuadrar sincronía, reparar** |
| **Equilibrio** | **Niveles relativos entre diálogo, ambiente, efectos y música** |
| **Procesado** | **Ecualización, dinámica y reverberación** |
| **Espacialización** | **Reparto entre canales**, en estéreo o en multicanal |
| **MASTERIZADO** | **Ajustar a la norma de entrega y comprobarlo** |

**Y la regla que ordena una mezcla de televisión, declarada como oficio**: **manda el DIÁLOGO.**
**Todo lo demás se coloca respecto a él**, porque **el espectador que no entiende lo que se dice apaga.**

**El masterizado a norma de entrega**, que es la parte que decide si un programa se acepta:

| Magnitud | Qué es |
|---|---|
| **SONORIDAD integrada** | **Cuán fuerte suena el programa entero**: es lo que se normaliza |
| **Rango de sonoridad** | **Cuánto varía** entre lo más flojo y lo más fuerte |
| **PICO VERDADERO** | **El máximo real de la señal reconstruida**, que puede superar al máximo de las muestras |

**Y las dos cosas que hay que saber decir de ellas:**

1. **La normalización moderna es por SONORIDAD, no por pico.** **Ajustar al pico dejaba programas con
   niveles percibidos muy distintos**, y **eso es lo que producía el salto de volumen entre programa y
   publicidad.** **Normalizar por sonoridad lo resuelve.**
2. **El pico verdadero NO es el pico de las muestras.** **Al reconstruir la señal analógica entre
   muestras pueden aparecer valores más altos que cualquier muestra**, y **por eso se deja margen: una
   señal que llega al máximo digital puede saturar el convertidor de quien la reproduce.**

**El temario no da ninguno de esos valores objetivo**, y **lo declara**: **están en las recomendaciones
de entrega, que no se han consultado.**

## 5. La interconexión

**Con qué habla una sala de postproducción, que es lo que el enunciado pide:**

| Con quién | Para qué |
|---|---|
| **ALMACENAMIENTO compartido** | **Es de donde lee y a donde escribe**: tema 18 |
| **Gestión de medios y archivo** | **Buscar material y devolver el máster catalogado** |
| **INGESTA** | **Recibir el material rodado** |
| **Salas de grafismo** | **Intercambiar elementos y composiciones**: tema 16 |
| **Continuidad y emisión** | **Entregar el máster listo para su hora**: tema 13 |
| **La red de la casa** | **Por donde va todo eso**: tema 20 |

**Y las dos reglas de intercambio que evitan el trabajo perdido:**

1. **El proyecto se intercambia con un formato de PROYECTO, no con un vídeo.** **Un formato de
   intercambio de proyecto lleva las decisiones —cortes, pistas, niveles, referencias— y permite
   seguir trabajando; un vídeo plano no.**
2. **Se pacta la ENTREGA antes de empezar.** **Códec, contenedor, estructura de pistas de audio,
   sonoridad, código de tiempo de inicio, cabecera y metadatos.** **Descubrir al final que la entrega
   pedía otra estructura de audio cuesta rehacer la mezcla.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna cifra de sonoridad objetivo, ningún límite de pico verdadero, ningún
   rango de sonoridad, ninguna tasa de códec y ningún nivel de referencia de monitorado.** **Están en
   las recomendaciones de entrega, que NO se han consultado**, y **una cifra que no se ha leído en su
   fuente no se escribe.**
2. **El orden de las tres operaciones de conversión del epígrafe 3 es el que la plantilla oficial de
   esta ocupación confirma en su pregunta 28**, y **el temario declara esa procedencia y añade el
   razonamiento de por qué ese orden y no otro.**
3. **Este tema NO nombra ningún programa de edición, de etalonaje o de audio, ningún fabricante y
   ningún panel de control por su modelo.**
4. **Los formatos de intercambio se nombran por su función y por su sigla de uso común**, y **el
   temario NO les atribuye ninguna estructura interna ni ninguna versión**: **no se han consultado sus
   especificaciones.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la edición y
   las copias ligeras, al tema 11**; **la medida de vídeo y de audio, al tema 12**; **las salas y la
   entrega a emisión, al tema 13**; **la edición de informativos, al tema 14**; **el grafismo, al tema
   16**; **el almacenamiento compartido, al tema 18**; **los estándares de alto rango dinámico, al
   tema 8**; **y el audio y sus formatos, al tema 21.**

**El resto del tema va como oficio y así se declara**: la distinción entre postproducción e informativos
—allí manda el reloj y aquí el resultado—, la idea de que la postproducción es una cadena con un orden
que importa, las tres reglas del orden y la observación de que el código de tiempo es lo que ata copia
y original, las dos condiciones invisibles de la sala y de la calibración con fecha, la separación
entre igualar y crear en el etalonaje, el razonamiento completo del orden de las tres operaciones de
conversión y el descarte de las opciones falsas, el aviso de que una conversión de rango es una
decisión creativa disfrazada de técnica, la regla de que en televisión manda el diálogo, las dos cosas
que hay que saber de la normalización por sonoridad y del pico verdadero, y las dos reglas de
intercambio sobre el formato de proyecto y sobre pactar la entrega antes de empezar. **Nada de eso está
en un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta
como si lo estuviera.
