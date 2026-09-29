# Realizador/a (puesto 33) · Tema 10 · Remate (fase 5)

Fecha de trabajo: 24-09-2026 (fuentes leídas el 29-09-2026, fecha del sistema). Tema:
`temas/canal-sur-especificos/33-realizador-a/10-iluminacion-para-realizacion.md`. Entradas:
`33-T10-refutacion.md` (2 hallazgos menores, 2 lagunas) y `33-T10-preguntas.md` (13 enteras,
1 a medias, 1 no). **Amplía contenido nuevo: sí** (pasa a fase 5 bis).

## Hallazgos: comprobados y aplicados

| # | Comprobación en la fuente | Pasaje cambiado |
|---|---|---|
| 1 | El tema cita LE 6.3.4 (p. 91), 6.5 (p. 92) y 5.1 (p. 79): el «sólo» de «Lo que este tema no da» era incompleto. Correcto | «Lo que este tema no da», tercer punto: añade «la armonía del material de archivo (6.3.4), la responsabilidad del realizador sobre la corrección de la imagen (6.5)» |
| 2 | La ficha 5341111 dice sólo **«Realizar pruebas y ensayos de programas.»**; la consecuencia es de oficio. Correcto | «Cómo se coordina…», «Tres reglas…»: «, de donde, como costumbre de oficio y no como texto de la ficha, la luz se aprueba en ensayo y no al aire» |

## Lagunas: tema ampliado

1. **Fracciones de los geles (pregunta 12)**. Fuente nueva descargada: Rosco, *Filter Facts* (PDF de
   2009, 32 pp.), `fuentes/canal-sur/realizador/Rosco_Filter-Facts.pdf` y `.txt` (con
   `documento.py texto`). Leídas p. 6 (mired constante y aditivo; aviso CCT/IRC > 90), p. 8 (aviso de
   la calculadora) y p. 9 (guía rápida Cinegel). El texto extraído rompe espacios; cada negrita se
   cotejó sin espacios y contra la página del PDF: todas halladas. Pasaje nuevo: epígrafe
   **«Las fracciones de los geles: mired y pérdida de luz»** (tras «Los filtros de conversión: CTO y
   CTB»): tabla de 3202, 3204, 3208, 3216, 3407, 3408, 3409, 3410 (conversión, mired, transmisión);
   lectura en cálculo (fracción ≈ parte del completo, suma de mired, 36 % ≈ 1,5 pasos, −131 frente al
   −134 calculado); dos avisos del fabricante; Lee declarado no leído. Resuelve además la «pérdida de
   luz de cada gel», antes declarada como no dada: «Lo que este tema no da» (séptimo punto) cambia a
   «se dan sólo con la guía de un fabricante (Rosco); los de otras marcas, no».
2. **El nit (pregunta 15)**. Fuentes: UIT-R BT.2100-3 (02/2025), cuadro 3
   (`fuentes/canal-sur/montador/itu/bt2100.txt`, l. 247-251: «≥ 1 000 cd/m2», «≤ 0.005 cd/m2»);
   Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, cap. 10, p. 261 («a peak luminance level
   of 100 nits (cd/m2)»). Se usa la edición -3 y no la -1 de `fuentes/normas-tecnicas/`, porque es la
   vigente y la que cita el tema 14. Pasajes: fila «Luminancia» de la tabla de magnitudes («…(cd/m²),
   llamada nit en monitores y pantallas») y párrafo nuevo tras «La distinción entre iluminancia y
   luminancia…» («La luminancia es también la magnitud de las pantallas…», remite al tema 14).

## Otros pasajes tocados por la ampliación

- Portada, «Fuente»: añade UIT-R BT.2100-3, Rosco *Filter Facts* y el manual de DaVinci Resolve 21.
- Siglas y términos: añade el nit.
- «Trazabilidad»: tres filas nuevas (Rosco, BT.2100-3, Resolve), leídas el 29-09-2026.
- Índice regenerado.

Antecedentes releídos en cada pasaje cambiado: «ese apartado», «el mismo fabricante», «el epígrafe
anterior» tienen delante su referente.

## Lentes

- `indice.py`: 15.847 palabras, 59 epígrafes, sin avisos de ruta.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` con Rosco, BT.2100-3 y Resolve: las negritas nuevas de BT.2100 y Resolve, halladas;
  las de Rosco salen «no está» sólo por los espacios rotos de la extracción, y se hallan todas
  normalizando espacios (cotejo en el scratchpad). El resto de «no está» son de otras fuentes no
  pasadas en esta corrida (RD, convenio), ya verificadas.

## Ficheros tocados

El tema 10; este informe; `fuentes/canal-sur/realizador/Rosco_Filter-Facts.pdf` y `.txt` (nuevos).
