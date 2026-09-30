# Tema 9 del específico de Ayudante de Realización · Mezcladores de vídeo, efectos, transiciones, incrustaciones, chroma, DVE y señalización técnica

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Ayudante de Realización · punto 9 |
| Sirve para | Ayudante de Realización de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Sin norma que regule el mezclador, su uso ni su señalización. Documentación de fabricante: manual en español de los mezcladores Blackmagic Design ATEM (edición de diciembre de 2024), con su anexo en inglés «Blackmagic Embedded Tally Control Protocol»; TSL Products, «TSL UMD Protocol» (documento fechado el 19-09-2009). Especificación de la AMWA: NMOS IS-07. Norma de enseñanza, no del oficio: Real Decreto 1680/2011, título de Técnico Superior en Realización de proyectos audiovisuales y espectáculos (módulos 0905 y 0910). Catálogo de cualificaciones: IMS077_3 «Asistencia a la realización en televisión» (INCUAL). Lo propio de la casa: *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004). Manual universitario: F. J. Mateu Torres, *Fundamentos teóricos de la edición y el montaje audiovisual* (Editorial UMH, 2024). Documentación de Adobe (Premiere) y Blackmagic Design (DaVinci Resolve 21) sobre transiciones. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Manual ATEM en su edición de diciembre de 2024 (descargado el 03-09-2026; releído el 24-09-2026 en el texto tomado del tema 9 de Realizador/a y el 29-09-2026 en lo añadido sobre señalización). Protocolo TSL UMD en su documento de 2009, el único de TSL que se ha leído (descargado el 29-09-2026; no se ha confirmado si hay versión posterior). Real Decreto 1680/2011 en su texto de 2011: el Real Decreto 500/2024 lo modifica, pero no toca los módulos que se citan. IMS077_3, documento publicado del INCUAL (publicación: Orden PCI/797/2019), leído el 29-09-2026. Libro de Estilo de 2004, leído el 24-09-2026 |
| Extensión | 16.400 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial del Estado (BOE); Boletín Oficial de la Junta de Andalucía
(BOJA); real decreto (RD). En las citas del RD 1680/2011, cada resultado de
aprendizaje (RA) del módulo va con la letra de su criterio de evaluación. El *Libro de Estilo de Canal
Sur Televisión y Canal 2 Andalucía* se cita como Libro de Estilo o LE.

Los términos técnicos del tema, presentados de entrada: el banco de mezcla y efectos (M/E, del inglés
*mix/effects*); el generador de efectos digitales (DVE, del inglés *digital video effects*, y DME, del inglés *digital
multi effects*, en la nomenclatura de otros fabricantes); la
composición posterior (DSK, del inglés *downstream keyer*) y su pareja anterior (USK, del inglés
*upstream keyer*); la imagen dentro de imagen (PinP o PIP, del inglés *picture in picture*); la
mezcla aditiva total (FAM, del inglés *full additive mix*) y la mezcla no aditiva (NAM, del inglés
*non-additive mix*); la interfaz de propósito general (GPI, del inglés *general purpose interface*);
el previo (PVW, del inglés *preview*) y el programa (PGM o PP); la interfaz digital serie (SDI, del
inglés *serial digital interface*); el fundido a negro (FTB, del inglés *fade to black*); el
fotograma (fr, del inglés *frame*), que es como el mezclador cuenta las pausas y las duraciones; la
incrustación en general (llave, *key*) y la incrustación por color (croma, *chroma key*); el canal de
transparencia de una imagen (canal alfa); el pulso de sincronismo de tres niveles (*tri-level*) y la
señal de negro con sincronismos (*black burst*); la luz de aviso de cámara en antena (piloto o
*tally*); la transición animada (*stinger*, que el manual ATEM rotula STING en el panel); y los
botones del panel que el tema nombra como los rotula el fabricante, en inglés: CUT (corte), AUTO
(transición automática), BKGD (del inglés *background*, fondo), TIE (vincular), ON AIR (al aire) y PREV
TRANS (ensayar la transición en el previo). El manual universitario citado lo publica la editorial de
la Universidad Miguel Hernández (UMH). El manual
de los ATEM, en su traducción española, llama «composición» a lo que el oficio llama llave, «anticipo»
al previo, «señal principal» al programa y «visualización simultánea» al multipantalla (*multiview*):
el tema usa el vocabulario del oficio y avisa cuando cita el manual.

Los que añade la señalización técnica: la alta definición (HD, del inglés *high definition*), que aparece en nombres de monitores; el botón de llamada a los cámaras (CALL, en el panel ATEM);
la interfaz entre mezclador y pilotos de ese fabricante (*GPI and Tally Interface*); la etiqueta
electrónica bajo el monitor y el protocolo de TSL Products que la gobierna (UMD, sigla que el
documento de TSL no desarrolla); el protocolo de internet (IP) y, sobre él, los protocolos de red de datagramas (UDP, *user datagram protocol*)
y de control de transmisión (TCP/IP, *transmission control protocol / internet protocol*); las interfaces eléctricas serie RS-422 y RS-485, que el documento de TSL escribe «RS 422/ RS 485»; la
Society of Motion Picture and Television Engineers (SMPTE), cuyo formato de paquete 291M cita el
protocolo de piloto de Blackmagic, con sus identificadores de datos (DID y SDID, del inglés *data identifier* y *secondary data identifier*); la zona de datos auxiliares del borrado vertical de la señal (VANC, del inglés
*vertical ancillary*); la Advanced Media Workflow Association (AMWA) y su familia de especificaciones
de medios en red (NMOS). De la cualificación: Instituto Nacional
de las Cualificaciones (INCUAL); unidad de competencia (UC), realización profesional (RP), criterio
de realización (CR), módulo formativo (MF) y criterio de evaluación (CE).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.5, punto 9): «Mezcladores de vídeo,
> efectos, transiciones, incrustaciones, chroma, DVE y señalización técnica.»

Qué se puede preguntar: qué hace un mezclador, qué es un banco M/E y qué atributos tiene una fuente;
qué le pide la cualificación al ayudante respecto del mezclador; qué salidas lleva o no las llaves y
qué señales se graban; qué es un efecto del mezclador, qué diferencia hay entre *snapshot*, macro y
*timeline*, qué es el *clip store* y por qué un efecto programado no se retoca en marcha; qué
transiciones hay, en qué se distinguen el encadenado, la cortinilla, el fundido a color, la NAM y la
FAM, qué hacen CUT, AUTO, la palanca, los botones de próxima transición, PREV TRANS y el fundido a
negro, qué es una transición animada y qué significa cada una en el relato; cuáles son las tres
señales de una incrustación y la fórmula del compuesto, qué diferencia hay entre llave lineal y
aditiva, qué son el clip y la ganancia, la máscara, una señal premultiplicada, un *self key* y el
*show key*, qué tipos de llave hay y cuál no lo es, y qué es una llave previa y una posterior; con qué
color se hace un croma, qué controles tiene, qué es el rebase y qué pide al plató; qué parámetros
tiene un DVE, qué es el *corner pinning*, cómo se amplía sin deformar y qué es una gafa; qué es el
piloto, dónde se enciende y en qué color, a qué cámaras se enciende en unas ventanas, por qué vías
llega (contacto, retorno SDI, señal, red), qué hace el botón CALL, qué indican los bordes del
multipantalla, qué es una etiqueta UMD y el protocolo TSL, qué son el *black burst*, el *tri-level*
y el *genlock*, qué generadores de señales hay en un control y para qué sirven las barras de color.
En la prueba práctica: comprobar con el mezclador y la escaleta las entradas, los nombres, los
pilotos, las transiciones y las llaves antes de un informativo, cantar las transiciones en el directo
y resolver a quién se avisa cuando un piloto no se enciende, un croma deja bordes o un rótulo sale
mal.

<!-- indice -->

## Índice

- [Advertencia sobre las fuentes](#advertencia-sobre-las-fuentes)
- [1. Mezcladores de vídeo](#1-mezcladores-de-vídeo)
  - [Qué es un mezclador de vídeo](#qué-es-un-mezclador-de-vídeo)
  - [Lo que hace, función por función](#lo-que-hace-función-por-función)
  - [Lo que la norma de enseñanza pide saber hacer](#lo-que-la-norma-de-enseñanza-pide-saber-hacer)
  - [Lo que la cualificación pide al ayudante](#lo-que-la-cualificación-pide-al-ayudante)
  - [Los bancos de mezcla y efectos (M/E)](#los-bancos-de-mezcla-y-efectos-me)
  - [Las fuentes y sus atributos](#las-fuentes-y-sus-atributos)
  - [Las salidas y lo que se graba](#las-salidas-y-lo-que-se-graba)
- [2. Efectos](#2-efectos)
  - [Qué es un efecto en el mezclador](#qué-es-un-efecto-en-el-mezclador)
  - [Dónde se preparan](#dónde-se-preparan)
  - [Memorias: *snapshots*, macros y *timelines*](#memorias-snapshots-macros-y-timelines)
  - [La macro, según el fabricante](#la-macro-según-el-fabricante)
  - [Un efecto programado no se retoca en marcha](#un-efecto-programado-no-se-retoca-en-marcha)
  - [El *clip store*](#el-clip-store)
- [3. Transiciones](#3-transiciones)
  - [Los modos de transición](#los-modos-de-transición)
  - [Los parámetros de la cortinilla](#los-parámetros-de-la-cortinilla)
  - [NAM y FAM](#nam-y-fam)
  - [Cómo se ejecuta una transición](#cómo-se-ejecuta-una-transición)
  - [El fundido a negro](#el-fundido-a-negro)
  - [La transición animada](#la-transición-animada)
  - [Corte y transición](#corte-y-transición)
  - [Lo que significa cada recurso](#lo-que-significa-cada-recurso)
  - [Lo que el ayudante comprueba de las transiciones](#lo-que-el-ayudante-comprueba-de-las-transiciones)
  - [Errores de uso](#errores-de-uso)
- [4. Incrustaciones](#4-incrustaciones)
  - [Las tres señales de una incrustación](#las-tres-señales-de-una-incrustación)
  - [Aditivo frente a lineal](#aditivo-frente-a-lineal)
  - [Clip y ganancia](#clip-y-ganancia)
  - [La máscara de la llave](#la-máscara-de-la-llave)
  - [Las señales premultiplicadas](#las-señales-premultiplicadas)
  - [Los tipos de llave](#los-tipos-de-llave)
  - [El *self key* y el *show key*](#el-self-key-y-el-show-key)
  - [Llaves previas y posteriores](#llaves-previas-y-posteriores)
  - [Cómo entra el grafismo en el mezclador](#cómo-entra-el-grafismo-en-el-mezclador)
- [5. Chroma](#5-chroma)
  - [Qué es el croma](#qué-es-el-croma)
  - [Cualquier color sirve](#cualquier-color-sirve)
  - [Los ajustes del croma](#los-ajustes-del-croma)
  - [Lo que el croma pide al plató](#lo-que-el-croma-pide-al-plató)
  - [Croma en directo y decorado virtual](#croma-en-directo-y-decorado-virtual)
- [6. DVE](#6-dve)
  - [El generador de efectos digitales](#el-generador-de-efectos-digitales)
  - [Tres operaciones que hay que saber hacer](#tres-operaciones-que-hay-que-saber-hacer)
  - [La gafa y la composición múltiple](#la-gafa-y-la-composición-múltiple)
- [7. Señalización técnica](#7-señalización-técnica)
  - [Qué se entiende por señalización técnica](#qué-se-entiende-por-señalización-técnica)
  - [El piloto](#el-piloto)
  - [El piloto en el panel del mezclador](#el-piloto-en-el-panel-del-mezclador)
  - [Cómo llega el piloto a la cámara y a los monitores](#cómo-llega-el-piloto-a-la-cámara-y-a-los-monitores)
  - [La llamada](#la-llamada)
  - [El multipantalla](#el-multipantalla)
  - [Qué enseña, según el manual ATEM](#qué-enseña-según-el-manual-atem)
  - [Cómo se ordena](#cómo-se-ordena)
  - [Las etiquetas de los monitores: el protocolo TSL UMD](#las-etiquetas-de-los-monitores-el-protocolo-tsl-umd)
  - [La sincronización](#la-sincronización)
  - [Los generadores de señales del control](#los-generadores-de-señales-del-control)
  - [Lo que comprueba el ayudante](#lo-que-comprueba-el-ayudante)
- [Aplicación práctica: el ayudante y el mezclador en un informativo](#aplicación-práctica-el-ayudante-y-el-mezclador-en-un-informativo)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Advertencia sobre las fuentes

Ninguna norma regula cómo es un mezclador ni cómo se usa. Cada fabricante nombra los mismos recursos
con palabras distintas, y la única documentación de fabricante que se ha leído para este tema es el
manual en español de los mezcladores ATEM de Blackmagic Design; lo que se cita de él es de ese
fabricante, aunque el concepto sea común a los mezcladores profesionales. Qué mezclador tienen los
controles de Canal Sur no consta en documento publicado leído, y el tema no lo afirma.

La norma de enseñanza del título de Técnico Superior en Realización (RD 1680/2011) pone con rango de
norma qué debe saber hacer en el mezclador quien se forma para realizar, y pone expresamente en su
temario los usos narrativos de las transiciones; se cita por eso, no porque regule el oficio. El
Libro de Estilo de Canal Sur da el criterio de la casa sobre el uso de los recursos en los
informativos. Las fórmulas del compuesto, los tipos de llave, las memorias y los criterios de uso por
género son oficio y física de la señal, y así se declaran.

## 1. Mezcladores de vídeo

### Qué es un mezclador de vídeo

Un mezclador de vídeo hace tres cosas y sólo tres, aunque las haga de muchas maneras:

1. Conmutar: elegir cuál de las fuentes de entrada sale al aire.
2. Mezclar: pasar de una fuente a otra con una transición, en lugar de con un corte seco.
3. Combinar: superponer una fuente sobre otra, que es lo que se llama incrustar o *key*.

Todo lo demás —memorias, efectos digitales, generadores de color, reproductores de clips— existe para
servir a esas tres.

Dónde está en el control, quién lo opera en la RTVA, cómo es su panel, qué salidas tiene (programa,
previo, limpia, auxiliares y multipantalla), para qué sirven los buses auxiliares y cómo manda sobre
otros equipos por GPI son materia del tema 4. Aquí se estudian los recursos que el mezclador pone en
manos del realizador y cuándo se usa cada uno.

### Lo que hace, función por función

Otra manera de contarlo, que separa la composición de la incrustación y añade la automatización que
sirve a las tres funciones anteriores:

| Función | Qué significa |
|---|---|
| Conmutar | Pasar de una entrada a otra: el corte, que es la transición instantánea |
| Transicionar | Encadenado, cortinilla, fundido: pasar de una a otra con duración |
| Incrustar | Meter una imagen dentro de otra por color, por luminancia o por canal alfa |
| Componer | Reducir, colocar y superponer varias señales en el mismo cuadro: es el trabajo del DVE |
| Automatizar | Guardar una secuencia de esas operaciones y lanzarla con un botón: la macro |

### Lo que la norma de enseñanza pide saber hacer

El módulo 0905, «Procesos de realización en televisión», del RD 1680/2011 dedica un resultado de
aprendizaje entero al mezclador (RA 5): **«Mezcla las fuentes, transiciones, incrustaciones y efectos
durante la grabación o emisión del programa de televisión, mediante el mezclador, describiendo las
características funcionales y operativas de los equipos que posibilitan el control de la calidad de
la imagen.»** Su criterio e) resume la preparación de este tema: **«Se han ajustado y prefijado en el
mezclador las transiciones, cortinillas, efectos digitales e incrustaciones mediante croma,
luminancia o DSK, que se utilizarán en el programa de televisión.»**

Entre los contenidos del mismo módulo, en el bloque «Realización de programas de televisión en
multicámara», están **«Técnicas de montaje en vivo en la realización televisiva.»**, **«Realización
de transiciones. Usos expresivos y narrativos.»**, **«Incrustación de la señal.»** y **«Gráficos en
la realización de televisión.»**; y en el bloque «Mezcla de fuentes, transiciones, incrustaciones y
efectos», **«Diagrama de líneas de entrada y salida del mezclador de vídeo.»**, **«Técnicas de
configuración de entradas y salidas del mezclador de vídeo.»** y **«Técnicas de mezclado de
vídeo.»** El módulo 0910, «Medios técnicos audiovisuales y escénicos», pide evaluar los mezcladores
(RA 4): **«b) Se han evaluado las características de diversos mezcladores de vídeo y sus capacidades
en cuanto a operaciones de selección de líneas de entrada, sincronización, buses primarios y
auxiliares, transiciones, incrustaciones, DSK y efectos digitales.»**

### Lo que la cualificación pide al ayudante

El ayudante no mezcla: quién opera el mezclador en la RTVA es materia del tema 4. Lo que la
cualificación IMS077_3 le pide respecto del mezclador es comprobar, anotar y anticipar.

Antes de grabar, dos criterios de evaluación del módulo formativo MF0217_3, «Técnicas de realización
en control» (p. 18). El primero, en su parte que toca al mezclador: **«CE1.5 En el control de
realización verificar que todo el equipo está listo para la grabación comprobando que el técnico del
control de imagen ha ajustado la cámara a los parámetros de calidad pertinentes, que el técnico de
sonido ha ajustado su equipo, que el mezclador está preparado»**. El segundo, entero: **«CE1.6
Identificar las transiciones para asegurar que son las previstas para un determinado programa, con el
ritmo y los tiempos de entrada y salida adecuados.»**

Contra el parte de emisión, la unidad de competencia UC0217_3 (p. 7): la RP1 manda **«Verificar que
las duraciones, calidades, efectos, grafismos, titulaciones, músicas, efectos de sonido e iluminación
del programa de televisión son las previstas en el parte de emisión, informando de cualquier
incidencia al realizador.»**; su CR1.2, que **«Los coleos de los videos se verifican sobre el parte de
emisión comprobando que responden a las necesidades del programa, y avisando al mezclador y al
operador de sonido si fueran insuficientes.»**; y su CR1.3, que **«Las duraciones de videos, músicas,
gráficos, rótulos y efectos de imagen y sonido se comprueban, anotándolo en el parte de emisión según
criterio marcado por el departamento de realización.»**

En el directo, el CR2.1 de la misma unidad (p. 7): **«Los minutados y escaleta técnica, se siguen
asegurando la llegada al plano requerido y a los efectos y transiciones en el momento oportuno y con
precisión, anticipando las acciones del personal artístico y pies de guion, cantando los tiempos de
minutados musicales y anticipando las órdenes al equipo técnico y a los operadores de cámara.»** Cómo
se canta y se anticipa es el tema 6.

Y lo que hay que saber: entre los contenidos del MF0217_3 (p. 20) están **«5 Los generadores de
señales»** y **«6 Los paneles de interconexión, los preselectores, la matriz de conmutación»**, que
incluye **«La tituladora y los generadores de efectos.»** y **«El mezclador de vídeo.»** Los
generadores de señales se estudian en el epígrafe 7.

### Los bancos de mezcla y efectos (M/E)

Un banco M/E es un mezclador completo dentro del mezclador. Tiene su bus de programa, su bus de
previo, su módulo de transición y sus llaves, y su salida se puede usar como fuente de otro banco
o del programa. Es la pieza que permite construir una imagen compleja aparte y meterla al aire de
una vez.

El manual de los ATEM lo explica así, y merece la pena porque dice de dónde viene la idea:

> La línea de mezcladores ATEM incluye dispositivos de alta gama que funcionan según la dinámica M/E
> utilizada en la industria de la teledifusión.

y añade para qué se inventó:

> El modo M/E ha sido desarrollado durante décadas para tratar de eliminar los errores cometidos al
> alternar señales durante la transmisión de eventos en directo. Permite ver con facilidad lo que
> acontece en todo momento, a fin de evitar confusiones que conducen a equivocaciones. Este tipo de
> funcionamiento brinda la posibilidad de verificar las fuentes que van a ser transmitidas y probar
> diferentes efectos antes de emitirlas al aire.

El M/E es lo que se utiliza para aplicar transiciones y combinaciones complejas entre distintas
fuentes de vídeo. Las piezas más pequeñas no lo son: el bus de llave elige una sola señal, el previo es
una salida de monitorizado y el DSK es una llave posterior, no un banco.

En un control con dos bancos, el uso corriente (oficio) es preparar en el segundo lo que no cabe en el
primero —una gafa con el invitado y la conexión, el decorado virtual con su presentador— y llevarlo al
programa como una fuente más.

### Las fuentes y sus atributos

En un mezclador, *source* no es «un cable»: es una fuente de vídeo con todos sus atributos asociados.
Cada fuente del mezclador tiene, además de su señal:

| Atributo | Para qué |
|---|---|
| Nombre largo y nombre corto | Lo que se lee en el multipantalla y en el panel |
| Señal de llave asociada | Para que al elegir esa fuente como relleno se cargue sola su llave |
| Retardo | Para compensar el desfase de esa entrada |
| Corrección de color de entrada | Para igualarla con las demás |
| Grupo de piloto (*tally*) | Qué luz roja se enciende cuando está al aire |
| Botón asignado | En qué tecla del panel está |

El mapeado de fuentes a botones es sólo uno de esos atributos, no la definición. Y que la fuente lleve
sus atributos es lo que hace posible la selección automática de la llave (*autoselect*): cuando una
fuente tiene declarada su señal de llave, seleccionarla como relleno carga automáticamente la llave
que le corresponde.

Los nombres, en el manual ATEM: **«Para identificar la fuente en el panel, se utiliza una denominación
corta de cuatro caracteres. Los nombres más largos admiten hasta veinte caracteres»**, y el manual
recomienda que coincidan, con el ejemplo **«Cámara 1 corresponde a la denominación por extenso, y CAM1
al nombre corto.»** El propio manual se contradice en otro pasaje, donde da **«uno de 20 caracteres,
utilizado en el panel, y otro limitado a cuatro para el programa informático»**: lo seguro es que hay
un nombre largo de hasta veinte caracteres y uno corto de cuatro.

Qué señales entran (oficio, con el criterio c) del módulo 0905, RA 5: **«Se han configurado las
entradas de vídeo a los buses del mezclador, mediante la adecuada ordenación de cámaras, líneas de
vídeo, señales exteriores, gráficos y otras.»**): las cámaras del plató; los servidores de vídeo; las
líneas exteriores (unidades móviles, conexiones, otros centros); el titulador y el sistema de grafismo,
cada uno con su pareja de relleno y llave; y las fuentes internas del propio mezclador —generadores de
color, barras, *clip store*, salidas de los bancos—. Ordenarlas en el panel es parte de preparar el
programa: las cámaras juntas y en su orden, y cada relleno con su llave.

### Las salidas y lo que se graba

Las salidas del mezclador —programa, previo, limpia, auxiliares y multipantalla— se estudian en el
tema 4. Lo que importa aquí es qué lleva cada una respecto de las capas: la salida limpia es el
programa sin lo que añaden las llaves posteriores, y por eso sale sin mosca y sin rótulos (epígrafe 4).
El manual ATEM tiene dos: la limpia 1, **«Señal idéntica a la emitida al aire, pero sin elementos
superpuestos»**, y la limpia 2, que **«incluye además la penúltima capa (DSK 1), pero no la final (DSK
2)»**. Qué lleva la limpia depende, pues, de cuál se tome.

La norma de enseñanza pide decidir qué se graba (módulo 0905, RA 1): **«f) Se han determinado las
señales de la realización televisiva que van a ser grabadas: master, señal sin incrustaciones y
cámaras dobladas o masterizadas.»**, y lo repite entre los contenidos: **«Tipos de grabación en la
realización de televisión: máster, señal sin incrustaciones y cámaras masterizadas.»** El máster es el
programa tal como se emite; la señal sin incrustaciones permite rehacer rótulos y grafismo después,
en otro idioma o con datos corregidos; y las cámaras grabadas por separado permiten remontar el
programa (oficio).

El manual ATEM añade una posibilidad para el croma: en algunos de sus modelos, el canal alfa de una
llave puede salir por una salida auxiliar, y el fabricante explica para qué sirve grabar a
la vez la señal con el fondo verde y su canal alfa: **«es útil, especialmente si es necesario realizar
composiciones por crominancia en el proceso de posproducción.»**

## 2. Efectos

### Qué es un efecto en el mezclador

En el mezclador, «efecto» nombra todo lo que no es conmutar: superponer una imagen a otra, recortarla
con una forma, reducirla a una ventana, moverla, pasar de una a otra con una transición. El manual
ATEM llama al conjunto composición de imágenes: **«La composición de imágenes es una herramienta muy
útil que permite superponer elementos visuales de diferentes fuentes sobre una misma imagen.»** Y
explica cómo: **«se superponen múltiples capas o elementos gráficos sobre una imagen de fondo. Esta
será visible en mayor o menor medida, según cómo se ajuste la transparencia de las capas
superpuestas.»**

Los efectos del mezclador, agrupados por la herramienta que los hace (oficio, con los nombres del
manual ATEM entre paréntesis):

| Efecto | Con qué se hace | Epígrafe |
|---|---|---|
| Superponer un rótulo, una mosca, un presentador recortado | Una llave: de luminancia, lineal o de croma (composición por luminancia, lineal o por crominancia) | 4 y 5 |
| Recortar una imagen con una forma fija | Una llave de figura (composición geométrica) | 4 |
| Reducir, mover, girar una imagen; ventanas | El DVE (composición con efectos visuales digitales) | 6 |
| Varias ventanas a la vez sobre un fondo | Varios DVE, o un generador de composición múltiple (SuperSource, en ATEM) | 6 |
| Pasar de una fuente a otra con forma o movimiento | Una transición: cortinilla, DVE, animada | 3 |
| Fondos de color | Los generadores de color | — |
| Una secuencia de efectos que se repite | Una macro o un *timeline* | 2 |

Los generadores de color son la fuente más simple: el manual ATEM dice que **«permiten seleccionar un
color y ajustar el tono, la saturación y la luminancia»**. Sirven de fondo para rótulos, de color
intermedio para un fundido o de relleno del borde de una cortinilla, aunque ese borde admite
cualquier fuente del mezclador (epígrafe 3).

La llave de figura recorta con una forma que genera el propio mezclador. En la descripción del manual
ATEM, **«permite superponer sobre el fondo una imagen recortada según una cierta figura geométrica. En
este caso, el canal alfa es generado por el mezclador.»**, y el mezclador **«brinda la posibilidad de
crear 18 formas diferentes»**. Es la forma más barata de hacer una ventana fija, porque no gasta DVE
(oficio).

### Dónde se preparan

Un efecto se prepara antes y se lanza después: ése es el sentido del criterio e) del módulo 0905 ya
citado: transiciones, cortinillas, efectos e incrustaciones se dan por **«ajustado y prefijado»** en
el mezclador antes del programa. En el directo, el efecto que no está preparado no existe: se construye en el banco o en
la llave que no está al aire, se comprueba en el previo y se guarda en una memoria (más abajo, en este epígrafe) para
lanzarlo con un botón (oficio).

### Memorias: *snapshots*, macros y *timelines*

Tres maneras de guardar trabajo hecho, que se distinguen por lo que guardan:

| Memoria | Qué guarda | Cuándo se usa |
|---|---|---|
| Snapshot | Un estado del mezclador en un instante: qué fuente hay en cada bus, qué llaves están puestas, cómo están sus parámetros | Recuperar de golpe una configuración conocida |
| Macro | Una secuencia de instrucciones con sus tiempos, que se ejecutan una tras otra al pulsar un botón | Automatizar una entrada, una cabecera, un cambio de escenario |
| Timeline | Una sucesión de estados con transiciones entre ellos, ejecutada sobre una línea de tiempo | Efectos largos y precisos |
| Shotbox | Un teclado de disparo rápido donde se colocan las memorias | Tener a mano lo que se usa a cada rato |

La diferencia entre *snapshot* y macro es la del tiempo: el *snapshot* es una fotografía, la macro
es una película.

### La macro, según el fabricante

El manual de los ATEM define la macro exactamente así:

> Una macro es una secuencia de instrucciones que se llevan a cabo automáticamente al presionar un
> botón. Por ejemplo, es posible grabar una serie de transiciones entre distintas fuentes que
> incluyan imágenes superpuestas, ajustes del volumen y modificaciones en la configuración de las
> cámaras. Una vez registradas las instrucciones, pueden ejecutarse inmediatamente presionando dicho
> botón.

Y dice dónde viven: **«Las macros se graban mediante el programa ATEM Software Control, un dispositivo
ATEM Advanced Panel o ambos, y se almacenan en el mezclador.»** Una macro no es un aparato ni un
mezclador pequeño, ni tiene nada que ver con el objetivo macro de la fotografía: es una lista de
instrucciones guardada en el propio mezclador. En ese fabricante, **«Las macros pueden asignarse a
cualquiera de los 100 espacios disponibles.»**, y el panel de macros alterna entre crear y ejecutar
**«durante un programa en directo»**.

Cómo se reconoce una macro escrita. Una secuencia como «*snapshot* de programa, pausa de 15 fr,
transición MIX de programa, llave 1 de programa a apagado» es una macro: tiene una pausa medida en
fotogramas y contiene un *snapshot* dentro. Un *snapshot* es instantáneo y no contiene pasos; una
memoria de llave guarda parámetros, no acciones; y un *timeline* coloca estados sobre una línea de
tiempo continua, mientras que lo que se enseña es una lista de instrucciones ejecutadas una tras otra,
con una pausa explícita entre dos de ellas (oficio).

### Un efecto programado no se retoca en marcha

Las posiciones que forman parte de un *timeline* ya en marcha están escritas en el propio efecto, y
tocarlas mientras corre no reposiciona la ventana: rompe el efecto o no hace nada, según el
mezclador. El *timeline* es una secuencia programada, y una secuencia programada se edita parada, no
en vuelo. Un DVE suelto sí se mueve en cualquier momento; el que va dentro de un *timeline* lanzado,
no.

El concepto que hay que llevarse, y que vale para toda la automatización de un control: un efecto
programado se comporta como una grabación, no como un mando. Se prepara antes o se cancela; mientras
corre, manda él. Una macro y un *timeline* son la misma idea —una secuencia guardada que se lanza con
un botón— y por eso comparten la misma limitación: se editan paradas.

La idea llega más lejos en los sistemas que guardan no una secuencia corta sino la escaleta entera de
un programa, cambio de plano a cambio de plano, y la ejecutan contra código de tiempo; el control pasa
entonces de ejecutar a supervisar. Es la técnica de las realizaciones musicales o de grandes eventos
escritas de antemano (oficio; qué sistema concreto se use no consta en documento leído).

### El *clip store*

El *clip store* es la memoria de vídeo e imágenes fijas del propio mezclador: un almacén interno
donde se cargan clips cortos —cabeceras, ráfagas, cortinillas animadas— y grafismos fijos, para
poder dispararlos como una fuente más sin depender de un servidor externo.

Sus rasgos:

- Cada clip ocupa una fuente del mezclador, y se selecciona en los buses como si fuera una
  cámara.
- Los grafismos se cargan con su canal alfa, de modo que al elegirlos como relleno el mezclador
  toma también su llave. El manual de los ATEM lo describe con esa automatía: «al elegir un
  reproductor multimedia, tanto el canal alfa como la imagen principal se activan automáticamente sin
  que sea necesario seleccionarlos por separado».
- La duración es corta, porque la memoria es limitada: para material largo se usa un servidor.
- Se dispara con un botón o desde una macro, y por eso es la pieza que convierte una entrada de
  programa en una operación de una sola tecla.

Ejemplo de entrada de programa en una sola tecla (oficio): una macro que lanza la cabecera desde el
*clip store*, espera su duración, pasa por transición animada al plano general del plató, mete la
mosca en la llave posterior y deja en previo el plano del presentador. El realizador la dispara con
un botón y la ensaya antes, entera, con el mezclador fuera del aire.

## 3. Transiciones

### Los modos de transición

| Transición | Qué hace | Nombre en el panel |
|---|---|---|
| Corte | Cambio instantáneo de una fuente a otra | CUT |
| Mezcla o encadenado | Las dos imágenes se superponen y una sustituye a la otra progresivamente | MIX, *dissolve* |
| Cortinilla | Un borde con forma recorre la pantalla revelando la nueva imagen | WIPE |
| Fundido a color | La primera imagen pasa a través de un color intermedio hasta la segunda | *Fade*, *dip to colour*, SÚPER MIX cuando el color es blanco |
| Mezcla no aditiva | En cada punto se muestra la más brillante de las dos imágenes | NAM |
| Mezcla aditiva total | Las luminancias de las dos fuentes se suman | FAM |
| Transición con efecto digital | La imagen se mueve, gira o se encoge para dejar paso | DVE wipe, *DME wipe* |

La cortinilla es la transición en la que un borde con forma se mueve a través de la pantalla,
revelando la nueva imagen mientras la primera desaparece. La palabra que la identifica es borde: la
mezcla no tiene borde, porque las dos imágenes se superponen en toda la pantalla a la vez.

El manual ATEM describe las tres básicas así. El encadenado, que el manual llama disolvencia:
**«Una disolvencia consiste en una transición gradual de un plano a otro que se realiza interpolando
ambas fuentes y superponiéndolas durante el tiempo determinado para la duración del efecto, que
puede ajustarse según las preferencias del usuario.»** El fundido a color, que el manual llama
fundido: **«el plano saliente da paso a una fuente intermedia que permanece en la pantalla durante
unos instantes hasta fundirse gradualmente con el plano siguiente. Este tipo de transición puede
utilizarse para lograr un efecto, por ejemplo, mediante un fundido en blanco, o mostrar rápidamente
el logotipo de un patrocinador.»** Y la cortinilla: **«Es un tipo de transición entre dos planos que
consiste en reemplazar una fuente mediante un patrón o una forma geométrica, por ejemplo, un rombo o
un círculo en expansión.»** El panel de ese fabricante reúne cinco tipos: **«disolvencias, fundidos,
cortinillas, transiciones con efectos visuales digitales y transiciones animadas»**, con los botones
MIX, DIP, WIPE, DVE y STING; y el propio manual avisa de que **«Las transiciones disponibles dependen
del modelo de mezclador.»**

### Los parámetros de la cortinilla

En un panel ATEM, la cortinilla se prepara en el previo, se elige con el botón WIPE y se ajusta
antes de lanzarla. Dos de los pasos del manual: **«Gire el mando para seleccionar la forma de la
cortinilla.»** y **«Seleccione la fuente para el borde.»** El borde no está limitado a un color:
**«Es posible emplear cualquier fuente del mezclador para el borde de una cortinilla. Por ejemplo, se
puede utilizar una imagen del reproductor multimedia en un borde ancho para destacar una marca o un
patrocinador.»**

Además de la duración (tiempo, en segundos y fotogramas), el manual da estos parámetros:

| Parámetro (manual ATEM) | Qué hace |
|---|---|
| Simetría | **«Se utiliza para controlar la relación de aspecto de la forma geométrica. Por ejemplo, ajustando este valor, es posible transformar un círculo en una elipse.»** |
| Posición | Mueve el centro de la forma en la pantalla, si la forma lo permite, con la palanca de mando del panel o desde el programa informático de control |
| Invertir dirección | **«Al invertirla, la transición comienza desde los bordes de la pantalla hacia el centro.»** |
| Alternar | Con la función activada, **«la dirección de la transición alterna entre normal e inversa cada vez que se ejecuta.»** |
| Ancho | **«Permite ajustar el ancho del borde.»** |
| Atenuación | **«Permite ajustar la definición de los bordes.»** |

Una variante es la cortinilla con gráficos: un gráfico fijo hace de borde y cruza la pantalla en
horizontal. Según el manual, ese gráfico debería ser **«una especie de pancarta vertical cuyo ancho no supere el 16 % del
ancho total de la pantalla.»**

### NAM y FAM

Las dos son maneras de mezclar dos imágenes sin encadenarlas linealmente, y se diferencian en lo que
hacen con las luminancias:

- NAM (mezcla no aditiva): en cada punto de la pantalla se muestra la más brillante de las
  dos. El efecto es que las partes brillantes de la fuente que se desvanece se ven durante más
  tiempo que las oscuras: los rótulos blancos aguantan hasta el final.
- FAM (mezcla aditiva total): las luminancias se suman, de modo que en el punto medio de la
  transición la luminancia de las dos fuentes está al 100 %. La imagen se va a blanco en la mitad
  del recorrido, como un destello.

La palabra que las separa es *suman*: la FAM suma; la NAM elige la más brillante. Y ninguna de las dos
es el encadenado normal, en el que las dos imágenes se desvanecen por igual en todos los niveles de
brillo, ni el fundido a color, en el que la primera fuente pasa a través de un color preseleccionado.

### Cómo se ejecuta una transición

Toda transición va del programa al previo: lo que está en el bus de previo es lo que entra. El manual
ATEM da los tres modos de lanzarla:

| Mando | Qué hace, según el manual ATEM |
|---|---|
| CUT | **«permite realizar una transición inmediata entre la señal principal y el anticipo, independientemente del tipo de transición seleccionado»** |
| AUTO | **«permite llevar a cabo la transición seleccionada según la duración indicada»** |
| Palanca (*T-bar*) | **«se emplea como alternativa al botón AUTO y permite al operador controlar la transición de forma manual»** |

La duración se fija en fotogramas y queda guardada: **«Cada transición tiene una duración
independiente, lo cual permite aumentar la velocidad simplemente eligiendo el tipo de transición y
presionando el botón AUTO. Este valor se almacena en la memoria del dispositivo hasta que el usuario
lo modifique nuevamente.»** La palanca sirve cuando el ritmo de la transición lo marca lo que pasa en
el plató o en la música, y no un número de fotogramas (oficio).

Una transición no mueve sólo el fondo. Los botones de «próxima transición» eligen qué capas entran o
salen con ella: **«Los botones BKGD, KEY 1, KEY 2, KEY 3 y KEY 4 permiten seleccionar los elementos
que formarán parte de la transición siguiente.»** Con BKGD se cambia la imagen de fondo; con una llave
seleccionada, esa llave entra o sale con la transición; y **«También es posible realizar una
transición con los elementos superpuestos solamente, sin cambiar la imagen de fondo.»** Antes de
lanzar hay que mirar el previo: **«Al escoger los elementos de la transición siguiente, el operador
debe mirar el anticipo, ya que este brinda un adelanto de las imágenes que se transmitirán a través de
la salida principal una vez que la transición finalice.»**

Y la transición se puede ensayar sin salir al aire. El botón PREV TRANS **«permite al operador
comprobar la transición antes de emitirla al aire, llevándola a cabo con la palanca»**; el manual lo
justifica con la misma idea que el M/E: **«Esta función resulta de suma utilidad a fin de no cometer
errores al aire.»**

### El fundido a negro

El fundido a negro es la última etapa del mezclador y no una transición más: lleva a negro todo lo que
sale, capas incluidas. El manual ATEM: **«El botón FTB permite realizar un fundido a negro de la imagen
transmitida según la duración indicada en el campo Tiempo.»** y **«El fundido a negro se emplea
habitualmente al principio y al final de una producción, o antes de una pausa publicitaria, y resulta
útil para asegurarse de que todas las capas superpuestas se atenúen al mismo tiempo.»** Dos
precisiones del mismo manual: **«no es posible ver un fundido a negro de forma anticipada»**, y el
sonido puede acompañarlo si se activa la opción de audio sigue a vídeo (AFV) de la salida principal.

### La transición animada

La transición animada (*stinger*) tapa el paso de una fuente a otra con una animación gráfica. El
manual ATEM la describe así, para sus modelos 1 M/E y 2 M/E: **«las transiciones animadas usan una secuencia del reproductor de medios
para realizar una transición. Dicha secuencia normalmente consiste en una animación gráfica que se
superpone a la imagen de fondo. Cuando se reproduce la animación en pantalla completa, se realiza un
corte directo o disolvencia de la imagen de fondo.»** Y da su uso típico: **«este tipo de transición
se utiliza con frecuencia en producciones de eventos deportivos para mostrar repeticiones
instantáneas.»** El cambio de fondo queda escondido detrás de la animación: el espectador no ve el
corte, ve la ráfaga con la marca del programa (oficio).

### Corte y transición

Adobe parte del corte: **«By default, placing one clip next to another in the Timeline panel results
in a cut, where the last frame of one clip is followed by the first frame of the next.»** La
transición es otra cosa: **«A transition is an effect added between pieces of media to create an
animated link between them.»** (ayuda de Premiere, «Transitions overview», actualizada el
07-01-2026). Blackmagic añade para qué sirve: **«Transitions provide another way of bridging the
change from one clip to another, and are often used to indicate a change in time or location when
changing scenes.»** (*Resolve 21*, cap. 55, p. 1194).

El corte es la unión por defecto y la más usada; la transición significa algo (paso del tiempo,
cambio de lugar, cierre) y por eso no se pone por adorno (oficio). El valor narrativo del corte, del
fundido y de la elipsis está en el tema 1.

El manual universitario de Mateu Torres da el sentido de las dos transiciones clásicas:

| Recurso | Relación con la elipsis |
|---|---|
| Fundido | **«es una transición empleada para acentuar el paso del tiempo —elipsis—, lo que denota a su vez un cambio temporal y/o espacial sustancial, dando paso de una secuencia a la siguiente»**; el fundido a negro es el ***fade out*** y el **«fundido de apertura»** desde negro, el ***fade in*** (3.2, p. 37) |
| Encadenado | **«sobreimpresiona durante unos instantes el final de un plano, que se va desvaneciendo, con el inicio del siguiente»**; **«tiende a ofrecer cierto carácter elíptico»**, pero **«"el fundido separa las secuencias, mientras que el encadenado y el corte las conectan"»** (3.2, p. 38, citando a Katz) |

En el directo eso se traduce así (oficio): el corte une planos del mismo tiempo y del mismo espacio, y
es la unión de la conversación, de la entrevista, del deporte; el encadenado conecta, pero marca un
salto o suaviza un cambio —de un bloque a otro de una actuación musical, de la presentación al
reportaje, entre dos planos de recurso sobre la misma música—; el fundido a negro separa, y es la
puntuación de los bloques, del principio y del final.

### Lo que significa cada recurso

| Recurso | Qué dice al espectador | Uso corriente en directo (oficio) |
|---|---|---|
| Corte | Continuidad: lo que sigue ocurre ahora, aquí o en paralelo | La unión por defecto; entrevista, debate, deporte, informativo |
| Encadenado | Cambio de tiempo o de lugar, o paso suave | Música, recursos sobre locución, paso a un vídeo en magacín |
| Fundido a negro | Fin de una unidad | Apertura y cierre del programa, entrada a publicidad |
| Fundido a color (blanco) | Destello, corte de tono | Efecto puntual, logotipo de patrocinio (manual ATEM) |
| Cortinilla | Cambio de apartado, marca del programa | Separadores, sumarios, deportes; casi nunca dentro de una noticia |
| Transición animada | Firma del programa sobre el cambio | Entrada y salida de repeticiones en deportes (manual ATEM), ráfagas |
| DVE, gafa | Simultaneidad: dos lugares o dos personas a la vez | Presentador y conexión, dos invitados remotos, pregunta y respuesta |
| Croma, decorado virtual | Explicación: el presentador dentro del dato | Tiempo, elecciones, datos, deportes |
| Llave posterior (rótulo) | Identificación e información | Quién habla, dónde, cuándo; titulares |

La regla que ordena la tabla: el corte no se nota y la transición sí, y lo que se nota tiene que
significar algo. Un efecto que no dice nada distrae de lo que se dice (oficio).

### Lo que el ayudante comprueba de las transiciones

La cualificación le pide identificar las transiciones **«para asegurar que son las previstas para un
determinado programa, con el ritmo y los tiempos de entrada y salida adecuados»** (MF0217_3, CE1.6,
epígrafe 1). En la práctica, eso son cuatro comprobaciones (oficio):

1. Que cada paso de la escaleta lleva anotada su transición —corte, encadenado, cortinilla,
   transición animada, fundido a negro— y que el mezclador la tiene preparada con esa duración.
2. Que los vídeos traen coleo bastante para la transición prevista: un encadenado consume imagen del
   plano que sale y del que entra, y si el coleo no llega, la transición deja ver lo que hay antes o
   después de la pieza. Si no llega, se avisa al mezclador y al operador de sonido (UC0217_3,
   CR1.2, epígrafe 1).
3. Que la transición animada o el fundido que abre o cierra un bloque están contados en el minutado:
   duran, y ese tiempo es del programa.
4. Que en el directo la transición se anticipa con la orden, no se pide encima (tema 6).

### Errores de uso

Los errores más corrientes, todos de oficio: la transición por adorno, que convierte un corte de
conversación en un encadenado sin motivo; la cortinilla dentro de una noticia; la gafa que pone juntas
a dos personas que están en el mismo plató y se pueden sacar en un plano de dos; el rótulo que tapa
la cara o que sale antes de que el que habla haya empezado; la llave posterior que se queda al aire
después de su tiempo; el croma con bordes verdes o con el presentador vestido del color del fondo; y
la macro que se lanza sin haberla ensayado.

## 4. Incrustaciones

### Las tres señales de una incrustación

Incrustar es superponer una imagen sobre otra, y en ello intervienen siempre tres señales:

| Señal | Nombre inglés | Qué es |
|---|---|---|
| Fondo | *background* | La imagen de base, sobre la que se superpone |
| Relleno | *fill* | Lo que se ve de la imagen superpuesta: el logotipo, el rótulo, el presentador |
| Llave | *key*, *alpha* | Dónde se ve: una máscara en escala de grises que dice, punto por punto, cuánta transparencia hay |

El manual de los ATEM lo dice con esas mismas tres piezas al describir la composición lineal, que es
la que las lleva separadas:

> Una composición lineal requiere una fuente para el primer plano y un canal alfa. La señal principal
> incluye la imagen que se superpone al fondo, mientras que el canal alfa contiene una máscara en
> escala de grises que permite definir la transparencia. Ambas señales son fuentes audiovisuales.

La fórmula del compuesto:

salida = relleno × llave + fondo × (1 − llave)

Leída despacio: donde la llave vale 1 —blanco— se ve el relleno; donde vale 0 —negro— se ve el
fondo; y donde vale un valor intermedio se ven los dos en esa proporción. El borde suavizado de un
rótulo es justamente eso: una franja de valores intermedios.

Las señales son tres aunque vengan por dos cables o por uno. En un titulador, relleno y llave llegan
por dos entradas distintas del mezclador; en una llave de luminancia, la llave se fabrica del propio
relleno; en una de croma, del color del relleno. El mezclador sigue manejando tres señales: fondo,
relleno y llave (oficio).

### Aditivo frente a lineal

Las dos maneras de combinar el relleno con el fondo:

| | Llave lineal (o no aditiva) | Llave aditiva |
|---|---|---|
| Fórmula | salida = relleno × llave + fondo × (1 − llave) | salida = relleno + fondo × (1 − llave) |
| El relleno se atenúa con la llave | Sí | No: entra entero |
| Dónde la llave vale 0 | No aparece nada del relleno | Aparece el relleno tal cual, sumado al fondo |
| Para qué se pensó | Grafismo con canal alfa correcto | Rótulos y llamas sobre fondo, donde se quiere que lo brillante se sume |

La consecuencia práctica es una sola frase: en la llave aditiva, todo lo que tenga señal el relleno
se ve, tenga o no tenga llave.

Dos casos de control que se resuelven con las fórmulas (física de la señal):

- El relleno de un gráfico trae el negro levantado —por ejemplo, al 7 %— y no se toca ningún
  parámetro. Con llave lineal, donde la llave vale 0 el relleno se multiplica por cero y desaparece:
  nada cambia. Con llave aditiva, ese 7 % se suma al fondo en toda la pantalla, y se nota en el fondo
  al meter o sacar la llave por corte: la imagen de fondo se levanta y se baja de golpe.
- El titulador entrega una llave que no cubre una parte donde el relleno sí tiene señal, y esa parte
  no debe verse. La solución es una llave no aditiva: al multiplicar el relleno por la llave, lo que
  la llave no cubre se anula. Con una aditiva, esa parte aparecería sumada al fondo.

Y un tercero: si el relleno trae su canal alfa acoplado y la llave toma ese alfa, la luminancia de los
píxeles del relleno es indiferente para la transparencia. La decide la llave; el brillo del relleno
sólo decide de qué color se ve lo que se ve, no si se ve.

### Clip y ganancia

Cuando la llave se fabrica a partir del brillo del relleno, hay que decidir a partir de qué nivel
de gris se considera opaco. Eso lo hacen dos controles:

| Control | Qué mueve |
|---|---|
| Clip (recorte, nivel, *threshold*) | El punto de la escala de grises donde la señal se recorta: por encima, opaco; por debajo, transparente |
| Ganancia (*gain*) | La pendiente del recorte: cuán brusco es el paso de transparente a opaco, y por tanto la dureza del borde |

El punto donde se recorta la señal de llave en una incrustación de luminancia se ajusta con los
controles de clip y ganancia. Otros controles del menú de la llave hacen otras cosas: los bordes
añaden filete o sombra al rótulo, y la saturación es de color.

El manual de los ATEM describe esos dos controles con otro nombre y la misma función:

> Nivel Permite ajustar el valor a partir del cual la imagen de fondo es visible a través de la
> máscara. Al disminuir este valor, la imagen de fondo se verá con mayor nitidez. Aumente este
> parámetro si el fondo se ve completamente negro. Ganancia Permite modificar electrónicamente el
> valor de visibilidad de la imagen superpuesta atenuando su borde.

### La máscara de la llave

Las llaves del mezclador llevan una máscara rectangular. El manual ATEM la describe así: **«Las
diferentes funciones para combinar imágenes cuentan con una máscara rectangular ajustable que puede
utilizarse para eliminar bordes ásperos y otros artefactos de la señal. Al modificar el largo o el
ancho de dicho rectángulo, es posible cubrir diversas partes de la imagen. Asimismo, se puede emplear
como una herramienta creativa para ocultar diversos elementos.»** En las llaves lineal y de luminancia,
la opción de máscara **«Permite crear una máscara rectangular que puede ajustarse modificando los
campos Superior, Inferior, Izquierda y Derecha.»**

En el croma es un recurso de oficio: cuando el ciclorama no cubre todo el encuadre y asoman focos,
bordes del fondo o parte del plató, la máscara tapa esas zonas sin tocar el plano ni los ajustes del
color.

### Las señales premultiplicadas

Un grafista entrega un logotipo con su señal de llave y avisa de que está precortado o
premultiplicado. Eso quiere decir que la señal de relleno ya ha sido multiplicada por la señal de
llave antes de salir del titulador: el relleno viene ya con sus bordes atenuados y su fondo a negro. El
orden de la frase importa: es el relleno multiplicado por la llave, no al revés, porque la llave es la
máscara, y una máscara no se multiplica por lo que enmascara.

Qué hay que hacer con una señal premultiplicada. El mezclador tiene un ajuste que lo declara
—Blackmagic lo llama «composición precompuesta»— y cuando se activa, el mezclador deja de multiplicar
otra vez. Si no se declara, el relleno se multiplica dos veces por la llave y los bordes salen
oscurecidos. El manual de los ATEM lo dice en una línea:

> Composición precompuesta Indica que el canal alfa del clip en el reproductor multimedia está
> premultiplicado.

y avisa de cuándo hacen falta los controles manuales en su lugar:

> Si el elemento gráfico no incluye un canal premultiplicado, utilice los controles Recorte y
> Ganancia según se describe en el apartado Composición de imágenes para obtener el resultado
> deseado.

Premultiplicar no es recortar la imagen a unas dimensiones, que es un recuadre.

### Los tipos de llave

Un *keyer* es el módulo del mezclador que hace una llave. Los tipos, según de dónde sale la máscara:

| Llave | Cómo se hace la máscara | Cuándo se usa |
|---|---|---|
| De luminancia (*luminance key*) | A partir del brillo de la propia señal de relleno: lo oscuro se hace transparente | Rótulos blancos sobre negro; grafismo sin canal alfa |
| Lineal (*linear key*) | Con una señal de llave separada, en escala de grises | Grafismo profesional, tituladores; es la de mayor calidad |
| De crominancia (*chroma key*) | A partir de un color, normalmente verde o azul, que se declara transparente | Plató virtual, hombre del tiempo |
| De figura (*preset pattern*, *pattern key*) | Con una forma geométrica generada por el mezclador | Ventanas, círculos, cortinillas fijas |
| Con efectos digitales (*DVE key*) | Combina la llave con una transformación geométrica | Ventanas móviles, imagen dentro de imagen |

La de luminancia, en el manual ATEM: **«Una composición por luminancia consiste en una sola fuente con
la imagen principal que se superpone al fondo. Todas las áreas negras definidas según la luminancia de
la señal se tornarán transparentes para que se visualice el fondo.»**, de modo que **«se emplea la
misma señal para el canal alfa y el primer plano.»**

La llave aditiva (*additive key*) nombra un modo de combinar relleno y fondo (arriba, en este epígrafe), no una
forma de hacer la máscara. Lo que no es una llave es el *coring*: es un
control de reducción de ruido que recorta los valores pequeños de una señal para que el ruido de
fondo no se amplifique (oficio). No genera ninguna máscara, que es lo que define a una llave.

### El *self key* y el *show key*

Un *self key* es una llave en la que el relleno se usa también como llave. No hay señal de llave
separada: el mezclador se la fabrica del brillo del propio relleno. Es lo mismo que una llave de
luminancia, mirado desde el encaminamiento. Sirve cuando la fuente no trae canal alfa y lo que se
quiere incrustar es claro sobre fondo negro: un rótulo blanco, un reloj, una llama. Y no sirve cuando
el gráfico tiene medios tonos que deben verse opacos, porque entonces el propio gris los volvería
semitransparentes. En un *self key* intervienen igualmente tres señales —fondo, relleno y llave—,
aunque dos de ellas salgan de la misma fuente.

El *show key* es otra cosa y no hay que confundirlas: es la previsualización de la señal de llave.
Sirve para ver la máscara sola, en blanco y negro, y comprobar que recorta donde debe antes de meterla
al aire. No es lo mismo que previsualizar los ajustes, que es ver el resultado compuesto en el previo:
el *show key* enseña la señal de llave en bruto.

### Llaves previas y posteriores

Las llaves se reparten en dos lugares de la cadena. El manual ATEM: **«El mezclador permite realizar
dos tipos de composiciones: previas y posteriores. El módulo M/E del panel de control dispone de
cuatro botones para superponer efectos. Cada uno de ellos puede asignarse a una composición lineal,
precompuesta, geométrica, por crominancia, por luminancia o con efectos visuales digitales. Por su
parte, el módulo DSK cuenta con dos botones para composiciones previas. Cada uno de ellos puede
asignarse a una composición lineal o por luminancia.»** Así en el manual, que en la misma página
llama a sus paneles «Composición previa» y «Composición posterior»: por su nombre y por su lugar en la
cadena, las del módulo DSK son las posteriores, y el propio manual explica **«Cómo realizar una
composición posterior lineal o por luminancia»** en el panel «Composición posterior».

| | Llave previa (USK) | Llave posterior (DSK) |
|---|---|---|
| Dónde está | Dentro de cada banco M/E, antes de su salida | Después del programa, al final de la cadena |
| Tipos (en el manual ATEM) | Lineal, precompuesta, figura, croma, luminancia, DVE | Lineal o luminancia |
| Para qué (oficio) | Lo que forma parte de la imagen: el presentador del croma, la ventana de la conexión | Lo que va encima de todo: mosca, rótulos, créditos |
| Sale en la limpia | Sí | No (en el ATEM, la limpia 2 lleva la DSK 1) |

La cadena de un mezclador de varios bancos, de arriba abajo:

| Etapa | Qué hace | Se ve en la salida limpia |
|---|---|---|
| M/E 1, M/E 2, M/E 3… | Construyen imágenes compuestas | Sí, si van al programa |
| Programa | Elige y transiciona entre fuentes y salidas de M/E | Sí |
| DSK 1 y DSK 2 | Añaden mosca, rótulos y créditos después del programa | No |
| Fundido a negro | Lo último de todo | — |

Que el DSK vaya después del programa es lo que hace posible la salida limpia: la señal se toma antes
de esa etapa. Y es lo que permite cambiar de plano por debajo del rótulo sin que el rótulo se mueva.

El DSK se opera con sus propios botones. Según el manual ATEM, TIE **«permite vincular elementos
superpuestos a la transición siguiente transición, de manera que puedan emitirse al aire
simultáneamente»**; ON AIR los muestra u oculta al instante; y su AUTO propio **«solo afecta a las
capas que se superponen posteriormente. Es de gran utilidad para lograr que elementos tales como
logotipos, textos móviles o repeticiones en directo aparezcan o desaparezcan gradualmente sin
interferir con las transiciones del programa principal.»** El manual precisa que vincular la llave a
la transición no cambia la señal limpia: **«si los elementos superpuestos están vinculados a la
transición, el direccionamiento de la señal limpia no se verá afectado.»**

### Cómo entra el grafismo en el mezclador

El grafismo en directo es lo que se incrusta sobre la imagen mientras se emite: rótulos de nombre y
cargo, titulares, mosca, marcadores, relojes, cortinillas y ráfagas, gráficos de datos. Llega al
mezclador por tres caminos (oficio):

| Camino | Qué entra | Cómo se incrusta |
|---|---|---|
| Titulador o sistema de grafismo | Relleno y llave por dos entradas | Llave lineal, normalmente en un DSK |
| *Clip store* del mezclador | Grafismos fijos y animaciones cortas con su alfa | Se toma como relleno y el alfa se carga solo (epígrafe 2) |
| Sistema de plató virtual o de realidad aumentada | La imagen ya compuesta | Se conmuta como una fuente más (epígrafe 5) |

La norma de enseñanza pide comprobar la incrustación del titulador y controlar su salida hacia el
mezclador (módulo 0905, RA 6): **«d) Se han configurado las opciones gráficas y de almacenamiento de
textos del titulador, comprobando que su señal se incrusta adecuadamente.»** y **«e) Se han generado
los rótulos y claquetas identificativas necesarias en el titulador, para la realización de un
programa de televisión, gestionando su almacenamiento y controlando su salida hacia el mezclador de
vídeo.»**

Lo que el realizador decide sobre el grafismo en el mezclador (oficio): en qué llave va cada elemento
—la mosca y los rótulos, en las posteriores, para que no se muevan con los cambios de plano y no
salgan en la limpia; una ventana de datos que forma parte de la imagen, en una previa—; si la llave
entra por corte, por mezcla o con su AUTO propio; si va vinculada a la transición (TIE) o se lanza
aparte; y qué llave tiene prioridad cuando dos coinciden. Comprobar que la señal del titulador viene
premultiplicada o no, y declararlo en la llave, es la primera prueba del ensayo (arriba, en este epígrafe). Quién
diseña, rellena y lanza los rótulos en la RTVA, el titulador y la paginación son el tema 4; la
rotulación, la realidad aumentada, los decorados virtuales y las pantallas del plató, el tema 12.

## 5. Chroma

### Qué es el croma

El croma (*chroma key*) es la llave que fabrica la máscara a partir de un color del relleno. El manual
ATEM la describe con su ejemplo clásico: **«Este tipo de composición se utiliza principalmente para
pronósticos del tiempo en los cuales el meteorólogo aparece delante de un gran mapa. En realidad, en
el estudio, el presentador está parado frente a un fondo azul o verde. En una composición por
crominancia se combinan dos imágenes usando una técnica especial que permite eliminar un color de la
imagen en primer plano para dejar ver la imagen de fondo.»** Y da sus otros nombres: **«Esta técnica
también es conocida como inserción cromática, superposición por separación de colores, o simplemente
pantalla azul o verde.»**

Las tres señales del epígrafe 4 están también aquí: el fondo es el mapa; el relleno, la cámara del
presentador ante el verde; y la llave, en palabras del manual, **«se genera a partir de la imagen que
se colocará en primer plano»**.

### Cualquier color sirve

Un *chroma key* se puede hacer con cualquier color.

El mecanismo: la incrustación por croma no reconoce «el verde»: reconoce el color que se le diga
que reconozca. Se le indica al mezclador un color de referencia y una tolerancia, y todo píxel
que caiga dentro de ese margen se sustituye por la señal de fondo.

Por qué entonces todo el mundo usa verde y azul:

1. Ni el verde ni el azul saturados aparecen en la piel humana, y la piel es lo que casi siempre
   hay delante del croma.
2. En los sensores el canal verde es el que más resolución tiene —hay el doble de fotositos
   verdes—, así que el recorte sale más limpio.
3. El azul se prefiere cuando el vestuario lleva verde, y al revés. Se elige por lo que hay
   delante, no por una limitación del aparato.

Hay que saber distinguir una costumbre bien fundada de una imposibilidad técnica: las afirmaciones del
tipo «sólo se puede hacer con verde» o «sólo con azul» convierten una costumbre en una regla.

### Los ajustes del croma

El manual ATEM da dos juegos de controles. En los modelos sin croma avanzado se elige el color por su matiz:
**«Matiz Permite seleccionar el color que será reemplazado. Gire el mando correspondiente hasta que el
fondo sea visible.»**, y se ajustan la ganancia (**«Permite atenuar los bordes de la imagen
superpuesta.»**), el límite de luminancia y la opción de espectro limitado, que sirve cuando algún
color del primer plano se parece al del fondo: **«Si algunos de los colores de la imagen en primer
plano son demasiado parecidos al color de fondo seleccionado para la composición, es posible que
resulte difícil excluirlos. Al activar esta opción, se reduce el espectro en torno a dicho color.»**
Esos parámetros se pueden ajustar poniendo las barras de color como imagen de fondo y mirando el
resultado en un vectorscopio.

En los modelos con croma avanzado, el color no se busca con un mando: se toma una muestra del fondo.
**«Seleccione un área representativa del fondo verde que abarque el mayor rango de luminancia
posible.»**, y el manual añade que el tamaño de la muestra por defecto vale **«cuando el fondo está
bien iluminado»**. Después se afina:

| Control (manual ATEM) | Qué corrige |
|---|---|
| Primer plano | **«Al aumentar este valor, es posible rellenar pequeñas áreas de transparencia en la imagen en primer plano.»** |
| Fondo | **«Utilícelo para eliminar artefactos menores en el área de la imagen que desea eliminar.»** |
| Borde | Mueve el borde de la superposición **«para eliminar elementos del fondo cercanos a la imagen en primer plano, o extenderla si la composición es demasiado notoria»**; **«Esto resulta de suma utilidad con ciertos detalles, tales como el cabello.»** |
| Rebase | **«Ajuste este control para eliminar el tinte cromático en el contorno de los elementos en primer plano, por ejemplo, causados por el reflejo de la luz en un fondo verde.»** |
| Reflejo | **«Permite eliminar una cierta tonalidad general en todos los elementos en primer plano.»** |
| Ajustes cromáticos | Brillo, contraste y saturación del primer plano, **«a fin de que la superposición sea más convincente»** |

El rebase de color (*spill*) tiene su definición en el mismo manual: **«La luz que rebota en una
superficie verde puede provocar la aparición de un contorno del mismo color en los elementos en primer
plano, así como de un cierto matiz en toda la imagen principal. Esto se denomina rebase o reflejo
cromático.»**

Y un consejo de método del fabricante: ver la máscara sola mientras se ajusta. **«Al realizar
ajustes, podría resultar útil asignar una de las ventanas del modo de visualización simultánea a la
máscara.»** Es la misma idea que el *show key* del epígrafe 4.

### Lo que el croma pide al plató

Un croma se resuelve antes en el plató que en el mezclador (oficio).

Tres consecuencias de oficio para el croma: el fondo ha de estar iluminado de forma uniforme; el
sujeto no puede llevar ropa del color del fondo, porque se volvería transparente; y la luz que rebota
del fondo tiñe los bordes del sujeto, que hay que limpiar después. Y una de señal: el recorte por color
necesita resolución de color, así que un material con submuestreo cromático fuerte (tema 14) da bordes
peores que uno 4:2:2 o 4:4:4.

El Libro de Estilo de Canal Sur lo lleva al vestuario de los presentadores (8.6.1, p. 122). Punto 4:
**«Los colores fuertes tampoco son aconsejables. Se saturan e impregnan de ‘croma’ el cuello y el
mentón.»** Punto 9: **«Los departamentos de Estilismo y Realización deberán tener muy en cuenta los
condicionantes técnicos de cromas, transparencias o bien de la grabación o emisión desde un plató con
decorado virtual.»** Es un **«deberán»**: el realizador responde, con Estilismo, de que el vestuario no
rompa el croma.

### Croma en directo y decorado virtual

Lo que separa un croma de directo de uno de postproducción es el tiempo: una herramienta de
postproducción no se define por no ser rápida, sino por trabajar sobre material que ya existe, y en
directo el material no existe todavía (oficio). Por eso el croma del control lo hace el mezclador o un
sistema de plató virtual que trabaja en tiempo real, y no un programa de composición de sala.

La incrustación no tiene por qué hacerla el mezclador. Si la señal de cámara entra en el motor de
render, el motor compone el decorado virtual con la figura ya recortada y devuelve una sola señal ya
montada, que el mezclador se limita a conmutar como conmutaría cualquier otra. El mezclador deja de
ser el que incrusta y pasa a ser el que emite.

Por la misma razón, un mezclador sin llaves de croma puede trabajar con decorado virtual: basta con
que la incrustación se haga antes, en el sistema de grafismo. La sincronía de la señal no es lo que lo
resuelve —hace falta siempre, con llave o sin ella—. Y el croma es una clase de llave, la incrustación
por color: decir que «el croma no se hace por *key*» es falso. La norma de enseñanza pide conocer ese
enlace (módulo 0910, RA 4): **«g) Se han determinado las capacidades técnicas de sistemas de
escenografía virtual y su vinculación con las cámaras y el mezclador de imagen.»** Los decorados
virtuales y la realidad aumentada son el tema 12.

## 6. DVE

### El generador de efectos digitales

Un DVE transforma geométricamente una imagen antes de componerla. El manual ATEM da su uso más
corriente: **«Los efectos visuales digitales (DVE) se usan para mostrar una imagen más pequeña en un
recuadro con bordes sobre la imagen de fondo. La mayoría de los modelos cuentan con un canal para
efectos visuales que brinda la posibilidad de ajustar el tamaño de las ventanas o girarlas, así como
utilizar bordes tridimensionales o sombras paralelas.»** Sus parámetros, agrupados:

| Grupo | Parámetros | Qué hacen |
|---|---|---|
| Traslación (*location*) | X, Y, Z | Mueve la imagen. La Z la acerca o la aleja, y por tanto la agranda o la empequeñece en perspectiva |
| Tamaño (*size*) | X, Y, Z | Escala la imagen, con un valor por eje |
| Rotación | X, Y, Z | Gira la imagen sobre cada eje |
| Aspecto (*aspect*) | — | Cambia la proporción entre ancho y alto: deforma |
| Recorte (*crop*) | Superior, inferior, izquierda, derecha | Recorta la ventana |
| Perspectiva | — | Cuánto se nota la profundidad |
| Bordes | Anchura, color, sombra | El filete de la ventana |
| Esquinas (*corner pinning*) | Las cuatro esquinas | Cambia la perspectiva llevando cada esquina a un sitio |

El DVE trabaja en dos sitios del mezclador (oficio): como llave, que coloca una ventana sobre el fondo
y la mantiene; y como transición, en la que la imagen se mueve, gira o se encoge para dejar paso a la
siguiente (epígrafe 3).

### Tres operaciones que hay que saber hacer

- Meter una imagen en una pantalla que no está de frente. El *corner pinning* es el efecto que
  permite cambiar la perspectiva manejando la posición de las esquinas de la imagen: se llevan las
  cuatro esquinas de la imagen a las cuatro esquinas de la pantalla que aparece en escena y la imagen
  se deforma sola para encajar.
- Ampliar una imagen sin deformarla. En un DVE con perspectiva, mover la imagen hacia la cámara por
  el eje Z la agranda sin tocar su geometría: es un acercamiento, no una escala, y por construcción
  no puede deformarla. Cambiar el aspecto es exactamente lo que deforma; la rotación gira, no amplía;
  y variar el tamaño conserva las proporciones sólo si se aplica el mismo valor al ancho y al alto
  (ejes X e Y).
- Superponer una o varias ventanas. El efecto con el que se consigue la superposición de una o varias
  ventanas es el PinP, imagen dentro de imagen, que se construye con un DVE reduciendo y colocando la
  fuente sobre el fondo. No es lo mismo que el mosaico, que pixela la imagen, ni que la multi-imagen,
  que divide la pantalla en partes iguales sin superponer nada.

### La gafa y la composición múltiple

En los controles españoles se llama «gafa» a la composición de dos o más ventanas en pantalla: una
gafa 50/50 es la pantalla partida en dos mitades; una gafa 20/60/20, tres ventanas con la central más
ancha. Es vocabulario de plató, no término normalizado.

Una gafa se hace con tantos DVE como ventanas, o con un generador de composición múltiple. El manual
ATEM llama al suyo SuperSource, y lo da para sus modelos con más de un banco M/E: **«permite visualizar varias fuentes en un monitor al mismo tiempo»**
y **«solo utiliza una de las entradas del mezclador»**; se elige uno de sus formatos predeterminados y
se ajustan la posición, el tamaño y el recorte de cada ventana. Pese a la palabra «monitor» del
manual, SuperSource es una fuente que sale al aire —una composición—, no el monitor del control, que es
el multipantalla del epígrafe 7 (oficio).

El uso de la gafa es narrativo (epígrafe 3): pone en la misma pantalla a dos personas que no están en
el mismo sitio —el presentador y la conexión, dos invitados remotos— o a la persona y lo que comenta.

## 7. Señalización técnica

### Qué se entiende por señalización técnica

Ninguna norma ni documento publicado leído define la «señalización técnica» de un control. El manual
de los ATEM titula «Sistemas de señalización» el capítulo en el que explica cómo avisa el mezclador de
qué fuente está al aire: **«Los mezcladores ATEM pueden comunicarse con cámaras y monitores enviando
señales para identificar la fuente que está siendo transmitida.»** Y sigue: la señal **«se utiliza
generalmente para encender una luz roja sobre la cámara o el monitor, de forma que el operador sepa
que está al aire. Asimismo, en dispositivos tales como los monitores Blackmagic SmartView Duo o
SmartView HD, permite identificar las imágenes al aire y los anticipos mediante bordes de distinto
color. De esta forma, el equipo de producción puede determinar con facilidad la cámara cuya señal se
está transmitiendo.»**

En ese sentido, que es el núcleo del epígrafe, la señalización técnica es el conjunto de avisos con
los que el mezclador dice a todo el equipo en qué estado está cada fuente (oficio lo que no lleva
cita en los apartados siguientes):

| Aviso | Dónde se ve | Qué dice |
|---|---|---|
| Piloto rojo | En la cámara, delante y detrás; en monitores; en el plató | Esa fuente está al aire |
| Piloto verde | En las cámaras que lo admiten; en el multipantalla | Esa fuente está en previo |
| Botones iluminados | En el panel: bus de programa en rojo, bus de previo en verde | Qué hay en cada bus |
| Bordes del multipantalla | Alrededor de cada ventana: rojo, verde o blanco | Al aire, en previo o en ninguno |
| Etiqueta bajo monitor | Debajo de cada monitor o ventana | El nombre de la fuente, a veces con su piloto |
| Llamada | El piloto de la cámara parpadea | Atención: vas a salir |

En un sentido más amplio, la cualificación del ayudante pone entre lo que debe saber del control los
generadores de señales —sincronismos, logotipo, señales de prueba y cartas de ajuste—: son las
señales técnicas que no se ven en antena, pero sin las que el mezclador no funciona o no se puede
comprobar. Van al final del epígrafe.

### El piloto

El piloto —*tally*— es el sistema que enciende una luz roja en la cámara que está al aire. Va en
tres sitios a la vez:

- En la cámara, delante —para el presentador— y detrás o en el visor —para el operador—.
- En el multipantalla del control, con un recuadro rojo alrededor de la fuente que está al aire y
  uno verde alrededor de la que está en previo.
- En el plató, con luces generales de «en el aire» y con avisos en los monitores.

El manual en español de los mezcladores ATEM describe el piloto: la señal **«se utiliza
generalmente para encender una luz roja sobre la cámara o el monitor, de forma que el operador sepa
que está al aire.»** Y la llamada: **«Manteniendo presionado el botón CALL, la luz piloto de las
cámaras conectadas comenzará a parpadear. Esta es una manera muy útil de llamar la atención de los
camarógrafos o de indicarles que la señal va a ser emitida al aire.»**

Cuando la imagen que sale está compuesta por varias fuentes —unas ventanas con tres cámaras, por
ejemplo—, el piloto se enciende en todas ellas (oficio). La razón es la definición misma: el piloto marca lo
que está contribuyendo a la imagen que sale, no lo que está seleccionado en el bus de programa. Si
tres cámaras están dentro del compuesto, las tres están al aire, y sus tres operadores tienen que
saberlo para no moverse ni bajar el objetivo. El sistema de pilotos de un mezclador calcula esa
cadena hacia atrás: mira qué hay en programa, mira de qué está hecho, y enciende todas las fuentes
implicadas.

El manual ATEM confirma los dos lados de la cámara: en el protocolo con el que sus mezcladores
controlan por SDI las cámaras del fabricante (*Blackmagic SDI Camera Control Protocol*), el brillo del
piloto se regula junto o por separado, delante y detrás (**«Sets the tally front brightness.»**, **«Sets the tally rear brightness.»**).

### El piloto en el panel del mezclador

El panel repite los mismos colores en sus botones. En el bus de programa, **«La señal transmitida al
aire se indica mediante un botón que se enciende de color rojo.»**, con un aviso del fabricante:
**«Tenga cuidado al presionar uno de estos botones, ya la fuente seleccionada se emitirá al aire
inmediatamente.»** (así en el manual). En el modo de bancos A/B, uno es el bus de programa, **«que
indica la fuente transmitida mediante un botón encendido en rojo. El otro es el bus de anticipos y
dispone de un botón verde que permite ver las imágenes en forma anticipada.»** Y en el programa
informático de control, en la ventana de cada cámara: **«Cuando su señal está al aire, la barra
superior de la ventana se enciende en rojo e indica Al aire.»**

### Cómo llega el piloto a la cámara y a los monitores

El piloto sale del mezclador, que es quien sabe qué está al aire, y llega a cada cámara y a cada
monitor por una de cuatro vías:

| Vía | Cómo funciona | Fuente |
|---|---|---|
| Contacto | Un relé por fuente: se cierra cuando la fuente está al aire | Manual ATEM, GPI and Tally Interface |
| Retorno SDI | El mezclador manda el estado a las cámaras por la señal de retorno | Manual ATEM |
| Datos en la señal | El estado viaja como paquete de datos dentro del vídeo de programa | Protocolo de piloto de Blackmagic |
| Red | El estado viaja como mensaje por la red IP | TSL UMD sobre UDP; NMOS IS-07 |

Por contacto. Es la vía clásica y la de la GPI en sentido contrario (tema 4). En los ATEM la hace un
aparato aparte: **«El dispositivo GPI and Tally Interface cuenta con ocho relés mecánicos utilizados
en sistemas de señalización. La señal se envía desde el puerto Ethernet del mezclador ATEM al
dispositivo, y ambos deben compartir la misma red.»** A él **«se pueden conectar equipos compatibles
con sistemas de señalización por cierre de contacto»**; **«Es posible conectar hasta ocho unidades GPI
and Tally Interface. Solo es necesario contar con una unidad en el caso de mezcladores que disponen de
un solo banco de mezcla y efectos»**, y con varias se reparten los pilotos: **«se pueden asignar las
luces piloto 1-8 a la primera unidad, y las luces 9-16 a la segunda, y las luces 17-24 a la
tercera.»** Las cifras eléctricas son de ese aparato: **«Las entradas consisten en interruptores
ópticos que se activan por una conexión a tierra con un voltaje máximo de 5 V a 14 mA.»** y **«Las
salidas consisten en relés mecánicos conectados a tierra con un voltaje máximo de 30 V a 1 A.»**

Por el retorno SDI. Con cámaras del mismo fabricante, el piloto va por el cable que devuelve a la
cámara el programa. El manual lo cuenta en la puesta en marcha: **«presione uno de lo botones
correspondientes a una entrada a fin de seleccionarla como anticipo. Esto hará que la luz piloto en las
cámaras compatibles de Blackmagic Design se encienda de color verde. Al presionar el botón CUT o AUTO,
se producirá un corte o una transición para transmitir la fuente a través de la salida principal y por
ende la luz piloto se encenderá de rojo, indicando así que la cámara está al aire.»** (así, «lo
botones», en el manual).

Como datos dentro de la señal. El anexo para desarrolladores del manual, en inglés, describe el
protocolo propio de Blackmagic (*Blackmagic Embedded Tally Control Protocol*, versión 1.0, de
30-04-2014): **«It describes the protocol for sending tally information embedded in the non-active
picture region of a digital video stream.»** El reparto: **«A master device such as a broadcast
switcher embeds tally information into its program feed which is broadcast to a number of slave
devices such as cameras or camera controllers.»** El formato: **«Packets are encoded as a SMPTE 291M
packet with DID/SDID x51/x52 in the active region of VANC line 15.»**, y cada estado ocupa cuatro
bits, de los que dos dicen lo que importa: **«bit 0: program tally status (0=off, 1=on)»** y **«bit 1:
preview tally status (0=off, 1=on)»**. Es un protocolo de un fabricante, no una norma: lo que la
SMPTE fija es el formato del paquete, no el piloto.

Por la red. Los protocolos de etiquetas de TSL, que llevan también el piloto, **«can also be
implemented over UDP/IP»** (apartado siguiente). Y en una instalación IP normalizada, la familia NMOS
de la AMWA tiene una especificación para ello:

| Especificación | Título | Para qué sirve |
|---|---|---|
| IS-07 | **«Event & Tally»** | Eventos y piloto por la red |

Para el ayudante, IS-07 es la que toca de cerca: en una instalación IP, el piloto de las cámaras
(el *tally* que dice cuál está en el aire) también viaja por la red. Los directos IP son el tema 15.

Qué vía usan los controles de Canal Sur no consta en documento publicado leído.

### La llamada

El piloto sirve también para avisar sin hablar: es la llamada con el botón CALL, que hace parpadear
el piloto de las cámaras (arriba, en «El piloto»). En la puesta en marcha, el manual ATEM dice por
dónde va: **«al presionar el botón CALL, se transmite
una señal a las cámaras Blackmagic mediante la señal SDI de retorno y se activan simultáneamente las
luces piloto.»** La llamada no sustituye a la orden por intercom (tema 4): la refuerza, y sirve cuando
el cámara no tiene el intercom abierto o hay ruido en el plató (oficio).

### El multipantalla

El multipantalla (*multiview*) es la salida que junta en un solo monitor del control varias fuentes en
mosaico, cada una con su nombre, más el programa y el previo en grande. Es lo que el realizador mira
en lugar del plató. La norma de enseñanza lo pone entre las operaciones de apoyo del módulo 0905
(RA 6): **«b) Se ha determinado la configuración idónea de monitorizado en multipantalla, para la
realización de un programa de televisión.»**; y entre sus contenidos, **«Monitorizado en sistemas
multipantalla del control de realización.»**

### Qué enseña, según el manual ATEM

El manual ATEM, que lo llama modo de visualización simultánea, describe lo que lleva:

- Ventanas asignables: **«Las ocho ventanas pequeñas permiten ver cualquier fuente.»**, y el ATEM
  Constellation 8K permite ver 4, 7, 10, 13 o 16 fuentes, sustituyendo si hace falta las dos
  ventanas grandes del previo y del programa.
- El piloto en pantalla: **«El modo de visualización simultánea muestra además un borde rojo o verde
  alrededor de cada ventana función para diferenciar la señal al aire de los anticipos.»** Rojo es lo
  que está al aire; verde, lo que está en previo; blanco, lo que no está en ninguno de los dos:
  **«Si el borde es blanco, la fuente no corresponde ni a un anticipo ni a la señal al aire o la
  principal. El borde rojo indica que la fuente está siendo utilizada como señal principal, mientras que
  el borde verde corresponde a un anticipo.»**
- Las zonas seguras en el previo: **«La ventana de anticipos dispone de marcadores que indican el
  área de seguridad de la imagen y permiten asegurarse de que esta se verá correctamente en cualquier
  monitor.»**, con guías **«16:9 (horizontal) o 9:16 (vertical)»**.
- Los vúmetros: **«La opción Activados permite ver los vúmetros de todas las fuentes.»**
- Los nombres: las entradas se rotulan con el nombre que se les da en la configuración de fuentes
  (epígrafe 1).

Y cualquier señal interna puede ir a una ventana: la máscara de una llave, para ajustar un croma
(epígrafe 5), o la salida de un banco.

### Cómo se ordena

Configurarlo es decidir qué fuentes se ven, de qué tamaño y en qué orden (oficio): el programa y el
previo, grandes; las cámaras, en el orden en que se van a usar; los vídeos, los gráficos y las
conexiones exteriores, al lado de las cámaras con las que alternan. Con el croma o el decorado
virtual, una ventana para la máscara o para la señal limpia de la cámara del croma. En el directo, los
bordes son la comprobación rápida de la orden: la fuente que se va a pedir tiene que verse en verde
antes de la transición, y en rojo después (oficio). Quién ve qué en el control y los monitores de cada puesto son el
tema 4.

### Las etiquetas de los monitores: el protocolo TSL UMD

Debajo de cada monitor del control —o de cada ventana del multipantalla— va una etiqueta con el nombre
de la fuente, que puede llevar también su piloto. Cuando el nombre y el color los manda el mezclador o
el sistema de control por datos, lo hacen con un protocolo, y el más extendido es el de TSL Products,
según el propio fabricante: **«The TSL protocols are widely implemented throughout the industry,
especially for Multiviewer use.»** y **«There is no charge for the use of these protocols.»** Es
protocolo de un fabricante, de uso libre, no norma.

El documento de TSL (fechado el 19-09-2009) describe tres versiones:

| Versión | Qué es, según TSL | Datos del documento |
|---|---|---|
| UMD V3.1 | **«the TSL basic industry standard serial protocol»** | Línea serie **«RS 422/ RS 485»** a **«38k4 baud»**; cada mensaje lleva la dirección de la etiqueta (**«Display address (0-126) + 80 hex»**), un byte de control con cuatro bits de piloto y dos de brillo, y **«16 displayable ASCII characters»**: **«All 16 characters must be sent.»** |
| UMD V4.0 | **«extends the basic V3.1 protocol to add full control of text and tally lamp colours.»** | Colores de piloto y de texto en dos bits: **«0 = OFF; 1 = RED, 2 = GREEN, 3 = AMBER.»** |
| UMD V5.0 | **«a new protocol, specifically aimed at multiviewer display devices, over Ethernet.»** | **«Packets are sent via UDP. Maximum packet length is 2048 bytes.»**; **«Optionally, the protocol can operate over TCP/IP»**; direcciones **«up to 65,535 per screen»**; **«ASCII or Unicode character sets»** |

De las dos primeras dice TSL: **«These two protocols can also be implemented over UDP/IP where each UDP
packet contains one serial data packet.»** Y de la V3.1, que la comunicación va en un solo sentido:
**«The protocol described is for one way communication only.»** La etiqueta recibe; no contesta.

Para el ayudante, la consecuencia es de oficio: el nombre que se lee bajo el monitor es el que alguien
escribió en la configuración, y tiene que coincidir con el de la escaleta y con el que se canta. Una
etiqueta V3.1 admite dieciséis caracteres; el nombre corto de una fuente ATEM, cuatro (epígrafe 1).

Qué protocolo, qué multipantalla y qué etiquetas usan los controles de Canal Sur no consta en
documento publicado leído.

### La sincronización

Dos señales de vídeo sólo se pueden conmutar limpiamente si sus imágenes empiezan en el mismo
instante. Si no, el corte cae en mitad de un cuadro y la imagen salta. De ahí que todo un centro de
producción trabaje contra una misma referencia de sincronismo, que se genera en un sitio y se
reparte a todos los equipos.

Las dos señales de referencia:

| Referencia | Qué es | Para qué |
|---|---|---|
| Black burst | Una señal de vídeo negro completa, con sus sincronismos y su salva de color | La referencia clásica, de la definición convencional; sigue sirviendo para sincronizar equipos de alta definición |
| Tri-level sync | Un impulso de tres niveles —positivo, negativo y reposo—, definido para alta definición | La referencia de los formatos de alta y ultraalta definición, más precisa |

El aparato que las genera se llama generador de sincronismos, y lo que hace cada equipo al
recibirla es engancharse a ella: eso es el *genlock*.

Las señales que llegan de fuera y no están en fase con la casa pasan por un sincronizador de cuadro,
que las retrasa uno o varios cuadros; ese retraso descuadra la imagen con el sonido y con las demás
fuentes, y por eso las fuentes llevan un retardo entre sus atributos. Los sincronizadores, el retardo
diferencial y la GPI están en el tema 4; la sincronía entre imagen y sonido, en el tema 11.

### Los generadores de señales del control

La cualificación los enumera entre los contenidos del módulo del control (MF0217_3, p. 20): **«5 Los
generadores de señales»**: **«Generador de sincronismos.»**, **«Generador de logotipo.»**,
**«Generador de señales test.»** y **«Generador de cartas de ajuste.»** No los describe. Lo que se ha
podido confirmar de cada uno:

| Generador | Para qué sirve (oficio, salvo cita) | Dónde está en el tema |
|---|---|---|
| De sincronismos | Da la referencia a la que se enganchan todos los equipos | Apartado anterior |
| De logotipo | La mosca de la cadena | La mosca entra en una llave posterior (epígrafe 4); el aparato concreto no consta en documento leído |
| De señales de prueba | Barras de color, con su tono, para comprobar la cadena | Abajo |
| De cartas de ajuste | No se ha leído fuente que las describa | — |

Las barras de color son la señal de prueba que el ayudante verá más. El mezclador las genera: en el
manual ATEM, **«Otra de las fuentes disponibles son las barras de color generadas internamente. Son
útiles para comprobar las señales transmitidas desde el mezclador o realizar una composición por
crominancia con un vectorscopio.»** Y las cámaras también: desde la ventana de control de cada cámara del programa del
mezclador se pueden mostrar u ocultar las barras de las cámaras del fabricante, y **«Esta función es de suma utilidad para identificar las unidades de forma visual
durante la preparación de un programa en directo. Asimismo, dicha señal incluye un tono auditivo que
brinda la posibilidad de comprobar o modificar la intensidad del volumen de cada cámara.»** Barras en
una cámara concreta dicen, en el multipantalla, qué ventana es cuál: es una comprobación de
señalización antes del ensayo (oficio).

La norma que define las barras de color de alta definición no se ha podido leer para este tema, y no
se cita.

### Lo que comprueba el ayudante

El manual ATEM, en su puesta en marcha, pone la comprobación de los pilotos después de la del
intercom: **«Después de haber comprobado el funcionamiento del sistema de comunicación, es buena idea
verificar que la luz piloto está operativa en todas las cámaras.»** Y da la avería típica: **«Si las
luces piloto no se encienden, compruebe que los números de las cámaras corresponden a las entradas
asignadas en el mezclador.»**

Con eso y con la cualificación (MF0217_3, CE1.5: **«que el mezclador está preparado»**), la
comprobación de la señalización que hace el ayudante con el mezclador antes del ensayo es ésta
(oficio):

1. Cada cámara, por su número: se pasa a previo y a programa, y su operador confirma que ve verde y
   luego rojo, delante y detrás.
2. Unas ventanas o una gafa: se comprueba que se encienden los pilotos de todas las cámaras que
   entran en el compuesto.
3. Los nombres: los del panel, los del multipantalla y los de las etiquetas coinciden entre sí y con
   la escaleta.
4. Los bordes: rojo el programa, verde el previo.
5. La llamada: cada cámara ve parpadear su piloto.
6. Las barras o la identificación de cada cámara, si hay duda de qué ventana es cuál.

Lo que falla se anota y se avisa al realizador, como pide la cualificación con cualquier incidencia
del parte de emisión (UC0217_3, RP1, epígrafe 1), y al técnico que lleva el equipo afectado (oficio).
La gestión de incidencias en el directo es el tema 6.

## Aplicación práctica: el ayudante y el mezclador en un informativo

El caso: un informativo de media hora con dos presentadores en plató, tres cámaras, un servidor de
vídeos, dos conexiones exteriores, un titulador, un espacio del tiempo en croma y un gráfico de datos.
Lo que sigue es un orden de trabajo de oficio para el ayudante, apoyado en la cualificación (UC0217_3,
RP1, CR1.2, CR1.3 y CR2.1; MF0217_3, CE1.5 y CE1.6). El ayudante no configura el mezclador: comprueba
con quien lo opera que está como la escaleta pide.

Antes del ensayo:

1. Entradas y nombres (epígrafes 1 y 7). Una lista común con el mezclador: qué fuente va en cada
   botón —cámaras 1 a 3, servidor A y B, exteriores 1 y 2, titulador, cámara del croma— y con qué
   nombre largo y corto; que coincida con el multipantalla, con las etiquetas y con la escaleta.
2. Pilotos (epígrafe 7). Cada cámara en previo y en programa; la gafa de las conexiones y las
   ventanas, con todos sus pilotos encendidos; la llamada. Si una cámara no enciende, se comprueba que
   su número corresponde a su entrada.
3. Transiciones (epígrafe 3). Cada paso de la escaleta con su transición y su duración: corte por
   defecto; encadenado para el paso a los sumarios con música; transición animada o cortinilla sólo en
   los separadores; fundido a negro al final. Coleos de los vídeos contra la transición prevista.
4. Llaves (epígrafe 4). Mosca y rótulos en las llaves posteriores; que el primer rótulo del titulador
   sale limpio, sin borde oscuro; la llave de croma y el DVE de la gafa, en el banco.
5. Croma (epígrafe 5). Con el presentador del tiempo en su marca, la luz definitiva y el vestuario
   revisado (LE 8.6.1): la máscara limpia en su ventana del multipantalla.
6. Memorias (epígrafe 2). Que las macros de entrada y salida están ensayadas enteras, con el
   mezclador fuera del aire, y cuánto duran, para el minutado.

En el directo (tema 6): se anticipa cada transición y cada efecto con la orden, se vigila en el
multipantalla que la fuente pedida está en verde antes de la transición y en rojo después, y se
cuenta el tiempo de los gráficos y de las piezas.

Incidencias que el tribunal puede plantear y su respuesta de oficio:

| Incidencia | Qué hace el ayudante |
|---|---|
| Una cámara no enciende su piloto | Avisa; se comprueba que el número de la cámara corresponde a la entrada asignada en el mezclador; mientras, se le avisa por intercom de cuándo está al aire |
| En unas ventanas, un cámara mueve el plano porque cree que no está al aire | Recuerda al equipo que en un compuesto el piloto se enciende en todas las cámaras que lo forman, y comprueba que así ocurre |
| El nombre de una fuente no coincide con el de la escaleta | Lo corrige en su lista y avisa al mezclador y al realizador antes del directo: una orden con un nombre equivocado se entiende mal |
| El croma deja bordes verdes en el pelo | Avisa al realizador; el ajuste es del mezclador (control de borde o de rebase) y, si no basta, se sale a un plano sin croma |
| Un rótulo sale con el borde oscuro | La señal venía premultiplicada y no se declaró en la llave: aviso al mezclador |
| Se pide mover la ventana de una gafa que va dentro de un *timeline* ya lanzado | No se puede hasta que termine: hay que cancelarlo o esperar |
| Un vídeo trae el coleo corto para el encadenado previsto | Aviso al mezclador y al operador de sonido; se cambia a corte o se acorta la transición |

## Normativa que el tema invoca

| Norma | Qué se cita | Redacción |
|---|---|---|
| Real Decreto 1680/2011, de 18 de noviembre, por el que se establece el título de Técnico Superior en Realización de proyectos audiovisuales y espectáculos y se fijan sus enseñanzas mínimas (BOE núm. 302, de 16-XII-2011) | Módulo 0905, RA 1 f), RA 5 y criterios c) y e), RA 6 b), d) y e), y contenidos; módulo 0910, RA 4 b) y g) | Texto de 2011. Lo modifica el Real Decreto 500/2024, de 21 de mayo, que suprime otros módulos y no toca los citados |

Es norma de enseñanza: dice lo que aprende quien se forma para realizar, no cómo trabaja la RTVA.

## Lo que este tema no da, y dónde está

- Qué mezclador, qué titulador, qué multipantalla, qué sistema de pilotos y etiquetas y qué sistema
  de grafismo o de plató virtual tienen los controles de Canal Sur: no consta en documento publicado
  leído.
- Un manual de identidad gráfica de Canal Sur (mosca, tipografías, cortinillas, ráfagas): no se ha
  localizado publicado.
- La documentación de otros fabricantes de mezcladores (Sony, Grass Valley, Ross, Panasonic) no se ha
  leído: la nomenclatura que no es de Blackmagic (DME, SÚPER MIX) se da como uso del oficio, sin
  contrastar en su fabricante. Tampoco la de sistemas de incrustación externos como Ultimatte.
- La versión vigente del protocolo TSL UMD: el documento leído es de 2009 y no se ha leído otro
  publicado por TSL. El texto de la especificación NMOS IS-07 no se ha leído para este tema: se da su
  título y su objeto.
- La norma de las barras de color de alta definición y la de las cartas de ajuste: no se han podido
  leer.
- El criterio de la casa sobre el uso de los recursos en los informativos (Libro de Estilo, 6.5) y su
  uso por géneros: los desarrolla el temario del Realizador/a; al ayudante le toca comprobar que se
  cumple lo que el realizador decide.
- El panel, las salidas, los auxiliares, los sincronizadores, la GPI, el piloto como parte de las
  comunicaciones del control, el titulador y quién opera cada equipo en la RTVA: tema 4.
- Órdenes, cantar las transiciones, llamadas e incidencias en el directo: tema 6.
- Plano, eje, ritmo y elipsis: tema 1.
- Rotulación, zonas seguras, realidad aumentada, decorados virtuales y pantallas del plató: tema 12.
- Transiciones y efectos en la sala de montaje: tema 13. Submuestreo de color y formatos: tema 14.
- Sincronía entre imagen y sonido: tema 11. Directos IP: tema 15.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| Blackmagic Design, manual en español de los mezcladores ATEM (edición de diciembre de 2024), epígrafes de transiciones, composición de imágenes (luminancia, lineal, crominancia y crominancia avanzada, geométrica, efectos visuales digitales), transiciones animadas, SuperSource, visualización simultánea, ajustes de fuentes, macros, reproductores multimedia, máscaras y fundido a negro | Tipos de transición y sus mandos; parámetros de la cortinilla y cortinilla con gráficos; máscara de la llave; fundido a negro; transición animada; composiciones previas y posteriores; luminancia y lineal; croma y sus controles; rebase; DVE; figura; SuperSource; multipantalla; nombres de fuente; macros; *clip store*; salida del alfa | Descargado el 03-09-2026; releído el 24-09-2026 |
| Real Decreto 1680/2011 (BOE-A-2011-19599), texto del diario oficial; vigencia comprobada en su ficha (modificación por el Real Decreto 500/2024) | Lo que la norma de enseñanza pide hacer con el mezclador, el multipantalla, el titulador y la grabación; usos narrativos de las transiciones | 24-09-2026 |
| *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004: 3.6.1, 3.10, 3.16 a 3.16.2, 6.5.1, 6.5.2, 8.6.1 y 9.9.2 | Rótulo, cierres, gráficos, criterio de realización informativa, vestuario ante el croma, imágenes duras | 24-09-2026 |
| Francisco José Mateu Torres, *Fundamentos teóricos de la edición y el montaje audiovisual*, Elche, Editorial UMH, 2024, 3.2 | Fundido y encadenado | Texto tomado del tema cerrado del puesto de Operador/a Montador/a de Vídeo |
| Adobe, ayuda de Premiere, «Transitions overview» (actualizada el 07-01-2026); Blackmagic Design, *DaVinci Resolve 21*, cap. 55 | Corte y transición | Texto tomado del tema cerrado del puesto de Operador/a Montador/a de Vídeo |
| Blackmagic Design, manual en español de los mezcladores ATEM (edición de diciembre de 2024): «Sistemas de señalización» y GPI and Tally Interface; puesta en marcha (comprobación de pilotos y llamada); botones de los buses de programa y de anticipo; botón de llamada; ventana de control de cámara; barras de color del mezclador y de las cámaras; anexos en inglés *Blackmagic SDI Camera Control Protocol* (parámetros de brillo del piloto) y *Blackmagic Embedded Tally Control Protocol* (versión 1.0, 30-04-2014) | Qué es la señalización; piloto delante y detrás; piloto en el panel; vías del piloto (contacto, retorno SDI, datos en la señal); llamada; barras de color; comprobación de pilotos y su avería típica | 29-09-2026 |
| TSL Products, «TSL UMD Protocol», documento fechado el 19-09-2009 (web del fabricante) | Protocolos de etiquetas de monitor V3.1, V4.0 y V5.0: uso, gratuidad, línea, caracteres, colores, UDP y TCP/IP, sentido único | 29-09-2026 |
| AMWA, especificación NMOS IS-07 «Event & Tally» | Piloto por la red | Texto tomado del tema cerrado 15 de Realizador/a |
| Tema cerrado 4 de Realizador/a, epígrafe «El piloto» | Qué es el piloto, dónde se enciende, llamada, piloto en un compuesto | Texto tomado literal; sus fuentes, en ese tema |
| INCUAL, cualificación IMS077_3 «Asistencia a la realización en televisión», documento publicado (Orden PCI/797/2019): UC0217_3 (RP1, CR1.2, CR1.3, CR2.1; p. 7) y MF0217_3 (CE1.5 y CE1.6, p. 18; contenidos 5 y 6, p. 20) | Lo que se pide al ayudante respecto del mezclador, las transiciones y el parte de emisión; generadores de señales | 29-09-2026 |

Oficio y física de la señal, declarados así en el texto: las tres funciones del mezclador y la tabla
de funciones; el M/E como mezclador dentro del mezclador; la tabla de modos de transición y la
distinción entre NAM y FAM; las tres señales, la fórmula del compuesto y la diferencia entre llave
lineal y aditiva; clip y ganancia; la premultiplicación; el uso de la máscara en el croma; *self key*
y *show key*; la tabla de tipos de llave y el *coring*; el croma con cualquier color y el porqué del
verde y el azul; croma en directo y decorado virtual; los parámetros del DVE, el *corner pinning*, el
eje Z y el PinP; la gafa; la tabla de memorias y el comportamiento de un efecto programado en marcha;
el *clip store*; los atributos de la fuente; *black burst*, *tri-level* y *genlock*; el orden de las
capas y la salida limpia; los criterios de uso por recurso; la tabla de la señalización técnica; la
llamada frente al intercom; la tabla de generadores; la comprobación de la señalización y de las
transiciones por el ayudante; la sigla VANC; y la aplicación práctica.
