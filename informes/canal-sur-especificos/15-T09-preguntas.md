# Grafista (15) · Tema 9 · Preguntas de refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`.
Fecha de trabajo del encargo: 24-09-2026; preguntas escritas y contestadas el 29-09-2026 (fecha del
sistema), **sólo con el texto del tema**. Teoría (T) y aplicación práctica (P). Veredicto: entera / a
medias / no.

1. (T, diseño) Se puede duplicar el tamaño de una imagen sin ninguna pérdida de calidad: a) siempre,
   con un buen remuestreo; b) sólo si es vectorial; c) sólo si se guarda en TIFF; d) nunca.
   → **b**. §1 «Las familias de programa» (con el matiz de lo vectorial dentro del mapa de bits).
   **Entera.**

2. (T, diseño) ¿Qué formato de imagen NO admite el modelo CMYK? a) PSD; b) JPG; c) TIFF; d) PNG.
   → **d**. §2 «El programa de imagen fija», tabla «¿Admite CMYK?». **Entera.**

3. (P, vectorial) Dos formas solapadas dan un resultado en el que todo se conserva salvo la zona común,
   que queda hueca. La operación de buscatrazos es: a) unir; b) restar; c) intersecar; d) excluir.
   → **d**. §2 «El programa vectorial», tabla y regla «Cómo se decide mirando». **Entera.**

4. (T, composición) El parámetro de la máscara que permite animar el desenfoque de sus bordes es: a)
   la expansión; b) la opacidad; c) el calado; d) el trazado. → **c** (la expansión mueve el borde, no
   lo difumina). §3 «La máscara y sus parámetros». **Entera.**

5. (P, composición) Se añade una luz a una composición y ninguna capa cambia. Lo más probable es que:
   a) la luz esté en una capa inferior; b) las capas no tengan activada la tercera dimensión; c) falte
   precomponer; d) el calado sea cero. → **b**. §3 «La línea de tiempo y el orden de las capas».
   **Entera.**

6. (T, composición) Según las reglas del manual de DaVinci Resolve sobre el premultiplicado, la
   corrección de color debe hacerse: a) sobre la imagen premultiplicada; b) sólo sobre imágenes no
   premultiplicadas; c) después de premultiplicar dos veces; d) en el nodo *Merge*. → **b**. §3 «El
   alfa dentro del compositor» y §«Aplicación práctica» (cabecera, paso 2). **Entera.**

7. (P, edición/entrega) Una cortinilla animada que va encima de la imagen se entrega en un solo
   fichero de vídeo de la familia ProRes. ¿Cuál vale? a) ProRes 422 HQ; b) ProRes 422; c) ProRes
   4444; d) cualquiera, el alfa va aparte. → **c** (4444 y 4444 XQ, únicos ProRes con alfa). §4 «Qué
   fichero se entrega». **Entera.**

8. (T, plantillas) En DaVinci Resolve, los generadores de texto de la página de edición son en
   realidad: a) *presets* de *render* en .xml; b) composiciones de Fusion convertidas en macros; c)
   ficheros .mogrt; d) escenas de Viz Artist. → **b** (cap. 56, p. 1226). §5 «Hacer la plantilla
   propia en un compositor». **Entera.**

9. (T, plantillas) Sobre la exportación de un gráfico como plantilla de *motion graphics* desde
   Premiere, es cierto que: a) sirve para cualquier .mogrt, venga de donde venga; b) no está
   disponible para .mogrt creados originalmente en After Effects; c) admite varios gráficos
   seleccionados a la vez; d) sólo exporta a Adobe Stock. → **b** (y no con dos o más gráficos
   seleccionados). §5 «Plantillas de rótulo en el programa de edición». **Entera.**

10. (T, automatización) El protocolo MOS: a) es una norma de la SMPTE; b) comunica el sistema de
    redacción con servidores de vídeo, audio, imágenes fijas y generadores de caracteres, y no es norma
    oficial de ningún organismo; c) sólo transporta vídeo; d) sustituye a la escaleta. → **b**; y su
    versión 4.0 (7-VI-2019) va sobre *Secure Web Sockets*. §6 «La escaleta manda». **Entera.**

11. (T, automatización) En Fusion, los *scripts* se escriben en: a) sólo JavaScript; b) Lua y, en
    algunos contextos, Python 2 y 3 (FusionScript); c) TypeScript; d) sólo con *blueprints*. → **b**.
    §6 «Los *scripts*». **Entera.**

12. (P, automatización) Para la noche electoral, ¿qué NO debe faltar en una plantilla alimentada por
    datos? a) un camino para teclear el dato a mano si la fuente cae; b) un *preset* H.264; c) la
    precomposición de todas las capas; d) una licencia de Studio. → **a** (y prueba de límites: nombre
    más largo, cero, empate). §6 «Los datos rellenan la plantilla» y «Aplicación práctica». **Entera.**

13. (T, automatización en directo) En Unreal Engine, el grafismo de Motion Design se controla desde
    fuera combinando: a) MOS y FTP; b) la API del Rundown Server y la Remote Control API, expuestas por
    WebSocket; c) *blueprints* y Python; d) una carpeta vigilada. → **b**. §5 y §6 «La emisión
    automatizada del grafismo». **Entera.**

14. (T, automatización en diseño) En Photoshop, para generar automáticamente muchas versiones de un
    gráfico sustituyendo textos e imágenes desde un fichero de datos se usan: a) los canales alfa; b)
    las variables y los conjuntos de datos; c) el calco de imagen; d) el buscatrazos. → **b**. El tema
    sólo nombra «variables y conjuntos de datos de Photoshop» en «Lo que este tema no da» como
    documentación no leída; no dice qué hacen. Se acierta por descarte. **A medias.**

15. (P, plantillas en After Effects) Para que el montador pueda cambiar en Premiere el texto de un
    rótulo diseñado en After Effects, en After Effects hay que: a) recopilar archivos; b) añadir las
    propiedades que se quieren abrir al panel de gráficos esenciales (*Essential Graphics*) y exportar
    la plantilla .mogrt; c) precomponer y renderizar en TGA; d) guardar un *preset* en .xml. → **b**.
    El tema dice que el .mogrt se diseña en After Effects y se usa en Premiere, pero declara que cómo se
    exponen los controles «no se ha podido leer». **No.**

Resultado: 13 enteras, 1 a medias (14), 1 no (15). Las dos caen en el mismo hueco, ya declarado: la
creación de plantillas y la automatización en los programas de Adobe (After Effects, Photoshop).
