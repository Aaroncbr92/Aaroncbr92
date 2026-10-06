# Puesto 29 · Tema 13 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`.
Quince preguntas tipo test de cuatro opciones, repartidas por las rúbricas del enunciado; (AP) =
aplicación práctica. Se contestan **sólo con el tema**; veredicto: entera, a medias o no.

1. (Arquitectura) Según el RFC 1122, la arquitectura de Internet se organiza en: a) siete capas;
   b) cinco capas; c) cuatro capas: aplicación, transporte, internet y enlace; d) tres capas.
   → **c**. § 1, «Las capas». **Entera** (incluida la salvedad de que el RFC une sólo dos capas OSI).

2. (Origen) ARPANET pasó de NCP a TCP/IP: a) en septiembre de 1969; b) el 1 de enero de 1983, de
   golpe; c) en 1985, con NSFNET; d) en 1990. → **b**. § 1, «El origen». **Entera**.

3. (Servicios) Un cliente obtiene su dirección IPv4 por DHCP. El orden de los mensajes es:
   a) DHCPREQUEST, DHCPOFFER, DHCPDISCOVER, DHCPACK; b) DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, DHCPACK;
   c) DHCPOFFER, DHCPDISCOVER, DHCPACK, DHCPREQUEST; d) DHCPDISCOVER, DHCPACK, DHCPOFFER, DHCPREQUEST.
   → **b** (RFC 2131). El tema define DHCP y dice qué entrega, pero no da los mensajes ni el
   intercambio, ni los puertos 67/68. **No**.

4. (HTTP) Es idempotente pero no seguro: a) GET; b) PUT; c) POST; d) OPTIONS. → **b**. § 2, tabla de
   métodos. **Entera**.

5. (TLS) En TLS 1.3 (RFC 9846): a) se permite negociar TLS 1.0 por compatibilidad; b) todos los
   mensajes de negociación posteriores al ServerHello van cifrados; c) se mantiene el intercambio RSA
   estático; d) el cliente se autentica siempre. → **b**. § 2, «Las versiones» y «TLS». **Entera**.

6. (Navegadores, seguridad) El atributo de cookie que impide que la lea el JavaScript de la página
   es: a) Secure; b) HttpOnly; c) Domain; d) Expires. → **b** (RFC 6265). El tema define la cookie y
   distingue propias y de terceros, pero no da sus atributos (Secure, HttpOnly, SameSite, Expires).
   **No**.

7. (Navegadores, privacidad) Nivel de prevención de seguimiento de Edge marcado como recomendado:
   a) Básico; b) Equilibrado; c) Estricto; d) Desactivado. → **b**. § 3, tabla de Edge. **Entera**.

8. (Cabeceras, AP) Un datagrama IPv4 llega con IHL = 7. Su cabecera mide: a) 7 octetos; b) 20;
   c) 28, con 8 de opciones; d) 60. → **c**. § 4 y supuesto 5. **Entera**.

9. (Subredes, AP) Del equipo 172.16.5.70/27, la dirección de subred y la de difusión son:
   a) .0 y .255; b) .64 y .95; c) .64 y .127; d) .32 y .63. → **b**. § 4: tabla de prefijos (/27 = 32
   direcciones), método por bloques y ejemplo de partición. **Entera**.

10. (Transición) Mecanismo que encapsula IPv6 en UDP sobre IPv4 para atravesar NAT: a) 6to4;
    b) Teredo; c) DS-Lite; d) NAT64. → **b**. El tema sólo nombra 6to4, Teredo y DS-Lite con su
    bloque (lo declara en «Lo que este tema no da»); no dice qué hace cada uno. Descarta NAT64 (sí
    explicado), pero no permite elegir entre los otros tres. **A medias**.

11. (Normas IEEE 802) La norma que añadió Gigabit Ethernet sobre par trenzado (1000BASE-T) es:
    a) IEEE 802.3u; b) IEEE 802.3ab; c) IEEE 802.3z; d) IEEE 802.1Q. → **b**. El tema da 1000BASE-T y
    su uso de los cuatro pares, pero ninguna enmienda de 802.3 (802.3u, z, ab, af/at/bt de PoE…).
    **No**.

12. (Control de acceso al medio) Al detectar una colisión, una estación Ethernet con CSMA/CD:
    a) sigue transmitiendo y la repite al final; b) para, emite una señal de atasco y reintenta tras
    una espera aleatoria creciente; c) espera el testigo; d) envía una trama RTS. → **b**. § 5.
    **Entera**.

13. (802.11, estándares, AP) En 2,4 GHz, ¿qué canales de 20 MHz no se solapan en la práctica en
    Europa? a) 1, 6 y 11 (o 1, 5, 9 y 13); b) 1, 2 y 3; c) 36, 40 y 44; d) todos se solapan. → **a**.
    El tema lo declara fuera («Lo que este tema no da»: falta el CNAF). **No**.

14. (Seguridad 802.11) WPA3-Personal sustituye la clave precompartida de WPA2 por: a) TKIP;
    b) SAE (autenticación simultánea de iguales); c) EAP-TLS; d) WEP. → **b**. El tema quitó en la
    verificación la atribución de SAE por falta de fuente; da de WPA3-Personal sólo la protección
    frente a la adivinación de contraseñas. **No**.

15. (802.1X, AP) En 802.1X con un punto de acceso y NPS: a) el punto de acceso es el solicitante;
    b) el punto de acceso es el autenticador y cliente RADIUS, NPS el servidor (puerto 1812);
    c) NPS es el autenticador; d) el equipo del usuario es cliente RADIUS. → **b**. § 6, «La
    autenticación 802.1X». **Entera**.

## Recuento

Entera: 9 (1, 2, 4, 5, 7, 8, 9, 12, 15). A medias: 1 (10). No: 5 (3, 6, 11, 13, 14).
