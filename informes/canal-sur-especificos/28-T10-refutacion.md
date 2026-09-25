# Puesto 28 · Operador/a de Sonido · Tema 10 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/10-sonorizacion.md`. Fecha de trabajo y
de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). No corrijo: señalo.

Exactitud: salto lo listado en `28-T10-redaccion.md` como «Copiado de RTVE sin cambios» (nueve
bloques; «Copiado del común»: ninguno). Cobertura: el tema entero contra el enunciado.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| Shure/Frank, AL1174 (`fuentes/canal-sur/sonido/fabricantes/shure-pag.txt`) | líneas 28-349: todas las citas y cifras (NAG 70/49/21; PAG 20, 22, 16, 24; NOM; peor caso; 6 dB; DS; techo; ecos tardíos) | conforme, con la observación 4 |
| Ureda, JAES 2004 (`line-array-theory.txt`) | líneas 1-125 y 477-510 | conforme (Klepper y Steele 1963; −3/−6 dB; 4 m, 8 kHz, 100 m; arcos) |
| TI AN-1497 (`ti-snaa034a.txt`) | líneas 80-160 | hallazgos 1 y 3 |
| Shure, guía de antenas (`shure-antenna.txt`) | líneas 460-525 | conforme (IEM en rack; 4 a 8; no encadenar; 3 dB en varias salas) |
| Crown FAQ (copia de texto guardada por la verificación el 25-09-2026; hoy la web responde 403) | todas las citas | literales; laguna de cobertura (L1) |
| Temas 1, 2, 3 y 5 del puesto (remisiones) | grep | remisiones correctas (DPA en el tema 3; lazo en el 5; 340 m/s y 50 ms en el 1) |

Cálculos rehechos: 68 Hz / 5 m; 2 kHz / 17 cm; 97 + 26 = 123 → 93 dB a 32 m; ×4 = +6 dB; 38 − 4 =
34 → 100 ms; PAG 19 − 26 + 27 = 20; 22; 16; 24; 24 − 3 = 21; 25 pies = 7,62 m. Todos bien.

## Hallazgos de exactitud

**Graves: 0.**

**Menores: 3.**

1. **Error 9/6 · línea 248** («su impedancia nominal decide cuánta corriente pide (TI da como típicos
   de los altavoces 4 u 8 ohmios)»). TI habla de resistencia en continua, no de impedancia nominal:
   «Speakers are characterized by their DC resistance, typically 4Ωor 8Ωfor loudspeakers» (TI,
   líneas 149-150). Propuesta: «TI da como típica de los altavoces una resistencia en continua de 4 u
   8 ohmios» o volver la cifra a oficio.
2. **Terminología · línea 257** («Sus clases lineales (A, B, AB y C)»). La clase C no es lineal (el
   propio tema 2 dice que no sirve para audio por su distorsión); TI opone «linear classes» a la
   conmutada sin incluir la C. Propuesta: «Las clases A, B, AB y C se definen por qué parte del ciclo
   conduce…». (El tema 2, línea 199, llama a la C «la más alta de las lineales»: aviso fuera de mi
   tema, sin tocar.)
3. **Error 6 (salvedad de cálculo) · línea 262**. La cita de TI «a 90% efficient amplifier at 1W
   output dissipates 100mW» es literal, pero redondeada: con 1 W de salida al 90 % entran 1,11 W y se
   disipan unos 111 mW. El tema ya añade la salvedad análoga a Crown (1,4 V / +4 dBu); por coherencia,
   aquí también. Menor.

**Observaciones (no cuentan):**

4. Línea 463: la cita de Shure dice «are far apart»; la fuente trae «arc far apart» (errata de
   escaneo). Corregirla en silencio dentro de una negrita literal es aceptable, pero el tema sí
   señala las otras dos erratas («NOW», «11 dB»); podría añadirse «[sic: arc]» o dejarse.
5. Líneas 559-560: Shure da también «using only one microphone and passing it around» y dice que
   las tres primeras vías tienen inconvenientes prácticos; y describe un tercer tipo de mezclador
   automático (el que detecta la dirección de la fuente). El tema no falsea, sólo resume.
6. Línea 371 («la pregunta mide»): sabor RTVE en bloque literal, ya avisado por la verificación.

## Cobertura del enunciado

«Sonorización: altavoces, amplificadores, PA, monitores, cobertura, realimentación y acústica de
salas.» Las ocho rúbricas tienen epígrafe, en el orden del enunciado. 15 preguntas en
`28-T10-preguntas.md`: **13 enteras, 0 a medias, 2 no**.

- **L1 · Laguna (pregunta 7).** El tema dice cómo se conectan el puente mono y el paralelo mono, pero
  no cuándo se usa cada uno, que es lo que se pregunta en práctica. La fuente ya citada lo da: Crown,
  «Should I use Bridge Mono or Parallel Mono?»: «the deciding factor to this dilemma is the total
  speaker load impedance»; puente «when driving 8 or 4-ohm loads», «Parallel Mono can be used when
  driving lower impedance loads» (hasta 1 ohmio en Micro-Tech/Macro-Tech, 2 en Power-Tech/Com-Tech), y
  su ventaja con un número impar de cajas. Ampliar «Los modos de funcionamiento» con dos o tres
  líneas (Opus, por ser ampliación).
- **Pregunta 15 (Linkwitz-Riley de cuarto orden, 24 dB/octava):** hueco ya declarado en «Lo que este
  tema no da». No lo cuento como laguna; se amplía sólo si se lee una fuente (nota de fabricante o
  AES).

## Lentes

Tema técnico sin norma: `negritas.py` y `refutar_*` de normas no aplican. No he pasado
`refutar_prosa.py` ni `indice.py` de nuevo (la verificación los pasó sin cambios de epígrafes y no he
tocado el tema).

## Otros ficheros tocados

`informes/canal-sur-especificos/28-T10-preguntas.md` y este informe. En el scratchpad, un intento de
descarga de la FAQ de Crown sobrescribió `crown.html` con una página 403; la copia de texto
`crown.txt` de la verificación sigue intacta y es la que se usó.

## Sobre el porcentaje de RTVE

La redacción ya lo avisó: la tabla de reuso da el 85 % y lo realmente copiado literal es en torno a
una sexta parte del cuerpo; el tema no ha sido rápido por eso (cuatro rúbricas salieron de fuentes
nuevas).

## Resumen

Graves 0 · menores 3 · lagunas 1 (más un hueco declarado).
