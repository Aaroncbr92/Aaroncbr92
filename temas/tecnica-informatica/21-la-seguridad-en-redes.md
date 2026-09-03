# Tema 21 del específico de Técnica Informática · La seguridad en redes

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 24 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la seguridad perimetral y de aplicación, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Rasgo del punto** | **Es el que mejor mide si alguien ha montado una red o sólo la ha leído**: una de sus preguntas describe una situación completa y pide la consecuencia |
| **Extensión** | **1.896 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la zona desmilitarizada o red perimetral (**DMZ**);
el nombre alternativo del sujeto de un certificado (**SAN**, *subject alternative name*) y la
indicación del nombre del servidor (**SNI**, *server name indication*); el cortafuegos de aplicación
web (**WAF**, *web application firewall*); la red privada virtual (**VPN**); la red inalámbrica de
área local (**WLAN**); el protocolo de transferencia de hipertexto (**HTTP**) y su versión segura
(**HTTPS**); el sistema de detección de intrusiones (**IDS**) y el de prevención (**IPS**); el lenguaje de
consulta estructurado (**SQL**) del tema 1 y la biblioteca de infraestructura de tecnologías de la
información (**ITIL**) del tema 20; y el
formato de certificado **X.509**, que es un número de norma y no unas siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 24):
> «La seguridad en redes. Tipos de ataques y herramientas para su prevención. La seguridad en el nivel
> de aplicación. Seguridad perimetral. Redes Privadas Virtuales (VPN). Cortafuegos. Tipos de ataques y
> protección de servicios web.»

**Cinco preguntas.** **Y es el punto que mejor mide si alguien ha montado una red o sólo la ha
leído**: **una de sus preguntas describe una situación completa y pide la consecuencia.**

**Su reparto**: **una es de arquitectura perimetral**, **una de certificados**, **una de aislamiento
de procesos**, **una de cortafuegos de aplicación** y **una de red privada virtual.**

<!-- indice -->

## Índice

- [1. La seguridad perimetral y la zona desmilitarizada](#1-la-seguridad-perimetral-y-la-zona-desmilitarizada)
- [2. Los certificados y sus extensiones](#2-los-certificados-y-sus-extensiones)
- [3. El aislamiento de procesos](#3-el-aislamiento-de-procesos)
- [4. Los cortafuegos](#4-los-cortafuegos)
- [5. La red privada virtual](#5-la-red-privada-virtual)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. La seguridad perimetral y la zona desmilitarizada

**La pregunta 15**: **una red perimetral o zona desmilitarizada se considera menos segura que las
redes internas, pero más segura que las redes externas.** Ésa es la respuesta oficial.

---

**Y la respuesta está en la propia razón de ser de esa zona**, que es lo que hay que entender:

| Zona | Qué contiene | Quién llega |
|---|---|---|
| **Externa** | **Internet** | **Cualquiera** |
| **Perimetral** | **Lo que tiene que ser accesible desde fuera**: servidor web, correo, portal ✔ | **Desde fuera, sí; hacia dentro, no** |
| **Interna** | **Lo que nunca debe verse desde fuera**: bases de datos, ficheros, puestos | **Sólo desde dentro** |

**La regla que la define, y que es la respuesta**: **desde la zona perimetral NO se puede iniciar una
conexión hacia la red interna.** **Ésa es toda su gracia**: **si alguien toma el servidor web
publicado, se queda ahí y no salta al interior.**

**Y de ahí la ordenación de la pregunta**: **es más segura que internet porque está detrás de un
cortafuegos, y menos que la interna porque está expuesta a propósito.**

**La arquitectura clásica se monta con dos cortafuegos o con uno de tres patas**, y **la diferencia
práctica es que con dos, para llegar de fuera a dentro hay que atravesar dos equipos distintos**, a
poder ser de fabricantes distintos.

## 2. Los certificados y sus extensiones

**La pregunta 23**: **la extensión de los certificados X.509 que permite cubrir múltiples dominios web
con un único certificado HTTPS es SAN.** Ésa es la respuesta oficial.

---

**El distractor bueno es SNI**, porque **las dos siglas aparecen siempre juntas y hacen cosas
complementarias:**

| Sigla | Qué es | Quién la usa |
|---|---|---|
| **SAN** | **Una extensión DEL CERTIFICADO** que enumera los nombres que ampara | **El certificado** ✔ |
| **SNI** | **Una extensión DEL PROTOCOLO** por la que el cliente dice a qué nombre quiere conectarse | **El cliente, al iniciar la conexión** |

**Para qué sirve cada una, con el caso que las explica**: **un servidor aloja tres sitios web
distintos en la misma dirección.** **El cliente usa la indicación del nombre para decir a cuál de los
tres viene**; **el servidor le presenta un certificado que, gracias al nombre alternativo, vale para
los tres.** **Sin la primera el servidor no sabría qué certificado enviar; sin la segunda haría falta
un certificado por sitio.**

**Las otras dos opciones —«Host» y «VirtualHost»— no son extensiones de certificado**: **la primera es
una cabecera de HTTP y la segunda una directiva de configuración de servidor web.**

## 3. El aislamiento de procesos

**La pregunta 36**: **la técnica de seguridad que se basa en ejecutar programas en un espacio virtual
limitado, donde se pueden controlar todos los procesos sin que afecten al resto del equipo, se
denomina sandboxing.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son de tres categorías distintas**, lo que hace la pregunta fácil si se
leen:

| Opción | Qué es |
|---|---|
| **ITIL** | **Un marco de gestión de servicios**: el tema 20 |
| **Phishing** | **Un ataque**, no una defensa |
| **Sandboxing** | **Una técnica de aislamiento** ✔ |
| **Sniffer** | **Una herramienta de análisis de tráfico** |

**Dónde se usa el aislamiento en la práctica**: **el navegador ejecuta cada pestaña en su propia caja,
el sistema operativo móvil encierra cada aplicación en la suya, y el antivirus detona los adjuntos
sospechosos dentro de una para ver qué hacen antes de dejarlos pasar.**

**Y el contraste con la virtualización del tema 17**: **la máquina virtual aísla un sistema operativo
entero; la caja de arena aísla un proceso.** **La idea es la misma —limitar el daño— a dos escalas.**

## 4. Los cortafuegos

**La pregunta 39**: **un WAF es un Web Application Firewall.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son la misma expresión con una palabra cambiada** —*Wide Area*, *Filter*
en vez de *Firewall*—, **de modo que la pregunta es de memoria literal.** **El apoyo está en que la
«A» es de *application*, no de *area*.**

**Los tipos de cortafuegos, que es lo que da sentido a la respuesta:**

| Tipo | En qué capa decide | Qué mira |
|---|---|---|
| **De filtrado de paquetes** | **Red y transporte** | **Direcciones y puertos** |
| **Con estado** | **Red y transporte** | **Además, si el paquete pertenece a una conexión ya establecida** |
| **De aplicación (WAF)** | **Aplicación** | **El contenido de la petición web** ✔ |

**Qué hace un cortafuegos de aplicación web que los otros no pueden**: **entiende HTTP.** **Un
cortafuegos corriente ve una petición al puerto 443 y la deja pasar**; **el de aplicación lee lo que
va dentro y puede rechazar una inyección de instrucciones en una consulta o un guion incrustado en un
formulario.**

**Los ataques que el enunciado pide y que ese cortafuegos ataja:**

| Ataque | En qué consiste |
|---|---|
| **Inyección de SQL** | **Meter instrucciones de consulta en un campo del formulario** |
| **Guion entre sitios** | **Colar código de navegador que se ejecuta en la sesión de otro usuario** |
| **Falsificación de petición** | **Hacer que el navegador de la víctima envíe una petición legítima sin querer** |
| **Denegación de servicio** | **Agotar los recursos del servicio con peticiones** |

## 5. La red privada virtual

**La pregunta 77 es la mejor del punto**, porque **describe una situación entera**: **un usuario en una
red inalámbrica abierta y pública, con una conexión de red privada virtual establecida por software
hacia la red de su empresa, navegando por la intranet.** **La pregunta es si otro usuario de esa misma
red inalámbrica podría espiarlo con un analizador de tráfico.**

**La respuesta oficial**: **no, tanto si el protocolo de navegación es HTTP como si es HTTPS, porque
el tráfico a través de la red privada virtual está cifrado.**

---

**Y la clave está en el orden en que se aplican los cifrados:**

1. **El navegador produce la petición**, cifrada o no según el protocolo.
2. **El cliente de red privada virtual mete esa petición entera dentro de su propio túnel cifrado.**
3. **Lo que sale por la tarjeta inalámbrica es el túnel**, no la petición.

**Por eso el vecino no ve nada**: **lo único que capta es tráfico cifrado hacia la pasarela de la
empresa.** **Ve QUE hay tráfico y CUÁNTO, y no ve qué.**

**Las tres opciones falsas, y por qué cada una se equivoca:**

| Opción | Su error |
|---|---|
| **a) Sólo si es HTTP y no HTTPS** | **Confunde el nivel**: la protección la da el túnel, no el protocolo de dentro |
| **b) Sí, con los dos protocolos** | **Ignora el túnel por completo** |
| **c) No, porque el tráfico de la red inalámbrica está cifrado** | **El enunciado dice «abierta»**, y **una red abierta no cifra nada** |

**La opción c es la trampa fina**: **da la respuesta correcta con el argumento equivocado.** **Y eso
la hace falsa**, porque **si el razonamiento fuera ése, en una red abierta el usuario estaría
expuesto.**

**Y el aviso de oficio que este caso deja**: **una red privada virtual protege el transporte, no el
destino.** **Si el usuario visita un sitio malicioso a través del túnel, el túnel lo lleva
igualmente.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 15 | Nivel de seguridad de una red perimetral | c) Menos segura que la interna, más que la externa ✔ |
| 23 | Extensión de X.509 para cubrir varios dominios | b) SAN ✔ |
| 36 | Técnica de ejecución en espacio virtual limitado | c) Sandboxing ✔ |
| 39 | Qué dispositivo es un WAF | d) *Web Application Firewall* ✔ |
| 77 | Si un vecino puede espiar tráfico bajo una red privada virtual | d) No, porque el tráfico de la VPN está cifrado ✔ |

**Las cinco respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la pregunta 77 es la que más enseña del punto entero.** **Entender el orden
en que se encapsulan los cifrados contesta ésa y cualquier variante que pongan.** **Y la pareja SAN y
SNI es el dato más confundible: conviene fijarlo.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La norma que define el formato de certificado X.509 y las especificaciones de sus extensiones no
   se han consultado.** **Lo que el tema afirma del nombre alternativo del sujeto y de la indicación
   del nombre del servidor es de uso universal**, y **coincide con la respuesta oficial de la
   pregunta 23.**
2. **La forma larga de WAF procede de la propia respuesta oficial de la pregunta 39.**
3. **La arquitectura de zona perimetral, la clasificación de cortafuegos y la lista de ataques a
   servicios web son oficio de seguridad de redes**, de uso universal, **presentados como conocimiento
   común de la materia.**
4. **El razonamiento de la pregunta 77 no procede de ninguna fuente: se deduce del orden de
   encapsulación**, y **queda escrito paso a paso para que se pueda comprobar.**

**El resto del tema va como oficio y así se declara**: la regla de que desde la zona perimetral no se
inicia conexión hacia dentro, el caso que explica la pareja SAN y SNI, los usos corrientes del
aislamiento de procesos, el contraste con la virtualización, lo que un cortafuegos de aplicación ve y
los otros no, y el aviso de que una red privada virtual protege el transporte y no el destino. **Nada
de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
