# Tema 8 del específico de Operador/a Montador/a de Vídeo · Ingesta, digitalización, transferencia, verificación, copias de seguridad, metadatos y archivo

**Siglas**: RTVA; CSRTV; EBU; SMPTE; CCSDS; OAIS (SIP, AIP, DIP, PDI); ISO; MXF (OP-Atom); UMID; AAF; EDL; ALE; CSV; DPX; MOV; YUV; RGB; TC; VTR; SD; SSD; RAID; NAS; SAN; LTO; LTFS; USB; SDI; IP; BWF; FTP; FTPES/FTPS; MAM; DAM; NRCS; CRC; MD5; SHA-256/512; XXHASH64; INCIBE; Mb/s; MB/s; GB; TB; IMF; ISBN.

Esqueleto para repasar, no resumen: cada línea remite al tema; sin el tema no se entiende.

<!-- indice -->
<!-- /indice -->

## Ficha del puesto

- (X Convenio, anexo III, ficha 5212206, p.190) Objeto: «Realizar todo tipo de procesos de grabación, reproducción, manipulación, edición y postproducción... en coordinación con otras áreas.» Tareas del tema: configurar sistemas y preparar materiales (ingesta/verificación/metadatos); recibir y enviar enlaces (ingesta directo/transferencia); compactar para archivo; repicar cintas (digitalización/copia); control técnico de calidad (temas 2 y 7).
- (oficio) Ficha de 2014, habla de cintas; convenio no define «compactar»/«repicar». Reparto entre montador/archivo/documentación: no consta.

## 1. Ingesta

- (oficio) Meter material en el sistema; 3 formas: de fichero, en directo (*crash record*, irrepetible → doble grabación), programada. Por origen: señal, soporte, fichero.
- (oficio) Flujo redacción: ingesta→gestión→edición→emisión; archivo atraviesa las 4. Datos descriptivos, no nombre de fichero. Reparto CSRTV: no consta.
- (oficio, DPC/Adobe/Sony) Tarjeta: 1) lock, bloqueador de escritura (DPC nivel 2: «use write-blockers»; salvedad: no para todo soporte). 2) copiar entera con estructura (Z200: proxy en /PRIVATE/M4ROOT/SUB; P2: audio OP-Atom aparte). 3) comprobar (checksum o tamaño+apertura; DPC: «check fixity on all ingests»). 4) revisar clips partidos (relevo, Z200 no reproduce sin cortes) y sonido. 5) anotar y entregar; sólo entonces formatear en cámara.
- (Adobe, Premiere help 7-1-2026) Ingesta=copiar/transcodificar a almacenamiento del proyecto; verifica sin decir algoritmo; combinable con proxies. (Blackmagic cap.17 p.373) *Clone Tool*, página Media, checksum a elegir, antes de Media Pool.
- (oficio) Ingestar ≠ importar (enlaza, se rompe si se retira soporte); reenlace: tema 3.

## 2. Digitalización

- (oficio) Convertir en fichero una cinta (analógica: muestreo+cuantificación, tema 2). Tiempo real (1h cinta=1h captura), al revés que tarjeta. Ficha: «repicar cintas»; fondo digitalizado: no consta.
- (Resolve cap.24, pp.558-564) Tarjeta/caja de entrada + VTR gobernable. Modo captura: transporte controla VTR; panel de metadatos sustituye a audio, antes de capturar. Se fija: audio+vídeo o sólo vídeo; formato fichero (DPX/QuickTime); códec (ProRes, YUV 422, RGB, DNxHD); carpeta con caudal suficiente; nombre de cinta (fichero y/o cabecera); prefijo; pistas audio 2-16.
- (Resolve p.562-563) 3 métodos: *Capture Now* (tramo rápido); *Capture Clip* (entrada/salida+metadatos, 1 clip); *Log Clip*+lotes (varios tramos, eficiencia, orden por cinta). + *Batch Capture Via EDL* (p.563-564): recrea tramos de una EDL; no duplica si ya existe mismo nombre+TC inicio.
- (oficio) Clip se reconoce por nombre de cinta+TC entrada/salida; sin nombre único falla lotes y reconformado. (Resolve p.562) Captura inmediata nombra por TC en cuadros según cadencia (00086400.dpx = TC 01:00:00:00). Reconformado/*Redigitize*: tema 3.
- (oficio) Revisar al digitalizar: cinta (estado, etiqueta, protección); VTR (limpio, remoto — sin él sólo Capture Now); señal (niveles, tema 2; cortes/congelados); fichero final (duración, pistas, entrada/salida).

## 3. Transferencia

- (oficio) Mover material; 2 maneras: señal/enlace (tiempo real, no grabado se pierde; tema 14) o fichero (por red, se comprueba al llegar). Ficha: «recibir y enviar enlaces».
- (oficio) Envío desde el lugar: primero proxy, luego original. (Z200 p.196) FTP sin cifrar; usar FTPES/FTPS. Comprobar fichero completo antes de avisar disponibilidad; no borrar origen hasta confirmar.
- (cálculo) Tiempo=tamaño/velocidad, bits↔bytes (×8). Ej.: 12 GB a 100 Mb/s = 96.000 Mb ÷100 = 960 s = 16 min mínimo.
- (oficio) Almacenamiento: local (una sala); NAS (fichero por red, compartido ligero/archivo); SAN (bloques de disco, edición compartida tiempo real). Bajo los tres hay RAID (ver 5). Qué usa CSRTV: no consta.
- (oficio) 3 redes: señal (tiempo real, caudal/retardo); producción (ficheros, ráfagas); ofimática (expuesta a internet, separada). Fichero externo (USB, descarga) no va directo a producción sin procedimiento.

## 4. Verificación

- (oficio) 2 sentidos: datos (copia idéntica) y contenido (material usable).
- (DPC, «Fixity and checksums») Fijeza=fichero no ha cambiado; checksum=huella digital, detecta cambio pero no dónde. Cadena de custodia. Algoritmos de fuerza creciente (MD5, SHA-256); MD5 basta para pérdida/daño accidental, rápido y soportado. Con varias copias, checksum dice cuál usar de recambio (*data scrubbing*).
- (Resolve cap.17 pp.373-374) 6 opciones *Clone Tool*, velocidad↔seguridad: None (sin verificación); File Size (rápido, mínima resistencia a colisión); CRC32 (más rápido que MD5, menos seguro); MD5 (por defecto, 128 bits, equilibrio; colisión improbable en flujo audiovisual); SHA256/512 (más lento, más seguro; 512>256); XXHASH64 (más rápido, buena protección, ideal en terabytes). Informe de checksum se guarda en cada destino.
- (oficio, 3 reglas) Tamaño solo no verifica; checksum en origen y cada copia, se compara (sirve años después en archivo); dice que cambió, no dónde (reparación desde otra copia).
- (CCSDS 650.0-M-3 §4.2.3.3) Ingesta OAIS valida transferencia del SIP con CRC/checksums o logs. (§4.2.3.4) *Error Checking*: garantía estadística de que el AIP no se corrompe en almacenamiento/transferencia interna.
- (oficio) Verificación de contenido: completo (clips/pistas), es lo que dice ser (formato/TC, tema 4; corresponde al encargo), se ve/oye bien (niveles, tema 2; ficha: «control técnico de calidad»), se puede usar (derechos, tema 10). (Libro de Estilo 5.3.3 p.82) «Revisar la grabación en el mismo lugar... comprobar imagen y sonido.»

## 5. Copias de seguridad

- (Sony, Help Guide ILCE-1) «Be sure to back up the data for protection.» Protección de la jornada, no trámite de archivo (oficio). (Resolve cap.17 p.373) Clonar el original a backup antes de añadir al proyecto, y a backup externo.
- (INCIBE, 29-09-2021) Regla 3-2-1: 3 copias, 2 dispositivos distintos, 1 en lugar diferente. (oficio) En sala: original hasta 2 copias comprobadas; 1 copia en almacenamiento de trabajo; 1 en soporte/sitio distinto. (Resolve p.373) *Clone Tool* hace varios destinos a la vez.
- (oficio) Además del material: proyecto (decisiones, se pierde aparte; *Attic* Avid tema 15); metadatos exportados (Resolve cap.18 p.434: .csv o .ale, reimportables); informes de checksum y listas de entrega (prueba de qué se copió y cuándo).
- (oficio) RAID no es copia de seguridad: RAID0 *striping* sin redundancia (velocidad+capacidad, cero seguridad); RAID1 *mirroring* (2 discos, mitad capacidad, aguanta 1); RAID5 *striping*+paridad distribuida (mín. 3, aguanta 1, reconstrucción lenta); RAID6 doble paridad (aguanta 2); RAID10 espejos en striping (mitad capacidad, 4 discos). El número no es el nº de discos. Protege de fallo de disco, no de borrado/corrupción replicada/robo/incendio; RAID0 no protege nada.
- (oficio) RAID5 con 3 discos: capacidad útil 2/3; pierde 1 disco; lectura alta, escritura menor (cálculo paridad). Mnemotecnia: RAID0=cero seguridad, RAID1=disco copiado. Durante reconstrucción RAID5 sin protección: si cae otro disco, se pierde todo.

## 6. Metadatos

- (oficio) Datos sobre el material (cuándo, cámara, TC, nombre, bueno/malo). Cámara sola / configurado antes (nombre, TC, bits usuario) / operador en vivo (marcas). (EBUCore p.7) «If you can't find it, you don't have it!»
- (oficio) Van con el material si se copia entero; contenedores profesionales los llevan dentro (MXF); cámaras guardan ficheros de gestión y proxy aparte (Z200: [Update Media] actualiza ficheros de gestión, p.252). UMID (identificador único MXF, tema 15) no se cambia, a diferencia del nombre de fichero. TC: temas 2 y 15.
- (Resolve cap.18 p.417-420,434) «Once your metadata house is in order...» usable en Cut/Edit/Color/Fairlight. Llegan solos (BWF: escena/toma/canales) o se escriben en editor (Description, Shot, Scene, Take, keywords, de lista para consistencia). Para Smart Bins/Smart Filters; varios clips a la vez; exporta/importa CSV o ALE.
- (Adobe XMP docs) XMP=metadatos embebidos en el fichero, norma ISO 16684-1 desde 2012, extensible. Espacios: Dublin Core (`dc`, base también de EBUCore) y medios dinámicos (`xmpDM`): `tapeName`, `altTapeName` (vía Premiere), `startTimecode`, `good`, `logComment`, `scene`/`shotName`. XMP viaja con el fichero; proyecto se queda. Campos de Premiere→XMP: no consta (ayuda no leída).
- (oficio) 3 datos clave en ingesta: quién trae, de qué es, qué derechos. MAM, 5 funciones: catálogo, versiones, baja resolución, ciclo de vida, permisos. DAM=general; MAM=audiovisual (TC, subclips, versiones, derechos). Sistema/campos CSRTV: no consta.
- (EBU Tech 3293 v1.10, §2.1, pp.3,7) EBUCore=metadatos descriptivos/técnicos, extensión Dublin Core; «the Dublin Core for media». Archivos, intercambio, producción, no sólo archivo; compatible IMF (§2.3, tema 4). Viva/mantenida; SMPTE RP 210: retirada.
- (oficio, EBUCore) Descriptivos (título, descripción, lugar, personas, keywords, derechos — redacción/montador/documentación) vs. técnicos (formato, códec, resolución, cadencia, pistas, duración, TC — cámara/sistema solos).

## 7. Archivo

- (Convenio, ficha) «Compactar para el archivo»; catalogación=documentación (tema 9). Compactar=oficio: reducir a lo que merece guardarse (emitido+bruto útil, sin duplicados/pruebas/intermedios), identificado, completo, comprobado. Qué conserva CSRTV, formato, plazos: no consta.
- (oficio) 2 almacenamientos: producción (en uso, acceso inmediato, red de bloques, coste alto) vs. archivo (conservado, acceso diferido/cinta, coste bajo). Lo no archivado no está protegido; lo archivado no se monta directo, se recupera antes.
- (CCSDS 650.0-M-3 §1.1) OAIS: sistema con hardware/software/información/procedimientos que acepta preservar información para una comunidad designada (en TV: redactores/montadores/documentalistas). «Open»=desarrollado en foros abiertos, no acceso sin restricción (§1.1). Largo plazo=periodo indefinido con cambio de tecnología (§1.6.2). Abarca ingest, archival storage, data management, access, dissemination, migración (§1.1).
- (§1.6.2) 3 paquetes: SIP (Productor→OAIS, para construir AIP) = lo que la sala entrega (pieza+bruto+datos); AIP (Contenido+PDI, preservado) = lo que archivo guarda; DIP (derivado de AIP, a Consumidor) = copia que archivo devuelve para montar.
- (§1.6.2) PDI: procedencia (historia, origen, custodia), contexto, referencia (identificador, ej. ISBN), fijeza (mecanismos de no-alteración = checksum guardado), derechos de acceso.
- (§4.2.2-4.2.3.4) 6 entidades funcionales: Ingest, Archival Storage, Data Management, Administration, Preservation Planning, Access. Dentro de Archival Storage: Replace Media (renovar soportes/migración, sin alterar contenido+PDI) y Disaster Recovery (duplicado en instalación separada = regla 3-2-1).
- (lto.org, «LTO Technology Roadmap», 25-09-2026) LTO=cinta magnética alta capacidad, escalable, regrabable, formato abierto multifabricante. Generación vigente: 10.ª. Capacidad LTO-10: hasta 100 TB comprimida; cartuchos 30 TB/40 TB (no se dice si nativos; vídeo ya comprimido → cifra útil más cerca de nativa). Velocidad hasta 1200 MB/s (asumiendo compresión 2,5:1). Compatibilidad atrás: hasta 7.ª gen escribe 1 atrás/lee 2 atrás; 8.ª-9.ª escribe/lee 1 atrás; 10.ª sin compatibilidad atrás (cabezal rediseñado, sin inicialización). Ventajas oficio: coste/TB bajo, sin consumo en reposo, dura décadas, fuera de red; desventaja: acceso secuencial y lento, no es almacenamiento de trabajo.
- (lto.org, «Linear Tape File System», 25-09-2026) LTFS=lee LTO como disco con ficheros/carpetas, incluida desde LTO-5. Partición de índice + partición de datos; interfaz simple, arrastrar y soltar. Sigue siendo secuencial: LTFS localiza, la unidad tiene que llegar.
- (Libro de Estilo 9.9.1 p.166) «En rotulación debe hacerse constar claramente que es material de 'Archivo' durante todo el tiempo en que la imagen permanezca en pantalla...» — norma escrita para reportajes de sucesos/delincuencia/judicial (cap.9.9); rotular siempre fuera de eso es costumbre de oficio, no regla del pasaje. Derechos de archivo/terceros: tema 10.

## Aplicación práctica: del material que llega al que se archiva

- (oficio, caso: 2 tarjetas + cinta archivo 20 años + clip de corresponsal) Tarjetas: bloquear, clonar enteras (estructura) a 2 destinos con MD5/XXHASH64, guardar informe de sumas. Revisión: clips, pistas, formato, cadencia, TC. No devolver a formatear hasta 2 copias comprobadas. Cinta: captura registrada, nombre único, entradas/salidas, metadatos antes, por lotes. Clip corresponsal: comprobar llegada íntegra antes de confirmar; avisar si FTP sin cifrar. Metadatos: descripción/lugar/personas/keywords/origen/derechos. Montaje: desde almacenamiento de trabajo, no desde tarjeta/disco externo; rotular archivo. Cierre: compactar (emitido+bruto útil) con metadatos y sumas al procedimiento de archivo; limpiar almacenamiento de trabajo sólo tras confirmación (SIP completo y comprobado).

## Lo que este tema no da, y dónde está

- Sistema de ingesta/almacenamiento/MAM/archivo de CSRTV; quién ingesta; qué se conserva del bruto, formato, plazos; procedimiento de material externo: no consta.
- Sentido actual de «compactar»/«repicar»: convenio no lo define.
- Capacidad nativa LTO-10, campos de Premiere que van a XMP, edición ISO 14721 del OAIS, versión EBUCore posterior a 1.10, algoritmo de Premiere al ingestar: no confirmados/no leídos.
- Proxies/reenlace/*Redigitize*: tema 3. Formatos/códecs/MXF/SDI-IP: tema 4. Señal, niveles, TC: tema 2. Control de calidad/corrección: temas 2 y 7. Reparto con documentación: tema 9. Derechos de archivo/terceros: tema 10. MAM/redacción/automatización: tema 13. Directo/enlaces: tema 14. Nomenclatura/UMID/*Attic*: tema 15.
