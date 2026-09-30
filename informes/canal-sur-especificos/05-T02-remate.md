# Remate · Ayudante de Realización (05) · Tema 2 · Guion, escaleta y documentación de realización

Fase 5. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/02-guion-escaleta-documentacion.md`.
Hecho el 30-09-2026 (reloj del sistema; el encargo fecha el trabajo el 24-09-2026). Entrada:
`05-T02-refutacion.md` (E1, C1, C2) y `05-T02-preguntas.md` (preguntas 3 y 13).

## Correcciones, comprobadas en la fuente antes de aplicarlas

| N.º | Comprobación | Resultado |
|---|---|---|
| E1 | RD 1680/2011 (`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`, módulo 0904, RA 2.a-2.c, ll. 543-545), leído el 30-09-2026: dice «listas coherentes» y «hojas de desglose»; no «listados generales» | Aplicada |
| C2 | IMS077_3 (`incual-IMS077_3.txt`, l. 301), leída el 30-09-2026: CR1.5 nombra los pies y no los define | Aplicada, como oficio |
| C1 | SMPTE ST 2059-1:2021 (`fuentes/canal-sur/sonido/smpte/st2059-1/st2059-1-2021.txt`, 9.3.3.2, ll. 1606-1630), leída el 30-09-2026: a 24, 25 y 30 fps, *non-drop frame* «per SMPTE ST 12-1»; FF = frames − FR × (SS + 60 × (MM + 60 × HH)); HH = HH24 % 24. De ahí, a 25 fps, FF de 00 a 24. No hay copia local de ST 12-1 ni de EBU Tech 3097: la ampliación se apoya en ST 2059-1, que es la que se cita | Aplicada (ampliación) |

Quitado antes de guardar: «la cadencia de la televisión europea» (sin fuente leída que lo diga).

## Pasajes cambiados

1. **2, «El guion de trabajo»**, tras la cita de CR1.5 (nuevo párrafo, oficio): «La cualificación no
   define esos dos pies; en el oficio, el pie de salida a vídeo es la frase del plató tras la cual se
   lanza la pieza, y el pie de vuelta de vídeo es la última frase o la última acción de la pieza, la
   que avisa de que hay que volver a plató o pasar a lo siguiente. Visto desde la pieza, este segundo
   es el mismo pie de salida que recoge su minutado (epígrafe 4).»
2. **8, «El código de tiempo y la claqueta»**, tras la definición (nuevo párrafo): presenta la SMPTE;
   con ST 2059-1:2021, 9.3.3.2, código sin salto a 24, 25 y 30 fps, horas módulo 24, fotogramas como
   resto; a 25 fps, de 00 a 24 y de 00:00:00:00 a 23:59:59:24; 00:05:10:25 imposible; ejemplo de suma
   00:00:10:20 + 00:00:00:10 = 00:00:11:05 (cálculo).
3. **9, «Los listados»**, tabla, fila «Hojas de desglose y listados generales», columna Fuente:
   «RD, módulo 0904, RA 2.a a 2.c, las hojas de desglose; los listados generales, oficio (epígrafe 10)».
4. **«Lo que este tema no da»**: añadido «El código de tiempo con salto de fotogramas (*drop frame*)
   de las cadencias de 30/1,001 y la relación entre cadencias y formatos: tema 14.»
5. **«Trazabilidad»**: fila nueva SMPTE ST 2059-1:2021, 9.3.3.2 (leída 30-09-2026); en la fila
   «Oficio», añadidos «pies de salida a vídeo y de vuelta de vídeo» y «suma de códigos de tiempo».

Antecedentes releídos: «esos dos pies» sigue a la cita de CR1.5; «este segundo», al pie de vuelta;
«lo fija así», a «Cada campo cuenta…». Sin negritas nuevas (todo en redonda: paráfrasis y oficio).

## Preguntas

- 3: pasa de «a medias» a **entera** (pasaje 1).
- 13: pasa de «no» a **entera** (pasaje 2). La pregunta no se ha tocado.

## Lentes

- `indice.py`: 60 epígrafes, sin rúbricas nuevas; índice sin cambios.
- `refutar_prosa.py`: 0 hallazgos.
- Sin negritas ni preceptos nuevos: no tocan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Amplió

Sí (pasajes 1 y 2): hay que hacer la fase 5 bis sobre esos dos pasajes.

## Ficheros tocados

- El tema 02 (arriba) y este informe. Los cambios en los temas 03 y 06 del árbol de trabajo no son míos.
