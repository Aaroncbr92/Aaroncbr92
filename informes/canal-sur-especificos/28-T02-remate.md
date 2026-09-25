# Puesto 28 · Operador/a de Sonido · Tema 2 · Fase 5, remate

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/02-electricidad-y-electronica-aplicada-al-audio.md`.
Entrada: `28-T02-refutacion.md` (1 grave, 3 menores, 2 lagunas) y `28-T02-preguntas.md`.

**Resultado: el remate AMPLÍA contenido nuevo** (dos párrafos con fuente: CMRR en 4.2 y masa en
estrella en 5.2). Toca fase 5 bis sobre los pasajes listados abajo. De unas 8.500 a unas 9.000 palabras.

## Fuentes (leídas el 25-09-2026, con curl)

| Fuente | Copia local | Qué sostiene |
|---|---|---|
| DPA, Mic University, «Electromagnetic interference: EMC, RFI immunity and CMRR» | `fuentes/canal-sur/sonido/fabricantes/dpa-emc-rfi-cmrr.txt` (ya extractada en `fuentes/fabricantes/DPA_mic-university_extractos.txt`) | Definición de CMRR; impedancias iguales pin 2/pin 3; eslabón más débil; más es mejor; 65 dB, menos de una milésima; sigla EMI |
| Rane, RaneNote 151 «Grounding and Shielding Audio Devices» | `fuentes/canal-sur/sonido/fabricantes/rane-note151.txt` | Masa en estrella; unión señal-chasis en un solo punto; dos escuelas (fuente de alimentación / masa del conector de entrada) |

Las diez negritas nuevas se cotejaron literalmente contra esas copias (todas presentes).

## Hallazgos de exactitud

1. **Grave, Crown 1,4 V / +4 dBu**: comprobado por cálculo (0,775 × 10^(4/20) = 1,228 V; 1,4 V =
   +5,14 dBu). **Aplicado**: se mantiene la cita literal y se añade tras ella: «Ojo con la segunda
   cifra, que es la del fabricante y no la de la escala: con la definición del epígrafe 2.1, +4 dBu son
   0,775 × 10^(4/20) ≈ 1,23 V eficaces (cálculo), y 1,4 V quedan algo por encima, en unos +5 dBu. Si se
   pregunta a cuántos voltios equivale +4 dBu, la respuesta es 1,23 V.»
2. **Clase C «el más alto de las lineales»**: **aplicado**. Fila C: «Más alto que A, B y AB».
3. **Siglas EBU, MADI, Dante**: **aplicado**, con la redacción ya usada en los temas hermanos del
   puesto. Añadidas también EMI y CMRR, que traen los pasajes nuevos.
4. **Remisión de la DI a 5.3**: **aplicado**. 3.2 dice ahora: «la que lleva transformador es además la
   forma habitual del aislamiento de los epígrafes 4.4 y 5.3» (4.4 une la DI al transformador; 5.3
   trata el transformador de aislamiento).

## Lagunas: ampliadas

| Pregunta | Dónde | Pasaje |
|---|---|---|
| 11 (CMRR) | 4.2, párrafo nuevo antes de «De ahí las consecuencias» | «La capacidad de una entrada balanceada para rechazar lo que llega igual a los dos conductores se mide con la relación de rechazo en modo común (CMRR)…», con cinco citas DPA |
| 12 (masa en estrella) | 5.2, párrafo nuevo tras el del problema del pin 1 | «Dentro de cada equipo, la misma nota de Rane pide…», cinco citas RaneNote 151 |

La refutación decía que el CMRR no estaba en fuente a mano: sí lo estaba en DPA (página releída).
Con el remate, las preguntas 3, 11 y 12 quedan enteras. Las 4 y 15 siguen a medias / no por huecos ya
declarados (sin fuente nueva).

## Otros pasajes cambiados

- Portada: «Fuente» (DPA también para el CMRR) y «Extensión» (9.000).
- Siglas: EMI, CMRR, EBU, MADI; frase sobre Dante.
- «Qué se puede preguntar»: CMRR y masa en estrella.
- «Trazabilidad»: fila RaneNote 151 (masa en estrella, punto único) y fila DPA (página CMRR).
- «Lo que este tema no da»: sin cambios.

Antecedentes releídos: «la misma nota de Rane» sigue a la cita de la RaneNote 151; «epígrafe 2.1»
define el dBu; 4.4 y 5.3 existen y tratan lo remitido.

## Lentes

`indice.py`: sin cambios de epígrafes (39). `refutar_prosa.py`: 0 hallazgos. Sin normas nuevas: no
tocan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py` (cotejo literal hecho a mano).

## Otros ficheros tocados

Copias de fuente nuevas: `fuentes/canal-sur/sonido/fabricantes/dpa-emc-rfi-cmrr.txt` y `rane-note151.txt`.
