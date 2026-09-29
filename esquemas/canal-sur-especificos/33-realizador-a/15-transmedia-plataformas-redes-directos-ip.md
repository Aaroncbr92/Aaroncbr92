# Tema 15 del específico de Realizador/a · Producción transmedia y realización para plataformas digitales, redes sociales y directos IP

**Siglas**: RTVA, CSRTV, RTVE, LGCA (Ley 13/2022), C-P (Contrato-programa), OTT, TDT, CMS, ID, FTP, GOP, CBR, LUFS, dBTP, RTMP(S), HLS, SRT, ARQ, PTP, NMOS/IS, NDI, N-1.

Esqueleto para repasar, no resumen: cada línea lleva su fuente; manda el texto del tema.

<!-- indice --><!-- /indice -->

## 1. Producción transmedia

- Convenio X, anexo III, ficha 5351000 (p. 196): «Diseñar, coordinar, supervisar y dirigir la realización de los programas audiovisuales»; calidad y duración; montaje, postproducción, mezclas; «no constituye una lista cerrada»
- C-P Manifiestan 4: LGCA suma al servicio público esencial servicios a petición, podcast, usuario de plataforma de vídeo, TV conectada. Manifiestan 5: «tercera línea», Canal Sur Media, OTT Canal Sur Más
- C-P cl. 3ª: p. 48 web propia, radio/TV lineales en línea, «en directo y en diferido», «posición proactiva en todo tipo de redes sociales»; p. 46 «Canal Sur Media» (OTT, pódcast, portales, redes, apps); p. 45 prioritaria Canal Sur Más; p. 29 registros «cross media» y «transmedia»
- Carta art. 7: 7.1 expansión prioritaria; 7.2 presencia en redes conforme LGCA; 7.5 TV conectada, IA, realidad virtual/extendida/aumentada; 7.6 TDT HD exclusiva desde 14-02-2024, cooperar en UHD 4K; 7.7 empresas contratadas «podrán ser instadas». Art. 6.7 «crossmedia y transmedia»; exposición de motivos «multimodal, transmedia y multiplataforma»; ninguno define
- Oficio: multiplataforma = misma información adaptada a cada salida; transmedia = cada medio cuenta una parte distinta; CMS = crea, publica, retira; metadatos descriptivos, técnicos, de gestión, estructurales, de uso; cross media = medios que se remiten, sin fuente
- Jenkins, «Transmedia Storytelling 101» (21-III-2007), 1: elementos integrales «dispersed systematically across multiple delivery channels», experiencia unificada; cada medio, aportación propia («makes it own» en original); The Matrix, «no one single source or ur-text». Académica, no norma
- Jenkins 3 mundos, no personajes ni tramas (*world-building*, impulso enciclopédico); 4 extensiones (BBC, radiodramas de Doctor Who); 6 cada entrega accesible sola, «additive comprehension»; 7 cocreación frente a licencia; 9 papeles y objetivos del público
- *Storyworld* (oficio): universo compartido; no es la biblia ni el *storyboard*; antes del guion
- *Agency*: Murray 1997 p. 126, vía Stang, Game Studies 19(1) 2019, «satisfying power to take meaningful action…»; oficio: sensación de cambios significativos
- Narrativas digitales (oficio): Juxtapose, Scrollytelling, Timeline, StoryMap, vídeo interactivo, transmedia
- Vídeo interactivo: rodar más de lo visto; árbol antes de rodar; raccord por rama. Mateu Torres (UMH 2024): «jerárquica y exponencial», «costosa de desarrollar»
- 360° (oficio): *stitching*; sin fuera de campo. YouTube 360: no leída
- Multiplataforma (versionar; al montar) frente a transmedia (material distinto; antes del guion) (oficio)
- RD 1680/2011 art. 7.1 «cine, vídeo, multimedia, televisión y new media»; módulo 0910 RA 7 opciones multimedia, multicanal e interactivas «por cualquier sistema o soporte»: a) TDT, IPTV, satélite, cable, streaming, podcast, móvil; c) canal de retorno (set-top-box, línea telefónica, SMS, Internet, cable); f) interactivos y videojuegos; contenidos: streaming, podcast; módulo 0902: new media. Norma de enseñanza

## 2. Realización para plataformas digitales

- Reuters DNR 2026 (48 mercados, global): redes y vídeo 54 % frente a webs y apps propias 51 %; 77 % vídeo informativo semanal; vídeo en sitios propios −5 pp; Facebook 43, YouTube 34, Instagram 26, TikTok 20 (menos de dos minutos); TV conectada 27 %
- LGCA art. 2: 2.5 TV lineal (simultáneo, horario); 2.6 TV a petición (catálogo); 2.7 sonoro lineal («cualquier soporte tecnológico»); 2.8 sonoro a petición; 2.18 programa «con independencia de su duración», incluidos «vídeos cortos»; 2.22 catálogo. Directo online = lineal; clip = programa
- Oficio, web: duración variable; 16:9, 1:1, 9:16; sin sonido; versión por destino. Flujo: rodaje, servidor (ID, metadatos), edición, exportación por destino
- Máster por destino (oficio): códec, resolución, color, pistas, sonoridad, estructura, subtítulos; emisión, plataforma, venta internacional. Especificaciones de Canal Sur: no constan
- YouTube subidas (25-09-2026; sólo partners con Gestor de contenido): MP4, sin listas de edición, moov al inicio; AAC-LC, Opus o Eclipsa, 48 kHz; H.264 progresivo, perfil alto, 2 B, GOP cerrado de media cadencia, CABAC, tasa variable sin límite; 4:2:0; misma cadencia (24, 25, 30, 48, 50, 60); SDR BT.709. 1080i60 a 1080p30; 50 campos a 25 fotogramas = aplicación, no texto
- YouTube Mbps SDR (24-25-30 / 48-50-60): 2160p 35-45 / 53-68; 1440p 16 / 24; 1080p 8 / 12; 720p 5 / 7,5. Audio 128 kbps mono, 384 estéreo, 512 5.1. BT.2020 pasa a BT.709 (8 bits) sin transferencia HDR. Fichero: variable y GOP media cadencia; directo: CBR y clave cada 2 s
- EBU R 128 s2 (nov. 2023): d) producir según R 128 y Tech 3343; e) emitir a −23,0 LUFS; f) metadatos de sonoridad; g) sin metadatos, provisional −20,0 a −16,0 LUFS; h) volver a −23,0. AES TD1008.1.21-9 (2021): −18 LUFS, ≤ −1 dBTP. Blackmagic, Resolve 21, cap. 182 p. 4140: YouTube −14 LUFS (YouTube no lo publica). Canal Sur: no consta
- C-P 3.19 p. 103: Canal Sur Más 24 h/día, lineal y a petición, mundial «conforme a la posesión de derechos»; sustituir piezas sin derechos (tema 17)
- LGCA 101.1.g) webs y apps gradualmente accesibles; Ley 10/2018 31.1.i) mantener «la clasificación por edades y las características de accesibilidad»; tema 16
- Por salida (oficio): antena y OTT 16:9; YouTube 16:9 sin barras, progresivo; redes 9:16 (1:1, 4:5) cuadro lleno, abiertos, grafismo rehecho. Cifras de plataforma: comprobar antes

## 3. Redes sociales

- C-P p. 48 y Carta 7.2; Carta 6.8: «inmediatez en la interactuación con la audiencia y participación efectiva»
- LGCA 2.13 intercambio de vídeos a través de plataforma (sin responsabilidad editorial, algoritmos); 2.20 vídeo generado por usuarios; Canal Sur es usuario; obligaciones de plataformas: tema 14 de Redactor/a
- YouTube aspecto (25-09-2026): 16:9 estándar; 9:16 en ordenador con relleno; «no añadas márgenes ni barras negras»; 2160p 3840x2160, 1440p 2560x1440, 1080p 1920x1080, 720p 1280x720, 4320p 7680x4320; desde 2022 se retira reproducción entre 4K y 8K. Vertical HD 1080 × 1920 (giro; la página no lo da); montar en vertical, sin franjas
- Short (YouTube, 25-09-2026): desde 15-10-2024 cuadrado o vertical hasta tres minutos; antes, largos; 16:9 para no serlo
- Resolve: cap. 41 p. 860 líneas de tiempo propias (*Use Project Settings*); cap. 127 p. 3119 guías «Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9»; zonas Action y Title valen para móviles (tema 12)
- Reencuadre (oficio): 3413 × 1920, franja de 1080 = 32 %; sin escalar 608 × 1080 (607,5); plano a plano; rodar abierto o UHD (4K = 4 veces el HD); zonas que tapa la app: no publicado
- Clip: en edición, elemento de línea de tiempo (tema 13); en redes, pieza corta sola (oficio); es programa (2.18). RTVE Manual de Estilo 4.1: pieza independiente; 4.3.2-4.3.3: «Se evitarán los videos de recurso». Oficio: rótulo, unidad de sentido, metadatos propios
- Miniatura (YouTube): «captura rápida»; propia si cuenta verificada; Shorts sólo en YouTube Studio desde ordenador; «el mayor tamaño posible». Oficio: derecho de imagen (tema 17)
- Pautas (oficio): esencial al inicio; texto por el sonido apagado; planos cerrados; una idea por pieza; ritmo sin cambiar el sentido. Sin pautas de la RTVA
- YouTube música en Shorts: Biblioteca de audio; mayoría 90 s en Short de hasta tres minutos, algunas 60 o 30 s; sin regalías, sin reclamación. Content ID: desde 24-09-2026 Shorts de más de uno y menos de tres minutos no se bloquean; menos de un minuto, igual; si bloquea, retirar o impugnar. Licencia de emisión no cubre redes (tema 17)
- Carta 26.1 Defensa de la Audiencia; 26.2 «eje rector». C-P p. 30: interacción «eslabón de la cadena de valor», quejas, protección de datos. Oficio: moderar, no rotular sin filtro
- LGCA 156.2: conservar seis meses desde la primera puesta a disposición programas y contenidos (con comunicaciones comerciales) y registrar sus datos; alcanza lo a petición. Retirar de la web no es borrar del archivo (oficio)

## 4. Directos IP

- *Streaming* (oficio): descarga; progresiva (entero, sin adaptación); por secuencias (segmentos, adaptación). Directo = secuencias
- Contribuir (al centro; latencia baja y constante; SRT) frente a distribuir (al espectador; OTT) (oficio)
- YouTube emisión (29-09-2026): URL del servidor y clave; por defecto RTMP; RTMPS = TLS/SSL, recomendado
- RTMP: Adobe (21-XII-2012), sobre TCP, comando publish, tipo «live» (7.2.2.6); ni norma ni RFC. HLS: RFC 8216 (agosto 2017), Informational, vía independiente; segmentos y adaptación; versión 7; rfc8216bis en borrador; mayor latencia; HDR: primero H.265 sobre RTMP(S)
- YouTube ajustes (answer 2853702): H.264, H.265 o AV1; hasta 60 fps; clave cada 2 s, máximo 4; AAC o MP3; CBR; progresivo, 2 B, 1 referencia; CABAC; 128 kbps estéreo, 384 5.1 (sólo AAC); tabla: tema 14
- Ingesta Mbps (mínima AV1/H.265, máxima, recomendada H.264): 4K60 10/40/35; 4K30 8/35/30; 1440p60 6/30/24; 1440p30 5/25/15; 1080p60 4/10/12; 1080p30 3/8/10; 720p60 3/8/6; 240-720p30 3/8/4. Sin 25 ni 50. 4K sin baja latencia. «Make sure to test»; «monitor the stream health»; speed test. 1080p60 = 12 Mbps + 128 kbps; dos emisiones, más de 24
- Latencia (answer 7444635): reserva del reproductor. Normal (no interactivo, máxima calidad); baja (menos de 10 s, encuestas, sin 4K); ultrabaja (menos de 5 s, sin 4K, más cortes); webcam y móvil, siempre interactivos
- Horizontal y vertical (answer 2474026): ambos por defecto; vertical = recorte central (Center crop, Fit to phone width, Stacked); codificador propio: RTMP(S) y segunda clave; no se añade con la emisión en marcha; Shorts ven el vertical; mismo chat; vertical sin enlaces en chat, anuncios, estrenos ni redirección, sin 4K en la app.
- SRT (draft-sharabayko-srt-01, 7-IX-2021): latencia inferior a un segundo; sobre UDP; ARQ (1.1); *listener/caller* (1.2), *rendezvous*; AES 128, 192, 256; contraseña 10-80 caracteres; latencia por defecto 120 ms; abierto, no norma; Informational, «Expires: 11 March 2022»; no RFC
- Mochila (oficio): agrega SIM, wifi, cable (la más estable); no es radio. No promete: estabilidad, ausencia de retardo, poca cobertura. LiveU LU800 (fabricante): 14 conexiones, ocho módems 5G/4G doble SIM, 60 Mbps, HEVC; «the lowest latency» sin cifra.
- Producción remota (oficio): control en el centro. Mochila: medir y avisar el retardo; N-1; grabar en cámara. Videoconferencia: prueba previa
- ST 2110-10:2022: IP en instalaciones, cada esencia por separado; sobre VSF TR-03, TR-04 y AES67. Familia «Professional Media Over Managed IP Networks»: -10 System Timing and Definitions; -20 Uncompressed Active Video; -21 Traffic Shaping and Delivery Timing for Video; -22 Constant Bit-Rate Compressed Video; -30 PCM Digital Audio; -31 AES3 Transparent Transport; -40 SMPTE ST 291-1 Ancillary Data; -41 Fast Metadata Framework; -43 Timed Text Markup Language for Captions and Subtitles. Leídas -10, -20, -30; OV 2110-0; RP 2110-23, 24, 25
- ST 2110-10 cl. 1: RTP, reloj común, marcas de tiempo. -20:2022: vídeo sin comprimir, SDP. -30:2025 (revisa 2017): PCM por AES67; audio no PCM fuera de alcance
- PTP, -10 cl. 7.2: reloj común «should» (IEEE 1588-2008); «shall» admitirlo (perfil ST 2059-2, no leída); = generador de sincronismos. Cl. 8.5: flujos duplicados ST 2022-7 «may». Cl. 6.3: UDP 1460 octetos «shall»; cl. 6.4: extendido 8960, opcional; receptores sólo el estándar
- NMOS (AMWA): IS-04 Discovery & Registration; IS-05 Device Connection Management; IS-07 Event & Tally (piloto); IS-08 Audio Channel Mapping
- NDI: estándar de especificaciones propietarias; no es códec (SpeedHQ; H.264 y HEVC en HX); mDNS o Discovery Service.
- Previsión (oficio): claves (Canal Sur Media); prueba; línea de reserva; latencia y vertical antes; grabar en local; conservar el plazo legal. Protocolo, plataformas y equipo IP de Canal Sur: no consta

## Aplicación práctica

- Magacín en directo (TDT, Canal Sur Más, YouTube en ambos formatos, tres clips): salidas y claves con Canal Sur Media; derechos para internet; vertical decidido (608 × 1080 central); RTMPS H.264 1080p, a 50 cuadros fila de 60 (12 Mbps), dos claves, doble subida; latencia baja o ultrabaja; mochila por SRT; invitado con N-1; antena −23 LUFS, Canal Sur Más según R 128 s2; clips MP4, H.264, 4:2:0, AAC-LC 48 kHz, BT.709, 25 fotogramas
- Cuentas: 1080 × 9/16 = 607,5; 608/1920 = 32 %; 2 × 50 = clave cada 100 imágenes; clip del 1 de octubre, hasta el 1 de abril

## Lo que el tema no da

- No leídas: TikTok, Instagram, Facebook, X; YouTube 360; ST 2059-2; norma EBU de producción remota; DNR España; Murray directamente
- No consta: guía de Canal Sur para redes, directos o transmedia; plataformas, protocolos, equipo IP, vertical, producción remota, sonoridad de streaming
