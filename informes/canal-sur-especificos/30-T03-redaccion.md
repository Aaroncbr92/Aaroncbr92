# Puesto 30 · Tema 3 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/03-sistemas-de-edicion-no-lineal.md`.
Material: `30-investigacion-A-tecnica.md` (§ Tema 3); RTVE `edicion-montaje/07` y `realizacion/20`
(`informes/canal-sur-reuso/realizacion.tsv`: 70 %, «actualizar: no»). Fuentes de fabricante leídas en
local: `fuentes/fabricantes/` (Avid 1999, What's New 2022.10 y 2023.3, DNxHD 2012) y
`fuentes/canal-sur/montador/` (extractos de Resolve 21 y copias de la ayuda de Premiere).

## Avance
- Portada, siglas, enunciado, preguntas, índice: guardado.
- § 1 La edición no lineal: guardado.
- § 2 Proyectos: guardado.
- § 3 Bins: guardado.
- § 4 Timeline: guardado.
- § 5 Códecs: guardado.
- § 6 Proxies: guardado.
- § 7 Conformado: guardado.
- § 8 Exportación: guardado.
- Aplicación práctica, Lo que no da, Trazabilidad: guardado.

Extensión final: ~8.400 palabras (la portada lo dice).

## Fuentes leídas y fecha (todas el 25-09-2026, en copia local)
- Avid, *Media Composer User's Guide* R8.0, 1999 (`fuentes/fabricantes/Avid_Media-Composer-User-Guide-R8-1999.txt`).
- Avid, *What's New v2022.10* y *v2023.3* (`fuentes/fabricantes/WhatsNew_MediaComposer_*.txt`).
- Avid, *DNxHD Technology*, 2012 (`fuentes/fabricantes/Avid_DNxHD_white-paper-2012.txt`).
- Blackmagic, *DaVinci Resolve 21 Reference Manual*, extractos con marca de página
  (`fuentes/canal-sur/montador/resolve21-extractos/`: intro, projects, mediapool, timelines, proxy,
  conform, render, export, imf).
- Adobe, ayuda de Premiere vía Wayback (`fuentes/canal-sur/montador/web/wb-*.txt`).
- Todas las citas en negrita del tema se contrastaron por script contra esos textos: 0 no encontradas.

## Novedades frente a la investigación
- Proxies de Avid: la investigación los daba por no confirmados; están en *What's New v2022.10*,
  pp. 9-10 (Media Composer | Enterprise). Añadidos.
- Página del manual de Resolve: la definición de *Proxy Media* está en p. 213 (no 202); medios
  optimizados, pp. 202-204; comparación proxies/optimizados/caché, p. 222; *Timeline Proxy Mode*, p. 201.
- Añadido de Resolve: cadencia no modificable tras importar (p. 375); *Project Manager* (p. 76);
  reenlace desde el *Media Pool* (p. 495); conformado por bobina y TC (p. 492); caché Smart/User (p. 209);
  exportar líneas de tiempo con clips individuales (p. 4241); cola de *render* y preajustes (pp. 4185-4186).
- Menú de reenlace manual de Premiere («Link Media»): no confirmado, no se cita (va a «Lo que no da»).
- Errata de Adobe «32 Hz or 48 Hz»: no se cita.

## Copiado del común
Ninguno. El tema remite al 15 (organización de *bins*, vistas, *Attic*, AAF/OMF) y a los 2, 4, 7, 8,
12 y 13 del puesto, sin copiar su texto.

## Copiado de RTVE sin cambios
Pasajes técnicos copiados palabra por palabra (sólo se ha quitado la negrita, porque en este proyecto
la negrita marca literal de fuente) de temas RTVE con «actualizar: no». No citan normas; son oficio.
1. § 1 «Lineal y no lineal»: la tabla de cinco filas (de `realizacion/20`, § 4) y las frases «La
   palabra "lineal" no se refiere a la duración ni al relato: se refiere al acceso. Una cinta se
   recorre en línea; un disco, no.»
2. § 4 «El render»: la frase «Hacer render es el cálculo que el sistema de edición no lineal tiene que
   hacer en los efectos para hacerlos visibles y utilizables.» y el párrafo «Por qué hace falta. […]
   Eso es renderizar.» (de `realizacion/20`, § 5).
3. § 5 «Formato de codificación, códec y contenedor»: la tabla de tres filas y las frases «Un formato
   contenedor es un estándar para la distribución o el almacenamiento de un determinado contenido
   multimedia.», «Un formato de codificación es el estándar desarrollado que indica las reglas y
   operaciones matemáticas que realiza un algoritmo de compresión.» y «el estándar dice qué hay que
   hacer, el códec lo hace y el contenedor lo guarda.» (de `realizacion/20`, § 6).
4. § 6 «Offline y online»: la tabla de dos filas y el párrafo «Por qué existió la separación: […] el
   montaje se hace en una sala y el acabado en otra.» (de `edicion-montaje/07`, § 2).

Adaptado de RTVE (sí se verifica): § 1, «La edición lineal utiliza cintas físicas…» (quitada la
referencia a la pregunta) y «En Avid, el proyecto guarda decisiones…» (de `07`, § 1); § 3, «El *bin* es
la carpeta donde viven los clips y las secuencias» (de la tabla de `07`, § 1); § 5, frase de entrada.

Descartado de RTVE por propio de RTVE o sin fuente: las trece preguntas de Avid de `07` (atajos,
colores de barra de posición, (G), *Active Palette*, modos de *keyframe*, *Dupe Detection*, *Dynamic
Relink*: sólo con plantilla, sin documentación del fabricante); de `20`, montajes, teoría, formatos
del examen, gráficos, animación, etalonaje, LUT, transcripción y entidades de gestión (otros temas o
fuera del enunciado).

## Ficheros tocados
Sólo el tema 3 y este informe.

## Preguntas tipo test de comprobación (10), contestadas sólo con el tema

1. (Proyectos) En DaVinci Resolve, una vez importados clips al *Media Pool*, la cadencia del proyecto:
   a) se cambia en cualquier momento desde el *Project Manager*; b) ya no se puede cambiar ✔; c) sólo
   se cambia en la página *Deliver*; d) se adapta sola a cada *timeline*. — § 2. Entera.
2. (Timeline) En Premiere, la base de tiempo de una secuencia: a) se puede cambiar en sus ajustes
   cuando se quiera; b) queda bloqueada al crear la secuencia ✔; c) la fija el primer clip exportado;
   d) no existe en Premiere. — § 4 (y la salida: secuencia nueva). Entera.
3. (Bins) En Resolve, todo lo que se importa a un proyecto va por defecto al *bin*: a) *Media*;
   b) *Master* ✔; c) *Source*; d) *Smart Bin*. — § 3. Entera.
4. (Timeline, práctica) En Media Composer, con *Clip Color > Offline*, los clips sin material se ven:
   a) verdes; b) azules; c) morados; d) rojos ✔. — § 4 (morado es Resolve con *proxies*). Entera.
5. (Códecs) Un formato contenedor es: a) la implementación de un algoritmo en un programa; b) el
   estándar que fija las operaciones de compresión; c) un estándar para la distribución o el
   almacenamiento de un contenido multimedia ✔; d) una estructura de GOP. — § 5. Entera.
6. (Códecs / proxies) Avid DNxHD 36 está pensado para: a) masterizado 4:4:4; b) montaje *offline* de
   fuentes HD progresivas ✔; c) entrega a plataformas; d) archivo en LTO. — § 5 y § 6 (y VC-3). Entera.
7. (Proxies, práctica) Se ha montado en Resolve con *proxies*; al exportar en *Deliver* sin tocar
   nada: a) sale con los *proxies*; b) sale con el material original ✔; c) da error; d) sale con los
   medios optimizados. — § 6 («Use proxy media» lo cambia). Entera.
8. (Conformado) Para reenlazar, Media Composer compara: a) tamaño y fecha del fichero; b) nombre de
   cinta de origen, código de tiempo y canales capturados ✔; c) resolución de captura y de audio;
   d) el contenido de la imagen. — § 7 (y que ignora c). Entera.
9. (Conformado, práctica) La función *Decompose* de Avid: a) borra el material no usado; b) crea
   *master clips* nuevos y más cortos con sólo lo usado en la secuencia, con colas para retoques y
   transiciones ✔; c) divide la secuencia en bloques; d) separa audio y vídeo. — § 7. Entera.
10. (Exportación) En la página *Deliver* de Resolve, al calcular en modo *Individual clips*: a) sale un
    único MXF; b) cada clip sale en su fichero con el código de tiempo copiado del original, para
    reconformar en otro programa ✔; c) los clips pierden el código de tiempo; d) sólo se exporta la
    EDL. — § 8 (y exportación directa frente a Media Encoder en Premiere). Entera.

Resultado: 10 de 10 enteras; no hizo falta ampliar.
