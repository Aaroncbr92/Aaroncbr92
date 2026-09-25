# Tema 13 del específico de Operador/a Montador/a de Vídeo · Automatización, plantillas, MAM/PAM, newsroom y flujos de producción integrados

**Siglas**: RTVA, CSRTV, RTVE, BOJA, EBU, MAM, PAM, DAM, NRCS/NCS, MOS, CG, XML, API.

Esqueleto para repasar, no resumen: cada línea manda a la fuente del tema, no sustituye leerlo.

<!-- indice --><!-- /indice -->

## 1. Automatización

- Convenio, ficha 5212206 (p. 190): **«Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de programas y bloques publicitarios.»**
- Convenio, ficha encargado 5212204 (p. 127): **«Realizar todas las operaciones necesarias previas para la posterior emisión automatizada»**.
- Convenio no dice qué sistema ni qué campos lleva la base de datos.
- Oficio (RTVE, sin fuente citada): escaleta → servidor de emisión → automatización dispara servidor, grafismo, conmutación.
- Principio de diseño: la emisión va separada (servidores, almacenamiento y red propios); único punto donde un fallo se ve en antena.
- Oficio: pieza con el nombre exacto que espera la escaleta; duración real = la anunciada; terminada y en servidor antes de su hora.
- Manual Resolve 21, cap. 8 (p. 215-217): carpetas vigiladas del Blackmagic Proxy Generator generan *proxy* automático; subcarpeta «Proxy» reservada; *Start*/*Stop* en *Processing*; estado *Waiting*.
- Manual Resolve 21, cap. 8 (p. 198): tareas en segundo plano (render, *quick export*, *proxy*); desactivado por defecto.
- Manual Resolve 21, cap. 187 (p. 4185): cola de *render* en *Deliver*, varios trabajos con distintos ajustes.
- Ayuda Premiere, «Export directly to Adobe Media Encoder»: cola de Media Encoder, recomendada para exportaciones largas o varias versiones.
- Manual Resolve 21, cap. 187 (p. 4215): *render* remoto entre estaciones Studio; exige misma biblioteca de proyectos y acceso al mismo material.
- Manual Resolve 21, cap. 201 (p. 4418): *Workflow Integration Plugins* (Electron, API Javascript, Python/Lua) — vía de conexión de un MAM.
- Oficio: la automatización no mira contenido; lo automatizado se revisa al final (nombre, duración, principio y final).

## 2. Plantillas

- Definición de oficio: elemento o ajuste preparado que se reutiliza; tres clases: rótulo, salida, nombre.
- Manual Resolve 21, cap. 56 (p. 1215): *Lower 3rd* central posiciona dos líneas en *title safe*; *Text+* con estilo único; *Fusion Titles*, biblioteca de plantillas prediseñadas.
- Ayuda Premiere, «Overview of Motion Graphics templates»: fichero **.mogrt**, creado en Premiere o After Effects; para *titles*, *lower thirds*, botones; panel *Graphics Templates*.
- Ayuda Premiere, «Install Motion Graphics templates»: instalación en pestaña *My Templates*; desde Creative Cloud, disponible sin instalar.
- Ayuda Premiere, «Export graphic as a Motion Graphics template»: exportación sólo de gráficos creados en Premiere, no de .mogrt de After Effects; no con varios gráficos seleccionados.
- Ayuda Premiere, «Use data-driven Motion Graphics templates»: datos de tres tipos (texto, color, número), fijados en After Effects, no editables en Premiere.
- Manfredi (2010, pp. 139-140), sobre iNews: rótulos que inserta el periodista **«irán directamente a la emisión»**.
- Manual Resolve 21, cap. 187 (pp. 4193-4194): *presets* de exportación con *Save as New Preset*; exportables/importables en ficheros **.xml**.
- Ayuda Premiere, «Export directly to Adobe Media Encoder»: *preset* por defecto **«H.264 Match Source - Adaptive High Bitrate»**, salvo último ajuste usado.
- Manual Resolve 21, cap. 15 (p. 345-346): variables de metadatos con «%»; ejemplo escena_plano_toma; variables %date/%time toman fecha de salida, no de rodaje.
- Oficio: el nombre del vídeo que manda es el de la escaleta, no lo compone la variable.

## 3. MAM/PAM

- MAM = *media asset management*; PAM = *production asset management* (nombres de industria, sin definición UIT/EBU/SMPTE hallada).
- Oficio (RTVE, sin fuente citada), cinco funciones del MAM: catálogo, versiones, baja resolución, ciclo de vida, permisos.
- DAM = término general (fotos, documentos, audio); MAM especializado en audiovisual (código de tiempo, subclips, versiones, derechos por ventana).
- Oficio: distinción MAM/PAM es de oficio (PAM = producción en curso; MAM = terminado y archivo); ningún fabricante la define igual.
- Avid, página de producto *MediaCentral | Production Management* (leída 25-09-2026): seguimiento ingesta-archivo, multiusuario, permisos, transcodificación/archivo/restauración automáticos, almacenamiento Avid NEXIS, búsqueda desde Media Composer/Premiere/Cloud UX.
- Oficio (RTVE): copia de baja resolución viaja por red ofimática, se ve y se marca; fichero grande no se mueve hasta el conformado.
- Ayuda Premiere, «Ingest and proxy workflows in Premiere»: **«you first create proxy files, edit these proxies, and then convert to full resolution»**.
- EBU Tech 3293 v1.10 (abril 2020), p. 7: **«"If you can't find it, you don't have it!"»**; metadatos = **«glue between production operations»**; EBUCore **«is a minimum requirement»**.
- EBU Tech 3293, p. 8: EBUCore definida como **«the Dublin Core for media»**.
- Manual Resolve 21, cap. 201 (p. 4418): MAM accesible desde Resolve por *Workflow Integration Plugins* (ejemplo EditShare/FLOW: comentar, buscar, previsualizar sin salir de Resolve).
- Oficio: montador busca por datos, no por nombre de fichero; devuelve la pieza al sistema con metadatos completos.
- Oficio (RTVE): almacenamiento de producción (inmediato, red de bloques, coste alto) vs. de archivo (diferido, cinta posible, coste bajo).
- Oficio (RTVE): la ingesta es donde se llena el almacenamiento; falta política de borrado/archivo = sistema se para.

## 4. Newsroom

- Oficio (RTVE, sin fuente citada): *newsroom* = redacción y su sistema (NRCS); contiene escaleta, guion, referencias a material, cronometría, estados, agenda/teletipos.
- Oficio: la escaleta es la base de datos; todo lo demás cuelga de ella.
- Oficio: cronometra en tiempo real; es el único sitio donde se cambia algo; habla con los demás equipos por protocolo (MOS).
- mosprotocol.com (portada, leída 25-09-2026): MOS = **«An evolving protocol for communications between Newsroom Computer Systems (NCS) and Media Object Servers (MOS)»**.
- mosprotocol.com, FAQ: reparto — NCS crea/modifica/borra información editorial y *playlists*; MOS crea/modifica/borra objetos de medios y sus metadatos.
- mosprotocol.com, FAQ: tres tipos de mensajes — *Descriptive Data for Media Objects*, *Playlist Exchange*, *Status Exchange*.
- mosprotocol.com, FAQ: transporte **«TCP/IP network via socket communication»**; texto etiquetado unicode; cada versión «super set» de la anterior.
- Especificación MOS 2.8.5/4.0: mensajes XML según DTD MOS, **«must be well formed XML, but are not required to be valid»**; codificación ISO 10646 UCS-2 *big endian*.
- Especificación MOS 2.8.5: puertos por defecto 10540 (redacción), 10541 (servidor), 10542 (búsquedas), seleccionables por proveedor desde la 2.5. MOS 4.0: web sockets, canales mom/ro/aux = 10540/10541/10542.
- mosprotocol.com, «Current Versions»: 4.0 (7-VI-2019, *Secure Web Sockets*); 2.8.5 (7-IX-2017, *Socket*); 3.8.4 (11-II-2011, *Web Services*).
- mosprotocol.com: origen en Orlando, 1998, conferencia de desarrolladores ENPS de AP; más de 150 empresas participantes (2021); **no es norma oficial** de organismo de normalización.
- Avid, página de producto *MediaCentral | Newsroom Management* (iNEWS, leída 25-09-2026): **«Build rundowns, adjust timing, go live and make real-time changes—even on-air»**; integración con automatización de estudio, apuntador, grafismo, servidores de emisión.
- Libro de estilo CSTV (2004), 6.1 (p. 88): la escaleta **«es el documento básico en el que se plasma y ordena el contenido de un programa»**, con hecho noticioso, formato, tiempos, autor, procedencia, identificación del presentador y acotaciones técnicas.
- Libro de estilo, 6.1 (p. 88): cambio de escaleta se comunica **«inmediata y simultáneamente, a todas las personas y departamentos afectados»**.
- Libro de estilo, 6.1.1 (p. 88): **«Son inadmisibles los cambios en la identificación de un vídeo [...] El nombre de una noticia en escaleta debe respetarse por obligación»**; excepción, vídeo terminado antes de la escaleta.
- Libro de estilo, 6.1.2 (p. 89): el redactor fija en escaleta **«sus textos definitivos (incluidos los rótulos con su orden y ubicación precisa)»**.
- Manfredi (2010, p. 138): sistema Avid instalado **«en todos los Servicios Informativos de RTVE y, en el caso de Andalucía, en Canal Sur»** (dato de 2010, no consta que siga vigente).
- Manfredi (2010, pp. 139-140): periodista trabaja en iNews de Avid; iNews Instinct (2005) permite montar con vídeo y guion en el propio puesto.
- No consta en documento publicado qué sistema de redacción, MAM ni servidores usa CSRTV hoy.
- Oficio (RTVE): edición ligera en el puesto del redactor (copia de baja resolución) vs. edición completa en sala del montador (alta resolución); el conformado une ambas.
- Oficio (RTVE): edición de informativos en minutos, sencilla, prioridad a tiempo, frente a postproducción en días, completa, prioridad a que esté bien.
- Oficio: edición tiene que estar donde está el redactor; el material se edita mientras se ingesta (prestación clave para informativos).

## 5. Flujos de producción integrados

- Definición de oficio: flujo integrado = todas las etapas sobre el mismo material y los mismos datos, sin copias ni pasos a mano.
- Oficio (RTVE): etapas — ingesta, gestión, edición, emisión; el archivo atraviesa las cuatro, no es una quinta.
- Oficio: cada etapa encuentra el material por sus datos descriptivos, no por el nombre de fichero.
- Oficio (RTVE): vías de ingesta — tarjeta/cámara (copia y verificación), tiempo real (canal ocupado), agencia/intercambio (normalización), archivo (restauración).
- Oficio (RTVE): se ingesta con metadatos o no se ingesta; se genera copia ligera al ingestar; ingesta en tiempo real ocupa un recurso entero; grabación doble por ser irrepetible.
- Oficio (RTVE): tres redes — de señal (tiempo real), de producción (ficheros/proxy/control), ofimática (expuesta a internet, por eso separada).
- Oficio (RTVE): degradación por fallo — sistema de redacción (papel/manual), servidor de emisión (segundo servidor replicado), almacenamiento (redundancia propia), red (doble camino), estudio (alternativo con escaleta cargada), energía (SAI y grupo).
- Oficio: la redundancia se prueba; la degradación tiene que ser ordenada y ensayada.
- Convenio, ficha 5212206 (p. 190), tareas literales leídas sobre el flujo (oficio): **«Recibir y enviar enlaces»**, **«Configurar sistemas de edición y preparar los materiales a utilizar»** (ingesta); **«Editar y postproducir material audiovisual con criterios de narrativa audiovisual»** (edición); **«Realizar el control técnico de calidad y corregir video y audio para su emisión y/o venta»** (control); **«Etiquetar, grabar e introducir en base de datos [...] emisión automatizada»** (emisión); **«Compactar para el archivo de material audiovisual»** (archivo).
- Ficha 5212206: otras tareas no ligadas al flujo — **«Grabar, emitir y reproducir videos [...] con selección alternativa a la realización»**; **«Repicar cintas orientadas a la producción, emisión y comercialización»**; lista **«no constituye una lista cerrada de funciones»**.
- Aplicación práctica (oficio, con fuentes puntuales del tema): pieza de ingesta a emisión, en 9 pasos (nace en escaleta con nombre fijo, entradas verificadas/grabadas con metadatos, copia ligera automática, búsqueda en MAM/PAM, montaje con escaleta de planos —Libro de estilo, 6.3—, rótulo con plantilla o desde grafismo, exportación con *preset* de la casa, revisión, entrega al servidor con MOS, devolución al sistema).
- Aplicación práctica: cambio de escaleta a 20 minutos — cambio se comunica desde el origen (Libro de estilo 6.1); nombre no cambia (6.1.1); se duplica antes de recortar, se exporta con mismo *preset*, se sustituye en servidor y se avisa a emisión.
