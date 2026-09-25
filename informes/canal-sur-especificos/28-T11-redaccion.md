# Puesto 28 · Operador/a de Sonido · Tema 11 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md` (10.754 palabras según
`indice.py`, contando ficha, siglas, índice y trazabilidad; 10 rúbricas `##` en el orden del enunciado
—Líneas y conexiones, XLR, Jack, BNC, Dante/AES67, MADI, AES/EBU, ADAT, SDI, Embebido y
desembebido—, 45 epígrafes `###`, más «Normas técnicas que el tema cita», «Lo que este tema no da» y
«Trazabilidad»).

Escrito por partes, guardando cada una: (1) ficha, siglas, enunciado, qué se puede preguntar y
«Líneas y conexiones»; (2) XLR, Jack y BNC; (3) Dante/AES67; (4) MADI y AES/EBU; (5) ADAT, SDI y
Embebido y desembebido; (6) cierre, índice y siglas.

Material: `informes/canal-sur-especificos/28-investigacion-C-conexiones-ip-rf.md` (§§ 11.1-11.5,
15.1-15.5 y § 10.4 para Crown); RTVE `temas/sonido/11-lineas-y-conexiones.md`,
`temas/sonido/16-audio-sobre-ip.md`, `temas/sonido/17-audio-sobre-protocolos-digitales.md` y
`temas/produccion/13-control-central.md`. Releídos hoy en su volcado todas las citas en inglés (script
de cotejo con espacios normalizados): EBU Tech 3250 (`fuentes/canal-sur/sonido/EBU_Tech3250.txt`),
SMPTE 276M, 272M, ST 299-1, ST 299-2 (`smpte/`), ST 2110-30:2025
(`fuentes/normas-tecnicas/SMPTE_ST-2110-30-2025.txt`), Audinate DC 4.18 (`audinate/dc-latest.txt`),
RME MADI Converter y ADI-648 y DiGiCo TN294 (`fabricantes/`). Crown y Rane RN151, sólo a través de los
informes de investigación C (§ 10.4) y A (§ 2.2). Consultados para no repetir y remitir: temas 2, 4,
7, 8, 9 y 14 del puesto 28 (en curso, no copiados) y el tema 13 de Cámara Operador (cerrado).

El tema no cita ninguna norma legal.

## Aviso al coordinador: el porcentaje de RTVE

El usuario habla de un 75 % de RTVE; la tabla de reuso (`28-args.json`, tema 11) dice **85 %**. Lo
copiado literal de RTVE es mucho menos: unas 700 palabras de 10.750 (en torno al 7 %), más unas
cuantas frases adaptadas. Motivos: los cuatro temas RTVE están escritos en torno a las preguntas de su
examen (tablas de respuestas, opciones falsas, «Ésa es la respuesta oficial»), que se quitan; varias
cifras de RTVE no tenían fuente (MADI, Dante, AES67) o estaban mal (monomodo de «9 micras», fibra de
plástico del ADAT, latencia «el sistema entero se alinea al mayor»), y ahora van con la cita de la
EBU, la SMPTE, Audinate o RME, que ocupa más; y el enunciado de Canal Sur pide cosas que RTVE no
desarrollaba (jack, BNC, ADAT, estructura de la AES/EBU, audio embebido en SDI con sus normas).

## Qué se quitó por propio de RTVE o sin fuente

- Todas las referencias a preguntas y respuestas oficiales del examen RTVE (18, 25, 32, 42, 48, 49, 51,
  57 del sonido 11; 7, 43, 47, 52, 58, 72, 73, 75, 76 del sonido 16; 19, 27, 28, 61, 77 del sonido 17;
  3, 25, 37 del producción 13), las marcas ✔, las tablas de «Los datos que el examen ha preguntado»,
  los recuentos de preguntas y los avisos de estudio.
- La negrita de todo lo copiado de RTVE (allí era énfasis; aquí negrita = literal de fuente).
- Sonido 11: la opción d) «diseño balanceado inferior» (se conserva la idea en una frase propia); las
  tres opciones falsas del *splitter* (reducido a una frase: no es crossover ni fader); la fila «Vídeo
  SDI | 75 ohmios» de la tabla de cables (sin norma leída: se da aparte como oficio); los 100 m de
  categoría 5 como «límite de la norma» y el reparto 90 + 10 (sin fuente: se dan como oficio, sin el
  reparto); la pregunta del Cat6 para Dante.
- Sonido 16: «siete de las nueve son de Dante…»; la tabla NTP/SNTP/PTP con «sub-microsegundo» y
  «milisegundos» (sin fuente; y es tema 15); «el sistema entero se alinea al mayor» (corregido con
  Audinate: latencia efectiva de cada flujo); los 18 Mbps de la pregunta 47 (sin fuente; se conserva la
  explicación de la sobrecarga como oficio); los 96 kHz como máximo de AES67 (sin fuente directa; se
  declara en «no da»); la cita de la presentación de normas de la AES.
- Sonido 17: la tabla de interfaces con «fibra óptica de plástico» para ADAT (sin fuente); la tabla de
  fibras con «9 micras» y «cientos de metros» (sustituida por RME: 8 µm, casi 2 km); las opciones
  falsas de MADI («50 metros», «125 ohmios», «24 bits y 128 kHz»); el LTC/VITC, word clock, AFV, GPI,
  MIDI (no están en el enunciado de este tema; sincronía al tema 15 y 9); «el problema nunca es que los
  formatos no se entiendan», rehecho porque el propio tema documenta incompatibilidades de formato
  (MADI 56/64 y S/MUX frente a alta velocidad).
- Producción 13: la frase «va metido en los espacios que la señal deja libres entre líneas y entre
  cuadros» (sustituida por la ST 299-1: espacio auxiliar horizontal); la tabla de opciones falsas del
  embebedor se reconvierte en «Lo que no hace / Qué aparato lo hace» sin comillas de cita.
- No se ha copiado ninguna afirmación de RTVE que la investigación marcara como errónea.

## Copiado del común

De temas ya cerrados de Canal Sur, sin tocar (comprobado por script, byte a byte con espacios
normalizados):

1. Tema 13 de Cámara Operador (`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`),
   «La familia SMPTE ST 2110», el elemento de lista «ST 2110-30:2025, alcance: **«This standard
   specifies…»** Y el límite: **«Non-PCM digital audio signals…»** La edición vigente de esta parte es
   la de 2025, que revisa la de 2017.» → en el tema 11, epígrafe «AES67 y la ST 2110-30».

(Nada más: los temas del puesto 28 que tratan lo mismo —2, 8, 14— no están cerrados y sólo se remite a
ellos.)

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra; **sólo se ha quitado la negrita** y la marca ✔.
Ninguno cita norma. Los cuatro temas RTVE están marcados «actualizar: no». Comprobado por script:
cada párrafo, fila o elemento de lista, sin `**` ni ✔ y con los espacios normalizados, es subcadena
del RTVE.

De `temas/sonido/11-lineas-y-conexiones.md`:
1. «Qué es una línea…»: el párrafo «Por qué importa: una señal digital tiene flancos… más difíciles de
   encontrar.» (§ 5).
2. «Los cables y sus impedancias»: la cabecera y las tres primeras filas de la tabla (micrófono, AES3
   sobre XLR, AES3 sobre coaxial) (§ 5).
3. «El panel de conexiones»: la tabla de tres diseños con su cabecera; y del párrafo siguiente, las
   frases «permite ESCUCHAR o DERIVAR una señal sin interrumpirla. Se pincha en la fila de arriba…
   sin tirar la emisión.» (§ 3).
4. «El *splitter*»: la frase «el dispositivo que distribuye la señal… es el splitter de audio»; «el
   previo de cada mesa es suyo. Subir la ganancia en la mesa de sala no cambia lo que oye la mesa de
   monitores.»; y el pasaje «con un splitter PASIVO —normalmente… y no un simple paralelo.» (§ 4).
5. «Las matrices de conmutación»: el párrafo «Qué es una matriz: … Es el conmutador central de una
   instalación.»; la cabecera y las filas «Analógica» y «Digital» de la tabla de clases; y las frases
   «una matriz física tiene un límite duro… y no la calidad del sonido.» (§ 6).
6. «El conector y su patillaje»: la tabla de pines con su cabecera y la frase «Y la regla que el
   oficio usa para no olvidarlo: uno, dos, tres: masa, vivo, retorno.» (§ 1).
7. «Por qué el XLR va balanceado»: los puntos 1 y 2 de la lista (§ 1).

De `temas/sonido/16-audio-sobre-ip.md`:
8. «De la matriz a la red»: la tabla matriz/red completa (§ 1); y la frase «una red no garantiza nada
   por sí sola. Hay que darle un reloj común… con el resto del tráfico.»
9. «Por qué UDP…»: la tabla TCP/UDP completa (§ 2); «El razonamiento: en audio en directo… Ese
   instante de sonido ya pasó.»; la fórmula del caudal; «A 48 kHz y 24 bits, un canal son 1,152
   megabits por segundo. Ése es el número que hay que tener.»; los tres pasos de la cuenta (§ 6); y
   «cada paquete lleva sus cabeceras… nunca se puede despreciar.»

De `temas/sonido/17-audio-sobre-protocolos-digitales.md`:
10. «Cómo se protege un enlace MADI»: «El MADI es una conexión PUNTO A PUNTO por un solo cable.
    Sesenta y cuatro canales… segundo camino físico.»; «Una interfaz dedicada y una red no se protegen
    igual. La primera se duplica; la segunda se configura.» (§ 2).
11. «Conversiones y compatibilidad»: la tabla de cuatro conversiones con su cabecera (§ 6).

De `temas/produccion/13-control-central.md`:
12. «Las matrices de conmutación»: la tabla Concepto/Qué es completa (cinco filas) y el párrafo «Y la
    regla de oro del control central… tire una emisión.» (§ 2).
13. «Qué es embeber y desembeber»: la tabla Operación/Qué hace/Aparato; «En la práctica el mismo
    aparato hace las dos cosas»; «La función de un embebedor situado en un control central técnico de
    televisión es extraer o insertar audios en una señal de vídeo.»; «no mueve señales entre sitios:
    mueve audio dentro de una señal. Es una operación de formato, no de encaminamiento.»; y el párrafo
    «Y por qué importa en la práctica… en el canal equivocado.» (§ 4).

**Adaptado de RTVE (sí se verifica):** la entrada del pin 2 («En audio analógico balanceado, …») y la
frase de Rane añadida; «Qué gana el seminormalizado:» sin «y es exactamente lo que el enunciado
describe»; la frase del vocabulario balanceado/normalizado; la entrada «Lo que sí se comparte»; la
fila «Sobre red (IP)» de las clases de matriz (remisión cambiada a este tema y al 15); «La diferencia
de fondo:» sin «que conviene entender antes del tema 16»; la definición de Dante (sin «Ésa es la
respuesta oficial») y la frase del audio y control; los requisitos del conmutador; la frase de UDP y
la ST 2110-10; la frase de los tres flujos para diez canales (reescrita con «Con ella…» y «(cálculo)»); «Es el caudal del audio en crudo»; el párrafo de las soluciones de red que no sirven
para MADI; la tabla de las tres confusiones del embebedor; «En una instalación mixta, lo que más
falla…».

## Nuevo (se verifica entero)

- EBU Tech 3250: nombre del XLR e IEC 60268-12; macho/hembra en salida y entrada; pines 1-2-3 y
  polaridad indiferente; bifase y polaridad (2.3); rotulado DI/DO; alcance y «few hundred metres»; 48
  kHz y CCIR 646; modos de los dos canales (2.2) y estéreo A/B; subtrama de 32 intervalos, tabla de
  intervalos 0-31 (24 y 20 bits, auxiliares); trama; bloque de 192 y preámbulo Z; estado de canal,
  contenido, 192 bits y errata «92-bit»; tasa de tramas = frecuencia de muestreo; tabla eléctrica
  (V.11, 110 Ω cable, emisor y receptor ±20 %, 2-7 Vpp, 200 mV, modo común 7 V, 0,025 UI con «less
  then»); un receptor por línea; ecualización sólo en recepción y cable de más de 100 m; apéndice 2
  (Cat5, 400/800 m, RJ45 4-5 y 3-6, adaptador XLR-RJ45).
- SMPTE 276M: BNC e IEC 169-8 (de 50 Ω en su título), alcance, compatibilidad con vídeo analógico,
  75 Ω, 1 V ± 10 %, 100 mV de ojo, ecualización, cable, anexo A (restricción de 1 V, 110/75 Ω, AES
  3ID).
- SMPTE 272M, ST 299-1, ST 299-2: toda la rúbrica SDI (tabla de normas, canales, bits, grupos, pares
  derivados de AES3, HANC, reloj preferido, opción de 32 a 48 kHz, SMPTE 337, anexo A: SRC y procesado
  PCM, dispositivos que no lo manejan, «multiplexing (embedding) and demultiplexing (receiving)
  devices», renumeración).
- ST 2110-30:2025: conformidad con AES67 y AES67-2023, 48 kHz «shall», 44,1/96 «should», tabla de
  niveles de emisores, nivel A obligatorio, nota SDI y reparto en varios flujos, SGRP.
- Audinate DC 4.18: presentación comercial de Dante; suscripción; nombres «Analog L@my-transmitter»;
  renombrar rompe; flujo; unicast (4 canales, «typically») y multicast (ancho de banda, creación en el
  emisor, por defecto unicast, preferencia de multicast); formatos; tabla de tres mensajes de error;
  latencia (receptor, 1 ms, 150 µs, 1 ms con 100 Mbps, la mayor de las dos por flujo); PTP, elección
  del *leader* con entradas word clock/AES3, PTPv1/v2; redundancia (segunda red, sin comunicación
  primario-secundario, misma velocidad, no redundantes al primario); gigabit preferido; EEE y enlaces
  saturados; DSCP; AES67 y ST 2110-30; flujos multicast AES67/ST 2110-30; no mezclar modos.
- RME MADI Converter: 1989, 28 señales AES/EBU, ±12,5 %, 100 Mbit/s, modo de 64 canales en 2001,
  48 kHz + 1 %, 32 canales a 96 kHz, 125 Mbit/s, equipos antiguos de 56; BNC 75 Ω AES10-1991; 100 m
  coaxial; niveles 400/180 mVpp; FDDI y SC, no ST; fibras 50/62,5/125; vidrio y no POF; multimodo casi
  2 km; monomodo 8 µm; 1.300 nm; separación galvánica.
- RME ADI-648: ADAT 8/4/2 canales, TOSLINK, 10 m, especificación Alesis, S/MUX y S/MUX4, DS, sin
  codificación; 64 canales MADI a 8 salidas ADAT.
- DiGiCo TN294: definición de AES10, revisiones 2003 y 2008 (discrepancia con RME declarada), RG59U,
  0,5 V y 125 MHz, 0,25 V de diferencia de masa, distancia dependiente, 56 no aceptado por terceros,
  S-MUX y Hi-Speed incompatibles y canales equivocados, dos pares de cables a 96 kHz, puertos 1A/1B.
- Crown (vía investigación C § 10.4): patillaje XLR y TRS. Rane RN151 (vía investigación A § 2.2):
  «pin 2 is hot» y malla al cuerpo del jack de 6,35 mm.
- Oficio declarado: tabla de tres familias de línea; qué puede ir por un XLR; el jack TRS usado para
  señales no balanceadas; 75 Ω y BNC del SDI; 100 m y categorías 5e/6 de Ethernet; distribuidor para
  varios receptores AES/EBU; orden de comprobación de una AES/EBU con cortes; alcance práctico del
  ADAT; dónde se embebe y desembebe; mesas y mezcladores con embebedor integrado; supuesto práctico.
- Cálculos: 56 = 28 × 2; tres flujos para diez canales; 3,072 millones de intervalos por segundo;
  24 × 8 = 192; ocho pares en 16 canales.

## Avisos para verificación

- ST 299-1: la cita «linear PCM audio or non-PCM data formatted according to SMPTE 337» está partida en
  el volcado como «non-\nPCM»; el cotejo automático falla por el guion de fin de línea, no por el texto.
- DiGiCo dice que la AES10 se revisó en 2003 y 2008 añadiendo 64 canales y 96 kHz; RME dice que el
  modo de 64 canales se introdujo «officially in 2001». El tema da las dos y no decide.
- Crown y Rane RN151: sin volcado; citas tomadas de los informes de investigación C y A.
- «La IEC 169-8 describe el BNC de 50 Ω»: sale del título de la referencia normativa en la 276M
  («Characteristic Impedance 50 Ohms (Type BNC)»), no de la IEC leída.
- Presentación de FDDI como *fiber distributed data interface*: desarrollo de sigla de oficio; RME sólo
  da «FDDI (ISO/IEC 9413-3)». El verificador puede quitar el desarrollo.
- «Dante es… un protocolo que permite la transmisión de señales de audio y control a través de una red
  Ethernet»: frase de RTVE (respuesta oficial de su examen), sin cita de Audinate con esas palabras; va
  como oficio.
- En la tabla de flujos, «Una copia por destino (oficio)» para el ancho de banda unicast es inferencia
  de la definición punto a punto, no cita.

## Huecos declarados (en el tema, «Lo que este tema no da»)

Texto de AES3, AES10 y AES67 (y por tanto el máximo de muestreo de AES67 y la fecha de los 64 canales
de MADI); capa física del SDI y norma de cableado estructurado; jack de 3,5 mm y norma del jack;
material de la fibra TOSLINK; lo propio de CSRTV (equipamiento, mesas, red, reparto de pistas).

## Lentes

`indice.py`: índice generado (sin fila en `portadas.tsv`; extensión puesta a mano con su cifra,
10.754 → «10.800 palabras aproximadamente»). `refutar_prosa.py`: 10 siglas sin presentar en la
primera pasada (AX, BX, DC, DI, DS, EMI, FAQ, FDDI, SGRP, ST), corregidas en el párrafo de siglas; queda
1 hallazgo que se deja (ST: el script la detecta dentro del propio párrafo de siglas, donde se
presenta).

## Otros ficheros tocados

Ninguno fuera del tema y este informe.

## Preguntas tipo test de comprobación (10)

| # | Rúbrica | Pregunta | Respuesta | ¿La contesta el tema? |
|---|---|---|---|---|
| 1 | Líneas y conexiones | Para tomar una copia de una señal en un panel de conexiones sin cortar el camino normal, el panel debe ser: a) normalizado b) seminormalizado c) no normalizado d) balanceado | b) | Entera: «El panel de conexiones» (tabla de tres diseños; «balanceado» no es un diseño de normalización) |
| 2 | XLR (práctica) | En una línea AES/EBU con XLR, si se cruzan los pines 2 y 3: a) se invierte la polaridad del audio b) la señal no se ve afectada c) se pierde un canal d) el receptor se desincroniza | b) | Entera: «El XLR en audio digital» (nota de la EBU sobre la polaridad de 2 y 3; código bifase insensible a la polaridad) y contraste con el analógico en «Por qué el XLR va balanceado» |
| 3 | Jack | En un jack TRS balanceado de 6,35 mm, el anillo lleva: a) el vivo b) la malla c) el retorno d) la alimentación *phantom* | c) | Entera: «El jack TRS y el TS» (cita de Crown y tabla XLR/TRS) |
| 4 | BNC | Según la SMPTE 276M, la AES/EBU por coaxial usa: a) 110 Ω y 2-7 Vpp b) 75 Ω y 1 V ± 10 % c) 75 Ω y 400 mVpp d) 50 Ω y 1 V | b) | Entera: «La AES/EBU por coaxial» (tabla comparada; BNC de 75 Ω; ecualización en el receptor) |
| 5 | Dante/AES67 (práctica) | Se envían 10 canales por Dante en unicast. Con la capacidad habitual de un flujo unicast, se necesitan: a) 1 flujo b) 2 flujos c) 3 flujos d) 10 flujos | c) | Entera: «Flujos: unicast y multicast» (4 canales «typically»; cálculo 4 + 4 + 2) |
| 6 | Dante/AES67 | Según la SMPTE ST 2110-30:2025, la frecuencia de muestreo que todo emisor y receptor debe admitir es: a) 44,1 kHz b) 48 kHz c) 96 kHz d) 192 kHz | b) | Entera: «AES67 y la ST 2110-30» (48 kHz «shall»; 44,1 y 96 «should»; nivel A) |
| 7 | MADI (práctica) | Una mesa y un grabador conectados por MADI a 96 kHz reciben audio en canales equivocados. La causa más probable es: a) cable de 110 Ω b) modos S/MUX y alta velocidad distintos en cada extremo c) fibra monomodo d) PTP mal configurado | b) | Entera: «Por qué dos equipos MADI pueden no entenderse» (DiGiCo: modos incompatibles y canales equivocados) y «Qué es el MADI» (32 canales a 96 kHz) |
| 8 | AES/EBU | Un bloque de la interfaz AES/EBU está formado por: a) 2 subtramas b) 32 intervalos c) 64 tramas d) 192 tramas | d) | Entera: «La estructura: subtrama, trama y bloque» (subtrama de 32, trama de 2, bloque de 192, preámbulo Z) |
| 9 | ADAT | Por una fibra ADAT a 96 kHz se transmiten: a) 2 canales b) 4 canales c) 8 canales d) 16 canales | b) | Entera: «Qué lleva y por dónde» (8/4/2 canales, TOSLINK, 10 m, S/MUX) |
| 10 | SDI / embebido (práctica) | Un par AES embebido en HD-SDI lleva datos SMPTE 337 (Dolby E). Según la ST 299-1, lo que no debe hacerse es: a) desembeberlo b) llevarlo síncrono a 48 kHz c) convertir su frecuencia de muestreo o cambiar su ganancia d) llevarlo al decodificador | c) | Entera: «Audio no PCM embebido» (SRC y procesado PCM lo corrompen; 48 kHz síncrono) y «Un supuesto práctico», paso 3 |

Las diez, repartidas por las diez rúbricas (SDI y embebido comparten la 10; Dante/AES67 lleva dos), se
contestan enteras con el tema; cuatro son de aplicación práctica (2, 5, 7, 10). Comprobación adicional
de lo que dejan fuera, también en el tema: canales embebidos en SD y en HD a 48 y 96 kHz (16 y 8) y
ampliación a 32 con la ST 299-2; grupos de cuatro y HANC; qué hace un embebedor frente a una matriz;
latencia por defecto de Dante (1 ms), mínima (150 µs) y en 100 Mbps; PTPv1/v2; redundancia primaria y
secundaria en redes separadas; MADI coaxial 100 m, fibra multimodo casi 2 km, SC, 1.300 nm, monomodo
8 µm; 56 frente a 64 canales; 110 Ω, 2-7 Vpp y un receptor por línea; Cat5 a 400/800 m; salida macho y
entrada hembra en AES/EBU; *splitter* pasivo y *phantom*; caudal de 1,152 Mbps por canal. No ha hecho
falta ampliar.
