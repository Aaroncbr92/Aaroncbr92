# Realizador/a (puesto 33) · Tema 9 · Fase 2, redacción

Fecha de trabajo: 24-09-2026. Tema: `temas/canal-sur-especificos/33-realizador-a/09-mezclador-recursos-realizacion.md`
(12.492 palabras según `indice.py`, 61 epígrafes; índice generado con `indice.py`). `refutar_prosa.py`:
1 hallazgo, DVE «sin presentar» porque su primera aparición es el título, que reproduce el enunciado;
las siglas se presentan en el párrafo de entrada. Tema técnico: no se pasan las lentes de norma, salvo
`negritas.py` contra el manual ATEM, el RD 1680/2011 y el Libro de Estilo (ligaduras normalizadas):
105 negritas, 9 no halladas; 8 son las copiadas del común (Adobe, Resolve, Mateu, sin volcado local) y 1
es la de 3.16.1 del LE, cortada por el salto de página 57-58 (comprobada a mano; cita corregida a
«pp. 57-58»).

Material: `33-investigacion-B-control-directo.md` (9.1 a 9.4), los dos temas de RTVE de
`realizacion.tsv` (fila 33/9, 85 %, actualizar «no») y los temas cerrados 30-01 y 30-07. Releídos en
`fuentes/` el 24-09-2026 todos los pasajes que el tema cita fuera de lo copiado: manual ATEM
(`fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt`: transiciones, disolvencias, fundidos,
cortinillas, transiciones animadas, FTB, composición de imágenes, luminancia, lineal, crominancia y
crominancia avanzada, rebase, geométrica, DVE, SuperSource, visualización simultánea, ajustes de
fuentes, macros, reproductores), RD 1680/2011 (`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`:
0905 RA 1 f, RA 5 y c/e, RA 6 b/d/e y contenidos; 0910 RA 4 b/g) y Libro de Estilo (3.6.1, 3.10, 3.16
a 3.16.2, 6.5.1, 6.5.2, 8.6.1, 9.9.2), con páginas tomadas de los marcadores del volcado.

## Decisiones

- Reparto con el tema 4 (organización del control): panel, salidas, auxiliares, sincronizadores,
  GPI, piloto, titulador y quién opera cada equipo quedan allí; el tema 4 remite al 9 las
  transiciones, llaves, croma, DVE, memorias, usos narrativos y *black burst*/*tri-level*, y todo eso
  está aquí.
- Se quitan de RTVE todas las referencias a preguntas, cuadernillos y respuestas oficiales. Los
  razonamientos de las preguntas que enseñan algo (aditivo 7 %, llave no aditiva, alfa en
  *autoselect*, macro con pausa de 15 fr, *timeline* en marcha, eje Z, corner pinning, PinP) se
  conservan reescritos como casos.
- No se copian los nombres comerciales que RTVE sostenía sólo con la plantilla (Live Edit, CuePilot,
  Infinity Set, Mistika, Chyron, Brainstorm, Ventuz): la realización programada y el croma en directo
  frente a postproducción quedan como concepto de oficio, sin marca. Se quita también «o DME en la
  nomenclatura de Sony» del DVE (Sony no se leyó); DME y SÚPER MIX quedan en siglas y tabla como
  nomenclatura de otros fabricantes, declarada sin contrastar en «Lo que este tema no da».
- *Additive key*: RTVE lo daba como «término de las llaves de un mezclador Sony» (sin fuente); aquí se
  dice sólo que nombra un modo de combinar, no un tipo de máscara.
- Manual ATEM, composiciones del DSK: el manual dice «el módulo DSK cuenta con dos botones para
  composiciones previas». Se cita literal y se advierte que, por el nombre de sus paneles
  («Composición previa» / «Composición posterior», misma página) y por su lugar en la cadena, las del
  DSK son las posteriores. **El verificador debe mirar si la advertencia es correcta.**
- SuperSource: el manual dice «visualizar varias fuentes en un monitor»; el tema aclara, como oficio,
  que es una fuente que sale al aire y no el multipantalla (el propio manual la presenta como
  «PIP» y ocupa una entrada del mezclador).
- Criterios narrativos (lo que RTVE no tenía): RD 1680/2011 («Usos expresivos y narrativos»), las
  filas de Mateu del tema 30-01, el pasaje de Adobe/Resolve del 30-07, Libro de Estilo (6.5.1, 6.5.2,
  3.10, 9.9.2) y dos tablas de oficio declaradas (recurso y género).
- LE 8.6.1: el punto 9 es un «deberán», y así se señala.
- Extensión: 12.500 palabras; el enunciado nombra once materias y el tema 4 tiene 12.800.

## Copiado del común

Temas cerrados del puesto 30 (Operador/a Montador/a de Vídeo), extraídos por líneas con `sed` y
comprobados por script (literales al carácter):

- `30-operador-a-montador-a-de-video/07-postproduccion.md`, § 6 «Corte y transición»: los dos
  párrafos enteros («Adobe parte del corte…» y «El corte es la unión por defecto…», que ya remite al
  tema 1, cuyo número coincide en el puesto 33). En § 11, «Corte y transición».
- `30-operador-a-montador-a-de-video/01-lenguaje-y-montaje-audiovisual.md`, tabla «Con qué se hace»:
  las filas «Fundido» y «Encadenado» (Mateu Torres, 3.2, pp. 37-38), con la cabecera de la tabla. No
  se copia la fila «Corte», que remite a un ejemplo anterior de aquel tema. En § 11, «Corte y
  transición».
- Adaptado (sí se verifica): `30-07`, § 3 «Incrustar», párrafo «Tres consecuencias de oficio para el
  croma…», literal salvo la remisión «(tema 2)», que pasa a «(tema 14)». En § 4, «Lo que el croma pide
  al plató».

## Copiado de RTVE sin cambios

Palabras sin tocar; sólo se han quitado las negritas de énfasis. Comprobado por script (normalizando
negrita y saltos de línea), párrafo a párrafo y fila a fila, contra los dos ficheros.

`temas/realizacion/10-el-mezclador-de-video.md`:
- § 1: «Un mezclador de vídeo hace tres cosas…», la lista y «Todo lo demás…» (en «Qué es un mezclador
  de vídeo»).
- § 3: la frase «Cada fuente del mezclador tiene, además de su señal:» y la tabla de atributos (en § 8,
  «Las fuentes y sus atributos»).
- § 4: «Un banco M/E es un mezclador completo…», «El manual de los ATEM lo explica así…» con sus dos
  citas y «y añade para qué se inventó:»; la frase «El M/E es lo que se utiliza para aplicar
  transiciones y combinaciones complejas entre distintas fuentes de vídeo.»; «La cadena de un
  mezclador de varios bancos, de arriba abajo:» y su tabla (en § 9).
- § 7: la tabla de modos de transición entera.
- § 7: la lista NAM/FAM (los dos puntos).
- § 8: «Incrustar es superponer…», la tabla de las tres señales, «El manual de los ATEM lo dice con
  esas mismas tres piezas…» con la cita, la fórmula y «Leída despacio…».
- § 9: la tabla de tipos de llave.
- § 10: «Las dos maneras de combinar el relleno con el fondo:», la tabla y «La consecuencia práctica
  es una sola frase…».
- § 11: «Cuando la llave se fabrica…», la tabla de clip y ganancia, «El manual de los ATEM describe
  esos dos controles…» y la cita; y las dos citas del manual sobre la composición precompuesta.
- § 13: la tabla de parámetros del DVE.
- § 14: la tabla de memorias, «La diferencia entre *snapshot* y macro…», «El manual de los ATEM define
  la macro exactamente así:» y la cita.
- § 15: el epígrafe del *clip store* entero (párrafo, «Sus rasgos:» y los cuatro puntos).
- § 16: la tabla de *black burst* y *tri-level* y «El aparato que las genera…».

`temas/realizacion-tv/15-el-mezclador.md`:
- § 2: «El mecanismo: …» y la lista de tres razones del verde y el azul.

Adaptado de RTVE (sí se verifica): la frase de entrada de la fórmula («La fórmula del compuesto:»); la
de entrada de memorias («Tres maneras de guardar trabajo hecho, que se distinguen por lo que
guardan:»); la de las referencias («Las dos señales de referencia:»); la entrada del DVE (sin Sony y
con la cita ATEM); «Por qué entonces todo el mundo usa verde y azul:»; la frase «El punto donde se
recorta…» (sin la pregunta 119, con las falsas reescritas); los párrafos de la cortinilla, la
distinción NAM/FAM, *source*, *autoselect*, bancos divididos, premultiplicación, *self key*, *show key*,
*coring*, Ultimatte, *corner pinning*, eje Z, PinP, gafa, croma en directo y decorado virtual,
*timeline* en marcha y realización programada, y la macro con pausa de 15 fr: todos con frases de RTVE
reescritas sin las preguntas.

## Fuentes y fechas de lectura

| Fuente | Leída |
|---|---|
| Manual ATEM de Blackmagic Design, edición de diciembre de 2024 (volcado local) | Descargado el 03-09-2026 (según RTVE); releído el 24-09-2026 |
| RD 1680/2011, texto del diario oficial (volcado local); vigencia según la investigación B (RD 500/2024) | 24-09-2026 |
| Libro de Estilo de Canal Sur TV y Canal 2 Andalucía (2004), volcado local | 24-09-2026 |
| Mateu Torres (2024); Adobe «Transitions overview»; Resolve 21 cap. 55 | No releídos: copiados del común |

## Lo que no se pudo confirmar

- Equipamiento de los controles de Canal Sur, sistema de grafismo y manual de identidad gráfica: sin
  documento publicado (lo mismo que la investigación, 9.4 y 12.5).
- Nomenclatura Sony (DME, SÚPER MIX) y de otros fabricantes: sin documentación leída.

Ficheros tocados: el tema y este informe. Fragmentos de trabajo en el scratchpad.

## Preguntas de control (10)

Tipo test, repartidas por las rúbricas del enunciado; contestadas sólo con el tema.

1. (Transiciones) En una mezcla aditiva total (FAM), ¿qué se ve en el punto medio de la transición?
   a) En cada punto, la más brillante de las dos imágenes. b) Las luminancias se suman y las dos
   fuentes están al 100 %. c) Un color intermedio preseleccionado. d) Las dos imágenes atenuadas por
   igual. — b) · Entera: § 1, «NAM y FAM».
2. (Efectos) En una composición geométrica (llave de figura), ¿de dónde sale el canal alfa? a) Del
   titulador. b) Del brillo del relleno. c) Lo genera el mezclador. d) De un color del fondo. — c) ·
   Entera: § 2, cita ATEM.
3. (Incrustaciones) Con una llave de luminancia aditiva, el relleno de un gráfico trae el negro al
   7 % y no se toca nada. ¿Qué ocurre? a) Nada. b) El fondo se levanta y se baja al meter y sacar la
   llave. c) El rótulo sale oscurecido. d) La llave se invierte. — b) · Entera: § 3, «Aditivo frente a
   lineal».
4. (Chroma) Un *chroma key* puede hacerse con: a) Sólo verde. b) Sólo azul. c) Sólo verde o azul.
   d) Cualquier color. — d) · Entera: § 4, «Cualquier color sirve».
5. (Chroma, práctica) En el croma avanzado del manual ATEM, ¿qué control elimina el contorno verde que
   la luz rebotada del fondo deja en el pelo del presentador? a) Matiz. b) Rebase. c) Límite Y.
   d) Generador de color. — b) · Entera: § 4, tabla de controles y definición de rebase.
6. (DVE) Para ampliar una imagen conservando sus proporciones en un DVE con perspectiva: a) Cambiar el
   aspecto. b) Rotar en X e Y. c) Trasladar en el eje Z. d) Recortar. — c) · Entera: § 5.
7. (Multipantalla) En el multipantalla de un ATEM, un borde rojo alrededor de una ventana indica que
   la fuente: a) Está en previo. b) Está al aire. c) No está sincronizada. d) Tiene la llave activada.
   — b) · Entera: § 6, cita ATEM.
8. (Macros) La secuencia «*snapshot* de programa, pausa de 15 fr, transición MIX, llave 1 a apagado»
   es: a) Un *snapshot*. b) Un *timeline*. c) Una macro. d) Una memoria de llave. Y, según el manual
   ATEM, las macros se almacenan: en el mezclador. — c) · Entera: § 7.
9. (Señales y keyers, práctica) Un rótulo lanzado en el DSK 2, ¿aparece en la salida limpia? a) Sí,
   siempre. b) No, porque la limpia se toma antes de las llaves posteriores. c) Sólo si está vinculado
   con TIE. d) Sólo si es una llave lineal. — b) · Entera: § 9, tabla USK/DSK y cadena; § 8; y la cita
   ATEM de que TIE no afecta a la limpia.
10. (Grafismo en directo y criterios de uso narrativo) Según el Libro de Estilo de Canal Sur, un
    gráfico informativo: a) No debe llevar más de cuatro o cinco elementos por pantalla, con una
    presencia mínima recomendable de ocho segundos. b) Debe durar lo que la locución, sin mínimo.
    c) No lleva audio. d) Se lanza siempre por cortinilla. — a) · Entera: § 10. Complemento de
    criterios narrativos: ante imperfecciones técnicas moderadas, la información tiene preeminencia
    sobre la técnica (6.5.1) — entera: § 11, «El criterio de la casa».

Resultado: las 10 enteras; no hizo falta ampliar el tema.
