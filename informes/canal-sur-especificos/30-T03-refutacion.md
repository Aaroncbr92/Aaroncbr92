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
