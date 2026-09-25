# Puesto 28 · Operador/a de Sonido · Tema 8 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/08-sonido-en-television.md`.
Entrada: `28-T08-refutacion.md` (3 hallazgos) y `28-T08-preguntas.md` (14 enteras, 1 no: la 13).
Fecha de trabajo: 25-09-2026 («hoy» del encargo, 24-09-2026).

## Fuentes releídas antes de aplicar (fecha de lectura 25-09-2026)

- Ley 13/2022, art. 121: `herramientas/boe.py precepto BOE-A-2022-11311 a1-33` contra el BOE en
  vivo: una sola redacción (vigencia 09-07-2022), vigente hoy. 121.4 literal confirmado; 121.1
  («La publicidad televisiva, el patrocinio…», «con fines de autopromoción») confirmado.
- EBU Tech 3343-2023, § 9.1 (`fuentes/normas-tecnicas/EBU_Tech3343-2023.txt`, l. 1109-1146, y el
  PDF para «short-form», que el .txt une por el corte de línea).
- Tech 3343 l. 615/646 («shall not exceed −1 dBTP») para el hallazgo 2.
- El común (`temas/canal-sur-comun/04-…`) no recoge el art. 121.4: se cita de la fuente, no se copia.

## Hallazgos aplicados

| # | Resultado |
|---|---|
| 1 (laguna, error 9) | Aplicado y ampliado. Confirmado en la fuente. |
| 2 | Aplicado: «el pico verdadero sin superar −1 dBTP». |
| 3 | Aplicado: `[...]»**.` |

## Pasajes cambiados

1. Portada, «Fuente»: «Sin norma jurídica.» → «Una norma jurídica: la Ley 13/2022, de 7 de julio,
   General de Comunicación Audiovisual, artículo 121.4 (nivel sonoro de las comunicaciones
   comerciales).»; Tech 3343 «con su apartado sobre la publicidad».
2. Portada, «Redacción que se estudia»: añadida la Ley 13/2022 en texto consolidado.
3. Portada, «Extensión»: 9.200 → 9.900 palabras (9.874 medidas).
4. Siglas: añadida **MSL** (*maximum short-term loudness level*).
5. «Qué se puede preguntar»: añadido el nivel sonoro de la publicidad en la ley y los parámetros
   de la EBU para el contenido corto.
6. Índice: nuevas entradas «La publicidad no puede sonar más fuerte que el programa» y
   «Normativa que el tema invoca».
7. **Nuevo epígrafe** «### La publicidad no puede sonar más fuerte que el programa» (en «Mezcla
   para emisión», tras «Lo que la EBU R 128 pide al programa»): art. 121.4 y 121.1 literales;
   «no puede» = prohibición; la ley no fija unidad ni método; aplicación (oficio, declarado);
   Tech 3343 § 9.1 (molestia del oyente, BCAP y CALM Act, contenido corto hasta 2 min, tabla R 128
   s1: −23,0 LUFS, −1 dBTP, MSL −18,0 LUFS/+5,0 LU, LRA no aplicable; definición de MSL; «encouraged»,
   no obligatorio).
8. «Cuatro hilos y el híbrido»: cierre de negrita tras la comilla.
9. Supuesto práctico, punto 6: «el pico verdadero sin superar −1 dBTP».
10. «Recomendaciones técnicas que el tema cita»: fila Tech 3343 con § 9.1; párrafo final: R 128 s1
    conocida sólo a través de la Tech 3343; «Salvo el artículo 121.4 de la Ley 13/2022 […], ninguna
    ley ni reglamento regula…».
11. **Nueva sección** «## Normativa que el tema invoca» (Ley 13/2022, art. 121.1 y 121.4).
12. «Lo que este tema no da»: texto de la R 128 s1 no leído; cómo mide y vigila la autoridad
    audiovisual el nivel de la publicidad, sin fuente.
13. Trazabilidad: fecha de lectura de la Ley 13/2022; fila de la Ley; en «Oficio», que la sonoridad
    normalizada es la forma práctica de cumplir el 121.4.

Releídos todos: cada «el mismo artículo», «el apartado 1», «el precepto», «su límite» tiene su
antecedente inmediato.

## Lentes

- `indice.py`: índice regenerado sin error (9.874 palabras, 49 epígrafes).
- `negritas.py` con BOE-A-2022-11311 y Tech 3343: todas las negritas nuevas casan; la única nueva
  que marca «NO ESTÁ» es «short-form content», por el corte de línea del .txt (confirmada en el PDF).
  Las demás «NO ESTÁ» son citas de otras fuentes no pasadas a la lente (EBU 3347, Clear-Com, Libro
  de estilo…), ya verificadas en fase 3.
- `refutar_exactitud.py` con la Ley: 0 negritas de la Ley mal; las 13 «no literales» son citas del
  Libro de estilo con «(art. 8)», copiadas del común, fuera de la Ley.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 1, «IFB» en el título (es el enunciado literal; se presenta en las siglas). Sin cambio.

## Pregunta 13

Ahora **entera**: el tema da el art. 121.4 literal. No se ha tocado la pregunta.

## Amplió contenido nuevo

**Sí** (epígrafe nuevo y sección de normativa): procede la fase 5 bis sobre los pasajes 1, 7, 10-13.

## Ficheros tocados

El tema 8 y este informe.
