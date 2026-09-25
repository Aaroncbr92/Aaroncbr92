# Tema 13 del específico de Operador/a Montador/a de Vídeo · Automatización, plantillas, MAM/PAM, newsroom y flujos de producción integrados

**Siglas**: RTVA; CSRTV; RTVE; BOJA; UIT; EBU (*European Broadcasting Union*); MAM (*media asset management*); PAM (*production asset management*); DAM; NRCS (*newsroom computer system*, en MOS «NCS»); MOS (*Media Object Server Communications Protocol*); CG (*character generator*); TCP/IP; XML; API.

Esqueleto para repasar, no resumen: cada línea es un dato con su fuente delante; vuelve al tema para el desarrollo.

<!-- indice -->
<!-- /indice -->

## De dónde sale el tema

- Sin norma legal. Convenio (fichas); Libro de estilo (escaleta); Manfredi (2010, sistema de redacción en CS); mosprotocol.com; EBU Tech 3293; manuales de fabricante (Resolve, Premiere, Avid) como ejemplo, no como regla.
- MAM, PAM y *newsroom*: palabras de industria; no hay definición de UIT/EBU/SMPTE para MAM ni PAM.

## 1. Automatización

- Convenio, ficha 5212206 (p. 190): **«etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de programas y bloques publicitarios»**.
- Convenio, ficha encargado 5212204 (p. 127): **«realizar todas las operaciones necesarias previas para la posterior emisión automatizada»**. No dice qué sistema usa la casa ni qué campos lleva la base de datos.
- Oficio (RTVE): 3 piezas — escaleta de emisión (orden, viene de redacción), servidor de emisión (reproduce a su hora), automatización (ejecuta: dispara servidor, grafismo, conmutación). La emisión va separada de todo — servidores, almacenamiento y red propios, único punto donde un fallo se ve en antena.
- Oficio: sala debe dar nombre exacto de escaleta, duración real anunciada, entrega antes de hora; lo tardío no sale.
- Manual Resolve 21, cap. 8 (p. 215-217): carpetas vigiladas — Proxy Generator genera *proxy* automáticamente de lo que entra; subcarpeta «Proxy» reservada; *Start*/*Stop* en *Processing*. Cap. 8 (p. 198): *background rendering* (renders, *quick export*, *proxies*), desactivado por defecto por consumo de recursos.
- Manual Resolve, cap. 187 (p. 4185, 4215): cola de *render* en *Deliver*, varios trabajos, *Start Render*; *render* remoto entre estaciones — exige Studio en ambas, biblioteca de proyectos común, mismo material. Ayuda Premiere: cola de Media Encoder, para exportaciones largas o varias versiones.
- Manual Resolve, cap. 201 (p. 4418): *scripting* (*Workflow Integration Plugin*, JS/Python/Lua); vía de conexión de un MAM al editor.
- Oficio: no mira contenido; por eso se revisa lo automatizado al final.

## 2. Plantillas

- Oficio: plantilla = elemento/ajuste preparado que se reutiliza; 3 clases — rótulo, salida, nombre.
- Manual Resolve, cap. 56 (p. 1215): *Lower 3rd* (2 líneas, posición automática), *Text+* (estilo único para todo el texto), *Fusion Titles* (biblioteca de plantillas propias de la casa).
- Ayuda Premiere: fichero **.mogrt**, creado en Premiere o After Effects, para *titles, lower thirds, buttons*; panel *Graphics Templates*; llega de carpeta local, Creative Cloud (automática) o Adobe Stock; exportar sólo si el gráfico es de Premiere, y no con 2+ seleccionados; plantillas con datos admiten texto, color, números, fijados en After Effects.
- Manfredi (2010, p. 139-140), iNews: rótulos que inserta el periodista **«irán directamente a la emisión»**; qué rótulos van incrustados y cuáles en directo, decisión de la casa, no consta publicada.
- Manual Resolve, cap. 187 (p. 4193-4194): *preset* de exportación guarda todos los ajustes; se exporta/importa como fichero .xml entre puestos/máquinas.
- Ayuda Premiere: *preset* por defecto de Media Encoder — **«H.264 Match Source - Adaptive High Bitrate»**, salvo último ajuste usado.
- Manual Resolve, cap. 15 (p. 345-346): variables de metadatos con «%» (escena_plano_toma → «12_A_3»); campo vacío no aparece; %date/%time toman fecha/hora de salida, no de grabación.
- Oficio: el nombre que manda es el de la escaleta, no lo inventa la máquina.

## 3. MAM/PAM

- Oficio: MAM y PAM guardan, catalogan y reparten material; sin definición normalizada.
- Oficio (RTVE): 5 funciones MAM — catálogo, versiones, baja resolución, ciclo de vida, permisos.
- Oficio: DAM = término general (fotos, docs, audio); MAM = especializado en audiovisual (código de tiempo, subclips, versiones, derechos por ventana). Distinción MAM/PAM, de industria — PAM gestiona material en producción (brutos, *proxies*, secuencias en curso); MAM, material terminado y archivo.
- Avid, producto *Production Management* (leída 25-09-2026): seguimiento ingesta-archivo, multiusuario, permisos, servicios automáticos (transcodificación, archivo, restauración), almacenamiento Avid NEXIS, búsqueda por metadatos desde Media Composer/Premiere/Cloud UX.
- Oficio (RTVE): copia de baja resolución viaja por red ofimática, se ve y marca; el fichero grande no se mueve hasta el conformado. Ayuda Premiere: se crean *proxies*, se edita sobre ellos y se pasa a resolución completa cuando hace falta.
- EBU Tech 3293 (EBUCore), v1.10 abril 2020, p. 7: **«"If you can't find it, you don't have it!"»**; metadatos como **«glue between production operations»**; documentar con EBUCore es requisito mínimo.
- EBU Tech 3293, p. 8: EBUCore se define como **«the Dublin Core for media»**.
- Manual Resolve, cap. 201 (p. 4418): MAM accesible desde el editor vía *Workflow Integration Plugins* (ej. EditShare/FLOW: comentar, buscar, gestionar *proxies* sin salir de Resolve).
- Oficio: montador busca por datos, no por nombre; devuelve la pieza con metadatos completos; lo no devuelto «existe para la cabina, no para la casa».
- Oficio (RTVE): 2 almacenamientos — de producción (uso, red de bloques, coste alto, dimensiona el material vivo) y de archivo (conservación, diferido/cinta, coste bajo, dimensiona lo conservado).
- Oficio: la ingesta llena el almacenamiento; sin política de borrado/archivo escrita antes, el sistema se para solo.

## 4. Newsroom

- Oficio (RTVE): *newsroom* = redacción y su sistema (NRCS); contiene ESCALETA (piezas, duración, fuente, estado), guion, referencias al material, CRONOMETRÍA, estados, agenda/teletipos. Es la base de datos; todo cuelga de ella.
- Oficio: 3 cosas que hacen útil el sistema — cronometra en tiempo real; único sitio donde se cambia algo; habla con los demás equipos por protocolo (MOS).
- mosprotocol.com (portada): MOS = protocolo evolutivo de comunicación entre Newsroom Computer Systems (NCS) y Media Object Servers (vídeo, audio, *still stores*, CG); finalidad — integrar equipos NCS y MOS diversos. Resuelve (FAQ): comunicar sistema de marca X con servidor de marca Y.
- mosprotocol.com (FAQ): «un MOS» = dispositivo capaz de guardar objetos de medios (CG, audio, *still store*, vídeo); se supone equipo no lineal, no es requisito.
- mosprotocol.com («In General»): NCS crea/modifica/borra información editorial y *playlists*; MOS, objetos de medios y sus metadatos. 3 tipos de mensajes: *Descriptive Data* (servidor empuja datos a NCS), *Playlist Exchange* (NCS manda la lista al servidor), *Status Exchange* (estado mutuo de clips/sistema/órdenes de emisión).
- mosprotocol.com: transporte típico TCP/IP por *sockets*; texto etiquetado unicode; cada versión es superconjunto de la anterior. Vigentes: v4.0 (7-VI-2019, *Secure Web Sockets*); v2.8.5 (7-IX-2017, *Socket*); v3.8.4 (11-II-2011, *Web Services*).
- mosprotocol.com: lo desarrollan fabricantes, proveedores de software y usuarios desde Orlando 1998 (conferencia ENPS de AP); más de 150 empresas en 2021. No es norma oficial: se presentará a organismos de normalización más adelante.
- Salvedad: MOS llama NCS al sistema de redacción; industria (Avid) también dice NRCS — son lo mismo.
- Avid, *MediaCentral | Newsroom Management* (iNEWS), ejemplo de NRCS de mercado: escaletas, tiempos, cambios en directo, integrado con automatización, apuntador, grafismo, emisión (publicidad de fabricante).
- Libro de estilo, 6.1 (p. 88): **«la escaleta es el documento básico»**; hecho noticioso, formato, identificación, tiempo asignado/real, autor, procedencia, presentador, acotaciones técnicas; partes de emisión añaden vías de sonido, coleo, rótulos, observaciones, pie del texto.
- Libro de estilo, 6.1: cambio de escaleta se comunica **«inmediata y simultáneamente»** a todos los afectados. 6.1.1: **«son inadmisibles»** los cambios de nombre de un vídeo; excepción — vídeo terminado antes de escaletar, lo traslada el equipo de edición.
- Libro de estilo, 6.1.2: el redactor fija en escaleta sus textos definitivos, rótulos (orden/ubicación) y pasos de locutor; disponibles para el equipo y ediciones posteriores. No describe formato de guion ni nombra el programa informático de CSRTV.
- Manfredi (2010, p. 138): Avid instalado **«en todos los Servicios Informativos de RTVE y, en el caso de Andalucía, en Canal Sur»**; dato de 2010, no consta vigente.
- Manfredi (2010, p. 139-140): iNews = escritura de noticias con agencias, textos y escaletas de todos los informativos; periodista conoce duración y lugar de emisión al recibir la noticia. iNews Instinct (Avid, 2005): modo sencillo de edición de vídeo y guion; ajusta audio y minutado.
- No consta documento publicado: qué sistema de redacción, MAM ni servidores usa CSRTV hoy.
- Oficio (RTVE): 2 niveles de edición — ligera en puesto del redactor (baja resolución) y completa en sala del montador (alta resolución); el conformado une ambas. Edición de informativos (minutos, redactor, sencilla, prioridad tiempo) frente a postproducción (días, montador, completa, prioridad calidad).
- Oficio: la edición debe estar donde está el redactor (copia de trabajo evita mover material de alta tasa); se edita mientras se ingesta. El sistema de redacción es la pieza más integrada de la casa; se elige por sus INTERFACES.

## 5. Flujos de producción integrados

- Oficio (RTVE): flujo integrado = todas las etapas sobre el mismo material y datos, sin copias sueltas ni pasos a mano.
- Oficio: 4 etapas — ingesta (operadores de ingesta), gestión (catalogar/buscar/controlar versiones), edición (redactores y montadores), emisión (control de emisión); el archivo atraviesa las cuatro. Cada etapa se encuentra por DATOS DESCRIPTIVOS, no por nombre de fichero.
- Oficio (RTVE): 4 vías de ingesta — tarjeta/cámara (copia+verificación), tiempo real desde señal (canal ocupado todo el acto), agencia/intercambio (normalización), archivo (restauración). 3 reglas: con metadatos o no se ingesta; se genera copia ligera al ingestar; la ingesta en tiempo real ocupa un recurso entero. No se repite; se graba por partida doble en dos sistemas independientes.
- Oficio: 3 datos que deciden si se encuentra — quién lo trae, de qué es, qué derechos tiene.
- Oficio (RTVE): 3 redes separadas — señal (vídeo/audio tiempo real), producción (ficheros/baja resolución/control), ofimática (correo/internet, expuesta); si producción cuelga de ofimática, un incidente de seguridad puede parar la emisión.
- Oficio (RTVE): debilidades y respaldo — redacción (escaleta en papel, manual), servidor de emisión (segundo replicado), almacenamiento (redundancia+copia del día), red (doble camino), estudio (alternativo), energía (SAI+grupo). 2 reglas: la redundancia se prueba; la degradación debe ser ordenada y ensayada.
- Oficio: la sala debe tener localizada cada pieza y avisar en cuanto falla una entrega, sin esperar a que la echen en falta.
- Convenio, ficha 5212206, lectura de oficio sobre las 5 etapas: recibir/enviar enlaces, configurar sistemas → ingesta; editar/postproducir → edición; control técnico de calidad, corregir vídeo/audio → control; etiquetar/introducir en base de datos → emisión; compactar → archivo. Ficha incluye también grabar/emitir/reproducir y repicar cintas (no ligadas al flujo en la tabla).
- Convenio: no define «compactar» ni la base de datos/automatización de la casa; la lectura por etapas es de oficio.

## Aplicación práctica

- Ingesta a emisión (oficio): nace en escaleta con nombre fijo (6.1; 6.1.1) → tarjeta o señal grabada, verificada → copia ligera automática si hay carpeta vigilada activa → montador busca en MAM/PAM por datos, monta con escaleta de planos (6.3) y texto del redactor (6.1.2) → rótulo, plantilla de la casa → exporta con *preset* de la casa, nombre de escaleta → revisa nombre/duración/inicio/fin/audio → entrega al servidor esperado, datos para automatización (MOS) → tras emisión, vuelve al sistema con metadatos.
- Cambio de escaleta a 20 min (oficio): se cambia en escaleta, se comunica desde su origen (6.1); orden/duración llegan solos si integrado; nombre no cambia (6.1.1); se duplica, recorta, exporta con mismo *preset*, se revisa duración real; sustituye a la anterior con el mismo nombre, se avisa a emisión.

## Lo que este tema no da, y dónde está

- Sistema de redacción, MAM/PAM, servidores de emisión y automatización que usa CSRTV hoy: no consta (dato Avid es de 2010). Campos de la base de datos de emisión automatizada y significado de «compactar»: el convenio no lo dice.
- Definición normalizada de MAM/PAM: no se ha encontrado. Contenido técnico de las especificaciones MOS: no leído, sólo portada/versiones/FAQ.
- Carpetas vigiladas de Adobe Media Encoder, diseño de .mogrt en After Effects y página de Avid sobre *Asset Management*: no leídos.
- Remite: sistemas de edición/*proxies*/conformado/exportación → tema 3; formatos de entrega → tema 4; montaje de noticias → tema 5; grafismo/rótulos → tema 7; ingesta/verificación/metadatos/archivo → tema 8; coordinación con otras áreas → tema 9; plataformas → tema 12; urgencia/versionado → tema 14; nomenclatura/trazabilidad → tema 15.
