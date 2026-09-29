# Grafista (15) · Tema 9 · Redacción (fase 2)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`
(unas 10.500 palabras con tablas; 43 epígrafes). Fecha de trabajo del encargo: 24-09-2026; fecha de
sistema en que se redactó: 29-09-2026. Escrito por partes (cabecera, §1 a §6, cierre), guardando cada
una.

Ficheros tocados: sólo el tema y este informe. `herramientas/indice.py` generó el índice.
`refutar_prosa.py`: quedan 3 avisos (PRIME, CAMIO, XQ), nombres de producto presentados como tales en
el párrafo de términos, igual que en el tema 6; se quitaron del párrafo de siglas las no usadas (SDI,
UHD, NRCS, *fill*/*key*, *watch folder*) y se presentaron SMPTE, EBU y README. El tema no cita norma
legal (sólo el convenio, copiado de tema cerrado): basta `refutar_prosa.py` e `indice.py`.

## Material usado

- Investigación B, §9 (y §5.2, 5.3, 6.3, 6.4, 8.2, 8.3 en lo que toca a herramientas). Fuentes leídas
  por el investigador el 29-09-2026; el redactor no las ha releído: todo lo nuevo pasa por verificación.
- RTVE `temas/diseno-grafico/10-equipos-y-programas-de-diseno.md` (sin actualizar): copiado lo técnico,
  quitados números de pregunta, respuestas oficiales, plantilla, reparto del banco y avisos de estudio.
- **No copiados de RTVE, por no poder confirmarse** (salen de respuestas oficiales, no de fuente): 56
  canales máximos, 30.000 píxeles de composición, límite de 2 GB del PSD, «H.265 ahorra hasta un 50 %».
  Declarado en «Lo que este tema no da».
- Temas del propio puesto (1, 3, 5, 6, 8) sólo remitidos: no están cerrados y no se copian.

## Copiado del común

Literal de temas cerrados de Canal Sur (verificación y refutación lo saltan):

De `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`:

1. «Plantillas de rótulo»: desde «Resolve trae generadores de rótulos…» hasta «…Todas esas páginas
   llevan fecha de 7-I-2026.», entero, en §5 «Plantillas de rótulo en el programa de edición». El
   párrafo siguiente («La otra vía…») va **adaptado** (quitado «(epígrafe 4)»): se verifica.
2. «Plantillas de salida: los *presets*»: párrafo de entrada, las dos viñetas (Resolve, Premiere) y la
   primera frase de «Que el *preset* se pueda mandar…»; omitida la frase final de remisiones. §5.
3. «Plantillas de nombre: las variables de metadatos»: sus dos primeros párrafos, enteros; omitido el
   tercero. §5.
4. §4 «El protocolo MOS»: el párrafo de definición («La web del proyecto MOS lo define así…») y las
   viñetas «El reparto de papeles», «Los tres tipos de mensajes», «Cómo viaja», «Versiones vigentes» y
   «No es una norma oficial», literales. La frase que las presenta se acortó (sin «leídas el
   25-09-2026»). §6 «La escaleta manda».
5. Viñeta «Cola de *render*», entera. §6 «Automatizar la salida».
6. Viñeta «Integraciones por *scripts*», sin su última frase («Es la vía por la que un MAM…»). §6
   «Los *scripts*».
7. Párrafo «Lo que la automatización no hace, como oficio…», entero. §6 «Automatizar la salida».

De `temas/canal-sur-especificos/33-realizador-a/12-grafismo-rotulacion-ra-decorados-pantallas.md`:

8. «Diseñar, rellenar y lanzar», primer párrafo entero («En un control moderno…» hasta «…for
   playout.»»). §5 «Plantillas en el sistema de grafismo de directo».

De `temas/canal-sur-especificos/33-realizador-a/04-organizacion-control-realizacion.md`:

9. Párrafo «En la RTVA, el diseño es del Grafista (5345100, p. 129): …La ficha no le atribuye el
   lanzamiento de rótulos en el control.», entero. §1 «Qué dice el convenio». La cita de la función
   básica que lo precede está en la tabla de ese mismo tema (fila Grafista); la frase que la presenta
   es nueva.

## Copiado de RTVE sin cambios

Pasajes técnicos de `temas/diseno-grafico/10-equipos-y-programas-de-diseno.md` (sin actualizar),
copiados sin tocar una palabra (sólo quitada la negrita, que en RTVE no marcaba literal). El
verificador comprueba sólo que es literal:

- Tabla de las cinco familias, salvo la cabecera de la última columna (ver «Adaptado»). §1.
- Tabla «Renderizado diferido / Tiempo real». §1.
- Tabla de programas de tiempo real (Unreal, Unity, Vizrt, Chyron), sin el ✔. §1.
- «Por qué un motor de videojuego está en el temario de un grafista de televisión: porque la
  escenografía virtual y la realidad aumentada de los platós se calculan hoy con ellos.» §1.
- «Qué es un trazado, en una línea: una curva vectorial dibujada dentro de un documento de mapa de
  bits. No pinta píxeles: describe un contorno, y de ahí que sirva para recortar con precisión lo que
  una selección a mano no consigue.» §2.
- «Qué es un canal…» (dos frases, «Una imagen en rojo, verde y azul tiene tres canales…»). §2.
- Tabla «¿Conserva capas?» (sin ✔); tabla «Para qué nació / ¿Admite CMYK?» (sin ✔) y el párrafo «La
  regla que lo fija…» (tres frases). §2.
- Tabla de las cuatro funciones del vectorial; tabla de las cinco operaciones de buscatrazos; párrafo
  «Cómo se decide mirando…». §2.
- «La regla es que una curva Bézier necesita los dos extremos Y los controles que la doblan, y una
  lista sin nodo inicial y final está incompleta.» §2.
- «La distinción es que el área de trabajo es un TRAMO DE TIEMPO…» (frase entera). §3.
- «Y es la regla que gobierna el orden de apilamiento: …lo de arriba tapa a lo de abajo.» §3.
- «Una luz es un objeto del espacio, y una capa plana no está en el espacio. Sólo lo que tiene
  profundidad puede recibir una luz. La consecuencia práctica que conviene llevar: …las capas.» §3.
- «Qué hace precomponer, en una línea: …Es la manera de aplicar un efecto al conjunto y no a cada una
  por separado.» §3.
- Tabla de los cuatro parámetros de una máscara (sin ✔). §3.
- Tabla de interpolación espacial/temporal. §3.
- «La palabra que decide es COPIA: …Un programa serio no mueve lo que no es suyo.» y «Para qué sirve,
  que es lo que hay que entender: …es no haberlo hecho.» §3.
- Tabla de formatos de fichero (nueve filas) y «La regla que este cuadro deja para el examen: …es
  `JPG`.» §4.
- «La razón es la definición misma de «sin compresión»: …cambian cuántos píxeles hay.» §4.

## Adaptado de RTVE (se verifica)

- Tabla de familias: cabecera «Programas del enunciado» → «Programas de ejemplo».
- Frases que en RTVE eran respuesta oficial, reescritas como afirmación sin número de pregunta:
  vectorial y ampliación (con su matiz: «El matiz: un programa de mapa de bits, aun así, admite objetos
  vectoriales…», «En la práctica una ampliación al doble…», «“Casi no se nota” no es “sin pérdida
  alguna”»); trazado; PSD; PNG sin CMYK; características de la curva Bézier; área de trabajo; capa en
  primer término (y «En cuanto hay capas de tres dimensiones…», sin «Ésa es exactamente la trampa…»);
  luces; precomponer; calado («La expansión también modifica el borde: pero lo mueve, no lo
  difumina.»); interpolación; *wiggle* («suele llamarse efecto aunque es, en rigor, una expresión…»);
  recopilar archivos; TGA sin compresión.
- *Blueprints*: «son el sistema de programación visual de ese motor, en el que se programa uniendo
  nodos con cables en vez de escribiendo código» (de «Qué son, en una línea: …»).

## Lo nuevo que el verificador debe cotejar

Citas de la investigación B: Resolve 21 (presentación «integrates editing…»; caps. 56 p. 1226, 73 pp.
1634 y 1640, 77 p. 1728, 79 máscaras de polígono y nodos de máscara, 139 «Studio Version Only»);
Blender 5.2 (Render, Ray Tracing «but much slower», Interpolation, «a free form Bézier mode»); Apple
ProRes; Vizrt (Viz Multiplay «Uses Viz Engine for playout», Pilot Data Server, MOS; Dual Channel
«external application»; licencia por *dongle*); Chyron (Base Scenes con la frase «With full access…»,
Logic-based scenes, CAMIO, HTML Input, Playout Automation); Unreal (Quickstart «an Internal Editor
plugin for broadcasting» y la lista de usos; Rundown Server: tres citas y «combining two APIs»);
CasparCG (README: definición, 2006, GPLv3, cliente). Cita nueva de la función básica del Grafista
(convenio, ficha 5345100). Atribución: «Template Builder … supports scripting (Typescript)» se reutiliza
del párrafo copiado de Realizador/a 12. Paráfrasis a vigilar: la carpeta vigilada con el fragmento
**«without any additional human interaction needed»** (cap. 8, p. 215, vía Montador/a 13); «la mezcla
de dos imágenes se hace en un nodo *Merge*» se apoya sólo en la regla de p. 1728.

Oficio declarado: dos mitades del enunciado; familias añadidas (edición, directo); licencias;
qué se diseña en cada familia; capas frente a nodos; edición lineal/no lineal; dos puertas al montaje;
reparto fichero/plantilla; definición de plantilla y tabla de lo que fija; definición y cuatro niveles
de automatización; diseño para datos y camino manual; lectura común de los tres sistemas; aplicación
práctica.

## Diez preguntas tipo test (comprobación de cobertura)

1. (Herramientas, familias) Se puede duplicar el tamaño de una imagen sin ninguna pérdida de calidad:
   a) siempre, con buen remuestreo; b) sólo si es vectorial; c) sólo en TIFF; d) nunca. → b. §1 «Las
   familias de programa». **Entera.**
2. (Herramientas, convenio) Según su ficha del convenio, al Grafista de la RTVA le corresponde: a)
   lanzar los rótulos en el control; b) crear y realizar, con criterios artísticos, el diseño gráfico de
   canales y programas, y realizar escenarios virtuales; c) montar las piezas; d) operar el titulador.
   → b (la ficha no le atribuye el lanzamiento). §1 «Qué dice el convenio». **Entera.**
3. (Diseño, imagen fija) El formato que NO admite CMYK es: a) PSD; b) JPG; c) TIFF; d) PNG. → d. §2.
   **Entera.**
4. (Diseño, vectorial, práctica) Dos formas solapadas quedan reducidas a la zona común. Operación de
   buscatrazos: a) unir; b) restar; c) intersecar; d) excluir. → c. §2. **Entera.**
5. (Composición) Una luz añadida a una composición no ilumina nada. Lo más probable: a) la luz está en
   una capa inferior; b) las capas no tienen activada la tercera dimensión; c) falta precomponer; d) el
   calado es cero. → b; y con sólo capas 2D delante está la de numeración más baja. §3. **Entera.**
6. (Composición, práctica) Un logotipo 3D compuesto en Fusion muestra un borde claro. Según el manual,
   la regla incumplida probablemente es: a) mezclar con la imagen premultiplicada; b) corregir color
   sobre la premultiplicada; c) usar PNG; d) filtrar la directa. → a (y no premultiplicar dos veces). §3
   «El alfa dentro del compositor». **Entera.**
7. (Edición, entrega) Una cortinilla animada que va encima del programa se entrega en: a) ProRes 422
   HQ; b) JPG en secuencia; c) ProRes 4444 o 4444 XQ, o secuencia PNG/TGA; d) H.264. → c (únicos ProRes
   con alfa). §4 y «Aplicación práctica». **Entera.**
8. (Plantillas, edición) Un fichero .mogrt: a) es un *preset* de exportación de Resolve; b) es una
   plantilla de *motion graphics* que se crea en Premiere o After Effects y se usa en Premiere; c) se
   exporta desde Premiere aunque venga de After Effects; d) sólo admite texto. → b (la exportación desde
   Premiere no vale para las creadas en After Effects; las de datos admiten texto, color y números). §5.
   Y los *presets* de Resolve se guardan en .xml. **Entera.**
9. (Plantillas y automatización en directo) En Viz Pilot Edge, las plantillas las crea el equipo de
   diseño con: a) Viz Multiplay; b) Template Builder, que admite programación en TypeScript; c) Viz
   Trio; d) el sistema de redacción. → b; y en Fusion los *scripts* se escriben en Lua o Python
   (FusionScript). §5 y §6. **Entera.**
10. (Automatización, redacción) El protocolo MOS: a) es una norma SMPTE; b) comunica el sistema de
    redacción con servidores de vídeo, audio, imágenes fijas y generadores de caracteres, con tres tipos
    de mensajes (datos descriptivos, intercambio de listas y de estados), y no es norma oficial; c) sólo
    sirve para vídeo; d) sustituye a la escaleta. → b. §6 «La escaleta manda». **Entera.**

Resultado: las diez se contestan enteras con el tema; no ha hecho falta ampliar tras la comprobación.
Durante la redacción, pensando en el test y en la prueba práctica, se añadieron la sección de licencias
y versiones, el cuadro de cuatro niveles de automatización, el diseño para datos con camino manual y
los cuatro casos de aplicación práctica.
