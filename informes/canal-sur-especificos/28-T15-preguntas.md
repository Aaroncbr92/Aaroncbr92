# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 4, preguntas tipo test

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.
Fecha: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Quince preguntas de cuatro opciones, teoría (T)
y aplicación práctica (P), repartidas por las seis rúbricas del enunciado. Clave en negrita. Cada una
se contesta **sólo con el tema**; cuando el tema no la tiene, se da la fuente de la clave (leída el
25-09-2026).

Resultado: **12 enteras, 0 a medias, 3 no**.

1. (T · Audio sobre IP) El audio en tiempo real sobre red viaja por norma general en: a) TCP, porque
   garantiza la entrega; **b) UDP, porque no espera retransmisiones**; c) TCP/IP; d) NTP.
   → **Entera**: «Qué protocolo lleva el audio: UDP».

2. (T · Audio sobre IP) Según la SMPTE ST 2110-30:2025, la frecuencia de muestreo que deben admitir
   todos los emisores y receptores es: a) 44,1 kHz; **b) 48 kHz**; c) 96 kHz; d) 48 y 96 kHz.
   → **Entera**: «SMPTE ST 2110-30» (44,1 y 96 kHz, «should»).

3. (P · Audio sobre IP) En Dante Controller un canal aparece en gris y no se puede encaminar. Lo más
   probable: a) un cable de red cortado; b) IGMP *snooping* desactivado; **c) emisor y receptor con
   formatos (p. ej. frecuencia de muestreo) incompatibles**; d) el equipo es *PTP Follower Only*.
   → **Entera**: «Dante, un sistema propietario».

4. (P · Audio sobre IP) Un equipo Dante se suscribe a un flujo AES67 de otra marca; la suscripción
   aparece correcta, pero no llega audio. Lo primero que se comprueba: a) la latencia del receptor;
   **b) que el prefijo multicast del receptor coincida con la dirección del flujo**; c) la versión de
   PTPv1; d) la velocidad del puerto secundario.
   → **Entera**: «AES67, la norma de interoperabilidad».

5. (T · Audio sobre IP) Un receptor que declara el nivel C de la ST 2110-30:2025 debe admitir:
   a) sólo 48 kHz, 125 µs y 9 a 64 canales; **b) también 48 kHz con 1 ms y 1 a 8 canales, y 125 µs
   con 1 a 64 canales**; c) 96 kHz con 125 µs y hasta 32 canales; d) cualquier tiempo de paquete.
   → **No**. El tema sólo da la tabla 2 (emisores). Fuente: ST 2110-30:2025, cl. 7 («receivers shall
   support all possible combinations of sampling clock rate, packet time and channel count within the
   ranges as defined in Table 3») y tabla 3 (nivel C: 48000/1000/1 to 8 y 48000/125/1 to 64).

6. (T · Redes) Según la guía de Dante Controller 4.18, un flujo multicast Dante puede llevar:
   a) 4 canales, como el unicast; b) 8 canales; **c) hasta 64 canales, según el tipo de equipo**;
   d) un número ilimitado.
   → **No**, y el tema dice lo contrario («La guía no da una cifra»). Fuente: Audinate DC 4.18,
   «About Transmit Flows»: «Multicast flows can be configured with up to 64 channels (depending on the
   Dante device type).»

7. (P · Redes) Caudal de audio, sin cabeceras, de 32 canales bidireccionales a 48 kHz y 24 bits:
   a) 36,9 Mbps; b) 49,2 Mbps; **c) 73,7 Mbps**; d) 147,5 Mbps.
   → **Entera**: «Las cuentas de ancho de banda».

8. (T · Redes) Límite estándar de tamaño del datagrama UDP de la ST 2110-10, que la ST 2110-30 impone
   al audio: a) 1.500 octetos; **b) 1.460 octetos**; c) 8.960 octetos; d) 9.000 octetos.
   → **Entera**: «El tamaño de los paquetes».

9. (P · Redes) Con IGMP *snooping* activado en el conmutador, el multicast: a) se reparte a todos los
   puertos; **b) sólo sale por los puertos cuyo equipo ha pedido unirse al grupo**; c) se convierte en
   unicast; d) se bloquea en todos los puertos.
   → **Entera**: «El conmutador de red».

10. (P · Sincronía) Un equipo Dante supera su margen de corrección de frecuencia (*pull range*)
    respecto al *leader*. Resultado: a) pasa a ser *leader*; **b) pierde la sincronía y se silencia
    automáticamente**; c) duplica su latencia; d) conmuta a la red secundaria.
    → **Entera**: «Por qué hace falta un reloj común».

11. (P · Sincronía) El equipo A tiene «Enable Sync To External» con el word clock de la casa y el B,
    sin esa fuente, está marcado *Preferred Leader*. Qué ocurre: a) A manda igualmente; b) los dos
    mandan en dominios distintos; **c) A pierde la sincronía con la red y acaba silenciado**; d) nada,
    B hereda el word clock.
    → **Entera**: «Reloj interno o reloj externo».

12. (P · Sincronía) Dos equipos Dante en la misma red, uno sin *pull-up/down* y otro a +4,1667 %:
    a) intercambian audio con un chasquido periódico; **b) no pueden enviarse ni recibirse audio: están
    en dominios de reloj distintos**; c) el de *pull-up* pasa a *leader*; d) Dante corrige la diferencia
    con la latencia.
    → **No**. El tema no trata los dominios de reloj por *pull-up/down*. Fuente: Audinate DC 4.18
    («Dante devices can only transmit media to, and receive media from other devices on the same clock
    domain […] cannot transmit media to, or receive media from any devices on the +4.1667% clock
    domain»; «Up to 5 separate clock domains can be supported at any one time»).

13. (P · Latencia) Una tarjeta en un puerto de 100 Mbps se ajusta a 0,5 ms y el receptor a 1 ms.
    a) El flujo va a 0,5 ms; **b) no es posible por debajo de 1 ms en 100 Mbps («Tx Scheduler
    Failure»), y en todo caso el flujo tomaría la mayor de las dos, 1 ms**; c) 0,75 ms; d) 1,5 ms.
    → **Entera**: «Los valores de Dante».

14. (T · PTP) Dominio PTP de AES67 en Dante y dominio por defecto del perfil SMPTE ST 2059-2:
    **a) 0 y 127**; b) 127 y 0; c) 0 y 0; d) 1 y 128.
    → **Entera**: «Las versiones: PTPv1 y PTPv2» y «El perfil SMPTE: ST 2059-2».

15. (P · Redundancia) Un equipo Dante con redundancia tiene el primario a 1 Gbps. El secundario:
    a) al mismo conmutador, a 100 Mbps; **b) a una segunda red separada, también a 1 Gbps**; c) a
    cualquier puerto libre de la primaria; d) no se conecta si el equipo no es *leader*.
    → **Entera**: «La redundancia de Dante» y «Aplicación práctica de la redundancia».
