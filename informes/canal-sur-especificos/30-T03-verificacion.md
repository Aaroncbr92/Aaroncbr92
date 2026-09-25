# Puesto 30 · Tema 3 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/03-sistemas-de-edicion-no-lineal.md`.
Tema técnico sin norma jurídica: lentes `refutar_prosa.py` (0 hallazgos) e `indice.py` (8.478 palabras,
43 epígrafes). Sin `negritas.py`/`refutar_exactitud.py`/`refutar_modo.py` (no cita normas).

## Fuentes releídas y fecha (todas el 25-09-2026, copia local)

| Fuente | Qué se releyó |
|---|---|
| Avid, *Media Composer User's Guide* R8.0, 1999 (txt; número de página en línea propia, al principio de cada página) | pp. 72, 231-235, 285-287, 321, 333-337, 462, 470-471, 716-717 |
| Avid, *What's New v2022.10* (PDF, página a página con PyMuPDF) | pp. 4-5, 9-10, 13-17 |
| Avid, *What's New v2023.3* (PDF) | p. 3 |
| Avid, *DNxHD Technology*, 2012 (txt) | variantes, tabla comparativa, «Offline to Online HD», «Avid DNxHD mixed in the timeline» |
| Blackmagic, *Resolve 21 Reference Manual*, extractos con `[[pN]]` | intro (21, 23), projects (76, 78), mediapool (375), proxy (201-222), conform (476, 479, 492, 495), timelines (860), render (4185-4196), imf (4219), export (4241) |
| Adobe, ayuda de Premiere (Wayback, `wb-*.txt`) | seq, organizing (Add and delete bins), ingest-proxy, relinkauto, expopt, ame; fechas de actualización |

## Método

- Las 108 negritas buscadas por script (normalizando espacios y comillas) en todas las fuentes, con la
  página de cada una. 105 casan; las 3 restantes (Media Pool con «[…]», caché con «[…]», «processor-
  intensive» partido por guion de fin de línea) se comprobaron a mano: literales.
- Páginas: todas cuadran con el marcador de página, salvo lo anotado abajo.
- Cada paráfrasis en redonda con fuente releída en su página.
- «Copiado de RTVE sin cambios» (4 pasajes de `realizacion/20` y `edicion-montaje/07`): sólo cotejo
  literal por script, quitando negritas. Los cuatro son literales (tablas y frases). No se re-verificaron.
  «Copiado del común»: ninguno.
- Adaptado de RTVE (§ 1 «La edición lineal utiliza…», «En Avid, el proyecto guarda decisiones…»; § 3
  definición de *bin*; § 5 entrada): son oficio y no contradicen las fuentes; sin cambios.

## Hallazgos y correcciones

1. **Error 9 · cita mal aplicada.** § 2: «Avid lo decía ya de su códec DNxHD, "They can handle…"». En
   el libro blanco el sujeto de «They» es **«Avid editing systems»**, no el códec. Reescrito: lo dice de
   sus sistemas de montaje, en el documento del códec; la cita empieza ahora por esa frase. Trazabilidad
   ajustada.
2. **Error 6 · salvedad omitida.** Resolve, cadencia (p. 375): «al importar el primer clip el programa
   ofrece adaptar el proyecto». La fuente dice «If a dialog appears…», sin hablar de primer clip.
   Corregido: «al importar puede aparecer un aviso…».
3. **Error 9.** § 2, un proyecto por programa: la guía de Avid lo da como ejemplo («consider creating
   one new project for each show, episode, spot, or scene», p. 72) y el tema no daba página. Añadido
   «como ejemplo» y p. 72 (también en Trazabilidad).
4. **Error 8 · página.** § 4: lo del material anidado «muchas capas por debajo» está en p. 471, no 470.
   Añadido «(p. 471)»; Trazabilidad «470-471».
5. **Error 9.** § 3, *Select Unreferenced Clips*: la fuente habla de clips a los que no remiten «clips or
   sequences» de los *bins* abiertos, no sólo secuencias. Corregido.
6. **Error 9.** § 5, DNxHD 220: «la misma calidad para fuentes de 8 bits» → la fuente dice «highest
   quality image when using 8-bit color sources» y mismos flujos por cadencia que la 220x. Corregido.
7. **Error 9.** § 6, Premiere: los *proxies* externos «se asocian a mano»; la fuente sólo dice «attach».
   Quitado «a mano».
8. **Error 3 · recuento.** § 6: «Dos salvedades de la misma página»; la página da cuatro funciones no
   admitidas con *proxies*. Reescrito: «Entre las funciones… están estas dos».
9. **Error 8 · página / error 6.** § 6, audio de 48,048 kHz: está en *What's New v2022.10* p. 4 (sección
   NEXIS | EDGE), no en pp. 9-10, y la fuente lo pone como ejemplo («such as audio produced through a
   pull down process»). Añadido «como el que resulta de» y «(p. 4)»; Trazabilidad «pp. 4 y 9-10».
10. **Error 3 · recuento.** § 7: «El manual de Resolve da dos consejos» (p. 479); da tres (el tercero,
    aislar formatos no admitidos). Reescrito: «hay dos que tocan al montador».
11. **Error 6.** § 7, *Decompose*: «Sin colas, el sistema avisa…»; la fuente avisa al retocar o poner
    efectos sin colas (p. 235). Corregido.
12. **Error 9.** § 7, Avid: «conservar la resolución de captura original» → la fuente dice «original
    capture settings» y manda usar *Batch Digitize* (p. 337). Corregido.
13. **Dato que faltaba y hueco mal declarado.** Premiere, reenlace: el redactor dio por no confirmado
    el menú manual, pero la misma página «Relink media in Premiere» (act. 15-04-2026) dice **«If both
    passes fail, Premiere opens the Link Media dialog box for manual relinking»**, describe las dos
    pasadas (carpeta del proyecto y subcarpetas; después la carpeta superior) y pone los renombrados
    entre los casos que exigen reenlace manual. Añadido con cita; quitada la línea de «Lo que no da».
14. **Error 5 · siglas.** PAM (en «Lo que no da») y JPEG2K (en cita de Resolve) sin presentar. Añadidas
    a las siglas.
15. Trazabilidad: Resolve «pp. 13, 21, 23» → «pp. 21 y 23» (la p. 13 no sostiene nada); *What's New*
    «17» → «16-17» (*Choose For Me* empieza en p. 16, «New users…»). Ficha: 8.400 → 8.500 palabras.

Comprobado sin hallazgo: fechas de las seis páginas de Adobe; preajustes de cámara de Premiere; *bins*
de Premiere; exportación directa / Media Encoder; páginas de exportar EDL, XML de FCP y OMF en la ayuda;
DNxHD 8/10 bits, VC-3, 220x (220/175 Mb/s), 145 (120 Mb/s a 25p), 100 (1.920→1.440, 1.280→960),
HDCAM 1.440 y DVCPRO HD 1.280 muestras, DNxHD 36 y sus cadencias; *proxies*, medios optimizados, caché y
*Timeline Proxy Mode* de Resolve (incluida la exclusión de la gestión de medios y del archivo, p. 204);
*Deliver* (cola, preajustes, *Single/Individual clips*, TC clonado, p. 4241, IMF sólo en Studio);
*Relink* de Avid 2022.10/2023.3 (rojo, *Locate Media*, fichero o carpeta); plantillas de secuencia;
*Redigitize* y duplicado de secuencia (p. 233); *Load Media Database* (pp. 333-334); exportación y
plantillas (pp. 716-717).

## Observación sin cambio

- «Dos avisos de la misma página de entrega» (§ 8) mezcla p. 220 (capítulo de *proxies*) y p. 4219: se
  refiere a la página *Deliver* del programa, no del manual; es defendible.

## Ficheros tocados
Sólo el tema 3 y este informe.
