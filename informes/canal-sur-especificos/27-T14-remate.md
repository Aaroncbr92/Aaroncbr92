# Remate · Oficial Técnico Electricista (27) · Tema 14 · Medidas eléctricas e instrumentación

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/14-medidas-electricas-e-instrumentacion.md`.
Base: `27-T14-refutacion.md` (2 menores, 2 lagunas) y `27-T14-preguntas.md`. Fuentes leídas el
05-10-2026 (reloj del sistema; el encargo fija «hoy» en el 24-09-2026: ninguna de las fuentes
técnicas añadidas tiene fecha posterior).

**Resultado: se amplió contenido nuevo (amplio = true). Toca fase 5 bis sobre 1.3, 3.5, 5.7 y 6.2.**

## Correcciones (comprobadas en la fuente antes de aplicarlas)

| Id | Comprobación | Aplicada |
|---|---|---|
| M1 | INSST 2020, pp. 33-35: «Antes de utilizar un detector de tensión, es importante comprobar su tensión o gama…» está en «Verificación de la ausencia de tensión en instalaciones de alta tensión», tras UNE-EN 61243-1 y -2; el apartado de baja tensión (p. 35) no la repite. La p. 33 dice «es obligatorio comprobar… antes y después» en AT y «También es recomendable» en BT. El informe acertó | Sí, epígrafe 1.3 |
| M2 | El 3.2 del tema distingue pinza de transformador y de efecto Hall. El informe acertó | Sí, epígrafe 3.5 |

## Lagunas (se amplía el tema; las preguntas no se tocan)

| Id | Fuente nueva | Ampliación |
|---|---|---|
| L1 (pregunta 12) | Megger, *Una puntada a tiempo. Guía completa para pruebas de aislamiento eléctrico*, ed. española (copyright 2006/2017), pp. 10-15 y 64 | Nuevo epígrafe 5.7: tres tipos de prueba, método tiempo-resistencia, definiciones literales de DAR (60 s/30 s) e índice de polarización (10 min/1 min), tabla I traducida (la edición española la deja en inglés) con sus tres notas, prueba de doble lectura, aplicación de oficio. La respuesta b de la pregunta 12 queda confirmada |
| L2 (pregunta 14) | Circutor, manual CVM-NRG96 (M98245001-01-13A), apartado 1.11; Fluke, nota de aplicación Pub-ID 10562-es (2002), pp. 2-3 | En 6.2: THD con sus dos cálculos (respecto a la fundamental y al valor eficaz), factor de cresta (pico/rms, 1,4 en senoidal, 2 en cargas de oficina), factor de desclasificación HDF como regla general del fabricante, neutro al 80-130 % con armónicos de orden 3 y 150 Hz. La respuesta c de la pregunta 14 queda confirmada |
| Hueco declarado (pregunta 15) | No se buscó tabla de prioridad por ΔT | Sigue declarado en «Lo que este tema no da» |

La nota de Fluke cita la ITC-BT-19 (sección del neutro): no se ha tomado; el tema no la usa desde ahí.

## Pasajes cambiados

1. Ficha: «Fuente» añade Megger; «Extensión» pasa a unas 14.500 palabras.
2. Siglas: THD, CF, IP, DAR; fabricantes (se añade Megger y el modelo CVM-NRG96).
3. «Qué se puede preguntar»: añade THD, factor de cresta, DAR e índice de polarización.
4. Epígrafe 1.3, párrafo del detector (M1): la frase sobre comprobar la gama, puntas y pilas se
   atribuye al apartado de alta tensión; se añade la comprobación del verificador antes y después,
   **obligatoria** en AT y **recomendable** en BT; «Y que la verificación…» pasa a «La guía pide además
   que la verificación…» (antecedente explícito).
5. Epígrafe 3.5 (M2): «La pinza de alterna es, por dentro, un transformador de intensidad».
6. Epígrafe 5.7 nuevo (L1), entero.
7. Epígrafe 6.2 (L2): lista de THD y factor de cresta y párrafo de la corriente de neutro.
8. «Trazabilidad»: tres filas nuevas (Megger, Circutor CVM-NRG96, Fluke 10562-es) y la fila del
   INSST amplía lo tomado; la lista de oficio añade dos lecturas de aplicación.
9. Índice regenerado.

Relectura de los pasajes: cada «la guía», «la misma nota», «la tercera nota», «5.2» tiene su
antecedente delante.

## Lentes

- `indice.py`: 14.445 palabras, 45 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` contra REBT, RD 614/2001 y las ocho fuentes técnicas: 212 negritas, 10 «no está»:
  las 8 ya explicadas en la refutación y las 2 nuevas del INSST (1.3), que son literales al quitar
  el guion blando U+00AD (comprobado; en la segunda, «También» pasa a minúscula). Las del 5.7 y 6.2,
  todas encontradas tras retirar de la negrita una enumeración con «tiempo-resistencia» (cortado
  en el PDF) y dos rótulos de lista.
- `refutar_exactitud.py` y `refutar_modo.py`: no se corren; ningún pasaje cambiado cita norma.

## Ficheros tocados

El tema; este informe; fuentes nuevas en `fuentes/canal-sur/tecnica/`:
`megger-guia-pruebas-aislamiento.{pdf,txt}`, `circutor-cvm-nrg96-M98245001-01.{pdf,txt}`,
`fluke-nota-aplicacion-gen03.{pdf,txt}`.
