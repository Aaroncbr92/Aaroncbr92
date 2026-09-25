# Puesto 28 · Operador/a de Sonido · Tema 1 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/01-fundamentos-de-sonido.md` (unas 7.100
palabras según `indice.py`; 8 rúbricas en el orden del enunciado, 28 epígrafes `###`).

Material usado: `informes/canal-sur-especificos/28-investigacion-A-fundamentos.md` (§ 1.1-1.4, 5.1
rango dinámico, 13.7 correlador); RTVE `temas/sonido/02`, `temas/sonido/04`,
`temas/edicion-montaje/03` (§ 1-2); tema cerrado de Canal Sur `08-camara-operador/06`.

## Fuentes releídas en esta fase

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 2032/2009 (BOE-A-2010-927), `boe.py precepto` bloques `cii` y `civ`, vigente hoy | 25-09-2026 | Cap. II (redacción vig. 30-04-2020, pub. 29-04-2020, BOE-A-2020-4707): tabla 3, filas «frecuencia · hercio · Hz» y «presión, tensión · pascal · Pa · N/m2», nota (d). Cap. IV (redacción única, vig. 22-03-2010): apartado 4 literal, tabla 8 (bar = 0,1 MPa = 100 kPa; neper, belio, decibelio) y nota (i) literal |

**Corrección al RTVE (manda la fuente):** el RTVE 02 sitúa el pascal en un «cuadro de unidades
derivadas coherentes» sin decir dónde; está en la **tabla 3 del capítulo II**. El decibelio está
en la **tabla 8 del capítulo IV** (apartado 4 y nota (i)), no en una tabla de «unidades ajenas al SI
cuyo uso se acepta» (esa es la tabla 6; la 8 es «de aplicación exclusiva en sectores específicos»).
El tema lo dice bien. La cita del bar se ha cortado en «100 kPa» porque el volcado da «105 Pa»
(superíndice perdido de 10⁵).

## Qué se quitó por propio de RTVE o sin fuente

- Todas las referencias a preguntas y respuestas oficiales del examen RTVE (89, 65, 90, 94, 50, 55,
  33, 37) y los epígrafes «Los datos que el examen ha preguntado»; las cuentas se reconvierten en
  ejemplos resueltos.
- RTVE 02: la temperatura de 20 °C como condición de la referencia de 20 µPa (sin fuente; el propio
  RTVE admitía que no la sostiene el RD); la curva de Wegel (no contrastada).
- RTVE edicion-montaje/03 § 3-6 (audio digital, RTP, filtros, *ducking*): fuera de este enunciado
  (van a los temas 5, 7, 9 y 15); sólo se tomaron § 1-2.
- RTVE 04: la mención a `fuentes/normas-tecnicas/README.md` y a la ISO 3382 no leída.

## Copiado del común

Pasajes literales del tema 6 del específico de Cámara Operador (cerrado: `08-T06-final.md`). No se
re-verifican.

1. «Qué es el sonido y qué lo describe»: párrafo «El sonido es una onda de presión que viaja por un
   medio elástico…», la tabla de cuatro magnitudes (frecuencia, periodo, longitud de onda,
   amplitud) y el párrafo «El número de ciclos por segundo es la frecuencia…».
2. «El margen de frecuencias audibles»: frase «El margen de frecuencias audible por un ser humano va
   de 20 Hz a 20.000 Hz. Es un valor convencional para un oído joven y sano.», la tabla de zonas y
   la frase «Los límites entre graves, medios y agudos son de oficio, no de norma.» (el resto del
   párrafo es nuevo).
3. «El margen dinámico de un equipo»: definición, tabla techo/suelo, párrafo «El margen dinámico es
   la distancia entre los dos…», párrafo «Las definiciones falsas cambian uno de los dos
   extremos…» y la frase «El cálculo que va con el margen: … Por eso el audio de producción se graba
   a 24 bits.» (sin la cita de EBU R 68, que se deja al tema 13).
4. «La amplitud y la distancia»: la cita de DPA «The SPL from point sources drops by 6
   dB/doubling of distance.» y el ejemplo de 40/20/10 cm, adaptados en redacción (el verificador
   puede saltar la cita, ya verificada en Cámara).

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra; **sólo se ha quitado la negrita** (en el RTVE era
énfasis y aquí negrita = literal de fuente) y la marca ✔. Ninguno cita norma. Comprobado por
script: cada línea, sin `**`, es subcadena del RTVE.

De `temas/sonido/02-principios-fisicos-del-sonido-y-la-audicion.md`:
1. «No hay sonido en el vacío, y la onda no transporta materia: transporta una perturbación.» (§ 1)
2. «La relación que las une… diez centímetros.» y «De ahí salen dos consecuencias… cualquier
   obstáculo—.» (§ 1)
3. Tabla de ruido blanco/rosa (fila rosa sin ✔), párrafos «Por qué el rosa cae…» y «De ahí que el
   ruido rosa sea el que se usa…» (§ 5)
4. «Un pascal es un newton por metro cuadrado. Y el orden de magnitud… Un millón de veces más.»
   (§ 2); fila «Newton» de la tabla de unidades.
5. «De esa frase se sigue la regla… cambia el número.» y la tabla de escalas dB SPL, dBu, dBV, dBFS,
   dBm (§ 3).
6. «Para magnitudes de AMPLITUD… Ésa es la distinción que más se falla.» (§ 4)
7. «El conjunto de curvas que representan…», «Qué dicen: …» y las tres consecuencias numeradas
   (§ 6).
8. «El margen audible del oído humano…» y la definición y tres reglas del enmascaramiento (§ 7).

De `temas/sonido/04-acustica-arquitectonica.md`:
9. § 1 entero (frase de entrada, tabla de tres componentes y párrafo de los 50 ms).
10. § 2: definición de RT60, «Y los valores que se buscan…», tabla de RT60 y párrafo de Sabine.
11. § 3: «Qué es una onda estacionaria…», «Por qué las paralelas…» y las tres consecuencias.
12. § 4: tabla palabra/música y párrafo de salas polivalentes.
13. § 5: tabla de decisiones de oficio y «La regla que resume el tema…».

De `temas/edicion-montaje/03-conceptos-basicos-de-sonido.md`:
14. § 1: frase de entrada, tabla de las tres cualidades y «La frecuencia no es el tono…».
15. § 2: «La propiedad del sonido directamente relacionada…» (sin «Ésa es la respuesta
    oficial…»), «Qué son los armónicos…», «Lo que cambia de un instrumento a otro…» (sin su última
    frase sobre el enunciado) y «Y una consecuencia de oficio…».

**Adaptado de RTVE (sí se verifica):** las citas del RD 2032/2009 (pascal y decibelio, releídas hoy
en el BOE; ver arriba), la tabla de unidades falsas (bar con cita del RD; W/m² en lugar de W/cm²),
la tabla de aritmética (ampliada a columna de potencia), los tres ejemplos resueltos, las NC/NR
resumidas, la frase de las ondas estacionarias y la de los RT60 orientativos, la frase del
margen audible por edad en «Frecuencia».

## Nuevo (se verifica entero)

- «Fase» entera (DPA «Polarity, phase and delay» y «Comb filtering»; RTW), con cálculos propios
  (retardo de 1 ms a 1 kHz, 500 Hz y 250 Hz; 34 cm).
- «El hercio, unidad legal» (RD, tabla 3 y nota (d)).
- Rango dinámico de una señal y la cita de Rane RN155 (+26/−94 dBu, 120 dB).
- «El oído y la fase» (DPA), «La audición como riesgo» (remisión al tema 16).
- Cálculos: tabla de periodos y longitudes de onda; 20 × log 10⁶ = 120 dB; suma de fuentes
  correladas (+6 dB) y no correladas (+3 dB); 50 ms ≈ 17 m; primer modo de 50 Hz entre paredes a
  3,4 m; octavas del margen audible (2¹⁰).
- Aplicaciones prácticas de oficio: sombra de obstáculos, mesa de tertulia, mezcla a volumen bajo,
  hueco a la voz frente a la música, micrófono fuera de eje, coeficiente α.

## Huecos declarados (en el tema, «Lo que este tema no da»)

Fisiología del oído y de la voz; localización biaural; velocidad del sonido exacta; constante de
Sabine y medición normalizada de RT60; goniómetro; lo propio de CSRTV (salas y estudios).

## Lentes

`indice.py`: índice regenerado. `refutar_prosa.py`: 1 hallazgo (sigla RTW sin presentar), corregido
presentando a los fabricantes en las siglas. Sin lentes de norma (el tema cita una sola norma,
releída a mano).

## Otros ficheros tocados

Ninguno fuera del tema y este informe.

## Preguntas tipo test de comprobación (10)

| # | Rúbrica | Pregunta | Respuesta | ¿La contesta el tema? |
|---|---|---|---|---|
| 1 | Ondas (práctica) | Con una velocidad del sonido de 340 m/s, ¿cuánto mide la longitud de onda de un tono de 170 Hz? a) 0,5 m b) 1 m c) 2 m d) 57,8 m | c) | Entera: «La relación entre longitud de onda y frecuencia» (λ = v/f y tabla) |
| 2 | Frecuencia | El ruido rosa: a) tiene la misma energía por hercio b) cae 6 dB por octava c) tiene la misma energía por octava y cae 3 dB por octava d) es el ruido marrón | c) | Entera: «El ruido rosa y el ruido blanco» |
| 3 | Timbre | La propiedad del sonido directamente relacionada con las intensidades relativas de sus armónicos es: a) la intensidad b) el tono c) la frecuencia d) el timbre | d) | Entera: «El timbre y los armónicos» (y por qué «frecuencia» es magnitud, no cualidad) |
| 4 | Amplitud (práctica) | ¿Qué diferencia de nivel hay entre una tensión de 1 V y otra de 2 V? a) 3 dB b) 6 dB c) 2 dB d) 10 dB | b) | Entera: «La aritmética del decibelio», ejemplo 1 |
| 5 | Amplitud (norma) | Según el Real Decreto 2032/2009, el decibelio: a) es unidad SI b) exige indicar la naturaleza de la magnitud y el valor de referencia empleado c) equivale a 10 belios d) es unidad de presión | b) | Entera: «El decibelio, y por qué siempre necesita una referencia» (apartado 4 y nota (i); 1 dB = 1/10 B) |
| 6 | Fase (práctica) | Dos micrófonos captan la misma fuente con 1 ms de diferencia. ¿A qué frecuencia quedan en contrafase? a) 250 Hz b) 500 Hz c) 1 kHz d) 2 kHz | b) | Entera: «Un mismo retardo, un desfase distinto en cada frecuencia» |
| 7 | Audición | Las curvas que representan la sensibilidad del oído a las distintas frecuencias en todo el margen audible son: a) las curvas NC b) las curvas NR c) las curvas isofónicas d) la curva de ponderación C | c) | Entera: «Cómo oímos: las curvas isofónicas» (NC y NR describen ruido de fondo de sala) |
| 8 | Fase (práctica) | Para evitar el filtro en peine entre dos micrófonos iguales con la misma ganancia, la regla 3:1 pide que: a) el vecino esté al menos a tres veces la distancia de la fuente a su micrófono b) haya tres micrófonos por fuente c) el retardo sea de 3 ms d) la ganancia baje 3 dB | a) | Entera: «Interferencia y filtro en peine» (tabla de remedios, 3:1 ≈ −10 dB) |
| 9 | Dinámica | El margen dinámico teórico de una cuantificación de 24 bits es de unos: a) 96 dB b) 120 dB c) 144 dB d) 24 dB | c) | Entera: «El margen dinámico de un equipo» (6,02 dB por bit) |
| 10 | Acústica básica | ¿Qué superficies favorecen en mayor medida las ondas estacionarias en una sala? a) las curvas b) las paralelas c) las absorbentes d) las irregulares | b) | Entera: «Los modos propios y las ondas estacionarias» (y por qué no se corrigen ecualizando) |

Comprobación adicional de lo que las diez dejan fuera: el hercio en el RD 2032/2009 («sólo se
utiliza para los fenómenos periódicos», «El hercio, unidad legal»); polaridad frente a fase (DPA,
«Polaridad no es fase»); enmascaramiento; RT60 como caída de 60 dB. Las diez, repartidas por las
ocho rúbricas (ondas 1; frecuencia 1; amplitud 2; fase 2; dinámica 1; timbre 1; audición 1;
acústica 1; cuatro de aplicación práctica o cálculo), se contestan enteras con el tema; no ha hecho
falta ampliar.
