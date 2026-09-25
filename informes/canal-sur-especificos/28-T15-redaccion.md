# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema que se escribe:
`temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.

Estado: redacción terminada (se guardó por partes; abajo, cada parte).
- Parte 1 guardada: ficha, siglas, enunciado, qué se puede preguntar.
- Parte 2 guardada: rúbrica «Audio sobre IP» (red frente a matriz, UDP, Dante, AES67, ST 2110-30).
- Parte 3 guardada: rúbrica «Redes» (unicast/multicast, conmutador, tamaño de paquete, ancho de banda).
- Parte 4 guardada: rúbricas «Sincronía» y «Latencia».
- Parte 5 guardada: rúbricas «PTP» y «Redundancia».
- Parte 6 guardada: normas técnicas citadas, «Lo que este tema no da», «Trazabilidad»; índice
  generado con `indice.py`; extensión medida (8.235 palabras con portada e índice; en la ficha,
  «8.200 aproximadamente»).

Tema cerrado en redacción. Lentes pasadas: `indice.py` (índice regenerado) y `refutar_prosa.py`
(sin relleno, sin frases repetidas, sin negritas rotas; quedan 3 avisos de siglas que son falsos
positivos: IP y PTP en el título, que es el enunciado literal y se presentan justo debajo, y
`TRUE`, valor de un parámetro dentro de una cita). No hay norma legal: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`.

## Aviso al coordinador: el reuso de RTVE es bastante menor que el 95 %

El `.tsv` de reuso da el 95 % (la persona usuaria habla de un 75 %). Medido sobre el tema escrito,
el texto de RTVE copiado literal son unas 600 palabras de 8.200 (≈ 7 %), y el adaptado, otras
400. Motivos:

1. RTVE (sonido/16) está construido sobre las nueve preguntas de su cuadernillo («Ésa es la
   respuesta oficial…», opciones falsas, tabla de preguntas): todo eso es propio de RTVE y se quita.
2. El enunciado de Canal Sur pide «redes, sincronía, … redundancia», que RTVE no tiene: la
   redundancia (Dante primaria/secundaria, ST 2022-7), el perfil PTP ST 2059-2, la ST 2110-10/-30
   y la sincronía entre flujos son nuevos, con la fuente de la investigación C.
3. Varias cifras de RTVE no tienen fuente leída y se quitan (abajo).

## Copiado del común

Nada. Ningún tema de `temas/canal-sur-comun/` trata esta materia. El tema 11 de este puesto
(Dante/AES67 como conexión) está en redacción, no cerrado: no se ha copiado de él; los dos temas
citan los mismos pasajes de Audinate, cada uno desde su ángulo, y se remiten entre sí.

## Copiado de RTVE sin cambios

De `temas/sonido/16-audio-sobre-ip.md` (tema técnico, `actualizar: no`). Palabras idénticas; sólo
se ha quitado el formato (la negrita, porque en Canal Sur la negrita es sólo cita literal de
fuente, y el signo ✔ de la columna «UDP»). Comprobado por script contra el original, normalizando
negrita y espacios.

1. Epígrafe «Por qué el audio va por red»: la tabla matriz clásica / red IP (cuatro filas) y el
   párrafo «Y el precio de esa flexibilidad es lo que ocupa el resto del tema: … con el resto del
   tráfico.»
2. Epígrafe «Qué protocolo lleva el audio: UDP»: «El protocolo que se utiliza por norma general para
   audio en red es UDP.»; «Y la razón es exactamente la contraria de la que la intuición sugiere:»;
   la tabla TCP/UDP (cuatro filas); el párrafo «El razonamiento: en audio en directo, … y seguir en
   hora.»
3. Epígrafe «Dante, un sistema propietario»: el fragmento «un protocolo que permite la transmisión
   de señales de audio y control a través de una red Ethernet.»
4. Epígrafe «AES67, la norma de interoperabilidad»: «Qué es la AES67 y qué la distingue de Dante:
   es una norma de INTEROPERABILIDAD. No pretende sustituir a los sistemas propietarios, sino
   definir un terreno común en el que puedan entenderse.»
5. Epígrafe «Unicast y multicast»: las celdas «Una copia POR DESTINO: si tres equipos quieren la
   misma señal, se manda tres veces», «UNA sola copia que la red reparte a quien se haya suscrito»,
   «Pocos destinos» y «Muchos destinos de la misma señal».
6. Epígrafe «El conmutador de red»: «Una red Dante pide conmutadores gestionables, con calidad de
   servicio para dar prioridad al audio, con soporte de PTP y, si se usa multicast, con control de
   suscripciones.»
7. Epígrafe «Las cuentas de ancho de banda»: la fórmula «Caudal de un canal = frecuencia de
   muestreo × profundidad de bits»; «A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo.
   Ése es el número que hay que tener.»; los tres pasos de la cuenta de 32 canales
   bidireccionales; «cuatro, cuatro y dos».
8. Epígrafe «Por qué hace falta un reloj común»: desde «cada equipo de audio digital tiene su
   propio oscilador» hasta «un chasquido periódico.»
9. Epígrafe «Qué pasa con una latencia alta o baja»: «Si una red Dante presenta alta latencia, se
   introduce un retraso entre la reproducción de las señales de audio, lo que afecta a la
   sincronización.» y «el problema de la latencia no es que el sonido llegue tarde, es que llegue a
   DESTIEMPO respecto a otra cosa —la imagen, otro camino de audio, el sonido directo de una
   sala—.»

## Adaptado de RTVE (sí se verifica)

- «Por la misma red viajan … Un cable hace el trabajo del audio y el del control» (mayúscula y
  marca «oficio»).
- Definición del conmutador («permite la conexión de múltiples dispositivos en una red, gestionando
  el tráfico de datos»), reescrita sin la pregunta 76; «no vale cualquier switch».
- La sobrecarga de cabeceras (se añade RTP y el efecto del tiempo de paquete; se quita la cifra de
  18 Mbps).
- «El PTP no se limita a decir la hora: mide el retardo … y lo compensa», ahora apoyado en la ST
  2059-2 §6.4 (RTVE decía «ida y vuelta» sin fuente); «no se monta una red de audio con cualquier
  switch doméstico».
- «TCP/IP es la familia de protocolos», sin la referencia a las opciones del examen.
- El ejemplo de 10 canales en unicast y el de 16 bits (49,2 Mbps; RTVE daba «26 Mbps» como
  opción falsa de examen y se quita).
- «Latencia configurada, no casual», con los valores ya con fuente (Audinate).

## Quitado de RTVE, y por qué

- Todas las referencias a preguntas, respuestas oficiales, opciones falsas, «sólo con la
  plantilla» y la tabla «Los datos que el examen ha preguntado»: propio de RTVE.
- La tabla NTP / SNTP / PTP con precisiones (milisegundos, «sub-microsegundo») y «tres órdenes de
  magnitud»: sin fuente leída (investigación C, «no confirmado» 3).
- «A 48 kHz, una muestra dura 20 microsegundos»: redondeo (1/48.000 s ≈ 20,8 µs) y sólo servía al
  argumento de la tabla quitada.
- «La máxima frecuencia de muestreo que se puede utilizar en AES67 es 96 kHz»: texto de AES67 no
  leído. Se da en su lugar lo que dice la ST 2110-30 (48 obligatorio; 44,1 y 96 recomendables).
- «El sistema entero se alinea al mayor» (latencia): corregido según Audinate — la latencia
  efectiva de cada flujo es la mayor de emisor y receptor.
- «Cada equipo tiene un valor de latencia —desde unos 150 microsegundos hasta unos pocos
  milisegundos—»: sustituido por las cifras literales de Audinate (1 ms por defecto, 150 µs mínimo,
  1 ms en 100 Mbps).
- «18 Mbps y 3 flujos» (pregunta 47): se conservan los 3 flujos (con el «typically» de Audinate);
  los 18 Mbps no tienen fuente.
- La cita de la presentación de normas AES y la referencia a su tema 17 (MADI): no aportan al
  enunciado de Canal Sur.
- La afirmación «precisamente porque Dante sincroniza, alguno de sus equipos tiene que ser el
  maestro de reloj» se sustituye por la elección del *leader* según Audinate.

## Lo nuevo, con fuente (investigación C y relectura propia el 25-09-2026)

Audinate DC 4.18: flujos, suscripción, formatos, unicast/multicast, inundación, IGMP, Wi-Fi,
DSCP, reloj (cuarzo, *offset*, *pull range*, silenciado, avisos, histograma), reloj externo,
*Preferred Leader*, *PTP Follower Only*, elección, PTPv1/v2, dominio 0 en AES67, latencia,
redundancia y reloj en redundancia, modo AES67 (239.x/16, prefijo). SMPTE ST 2110-30:2025,
ST 2110-10:2022, ST 2059-2:2021, ST 2059-1:2021, ST 2022-7:2019: todo lo citado en la tabla de
trazabilidad del tema. Relectura hecha: cada cita en negrita se buscó en el volcado.

Discrepancia de fuentes que el tema declara: Audinate da «AX: Up to 8 audio channels» y «CX: Up to
64» para sus equipos; la tabla 2 de la ST 2110-30:2025 da 1 a 4 (AX) y 9 a 32 (CX). Manda la norma
y el tema lo dice.

Cálculos propios (declarados en el tema): 1.152 octetos por paquete en A, AX, C y CX con 24 bits
(la profundidad de 24 bits sale de AES67, no leída, y el tema lo advierte); 73,7 Mbit/s para 64
canales; intervalos PTP 2⁰ y 2⁻³.

## Ficheros tocados

- Creado `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.
- Creado este informe.
- No se ha tocado nada más (fuentes sólo leídas).

## Preguntas de control (10, tipo test) y comprobación contra el tema

1. **Audio sobre IP.** ¿Qué protocolo de transporte se usa por norma general para el audio en
   tiempo real en red? a) TCP b) TCP/IP c) UDP d) SNMP. → c. **Entera**: «Qué protocolo lleva el
   audio: UDP» (con la razón y por qué no TCP/IP).
2. **Audio sobre IP (AES67/ST 2110-30).** Según la SMPTE ST 2110-30:2025, ¿qué frecuencia de
   muestreo deben admitir obligatoriamente todos los emisores y receptores? a) 44,1 kHz b) 48 kHz
   c) 96 kHz d) 48 y 96 kHz. → b (44,1 y 96, recomendables). **Entera**: «SMPTE ST 2110-30».
3. **Redes (aplicación práctica).** Ancho de banda de audio de 32 canales bidireccionales a 48 kHz
   y 24 bits, sin cabeceras: a) 36,9 Mbps b) 49,2 Mbps c) 73,7 Mbps d) 147 Mbps. → c. **Entera**:
   «Las cuentas de ancho de banda» (también da 36,9 por sentido y 49,2 con 16 bits).
4. **Redes.** Límite estándar de tamaño UDP en la ST 2110-10, que la ST 2110-30 impone al audio:
   a) 1.500 octetos b) 1.460 c) 8.960 d) 9.000. → b. **Entera**: «El tamaño de los paquetes»
   (con el porqué: 1.500 − 40).
5. **Redes (aplicación práctica).** Se envían 10 canales Dante en unicast. ¿Cuántos flujos hacen
   falta? a) 1 b) 2 c) 3 d) 10. → c (cuatro canales por flujo, «typically»). **Entera**:
   «Unicast y multicast» y «Las cuentas de ancho de banda».
6. **Sincronía (aplicación práctica).** Un equipo Dante excede su margen de corrección de
   frecuencia (*pull range*) respecto al reloj principal. ¿Qué ocurre? a) Pasa a ser *leader*
   b) Pierde la sincronía y se silencia automáticamente c) Duplica su latencia d) Cambia a
   multicast. → b. **Entera**: «Por qué hace falta un reloj común».
7. **Latencia.** Un emisor Dante tiene 0,5 ms de latencia y el receptor 1 ms. ¿Latencia efectiva
   del flujo? a) 0,5 ms b) 0,75 ms c) 1 ms d) 1,5 ms. → c. Pregunta asociada: mínima con un puerto
   de 100 Mbps → 1 ms («Tx Scheduler Failure» si es menor). **Entera**: «Los valores de Dante».
8. **PTP.** En la elección del reloj principal de una red Dante, sin *Preferred Leader*, ¿qué
   equipo se prefiere? a) El de menor latencia b) El que tiene entrada de reloj (word clock o
   AES3) c) El de mayor dirección MAC d) El primero que se conecta. → b (luego gigabit sobre
   100 Mbps; desempate por menor MAC). **Entera**: «Cómo se elige el reloj principal».
9. **PTP.** ¿Qué número de dominio PTP usa AES67 en Dante y cuál es el valor por defecto del
   perfil SMPTE ST 2059-2? a) 0 y 127 b) 127 y 0 c) 0 y 0 d) 1 y 128. → a. **Entera**: «Las
   versiones: PTPv1 y PTPv2» y «El perfil SMPTE: ST 2059-2».
10. **Redundancia (aplicación práctica).** En un equipo Dante con redundancia, el puerto
    secundario se conecta: a) Al mismo conmutador que el primario b) A una segunda red separada, a
    la misma velocidad que el primario c) A cualquier puerto libre, a cualquier velocidad d) Sólo
    si el equipo no admite redundancia. → b. **Entera**: «La redundancia de Dante» y «Aplicación
    práctica de la redundancia».

Resultado: 10 de 10 enteras; no ha hecho falta ampliar. Riesgo conocido y declarado: una pregunta
del tipo «máxima frecuencia de muestreo de AES67» (la que RTVE daba como 96 kHz) no la contesta el
tema, porque el texto de la AES67 no se ha leído; el tema da lo que sí consta (ST 2110-30 y modo
AES67 de Audinate a 48 y 96 kHz) y lo declara en «Lo que este tema no da».
