# Tema 15 del específico de Realización (Asistencia) · La emisión: gestión de pantallas, servidores y grafismo

Las siglas de este tema, presentadas de entrada: el banco de mezcla y efectos (**M/E**, escrito
**ME** en el examen); el programa (**PGM**, escrito **PP** en el panel); el previo (**PVW**); el
fotograma (**fr**, del inglés *frame*); el diodo emisor de luz (**LED**); la unidad de control de
cámara (**CCU**); la interfaz de propósito general (**GPI**); la corporación de radio y televisión
pública española
(**RTVE**); el Boletín Oficial del Estado (**BOE**); los efectos visuales (**VFX**, del inglés
*visual effects*); y el nombre de la empresa **EVS**, que en el examen se usa como nombre común para
el servidor de repeticiones.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> puntos 5.5, 5.6 y 5.7): «5.5. Gestión de pantallas. 5.6. Soportes y software de emisión de vídeo
> digital. 5.7. Grafismo y generadores de caracteres.»

**Este tema reúne tres subpuntos del anexo porque el examen los pregunta juntos**: seis preguntas
sobre lo que sale a las pantallas del plató, lo que guarda y devuelve un servidor, y lo que dibuja un
generador de caracteres.

**Y es el primer tema del bloque específico de esta ocupación que se apoya en una norma con
rango de ley**: la **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual**, que es la que
fija cuánto tiempo hay que guardar lo emitido.

<!-- indice -->

## Índice

- [1. La gestión de pantallas](#1-la-gestión-de-pantallas)
- [2. El retardo de las pantallas y cómo se compensa](#2-el-retardo-de-las-pantallas-y-cómo-se-compensa)
- [3. Cómo se manda una señal distinta a las pantallas](#3-cómo-se-manda-una-señal-distinta-a-las-pantallas)
- [4. El servidor de vídeo](#4-el-servidor-de-vídeo)
- [5. Los programas de grafismo en directo](#5-los-programas-de-grafismo-en-directo)
- [6. La continuidad](#6-la-continuidad)
- [7. Lo que hay que guardar de lo emitido](#7-lo-que-hay-que-guardar-de-lo-emitido)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. La gestión de pantallas

**En un plató moderno el decorado es, en buena parte, pantallas**: paneles de LED, retroproyección,
monitores empotrados. Y esas pantallas **no enseñan el programa por defecto**: enseñan lo que se les
mande, y decidir qué se les manda es una tarea de realización.

Lo que puede ir en una pantalla de plató:

| Contenido | De dónde sale |
|---|---|
| **Grafismo de fondo** | Del programa de gestión de pantallas, con su propio servidor |
| **El programa** | De un bus auxiliar o de un banco M/E |
| **Una conexión exterior** | De la matriz, para «abrir una ventana» en el decorado |
| **Un vídeo** | Del servidor de vídeo |
| **El marcador o los datos** | De un sistema de datos |

**Y hay tres restricciones que hacen de esto un problema técnico y no una decisión estética:**

1. **El moiré**, que es materia del tema 7: la trama de la pantalla y la del sensor interfieren, y se
   resuelve desenfocando.
2. **El retardo**, que es el epígrafe 2: el programa que gestiona las pantallas tarda en pintar.
3. **La realimentación**: si a una pantalla que sale en imagen se le manda el programa, y el programa
   la está enseñando, se produce un túnel infinito. **Por eso a las pantallas nunca se les manda el
   programa a secas**, y de ahí el epígrafe 3.

---

## 2. El retardo de las pantallas y cómo se compensa

**Todo procesado añade retardo.** El programa que gestiona una pared de LED recibe una señal, la
escala, la reparte entre los paneles y la pinta: eso lleva unos cuantos fotogramas. Si por esa
pantalla entra una conexión en directo, **la imagen del exterior llega al plató más tarde que su
sonido**, y el resultado es un desfase visible.

**Ésta es la pregunta 33 del primer cuadernillo**, y merece resolverse paso a paso porque es el mejor
ejemplo de razonamiento técnico de todo el examen.

**El planteamiento**: un plató cuyo decorado son pantallas de LED gestionadas por un programa que
**produce un retardo de 4 fotogramas**. Se hacen conexiones en directo con exteriores **a través de
ventanas abiertas en esas pantallas**. El audio y el vídeo no van sincronizados. ¿Qué se hace?

**La respuesta oficial: retrasar la entrada de los exteriores al mezclador 4 fotogramas, mandarlos a
las pantallas por matriz y retrasar el sonido de los exteriores 4 fotogramas.**

**Por qué esas tres cosas a la vez:**

| Acción | Qué corrige |
|---|---|
| **Mandar el exterior a las pantallas por matriz**, no por un auxiliar del mezclador | Que la señal llegue a la pantalla **por el camino más corto**, sin pasar por el mezclador: así **el único retardo que sufre es el del programa de pantallas**, y es un retardo conocido y constante |
| **Retrasar 4 fotogramas la entrada del exterior al mezclador** | Que **la imagen que el mezclador toma del exterior coincida con la que se está viendo en la pantalla del plató**. Las cámaras del plató filman la pantalla, que va 4 fotogramas retrasada; si el mezclador tuviera el exterior sin retrasar, al cortar de la pantalla al exterior habría un salto de 4 fotogramas |
| **Retrasar 4 fotogramas el sonido del exterior** | Que **el sonido acompañe a la imagen**, que es lo que el enunciado pide |

**Las tres opciones falsas fallan cada una por un sitio.** Las dos primeras mandan la señal a las
pantallas **por un auxiliar del mezclador** —añadiendo el retardo del mezclador al del programa de
pantallas, en lugar de evitarlo— y además **no tocan el sonido**, con lo que dejan sin resolver el
problema que el enunciado plantea; y una de ellas, la b), **adelanta** la entrada en lugar de
retrasarla, que es imposible: **una señal no se puede adelantar, sólo se puede retrasar lo demás**.
La d) manda la señal al programa de pantallas por un auxiliar, con lo que vuelve a meter el retardo
del mezclador por el camino que se quería evitar.

**La regla general que hay que llevarse de aquí: en televisión, sincronizar es siempre retrasar lo
que va adelantado.** Nunca se adelanta nada, porque nadie sabe lo que va a pasar dentro de cuatro
fotogramas.

**Y la aritmética que hace falta para hablar con el técnico de sonido**: a 25 fotogramas por segundo,
**un fotograma son 40 milisegundos**. Cuatro fotogramas son **160 milisegundos**. Es el cálculo que
la pregunta 34 del tema 16 pide expresamente.

---

## 3. Cómo se manda una señal distinta a las pantallas

**La pregunta 31 del primer cuadernillo plantea el caso más frecuente de una retransmisión
deportiva**: hay que mandar la señal del programa a las pantallas del pabellón durante todo el
evento, **pero sin que se vean las repeticiones ni los vídeos**.

**Es un requisito real y tiene una razón**: una repetición en la pantalla del pabellón puede provocar
protestas del público contra una decisión arbitral, y los reglamentos deportivos lo prohíben.

**La respuesta oficial: enviar a las pantallas otro banco M/E distinto del programa, enlazarlo al
programa con un *link* y cambiar el mapeado de ese banco para que no tenga los vídeos.**

**Cómo funciona, pieza por pieza:**

1. **Otro banco M/E**, del tema 10. Se construye una segunda salida completa, independiente del
   programa.
2. **Un *link* al programa.** El banco sigue automáticamente al de programa: lo que el realizador
   pincha en programa se pincha solo en el otro banco, **sin que nadie tenga que operarlo**.
3. **Un mapeado distinto.** El mapeado es la correspondencia entre botones y fuentes, y es un atributo
   por banco. **Si en ese banco el botón donde el programa tiene el servidor de repeticiones apunta a
   otra cosa** —a la cámara máster, por ejemplo—, cuando el programa pinche la repetición, la pantalla
   pinchará la cámara.

**Con eso se cumple lo que el enunciado pide: la pantalla lleva el programa siempre, y cuando el
programa lleva una repetición, la pantalla lleva otra cosa.**

**La opción b) es la que más se le acerca y por eso conviene decir por qué no vale**: propone lo
mismo pero resolviéndolo con **una tabla de sustitución para el *link***. Una tabla de sustitución
—que existe en algunos mezcladores— sustituye fuentes al vuelo. **El problema es que es una capa
añadida al enlace, no una propiedad del banco**: lo que el enunciado pide se consigue de manera más
sencilla y más robusta cambiando el mapeado del banco, que es un ajuste permanente y que no depende
de que el enlace esté activo.

**La opción a) es ingeniosa y peligrosa**: propone otra salida de programa y una macro que cierra la
señal a negro cuando se selecciona un vídeo en previo. Falla porque **cierra la pantalla a negro en
lugar de darle contenido** —el enunciado pide mandar el programa *durante todo el evento*— y porque
**depende de que el vídeo se seleccione en previo**, cosa que no siempre ocurre: en directo se pincha
muchas veces sin pasar por previo.

**La opción d) no es una opción**: es una broma —«no hacemos nada porque lo divertido es discutir con
los árbitros»—. **Aparece en el examen y hay que anotarlo**: es un distractor humorístico, y en un
examen de cuatro opciones **reduce a tres las que hay que considerar**.

---

## 4. El servidor de vídeo

**Un servidor de vídeo es un disco duro con entradas y salidas de vídeo que graba y reproduce a la
vez.** En una retransmisión es la pieza que hace posible la repetición; en un control de continuidad
es la que emite.

**Lo que un servidor hace:**

| Función | Cómo |
|---|---|
| **Grabar** varias señales a la vez | Todas las cámaras entran y se graban en continuo |
| **Reproducir** desde cualquier punto mientras sigue grabando | Es la **repetición**: se busca hacia atrás sin dejar de registrar |
| **Cámara lenta** | Reproduciendo a menos velocidad de la de grabación |
| **Montar listas de reproducción** | Encadenar clips: un resumen, un bloque publicitario |
| **Emitir** una lista | Es lo que hace la continuidad |
| **Marcar y catalogar** | Poner puntos de entrada y salida, y nombrarlos, para encontrarlos después |

**Lo que un servidor NO hace: corregir el color de una señal.** Ésa es la respuesta oficial a la
pregunta 8 del primer cuadernillo, y la razón es de reparto de funciones: **la corrección de color es
un proceso de la señal**, y de eso se encargan el control de imagen —con las CCU—, el mezclador —con
sus correctores de entrada— o un corrector dedicado. **El servidor almacena y devuelve; no
procesa la imagen.**

Las tres opciones que sí hace —repetición de jugadas, emitir una lista de reproducción, montar un
bloque publicitario— son sus tres usos más corrientes, y por eso la pregunta se responde sabiendo
para qué sirve, no por descarte.

**Y la manera de dispararlo desde el mezclador es la GPI del tema 10.**

---

## 5. Los programas de grafismo en directo

**Un generador de caracteres, o titulador, es el equipo que dibuja los rótulos y los entrega con su
señal de llave** —el relleno y la llave del tema 10—. Los programas que hacen ese trabajo hoy hacen
mucho más: escenografías virtuales, gráficos de datos en tiempo real, realidad aumentada.

| Programa | Qué es | ¿Sirve para directo? |
|---|---|---|
| **Vizrt** | Sistema de grafismo en tiempo real; el más extendido en televisión | **Sí** |
| **Chyron** (**Chyron Prime**) | Grafismo y titulación en tiempo real; la marca es tan antigua que *chyron* se usa como nombre común del rótulo | **Sí** |
| **Ventuz** | Motor de gráficos interactivos en tiempo real | **Sí** |
| **Unreal Engine** | Motor de representación en tiempo real, del tema 16 | **Sí** |
| **After Effects** | **Programa de composición y efectos de posproducción**, de Adobe | **No**: trabaja por renderizado, no en directo |

**El programa que no permite la creación y distribución de contenidos en vivo es After Effects**, y
ésa es la respuesta oficial a la pregunta 42 del segundo cuadernillo. **La razón es su naturaleza:
After Effects compone fotograma a fotograma y entrega un fichero**; no tiene entrada de vídeo en
directo ni salida a la que un mezclador pueda enchufarse. Es la herramienta con la que **se preparan
antes** las cabeceras y las ráfagas que después dispara un servidor.

**Y una errata del cuadernillo que hay que anotar**: la opción a) está escrita **«Chayron Prime»**, y
la marca se llama **Chyron**. No afecta a la respuesta —la opción sigue siendo reconocible y sigue
siendo un programa de directo, es decir, sigue siendo falsa— pero **queda constancia**.

---

## 6. La continuidad

**La continuidad es el área que emite el canal.** No hace programas: **hace lo que va entre los
programas** y garantiza que el canal no se quede en negro.

Lo que sale de continuidad:

- **Las cortinillas y la identidad corporativa** del canal: la mosca, las caretas, las cabeceras.
- **Las autopromociones.**
- **La publicidad**, en sus bloques.
- **El enlace entre programas**: la entrada y la salida de cada uno.
- **Los avisos**: la señalización de contenido, los rótulos de servicio.

**El área destinada a incrustar o emitir las imágenes que constituyen la identidad corporativa de la
cadena es el área de continuidad.** Ésa es la respuesta oficial a la pregunta 13 del segundo
cuadernillo, y las tres opciones falsas son áreas reales de la casa con otro cometido: **realización**
hace los programas, **posproducción** los termina y «área de emisión» es un nombre general que
englobaría a la continuidad y a lo que va detrás.

**La continuidad es también el último eslabón del recorrido del tema 14**: la señal del programa,
después de pasar por el control central, llega a la continuidad del canal y de ahí a la red de
difusión.

---

## 7. Lo que hay que guardar de lo emitido

Ésta es la única pregunta de este tema que tiene respuesta en una ley, y conviene resolverla con la
ley delante. La norma es la **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual** (BOE
núm. 163, de 8 de julio de 2022), y la obligación de conservar está en su artículo 156, dentro del
régimen sancionador.

**Artículo 156**, apartado 2: los sujetos responsables por las infracciones «deberán **conservar
durante un plazo de seis meses** a contar desde la fecha de puesta a disposición del público por
primera vez **los programas y contenidos audiovisuales, incluidas las comunicaciones comerciales** y
**registrar los datos** relativos a dichos programas y contenidos audiovisuales, incluidas las
comunicaciones comerciales».

Tres cosas dice ese apartado y las tres importan. Qué se guarda: los programas y contenidos
audiovisuales, incluidas las comunicaciones comerciales; es decir, lo emitido tal cual salió, con su
publicidad dentro. Cuánto tiempo: seis meses, contados desde la primera puesta a disposición del
público. Y para qué: el apartado empieza diciendo «a los efectos de lo previsto en el apartado
anterior», que es el de la responsabilidad por infracciones, así que su finalidad es poder comprobar
lo que se emitió si alguien lo denuncia.

Apartado 3, que es la salvedad que acompaña a esa responsabilidad: no incurre en responsabilidad
administrativa el prestador que emita «comunicaciones comerciales audiovisuales elaboradas por
personas ajenas al prestador» que infrinjan la normativa de publicidad. **No obstante**, el prestador
«habrá de **cesar en la emisión** de tal comunicación comercial **al primer requerimiento** de la
autoridad audiovisual o de cualquier organismo de autorregulación al que pertenezca». Guardar lo emitido y responder de ello son
cosas distintas, y esta salvedad delimita la segunda.

Y el incumplimiento del deber de conservar tiene sanción propia en el catálogo de infracciones de la
misma ley, que lo describe como el incumplimiento de las obligaciones establecidas en el artículo
156.2 de conservar los programas y contenidos emitidos, incluidas las comunicaciones comerciales, y
registrar los datos relativos a ellos.

Con eso se responde la pregunta 31 del segundo cuadernillo, que pregunta qué contenido está obligado
a guardar el Archivo de RTVE durante un tiempo determinado. La respuesta oficial es «la emisión tal
cual se ha emitido», y es exactamente lo que dice ese apartado 2.

Las tres opciones falsas añaden materiales que la ley no exige. Una copia de emisión sin rótulos
—lo que en el tema 9 se llamó soporte internacional— es una práctica de mercado, no una obligación
legal: sirve para vender el programa fuera, no para responder ante la autoridad audiovisual. Los
brutos del rodaje no se emiten, y la obligación es sobre lo emitido. Y la opción que pide sólo la
copia sin rótulos deja fuera justamente lo único que la ley exige.

Hay que separar esta obligación de otras dos que la misma ley impone a RTVE y que no son la misma
cosa, porque el enunciado habla del «Archivo de RTVE» y eso invita a confundirlas.

**Artículo 71**, apartado 1: la Corporación de Radio y Televisión Española «velará por la
**conservación de los archivos históricos audiovisuales y sonoros**, de acuerdo con lo previsto en el
artículo 3 de la Ley 17/2006, de 5 de junio, de la radio y la televisión de titularidad estatal».
Apartado 2: de conformidad con el mandato-marco y el contrato-programa, «**garantizará el acceso** a
los archivos históricos audiovisuales y sonoros».

**Artículo 152**, apartado 1: los archivos audiovisuales de la Corporación «tendrán una **protección
especial**», y la Corporación «velará por su conservación y la cesión de estos archivos para fines de
investigación y su uso institucional o comercial». Apartado 2: «Se **fomentará el archivo** de los
programas audiovisuales por parte de los prestadores del servicio de comunicación audiovisual, así
como el acceso a los mismos para fines de investigación y educativos.»

Las tres obligaciones son distintas y conviven:

| Artículo | Qué obliga | Plazo |
|---|---|---|
| 156, apartado 2 | Conservar lo emitido, con su publicidad, para responder de ello | Seis meses |
| 71 | Velar por la conservación de los archivos históricos y garantizar el acceso | Indefinido |
| 152 | Protección especial de los archivos audiovisuales de la Corporación, y fomento del archivo en los demás prestadores | Indefinido |

La pregunta habla de «un tiempo determinado», y el único de los tres artículos que fija un plazo es
el 156. Ésa es la pista que resuelve el enunciado.

---

## 8. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 8 | primero | Qué NO hace un servidor de repeticiones | c) Corregir el color de una señal ✔ |
| 31 | primero | Cómo mandar el programa a las pantallas sin repeticiones | c) Otro M/E enlazado, con el mapeado cambiado ✔ |
| 33 | primero | Cómo sincronizar audio y vídeo con pantallas que retrasan | c) Retrasar entrada y sonido, y mandar por matriz ✔ |
| 13 | segundo | Área que emite la identidad corporativa | b) Área de continuidad ✔ |
| 31 | segundo | Qué está obligado a guardar el Archivo de RTVE | a) La emisión tal cual se ha emitido ✔ |
| 42 | segundo | Qué programa no sirve para directo | c) After Effects ✔ **·** con errata en otra opción |

**Las seis respuestas oficiales son correctas.**

**Dos anotaciones sobre la construcción de las preguntas:**

1. **La 42 escribe «Chayron Prime» donde la marca es Chyron.** No afecta a la respuesta.
2. **La 31 del primer cuadernillo incluye un distractor humorístico** —«no hacemos nada porque lo
   divertido es discutir con los árbitros en el pabellón al ver las Repeticiones»—. Es la única
   opción de todo el examen escrita en broma, y en la práctica **deja la pregunta en tres opciones**.

**Y la observación de fondo de este tema: sus dos preguntas más difíciles —la 31 y la 33 del primer
cuadernillo— no se responden sabiendo definiciones, sino sabiendo montar una solución.** Piden
combinar tres o cuatro recursos del mezclador y de la matriz para cumplir un requisito de producción.
**Son las preguntas que más se parecen al trabajo real de la ocupación**, y las dos están en el mismo
llamamiento.

---

## 9. Trazabilidad

**Una norma con rango de ley sostiene el epígrafe 7**, y es del primer nivel de la jerarquía de
fuentes —norma del BOE vigente en la fecha de corte del 21 de diciembre de 2022—:

| Norma | Artículos citados | Qué sostiene | Fichero |
|---|---|---|---|
| **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual** (BOE núm. 163, de 8 de julio de 2022) | **156.2**, **71.1** y **152.1** | El plazo de **seis meses** para conservar lo emitido con su publicidad; la obligación de RTVE de velar por sus archivos históricos; y la protección especial de sus archivos audiovisuales | `fuentes/BOE-A-2022-11311.md` |

**Las tres citas entre comillas están tomadas del texto consolidado del BOE en su redacción vigente
en la fecha de corte**, y la ley es la misma que el bloque general de esta convocatoria ya usa.

**Lo que va como oficio y así se declara**: la tabla de contenidos posibles de una pantalla de plató,
las tres restricciones del epígrafe 1, el razonamiento de compensación de retardo del epígrafe 2 —que
se deduce de las cifras del propio enunciado y de la regla de que sólo se puede retrasar—, el montaje
con banco enlazado y mapeado distinto del epígrafe 3, la tabla de funciones de un servidor de vídeo,
la de programas de grafismo y la descripción de la continuidad.

**Sobre los programas de grafismo del epígrafe 5 hay que hacer una declaración expresa.** Sus fichas
de fabricante **no se han consultado**: la tabla dice de cada uno lo que es y si trabaja en directo,
y eso es conocimiento corriente del sector. **Lo único que la pregunta 42 exige** —que After Effects
no genera ni distribuye contenido en vivo— **se sostiene en la naturaleza del programa**, que compone
por renderizado y entrega un fichero.

**Y una nota sobre el nombre del servidor.** El examen escribe «Disco Duro (EVS)» y usa **EVS** como
si fuera un nombre común. **EVS es una marca**, la del fabricante belga cuyos servidores de
repeticiones dominan el mercado; el nombre común es **servidor de vídeo** o **servidor de
repeticiones**. Este tema usa el nombre común y señala la marca donde el examen la usa. La ficha de
producto de EVS **está cerrada**, comprobado con agente de navegador, según consta en
`fuentes/fabricantes/README.md`.
