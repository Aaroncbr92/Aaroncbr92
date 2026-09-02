# Tema 10 del específico de Gestión Administrativa · La red Internet

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 10 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | **Ninguna**: es terminología técnica común de redes, no el contenido de una norma ni de un manual de producto |
| **Identificador** | — |
| **Redacción que se estudia** | No procede |
| **Aviso sobre las fuentes** | **Una sola pregunta** —qué aparato hace falta para conectar una red doméstica— y **nueve líneas de enunciado sin preguntar nunca**. El tema las desarrolla igual, y **dice que no cita especificaciones**: lo que afirma es vocabulario de la disciplina, no la cita de un documento |
| **Extensión** | **1.294 palabras** |

<!-- /portada -->

**Las siglas de este tema, presentadas de entrada**: protocolo de control de transmisión y protocolo
de internet (**TCP/IP**), protocolo de transferencia de hipertexto (**HTTP**) y su versión segura
(**HTTPS**), sistema de nombres de dominio (**DNS**), localizador uniforme de recursos (**URL**),
protocolo de configuración dinámica de anfitrión (**DHCP**), protocolo de transferencia de ficheros
(**FTP**), protocolo simple de transferencia de correo (**SMTP**), protocolo de oficina de correos
(**POP3**), protocolo de acceso a mensajes de internet (**IMAP**), red de área local (**LAN**), red
privada virtual (**VPN**), la Red Informática Mundial (**WWW**), seguridad de la capa de transporte
(**TLS**), proveedor de acceso a internet (**ISP**), el protocolo de internet a secas (**IP**) y la
transferencia segura de ficheros (**SFTP**).

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 10):**
> «La Red Internet: terminología relacionada con internet; navegación y búsqueda; vínculos;
> favoritos; protocolos y servicios en Internet. Funcionalidades básicas de los navegadores web.
> Servicios avanzados: videoconferencia, tele-formación. Conceptos de seguridad.»

<!-- indice -->

## Índice

- [1. Qué es internet y qué es la web](#1-qué-es-internet-y-qué-es-la-web)
- [2. Lo que hace falta para conectarse](#2-lo-que-hace-falta-para-conectarse)
- [3. Direcciones, dominios y URL](#3-direcciones-dominios-y-url)
- [4. Protocolos y servicios](#4-protocolos-y-servicios)
- [5. Navegadores web](#5-navegadores-web)
- [6. Servicios avanzados](#6-servicios-avanzados)
- [7. Conceptos de seguridad en la red](#7-conceptos-de-seguridad-en-la-red)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Qué es internet y qué es la web

**Internet es la red de redes**: un conjunto mundial de redes interconectadas que se comunican
mediante la familia de protocolos **TCP/IP**. **La web no es internet**: es **uno de los servicios**
que funcionan sobre ella, el que usa HTTP para transferir documentos de hipertexto. Otros servicios
son el correo electrónico, la transferencia de ficheros, la mensajería o la voz sobre IP.

**Confundir internet con la web es el error de vocabulario más extendido**, y de él salen la mitad de
los distractores de un test.

---

## 2. Lo que hace falta para conectarse

Una conexión doméstica o de oficina necesita, como mínimo:

1. **Un acceso contratado con un proveedor de acceso a internet** —fibra, cable, línea telefónica o
   red móvil—.
2. **Un dispositivo que traduzca la señal de esa línea a datos de red y encamine el tráfico**: el
   **módem** y el **router**, hoy casi siempre integrados en un solo aparato.
3. **Un equipo con una interfaz de red**, cableada o inalámbrica.

**El componente esencial y específico es el módem-router**, y conviene ver por qué las alternativas
no lo son:

- **Un servidor web** es un programa que **sirve** páginas. Se necesita para **publicar** un sitio, no
  para **navegar**.
- **Un sistema operativo** hace falta para que el equipo funcione, pero **no establece la conexión**:
  la usa.
- **Un proyector** es un periférico de salida y no interviene.

**Qué hace cada mitad del aparato**: el **módem** adapta la señal entre el medio físico del operador
y la red local; el **router** encamina los paquetes entre la red local e internet, y normalmente
también asigna direcciones por **DHCP** y hace traducción de direcciones.

---

## 3. Direcciones, dominios y URL

- **Dirección IP**: el número que identifica a un equipo en la red. En **IPv4** son cuatro octetos
  —`192.168.1.1`—; en **IPv6**, ocho grupos hexadecimales.
- **Nombre de dominio**: el nombre legible que sustituye a la dirección. El **DNS** es el servicio que
  traduce nombres en direcciones. **Manipular esa traducción es lo que hace el *pharming***, que se
  explica en el tema 8.
- **URL**: la dirección completa de un recurso. Sus partes: **esquema** (`https`), **anfitrión**
  (`www.rtve.es`), **ruta** (`/noticias/`), y opcionalmente **puerto**, **parámetros** y
  **fragmento**.

---

## 4. Protocolos y servicios

| Protocolo | Para qué |
|---|---|
| **HTTP / HTTPS** | Transferencia de páginas web; el segundo, cifrado con **TLS** |
| **DNS** | Traducción de nombres de dominio a direcciones IP |
| **DHCP** | Asignación automática de configuración de red |
| **FTP / SFTP** | Transferencia de ficheros |
| **SMTP** | **Envío** de correo |
| **POP3 / IMAP** | **Recepción** de correo. POP3 descarga y suele borrar del servidor; **IMAP mantiene el buzón en el servidor** y sincroniza |

**La distinción entre SMTP y POP3/IMAP se pregunta mucho**: uno es para enviar, los otros para
recibir. Y entre POP3 e IMAP, la diferencia práctica es que **IMAP permite ver el mismo buzón desde
varios dispositivos**, porque los mensajes viven en el servidor.

---

## 5. Navegadores web

**Funcionalidades básicas** que comparten todos:

- **Barra de direcciones**, que en los navegadores actuales es también **caja de búsqueda**.
- **Pestañas**, para varias páginas en una ventana.
- **Historial**, con las páginas visitadas.
- **Favoritos o marcadores**: enlaces guardados por el usuario, organizables en carpetas. **Un
  favorito no guarda la página, guarda su dirección**: si la página desaparece, el favorito deja de
  funcionar.
- **Descargas**, con su gestor.
- **Navegación privada**, que **no guarda historial, cookies ni datos de formularios en el equipo**.
  **No hace anónimo al usuario**: el proveedor de acceso y el sitio visitado siguen viendo la
  conexión. Es la confusión más frecuente sobre esta función.
- **Vínculos o hipervínculos**: los enlaces que conectan un documento con otro. Son la pieza que da
  sentido al hipertexto y, con él, a la web.

---

## 6. Servicios avanzados

- **Videoconferencia**: comunicación de audio y vídeo en tiempo real entre dos o más puntos. Necesita
  ancho de banda suficiente y, sobre todo, **latencia baja**: en una conversación importa más el
  retardo que la velocidad bruta. Es el servicio del punto 12 de este mismo temario, con Teams.
- **Tele-formación**: la enseñanza a distancia sostenida en plataformas de aprendizaje, con contenidos,
  evaluación y seguimiento. Combina lo **síncrono** —clases en directo— con lo **asíncrono**
  —materiales y actividades que cada uno hace a su ritmo—.
- Otros servicios sobre internet: almacenamiento en la nube, mensajería, voz sobre IP,
  administración electrónica.

---

## 7. Conceptos de seguridad en la red

- **HTTPS y el candado**: indican que la comunicación con el sitio va **cifrada** y que el
  certificado del sitio es válido. **No garantizan que el sitio sea honrado**: un sitio fraudulento
  puede tener certificado. El candado dice **cómo** viaja la información, no **a quién** llega.
- **Cortafuegos**: filtra el tráfico entre redes según reglas.
- **VPN**: crea un túnel cifrado entre el equipo y una red remota. Sirve para acceder a la red de la
  organización desde fuera y para proteger el tráfico en redes no confiables.
- **Cookies**: pequeños ficheros que el sitio guarda en el navegador. Las hay **técnicas** —necesarias
  para que el sitio funcione— y **de seguimiento**, cuyo uso exige consentimiento.
- **Actualizaciones del navegador**: la mayoría de los ataques que llegan por la web explotan
  vulnerabilidades ya corregidas.

**Y las amenazas que llegan por la red están en el tema 8**: *phishing*, *pharming*, troyanos y
*ransomware*, con la distinción entre las dos primeras, que es la que el examen pregunta.

---

## 8. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Dónde se contesta |
|---|---|---|
| 34 | Qué componente es esencial para conectar una red doméstica | Epígrafe 2: **el módem o router** |

**Una sola pregunta.** El resto del enunciado del programa —terminología, navegación y búsqueda,
vínculos, favoritos, protocolos y servicios, funcionalidades de los navegadores, videoconferencia,
tele-formación y conceptos de seguridad— **no ha caído ni una vez**, y va desarrollado por la regla
del apartado 7 del manual.

---

## 9. Trazabilidad

**Este punto no cita ningún producto ni ninguna norma**, y su contenido es **terminología técnica
común de redes**: los protocolos que se describen están definidos en documentos de peticiones de
comentarios del organismo que estandariza internet, y sus nombres y funciones son de dominio público
en la disciplina.

**No se ha descargado ninguno de esos documentos para este tema**, y conviene decirlo: lo que aquí se
afirma es vocabulario de la materia, no la cita de una especificación. **La única pregunta del examen
no requiere más**: qué aparato hace falta para conectar una red doméstica a internet.

- **Cuadernillo `23_preguntas_gea`**, pregunta 34, con su plantilla oficial.
