# Tema 4 del específico de Técnica Informática · Internet: origen, servicios y protocolos seguros

Las siglas de este tema, presentadas de entrada: el protocolo de transferencia de hipertexto
(**HTTP**) y su versión segura (**HTTPS**); la capa de conexión segura (**SSL**, *secure sockets
layer*) y su sucesora, la seguridad de la capa de transporte (**TLS**, *transport layer security*); el
protocolo de transferencia de ficheros (**FTP**); el sistema de nombres de dominio (**DNS**); el protocolo simple de
transferencia de correo (**SMTP**), el de acceso a mensajes de internet (**IMAP**) y el de oficina de
correos (**POP3**); el intérprete de órdenes seguro (**SSH**) y la transferencia de ficheros sobre él
(**SFTP**); el
acceso múltiple por detección de portadora con detección de colisión (**CSMA/CD**), que aparece como
opción falsa; y el localizador uniforme de recursos (**URL**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 5):
> «Internet. Origen, servicios, protocolos HTTP, HTTPS y SSL/TLS.»

**Tres preguntas.** **Y las tres son de lo mismo: el par de protocolos web y su versión cifrada.**

**Dos son de puerto y una es de historia**, lo que **convierte este punto en el más memorizable del
temario**: **con dos números y un nombre propio se contestan las tres.**

<!-- indice -->

## Índice

- [1. El par de puertos](#1-el-par-de-puertos)
- [2. La historia que el enunciado pide](#2-la-historia-que-el-enunciado-pide)
- [3. Qué añade la capa segura](#3-qué-añade-la-capa-segura)
- [4. Los servicios de internet que el enunciado nombra](#4-los-servicios-de-internet-que-el-enunciado-nombra)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. El par de puertos

**La pregunta 26**: **el puerto estándar de HTTP es el 80.** Ésa es la respuesta oficial.

**La pregunta 60**: **el puerto estándar de HTTPS es el 443.** Ésa es la respuesta oficial.

---

**Son la misma pregunta con el protocolo cambiado**, y **conviene aprenderlas como pareja porque las
opciones falsas de cada una son las respuestas de la otra:**

| Protocolo | Puerto estándar | Puerto alternativo corriente |
|---|---|---|
| **HTTP** | **80** ✔ | **8080** |
| **HTTPS** | **443** ✔ | **8443** |

**Qué son 8080 y 8443, porque las dos preguntas los ofrecen**: **son los puertos que se usan cuando el
servicio no puede abrir los estándares**, normalmente porque **por debajo del 1024 hace falta ser
administrador para escuchar.** **Un servidor de aplicaciones arrancado por un usuario corriente
escucha en 8080**, y un intermediario lo publica después en el 80.

**Y el 25 de la primera pregunta es el del correo saliente**, que es de otro servicio.

## 2. La historia que el enunciado pide

**La pregunta 71**: **el protocolo creado por Netscape en 1994 para asegurar la navegación web es
HTTPS.** Ésa es la respuesta oficial.

---

**Aquí conviene una precisión que la respuesta oficial no hace y este temario sí**: **lo que Netscape
creó en 1994 fue SSL**, la capa de conexión segura; **HTTPS es el resultado de meter HTTP dentro de
esa capa.** **La respuesta oficial es la correcta de las cuatro que ofrece** —DNS, FTP y CSMA/CD no
tienen nada que ver con asegurar la navegación—, **y el temario la sostiene con esa salvedad.**

**La secuencia completa, que es lo que hay que llevar aprendido:**

| Año, aproximado | Qué apareció |
|---|---|
| **1994** | **SSL**, creado por Netscape para cifrar la conexión del navegador |
| **1995** | **SSL 3.0**, la versión que se generalizó |
| **1999** | **TLS 1.0**, que toma el relevo con otro nombre al pasar a un organismo de normalización |
| **Hoy** | **TLS 1.2 y TLS 1.3.** **Todas las versiones de SSL están desaconsejadas** |

**El aviso de nomenclatura, porque el sector arrastra el nombre viejo**: **cuando alguien dice
«certificado SSL» quiere decir certificado para TLS.** **SSL, como protocolo, no debe usarse.**

## 3. Qué añade la capa segura

**HTTPS no es un protocolo distinto de HTTP**: **es el mismo HTTP hablado dentro de un túnel
cifrado.** **Lo que ese túnel aporta son tres cosas, y conviene no confundirlas:**

| Qué aporta | Qué significa |
|---|---|
| **Confidencialidad** | **Nadie por el camino puede leer lo que pasa** |
| **Integridad** | **Nadie por el camino puede modificarlo sin que se note** |
| **Autenticación del servidor** | **El cliente comprueba, con el certificado, que habla con quien cree** |

**Lo que NO aporta, y es la confusión más extendida**: **HTTPS no dice que el sitio sea de fiar.**
**Dice que la conexión con ese sitio es privada.** **Un sitio fraudulento puede tener un certificado
válido**, y millones lo tienen.

**Cómo funciona el certificado, en tres líneas**: **el servidor presenta un certificado firmado por
una autoridad de certificación**; **el navegador comprueba que esa autoridad está en su lista de
confianza y que el nombre del certificado coincide con el del sitio**; **si las dos cosas cuadran,
negocian una clave de sesión y a partir de ahí todo va cifrado.**

## 4. Los servicios de internet que el enunciado nombra

**El punto pide «servicios» y el examen ha entrado sólo por el web.** **La lista mínima, con el
protocolo de cada uno:**

| Servicio | Protocolo | Puerto |
|---|---|---|
| **Web** | **HTTP / HTTPS** | **80 / 443** |
| **Nombres de dominio** | **DNS** | **53** |
| **Correo saliente** | **SMTP** | **25**, y **587** para el envío del cliente |
| **Correo entrante** | **IMAP / POP3** | **143 / 110**, y **993 / 995** cifrados |
| **Transferencia de ficheros** | **FTP**, hoy desaconsejado, y **SFTP** | **21** y **22** |
| **Terminal remota** | **SSH**, y el desaconsejado **Telnet** | **22** y **23** |

**El patrón que ordena toda la columna de la derecha**: **casi todos los servicios tienen un puerto en
claro y otro cifrado**, y **la versión cifrada es la que hay que usar.** **FTP y Telnet mandan la
contraseña en claro por la red**, y por eso están desaconsejados: **sus sustitutos son SFTP y SSH,
que van los dos por el puerto 22.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 26 | Puerto estándar de HTTP | c) 80 ✔ |
| 60 | Puerto estándar de HTTPS | c) 443 ✔ |
| 71 | Protocolo creado por Netscape en 1994 | b) HTTPS ✔ **·** con la salvedad del epígrafe 2 |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una lleva
salvedad declarada**: lo que Netscape creó en 1994 fue SSL, y HTTPS es HTTP sobre esa capa.

**El aviso de estudio**: **el punto entero cabe en dos números.** **Es el de mejor rendimiento por
minuto de todo el temario, y no conviene dedicarle más tiempo del que pide.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Los documentos que definen HTTP, TLS y los demás protocolos de este tema no se han
   consultado.** **Sus números de puerto son de uso universal** y **coinciden con las respuestas
   oficiales.**
2. **La cronología del epígrafe 2 se da con años aproximados y como conocimiento común de la
   materia.** **No se ha consultado ninguna fuente histórica**, y **la única cifra que una respuesta
   oficial usa —1994— procede del propio enunciado de la pregunta.**
3. **La salvedad sobre la pregunta 71 es una precisión del temario, no una impugnación**: **la
   respuesta oficial es la correcta de las cuatro opciones**, y **el temario la sostiene** señalando
   que el protocolo que Netscape creó se llamó SSL.
4. **La descripción del funcionamiento de un certificado y la lista de servicios y puertos del
   epígrafe 4 son oficio.** **Ninguna pregunta depende de ellas.**

**El resto del tema va como oficio y así se declara**: la explicación de por qué existen los puertos
8080 y 8443, la distinción entre lo que HTTPS aporta y lo que no, y el patrón de puerto en claro y
puerto cifrado. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**,
y el tema no lo presenta como si lo estuviera.
