# Tema 14 del específico de Operador/a Informático · Seguridad informática, criptografía y protección en redes

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 14 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Normas: Reglamento (UE) n.º 910/2014 (eIDAS), Ley 6/2020 de servicios electrónicos de confianza, Ley 39/2015 (art. 10) y Real Decreto 311/2022 (Esquema Nacional de Seguridad, anexo II). Técnica: publicaciones del NIST (SP 800-83, 800-41, 800-46, 800-77 y su glosario), RFC de la IETF (5280, 3161, 6960, 7208, 6376 y 9989), documentación de Microsoft Learn en castellano, guía de INCIBE y sede electrónica de la FNMT-RCM |
| Redacción que se estudia | eIDAS en el texto consolidado de EUR-Lex de 18-10-2024 (el último publicado); leyes y real decreto en su redacción vigente según el BOE; páginas técnicas en su versión en línea. Todo leído el 05-10-2026 |
| Extensión | 15.700 palabras aproximadamente (con las siglas y los cuadros) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); Fábrica Nacional de Moneda
y Timbre-Real Casa de la Moneda (FNMT-RCM, o FNMT); Instituto Nacional de Estándares y Tecnología de
Estados Unidos (NIST, *National Institute of Standards and Technology*) y sus publicaciones especiales
(SP, *Special Publication*); el grupo de trabajo de ingeniería de Internet (IETF, *Internet Engineering
Task Force*) y sus documentos (RFC, *Request for Comments*); Instituto Nacional de Ciberseguridad
(INCIBE); Centro Criptológico Nacional (CCN) y su equipo de respuesta (CCN-CERT); Esquema Nacional de
Seguridad (ENS); Reglamento General de Protección de Datos (RGPD) y Ley Orgánica 3/2018, de Protección
de Datos Personales y garantía de los derechos digitales (LOPDGDD); el reglamento europeo de
identificación electrónica y servicios de confianza (eIDAS, *electronic IDentification, Authentication
and trust Services*); el documento nacional de identidad electrónico (DNIe); el control de cuentas de
usuario de Windows (UAC, *User Account Control*); aplicación potencialmente no deseada (PUA,
*potentially unwanted application*); detección y respuesta en el punto final (EDR, *Endpoint Detection
and Response*); la zona desmilitarizada o red perimetral (DMZ); el sistema de detección de intrusiones
(IDS) y el de prevención (IPS); el cortafuegos de aplicación web (WAF, *web application firewall*); la
red privada virtual (VPN); el conjunto de protocolos de seguridad de IP (IPsec), su carga de seguridad
encapsulada (ESP, *Encapsulating Security Payload*), su cabecera de autenticación (AH, *Authentication
Header*) y su intercambio de claves (IKE, *Internet Key Exchange*); la capa de conexión segura (SSL) y
la seguridad de la capa de transporte (TLS), con su variante sobre datagramas (DTLS); el protocolo de
transferencia de hipertexto (HTTP) y su versión segura (HTTPS); el intérprete de órdenes seguro (SSH) y
la transferencia de ficheros sobre él (SFTP); el protocolo de transferencia de ficheros (FTP); el
sistema de nombres de dominio (DNS); los protocolos de correo SMTP (envío), IMAP y POP3 (recogida); los
mecanismos de autenticación del correo SPF (*Sender Policy Framework*), DKIM (*DomainKeys Identified
Mail*) y DMARC (*Domain-based Message Authentication, Reporting, and Conformance*); el lenguaje de
consulta estructurado (SQL); la infraestructura de clave pública (PKI, *public key infrastructure*); la
autoridad de certificación (CA, *certification authority*; la FNMT escribe AC) y la de registro (RA); la lista de revocación de certificados (CRL,
*certificate revocation list*) y el protocolo de estado de certificados en línea (OCSP, *Online
Certificate Status Protocol*); la autoridad de sellado de tiempo (TSA, *Time Stamping Authority*); el
tiempo universal coordinado (UTC); el estándar de cifrado avanzado (AES), el algoritmo internacional de
cifrado de datos (IDEA), el triple DES (3DES) y el algoritmo de Rivest, Shamir y Adleman (RSA), más
Diffie-Hellman y ElGamal, que son apellidos; el nombre alternativo del sujeto de un certificado (SAN,
*subject alternative name*) y la indicación del nombre del servidor (SNI, *server name indication*);
la consola de administración de Microsoft (MMC); el estándar de interfaz criptográfica PKCS#11 y el
formato de almacén PKCS#12 (de donde vienen las extensiones `.p12` y `.pfx`); las codificaciones
de certificados DER (*Distinguished Encoding Rules*) y PEM (*Privacy-Enhanced Mail*); el número de
identificación personal de una tarjeta (PIN); el ordenador personal (PC); el bus serie universal (USB);
el servicio de mensajes cortos (SMS); la Agencia Estatal de Administración Tributaria (AEAT); las
preguntas frecuentes de una sede (FAQ, *frequently asked questions*); la Organización Internacional de
Normalización (ISO) y la Comisión Electrotécnica Internacional (IEC); la ciberseguridad (CS,
*cybersecurity*, en una cita del NIST); y X.509, que es el
número de una recomendación de la Unión Internacional de Telecomunicaciones y no unas siglas.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 14): «Seguridad informática,
> criptografía y protección en redes: seguridad en el puesto de usuario, mecanismos de infección y
> protección en sistemas operativos de ordenadores personales, antivirus, malware, virus, gusanos,
> troyanos, adware, spyware y ransomware; seguridad y protección en redes de comunicaciones, correo y
> servicios de Internet, seguridad perimetral, acceso remoto seguro, redes privadas virtuales —VPN—,
> técnicas y mecanismos de seguridad; criptografía, algoritmos, certificados digitales, autoridades de
> certificación, sellado de tiempo, firma electrónica, instalación y administración de certificados
> electrónicos y software de la FNMT.»

Qué se puede preguntar: qué es malware y en qué se distinguen un virus, un gusano y un troyano (quién
necesita anfitrión, quién se propaga solo, quién no se propaga); qué son el adware, el spyware y el
ransomware, y cuál de ellos Microsoft no clasifica como malware; por qué vías se infecta un equipo y
qué medidas lo protegen (actualizaciones, cuenta sin privilegios, UAC, unidades extraíbles); qué hace
un antivirus, qué es la detección por firmas frente a la de comportamiento, qué es el modo pasivo de
Microsoft Defender y con qué orden se comprueba; qué se hace ante un *ransomware* y cuándo se notifica
una brecha; qué tipos de cortafuegos hay y en qué capa decide cada uno; qué es una DMZ y qué contiene;
qué es «denegar por defecto»; qué diferencia un IDS de un IPS; qué protegen SPF, DKIM y DMARC; cuáles
son las cuatro formas de acceso remoto; qué arquitecturas de VPN hay, qué hacen ESP e IKE y qué es
una VPN SSL; qué exige el ENS sobre perímetro, VPN, correo y código dañino; qué distingue la
criptografía simétrica de la asimétrica, qué es Diffie-Hellman y qué es una función resumen; qué es un
certificado, quién lo expide, cómo se revoca y cómo se comprueba su estado; qué es un sello de tiempo
y qué presunción da el cualificado; qué tres clases de firma electrónica define el eIDAS, qué requisitos
tiene la avanzada y cuál equivale a la manuscrita; cuánto dura como máximo un certificado cualificado;
qué pasos tiene la obtención del certificado de la FNMT, qué programa hay que instalar antes y qué
precauciones exige; cómo se exporta con su clave privada y en qué formato; y dónde se ven los
certificados en Windows y en el navegador. En la aplicación práctica: diagnosticar un puesto infectado,
elegir dónde colocar un servidor, decidir si una conexión remota está protegida, o resolver un fallo
en la obtención o el uso de un certificado.

<!-- indice -->

## Índice

- [1. Seguridad en el puesto de usuario](#1-seguridad-en-el-puesto-de-usuario)
  - [Las tres propiedades que se protegen](#las-tres-propiedades-que-se-protegen)
  - [Qué es el malware](#qué-es-el-malware)
  - [Virus, gusanos y troyanos: cómo se reproduce cada uno](#virus-gusanos-y-troyanos-cómo-se-reproduce-cada-uno)
  - [Adware, spyware y ransomware: qué hace cada uno](#adware-spyware-y-ransomware-qué-hace-cada-uno)
  - [Las demás categorías de malware](#las-demás-categorías-de-malware)
  - [Mecanismos de infección](#mecanismos-de-infección)
  - [Protección en el sistema operativo del ordenador personal](#protección-en-el-sistema-operativo-del-ordenador-personal)
  - [El antivirus](#el-antivirus)
  - [Si el puesto se infecta: el ransomware y la brecha](#si-el-puesto-se-infecta-el-ransomware-y-la-brecha)
  - [Cuando el operador entra en el equipo de otro](#cuando-el-operador-entra-en-el-equipo-de-otro)
- [2. Seguridad y protección en redes de comunicaciones](#2-seguridad-y-protección-en-redes-de-comunicaciones)
  - [El cortafuegos](#el-cortafuegos)
  - [Seguridad perimetral y zona desmilitarizada](#seguridad-perimetral-y-zona-desmilitarizada)
  - [Detección y prevención de intrusiones](#detección-y-prevención-de-intrusiones)
  - [El aislamiento de procesos (sandboxing)](#el-aislamiento-de-procesos-sandboxing)
  - [El correo electrónico](#el-correo-electrónico)
  - [Los servicios de Internet](#los-servicios-de-internet)
  - [El acceso remoto seguro](#el-acceso-remoto-seguro)
  - [Las redes privadas virtuales (VPN)](#las-redes-privadas-virtuales-vpn)
  - [Técnicas y mecanismos de seguridad: el mapa](#técnicas-y-mecanismos-de-seguridad-el-mapa)
- [3. Criptografía y algoritmos](#3-criptografía-y-algoritmos)
  - [Simétrica y asimétrica](#simétrica-y-asimétrica)
  - [Los algoritmos](#los-algoritmos)
  - [Las funciones resumen (hash)](#las-funciones-resumen-hash)
  - [Qué aporta la firma digital](#qué-aporta-la-firma-digital)
- [4. Certificados digitales y autoridades de certificación](#4-certificados-digitales-y-autoridades-de-certificación)
  - [El certificado](#el-certificado)
  - [La autoridad de certificación y la infraestructura de clave pública](#la-autoridad-de-certificación-y-la-infraestructura-de-clave-pública)
  - [Vigencia, revocación y suspensión](#vigencia-revocación-y-suspensión)
- [5. Sellado de tiempo](#5-sellado-de-tiempo)
- [6. Firma electrónica](#6-firma-electrónica)
  - [Las tres clases del eIDAS](#las-tres-clases-del-eidas)
  - [La firma ante las Administraciones](#la-firma-ante-las-administraciones)
  - [La identidad en el certificado](#la-identidad-en-el-certificado)
- [7. Instalación y administración de certificados electrónicos y software de la FNMT](#7-instalación-y-administración-de-certificados-electrónicos-y-software-de-la-fnmt)
  - [Dónde vive un certificado](#dónde-vive-un-certificado)
  - [Obtener el certificado de la FNMT en software](#obtener-el-certificado-de-la-fnmt-en-software)
  - [El software de la FNMT](#el-software-de-la-fnmt)
  - [Instalar, ver y exportar](#instalar-ver-y-exportar)
  - [Renovar, revocar y comprobar el estado](#renovar-revocar-y-comprobar-el-estado)
- [8. Aplicación práctica](#8-aplicación-práctica)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Seguridad en el puesto de usuario

### Las tres propiedades que se protegen

Toda la seguridad de la información se ordena en tres propiedades que hay que preservar:

- Confidencialidad: que la información sólo sea accesible a quien está autorizado.
- Integridad: que no se altere sin autorización.
- Disponibilidad: que esté accesible cuando se necesita.

Todo lo que sigue —antivirus, cortafuegos, cifrado, firma— sirve a una o varias de ellas: el
*ransomware* ataca la disponibilidad; el *spyware*, la confidencialidad; la firma electrónica y el
sello de tiempo protegen la integridad y prueban el origen.

### Qué es el malware

El NIST recoge varias definiciones; la más completa, de su SP 800-128, dice que es **«Software or
firmware intended to perform an unauthorized process that will have adverse impact on the
confidentiality, integrity, or availability of an information system. A virus, worm, Trojan horse, or
other code-based entity that infects a host. Spyware and some forms of adware are also examples of
malicious code.»** (programa o *firmware* destinado a ejecutar un proceso no autorizado que perjudica
la confidencialidad, la integridad o la disponibilidad de un sistema de información; un virus, un
gusano, un troyano u otro código que infecta un equipo; el *spyware* y algunas formas de *adware*
también son código malicioso). Microsoft, en castellano: **«El malware es una aplicación o código que
pone en peligro la seguridad del usuario. El malware puede robar su información personal, bloquear el
dispositivo hasta que pague un rescate, usar su dispositivo para enviar correo no deseado o descargar
otro malware.»**

La norma española usa otra palabra: el ENS habla de **«código dañino»** y lo enumera al regular el
correo: **«Código dañino, constituidos por virus, gusanos, troyanos, espías, u otros de naturaleza
análoga.»** [sic].

### Virus, gusanos y troyanos: cómo se reproduce cada uno

La diferencia entre los tres está en cómo se propagan, y es lo que se pregunta.

| Tipo | Definición | Cómo se propaga |
|---|---|---|
| Virus | **«A hidden, self-replicating section of computer software, usually malicious logic, that propagates by infecting (i.e., inserting a copy of itself into and becoming part of) another program. A virus cannot run by itself; it requires that its host program be run to make the virus active.»** (NIST, de la RFC 4949) | Se copia dentro de otro programa o fichero: necesita anfitrión y que alguien lo ejecute |
| Gusano | **«A self-replicating program that propagates itself through a network onto other computer systems without requiring a host program or any user intervention to replicate.»** (NIST SP 800-28) | Se replica solo, sin anfitrión ni intervención del usuario |
| Troyano | **«A useful or seemingly useful program that contains hidden code of a malicious nature that executes when the program is invoked.»** (NIST SP 800-28) | No se replica: el usuario lo instala creyéndolo legítimo |

Lo que añaden la guía de malware del NIST y Microsoft (esta, en castellano):

- Virus: el NIST, en su guía de malware para equipos de escritorio, dice que **«A virus self-replicates
  by inserting copies of itself into host programs or data files. Viruses are often triggered through
  user interaction, such as opening a file or running a program.»** (el virus se replica insertando
  copias de sí mismo en programas o ficheros de datos anfitriones, y suele activarse por una acción del
  usuario, como abrir un fichero o ejecutar un programa). Microsoft destaca una variante del puesto de
  oficina, el **«Virus de macros: Un tipo de malware que se propaga a través de documentos infectados,
  como documentos de Microsoft Word o Excel. El virus se ejecuta al abrir un documento infectado.»**
- Gusano: **«Un gusano es un tipo de malware que puede copiarse a sí mismo y, a menudo, se propaga a
  través de una red aprovechando las vulnerabilidades de seguridad. Puede propagarse a través de datos
  adjuntos de correo electrónico, mensajes de texto, programas de uso compartido de archivos, sitios de
  redes sociales, recursos compartidos de red, unidades extraíbles y vulnerabilidades de software.»** Y
  el aviso sobre los actuales: **«A diferencia de los gusanos más antiguos que a menudo se propagan solo
  porque podían, los gusanos modernos a menudo se propagan para soltar una carga útil (como
  ransomware).»**
- Troyano: **«Los troyanos son un tipo común de malware, que, a diferencia de los virus, no se puede
  propagar por sí mismos. Esto significa que tienen que descargarse manualmente u otro malware debe
  descargarlos e instalarlos.»** **«Los troyanos suelen usar los mismos nombres de archivo que las
  aplicaciones reales y legítimas.»** Lo que suelen hacer, según la misma página: descargar e instalar
  otro malware, grabar pulsaciones de teclas y sitios visitados, enviar contraseñas e historial al
  atacante y darle el control del equipo.

La regla para el test, que sale de las tres definiciones: el virus necesita anfitrión; el gusano no
necesita ni anfitrión ni usuario; el troyano no se reproduce, engaña.

### Adware, spyware y ransomware: qué hace cada uno

| Tipo | Definición | Qué ataca |
|---|---|---|
| *Spyware* | **«Software that is secretly or surreptitiously installed into an information system to gather information on individuals or organizations without their knowledge; a type of malicious code.»** (NIST, de la CNSSI 4009) | La confidencialidad: recoge información sin que el usuario lo sepa |
| *Adware* | Microsoft lo llama **«Software de publicidad: Software que muestra anuncios o promociones, o le pide que complete encuestas para otros productos o servicios en software distinto de sí mismo. Esta categoría incluye software que inserta anuncios en páginas web.»** | La experiencia del usuario y, a veces, su privacidad |
| *Ransomware* | **«Un tipo de malware que cifra los archivos o realiza otras modificaciones que pueden impedir que use el dispositivo. Luego, aparece una nota de rescate que indica que debe pagar o realizar otras acciones para poder volver a usar el dispositivo.»** (Microsoft) | La disponibilidad |

Tres precisiones que se pueden preguntar:

1. El *adware* no siempre es malware. Microsoft lo clasifica como aplicación potencialmente no deseada,
   y de esa categoría dice: **«Las PUA no se consideran malware.»** El NIST, en la definición citada
   arriba, dice lo mismo con otras palabras: **«some forms of adware»** (algunas formas de *adware*) son
   código malicioso. El *spyware*, en cambio, es malware en las dos clasificaciones.
2. El *spyware* tiene una forma concreta muy dañina: el registrador de teclas. Microsoft describe el
   **«Roba contraseñas: Un tipo de malware que recopila su información personal, como nombres de usuario
   y contraseñas. A menudo funciona junto con un registrador de teclas, que recopila y envía información
   sobre las teclas que presiona y sitios web que visita.»**
3. El *ransomware* actual no sólo cifra: también amenaza con publicar. INCIBE lo define así: **«El
   ransomware es un tipo de malware en continua evolución que impide el acceso a la información de un
   dispositivo, amenazando con destruirla o hacerla pública si las víctimas no acceden a pagar un rescate
   en un determinado plazo.»** Y Microsoft añade el riesgo de red: **«Si tu equipo está conectado a una
   red, el ransomware también puede propagarse a otros equipos o dispositivos de almacenamiento en la
   red.»**

### Las demás categorías de malware

El enunciado nombra seis tipos; Microsoft clasifica la mayoría del malware en más categorías, y algunas
aparecen como opción en las preguntas:

| Categoría | Definición de Microsoft |
|---|---|
| Puerta trasera | **«Un tipo de malware que proporciona a los hackers malintencionados acceso remoto y control del dispositivo.»** |
| Descargador | **«Un tipo de malware que descarga otro malware en el dispositivo. Debe conectarse a Internet para descargar archivos.»** |
| *Dropper* | **«A diferencia de un descargador, un dropper no necesita conectarse a Internet para eliminar archivos malintencionados.»** [sic: «eliminar» por «soltar»] |
| *Exploit* | **«Fragmento de código que aprovecha vulnerabilidades de software para obtener acceso a tu dispositivo y realizar otras tareas, como instalar malware.»** |
| Software de seguridad no autorizado | **«Malware que pretende ser software de seguridad, pero no proporciona ninguna protección.»** |
| Ofuscador | **«Un tipo de malware que oculta su código y propósito, lo que dificulta la detección o eliminación del software de seguridad.»** |

Dos más, del NIST: el *rootkit*, **«a collection of files that is installed on a host to alter its
standard functionality in a malicious and stealthy way»** (un conjunto de ficheros que se instala en un
equipo para alterar su funcionamiento normal de forma maliciosa y oculta); y el ataque combinado, que
**«uses multiple infection or transmission methods»** (usa varios métodos de infección o
transmisión). Y una técnica moderna: el malware sin archivos, que no se apoya, o no del todo, en
ficheros escritos en el disco, y que Microsoft Defender puede detener por su comportamiento aunque ya
se esté ejecutando (se ve más abajo, en el antivirus).

### Mecanismos de infección

Las vías por las que entra el malware en un ordenador personal, según la guía de prevención de
Microsoft:

| Vía | Qué dice la fuente |
|---|---|
| Software sin actualizar | **«Los exploits suelen utilizar vulnerabilidades del software. Es importante mantener actualizado el software, las aplicaciones y los sistemas operativos.»** |
| Mensajes con enlaces y adjuntos | **«Email, mensajes SMS, chat de Microsoft Teams y otras herramientas de mensajería son algunas de las formas más comunes en que los atacantes pueden infectar dispositivos.»** |
| Sitios web maliciosos o comprometidos | **«Cuando visita sitios malintencionados o en peligro, el dispositivo puede infectarse con malware automáticamente o puede ser engañado para descargar e instalar malware.»** |
| Material pirateado | **«A veces el software pirateado se incluye con malware y otro software no deseado cuando se descarga, incluidos los complementos de navegador intrusivo y adware.»** |
| Unidades extraíbles | **«Algunos tipos de malware se propagan copiando a sí mismos en unidades flash USB u otras unidades extraíbles.»** [sic] |

Para el *ransomware*, INCIBE añade **«campañas de spam»**, **«vulnerabilidades o malas configuraciones
de software, actualizaciones de software falsas, canales de descarga de software no confiables y
herramientas de activación de programas no oficiales (cracking)»**. El *phishing* es la puerta de
muchas de estas infecciones; el NIST lo define como **«A technique for attempting to acquire sensitive
data, such as bank account numbers, through a fraudulent solicitation in email or on a web site, in
which the perpetrator masquerades as a legitimate business or reputable person.»** (técnica para
obtener datos sensibles mediante una solicitud fraudulenta por correo o en un sitio web en la que el
atacante se hace pasar por una empresa o persona de confianza). Dos formas de engaño al usuario que se
confunden:

| Amenaza | Qué es |
|---|---|
| Phishing | Suplantación mediante una solicitud fraudulenta —por correo o en un sitio web, según la definición del NIST de arriba— que induce a entregar credenciales o datos |
| Pharming | Suplantación del destino: se redirige al usuario a un sitio falsificado; el NIST (SP 800-63-4) dice que **«This may be accomplished by corrupting an infrastructure service (e.g., the DNS) or the subscriber’s endpoint.»** (puede lograrse corrompiendo un servicio de infraestructura, como el DNS, o el equipo del usuario) |

Una señal práctica que da Microsoft para reconocer un sitio falso: **«los sitios malintencionados
suelen usar nombres de dominio que intercambian la letra O con un cero (0) o las letras L y I con uno
(1). Si example.com se escribe examp1e.com, el sitio que está visitando es sospechoso.»**

### Protección en el sistema operativo del ordenador personal

Lo primero es no dar privilegios al malware. Microsoft lo explica así: **«la mayoría del malware se
ejecuta con los mismos privilegios que el usuario activo. Esto significa que al limitar los privilegios
de la cuenta, puede evitar que el malware realice cambios consecuentes en cualquier dispositivo.»** De
ahí su recomendación: **«se recomienda usar una cuenta que no sea de administrador para su uso
normal»** y **«Evite examinar la web o comprobar el correo electrónico con una cuenta con privilegios
de administrador.»** El control de cuentas de usuario ayuda, pero no basta: **«Aunque UAC ayuda a
limitar los privilegios de los usuarios administradores, los usuarios pueden invalidar esta restricción
cuando se le solicite. Como resultado, es bastante fácil para un usuario administrador permitir
involuntariamente que se ejecute malware.»**

Las medidas de base, en una línea cada una:

Contraseñas robustas y distintas por servicio; doble factor
de autenticación; actualizaciones al día; copias de seguridad probadas; cifrado de los soportes que
salen de la oficina; principio de mínimo privilegio —cada usuario, sólo los permisos que necesita—; y
formación, que es la medida que más rendimiento da contra el *phishing*.

Microsoft añade la regla de copias **«3-2-1: hacer 3 copias, almacenar en al menos 2 ubicaciones, con
al menos 1 copia sin conexión»**, prudencia con las redes inalámbricas públicas **«especialmente
aquellas que no requieren autenticación»**, y no conectar memorias desconocidas: **«Utilice solo
unidades extraíbles que conozca o que provengan de una fuente de confianza.»** Para el puesto de
Windows 11, las herramientas concretas —la aplicación Seguridad de Windows, BitLocker, el UAC, el
acceso controlado a carpetas y los puntos de restauración— están en el tema 6.

En el sector público hay además una obligación normativa. El ENS (Real Decreto 311/2022, anexo II,
medida «Protección frente a código dañino [op.exp.6]») exige, ya en categoría básica:

- **«[op.exp.6.1] Se dispondrá de mecanismos de prevención y reacción frente a código dañino,
  incluyendo el correspondiente mantenimiento de acuerdo a las recomendaciones del fabricante.»**
- **«[op.exp.6.2] Se instalará software de protección frente a código dañino en todos los equipos:
  puestos de usuario, servidores y elementos perimetrales.»**
- **«[op.exp.6.3] Todo fichero procedente de fuentes externas será analizado antes de trabajar con
  él.»**
- **«[op.exp.6.4] Las bases de datos de detección de código dañino permanecerán permanentemente
  actualizadas.»**
- **«[op.exp.6.5] El software de detección de código dañino instalado en los puestos de usuario deberá
  estar configurado de forma adecuada e implementará protección en tiempo real de acuerdo a las
  recomendaciones del fabricante.»**

Y los refuerzos por categoría: **«Categoría MEDIA: op.exp.6+ R1 + R2.»** (escaneo regular de todo el
sistema y análisis de las funciones críticas al arrancar) y **«Categoría ALTA: op.exp.6+ R1 + R2 + R3 +
R4.»**, donde R3 es la lista blanca (**«Solamente se podrán ejecutar aquellas aplicaciones previamente
autorizadas.»**) y R4 el EDR (**«Se emplearán herramientas de seguridad orientadas a detectar,
investigar y resolver actividades sospechosas en puestos de usuario y servidores (EDR - Endpoint
Detection and Response).»**). Otra medida del mismo anexo que toca al puesto: **«[mp.eq.2.1] El puesto
de trabajo se bloqueará al cabo de un tiempo prudencial de inactividad, requiriendo una nueva
autenticación del usuario para reanudar la actividad en curso.»** El ENS **«es de aplicación a todo el
sector público, en los términos en que este se define por el artículo 2 de la Ley 40/2015»**; cómo
encajan en él la RTVA y CSRTV es materia del tema 15.

### El antivirus

Qué es, según el NIST (SP 800-83): **«A program that monitors a computer or network to identify all
major types of malware and prevent or contain malware incidents.»** (programa que vigila un equipo o
una red para identificar los principales tipos de malware y prevenir o contener los incidentes).

*Cómo detecta.* Tradicionalmente, por firmas: compara los ficheros con una base de patrones de
malware conocido, y por eso hay que actualizarla (el ENS lo exige en op.exp.6.4). Su límite es el
malware nuevo, que todavía no tiene firma. Los antivirus actuales añaden detección por comportamiento.
Microsoft lo cuenta de su propio producto: **«En 2015, Microsoft Defender Antivirus pasó de usar un
motor estático basado en firmas a un modelo que usa tecnologías predictivas (como el aprendizaje
automático, la ciencia aplicada y la inteligencia artificial)»**; ofrece **«detección de anomalías, una
capa de protección para malware que no se ajusta a ningún patrón predefinido»**, que **«está activada
de forma predeterminada»**; y **«también puede detener las amenazas en función de sus comportamientos y
procesar árboles incluso cuando la amenaza ha comenzado a ejecutarse. Un ejemplo común de estos tipos
de ataques es el malware sin archivos.»** La división firmas/comportamiento es la clásica de oficio; la
fuente que la sostiene aquí es la descripción de Microsoft.

*El antivirus del puesto Windows: Microsoft Defender Antivirus.* **«Antivirus de Microsoft Defender
está disponible en Windows 10, Windows 11 y en versiones de Windows Server.»** Lo que conviene saber
para administrarlo:

- Convivencia con otro antivirus. **«Si usa un producto antivirus o antimalware que no es de Microsoft
  en el dispositivo, es posible que pueda ejecutar Microsoft Defender Antivirus en modo pasivo junto con
  la solución antivirus que no es de Microsoft.»** Los tres modos: en el activo, **«se usa como la
  aplicación antivirus principal en el dispositivo»**; en el pasivo, **«Se analizan los archivos y se
  notifican las amenazas detectadas, pero Microsoft Defender Antivirus no neutraliza las amenazas.»**;
  deshabilitado, **«Los archivos no se analizan y las amenazas no se neutralizan.»** El modo pasivo
  tiene una condición: **«Microsoft Defender Antivirus solo puede ejecutarse en modo pasivo en los
  puntos de conexión que están incorporados a Microsoft Defender para punto de conexión.»**
- Comprobar su estado. En la aplicación Seguridad de Windows, **«Protección antivirus y contra
  amenazas»** y, en **«¿Quién me protege?»**, **«Administrar proveedores»**. O en PowerShell:
  **«Escriba Get-MpComputerStatus.»** y mire la fila **«AMRunningMode»**, donde **«Normal significa que
  el Antivirus de Microsoft Defender se ejecuta en modo activo.»**
- Sus servicios y procesos, que se ven en el Administrador de tareas:

| Servicio | Proceso |
|---|---|
| **«Servicio principal de Microsoft Defender Antivirus»** (MdCoreSvc) | `MpDefenderCoreService.exe` |
| **«servicio de Antivirus de Microsoft Defender»** (WinDefend), que aparece como **«Antimalware Service Executable»** | `MsMpEng.exe` |
| **«Servicio de inspección de red en tiempo real de Microsoft Defender Antivirus»** (WdNisSvc) | `NisSrv.exe` |
| **«Utilidad de línea de comandos de Microsoft Defender Antivirus»** | `MpCmdRun.exe` |

- Mantenerlo al día: **«Es importante mantener Microsoft Defender Antivirus (o cualquier solución
  antivirus/antimalware) actualizada.»** Y el coste: **«Microsoft Defender Antivirus, al igual que otros
  software antivirus, puede causar problemas de rendimiento en los dispositivos de punto de conexión.»**
  [sic]

Además del antivirus, Microsoft cita el **«Examen de seguridad de Microsoft»**, que **«ayuda a quitar
software malintencionado de los equipos»**, con una advertencia: **«Esta herramienta no reemplaza el
producto antimalware.»**

Un efecto secundario que se encuentra en la práctica: el antivirus puede bloquear programas legítimos.
La propia FNMT avisa de que en la obtención del certificado **«Los antivirus y proxies pueden impedir el
uso de esta aplicación»** (epígrafe 7).

### Si el puesto se infecta: el ransomware y la brecha

Lo que dice INCIBE que se haga primero: **«Recuerda que lo primero es apagar el equipo afectado para
que no se extienda a otros dispositivos de la red interna.»** Y dos reglas: **«No pagar nunca el
rescate, ya que esto no garantiza que puedas recuperar la información ni que no vuelvan a exigirte un
segundo rescate.»**; y aplicar el plan de respuesta ante incidentes, si lo hay. Para descifrar sin
pagar, el proyecto No More Ransom publica herramientas, con la salvedad de que **«Por el momento, no
todos los tipos de ransomware tienen solución.»** Microsoft recomienda limpiar antes de recuperar:
**«Intenta limpiar completamente tu equipo con Seguridad de Windows. Debes hacer esto antes de intentar
recuperar los archivos.»** La recuperación de los datos desde las copias y con herramientas de
recuperación es materia del tema 3.

Si el incidente afecta a datos personales es una violación de seguridad en el sentido del RGPD, con
estas obligaciones:

*Violaciones de seguridad (artículos 33 y 34 del Reglamento).*

- El responsable la notifica a la autoridad de control «**sin dilación indebida y, de ser posible,
  a más tardar 72 horas después de que haya tenido constancia de ella**», a menos que sea
  improbable que constituya un riesgo para los derechos y libertades. Pasadas las 72 horas, la
  notificación irá acompañada de los motivos de la dilación.
- El encargado la notifica al responsable sin dilación indebida.
- Se comunica al interesado cuando sea probable que entrañe un alto riesgo para sus derechos y
  libertades. No es necesaria si el responsable había aplicado medidas que hagan ininteligibles los
  datos, como el cifrado, si ha tomado medidas ulteriores que eliminen el alto riesgo, o si supone
  un esfuerzo desproporcionado, en cuyo caso se opta por una comunicación pública o medida
  semejante.
- En todo caso, el responsable documentará cualquier violación, con los hechos, sus efectos y las
  medidas correctivas.

La excepción del cifrado es la razón práctica para cifrar portátiles y soportes: si se pierde un disco
cifrado, no hace falta comunicarlo a cada afectado.

### Cuando el operador entra en el equipo de otro

Revisar un equipo infectado obliga a ver contenidos del usuario. La LOPDGDD lo regula así:

*Artículo 87. Intimidad y uso de dispositivos digitales.*

1. Los trabajadores y los empleados públicos tienen derecho a la protección de su intimidad en el
   uso de los dispositivos digitales puestos a su disposición por su empleador.
2. El empleador podrá acceder a los contenidos derivados del uso de esos medios «**a los solos
   efectos de controlar el cumplimiento de las obligaciones laborales o estatutarias y de
   garantizar la integridad de dichos dispositivos**».
3. Los empleadores deberán establecer criterios de utilización respetando los estándares mínimos
   de protección de la intimidad de acuerdo con los usos sociales y los derechos reconocidos
   constitucional y legalmente, y «**En su elaboración deberán participar los representantes de los
   trabajadores.**» Si el empleador ha admitido el uso con fines privados, el acceso al contenido
   requerirá que se especifiquen de modo preciso los usos autorizados y se establezcan garantías,
   «**tales como, en su caso, la determinación de los períodos en que los dispositivos podrán
   utilizarse para fines privados**». Los trabajadores deberán ser informados de esos criterios.

«Garantizar la integridad de dichos dispositivos» es la finalidad que ampara la intervención técnica;
fuera de ella, el acceso al contenido no está cubierto por ese artículo.

## 2. Seguridad y protección en redes de comunicaciones

### El cortafuegos

Definición del NIST: **«A gateway that limits access between networks in accordance with local
security policy.»** (una pasarela que limita el acceso entre redes conforme a la política de seguridad
local). La regla con la que se configura, de su guía de cortafuegos (SP 800-41 Rev. 1, de 2009):
**«Generally, firewalls should block all inbound and outbound traffic that has not been expressly
permitted by the firewall policy—traffic that is not needed by the organization. This practice, known
as deny by default, decreases the risk of attack and can also reduce the volume of traffic carried on
the organization's networks.»** (los cortafuegos deben bloquear todo el tráfico de entrada y de salida
que la política no permita expresamente; es lo que se llama «denegar por defecto», y reduce el riesgo
de ataque y el volumen de tráfico).

Los tipos, por la capa en que deciden:

| Tipo | En qué capa decide | Qué mira |
|---|---|---|
| De filtrado de paquetes | Red y transporte | Direcciones y puertos |
| Con estado | Red y transporte | Además, si el paquete pertenece a una conexión ya establecida |
| De aplicación | Aplicación | Cómo se usa el protocolo: por ejemplo, un adjunto ejecutable en un correo o una orden FTP no permitida |
| De aplicación web (WAF) | Aplicación (HTTP), delante del servidor web | El contenido de la petición web |

Lo que dice la guía del NIST de los dos primeros. El filtro de paquetes es **«The most basic feature of
a firewall»** (la función más básica); los que sólo filtran, **«also known as stateless inspection
firewalls, do not keep track of the state of each flow of traffic that passes though the firewall»**
[sic] (no llevan la cuenta del estado de cada flujo); y **«the most common example of a pure packet
filtering device is a network router that employs access control lists»** (el ejemplo más corriente es
un encaminador con listas de control de acceso). La inspección con estado **«improves on the functions
of packet filters by tracking the state of connections and blocking packets that deviate from the
expected state»** (mejora el filtro siguiendo el estado de las conexiones y bloqueando los paquetes que
se salen del estado esperado), y para ello **«keeps track of each connection in a state table»**
(guarda cada conexión en una tabla de estado). Por encima están el cortafuegos de aplicación y la
pasarela *proxy* de aplicación, que miran el contenido.

Qué hace un cortafuegos de aplicación web que los otros no pueden: entiende HTTP. Un cortafuegos
corriente ve una petición al puerto 443 y la deja pasar; el de aplicación lee lo que va dentro y puede
rechazar una inyección de instrucciones en una consulta o un guion incrustado en un formulario.

En el puesto de usuario también hay cortafuegos: el de Windows, que se gestiona desde Seguridad de
Windows, en «Firewall y protección de red» (tema 6).

### Seguridad perimetral y zona desmilitarizada

El perímetro es la frontera entre la red propia y las ajenas, y el ENS lo exige en todas las
categorías (medida «Perímetro seguro [mp.com.1]»):

- **«[mp.com.1.1] Se dispondrá de un sistema de protección perimetral que separe la red interna del
  exterior. Todo el tráfico deberá atravesar dicho sistema.»**
- **«[mp.com.1.2] Todos los flujos de información a través del perímetro deben estar autorizados
  previamente.»**

La segunda regla es el «denegar por defecto» del NIST dicho en norma española.

La zona desmilitarizada (DMZ) es, según la definición que recoge el NIST (de la CNSSI 4009-2022), un
**«Perimeter network segment that is logically between internal and external networks. Its purpose is
to enforce the internal network's CS policy for external information exchange and to provide external,
untrusted sources with restricted access to releasable information while shielding the internal
networks from outside attacks.»** (un segmento de red perimetral situado lógicamente entre las redes
interna y externa; sirve para aplicar la política de seguridad de la red interna al intercambio con el
exterior y para dar a fuentes externas, no fiables, un acceso restringido a la información publicable,
protegiendo la red interna de los ataques de fuera). Lo que va en cada zona:

| Zona | Qué contiene | Quién llega |
|---|---|---|
| Externa | Internet | Cualquiera |
| Perimetral | Lo que tiene que ser accesible desde fuera: servidor web, correo, portal | Desde fuera, sí; hacia dentro, no |
| Interna | Lo que nunca debe verse desde fuera: bases de datos, ficheros, puestos | Sólo desde dentro |

La regla de oficio que la hace útil: desde la DMZ no se abren conexiones hacia la red interna, de modo
que quien tome un servidor publicado se queda en la DMZ y no salta al interior. Por eso la DMZ es más
segura que Internet, porque está detrás de un cortafuegos, y menos que la red interna, porque está
expuesta a propósito.

La arquitectura clásica se monta con dos cortafuegos o con uno de tres patas, y la diferencia práctica
es que con dos, para llegar de fuera a dentro hay que atravesar dos equipos distintos, a poder ser de
fabricantes distintos.

Un aviso del NIST sobre el uso doméstico de la palabra: **«Many hardware firewall devices have a
feature called DMZ»** (muchos cortafuegos tienen una función llamada DMZ), que el glosario del NIST
define, de esa misma guía, como **«An interface on a routing firewall that is similar to the
interfaces found on the firewall's protected side.»** (una interfaz del cortafuegos parecida a las del
lado protegido): el tráfico entre esa interfaz y la red
interna **«still goes through the firewall and can have firewall protection policies applied»** (sigue
pasando por el cortafuegos y se le pueden aplicar sus políticas).

### Detección y prevención de intrusiones

El cortafuegos decide por reglas; el IDS y el IPS vigilan lo que pasa. Un IDS es **«A security service
that monitors and analyzes network or system events for the purpose of finding, and providing real-time
or near real-time warning of, attempts to access system resources in an unauthorized manner.»** (un
servicio que vigila y analiza los eventos de la red o del sistema para encontrar intentos de acceso no
autorizado y avisar de ellos en tiempo real o casi). Un IPS es **«A system that can detect an intrusive
activity and also attempt to stop the activity, ideally before it reaches its targets.»** (un sistema
que detecta la actividad intrusiva y además intenta pararla, a ser posible antes de que llegue a su
objetivo). La diferencia, por tanto: el IDS avisa; el IPS, además, corta.

### El aislamiento de procesos (sandboxing)

Una caja de arena (*sandbox*) es **«A restricted, controlled execution environment that prevents
potentially malicious software, such as mobile code, from accessing any system resources except those
for which the software is authorized.»** (un entorno de ejecución restringido y controlado que impide
que un programa potencialmente malicioso acceda a otros recursos del sistema que los autorizados).

Dónde se usa el aislamiento en la práctica: el navegador ejecuta cada pestaña en su propia caja, el
sistema operativo móvil encierra cada aplicación en la suya, y el antivirus detona los adjuntos
sospechosos dentro de una para ver qué hacen antes de dejarlos pasar.

Y el contraste con la virtualización (tema 10): la máquina virtual aísla un sistema operativo entero;
la caja de arena aísla un proceso. La idea es la misma —limitar el daño— a dos escalas.

### El correo electrónico

El correo es la vía de entrada más frecuente del malware y del *phishing*. El ENS le dedica una medida
propia, «Protección del correo electrónico [mp.s.1]», que se aplica en todas las categorías:

- **«[mp.s.1.1] La información distribuida por medio de correo electrónico se protegerá, tanto en el
  cuerpo de los mensajes como en los anexos.»**
- **«[mp.s.1.2] Se protegerá la información de encaminamiento de mensajes y establecimiento de
  conexiones.»**
- Frente al **«[mp.s.1.3] Correo no solicitado, en su expresión inglesa «spam».»**, el
  **«[mp.s.1.4] Código dañino, constituidos por virus, gusanos, troyanos, espías, u otros de naturaleza
  análoga.»** y el **«[mp.s.1.5] Código móvil de tipo micro-aplicación, en su expresión inglesa
  «applet».»**
- Con normas de uso para el personal que contendrán **«[mp.s.1.6] Limitaciones al uso como soporte de
  comunicaciones privadas.»** y **«[mp.s.1.7] Actividades de concienciación y formación relativas al uso
  del correo electrónico.»**

El problema técnico de fondo es que el correo se puede falsificar. La RFC 7208 lo dice al empezar:
**«Email on the Internet can be forged in a number of ways.»** (el correo de Internet puede
falsificarse de varias maneras). Tres mecanismos, que se publican en el DNS del dominio emisor, lo
remedian:

| Mecanismo | Qué hace (fuente) |
|---|---|
| SPF (RFC 7208) | Permite que los dominios **«can explicitly authorize the hosts that are allowed to use their domain names, and a receiving host can check such authorization»** (autoricen expresamente qué servidores pueden usar su nombre de dominio, y que el receptor lo compruebe) |
| DKIM (RFC 6376) | El dominio firmante asume responsabilidad sobre el mensaje, y **«Assertion of responsibility is validated through a cryptographic signature and by querying the Signer's domain directly to retrieve the appropriate public key.»** (esa responsabilidad se valida con una firma criptográfica y consultando al dominio firmante su clave pública) |
| DMARC (RFC 9989, mayo de 2026) | **«DMARC permits the owner of an email's Author Domain to enable validation of the domain's use to indicate the Domain Owner's or Public Suffix Operator's message handling preference regarding failed validation and to request reports about the use of the domain name.»** (permite al dueño del dominio del autor pedir que se valide su uso, decir qué hacer con los mensajes que no superen la validación y recibir informes) |

La RFC 9989 **«obsoletes RFCs 7489 and 9091»**: la RFC 7489, de 2015, que es la que aún citan muchos
manuales, ya no es la vigente.

Los protocolos del buzón tienen versión cifrada (puertos 993 y 995, en el cuadro siguiente). Y el
cifrado y la firma del contenido del mensaje se hacen con los certificados del epígrafe 4: la FNMT
dedica una sección de su sede a **«Uso de los Certificados con Correo Electrónico»**.

### Los servicios de Internet

Cada servicio tiene su protocolo y su puerto, y casi todos tienen una versión cifrada:

| Servicio | Protocolo | Puerto |
|---|---|---|
| Web | HTTP / HTTPS | 80 / 443 |
| Nombres de dominio | DNS | 53 |
| Correo saliente | SMTP | 25, y 587 para el envío del cliente |
| Correo entrante | IMAP / POP3 | 143 / 110, y 993 / 995 cifrados |
| Transferencia de ficheros | FTP, hoy desaconsejado, y SFTP | 21 y 22 |
| Terminal remota | SSH, y el desaconsejado Telnet | 22 y 23 |

El patrón que ordena toda la columna de la derecha: casi todos los servicios tienen un puerto en claro
y otro cifrado, y la versión cifrada es la que hay que usar. FTP y Telnet mandan la contraseña en
claro por la red, y por eso están desaconsejados: sus sustitutos son SFTP y SSH, que van los dos por
el puerto 22.

Lo que HTTPS aporta y lo que no (los protocolos HTTP, HTTPS y TLS y la seguridad del navegador se
desarrollan en el tema 13). HTTPS no es un protocolo distinto de HTTP: es el mismo HTTP hablado dentro
de un túnel cifrado. Lo que ese túnel aporta son tres cosas, y conviene no confundirlas:

| Qué aporta | Qué significa |
|---|---|
| Confidencialidad | Nadie por el camino puede leer lo que pasa |
| Integridad | Nadie por el camino puede modificarlo sin que se note |
| Autenticación del servidor | El cliente comprueba, con el certificado, que habla con quien cree |

Lo que NO aporta, y es la confusión más extendida: HTTPS no dice que el sitio sea de fiar. Dice que
la conexión con ese sitio es privada. Un sitio fraudulento puede tener un certificado válido, y
millones lo tienen.

Los servicios web publicados tienen sus propios ataques, que el cortafuegos de aplicación ataja:

| Ataque | En qué consiste |
|---|---|
| Inyección de SQL | Meter instrucciones de consulta en un campo del formulario |
| Guion entre sitios | Colar código de navegador que se ejecuta en la sesión de otro usuario |
| Falsificación de petición | Hacer que el navegador de la víctima envíe una petición legítima sin querer |
| Denegación de servicio | Agotar los recursos del servicio con peticiones |

El ENS, en «Protección de servicios y aplicaciones web [mp.s.2]», obliga a protegerlos; entre otras
cosas, entre las amenazas de las que hay que protegerlos que enumera el [mp.s.2.1], **«d) Se prevendrán ataques de inyección de código.»**, **«[mp.s.2.2] Se prevendrán intentos de
escalado de privilegios.»** y **«[mp.s.2.3] Se prevendrán ataques de cross site scripting.»**

### El acceso remoto seguro

El NIST (SP 800-46 Rev. 2, guía de teletrabajo y acceso remoto) agrupa las formas de acceso remoto en
cuatro: **«tunneling, portals, remote desktop access, and direct application access»** (túnel,
portal, escritorio remoto y acceso directo a la aplicación). Y advierte de lo que tienen en común:
**«They are all dependent on the physical security of the client devices.»** (todas dependen de la
seguridad física del equipo cliente).

| Forma | Cómo funciona (SP 800-46) |
|---|---|
| Túnel | **«Tunnels are typically established through virtual private network (VPN) technologies.»** Con el túnel abierto, el teletrabajador usa en su equipo sus propias aplicaciones contra los servidores de la organización |
| Portal | **«A portal is a server that offers access to one or more applications through a single centralized interface.»** **«Most portals are web-based—for them, the portal client is a regular web browser.»** La aplicación corre en el servidor del portal, no en el equipo del usuario |
| Escritorio remoto | **«A remote desktop access solution gives a teleworker the ability to remotely control a particular PC at the organization, most often the user's own computer at the organization's office»** |
| Acceso directo | **«A teleworker can access an individual application directly, with the application providing its own security»**; el servidor suele estar **«located at the organization's perimeter (e.g., in a demilitarized zone [DMZ])»**, y el ejemplo más común es el correo web |

La diferencia entre túnel y portal es dónde quedan los datos: **«In a tunnel, the software and data
are on the client»** (en el túnel, el programa y los datos están en el cliente). Por eso el túnel
protege el trayecto pero no el equipo: **«the application client software and data at rest resides on
the client device, so they are not protected by the tunneling solution and should be protected by
other means»** (el programa y los datos guardados en el cliente no los protege el túnel y hay que
protegerlos por otros medios). Y tampoco protege más allá de la pasarela: **«they do not provide any
protection for the communications between the VPN gateway and internal resources»**. El escritorio
remoto y la virtualización de escritorios se tratan en el tema 10.

### Las redes privadas virtuales (VPN)

Qué es una VPN, según la definición que recoge el NIST (de la RFC 4949): una **«Restricted-use logical
computer network that is constructed from the system resources of a physical network by using
encryption and/or by tunneling links of the virtual network across the real network.»** (una red lógica
de uso restringido construida sobre los recursos de una red física, cifrando o tunelizando los enlaces
de la red virtual a través de la real). Lo que el túnel garantiza: **«Tunnels use cryptography to
protect the confidentiality and integrity of the transmitted information between the client device and
the VPN gateway.»** (cifra para proteger la confidencialidad y la integridad entre el equipo cliente y
la pasarela). Las más usadas para el teletrabajo, según el NIST, son **«Internet Protocol Security
(IPsec) and Secure Sockets Layer (SSL)»**.

*Arquitecturas* (NIST SP 800-77 Rev. 1, guía de VPN IPsec, de 2020):

| Arquitectura | Qué une (SP 800-77) |
|---|---|
| Pasarela a pasarela | **«This architecture protects communications between two specific networks, such as an organization's main office network and a branch office network or two business partners' networks.»** (dos redes: sede y delegación, o dos socios) |
| Acceso remoto | **«Also known as host-to-gateway, this architecture protects communications between one or more individual hosts and a specific network belonging to an organization.»** (uno o varios equipos sueltos contra la red de la organización: el teletrabajador) |
| Equipo a equipo | **«A host-to-host architecture protects communication between two specific computers.»** (dos ordenadores concretos) |
| Malla | **«In a mesh architecture, many hosts within one or a few networks all establish individual VPNs with each other.»** (muchos equipos con VPN entre todos) |

*IPsec.* **«IPsec is a network layer security protocol with two main components»** (protocolo de
seguridad de la capa de red con dos componentes):

- ESP: **«Encapsulating Security Payload (ESP) is the protocol that transports the encrypted and
  integrity-protected network communications across the network.»** (transporta las comunicaciones
  cifradas y con integridad). El antiguo AH, que no cifra, **«is no longer recommended by this
  guidance»** (ya no lo recomienda la guía).
- IKE: **«Internet Key Exchange (IKE) is the protocol used by IPsec to negotiate IPsec connection
  settings; authenticate endpoints to each other; define the security parameters of IPsec-protected
  connections; negotiate session keys; and manage, update, and delete IPsec-protected communication
  channels. The current version is IKEv2.»** (negocia la conexión, autentica los extremos, fija los
  parámetros, negocia las claves de sesión y gestiona los canales; la versión vigente es IKEv2).

*VPN SSL (en realidad, TLS).* **«The most common IPsec alternative is the SSL VPN. Although these are
still called SSL VPNs, they now use the TLS protocol rather than the older SSL protocol.»** (la
alternativa más común a IPsec es la VPN SSL, que aunque se siga llamando así usa TLS). Su ventaja:
**«Usually, it is run over port 443 (HTTPS) since most networks pass on this traffic without attempting
any kind of deep packet inspection.»** (suele ir por el puerto 443, que casi todas las redes dejan
pasar). La SP 800-77 describe también WireGuard, **«a fairly new VPN implementation originally written
for the Linux kernel»**, **«less complex than IPsec but, as a result, is also not as flexible as
IPsec»** (una implementación reciente, más sencilla y menos flexible que IPsec).

*Lo que exige el ENS.* En la medida «Protección de la confidencialidad [mp.com.2]», ya en nivel bajo:
**«[mp.com.2.1] Se emplearán redes privadas virtuales cifradas cuando la comunicación discurra por
redes fuera del propio dominio de seguridad.»**; y desde el nivel medio, **«[mp.com.2.r1.1] Se
emplearán algoritmos y parámetros autorizados por el CCN.»** En la de integridad y autenticidad
[mp.com.3], **«[mp.com.3.1] En comunicaciones con puntos exteriores al dominio propio de seguridad, se
asegurará la autenticidad del otro extremo del canal de comunicación antes de intercambiar
información.»**

*Un caso que lo explica todo.* Un usuario está en una red inalámbrica abierta y pública, con una VPN
establecida por software hacia la red de su empresa, navegando por la intranet. ¿Puede otro usuario de
esa red espiarlo con un analizador de tráfico? No, sea la navegación HTTP o HTTPS, y la clave está en
el orden en que se aplican los cifrados:

1. El navegador produce la petición, cifrada o no según el protocolo.
2. El cliente de red privada virtual mete esa petición entera dentro de su propio túnel cifrado.
3. Lo que sale por la tarjeta inalámbrica es el túnel, no la petición.

El vecino sólo capta tráfico cifrado hacia la pasarela de la empresa: ve que hay tráfico y cuánto, y
no ve qué. Y no le protege la red inalámbrica: una red abierta no cifra nada.

El aviso de oficio que este caso deja: una red privada virtual protege el transporte, no el destino.
Si el usuario visita un sitio malicioso a través del túnel, el túnel lo lleva igualmente.

### Técnicas y mecanismos de seguridad: el mapa

| Amenaza o necesidad | Mecanismo | Dónde se ve |
|---|---|---|
| Malware en el puesto | Antivirus con protección en tiempo real, actualizaciones, cuenta sin privilegios, lista blanca | Epígrafe 1 |
| Robo del equipo o del disco | Cifrado de volumen (BitLocker) | Tema 6 |
| Pérdida de datos | Copias de seguridad 3-2-1 probadas | Tema 3 |
| Tráfico no autorizado | Cortafuegos con «denegar por defecto», perímetro, DMZ | Este epígrafe |
| Ataque en curso | IDS que avisa, IPS que corta | Este epígrafe |
| Correo falsificado o malicioso | SPF, DKIM, DMARC, filtrado | Este epígrafe |
| Escucha en redes ajenas | VPN, HTTPS, protocolos cifrados | Este epígrafe y tema 13 |
| Suplantación de identidad | Autenticación fuerte, certificados, firma | Epígrafes 3 a 6 |
| Prueba de la fecha | Sello de tiempo | Epígrafe 5 |

## 3. Criptografía y algoritmos

### Simétrica y asimétrica

La criptografía se divide por el número de claves:

- Simétrica: el NIST define el algoritmo de clave simétrica como **«A cryptographic algorithm that uses
  the same secret key for an operation and its complement (e.g., encryption and decryption). Also
  called a secret-key algorithm.»** (usa la misma clave secreta para una operación y su inversa, por
  ejemplo cifrar y descifrar; también se llama de clave secreta).
- Asimétrica: **«Cryptography that uses two separate keys to exchange data — one to encrypt or
  digitally sign the data and one to decrypt the data or verify the digital signature. Also known as
  public-key cryptography.»** (usa dos claves distintas: una para cifrar o firmar y otra para descifrar
  o verificar la firma; también se llama de clave pública).

| Familia | Cómo funciona | Ejemplos |
|---|---|---|
| Simétrica | La misma clave cifra y descifra | IDEA, AES, 3DES, ChaCha20 |
| Asimétrica | Un par de claves: la pública cifra, la privada descifra | RSA, ElGamal, curva elíptica |
| Intercambio de claves | Acordar una clave por un canal público sin transmitirla | Diffie-Hellman |

El cuadro describe el uso para cifrar. Para firmar el orden se invierte (la definición del NIST ya
separa la clave que firma de la que verifica): se firma con la clave privada, que sólo tiene el titular, y cualquiera verifica con la pública.
Por eso la clave privada no se entrega nunca y la pública se reparte dentro del certificado (epígrafe
4).

El matiz sobre Diffie-Hellman, porque es el que se escapa: no es exactamente un algoritmo de cifrado.
Es un método de intercambio de claves: permite que dos partes acuerden una clave secreta hablando por
un canal público. Lo que después se cifra con esa clave se hace con un algoritmo simétrico.

Y por qué en la práctica se usan las dos familias juntas: la asimétrica es lenta y resuelve el
problema de distribuir la clave; la simétrica es rápida y resuelve el de cifrar mucho volumen. Una
conexión segura empieza con criptografía asimétrica para acordar una clave y sigue con simétrica para
el resto de la sesión.

### Los algoritmos

AES es el simétrico de referencia: **«A U.S. Government-approved cryptographic algorithm that can be
used to protect electronic data. The AES algorithm is a symmetric block cipher that can encrypt
(encipher) and decrypt (decipher) information.»** (algoritmo aprobado por el Gobierno de Estados
Unidos, normalizado en el FIPS 197; es un cifrador simétrico de bloque). Es el que usa BitLocker
(XTS-AES, tema 6). RSA y ElGamal son asimétricos; Diffie-Hellman, de intercambio de claves. Los
algoritmos de la lista que no llevan cita se dan por su familia, como clasificación de oficio.

En el sector público español la elección no es libre: el ENS pide, desde el nivel medio de
confidencialidad, **«algoritmos y parámetros autorizados por el CCN»** (medida mp.com.2, refuerzo R1).

### Las funciones resumen (hash)

Es la tercera pieza, y la que hace posible firmar y sellar: una función que reduce un documento de
cualquier tamaño a un resumen de longitud fija. El NIST: **«A function on bit strings in which the
length of the output is fixed.»** Las aprobadas están diseñadas para cumplir dos propiedades: **«(One-way) It is
computationally infeasible to find any input that maps to any new pre-specified output»** (de un solo
sentido: no se puede encontrar una entrada que dé un resumen fijado de antemano) y **«(Collision-resistant)
It is computationally infeasible to find any two distinct inputs that map to the same output.»**
(resistente a colisiones: no se pueden encontrar dos entradas distintas con el mismo resumen). Los
estándares que cita son el **«FIPS 180 and FIPS 202»**.

Para qué sirve: si cambia un solo bit del documento, cambia el resumen. Al firmar se firma el resumen,
no el documento entero; al sellar en el tiempo, se envía el resumen a la autoridad de sellado (epígrafe
5), que no llega a ver el documento.

### Qué aporta la firma digital

El NIST define la firma digital como **«The result of a cryptographic transformation of data that, when
properly implemented, provides a mechanism for verifying origin authentication, data integrity, and
signatory non-repudiation.»** (el resultado de una transformación criptográfica de los datos que,
bien aplicada, permite verificar el origen, la integridad de los datos y el no repudio del firmante).
Tres garantías: quién lo firmó, que no se ha cambiado, y que el firmante no puede negar que lo firmó.
La confidencialidad no está entre ellas: firmar no cifra. La firma digital es el mecanismo técnico;
la firma electrónica es la figura jurídica del epígrafe 6.

## 4. Certificados digitales y autoridades de certificación

### El certificado

El problema que resuelve, en palabras de la RFC 5280: **«Users of a public key require confidence that
the associated private key is owned by the correct remote subject (person or system) with which an
encryption or digital signature mechanism will be used. This confidence is obtained through the use of
public key certificates, which are data structures that bind public key values to subjects. The
binding is asserted by having a trusted CA digitally sign each certificate.»** (quien usa una clave
pública necesita confiar en que la privada correspondiente es de quien dice; esa confianza la dan los
certificados, estructuras de datos que vinculan una clave pública con su titular, vínculo que asegura
una autoridad de certificación de confianza firmando cada certificado). Y **«A certificate has a
limited valid lifetime, which is indicated in its signed contents.»** (tiene una vida limitada, que
consta en su contenido firmado). El formato es el de la recomendación X.509, versión 3, que la RFC 5280
perfila para Internet.

El eIDAS lo define en términos jurídicos: **«"certificado de firma electrónica", una declaración
electrónica que vincula los datos de validación de una firma con una persona física y confirma, al
menos, el nombre o el seudónimo de esa persona;»** (art. 3.14). Hay tres clases de certificado según el
titular y el uso: de firma (persona física), de sello electrónico (persona jurídica: **«una declaración
electrónica que vincula los datos de validación de un sello con una persona jurídica y confirma el
nombre de esa persona;»**, art. 3.29) y de autenticación de sitio web (**«declaración electrónica que
permite autenticar un sitio web y vincula el sitio web con la persona física o jurídica a quien se ha
expedido el certificado;»**, art. 3.38). Cada uno puede ser cualificado si lo expide un prestador
cualificado y cumple el anexo correspondiente (I, III y IV del Reglamento).

Cómo funciona el certificado, en tres líneas: el servidor presenta un certificado firmado por una
autoridad de certificación; el navegador comprueba que esa autoridad está en su lista de confianza y
que el nombre del certificado coincide con el del sitio; si las dos cosas cuadran, negocian una clave
de sesión y a partir de ahí todo va cifrado.

Una extensión del certificado de servidor que se pregunta, el nombre alternativo del sujeto (SAN): la
RFC 5280 dice que **«The subject alternative name extension allows identities to be bound to the
subject of the certificate.»** (permite vincular más identidades al titular del certificado). El
distractor habitual es SNI:

| Sigla | Qué es | Quién la usa |
|---|---|---|
| SAN | Una extensión DEL CERTIFICADO que enumera los nombres que ampara | El certificado |
| SNI | Una extensión DEL PROTOCOLO por la que el cliente dice a qué nombre quiere conectarse | El cliente, al iniciar la conexión |

Para qué sirve cada una, con el caso que las explica: un servidor aloja tres sitios web distintos en
la misma dirección. El cliente usa la indicación del nombre para decir a cuál de los tres viene; el
servidor le presenta un certificado que, gracias al nombre alternativo, vale para los tres. Sin la
primera el servidor no sabría qué certificado enviar; sin la segunda haría falta un certificado por
sitio.

### La autoridad de certificación y la infraestructura de clave pública

Autoridad de certificación es el término técnico: **«A trusted entity that issues and revokes public
key certificates.»** (una entidad de confianza que expide y revoca certificados de clave pública,
según el NIST). Forma parte de una infraestructura de clave pública (PKI), **«A framework that is
established to issue, maintain and revoke public key certificates.»** (el marco que se establece para
expedir, mantener y revocar certificados). Los componentes de la PKI, según la RFC 5280:

| Componente | Qué es (RFC 5280) |
|---|---|
| Entidad final | **«user of PKI certificates and/or end user system that is the subject of a certificate»** (el usuario o sistema titular del certificado) |
| CA | **«certification authority»**: la autoridad de certificación, que firma los certificados |
| RA | **«registration authority, i.e., an optional system to which a CA delegates certain management functions»** (autoridad de registro: sistema opcional en el que la CA delega funciones de gestión) |
| Emisor de CRL | **«a system that generates and signs CRLs»** (genera y firma las listas de revocación) |
| Repositorio | **«a system or collection of distributed systems that stores certificates and CRLs and serves as a means of distributing these certificates and CRLs to end entities»** (almacena y distribuye certificados y listas) |

En la FNMT, la identidad del solicitante se acredita en una Oficina de Acreditación de Identidad
(epígrafe 7); verlas como la autoridad de registro del modelo de la RFC 5280 es una lectura de oficio,
no algo que diga la FNMT en las páginas leídas.

*El término legal no es «autoridad de certificación».* El eIDAS y la Ley 6/2020 hablan de
*prestador de servicios de confianza*: **«"prestador de servicios de confianza", una persona física o
jurídica que presta uno o más servicios de confianza, bien como prestador cualificado o como prestador
no cualificado de servicios de confianza»** (art. 3.19, con la corrección de errores C2); y
**«"prestador cualificado de servicios de confianza", un prestador de servicios de confianza que presta
uno o varios servicios de confianza cualificados y al que el organismo de supervisión ha concedido la
cualificación;»** (art. 3.20). La Ley 39/2015 (art. 10.2) todavía remite a la «Lista de confianza de prestadores
de servicios de certificación», terminología anterior al eIDAS.

Los servicios de confianza son, desde la reforma del Reglamento (UE) 2024/1183, catorce (art. 3.16,
letras a) a n)): expedir y validar certificados; crear y validar firmas y sellos electrónicos;
conservarlos; gestionar dispositivos de firma a distancia; expedir y validar declaraciones electrónicas
de atributos; **«i) la creación de sellos de tiempo electrónicos;»** y **«j) la validación de sellos de
tiempo electrónicos;»**; la entrega electrónica certificada y la validación de sus datos; **«m) el
archivo electrónico de datos y documentos electrónicos;»**; y **«n) la actividad de registro de datos
electrónicos en un libro mayor electrónico.»** Expedir certificados es uno de ellos: una «autoridad de
certificación» es, en lenguaje del eIDAS, un prestador que presta el servicio de la letra a).

*Las listas de confianza.* Cómo se sabe qué prestadores son cualificados: **«Cada Estado miembro
establecerá, mantendrá y publicará listas de confianza con información relativa a los prestadores
cualificados de servicios de confianza con respecto a los cuales sea responsable, junto con la
información relacionada con los servicios de confianza cualificados prestados por ellos.»** (art. 22.1),
y lo hará **«en una forma apropiada para el tratamiento automático»** (art. 22.2). Es la «Lista de
confianza de prestadores de servicios de certificación» a la que remite la Ley 39/2015.

### Vigencia, revocación y suspensión

*Vigencia.* Ley 6/2020, art. 4: **«1. Los certificados electrónicos se extinguen por caducidad a la
expiración de su período de vigencia, o mediante revocación por los prestadores de servicios
electrónicos de confianza en los supuestos previstos en el artículo siguiente.»** **«2. El período de
vigencia de los certificados cualificados no será superior a cinco años.»**

*Revocación.* El art. 5.1 de la misma ley enumera nueve supuestos, de la a) a la i). Los que más
tocan al usuario y al operador:

- **«a) Solicitud formulada por el firmante, la persona física o jurídica representada por este, un
  tercero autorizado, el creador del sello o el titular del certificado de autenticación de sitio
  web.»**
- **«b) Violación o puesta en peligro del secreto de los datos de creación de firma o de sello, o del
  prestador de servicios de confianza, o de autenticación de sitio web, o utilización indebida de
  dichos datos por un tercero.»**
- **«h) En caso de que se advierta que los mecanismos criptográficos utilizados para la generación de
  los certificados no cumplen los estándares de seguridad mínimos necesarios para garantizar su
  seguridad.»**

Los demás son la resolución judicial o administrativa (c), el fallecimiento o la extinción del titular
(d), el fin de la representación (e), el cese del prestador sin traspaso (f), la falsedad o el cambio
de los datos (g) y cualquier otra causa lícita de la declaración de prácticas (i).

La revocación es definitiva: **«Si un certificado cualificado de firma electrónica ha sido revocado
después de su activación inicial, perderá su validez desde el momento de su revocación y no podrá en
ninguna circunstancia recuperar su estado.»** (eIDAS, art. 28.4).

*Suspensión.* Es temporal y sólo si el prestador la prevé: **«Los prestadores de servicios de
confianza suspenderán la vigencia de los certificados electrónicos en los supuestos previstos en las
letras a), c) y h) del apartado anterior, así como en los casos de duda sobre la concurrencia de las
circunstancias previstas en sus letras b) y g), siempre que sus declaraciones de prácticas de
certificación prevean la posibilidad de suspender los certificados.»** (Ley 6/2020, art. 5.2).

*Cómo se comprueba el estado de un certificado.* Dos mecanismos técnicos:

- La lista de revocación (CRL). La RFC 5280: **«A CRL is a time-stamped list identifying revoked
  certificates that is signed by a CA or CRL issuer and made freely available in a public
  repository.»** (una lista con fecha y hora de los certificados revocados, firmada por la CA o el
  emisor de listas y publicada en un repositorio). Quien usa un certificado **«not only checks the
  certificate signature and validity but also acquires a suitably recent CRL and checks that the
  certificate serial number is not on that CRL»** (no sólo comprueba la firma y la vigencia, sino que
  obtiene una lista reciente y comprueba que el número de serie no está en ella).
- El protocolo OCSP (RFC 6960), que **«specifies a protocol useful in determining the current status
  of a digital certificate without requiring Certificate Revocation Lists (CRLs)»** (sirve para saber
  el estado actual de un certificado sin descargar listas).

Cuándo pedir la revocación, en palabras de la FNMT: **«La revocación puede ser solicitada en cualquier
momento, y en especial, debe ser solicitada cuando el titular crea que su certificado puede haber sido
copiado, que su PIN pueda ser conocido por un tercero, si lo ha extraviado, etc...»** (epígrafe 7).

*Identificación del solicitante.* Para un certificado cualificado, Ley 6/2020, art. 7.1: **«La
identificación de la persona física que solicite un certificado cualificado exigirá su personación
ante los encargados de verificarla y se acreditará mediante el Documento Nacional de Identidad,
pasaporte u otros medios admitidos en Derecho. Podrá prescindirse de la personación de la persona
física que solicite un certificado cualificado si su firma en la solicitud de expedición de un
certificado cualificado ha sido legitimada en presencia notarial.»** El art. 7.2 remite a una orden ministerial
las condiciones de la identificación a distancia **«mediante otros métodos de identificación como videoconferencia o vídeo-identificación
que aporten una seguridad equivalente en términos de fiabilidad a la presencia física»**. Y el 7.6
permite no exigirla de nuevo («podrá no ser exigible») si hay relación previa con identificación presencial y **«el período de tiempo
transcurrido desde la identificación fuese menor de cinco años.»** Son las tres vías que ofrece la
FNMT: oficina, vídeo-identificación y DNIe.

## 5. Sellado de tiempo

Qué es, según el eIDAS: **«"sello de tiempo electrónico", datos en formato electrónico que vinculan
otros datos en formato electrónico con un instante concreto, aportando la prueba de que estos últimos
datos existían en ese instante;»** (art. 3.33). En lenguaje técnico, la RFC 3161 describe el papel de
la autoridad de sellado de tiempo: **«The TSA's role is to time-stamp a datum to establish evidence
indicating that a datum existed before a particular time.»** (sellar un dato para dejar prueba de que
existía antes de un momento dado).

Para qué sirve en la práctica, con el ejemplo de la propia RFC: **«to verify that a digital signature
was applied to a message before the corresponding certificate was revoked thus allowing a revoked
public key certificate to be used for verifying signatures created prior to the time of revocation»**
(comprobar que una firma se hizo antes de que se revocara el certificado, de modo que siga valiendo una
firma hecha con un certificado revocado después). Es lo que permite que un documento firmado hoy siga
siendo verificable cuando el certificado haya caducado. Lo que se envía a la autoridad no es el
documento sino su resumen: **«The messageImprint field SHOULD contain the hash of the datum to be
time-stamped.»** (el campo de la petición debería contener —*SHOULD*, recomendación y no obligación— el resumen del dato que se sella).

Efectos jurídicos (eIDAS, art. 41):

1. **«No se denegarán efectos jurídicos ni admisibilidad como prueba en procedimientos judiciales a un
   sello de tiempo electrónico por el mero hecho de estar en formato electrónico o de no cumplir los
   requisitos de sello cualificado de tiempo electrónico.»**
2. **«Los sellos cualificados de tiempo electrónicos disfrutarán de una presunción de exactitud de la
   fecha y hora que indican y de la integridad de los datos a los que la fecha y hora estén
   vinculadas.»**

Requisitos del sello cualificado (art. 42.1):

- **«a) vincular la fecha y hora con los datos de forma que se elimine razonablemente la posibilidad de
  modificar los datos sin que se detecte;»**
- **«b) basarse en una fuente de información temporal vinculada al Tiempo Universal Coordinado, y»**
- **«c) haber sido firmado mediante el uso de una firma electrónica avanzada o sellado con un sello
  electrónico avanzado del prestador cualificado de servicios de confianza o por cualquier método
  equivalente.»**

No hay que confundirlo con el sello electrónico, que no prueba la fecha sino el origen: el eIDAS
define el **«"sello electrónico", datos en formato electrónico anejos a otros datos en formato
electrónico, o asociados de manera lógica con ellos, para garantizar el origen y la integridad de estos
últimos;»** (art. 3.25). El sello electrónico es la firma de una persona jurídica; el sello de tiempo
es una fecha y hora certificada.

El ENS lo exige sólo en nivel alto de trazabilidad (medida «Sellos de tiempo [mp.info.4]», **«Nivel
ALTO: mp.info.4.»**); entre sus cautelas:

- **«[mp.info.4.1] Los sellos de tiempo se aplicarán a aquella información que sea susceptible de ser
  utilizada como evidencia electrónica en el futuro.»**
- **«[mp.info.4.3] Se renovarán regularmente los sellos de tiempo hasta que la información protegida ya
  no sea requerida por el proceso administrativo al que da soporte, en su caso.»**
- **«[mp.info.4.4] Se emplearán "sellos cualificados de tiempo electrónicos" atendiendo a lo dispuesto
  en el Reglamento (UE) n.º 910/2014 y normativa de desarrollo.»**

## 6. Firma electrónica

### Las tres clases del eIDAS

| Clase | Definición (art. 3) |
|---|---|
| Firma electrónica | **«los datos en formato electrónico anejos a otros datos electrónicos o asociados de manera lógica con ellos que utiliza el firmante para firmar;»** (3.10) |
| Firma electrónica avanzada | **«la firma electrónica que cumple los requisitos contemplados en el artículo 26;»** (3.11) |
| Firma electrónica cualificada | **«una firma electrónica avanzada que se crea mediante un dispositivo cualificado de creación de firmas electrónicas y que se basa en un certificado cualificado de firma electrónica;»** (3.12) |

Las tres están encajadas: toda cualificada es avanzada, y toda avanzada es firma electrónica. El
firmante es siempre **«una persona física que crea una firma electrónica;»** (art. 3.9); la persona
jurídica no firma: sella.

*Requisitos de la avanzada* (art. 26):

- **«a) estar vinculada al firmante de manera única;»**
- **«b) permitir la identificación del firmante;»**
- **«c) haber sido creada utilizando datos de creación de la firma electrónica que el firmante puede
  utilizar, con un alto nivel de confianza, bajo su control exclusivo, y»**
- **«d) estar vinculada con los datos firmados por la misma de modo tal que cualquier modificación
  ulterior de los mismos sea detectable.»**

La letra d) es la función resumen del epígrafe 3; la c) es la razón de que la clave privada no se
comparta nunca.

*Efectos* (art. 25):

1. **«No se denegarán efectos jurídicos ni admisibilidad como prueba en procedimientos judiciales a una
   firma electrónica por el mero hecho de ser una firma electrónica o porque no cumpla los requisitos de
   la firma electrónica cualificada.»**
2. **«Una firma electrónica cualificada tendrá un efecto jurídico equivalente al de una firma
   manuscrita.»**

La equivalencia con la manuscrita es exclusiva de la cualificada. La simple y la avanzada valen como
prueba, pero sin esa equivalencia automática.

Ni el formato ni el programa garantizan nada. Guardar en PDF no hace auténtico un documento, y poder
abrirlo en cualquier sistema operativo tampoco: eso es interoperabilidad, que es otra cosa. Y una firma
pegada como imagen no es una firma electrónica: es un dibujo.

### La firma ante las Administraciones

La Ley 39/2015, art. 10.2, en su redacción vigente (desde el 30-06-2022), admite para los interesados
que se relacionan electrónicamente:

- **«a) Sistemas de firma electrónica cualificada y avanzada basados en certificados electrónicos
  cualificados de firma electrónica expedidos por prestadores incluidos en la ‘‘Lista de confianza de
  prestadores de servicios de certificación’’.»**
- **«b) Sistemas de sello electrónico cualificado y de sello electrónico avanzado basados en
  certificados electrónicos cualificados de sello electrónico expedidos por prestador incluido en la
  ‘‘Lista de confianza de prestadores de servicios de certificación’’.»**
- c) cualquier otro sistema que las Administraciones consideren válido, con registro previo del usuario
  y comunicación previa a la Secretaría General de Administración Digital; el sistema no tiene eficacia
  jurídica hasta dos meses después de esa comunicación. Las Administraciones deben garantizar que los
  de las letras a) y b) se puedan usar en todos los procedimientos.

Y una regla útil: **«Cuando los interesados utilicen un sistema de firma de los previstos en este
artículo, su identidad se entenderá ya acreditada mediante el propio acto de la firma.»** (art. 10.5).

En el ENS, la medida «Firma electrónica [mp.info.3]» admite **«cualquier tipo de firma electrónica de
los previstos en el vigente ordenamiento jurídico»** y añade, desde el nivel medio: **«[mp.info.3.r1.1] Cuando se empleen
sistemas de firma electrónica avanzada basados en certificados, estos serán cualificados.»** La firma y
el sello de los órganos administrativos (Ley 40/2015) y la interoperabilidad de las firmas son materia
del tema 15.

### La identidad en el certificado

La Ley 6/2020, art. 6.1.a), fija cómo se identifica a la persona física en un certificado: **«por su
nombre y apellidos y su número de Documento Nacional de Identidad, número de identidad de extranjero o
número de identificación fiscal, o a través de un pseudónimo que conste como tal de manera
inequívoca.»** La sede de la FNMT ofrece, entre otros, el certificado de ciudadano, los de empresa
(administrador único o solidario, persona jurídica, entidad sin personalidad jurídica) y, para el
sector público, **«Certificado de empleado público»** y **«Certificado con Seudónimo»**.

## 7. Instalación y administración de certificados electrónicos y software de la FNMT

### Dónde vive un certificado

Un certificado con su clave privada puede estar en tres sitios, y de eso depende cómo se administra:

| Soporte | Qué es | Se puede copiar |
|---|---|---|
| Software | Un fichero instalado en el almacén del sistema o del navegador; la FNMT lo llama **«Certificado software (como archivo descargable)»** | Sí, con su clave privada, como copia de seguridad |
| Tarjeta criptográfica | El certificado se obtiene en la tarjeta y su clave privada no sale de ella | No: **«No, un certificado obtenido en tarjeta no se puede exportar con clave privada.»** |
| En la nube | La clave la custodia el prestador; la FNMT ofrece al sector público el **«Certificado de Firma Centralizada»** | No es un fichero del usuario |

Las modalidades del certificado de ciudadano que ofrece la sede de la FNMT: **«App Móvil»**,
**«Certificado con Vídeo Identificación»**, **«Certificado con Acreditación Presencial»** y
**«Certificado con DNIe»**.

### Obtener el certificado de la FNMT en software

**«El proceso de obtención del Certificado software (como archivo descargable) de usuario, se divide
en cuatro pasos que deben realizarse en el orden señalado:»**

1. **«Configuración previa . Para solicitar el certificado es necesario instalar el software que se
   indica en este apartado.»** [sic: el espacio ante el punto es de la página]
2. **«Solicitud vía internet de tu Certificado . Al finalizar el proceso de solicitud, recibirás en tu
   cuenta de correo electrónico un Código de Solicitud que te será requerido en el momento de acreditar
   tu identidad y posteriormente a la hora de descargar su certificado.»**
3. **«Acreditación presencial en una Oficina de Acreditación de Identidad .»** Con el código de
   solicitud, el interesado acredita su identidad en una oficina (de la AEAT, la Seguridad Social u
   otras, con cita previa).
4. **«Descarga tu Certificado de Usuario . Aproximadamente 1 hora después de que hayas acreditado tu
   identidad en una Oficina de Acreditación de Identidad y haciendo uso de su Código de Solicitud,
   desde aquí podrás descargar e instalar tu certificado y realizar una copia de seguridad (
   RECOMENDADO ).»**

En la solicitud se fija además una contraseña: **«Asegúrate que en esta solicitud te solicita
establecer una contraseña nueva para solicitar el código y que será también requerida en el paso 4 de
la Descarga, en caso de olvido, la contraseña no se podrá recuperar teniendo que iniciar de nuevo la
solicitud.»** [sic]

### El software de la FNMT

*El Configurador FNMT-RCM.* Es el programa que hay que instalar antes de pedir el certificado, porque
las claves se generan en el equipo del solicitante: **«Para poder solicitar y obtener tu certificado
digital es necesario generar previamente un par de claves en tu equipo.»** **«Sin este software no
podrás completar la solicitud del certificado.»** La FNMT lo describe así: **«La Fábrica Nacional de
Moneda y Timbre ha desarrollado esta aplicación para solicitar las claves necesarias en la obtención de
un certificado digital. Puede ser ejecutada en cualquier navegador y sistema Operativo.»** Y no exige
manejo: **«Una vez descargado e instalado el software no es necesario hacer nada, este se ejecutará
cuando el navegador lo requiera.»**

Los requisitos del equipo y las precauciones, que son las causas de casi todos los fallos:

- Navegador: **«Última versión de cualquiera de los siguientes navegadores:»** Mozilla Firefox, Google
  Chrome, Microsoft Edge, Opera o Safari.
- **«No formatear el ordenador, entre el proceso de solicitud y el de descarga del certificado.»**
- **«Se debe realizar todo el proceso de obtención desde el mismo equipo y mismo usuario.»** Y en la
  descarga: **«Para descargar el certificado debes usar el mismo ordenador y el mismo usuario con el
  que realizaste la Solicitud e introducir los datos requeridos exactamente tal y como los introdujiste
  entonces.»**
- **«Los antivirus y proxies pueden impedir el uso de esta aplicación, por favor no utilice proxy o
  permita el acceso a esta aplicación en su proxy.»**

La razón de las dos reglas del mismo equipo y no formatear es la criptografía del epígrafe 3: la clave
privada se generó en ese equipo y para ese usuario, y el certificado que se descarga sólo funciona
emparejado con ella. Si se formatea o se cambia de usuario, la clave se pierde y hay que empezar otra
vez.

*El software para tarjeta criptográfica.* En Windows, **«La FNMT-RCM ha desarrollado un Instalable
que integra todos los elementos necesarios para el funcionamiento de los Certificados de Usuario en
Tarjeta.»**, que instala:

- **«Software adicional para certificados de usuario en tarjeta criptográfica. (Requiere Java v.8
  Update 45 hasta Java 15)»**
- **«Módulo PKCS#11, para trabajar en Mozilla.»**
- **«Módulo Smart Card Minidriver para Windows.»**

Se instala **«con permisos de administrador»**, cerrando antes los navegadores, y hay versión de 32 y de
64 bits (**«Instalador Tarjeta TC-FNMT para 64 bits (Versión 2.0.0 ; EXE - 27,5 MB)»**). Para Mac y
Linux, las **«librerías para usar tarjetas criptográficas en Mac o Linux»** (MultiCard PKCS11 FNMT
DNIe). Y unas utilidades para la tarjeta: la **«Utilidad para la Gestión de Certificados»** (versión
1.4.0.8), que sirve para **«Ver certificados»**, importar copias de seguridad y **«Cambiar o desbloquear
el PIN»**; el **«Software de Eliminación de Certificado»**, que **«Permite borrar certificados antiguos
si existen varios en la tarjeta.»**; el **«Actualizador de Claves»**, que **«Elimina claves que no están
asociadas a ningún certificado, tanto públicas como privadas.»**; y **«Formatear tarjeta»**.

### Instalar, ver y exportar

*Dónde se ven los certificados.*

- En Microsoft Edge (que usa el almacén de Windows), según la FNMT: **«acceder al menú (botón de 3
  puntos o pulsar ALT+F) y pulsar en Configuración, en el buscardor escribir "Certificados" y pulsar
  Intro. A la derecha acceder a Administrar Certificados. En la ventana pulsaremos la pestaña
  "Personal".»** [sic: «buscardor»]
- En Firefox: **«Menú / Ajustes / Privacidad y Seguridad / Certificados / botón Ver certificados.»**
- En Windows, con la consola de certificados. Hay **«tres tipos diferentes de almacenes de
  certificados»**: **«Ordenador local: el almacenamiento es local para el dispositivo y global para
  todos sus usuarios.»**, **«Usuario actual: el almacén es local para la cuenta de usuario actual del
  dispositivo.»** y **«Cuenta de servicio: el almacén es local para un servicio determinado del
  dispositivo.»** Se abren escribiendo en Ejecutar **«certlm.msc»** (equipo local) o **«certmgr.msc»**
  (usuario actual), o añadiendo el complemento Certificados a una consola `mmc`. Desde cada carpeta
  **«puede ver, exportar, importar y eliminar sus certificados.»** Una limitación: **«Si no es
  administrador del dispositivo, solo puede administrar certificados para su cuenta de usuario.»**

El certificado personal de un usuario va en su almacén (usuario actual, carpeta Personal); por eso
otro usuario del mismo equipo no lo ve.

*Exportar: la copia de seguridad.* La diferencia entre exportar con y sin clave privada, de la FAQ de
la FNMT:

- **«Ud. deberá exportar el certificado con su clave privada solo para su uso personal o como copia de
  seguridad.»** **«La clave privada servirá para realizar firma digital.»**
- **«El certificado sin la clave privada podrá exportarlo para entregarlo a todo aquel que quiera
  comunicarse con Ud. de forma segura.»**
- **«Nunca entregue copia de su clave privada a nadie bajo ningún concepto.»**

Los formatos de fichero:

| Extensión | Qué es (FNMT) |
|---|---|
| `.pfx` | **«es la copia de seguridad con clave privada de un certificado (exportado desde Internet Explorer).»** |
| `.p12` | **«es la copia de seguridad con clave privada de un certificado (exportado desde Firefox).»** |
| `.cer` | **«es un formato de exportación de clave pública desde Internet Explorer, puede ser en formato DER o formato PEM (Base64)»** |
| `.crt` | **«es un formato de exportación de clave pública desde Mozilla firefox. Es en formato PEM (Base 64).»** |

La regla: `.pfx` y `.p12` llevan la clave privada y van protegidos con contraseña; `.cer` y `.crt` sólo
la pública y se pueden repartir.

El procedimiento en Edge, resumido de la FAQ 1551 de la FNMT: Administrar certificados, pestaña
«Personal», seleccionar el certificado y pulsar «Exportar»; en el asistente de Windows, **«Seleccionamos
la opción "Exportar la clave privada"»**; dejar el formato por defecto; poner una contraseña, que
**«se pedirá para importar el certificado a otro navegador o equipo diferente»**; elegir ruta y nombre
del fichero y finalizar. **«El archivo generado en la ruta indicada será la copia de seguridad de su
certificado junto con la clave privada, guárdela en lugar seguro.»** Importar es el camino inverso
(botón «Importar» y la contraseña del fichero).

### Renovar, revocar y comprobar el estado

- Renovación: **«El proceso de renovación de tu Certificado de Ciudadano podrá realizarse durante los
  60 días previos a la fecha de caducidad de tu certificado y siempre y cuando no haya sido previamente
  revocado.»** Tiene tres pasos —configuración previa, solicitar la renovación autenticándose con el
  certificado vigente y descargar, **«Aproximadamente 1 hora después»**—. Tiene límite: si el
  certificado se obtuvo con otro certificado, con DNIe, por vídeo-identificación **«o ya fue renovado
  anteriormente»**, no se renueva sin acreditar la identidad presencialmente en una oficina.
- Revocación (la FNMT la llama anulación): con el certificado a mano, **«la revocación puede efectuarse
  en la aplicación de anulación online»**; sin él, **«por extravío, pérdida o robo, deberá personarse en
  una Oficina de Acreditación»**; y con el código de solicitud existe un servicio telefónico 24x7.
- Comprobar el estado: la FNMT ofrece **«un servicio de verificación con el que podrás confirmar si tu
  Certificado digital FNMT es Válido o ha sido Revocado.»**
- Validez: **«Si su Certificado de Ciudadano es emitido por AC FNMT Usuarios tiene un periodo de validez
  hasta el 31 de diciembre de 2028. Dicho período de validez se incluye en el propio Certificado.»** El
  límite legal de cualquier certificado cualificado es de cinco años (epígrafe 4).

## 8. Aplicación práctica

*Un puesto que se ha vuelto lento, abre ventanas de anuncios y cambia la página de inicio del
navegador.* Es el perfil del *adware* o de una aplicación potencialmente no deseada (Microsoft cita
software que **«Abra las ventanas del explorador sin autorización.»** o **«Redirigir el tráfico web sin
previo aviso y obtener consentimiento.»**). Se comprueba que el antivirus está activo
(`Get-MpComputerStatus`, «Administrar proveedores»), se hace un análisis completo y se revisan las
extensiones del navegador y los programas instalados. Si el usuario trabaja como administrador, se le
pasa a cuenta estándar.

*Los ficheros de una carpeta compartida aparecen con otra extensión y hay una nota que pide un pago.*
*Ransomware*. Primero se aísla: apagar o desconectar el equipo **«para que no se extienda a otros
dispositivos de la red interna»**; no se paga; se limpia antes de restaurar; se recupera de copia (tema
3) y se consulta No More Ransom. Si había datos personales, se avisa al responsable para la
notificación en 72 horas. Se previene con el acceso controlado a carpetas y con una copia sin conexión.

*Dónde se pone el servidor web público.* En la DMZ, nunca en la red interna; la base de datos que lo
alimenta, en la interna; el cortafuegos sólo deja entrar al 443 de la DMZ, y desde la DMZ sólo se
permiten hacia dentro las conexiones imprescindibles, expresamente autorizadas (ENS mp.com.1.2).

*Un redactor tiene que trabajar desde un hotel.* VPN de acceso remoto (de equipo a pasarela) contra la
red de la empresa, con autenticación del usuario; el túnel protege el tramo inseguro, pero el portátil
tiene que estar cifrado y con antivirus, porque los datos que guarda no los protege la VPN. Si sólo
necesita el correo, basta el acceso directo por web con HTTPS.

*Llegan correos que parecen de la casa y no lo son.* Falsificación del remitente: se revisan los
registros SPF, DKIM y DMARC del dominio propio para que los servidores receptores puedan rechazar lo
falsificado, y se forma al personal (ENS mp.s.1.7).

*Un usuario no consigue descargar su certificado de la FNMT.* Las tres comprobaciones de la sede:
mismo equipo y mismo usuario que en la solicitud, que no se ha formateado entre medias, y que el
antivirus o el *proxy* no bloquean el Configurador. Si el equipo se formateó, la clave privada se
perdió y hay que solicitar de nuevo.

*Un usuario cambia de ordenador.* Exporta el certificado con clave privada a un `.pfx` protegido con
contraseña, lo importa en el equipo nuevo y borra el fichero cuando ya no lo necesita. Si su certificado
está en tarjeta, no hay nada que exportar: basta instalar en el equipo nuevo el software de la
tarjeta.

*Un empleado pierde el portátil con su certificado instalado.* Debe pedir la revocación (Ley 6/2020,
art. 5.1.b), puesta en peligro de los datos de creación de firma); sin el certificado, en una oficina
de acreditación o por el servicio telefónico. Una vez revocado, el certificado no recupera su validez
(eIDAS, art. 28.4).

*Se quiere probar que un vídeo o un documento existía en una fecha.* Sello de tiempo: se envía su
resumen a una autoridad de sellado; si el sello es cualificado, se presume exacta la fecha y la
integridad (eIDAS, art. 41.2).

## Normativa que el tema invoca

| Norma | Qué se usa | Redacción |
|---|---|---|
| Reglamento (UE) n.º 910/2014 (eIDAS), modificado por el Reglamento (UE) 2024/1183 | Arts. 3 (definiciones 9 a 38), 22, 25, 26, 28.4, 41 y 42 | Texto consolidado de EUR-Lex de 18-10-2024, el último publicado a 05-10-2026 |
| Ley 6/2020, de 11 de noviembre, reguladora de determinados aspectos de los servicios electrónicos de confianza | Arts. 4, 5, 6.1.a) y 7 | Original, vigente desde 13-11-2020 |
| Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común | Art. 10.2 y 10.5 | Vigente desde 30-06-2022 |
| Real Decreto 311/2022, de 3 de mayo, Esquema Nacional de Seguridad | Art. 2.1; anexo II, medidas op.exp.6, mp.eq.2, mp.com.1, mp.com.2, mp.com.3, mp.info.3, mp.info.4, mp.s.1 y mp.s.2 | Anexo II en redacción original, vigente desde 05-05-2022 |
| Reglamento (UE) 2016/679 (RGPD), arts. 33 y 34, y Ley Orgánica 3/2018, art. 87 | Violaciones de seguridad e intimidad en los dispositivos del empleador | Tomados del tema 10 del común |

## Lo que este tema no da, y dónde está

- Los protocolos HTTP, HTTPS y TLS en detalle, la configuración de privacidad y seguridad de los
  navegadores, la seguridad de las redes inalámbricas y la autenticación 802.1X: tema 13.
- La aplicación Seguridad de Windows, BitLocker, el UAC, el acceso controlado a carpetas y los puntos de
  restauración en Windows 11: tema 6. El cortafuegos y la seguridad de Windows Server: tema 8.
- Las copias de seguridad y la recuperación de datos tras borrado, avería o virus: tema 3. El escritorio
  remoto y la virtualización de escritorios: tema 10.
- El ENS en su conjunto, la interoperabilidad de firmas y certificados y la firma de los órganos
  administrativos: tema 15. La protección de datos: tema 10 del común.
- La transposición de la Directiva (UE) 2022/2555 (NIS2): a 05-10-2026 no se ha publicado en el BOE la
  ley que la transpone, según la búsqueda en la legislación consolidada del BOE de ese día; siguen
  vigentes el Real Decreto-ley 12/2018, de seguridad de las redes y sistemas de información, y su
  reglamento, el Real Decreto 43/2021. El enunciado no la pide.
- La familia ISO/IEC 27000: no se ha leído (es de pago) y el enunciado no la nombra.
- El contenido de las guías CCN-STIC de bastionado de Windows 11: sólo consta su existencia en el
  listado público del CCN-CERT; no se han leído.
- Las especificaciones de los algoritmos (FIPS 197 de AES, RSA, curvas elípticas) y la criptografía
  poscuántica: no se han leído; los algoritmos se dan por su familia.
- AutoFirma y las demás aplicaciones de firma de la Administración General del Estado: no son
  software de la FNMT, que es lo que pide el enunciado.
- Qué antivirus, cortafuegos, VPN o certificados usan la RTVA y CSRTV, y si sus sistemas están
  categorizados en el ENS: no consta en ningún documento publicado.
- La validez general del certificado de ciudadano de la FNMT fuera del caso de la AC FNMT Usuarios: la
  sede sólo da esa fecha; no se afirma un plazo general.

## Trazabilidad

Todas las fuentes se leyeron el 05-10-2026, salvo el término *pharming* del glosario del NIST, leído
el 06-10-2026, y se releyeron en la verificación el 06-10-2026 (el encargo fija «hoy» en 24-09-2026, fecha del BOJA; no
consta cambio entre ambas fechas en las normas citadas).

| Fuente | Qué sostiene |
|---|---|
| Reglamento (UE) n.º 910/2014, consolidado «02014R0910 — ES — 18.10.2024» (eur-lex.europa.eu) | Definiciones de firma, certificado, servicio y prestador de confianza, sello electrónico, sello de tiempo y certificado de sitio web; listas de confianza; efectos de la firma y del sello de tiempo; requisitos de la firma avanzada y del sello cualificado de tiempo; revocación definitiva |
| Ley 6/2020 (BOE-A-2020-14046), Ley 39/2015 (BOE-A-2015-10565) y Real Decreto 311/2022 (BOE-A-2022-7191), volcados del BOE | Vigencia, revocación, suspensión, identidad e identificación; sistemas de firma ante las Administraciones; medidas del anexo II del ENS y ámbito |
| NIST, glosario del CSRC (csrc.nist.gov/glossary): términos *malware, virus, worm, Trojan horse, spyware, antivirus software, firewall, demilitarized zone, intrusion detection system, intrusion prevention system, sandbox, phishing, pharming* (leído el 06-10-2026), *virtual private network, symmetric key algorithm, asymmetric cryptography, hash function, digital signature, advanced encryption standard, certification authority, public key infrastructure* | Definiciones, con la publicación de origen que cita cada una |
| NIST SP 800-83 Rev. 1 (2013), SP 800-41 Rev. 1 (2009), SP 800-46 Rev. 2 (2016) y SP 800-77 Rev. 1 (2020) | Virus, *rootkit* y ataque combinado; tipos de cortafuegos, «denegar por defecto» y DMZ de los cortafuegos; las cuatro formas de acceso remoto y los límites del túnel; arquitecturas de VPN, ESP, IKE, VPN SSL y WireGuard |
| RFC 5280, 6960, 3161, 7208, 6376 y 9989 (rfc-editor.org, con su estado consultado ese día) | Certificado, PKI y CRL; OCSP; autoridad de sellado de tiempo; SPF; DKIM; DMARC |
| Microsoft Learn y Soporte de Microsoft, en castellano: «Cómo Microsoft identifica el malware y las aplicaciones potencialmente no deseadas», «Troyanos», «Gusanos», «Evitar infecciones por malware», «Introducción a Microsoft Defender Antivirus en Windows», «Proteger el PC contra el ransomware», «Cómo: Ver certificados con el complemento de MMC» | Categorías de malware y PUA; troyanos y gusanos; vías de infección y prevención; funcionamiento, modos, servicios y comprobación de Defender; *ransomware*; almacenes de certificados de Windows |
| INCIBE, «Ransomware. Una guía de aproximación para el empresario» (2020), y No More Ransom (nomoreransom.org/es) | Definición, vías de infección y respuesta ante el *ransomware* |
| Sede electrónica de la FNMT-RCM: obtener certificado software, configuración previa, solicitar, descargar, descarga de software, renovar, anular, verificar estado; preguntas frecuentes 1063, 1146, 1208, 1551 y 1553 | Modalidades, pasos, Configurador, precauciones, software de tarjeta y utilidades, exportación y formatos, renovación, revocación, verificación y validez |

Las citas en inglés llevan detrás, en redonda, la traducción del tema. Las páginas traducidas
automáticamente por Microsoft traen erratas, que se citan tal cual con [sic].

Oficio sin fuente detrás, y así se declara: la división de la detección en firmas y comportamiento
(apoyada sólo en la descripción de Microsoft); el cuadro de tipos de cortafuegos por capas (las
dos últimas filas siguen la distinción de la SP 800-41 entre cortafuegos de aplicación y de aplicación
web); que las oficinas de acreditación de la FNMT hagan de autoridad de registro; la regla de
que desde la DMZ no se abren conexiones hacia dentro y la arquitectura de dos cortafuegos o de tres
patas; lo que hace un cortafuegos de aplicación y el cuadro de ataques web; los usos corrientes del
aislamiento y su contraste con la virtualización; el cuadro de servicios y puertos; lo que HTTPS aporta
y no aporta; el caso de la VPN en la red abierta y el aviso de que protege el transporte y no el
destino; el cuadro de familias criptográficas con sus ejemplos (IDEA, 3DES, ChaCha20, curva elíptica),
la precisión sobre Diffie-Hellman y el uso combinado de las dos familias; cómo funciona el certificado
en la navegación; la pareja SAN y SNI; el mapa de técnicas y mecanismos; la explicación de por qué la
FNMT exige el mismo equipo y usuario; y los casos de aplicación práctica.
