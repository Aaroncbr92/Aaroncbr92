# Esquema · Tema 21 del específico de Técnica Informática · La seguridad en redes

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de seguridad de redes ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: la zona desmilitarizada o red perimetral
(**DMZ**); el nombre alternativo del sujeto de un certificado (**SAN**) y la indicación del nombre del
servidor (**SNI**); el cortafuegos de aplicación web (**WAF**); la red privada virtual (**VPN**); la
red inalámbrica de área local (**WLAN**); el protocolo de transferencia de hipertexto (**HTTP**) y su
versión segura (**HTTPS**); el sistema de detección de intrusiones (**IDS**) y el de prevención
(**IPS**); el lenguaje de consulta estructurado (**SQL**) del tema 1 y la biblioteca de
infraestructura de tecnologías de la información (**ITIL**) del tema 20; y el formato de certificado
**X.509**, que es un número de norma y no unas siglas.

**Cabecera.** Enunciado: punto 24 del anexo · **5 preguntas** · **ninguna lleva figura** · **es el
punto que mejor mide si alguien ha montado una red o sólo la ha leído**: **una de sus preguntas
describe una situación completa y pide la consecuencia.**

<!-- indice -->

## Índice

- [La zona perimetral](#la-zona-perimetral)
- [Certificados](#certificados)
- [Aislamiento de procesos](#aislamiento-de-procesos)
- [Cortafuegos](#cortafuegos)
- [La red privada virtual](#la-red-privada-virtual)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La zona perimetral

- **PREGUNTA 15** · `[exam]` · **La red perimetral es menos segura que las internas y más segura que
  las externas.**

| Zona | Qué contiene | Quién llega |
|---|---|---|
| **Externa** | **Internet** | **Cualquiera** |
| **Perimetral** | **Lo que tiene que ser accesible desde fuera**: web, correo, portal ✔ | **Desde fuera sí; hacia dentro no** |
| **Interna** | **Lo que nunca debe verse desde fuera**: bases de datos, ficheros, puestos | **Sólo desde dentro** |

- **LA REGLA QUE LA DEFINE, Y QUE ES LA RESPUESTA**: **desde la zona perimetral NO se puede iniciar
  una conexión hacia la red interna.** **Ésa es toda su gracia**: **si alguien toma el servidor web
  publicado, se queda ahí.**
- **DE AHÍ LA ORDENACIÓN**: **más segura que internet porque está detrás de un cortafuegos, y menos
  que la interna porque está expuesta a propósito.**
- **SE MONTA CON DOS CORTAFUEGOS O CON UNO DE TRES PATAS**: **con dos, para llegar de fuera a dentro
  hay que atravesar dos equipos distintos**, a poder ser de fabricantes distintos.

## Certificados

- **PREGUNTA 23** · `[exam]` · **La extensión de X.509 que cubre varios dominios con un solo
  certificado es SAN.**

| Sigla | Qué es | Quién la usa |
|---|---|---|
| **SAN** | **Extensión DEL CERTIFICADO** que enumera los nombres que ampara | **El certificado** ✔ |
| **SNI** | **Extensión DEL PROTOCOLO** por la que el cliente dice a qué nombre viene | **El cliente, al conectar** |

- **EL CASO QUE LAS EXPLICA**: **un servidor aloja tres sitios en la misma dirección.** **El cliente
  usa la indicación del nombre para decir a cuál viene; el servidor le presenta un certificado que,
  gracias al nombre alternativo, vale para los tres.** **Sin la primera el servidor no sabría qué
  certificado enviar; sin la segunda haría falta uno por sitio.**
- **LAS OTRAS DOS OPCIONES NO SON EXTENSIONES DE CERTIFICADO**: **«Host» es una cabecera de HTTP y
  «VirtualHost» una directiva de configuración de servidor web.**

## Aislamiento de procesos

- **PREGUNTA 36** · `[exam]` · **Ejecutar programas en un espacio virtual limitado se llama
  sandboxing.**

| Opción | Qué es |
|---|---|
| **ITIL** | **Un marco de gestión de servicios**: el tema 20 |
| **Phishing** | **Un ataque**, no una defensa |
| **Sandboxing** | **Una técnica de aislamiento** ✔ |
| **Sniffer** | **Una herramienta de análisis de tráfico** |

- **DÓNDE SE USA** · `[of]` · **el navegador ejecuta cada pestaña en su caja, el sistema operativo
  móvil encierra cada aplicación en la suya, y el antivirus detona los adjuntos sospechosos dentro de
  una para ver qué hacen antes de dejarlos pasar.**
- **EL CONTRASTE CON LA VIRTUALIZACIÓN DEL TEMA 17**: **la máquina virtual aísla un sistema operativo
  entero; la caja de arena aísla un proceso.** **La misma idea a dos escalas.**

## Cortafuegos

- **PREGUNTA 39** · `[exam]` · **Un WAF es un *Web Application Firewall*.**
- **LAS TRES FALSAS SON LA MISMA EXPRESIÓN CON UNA PALABRA CAMBIADA** —*Wide Area*, *Filter* por
  *Firewall*—: **memoria literal.** **El apoyo es que la «A» es de *application*, no de *area*.**

| Tipo | En qué capa decide | Qué mira |
|---|---|---|
| **De filtrado de paquetes** | **Red y transporte** | **Direcciones y puertos** |
| **Con estado** | **Red y transporte** | **Además, si el paquete pertenece a una conexión establecida** |
| **De aplicación (WAF)** | **Aplicación** | **El contenido de la petición web** ✔ |

- **QUÉ HACE EL DE APLICACIÓN QUE LOS OTROS NO PUEDEN**: **entiende HTTP.** **Un cortafuegos corriente
  ve una petición al puerto 443 y la deja pasar; el de aplicación lee lo que va dentro** y puede
  rechazar una inyección de instrucciones o un guion incrustado en un formulario.

| Ataque | En qué consiste |
|---|---|
| **Inyección de SQL** | **Meter instrucciones de consulta en un campo del formulario** |
| **Guion entre sitios** | **Colar código de navegador que se ejecuta en la sesión de otro usuario** |
| **Falsificación de petición** | **Hacer que el navegador de la víctima envíe una petición legítima sin querer** |
| **Denegación de servicio** | **Agotar los recursos del servicio con peticiones** |

## La red privada virtual

- **PREGUNTA 77, LA MEJOR DEL PUNTO** · `[exam]` · **Un usuario en una red inalámbrica abierta y
  pública, con túnel establecido hacia su empresa, navegando por la intranet: ¿puede espiarlo un
  vecino con un analizador de tráfico?** **NO, tanto con HTTP como con HTTPS, porque el tráfico del
  túnel está cifrado.**
- **LA CLAVE ESTÁ EN EL ORDEN DE LOS CIFRADOS**: **el navegador produce la petición, cifrada o no** →
  **el cliente de red privada virtual la mete entera dentro de su propio túnel cifrado** → **lo que
  sale por la tarjeta inalámbrica es el túnel, no la petición.**
- **POR ESO EL VECINO NO VE NADA**: **capta tráfico cifrado hacia la pasarela de la empresa.** **Ve
  QUE hay tráfico y CUÁNTO, y no ve qué.**

| Opción falsa | Su error |
|---|---|
| **Sólo si es HTTP y no HTTPS** | **Confunde el nivel**: la protección la da el túnel, no el protocolo de dentro |
| **Sí, con los dos protocolos** | **Ignora el túnel por completo** |
| **No, porque el tráfico inalámbrico está cifrado** | **El enunciado dice «abierta»**, y **una red abierta no cifra nada** |

- **LA ÚLTIMA ES LA TRAMPA FINA**: **da la respuesta correcta con el argumento equivocado**, y **eso
  la hace falsa**: si el razonamiento fuera ése, en una red abierta el usuario estaría expuesto.
- **EL AVISO DE OFICIO**: **una red privada virtual protege el transporte, no el destino.** **Si el
  usuario visita un sitio malicioso a través del túnel, el túnel lo lleva igualmente.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 15 | Nivel de seguridad de una red perimetral | c) Menos segura que la interna, más que la externa ✔ |
| 23 | Extensión de X.509 para varios dominios | b) SAN ✔ |
| 36 | Técnica de ejecución en espacio limitado | c) Sandboxing ✔ |
| 39 | Qué es un WAF | d) *Web Application Firewall* ✔ |
| 77 | Si un vecino puede espiar bajo una red privada virtual | d) No, el tráfico del túnel está cifrado ✔ |

**Las cinco oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la 77 es la que más enseña del punto entero.** **Entender el orden de encapsulación contesta ésa y
cualquier variante.** **Y la pareja SAN y SNI es el dato más confundible: conviene fijarlo.**
