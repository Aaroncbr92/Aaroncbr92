# Operador/a de Sonido (28) · Tema 12 · Redacción

Fase 2. Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`
(unas 8.800 palabras con tablas; 4 rúbricas `##`, 24 epígrafes `###`, más los de cierre).

Fecha de lectura de todas las fuentes: **25-09-2026**. El encargo fija el día de trabajo en el 24-09-2026; la
sesión corre el 25-09-2026 y la investigación C leyó el CNAF ese día. Declaro la fecha real.

## Fuentes leídas por el redactor (25-09-2026)

- Orden TDF/732/2026 (BOE-A-2026-15661), volcado `fuentes/canal-sur/sonido/BOE-A-2026-15661.txt`: preámbulo,
  DA 2.ª, derogatoria, DF 2.ª, notas UN-36, 48, 49, 81, 95, 105, 118, 119, 127, 151, 153 y rótulo del cuadro en
  790-862 MHz. Cada cita del tema, comprobada contra el volcado.
- Shure, *Wireless Systems Guide for Antenna Setup* (`shure-antenna.txt`) y *Selection and Operation of
  Wireless Microphone Systems* (`shure-selection.txt`): cada cita en inglés, buscada en el volcado (con los
  saltos de línea unidos).
- `28-investigacion-C-conexiones-ip-rf.md` (§12), RTVE `temas/sonido/13-radiofrecuencia.md` y
  `temas/informacion-grafica/06-el-sonido-en-eng.md`; Canal Sur `08-camara-operador/06-captacion-de-sonido.md`
  (cerrado) y `28-operador-a-de-sonido/03-microfonia.md` (en ciclo; sólo para no repetir y remitir).

## Copiado del común

Del tema 6 del específico de Cámara Operador de Canal Sur (cerrado: tiene `08-T06-final.md`), epígrafe
«Los inalámbricos y los grupos de frecuencia»:

- La tabla Banda / Grupo / Canal y los dos párrafos siguientes («El grupo es la clave…» hasta «…niega la
  razón de ser del grupo.»), literales, en el epígrafe **«Banda, grupo y canal»** de la rúbrica
  Coordinación de frecuencias. No se copió el primer párrafo (el receptor «va en la cámara») ni la lista
  de comprobación del cámara. El párrafo que sigue («El grupo vale para los equipos de una misma marca…»)
  es nuevo, de oficio, y sí se verifica.

## Copiado de RTVE sin cambios

RTVE marcado «actualizar: no» para este tema. Palabras idénticas (comprobado por programa con los
espacios y negritas normalizados); sólo se han quitado las negritas de RTVE, porque en Canal Sur la
negrita marca literal de fuente.

1. `sonido/13` §4: la tabla de modulaciones (AM, FM, PM, digitales) y el párrafo «Y la razón de que la FM
   ganara a la AM en calidad… ahí el ruido y la señal son lo mismo.» → epígrafe «Los tipos de modulación».
   No se copiaron las dos frases sobre el examen de RTVE.
2. `sonido/13` §5: la frase «Los cinco problemas que un montaje de inalámbricos plantea, y cómo se
   resuelven:» y su tabla de cinco filas → epígrafe «Los cinco problemas de un montaje».
3. `sonido/13` §5: «un cable de audio largo casi no pierde nivel; un cable de radiofrecuencia largo pierde
   mucho y a más frecuencia más pierde. Por eso las antenas se acercan al escenario y no los receptores.»
   (sólo la mayúscula inicial) → epígrafe «El cable y los conectores».
4. `sonido/13` §1: «Cada vez que ese espectro se reasigna, los equipos de microfonía se quedan fuera de
   banda.» → epígrafe «Por qué ya no hay micrófonos por encima de 694 MHz».
5. `informacion-grafica/06` §7: «Un receptor sintoniza una frecuencia: dos emisores en el mismo receptor se
   pisan.» → epígrafe «Una frecuencia por micrófono, y el efecto captura».

## Adaptado de RTVE (sí se verifica)

- `sonido/13` §1: «Los micrófonos sin hilos han trabajado siempre en los huecos del espectro de la
  televisión» (RTVE: «trabajan históricamente en huecos de las bandas IV y V»; quito las bandas, sin
  fuente). «La banda II es la de la radio FM, la del dial de 87,5 a 108 MHz» (RTVE las da como cifras de
  uso corriente sin norma leída: **a verificar**).
- `informacion-grafica/06` §7: «Lo que descarta conectar dos micrófonos a un solo receptor es entender que
  un receptor es un sintonizador…» (RTVE: «Lo que la descarta es entender…»).

Lo quitado de RTVE: bandas I-V, tono piloto, DAB+, tabla de preguntas de RTVE (radiodifusión, fuera de
este enunciado; declarado en «Lo que este tema no da»).

## Decisiones y avisos para verificación

- **Discrepancias de la fuente, declaradas y no resueltas**: 1785-1805 (UN-119) frente a 1785-1804,8 MHz
  (UN-48); 821,5-832 (texto UN-151) frente a 823-832 MHz (rótulo del cuadro).
- **Shure no cuadra consigo mismo**: el ejemplo de 200 MHz («approximately 6 feet (2 m)», 1 m, 45 cm) no
  sale de su fórmula (300/200 = 1,5 m). Uso la fórmula y el ejemplo de 500 MHz (15 cm), que sí cuadra.
  Declarado en Trazabilidad.
- Las definiciones de los tipos de diversidad se reescribieron contra el texto de Shure (la investigación
  sólo daba los nombres).
- Cálculos propios, rehacibles: tabla de longitudes de onda, cuarto de onda en TDT, ejemplo de pérdida
  en cable, caso de intermodulación 606,0 / 606,8 / 607,2 MHz (y la trampa de 607,6).
- El «canal de TDT de 8 MHz en Europa» se toma del tema 3 (DPA); si el tema 3 cambia, revisar.
- `refutar_prosa.py`: queda un falso positivo, «ETD» (parte del código de la Orden ETD/1449/2021).
- `indice.py`: índice generado. El tema no está en `herramientas/portadas.tsv`, así que la portada es
  manual (extensión 8.800 palabras).
- Lentes de normas pendientes para verificación: el tema cita el CNAF (`negritas.py`,
  `refutar_exactitud.py`, `refutar_modo.py` con el BOE-A-2026-15661).

## Preguntas tipo test (comprobación antes de entregar)

Repartidas por las cuatro partes del enunciado (radiofrecuencia y norma, antenas, coordinación,
interferencias), teoría y aplicación práctica. Resultado: **las 10 las contesta enteras el tema**.

1. ¿Qué norma aprueba el Cuadro Nacional de Atribución de Frecuencias vigente?
   a) Orden ETD/1449/2021 · b) **Orden TDF/732/2026** · c) Real Decreto 123/2017 · d) Ley 11/2022.
   → Entera: «Qué bandas puede usar…» (y la derogación de la ETD/1449/2021).
2. Según el CNAF, los micrófonos profesionales en la banda 470-694 MHz se permiten:
   a) con carácter preferente y 10 mW · b) **a título secundario, sin derecho a protección, con 50 mW de
   p.r.a. como máximo** · c) sólo en exteriores · d) con título habilitante siempre.
   → Entera: tabla de notas y salvedades (UN-36).
3. La banda 1785-1805 MHz para micrófonos profesionales en recintos cerrados admite como potencia máxima:
   a) 10 mW p.r.a. · b) 50 mW p.r.a. · c) **20 mW p.i.r.e., y hasta 50 mW p.i.r.e. los dispositivos junto al
   cuerpo** · d) 4 W p.i.r.e.
   → Entera: tabla de notas (UN-119).
4. ¿Por qué un micrófono que emite en 750 MHz ya no puede usarse?
   a) porque es VHF · b) **porque la banda 694-790 MHz está destinada desde el 31-10-2020 a banda ancha
   inalámbrica** · c) porque es la banda del DECT · d) porque sólo se permite en interiores.
   → Entera: «Por qué ya no hay micrófonos por encima de 694 MHz» (UN-153).
5. (Práctica) Un receptor trabaja hacia 600 MHz. ¿Cuánto mide aproximadamente su antena de cuarto de onda?
   a) 50 cm · b) 25 cm · c) **12,5 cm** · d) 4 cm.
   → Entera: fórmula λ = 300/f y tabla.
6. Para montar una antena lejos del receptor, con cable, se usa:
   a) una de cuarto de onda, que necesita plano de tierra · b) **una de media onda o una direccional** ·
   c) cualquiera, siempre que sea de 75 Ω · d) una yagi de canal estrecho.
   → Entera: tabla de tipos de antena y resumen de Shure.
7. (Práctica) Hay que alimentar cuatro receptores desde un par de antenas. Lo correcto es:
   a) dos repartidores pasivos en cascada · b) **un sistema de distribución activa** · c) un combinador
   pasivo · d) un amplificador de 20 dB por receptor.
   → Entera: «La distribución de antena» (3 dB por división, máximo 5 dB, pasivo sólo para dos).
8. En un tendido de antena, ¿a partir de qué pérdida deben usarse amplificadores de antena, y con qué
   ganancia neta máxima?
   a) 1 dB; 20 dB · b) **más de 5 dB; menos de 10 dB** · c) 10 dB; 30 dB · d) nunca hacen falta con cable de 50 Ω.
   → Entera: tabla «El cable y los conectores».
9. (Práctica) Dos micrófonos en 500,0 y 500,5 MHz. Sus productos de intermodulación de tercer orden caen en:
   a) 1000,5 y 0,5 MHz · b) **499,5 y 501,0 MHz** · c) 500,25 MHz · d) 250,0 y 250,25 MHz.
   ¿Y qué margen recomiendan los fabricantes entre un producto de tercer orden y un canal en uso? **250 kHz**.
   → Entera: fórmulas IM1/IM2, «f1 – F / f2 + F» y margen.
10. Un receptor sufre cortes por multitrayecto en UHF. ¿Qué lo remedia y cómo se colocan sus antenas?
   a) subir la potencia del emisor; antenas juntas · b) **diversidad; antenas separadas al menos un cuarto de
   onda (unos 10 cm en UHF)** · c) cable de 75 Ω; antenas horizontales · d) silenciador más alto; antenas
   dentro del bastidor.
   → Entera: «El multitrayecto y los cortes», «La diversidad», «Dónde se pone la antena».

Reserva comprobada también (no numerada): los dos emisores de un inalámbrico doble van en el mismo grupo
(«Banda, grupo y canal»); la frecuencia imagen dista 2 × FI del canal («Las frecuencias internas del
receptor»); el silenciador de tono sólo abre con señal y tono («El receptor por dentro»); distorsión con
indicación de pico → bajar la ganancia del emisor («Diagnóstico»). No hizo falta ampliar el tema.

## Ficheros tocados

- Creado `temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`.
- Creado este informe.
- Temporales en el scratchpad de la sesión (volcados de Shure en una sola línea para buscar citas).
