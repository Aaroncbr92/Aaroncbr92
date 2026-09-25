# Puesto 30 · Tema 5 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/05-montaje-de-noticias.md`.

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), txt local | Introducción (p. 9), 3.2, 3.2.2 (p. 46, música), 3.8, 3.9, 3.9.1, 3.10, 3.13, 5.3.1-5.3.3 (pp. 80-82), cap. 6 intro, 6.1-6.1.2, 6.2.2, 6.3-6.4 (pp. 90-92), 9.2.11.3 (p. 128), 9.10.1 (p. 168); búsqueda de «cierre» y «música» en todo el libro | 25-09-2026 |
| `temas/realizacion/02-el-guion.md` § 8 (RTVE) | Cotejo literal de lo copiado y lo adaptado | 25-09-2026 |
| `temas/canal-sur-especificos/34-redactor-a/07-...md` | Cotejo literal de lo copiado del común | 25-09-2026 |

## Método

- «Copiado del común» (20 tramos de T07 listados por el redactor): script por bloques (párrafo, fila,
  viñeta) contra T07. Todos literales. No re-verificados.
- «Copiado de RTVE sin cambios»: cotejado a mano con § 8 RTVE; literal salvo la negrita quitada, declarada.
  No re-verificado. Lo adaptado de RTVE es vocabulario declarado oficio; los cortes coinciden con lo que
  dice el informe de redacción.
- Todo lo demás (líneas que no están en T07): cada negrita (≈180 segmentos) buscada normalizada en el txt
  con página y epígrafe; cada afirmación en redonda releída en su pasaje. Las únicas negritas que no casan
  están dentro de lo copiado del común (Totales «deben reflejar…», y tres citas del Manual de RTVE, otra
  fuente).
- Lentes: tema sin norma → `refutar_prosa.py` (0 hallazgos) e `indice.py` (7.286 palabras; ficha 7.300, se deja).

## Hallazgos y correcciones

1. **Error 3 · recuento.** § 2: «El texto completo de dos de ellas, que dan las cifras…» precede a tres
   citas (6.3.2, 6.3.3, 6.3.4), y ninguna da las cifras. Ahora: «Los ejemplos de selección que el libro da
   en tres de ellas:».
2. **Error 3 · cálculo.** «unos tres segundos de media por plano si se usan veinticinco»: 60/25 = 2,4 s.
   Ahora: tres segundos con veinte planos, dos y medio con veinticinco (cálculo propio, dicho).
3. **Error 6 · salvedad omitida.** Introducción del Libro (p. 9): tras «no hay elección posible», las
   normas «han de tomarse con una prudente elasticidad… pero en modo alguno pueden incumplirse o tomarse
   a la ligera». Añadido, porque «las duraciones son referencias» sin ella induce a error.
4. **Error 9 · sin fuente.** «Está escrito para el redactor y el cámara»: el libro dice «destinado a los
   profesionales de la información en televisión». Sustituido por la cita.
5. **Error 6 · salvedad omitida.** § 1, 6.1.1: el equipo de edición «está obligado a trasladar… el nombre
   asignado por el autor del trabajo o, en su caso, adaptarlo»; faltaba «o adaptarlo». Reescrito con cita
   (p. 88). El mismo recorte está en la frase copiada de T07 (l. 185): no se toca; nota para T07.
6. **Error 8/1 · epígrafe mal.** Tabla de formatos: «con holgura» iba en la fila de colas (3.9); la holgura
   está en 3.9.1 (colas + total). Movida; añadido «en piezas separadas».
7. **Error 9.** § 3: «La razón de separarlas es la holgura de las colas» no lo dice el libro (sólo pide
   ambas cosas en la misma frase). Reescrito como lectura de oficio.
8. **Error 9 · literalidad.** 5.3.3: «ponerlo a cero al principio de la grabación» → «poner el marcador a
   00:00:00 al principio de la cinta», como dice el libro.
9. **Error 4/9.** § 7: «admite música como regla y no como excepción» contradice 3.10 («contra la norma
   general… sí puede ser oportuna»). Reescrito con las citas de 3.10 y 3.2.2 (p. 46).
10. **Error 6 · salvedad omitida.** 9.2.11.3 (p. 128, malos tratos): «que en los cierres descartemos
    cualquier orientación melíflua o simplemente estética». Añadida en § 7 y en la Trazabilidad.
11. Menores: tabla, intro «Nadie» → «Nadie (a veces acoge una declaración)» (3.13); § 6 «En la práctica
    de Canal Sur» → «En el modelo habitual que describe el Libro de estilo» (el dato es de 2004).

Sin hallazgos en: páginas y epígrafes de todas las citas propias; siglas (CSTV, TC, cabina de montaje/
edición, *vidiwall*, *stand up*, *preroll* constan en el libro); «podrá/deberá»; «sólo llama "cierre"
al segundo» (los otros usos del libro, 9.2.11.3 y 9.10.1, también son final de informativo).

## Observaciones sin cambio (en lo copiado del común)

- 6.2.2, defecto 3: la cita corta «y de la capacidad de comprensión de los espectadores».
- l. 185: omite «o, en su caso, adaptarlo» (ver 5).

## Ficheros tocados

- Modificado: el tema 05. Creado: este informe. Ningún otro.
