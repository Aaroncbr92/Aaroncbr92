# Grafista (15) · Tema 15 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/15-innovacion-ia-generativa-etica-visual-validacion-humana-deepfakes-trazabilidad.md`.
Fecha del encargo: 24-09-2026. Fuentes releídas el 29-09-2026 (fecha de sistema). Ficheros tocados: el
tema y este informe. Copia previa del tema en el scratchpad (`t15.orig.md`), fuera del repositorio.

## Copiado del común: sólo comprobación de literalidad

Script (bloque a bloque, texto normalizado contenido en la fuente) contra el tema 19 y el tema 7 de
Redactor/a: todos los pasajes listados bajo «Copiado del común» en `15-T15-redaccion.md` son literales
(88 bloques coinciden, antes y después de las correcciones). No se han vuelto a verificar. «Copiado de
RTVE sin cambios»: ninguno, así que no hay nada que comprobar.

Los «copiados con ajuste» sí se verificaron: «(epígrafe 4)» es correcto (el art. 50 está en el
epígrafe 4); «No es un uso gráfico»; las citas de los arts. 14.4.b y 18.1.e EMFA y de los principios 1 y 3 de
la Carta de París coinciden con R19; la frase nueva de la viñeta DSA se ha corregido (abajo).

## Fuentes releídas (29-09-2026)

- RIA, volcado DOUE-L-2024-81079 (arts. 1, 3, 5, 14, anexo III), corrección DOUE-L-2025-81474 y Ómnibus
  DOUE-L-2026-81147 (art. 3 sin definición de «IA generativa»; art. 4; 111.4; 113 con b bis/b ter desde
  2-12-2026; vigor a los tres días de la publicación del 24-07-2026).
- **Considerandos 133 y 134, en el BOE** (`buscar/doc.php?id=DOUE-L-2024-81079`, descargado el 29-09-2026):
  las cuatro citas del 133 y la del 134 son literales. La corrección de 9-10-2025 cambia en el 134 sólo el
  término (frases 1.ª y 3.ª) y no toca el 133: confirmado.
- Comisión: preguntas del art. 50 (24-07-2026), noticia de las directrices (20-07-2026), página del
  Código (31-07-2026; cronología, secciones, 190 firmantes), iconos (24-09-2026). IPTC (noticia del
  10-06-2026 y *Digital Source Type*: los siete valores, nombres y definiciones), DLA Piper (16-07-2026),
  C2PA (definiciones 2.3.4, 2.3.6, 2.3.12, 2.3.13, 2.4.3, 2.4.4; principios; 18.14.4.5), Getty (April 2026),
  Adobe Stock.
- TRLPI art. 5 (1 redacción); RDL 24/2021 arts. 66.1 y 67 (1 redacción); LO 1/1982 art. 7.6 (vigente,
  última redacción del art. 7 de 2010); convenio, BOJA 240/2014, anexo III, ficha 5345100, p. 129.

Lentes: `negritas.py` (149 negritas; las 10 «no están» son las 4 del convenio y la de la LO 1/1982, cuyas
fuentes no se pasaron y se cotejaron a mano; las 4 del considerando 133, confirmadas en el BOE; y la de
C2PA con «…», que es una elipsis legítima). El aviso sobre el art. 111 es la cita del Ómnibus (art. 1 del
Ómnibus, que añade el 111.4): correcto. `refutar_exactitud.py`: 10 citas no literales frente al texto
original del RIA, todas explicadas (3.1 y 3.60 en redacción corregida, citas inglesas de la página de
la Comisión, art. 18 EMFA, 111.4 del Ómnibus, «séptimo» de la LO). `refutar_modo.py`: 0.
`refutar_prosa.py`: 1 aviso, «IA» en el título (falso positivo). `indice.py`: 42 epígrafes y el índice
no cambia.

## Correcciones aplicadas (error del catálogo)

1. Letra b bis del art. 5, en «Para el grafista…»: se presentaba como vigente y no se aplica hasta el
   2-12-2026 → «desde el 2-12-2026» (7/6).
2. «Fuera del alto riesgo, el RIA usa la intervención humana como condición en un solo sitio»: es falso
   (el art. 5.1.d también exceptúa el apoyo a la valoración humana) → «la intervención humana que interesa
   a este tema aparece como condición en…» (9).
3. Texto del grafista sin aviso si hay control editorial: faltaba la condición de que sea texto que
   informa sobre asuntos de interés público (6).
4. Caso «Vídeo para redes»: presentaba el icono como obligatorio. Ahora pone aviso incrustado y, si se usa
   el icono de la UE, que es voluntario, sus reglas de colocación (4).
5. C2PA: «digitalSourceType … toma sus valores del vocabulario IPTC». La especificación dice que es
   un término IPTC **o** un valor propio de C2PA (18.14.4.5). Ahora pone «clave de una acción» y los
   dos orígenes del valor (9). Se quita «abierta» de «especificación técnica abierta», que no consta en
   la especificación (9).
6. Viñeta DSA: «es lo que explica que las redes etiqueten por su cuenta…» era causalidad sin fuente →
   se quita (9).
7. Magic Mask: «el grafista la corrige fotograma a fotograma» se atribuía al tema 5 (fabricante). El
   tema 5 dice que se comprueba fotograma a fotograma y que eso es oficio → corregido y marcado como oficio (9).
8. Uso personal (preguntas del art. 50): la regla es para la «persona física», y la página cita la actividad
   «business, trade, occupational or freelance» → se añaden los dos matices (6).
9. Traducción de «closed loop industrial and product development environments»: faltaba «industrial y
   de producto».
10. DLA Piper: «end credits or the exhibition notes» → se añade «o en las notas de la exposición»;
    «(dónde, según el Código…)» → «según el resumen del Código», porque el Código no se ha leído.
11. Adobe Stock: la frase es para las salidas *Text to Image* descargadas de la página Generate → se precisa.
12. Siglas sin presentar: BOE, BOJA, LO, EBU → añadidas a la frase de siglas; «(LO 1/1982)» en su
    primera mención (5).
13. En «Qué es un sistema de IA», el párrafo sobre la IA generativa: la descripción no tiene fuente → «En
    el uso corriente…» (9).
14. «Deepfake no es un término de oficio sin más: el RIA lo define. El RIA le da nombre…»: la frase se
    repetía → «no es sólo un término de oficio. El RIA le da nombre…». La parte literal de R19 no cambia.
15. Ficha: se añade el artículo 1 a la fuente y la extensión pasa a 11.800. En «Trazabilidad» se añaden al
    RIA los apartados 5.1 bis y ter y el 111.4, y se anota que los considerandos 133 y 134 los releyó el verificador en el BOE.

Antecedentes: cada «ese artículo», «la letra» o «el mismo resumen» de los pasajes cambiados tiene delante
su referente (releídos).

## Comprobado sin cambios

Ficha del convenio (función y tres de las cuatro tareas, «Entre sus tareas»); la definición de responsable del
despliegue y la cita de empleados; los tres criterios y los cuatro factores; los fondos y efectos «not
likely»; la revisión humana, el control y la responsabilidad editorial; la vigilancia por autoridades nacionales;
el aviso perceptible; el calendario de la página; los iconos (4 variantes, 3 iconos con sus ejemplos, carácter
voluntario, licencia, colocación y accesibilidad); el Código (fechas, secciones, carácter, firmantes);
las medidas 1.1 y 1.2 según IPTC; la tabla IPTC; C2PA (manifiesto, credencial, enlaces duro y blando,
marcas de agua, principio de no valorar, opt-in, versiones 2.2 a 2.4); Getty (prohibición, «Training»,
usos permitidos); el TRLPI 5; el RDL 24/2021 66.1, 67.1 y 67.3; la LO 1/1982 7.6; el anexo III del RIA (sin usos
gráficos); el RIA sin definición de «IA generativa» (el Ómnibus sólo la usa en códigos de un anexo).

## Lo que no se ha podido confirmar (queda como hueco declarado en el tema)

Texto de las directrices y del Código (PDF); autoridad española del art. 50; firma del Código por la
RTVA; reforma española sobre *deepfakes* (la afirmación del tema es sólo que la búsqueda no dio nada, y así
se deja).
