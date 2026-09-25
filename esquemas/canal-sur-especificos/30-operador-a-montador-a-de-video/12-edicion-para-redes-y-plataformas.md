# Tema 12 del específico de Operador/a Montador/a de Vídeo · Edición para redes y plataformas

**Siglas**: RTVA; CSRTV («Canal Sur»); RTVE; LGCA (Ley 13/2022); UE; CNMC; OTT; TDT; HD/UHD; CMS; ID; FTP; SDR/HDR; GOP; AAC(-LC); LUFS; EBU; BT.709. MP4, H.264, JPG, PNG: nombres de uso, no siglas.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; se lee el tema para el desarrollo.

<!-- indice -->
<!-- /indice -->

## Contexto: por qué y para quién
- Contrato-programa «Manifiestan» 4: LGCA suma al servicio público esencial lo digital (a petición, podcast, usuario de plataformas de vídeo, TV conectada).
- Contrato-programa «Manifiestan» 5 / cláusula 3ª pto.46: **Canal Sur Media**, dirección específica, coordina OTT, podcast, web, redes, apps.
- Contrato-programa cláusula 3ª pto.45: plataforma propia streaming **Canal Sur Más**; pto.48: propio dominio web + posición proactiva en redes.
- Carta art.7 (Expansión digital): 7.1 expansión prioritaria en digital; 7.2 refuerzo en redes/plataformas de vídeo conforme LGCA; 7.6 TDT HD exclusiva desde 14-02-2024.
- Reuters, *Digital News Report 2026*: redes/vídeo 54 % vs webs propias 51 % como vía de acceso a noticias (primera vez); 77 % ve vídeo informativo semanal; consumo en webs propias baja 5 pp.

## Formatos verticales
- YouTube ayuda «Resoluciones y relaciones de aspecto» (25-09-2026): estándar ordenador 16:9; vertical añade relleno; **no** añadir barras negras.
- Resoluciones 16:9: 4K 3840×2160, 2K 2560×1440, HD 1920×1080/1280×720; por encima 8K 7680×4320 (compatibilidad retirada 2022 entre 4K-8K).
- Página no da resolución vertical: se toma girando el cuadro (HD vertical 1080×1920).
- YouTube ayuda Shorts: subido desde 15-10-2024, vertical/cuadrado ≤3 min = **Short**; antes de esa fecha, vídeo largo; para evitar Short, usar 16:9.
- Resolve manual cap.41 p.860: líneas de tiempo propias (desmarcar *Use Project Settings*) para varias entregas.
- Resolve cap.127 p.3119: guías «Social Media» 1:1, 4:5, 9:16, 1.91:1, 16:9; zonas seguras Action/Title siguen sirviendo para móvil/redes.
- Oficio: reencuadre plano a plano (no recorte fijo al centro); rodar abierto/UHD da margen; rótulos rehechos para vertical, fuera de zonas tapadas por la app; sin franjas negras, se sustituye o pantalla partida.

## Clips
- Oficio: «clip» en redes = pieza corta publicada sola; sin definición en norma leída (distinto del clip de línea de tiempo, tema 3).
- LGCA 2.18 «Programa televisivo»: conjunto de imágenes, «**con independencia de su duración**»; incluye «**vídeos cortos**».
- Manual RTVE 4.1 (pauta de oficio): cada pieza debe consultarse independiente, sentido propio.
- Manual RTVE 4.3.2/4.3.3: vídeo formato único o de apoyo; evitar vídeos de recurso; preferible el corte concreto.
- Oficio: clip lleva contexto propio (rótulo/subtítulo); se corta por unidad de sentido; duración la manda la salida (Short ≤3 min, TikTok <2 min); cada clip = fichero/publicación propios con derechos (tema 10).
- Resolve cap.187 p.4211: marcar rango con I/O; **Single Clip** renderiza el rango elegido; **Individual Clips** ajusta a cortes de plano y no admite parciales.
- Identificador (tema 18 Realización RTVE, oficio): localizar en archivo masivo; referencia sin ambigüedad entre sistemas; sobrevive a cambios de nombre/ruta.

## Miniaturas
- YouTube ayuda «Miniaturas personalizadas» (25-09-2026): subir propia requiere cuenta verificada; Shorts sólo desde YouTube Studio en ordenador.
- Recomendado vídeo: 3840×2160, mín. 640 px ancho, 16:9, JPG/PNG, 50 MB ordenador / 2 MB móvil.
- Recomendado Short: 2160×3840, mín. 640 px alto, 9:16, JPG/PNG, 50 MB ordenador (móvil no consta).
- Trampa: miniatura 16:9 en vídeo vertical se sustituye por 4:5 autogenerada en portada/exploración/suscripciones.
- Normas comunidad: rechazo por desnudos, incitación al odio, violencia, contenido dañino; reincidencia = 30 días sin miniaturas o cancelación; límite diario de subidas variable.
- Oficio: fotograma propio del máster (no captura de pantalla); legible en pequeño; mismo formato que el vídeo; derechos de imagen de terceros; veracidad (art.9 LGCA) antes que técnica.
- Resolve cap.187 p.4187: casilla «Upload Thumbnail» sube imagen fija como miniatura de YouTube.

## Ritmo
- Ninguna norma ni fuente académica da pautas de ritmo vertical/redes; Libro de estilo CS (2004) no trata internet.
- *Digital News Report 2026*: duración difiere por plataforma; TikTok sesgado a <2 min; YouTube admite clips cortos a programas completos.
- Oficio: lo esencial en los primeros segundos (arranque fuerte); sonido a menudo apagado → subtítulo incrustado/rótulos parte del montaje; planos más cortos y cerrados que en emisión; una idea por pieza; cierre breve sin cabecera larga.
- Oficio: ritmo no autoriza cambiar el sentido (veracidad, temas 1 y 5); en Shorts con música, el tiempo permitido de la canción condiciona el corte.

## Distribución multiplataforma
- Cada salida (emisión, OTT, web, cada red) = fichero propio; RTVA no publica especificaciones por salida: se preguntan (oficio).
- YouTube «Codificación recomendada» (25-09-2026): MP4, sin listas de edición, moov al inicio; audio AAC-LC/Opus/Eclipsa a 48 kHz; vídeo H.264, progresivo, perfil alto, 2 B consecutivos, GOP cerrado, CABAC, VBR sin límite; croma 4:2:0; misma cadencia que grabación; SDR en BT.709.
- Entrelazado: se desentrelaza antes de subir (ej. 1080i60 → 1080p30; aplicación de la regla, 50 campos → 25p).
- Tasas de bits SDR: 4K 35-45/53-68 Mbps, 2K 16/24, 1080p 8/12, 720p 5/7,5 (estándar/alta cadencia).
- Audio: mono 128 kbps, estéreo 384 kbps, 5.1 512 kbps.
- Preajustes Resolve cap.187 pp.4187-4189: YouTube (MP4, H.264 High, AAC, normalizar audio, subida directa, capítulos desde marcadores, miniatura); TikTok (1920×1080, casilla vertical marcada, Encoding Auto); Vimeo/Dropbox (MP4, H.264 Auto, AAC).
- Sonoridad: Resolve normaliza al «estándar YouTube»; Blackmagic (cap.182 p.4140) cifra −14 LUFS (deducción, no texto de YouTube); emisión −23 LUFS EBU R128 (tema 4).
- CMS gestiona lo publicado (crear/organizar/publicar/retirar, permisos); metadatos: descriptivos, técnicos, de gestión, estructurales, de uso.
- Lista de reproducción: función editorial, estructural o de continuidad (RTVE, oficio). FTP: transferencias largas/reanudables/automatizadas (oficio).
- LGCA 2.13 «Servicio de intercambio de vídeos a través de plataforma»: sin responsabilidad editorial del prestador; organización por algoritmos. 2.20 «Vídeo generado por usuario».
- LGCA art.86: plataformas garantizan arts. 4, 6, 10, 12, 14, 15 y 7.1 respecto a contenidos distribuidos.
- art.88: protección de menores y del público (art.4.2 y 4.4); art.89.1: 9 medidas (cláusulas, notificación, calificación, verificación edad/control parental, reclamación, alfabetización, resolución de litigios).
- art.91.2.b y 91.3: declaración de comunicaciones comerciales por quien sube el vídeo; art.93.1: CNMC controla el cumplimiento.
- YouTube Shorts: música de Biblioteca de audio hasta 90 s (algunas 60/30) sin reclamación; desde 24-09-2026, Shorts de 1-3 min con Content ID activo ya no se bloquean automáticamente.
- Licencia de música/imagen de emisión puede no cubrir redes (tema 10).
- art.156.2 LGCA: conservar 6 meses desde la primera puesta a disposición del público (no sólo emisión); retirar de la web ≠ borrar del archivo.
- Accesibilidad por versión: subtítulo abierto en redes, cerrado en OTT/web (tema 11); LGCA art.101.1.g y LAA art.31.1.i.
