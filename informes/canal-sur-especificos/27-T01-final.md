# Puesto 27 · Oficial Técnico Electricista · Tema 1 · Fase 5 bis, revisión del remate

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026). Revisados sólo los pasajes que
lista `27-T01-remate.md` (hallazgos 1-3, ampliaciones 4-8 y arrastres de portada, «Qué se puede
preguntar», Normativa y Trazabilidad), sobre el `git diff` del tema.
Ficheros tocados: el tema 01 y este informe.

## Fuentes releídas

| Fuente | Fecha de lectura | Resultado |
|---|---|---|
| RD 842/2002, BOE consolidado (volcado `fuentes/canal-sur/BOE-A-2002-18099.md`), ITC-BT-48, apartado 2.3 «Condensadores», 1 redacción (desde 18-09-2003) | 05-10-2026 | Cita del tema literal, los cinco párrafos (50 ºC, carga residual, 2.000 m, UNE-EN 60.831-1, 1,3 veces, 1,5 a 1,8 veces) |
| Mismo volcado, ITC-BT-09, apartado 3 «DIMENSIONAMIENTO DE LAS INSTALACIONES», 1 redacción | 05-10-2026 | Párrafos 1 y 2 literales; el párrafo 3 confirma el ≥ 0,90 por punto de luz (alumbrado exterior obligatorio, pasaje 2) |
| Mismo volcado, ITC-BT-44, apartado 3.1 | 05-10-2026 | Obligación para receptores con lámparas de descarga y coeficiente diferente: «como la ITC-BT-44» se sostiene |

## Comprobaciones

- Cálculos rehechos: Boucherot P 15 kW, Q 7,5 kvar, S 16,77 ≈ 16,8 kVA, fp 0,894 ≈ 0,89; suma
  aritmética 12,5 + 5 = 17,5 kVA. Capacidad: 5.800 / (3 · 400² · 314,16) = 38,5 µF; en estrella,
  115,4 µF (con 230 V exactos, 116 µF): «unos 115 µF» y «el triple» correctos. Kirchhoff: 8 A y
  224 V correctos.
- Antecedentes: «la batería de 5,8 kvar del ejemplo» (6.2, Qc ≈ 5,8 kvar), «epígrafe 3.2» (define
  ω), «epígrafe 8.2» (suma vectorial en el neutro), «epígrafe 8.3» (armónicos), «Ese 1,5 a 1,8»,
  «El mismo 1,8», «El mismo apartado»: todos existen y están delante o donde se remite.
- Hallazgos 1-3 del remate: aplicados como dice el informe; la frase quitada en 7.2 deja la lectura
  5 bien enlazada.
- Física y oficio nuevos (Kirchhoff, Boucherot, capacidad, conexión en triángulo, aparamenta
  sobredimensionada por armónicos) declarados en Trazabilidad.

## Correcciones aplicadas (2)

1. 2.2: «Las dos reglas de esas tablas son casos de las leyes de Kirchhoff» → «Las dos reglas de esa
   tabla se deducen de las leyes de Kirchhoff, junto con la de Ohm; las de Kirchhoff resuelven
   cualquier circuito». El antecedente es una sola tabla (asociación serie/paralelo), y las fórmulas
   de resistencia equivalente necesitan también la ley de Ohm (error 1, cita cruzada; precisión).
2. 7.5: el rótulo «**Dimensionamiento de las instalaciones**» iba en negrita con mayúsculas
   cambiadas; en la fuente está en versalitas («DIMENSIONAMIENTO DE LAS INSTALACIONES»). Pasa a
   redonda entre comillas (negrita = literal).

## Lentes

- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 11.014 palabras, 36 epígrafes, índice sin cambios.

Sin más hallazgos. El tema queda cerrado.
