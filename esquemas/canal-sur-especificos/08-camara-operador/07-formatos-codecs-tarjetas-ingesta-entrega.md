# Tema 7 del específico de Cámara Operador · Formatos de grabación, códecs, tarjetas, metadatos, ingesta, copia de seguridad y entrega de material

**Siglas**: RTVA; Canal Sur Radio y Televisión, S.A. (**CSRTV**); UIT-R; EBU; SMPTE; ENG; HD/UHD; fps; RGB; p/i; Mb/s, GB, TB; GOP (*group of pictures*, GOP largo=*Long GOP*); AVC/H.264; HEVC/H.265; MXF (patrones **OP1a**, **OP-Atom**); MOV, MP4, AVI; AAF; EDL; XML; PCM/LPCM; VBR/CBR; PSNR; TC, LTC, VITC; DF/NDF; SD/SDXC; CFexpress (VPG); USB; UHS; V (clase de vídeo); exFAT; RAID; LTO; FTP/FTPES; MD5/SHA-256; INCIBE.

Esqueleto, no resumen. Telegrama, fuente delante de cada línea; se quita explicación, no el dato. Vigente el **24/09/2026**. Sin norma jurídica: UIT-R (formato de imagen), documentación de fabricante, LOC/DPC/INCIBE/SD Association, Libro de estilo CSTV (2004) y oficio.

<!-- indice -->

## Índice

- [Esencia, códec, contenedor](#esencia-códec-contenedor)
- [Qué define un formato](#qué-define-un-formato)
- [El *proxy* y la capacidad](#el-proxy-y-la-capacidad)
- [Códecs](#códecs)
- [Tarjetas](#tarjetas)
- [Metadatos y código de tiempo](#metadatos-y-código-de-tiempo)
- [Ingesta](#ingesta)
- [Copia de seguridad](#copia-de-seguridad)
- [Entrega de material](#entrega-de-material)
- [Fuentes citadas](#fuentes-citadas)
- [Lo que este tema no da](#lo-que-este-tema-no-da)

<!-- /indice -->

## Esencia, códec, contenedor

- oficio — Cinta→disco óptico (XDCAM)→tarjeta: acceso no lineal + ficheros con metadatos, no señal; ingesta=copia, no volcado.
- oficio — Esencia (imágenes/sonido) · códec (comprime la esencia: H.264/H.265/ProRes/DNxHD/PCM) · contenedor (empaqueta esencia+metadatos: MXF/MOV/MP4/AVI) · metadatos (TC, nombre, fecha) · proyecto (decisiones sin esencia: AAF/EDL/XML). Un contenedor admite varios códecs y viceversa: «MXF» o «MP4» solos no dicen la calidad.
- oficio — Contenedores: MXF (SMPTE, broadcast/servidor/archivo) · MOV (Apple, habitual de ProRes) · MP4 (familia MPEG, cámaras ligeras/distribución) · AVI (Microsoft, apenas TV).
- LOC, fdd000013 — MXF: «**Object-based file format that wraps video, audio, and other bitstreams («essences»)... optimized for content interchange or archiving**»; «**"digital equivalent of videotape"**»; norma central «**SMPTE ST 377-1:2011**».
- LOC, fdd000013 — MXF no es códec, es contenedor. Patrón OP1a («**SMPTE ST 378:2004... Single Item, Single Package**»): todo en un fichero, emisión/intercambio, mayoría de cámaras. Patrón OP-Atom («**SMPTE ST 390:2011... Simplified Representation of a Single Item**»): un fichero por pista (vídeo + cada audio); Avid y cámaras P2.
- Panasonic, *AVC-Intra FAQ*, preg. 12 — P2/AVC-Intra: «**MXF OP-ATOM**»; sonido en ficheros aparte del vídeo.
- LOC, fdd000013 — TC en MXF: EBU **«Recommendation R122-2010»** define su codificación (no leída).
- oficio — Proyecto: EDL (solo cortes+TC, una pista, sin efectos/audio complejo) · AAF (cortes+pistas+niveles+efectos+metadatos, puede llevar esencia) · XML (equivalente, no universal). Los tres dependen del TC: dos clips con el mismo código no se distinguen.

## Qué define un formato

- UIT-R BT.709-6 — HD: «**Muestras por línea activa 1920**», «**Líneas activas por imagen 1080**».
- UIT-R BT.2020-2, cuadro 1 — UHD: **«7 680 × 4 320»** y **«3 840 × 2 160»**, **«Formato de imagen 16:9»**.
- oficio (cálculo) — 4K TV (3.840×2.160, 16:9) ≠ 4K cine DCI (4.096×2.160, ≈17:9): 3.840÷2.160=1,777…(16/9); 4.096÷2.160=1,896…
- oficio — Cadencia: Europa 25/50; sistemas americanos 29,97/59,94; cine 24/23,98 (origen del .97: B/N a 30 exactos, color bajó la tasa en 1.000/1.001). Barrido p/i. Muestreo cromático: 4:2:2 producción, 4:2:0 distribución (1.ª cifra=luminancia; 4:4:4 sin submuestreo; 4:2:2 mitad color horizontal; 4:2:0 mitad horiz.+mitad vert.). Profundidad 8/10 bits (2⁸=256, 2¹⁰=1.024 niveles).
- Sony, Z200 Help Guide p.336 — Formato ejemplo: MP4→**«XAVC HS Long 422/420»**, **«XAVC S Long 422/420»**, **«XAVC S-I Intra»**; MXF (solo Z200)→**«XAVC Long 422/420»**, **«XAVC I Intra»**, **«MPEG HD 422 (license required)»**; audio **«LPCM 24-bit, 48 kHz, 4-channel»**; cadencias hasta **«3840×2160P/119.88P*»**.
- Sony, ILCE-7SM3 — Ejemplo con tasa/bits: **«200M 4:2:2 10bit»** a **«50p (PAL)»** en XAVC S 4K.
- Sony, Z200 p.336 / PXW-X400 «Specifications» p.144 — MPEG HD 422 = MPEG-2 GOP largo: **«MPEG HD422 mode: CBR, 50 Mbps, MPEG-2 422P@HL»**; MPEG HD 420: **«VBR, 35 Mbps (max), MPEG-2 MP@HL»**; XAVC-L 50 = H.264: **«VBR, 50 Mbps (max)»** (equivalencia MPEG HD422/Z200 deducida, no en manual Z200).

## El *proxy* y la capacidad

- oficio — *Proxy*: copia de menor resolución, muy comprimida, con TC; flujo *offline*-*online*; sin TC no sirve para montar.
- Sony, Z200 pp.160-161 — Proxy simultáneo al original: **«record a low-resolution proxy clip at the same time as recording a high-resolution original clip»**; extensión **«.mp4»**; **«timecode is also recorded simultaneously»**; nombre = clip+**«"S03"»**; se subdivide en trozos y se transfiere antes de acabar la grabación; carpeta propia (**«/PRIVATE/M4ROOT/SUB»**), no junto al original.
- oficio (cálculo) — minutos = capacidad(bits)÷tasa(bit/s)÷60. 128 GB a 200 Mb/s: 128×8=1.024.000 Mbit÷200=5.120 s≈85 min. Misma tarjeta a 500 Mb/s: 1.024.000÷500=2.048 s≈34 min.
- Panasonic, *AVC-Intra FAQ*, preg.10 — Tarjeta P2 16 GB, 1080/50i-25p: «**16 minutes... AVC-Intra 100**» / «**32 minutes... AVC-Intra 50**»; a 23,98p: «**20 minutes... AVC-Intra 100**» / «**40 minutes... AVC-Intra 50**» (nominal a 100 Mb/s≈21 min: fuente da 1/4 menos, sin explicarlo).
- Sony, Z200 p.97 — Tiempo restante: **«calculated from the remaining capacity of the memory card... and the currently configured recording format»**; cambia con el formato.

## Códecs

- oficio — Códec=codificador-decodificador; casi todo vídeo TV, con pérdida (transformada discreta del coseno, recuantifica altas frecuencias). Audio de cámara sin comprimir: LPCM.
- Sony, *Help Guide ILCE-1* — Intra/Long GOP: «**Intra compresses the movie by frame, and Long GOP compresses multiple frames. Intra... better response and flexibility when editing, but Long GOP... better compression efficiency.**»
- Panasonic, *AVC-Intra FAQ*, preg.2 — GOP largo: «**usually used for content delivery and packaged media**», pero «**any image manipulation or processing will severely degrade the image quality**»; Intra: «**zero interaction between adjacent frames... stands up well to motion and editing**» (fuente comercial de un fabricante de intracuadro).
- Sony, ILCE-7SM3 — XAVC S: «**MPEG-4 AVC/H.264 codec**»; XAVC HS: «**MPEG-H HEVC/H.265 codec with 10-bit color sampling**», más eficiente, más cálculo; edición exige **«high processing capability»**.
- Sony, Z200 p.202 — Streaming H.265: **«some receivers may not support playback correctly»**.
- Sony (Help Guide ILCE-1, ILCE-7SM3, Z200 p.336) — XAVC (familia Sony, no códec): XAVC S(Long)=H.264 GOP largo/MP4; XAVC HS(Long)=H.265 GOP largo/MP4; XAVC S-I=H.264 intra/MP4; XAVC Long/I=GOP largo o intra/MXF (norma en MXF no consta). Recomendado editar en **«10-bit 4:2:2»**.
- LOC, fdd000389 — ProRes: **«family of proprietary, lossy compressed... video intermediate codecs... FCP»**; dos ramas 422 (Proxy/LT/422/HQ) y 4444 (incl. **«4444 XQ»**); rasgos 422: «**4:2:2**», «**10-bit**», «**intraframe only**», «**variable bit rate**»; contenedor MOV, y MXF desde FCP 10.3 (27-10-2016); PSNR 422 HQ 15-20 dB más que 422 Proxy con ≈5× su tasa. Tasas por variante: no leídas.
- Avid, *DNxHD Technology* (2012) — «**10 and 8-bit HD encoding**», codificado por SMPTE **«VC-3»**; mapeo MXF **«SMPTE 2019-4»**. Variantes (1080i/30, 60 campos, salvo 444): 444=10 bit/4:4:4/440 Mb/s; 220x/220=8-10 bit/4:2:2/220 Mb/s (progresivo 24p=175 Mb/s); 145=8 bit/4:2:2/145 Mb/s (24p=115, 25p=120); 100=8 bit/4:2:2/100 Mb/s (submuestrea a 1440 o 960); 36=8 bit/4:2:2/36 Mb/s, solo offline HD progresivo. A 1080i/50: 185x/185=184 Mb/s, 120=121 Mb/s, 85=84 Mb/s (submuestreada a 1440×1080). A 1080p/25: añade 365x (10 bit/4:4:4/367 Mb/s) y 36 (36 Mb/s). DNxHR: no leído.
- Panasonic, *AVC-Intra FAQ*, preg.1,4,12,13 — AVC-Intra: «**intra-frame video codec... bit rates of 50 and 100Mb/s**», perfiles H.264 High 10/High 422; modo 100=4:2:2/10-bit/raster completo 1920×1080; MXF OP-Atom en P2; soporta metadatos MXF.
- oficio — Cuadro resumen: H.264(AVC)=norma, GOP o intra según perfil, MP4/MXF/MOV · H.265(HEVC)=norma más eficiente, en cámara GOP largo, MP4 · XAVC=familia Sony, H.264/H.265, intra o GOP, MP4/MXF · AVC-Intra=Panasonic sobre H.264, intra 50-100 Mb/s, MXF OP-Atom · ProRes=Apple, intra, VBR, MOV(MXF) · DNxHD=Avid/VC-3, 36-440 Mb/s, MXF(MOV) · LPCM=audio sin comprimir, dentro del vídeo.

## Tarjetas

- oficio — Estado sólido: SxS (Sony/SanDisk) · P2 (Panasonic, MXF OP-Atom) · disco XDCAM (Sony, en retirada) · SD/SDXC/CFexpress genéricas.
- Sony, Z200 p.67 — **«records audio and video on CFexpress Type A memory cards... or SDXC memory cards»**; también proxy y ajustes/actualización de la cámara.
- SD Association, «Speed Class» — Familias: **«Class 2, 4, 6 and 10»**; UHS **«U1»** y **«U3»**; vídeo **«V6, 10, 30, 60 and 90»**; el número=«**minimum writing speed**».
- SD Association, *Video Speed Class* (02/2016) p.4-5 — Escritura mínima (MB/s)→clase: 90=V90; 60=V60; 30=U3/V30; 10=Class10/U1/V10; 6=Class6/V6; 4=Class4; 2=Class2. Salvedad: una tarjeta puede cumplir V30 y solo C10 (métodos distintos); «**match the SD memory card to your specific application's requirements**».
- oficio (cálculo) — Mb/s÷8=MB/s. 200 Mb/s=25 MB/s→basta V30/U3, no basta V10/U1/C10. 500 Mb/s=62,5 MB/s→supera V60, pide V90.
- Sony, Z200 p.68 — CFexpress: **«VPG200»**/**«VPG400»** (qué garantizan: no leído en fuente que define VPG); tarjeta recomendada, según **«[Rec Format]»**, en tabla del manual; capacidad grande no implica velocidad. Relevo con SD: **«use SD cards of the same type»** (p.99).
- Sony, Z200 p.98 — Relevo: **«recording automatically switches to the second memory card just before the remaining capacity on the first card reduces to zero»**; solo cambiar tarjeta con acceso apagado; **«cannot be played back seamlessly»** en la unidad.
- Sony, Z200 p.153 — Simultánea (**«Simul Rec»**): mismo nombre de clip en las dos tarjetas; primera copia de seguridad hecha en cámara. No compatibles entre sí (una u otra ranura, no ambas funciones a la vez).
- Sony, Z200 p.95 — Extracción: **«if... the memory card is removed while... being accessed, the integrity... cannot be guaranteed»**; esperar indicador verde/apagado; tarjeta caliente tras grabar no indica avería.
- Sony, *Help Guide ILCE-1* — No retirar tarjeta/batería/USB con piloto de acceso encendido.
- Sony, Z200 p.96 — Formatear: **«erases all data»**; **«Full Format»** (completo)/**«Quick Format»** (solo gestión); avisa si hay envíos pendientes.
- Sony, *Help Guide ILCE-1* — Formatear siempre en la cámara que graba (**«not guaranteed»** si es en ordenador); nunca si lo pide un equipo incompatible (**«Never format the card in response to this prompt»**); si se fragmenta, guardar y formatear en cámara. exFAT en SDXC/CFexpress-A.
- Sony, Z200 p.96 — Cambio de cámara: **«make a backup of the card, then reformat the card in the device to be used»**.
- oficio — Regla: no formatear sin copia comprobada.
- Sony, *Help Guide ILCE-1* — Bloqueo SD (**«LOCK»**): impide grabar/borrar. Cuidado: no mojar/golpear/doblar; no tocar terminales; no pegar etiqueta en la tarjeta.
- Sony, Z200 p.31, p.310 — Icono **«(Protected)»**. Aviso **«[Media Temperature High]»**: tarjeta CFexpress caliente, reemplazar o enfriar.
- Sony, Z200 pp.310-311, 97 — Avisos: **«[Media Near Full]»** (menos de 5 min entre tarjetas) · **«[Media Full]»** · **«[Clips Near Full]/[Clips Full]»** · **«[Media(A) Life Near End]/[Media(A) Life End]»**. Máximo de clips por tarjeta: **«9999... XAVC S»** / **«600... XAVC»**.

## Metadatos y código de tiempo

- oficio — Metadatos: cuándo/cómo se grabó, TC, nombre, bueno/malo. Unos automáticos (cámara), otros configurados antes (nombre, TC, bits de usuario), otros en directo (marcas/banderas).
- Sony, Z200 p.99, p.252 — Clip=grabación de inicio a fin de una toma; nombre automático por **«[Clip Name Format]»**; en Z200, título (**«[Title Prefix]»**/**«[Title Name Settings]»**) + número 4 cifras (**«[Number Set]», «0001 to 9999»**), solo MXF/Z200; numeración por **«[Series]»** o **«[Reset]»**. Duración máx. de clip: **«13 hours»** (XAVC S), **«24 hours»** (XAVC, solo Z200).
- oficio — TC: etiqueta HH:MM:SS:CC; forma LTC (como audio, entre equipos) o VITC (dentro de la señal de vídeo). Palabra LTC: 80 bits/cuadro, 32 de usuario (norma SMPTE no leída).
- Sony, Z200 p.251 — TC: **«[Mode]»**=[Preset]/[Regen]/[Clock] («**Preset: Starts from a preset value**»; «**Regen: from the timecode of the end of the previous clip**»; «**Clock: internal clock**»); **«[Run]»**=[Rec Run]/[Free Run] («**Rec Run: only when recording**»; «**Free Run: always running**»); **«[TC Format]»**=[DF]/[NDF].
- oficio — Rec Run+Regen: continuo, sin repetir código en la tarjeta. Free Run/Clock: hora real, para sincronizar varias cámaras/sonido. DF/NDF solo importa a 29,97/59,94 (no entero); a 25/50 no hace falta.
- Sony, Z200 p.151 — Pregrabación fuerza **«[Free Run]»** aunque esté en Regen/Rec Run.
- Libro de estilo CSTV, 5.3.3 p.81 — TC: **«un acuerdo básico entre periodista y cámara... puede usarse un código de tiempo real previamente acotado... TC poniendo el marcador a 00:00:00 al principio de la cinta. Esta referencia es generalmente mejor... cuando el material va a ser usado por terceras personas»** (pacto vigente; referencia a cinta, de 2004).
- Sony, Z200 p.99, p.251 — Bits de usuario: número hex de 8 cifras (32 bits=8×4); **«[Fix]»** (valor fijo) o **«[Time]»** (hora actual).
- oficio (cálculo) — Resta de TC a 25 fps, de 00:47:17:23 a 01:23:54:00: cuadros 25-23=2 (préstamo 1 s=25 cuadros); segundos 54-1-17=36; minutos 83-47=36 (préstamo 1 h); horas 0. Resultado 00:36:36:02 (+1 si inclusiva=00:36:36:03). Cambia el préstamo a 24/30.
- Sony, Z200 p.298 — Sincronizar TC externo: solo Z200 (no HXR-NX800); modo Preset+Free Run, TC IN, **«acquires lock... "EXT-LK"»**; tras ≈10 s de lock se mantiene sin la fuente; esperar estabilización antes de grabar; deriva posible **«one frame per hour»**; para dar TC a otro equipo, fuente en Free Run o Clock.
- Sony, Z200 p.242, p.160 — Marcas: **«[Shot Mark1]/[Shot Mark2]»** (instante dentro del clip); banderas **«[Clip Flag OK]/[Clip Flag NG]/[Clip Flag Keep]»** (califican el clip entero); miniaturas ordenables por bandera.
- Panasonic, *AVC-Intra FAQ* — **«AVC-Intra supports MXF metadata»**. Sony, Z200 p.252 — **«[Update Media]»**: actualiza fichero de gestión de la tarjeta.

## Ingesta

- oficio — Ingesta=meter el material en el sistema de trabajo; formas: de fichero (copiar con comprobación) · en directo/*crash record* (grabar señal entrante) · programada (horario, sin nadie). Al cámara, sobre todo la primera, y en directo al enviar (tema 13). Quién ingesta y con qué sistema en CSRTV: no consta.
- DPC, *Digital Preservation Handbook*, «Fixity and checksums» — Bloqueo de escritura: **«Use write-blockers when working with original media»**, para **«prevent write access»**; salvedad: **«don't exist for all types of media»**, algunas casas lo ven **«unnecessary or a level 3 or level 4 step»**.
- oficio — Pasos: 1) proteger/bloquear original; 2) copiar la tarjeta entera con estructura (proxy en carpeta propia; en P2 audio en ficheros aparte; ficheros de gestión aparte); 3) comprobar con suma de verificación (o mínimo tamaño+apertura); 4) revisar (nº clips, clips partidos por relevo, sin sonido en cámara lenta); 5) anotar y entregar; solo luego, formatear en la cámara.
- DPC, *Handbook* — Recomendaciones de nivel 2: **«Check fixity on all ingests»**, **«Virus-check high risk content»**.
- Sony, Z200 p.163, p.162, p.151 — Envío desde el lugar: proxy por trozos, **«[Auto Upload (Proxy)]»**=[Chunk], trozo por defecto **«[30s]»** (o 1-2 min), sube mientras graba; ranura B dedicada, incompatible con relevo y simultánea. Proxy incompatible con cámara lenta. Pregrabación incompatible con Interval Rec, simultánea y proxy.

## Copia de seguridad

- Sony, *Help Guide ILCE-1* — **«Be sure to back up the data for protection.»**
- oficio — Primera copia: simultánea en dos tarjetas (mismo nombre de clip), única antes de llegar a ordenador; incompatible con pregrabación y proxy por trozos.
- DPC, *Handbook* — Suma de verificación: **«fixity... means the assurance that a digital file has remained unchanged»**; **«checksum... "digital fingerprint"»**, pero **«do not tell you where in the file that the change has occurred»**; sirve para cadena de custodia; algoritmos **«MD5 and SHA-256»**, MD5 suficiente para pérdida accidental; con varias copias, la suma dice cuál sirve de repuesto (**«data scrubbing»**).
- oficio — Aplicado: programa compara suma de original y copia; comparar solo tamaño no basta.
- INCIBE, 29-09-2021 — Regla 3-2-1: **«tres copias de seguridad de un mismo tipo de información, en dos dispositivos distintos y, una de ellas, almacenarla en un lugar diferente»**.
- oficio — Traducción a jornada: original en tarjeta + copia en disco de equipo + envío al servidor (o dos discos por separado); no formatear sin dos copias comprobadas.
- oficio — RAID no es copia de seguridad: RAID 0 (reparte, sin redundancia, mínimo 2 discos) · RAID 1 (espejo, mínimo 2) · RAID 5 (paridad distribuida, mínimo 3) · RAID 6 (doble paridad, mínimo 4). Protege de fallo de disco, no de borrado, corrupción replicada, robo o incendio; RAID 0 no protege de nada.
- oficio — LTO: cinta magnética, alta capacidad, escalable, regrabable, norma abierta; barata por TB, sin consumo en reposo, dura décadas, fuera de red; acceso secuencial y lento; archivo, no trabajo. Sistema/plazos de CSRTV: no constan.

## Entrega de material

- Libro de estilo CSTV, 5.3.3 p.82 — **«Es conveniente mantener la norma de registrar una sola noticia por cinta, después de un mínimo de treinta segundos de barras al principio de la misma. Si hay dos noticias en el mismo soporte deben separarse con un minuto de barras.»** (regla de cinta, histórica; no consta sustituta vigente en fichero).
- Libro de estilo CSTV, 5.3.3 p.82 — Vigente: **«revisar la grabación en el mismo lugar... para comprobar que es correcta desde la perspectiva de la imagen y del sonido»**. Sony, Z200 p.99 — **«[Rec Review]»**: revisión del último clip.
- oficio — Protocolo de entrega CSRTV (nomenclatura, carpetas, formato de casa, sistema de envío): no consta publicado. Lista de oficio: 1) material completo, sin seleccionar; 2) identificado (tarjeta con encargo/fecha, clip con cámara, orden si hay varias); 3) con datos (formato, cadencia, TC usado, momentos clave); 4) con avisos (ruido, cámara lenta sin sonido, clip partido, imagen sensible→tema 12); 5) con estado de copia, sin formatear hasta confirmarlo.
- Sony, Z200 p.196 — **«In FTP, the contents, user name, and password are not encrypted. For secure data transfer, use FTPES (FTPS).»**; FTPES=**«FTPS in Explicit mode»**.
- oficio — Enviar antes proxy o lo urgente; comprobar llegada completa antes de borrar; no formatear tarjeta con envíos pendientes (aviso del manual, ver «Tarjetas»); mochilas/enlaces/streaming en tema 13.
- oficio (supuesto) — Rueda de prensa+declaración, envío urgente+pieza larga: antes de salir, comprobar formato/cadencia, formatear tarjetas ya copiadas, nombre y TC; en el lugar, acordar TC (hora real si varias cámaras), elegir simultánea o proxy por trozos (no ambas); mientras graba, marcar/banderar OK, vigilar tarjeta llena; tras la declaración, revisar y enviar por FTPES; en redacción, bloquear tarjeta, copiar con suma de verificación a dos destinos, entregar con avisos; formatear solo con dos copias comprobadas.

## Fuentes citadas

- UIT-R BT.709-6, BT.2020-2 (cuadro 1). Library of Congress, *Sustainability of Digital Formats*, fdd000013 (MXF) y fdd000389 (ProRes 422). Avid, *Avid DNxHD Technology* (2012). Panasonic, *AVC-Intra Frequently Asked Questions*. Sony: *PXW-Z200/HXR-NX800 Help Guide* (2024), *Help Guide ILCE-1*, ILCE-7SM3 «Characteristics of each file format», *PXW-X400 Operating Instructions* (2015). SD Association, «Speed Class» y *Video Speed Class* (02/2016). Digital Preservation Coalition, *Digital Preservation Handbook*, «Fixity and checksums». INCIBE, 29-09-2021. Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía (2004), 5.3.3.

## Lo que este tema no da

- Cámaras, formatos de casa, códec/sistema de ingesta y protocolo de entrega de CSRTV: no constan; ejemplos son de manuales Sony públicos, no del equipo real.
- Regla vigente de CSRTV sobre barras/tono al inicio de tarjeta (Libro de estilo solo trata cinta). Qué garantizan las clases VPG de CFexpress. Tasas de cada variante ProRes y su año; DNxHR; norma de compresión de XAVC en MXF. Reparto de los 80 bits del TC y su norma SMPTE; UMID y metadatos de planificación. Especificación DCI del 4K de cine.
- Compresión/defectos/tasas EBU → tema 9; sonido y sincronía → tema 6; envío en directo/mochilas → tema 13; cámara lenta/multicámara → tema 15; cuidado de equipo/incidencias → tema 11; imágenes sensibles/derechos → tema 12; protección de datos → tema 10 del común.
