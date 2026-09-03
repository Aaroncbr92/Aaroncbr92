# Esquema · Gestión Administrativa 10: la red Internet

Esqueleto para repasar. Todo desarrollado en el tema.

**Siglas**: protocolo de control de transmisión y protocolo de internet
(**TCP/IP**), protocolo de transferencia de hipertexto (**HTTP**) y su versión segura (**HTTPS**),
sistema de nombres de dominio (**DNS**), localizador uniforme de recursos (**URL**), protocolo de
configuración dinámica de anfitrión (**DHCP**), protocolo de transferencia de ficheros (**FTP**),
protocolo simple de transferencia de correo (**SMTP**), protocolo de oficina de correos (**POP3**),
protocolo de acceso a mensajes de internet (**IMAP**), red de área local (**LAN**), red privada
virtual (**VPN**), la Red Informática Mundial (**WWW**), seguridad de la capa de transporte
(**TLS**), proveedor de acceso a internet (**ISP**), el protocolo de internet a secas (**IP**) y la
transferencia segura de ficheros (**SFTP**).

<!-- indice -->

## Índice

- [Internet ≠ web](#internet--web)
- [Para conectarse hacen falta](#para-conectarse-hacen-falta)
- [Direcciones](#direcciones)
- [Protocolos](#protocolos)
- [Navegadores](#navegadores)
- [Servicios avanzados](#servicios-avanzados)
- [Seguridad](#seguridad)
- [La única pregunta](#la-única-pregunta)

<!-- /indice -->

## Internet ≠ web

**Internet** es la red de redes sobre **TCP/IP**. **La web es uno de sus servicios**, el que usa
HTTP. También lo son correo, transferencia de ficheros, mensajería y voz sobre IP.

## Para conectarse hacen falta

1. **Acceso contratado** con un proveedor.
2. **Módem-router**: el módem adapta la señal, el router encamina y reparte por **DHCP**.
3. **Equipo con interfaz de red.**

**No sirven**: un servidor web (es para **publicar**), el sistema operativo (**usa** la conexión, no
la establece), un proyector.

## Direcciones

- **IP**: IPv4, cuatro octetos; IPv6, ocho grupos hexadecimales.
- **DNS**: traduce nombre → dirección. **Manipularlo es el *pharming*.**
- **URL**: esquema · anfitrión · ruta · puerto · parámetros · fragmento.

## Protocolos

| **HTTP/HTTPS** | web; el segundo cifrado con **TLS** |
| **DNS** | nombres a direcciones |
| **DHCP** | configuración automática |
| **FTP/SFTP** | ficheros |
| **SMTP** | **enviar** correo |
| **POP3 / IMAP** | **recibir**; **IMAP deja el buzón en el servidor** y sincroniza |

## Navegadores

Barra de direcciones y búsqueda · pestañas · historial · **favoritos (guardan la dirección, no la
página)** · descargas · **navegación privada: no guarda datos en el equipo, pero no da anonimato** ·
**vínculos**, la pieza del hipertexto.

## Servicios avanzados

- **Videoconferencia**: manda la **latencia**, más que la velocidad bruta.
- **Tele-formación**: **síncrona** (directo) y **asíncrona** (a su ritmo).

## Seguridad

- **HTTPS y candado dicen cómo viaja la información, no a quién llega.** Un sitio fraudulento puede
  tener certificado.
- Cortafuegos · **VPN** (túnel cifrado) · **cookies** técnicas y de seguimiento · actualizar el
  navegador.

## La única pregunta

34: hace falta **un módem o router**.
