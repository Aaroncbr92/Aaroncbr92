# Puesto 30 · Tema 3 · Refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/03-sistemas-de-edicion-no-lineal.md`.
No corrijo: sólo informo. Ficheros tocados: este informe y `30-T03-preguntas.md`.

## Alcance

- Exactitud: todo lo no listado en `30-T03-redaccion.md` como «Copiado de RTVE sin cambios» (cuatro
  pasajes: tabla lineal/no lineal, definición de *render*, tabla formato/códec/contenedor, tabla
  *offline*/*online*). «Copiado del común»: ninguno.
- Cobertura: tema entero contra el enunciado («proyectos, bins, timeline, códecs, proxies, conformado
  y exportación»): los siete puntos tienen epígrafe propio y en su orden.

## Fuentes releídas (25-09-2026, copia local)

Avid *Media Composer User's Guide* R8.0 1999 (pp. 72, 231-237, 285-287, 327-337, 462, 470-471);
*What's New v2022.10* (proxies, *Relink*, plantillas, *Choose For Me*); *Avid DNxHD Technology* 2012
(variantes, tabla de submuestreo, «Offline to Online HD», «mixed in the timeline»); *Resolve 21
Reference Manual*, extractos (pp. 201-222, 375, 476-495, 860, 4185-4196, 4219, 4241); ayuda de
Premiere vía Wayback (seq, ingest-proxy, relinkauto, expopt; fechas de actualización).

## Exactitud: hallazgos

Graves: ninguno. Menores: cuatro.

1. **Error 6 · salvedad omitida.** § 7 «Reenlazar», Avid: «Pasa, según la misma guía, "after you
   consolidate or move material between systems"». La guía (p. 336) dice «**Sometimes** after you
   consolidate…». Propuesta: «A veces pasa, según la misma guía, …».
2. **Error 6 · paso opcional como recomendación.** § 7 *Decompose*: «Avid recomienda duplicar antes la
   secuencia y guardar la copia en otro *bin*». En p. 233 lo recomendado es el duplicado; moverlo a un
   *bin* nuevo va marcado «(Option)». Propuesta: «…duplicar antes la secuencia (y, si se quiere,
   pasar la copia a otro *bin*)». Además la razón de la fuente es conservar la primera versión, no
   «rompe el enlace, así que»; se puede dejar, pero conviene decir las dos cosas.
3. **Error 9 · dato sin la salvedad de la fuente.** § 5, medios optimizados: la cita de p. 202 da
   cuatro formatos contra el recorte en HDR (16-bit float, ProRes 4444, 4444 XQ y DNxHR 444); la
   p. 203 del mismo manual da sólo tres («any of these three codecs», sin DNxHR 444). El tema cita la
   primera sin avisar. Propuesta: añadir que en p. 203 el manual nombra sólo los tres primeros como
   apropiados para HDR.
4. **Error 9 · dato de más en el supuesto.** «Aplicación práctica», paso 6: «se reenlaza por nombre
   de fichero, bobina y código de tiempo»; los datos que da el tema (§ 7) son cinta/bobina, código de
   tiempo y canales (Avid) y bobina y TC (Resolve EDL). «Nombre de fichero» no sale de los epígrafes
   citados. Propuesta: «por nombre de cinta o bobina y código de tiempo (epígrafe 7)».

Comprobado sin hallazgo: familia DNxHD (444, 220x 220/175 Mb/s, 220, 145 a 25p 120 Mb/s, 100 con
1.920→1.440 y 1.280→960, 36 y sus cuatro cadencias), HDCAM/DVCPRO HD 1.440/1.280, VC-3; *Choose For
Me*, *bins* verde y azul, plantillas y TC inicial; *proxies* de Media Composer (Enterprise, icono y
botón naranjas, tres modos, 48,048 kHz); *Relink* 1999 y 2022.10/2023.3; *Select …* del *bin*;
Resolve: cadencia (p. 375), *Master bin*, *timelines* (p. 860), caché Smart/User, *Proxy Media*
(resolución, códecs, p. 213), línea morada y «Use proxy media» (p. 220), *Timeline Proxy Mode*,
conformado (pp. 476, 479, 492, 495), *Deliver* (pp. 4185-4186, 4196), IMF (p. 4219), p. 4241;
Premiere: base de tiempo bloqueada y secuencia nueva, preajustes, *proxies* (*attach*, After
Effects, Audition), rutas históricas y dos pasadas, *Link Media*, exportación directa / Media
Encoder, AAF; fechas de las páginas de Adobe.

## Cobertura: 15 preguntas (`30-T03-preguntas.md`)

12 enteras, 1 a medias, 2 no. Lagunas para el remate (ampliar, con fuente ya en local):

1. **Consolidate de Avid** (guía 1999, pp. 327-331): el tema usa «consolidar» tres veces y no dice
   qué es. Basta un párrafo en § 7 junto a *Decompose*: copia los ficheros o la parte usada a otro
   disco; *master clip* = copia exacta (.old/.new, no ahorra espacio); *subclip* = sólo la parte usada,
   *master clip* nuevo; diferencia con *Decompose* (no recaptura).
2. **Resolve, alternar medios optimizados** (p. 202): «Playback > Use Optimized Media if Available».
   Una línea en § 6, tabla de las tres ayudas.
3. **Premiere, incompatibilidades de *proxies***: la página da tres, el tema dos; añadir **«Dynamic
   Link is not supported for After Effects compositions or projects.»** (misma página, act.
   07-01-2026).

Fuera de lagunas: cómo alternar *proxy*/original en Premiere desde el monitor no está en las fuentes
locales; si se quiere, a «Lo que no da».

## Veredicto

Tema exacto en lo esencial y con cobertura completa del enunciado. 0 graves, 4 menores, 3 lagunas
(ampliación breve, Opus en el remate).

---

# Segunda ronda (fase 4 repetida sobre el tema rematado y revisado en 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema en su estado actual (remate y 5 bis aplicados;
8.913 palabras de cuerpo, 44 epígrafes). No corrijo. Ficheros tocados: este informe y
`30-T03-preguntas.md` (sección «Segunda ronda»); los dos se amplían, no se sobrescribe la primera ronda.

## Alcance

- Exactitud: todo menos los cuatro pasajes «Copiado de RTVE sin cambios» de `30-T03-redaccion.md`
  (tabla lineal/no lineal y su frase, definición de *render* y su párrafo, tabla formato/códec/
  contenedor y sus frases, tabla *offline*/*online* y su párrafo). «Copiado del común»: ninguno.
- Cobertura: tema entero contra el enunciado («proyectos, bins, timeline, códecs, proxies, conformado
  y exportación»): siete epígrafes propios y en su orden, más supuesto práctico.

## Fuentes releídas (25-09-2026, copia local)

- Avid, *Media Composer User's Guide* R8.0 (1999): pp. 72, 231-235, 285-288, 321, 327-340, 462,
  469-471, 715-717.
- Avid, *What's New v2022.10* (pp. 4-7, 9-10, 13-17) y *v2023.3* (p. 3); *Avid DNxHD Technology*
  (2012): variantes, tabla de formatos, submuestreo HDCAM/DVCPRO HD, VC-3, DNxHD 36, «mixed in the
  timeline».
- Blackmagic, *DaVinci Resolve 21 Reference Manual*, extractos: pp. 21, 23, 76-78, 201-204, 209,
  213, 219-222, 375, 476, 479, 492, 495, 860, 4185-4187, 4196, 4219, 4241.
- Adobe, ayuda de Premiere (Wayback): «Sequence presets and settings» y «Add and delete bins»
  (22-08-2025), «Ingest and Proxy workflow» (07-01-2026), «Relink media in Premiere» (15-04-2026),
  «Export directly to Adobe Media Encoder» (01-04-2026), «Export options in Premiere» (18-08-2026).

## Método

- Las 127 citas en negrita, cotejadas por script contra las fuentes locales (normalizando comillas y
  saltos de línea; los tramos con «[…]» por partes): **0 no encontradas**. Cada una, localizada en su
  página por las marcas del texto: todas cuadran con la página que da el tema.
- Paráfrasis y datos en redonda, releídos a mano en la página citada (familia DNxHD, *Consolidate*,
  *Decompose*, *Relink*, *Load Media Database*, modos de *proxy* de Avid, 48,048 kHz, medios
  optimizados y alfa, caché, línea morada, «Use proxy media», *Deliver*, IMF, p. 4241, reenlace de
  Premiere, preajustes de secuencia, borrado de *bins*).
- Lentes: `refutar_prosa.py`, 0 hallazgos (siglas, relleno, repetidas, negritas rotas);
  `indice.py` sobre una copia, índice idéntico al del tema (44 epígrafes) y sin rutas del proyecto
  en el cuerpo. Tema técnico sin norma: no tocan las demás lentes.

## Exactitud: hallazgos

Graves: ninguno. Menores: dos.

1. **Error 9 · afirmación sin fuente.** «Lo que este tema no da», segundo punto: «*Dynamic Relink*
   (el ajuste de Avid para cambiar de resolución de material en almacenamiento compartido)». Ninguna
   fuente local habla de *Dynamic Relink* (sólo aparece en los informes de investigación, tomado del
   tema de RTVE, y la redacción lo descartó por «sin documentación del fabricante»); el propio punto
   dice que no se ha comprobado. La definición entre paréntesis es de memoria. Propuesta: quitar el
   paréntesis y dejar «… o *Dynamic Relink* no se ha comprobado en la documentación de Avid».
2. **Error 5 · sigla sin presentar.** «Lo que este tema no da», cuarto punto: «estándares de entrega
   (IMF, AS-11)». AS-11 no está entre las siglas de entrada. Propuesta: «AS-11 (familia de
   especificaciones de la AMWA para entregar a una cadena ficheros MXF acotados)», con la página local
   de AMWA («define constrained media file formats (based on MXF) for the delivery of finished media
   assets to a broadcaster or publisher»), o simplemente «y los demás estándares de entrega, tema 4».

Comprobado sin hallazgo (además de lo que ya dio por bueno la primera ronda): pasajes del remate y
del 5 bis (*Consolidate* con .old/.new y los tres fines, *Subclips* y secuencias desde el *bin*,
«A veces pasa…», *Decompose* con el paso «(Option)», tres códecs para HDR en p. 203, «Playback > Use
Optimized Media if Available», cuatro funciones no admitidas en *proxies* de Premiere, paso 6 del
supuesto); submuestreo HDCAM 1.440 y DVCPRO HD 1.280; «six user-selectable bit rates» = seis
variantes; *Select Unreferenced Clips* «effectively the reverse of the Select Media Relatives»;
Premiere, «A single project can contain multiple sequences…» (la misma página añade que algunos
ajustes sí se cambian después: coherente con § 4, «algunos ya no se tocan»); p. 204, medios
optimizados fuera de *Media Management* y del archivo; fechas de las cinco páginas de Adobe.

## Cobertura: 15 preguntas nuevas (`30-T03-preguntas.md`, «Segunda ronda»)

11 enteras, 0 a medias, 4 no. Lagunas para el remate (ampliación breve, fuente ya en local):

1. **Resolve, *Playback > Proxy Handling*** (p. 219): *Disable All Proxies* (sólo original; si falta,
   «Media Offline»), *Prefer Proxies* (si no hay *proxy*, el original; si falta el original, el
   *proxy* con línea morada) y *Prefer Camera Originals* (a la inversa). En § 6, «En cada programa»,
   Resolve, en lugar de «se prefiere el *proxy* o el original»; queda paralelo a los tres modos de
   Avid. Añadir también la frase de p. 220 sobre «Use proxy media» cuando no hay acceso al original.
2. **Colas por defecto al consolidar en Avid** (p. 332): al consolidar *subclips* o secuencias se
   da una longitud de colas o se aceptan **60 cuadros (NTSC) o 50 (PAL)**. Una línea en § 7,
   «Consolidar en Avid»; conecta con las colas de *Decompose*.
3. **Premiere, otros casos de reenlace manual** («Relink media in Premiere», «Required manual
   relinking»): además de los renombrados, cambios grandes de estructura de carpetas, cambio de
   formato de fichero (.mov a .mp4: desmarcar *File Extension* en *Match File Properties* del
   diálogo) y discos externos desmontados. Una frase en § 7, «Reenlazar», Premiere.
4. ***Single clip* e *Individual clips*: cadencia, código de tiempo y efectos** (p. 4196): en
   *Single clip*, el TC sale de «Start timeline timecode at» y las cadencias mezcladas se convierten
   a la del proyecto; en *Individual clips*, cada clip a su cadencia, efectos a elegir («Render
   Timeline Effects») y resolución de *timeline* o de origen («Render at Source Resolution»). Dos
   líneas en § 8, «Resolve: la página *Deliver*».

Fuera de lagunas (no se piden): lista de preajustes de *Deliver* (ProRes/H.264/H.265 Master, Avid
AAF, Pro Tools; p. 4185) y opción de *Decompose* «only those items for which media is currently
unavailable» (p. 234): detalle de menor rendimiento en examen.

## Veredicto

Tema exacto: 0 graves, 2 menores (ambos en «Lo que este tema no da»). Cobertura completa del
enunciado en sus siete puntos; 4 lagunas de detalle práctico, con fuente local, que piden
ampliación breve (Opus en el remate y 5 bis sobre lo ampliado). Cero hallazgos graves en dos rondas.
