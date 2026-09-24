# 34 · T07 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/07-redaccion-audiovisual-television.md`.
Entradas: `34-T07-refutacion.md` (0 graves, 6 menores, 1 laguna, 1 observación) y `34-T07-preguntas.md` (12 enteras, 2 a medias, 1 no).
Extensión: de 4.396 a 5.008 palabras (`indice.py`). **Amplía contenido nuevo** (§ 9, fuente nueva), así que toca la fase 5 bis sobre el subepígrafe nuevo de § 9 y las líneas de portada, «no da» y «Trazabilidad» que lo acompañan.

## Fuentes releídas (24-09-2026)

| Fuente | Cómo |
|---|---|
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), pp. 45-46, 49, 50, 52, 56-57, 116 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`, con `grep -n` / `sed -n` |
| Manfredi Díaz, A. (2010), «Escribir para televisión. La imagen manda», en R. Reig García (ed.), *La dinámica periodística*, Sevilla, Asociación Universitaria Comunicación y Cultura, pp. 129-145, ISBN 9788493760007 | idUS (Universidad de Sevilla), hdl.handle.net/11441/74192; PDF en la carpeta temporal y pasado a texto con `documento.py texto`; páginas comprobadas con PyMuPDF (la numeración impresa aparece como «!138» y siguientes) |

## Correcciones: todas confirmadas en la fuente y aplicadas

| # | Pasaje | Comprobación | Cambio |
|---|---|---|---|
| 1 | § 1 «Imágenes falsas y música» | LE 3.2.2, p. 46: literal | Añadida la frase del «procedimiento reprobable» y la salvedad «y siempre que no perturbe la narración, ni anule por completo el sonido natural» |
| 2 | § 4 lengua extranjera | LE 3.7.1, p. 52: el descarte de la voz superpuesta es general, y los subtítulos, preferibles en el total de 10-15 s | Frase reordenada; añadidos «especialmente en asuntos de especial gravedad o emotividad» y la tercera vía (desglosar en la locución encabalgada) |
| 3 | § 6 reglas de reportaje y crónica | LE 3.5, p. 49: literal | Añadido «Sólo es exigible la mención de la fuente cuando…» |
| 4 | § 11 «Versiones» | LE 3.15, p. 56: literal | Añadidos el supuesto «sin alterar la versión original» y «como norma general, siempre que pueda preverse» |
| 5 | § 7 «Tópicos» | LE 3.6.1, p. 50: literal | Añadido «ni conviene apoyarse en cifras de mucho detalle, sobre todo en el comienzo de frase» |
| 6 | § 11 «Vídeo recortable» | LE 3.2.1, p. 45: literal; la regla empieza por «Es muy recomendable», que el tema omitía | Añadidos «Es muy recomendable», «que deberá haber recibido al principio los elementos básicos de la noticia» y la precaución de los planos de transición que «'encabalguen'» |
| 7 | § 2, tabla, salidilla (la observación sin cómputo) | LE 8.2.2, p. 116: literal | Cita completada hasta «sino respuestas» |

## Laguna L1 (pregunta 15): ampliada en parte

- **Ampliado** (§ 9, subepígrafe nuevo «El guion en el sistema informático de la redacción»), con Manfredi (2010): Avid instalado en Canal Sur (p. 138, **dato de 2010**, dicho así); iNews como sistema de escritura de noticias con acceso a escaletas; el redactor recibe la noticia con la duración exigida y el lugar de emisión, y compone el texto insertando los rótulos (totales y localizadores) que van directos a emisión (pp. 139-140); edición de vídeo y guion y ajuste de audio y minutado (p. 139); claves sobre el guion (p. 143) y «Respete los tiempos que le marcan los editores» (p. 144).
- **No ampliado**: el guion a dos columnas (lo que pregunta la 15). Fuentes probadas y descartadas: `ual.dyndns.org/…/Unidad_08.pdf` (describe el formato de dos columnas, con la imagen a la izquierda, pero no tiene autor ni obra identificables, y el propio texto excluye de su método los productos periodísticos); Peña Rodríguez, *Diseño de guiones para audiovisual* (UAM Cuajimalpa, 2016), que excluye expresamente el guion de noticiarios (nota 2); Scribd, SlideShare, blogs (no son fuentes publicadas). El tema dice que no se ha encontrado fuente publicada. **La pregunta 15 no se recorta**: queda en «no», y su clave sigue sin confirmar. Hace falta un manual publicado (por ejemplo, de redacción o realización informativa en televisión) que no se ha podido consultar en línea.
- Se ha dejado fuera, adrede, el consejo de Manfredi de aparecer «mejor en el centro de la noticia» (p. 143), porque choca con el Libro de estilo (salidilla, «la fórmula más recomendable»), que es la fuente de la casa.

## Otros cambios

- Portada: «Fuente» y «Redacción que se estudia» incluyen Manfredi (2010); «Extensión» es ahora de 5.008 palabras. `indice.py` no reescribe la portada de este tema (no está en su .tsv: dice «sin portada»), así que la cifra se ha puesto a mano con el recuento del propio `indice.py`.
- «Lo que este tema no da»: la línea del guion dice ahora «disposición gráfica del guion informativo (columnas, marcas de total y colas)», y que el dato de Avid es de 2010.
- «Trazabilidad»: nueva fila para Manfredi (2010).
- Quitado de un primer borrador: la frase de que las dos columnas son «costumbre de oficio muy extendida», porque no tiene fuente.

## Pasajes cambiados, releídos y con sus antecedentes

1. § 1 «Imágenes falsas y música»: «Y **«La música…»**» sigue a la frase del procedimiento reprobable; no hay remisión colgando.
2. § 4, viñeta «En lengua extranjera»: «método» remite a la frase anterior (el desglose).
3. § 6, última viñeta: «historia. Sólo es exigible…» es continuación literal.
4. § 7 «Tópicos»: final literal.
5. § 2, tabla, fila «Salidilla».
6. § 11 «Vídeo recortable» y «Versiones»: «entonces» se refiere al supuesto que se acaba de nombrar.
7. § 9, subepígrafe nuevo: «Su ejemplo» y «según el autor» remiten a Manfredi, nombrado en la frase anterior; «sus claves» también remite a él.
8. «Lo que este tema no da», portada y «Trazabilidad».

## Lentes

- `indice.py`: índice rehecho (30 epígrafes, uno nuevo), 5.008 palabras.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py`, `refutar_exactitud.py` y `refutar_modo.py` no se han pasado: el tema no cita normas.

Ficheros tocados: el tema y este informe. Copia previa en la carpeta temporal (`T07-34-antes-remate.md`).
