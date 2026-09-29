# Tema 9 del específico de Grafista · Herramientas profesionales de diseño, composición, edición, plantillas y automatización gráfica

**Siglas**: RTVA; CSRTV; BOJA; CMYK; RGB; MOS (*Media Object Server*); NCS (*newsroom computer system*); CG; TCP/IP; GPL; SMPTE; EBU; CSV; TSV; RCP; of.=oficio, sin norma; AE=After Effects; Res.=manual de DaVinci Resolve 21.

Esqueleto para repasar, no resumen: lo que aquí no está, no se da por sabido.

<!-- indice -->
<!-- /indice -->

## Herramientas profesionales

- Sin norma: fuente=documentación de fabricante (ejemplos) y MOS; el resto, of. Se estudia la función, no el botón.
- Convenio (BOJA 240, 10-XII-2014), anexo III, Grafista 5345100, p. 129: «Crear y realizar, con criterios artísticos, el diseño gráfico que requieren los canales y programas.»; «Diseñar y realizar y todo tipo de imagen gráfica para programas y postproducciones, y otros fines promocionales.»; «Realizar escenarios virtuales y diseñar la representación gráfica de la información. Realizar el asesoramiento estético a otras áreas como rotulación o postproducción.» No le da lanzar rótulos en control ni nombra programa. Programas de CSRTV: no consta.
- Of. familias: bits (píxeles, pierde al ampliar; Photoshop); vectorial (curvas, no pierde; Illustrator); maquetación (InDesign); composición y animación (capas; AE); 3D (Blender, Cinema 4D). Aparte: editor y grafismo de directo. Res. integra edición, composición (Fusion), *motion graphics*, color, audio y acabado.
- Of. sin pérdida al ampliar: sólo lo vectorial, esté donde esté; al doble con buen remuestreo «casi no se nota» ≠ sin pérdida.
- Of. diferido (antes de emitir; Blender, Cinema 4D)/tiempo real (a velocidad de vídeo; Unreal, Unity, Vizrt, Chyron). Blender: render=cálculo de imagen 2D desde geometría 3D; trazado de rayos «but much slower». Of. Unreal=motor de videojuego (escenografía virtual, realidad aumentada); Motion Design=módulo de emisión.
- Licencias (of.): Viz Artist 5.3, funciones según la llave física; Res. gratuita/Studio (Studio Only: render remoto, módulos por scripts, Magic Mask v2); CasparCG, GPLv3 o posterior. Comprobar versión y licencia antes de mandar un proyecto.

## Diseño

- Of. imagen fija: trazado (*path*)=curva vectorial en documento de bits, recorta con precisión. Canal=capa de color o selección; RGB=3 + compuesto; cada máscara guardada=un canal alfa.
- Capas: PSD sí (capas, efectos, máscaras, canales, trazados); TIFF puede, no es su cometido; TGA no (alfa); PNG no. CMYK: PSD, JPG, TIFF sí; PNG no (web, RGB). CMYK=tinta; RGB=pantalla. TV en RGB; paso a señal=tema 8.
- Of. vectorial: calco de imagen=bits a vectores; buscatrazos (*pathfinder*)=combina formas; fusión (*blend*)=pasos intermedios; ajustar segmentos=tramo de curva.
- Buscatrazos: unir=contorno exterior; restar=la de abajo menos lo que tapaba la de arriba; intersecar=sólo el solape; excluir=todo menos el solape (hueco); dividir=tantas formas como trozos.
- Bézier: nodo inicial, nodo final, punto de control, palanca de curva (extremos Y controles). Blender: modo Bézier libre.
- Of. dónde: vectorial=logotipo, mosca, pictogramas, retícula de rótulos; fija=fotografía, textura, fondos, retoques, recortes; composición=lo que se mueve; 3D=decorados, realidad aumentada, logotipos corpóreos.

## Composición

- Of. capas: pila en línea de tiempo, lo de arriba tapa (AE). Nodos: cajas con cables (Fusion). Res.: nodo *Merge*=herramienta principal de composición (dos entradas); nodos de máscara=un canal, no RGBA.
- Área de trabajo (*work area*)=tramo de tiempo, dos asas; espacio de trabajo=disposición de paneles. Capas 2D: primer término=numeración más baja; con 3D decide la profundidad. Luces: sólo afectan a capas 3D. Precomponer: capas a composición nueva, queda una; efecto al conjunto.
- Of. máscara: trazado; calado (difumina bordes; *mask feather*; animable); opacidad; expansión (crece o encoge; no difumina). Res.: máscara de polígono=la más usada, Bézier, base de la rotoscopia (tema 5).
- Interpolación (Blender): cálculo de datos nuevos entre valores conocidos, como fotogramas clave. Espacial=por dónde; temporal=velocidad (editor de gráficos).
- Res. alfa: «Always use premultiplied images with a Merge node. / Only color-correct images that are not premultiplied. / Always filter and transform images that are premultiplied. / Never double premultiply an image.» Fallo: borde claro alrededor de la figura. Temas 5 y 8.
- Of. recopilar archivos: el proyecto enlaza; COPIA los usados a carpeta nueva (no mueve); para llevarlo a otro equipo; causa nº 1 de enlaces rotos. Tema 12.

## Edición

- El grafista no suele operar el editor (ficha: «para programas y postproducciones»). Of. dos puertas: fichero terminado (con transparencia si va encima); plantilla que rellena el montador. Lineal (cinta a cinta; cambiar el principio obliga a rehacer lo siguiente)/no lineal (ficheros, cualquier punto).
- Of. formatos: PSD nativo, capas; AI vectorial nativo; TIFF artes gráficas, archivo; PNG alfa, web, grafismo sobre fondo; JPG con pérdida, sin transparencia, fotografía; TGA alfa, secuencias de fotogramas; GIF 256 colores, transparencia de un solo valor, animaciones cortas; SVG vectorial, web; EPS vectorial, transparencia según el caso, imprenta.
- Of. regla: transparencia y web=PNG; capas=nativo; secuencias renderizadas=TGA; fotografía comprimida=JPG. TGA sin compresión: mismo tamaño siempre (píxeles × bytes por píxel); entrelazado y primer campo no lo cambian.
- Apple: ProRes 4444 XQ y 4444, «the only ProRes codecs that support alpha channels»; ningún ProRes 422 lleva alfa. Tema 8.
- Of. reparto: lo fijo (cabeceras, cortinillas, fondos, mosca)=fichero; lo que cambia (nombre, cargo, lugar, fecha)=plantilla. Quién rellena, qué se incrusta o lanza: no consta (tema 7).

## Plantillas

- Of. plantilla: diseño previo donde sólo cambia texto, dato o imagen. Fija: tipografía, cuerpo, color, posición, animación y duración, márgenes en zona segura (tema 8); cambia el usuario: sólo campos abiertos. Eslabones: rótulo, escena, salida, nombre.
- Res. cap. 56, p. 1215: Lower 3rd izquierdo, central, derecho (central: dos líneas en title safe); *Text+* (un solo estilo); *Fusion Titles* (prehechas, biblioteca propia). P. 1226: macros de Fusion; las propias, en Fusion guardadas como macro.
- Premiere (ayuda, 7-I-2026): .mogrt, creable en Premiere o AE; títulos, tercios inferiores y botones; panel *Graphics Templates*; origen: carpeta local, bibliotecas de Creative Cloud, Adobe Stock. Instalar: pestaña *My Templates*; en biblioteca de CC no se instala. Usar: arrastrar a pista de vídeo; aspecto en *Edit* de *Properties*. Exportar: *Graphics and Titles > Export Motion Graphics template* o botón derecho; sólo gráficos de Premiere, no .mogrt de AE; no con 2 o más gráficos seleccionados. Con datos: texto, color, números; fijados en AE.
- AE (ayuda, 11-V-2026), *Essential Graphics*: 1 *Composition > Open in Essential Graphics*=*Primary*; propiedad de otra composición fuera de su jerarquía=rojo, no funciona; anidar. 2 Arrastrar propiedades (o *Add Property to Essential Graphics*); sólo esas se personalizan: casilla, color, deslizadores, texto (*Source text*), posición, escala, giro. 3 Renombrar, reordenar, agrupar, comentarios. 4 *Export Motion Graphics Template*: bibliotecas CC, carpeta local *Essential Graphics* (directa en Premiere) u otra carpeta (no aparece sola); *Set Poster Time*=miniatura.
  - Sin AE instalado: sólo *Classic 3D*, sin módulos de terceros, sin FLV, sin *Dynamic Link*; fuera *Puppet* y *Warp Stabilizer*. Datos: CSV o TSV; el autor fija tipo de columna y filas mínimas y máximas.
- iNews (Manfredi, 2010, Canal Sur): rótulos del periodista «irán directamente a la emisión». Incrustar o lanzar: no consta.
- Vizrt (*Viz Pilot Edge* 3.5): Template Builder (diseño; TypeScript, datos en directo); redacción (rellena, guarda elementos de datos, los mueve a la escaleta); control (playout). Viz Multiplay 3.3: «Uses Viz Engine for playout»; plantillas del Pilot Data Server.
- Chyron *Base Scenes*: publicidad del fabricante. Unreal 5.8: Rundown con páginas y plantilla; Rundown Server API con RCP incorporado. CasparCG: 24/7 desde 2006; cliente aparte. Temas 3 y 6.
- *Presets*=formato, códec, resolución, audio, nombre, destino. Res.: *Save as New Preset*; .xml exportable a otros puestos; *Add to Render Queue Using* (cap. 187, pp. 4193-4194). Premiere→Media Encoder: por defecto «H.264 Match Source - Adaptive High Bitrate», salvo modo de exportación o exportación rápida abiertos antes («the last-used export setting»). Of.: un preset por destino. Temas 8 y 13.
- Variables de metadatos (Res. cap. 15, pp. 345-346): se teclea %; escena 12, plano A, toma 3 con guiones bajos=«12_A_3»; campo vacío=nada. Sitios: *Media Pool*, metadatos, galería, *Data Burn*, nombre de fichero en *Deliver*. %date y %time=de la salida, no del rodaje. Tema 12.

## Automatización gráfica

- Of. cuatro niveles: pieza (expresiones); programa (*scripts*); contenido (datos, escaleta); salida (colas de *render*, carpetas vigiladas, emisión automatizada).
- Expresión=fórmula sobre un parámetro (Res. cap. 73, p. 1634). *Wiggle* (of.): expresión, no efecto; oscilación al azar, dos números: veces por segundo y cuánto.
- Res. cap. 73, p. 1640: script crea funciones o automatiza tareas; en Fusion reordena nodos, gestiona cachés, genera varios ficheros de salida. FusionScript: Lua y Python 2 y 3 en algunos contextos. Cap. 201, p. 4418 (Studio): *Workflow Integration Plugin* (Electron, API JavaScript, Python o Lua). Unreal: *blueprints*=programación visual (of.).
- Photoshop: acción=«a sequence of recorded tasks» (18-VIII-2026). Lote: *File > Automate > Batch*; origen carpeta o abiertos; destino: abiertos, sobrescribir u otra carpeta. *Droplet*: *File > Automate > Create Droplet* (23-II-2026). Of.: copia antes de sobrescribir; probar con un caso conocido antes de cien.
- Chyron: escenas con lógica, actualización al segundo con datos y disparadores; PRIME 5.3: primera integración oficial de HTML (HTML Input). Unreal Motion Design: datos en tiempo real.
- Photoshop (24-V-2023): variables de visibilidad, de sustitución de texto y de sustitución de píxeles; no en la capa de fondo. Conjunto de datos=variables y datos, uno por versión; fichero con comas o tabuladores, nombres en la primera línea, un conjunto por línea, todas las variables. *Image > Variables > Define* y *Data Sets*; *File > Import > Variable Data Sets*; *File > Export > Data Sets As Files*=un PSD por conjunto. *Apply* sobrescribe el original.
- Of. diseño con datos: aguantar el más largo y el más corto (municipio más largo de Andalucía, siete dígitos, cero); qué muestra si no llega; camino manual.
- MOS (mosprotocol.com): protocolo en evolución entre NCS y servidores de objetos de medios (vídeo, audio, almacenes de fijas, CG). NCS=información editorial y listas; MOS=objetos de medios y metadatos.
  - Tres mensajes: *Descriptive Data for Media Objects* (el servidor empuja descripciones y punteros); *Playlist Exchange* (NCS controla la secuencia); *Status Exchange* (estado de clip o sistema; de elementos de lista u órdenes de emisión, *running orders*).
  - TCP/IP por *socket*; texto etiquetado unicode; cada versión, «super set» de la anterior. Versiones: 4.0, 7-VI-2019 (*Secure Web Sockets*); 2.8.5, 7-IX-2017 (*Socket*); 3.8.4, 11-II-2011 (*Web Services*).
  - No es norma oficial: se presentaría «at a later date» a organismos de normalización; no es de SMPTE ni EBU. Viz Multiplay abre y controla listas MOS; Chyron PRIME CG, vía CAMIO.
- Emisión automatizada: Chyron *Playout Automation mode* (PRIME 5.3, 12-II-2026); Unreal: dos API (Rundown Server y Remote Control), RCP de la página modificable por Remote Control API, Rundown Server API por WebSocket; Vizrt: Viz Trio o Viz Pilot controlan Viz Engine (*Dual Channel Mode*, guía 5.2).
- Salida: cola de Res. (*Deliver*, cap. 187, p. 4185; *Start Render*); Media Encoder (varias exportaciones, presets propios). Carpeta vigilada: Blackmagic Proxy Generator, sin intervención humana (cap. 8, p. 215).
- Of. límite: no mira el contenido; revisar nombre, duración, principio y final; dato mal enlazado=rótulo equivocado; fuente caída=hueco; ensayar, camino manual.

## Aplicación práctica

- Rótulo de informativo (of.): vectorial, tipografía de la identidad (tema 2), zona segura de título (tema 8); dos campos abiertos (nombre, cargo), probar el más largo y cargo de dos líneas; directo: redacción rellena desde escaleta; incrustado: Fusion Titles o .mogrt; alfa sin borde claro ni fondo negro.
- Cabecera con transparencia: reglas de alfa de Res.; ProRes 4444 o 4444 XQ, o secuencia PNG o TGA, nunca JPG ni ProRes 422; preset de la casa, nombre por variables; recopilar archivos; revisar salida.
- Noche electoral: plantillas enlazadas al escrutinio; límites: nombre más largo, cero, empate, municipio sin datos; camino manual (sin él, pantalla en blanco); ensayo con datos de prueba.
- Cuarenta versiones: una plantilla con campos (día, hora, formato); script o datos; Photoshop: variables y conjuntos, fichero de 41 líneas, acción por lotes; preset por destino; revisar varias al azar.

## No consta

- CSRTV: programas, grafismo, servidor de emisión, sistema de redacción actuales; iNews (Avid) en Canal Sur, de 2010.
- No leído: expresiones de AE, Illustrator automatizado, scripts de Photoshop; Cinema 4D, Maya, Houdini, Nuke, Brainstorm, Ross XPression, Ventuz; plantillas de CasparCG; límites de ficheros; equipo físico.
