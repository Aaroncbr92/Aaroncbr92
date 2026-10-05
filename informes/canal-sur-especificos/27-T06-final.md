# Puesto 27 · Oficial Técnico Electricista · Tema 6 · Fase 5 bis, revisión del remate

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/06-alumbrado-interior-exterior-y-de-emergencia.md`.
Alcance: sólo los pasajes que cambió el remate (`27-T06-remate.md`), sacados con `diff` contra la copia
previa al remate (`27t06-antes-remate.md`, scratchpad). Copia previa a esta fase: `27t06-antes-5bis.md`.
Fecha de trabajo y de lectura de todas las fuentes: 05-10-2026 (el encargo fija «hoy» en 24-09-2026).

Ficheros tocados: el tema y este informe. Nada más.

## Fuentes releídas (05-10-2026)

| Fuente | Qué se cotejó |
|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado | ITC-BT-01 (clases 0-III, doble aislamiento, masas), ITC-BT-09 (luminarias de clase I o II; «lámparas o tubos de descarga»), ITC-BT-30, 1.3, ITC-BT-44 (puesta a tierra, 1,8, 0,9, resistencia de descarga) |
| RD 1890/2008 (BOE-A-2008-18634), volcado | Art. 3 (apartados 2, 3, 5, 10, 13, 17 y encabezado); ITC-EA-04, 2 (40 y 65 lum/W, salvo festivas y navideñas) |
| RD 486/1997 (BOE-A-1997-8669), volcado | Anexo IV, apartado 4, a) a e): literal |
| Reglamento (UE) 2019/2020 (DOUE-L-2019-81880) y corrección (DOUE-L-2020-80257) | Art. 1, art. 2 (1, 11-19), anexo I (CCT, halogenuros metálicos), art. 11 (aplicable 01-09-2021), DOUE núm. 315 de 05-12-2019; la corrección sólo toca 2.1.a y un cuadro del anexo II |
| Reglamento (UE) 2021/341 (DOUE-L-2021-80227), volcado del remate | Art. 4: en el art. 2 sólo sustituye el punto 4; anexo IV: en el anexo I sólo el punto 52. Confirmado |
| DB HE (texto de 14-06-2022), `DBHE.txt` | Anejo A (iluminancia, eficacia, Ra, equipos auxiliares); HE 3, 1.3 a)-d); tabla 3.1 (zonas comunes 4,0 con nota 4; no residenciales 6,0) |
| IDAE, Guía 010 (junio de 2019), `idae-oficinas.txt` | 5.4 y tabla 4; 6.2 a 6.4: todas las cifras y citas del 2.5 |
| Zemper, página de 04-11-2021 (fecha de `article:published_time`) | Periodicidad y libro de registro atribuidos a UNE-EN 50172 / 62034 |

Las 80 negritas de los pasajes cambiados se cotejaron una a una (guion propio sobre el diff y
`negritas.py` con las nueve fuentes): todas literales en su fuente. Los números de apartado del
Reglamento 2019/2020 y del art. 3 del RD 1890/2008 son correctos.

## Hallazgos y correcciones aplicadas

1. **Atribución (error 8/1), 2.5.** «las **«lámparas de descarga»** de la ITC-BT-44 y la ITC-BT-09»:
   la ITC-BT-09 dice «lámparas o tubos de descarga», no «lámparas de descarga». Corregido: «las
   **«lámparas de descarga»** de la ITC-BT-44 y las **«lámparas o tubos de descarga»** de la ITC-BT-09».
2. **Afirmación sin fuente (error 9), 2.5.** «ese factor de potencia bajo es la razón de la
   compensación obligatoria a 0,9»: ni la ITC-BT-44 ni la guía del IDAE lo dicen (el IDAE sólo dice que
   el condensador corrige el factor de 0,5 por la penalización de la reactiva). Rebajado a lectura
   propia declarada: «explica, en lectura propia (la ITC-BT-44 no da la razón), la compensación...».
3. **Precisión de la definición, tabla de magnitudes de 2.5.** El RD 1890/2008, art. 3.5, define la
   «Iluminancia horizontal en un punto de una superficie», no la iluminancia sin más. Añadido en la
   celda, literal.
4. **Afirmación sin fuente (error 9), 3.1.** «la fila la elige y la justifica el proyecto»: el DB HE no
   lo escribe. Quitada; queda «El DB no escribe cuál prevalece [...]. El tema no resuelve lo que la
   tabla deja abierto.»
5. **Normativa que el tema invoca, fila del Reglamento 2019/2020.** Listaba los apartados 2 y 16 del
   art. 2 (mecanismo de control, descarga de gas), que el tema no cita, y omitía el art. 1, que sí cita
   en 2.4. Queda: «Artículo 1 (objeto); artículo 2, apartados 1, 11 a 15, 17 y 19 (definiciones), y
   anexo I».

## Comprobado sin hallazgo

- HE 3, 1.3 (letras a-d) y la nota (4) de la tabla: correctos y literales.
- Lectura del vapor de mercurio frente a la ITC-EA-04: la exigencia es general para las lámparas de
  alumbrado exterior salvo navideñas y festivas; 36-59 lm/W < 65 lm/W. Declarada como lectura propia.
- Clase III «no se basa»: así en el BOE; el tema lo cita y lo advierte. Correcto.
- Zemper: atribuye la periodicidad a las dos normas y el libro de registro a la UNE-EN 50172; el tema
  no dice otra cosa. Fecha 04-11-2021 confirmada.
- IDAE: discrepancia 5.300 K (tabla 4) / 5.000 K (6.2) real; 840/930 «en fluorescentes y lámparas de
  descarga», literal; incandescente retirada desde 2012 por la Directiva 2009/125/CE (el tema dice «por
  las normas de diseño ecológico»: correcto).

## Antecedentes releídos

«la misma ITC» (2.5) → ITC-BT-01; «Ese condensador» → el del balasto electromagnético recién citado;
«esas normas» (2.5, magnitudes) → las de los epígrafes anteriores; «La tabla trae dos filas» → tabla
3.1-HE3 que la precede; «Esas dos normas UNE» (5.2) → UNE-EN 50172 y 62034; «el epígrafe 3.1» desde
1.6 → existe. Todos con antecedente.

## Lentes tras corregir

- `negritas.py` (9 fuentes): 396 cotejadas; las 2 «no están» son rótulos de la plantilla («Enunciado
  del programa», «Qué se puede preguntar») y los 4 avisos de «otro artículo» son los ya explicados en el
  remate (anexo I colgado del art. 11 en el volcado; expresiones genéricas).
- `indice.py`: 32 epígrafes, índice correcto.
- `refutar_prosa.py`: 0 hallazgos.
- Extensión: 15.752 palabras (`wc -w`); la portada dice «Unas 15.000»: se mantiene.

**Resultado: 5 correcciones menores, 0 graves. El tema queda cerrado.**
