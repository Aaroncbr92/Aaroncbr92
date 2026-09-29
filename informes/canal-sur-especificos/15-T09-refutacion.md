# Grafista (15) · Tema 9 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`
(10.077 palabras, 43 epígrafes). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el
29-09-2026 (fecha del sistema). No se ha corregido nada en el tema.

Ficheros tocados: este informe y `15-T09-preguntas.md`. Nada más.

Saltado en exactitud (según `15-T09-redaccion.md`): los nueve pasajes «Copiado del común» (Montador/a
13, Realizador/a 12 y 04) y los «Copiado de RTVE sin cambios». La cobertura mira el tema entero.

## Lente 1 · Exactitud contra la fuente

Fuentes cotejadas (copias descargadas en la verificación, leídas el 29-09-2026): *DaVinci Resolve 21
Reference Manual* (texto completo), Blender 5.2 LTS Manual (Glossary; Keyframes), *Apple ProRes* (IV-2022),
Vizrt (*Introduction to Viz Artist*, *Viz Multiplay* 3.3, *Viz Engine* 5.2 «Dual Channel Mode»), Chyron
(*PRIME CG*, nota PRIME 5.3 de 12-II-2026), Epic (UE 5.8, *Motion Design Quick Start* y *Rundown
Server*), README de CasparCG.

Comprobación mecánica de todas las negritas entre comillas contra esas fuentes: las que no aparecen
son todas de pasajes copiados del común (Adobe, Viz Pilot Edge, MOS, Manfredi) o del convenio (literal
del tema cerrado de Realizador/a 04, fila Grafista). Lo nuevo aparece literal. Páginas y capítulos de
Resolve comprobados por el pie impreso y el rótulo «Chapter N»: cap. 1 p. 13; cap. 8 p. 215; cap. 56
p. 1226; cap. 66 p. 1449; cap. 73 pp. 1634 y 1640; cap. 77 p. 1728; cap. 79 p. 1775; cap. 139 p. 3339;
cap. 187 p. 4215: todo correcto. Traducciones y paráfrasis (borde claro sólo al mezclar sin
premultiplicar; *Merge* de dos entradas; máscara de polígono «la más usada»; Magic Mask v2 con IA y
«Studio Version Only»; carpeta vigilada del Blackmagic Proxy Generator; *render* remoto que no va en
la versión gratuita): fieles.

### Hallazgos

**Graves: ninguno.**

**Menores (3):**

1. **Error 9 · §1 «Licencias y versiones», l. 213.** «DaVinci Resolve tiene una versión gratuita y una
   de pago, Studio». El manual dice «free version» y «Studio Version Only» / «Resolve Studio only», pero
   en ningún sitio que Studio sea de pago (se buscó «purchase», «paid», «license key»: nada sobre
   Studio). La verificación lo dejó anotado sin corregir. Propuesta: «una versión gratuita y otra,
   Studio, con funciones que la gratuita no tiene», o quitar «de pago».
2. **Error 9 · §1 «Las familias de programa», l. 168.** «La primera fila del cuadro es la que más se
   pregunta»: resto adaptado de RTVE («La pregunta 78 mide exactamente esa primera fila»). En Canal Sur
   no hay exámenes anteriores; la afirmación no tiene apoyo. Propuesta: «La primera fila del cuadro es
   la que más conviene tener clara: …».
3. **Error 5 · §5 «Plantillas en el sistema de grafismo de directo», l. 580.** «UE 5.8» sin presentar
   (en el resto del tema es «Unreal Engine 5.8»). Propuesta: «Unreal Engine 5.8». (En la misma línea
   de cosas, «LTS» de *Blender 5.2 LTS Manual* es parte del título de la fuente; se puede dejar.)

Sin hallazgo, comprobado: remisiones a temas del puesto (1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 15, 17, 18)
casan con los puntos del enunciado; la regla del premultiplicado aplicada en «Aplicación práctica»
(«se corrige el color sobre la directa») coincide con «Only color-correct images that are not
premultiplied»; «Ningún ProRes 422 lleva alfa» se sigue de «the only ProRes codecs that support alpha
channels».

Lentes automáticas (tema técnico sin norma): `refutar_prosa.py`, 3 avisos (PRIME, CAMIO, XQ), nombres de
producto ya presentados como tales; aceptados. `indice.py`: índice al día, 10.077 palabras, 43 epígrafes.
El detector de siglas no ve «UE» (dos letras): hallazgo 3 visto a mano.

## Lente 2 · Cobertura del enunciado

Enunciado: «Herramientas profesionales de diseño, composición, edición, plantillas y automatización
gráfica.» Los cinco términos tienen epígrafe propio, en su orden, más la aplicación práctica. Diseño
(mapa de bits, vectorial, formatos), composición (capas/nodos, línea de tiempo, máscaras,
interpolación, alfa, recopilar), edición (entrega y reparto con montaje), plantillas (edición, compositor,
directo, salida, nombre) y automatización (expresiones, *scripts*, datos, MOS, emisión, salida):
cubiertos.

Preguntas (`15-T09-preguntas.md`): 15; **13 enteras, 1 a medias, 1 no**.

**Laguna (1):** la creación de plantillas y la automatización en los programas de Adobe distintos de
Premiere. El tema dice que el .mogrt «se diseña en After Effects» pero no cómo (panel *Essential
Graphics*, qué propiedades se exponen), y sólo nombra las variables y los conjuntos de datos de
Photoshop, sin decir qué hacen; tampoco las acciones ni el procesamiento por lotes. Está declarado en
«Lo que este tema no da» como documentación no leída, pero Adobe es la familia de ejemplo del propio
cuadro de familias y ambas cosas son de test y de prueba práctica (preguntas 14 y 15). Propuesta de
remate (Opus, amplía): leer la ayuda de Adobe (helpx.adobe.com: After Effects, «Essential Graphics
panel» / «Create Motion Graphics templates»; Photoshop, «Data-driven graphics» y «Automate with
actions» / «Process a batch of files») y añadir en §5 «Hacer la plantilla propia en un compositor» y
en §6 «Los *scripts*» un párrafo con cita en cada caso; si sigue sin poder leerse, se queda declarado.

## Resumen

Graves 0 · menores 3 · lagunas 1. Cero errores de fuente en lo nuevo; el tema está bien construido y
cita con página. El remate aplica tres correcciones de redacción y, si puede leer la ayuda de Adobe,
amplía; en ese caso, fase 5 bis sobre los pasajes nuevos.
