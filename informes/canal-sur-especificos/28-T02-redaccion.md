# Puesto 28 · Tema 2 · Fase 2 · Redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/02-electricidad-y-electronica-aplicada-al-audio.md`
(unas 8.000 palabras de cuerpo; 7 epígrafes `##` en el orden del enunciado —con un epígrafe 1 de
base eléctrica delante— + normativa, huecos y trazabilidad; 26 `###`). Escrito por partes, guardando
cada `##`. Índice con `indice.py` (no hay fila del tema en su `.tsv`: no generó portada; la ficha
va escrita a mano). `refutar_prosa.py`: 3 siglas sin presentar (AB, VU, DPA), corregidas; 0
hallazgos al final. Una norma citada (RD 2032/2009): procede `negritas.py` sobre esas tres filas.

Otros ficheros tocados: ninguno.

## Fuentes

- Leídas por mí el 25-09-2026: Rane RaneNote 110, 124, 135 y 169 (ranecommercial.com/legacy/
  noteNNN.html). Añaden lo que la investigación A no tenía para «niveles» e «impedancias»: dBu =
  0,775 V rms y origen en 0 dBm/600 Ω (169); dBFS como pico negativo (169); factor de cresta (169);
  +4 dBu = 0 VU, −10 dBV (316 mV) como máximo doméstico frecuente, +20 dBu máximo seguro, 22 dB de
  *headroom* entre +4 y +26 dBu, ganancia de una vez en el previo, sensibilidad de etapa (135);
  transferencia de tensión, 100 Ω/20 kΩ, 6 dB de pérdida al adaptar, 6 dB entre salida balanceada y
  desbalanceada (124); caja DI, par trenzado, RFI (110).
- `28-investigacion-A-fundamentos.md` §2.1-2.4 (masa, pin 1, remedios, *phantom*), §1.2 (polaridad),
  §3.2 (sensibilidad, ruido propio, 0,63/6,3 V). Citas tomadas del informe sin volver a la fuente:
  **verificar** (RN151, RN155, DPA, Schoeps).
- `28-investigacion-C-conexiones-ip-rf.md` §10.4 (Crown: pines XLR/TRS, factor de amortiguamiento,
  calibre, sensibilidad 0,775/1,4 V; TI: rendimientos AB y D). Tomadas del informe: **verificar**.
- RTVE `temas/sonido/01` y `temas/sonido/11`, leídos el 25-09-2026.

## Copiado del común

Ninguno: el común de Canal Sur no desarrolla esta materia.

## Copiado de RTVE sin cambios

Mismas palabras que el original; sólo se ha quitado la negrita de énfasis (en Canal Sur la negrita
es literal de fuente) y, en tablas, la marca ✔ de «respuesta oficial». El verificador sólo comprueba
que es literal.

De `temas/sonido/01-electricidad-y-electronica-basicas.md`:
- 1.1: tabla de las cuatro magnitudes; frase «El amperio, además, es una de las siete unidades
  básicas…».
- 1.2: frase «La ley de Ohm describe la relación entre tensión, corriente y resistencia en un
  circuito eléctrico.»; tabla de los tres despejes.
- 1.3: frase «Las redes eléctricas domésticas de la mayoría de los países europeos suministran
  corriente alterna a 230 voltios.»; tabla 230/110 V.
- 1.4: frase «Un diferencial salta cuando no hay la misma intensidad entre hilos.»; párrafo «El
  interruptor diferencial compara… y el diferencial corta.»; «El diferencial no protege la
  instalación: protege a las personas.»; párrafo «La distinción que hay que llevarse…».
- 3.1: definición de impedancia; tabla resistencia/reactancia/impedancia; párrafo «Por qué le
  importa a un técnico de sonido…».
- 3.3: tabla serie/paralelo; párrafo «Y la consecuencia práctica…».
- 3.4: los tres pasos numerados; párrafos «De ahí la regla del oficio…» (hasta «con 4, no.») y «Y de
  ahí también la razón de ser de la línea de 100 voltios…».
- 3.6: frase «Medir impedancia de verdad, frecuencia a frecuencia, exige un puente de impedancias o
  un analizador.»; filas de osciloscopio y sonómetro.
- 4.3: tabla de los cuatro ángulos.
- 6.2: celdas de las filas de distorsión armónica, de intermodulación y por transitorios; frase
  «El ruido no guarda relación con la señal; la distorsión armónica es hija de ella.»; frase «Está
  relacionada con la velocidad de subida de la etapa…».

De `temas/sonido/11-lineas-y-conexiones.md`:
- 4.1: frase «Por definición, en un conector XLR de tres pines el cable «vivo» se conecta al pin
  2.»; tabla de pines; «Y la regla que el oficio usa para no olvidarlo…».
- 4.2: párrafo «La señal viaja por dos conductores en oposición de fase… se cancela.»; puntos 1 y 2
  de la lista.
- 7.5: frase «La tensión de alimentación A-B, también llamada Tonader, es de 12 voltios.»; párrafo
  «La diferencia de fondo…».
- 3.5: frase «Un cable de micrófono y un cable AES3 llevan el mismo conector y no son el mismo
  cable.»; tabla de impedancias de cable; párrafo «Por qué importa… más difíciles de encontrar.».

## Copiado de RTVE que cita norma (se verifica)

- 1.1: el párrafo del Real Decreto 2032/2009 y las tres filas citadas celda a celda (voltio, ohmio,
  faradio). Las filas van en negrita porque son literal del BOE; releerlas en la redacción vigente.

## Adaptado de RTVE (se verifica)

- Quitado todo lo propio de RTVE: «Ésa es la respuesta oficial a la pregunta N», las tablas de
  opciones falsas, «Los datos que el examen ha preguntado», las salvedades de las preguntas 46 y 82
  (reescritas como consejo de test en 3.3 y 3.6).
- 1.2: ejemplo 5 Ω × 3 A y el aviso de unidades, reescritos sin pregunta; añadida P = V × I y sus
  formas (oficio).
- 1.3: párrafo de 50/60 Hz, sin la referencia al «cuadernillo de la otra ocupación».
- 1.4: tabla de disparos reescrita (fila de «frecuencias» quitada; fila del diferencial añadida).
  **Quitado** el párrafo de los 30 mA y la fibrilación: sin fuente.
- 1.5: tabla de clases: **quitado** «en torno al 25 %» de la clase A (sin fuente); añadida la fila D;
  rendimientos AB y D con fuente TI.
- 3.6: **quitado** «la resistencia de continua de un altavoz de 8 ohmios nominales ronda los 6» (sin
  fuente).
- 6.2: frase de la THD del 0,1 % y la de transitorios, sin «la palabra que decide».
- 7.5: tabla fantasma/A-B: fila fantasma con «48 V (también 12 y 24 en algunos equipos)».
  **Quitada** la regla de RTVE «la fantasma se puede dejar puesta casi siempre»: la contradice
  Schoeps (conectar con la alimentación apagada) y DPA (cinta y desbalanceados).

## Redacción propia (se verifica)

El resto: 2 (niveles) casi entero, 3.2, 4.3-4.4, 5 (masa), 6.1, 7.1-7.4. Oficio sin fuente
declarado en Trazabilidad: la tabla de escalas de 2.1 (dBV = 1 V, dB SPL), la definición de rms, la
tabla de orígenes del ruido de 6.1 (ruido térmico; reguladores y fluorescentes como fuentes, esto
último con apoyo en Rane), las tres masas de 5, y «*bridging*» como nombre del oficio.

## Avisos al verificador

1. Rane 135 da −10 dBV como **«max consumer level»**, no como nivel nominal doméstico; el tema lo
   dice así. No hay fuente leída para el «−10 dBV nominal» del sector (hueco declarado).
2. «Doblar la tensión son unos 6 dB» y «+4 dBu con cresta de 12-20 dB da picos de +16 a +24 dBu» son
   cuentas, no citas.
3. Las citas de DPA sobre polaridad y la del **«thanks to Mr. Ohm»** de RN110 conviene releerlas.

## Diez preguntas tipo test y comprobación

| Nº | Pregunta (rúbrica) | Respuesta | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Un nivel de 0 dBu equivale a: a) 1 V rms; b) 0,775 V rms; c) 0,775 V de pico; d) 1 mW (niveles) | b) | Entera: 2.1 (y por qué no de pico) |
| 2 | En un equipo profesional con nivel medio de +4 dBu y máximo de +26 dBu, el margen dinámico es: a) 4 dB; b) 16 dB; c) 22 dB; d) 30 dB (niveles, práctica) | c) | Entera: 2.3, cita literal |
| 3 | Para la mejor relación señal/ruido, la ganancia de un micrófono débil se toma: a) repartida entre etapas; b) toda en el previo de micrófono; c) en el máster; d) en la etapa de potencia (niveles/ruido, práctica) | b) | Entera: 2.4 |
| 4 | Entre equipos de línea modernos: a) se adaptan impedancias a 600 Ω; b) salida de baja impedancia a entrada de alta; c) salida alta a entrada baja; d) da igual (impedancias) | b) | Entera: 3.2, con la pérdida de 6 dB si se adapta |
| 5 | Cuatro altavoces de 8 Ω en paralelo dan: a) 32 Ω; b) 8 Ω; c) 4 Ω; d) 2 Ω (impedancias, práctica) | d) | Entera: 3.3 (Z / n) |
| 6 | En un jack TRS balanceado, el anillo lleva: a) la malla; b) el vivo; c) el retorno o señal invertida; d) la *phantom* (balanceado) | c) | Entera: 4.1, cita de Crown |
| 7 | La conexión balanceada rechaza el ruido porque: a) la malla lo absorbe; b) la interferencia llega igual a los dos conductores y se cancela al restarlos; c) usa más tensión; d) filtra los 50 Hz (balanceado) | b) | Entera: 4.2 |
| 8 | Según la práctica AES48 que recoge Rane, el pin 1 de un XLR en un equipo se une a: a) masa de señal; b) chasis; c) pin 3; d) nada (masa) | b) | Entera: 5.2, con el «problema del pin 1» |
| 9 | Para eliminar un zumbido de 50 Hz nunca se debe: a) usar un transformador de aislamiento; b) usar una DI; c) quitar la toma de tierra del enchufe; d) revisar las masas (masa/ruido, práctica) | c) | Entera: 5.3 y 6.1 |
| 10 | La alimentación *phantom* P48: a) 48 V ±4 V en los pines 2 y 3, 7 mA nominales y 10 mA máximo; b) 48 V entre los pines 2 y 3; c) 12 V con polaridad opuesta; d) 48 V en el pin 1 (phantom) | a) | Entera: 7.2; la b) y c) se descartan con 7.3 y 7.5 |

Las diez se contestan enteras con el tema; ninguna obligó a ampliar. Rúbricas cubiertas: niveles
(1, 2, 3), impedancias (4, 5), balanceado (6, 7), masa (8, 9), ruido (3, 9), *phantom* (10);
aplicación práctica en 2, 3, 5 y 9.
