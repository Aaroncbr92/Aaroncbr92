# Tema 11 del específico de Operador/a Informático · Herramientas colaborativas y ofimática Microsoft 365

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 11 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación de Microsoft: Microsoft Learn (Aplicaciones Microsoft 365, canales de actualización, ciclo de vida de Office 2019, Teams y su integración con SharePoint, canales privados y compartidos, eventos, vínculos de uso compartido, opciones de colaboración, OneDrive, historial de versiones, Exchange Online) y artículos del soporte de Microsoft (Word, Excel, PowerPoint, Outlook, OneDrive y Teams). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las páginas citadas, en línea el 05-10-2026 y leídas ese día. No se estudia Office 2019 ni el Teams clásico, que están fuera de soporte |
| Extensión | 11.000 palabras aproximadamente (con tablas) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur
Radio y Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); autenticación multifactor (MFA); colaboración entre empresas de Microsoft
Entra (B2B, *business to business*); red de entrega de contenido (CDN, *content delivery network*);
protocolo de oficina de correos, versión 3 (POP3 o POP); protocolo de acceso a mensajes de
internet, versión 4 (IMAP4 o IMAP); protocolo simple de transferencia de correo (SMTP); capa de
conexión segura y seguridad de la capa de transporte (SSL/TLS), y STARTTLS, la orden que pasa a
TLS una conexión que empezó sin cifrar; autorización abierta, versión 2.0 (OAuth 2.0); interfaz de programación de aplicaciones de mensajería (MAPI, *messaging application programming interface*), que Outlook usa sobre HTTP para hablar con Exchange; servicios web de Exchange (EWS); punto de conexión de servicio de Active Directory (SCP, *service connection
point*); localizador uniforme de
recursos (URL); formato de documento portátil (PDF); Visual Basic para Aplicaciones (VBA), el
lenguaje de macros de Office; tabla de almacenamiento personal (.pst), el archivo de datos de
Outlook; gigabyte (GB). Microsoft Entra ID es el nombre del directorio
de Microsoft (ID, de *identity*, identidad); SMTP AUTH es el envío SMTP autenticado; SUM es el
nombre interno de la operación suma en las tablas dinámicas, tal como lo escribe Microsoft. Las teclas se nombran como en el teclado español: Ctrl
(control), Mayús (mayúsculas), Alt, Supr y las de función F1 a F12.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 11): «Herramientas
> colaborativas y ofimática Microsoft 365: usos, métodos de compartición de información, trabajo en
> equipo con OneDrive, Teams y SharePoint; Word, Excel, PowerPoint y Outlook, configuración de
> cliente de correo electrónico, funcionalidades e integración con las herramientas
> colaborativas.»

Qué se puede preguntar: qué es Aplicaciones Microsoft 365, en qué se diferencia de una versión
de Office sin suscripción, en cuántos equipos se instala con una licencia, cada cuánto tiene que
conectarse y qué canales de actualización tiene; qué fue de Office 2019 y del Teams clásico; qué
crea Teams al crear un equipo; qué son un grupo de Microsoft 365 y Microsoft Entra ID; qué
herramienta conviene para cada uso (Teams, SharePoint, OneDrive); qué tres tipos de vínculo de
uso compartido hay y cuál no exige autenticarse; qué cuatro niveles de uso compartido externo
admite la organización y cuál es más restrictivo; qué estados tiene un archivo con Archivos a
petición y con qué orden se fija; qué carpetas mueve OneDrive y cuánto tiempo guarda la papelera
de reciclaje; dónde se guardan los archivos de un canal estándar, de un canal privado y de un chat;
quién crea canales privados y compartidos y quién añade gente a ellos; qué roles hay en una reunión
de Teams y qué pasó con los eventos en directo; en Word, para qué sirven los estilos de título, los
saltos de sección y la combinación de correspondencia; en Excel, las referencias relativas,
absolutas y mixtas y la tecla F4, los errores `#¡DIV/0!`, `#¡REF!` y `#N/A`, BUSCARV y BUSCARX,
las tablas dinámicas y la validación de datos; en PowerPoint, el patrón de diapositivas, las vistas
y la diferencia entre animación y transición; en Outlook, las reglas, los atajos de teclado y el
archivo .pst; cómo se agrega una cuenta de correo en el Outlook nuevo y en el clásico, qué hace la
detección automática y qué servidores, puertos y cifrado usa Exchange Online por POP, IMAP y SMTP;
en qué se diferencian POP e IMAP; qué es la autenticación básica y por qué ya no sirve en Exchange
Online; qué es la coautoría y qué exige; y cómo se programa una reunión de Teams desde Outlook. En
la aplicación práctica: elegir dónde guardar y cómo compartir un archivo; diagnosticar por qué un
usuario no ve un archivo enviado por chat; recuperar un archivo borrado; liberar espacio en un
portátil sincronizado; configurar a mano una cuenta IMAP; y explicar por qué un cliente antiguo no
se conecta al correo de la organización.

<!-- indice -->

## Índice

- [1. Microsoft 365: qué es y para qué se usa](#1-microsoft-365-qué-es-y-para-qué-se-usa)
  - [Aplicaciones Microsoft 365 frente a las versiones de Office sin suscripción](#aplicaciones-microsoft-365-frente-a-las-versiones-de-office-sin-suscripción)
  - [Canales de actualización](#canales-de-actualización)
  - [Por qué no se estudia Office 2019 ni el Teams clásico](#por-qué-no-se-estudia-office-2019-ni-el-teams-clásico)
  - [Las piezas del entorno colaborativo](#las-piezas-del-entorno-colaborativo)
  - [Qué herramienta para qué: usos](#qué-herramienta-para-qué-usos)
- [2. Métodos de compartición de información](#2-métodos-de-compartición-de-información)
  - [Vínculos en lugar de adjuntos](#vínculos-en-lugar-de-adjuntos)
  - [Los tres tipos de vínculo](#los-tres-tipos-de-vínculo)
  - [Los niveles de uso compartido externo de la organización](#los-niveles-de-uso-compartido-externo-de-la-organización)
- [3. Trabajo en equipo con OneDrive, Teams y SharePoint](#3-trabajo-en-equipo-con-onedrive-teams-y-sharepoint)
  - [OneDrive: el almacenamiento de cada usuario](#onedrive-el-almacenamiento-de-cada-usuario)
  - [SharePoint: sitios, bibliotecas y versiones](#sharepoint-sitios-bibliotecas-y-versiones)
  - [Teams: equipos, canales y pestañas](#teams-equipos-canales-y-pestañas)
  - [Tipos de canal y reparto de permisos](#tipos-de-canal-y-reparto-de-permisos)
  - [Dónde acaba cada archivo de Teams](#dónde-acaba-cada-archivo-de-teams)
  - [Mensajes y publicaciones](#mensajes-y-publicaciones)
  - [Chats, llamadas y estado](#chats-llamadas-y-estado)
  - [Reuniones, presentación y eventos](#reuniones-presentación-y-eventos)
- [4. Word, Excel, PowerPoint y Outlook](#4-word-excel-powerpoint-y-outlook)
  - [Word](#word)
  - [Excel](#excel)
  - [PowerPoint](#powerpoint)
  - [Outlook](#outlook)
- [5. Configuración del cliente de correo electrónico](#5-configuración-del-cliente-de-correo-electrónico)
  - [Agregar una cuenta: el camino automático](#agregar-una-cuenta-el-camino-automático)
  - [Configuración manual: POP, IMAP y SMTP](#configuración-manual-pop-imap-y-smtp)
  - [POP frente a IMAP](#pop-frente-a-imap)
  - [La autenticación: por qué un cliente antiguo deja de conectar](#la-autenticación-por-qué-un-cliente-antiguo-deja-de-conectar)
  - [Quitar una cuenta](#quitar-una-cuenta)
- [6. Funcionalidades e integración con las herramientas colaborativas](#6-funcionalidades-e-integración-con-las-herramientas-colaborativas)
  - [Coautoría y Autoguardado](#coautoría-y-autoguardado)
  - [Teams en Outlook](#teams-en-outlook)
  - [Archivos de Office dentro de Teams, OneDrive y SharePoint](#archivos-de-office-dentro-de-teams-onedrive-y-sharepoint)
  - [Integración entre las aplicaciones de escritorio](#integración-entre-las-aplicaciones-de-escritorio)
  - [Caso práctico](#caso-práctico)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Microsoft 365: qué es y para qué se usa

### Aplicaciones Microsoft 365 frente a las versiones de Office sin suscripción

Microsoft 365 es el nombre comercial de un conjunto de servicios en la nube y de aplicaciones de
escritorio. La parte que se instala en el puesto la define Microsoft así:

> **Aplicaciones Microsoft 365 es una versión de Office que está disponible a través de planes de
> Office 365. Incluye aplicaciones conocidas como Access, Excel, OneDrive, OneNote, Outlook,
> PowerPoint, Publisher, Skype Empresarial, Teams y Word. Puede usar estas aplicaciones para
> conectarse con servicios de Office 365 (o Microsoft 365), como SharePoint Online, Exchange Online
> y Skype Empresarial Online.**

Y añade que **Project y Visio no se incluyen con Aplicaciones Microsoft 365, pero están disponibles
en otros planes de suscripción.**

Lo que tiene en común con cualquier Office:

- **Aplicaciones Microsoft 365 es una versión completa de Office.**
- **Al implementar Aplicaciones Microsoft 365, se instala en el equipo local del usuario.
  Aplicaciones Microsoft 365 no es una versión basada en web de Office. Se ejecuta de forma local
  en el equipo del usuario.**
- Existe en 32 y en 64 bits, y en los equipos con procesador Arm **la versión de 32 bits de
  Aplicaciones Microsoft 365 no se admite**.
- Se configura con **muchas de las mismas configuraciones de directiva de grupo que usa con otras
  versiones de Office** (las directivas de grupo de Windows se estudian en el tema 6).

Y lo que la separa de una versión de Office sin suscripción, como Office 2019:

| Asunto | Aplicaciones Microsoft 365 (cita de Microsoft) |
|---|---|
| Actualizaciones | **La diferencia más significativa es que Aplicaciones Microsoft 365 se actualiza periódicamente, con frecuencia como mensualmente, con nuevas características, a diferencia de las versiones que no son de suscripción de Office.** |
| Instalación | **De forma predeterminada, Aplicaciones Microsoft 365 se instala como un único paquete**; usa **una tecnología de instalación diferente, denominada Hacer clic y ejecutar**, que por defecto toma las actualizaciones de la **Office Content Delivery Network (CDN) en Internet** |
| Quién instala | **Los usuarios deben ser administradores locales en sus equipos para instalar Aplicaciones Microsoft 365. Si los usuarios no son administradores locales, debe instalar Aplicaciones Microsoft 365 para ellos.** |
| Licencia por usuario | **Los usuarios pueden instalar Aplicaciones Microsoft 365 en hasta cinco equipos diferentes con una sola licencia de Office 365.** Además, **en hasta cinco tabletas y cinco teléfonos** |
| Conexión | **Deben conectarse al menos una vez cada 30 días para comprobar el estado de sus suscripciones de Microsoft 365. Si los usuarios no se conectan en un plazo de 30 días, Aplicaciones Microsoft 365 pasa al modo de funcionalidad reducida.** |
| Sin licencia | **En el modo de funcionalidad reducida, los usuarios pueden abrir y ver los archivos de Office existentes, pero los usuarios no pueden usar la mayoría de las demás características de Aplicaciones Microsoft 365.** |

Tampoco hay que confundir la aplicación de escritorio con la versión web: **Aplicaciones Microsoft
365 no es lo mismo que las versiones web de las aplicaciones de Office. Las versiones web permiten
a los usuarios abrir y trabajar con documentos de Word, Excel, PowerPoint o OneNote en un explorador
web.**

### Canales de actualización

El administrador elige con qué ritmo llegan las novedades. **Existen tres canales de actualización
principales**:

| Canal | Uso recomendado | Frecuencia |
|---|---|---|
| **Canal actual** | **Proporcione a los usuarios nuevas características de Aplicaciones Microsoft 365 en cuanto estén listos, pero sin una programación establecida.** | **Al menos una vez al mes (probablemente con mayor frecuencia), pero no según una programación establecida** |
| **Canal mensual para empresas** | **Proporcione a los usuarios nuevas características de Aplicaciones Microsoft 365 solo una vez al mes y según una programación predecible.** | **Una vez al mes, el segundo martes del mes** |
| **Canal empresarial semestral** | Dispositivos no interactivos o con cargas de trabajo especializadas o críticas que **requieren pruebas exhaustivas antes de implementar nuevas características** | Las nuevas características, **dos veces al año (en enero y julio, el segundo martes)**; las actualizaciones, **una vez al mes, el segundo martes del mes** |

Esa tabla es la que la página sigue mostrando, pero la misma página avisa de un cambio en curso:
**Microsoft está realizando cambios significativos en los canales de actualización a partir de julio
de 2026.** **El canal empresarial semestral recibirá actualizaciones de características y seguridad
mensuales, de la misma forma que el canal mensual de empresa.** Y en su apartado propio: **A partir de
julio de 2026, las versiones de características de Semi-Annual Enterprise Channel se admitirán durante
un mes.** El ritmo semestral (enero y julio) es, por tanto, el que el canal tenía hasta ese cambio.

### Por qué no se estudia Office 2019 ni el Teams clásico

El enunciado no fija versión, y conviene saber por qué no sirven ya dos que aún circulan en
manuales, Office 2019 y el Teams clásico:

- **Microsoft Office 2019 se rige por la directiva de ciclo de vida fijo.** Su fecha de
  finalización ampliada, en hora del Pacífico, fue el **10/15/2025 6:59:59 AM** (formato
  estadounidense: 15 de octubre de 2025). Desde entonces está fuera de soporte.
- Teams: **Se ha implementado un nuevo cliente de Teams que reemplaza al cliente clásico.** **La
  finalización del soporte para el cliente clásico de Teams comenzó el 1 de julio de 2024. La
  finalización de la disponibilidad del cliente clásico de Teams comenzó el 1 de julio de 2025.**
  Fin de disponibilidad significa que **el cliente clásico ya no funciona**.

Por eso este tema describe Word, Excel, PowerPoint, Outlook y Teams tal como los documenta hoy
Microsoft, con las páginas que se aplican a Microsoft 365 y que, en la mayoría de los casos,
siguen valiendo para las versiones 2019, 2021 y 2024.

### Las piezas del entorno colaborativo

Microsoft explica la relación entre las piezas en su página de integración de Teams y SharePoint:

| Pieza | Qué es (cita de Microsoft) |
|---|---|
| Teams | **Teams es una herramienta de colaboración en la que puede chatear con otras personas sobre un asunto o tarea determinados.** |
| SharePoint | **SharePoint es una herramienta para crear sitios web, publicar contenido y almacenar archivos.** |
| Equipo | **Un equipo es un lugar en Teams donde puede invitar a otros usuarios a colaborar. Cada equipo está conectado a uno o varios sitios de SharePoint. Estos sitios son donde se almacenan los archivos del equipo.** |
| Grupo de Microsoft 365 | **Un grupo de Microsoft 365 es un grupo de pertenencia que proporciona a los usuarios acceso a varios servicios de Microsoft 365 al mismo tiempo. La pertenencia de cada equipo se almacena en un grupo de Microsoft 365** |
| Microsoft Entra ID | **Microsoft Entra ID es el servicio de directorio donde se almacenan las cuentas de usuario de Microsoft 365.** Permite **aplicar reglas de negocio a las cuentas de usuario, como requerir la autenticación multifactor.** |

**Teams usa identidades almacenadas en Microsoft Entra ID.** Y **cuando se crea un equipo, esto es lo
que se crea**:

- **Un nuevo grupo de Microsoft 365.**
- **Un sitio de SharePoint y una biblioteca de documentos para almacenar los archivos del equipo.**
- **Un buzón y un calendario compartidos de Exchange Online.**
- **Un bloc de notas de OneNote.**

El grupo de Microsoft 365 es la llave de todo: **al agregar usuarios al grupo, se les concede
automáticamente el acceso adecuado.** Tiene tres roles: **propietarios**, que **pueden agregar o
quitar miembros**; **miembros**, que acceden **a todos los recursos del grupo, pero no puede cambiar
la configuración del grupo** (y **de forma predeterminada, los miembros pueden invitar a invitados,
aunque esa configuración se puede cambiar**); e **invitados**, **usuarios externos invitados a
participar en el grupo**. **Cualquier usuario puede crear un grupo a menos que limite la creación de
grupos a un conjunto específico de personas**; si se limita, los usuarios dejan de poder crear,
entre otros, **sitios de Microsoft SharePoint**, **Teams** y **bibliotecas compartidas en OneDrive**.

### Qué herramienta para qué: usos

La guía de Microsoft para usuarios resume el reparto en una tabla, de la que se extrae lo esencial:

| Herramienta | Usuarios principales | Ideal para | Uso compartido |
|---|---|---|---|
| Teams | Equipo | Equipos orientados a proyectos **para tener una conversación, trabajar juntos en archivos, llamar y reunirse** donde se hace el trabajo | **Los equipos pueden ser públicos (abiertos a todos los usuarios de su organización) o privados (pertenencia administrada).** |
| SharePoint | **Equipo, grupo, organización** | **Almacenar archivos en la nube y compartirlos con su equipo u organización, usar una administración de permisos sólida y crear sitios ricos en características que se agregarán a su canal de Teams.** | **Comparta archivos con su equipo, organización y usuarios externos.** |
| OneDrive | **Individual y de equipo** | **Almacenar y sincronizar archivos personales, laborales o educativos en la nube y acceder a ellos desde cualquier lugar con cualquier dispositivo. Ideal para trabajos en curso y compartidos con personas específicas.** | **Los documentos son privados hasta que los comparta.** |

La regla de oficio que se deduce: el borrador personal va en OneDrive; lo que es del equipo, en el
canal de Teams (que por debajo es SharePoint); lo que se publica para toda la organización, en un
sitio de SharePoint.

## 2. Métodos de compartición de información

### Vínculos en lugar de adjuntos

La idea de partida de Microsoft 365 es compartir el archivo, no copiarlo: **puede enviar vínculos a
documentos en lugar de enviar archivos adjuntos, que pueden revisar (y editar, si se les permite) en
Microsoft 365 para la Web. De este modo, ahorrará almacenamiento de correo electrónico y evitará
tener que conciliar varias versiones del mismo documento.** Para ello, el documento tiene que estar
en OneDrive o en SharePoint.

**Cuando un usuario comparte un archivo o carpeta en Microsoft 365, crea un vínculo que se puede
compartir con permisos para el elemento.** Al compartir, el usuario elige a quién y con qué
permiso: el soporte de Teams enumera **Puede editar, Puede revisar, Puede ver o No se puede
descargar**, y la opción **Copiar vínculo** para pegarlo en un chat o en un correo.

### Los tres tipos de vínculo

| Tipo | Quién entra | Cómo es la «clave» |
|---|---|---|
| **Cualquiera** | **Los vínculos Cualquiera conceden acceso al elemento a cualquiera que tenga el vínculo. Las personas que usen Cualquiera de los vínculos no tienen que autenticarse y sus accesos no pueden ser auditados.** | **Un vínculo Cualquiera es una clave secreta revocable y transferible.** |
| **Personas de su organización** | **Solo funcionan para las personas dentro de su organización de Microsoft 365. (No funcionan para invitados en el directorio, solo los miembros).** Quien lo abre **debe autenticarse como miembro en el directorio.** | Como el anterior, **revocable y transferible** |
| **Personas específicas** | **Los vínculos de usuarios específicos solo funcionan para las personas que especifican los usuarios al compartir el elemento.** Valen **para compartir con usuarios de la organización y personas ajenas a la organización. En ambos casos, el destinatario debe autenticarse como el usuario especificado en el vínculo.** | **Un vínculo de personas específicos es una clave secreta revocable y no transferible.** |

Las tres propiedades del vínculo Cualquiera, explicadas por Microsoft:

- **Es transferible porque se puede reenviar a otros usuarios.**
- **Es revocable porque puede revocar el acceso de todos los usuarios que usaron el vínculo
  eliminándolo.**
- **Es secreto porque no se puede adivinar ni derivar.**

Tres matices que un test aprovecha:

1. **Los vínculos de cualquier persona no se pueden usar con archivos en un sitio de canal compartido
   de Microsoft Teams.** En esos sitios, **solo se pueden enviar vínculos de personas específicos a
   otros usuarios del canal.**
2. Crear un vínculo no reparte el acceso por sí solo: **la creación de este vínculo no proporciona
   acceso de toda la organización al contenido.** El vínculo se activa al abrirlo (Microsoft lo
   llama canje). Si el vínculo de la organización se envía por la web de SharePoint u OneDrive, por
   Outlook o por un chat de Teams, **se canjea automáticamente por destinatarios individuales, hasta
   un límite de 100.** Salvedad: **Esta característica no es compatible con los destinatarios del grupo
   ni con los mensajes publicados en los canales de Microsoft Teams.**
3. Al contrario que los otros dos, **los vínculos de personas específicas hacen que el archivo o la
   carpeta asociados aparezcan en los resultados de búsqueda** de quienes se añaden al vínculo.

### Los niveles de uso compartido externo de la organización

Compartir fuera de la casa lo controla el administrador. **El uso compartido externo en SharePoint
y OneDrive usa Microsoft Entra colaboración B2B para crear cuentas de invitado para personas ajenas
a la organización.** Y viene activado: **El uso compartido externo está habilitado de forma
predeterminada en Microsoft 365, incluidos SharePoint y OneDrive.**

La configuración de la organización admite cuatro niveles, de más a menos abierto:

| Nivel | Qué permite (cita de Microsoft) |
|---|---|
| **Cualquiera** | **Los usuarios pueden compartir archivos y carpetas mediante vínculos que no requieren inicio de sesión.** |
| **Invitados nuevos y existentes** | **Los invitados se agregan al directorio cuando se comparte un elemento y deben iniciar sesión o proporcionar un código de verificación para acceder al contenido.** |
| **Invitados existentes** | **Los usuarios solo pueden compartir con invitados que ya están en el directorio de su organización.** |
| **Solo personas de la organización** | **No se permite el uso compartido externo.** |

Dos reglas de jerarquía:

- **Los sitios individuales se pueden bloquear aún más, pero no se pueden hacer más permisivos que
  la configuración de la organización.**
- **Esta configuración se puede establecer por separado para SharePoint y OneDrive, aunque la
  configuración de OneDrive no puede ser más permisiva que la configuración de SharePoint.**

El administrador puede además restringir el uso compartido externo: **restringir con qué dominios
pueden compartir los usuarios**, **limitar el uso compartido externo a personas de un grupo de
seguridad específico**, hacer que el acceso de invitado caduque, y **requerir la reautenticación
después de un período especificado para los usuarios que usan un código de verificación.** También
elige **el tipo de vínculo predeterminado que ven los usuarios cuando comparten un archivo o
carpeta**, si ese vínculo permite editar y **si los vínculos cualquiera expiran después de un
período determinado.**

En los equipos de Teams el reparto es este: en un canal estándar, **los archivos y carpetas se
pueden compartir con cualquier persona de la organización mediante vínculos que se pueden
compartir. Si el uso compartido de invitados está habilitado, se pueden usar los vínculos
Cualquiera y Personas específicas para compartir con personas ajenas a la organización.** En un
canal compartido, **no se admite el uso compartido con personas ajenas a la organización que no
sean miembros del canal.**

## 3. Trabajo en equipo con OneDrive, Teams y SharePoint

### OneDrive: el almacenamiento de cada usuario

OneDrive para la Empresa es el espacio en la nube de cada usuario de la organización, distinto del
OneDrive personal de una cuenta de Microsoft de consumo. La aplicación de sincronización lo integra
en el Explorador de archivos de Windows, y ahí entran dos funciones que el operador configura a
diario.

*Archivos a petición.* **Archivos a petición de OneDrive le ayuda a acceder a todos los archivos de
su almacenamiento en la nube en OneDrive sin tener que descargarlos y usar espacio de almacenamiento
en su equipo.** **A partir de la compilación 23.066 de OneDrive, Files On-Demand está habilitado de
forma predeterminada para todos los usuarios.** Cada archivo está en uno de tres estados, y cada uno
corresponde a un atributo que se consulta con `attrib <ruta>` y se cambia por orden:

| Estado | Atributo | Orden | Qué significa |
|---|---|---|---|
| **Solo en línea** | **Sin anclar** | `attrib +u <ruta>` | **Los archivos solo en línea no ocupan espacio en el equipo.** **Los archivos solo en línea no se pueden abrir cuando el dispositivo no está conectado a Internet.** Icono de nube azul |
| **Disponible localmente** | **Clearpin** | `attrib -p <ruta>` | **Al abrir un archivo solo en línea, se descarga en el dispositivo y pasa a ser un archivo disponible localmente.** Con «Liberar espacio» vuelve a solo en línea |
| **Siempre disponible** | **Fijado** | `attrib +p <ruta>` | Los marcados como **"Mantener siempre en este dispositivo"**, que **se descargan en el dispositivo y ocupan espacio, pero siempre están ahí incluso cuando se trabaja sin conexión.** Círculo verde con marca blanca |

Una regla de orden: **para establecer un archivo o carpeta solo en línea en "localmente
disponible", primero debe establecerlo en "siempre disponible".** Y una avería conocida: si la
opción no aparece en la configuración, Microsoft manda comprobar que el servicio **"Controlador de
filtro de archivos en la nube de Windows"** tenga el inicio automático (valor `Start` = 2 en la clave
`HKLM\SYSTEM\CurrentControlSet\Services\CldFlt`).

*Movimiento de carpetas conocidas.* OneDrive puede redirigir las carpetas de Windows a la nube.
**Hay dos ventajas principales de mover o redirigir carpetas conocidas de Windows (escritorio,
documentos, imágenes, capturas de pantalla y rollo de cámara) a Microsoft OneDrive**: **los usuarios
pueden seguir usando las carpetas con las que están familiarizados**, y **al guardar archivos en
OneDrive, se realizan copias de seguridad de los datos de los usuarios en la nube y se les
proporciona acceso a sus archivos desde cualquier dispositivo.** Se despliega por directiva: **las
directivas de OneDrive se pueden establecer mediante directiva de grupo, Intune Windows 10 plantillas
administrativas o mediante la configuración de la configuración del Registro**, con dos variantes,
**Preguntar a los usuarios si quieren mover las carpetas conocidas de Windows a OneDrive** y **Mover
silenciosamente las carpetas conocidas de Windows a OneDrive**. No vale para todo: **el movimiento de
carpetas conocido no funciona para los usuarios que sincronizan archivos de OneDrive en SharePoint
Server.**

*Recuperar lo borrado.* Hay tres escalones:

1. Papelera de Windows: **Para restaurar archivos de la Papelera de reciclaje en Windows, abra la
   Papelera de reciclaje, seleccione los archivos o carpetas que desea recuperar, haga clic con el
   botón derecho en ellos y seleccione Restaurar.** Pero **los archivos eliminados solo en línea**
   no aparecen ahí, y **los Files eliminados de la nube no aparecerán en la papelera de reciclaje del
   equipo**: se recuperan desde la papelera web.
2. Papelera de reciclaje de OneDrive, en el sitio web: con cuenta profesional o educativa, **los
   elementos de la Papelera de reciclaje se eliminan automáticamente después de 93 días, a menos que
   el administrador haya cambiado la configuración.** Con cuenta personal, **30 días después de
   colocarse allí**.
3. Restaurar todo OneDrive: **la característica Restaurar su OneDrive de OneDrive ayuda a los
   suscriptores de Microsoft 365 a deshacer todas las acciones que se produjeron en cualquier archivo
   y carpeta en los últimos 30 días.** Sirve cuando **algún archivo o carpeta de OneDrive se eliminó,
   sobrescribió, dañó o infectó con malware**. Con cuenta profesional, **Configuración>Restaurar
   OneDrive**. Ojo: **todos los archivos o carpetas creados después de la fecha del punto de
   restauración se enviarán a la papelera de reciclaje de OneDrive.**

Y un límite que no admite excepción: **si un archivo se ha eliminado permanentemente de la papelera
de reciclaje de OneDrive, nunca se podrá recuperar.**

### SharePoint: sitios, bibliotecas y versiones

**SharePoint y OneDrive en Microsoft 365 son servicios basados en la nube que ayudan a las
organizaciones a compartir y administrar contenido, conocimientos y aplicaciones**. Un **sitio de
SharePoint es un sitio web en SharePoint donde puede crear páginas web y almacenar y colaborar en
archivos.** Hay dos tipos que crea el usuario: **de forma predeterminada, los usuarios pueden crear
nuevos sitios de equipo y sitios de comunicación en SharePoint y bibliotecas compartidas en
OneDrive.** El sitio de equipo es el que va unido a un grupo de Microsoft 365 y a un equipo de Teams;
el de comunicación sirve para publicar a un público amplio (la diferencia se da como oficio: las
páginas leídas sólo los nombran).

Los archivos se guardan en bibliotecas de documentos, y cada biblioteca guarda versiones. **Los
límites del historial de versiones controlan cómo se almacenan las versiones en una biblioteca de
documentos de SharePoint o una cuenta de OneDrive.** Se fijan en cascada: **los límites se pueden
establecer en el nivel de la organización, el sitio, la biblioteca o la cuenta de usuario de
OneDrive**, y el propietario de un sitio puede **interrumpir la herencia** de los límites de la
organización. El control de versiones es lo que permite volver atrás un documento sin acudir a una
copia de seguridad, y Word lo exige: **para usar el control de versiones en Word, debe almacenar los
documentos en OneDrive o en una biblioteca de SharePoint.**

### Teams: equipos, canales y pestañas

- *Equipo*: **los equipos son colecciones de personas, contenido y herramientas que rodean
  diferentes proyectos y resultados dentro de una organización.** Puede ser privado o público; los
  públicos, abiertos a toda la organización, admiten **hasta 10 000 miembros**. **De forma
  predeterminada, todos los usuarios tienen permisos para crear un equipo.**
- *Roles del equipo*: **Hay dos roles principales en Teams**: **propietario del equipo**, **la
  persona que crea el equipo**, que puede hacer copropietario a cualquier miembro, y **miembros del
  equipo**, **las personas a las que los propietarios invitan a unirse a su equipo.** Los de fuera
  entran **como invitados o bien como participantes externos en canales compartidos**, según la
  configuración de la organización.
- *Canal*: **los canales son secciones dedicadas dentro de un equipo para mantener conversaciones
  organizadas por temas, proyectos y disciplinas específicos**. **Cada equipo viene con un canal
  estándar llamado "General".** Ese canal **no se puede eliminar (cada equipo debe tener al menos un
  canal).**
- *Pestañas*: dentro de cada canal, las secciones —Publicaciones, Archivos y las que se añadan—.

### Tipos de canal y reparto de permisos

| Tipo | Quién ve el contenido | Dónde guarda sus archivos |
|---|---|---|
| **Estándar** | Todos los miembros del equipo | Una carpeta en la biblioteca del sitio de SharePoint del equipo: **todos los canales estándar comparten un sitio de SharePoint. Hay una carpeta independiente para cada canal.** |
| **Privado** | Sólo los miembros del canal, que son un subconjunto del equipo | **Cada canal privado tiene su propio sitio de SharePoint para el almacenamiento de archivos. Solo los miembros del canal privado pueden acceder a este sitio.** |
| **Compartido** | Miembros del canal, que pueden pertenecer a otros equipos o a otras organizaciones | **Cada canal compartido tiene su propio sitio de SharePoint** |

Sobre el canal privado, la documentación de Microsoft dice:

> «Los canales privados de Microsoft Teams crean espacios prioritarios para la colaboración de los
> equipos. **Solo los usuarios del equipo que sean propietarios o miembros del canal privado podrán
> acceder al canal.** Cualquier persona, incluidos los invitados, puede agregarse como miembro de un
> canal privado **siempre y cuando sean miembros existentes del equipo**.»

Y sobre quién manda dentro de él:

> «**La persona que crea un canal privado es el propietario del canal privado y solo el propietario
> del canal privado puede agregar o quitar personas directamente.** El propietario de un canal
> privado puede agregar cualquier miembro del equipo a un canal privado que haya creado, incluyendo
> invitados. Los miembros de un canal privado tienen un espacio de conversación seguro, y cuando se
> agregan nuevos miembros, **pueden ver todas las conversaciones (incluso las conversaciones
> antiguas)** en ese canal privado.»

Y sobre quién puede crearlos:

> «**De forma predeterminada, los miembros del equipo o el propietario del equipo pueden crear un
> canal privado. Los invitados no pueden crear canales privados.** La posibilidad de crear canales
> privados se puede administrar a nivel de equipo y de organización.»

Tres consecuencias que hay que retener por separado:

1. *Sólo el propietario del canal privado añade o quita gente directamente.* Los demás miembros del
   canal, no.
2. *Sólo se puede añadir a quien ya sea miembro del equipo.* Un canal privado no es una puerta de
   entrada al equipo.
3. *Un miembro del equipo puede crear canales privados por defecto*, no hace falta ser propietario
   del equipo ni administrador global. Pero eso *se puede restringir por directiva*, y ahí la
   respuesta depende de cómo lo tenga configurado cada organización.

El canal compartido funciona al revés en la creación: **Solo los propietarios del equipo pueden
crear un canal compartido. Los miembros del equipo no pueden crearlos.** Su creador es su
propietario y **solo el propietario puede agregar o quitar personas de forma directa** (puede haber
más de un propietario). A él se
invita a gente que no es del equipo: **aunque los invitados (personas con Microsoft Entra cuentas de
invitado de su organización) no se pueden agregar a un canal compartido, puede invitar a personas de
fuera de su organización a participar en un canal compartido mediante Microsoft Entra conexión
directa B2B.** Y no cambia de naturaleza: **los canales compartidos no se pueden convertir en canales
estándar y viceversa.** **El canal compartido eliminado se puede restaurar en un plazo de 30 días
después de la eliminación**, igual que **los equipos eliminados**.

### Dónde acaba cada archivo de Teams

Es la distinción práctica más importante y la que produce más archivos «perdidos»:

- **Los Files que cargue en un canal se almacenan en la carpeta de SharePoint de su equipo. Estos
  archivos están disponibles en la pestaña Compartido en la parte superior de cada canal.**
- **Los Files que envíe en el chat se almacenan en su OneDrive para la Empresa y solo se comparten
  con las personas en esa conversación.**
- **Los archivos de OneDrive que ve en Teams son archivos de OneDrive para la Empresa asociados a su
  cuenta de Microsoft 365, no a su OneDrive personal. Actualmente, Teams no puede conectarse a su
  OneDrive personal.**

La pestaña Archivos de un canal estándar es, por tanto, una ventana a SharePoint: **la pestaña
Archivos de cada canal estándar está conectada a una carpeta de la biblioteca de documentos
predeterminada del sitio primario. La pestaña Archivos de cada canal privado y compartido está
conectada a la biblioteca de documentos predeterminada del sitio de canal correspondiente.** Y los
permisos van con el equipo: en el sitio primario, **los permisos de equipo se sincronizan con el
sitio**, y Microsoft recomienda **administrar todos los permisos a través de Teams**.

### Mensajes y publicaciones

- *Publicación*: el mensaje en un canal, visible para quien tiene acceso a él. Genera *hilo*: las
  respuestas quedan colgadas de la publicación original, no sueltas.
- *Menciones*: con @ se nombra a una persona, al canal o al equipo entero; mencionar a todo el
  equipo o canal es una de las opciones que el propietario regula en la configuración del equipo.
- *Anuncio*: publicación con titular y fondo destacado. **Los mensajes de anuncios solo están
  disponibles en canales, no en chats de grupo o individuales.**
- *Importante*: se marca desde **Establecer opciones de entrega**; **¡Aparece un mensaje
  importante con la palabra IMPORTANTE! en el chat.**
- *Moderación*: si se configura, **los moderadores pueden iniciar nuevas publicaciones en el canal
  y controlar si los miembros del equipo pueden responder a los mensajes de canal existentes.**

### Chats, llamadas y estado

- *Chat*: conversación privada entre dos personas o en grupo. *Vive fuera de los canales*, y por
  tanto *fuera del equipo*: sus archivos van al OneDrive para la Empresa de quien los comparte, no a
  la biblioteca del canal.
- *Llamadas*: de voz y de vídeo, entre personas o en grupo.
- *Estado de presencia*: Disponible, Ocupado, No molestar, Ahora vuelvo (o Vuelvo en seguida),
  Ausente y Sin conexión. **Disponible es cuando está activo en Teams y no tiene nada en el
  calendario**; **Teams establecerá automáticamente su estado de Disponible a Ausente cuando bloquee
  el equipo o cuando entre en modo de inactividad o de suspensión.** **Ocupado es cuando quieres
  centrarte en algo y aún quieres seguir recibiendo notificaciones.** **No molestar es cuando quieres
  enfocar o presentar tu pantalla y no quieres recibir notificaciones.**

### Reuniones, presentación y eventos

*Reunión*: encuentro programado o instantáneo, con calendario, invitados, sala de espera,
grabación y transcripción si la organización lo permite. **Hay tres roles entre los que elegir:
coorganizador, moderador y asistente. Los corganizadores y moderadores comparten la mayor parte de
permisos del organizador, mientras que los asistentes están más controlados.** Además, **el rol de
organizador de la reunión no se puede cambiar**, y **los coorganizadores no pueden cambiar una
reunión antes de que esta comience.**

*Compartir pantalla*: **Presente toda la pantalla o una ventana.** También se puede compartir **en
directo un archivo de PowerPoint, un archivo de Excel o una pizarra.** Para que otro maneje lo
compartido: **Seleccione Ceder el control para permitir que alguien acceda a la pantalla e
interactúe con ella.**

*Eventos*: la emisión a una audiencia grande no es una reunión. La distinción es de arquitectura:
en una reunión todos pueden hablar y verse; en un evento hay un grupo que produce y emite y una
audiencia que recibe. Los antiguos eventos en directo están retirados: **Los eventos en directo de
Teams se retiraron el 30 de junio de 2026. Los eventos programados antes del 30 de junio de 2026
reciben soporte técnico hasta el 28 de febrero de 2027.** Microsoft remite a los eventos de Teams,
con plantillas de **seminarios web y asambleas informativas**. Con Teams Enterprise:

- **Organice eventos para hasta 1000 asistentes** con micrófono y cámara de asistentes, chat,
  reacciones, levantar la mano, sondeos y preguntas y respuestas.
- **Organice eventos para hasta 10 000 asistentes en una experiencia de solo vista, con Q&A.**
- Con un complemento de licencia, **hasta 100 000 asistentes**.

Hasta mil asistentes, **Optimizar para gran audiencia** está desactivada y el organizador puede
activarla; **para eventos con más de 1000 asistentes, la opción Optimizar para gran audiencia está
activada y no se puede desactivar.** Con ella activada, **los asistentes
no pueden encender sus micrófonos y cámaras a petición, y los asistentes ven el evento con un ligero
retraso y pueden pausar y rebobinar el vídeo en directo.**

## 4. Word, Excel, PowerPoint y Outlook

### Word

*Estructura del documento.*

- Caracteres y párrafos: la unidad de formato de carácter es la fuente —tipo, tamaño, estilo,
  color—; la de párrafo, la alineación, la sangría, el interlineado y el espaciado.
- Estilos: conjuntos de formato con nombre. Aplicar estilos, y no formato directo, es lo que permite
  generar automáticamente la tabla de contenido, cambiar el aspecto de todo el documento de una vez y
  navegar por el panel de navegación. Los estilos Título 1, 2, 3 definen la jerarquía. Microsoft lo
  dice así para la tabla de contenido: **Una tabla de contenido en Word se basa en los títulos del
  documento.** **Las entradas que faltan a menudo se producen porque los títulos no tienen formato
  de títulos.** Se inserta desde **Referencias>tabla de contenido** y se actualiza con el botón
  derecho y **Actualizar campo**. Si se elige una tabla manual, **Word no usará los títulos para
  crear una tabla de contenido y no podrá actualizarlos automáticamente.**
- Secciones: **Puede usar saltos de sección para cambiar el diseño o el formato de las páginas del
  documento.** Sirven para que partes del mismo documento tengan distinta orientación, márgenes,
  columnas o encabezados y pies. No son lo mismo que los saltos de página. Tipos:

  | Salto de sección | Qué hace (cita de Microsoft) |
  |---|---|
  | Página siguiente | **Inserta un salto de sección y empieza la nueva sección en la siguiente página. Este tipo de salto de sección es útil para iniciar nuevos capítulos en un documento.** |
  | Continuo | **Inserta un salto de sección y empieza la nueva sección en la misma página. Un salto de sección continuo es útil para crear cambios de formato como un número diferente de columnas en una página.** |
  | Página par o impar | **Inserta un salto de sección y empieza la nueva sección en la siguiente página par o impar, respectivamente.** |

- Listas y esquemas: las listas numeradas y con viñetas establecen una estructura jerárquica de
  puntos dentro del documento, con sus niveles y su sangría; las listas multinivel enlazan esa
  numeración con los estilos de título. Word las crea solo: **Para iniciar una lista numerada,
  escriba 1, un punto (.), un espacio y algo de texto. Word iniciará automáticamente una lista
  numerada.** **Escriba * y un espacio antes del texto, y Word creará una lista con viñetas.**
- Tablas y objetos: tablas, imágenes, formas, gráficos, cuadros de texto.

*Herramientas de trabajo.*

- Plantillas: documentos de partida con formato y contenido predefinidos.
- Combinar correspondencia: **La combinación de correspondencia le permite crear un lote de
  documentos personalizados para cada destinatario.** Se trabaja **en el documento principal en
  Word, insertando campos de combinación** —los marcadores de posición que **indican a Word en qué
  parte del documento incluir información del origen de datos**—. **Las hojas de cálculo de Excel y
  las listas de contactos de Outlook son los orígenes de datos más comunes**. Produce cartas, correos
  electrónicos (en los que **la dirección de cada destinatario es la única dirección en la línea
  Para**), sobres, etiquetas y directorios.
- Personalización del entorno: la cinta de opciones y la barra de herramientas de acceso rápido, que
  se configura con los comandos de uso frecuente.
- Gestión de ficheros: guardar, guardar como, exportar a PDF, imprimir, recuperar versiones
  autoguardadas.

*Atajos de teclado que conviene no confundir.* En Word en español, la búsqueda no va con Ctrl+F:

| Acción | Word en español |
|---|---|
| **Mostrar el panel de tareas de Navegación para buscar en el contenido del documento.** | **Ctrl+B** |
| Buscar y reemplazar | **Ctrl+H** |
| **Mostrar el cuadro de diálogo Ir a** | **Ctrl+G** |
| **Insertar un salto de página.** | **Ctrl+Entrar** |
| **Aplicar formato en negrita al texto.** | **Ctrl+N** |
| Revisar ortografía y gramática | **F7** |

### Excel

*Libros, hojas y celdas.* Un libro contiene hojas; cada hoja es una cuadrícula de celdas
identificadas por columna y fila —`A1`—. El rango es un conjunto de celdas —`A1:B10`—. El tamaño
máximo de la hoja es de **1.048.576 filas por 16.384 columnas**.

*Referencias*, que es lo que decide si una fórmula se puede arrastrar. **De forma predeterminada, una
referencia de celda es una referencia relativa**, y **al copiar una fórmula que contiene una
referencia relativa a celda, esa referencia en la fórmula cambiará.** Microsoft lo resume con una
fórmula copiada dos celdas hacia abajo y dos hacia la derecha:

| Referencia | Qué fija | Al copiarla queda |
|---|---|---|
| `$A$1` | **columna absoluta y fila absoluta** | `$A$1` |
| `A$1` | **columna relativa y fila absoluta** | `C$1` |
| `$A1` | columna absoluta y fila relativa | `$A3` |
| `A1` | **columna relativa y fila relativa** | `C3` |

Para cambiar de tipo sin escribir los dólares: **Presione F4 para cambiar entre los tipos de
referencia.**

*Cálculos, fórmulas y funciones.*

- Toda fórmula empieza por `=`.
- Funciones habituales: `SUMA`, `PROMEDIO`, `CONTAR`, `CONTARA`, `SI`, `SUMAR.SI`, `CONTAR.SI`,
  `MAX`, `MIN`, `HOY`.
- Búsqueda: **Use BUSCARV cuando necesite encontrar elementos en una tabla o un rango por fila.** Su
  límite: **El secreto de BUSCARV es organizar los datos de forma que el valor que busque (fruta) esté
  a la izquierda del valor devuelto (cantidad) que desea encontrar.** Microsoft invita a probar
  BUSCARX, **una versión mejorada de BUSCARV que funciona en cualquier dirección y devuelve
  coincidencias exactas de forma predeterminada**; pero **BUSCARX no está disponible en Excel 2016 ni
  en Excel 2019.**

*Errores frecuentes y qué significan.*

| Error | Causa (cita de Microsoft) |
|---|---|
| `#¡DIV/0!` | **Microsoft Excel muestra el #DIV/0! cuando un número se divide por cero (0). Esto puede suceder al escribir una fórmula simple (como =5/0) o si una fórmula hace referencia a una celda con valor 0 o en blanco** |
| `#¡REF!` | **El error #REF! se muestra cuando una fórmula hace referencia a una celda que no es válida. Esto ocurre la mayoría de las veces cuando las celdas a las que se hace referencia mediante fórmulas se eliminan o se pegan encima.** |
| `#N/A` | **El error #N/A suele indicar que una fórmula no encuentra lo que se le ha pedido que busque.** Lo dan sobre todo **las funciones BUSCARX, BUSCARV, BUSCARH, BUSCAR o COINCIDIR** |
| `#¡VALOR!` | Tipo de dato incorrecto en la fórmula (oficio) |

Para que el error no se vea, **use un controlador de errores como SI.ERROR en la fórmula. Por
ejemplo, =SI.ERROR(FORMULA();0)**.

*Gestión y análisis de datos.*

- Ordenar y filtrar, con autofiltro y filtros avanzados.
- Formato condicional, que aplica formato según el valor.
- Validación de datos: **Use la validación de datos para restringir el tipo de datos o los valores
  que los usuarios escriben en una celda, como una lista desplegable.**
- Tablas dinámicas: **Una tabla dinámica es una herramienta avanzada para calcular, resumir y
  analizar datos que le permite ver comparaciones, patrones y tendencias en ellos.** Los datos de
  origen **deben organizarse en columnas con una sola fila de encabezado**; se crea con
  **Insertar>tabla dinámica**. Al marcar campos, **los campos no numéricos se agregan a Filas, las
  jerarquías de fecha y hora se agregan a Columnas y los campos numéricos se agregan a Valores**, y
  hay también un área de filtros. **De forma predeterminada, los campos de tabla dinámica colocados en
  el área Valores se muestran como SUM**. Si cambia el origen, hay que actualizarla: **si agrega
  nuevos datos al origen de datos de tabla dinámica, tendrá que actualizar las tablas dinámicas**.
- Gráficos: columnas, líneas, circulares, dispersión.
- Automatismos: macros grabadas o escritas en VBA.
- Protección: de celdas, de hoja y de libro, con contraseña.

### PowerPoint

- Vistas: **La vista Normal es el modo de edición en el que trabajará con más frecuencia para crear
  las diapositivas.** **La vista Clasificador de diapositivas (a continuación) muestra todas las
  diapositivas de la presentación en diapositivas en miniatura en secuencia horizontal.** Hay además
  la vista Página de notas, la vista Esquema —que **solo muestra el texto de las diapositivas, no las
  imágenes ni otros elementos gráficos**—, la vista Presentación con diapositivas, que **ocupa toda
  la pantalla del equipo**, y la vista Moderador.
- Patrón de diapositivas: **El patrón de diapositivas es la diapositiva superior en el panel de
  miniaturas situado a la izquierda de la ventana** en la vista Patrón de diapositivas. **Cuando el patrón de diapositivas se modifique,
  todas las diapositivas que se basen en dicho patrón reflejarán dichos cambios.** Es el equivalente
  a los estilos de Word. **Cada tema que use en la presentación incluye un patrón de diapositivas y el
  conjunto de diseños correspondiente.** Si no se puede quitar una imagen en la vista Normal,
  **puede deberse a que lo que intenta cambiar se define en el patrón de diapositivas o en un patrón
  de diseño.**
- Objetos: textos, imágenes, tablas, gráficos, diagramas —SmartArt—, formas.
- Elementos multimedia: audio y vídeo insertados o enlazados.

Animación y transición no son lo mismo, y es la distinción que un test aprovecha:

| | Animación | Transición |
|---|---|---|
| Qué es | **Una animación es un efecto especial que se aplica a un solo elemento de una diapositiva, como texto, forma, imagen, etc.** | **Una transición es el efecto especial que se produce al salir de una diapositiva y pasar a la siguiente durante una presentación.** |
| Cuántas | **Una animación se aplica a un solo elemento de una diapositiva, por lo que es posible que una diapositiva tenga varios efectos de animación.** | **Solo se puede aplicar un efecto de transición a una diapositiva.** |
| Tipos | **Los efectos de entrada hacen que aparezca un objeto. Los efectos de salida hacen desaparecer un objeto. Los efectos de énfasis resaltan un objeto ya visible. Las trayectorias de la animación mueven un objeto de una posición a otra.** | Se eligen en la pestaña Transiciones |

Y la excepción que confunde: **Transformación es un efecto de transición que tiene el aspecto de un
efecto de animación.**

### Outlook

Hoy conviven dos programas para Windows, el Outlook clásico y el nuevo Outlook para Windows, y
Microsoft documenta cada función con una pestaña para cada uno. El clásico tiene pestaña Archivo; el
nuevo, no.

- Entorno: correo, calendario, contactos (Personas), tareas y notas.
- Enviar, recibir, responder y reenviar. Responder contesta al remitente; responder a todos, también
  a los demás destinatarios; reenviar manda el mensaje a alguien nuevo, con sus archivos adjuntos.
- Reglas de mensaje: **Use rules to automatically perform specific actions on email that arrives in
  your inbox** (las reglas ejecutan acciones automáticas sobre el correo que llega: moverlo a una
  carpeta, cambiar su importancia, borrarlo). **Every rule needs at least three things: a name, a
  condition, and an action. Rules can also contain exceptions to conditions.** Con **Stop processing
  more rules** no se aplican las siguientes. Y un límite actual: **new Outlook does not support rules
  for managing third-party accounts like Gmail, Yahoo, and iCloud**.
- Libreta de direcciones: contactos, listas de distribución y, en entornos corporativos, la lista
  global de la organización.
- Archivo de datos .pst: **Los Outlook Data Files (.pst), o archivos de tablas de almacenamiento
  personal, contienen mensajes de usuario de Outlook y otros elementos de Outlook, como contactos,
  citas, tareas, notas y entradas de diario.** Sirven **para hacer una copia de seguridad de
  mensajes o almacenar elementos antiguos localmente en su equipo para mantener reducido el tamaño
  del buzón.** En el nuevo Outlook, **abrir archivos .pst en el nuevo Outlook requiere que también se
  instale Outlook clásico.**

*Métodos abreviados de teclado.* La documentación de Microsoft publica, para el Outlook clásico:

| Acción | Combinación |
|---|---|
| **Reenviar un mensaje.** | **Ctrl+F** |
| **Responder a un mensaje** | **Ctrl+R** |
| Responder a todos | **Ctrl+Mayús+R** |
| **Crear un mensaje nuevo.** | **Ctrl+Mayús+M** |
| **Enviar un mensaje.** | **Alt+S** |
| **Búsqueda de un elemento.** | **Ctrl+E o F3** |
| **Comprobar si hay nuevos mensajes.** | **Ctrl+M o F9** |
| **Ir a Calendario.** | **Ctrl+2** |

En el nuevo Outlook, reenviar sigue siendo Ctrl+F, **Enviar un mensaje de correo electrónico.** es
**Ctrl+Entrar** y **Crear un nuevo mensaje o evento de calendario.** es **Ctrl+N**; la página
española da **Ctrl+D** para **Responder mensaje de correo.**

Aquí está la trampa que el examen usa: en Outlook, clásico o nuevo, Ctrl+F reenvía —*forward*—, y
en el clásico la búsqueda va con Ctrl+E o F3. Quien traslade el hábito de otras aplicaciones, donde Ctrl+F (o Ctrl+B en Word en
español) busca, falla la pregunta.

## 5. Configuración del cliente de correo electrónico

### Agregar una cuenta: el camino automático

**Hay una gran variedad de tipos de cuentas de correo electrónico que puede agregar a Outlook, como
una cuenta Outlook.com o Hotmail.com, la cuenta profesional o educativa que usa con cuentas de
Microsoft 365, Gmail, Yahoo, iCloud y Exchange.**

| Outlook | Pasos (cita de Microsoft) |
|---|---|
| Clásico | **Seleccione Archivo>Agregar cuenta.** **Escriba su dirección de correo electrónico y seleccione Conectar.** Si se pide, la contraseña. Los pasos **son los mismos** para la primera cuenta y para las siguientes |
| Nuevo | **En la pestaña Vista , selecciona Configuración de vista o, en la pestaña Archivo , selecciona Información de la cuenta.** **Seleccione Cuentas>Sus cuentas.** Después, **Agregar cuenta**, la dirección y **Continuar** |

Con una cuenta de Exchange basta la dirección y la contraseña porque trabaja la detección
automática: **El servicio Detección automática reduce los pasos de implementación y configuración de
usuario al proporcionar acceso a los clientes a características de Exchange.** **Outlook configura los
servicios solo con el nombre de usuario y la contraseña.** En una instalación propia de Exchange
Server, los equipos del dominio encuentran el servicio por Active Directory: **el SCP almacena y
proporciona direcciones URL autoritativas del servicio Detección automática para los equipos unidos a
un dominio**; desde fuera, el cliente prueba direcciones como
**`https://autodiscover.<smtp-address-domain>/autodiscover/autodiscover.xml`**. (Active Directory se
estudia en el tema 8.)

### Configuración manual: POP, IMAP y SMTP

Cuando la detección no funciona, o el proveedor no es de Microsoft, se configura a mano. En el
Outlook clásico: **Abra Outlook clásico y seleccioneAgregar cuentade archivo>.** [*sic*: Archivo >
Agregar cuenta], **escriba su dirección de correo electrónico, seleccione Opciones avanzadas.
Después, active la casilla Permíteme configurar mi cuenta manualmente y seleccione Conectar.**
Luego se elige el tipo de cuenta —**Cuando necesite usar esta opción, normalmente seleccionará
IMAP.**— y se escriben los servidores de entrada y salida.

Los datos para un buzón de Exchange Online son estos:

| Protocolo | Servidor | Puerto | Cifrado |
|---|---|---|---|
| POP3 | **Outlook.office365.com** | **995** | **SSL/TLS** |
| IMAP4 | **Outlook.office365.com** | **993** | **SSL/TLS** |
| SMTP | **Smtp.office365.com** | **587** | **STARTTLS** |

Por qué hay tres filas y no dos: **los programas de correo electrónico POP3 e IMAP4 no usan POP3 ni
IMAP4 para enviar mensajes al servidor de correo electrónico. Los programas de correo electrónico que
usan POP3 e IMAP4 se basan en SMTP para enviar mensajes.** Para las cuentas de consumo
(Outlook.com) los servidores de entrada son los mismos, pero el de salida es **smtp-mail.outlook.com**,
también por el 587 con STARTTLS; además, **el acceso POP & IMAP está deshabilitado de forma
predeterminada** y **Outlook.com requiere el uso de autenticación moderna/OAuth2.**

Por defecto, en Exchange Online **POP3 e IMAP4 están habilitados para todos los usuarios**, pero
**si ha habilitado los valores predeterminados de seguridad en su organización, POP3 e IMAP4 se
deshabilitan automáticamente en Exchange Online.** Y no dan todo el buzón: **no ofrecen correo
electrónico enriquecido, calendario y administración de contactos**, que sí se tienen con Outlook
conectado a Exchange u Outlook en la web.

### POP frente a IMAP

| | POP3 | IMAP4 |
|---|---|---|
| Qué hace con lo descargado | **De forma predeterminada, los clientes POP3 quitan los mensajes descargados del servidor de correo electrónico.** Se puede configurar para dejar copia | **De forma predeterminada, los clientes IMAP4 no quitan los mensajes descargados del servidor de correo electrónico.** |
| Carpetas | **Los programas cliente POP3 descargan mensajes en una sola carpeta del equipo cliente (normalmente, la Bandeja de entrada).** | **Los clientes IMAP4 admiten la creación y el acceso a varias carpetas de correo electrónico en el servidor de correo electrónico.** |
| Varios equipos | Difícil, porque los mensajes quedan en el equipo local | **Este comportamiento facilita el acceso a mensajes de correo electrónico desde varios equipos.** |

El cliente decide cuándo conectarse: **Enviar y recibir mensajes cada vez que la aplicación de
correo electrónico se inicia**, **de forma manual** o **después de un número de minutos definido**.

### La autenticación: por qué un cliente antiguo deja de conectar

**La autenticación básica simplemente significa que la aplicación envía un nombre de usuario y una
contraseña con cada solicitud, y esas credenciales también se almacenan o guardan a menudo en el
dispositivo.** En Exchange Online se acabó: **La autenticación básica ahora está deshabilitada en
todos los inquilinos.** **Antes del 31 de diciembre de 2022, podía volver a habilitar los protocolos
afectados … Ahora nadie (usted o el soporte técnico de Microsoft) puede volver a habilitar la
autenticación básica en el inquilino.** La salvedad es el envío SMTP autenticado: **Aunque la
autenticación SMTP está disponible actualmente, Microsoft ha anunciado planes para retirar la
autenticación básica para autenticación SMTP en Exchange Online.** Y la autenticación SMTP ya está
deshabilitada donde no se usaba: **También hemos deshabilitado la autenticación SMTP en todos los espacios empresariales en los
que no se estaba usando.**

Lo que la sustituye es **la autenticación moderna (autorización basada en tokens de OAuth 2.0)**:
**los tokens de acceso de OAuth tienen una vida útil limitada y son específicos de las aplicaciones y
los recursos para los que se emiten, por lo que no se pueden reutilizar. Habilitar y aplicar la
autenticación multifactor (MFA) también es sencillo con la autenticación moderna.** Si una
aplicación de correo de un móvil sigue con autenticación básica, **es posible que deba quitar la
cuenta del dispositivo y volver a agregarla.**

Para POP e IMAP hay autenticación moderna; dice Microsoft: **En 2020, lanzamos la compatibilidad de
OAuth 2.0 para autenticación POP, IMAP y SMTP.** Algunos clientes de terceros ya la admiten (la página
cita Thunderbird). Pero no
Outlook: **No hay ningún plan para que los clientes de Outlook sean compatibles con OAuth para POP e
IMAP, pero Outlook puede conectarse mediante MAPI/HTTP (clientes de Windows) y EWS (Outlook para
Mac).** Es decir, a un buzón de Exchange Online, Outlook se conecta como cuenta de Exchange, no por la
configuración manual POP o IMAP del apartado anterior.

Con proveedores ajenos puede hacer falta una contraseña de aplicación (en Exchange Online no sirve
de atajo: **El desuso de la autenticación básica también impide el uso de contraseñas de aplicaciones
con aplicaciones que no admiten la verificación en dos pasos.**): **Las contraseñas de
aplicación se generan aleatoriamente contraseñas de un solo uso que proporcionan acceso temporal a las
cuentas en línea.** **En función de su proveedor de correo electrónico, puede ser necesaria una
contraseña de aplicación para agregar determinados tipos de cuenta al Outlook nuevo y clásico, como
cuentas IMAP o iCloud.**

### Quitar una cuenta

En el Outlook clásico se quita desde **Archivo**, configuración de la cuenta, **Quitar**. Quitarla no
la borra: **Quitar una cuenta de correo electrónico de Outlook clásico para Windows no desactiva la
cuenta de correo electrónico.** Lo que se pierde es la copia local: **Esto solo afecta a contenido
descargado y almacenado en el equipo.** Y si es la única cuenta, Outlook avisa de que **debe crear una
nueva ubicación para los datos antes de quitar la cuenta.**

## 6. Funcionalidades e integración con las herramientas colaborativas

### Coautoría y Autoguardado

Las aplicaciones de escritorio se unen a OneDrive y SharePoint por el archivo guardado en la nube.
**Si cualquier otra persona está trabajando en el documento, verá su presencia y los cambios que está
realizando. Esto se denomina coautoría o colaboración en tiempo real.** Tiene dos condiciones:

- El archivo en la nube: **Cuando los documentos se almacenan en línea, puede activar Autoguardado
  para guardar automáticamente como su trabajo.** También **puede compartir documentos invitando a
  alguien a la biblioteca o proporcionando un vínculo en lugar de enviar una copia discreta del
  documento.**
- Una versión con suscripción: **Si usa una versión anterior de Word, o si no está suscrito a
  Microsoft 365, puede editar el documento al mismo tiempo que otros usuarios trabajan en él, pero
  no tendrá colaboración en tiempo real. Para ver los cambios de otros usuarios y compartir los
  suyos, tendrá que guardar el documento de vez en cuando.**

Quien recibe un vínculo abre el documento en el navegador; **si prefiere trabajar en la aplicación de
Word, cambie de Edición a Abrir en el escritorio.** Dos efectos secundarios que conviene avisar al
usuario:

- **Dado que Microsoft 365 guarda automáticamente los cambios de todos los usuarios, es posible que
  los comandos Deshacer y Rehacer no funcionen según lo esperado.**
- **En Excel, cuando una persona cambia el criterio de ordenación o filtra datos, la vista cambia
  para todos los usuarios que están editando el libro.**

Y un caso particular: **si el documento contiene macros (.docm), aún puede editar y colaborar.**

### Teams en Outlook

**Depending on your version of Outlook, Microsoft Teams is either natively integrated or available
as an add-in, so that you can create Teams meetings directly in Outlook.** (Según la versión de
Outlook, Teams viene integrado o como complemento, y permite crear reuniones de Teams desde el
calendario de Outlook.) En el nuevo Outlook no hace falta complemento: **Microsoft Teams is
integrated into the new Outlook for Windows. You don't need to install a separate add-in to schedule
meetings in Outlook.** Dos límites: **The Outlook add-in doesn't support creating meetings with a
personal account.** y **POP/IMAP accounts, like @gmail.com, @yahoo.com, @icloud.com, and similar
providers, aren't supported.** Es decir, la integración exige una cuenta de trabajo de Exchange.

Al revés, el estado de presencia de Teams se ve en Outlook, y el equipo de Teams tiene **un buzón y
un calendario compartidos de Exchange Online**, que son los del grupo de Microsoft 365.

### Archivos de Office dentro de Teams, OneDrive y SharePoint

- En Teams, el botón OneDrive muestra los archivos del usuario: **Seleccione OneDrive en el lado
  izquierdo de Teams para acceder a sus archivos.** Desde ahí se comparte con **Copiar vínculo** o con
  **Configuración de uso compartido**.
- En un canal o un chat se adjunta un archivo desde **Acciones y aplicaciones>Adjuntar archivo**; si
  se adjunta en un canal, el archivo queda en la carpeta del canal en SharePoint; si en un chat, en el
  OneDrive de quien lo envía.
- Los archivos de un canal se abren y se editan dentro del propio Teams, con coautoría, y se guardan
  en la biblioteca del canal con su historial de versiones (oficio, coherente con el epígrafe 3).
- En OneDrive, **comente los documentos y use el -sign con el `@`nombre de alguien. La persona que
  menciona recibe un correo con un vínculo a su comentario.** [*sic*: el signo @ seguido del nombre].
- En una reunión de Teams se puede compartir en directo un PowerPoint; **tomar el control de una
  presentación de PowerPoint de otra persona** es una de las capacidades que la tabla de roles de la
  reunión reparte entre organizador, coorganizador, moderador y asistente (qué rol la tiene no se pudo
  leer: la tabla va con iconos).

### Integración entre las aplicaciones de escritorio

- Word con Excel y Outlook: la combinación de correspondencia toma los datos de una hoja de Excel o
  de los contactos de Outlook y puede enviar el resultado por correo desde Word (epígrafe 4).
- Excel con otras fuentes: una tabla dinámica puede crearse desde **un origen de datos externo** además
  de desde una tabla o rango de la hoja.
- Outlook con Teams: reuniones de Teams desde el calendario.
- Todas con OneDrive y SharePoint: guardar en la nube activa Autoguardado, coautoría y versiones.

### Caso práctico

1. *Un usuario envía por el chat de Teams un informe a tres compañeros; días después, uno de ellos,
   que se ha incorporado a un canal del equipo, no lo encuentra en la pestaña de archivos del
   canal.* El archivo nunca estuvo allí: lo enviado por chat está en el OneDrive para la Empresa del
   remitente y sólo lo ven los del chat. Si es documentación del equipo, se sube al canal (queda en
   SharePoint) y se comparte el vínculo.
2. *Hay que dar acceso de lectura a un periodista externo a una carpeta concreta, sin abrir la puerta
   a nadie más.* Vínculo de personas específicas con permiso de ver: no es transferible y exige que el
   destinatario se autentique. Un vínculo Cualquiera no exige autenticarse y su acceso no se puede
   auditar. Si la organización está en «Solo personas de la organización», el operador no podrá
   compartir fuera: es una decisión del administrador de SharePoint, y OneDrive no puede ser más
   permisivo que SharePoint.
3. *El disco de un portátil está lleno y el usuario tiene 80 GB en OneDrive sincronizados.* Con
   Archivos a petición, «Liberar espacio» sobre las carpetas que no se usan sin conexión (pasan a
   solo en línea, `attrib +u`); «Mantener siempre en este dispositivo» sólo para lo que deba ir de
   viaje (`attrib +p`).
4. *Un usuario borró hace dos meses una carpeta de su OneDrive de trabajo.* No estará en la papelera
   de Windows si era solo en línea; sí en la papelera de reciclaje web de OneDrive, que con cuenta
   profesional guarda 93 días salvo que el administrador lo haya cambiado. Si un ransomware cifró
   muchos archivos, Restaurar OneDrive deshace lo ocurrido en los últimos 30 días.
5. *Un usuario quiere leer el correo corporativo en un cliente de terceros configurado hace años con
   usuario y contraseña, y ya no conecta.* Exchange Online tiene la autenticación básica desactivada
   sin vuelta atrás; hace falta un cliente con autenticación moderna (OAuth 2.0). Si se configura por
   IMAP: Outlook.office365.com, puerto 993, SSL/TLS; salida por Smtp.office365.com, puerto 587,
   STARTTLS; y comprobar que la organización no tiene IMAP desactivado por los valores
   predeterminados de seguridad.
6. *En la reunión semanal se quiere que un compañero maneje la presentación del ponente.* El
   ponente comparte la ventana y usa Ceder el control; para emitir a toda la plantilla un acto de
   dos mil personas, no sirve una reunión: se crea un evento, que por encima de mil asistentes
   funciona como asamblea de solo vista.

## Lo que este tema no da, y dónde está

- La versión de Microsoft 365, de Office o de Teams que usan RTVA y CSRTV, sus planes de licencia y
  su configuración de uso compartido: no constan en ningún documento publicado.
- La cuota de almacenamiento por defecto de OneDrive para la Empresa y los límites de tamaño de
  archivo: no se han leído en fuente.
- La administración de Microsoft 365 en detalle (centro de administración, Intune, etiquetas de
  confidencialidad, retención, prevención de pérdida de datos): fuera del enunciado; las páginas
  leídas sólo las mencionan.
- El nombre exacto en español de la carpeta de OneDrive donde Teams guarda los archivos de chat: la
  página de Microsoft en español la da mal traducida y no se reproduce.
- La tabla completa de capacidades por rol en las reuniones de Teams: la página la da con iconos que
  no se pudieron leer en texto; el tema da sólo lo que dice en prosa.
- El archivo .ost (datos de Outlook sin conexión) y la diferencia entre sitio de equipo y sitio de
  comunicación de SharePoint: no se han leído en una página que los explique; se nombran como
  oficio.
- Los atajos de teclado de Word en español: la tabla de «más usados» de la página española tiene
  duplicados (Ctrl+A para abrir y para seleccionar todo; Ctrl+U para crear y para subrayar), así que
  el tema sólo da los que no se contradicen.
- Las funciones de Excel `SUMA`, `PROMEDIO`, `CONTAR`, `CONTARA`, `SI`, `SUMAR.SI`, `CONTAR.SI`,
  `MAX`, `MIN` y `HOY`, el error `#¡VALOR!`, la protección de hojas y las macros:
  se dan como oficio, sin página leída para cada una.
- OneNote, Planner, Loop, Copilot y el resto de aplicaciones de Microsoft 365: fuera del enunciado.
- Otras partes de la materia: Windows 11 y las directivas de grupo, en el tema 6; PowerShell, en el
  7; Windows Server y Active Directory, en el 8; virtualización y escritorios remotos, en el 10;
  protocolos de internet (HTTP, TLS) y redes, en el 13; seguridad, malware y certificados, en el 14;
  protección de datos personales, en el temario común.

## Trazabilidad

Todas las páginas se leyeron el 05-10-2026; las de Microsoft Learn y del soporte de Microsoft, en
español, con su traducción automática y sus erratas (se citan tal cual y se marcan con *sic* donde
estorban). Tres páginas del soporte redirigieron a su versión inglesa (reglas de Outlook,
complemento de Teams para Outlook y, en una de sus variantes, el error `#DIV/0!`); se citan en inglés
con la traducción en redonda. Entre paréntesis, la fecha de actualización que muestra la página
cuando la muestra.

| Fuente | Qué sostiene |
|---|---|
| Microsoft Learn, «Acerca de Aplicaciones Microsoft 365 en la empresa» (2025-05-20) | Definición, aplicaciones incluidas, instalación local, Hacer clic y ejecutar, CDN, administradores locales, cinco equipos, 30 días, funcionalidad reducida, versiones web, Arm |
| Microsoft Learn, «Introducción a los canales de actualización para Aplicaciones Microsoft 365» (2026-05-27) | Tres canales, uso recomendado y frecuencia; cambio del canal semestral desde julio de 2026 |
| Microsoft Learn, ciclo de vida de «Microsoft Office 2019» | Ciclo de vida fijo, fechas de soporte |
| Microsoft Learn, «Fin de disponibilidad para el cliente clásico de Teams» | Nuevo cliente, fin de soporte y de disponibilidad |
| Microsoft Learn, «Información general sobre la integración de Teams y SharePoint» (2026-06-25) | Teams, SharePoint, equipo, sitio primario, canales, grupo de Microsoft 365, Entra ID, dónde se guardan los archivos, uso compartido por tipo de canal, permisos |
| Microsoft Learn, «Introducción a Microsoft Teams para administradores» | Qué se crea con un equipo, identidades en Entra ID |
| Microsoft Learn, «Información general de los equipos y canales en Microsoft Teams» | Equipos, 10 000 miembros, roles, moderación, creación de equipos |
| Microsoft Learn, «Canales privados en Microsoft Teams» | Acceso, propietario del canal, creación |
| Microsoft Learn, «Canales compartidos en Microsoft Teams» | Creación sólo por propietarios, conexión directa B2B, no conversión, restauración en 30 días |
| Microsoft Learn, «Grupos de Microsoft 365 información general para administradores» | Recursos del grupo, roles, creación |
| Microsoft Learn, «¿Qué son los eventos en directo de Microsoft Teams?» | Retirada el 30-06-2026, transición a los eventos de Teams |
| Microsoft Learn, «Planear eventos en Teams» | Capacidades, Optimizar para gran audiencia (activable hasta 1000, obligatoria por encima) |
| Microsoft Learn, «Cómo funcionan los vínculos que se pueden compartir en OneDrive y SharePoint en Microsoft 365» (2026-05-19) | Tres tipos de vínculo y sus propiedades |
| Microsoft Learn, «Planear opciones de uso compartido y colaboración en SharePoint y OneDrive» (2023-04-07) | Sitios, uso compartido externo, cuatro niveles, restricciones, vínculo predeterminado |
| Microsoft Learn, «Consulta y establecimiento de estados de archivos a petición en Windows» (2024-09-01) | Tres estados, atributos y órdenes, servicio CldFlt |
| Microsoft Learn, «Redirigir y mover las carpetas conocidas de Windows a OneDrive» | Carpetas, ventajas, directivas, SharePoint Server |
| Microsoft Learn, «Introducción a SharePoint y OneDrive en Microsoft 365 para administradores» | Definición de SharePoint y OneDrive |
| Microsoft Learn, «Información general sobre los límites del historial de versiones» | Límites de versiones por niveles |
| Microsoft Learn, «POP3 e IMAP4 en Exchange Online» (2023-10-31) | Servidores, puertos y cifrado, SMTP, diferencias POP/IMAP, opciones de envío y recepción |
| Microsoft Learn, «Servicio Detección automática» (Exchange Server 2016, 2019 y Edición de suscripción) | Detección automática, SCP, direcciones |
| Microsoft Learn, «Desuso de la autenticación básica en Exchange Online» | Autenticación básica y moderna, SMTP AUTH, OAuth para POP e IMAP y Outlook, contraseñas de aplicación |
| Soporte de Microsoft, «Colaborar con Teams, SharePoint y OneDrive» | Tabla de usos, menciones en comentarios |
| Soporte de Microsoft, «Trabajar conjuntamente en documentos de Office» | Vínculos frente a adjuntos, Deshacer, ordenación en Excel |
| Soporte de Microsoft, «Almacenamiento de archivos en Microsoft Teams» | Archivos de canal y de chat, OneDrive personal |
| Soporte de Microsoft, «Compartir archivos en Microsoft Teams» | Permisos al compartir, adjuntar archivo |
| Soporte de Microsoft, «Ahorrar espacio en disco con Archivos a petición de OneDrive para Windows» | Activación por defecto, iconos, Liberar espacio |
| Soporte de Microsoft, «Restaurar archivos eliminados o carpetas en OneDrive» y «Restaurar su OneDrive» | Papeleras, 93 y 30 días, restauración total |
| Soporte de Microsoft, «Marcar un mensaje como importante», «Enviar un anuncio a un canal», «Cambiar el estado», «Roles en reuniones» y «Presentar contenido en reuniones» de Teams | Mensajes, presencia, roles, compartir pantalla y ceder el control |
| Soporte de Microsoft, «Insertar una tabla de contenido», «Usar saltos de sección…», «Crear una lista numerada o con viñetas», «Usar la combinación de correspondencia…» y «Métodos abreviados de teclado de Word» | Word |
| Soporte de Microsoft, «Cambiar entre referencias relativas, absolutas y mixtas», «Especificaciones y límites de Excel», «Función CONSULTAV» [*sic*, describe BUSCARV], «Función BUSCARX», «Corregir un error #N/A», «¡Cómo corregir un #REF! error», «¡Cómo corregir un #DIV/0! error», «Aplicar validación de datos a celdas» y «Crear una tabla dinámica…» | Excel |
| Soporte de Microsoft, «Elegir la vista adecuada…», «¿Qué es un patrón de diapositivas en PowerPoint?» y «La diferencia entre animaciones y transiciones» | PowerPoint |
| Soporte de Microsoft, «Métodos abreviados de teclado para Outlook», «Manage email messages by using rules in Outlook», «Abrir y buscar elementos en un archivo de datos de Outlook (.pst)», «Agregar una cuenta de correo electrónico a Outlook para Windows» y «Configuración POP, IMAP y SMTP para Outlook.com» | Outlook y cliente de correo |
| Soporte de Microsoft, «Colaborar en documentos de Word en coautoría a tiempo real» y «Usar el control de versiones con Word» | Coautoría, Autoguardado, versiones |
| Soporte de Microsoft, «Schedule a Microsoft Teams meeting from Outlook» | Integración de Teams en Outlook |

Proceden de otro temario, adaptados y releídos, la descripción de Word (caracteres y párrafos,
estilos, listas, tablas, plantillas, personalización, gestión de ficheros), la de Excel (libros,
fórmulas, funciones, ordenar, formato condicional, gráficos, macros, protección), la de PowerPoint
(objetos y multimedia) y Outlook (entorno, responder y reenviar, libreta) y la de Teams (pestañas,
publicaciones, chats, llamadas, reuniones y eventos): lo que se ha podido apoyar en una página
leída lleva la cita al lado; el resto se da como oficio. También son oficio la regla de dónde guardar
cada archivo (epígrafe 1), la distinción entre sitio de equipo y de comunicación (epígrafe 3), los
apartados de integración sin cita (epígrafe 6) y el caso práctico.
