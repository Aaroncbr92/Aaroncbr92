# Tema 8 del específico de Operador/a Montador/a de Vídeo · Ingesta, digitalización, transferencia, verificación, copias de seguridad, metadatos y archivo

**Siglas**: RTVA; CSRTV; EBU (EBUCore); CCSDS (OAIS: SIP, AIP, DIP, PDI); MXF (UMID); IETF (RFC 9043 FFV1, RFC 9559 Matroska); MAM/DAM; NAS/SAN; RAID; LTO/LTFS; FTP/FTPES; MD5, SHA-256/512, CRC32, XXHASH64; XMP (ISO 16684-1); INCIBE.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; se lee el tema entero antes del examen.

<!-- indice -->
<!-- /indice -->

## 1. Ingesta

- Convenio RTVA, anexo III, ficha 5212206 — objeto: grabación, reproducción, manipulación, edición y postproducción; tareas: configurar sistemas y preparar materiales, recibir/enviar enlaces, compactar para archivo, repicar cintas, control técnico de calidad.
- Oficio — ingesta = meter material en el sistema, con metadatos, comprobación y a veces conversión.
- Oficio — tres formas: de fichero, en directo (*crash record*), programada; tres orígenes: señal, soporte (tarjeta/disco), fichero por red. La de directo es la crítica: no se repite, se graba por partida doble.
- Oficio — flujo: ingesta → gestión → edición → emisión; el archivo atraviesa las cuatro; se busca por datos descriptivos, no por nombre de fichero.
- DPC, Digital Preservation Handbook — bloquear la tarjeta (write-blocker) antes de leerla; salvedad: no existe para todo soporte, algunas casas lo ven innecesario; «Check fixity on all ingests», «Virus-check high risk content» (nivel 2 de 4).
- Oficio — copiar la tarjeta entera, con su estructura de carpetas, no sólo el vídeo. Sony Z200 Help Guide, p. 161 — *proxy* en carpeta separada (/PRIVATE/M4ROOT/SUB); p. 98 — clips por relevo no se reproducen sin cortes.
- Oficio — pasos: proteger, copiar entera, comprobar, revisar (clips, partidos, sin sonido), anotar y entregar; sólo después se formatea la tarjeta.
- Adobe, ayuda Premiere (7-1-2026) — ingerir = copiar/transcodificar del origen al almacenamiento del proyecto; verifica sin corrupción (algoritmo no dicho); conserva calidad máxima y optimiza para editar; se combina con *proxies*.
- Resolve 21, cap. 17, p. 373 — *Clone Tool* en la página *Media*, antes de añadir al *Media Pool*; el manual lo propone, no lo impone.
- Oficio — ingestar ≠ importar: importar sólo enlaza (si se retira el soporte se pierde el clip); se copia antes de importar.

## 2. Digitalización

- Oficio — digitalizar = convertir en fichero un material en soporte no fichero (cinta), en tiempo real; si es analógica, conversión A/D (muestreo y cuantificación, tema 2).
- Convenio — tarea «repicar cintas orientadas a producción, emisión y comercialización»; el convenio no define «repicar».
- Resolve 21, cap. 24, p. 558-559 — hace falta un dispositivo de entrada de vídeo gobernable y un magnetoscopio con control de dispositivo; en captura, el transporte gobierna el VTR y el panel de audio se sustituye por metadatos de captura, puestos antes de capturar.
- Resolve 21, p. 561 — se ajusta: vídeo+audio o sólo vídeo; formato (DPX o QuickTime); códec (ProRes, YUV 8/10 bits, RGB 10 bits, DNxHD); carpeta destino con caudal suficiente; nombre de cinta (fichero y/o cabecera); prefijo; pistas de audio (2-16); mínimo (p. 562): «Video Capture and Playback», «Capture Clips Saved to», «Apply Reel Name to».
- Resolve 21, p. 562-563 — tres métodos: *Capture Now* (rápido, un tramo); registrar y capturar un clip (entrada/salida marcadas, metadatos, *Capture Clip*); registrar varios y capturar por lotes (*Log Clip*, eficiencia, orden por cinta).
- Resolve 21, p. 563-564 — *Batch Capture Via EDL*: crea clips *offline* por evento de la EDL; no duplica si ya hay clip con mismo nombre de cinta y TC de inicio.
- Oficio — nombre de cinta + TC de inicio/fin identifican el clip; sin nombre único falla la captura por lotes y el reconformado. Resolve 21, p. 562 — en *Capture Now* nombra el clip con el TC pasado a cuadros según la cadencia (ej. 00086400.dpx = TC 01:00:00:00 a 24 im/s).
- Oficio — se revisa: estado de la cinta y protección; magnetoscopio limpio y con control remoto (sin control, sólo *Capture Now*); niveles durante la captura (tema 2); duración y pistas al terminar.

## 3. Transferencia

- Oficio — transferir = mover material de un sitio a otro; como señal (enlace, ingesta en directo) o como fichero (por red, se comprueba al llegar); la ficha nombra «recibir y enviar enlaces».
- Oficio — se envía primero el *proxy*, que pesa poco. Sony Z200, p. 196 — FTP no cifra contenido, usuario ni contraseña; usar FTPES (FTPS, cifrado explícito).
- Oficio — quien recibe comprueba que llegó entero antes de avisar; quien envía no borra hasta confirmación. Cálculo propio — tiempo = tamaño/velocidad, cuidando bits/bytes (1 B = 8 b); 12 GB a 100 Mb/s = 960 s (16 min mínimo).
- Oficio — local (discos de la estación, una sala); NAS (sirve ficheros por red, trabajo compartido ligero/archivo); SAN (red de bloques, edición en tiempo real); NAS pide fichero, SAN pide bloque; bajo los tres hay un RAID.
- Oficio — tres redes de redacción: de señal (tiempo real), de producción (ficheros/control), ofimática (expuesta a internet, separada por seguridad); material externo no pasa a producción sin procedimiento.

## 4. Verificación

- Oficio — dos sentidos: de datos (copia idéntica) y de contenido; ficha: «control técnico de calidad y corrección».
- DPC, Fixity and checksums — fijeza = garantía de que el fichero no ha cambiado; el *checksum* es «huella digital», cambia si cambia el fichero, no dice dónde; sirve para la cadena de custodia; MD5 basta para pérdida/daño accidental; con varias copias, la suma señala cuál sustituir (*data scrubbing*).
- Resolve 21, cap. 17, p. 373-374 — seis opciones del *Clone Tool*, velocidad frente a seguridad: *None* (sin verificación); *File Size* (rápido, mínima resistencia a colisión); CRC32 (más rápido que MD5, menos seguro); MD5 (por defecto, 128 bits, equilibrio); SHA-256/512 (más lento, más seguro; 512 aún más resistente); XXHASH64 (el más rápido, buena protección, útil con terabytes); informe de *checksum* en la raíz de cada destino, se guarda con la copia.
- Oficio — comparar sólo tamaño no verifica; la suma se calcula sobre original y copia, sirve años después en archivo; dice que cambió, no dónde (se repara con otra copia buena).
- CCSDS 650.0-M-3, § 4.2.3.3/4.2.3.4 — QA en la ingesta del SIP con CRC/*checksum* o registros de sistema; comprobación de errores en el AIP durante el almacenamiento y las transferencias internas.
- Oficio — verificación de contenido: clips completos, pistas esperadas; formato/resolución/cadencia/TC coinciden (tema 4); se ve y oye bien; procedencia y derechos (tema 10).
- Libro de estilo CSRTV, 5.3.3, p. 82 — revisar la grabación en el propio lugar.

## 5. Copias de seguridad

- Oficio — hasta copiar, el material existe en un solo sitio; es protección de la jornada, no trámite de archivo. Resolve 21, cap. 17, p. 373 — clonar el original a volúmenes de respaldo antes de añadir al proyecto; considerar copia fuera de la sala.
- INCIBE (29-09-2021) — regla 3-2-1: tres copias, en dos dispositivos distintos, una en lugar diferente.
- Oficio — traducción a la sala: original hasta dos copias comprobadas; una en almacenamiento de trabajo; otra en soporte/sitio distinto; el *Clone Tool* admite varios destinos a la vez. Resolve 21, cap. 18, p. 434 — metadatos exportables a CSV o ALE (Avid), reimportables.
- Oficio — se guardan también los informes de *checksum* y las listas de entrega: demuestran qué se copió y cuándo.
- Oficio — el RAID no es copia de seguridad: RAID 0, sin redundancia (velocidad/capacidad total, ninguna seguridad); RAID 1, espejo (dos discos, aguanta uno); RAID 5, paridad distribuida (mín. 3 discos, aguanta uno, reconstrucción lenta); RAID 6, doble paridad (aguanta dos); RAID 10, espejos en *striping* (mín. 4 discos, mitad capacidad).
- Oficio — RAID 5 con tres discos: capacidad útil dos de tres; durante la reconstrucción, sin protección. El RAID protege del fallo de disco, no de borrado, fichero corrupto replicado, robo o incendio.

## 6. Metadatos

- Oficio — metadatos = datos sobre el material (fecha, cámara, TC, nombre, bueno/malo); los pone la cámara, los configura antes el operador, o los anota mientras graba.
- EBU Tech 3293, p. 7 — «If you can't find it, you don't have it!».
- Oficio — se pierden si se copia sólo el vídeo y no la tarjeta entera; los contenedores profesionales (MXF) los llevan dentro. Sony Z200, p. 252 — [Update Media] actualiza el fichero de gestión de la tarjeta.
- Oficio — el nombre de fichero se repite; el UMID de MXF, identificador único del paquete, no.
- Resolve 21, cap. 18, p. 417-420 — metadatos entran solos (ej. BWF con escena/toma/canal) o se escriben en el editor (descripción, *shot*, *scene*, *take*, palabras clave de lista); permiten *Smart Bins*/*Smart Filters*; edición por lotes; exportación a CSV/ALE con reenlace automático.
- Adobe, documentación XMP — embebe metadatos en el propio fichero; norma ISO 16684-1 desde 2012; extensible. Espacio Dublin Core (`dc`), propiedades comunes; espacio de medios dinámicos (`xmpDM`): *tapeName*, *altTapeName* (desde Premiere), *startTimecode*, *good*, *logComment*, *scene*, *shotName*.
- Oficio — lo escrito en XMP viaja con el fichero a otro proyecto/programa; lo anotado sólo en el proyecto se queda ahí (qué campos de Premiere van a XMP no consta, ayuda no leída).
- Oficio — tres datos deciden si se encuentra: quién lo trae, de qué es, qué derechos tiene; sin ellos, perdido dentro del sistema.
- Oficio — MAM, cinco funciones: catálogo, versiones, baja resolución, ciclo de vida, permisos; DAM es el término general, MAM el especializado en audiovisual (TC, subclips, ventanas de explotación); sistema de CSRTV, no consta publicado.
- EBU Tech 3293, § 2.1, p. 3/7 — EBUCore, extensión del Dublin Core («the Dublin Core for media»); describe audio/vídeo para archivo, intercambio y producción, no limitado a archivo; v. 1.10 compatible con IMF; especificación viva; RP 210 de SMPTE, retirada.
- Oficio — metadatos descriptivos (título, descripción, lugar, personas, palabras clave, derechos: redacción/montador/documentación) frente a técnicos (formato, códec, resolución, cadencia, TC: cámara y sistema solos).

## 7. Archivo

- Convenio — tarea «compactar para el archivo de material audiovisual»; catalogación es de documentación (tema 9); «compactar» no lo define el convenio; oficio: reducir a lo que merece guardarse, identificado, completo y comprobado.
- Oficio — producción (en uso, inmediato, caro) frente a archivo (conservación, diferido/cinta, barato); lo que queda en producción no está archivado; lo archivado no se monta directo, se recupera antes.
- CCSDS 650.0-M-3, § 1.1 — OAIS: sistema con personal, hardware, software y procesos que preserva información y la hace accesible a la comunidad designada; «abierto» = desarrollado en foros abiertos, no acceso sin restricción; abarca ingesta, almacenamiento, gestión de datos, acceso, difusión y migración a nuevos soportes.
- CCSDS, § 1.6.2 — SIP (de entrega, del productor al OAIS: pieza + bruto seleccionado + datos), AIP (lo conservado, con la PDI), DIP (lo entregado al usuario); PDI: procedencia, contexto, referencia, fijeza, derechos de acceso.
- CCSDS, § 4.2.2/4.2.3.4 — seis entidades funcionales: ingesta, almacenamiento de archivo, gestión de datos, administración, planificación de la conservación, acceso; *Replace Media* (migración de soporte, sin alterar contenido/PDI); *Disaster Recovery* (copia en sitio separado).
- lto.org (25-09-2026) — LTO: cinta abierta, escalable, de varios fabricantes; generación vigente, la 10.ª; capacidad hasta 100 TB comprimidos, cartuchos de 30/40 TB (no consta si nativos); velocidad hasta 1200 MB/s (compresión 2,5:1); LTO-10 no lee generaciones anteriores (hasta la 7.ª: escribe una atrás, lee dos atrás; 8.ª-9.ª: una atrás); ventajas: coste bajo, sin consumo en reposo, décadas de duración, fuera de red; desventaja: acceso secuencial y lento. LTFS presenta la cinta como disco, con dos particiones (índice y datos); el acceso sigue secuencial.
- IETF RFC 9043 — FFV1: códec de vídeo sin pérdidas intracuadro, útil para preservación; v. 3 añade CRC embebido; RFC 9559 define el contenedor Matroska.
- Library of Congress, fdd000341/fdd000206 — FFV1 en Matroska, formato preferido; IASA-TC 06 recomienda Matroska+FFV1 para vídeo digitalizado; JPEG 2000 sin pérdidas en MXF OP1a (SMPTE RDD 48), típico al formatear en la propia ingesta, para reducir tamaño frente a sin comprimir; transporte fijado por SMPTE ST 422 (no leída).
- Oficio — existe la vía sin comprimir, con ficheros mayores; el máster de conservación es distinto del fichero de trabajo; formato de CSRTV, no consta publicado.
- Libro de estilo CSRTV, 9.9.1, p. 166 — rotular «Archivo» mientras la imagen esté en pantalla, con margen de lectura; pasaje del capítulo de asuntos comprometidos (sucesos); rotular siempre fuera de esos casos es oficio, no regla escrita ahí.
