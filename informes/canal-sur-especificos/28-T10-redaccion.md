# Puesto 28 · Operador/a de Sonido · Tema 10 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/10-sonorizacion.md` (7.510 palabras según
`indice.py`, contando ficha, siglas y trazabilidad; 8 rúbricas `##` en el orden del enunciado
—Sonorización, Altavoces, Amplificadores, PA, Monitores, Cobertura, Realimentación, Acústica de
salas—, 35 epígrafes `###`).

Material usado: `informes/canal-sur-especificos/28-investigacion-C-conexiones-ip-rf.md` (§§ 10.1 a
10.5 y § 12.3); RTVE `temas/sonido/10-sonorizacion-altavoces-y-amplificadores.md` y
`temas/sonido/04-acustica-arquitectonica.md`. Releídos hoy en su volcado, para completar citas que la
investigación resumía: Shure/Frank (`fuentes/canal-sur/sonido/fabricantes/shure-pag.txt`: ejemplos de
PAG, peor caso, límite de 6 dB de lo direccional, ecos tempranos y techo, varios altavoces como ecos
tardíos, estimación de la distancia crítica), Ureda (`line-array-theory.txt`: columnas, guías de onda,
recta frente a arco) y la guía de antenas de Shure (`shure-antenna.txt`: combinación de antenas de
monitores personales, 4 a 8 transmisores, no encadenar activos). Crown y TI, sólo a través de la
investigación (Crown no tiene volcado). Consultados para no repetir y remitir: temas 1, 2, 3 y 5 del
puesto 28 (en curso, no copiados).

El tema no cita ninguna norma legal.

## Aviso al coordinador: el porcentaje de RTVE

El usuario habla de un 75 % de RTVE; la tabla de reuso (`28-args.json`, tema 10) y el encargo dicen
**85 %**. Lo copiado literal de RTVE es en realidad en torno a una sexta parte del cuerpo (unas 1.200
de 7.500 palabras). Motivos: el RTVE 10 tiene 2.450 palabras, un tercio dedicadas a comentar
preguntas de su examen (quitado); la acústica de salas del RTVE 04 ya está entera en el tema 1 de este
puesto (aquí sólo se recoge lo que decide la sonorización y se remite); y cuatro rúbricas del
enunciado (amplificadores, PA, monitores, cobertura) y la ganancia antes de realimentación apenas
estaban en RTVE y salen de la investigación.

## Qué se quitó por propio de RTVE o sin fuente

- Todas las referencias a preguntas y respuestas oficiales del examen RTVE (13, 14, 38, 60, 66 y 88
  del RTVE 10; 33 del RTVE 04), las marcas ✔, la tabla de opciones a/b/c/d de la pregunta 60 y los
  epígrafes «Los datos que el examen ha preguntado»; también el reparto de preguntas de la entrada.
- RTVE 10 § 1: las «tres opciones falsas» se reconvierten en «tres ideas equivocadas»; se quita
  «Confunde ligereza del imán con debilidad del campo».
- RTVE 10 § 2: «Las tres opciones falsas son unidades eléctricas…» reducido a una frase sobre la
  capacidad en faradios.
- RTVE 10 § 4: el párrafo de las «tres opciones falsas» (10 vatios, potencia acústica, distorsión).
- RTVE 10 § 5: el párrafo de opciones falsas (mezclador, limpiador de voz, conversor).
- RTVE 10 § 6: «es el efecto de precedencia del tema 4» → «Es el efecto de precedencia, que se da
  como oficio».
- RTVE 10 § 7: la entrada sobre el filtro notch «del tema 7»; remisiones a temas de RTVE («tema 1»,
  «tema 2», «tema 5») cambiadas a los temas de este puesto.
- RTVE 04: los valores de RT60 por uso, la fórmula de Sabine y la tabla palabra/música no se copian
  (están en el tema 1 del puesto); se resumen y remiten.
- No se ha copiado ninguna afirmación de RTVE que la investigación marcara como errónea (no había
  correcciones para el RTVE 10 ni el 04).

## Copiado del común

Ninguno. No hay tema cerrado de Canal Sur sobre sonorización (el tema 6 de Cámara Operador sólo toca
la captación).

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra; **sólo se ha quitado la negrita** (en RTVE era
énfasis y aquí negrita = literal de fuente) y la marca ✔. Ninguno cita norma. Los dos temas RTVE
están marcados «actualizar: no». Comprobado por script: cada párrafo, fila o elemento de lista, sin
`**` ni ✔ y con los espacios normalizados, es subcadena del RTVE.

De `temas/sonido/10-sonorizacion-altavoces-y-amplificadores.md`:
1. «El altavoz electrodinámico»: las cinco filas de la tabla de piezas (con su cabecera) (§ 1).
2. «La caja acústica»: la tabla de tres tipos de caja con su cabecera (§ 2).
3. «La directividad»: los tres puntos «Los graves sean…», «Los agudos sean…», «La bocina exista…»
   (§ 3).
4. «La sensibilidad»: el párrafo «Una sensibilidad de 90 dB/W/m significa…», el párrafo «La
   especificación tiene tres partes…», la tabla de tres cambios con su cabecera y el párrafo «Con ella
   se entiende… doblar la etapa.» (§ 4).
5. «El filtro de cruce»: el párrafo «Qué hace un filtro de cruce… diez octavas del margen audible.»,
   la frase «Y el filtro de cruce puede estar en dos sitios…» y la tabla pasivo/activo con su cabecera
   (§ 5).
6. «Los refuerzos y la alineación temporal»: los dos pasos de la cuenta (38 − 4 = 34; 34 ÷ 340), el
   párrafo «Y la parte que la pregunta mide de verdad… lo empeoraría.» y el párrafo «El atajo que
   conviene tener… unos 100 milisegundos.» (§ 6).
7. «Las cinco maneras de ganar margen»: los puntos 1, 3, 4 y 5 de la lista (§ 7).

De `temas/sonido/04-acustica-arquitectonica.md`:
8. «Lo que la sala añade al sistema»: la tabla de tres componentes con su cabecera (§ 1).
9. «Lo que la sala le manda al técnico de sonorización»: la cabecera y las cuatro primeras filas de
   la tabla (§ 5).

**Adaptado de RTVE (sí se verifica):** el párrafo de la fidelidad (sin «pregunta 88» ni «Ésa es la
respuesta oficial»); las tres ideas equivocadas; el párrafo de la caja en litros; la entrada de la
directividad y su regla; el párrafo del Linkwitz-Riley; el párrafo de los refuerzos a mitad de sala;
la presentación de la cuenta de 4 y 38 m; la definición del acople; la frase de entrada y el punto 2
de las cinco maneras («los nulos del tema 3»); «El orden importa…» (con frase añadida sobre Shure); la
frontera de los 50 ms (con la declaración de oficio); el RT60; la frase de las paralelas, el «No se
corrigen ecualizando…» y «Se corrige con trampas…» (con el subgrave); las salas polivalentes; la
última fila de la tabla de la sala (acople → PAG con 6 dB); «La sala es parte de la cadena de audio…».

## Nuevo (se verifica entero)

- Shure/Frank: la regla de campo libre; ley del cuadrado inverso (cita, fórmula, campo libre, fuente
  puntual, doblar o mitad); escala 1/3/10 dB; varios altavoces como ecos tardíos; distancia crítica
  (definición, validez de la ley, estimación con radio de FM y 3 dB); DS única distancia dentro de la
  crítica; NAG y su ejemplo; tabla de las cuatro distancias; PAG, supuestos, ejemplos (20, 22, 16, 24
  dB); margen de 6 dB; NOM (3 dB por duplicación; erratas «NOW» y «11 dB» señaladas en el tema);
  mezclador automático; peor caso; límite práctico de 6 dB; DS y +6 dB; ecos tempranos y techo.
- Ureda: columnas y cita de 1963; guías de onda; tabla campo cercano / transición / lejano; ejemplo de
  4 m, 8 kHz, 100 m; formas; rectas estrechas y arcos más anchos.
- Crown: sensibilidad de entrada; puente mono y paralelo mono; Speakon NL4FC; factor de
  amortiguamiento, «boomy» y realimentación negativa; calibre del cable.
- TI: rendimiento AB y D; 90 % y 100 mW; PWM.
- Shure antenas: combinación en IEM, intermodulación, pasivo/activo, 4 a 8, no encadenar, 3 dB.
- Cálculos: 68 Hz y 17 cm; 25 pies ≈ 7,6 m; 10 dB = ×10 de potencia; ejemplo 97 dB/W/m, 400 W,
  123 dB a 1 m y ~93 dB a 32 m; 1.600 W para +6 dB; 24 − 3 = 21.
- Oficio declarado: cadena de sonorización; impedancias habituales y carga mínima de la etapa; qué es
  la PA y sus partes; campo cercano del array como ventaja de uniformidad; cuñas e IEM como familias;
  mezcla de monitores por auxiliares; cuña en el nulo; lo que la reverberación hace al sistema;
  subgrave y modos.

## Avisos para verificación

- Crown: página web sin volcado; las citas vienen de la investigación. Cotejarlas en
  https://www.crownaudio.com/en-US/faq_categories/1. En particular, la cita del paralelo mono está
  reconstruida de la investigación («puente entre las dos salidas rojas» va en redonda, no como cita).
- Crown da 1,4 V = +4 dBu; por cálculo, 1,4 V son unos +5,1 dBu (20 log (1,4/0,775)). El tema cita al
  fabricante tal cual y no hace la cuenta; el verificador decide si se añade la salvedad.
- Ureda: el tema dice que en campo lejano cae 6 dB «como una fuente puntual»; la comparación es
  inferencia del redactor, no frase de la fuente.
- Shure, «A passive combiner will typically result in at least 3 dB of loss»: en la fuente va en el
  apartado de antenas para varias salas; el tema la presenta como dato general del pasivo.
- «4, 8 o 16 ohmios, las habituales»: oficio sin fuente leída en esta fase.
- «Se dispara a la frecuencia en la que la ganancia del lazo llega primero a uno»: tomado del tema 5
  del puesto (oficio).

## Huecos declarados (en el tema, «Lo que este tema no da»)

Normas de medida de altavoces, etapas y salas; cobertura angular de cajas y diseño de arrays;
fórmula de la distancia de transición; cuñas y mezcla de monitores con fuente; monitores del control;
procesadores de sistema y supresores de realimentación; pendientes del Linkwitz-Riley; todo lo propio
de CSRTV.

## Lentes

`indice.py`: índice generado (no hay fila en `portadas.tsv`; la extensión de la ficha se puso a mano
con la cifra de `indice.py`). `refutar_prosa.py`: 1 hallazgo que se deja («NOW», errata literal de la
fuente, explicada en el propio párrafo); los otros dos (FM, NC) se corrigieron presentándolas en las
siglas.

## Otros ficheros tocados

Ninguno fuera del tema y este informe.

## Preguntas tipo test de comprobación (10)

| # | Rúbrica | Pregunta | Respuesta | ¿La contesta el tema? |
|---|---|---|---|---|
| 1 | Altavoces | La capacidad de una caja acústica se mide en: a) faradios b) litros c) microfaradios d) vatios | b) | Entera: «La caja acústica» (volumen de aire; la trampa de «capacidad») |
| 2 | Altavoces (práctica) | Un altavoz de 93 dB/W/m con 100 W da el mismo nivel que uno de 90 dB/W/m con: a) 50 W b) 100 W c) 200 W d) 400 W | c) | Entera: «La sensibilidad» (tabla y ejemplo literal) |
| 3 | Altavoces / sonorización | En un sistema de refuerzo profesional con cruce activo, el filtro de cruce está: a) dentro de la caja, tras la etapa b) antes de las etapas, con una etapa por vía c) en el micrófono d) en la mesa de monitores | b) | Entera: «El filtro de cruce» (tabla pasivo/activo; Linkwitz-Riley) |
| 4 | Amplificadores | La clase de etapa de mayor rendimiento, que conmuta y da una salida PWM, es: a) A b) AB c) C d) D | d) | Entera: «La etapa de potencia y sus clases» (AB 78 % teórico, 30-40 % real; D) |
| 5 | Amplificadores | En una etapa Crown, la posición de sensibilidad de 0,775 V corresponde a: a) −10 dBV b) 0 dBu c) +4 dBu d) ganancia fija de 26 dB | b) | Entera: «La sensibilidad de entrada» |
| 6 | PA (práctica) | Dos altavoces a 4 y 38 m de un oyente (340 m/s). Para alinearlos: a) 40 ms al lejano b) 100 ms al cercano c) 120 ms al cercano d) 50 ms al lejano | b) | Entera: «Los refuerzos y la alineación temporal» (cuenta, a cuál y atajo de 3 ms/m) |
| 7 | Monitores | Para combinar más de dos transmisores de monitores intrauriculares en una antena, Shure recomienda: a) un combinador pasivo b) un combinador activo c) dos activos en cascada d) una antena por transmisor | b) | Entera: «Los transmisores de monitores intrauriculares» (pasivo para dos, activo para más, no encadenar activos) |
| 8 | Cobertura (práctica) | En campo libre, un altavoz de 97 dB/W/m con 400 W da a 32 m aproximadamente: a) 123 dB b) 111 dB c) 93 dB d) 73 dB | c) | Entera: «El nivel que da un altavoz en el público» (fórmula y ejemplo) y «La ley del cuadrado inverso» |
| 9 | Realimentación (práctica) | Un sistema tiene una PAG de 24 dB con un micrófono abierto. Si se abren cuatro, la PAG queda en: a) 24 dB b) 21 dB c) 18 dB d) 12 dB | c) | Entera: «Los micrófonos abiertos (NOM)» (10 log NOM; 3 dB por duplicación) |
| 10 | Acústica de salas / cobertura | La distancia crítica es aquella a la que: a) el sistema empieza a acoplar b) el sonido directo iguala al reverberante c) el array pasa de −3 a −6 dB d) la primera reflexión llega a 50 ms | b) | Entera: «La distancia crítica» (definición, estimación con 3 dB) y «La reverberación y el sistema» |

Las diez, repartidas por las ocho rúbricas (la de «Sonorización» a través de las 3 y 8), se
contestan enteras con el tema; cuatro son de cálculo o aplicación (2, 6, 8, 9). Comprobación
adicional de lo que dejan fuera: margen de estabilidad de 6 dB; DS como distancia que más rinde
(+6 dB al reducirla a la mitad); orden de las cinco maneras contra el acople; NAG de 21 dB del ejemplo;
array lineal a −3 dB en campo cercano y distancia de transición; superficies paralelas y ondas
estacionarias; graves omnidireccionales y agudos direccionales; araña sin contacto; factor de
amortiguamiento; puente mono; efecto de los ecos tempranos. Todo está en el tema; no ha hecho falta
ampliar.
