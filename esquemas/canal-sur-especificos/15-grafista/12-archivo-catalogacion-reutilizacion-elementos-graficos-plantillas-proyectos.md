# Tema 12 del específico de Grafista · Archivo, catalogación y reutilización de elementos gráficos, plantillas y proyectos

**Siglas**: RTVA, CSRTV, BOJA, EBU, SMPTE, ISO, CCSDS, OAIS (SIP, AIP, DIP, PDI), MXF, UMID, UUID, XMP, DCMI, MAM, DAM, RAID, LTO, LTFS, INCIBE, CRC, MD5, SHA, XXHASH64, CSV, ALE, EDL, LUT, TB, MB/s.

Esqueleto para repasar, no resumen: el detalle, en el tema. Sin norma jurídica; lo demás, oficio.

<!-- indice -->
<!-- /indice -->

## El punto en la ficha del puesto

- Convenio X RTVA (BOJA 240, 10-XII-2014), anexo III, ficha 5345100 Grafista (p. 129); B03, art. 45.1 (p. 73). Última tarea: «Mantener el archivo de imagen del departamento gráfico». Lista no cerrada.
- Oficio, 4 clases: elementos, plantillas, proyectos, piezas terminadas.
- Trampa: ficha 9420000 J. Sec. Diseño Asistido (p. 153): soporte gráfico de documentación técnica de instalaciones de RTVA y SSFF (Sociedades Filiales).
- Suyas: «Definir, desarrollar, implementar y mantener los sistemas de archivo gráfico»; librerías electrónicas; almacenamiento de planos y referencias. Archivo de planos, no del grafismo (lectura del objeto).
- No consta sistema, campos ni vocabulario de CSRTV.

## 1. Archivo

- Oficio: archivar = sacar de donde se trabaja y guardar. Producción: acceso inmediato, coste/TB alto. Archivo: acceso diferido (cinta), coste bajo.
- Oficio, dependencias: medios, elementos compartidos, fuentes, complementos, plantillas y ajustes (presets, tablas de color). Archivo = proyecto + lo que enlaza (tema 11, licencias).
- Resolve 21 (Blackmagic, jul. 2026), cap. 3, pp. 95-96. Archive: todos los medios, incluidos subtítulos, más proyecto; usos: pasar a otro usuario o archivar.
- Project Manager, «Archive»; volumen «large enough»; opcional Optimized media y Render Cache; errores de medios offline, al final.
- Escribe directorio .dra; subdirectorios con ruta original. Restaurar: copiar antes la .dra al volumen de trabajo (Restore no la mueve); «Restore» o arrastrar; nombre único; enlazado a los medios de dentro.
- Oficio: no comprueba sumas ni guarda fuentes instaladas ni complementos de terceros; no decide copias.
- DPC, «Fixity and checksums»: fixity = archivo sin cambios (Bailey, 2014); checksum = «digital fingerprint», no dice dónde cambió; «chain of custody»; MD5 y SHA-256 «of increasing strength»; para pérdida accidental MD5 basta; otra copia repara; «data scrubbing».
- Clone Tool, cap. 17, pp. 373-374, seis opciones (velocidad frente a seguridad; «Collision resistance»): None; File Size (mínima); CRC 32 (código de error, no hash; más rápido que MD5, menos seguro); MD5 (128 bits, por defecto); SHA 256 y 512 (más lentos, más seguros); XXHASH64 (el más rápido, buena protección).
- MD5: colisiones en cine y vídeo «probably small». Informe de sumas en la raíz de cada destino (p. 373); guardarlo con la copia (oficio).
- 3-2-1, INCIBE (29-09-2021): tres copias, dos dispositivos distintos, una en lugar diferente. Oficio: dos no cumplen; cada copia con suma.
- RAID (oficio): 0 striping sin redundancia; 1 mirroring, dos discos, mitad de capacidad; 5 paridad, mínimo 3 discos; 6 doble paridad; 10 espejos en striping, 4 discos. Fallo de un disco (dos en RAID 6), no borrado, corrupción, robo ni incendio. No es copia de seguridad.
- OAIS: CCSDS 650.0-M-3 (dic. 2024), §1.1: modelo CCSDS/ISO; no producto ni norma de televisión. Archivo que preserva para una Designated Community. «Open» = desarrollo abierto, no acceso libre. Abarca ingest, storage, gestión, acceso, dissemination, migración. Largo plazo (§1.6.2): cambios tecnológicos, futuro indefinido.
- §1.6.2: SIP (entrega, del Producer); AIP (Content Information + PDI, preservado); DIP (derivado de AIP, al Consumer). Oficio: SIP = entrega del grafista; DIP = copia a la sala.
- PDI, 5: Provenance (historia, origen, custodia), Context, Reference (identificador; ISBN), Fixity (no alterado sin documentar; suma guardada), Access Rights.
- §4.2.2: «six functional entities» (§4.2.3): Ingest, Archival Storage, Data Management, Administration, Preservation Planning, Access.
- §4.2.3.4: Replace Media (reproducir AIP; contenido y PDI «should not be altered») = migración. Disaster Recovery: duplicar en instalación separada = la copia externa de la 3-2-1.
- LTO (oficio): cinta abierta, regrabable; coste/TB bajo; sin energía guardada; décadas; acceso secuencial y lento: archivo, no trabajo.
- lto.org, leída 25-09-2026: 10.ª generación; LTO-10 hasta 100 TB comprimidos (nativa no dada); cartuchos 30 y 40 TB (no dice si nativos); hasta 1200 MB/s con compresión 2,5:1.
- Compatibilidad: hasta 7.ª escribe una generación atrás, lee dos; 8.ª y 9.ª escribe y lee una; 10.ª ninguna (cabezal rediseñado); solo LTO-10. Migrar cintas viejas (Replace Media).
- LTFS (25-09-2026): desde LTO-5; partición de índice y de ficheros; drag-and-drop; secuencial (oficio).
- Graphic Hub 3.9 (Vizrt), índice: Locate Duplicate Files, Add Metadata, Replace File References, Daily Backup Using a Second Graphic Hub, Main and Replication Servers with Failover, Graphic Hub Archives. Servidor de copia: parada diaria o semanal. Relevo: si cae el cluster. Archivos: importar y exportar arrastrando (Archives Panel).

## 2. Catalogación

- EBU Tech 3293 v. 1.10, p. 7: «If you can't find it, you don't have it!».
- Tres sitios (oficio): fichero (XMP; viaja); proyecto o base del programa (solo si se exporta, CSV, o se archiva); sistema de la casa, MAM (no viaja).
- XMP (Adobe): metadatos en el propio fichero; títulos, descripciones, palabras clave, autor, copyright; ISO 16684-1 desde principios de 2012; extensible. Espacios de nombres: Dublin Core `dc` (nombres y uso de DCMI); `xmpDM` (Adobe dynamic media group).
- Resolve, cap. 18 (p. 417): Cut, Edit, Color, Fairlight. Llegan con los medios (p. 418; Broadcast WAVE); editor: Description, Shot, Scene, Take, keywords.
- Keywords: lista estándar más las usadas (p. 420); varios clips a la vez en el Media Pool (p. 420); CSV o ALE, emparejado automático (p. 434).
- EBUCore, Tech 3293 v. 1.10 (abril 2020): §2.1 descriptivos y técnicos/estructurales, extensión del Dublin Core; «Dublin Core for media». Archivos, intercambio y producción (p. 3); creación, gestión y preservación (p. 7); interoperar con Europeana (p. 3).
- «Minimum requirement» (p. 7); no solo archivos (p. 7). §2.1 «living specification»: no se afirma última. SMPTE RP 210 retirado.
- Descriptivos: título, descripción, lugar, personas, palabras clave, derechos. Técnicos: formato, códec, resolución, cadencia, audio, duración, código de tiempo.
- Elemento gráfico (oficio): descriptivos = título, programa, tipo, autor, fecha, keywords, derechos, versión; técnicos = resolución, cadencia, duración, códec, espacio de color, alfa, programa y versión.
- Graphic Hub («Overview», «General Database Information»): base con Scenes, Geometries, Images, Materials, Fonts; Graphic Hub en marcha; local (un usuario) o multiusuario. Propiedades y UUID, idéntico en todas las carpetas. Hasta 20 keywords por fichero, criterio de búsqueda. UUID ~ UMID.
- MAM (oficio): ingesta con quién lo trae, de qué es, derechos. Funciones: catálogo, versiones, baja resolución, ciclo de vida, permisos. DAM general (fotos, documentos, audio); MAM audiovisual (código de tiempo, subclips, versiones de montaje, derechos por ventana). Fijos a DAM; animados y cabeceras a MAM; escenas de directo a su base.
- Nombres, Avid: 1) User's Guide 1999, p. 41: no usar / \ : * ? " < > | en proyectos, bins y usuarios; «Use Windows® compatible File Names». 2) pp. 126-127: una convención de mayúsculas (TAPE, Tape, tape = tres cintas). 3) p. 127: esquema previo. 4) p. 127: controladores truncan a seis caracteres.
- Sin convención de CSRTV. Propuesta (oficio): nombre = escaleta; fecha año-mes-día, programa, pieza, versión; sin espacios ni tildes; versión al final (v01 o destino), nunca «final»; no renombrar el origen. Elemento: programa, tipo, variante (formato, alfa, idioma), versión. Carpetas iguales: proyecto, medios, elementos, fuentes, salidas, documentación.
- UMID, SMPTE ST 377-1:2019 (MXF): Package ID solo Basic UMID de 32 bytes (o 32 bytes cero para terminar cadena); extendido 64 = básico + 32 de metadatos. ST 330 (ST 377-1 remite a 2011); estructura interna no leída. El nombre cambia; el identificador no.
- Versiones, Tech 3293, 3.5 (pp. 18-19): más corta, otra lengua, con o sin subtítulos, otro soporte; relaciones hasVersion, hasSource. Oficio: piezas ligadas; la original no se sobrescribe.

## 3. Reutilización

- Oficio: marca, plazo, coste. Por referencia (cambian todos: peligroso en lo emitido); por copia (marca desfasada).
- Graphic Hub, «General Database Information»: ficheros enlazados; cada uno sabe su carpeta, qué usa y quién lo usa. Borrar en carpeta quita solo el folder-link; sigue hasta quitarlos todos. Instancia única. Suma por fichero para hallar duplicados (algoritmo no dado).
- «Data Locking», tres: session lock (automático al abrir en Viz Artist; se quita al cerrar o desconectar; lo quita el usuario o el administrador; keyhole); check out (cualquier fichero; hasta check in o administrador; stop). Solo quien bloquea guarda.
- Access rights: lectura/escritura para User, Group, World. Viz Artist 3.3.x no los maneja.
- Power Bins, cap. 17, p. 392: medios para todos los proyectos (un usuario) o los del usuario (multiusuario): stock video, efectos, stills, claquetas de la casa, gráficos y animaciones de cadena. .drb (p. 390): metadatos, In/Out, timelines y clips, sin medios; en otro equipo, quizá reenlazar. Ocultos: menú de 3 puntos del Media Pool, Show Power Bins (p. 390).
- Plantillas (tema 9). Fusion, cap. 67, pp. 1480-1484: macro en carpeta de plantillas de títulos; Macro Editor elige los parámetros editables (p. 1483); salir y reabrir Resolve tras guardar (p. 1483).
- Premiere: .mogrt (Premiere o After Effects); títulos, lower thirds y botones; panel Graphics Templates; carpeta local, Creative Cloud o Adobe Stock; instalar: My Templates, varias arrastrando; en biblioteca de Creative Cloud no hay que instalar.
- Oficio: plantilla común, una actualización; copiada a mano, queda en su versión. Archivar con versión, fecha y lista de lo editable.
- Avid 1999, p. 73: guardar estructura de carpetas «as a template for future productions». Resolve, cap. 3, p. 82: project libraries; por año, programa o cliente («no hard and fast rule»); local, de red (varias estaciones en el mismo edificio), nube (Blackmagic Cloud).
- Copias automáticas (pp. 89-93): Live Save (incremental; por defecto, recomendado, p. 90); Project Backups (esquema GFS abuelo-padre-hijo; sin stills ni LUTs; proyectos independientes; pp. 90-91); Timeline Backups (timeline nuevo con «Backup»; p. 92).
- Por defecto cada 10 minutos, seis en la última hora (pp. 90 y 93); carpeta «ProjectBackup», cambiable (p. 91). Copias horarias y diarias: ocho y cinco (pp. 90-91), dos y dos (p. 93): el manual discrepa. No son el archivo (oficio).
- Otra versión, Avid (base de conocimiento, act. 11-08-2023), 5: 1) compatibilidad de formatos, funciones y ajustes; 2) complementos de terceros y versiones; 3) limitar efectos; 4) acceso a todos los medios (locales, transcodificaciones, enlazados, plantillas propias); 5) backup antes de migrar. Solo cortes: «nearly identical between versions». Más: fuentes, marca vigente.
- Libro de estilo (RTVA, 1.ª ed., marzo 2004), 9.9.1 (p. 166): rotular «Archivo» todo el tiempo en pantalla, con margen para leerlo. Salvedad: cap. 9, 9.9 «Material objetable», reportajes de delincuencia, malos tratos, asuntos judiciales; rotular siempre = costumbre de oficio. El rótulo, plantilla.
- Derechos (oficio): archivo no es licencia (uso, plazo, soporte, puestos); van en el catálogo.

## Aplicación práctica: una cabecera de la temporada pasada a la siguiente

- Supuesto (oficio): cabecera con otros colores, vertical, rótulos nuevos.
- Cierre: Archive (.dra) + fuentes, lista de complementos, pieza emitida. Tres copias, dos soportes, una fuera, suma e informe.
- Catálogo: título, programa, temporada, tipo, autor, fecha, versión, formatos, alfa, derechos, keywords comunes.
- Logo y claquetas en Power Bin (.drb sin medios: almacenamiento común o reenlazar).
- Nueva temporada: copiar .dra al volumen de trabajo, Restore, abrir como copia; comprobar versión, complementos, fuentes, medios.
- Versiones ligadas a la original. Rótulos: plantilla común.
- Errores: sin medios o fuentes; tres «final»; logo antiguo; imagen fuera de licencia; una copia en el disco de trabajo; borrado en una carpeta de Graphic Hub que sigue en otras.

## Lo que este tema no da

- No constan de CSRTV: sistema, MAM, campos, vocabulario, nombres, plazos, documentación compartida, programas ni sistema de directo.
- Adobe (reunir y archivar proyectos): ayuda no leída (rechazo del servidor, también 29-09-2026). Graphic Hub: formato de archivos y procedimientos de duplicados, metadatos, sustitución, no leídos.
- No comprobados: LTO-10 nativa; estructura del UMID (ST 330); EBUCore posterior a 1.10.
- Remisiones: temas 9 (plantillas), 2, 8, 7, 11, 17.
