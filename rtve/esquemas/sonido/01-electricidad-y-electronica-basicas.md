# Esquema · Tema 1 del específico de Sonido · Electricidad y electrónica básicas

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = norma del Boletín Oficial del Estado ·
`[of]` = oficio y electrónica básica · `[plan]` = plantilla oficial. **Siglas**: la distorsión armónica
total (**THD**, *total harmonic distortion*) y las clases de amplificador, que se nombran por letra
(**A**, **B**, **AB** y **C**).

**Cabecera.** Enunciados: puntos 1.1 y 1.2 del anexo, «Conocimientos básicos: electricidad y electrónica básica aplicada a la captación y tratamiento del sonido» · **12 preguntas: el banco más
grande de la ocupación** · **cuatro son cálculo, cuatro son definición y cuatro son electrónica de
amplificación.**

<!-- indice -->

## Índice

- [Las unidades son legales](#las-unidades-son-legales)
- [La ley de Ohm](#la-ley-de-ohm)
- [La impedancia](#la-impedancia)
- [Altavoces en paralelo](#altavoces-en-paralelo)
- [Por qué la impedancia baja hace perder corriente en el cable](#por-qué-la-impedancia-baja-hace-perder-corriente-en-el-cable)
- [El diferencial](#el-diferencial)
- [La red y los amplificadores](#la-red-y-los-amplificadores)
- [Las distorsiones](#las-distorsiones)
- [La medida y la trigonometría](#la-medida-y-la-trigonometría)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las unidades son legales

- `[BOE]` · **El voltio, el ohmio y el faradio están en el Real Decreto 2032/2009**, de unidades
  legales de medida. **No son convenio del oficio: son derecho vigente.**
- **La regla que este tema deja para todo el proyecto**: **antes de dar una materia técnica por
  «oficio», hay que preguntarse si sus magnitudes tienen unidad legal.**

## La ley de Ohm

- **PREGUNTA 74** · `[of]` · **La ley de Ohm describe la relación entre tensión, corriente y
  resistencia en un circuito eléctrico.**
- **PREGUNTA 11** · `[of]` · **5 ohmios con 3 amperios piden 15 voltios.** **V = I × R. 5 × 3 = 15.**
- **CÓMO SE DESCARTAN LAS FALSAS**: **dos opciones traen vatios en vez de voltios.** **La unidad de la
  respuesta ya elimina la mitad del examen.**

## La impedancia

- **PREGUNTA 35** · `[of]` · **La oposición a la corriente alterna debida a capacidad, inductancia y
  resistencia se llama impedancia.**
- **LO QUE LA DISTINGUE DE LA RESISTENCIA**: **la resistencia no depende de la frecuencia y la
  impedancia sí.**
- **«Resistancia» de la opción d no existe**: es la trampa por parecido.

## Altavoces en paralelo

- **PREGUNTA 46** · `[plan]` · **Tres altavoces de 8 ohmios en paralelo dan «lo más aproximado» a 2,5
  ohmios.**
- **LA CUENTA EXACTA ES 2,67** —ocho partido por tres—, **y la plantilla pide el valor más próximo de
  los cuatro ofrecidos.** **De 2,5 a 2,67 hay 0,17; de 4,5 a 2,67 hay 1,83.**
- **LA REGLA**: **en paralelo, la impedancia resultante es menor que la más pequeña de las que se
  asocian.** **Con eso sobran las opciones a y b, que son mayores que 8.**

## Por qué la impedancia baja hace perder corriente en el cable

- **PREGUNTA 31** · `[of]` · **Se pierde más corriente en el cable con el altavoz de 4 ohmios**, que
  es el de menor impedancia de los cuatro.
- **EL RAZONAMIENTO**: **menos impedancia, más corriente; más corriente, más caída de tensión en la
  resistencia del propio cable.**
- **CONSECUENCIA PRÁCTICA**: **cuanto más baja la impedancia del altavoz, más gruesa tiene que ser la
  sección del cable o más corta la tirada.**

## El diferencial

- **PREGUNTA 29** · `[of]` · **Un diferencial salta cuando no hay la misma intensidad entre hilos.**
- **POR QUÉ**: **compara lo que entra por la fase con lo que vuelve por el neutro**; si difieren, parte
  de la corriente se va por otro camino —tierra o persona— y abre.
- **NO CONFUNDIR**: **el diferencial protege a las personas; el magnetotérmico y el fusible protegen a
  los cables.** **Las opciones a y c —consumo excesivo y cortocircuito— son del magnetotérmico.**

## La red y los amplificadores

- **PREGUNTA 84** · `[of]` · **Las redes domésticas europeas dan corriente alterna a 230 voltios.**
- **PREGUNTA 70** · `[of]` · **Un amplificador cuya corriente de salida circula menos de un
  semiperiodo funciona en clase C.**
- **LA ESCALA DE CLASES, QUE ES LO QUE HAY QUE MEMORIZAR**: **clase A conduce el ciclo entero; clase B,
  medio ciclo; clase AB, algo más de medio; clase C, menos de medio.** **La pregunta dice «menos de un
  semiperiodo» y sólo la C cabe.**

## Las distorsiones

- **PREGUNTA 17** · `[of]` · **No poder seguir un cambio brusco y rápido —un percusivo— es distorsión
  por transitorios.**
- **PREGUNTA 67** · `[of]` · **Una distorsión armónica total del 0,1 % significa que el 0,1 % de la
  señal son armónicos que no estaban en la entrada.**
- **LA PALABRA QUE DECIDE LA 67 ES «NO PRESENTES»**: **la distorsión armónica añade lo que no había.**
  **La opción b la confunde con el ruido, que tampoco estaba pero no es armónico.**

## La medida y la trigonometría

- **PREGUNTA 82** · `[plan]` · **La herramienta fundamental para medir impedancia es el multímetro.**
- **SALVEDAD DEL TEMARIO**: **un multímetro corriente mide resistencia en continua, no impedancia**;
  **la respuesta oficial es la mejor de las cuatro ofrecidas y el temario lo declara.**
- **PREGUNTA 9** · `[of]` · **El seno de 90 grados sexagesimales es 1.**
- **POR QUÉ IMPORTA EN AUDIO**: **el seno de 90 grados es el máximo de la onda**, y de ahí sale la
  relación entre valor de pico y valor eficaz.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 9 | Cuánto vale el seno de 90 grados | c) 1 ✔ |
| 11 | Voltaje de un circuito de 5 Ω y 3 A | b) 15 V ✔ |
| 17 | Distorsión al no seguir un cambio brusco | c) Por transitorios ✔ |
| 29 | Cuándo salta un diferencial | b) No hay la misma intensidad entre hilos ✔ |
| 31 | Con qué impedancia se pierde más corriente en el cable | a) 4 ohmios ✔ |
| 35 | Cómo se llama la oposición a la corriente alterna | c) Impedancia ✔ |
| 46 | Tres altavoces de 8 Ω en paralelo | d) 2,5 ✔ **·** el valor exacto es 2,67 |
| 67 | Qué significa una THD del 0,1 % | c) El 0,1 % son armónicos no presentes en la entrada ✔ |
| 70 | Clase de un amplificador que conduce menos de medio ciclo | d) C ✔ |
| 74 | Qué describe la ley de Ohm | a) Tensión, corriente y resistencia ✔ |
| 82 | Herramienta para medir impedancia | d) Multímetro ✔ **·** con salvedad |
| 84 | Corriente de las redes domésticas europeas | b) Alterna a 230 V ✔ |

**Las doce oficiales son correctas**, **dos con salvedad declarada.** · **Aviso de estudio**: **cuatro
son cuenta y se ganan siempre**; **la escala de clases de amplificador y la de unidades legales son las
dos listas que hay que llevar memorizadas.**
