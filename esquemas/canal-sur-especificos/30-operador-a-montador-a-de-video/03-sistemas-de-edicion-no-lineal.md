# Tema 3 del específico de Operador/a Montador/a de Vídeo · Sistemas de edición no lineal

**Siglas**: RTVA; CSRTV; NLE; TC; EDL; AAF; OMF; XML; OTIO; MXF; AVI; DCP; IMF; SMPTE; MOV; DNxHD/DNxHR; ProRes; H.264; H.265/HEVC; GOP; SD/HD/UHD; DV/HDV/HDCAM; HDR; YCbCr/RGB; Mb/s; MAM/PAM; JPEG2K.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema, no lo sustituye.

<!-- indice -->
<!-- /indice -->

## 1. Edición no lineal: idea y programas
- Lineal/no lineal: soporte cinta vs. archivo; la diferencia es el acceso, no la duración (§1).
- No hay generaciones al montar; sí al renderizar o exportar (§1).
- Enunciado no nombra programa ni consta cuál usa CSRTV: tema toma Avid, Resolve, Premiere (§1).
- Idea común: proyecto y material separados; clip del *bin* = referencia (Resolve p.21; Avid p.321).
- Tabla equivalencias: proyecto/*bin*/secuencia-*timeline*/*master clip*/salida, por programa (§1).

## 2. Proyectos
- Avid: fija *raster* y *edit rate*; «Choose For Me» (2022.10) los toma del primer clip; crea *bin* verde (clips) y azul (secuencias) (What's New 2022.10, pp.16-17).
- Resolve: organización en *Project Manager*; .drp; cadencia no cambia tras importar el primer clip (p.375).
- Premiere: lo que se fija es la secuencia; un proyecto puede tener varias (ayuda Adobe).
- Oficio: un proyecto por pieza/programa/episodio (Avid 1999 p.72); criterio igual en toda la sala.
- Parámetros del material mandan: formato de grabación, aspecto de cuadro y píxel, cadencia, base de tiempo, campos, muestreo audio, códecs (Adobe, «Sequence presets»).
- Avid: mezcla de formatos y cadencias en un mismo *timeline* es posible, pero recodifica al vuelo (DNxHD Technology 2012).

## 3. Bins
- *Bin* = carpeta de clips/secuencias; guarda referencias y metadatos, no el material (§1, §3).
- *Master clip* enlazado al fichero entero; *subclip* = trozo del *master clip* (Avid p.232).
- Avid: *bins* en tres vistas (*Text*, *Frame*, *Script*); *Media Tool* con los mismos recursos (p.321).
- Resolve: *bins* en el *Media Pool*; todo va al *bin* maestro salvo organización propia; *timelines* también se guardan en un *bin* (p.23, p.860).
- Premiere: *bins* en el panel Proyecto; se crean y borran desde el menú contextual (ayuda Adobe).
- Órdenes de Avid: *Select Offline Items*, *Select Media Relatives*, *Select Sources*, *Select Unreferenced Clips* (Avid 1999, pp.285-287).

## 4. Timeline
- Representación gráfica del montaje: pistas de vídeo/audio, se actualiza al trabajar (Avid p.462).
- Premiere: ajustes se fijan al crear la secuencia; base de tiempo queda bloqueada (ayuda Adobe).
- Resolve: *timeline* copia por defecto los ajustes del proyecto; admite ajustes propios para varias entregas (p.860).
- Avid (2022.10): cada secuencia usa una plantilla (pistas, nombres, TC inicial) (What's New 2022.10, p.15).
- Aviso de material ausente: clips rojos en Avid (p.470); línea morada en Resolve si falta original con *proxies* (p.220).
- *Render*: cálculo de efectos no reproducibles al vuelo; Resolve con caché inteligente o de usuario, exclusiva del proyecto (pp.209, 222).

## 5. Códecs
- Formato de codificación (estándar) ≠ códec (implementación) ≠ contenedor (empaquetado): tabla del tema.
- Fases: captación (compresión de cámara), montaje/acabado (DNxHD/DNxHR, ProRes, sin comprimir), montaje ligero (DNxHD 36, ProRes Proxy, DNxHR LB), entrega (temas 4 y 8).
- Avid: códecs de cámara no aguantan posproducción compleja; DNxHD pensado para montaje no lineal multigeneración (DNxHD Technology 2012).
- Familia DNxHD: 8/10 bits, conserva el *raster* HD completo, normalizado como VC-3 SMPTE; variantes 444, 220x, 220, 145, 100, 36 (offline HD progresivo) (DNxHD Technology 2012).
- Resolve: *proxies* en ProRes/DNxHR/H.264/H.265; medios optimizados hasta sin comprimir 16-bit float; sólo 16-bit float, ProRes 4444/4444 XQ (y DNxHR 444, p.202) valen para HDR (pp.202-203, 213).
- H.264/H.265 (GOP largo) pesan al montar y se cachean antes en Resolve (p.209).

## 6. Proxies
- *Offline* (montaje, material ligero) / *online* (acabado, resolución completa): tabla del tema.
- Avid DNxHD 36: pensado para montaje creativo *offline*, sólo progresivo 23.976/24/25/29.97p, calidad suficiente sin conformar (DNxHD Technology 2012).
- «Offline» tiene un segundo sentido: clip sin material (no confundir con el flujo offline/online).
- *Proxy* = copia ligera enlazada al original, para montar en su lugar (Adobe «Ingest and Proxy»; Blackmagic p.213); el enlace no se pierde, a diferencia del offline clásico.
- Premiere: crear→montar→volver al original; *proxies* externos hay que asociarlos (*attach*); 4 funciones no compatibles con *proxies* (Dynamic Link, Audition, canales/interpretar) (ayuda Adobe).
- Resolve: resolución Original/Half/Quarter/Eighth/Sixteenth/Automática y códec al crear (p.213); *Deliver* vuelve siempre al original salvo casilla «Use proxy media» (p.220).
- Avid (2022.10, Enterprise): *Create Proxies* desde el *bin*, icono naranja; modos de reproducción High-Res/Proxy Preferred/High-Res Preferred; audio 48,048 kHz no admitido (What's New 2022.10, pp.4, 9-10).
- Resolve distingue *Proxy Media* (portable, exportable), medios optimizados (internos, no exportables) y caché de *render* (exclusiva del proyecto) (pp.201, 204, 222).
- *Timeline Proxy Mode* no crea ficheros, sólo baja resolución de reproducción; sin relación con *Proxy Media* (p.201).
- Oficio: *proxies* para material pesado, montaje remoto y montar mientras se copia el original; comprobar siempre antes de exportar.

## 7. Conformado
- Conformar = importar fichero de intercambio (EDL/AAF/XML) y reenlazar cada clip al material de calidad (Blackmagic p.476); o pasar de transcodificado a cámara raw dentro del mismo programa (p.492).
- Reconocimiento por metadatos, no por imagen: Avid compara nombre de cinta, TC y canales, ignora resolución de captura/audio (Avid 1999, pp.336-337); Resolve conforma EDL por nombre de bobina y TC (p.492).
- Regla de oficio: no tocar nombre de cinta/bobina ni TC de origen.
- Preparar el montaje: bajar a V1 lo no superpuesto; exportar película de referencia offline para comparar tras conformar (Resolve p.479).
- Avid: *Redigitize* (recapturar con datos ya en el *bin*, exige material original) y *Decompose* (crea *master clips* nuevos más cortos con colas, rompe enlace con origen) (Avid 1999, pp.231-235).
- *Consolidate*: copia a otro disco sin recapturar; trata distinto *master clip* (copia entera, .old/.new), *subclip* (sólo el tramo, .new) y secuencia (relinka sola) (Avid 1999, pp.327-330).
- Reenlazar: Avid *Relink* (Managed/Linked Media desde 2022.10; por carpeta desde 2023.3); Resolve *Relink* desde *Media Pool*, busca subcarpetas; Premiere: rutas históricas + búsqueda automática, si fallan abre *Link Media* (Avid What's New 2022.10 pp.13-14, 2023.3 p.3; Resolve p.495; Adobe «Relink media»).
- Antes de dar por bueno: buscar *offline* (rojo/morado), comparar con referencia, sincronía, confirmar resolución completa (no *proxy*).

## 8. Exportación
- Dos sentidos: exportar la pieza (fichero final) o el proyecto (decisiones: EDL/AAF/XML/OTIO/OMF sin o con material).
- Avid 1999: exporta audio/vídeo para otras aplicaciones; ajustes guardables como plantillas (pp.716-717).
- Premiere: exportación directa desde el programa o cola de Adobe Media Encoder (permite seguir montando); recomendada para exportaciones largas o varias versiones (ayuda Adobe, «Export options», «Export directly to Media Encoder»).
- Premiere exporta proyecto a AAF, EDL, XML (Final Cut Pro) y OMF (Pro Tools) (ayuda Adobe).
- Resolve, página *Deliver*: formato, tramo, cola de *render*, preajustes (p.4185-4186).
- Dos modos: *Single clip* (un fichero) / *Individual clips* (uno por clip, TC clonado del original para reconformar) (p.4196).
- Para pasar a otro programa: clips individuales + EDL/AAF/XML/OTIO con mismos metadatos de bobina/TC (p.4241).
- Deliver usa siempre el original aunque se monte con *proxies*; versión Studio exporta IMF (SMPTE ST.2067) (pp.4219 y aviso Deliver).
- Comprobaciones antes de exportar (oficio): secuencia última versión, sin *offline* ni efectos sin render, material original, preajuste del destino, nomenclatura de la casa, revisión del fichero.

## Aplicación práctica
- Supuesto: cámara H.265 UHD → pieza HD 1080/25 + versión vertical (§ «Aplicación práctica»).
- Proyecto fijado antes de importar; *bins* por origen/tipo/secuencias; *proxies* o transcodificado por GOP largo; *timeline* HD 25 + *timeline* vertical propio; *render* de efectos; conformado con reenlace por metadatos (rojo Avid); exportación con preajuste de emisión y de redes, revisión final; si pasa a otra sala, exportar también AAF/EDL/XML y clips individuales en Resolve.

## Lo que este tema no da, y dónde está
- Sistema, almacenamiento y preajustes reales de CSRTV: no consta.
- Guía vigente de Media Composer (sólo 1999 + notas 2022.10/2023.3 + DNxHD 2012); DNxHR y ProRes sin documentación Avid/Apple propia.
- Resolución, cadencia, muestreo, bits, compresión, GOP, contenedores, HDR, IMF/AS-11 → temas 2 y 4.
- Color, efectos, transiciones, grafismo, subtítulos, limpieza de audio → tema 7.
- Ingesta, copia verificada, metadatos, archivo → tema 8.
- Redes y plataformas → tema 12; automatización/MAM/PAM/redacción → tema 13.
- Vistas de *bin*, *Attic*, bloqueo de *bins* compartidos, nomenclatura, AAF/OMF a fondo → tema 15.
