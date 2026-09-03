# Esquema · Tema 12 del específico de Técnica de Equipos y Sistemas Electrónicos · Comunicaciones y redes

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes · `[plan]` = plantilla
oficial. **Siglas**: el protocolo de internet (**IP**), la interconexión de
sistemas abiertos (**OSI**) y el par de protocolos de internet (**TCP/IP**); el protocolo de datagramas de usuario (**UDP**); las versiones 4 y 6 del protocolo de
internet (**IPv4** e **IPv6**); la alimentación por Ethernet (**PoE**); el Instituto de Ingenieros
Eléctricos y Electrónicos (**IEEE**); el protocolo de inicio de sesión (**SIP**) y la voz sobre
internet (**VoIP**); el conector de red (**RJ 45**) y las categorías de cableado (**CAT6**); el
conector de fibra de suscriptor con pulido físico ultra (**SC UPC**), junto a los tipos **LC**, **ST**
y **FC**, cuyas iniciales este esquema no desarrolla porque no las ha verificado; el teclado, vídeo y
ratón a distancia (**KVM**); la red de área local virtual (**VLAN**); la lista de control de acceso
(**ACL**) y el enlace troncal entre conmutadores (**TRUNK**); y el gigahercio (**GHz**).

**Cabecera.** Enunciado: punto 14 del anexo · **13 preguntas: el segundo banco de la ocupación** · **es
el punto más calculable del volumen.**

<!-- indice -->

## Índice

- [Los dos modelos](#los-dos-modelos)
- [Direccionamiento y máscaras](#direccionamiento-y-máscaras)
- [Los protocolos](#los-protocolos)
- [Cableado y conectores](#cableado-y-conectores)
- [Equipos de red y diagnóstico](#equipos-de-red-y-diagnóstico)
- [Lo que el enunciado nombra y no ha caído](#lo-que-el-enunciado-nombra-y-no-ha-caído)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos modelos

| OSI (siete capas) | TCP/IP (cuatro capas) |
|---|---|
| **Aplicación, presentación, sesión** | **Aplicación** |
| **Transporte** | **Transporte** |
| **Red** | **Internet** |
| **Enlace, física** | **Acceso a la red** |

- **PREGUNTA 85** · `[of]` · **El modelo TCP/IP tiene 4 capas.**
- **LAS DOS CIFRAS HAY QUE APRENDERLAS JUNTAS Y CON NOMBRE**: **siete el OSI, cuatro el TCP/IP.**
  **La opción «7» es la trampa.**
- **EL USO PRÁCTICO DEL MODELO**: **situar la avería en su capa.** **Cable roto, capa física;
  dirección mal puesta, capa de red; puerto bloqueado, transporte; códec incompatible, aplicación.**

## Direccionamiento y máscaras

- **PREGUNTA 35** · `[of]` · **Una dirección IPv6 tiene 128 bits.** **Cuatro veces las 32 de la
  versión 4.**
- **PREGUNTA 11** · `[of]` · **Con 192.168.30.150 y máscara 255.255.255.128, comparte subred
  192.168.30.250/25.**
- **EL MÉTODO EN CUATRO PASOS**: **1) contar los unos de la máscara: 25 · 2) con `/25` el cuarto octeto
  se parte: 0-127 y 128-255 · 3) el 150 cae en la alta · 4) buscar la opción que caiga ahí con el mismo
  tercer octeto.**
- **PREGUNTA 27 del segundo llamamiento** · `[of]` · **Para 500 equipos, la máscara ajustada es
  255.255.254.0.**
- **LA CUENTA AL REVÉS**: **la potencia de dos por encima de 500 es 512 = 2⁹ · 32 − 9 = 23 · `/23` es
  255.255.254.0 · da 510 asignables.**

## Los protocolos

| | **TCP** | **UDP** |
|---|---|---|
| **Entrega garantizada** | **Sí** | **No** |
| **Orden garantizado** | **Sí** | **No** |
| **Control de congestión** | **Sí** | **No** |
| **Coste** | **Retardo variable** | **Retardo bajo y constante** |

- **PREGUNTA 68** · `[of]` · **El UDP se usa al priorizar la velocidad sin necesidad de retransmitir.**
- **POR QUÉ EN TELEVISIÓN**: **un paquete de vídeo que llega tarde ya no sirve**, porque su cuadro ya
  se emitió.
- **PREGUNTA 83** · `[of]` · **Es falso que el SIP sirva *únicamente* para sesiones de voz.** **El SIP
  señaliza sesiones multimedia en general.**
- **EL AVISO DE MÉTODO**: **en las preguntas negativas, desconfiar de los absolutos.** **«Únicamente»,
  «siempre», «nunca» y «todos» son las palabras que vuelven falsa una frase que sin ellas sería
  cierta.**
- **PREGUNTA 69** · `[of]` · **La norma 802.11b emite en 2,4 GHz.** **La b y la g son las viejas de
  2,4; la a es la vieja de 5; la doble banda llega con la n.**

## Cableado y conectores

- **PREGUNTA 30 del segundo llamamiento** · `[of]` · **Los cables CAT6 llevan cuatro pares trenzados.**
  **La categoría describe hasta qué frecuencia responde el par, no el número de hilos, que siempre es
  ocho.**
- **PREGUNTA 3 del segundo llamamiento** · `[of]` · **El T568B es blanco-naranja, naranja, blanco-verde,
  azul, blanco-azul, verde, blanco-marrón, marrón.**
- **LA REGLA QUE LO HACE MEMORIZABLE**: **el orden de los pares es naranja, verde, azul, marrón**, con
  **el par azul metido en los contactos 4 y 5** —los de la telefonía— **y el verde partido entre el 3 y
  el 6.**
- **PREGUNTA 2 del segundo llamamiento** · `[plan]` · **El conector para paneles SC UPC hembra es el
  C 2 de la figura.** **Este esquema no ha visto la figura.** **La regla de la familia**: **el SC es
  rectangular y entra empujando; el LC es la mitad de ancho; el ST es redondo y gira; el FC se
  rosca.** **Y el pulido tiene que coincidir: el azul es físico ultra y el verde es en ángulo.**

## Equipos de red y diagnóstico

- **PREGUNTA 10** · `[of]` · **Un conmutador PoE da alimentación por el cable Ethernet.** **La cuenta al
  instalar: la suma de lo que piden los aparatos no puede pasar el presupuesto de potencia del
  conmutador.**
- **PREGUNTA 14 del segundo llamamiento** · `[of]` · **Para localizar dónde se pierde la conexión se usa
  `tracert`.**

| Comando | Qué hace |
|---|---|
| **`ipconfig`** | **Enseña la configuración del propio equipo** |
| **`ping`** | **Dice si el destino contesta, sí o no** |
| **`tracert`** | **Enumera los saltos y dice en cuál se pierde** ✔ |
| **`netstat`** | **Enumera las conexiones abiertas** |

- **EL VERBO DEL ENUNCIADO DECIDE**: **«localizar dónde».** **El `ping` contesta si llega; no dice
  dónde se cortó.**
- **PREGUNTA 94** · `[of]` · **Un sniffer captura, analiza y monitoriza los paquetes de una red.** **Es
  la herramienta de última instancia: cuando el camino está bien y el equipo no funciona, hay que mirar
  los paquetes.**

## Lo que el enunciado nombra y no ha caído

| Asunto | Qué es, en una línea |
|---|---|
| **VLAN** | **Partir un conmutador en varias redes lógicas que no se ven** |
| **TRUNK** | **Enlace que transporta varias VLAN etiquetadas** |
| **ACL** | **Lista de qué tráfico pasa y cuál no** |
| **KVM sobre IP** | **Llevar teclado, vídeo y ratón por la red** |

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 10 | Característica especial de un conmutador PoE | b) Da alimentación por el cable ✔ |
| 11 | Equipo de la misma subred que 192.168.30.150/25 | d) 192.168.30.250/25 ✔ |
| 35 | Bits de una dirección IPv6 | c) 128 ✔ |
| 68 | Cuándo se usa el protocolo UDP | a) Al priorizar velocidad ✔ |
| 69 | Banda de la norma 802.11b | a) 2,4 GHz ✔ |
| 83 | Afirmación falsa sobre el SIP | b) Que sea únicamente de voz ✔ |
| 85 | Capas del modelo TCP/IP | d) 4 ✔ |
| 94 | Qué es un sniffer | b) Herramienta de captura y análisis ✔ |
| 2 (2.º llam.) | Conector para paneles SC UPC hembra | b) C 2 ✔ **·** figura |
| 3 (2.º llam.) | Código de color T568B | a) Blanco-naranja, naranja, blanco-verde… ✔ |
| 14 (2.º llam.) | Comando para localizar el fallo de conectividad | c) `tracert` ✔ |
| 27 (2.º llam.) | Máscara ajustada para 500 equipos | a) 255.255.254.0 ✔ |
| 30 (2.º llam.) | Qué son los cables CAT6 | b) Cuatro pares trenzados ✔ |

**Las trece oficiales son correctas** · **una descansa en la plantilla, y es la que lleva figura.** ·
**Aviso de estudio**: **dos preguntas son aritmética binaria y se ganan siempre con el método del
segundo epígrafe.** **Es el punto donde el estudio rinde de forma más previsible.**
