# Puesto 08 · Tema 17 · Fase 5 · Remate

Tema: `temas/canal-sur-especificos/08-camara-operador/17-prevencion-riesgos-laborales.md`.
Entrada: `08-T17-refutacion.md` (2 menores, 2 lagunas) y `08-T17-preguntas.md` (13 no, 14 a medias).
Fecha de trabajo y de lectura de todas las fuentes: **24-09-2026**.

**Resultado: el remate AMPLIÓ contenido nuevo** (subepígrafe «Ruido y riesgo eléctrico», con dos
normas nuevas). Procede la fase 5 bis sobre los pasajes listados abajo.

## Fuentes leídas (24-09-2026)

| Fuente | Cómo | Qué se comprobó |
| --- | --- | --- |
| RD 286/2006, de 10 de marzo, ruido (BOE-A-2006-4414) | `boe.py precepto` a1-a9, a11, anI; metadatos API BOE (número, fecha) | 1 redacción en toda la norma, vigente desde 31-03-2006. Arts. 1, 3.1, 4.1 (y g), 4.2, 4.3, 5.1, 5.2, 6.1, 6.4, 6.5.a, 7.1, 8.1, 9, 11.2; títulos de los anexos I-III |
| RD 614/2001, de 8 de junio, riesgo eléctrico (BOE-A-2001-11881) | `boe.py precepto` a1-a5, anI; anexo III.A en volcado; metadatos API | 1 redacción, vigente desde 21-08-2001. Arts. 1, 3.1, 3.2, 4.2, 4.3.a, 5; anexo I.1 y I.3; anexo III.A.1 y A.6; títulos de los anexos II-VI |
| RD 773/1997 (volcado vigente `fuentes/canal-sur/BOE-A-1997-12735.md`) | grep | Anexo III: «Oídos.» / «Protectores auditivos contra el ruido.» |
| INSST, tema 69 (`fuentes/prl-especifico/insst-tme-extremidad-superior.txt`) | cabecera | Título completo: «Trastornos musculoesqueléticos de la extremidad superior. Identificación de los factores de riesgo asociados y su prevención. …» |
| Ley 31/1995, art. 29.2 (en el propio tema, copiado del común) | lectura | Obligación 4.ª (informar de situaciones de riesgo) |

## Correcciones de la refutación

| # | Hallazgo | Comprobación en la fuente | Aplicada |
| --- | --- | --- | --- |
| 1 | Título del tema 69 entre comillas como si fuera completo | Confirmado: la fuente sigue tras «…extremidad superior.» | Sí: en §3 se cita sin comillas de título; en Trazabilidad, título más largo con «(título abreviado)» |
| 2 | «Es el riesgo ergonómico más propio del puesto» sin fuente | Confirmado: ninguna fuente lo dice | Sí: «Es, a juicio de este tema, …» |
| L1 | Ruido (RD 286/2006) | Norma leída | Sí, ampliación |
| L2 | Riesgo eléctrico (RD 614/2001) | Norma leída | Sí, ampliación breve |

Ninguna corrección del informe resultó equivocada. La pregunta 15 (peso de la cámara) no se
amplía, como proponía la refutación: no hay cifra general en fuente y el tema ya lo declara.

## Pasajes cambiados

1. **Portada, «Fuente»**: añadidos RD 614/2001 y RD 286/2006. **«Extensión»**: 16.598 palabras
   (recuento de `indice.py`).
2. **«Qué se puede preguntar»**: nueva línea sobre valores de exposición al ruido y sobre riesgo
   eléctrico y operaciones en tensión.
3. **«De dónde sale este tema»**: frase nueva: ruido y riesgo eléctrico se estudian en la segunda
   rúbrica.
4. **Índice**: nueva entrada «Ruido y riesgo eléctrico» (`indice.py` la confirma sin cambios).
5. **§2, tabla «Los riesgos específicos»**: fila nueva (toma del sonido → ruido); la fila de
   iluminación ya no remite a «no se da» para el eléctrico (el térmico sigue sin darse).
6. **§2, subepígrafe nuevo «Ruido y riesgo eléctrico»** (antes de «Otros riesgos del puesto»):
   - Ruido: objeto (art. 1), ámbito (3.1), tabla de los tres escalones del art. 5.1 con lo que
     obliga cada uno (4.2, 4.3, 6.4, 7.1.a y b, 8.1, 9, 11.2), salvedad del 5.2 (atenuación del
     protector sólo para valores límite), orden de medidas (4.1 y 4.1.g), protector como último
     recurso (7.1) y anexo III del RD 773/1997, evaluación por medición salvo apreciación
     profesional (6.1), ruido de impulsos (6.5.a); aplicación al cámara declarada como del tema.
   - Riesgo eléctrico: objeto y ámbito (art. 1), definición y cuatro riesgos (anexo I.1),
     instalación eléctrica con baterías (anexo I.3), humedad y compatibilidad de equipos (3.1, 3.2),
     regla sin tensión (4.2) y operaciones elementales (4.3.a), trabajos en tensión por
     trabajadores cualificados (anexo III.A.1), formación (art. 5); salvedad expresa: la
     suspensión por lluvia/tormenta del anexo III.A.6 es de los trabajos en tensión y no se
     extiende al cámara; medidas de oficio declaradas como tales, con enlace al art. 29.2, 4.ª.
7. **§3, «La cámara al hombro»**: primera frase (corrección 2) y cita del tema 69 (corrección 1).
8. **§5, tabla «Las medidas preventivas del puesto, en resumen»**: dos filas nuevas (ruido; riesgo
   eléctrico).
9. **«Normativa que el tema invoca»**: dos filas nuevas (RD 614/2001; RD 286/2006).
10. **«Lo que este tema no da»**: la viñeta de ruido y eléctrico se reescribe (qué partes de ambas
    normas no se dan; sin medición publicada de ruido en la RTVA; riesgo térmico no investigado).
11. **«Trazabilidad»**: dos filas nuevas (RD 614/2001, RD 286/2006) y título abreviado del tema 69.

Antecedentes releídos: «El ruido y el riesgo eléctrico tienen…» (antes «Los dos», sin antecedente
fuera del rótulo, corregido); «esa segunda rúbrica» remite a «La segunda (riesgos del puesto…)» del
mismo párrafo; «el apartado anterior» va dentro de la cita literal del 3.2; «Tres preceptos» los
enumera la lista siguiente.

## Preguntas tras el remate

13 (ruido, 80 dB(A)): ahora **entera** (tabla del art. 5.1 y art. 7.1.a). 14 (eléctrico): ahora
**entera** (RD 614/2001; art. 4.3.a y 3.1). 15: sigue **a medias**, sin ampliación. Recuento: 14
enteras, 1 a medias, 0 no.

## Lentes

- `indice.py`: 37 epígrafes; índice ya coincidente.
- `negritas.py` (subepígrafe nuevo contra RD 286/2006, RD 614/2001, RD 773/1997 y Ley 31/1995):
  48 negritas; 4 «no están», que son rótulos en negrita (convención del tema) y la cita con elisión
  «[…]» del art. 8.1 (literal a ambos lados); 6 «otro artículo» son las cifras de la tabla, que
  están en el art. 5.1 como dice la cabecera de la tabla.
- `refutar_exactitud.py`: los mismos avisos por proximidad de artículo; ninguno real.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py` (tema entero): 0 hallazgos.

## Otros ficheros tocados

- Volcados nuevos: `fuentes/canal-sur/BOE-A-2006-4414.md`, `.redacciones.tsv`,
  `fuentes/canal-sur/BOE-A-2001-11881.md`, `.redacciones.tsv` (`boe.py norma`, 24-09-2026).
- Auxiliares en el scratchpad. Ningún otro tema tocado.
