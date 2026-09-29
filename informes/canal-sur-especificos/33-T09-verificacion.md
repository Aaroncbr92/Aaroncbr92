# Realizador/a (puesto 33) · Tema 9 · Fase 3, verificación

Fecha de trabajo: 24-09-2026. Tema: `temas/canal-sur-especificos/33-realizador-a/09-mezclador-recursos-realizacion.md`
(12.625 palabras y 61 epígrafes tras la verificación; índice regenerado con `indice.py`).

## Pasajes copiados: comprobación de que son literales

Script de párrafos, filas y citas (quitando negritas, `> ` de cita y saltos de línea) contra los cuatro ficheros de origen:

- **Copiado de RTVE sin cambios** (`realizacion/10`, `realizacion-tv/15`): todos los pasajes de la lista del
  redactor aparecen literales (§ 1, § 3 con la tabla de atributos, § 4 con las dos citas ATEM y la tabla de la cadena,
  § 7 con la tabla de modos y la lista NAM/FAM, § 8, § 9, § 10, § 11 con las citas de Nivel/Ganancia y de la
  composición precompuesta, § 13, § 14 con la cita de la macro, § 15, § 16, y la lista del verde y el azul de `15`).
  No se re-verifican.
- **Copiado del común** (30-07 § 6; 30-01, filas Fundido y Encadenado): literal. No se re-verifica.
- **Adaptado del común** (30-07, «Tres consecuencias…»): literal salvo «(tema 2)» → «(tema 14)»; el tema 14 del puesto 33
  trata el submuestreo (4:2:2, 4:4:4). Correcto.

## Fuentes releídas y fechas

| Fuente | Qué se cotejó | Leída |
|---|---|---|
| Manual ATEM, español, ed. dic. 2024 (volcado local) | Todas las citas no copiadas: transiciones y mandos, FTB, AFV, transición animada, generadores, figura, croma normal y avanzado, rebase, DVE, SuperSource, multipantalla, nombres de fuente, macros, DSK, TIE, limpias, salida del alfa | 24-09-2026 |
| RD 1680/2011 (BOE-A-2011-19599) | 0905: RA 1 f), RA 5 y c)/e), RA 6 b)/d)/e), contenidos y sus bloques; 0910: RA 4 b)/g) | 24-09-2026 |
| RD 500/2024 (BOE-A-2024-10685), art. séptimo y nota de modificaciones | Modifica el anexo I suprimiendo FOL, EIE y FCT y añadiendo módulos nuevos; no toca 0905 ni 0910 | 24-09-2026 |
| Libro de Estilo (2004), copia sin ligaduras | 3.6.1, 3.10, 3.16 a 3.16.2, 6.5.1, 6.5.2, 8.6.1 (puntos 4 y 9), 9.9.2; páginas según los marcadores | 24-09-2026 |

`negritas.py` (ATEM, RD, LE sin ligaduras): 109 negritas, 9 no halladas: 8 del común, sin volcado local, y la de 3.16.1,
cortada por el salto de página 57-58 (comprobada a mano). `refutar_prosa.py`: 1, DVE en el título, que reproduce el
enunciado (se acepta).

## Correcciones aplicadas (con el error del catálogo)

1. **6 salvedad omitida**. Transición animada: el manual limita la descripción a **«los modelos ATEM 1 M/E y 2 M/E»**. Se añade.
2. **6**. SuperSource: el manual la da para los modelos con más de un banco M/E. Se añade.
3. **6**. Salida limpia: el ATEM tiene la limpia 1 (sin elementos superpuestos) y la limpia 2, que **«incluye además la
   penúltima capa (DSK 1), pero no la final (DSK 2)»**. Se añade en § 8 y en la tabla USK/DSK («No (en el ATEM, la
   limpia 2 lleva la DSK 1)»). La tabla de la cadena, copiada de RTVE, no se toca. La pregunta de control 9 (DSK 2) sigue siendo correcta.
4. **6**. Nombres de fuente: el manual se contradice (en la p. de opciones de visualización, 20 caracteres para el panel
   y 4 para el programa). Se cita y se deja lo seguro.
5. **9 afirmación sin fuente**. Se quita «los mezcladores modernos permiten dividir un banco en dos… o crear bancos virtuales».
6. **9**. Se quita el párrafo de Ultimatte (integrado en gama alta, unidad externa…): ningún documento leído lo sostiene
   (en los volcados de Avid sólo aparece como licenciante). Se declara en «Lo que este tema no da» y se retira de la lista de oficio.
7. **9**. *Coring*: se quita «se encuentra en el procesado de las cámaras y en algunos ajustes de detalle». La definición
   se marca como oficio.
8. **9**. Salida del alfa: «el fabricante lo recomienda» → el manual dice «es útil». Corregido.
9. **9**. Multipantalla: «el modelo más grande que describe» → «el ATEM Constellation 8K», que es lo que dice el manual.
10. **9**. «En los mezcladores sencillos» → «En los modelos sin croma avanzado» (el manual da el avanzado para Constellation
    8K y 4 M/E Broadcast Studio 4K). «ese modelo» (18 formas) → «el mezclador», como el manual.
11. **9**. LE 3.16: el «porque» que unía la cama de audio con **«Los gráficos tienen que primar…»** no está en la fuente → «Y añade:».
12. DVE: «el mismo valor a los tres ejes» → «al ancho y al alto (ejes X e Y)»: la Z no cambia la forma de una imagen plana.
13. **5 siglas**: se presentan BOE y BOJA, como en los temas 02-06 del puesto.
14. Rótulo «Los bancos de mezcla efectos» → «de mezcla y efectos (M/E)»; índice regenerado.

## Comprobado y correcto

- **La advertencia del DSK (pedida por el redactor) es correcta.** El manual dice «el módulo DSK cuenta con dos botones
  para composiciones previas», pero en el mismo pasaje nombra los paneles «Composición previa» y «Composición posterior»,
  y explica «Cómo realizar una composición posterior lineal o por luminancia» en el panel «Composición posterior 1»:
  lineal o luminancia son justo los tipos del DSK. Se añade esa segunda prueba al tema.
- Botones MIX, DIP, WIPE, DVE y STING (rótulos del panel en el manual); CUT, AUTO, palanca, BKGD/KEY 1-4, PREV TRANS, FTB
  y AFV, TIE, ON AIR, AUTO del DSK; 100 espacios de macro; vectorscopio con barras; muestra y controles del croma avanzado.
- RD 1680/2011: cada cita, en su RA, criterio y bloque de contenidos; BOE núm. 302, de 16-XII-2011.
- Libro de Estilo: todas las páginas cuadran con los marcadores (50, 53, 57, 57-58, 58, 93, 122, 167); 8.6.1.9 es «deberán».
  La cama de audio está, por su posición, dentro de 3.16.2 («Microeconomía»), aunque habla de los gráficos en general; la cita es correcta.
- Remisiones a los temas 1, 4, 6, 11, 12, 13 y 14: cada uno trata lo que se le atribuye (el 4 remite al 9 lo mismo).

## Lo que no se pudo confirmar (sigue declarado en el tema)

Equipamiento del control de Canal Sur, manual de identidad gráfica y nomenclatura de otros fabricantes (DME, SÚPER MIX, Ultimatte).

Ficheros tocados: el tema y este informe. Copia del Libro de Estilo sin ligaduras y scripts de cotejo, en el scratchpad.
