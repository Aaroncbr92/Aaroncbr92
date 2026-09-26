# Productor/a (puesto 32) · Tema 4 · Remate

Fase 5. Tema: `temas/canal-sur-especificos/32-productor-a/04-presupuesto-de-produccion.md`.
Entradas: `32-T04-refutacion.md` y `32-T04-preguntas.md`. Cada corrección se comprobó en la fuente
antes de aplicarla; fuentes leídas el 25-09-2026 («hoy» del encargo: 24-09-2026): Ley 18/2007,
arts. 17, 19, 35 y 37 (volcado BOE de 24-09-2026, redacción única de 15-01-2008); texto refundido
LGHP, arts. 97 y 98 (redacción desde 01-01-2018); Carta 2024-2029, art. 24.2.a; Contrato-Programa
2024-2026, cláusula octava.3 y séptima.4; Libro de Estilo (2004), 4.4.4, punto 5.
Ficheros tocados: el tema y este informe.

**Amplió contenido nuevo: sí** (lagunas 1 y 2; unas 350 palabras). Procede la fase 5 bis sobre los
pasajes 1, 2, 5 y 6.

## Correcciones: todas confirmadas en la fuente y aplicadas

| # | Hallazgo | Fuente comprobada | Resultado |
|---|---|---|---|
| Menor 1 | Carta 24.2.a cortada | Carta, l. 1150-1152: «…de los medios de Canal Sur y sobre la que se poseen derechos de explotación» | Aplicada |
| Menor 2 | Octava.3 resumida sin sujeto ni 5 % | Contrato-Programa, octava.3 (propone «su modificación»; valores objetivos de las cláusulas Tercera, Cuarta y Quinta; 2 %; < 5 %; ≥ 5 % → resolución) | Aplicada |
| Menor 3 | Coste completo incoherente | Cuarta.2 (fijos y variables; parte de la estructura «directamente como resultados») | Aplicada, sin nueva doctrina |
| Menor 4 | Art. 37 apoyado en «según el temario común» | TR LGHP 97.1 (sociedades mercantiles del sector público andaluz, contabilidad pública) y 98.1 (rendición por conducto de la Intervención General) | Aplicada |
| Laguna 1 | Quién elabora, aprueba y rinde | Ley 18/2007: 19.2.b, 17.1.f, 17.1.k, 17.2, 19.3 (indelegable la 17.1.f), 19.2.m, 35.1 y 35.2 | Ampliada |
| Laguna 2 | Libro 4.4.4.5, segunda frase | Libro, l. 2709-2712 | Ampliada |

No aplicado: la unificación del orden de la desviación en la tabla «Comprometido, ejecutado y
previsión de cierre» (pasaje copiado de RTVE sin cambios); la refutación la condicionaba a tocar la
tabla, y no se ha tocado.

## Pasajes cambiados

1. **«El presupuesto del programa dentro del presupuesto del grupo»**: nuevo bloque «Quién elabora y
   quién aprueba el presupuesto del grupo (artículos 17 y 19)», tres viñetas tras el artículo 23
   (19.2.b; 17.1.f y 17.2, con la regla de la falta de mayoría absoluta; 19.3; 17.1.k).
2. **«Qué se hace con una desviación»**, segundo párrafo: la octava.3 reescrita con sujeto (la
   Comisión propone la modificación del Contrato-Programa), los valores objetivos de las cláusulas
   Tercera, Cuarta y Quinta, el 2 %, la variación inferior al 5 % y la resolución con decremento
   igual o superior al 5 % no motivado por equilibrio.
3. **«Medios propios y medios ajenos»**: cita de la Carta 24.2.a completada.
4. **«La contabilidad analítica del grupo RTVA»**: las dos viñetas sobre el alcance dicen ahora
   «coste completo de los factores de producción» y «no es un coste completo puro».
5. **«El cierre del ejercicio del grupo»**: la nota del art. 37 cita directamente 97.1 y 98.1 del
   texto refundido; viñeta nueva con 19.2.m (aprobación de cuentas) y 35.2 (rendición ante la
   Comisión parlamentaria, identificada por 35.1).
6. **«El control del gasto en Canal Sur»**: la cita del Libro 4.4.4, punto 5, incluye su segunda frase.
7. **Qué se puede preguntar**, ficha (Fuente, Redacción), **Normativa** y **Trazabilidad**:
   añadidos los arts. 17, 19, 35 de la Ley 18/2007 y 97 y 98 del texto refundido.

Relectura de antecedentes: «ella misma» (pasaje 5) remite a la persona titular de la Dirección
General; «la referida Comisión parlamentaria» va seguida de su identificación (35.1); «puede
proponerla» (pasaje 2) remite a «la modificación». Sin referencias colgantes.

## Lentes

- `indice.py`: índice regenerado; 9.006 palabras, 43 epígrafes (la portada anuncia 8.000; el
  exceso viene de las lagunas, que el encargo manda ampliar).
- `negritas.py` (Ley 18/2007, TR LGHP, Ley 8/2025, Carta, Contrato-Programa, Libro, convenio, Cámara,
  Decreto 189/2026): 86 cotejadas; las 11 nuevas, todas literales; 6 «no está», las mismas de la
  refutación (rótulos, ligaduras del Libro, PGC). 0 mal atribuidas.
- `refutar_exactitud.py` (Ley 18/2007 y TR LGHP): ninguna cita nueva no literal. Los 13 avisos son
  citas de la Carta, convenio y Contrato-Programa emparejadas por número con artículos de la ley
  (falsos positivos, preexistentes salvo que el de cuarta.12 ahora se ancla a «art. 35» por
  cercanía de la viñeta nueva; la cita es literal del Contrato-Programa).
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: SA y SAP dentro de citas literales; falsos positivos, como en la refutación.
