# Esquema · Tema 4 del específico de Técnica Informática · Internet: origen, servicios y protocolos seguros

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes · `[exam]` = opciones
del propio cuadernillo. **Siglas**: el protocolo de transferencia de hipertexto (**HTTP**) y su
versión segura (**HTTPS**); la capa de conexión segura (**SSL**) y su sucesora, la seguridad de la
capa de transporte (**TLS**); el de transferencia de ficheros (**FTP**); el sistema de nombres de
dominio (**DNS**); el simple de transferencia de correo (**SMTP**), el de acceso a mensajes de
internet (**IMAP**) y el de oficina de correos (**POP3**); el intérprete de órdenes seguro (**SSH**) y
la transferencia de ficheros sobre él (**SFTP**); el acceso múltiple por detección de portadora con
detección de colisión (**CSMA/CD**), que sale como opción falsa; y el localizador uniforme de recursos
(**URL**).

**Cabecera.** Enunciado: punto 5 del anexo · **3 preguntas** · **ninguna lleva figura** · **las tres
son de lo mismo: el par de protocolos web y su versión cifrada** · **el punto de mejor rendimiento por
minuto de todo el temario: dos números y un nombre propio.**

<!-- indice -->

## Índice

- [El par de puertos](#el-par-de-puertos)
- [La historia, con una salvedad](#la-historia-con-una-salvedad)
- [Qué añade la capa segura](#qué-añade-la-capa-segura)
- [Los servicios y sus puertos](#los-servicios-y-sus-puertos)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El par de puertos

- **PREGUNTA 26** · `[exam]` · **El puerto estándar de HTTP es el 80.**
- **PREGUNTA 60** · `[exam]` · **El de HTTPS es el 443.**

| Protocolo | Estándar | Alternativo corriente |
|---|---|---|
| **HTTP** | **80** ✔ | **8080** |
| **HTTPS** | **443** ✔ | **8443** |

- **SE APRENDEN COMO PAREJA**, porque **las falsas de cada una son las respuestas de la otra.**
- **QUÉ SON 8080 Y 8443** · `[of]` · **los que se usan cuando el servicio no puede abrir los
  estándares**: **por debajo del 1024 hace falta ser administrador para escuchar.** **Un servidor de
  aplicaciones arrancado por un usuario corriente escucha en 8080**, y un intermediario lo publica
  después en el 80.
- **EL 25 QUE OFRECE LA PRIMERA ES EL DEL CORREO SALIENTE**, de otro servicio.

## La historia, con una salvedad

- **PREGUNTA 71** · `[exam]` · **El protocolo creado por Netscape en 1994 para asegurar la navegación
  web es HTTPS.**
- **LA SALVEDAD QUE EL TEMARIO AÑADE Y LA RESPUESTA OFICIAL NO HACE**: **lo que Netscape creó en 1994
  fue SSL**; **HTTPS es el resultado de meter HTTP dentro de esa capa.** **La oficial sigue siendo la
  correcta de las cuatro** —DNS, FTP y CSMA/CD no aseguran nada.

| Año, aproximado | Qué apareció |
|---|---|
| **1994** | **SSL**, de Netscape, para cifrar la conexión del navegador |
| **1995** | **SSL 3.0**, la versión que se generalizó |
| **1999** | **TLS 1.0**, que toma el relevo con otro nombre |
| **Hoy** | **TLS 1.2 y TLS 1.3.** **Todas las versiones de SSL están desaconsejadas** |

- **EL AVISO DE NOMENCLATURA**: **quien dice «certificado SSL» quiere decir certificado para TLS.**

## Qué añade la capa segura

- **HTTPS NO ES OTRO PROTOCOLO**: **es el mismo HTTP hablado dentro de un túnel cifrado.**

| Qué aporta | Qué significa |
|---|---|
| **Confidencialidad** | **Nadie por el camino puede leerlo** |
| **Integridad** | **Nadie puede modificarlo sin que se note** |
| **Autenticación del servidor** | **El cliente comprueba con el certificado que habla con quien cree** |

- **LO QUE NO APORTA, Y ES LA CONFUSIÓN MÁS EXTENDIDA**: **no dice que el sitio sea de fiar; dice que
  la conexión con ese sitio es privada.** **Un sitio fraudulento puede tener certificado válido**, y
  millones lo tienen.
- **EL CERTIFICADO EN TRES LÍNEAS**: **el servidor presenta uno firmado por una autoridad de
  certificación; el navegador comprueba que esa autoridad está en su lista de confianza y que el
  nombre coincide con el del sitio; si cuadra, negocian clave de sesión y todo va cifrado.**

## Los servicios y sus puertos

| Servicio | Protocolo | Puerto |
|---|---|---|
| **Web** | **HTTP / HTTPS** | **80 / 443** |
| **Nombres de dominio** | **DNS** | **53** |
| **Correo saliente** | **SMTP** | **25**, y **587** desde el cliente |
| **Correo entrante** | **IMAP / POP3** | **143 / 110**, y **993 / 995** cifrados |
| **Ficheros** | **FTP**, desaconsejado, y **SFTP** | **21** y **22** |
| **Terminal remota** | **SSH**, y el desaconsejado **Telnet** | **22** y **23** |

- **EL PATRÓN QUE ORDENA LA COLUMNA DE LA DERECHA**: **casi todo tiene un puerto en claro y otro
  cifrado**, y **el cifrado es el que hay que usar.**
- **POR QUÉ FTP Y TELNET ESTÁN DESACONSEJADOS**: **mandan la contraseña en claro por la red.** **Sus
  sustitutos, SFTP y SSH, van los dos por el 22.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 26 | Puerto estándar de HTTP | c) 80 ✔ |
| 60 | Puerto estándar de HTTPS | c) 443 ✔ |
| 71 | Protocolo creado por Netscape en 1994 | b) HTTPS ✔ **·** con salvedad |

**Las tres oficiales son correctas** · **ninguna descansa en la plantilla** · **una lleva salvedad
declarada**: lo de 1994 fue SSL, y HTTPS es HTTP sobre esa capa. · **Aviso de estudio**: **el punto
entero cabe en dos números**, y **no conviene dedicarle más tiempo del que pide.**
