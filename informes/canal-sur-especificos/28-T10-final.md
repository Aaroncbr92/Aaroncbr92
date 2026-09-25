# Puesto 28 · Operador/a de Sonido · Tema 10 · Fase 5 bis

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/10-sonorizacion.md`. Revisados sólo los
pasajes que lista `28-T10-remate.md`. Fecha de lectura de las fuentes: 25-09-2026 (el encargo fija
«hoy» en 24-09-2026).

## Fuentes releídas

| Fuente | Dónde | Fecha |
|---|---|---|
| TI AN-1497, SNAA034A (`fuentes/canal-sur/sonido/fabricantes/ti-snaa034a.txt`) | líneas 86-98 y 147-150 | 25-09-2026 |
| Crown FAQ «Professional Power Amplifiers» (copia de texto del scratchpad, `crown.txt`; la web daba 403) | «Should I use Bridge Mono or Parallel Mono?», «How do I set up… Bridge-Mono / Parallel-Mono» | 25-09-2026 |
| Shure/Frank AL1174 (`shure-pag.txt`) | línea 303 | 25-09-2026 |

## Pasaje por pasaje

1. **Impedancia del altavoz** (resistencia en continua 4 u 8 ohmios): TI, «Speakers are characterized
   by their DC resistance, typically 4Ωor 8Ωfor loudspeakers». Correcto; la precisión distingue ya
   resistencia en continua de impedancia nominal.
2. **Clases A, B, AB y C / la D**: sin dato nuevo; antecedente de «la D» y «están en el tema 2»
   correctos. Las negritas de TI siguen literales («linear classes»).
3. **Redondeo 1,11 W / 111 mW**: 1/0,9 = 1,111 W; 1,111 − 1 = 0,111 W. Correcto; la cita literal
   «a 90% efficient amplifier at 1W output dissipates 100mW» coincide con la fuente.
4. **Modos (ampliación L1)**: las cuatro negritas son literales de la FAQ. Paráfrasis comprobadas:
   puente, 8 o 4 ohmios en Micro-Tech y Macro-Tech, «8 ohms or greater» en Power-Tech y Com-Tech;
   paralelo, «one-ohm load» en Micro/Macro-Tech, «down to two ohms» en Power/Com-Tech; número impar
   («such a three»), dos en un canal y una en el otro, las tres en paralelo. Todo correcto. «No todos
   los modelos admiten los dos modos» queda respaldado por la nota de Crown (CE, CP660, D y K no
   trabajan en paralelo mono). La regla de la línea 250 («Crown da mínimos distintos según el modelo y
   el modo») tiene ahora su dato.
   **Corrección aplicada**: «Su mayor ventaja, según Crown,» → «La mayor ventaja del paralelo mono,
   según Crown,». El «Su» podía leerse referido al puente o a Crown; la fuente dice «The biggest
   advantage of using Parallel Mono».
5. **«arc [sic: are]»**: línea 303 de la fuente dice «arc far apart». Correcto.
6. **Trazabilidad**: filas de Crown, TI y Shure cuadran con lo que el cuerpo usa.
7. **Ficha**: `indice.py` da 7.991 palabras (tras la corrección, +3); «8.000 aproximadamente» vale.

## Lentes

`indice.py`: 45 epígrafes. `refutar_prosa.py`: 2 avisos, los mismos falsos positivos del remate
(AB, nombre de clase; «NOW», errata señalada).

## Resultado

Un cambio de antecedente; ningún dato erróneo. Queda el hueco declarado de Linkwitz-Riley
(pregunta 15) y el aviso del remate sobre el tema 2, línea 199, fuera de este tema.

## Otros ficheros tocados

Sólo el tema 10 y este informe.
