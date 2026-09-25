# Puesto 28 · Operador/a de Sonido · Tema 5 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md` (unas 7.700
palabras según `indice.py`, contando ficha, siglas y trazabilidad; 8 rúbricas en el orden del
enunciado —ecualización, dinámica, compresión, limitación, puertas, filtros, reverberación,
efectos—, 29 epígrafes `###`).

Material usado: `informes/canal-sur-especificos/28-investigacion-A-fundamentos.md` (§ 5.1-5.3
Rane RN155; § 13.2 R 128 punto m) y definición de pico verdadero; § 13.5 Tech 3343); RTVE
`temas/sonido/07-mezcla-y-tratamiento-del-sonido.md` y `temas/sonido/08-postproduccion-efectos-y-daw.md`
(§ 1 y 4); tema cerrado de Canal Sur `08-camara-operador/06-captacion-de-sonido.md`.

No se ha releído ninguna fuente primaria en esta fase: todas las citas nuevas salen del informe de
investigación (fuentes leídas allí el 25-09-2026) o del tema cerrado de Cámara. El tema no cita
ninguna norma legal.

## Reparto real del material

Lo copiado literal del RTVE es el 18 % de las palabras del cuerpo del tema (1.109 de 6.234, medido
por script); con lo adaptado, en torno a un tercio. No el 90 % de la tabla de reuso: el RTVE 07
dedica buena parte a comentar las preguntas de su examen (quitado), y el enunciado de Canal Sur pide
además puertas, reverberación y efectos, que el RTVE sólo trataba en una fila de tabla o en un
epígrafe.

## Qué se quitó por propio de RTVE o sin fuente

- Todas las referencias a preguntas y respuestas oficiales del examen RTVE (21, 22, 23, 40, 45, 56,
  91 del RTVE 07; 15 y 36 del RTVE 08), las marcas ✔ y los epígrafes «Los datos que el examen ha
  preguntado»; los distractores se reconvierten en explicación («Headroom no es rango dinámico»,
  «para qué no sirve el notch») o se quitan («lineal», «de ganancia constante»).
- RTVE 07 § 1: la tabla de *headroom* con «+4 dBu» y «de 18 a 24 dB» (orden de magnitud sin fuente;
  la propia investigación B declara no leído el +4 dBu). Se sustituye por la remisión al tema 2
  (Rane RN135: +4/+26 dBu, 22 dB) y por la alineación de la EBU copiada de Cámara.
- RTVE 07 § 3: «es obligación técnica en radiodifusión» (sin norma); la fila del transmisor queda
  en «Que no se sobremodule», con el apoyo de Rane.
- RTVE 07 § 5: «Lo que la pregunta mide es…» se reescribe como «Lo que hay que saber es…».
- RTVE 08 § 2 (latencia de la estación de trabajo), § 3 (capas de la banda sonora) y § 5
  (sincronización): fuera de este enunciado; van al tema 9.

## Copiado del común

Pasajes literales del tema 6 del específico de Cámara Operador (`08-camara-operador/06-captacion-de-sonido.md`,
cerrado: `08-T06-final.md`). No se re-verifican.

1. «El headroom», los dos párrafos del epígrafe «El nivel de alineación: −18 dBFS» de Cámara («En
   digital, el máximo absoluto es 0 dBFS…» y «La EBU R 68 recomienda…», con las citas de R 68 y
   Tech 3343) y la primera frase del tercero («Es decir: el tono de referencia es una senoide de 1
   kHz a −18 dBFS.»; el resto, propio de la cámara Sony, no se copia).
2. «Por qué 18 dB de reserva»: el epígrafe de Cámara entero (tres párrafos: R 68 y cuasipico; la
   suma de 9 + 6 = 15 dB; el PML de −9 dBFS obsoleto según Tech 3343 y la alineación sin cambios).
3. «El limitador y el pico verdadero»: la frase «Según la Tech 3343, «It is only necessary to leave
   a headroom of 1 dB…»; para dos sistemas de reducción de datos… el límite recomendado es −2
   dBTP.» (en Cámara, dentro del punto 2 de una lista; aquí sin la sangría).

Comprobado por script: cada pasaje es copia exacta del texto de Cámara (salvo saltos de línea).

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra; **sólo se ha quitado la negrita** (en el RTVE era
énfasis y aquí negrita = literal de fuente) y la marca ✔. Ninguno cita norma. Comprobado por script:
cada párrafo o fila, sin `**` ni ✔, es subcadena del RTVE.

De `temas/sonido/07-mezcla-y-tratamiento-del-sonido.md`:
1. «Los tipos de ecualizador»: la tabla de cuatro filas (Gráfico, Paramétrico, Semiparamétrico,
   «Multibanda») (§ 5).
2. «Los tipos de ecualizador»: «El compresor multibanda existe y es corriente —parte el espectro en
   bandas y comprime cada una por separado—. La palabra es real; el aparato al que se aplica es otro.
   Y para más confusión, todo ecualizador gráfico es, literalmente, de muchas bandas.» (§ 5; la frase
   siguiente es adaptada).
3. «El factor Q»: el párrafo «Qué es el Q: … la que hay que tener:» y la tabla de cinco filas (§ 6).
4. «El factor Q»: «En un gráfico el Q está fijo y no se toca, y es precisamente en el paramétrico
   donde el Q se ajusta.» (§ 6; la frase siguiente es adaptada).
5. «El headroom»: el párrafo «Qué es y por qué existe: … una entrada mal medida.» y el párrafo «La
   diferencia que más cuesta interiorizar: … bien por debajo del techo.» (§ 1).
6. «Headroom no es rango dinámico»: filas «Masterización» y «Nivel de presión sonora» de la tabla
   (§ 1; la fila «Rango dinámico» es adaptada: se quitó «Es la falsa mejor puesta»).
7. «Qué hace un compresor y sus mandos»: el párrafo de entrada y la tabla de seis mandos (§ 2).
8. «La recuperación de ganancia»: el párrafo «Por qué hace falta: … lo hace la ganancia de
   después.» (§ 2).
9. «Las tecnologías de compresor»: la tabla de cuatro tecnologías y el párrafo «Y la regla que
   ordena la tabla: …» (§ 4).
10. «Qué es un limitador»: la definición «El compresor que actúa sólo atenuando…» (sin «Ésa es la
    respuesta oficial…») y el párrafo «Qué lo define: …» (§ 3).
11. «Para qué se usa»: filas «Proteger una etapa de potencia» y «Cerrar una masterización» (§ 3).
12. «El filtro notch y el acoplamiento»: los párrafos «Qué es un notch: …» y «Por qué sirve contra
    el acoplamiento: …» (§ 6).
13. «Los sistemas de reducción de ruido»: la tabla de cinco familias (§ 7).

De `temas/sonido/08-postproduccion-efectos-y-daw.md`:
14. «Los parámetros de una reverberación»: la frase de entrada y los puntos 2 y 3 de la lista
    (§ 4; el punto 1 es adaptado: «tema 4» → «tema 1»).
15. «Las familias de efectos»: filas de TIEMPO, MODULACIÓN y De altura (§ 4; las de DINÁMICA y
    FRECUENCIA son adaptadas: se quitó la remisión «—el tema 7—»).
16. «El retardo a tempo»: la tabla de figuras a 102 BPM con su frase de entrada y la frase «Lo mismo
    vale para el tiempo de relajación… de una reverberación.» (§ 1).

**Adaptado de RTVE (sí se verifica):** la definición del *headroom* (antes, respuesta a la pregunta
21); la definición del *make-up* y la frase del codo; «De las cuatro, la de respuesta más rápida es
el VCA»; la frase de la clase A (sin «la del tema 1»); la fila «Proteger un transmisor»; la frase de
*rumble*; «Un filtro notch se utiliza idealmente…» y los tres casos en que no sirve; la regla «el
mejor sistema de reducción de ruido es no grabarlo» (remisión al tema 3); la frase de la
reverberación como miles de retardos; el punto 1 de los parámetros; las filas de DINÁMICA y
FRECUENCIA; «El retardo a tempo» (cuenta en dos pasos generalizada a las figuras, ejemplo de 102 BPM
sin la pregunta 15).

## Nuevo (se verifica entero)

- «Qué es un procesador de dinámica» (Rane RN155: estructura común, cadena lateral, la lista de
  procesadores, la analogía limitador/puerta) y su tabla de cuatro procesadores (oficio).
- «Puertas» entera: expansor y puerta, parámetros, usos y defectos, clave externa, *look-ahead* y
  *ducker* (Rane RN155); la histéresis, la tertulia y la música bajo la voz, como oficio.
- Rane en «Compresión» (umbral −40/+20 dBu; relajación 25 ms-2 s) y en «Para qué se usa» (usos del
  limitador de picos) y la frase del detector de pico en «Qué es un limitador».
- R 128 punto m) y definición de *Maximum True Peak Level* en «El limitador y el pico verdadero».
- Cálculos: fórmula Q = √(2ᴺ) ÷ (2ᴺ − 1) y sus cuatro valores; campana de Q 1,414 a 1 kHz (707 a
  1.414 Hz); compresor a −20 dBFS con 4:1 y 2:1 (−17 y −14 dBFS; 9 y 6 dB de reducción).
- Oficio declarado: formas de ecualización (campana, estantería, corte), reglas de ecualización,
  ataque y relajación, reductor de sibilantes, compresión de voz, limitador de captación, los
  cuatro filtros de corte, el paso alto como primer proceso, tipos y uso de la reverberación,
  efectos de modulación, inserción y envío, orden de la cadena.

## Avisos para verificación

- El ejemplo del expansor: la investigación resume el de Rane como «umbral just below the quietest
  recorded vocal level, ratio 2:1, escalón de −10 dB al ruido de fondo → 10 dB de mejora»; el tema lo
  lee como «ruido 10 dB bajo el umbral sale 20 dB bajo». Conviene cotejarlo con la RaneNote 155.
- El margen de umbral «−60 dBu» es de expansor en Rane; en la tabla de la puerta va rotulado «En
  expansores».
- Incoherencia entre temas cerrados/en curso, no de este tema: el tema 2 llama «margen dinámico» al
  *headroom*; el tema 1 y éste lo llaman «margen de seguridad». Conviene unificar en el remate.

## Huecos declarados (en el tema, «Lo que este tema no da»)

Pendiente de los filtros por orden y frecuencias de corte habituales; márgenes de compresor fuera de
Rane; histéresis; reducción espectral concreta (va al tema 9); lo propio de CSRTV (procesado de
salida, cadenas de voz).

## Lentes

`indice.py`: índice generado (no hay fila en `portadas.tsv`; la extensión de la ficha se puso a
mano con la cifra de `indice.py`). `refutar_prosa.py`: 0 hallazgos (tras quitar de las siglas
LUFS, QPPM y DAW, que el cuerpo no usa). Sin lentes de norma: el tema no cita normas legales.

## Otros ficheros tocados

Ninguno fuera del tema y este informe.

## Preguntas tipo test de comprobación (10)

| # | Rúbrica | Pregunta | Respuesta | ¿La contesta el tema? |
|---|---|---|---|---|
| 1 | Ecualización | En un ecualizador paramétrico, un factor Q de 1,41 corresponde aproximadamente a: a) 1/3 de octava b) 1/2 octava c) 1 octava d) 2 octavas | c) | Entera: «El factor Q» (tabla y fórmula) |
| 2 | Dinámica | Según la EBU R 68, el nivel de alineación en digital se sitúa: a) en 0 dBFS b) 9 dB bajo el máximo c) 18 dB bajo el máximo de codificación, sea cual sea el número de bits d) en −23 dBFS | c) | Entera: «El headroom» (R 68 y Tech 3343) |
| 3 | Compresión (práctica) | Compresor con umbral −20 dBFS y relación 4:1; entra un pico de −8 dBFS. ¿A qué nivel sale? a) −8 dBFS b) −17 dBFS c) −20 dBFS d) −14 dBFS | b) | Entera: «Qué hace un compresor y sus mandos», ejemplo resuelto |
| 4 | Compresión | ¿Qué tecnología de compresor tiene la respuesta más rápida? a) óptico b) clase A c) Vari-Mu d) VCA | d) | Entera: «Las tecnologías de compresor» (y por qué la clase A no es tecnología de compresión) |
| 5 | Limitación | Según la EBU R 128, el nivel de pico verdadero de un programa en producción no debe superar: a) 0 dBFS b) −1 dBTP c) −9 dBFS d) −18 dBFS | b) | Entera: «El limitador y el pico verdadero» (y PML de −9 dBFS obsoleto en «Por qué 18 dB de reserva») |
| 6 | Puertas | En una puerta de ruido, el mando que determina cuánto tiempo permanece abierta después de que la señal de control cae bajo el umbral es: a) el ataque b) la profundidad c) el mantenimiento (*hold*) d) la liberación | c) | Entera: «Los parámetros de la puerta» |
| 7 | Puertas (práctica) | Una puerta produce un chasquido al abrirse. La causa más probable es: a) profundidad escasa b) ataque demasiado rápido c) mantenimiento demasiado largo d) umbral demasiado bajo | b) | Entera: «Usos y defectos de la puerta» (Rane: cuanto más rápido abre, más agudo el clic) |
| 8 | Filtros | Un filtro notch se utiliza idealmente para: a) evitar la diafonía entre canales b) evitar un acople con una megafonía c) atenuar las medias de un bombo d) quitar las oclusivas de una voz | b) | Entera: «El filtro notch y el acoplamiento» (y por qué las otras tres no) |
| 9 | Reverberación | En una reverberación, el parámetro que fija cuánto tarda en empezar la cola es: a) el tiempo de reverberación b) la mezcla seco/húmedo c) la predemora d) la difusión | c) | Entera: «Los parámetros de una reverberación» |
| 10 | Efectos (práctica) | Un retardo de corchea en un tema de 4/4 a 102 BPM dura aproximadamente: a) 588 ms b) 294 ms c) 147 ms d) 920 ms | b) | Entera: «El retardo a tempo» |

Comprobación adicional de lo que las diez dejan fuera: «multibanda» no es tipo de ecualizador
(«Los tipos de ecualizador»); *make-up* («La recuperación de ganancia»); diferencia entre puerta y
expansor (relación infinita, detector de pico); *ducker* y clave externa; *headroom* frente a rango
dinámico; familia del *flanger* (modulación); reverberación en envío y compresor en inserción. Las
diez, repartidas por las ocho rúbricas (ecualización 1; dinámica 1; compresión 2; limitación 1;
puertas 2; filtros 1; reverberación 1; efectos 1; cuatro de aplicación práctica o cálculo), se
contestan enteras con el tema; no ha hecho falta ampliar.
