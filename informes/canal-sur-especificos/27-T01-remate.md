# Puesto 27 · Oficial Técnico Electricista · Tema 1 · Fase 5, remate

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026). Tema rematado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/01-instalaciones-electricas-de-baja-tension-magnitudes-potencia-y-cargas.md`.
Entradas: `27-T01-refutacion.md` (3 hallazgos menores, 5 lagunas) y `27-T01-preguntas.md`.
Ficheros tocados: el tema y este informe. **Amplía: sí** (procede fase 5 bis sobre los pasajes 4 a 8).

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002, volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md`, ITC-BT-48 (1 redacción, desde 18-09-2003), apartado 2.3 | 05-10-2026 | Sus cinco párrafos, literales: 50 ºC, carga residual, 2.000 m, 1,3 veces, 1,5 a 1,8 veces |
| Mismo volcado, ITC-BT-09 (1 redacción), apartado 3 «DIMENSIONAMIENTO DE LAS INSTALACIONES» | 05-10-2026 | Párrafos 1 y 2: el 1,8 y el coeficiente corrector |
| Mismo volcado, ITC-BT-19 2.2.2 e ITC-BT-44 3.1 | 05-10-2026 | Que no dicen lo quitado en el hallazgo 1 y que la obligación de 3.1 es para receptores con lámparas de descarga (hallazgo 2) |

Cálculos rehechos: Boucherot (P 15 kW, Q 7,5 kvar, S 16,77 kVA, fp 0,894); capacidad de 5,8 kvar a
50 Hz, 38,5 µF por fase en triángulo y 115,4 µF en estrella.

## Hallazgos: todos aplicados (el informe acertó en los tres)

1. 7.2, lectura 5. Quitada la frase «No es una tolerancia mayor: es la misma tolerancia contada
   desde más atrás.» (inferencia sin fuente).
2. 6.3. «Donde la compensación SÍ es obligatoria es en el alumbrado. La ITC-BT-44, apartado 3.1,
   para las lámparas de descarga:» pasa a «Donde sí es obligatoria es en el alumbrado con lámparas
   de descarga y en el alumbrado exterior. La ITC-BT-44, apartado 3.1, para los receptores con
   lámparas de descarga:».
3. 8.2. «el neutro lleva la diferencia» pasa a «el neutro lleva la suma vectorial, que ya no es cero».

## Lagunas: las cinco cubiertas ampliando el tema

4. 2.2, tras la asociación de resistencias: tabla de las dos leyes de Kirchhoff con ejemplo (el de
   la pregunta 4) y su uso en un cuadro. Física elemental, declarada en Trazabilidad.
5. 4.2, al final: «Varios receptores en un mismo cuadro», teorema de Boucherot con el ejemplo de la
   pregunta 8 (fp ≈ 0,89, no la media).
6. 6.2, tras el ejemplo: Q = U² · ω · C, tabla estrella/triángulo y capacidad de la batería de
   5,8 kvar (≈ 38 µF en triángulo, ≈ 115 µF en estrella). Oficio declarado: la conexión en triángulo.
7. 6.3, antes de la tabla: cita literal en negrita de la ITC-BT-48, apartado 2.3, entera, con una
   línea de lectura; fila nueva en la tabla resumen («Condensadores en general … ITC-BT-48, 2.3»).
8. 7.5, al final: cita literal de la ITC-BT-09, apartado 3, párrafos 1 y 2 (1,8 veces y coeficiente
   corrector).

Además, por arrastre: portada (Fuente, añade ITC-BT-48; Extensión «Unas 11.000 palabras»); «Qué se
puede preguntar» (Kirchhoff, suma de potencias, aparamenta de condensadores); Normativa (ITC-BT-48
2.3; UNE-EN 60831 nombrada también por la ITC-BT-48); Trazabilidad (fila ITC-BT-48; ITC-BT-09
apartado 3 con el 1,8; física y oficio nuevos declarados).

## Relectura de antecedentes

«Las dos reglas de esas tablas» (tablas de asociación, justo antes); «El mismo 1,8» (cita de la
ITC-BT-44, justo antes); «Ese 1,5 a 1,8» (cita ITC-BT-48, justo antes); «la batería de 5,8 kvar del
ejemplo» (ejemplo de 6.2, justo antes); «epígrafe 3.2» define ω. Todos con antecedente.

## Lentes

- `indice.py`: 11.007 palabras, 36 epígrafes; sin epígrafes nuevos, índice sin cambios.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (contra el REBT): 51 cotejadas; 2 «no están», que son los rótulos de plantilla
  «Enunciado del programa» y «Qué se puede preguntar»; 0 mal atribuidas.
- `refutar_exactitud.py`: 0 no literales. `refutar_modo.py`: 0 hallazgos.

Con lo ampliado, las 15 preguntas de `27-T01-preguntas.md` se contestan enteras con el tema.
