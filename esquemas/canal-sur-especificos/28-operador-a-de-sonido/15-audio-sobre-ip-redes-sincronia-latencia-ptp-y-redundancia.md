# Tema 15 del específico de Operador/a de Sonido · Audio sobre IP, redes, sincronía, latencia, PTP y redundancia

**Siglas**: RTVA; CSRTV; IP/IPv4/IPv6; TCP; UDP; RTP; SDP; SIP; IGMP; AES; SMPTE; IEEE; AES67; ST 2110-30; ST 2110-10; Dante; PTP/PTPv1/PTPv2; IEEE 1588; BMCA; NTP; PCM; SDI; QoS; DSCP; EEE; MAC; LAN; VCXO; TAI; ppm; Mbps/Gbps; ms/µs.

Esqueleto para repasar, no resumen: cada línea remite al dato del tema, no lo sustituye.

<!-- indice --><!-- /indice -->

## Audio sobre IP

- Matriz clásica: límite duro, un cable por señal; red IP: límite = ancho de banda, un cable por equipo (oficio).
- Audio en tiempo real va en UDP, no TCP: UDP no reintenta, retardo bajo y predecible; paquete tarde = inútil (oficio).
- RTP sobre UDP; «TCP/IP» = familia de protocolos, no protocolo de transporte (oficio).
- Dante: sistema propietario de Audinate, audio + control por la misma red; se gestiona con Dante Controller.
- Encaminar = suscribirse: canal Rx asociado a canal Tx («subscription»); canal nombrado equipo@canal (Audinate).
- Suscripción viaja en flujos; canal en gris = formato incompatible (p. ej. muestreo), no avería (Audinate).
- AES67: norma de INTEROPERABILIDAD, no sustituye a Dante; terreno común entre marcas (Audinate).
- ST 2110-30:2025 cita como referencia AES67-2023 (texto AES67 no leído).
- Dante en modo AES67: hasta 8 canales a 48/96 kHz; entre equipos Dante se usa protocolo nativo aunque AES67 esté activo (Audinate).
- AES67 y ST 2110-30 exigen PTPv2; dominio AES67 fijo en 0 (Audinate).
- Prefijo multicast del receptor debe coincidir con el del flujo AES67, si no: suscripción aparente, sin audio (Audinate).
- ST 2110-30:2025 (revisión de 2017): transporte RTP en tiempo real de PCM por referencia a AES67; audio comprimido fuera de alcance.
- Conforme a AES67 y su SDP (RFC 8866); SIP no obligatorio en receptores (ST 2110-30).
- 48 kHz obligatorio («shall»); 44,1 y 96 kHz recomendables («should») (ST 2110-30).
- Nivel A obligatorio para todo emisor y receptor (ST 2110-30).
- Niveles de emisor (tabla 2): A 48 kHz/1 ms/1-8 canales; AX 96 kHz/1 ms/1-4; B 48 kHz/125 µs/1-8; BX 96 kHz/125 µs/1-8; C 48 kHz/125 µs/9-64; CX 96 kHz/125 µs/9-32.
- Receptores (tabla 3), más exigentes: deben admitir todas las combinaciones del nivel declarado; C no admite 96 kHz, CX sí todas (ST 2110-30).
- SDI: ≥16 canales embebidos; para nivel A se agrupan en varios flujos AES67 (ST 2110-30).
- Orden de canales en SDP: símbolos M, DM, ST, LtRt, 51, 71, 222, SGRP, U01-U64; ejemplo «channel-order=SMPTE2110.(51,ST)» (ST 2110-30).

## Redes

- Unicast: punto a punto, una copia por destino, ~4 canales por flujo; multicast: una copia, hasta 64 canales por flujo, consume ancho aunque no haya receptores (Audinate).
- Dante por defecto unicast; receptor prefiere multicast si está disponible; multicast sin filtrar inunda la red (Audinate).
- 100 Mbps se satura fácil con multicast: usar sólo si hay buena razón (Audinate).
- Familia SMPTE: unicast (RFC 791) y multicast con IGMP (RFC 3376) obligatorios; IPv6 recomendable, no obligatorio (ST 2110-10).
- Conmutador de red: gestionable, con QoS, soporte PTP y control de suscripciones si hay multicast (oficio).
- IGMP *snooping*: bloquea multicast salvo puerto que lo pidió (Audinate).
- DSCP: campo IP para clasificar/priorizar tráfico (QoS); PTP con prioridad alta (Audinate).
- Gigabit preferido sobre 100 Mbps en elección de reloj; con 100 Mbps la latencia mínima es 1 ms (Audinate).
- EEE mal implementado y enlaces sobrecargados desestabilizan el reloj (Audinate).
- Wi-Fi y multicast incompatibles: pasar a unicast, reducir multicast o filtrar; Dante no admite audio/vídeo por Wi-Fi (Audinate).
- Límite UDP estándar: 1.460 octetos (incluye cabecera UDP de 8 + RTP); extendido: 8.960, optativo, no usado por ST 2110-30 (ST 2110-10).
- 1.460 = 1.500 (trama Ethernet) − 40 (cabecera IPv6, mayor de las dos) (ST 2110-10, anexo A).
- Emisor no puede fragmentar paquetes IP (ST 2110-10).
- Con 24 bits/muestra, audio por paquete = 1.152 octetos en niveles A, AX, C y CX (cálculo).
- Caudal de un canal = muestreo × profundidad de bits; 48 kHz/24 bits = 1,152 Mbps (cálculo).
- Ejemplo 32 canales bidireccionales, 48 kHz/24 bits: 1,152 × 32 = 36,9 Mbps; ×2 = 73,7 Mbps (cálculo).
- 16 bits en vez de 24: 49,2 Mbps para 32 canales (cálculo).
- 10 canales unicast: 3 flujos (4+4+2); caudal en crudo 11,5 Mbps, real mayor por cabeceras (Audinate/cálculo).
- Sobrecarga de cabeceras (Ethernet/IP/UDP/RTP) no se cifra: depende de implementación; Dante Controller muestra tráfico aproximado por interfaz (Audinate).

## Sincronía

- Cada equipo tiene oscilador propio; sin reloj común, sobra/falta muestra → chasquido periódico (Audinate).
- Seguidor corrige frecuencia al líder («offset»); límite de corrección = «pull range»; si se excede, pierde sync y se silencia (Audinate).
- Inestabilidad: enlaces sobrecargados, EEE mal implementado, reloj líder derivado de word clock externo inexacto (Audinate).
- Avisos Dante Controller: Clock Sync Warning, Clock Sync Unlocked (silenciado automático), Clock Sync Locked; histograma de desfase (Audinate).
- ST 2110-10: reloj de referencia común por PTP (IEEE 1588-2008), proveerlo recomendable, admitirlo obligatorio para todo equipo.
- Reloj interno (VCXO de a bordo) o externo (word clock del equipo anfitrión) (Audinate).
- «Enable Sync To External» convierte al equipo en líder PTP, salvo que otro tenga «Preferred Leader» (Audinate).
- Trampa: si A usa reloj externo y B es Preferred Leader sin la misma fuente externa, A pierde sync y se silencia (Audinate).
- Sincronía entre flujos: por comparación de marcas de tiempo RTP en el receptor (ST 2110-10).
- Época SMPTE: 1-I-1970 00:00:00 TAI, igual a la época PTP del IEEE 1588-2008 (ST 2059-1).
- *Pull-up/down* (p. ej. +4,1667% de 24 a 25 fps) crea dominio de reloj propio, con su PTP dedicado; hasta 5 dominios simultáneos (Audinate).
- Equipos de distinto dominio de reloj no intercambian media entre sí; aviso «Mismatched clock domains» (Audinate).

## Latencia

- Latencia = tiempo entre muestreo del emisor y reproducción del receptor; se compensa en el receptor, fijada por ajuste de latencia (Audinate).
- Receptor reproduce según marca de tiempo + latencia fijada; latencia debe superar el peor retraso de red, si no, se pierde el paquete (oficio/Audinate).
- Valor por defecto Dante: 1 ms, válido para red grande (núcleo gigabit, hasta 10 saltos, enlaces de 100 Mbps a los equipos) (Audinate).
- Mínimo en redes pequeñas todo gigabit: hasta 150 µs para equipos muy rápidos (p. ej. tarjetas PCIe) (Audinate).
- Con puerto de 100 Mbps, mínimo 1 ms; menos → error «Tx Scheduler Failure» (Audinate).
- Se ajusta en el receptor; negociación automática receptor-emisor para evitar pérdida de paquetes; multicast fijado a mínimo 1 ms (Audinate).
- Si emisor y receptor difieren, se usa la mayor de las dos, por flujo (Audinate).
- Problema de la latencia = destiempo (con imagen, otro camino de audio, sonido directo), no el retardo en sí (oficio).
- Alta latencia: margen en redes grandes, riesgo de desfase con imagen/otro camino; baja: mínimo retardo, riesgo de pérdida/chasquido si la red no es toda gigabit pequeña (oficio).
- En ST 2110-30, equivalente = tiempo de paquete: 1 ms en A/AX, 125 µs en B/BX/C/CX; retardo mínimo que se suma al de red y búfer (cálculo).
- Dos caminos del mismo audio con latencias distintas → filtro en peine al sumarse desfasados (oficio, tema 1).

## PTP

- PTP reparte el reloj común por la red; norma IEEE 1588-2008 (texto no leído); genera jerarquía con un reloj *grandmaster* (ST 2059-2).
- Todos los equipos Dante usan PTP para sincronía muestra-exacta (Audinate).
- PTP mide también el retardo de camino: mecanismo petición-respuesta por defecto, opcional el de pares (ST 2059-2).
- No confundir con NTP (reloj de ordenadores); PTP es el de audio/vídeo; cifras de precisión no dadas (IEEE 1588 no leído).
- Nombres actuales: *leader* (antes *master*), *follower* (antes *slave*), *grandmaster* = fuente última del dominio (ST 2059-2).
- Elección de líder en Dante, por orden: equipos con entrada de reloj (word clock/AES3); conexión gigabit sobre 100 Mbps; MAC más baja como desempate (Audinate).
- Se puede forzar con «Preferred Leader»; con varios, gana MAC más baja; «PTP Follower Only» impide ser *grandmaster* (Audinate).
- Preferred Leader no soportado en modo ST 2110-30 ni AES67 Manual; sí en AES67 Auto (Audinate).
- Perfil SMPTE: elección por BMCA del IEEE 1588 (subcláusulas 9.3.2-9.3.4), con *priority1*/*priority2* configurables (ST 2059-2).
- Equipos que no deben ser líder: *defaultDS.slaveOnly* = TRUE (ST 2110-10).
- Dos versiones: PTPv1 (Dante por defecto) y PTPv2 (se activa con RTP); AES67 y ST 2110-30 exigen PTPv2 (Audinate).
- Dominio AES67 fijo en 0; PTPv1 multicast desactivado por defecto en ST 2110-30/AES67 Manual, riesgo si hay equipos sólo PTPv1 (Audinate).
- Prioridad DSCP: EF por defecto en paquetes PTPv2 (norma AES67); CS7 mayor prioridad, recomendado para flujos Dante (Audinate).
- Perfil identificador 68-97-E8-00-01-00; basado en IEEE 1588-2008 (ST 2059-2).
- Valores por defecto del perfil SMPTE: priority1/2 = 128 (0-255); domainNumber = 127 (0-127); logAnnounceInterval = 0 (−3 a +1); announceReceiptTimeout = 3 (2-10); logSyncInterval = −3 (−7 a −1) (ST 2059-2).
- Intervalo corto de Sync = sincronía rápida; seguidores deben admitir *one-step* y *two-step*; *grandmaster* ≤ ±5 ppm del segundo SI (ST 2059-2).
- Dominio SMPTE (127) ≠ dominio AES67 (0); mensajes deben ajustarse a AES67 si se intercambia con esos equipos, según AES-R16-2016 (no leído) (ST 2110-10).

## Redundancia

- Dante: dos interfaces, primaria y secundaria, en dos redes físicas distintas; secundaria no comunica con primaria (Audinate).
- Si hay red secundaria conectada, redundancia automática; mismos datos por las dos redes a la vez; ante fallo de una, sigue la otra (Audinate).
- Primaria y secundaria deben ir a la misma velocidad de enlace; equipos sin redundancia sólo a la primaria (Audinate).
- Reloj en redundancia: cada red tiene su líder PTP, normalmente el mismo equipo en ambas; si no, un puente sincroniza ambas redes (Audinate).
- ST 2022-7: streams RTP redundantes idénticos por caminos distintos, reconstrucción sin cortes al nivel de datagrama.
- Emisor transmite al menos dos flujos idénticos (cabecera y payload RTP iguales); ejemplos citados: ST 2110-30, ST 2110-40 y AES67 (ST 2022-7).
- En familia ST 2110, redundancia obligada por ST 2022-7 según apartado 8.5 de la ST 2110-10.
- Clases de receptor por diferencia máxima de retardo (PD): A ≤10 ms; B ≤50 ms; C ≤450/150 ms (SBR/HBR); D ≤150 µs (ST 2022-7).
- Audio cae en SBR (<270 Mbit/s); 64 canales del nivel C ≈ 74 Mbit/s (cálculo).
- No consta en Audinate que la redundancia nativa de Dante cumpla la ST 2022-7 (dato no dado).
- Práctica: secundaria en conmutador distinto, para que ningún fallo único corte las dos redes; redundancia de red no sustituye la de equipos emisores (oficio).
