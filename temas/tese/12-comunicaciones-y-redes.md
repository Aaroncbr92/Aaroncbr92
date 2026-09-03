# Tema 12 del específico de Técnica de Equipos y Sistemas Electrónicos · Comunicaciones y redes

Las siglas de este tema, presentadas de entrada: la interconexión de sistemas abiertos (**OSI**, *open
systems interconnection*); el protocolo de control de transmisión y el protocolo de internet
(**TCP/IP**); el protocolo de internet (**IP**) y su protocolo
de datagramas de usuario (**UDP**), los dos ya presentados en el tema 9; la versión
6 del protocolo de internet (**IPv6**) y la versión 4 (**IPv4**); la alimentación a través de Ethernet
(**PoE**, *power over Ethernet*); el Instituto de Ingenieros Eléctricos y Electrónicos (**IEEE**); el
protocolo de inicio de sesión (**SIP**, *session initiation protocol*); la voz sobre el protocolo de
internet (**VoIP**); el conector de red de ocho contactos (**RJ 45**); la categoría de un cableado de
par trenzado (**CAT**, y de ahí **CAT6**); el conector de suscriptor de fibra óptica (**SC**) con
pulido físico ultra (**UPC**, *ultra physical contact*), junto a los otros tres tipos de conector de
fibra que este tema nombra —**LC**, **ST** y **FC**—, cuyas iniciales el temario no desarrolla porque
no ha verificado su forma larga; el teclado, vídeo y ratón a distancia
(**KVM**); la red de área local virtual (**VLAN**); la lista de control de acceso (**ACL**); el
gigahercio (**GHz**); y el ordenador personal (**PC**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 14):
> «COMUNICACIONES Y REDES: Terminología y conceptos. Los modelos de referencia OSI y TCP/IP.
> Protocolos TCP/IP. Redes de control IP en equipamiento broadcast. KVM sobre IP. Configuración de
> Switches y Routers (VLAN, TRUNK, políticas de enrutamiento, ACLS, etc.). Internet. Servicios y
> protocolos. Gestión de redes.»

**Trece preguntas: el segundo banco de la ocupación**, sólo por detrás del inventario del tema 10.

**Su reparto**: **tres preguntas son de direccionamiento y máscaras**, **cuatro de protocolos**,
**tres de cableado y conectores**, **dos de diagnóstico y herramientas** y **una de radio.**

**Y el rasgo que define este punto**: **es el más calculable de la ocupación.** **Dos de sus trece
preguntas se resuelven con aritmética binaria y no admiten discusión**, lo que **las convierte en las
más seguras del examen para quien sepa hacerlas y en las más perdidas para quien no.**

**Una de las trece depende de una figura** —la 2 del segundo cuadernillo, que enseña cuatro
conectores—, y **este tema no la describe**: da la regla de su familia y declara que la respuesta
descansa en la plantilla.

<!-- indice -->

## Índice

- [1. Los dos modelos de referencia](#1-los-dos-modelos-de-referencia)
- [2. El direccionamiento y las máscaras](#2-el-direccionamiento-y-las-máscaras)
- [3. Los protocolos](#3-los-protocolos)
- [4. El cableado y los conectores](#4-el-cableado-y-los-conectores)
- [5. Los equipos de red y el diagnóstico](#5-los-equipos-de-red-y-el-diagnóstico)
- [6. Lo que el enunciado nombra y el examen no ha preguntado](#6-lo-que-el-enunciado-nombra-y-el-examen-no-ha-preguntado)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Los dos modelos de referencia

**La pregunta 85**: **el modelo TCP/IP tiene cuatro capas.** Ésa es la respuesta oficial.

---

**Los dos modelos, uno frente a otro, que es la única manera de que las cifras no se crucen:**

| Modelo OSI (siete capas) | Modelo TCP/IP (cuatro capas) | Qué resuelve |
|---|---|---|
| **Aplicación, presentación, sesión** | **Aplicación** | **Qué significan los datos para el programa** |
| **Transporte** | **Transporte** | **Que los datos lleguen, o que lleguen rápido** |
| **Red** | **Internet** | **Cómo se encamina un paquete de una red a otra** |
| **Enlace, física** | **Acceso a la red** | **Cómo viajan los bits por el cable o por el aire** |

**La cifra que la pregunta persigue es cuatro**, y **la opción b, siete, es la trampa evidente:**
**quien memoriza «siete capas» sin distinguir el modelo cae.** **Las dos cifras hay que aprenderlas
juntas y con nombre propio: siete el OSI, cuatro el TCP/IP.**

**Por qué existen los dos**: **el OSI es un modelo de referencia académico, pensado para describir
cualquier red**; **el TCP/IP es el modelo de la red que realmente se construyó.** **El primero se usa
para explicar y para situar averías; el segundo para trabajar.**

**Y el uso práctico del modelo en esta ocupación**: **situar la avería en su capa.** **Un cable roto
es capa física; una dirección mal puesta es capa de red; un cortafuegos que bloquea un puerto es capa
de transporte; un códec incompatible es capa de aplicación.** **Preguntarse en qué capa está el fallo
antes de tocar nada es lo que ahorra las horas.**

## 2. El direccionamiento y las máscaras

**Tres preguntas, y las tres se resuelven contando bits.**

**La pregunta 35**: **una dirección IPv6 tiene 128 bits.** Ésa es la respuesta oficial.

---

**Las dos versiones, con la cifra que las separa:**

| Versión | Bits | Cómo se escribe | Cuántas direcciones |
|---|---|---|---|
| **IPv4** | **32** | **Cuatro números decimales de 0 a 255 separados por puntos** | **Unos cuatro mil millones** |
| **IPv6** | **128** | **Ocho grupos de cuatro cifras hexadecimales separados por dos puntos** | **Un número de treinta y nueve cifras** |

**Las tres opciones falsas son 32, 64 y 256**: **la primera es la longitud de la versión 4, la segunda
es la mitad de la respuesta —la parte de red de una dirección de la versión 6— y la tercera es el
doble.** **La cifra que hay que retener es 128, y el atajo es que son cuatro veces las 32 de la
versión anterior.**

**La pregunta 11 es la primera de cálculo**: **un equipo con dirección 192.168.30.150 y máscara
255.255.255.128 comparte subred con el equipo cuya dirección es 192.168.30.250/25.** Ésa es la
respuesta oficial.

---

**Cómo se hace, paso a paso, porque este método resuelve también la siguiente:**

1. **La máscara 255.255.255.128 tiene veinticinco unos**: los tres primeros octetos completos son
   veinticuatro, y el 128 del cuarto aporta uno más. **De ahí la notación `/25` que usan las
   opciones.**
2. **Con `/25`, el cuarto octeto se parte por la mitad**: **una subred va de 0 a 127 y la otra de 128
   a 255.**
3. **El 150 del equipo dado es mayor que 127**, luego **está en la subred alta: de 192.168.30.128 a
   192.168.30.255.**
4. **Se mira cuál de las cuatro opciones cae ahí dentro con el mismo tercer octeto.**

**Y las cuatro se clasifican solas:**

| Opción | Por qué sirve o no |
|---|---|
| **a) 192.168.31.150/25** | **Tercer octeto distinto: es otra red entera** |
| **b) 192.168.30.0/25** | **Cae en la subred baja, de 0 a 127** |
| **c) 192.168.30.124/25** | **124 es menor que 128: subred baja también** |
| **d) 192.168.30.250/25** | **250 está entre 128 y 255: la misma subred** ✔ |

**El aviso**: **la opción b tiene además el defecto de ser la propia dirección de red de la subred
baja**, que no se asigna a ningún equipo. **Dos motivos para descartarla, y basta con el primero.**

**La pregunta 27 es la segunda de cálculo, y va al revés**: **para una red de 500 equipos, la máscara
que mejor se ajusta sin dejar demasiadas direcciones libres es 255.255.254.0.** Ésa es la respuesta
oficial.

---

**La cuenta**: **con *b* bits de equipo hay 2^b direcciones, menos dos —la de red y la de difusión—
que no se asignan.** **Se busca la potencia de dos inmediatamente superior a 500**, que es **512**, y
**512 son nueve bits.** **Treinta y dos menos nueve son veintitrés**, luego **la máscara es `/23`**,
y **`/23` en decimal es 255.255.254.0**: veintitrés unos son los dos primeros octetos completos más
siete del tercero, y siete unos seguidos de un cero son 254.

**Las cuatro opciones, con lo que da cada una:**

| Máscara | Prefijo | Direcciones asignables | Veredicto |
|---|---|---|---|
| **255.255.254.0** | **/23** | **510** | **La ajustada** ✔ |
| **255.255.248.0** | **/21** | **2.046** | **Cuatro veces más de lo necesario** |
| **255.255.255.0** | **/24** | **254** | **No caben los 500** |
| **255.255.255.128** | **/25** | **126** | **Mucho menos aún** |

**Y el detalle que a veces despista**: **510 es menor que 512 por los dos que no se asignan**, y **aun
así basta para 500 equipos.** **Si la red hubiera pedido 511, habría que subir a `/22`.**

## 3. Los protocolos

**La pregunta 68 va de transporte**: **el protocolo UDP se usa cuando se prioriza la velocidad y no se
necesita retransmitir datos.** Ésa es la respuesta oficial.

---

**Los dos protocolos de transporte, frente a frente:**

| | **TCP** | **UDP** |
|---|---|---|
| **Establece conexión previa** | **Sí** | **No** |
| **Garantiza la entrega** | **Sí: retransmite lo perdido** | **No** |
| **Garantiza el orden** | **Sí: reordena en destino** | **No** |
| **Controla la congestión** | **Sí** | **No** |
| **Coste** | **Retardo variable y más carga** | **Retardo bajo y constante** |
| **Para qué se usa aquí** | **Ficheros, correo, páginas, control** | **Vídeo y audio en directo** |

**Y las tres opciones falsas describen las tres virtudes del TCP**: entrega garantizada, orden y
control de congestión. **La pregunta se contesta sabiendo que el UDP es el que renuncia a todo eso a
cambio de ir deprisa.**

**Por qué esto importa en una instalación de televisión**: **la señal en directo no se puede
retransmitir.** **Un paquete de vídeo que llega tarde ya no sirve para nada**, porque el cuadro al que
pertenecía ya se emitió. **Por eso el vídeo sobre red del tema 9 va sobre UDP y se protege con
redundancia y corrección de errores en vez de con retransmisión.**

**La pregunta 83 es negativa y va de señalización**: **la afirmación falsa sobre el protocolo de
inicio de sesión SIP es que sea un protocolo de la capa de aplicación que se utiliza para establecer,
modificar y terminar sesiones únicamente de voz sobre una red IP.** Ésa es la respuesta oficial.

---

**Y la palabra que la vuelve falsa es «únicamente».** **El SIP es en efecto un protocolo de capa de
aplicación y en efecto establece, modifica y termina sesiones**: **casi toda la frase es cierta.**
**Lo que la hace falsa es la restricción a la voz**, porque **el SIP señaliza sesiones multimedia en
general**: voz, vídeo, mensajería y datos. **La opción c dice exactamente eso, y es verdadera.**

**El aviso de método que esta pregunta enseña**: **en las preguntas negativas conviene desconfiar de
los absolutos.** **«Únicamente», «siempre», «nunca» y «todos» son las palabras que un enunciado usa
para volver falsa una frase que sin ellas sería cierta.**

**Y lo que conviene tener claro del SIP para no dudar**: **señaliza, no transporta.** **Establece la
llamada; los paquetes de voz viajan después por otro protocolo, sobre UDP.**

**La pregunta 69 va de radio**: **la norma 802.11b de la familia IEEE 802.11 emite en la banda de
2,4 GHz.** Ésa es la respuesta oficial.

---

**Las variantes que el examen puede pedir, con su banda:**

| Norma | Banda |
|---|---|
| **802.11b** | **2,4 GHz** |
| **802.11g** | **2,4 GHz** |
| **802.11a** | **5 GHz** |
| **802.11n** | **2,4 GHz y 5 GHz** |
| **802.11ac** | **5 GHz** |

**La opción c, «2,4 y 5», es la trampa**: **describe la variante n, no la b.** **La letra decide la
banda**, y la regla de memoria es que **la b y la g son las viejas de 2,4 y la a es la vieja de 5**;
**la doble banda llega con la n.**

## 4. El cableado y los conectores

**La pregunta 30**: **los cables catalogados como CAT6 son cables con cuatro pares trenzados.** Ésa es
la respuesta oficial.

---

**Y la categoría no describe el conector ni el color**: **describe hasta qué frecuencia responde el
par trenzado**, y con ello **qué velocidad admite y a qué distancia.**

| Categoría | Para qué alcanza |
|---|---|
| **CAT5e** | **Gigabit a cien metros** |
| **CAT6** | **Diez gigabit a distancias cortas; gigabit sobrado a cien metros** |
| **CAT6a** | **Diez gigabit a cien metros** |

**Lo que no cambia entre categorías es la cuenta de hilos**: **cuatro pares, ocho hilos, un conector
de ocho contactos.** **Las tres opciones falsas describen otros tres cables** —un coaxial, un doble
paralelo y una fibra multimodo—, **y ninguno de los tres se conecta a un RJ 45.**

**La pregunta 3 del segundo cuadernillo pide el orden de colores**: **según el estándar T568B, el
código de color en un conector RJ 45 es blanco-naranja, naranja, blanco-verde, azul, blanco-azul,
verde, blanco-marrón, marrón.** Ésa es la respuesta oficial.

---

**Es una pregunta de memoria pura**, y **la regla que la hace memorizable es que el orden de los
pares es naranja, verde, azul, marrón**, con **el par azul metido en medio del verde:**

| Contacto | Color |
|---|---|
| **1** | **Blanco-naranja** |
| **2** | **Naranja** |
| **3** | **Blanco-verde** |
| **4** | **Azul** |
| **5** | **Blanco-azul** |
| **6** | **Verde** |
| **7** | **Blanco-marrón** |
| **8** | **Marrón** |

**El motivo de esa colocación tan rara del azul**: **los contactos 4 y 5 son los que la telefonía
usaba**, y **el estándar los dejó juntos para que un mismo cable sirviera para las dos cosas.** **El
verde queda partido entre el 3 y el 6, que es lo que hay que recordar.**

**Y el otro estándar**: **el T568A intercambia el par naranja con el verde y deja el resto igual.**
**Un latiguillo con un extremo en cada estándar es un cable cruzado**, que era lo que antes se usaba
para unir dos equipos del mismo tipo.

**La opción a de la pregunta es la única con ese orden.** **La b empieza por azul, la c cruza el verde
con el naranja en los contactos 2 y 6 y la d saca el par marrón a los contactos 3 y 4.**

**La pregunta 2 del segundo cuadernillo enseña una figura con cuatro conectores** y pide cuál se usa
con paneles de conectores SC UPC hembra. **La plantilla da el segundo, el rotulado C 2.** **Este
temario no ha visto la figura y no la describe.** **La regla de la familia, que es lo que sí se puede
llevar aprendido:**

| Qué mirar | Qué dice |
|---|---|
| **El cuerpo del conector** | **El SC es rectangular y entra empujando; el LC es la mitad de ancho; el ST es redondo y entra girando; el FC es redondo y se rosca** |
| **El color** | **El azul es pulido físico ultra; el verde es pulido en ángulo; el beis suele ser multimodo** |
| **Con qué casa** | **Un conector sólo entra en un panel de su mismo tipo, y sólo empalma bien con su mismo pulido** |

**Y la regla que resuelve la familia entera**: **el pulido tiene que coincidir.** **Un conector de
pulido en ángulo contra uno de pulido físico ultra hace contacto malo y reflexión alta**, aunque el
cuerpo encaje. **Por eso los colores están normalizados: para que se vea a un metro si dos conectores
casan.** **Aun así, la identificación del conector concreto de la fotografía descansa en la
plantilla**, y el temario lo declara.

## 5. Los equipos de red y el diagnóstico

**La pregunta 10**: **la característica especial de un conmutador PoE es que proporciona energía
eléctrica a los dispositivos a través del cable Ethernet.** Ésa es la respuesta oficial.

---

**Y lo que hay que entender es que van por el mismo cable las dos cosas**: **los datos y la
alimentación.** **Una cámara de red, un punto de acceso o un teléfono de sobremesa se cuelgan de un
solo cable y no necesitan enchufe**, lo que **quita una toma de corriente de cada sitio donde hay un
aparato pequeño.** **En una instalación de televisión eso vale sobre todo para los intercomunicadores,
los relojes y las cámaras de vigilancia de plató.**

**La cuenta que hay que hacer al instalar**: **un conmutador PoE tiene un presupuesto total de
potencia**, y **la suma de lo que piden los aparatos no puede pasarlo.** **Un conmutador con muchos
puertos PoE no necesariamente alimenta a todos a la vez a plena potencia.**

**Las tres opciones falsas nombran cosas que un conmutador no hace por ser PoE**: **no conecta por
coaxial, no da acceso inalámbrico —eso lo hace el punto de acceso que él alimenta— y no acelera la
red.**

**La pregunta 14 del segundo cuadernillo es de diagnóstico**: **para localizar dónde se pierde la
conexión con un equipo situado en otra red, enlazada por encaminadores, el comando que se utiliza es
`tracert`.** Ésa es la respuesta oficial.

---

**Las cuatro herramientas de la opción, y para qué sirve cada una:**

| Comando | Qué hace | Cuándo se usa |
|---|---|---|
| **`ipconfig`** | **Enseña la configuración de red del propio equipo** | **Para saber qué dirección y qué puerta de enlace tengo yo** |
| **`ping`** | **Pregunta si el destino contesta** | **Para saber si hay conexión, sí o no** |
| **`tracert`** | **Enumera los saltos del camino hasta el destino** | **Para saber en qué salto se pierde** ✔ |
| **`netstat`** | **Enumera las conexiones abiertas del propio equipo** | **Para ver qué está hablando con qué** |

**Y lo que decide la respuesta es el verbo del enunciado: «localizar dónde».** **El `ping` contesta
si llega o no llega; no dice dónde se cortó.** **El `tracert` va preguntando por el camino, salto a
salto, y el último que contesta es el punto donde termina lo que funciona**: **el fallo está en el
salto siguiente.**

**La pregunta 94**: **un sniffer, en el ámbito de las redes, es una herramienta que se utiliza para
capturar, analizar y monitorizar los paquetes de datos que circulan a través de una red.** Ésa es la
respuesta oficial.

---

**Es la herramienta de la última instancia del diagnóstico**: **cuando el `tracert` dice que el camino
está bien y el equipo sigue sin funcionar, hay que mirar los paquetes.** **Un analizador de tráfico
enseña qué se está mandando de verdad, y muy a menudo la respuesta es «nada»**, que es un dato.

**En una instalación de televisión sobre red tiene un uso muy concreto**: **comprobar que los flujos
del tema 9 llegan al conmutador, que el envío a varios destinos está bien suscrito y que el reloj de
precisión anuncia.** **Las tres opciones falsas nombran un cortafuegos, un sistema de autenticación y
un protocolo de cifrado**: **tres cosas de seguridad de red que no capturan tráfico para
analizarlo.**

## 6. Lo que el enunciado nombra y el examen no ha preguntado

**El enunciado de este punto es largo y el examen ha entrado por una parte de él.** **Cuatro asuntos
figuran en el anexo y no han caído**, y **conviene llevarlos vistos:**

| Asunto del enunciado | Qué es, en una línea |
|---|---|
| **VLAN** | **Partir un conmutador físico en varias redes lógicas que no se ven entre sí** |
| **TRUNK** | **Un enlace entre conmutadores que transporta a la vez el tráfico de varias VLAN, etiquetado** |
| **ACL** | **Una lista que dice qué tráfico se deja pasar y cuál no, por dirección y puerto** |
| **KVM sobre IP** | **Llevar el teclado, el vídeo y el ratón de un ordenador por la red, para manejarlo desde otro sitio** |

**Por qué las VLAN importan en una instalación de televisión**: **es la forma de que el tráfico de
vídeo del tema 9, el de control y el de ofimática compartan la misma electrónica sin estorbarse.**
**El vídeo en tiempo real y una descarga de ficheros en la misma red plana se pelean por el ancho de
banda**, y **la VLAN, con su política de prioridad, es lo que evita esa pelea.**

**Y por qué el KVM sobre IP importa**: **permite sacar los ordenadores de la sala de realización y
dejarlos en el centro de proceso de datos**, quedando en el puesto sólo el teclado, el monitor y el
ratón. **Menos calor y menos ruido en la sala, y el mantenimiento se hace sin entrar en el plató.**

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 10 | Característica especial de un conmutador PoE | b) Da alimentación por el cable Ethernet ✔ |
| 11 | Equipo de la misma subred que 192.168.30.150/25 | d) 192.168.30.250/25 ✔ |
| 35 | Bits de una dirección IPv6 | c) 128 ✔ |
| 68 | Cuándo se usa el protocolo UDP | a) Al priorizar velocidad sin retransmisión ✔ |
| 69 | Banda de la norma 802.11b | a) 2,4 GHz ✔ |
| 83 | Afirmación falsa sobre el SIP | b) Que sea únicamente de voz ✔ |
| 85 | Capas del modelo TCP/IP | d) 4 ✔ |
| 94 | Qué es un sniffer | b) Herramienta de captura y análisis de paquetes ✔ |
| 2 (2.º llam.) | Conector para paneles SC UPC hembra | b) C 2 ✔ (figura) |
| 3 (2.º llam.) | Código de color T568B en un RJ 45 | a) Blanco-naranja, naranja, blanco-verde, azul… ✔ |
| 14 (2.º llam.) | Comando para localizar dónde falla la conectividad | c) `tracert` ✔ |
| 27 (2.º llam.) | Máscara ajustada para 500 equipos | a) 255.255.254.0 ✔ |
| 30 (2.º llam.) | Qué son los cables CAT6 | b) Cables con cuatro pares trenzados ✔ |

**Las trece respuestas oficiales son correctas.** **Una descansa en la plantilla**, y es la que lleva
figura.

**El aviso de estudio**: **dos preguntas son aritmética binaria** —la 11 y la 27— **y se ganan
siempre si se domina el método del epígrafe 2**; **dos son memoria pura** —el orden de colores y la
banda de la 802.11b—; **y las nueve restantes se contestan sabiendo para qué sirve cada cosa.**
**Es el punto de la ocupación donde el estudio rinde de forma más previsible.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **eso obliga a ser especialmente explícito**,
porque **casi todo lo que afirma tiene detrás una norma que no se ha leído.**

**Siete declaraciones expresas:**

1. **La familia de normas IEEE 802.11 no se ha consultado.** **Las bandas del cuadro del epígrafe 3
   —2,4 GHz para la b y la g, 5 GHz para la a y la ac, ambas para la n— son de uso universal y
   coinciden con la respuesta oficial de la pregunta 69**, y **el temario no las atribuye a ningún
   apartado de esas normas.**
2. **El estándar T568B no se ha consultado.** **El orden de colores del epígrafe 4 es el que da la
   respuesta oficial de la pregunta 3, reproducido de ella**, y **la explicación de por qué el par
   azul ocupa los contactos 4 y 5 es oficio, no cita.**
3. **Las categorías de cableado y sus alcances del epígrafe 4 son órdenes de magnitud del uso
   corriente.** **La norma de cableado estructurado no se ha consultado**, y **ninguna pregunta
   depende de esas cifras**: la 30 pregunta cuántos pares tiene el cable, no hasta qué velocidad
   llega.
4. **Los modelos OSI y TCP/IP del epígrafe 1 se presentan con el número y el nombre de sus capas,
   que son de conocimiento común.** **Ni la norma que define el OSI ni los documentos que definen el
   TCP/IP se han consultado.** **La cifra que la pregunta 85 pide —cuatro— coincide con la respuesta
   oficial.**
5. **Los cálculos de máscara del epígrafe 2 no se toman de ninguna fuente: se hacen.** **El método
   está escrito paso a paso para que el opositor lo repita**, y **su resultado coincide con las dos
   respuestas oficiales.**
6. **El comportamiento del SIP, del UDP y del TCP se describe por su función, no por su
   especificación.** **Los documentos que los definen no se han consultado**, y **lo que las
   preguntas 68 y 83 miden es precisamente para qué sirve cada uno.**
7. **La pregunta 2 del segundo cuadernillo depende de una figura que este temario no ha visto**, y
   **así se declara en el epígrafe 4 y en el cuadro del epígrafe 7.** **La correspondencia entre
   colores y tipos de pulido de fibra que allí se da es uso corriente del sector**, no cita de norma.

**El resto del tema va como oficio y así se declara**: la tabla de correspondencia entre capas, la
regla de situar la avería en su capa, la clasificación de las opciones falsas de cada pregunta, el
presupuesto de potencia de un conmutador PoE, la comparación entre las cuatro herramientas de
diagnóstico, el uso del analizador de tráfico en una instalación de vídeo sobre red y las cuatro
definiciones del epígrafe 6. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
