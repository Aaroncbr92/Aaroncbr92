# Tema 13 del específico de Cámara Operador · Producción móvil y transmisión

**Siglas**: Radio y Televisión de Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Canal Sur Televisión (**CSTV**); protocolo de Internet (**IP**); red inalámbrica local (**wifi**); tarjeta de abonado (**SIM**); redes móviles (**5G/4G**); interfaz digital serie (**SDI**); unidad de control de cámara (**CCU**); retorno de programa sin la propia fuente (**N-1**); periodismo electrónico por satélite (**SNG/DSNG**); Sector de Radiocomunicaciones de la UIT (**UIT-R**); Society of Motion Picture and Television Engineers (**SMPTE**); Advanced Media Workflow Association (**AMWA**), especificaciones **NMOS**; Internet Engineering Task Force (**IETF**), documentos **RFC**; protocolo de tiempo real (**RTP**); protocolo de tiempo de precisión (**PTP**, IEEE 1588); modulación por impulsos codificados (**PCM**); transporte seguro y fiable (**SRT**); interfaz de dispositivos en red (**NDI**); *streaming* en directo por HTTP (**HLS**); protocolo de mensajería en tiempo real (**RTMP**) y su versión segura (**RTMPS**); multiplexación **OFDM/COFDM**; televisión digital terrestre (**DVB-T**).

Esqueleto, no resumen. Telegrama, fuente delante de cada línea; se quita explicación, no el dato. Vigente el **24/09/2026**. Sin norma jurídica: normas técnicas (SMPTE, UIT-R, ETSI), especificaciones (AMWA NMOS, SRT, NDI, RFC, RTMP), documentación de fabricante y de la casa (Libro de estilo, Contrato-programa), y oficio.

<!-- indice -->

## Índice

- [Directo o diferido](#directo-o-diferido)
- [Qué pide la casa](#qué-pide-la-casa)
- [Mochilas](#mochilas)
- [Enlaces](#enlaces)
- [*Streaming*](#streaming)
- [Señales IP](#señales-ip)
- [Coordinación con control](#coordinación-con-control)
- [Fuentes citadas](#fuentes-citadas)
- [Lo que este tema no da](#lo-que-este-tema-no-da)

<!-- /indice -->

## Directo o diferido

- oficio — Producción móvil: fuera del centro, con equipos desplazados. Transmisión: llevarlo al centro. Eje: directo (caudal garantizado ya) / diferido (fichero, puede tardar).
- oficio — Caminos para sacar señal: microondas (línea de vista, directo) · satélite (exteriores remotos) · fibra contratada (previsto) · mochila celular (cobertura móvil) · fichero (la mayoría de piezas) · *streaming* (canales propios/redes).

## Qué pide la casa

- Libro de estilo RTVA (2004), Introducción — Recomendaciones periodísticas y métodos de trabajo; hay conductas obligatorias sin elección posible.
- Libro de estilo, 4.4 — Producción: **«planificación y asignación ordenada de recursos»** para grabaciones, transmisiones, enlaces, asistencias.
- Libro de estilo, 4.4.4 (paso 2) — Producción necesita desglose de asunto, espacio y formato: directos, enlaces, asistencias.
- Libro de estilo, 4.4.1 — Equipos desplazados se comunican con productores/editores ante eventualidad.
- Libro de estilo, 5.6 — Todo retraso fuera del centro se comunica a los editores.
- oficio — No consta manual operativo publicado de CSRTV sobre mochilas, enlaces o redes IP.

## Mochilas

- oficio — Agrega caudal de varias tarjetas móviles; permite llegar, conectar y emitir en directo con configuración simple.
- oficio — No promete: estabilidad total (red compartida se satura) · ausencia de retardo (inherente a la agregación) · funcionar sin cobertura.
- oficio — Vías de conexión: tarjetas de telefonía (habitual) · wifi (si hay red) · cable de red (más estable). No conecta por microondas ni «ondas hertzianas».
- LiveU, ficha LU800 (03/09/2026) — Hasta **14 conexiones**, **8 módems 5G/4G** dual SIM, **60 Mbps**, HEVC; hasta **4Kp60 10-bit HDR**, **16 canales de audio**; hasta **4 cámaras** sincronizadas (licencia PRO2/PRO4); envía ficheros editados; producción remota multicámara.
- oficio — Retardo: 1) se mide y se avisa al control · 2) retorno en N-1 para no oír la propia voz retrasada · 3) se graba siempre en cámara (única copia si cae el enlace).
- Blackmagic, manual ATEM (dic. 2024) — N-1: **«silenciar el audio de una entrada específica en la señal de retorno»**, evita que el presentador se distraiga con su voz retrasada.
- oficio — Cuentas: a 25 fps, 1 imagen=**40 ms** (1000÷25), 2=80 ms, 4=160 ms; a 50 fps, 1 imagen=**20 ms**. Regla: lo que llega antes se retrasa hasta lo más lento; el retardo de mochila no se compensa en mezclador.

## Enlaces

- oficio — Vías de contribución: fibra (calidad, sin imprevistos) · microondas (rápido, necesita visión directa) · satélite/DSNG (llega a cualquier sitio, coste y retardo) · mochila celular (barata, depende de cobertura) · redes de datos/FTTH (depende de terceros).
- UIT-R SNG.770-2 (01/2012), considerando c) / anexo 1, 1.1 — DSNG es temporal, escaso aviso, estaciones portátiles o fácilmente transportables.
- UIT-R SNG.770-2, anexo 1, 1.1 — Equipo DSNG manejable por **no más de 2 personas** en **~1 h**.
- UIT-R SNG.770-2, recomienda 8 / considerando g) — Circuitos de radiocomunicación bidireccionales antes y durante la transmisión.
- UIT-R SNG.770-2, anexo 1, 2.2.1 — Zona de servicio del enlace descendente debe incluir el lugar de recepción previsto.
- UIT-R SNG.770-2, recomienda 9 / considerando e) — Autorización del país del enlace ascendente; debe ser expeditiva.
- oficio — Contribución (hacia el centro, calidad alta, retardo mínimo) vs. distribución (hacia el espectador, retardo menos crítico). Todo lo externo entra por el control central: encamina, sincroniza, convierte, corrige niveles.
- oficio — Unidad móvil: control de realización sobre ruedas, cámaras por CCU y cable (triax/fibra); necesita su propio enlace de salida. Detalle en tema 3.
- oficio — Enlace inalámbrico de cámara: transmisor a la espalda, no es mochila (no agrega redes, es radioenlace propio).
- Domo, libro blanco COFDM — **«Coded Orthogonal Frequency-Division Multiplexing»**; muchas portadoras: una reflejada anula pocas, se recupera con corrección de errores; usada en cámaras inalámbricas frente a analógico/portadora única (multitrayecto, imagen rota sin visión directa).
- ETSI EN 300 744 V1.6.2 (2015-10), cláusula 4.1 — DVB-T: **«an OFDM system with concatenated error correcting coding»** (la «C» de COFDM).
- Domo, ficha Sapphire-BTX — Encoder 4K HEVC + modulador COFDM integrados; control de cámara y *tally*; audio analógico con alimentación; latencia de codificación típica **«35mS input to output»** (dato de fabricante, no de norma).

## *Streaming*

- oficio — Distribución continua: se consume mientras llega. Distinto de descarga (entera antes) y descarga progresiva (en orden, no se adapta a la red). Para directo: transmisión por secuencias (se adapta a la red).
- oficio — Dos usos: contribución (localización→centro, importa latencia baja sin pérdida) y distribución (centro→espectador, importa llegar a muchos y adaptarse).
- Ayuda de YouTube — Para emitir: **«URL del servidor y la clave de emisión»**; por defecto RTMP; ofrece RTMPS (TLS/SSL) y HLS.
- RTMP, especificación Adobe (21/12/2012), resumen — **«bidirectional message multiplex service over a reliable stream transport, such as TCP»**; no es norma ni RFC.
- RTMP, Adobe, 7.2.2.6 — Publicación **«live»**: **«Live data is published without recording it in a file.»**
- RFC 8216 (HLS, agosto 2017), resumen y estado — **«protocol for transferring unbounded streams of multimedia data»**; **«Category: Informational»**, vía independiente, no es *Internet Standards Track*.
- RFC 8216, 1 y 2 — Media Playlist con segmentos; **«adapt the bit rate… to maintain uninterrupted playback»**; versión 7 del protocolo; revisión en curso (draft-pantos-hls-rfc8216bis) sin sustituirla.
- Ayuda de YouTube — HLS más latencia que RTMP (segmentos vs. continuo); se elige para HDR o códecs incompatibles con RTMP.
- SRT, repositorio de referencia — **«ultra low (sub-second) latency»** para vídeo/audio en directo y transferencia de datos.
- draft-sharabayko-srt-01 (IETF, 07/09/2021), 1.1/1.2 — Sobre UDP; fiabilidad con **ARQ**, confirmaciones y gestión de latencia; modelo *listener/caller* como TCP.
- draft-sharabayko-srt-01, tabla de cifrado — AES **128/192/256** bits; contraseña 10-80 caracteres; latencia por defecto **120 ms**.
- oficio — SRT: código abierto, borrador IETF expirado (**«Informational»**, expiró 11/03/2022), no es RFC.
- Contrato-programa 2024-2026, cláusula 3.ª, 3.5, punto 46 — Canal Sur Media coordina OTT, pódcast, portales, redes sociales, apps móviles.
- Contrato-programa, 3.5, punto 45 — Plataforma propia **«Canal Sur Más»**, en todo dispositivo; pódcast en plataforma propia; acuerdos con terceros.
- Contrato-programa, 3.19, punto 103 — **«Se producirá y distribuirá 24 horas/día»** Canal Sur Más (OTT, protocolos IP); ámbito mundial según derechos de difusión.
- oficio — Qué protocolo/plataforma usa CSRTV para su distribución no consta en documento publicado.

## Señales IP

- SMPTE ST 2110-10:2022, introducción — Redes IP transportan vídeo, audio y metadatos; cada elemento de producción se encapsula por separado.
- SMPTE ST 2110-10, introducción — Familia basada en VSF TR-03/TR-04 y AES67.
- oficio — IP en tres sitios para el cámara: centro (ST 2110), calle (mochila/SRT), producción ligera (NDI).
- SMPTE, índice oficial ST 2110 — Título común **«Professional Media Over Managed IP Networks»**. Partes: **-10** *System Timing and Definitions* · **-20** *Uncompressed Active Video* · **-21** *Traffic Shaping…* · **-22** *Constant Bit-Rate Compressed Video* · **-30** *PCM Digital Audio* · **-31** *AES3 Transparent Transport* · **-40** *Ancillary Data* · **-41** *Fast Metadata* · **-43** *Timed Text… Captions*. No existe -50.
- oficio — Solo se han leído -10, -20 y -30; el resto, solo título.
- SMPTE ST 2110-10:2022, cláusula 1 — Flujos RTP referidos a reloj común, con marcas de tiempo para realinear.
- SMPTE ST 2110-20:2022, cláusula 1 — Vídeo activo sin comprimir por RTP/IP; metadatos técnicos por SDP.
- SMPTE ST 2110-30:2025, cláusula 1 — Audio PCM por RTP/IP, con referencia a AES67; excluye audio comprimido. Edición vigente 2025 (revisa 2017).
- SMPTE ST 2110-10, cláusula 7.2 — Reloj común por **IEEE 1588-2008 PTP**: distribución es **«should»** (recomendación); soporte del dispositivo es **«shall»** (obligación). Perfil ST 2059-2 no leído.
- SMPTE ST 2110-10, cláusula 8.5 — Redundancia: flujos duplicados según **ST 2022-7**, «may» (opcional).
- SMPTE ST 2110-10, cláusula 6.3 — Tamaño estándar UDP: **shall be 1460 octetos**; receptores obligados hasta ahí.
- SMPTE ST 2110-10, cláusula 6.4 — Límite extendido: **shall be 8960 octetos**, uso opcional («may transmit»).
- AMWA, índice NMOS — Familia de especificaciones de la AMWA para medios en red. ST 2110-10 remite a **IS-05** para gestión de conexiones.
- AMWA, índice NMOS — **IS-04** *Discovery & Registration* · **IS-05** *Device Connection Management* · **IS-07** *Event & Tally* (piloto por red) · **IS-08** *Audio Channel Mapping*.
- NDI, documentación — **«Network Device Interface»**; especificaciones IP propietarias; **«not a codec»**: admite SpeedHQ, AVC/HEVC; descubrimiento por **mDNS** o *Discovery Service*.
- oficio — Comparación: ST 2110 (SMPTE, es norma, red gestionada, PTP+ST 2022-7) · SRT (código abierto/borrador expirado, redes no gestionadas, ARQ+cifrado) · NDI (propietario, red ligera, SpeedHQ/H.264/HEVC).

## Coordinación con control

- Libro de estilo, 8.3 — **«La improvisación no tiene cabida»**; equipo coordinado (producción, realización, enlaces, informativos) prevé todo lo previsible.
- Libro de estilo, 8.1, punto 6 — Pacto del directo entre productor, cámara, técnicos de enlace, presentador, edición, realizador; reflejado en escaleta.
- Libro de estilo, 8.3.2 — **«Terminado el directo, en la despedida sólo habla el presentador.»**
- Libro de estilo, 8.3.2 — Enviado especial se coloca **«en un punto que permita al espectador reconocer… el lugar»**.
- oficio — Canales cámara-control: piloto (*tally*, saber si está en antena) · retorno de programa (en N-1) · intercomunicación · control remoto (por red).
- Blackmagic, manual ATEM — Piloto: **«luz roja… el operador sepa que está al aire»**; botón CALL hace parpadear la piloto de las cámaras conectadas.
- LiveU, ficha LU800 — Canales por la propia mochila: *Tally Light*, *Video Return*, *Audio Connect*, *IP Pipe* (control remoto de PTZ/CCU/intercom IP).
- oficio — Procedimiento: antes (pacto, baterías, tarjetas) · llegada (cobertura, encuadre, montaje) · prueba (imagen, audio, retorno N-1, intercom, piloto; medir y comunicar retardo) · espera (mantener señal y grabación) · en antena (piloto, correcciones mínimas) · incidencia (vía de reserva, seguir grabando, avisar de retraso) · después (mantener hasta cierre del control).
- oficio — Supuesto: directo con mochila en plaza; emplazamiento por cobertura y reconocimiento del lugar; conectar cámara-mochila-red; prueba con control; grabar en tarjeta; si se satura, decide el centro, no la calle; cierre solo del presentador.

## Fuentes citadas

- SMPTE ST 2110-10:2022, ST 2110-20:2022, ST 2110-30:2025.
- Recomendación UIT-R SNG.770-2 (01/2012).
- ETSI EN 300 744 V1.6.2 (2015-10), solo cláusula 4.1.
- AMWA NMOS (índice de especificaciones); SRT (repositorio de referencia y draft-sharabayko-srt-01); RFC 8216 (HLS); especificación RTMP de Adobe; documentación NDI.
- Documentación de fabricante: LiveU LU800, ATEM Blackmagic, libro blanco COFDM y Sapphire-BTX de Domo, ayuda de YouTube.
- Libro de estilo de Canal Sur (RTVA, 2004); Contrato-programa 2024-2026 RTVA.

## Lo que este tema no da

- Qué mochilas, enlaces y redes usa CSRTV, ni si sus instalaciones son SDI/ST 2110/NDI, ni si contribuye con SRT: no consta.
- Cifras de latencia real de mochila, satélite o NDI: no leídas.
- ST 2059-2 (perfil PTP) y partes ST 2110 distintas de -10/-20/-30: solo título.
- Protocolos de distribución más allá de HLS (resumen y §1-2) y RTMP (intro y *publish*): no leídos.
- ETSI EN 300 744 más allá de 4.1; detalle técnico de COFDM; bandas de frecuencia y régimen jurídico de enlaces: no leídos.
- Unidad móvil, cable de cámara, señal *pool* y piloto en plató → tema 3; formatos/ingesta/entrega → tema 7; relación con redacción/realización → tema 8; seguridad y transporte del equipo → tema 11; PRL en exteriores → tema 14.
