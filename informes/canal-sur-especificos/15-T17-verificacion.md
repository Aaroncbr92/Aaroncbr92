# Grafista (puesto 15) · Tema 17 · Verificación

Fase 3 · Verificar. Fecha de trabajo: 29-09-2026 (el encargo fija «hoy» el 24-09-2026).

Tema: `temas/canal-sur-especificos/15-grafista/17-buenas-practicas-colaboracion-plazos-cortos-directo.md`
(11.924 palabras según `indice.py` tras la verificación; 41 epígrafes, índice sin cambios).

## 1. Pasajes copiados: sólo literalidad

«Copiado del común» (15-T17-redaccion.md): 20 tramos, 17 del tema 18 de Realizador/a y 3 del tema 14 de
Operador/a Montador/a de Vídeo. Comprobación con un guion de cotejo (cada párrafo del tramo de origen,
normalizado el espacio, buscado en el tema): **77 párrafos, 77 literales, 0 diferencias**. No se han
re-verificado en la fuente. Los recortes que declara el redactor (l. 490-495 del Realizador, remisión al
«tema 6»; primera frase de l. 624-626; tabla y párrafo final de «Decidir con presión»; l. 131-136 y
154-156 del Montador) no están en el tema.

«Copiado de RTVE sin cambios»: ninguno (realizacion.tsv, 15/17: 0 %). Nada que cotejar.

Todo lo demás (párrafos de aplicación, tablas nuevas, supuestos, portada, siglas, normativa, «no da»,
trazabilidad) se ha releído en su fuente.

## 2. Fuentes releídas (29-09-2026)

| Fuente | Qué se ha cotejado | Resultado |
| --- | --- | --- |
| LE, `libro-de-estilo-333233b.txt` | 3.2.2 (p. 46); 3.6 y 3.6.1 (p. 50); 3.7.1 (p. 52); 3.13 (p. 55); 3.16 (p. 58); 3.17.1.1 (p. 59); 5.6 (p. 85); 6.1, 6.1.1 (p. 88) y párrafo tras el 6.1.2 (p. 89); 8.1 puntos 3 (p. 113) y 9 (p. 114); 9.2.12.3 (p. 130); 9.9.1 (p. 166). Páginas por el número de página del .txt | Literales y páginas exactos |
| Convenio, `x-convenio-rtva-boja-240-2014.txt` | Ficha 5345100, BOJA p. 129 | Literal. Cuatro tareas |
| IMS077_3, `incual-IMS077_3.txt` | UC0216_3 CR3.5, CR3.7; UC0217_3 RP1, CR1.3, CR1.6, CR2.5, CR3.5; UC0218_3 CR2.3; MF0217_3 CE1.5 (cada criterio situado bajo su UC o MF por número de línea) | Literales y atribuciones exactos |
| RD 1680/2011 (BOE-A-2011-19599) y RD 500/2024 (BOE-A-2024-10685) | Fechas de la tabla «Normativa»; qué modifica el RD 500/2024 del 1680/2011 | Arts. 2, 10, 12, 15 y anexos I (módulos transversales, FCT, «Proyecto intermodular») y III. No toca los arts. 5 y 9 ni los módulos 0905 y 0909 |
| Vizrt, *Viz Trio User Guide* 4.6, «Introduction» (documentation.vizrt.com) | Las diez citas | Literales. Las rutas 4.7, 4.8, 5.0 y 5.1 dan 404 |
| Frame.io, help.frame.io, arts. 9105251, 9101068 y 9105311 | Las ocho citas (comentarios, tramo, anotación: 9105251; pilas de versiones: 9101068; estados: 9105311) | Literales. Adobe: pie «© 2025 Adobe Inc.» de frame.io |
| mosprotocol.com (portada) | Nombre de MOS, para las siglas | «Media Object Server Communications Protocol (MOS)» |
| Temas 3, 6, 7, 8, 9, 12, 14 y 18 de Grafista | Remisiones del T17 (error 1) | Todas existen; tema 3 tiene «Diseñar, rellenar y lanzar» |

Lentes (ENCARGO, el tema cita normas):
- `negritas.py` contra el LE, el convenio, IMS077_3, BOE-A-2011-19599, la LPRL, las páginas de Vizrt y Frame.io y el T18 de Realizador/a: 198 cotejadas y 11 «no está». Las 11 son falsos positivos, revisados a mano: ligaduras ﬁ/ﬂ del .txt del LE, el corte […] y las comillas tipográficas de Frame.io, y los dos rótulos en negrita del pasaje copiado del Montador.
- `refutar_exactitud.py` con la LPRL: 25 «no literales». Son falsos positivos, porque lee los números del LE («LE 6.5.1») como si fueran artículos de la LPRL. La LPRL sólo se cita por remisión, dentro de pasajes copiados.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 0 hallazgos.

## 3. Correcciones aplicadas (cada una comprobada en la fuente)

1. **Error 4/6, «Los rótulos que no pueden faltar».** La entrada decía que el LE «obliga a poner» todos los
   rótulos de la tabla y que «fija su duración: todo el tiempo que la imagen esté en pantalla». Sólo es así en
   reconstrucción (3.2.2, 9.2.12.3) y archivo (9.9.1). La intro es **«Suele ser necesaria»**, la entrevista
   **«al menos en una ocasión»** y el total en lengua extranjera **«Es preferible»**. Se ha reescrito la entrada.
2. **Error 6, 9.2.12.3.** Faltaba la condición: el rótulo es obligatorio cuando el montaje de ficción
   **«sea inevitable»**. Se ha añadido.
3. **Error 6, 9.9.1.** Se ha añadido que el LE lo dice en el capítulo de asuntos comprometidos, a propósito
   del archivo que ilustra reportajes sobre delincuencia, malos tratos o asuntos judiciales.
4. **Error 9, LE 8.1, punto 9.** El tema atribuía al LE que el error lo reconoce «el presentador». El punto 9
   habla del periodista en una conexión en directo. Queda como oficio, y la cita va con su antecedente
   (**«para solventar cualquier inconveniente que surja, hacerlo con naturalidad…»**), en el epígrafe y en el
   paso 5 del segundo supuesto.
5. **Error 3, ficha del Grafista.** «Dos de sus cuatro tareas miran a otras áreas» chocaba con el tema 7,
   que es lectura de oficio y cuenta tres. Pasa a «dos nombran el trabajo de otras áreas», que es lo que dicen
   las dos citas.
6. **Error 9, Advertencia.** «El LE […] es el único documento de la casa que habla de urgencia…» no se puede
   confirmar. Pasa a «el documento publicado de la casa, de los leídos para este tema, que habla…».
7. **Error 5, sigla MOS.** No se presentaba. Se añade a las siglas: *Media Object Server*, según
   mosprotocol.com. La fuente entra en «Trazabilidad».
8. **Error 3, portada.** La LPRL figuraba «(artículos 14.2 y 15.1.g)», y la tabla «Normativa» cita además
   el 29.2.4.º. Se unifica. La salvedad del RD 500/2024 pasa a «no toca los artículos ni los módulos que se
   citan». La extensión pasa a 11.900.
9. **Trazabilidad.** El 8.1, punto 9 y la frase del 5.6 «Una buena previsión…» son lectura propia de este
   tema, no de los temas cerrados, y se pasan a las fuentes nuevas con su página.

Se han releído los pasajes cambiados. Cada «ese», «el mismo apartado» y «el epígrafe N» tiene delante su
antecedente.

## 4. Comprobado sin cambios

- Aviso 1 del redactor: el párrafo «El redactor ha de fijar…» está en la p. 89, entre el final del 6.1.2
  (centros territoriales) y el 6.2, sin rótulo propio. La fórmula del tema, «LE 6.1, párrafo que sigue al
  6.1.2», lo describe bien y se mantiene.
- Las dos citas de «3.16» (p. 58) van detrás del texto del 3.16.2 «Microeconomía», dentro del 3.16, pero
  tratan de los gráficos en general. La cita «LE 3.16» es correcta.
- Lectura de este tema que se mantiene porque está declarada como tal: que la alternativa ante un gráfico
  que no llega la decide el editor. El LE 5.6 dice que el retraso **«debe ser comunicado a los editores para
  que tomen una decisión»** y que la Redacción **«está obligada a encontrar una alternativa inmediata»**.
- Marcas de oficio: las listas de buenas prácticas, la tabla de estresores del grafismo y los dos
  supuestos van marcados como tales.

## 5. Lo que no se ha podido confirmar

Nada queda afirmado sin fuente. Sin leer: la NTP 926, que el tema ya declara no leída.

## Ficheros tocados

- El tema 17, sólo en los pasajes del apartado 3.
- Este informe.
