# Tema 3 del específico de Operador/a Montador/a de Vídeo · Sistemas de edición no lineal

**Siglas**: NLE, TC, EDL, AAF, OMF, XML, OTIO, MXF, AVI, MP4, MKV, DCP, IMF, SMPTE, MOV, DNxHD/DNxHR, ProRes, H.264, H.265/HEVC, GOP, SD/HD/UHD, DV/HDV/HDCAM, HDR, YCbCr/RGB, Mb/s, MAM/PAM, JPEG2K.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; repásalo con el tema abierto.

<!-- indice --><!-- /indice -->

## Proyectos

- Avid: proyecto fija *raster* + *edit rate*; «Choose For Me» (2022.10) los toma del 1er clip llevado a *Timeline*; crea *bin* verde (clips) y azul (secuencias).
- Resolve: proyectos = ficheros .drp, organizados en *Project Manager*; cadencia se fija al importar y ya no cambia tras el 1er clip importado.
- Premiere: se fija en la secuencia, no en el proyecto; un proyecto admite varias secuencias con distintos ajustes.
- Oficio: un proyecto por pieza/programa/episodio (Avid, guía 1999); en redacción, proyectos de vida corta por edición del informativo.
- Adobe: parámetros de secuencia deben igualar los del material (formato, *frame/pixel aspect ratio*, *frame rate*, *time base*, campos, muestreo audio, códecs).
- Avid (DNxHD 2012): sistemas Avid mezclan HD/HDV/SD/DV en la misma *timeline* en tiempo real; lo no coincidente se convierte al vuelo (coste de rendimiento).

## Bins

- Oficio/tema: *bin* = carpeta de referencias a clips y secuencias (no el material), con metadatos (nombre, TC in/out, duración, cinta/fichero, pistas, comentarios).
- Avid (guía 1999, p.232): *master clip* enlazado al fichero entero, fuente de *subclips* y secuencias; *subclip* = trozo del *master clip*.
- Avid: cambio en *master clip* alcanza a sus *subclips* y secuencias.
- Avid: *bins* en 3 vistas (*Text/Frame/Script*); *Media Tool* = ventana al material en disco, contrapartida de los *bins*.
- Resolve (p.23): *Media Pool* contiene todo lo importado; va al *bin Master* por defecto, repartible en *bins* propios; visible en páginas Edit/Fusion/Color/Fairlight; *timelines* se guardan en un *bin*.
- Premiere: *bins* en panel Proyecto; se crean con clic derecho > New Bin o Ctrl/Cmd+/.
- Avid (guía 1999, pp.285-287): órdenes de *bin*: *Select Offline Items* (sin material), *Select Media Relatives* (enlazados), *Select Sources* (fuentes de un objeto), *Select Unreferenced Clips* (sin usar).

## Timeline

- Tema: línea de tiempo = representación gráfica del montaje (pistas vídeo/audio); Avid (p.462): se actualiza mientras se trabaja.
- Se guarda en el *bin* como secuencia (Avid/Premiere) o *timeline* (Resolve).
- Premiere: ajustes se fijan al crear la secuencia; *time base* queda bloqueada; para cambiarla, nueva secuencia y pasar contenido; hay preajustes por cámara.
- Resolve (p.860): *timeline* copia por defecto los ajustes del proyecto; admite ajustes propios para varias entregas (resolución, *pixel aspect ratio*, *frame rate*) — vía de la versión vertical (tema 12).
- Media Composer (2022.10, p.15): cada secuencia nace de una plantilla (pistas, nombres, TC de arranque); TC inicial ya no está en ajustes generales.
- Avid (p.470): clips sin material se pintan en rojo, aunque estén anidados.
- Resolve (p.220): con *proxies* y falta el original, línea morada en la *timeline*.
- *Render*: cálculo de efectos (transición, rótulo, corrección, composición) que no se reproducen al vuelo.
- Resolve (p.209): caché *Smart* (calcula automático lo pesado) vs. de usuario; caché (p.222) solo sirve al proyecto que la creó, distinta de los *proxies*; el *render* es desechable (oficio).

## Códecs

- Tema: formato de codificación (estándar, ej. H.264/HEVC/AV1/MPEG-2) ≠ códec (implementación) ≠ contenedor (AVI/MOV/MP4/MXF/MKV).
- Oficio: fases: captación (formato de cámara), montaje/acabado (DNxHD/DNxHR, ProRes, sin comprimir), montaje ligero (DNxHD 36, ProRes Proxy, DNxHR LB, H.264 *proxy*), entrega (tema 4).
- Avid (DNxHD 2012): formatos de cámara no aguantan posproducción con efectos; sin comprimir da mejor imagen pero atasca por flujo/tamaño; DNxHD diseñado para montaje no lineal y multigeneración.
- Avid (DNxHD 2012): DNxHD de 8/10 bits, conserva el cuadro HD entero (a diferencia de HDCAM/DVCPRO HD, que submuestrean); codificado por SMPTE como VC-3.
- Variantes DNxHD (Avid 2012): 444 (10b 4:4:4 RGB, acabado 1080p); 220x (10b YCbCr, 220 Mb/s 1080i30/175 Mb/s prog24); 220 (máx. calidad de fuentes 8b); 145 (masterizado 8b, 120 Mb/s a 25p); 100 (submuestrea trama); 36 («*high-quality offline editing*», solo fuentes HD progresivas).
- Resolve (pp.213, 202-203): *proxies* = ProRes/DNxHR/H.264/H.265 según flujo-calidad; medios optimizados: sin comprimir 10/16b, ProRes Proxy a 4444 XQ, DNxHR LB a 444; HDR sin recortar: 16-bit float, ProRes 4444/4444 XQ (y DNxHR 444 según otra página).
- Oficio: H.264/H.265 (GOP largo) pesan al montar; Resolve (p.209) los cachea de antemano.

## Proxies

- Oficio: *offline* (montaje, material ligero) / *online* (acabado, material completo); origen histórico en disco caro/lento; hoy se mantiene por reparto sala-acabado.
- Avid (DNxHD 2012): DNxHD 36 para flujo *offline* creativo, solo 1080p/23.976-24-25-29.97, calidad suficiente para visionar sin conformar.
- Aviso: «*offline*» también = clip sin material (no confundir).
- Adobe / Blackmagic (p.213): *proxy* = copia ligera enlazada al original, se monta con ella en su lugar; enlace no se pierde (a diferencia del *offline* clásico); Resolve: fluidez al montar, vuelta al original para color/acabado/salida.
- Premiere: flujo crear-montar-volver; *proxies* externos hay que asociarlos (*attach*); 4 funciones no compatibles con *proxies*: Dynamic Link con After Effects, edición de audio en Audition, modificar canales/interpretar material.
- Resolve (p.213): al crear se elige resolución (Original/Half/Quarter/Eighth/Sixteenth/Automatically) y códec; reproducción (p.219): *Disable All Proxies*, *Prefer Proxies*, *Prefer Camera Originals*.
- Resolve: página *Deliver* vuelve siempre al original salvo marcar «Use proxy media» (obligatorio si no hay acceso al original).
- Media Composer (2022.10, pp.9-10): *Create Proxies* en edición Enterprise; icono naranja; modos *High-Resolution Only*/*Proxy Preferred*/*High-Resolution Preferred*; audio 48,048 kHz no admite *proxies*.
- Resolve (pp.201, 204, 222): distinguir *Proxy Media* (portátil, exportable) / medios optimizados (internos, no exportables) / caché de *render* (solo del proyecto); *Timeline Proxy Mode* no crea ficheros, sin relación con *Proxy Media*.
- Oficio: *proxies* sirven para material pesado, montaje remoto y empezar mientras copia el original; riesgo: exportar con *proxy* o faltar el original.

## Conformado

- Blackmagic (p.476): conformar = importar fichero de intercambio (EDL/AAF/XML) de otra aplicación y reenlazar cada clip a su material de calidad; también dentro de un programa (transcodificado → cámara original).
- Oficio: conformar = paso *offline*→*online* o entre programas; reenlazar (*relink*) = orden clip a clip.
- Avid (guía 1999, pp.336-337): reconoce material por nombre de cinta, TC y canales capturados; no por resolución de captura ni de audio.
- Resolve (p.492): EDL se conforma con clips del *Media Pool* por nombre de bobina y TC.
- Regla de oficio: no tocar nombre de cinta/bobina ni TC de origen; si se renombra a mano, ya no reenlaza.
- Resolve (p.479): bajar a V1 los clips no superpuestos antes de conformar; exportar película de referencia *offline* para comparar tras conformar.
- Avid (guía 1999, pp.231-232): *Redigitize* = recapturar con datos ya en el *bin*; exige el material original.
- Avid (pp.233-235): *Decompose* crea *master clips* nuevos y cortos solo con lo usado (ahorra disco); se fijan colas (*handles*); rompe enlaces con clips de origen — Avid recomienda duplicar la secuencia antes.
- Avid (pp.327-332): *Consolidate* copia material a otro disco sin recapturar; *master clip*: copia exacta, no ahorra espacio (.old/.new); *subclip*: copia solo su tramo, crea *master clip* nuevo; secuencia: copia solo lo montado, crea *master clips* .new, se reenlaza sola; colas por defecto 60 (NTSC)/50 (PAL) cuadros.
- Avid: para qué consolidar secuencias: copias de seguridad, quedarse solo con lo usado, reunir material disperso.
- Avid (p.336; What's New 2022.10 pp.13-14; 2023.3 p.3): *Relink* con *Managed Media* / *Linked Media* (clips sin enlace en rojo, *Locate Media*); desde 2023.3, reenlace por carpeta entera.
- Resolve (p.495): reenlaza desde *Media Pool* (Relink Media/Selected Clips/Clips in Selected Bins), actualiza todas las *timelines*; busca en subcarpetas.
- Premiere: reenlaza por *Historical path tracking* + *Automated search logic*; si fallan, abre *Link Media*; 4 casos de fallo: renombrados, carpetas reestructuradas, discos desconectados, cambio de formato (desmarcar *File Extension*).
- Oficio: tras conformar, revisar *offline* (rojo/morado), comparar con referencia *offline*, sincronía de audio, confirmar resolución completa (no *proxy*).

## Exportación

- Oficio: exportar la pieza (fichero calculado, códec+contenedor de entrega) ≠ exportar el proyecto (decisiones sin/con material: EDL/AAF/XML/OTIO/OMF).
- Avid (guía 1999, pp.716-717): exportar audio/vídeo para retocar en otras aplicaciones; ajustes se guardan como plantillas.
- Adobe: exportación directa (genera fichero desde Premiere) vs. cola de Media Encoder (permite seguir montando); Adobe recomienda la cola para exportaciones largas o varias entregas.
- Adobe: Premiere exporta a AAF (a sistemas de terceros), y tiene páginas propias para EDL, XML de FCP y OMF (Pro Tools).
- Resolve (p.4185-4186): página *Deliver*: define formato, tramo, añade a cola de *render* (*Start Render*); preajustes bloquean lo innecesario.
- Resolve (p.4196): *Single clip* (un fichero; con cadencias mezcladas, todo pasa a la del proyecto) vs. *Individual clips* (un fichero por clip; TC clonado del original, para reconformar entre Resolve y otros NLE).
- Resolve (p.4241): para pasar a otro programa: clips individuales + exportar *timeline* como EDL/AAF/XML/OTIO, así coincide bobina y TC.
- Resolve: la salida siempre parte del original aunque se haya montado con *proxies*; versión Studio exporta IMF (SMPTE ST.2067, entregas sin cinta).
- Oficio, antes de exportar: secuencia y versión correctas; sin *offline* ni efectos sin calcular; material original, no *proxy*; preajuste del destino (códec, contenedor, resolución, cadencia, audio, sonoridad); nombre según convención; revisión completa del fichero.
