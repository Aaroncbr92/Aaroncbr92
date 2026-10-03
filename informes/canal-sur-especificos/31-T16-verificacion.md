# 31-T16 · Verificación · Análisis de audiencia radiofónica y digital, indicadores y mejora de contenidos

Fase 3. Verificado el 03-10-2026 (fecha de referencia del encargo: 24-IX-2026).
Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/16-analisis-audiencia-radiofonica-digital-indicadores-mejora-contenidos.md`.
Copia previa: scratchpad `31t16-antes-verif.md`.

## Pasajes copiados (sólo literalidad)

Comprobados con grep contra el original, sin re-verificar el contenido:
- Común 06 (Carta 6.5, 6.7, 26.2): literales.
- Redactor/a T14 §5 (Manual de estilo de RTVE 4.7, comentarios y encuestas web): literales.
- RTVE gestion/27 §9 (definición de audiencia, denominador, madrugada) y §12 («Ninguna norma…»):
  literales, sin las negritas. produccion/04 §5, tabla (cabecera y fila «Métrica»): literal.

## Fuentes releídas (03-10-2026)

AIMC: *Normas de radio en EGM* (definición, pregunta, Canarias, indicadores y bases del *share*,
programas compartidos, publicación, corte, prioridad de asignación, pódcast); ficha técnica de la
1.ª ola de 2026 (bloque EGM RADIO); calendario; características técnicas; entrega de resultados;
fusión; usos; márgenes de error; radio *streaming*; noticia 18-04-2018; comunicados 08-10-2025,
10-07-2026 y 01-09-2026. *Marco General 2026*: tablas miradas en la imagen de las págs. 33 y 35
del PDF: Canal Sur Radio 0,5 (2005: 0,9) y *share* 1,6; Canal Fiesta 0,5 y 1,5; totales 30,8 y
31,5. Todo coincide. Metadatos del PDF: creado el 11-02-2026, así que «febrero de 2026» se sostiene.
IAB v2.2 (págs. 15-23). Carta art. 6.6-6.7 y 26; Contrato-programa ap. 29, 30, 126 y 129 (BOJA).
López Vigil, cap. 11. Web (03-10-2026): nota de prensa de IAB Tech Lab sobre la v2.3 (21-07-2026),
su página «Clarifying Today's Podcast Measurement…» y ppc.land.

## Correcciones aplicadas (error del catálogo)

1. **IAB v2.3 (9 y 7).** «En consulta pública en 2026, no leída» era un dato tomado de la
   investigación y nadie lo había leído. Comprobado: comentario público del 21-VII al 19-VIII-2026; IAB
   confirma una versión final, que según la prensa del sector salió el 29-IX-2026 (después de la
   fecha del temario) y cambia *listener* por *podcast consumer*. Se reescribe «Lo que este tema no
   da», se dice «vigente a la fecha del temario» en §2 y en la ficha, y se añade una fila a
   Trazabilidad. **Para el coordinador:** si «lo vigente el día en que se escribe» quiere decir el
   3-X y no el 24-IX, la guía vigente es ya la 2.3 (que no se ha leído) y habría que revisar §2.
2. **Remisión al tema 4 (1).** La identificación en antena no está en el tema 4. Pasa a «el indicativo
   y la identificación de la emisora se estudian en el tema 1» (tema 1, tabla «Indicativo»).
3. **«Recuerda la voz y el nombre» (9).** Las Normas hablan del nombre del locutor. Se quita «la voz».
4. **Contrato-programa ap. 30 (8 y 6).** «Será prioritaria» por **«continuará siendo prioritaria»** →
   «seguirá siendo». La cita se cortaba en «de radio» y se completa. Y «con la plena interacción de
   quien desempeñe la defensa de la audiencia» atribuía mal la idea: la fuente favorece la
   interactuación del defensor **con la sociedad**. Se corrige.
5. **Ap. 126 (6).** «Para obtener…» se queda sin la salvedad, porque es «en cumplimiento de la
   obligación comunitaria de obtener…». Se cita así.
6. **Comscore (9).** La frase «El servicio debía regirse por los principios…» se cambia: la fuente
   dice que el contrato marco y el modelo de gobernanza debían dar cumplimiento a esos principios.
7. **Client-Confirmed Ad Play (6).** Se informa por cuartiles «Whenever possible», y faltaba esa
   salvedad. Se añade.
8. **Grupo de discusión de López Vigil (9).** Es un ejercicio de taller en el que coordina y
   observa uno de los participantes, no la descripción general de un grupo de discusión. Se reescribe.
9. **Ficha (9).** «Comprobada como vigente el 24-09-2026»: las páginas de AIMC se descargaron el
   03-10. Se queda en «leída el 03-10-2026».
10. **Negritas de paráfrasis (regla negrita = literal).** Se quitan las negritas de «la propia ola»,
    «registros del servidor», «audiencia media en porcentaje sobre el universo», «la audiencia media
    del total del medio», «total de la radio generalista/temática», «al menos una media hora», la
    columna EGM de la tabla TV/radio (salvo «La media hora»), las ideas 2 y 3 de la Carta, «una
    medida, un efecto medible» y la advertencia inicial.

Sin hallazgos en el resto. Todas las cifras del EGM, el calendario, los cortes, las definiciones,
las bases del *share*, los comunicados y sus fechas, las citas de IAB y de López Vigil y los cálculos
de la práctica (*rating* 5 %, fidelidad 62,5, *share* 20, minutos 6 y 75) cuadran con la fuente.
«37 cadenas de doce grupos»: hay doce grupos. Las «cuatro fuentes» del ap. 29 cuadran. Remisiones
comprobadas: tema 2 (minutos por franja, Carta 6.6, público objetivo), 9, 11, 17 y común 05-06.

## Lentes

- `negritas.py` contra los `.txt` de `radio/`, la Carta y el Contrato-programa: había 176 negritas y
  46 no estaban en la fuente. Quedan 162 y 32. Las que faltan son rótulos, cifras o fechas
  destacadas, las preguntas de la práctica y las dos citas del Manual de RTVE (copiadas del común,
  y el Manual no está entre los volcados). No hay atribuciones cruzadas.
- `refutar_prosa.py`: 1 hallazgo (ODEC), que se deja como lo justificó la redacción. `indice.py`:
  9.803 palabras y 39 epígrafes, con el índice sin cambios.
- No se pasan `refutar_exactitud.py` ni `refutar_modo.py`: el tema no desarrolla preceptos del
  BOE. La Ley 18/2007 y la Ley 10/2018 sólo aparecen dentro de la cita del Contrato-programa.

## Ficheros tocados

- Modificado: el tema 16.
- Creado: este informe.
