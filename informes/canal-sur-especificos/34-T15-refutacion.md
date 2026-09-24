# 34 · T15 · Refutación (fase 4)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/15-periodismo-de-datos-informacion-publica.md`.
En esta fase no se corrige nada: las correcciones las aplica el remate. No se ha revisado lo que `34-T15-redaccion.md` lista bajo «Copiado del común» (Ley 9/2007 arts. 79 y 86; LTPA arts. 43 y 45; DA 2.ª LOPDGDD). Lo copiado de RTVE (estadística descriptiva) y los pasajes nuevos sí se han contrastado.

## Fuentes releídas (todas el 24-09-2026)

- LTAIBG, `fuentes/canal-sur/BOE-A-2013-12887.md`: arts. 2, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24 y 33; DA 1.ª y DF 8.ª.
- LTPA, `BOE-A-2014-7534.md`: arts. 2, 3, 6, 7, 8, 19, 24, 25, 26, 30, 31, 32, 33 y 34.
- LRISP, `BOE-A-2007-19814.md`: arts. 1, 2, 3, 4, 5, 8, 9 y 11 (redacción vigente).
- Libro de estilo, `documentos/libro-de-estilo-333233b.txt` (ligaduras normalizadas en copia del scratchpad): 3.3, 3.12, 3.12.1, 3.16, 3.16.1, 3.16.2, 4.3.2, 4.3.2.1, 7.1.3, 7.2.2 y 9.2.10.

## Lentes

`refutar_prosa.py`: 0 hallazgos. Las demás lentes se pasaron en la verificación, y el tema no ha cambiado desde entonces (`git diff` vacío).

## Hallazgos graves (0)

Ninguno. Todas las negritas contrastadas son literales y están en el precepto citado.

## Hallazgos menores (7)

- **M1 · §1, tabla «Plazos, silencio y reclamación» y viñetas (err. 6, salvedad omitida).** La reclamación se da como vía general. Pero el art. 33.2 LTPA dispone: «**Las resoluciones referentes al derecho de acceso a la información pública que sean dictadas por las instituciones y entidades a que se refiere el artículo 3.1.b) y 3.2 sólo serán recurribles ante la jurisdicción contencioso-administrativa.**» El 3.1.b) incluye el Consejo Audiovisual de Andalucía, que el propio tema nombra. En la ley estatal ocurre lo mismo con el art. 23.2 para los órganos del 2.1.f). Propuesta: una frase con las dos excepciones tras la tabla. Afecta a la pregunta 8.
- **M2 · §2 «Publicidad activa» (err. 1).** El tema dice «La transparencia, en sentido estricto, es lo que la Administración publica […]. La ley andaluza la define (artículo 2.b)». Pero el 2.b) define la «**Publicidad activa**», no la transparencia. Propuesta: «La ley andaluza define la publicidad activa (artículo 2.b) como…».
- **M3 · §4, LE 7.1.3 (err. 6).** La fuente empieza con «**Como norma general,** el resultado de una encuesta no debe ser nunca…», y el tema no lo recoge. Hay que añadirlo. Afecta a la pregunta 14.
- **M4 · §5, LE 3.16.2 (err. 6).** La fuente da primero una preferencia: «**Es preferible que digamos que la referencia Euribor de los tipos de interés ha subido 25 centésimas**», y luego admite lo del cuarto de punto. El tema sólo recoge esto último. Además, el 7.2.2 dice lo contrario: «No nos limitaremos a decir […] que los tipos de interés han bajado 25 centésimas sino […] un cuarto de punto». Conviene dar las dos preferencias y señalar que no coinciden.
- **M5 · §5, tabla de centralización (err. 9, contradicción interna).** Dice que la moda es «La única aplicable a variables cualitativas». Pero en «Variables estadísticas» el tema admite la mediana y los cuantiles en las ordinales. Propuesta: «La única aplicable a variables cualitativas nominales». Afecta a la pregunta 11.
- **M6 · §5, «Un cálculo, paso a paso» (err. 9).** Varianza y cuasivarianza se expresan en porcentaje: «es decir 2,17 %» y «es decir 3,25 %». Eso choca con lo que el tema dice antes, que la varianza está «en unidades al cuadrado». Propuesta: quitar la conversión a porcentaje de la varianza y la cuasivarianza, y mantenerla sólo en la desviación típica.
- **M7 · §4 y §5, prosa sin apoyo (err. 9).** «es un error de principiante» (l. 485) y «Es la distinción que más confusión genera» (l. 612) siguen en el texto. La verificación dio por quitadas frases de este tipo. Propuesta: suprimirlas.

## Lagunas de cobertura (2)

El enunciado pide «lectura e interpretación de datos, estadísticas básicas aplicadas a la información». El tema da la estadística descriptiva de manual, pero no la aritmética con la que trabaja una redacción. Todo lo que sigue es aritmética y se demuestra, así que puede ir como desarrollo propio, igual que el resto de los epígrafes 4 a 6.

- **L1 · Porcentajes y tasas (§5).** Faltan la diferencia entre variación porcentual y puntos porcentuales, la tasa de variación (interanual o sobre el periodo anterior), las tasas por habitante (por 1.000 o por 100.000) para comparar territorios de distinto tamaño y la diferencia entre valores nominales y reales (deflactar con el IPC, que el tema presenta pero no usa). Afecta a la pregunta 13.
- **L2 · Lectura crítica (§4 o §7, y §6).** Faltan dos cautelas: que correlación no implica causalidad y que un gráfico puede distorsionar (eje vertical que no empieza en cero, escalas distintas en gráficos que se comparan). El tema sí da una de estas distorsiones, la del histograma con intervalos desiguales. Encaja en «contexto» y en «visualización».

## Cobertura del enunciado

Las nueve materias del enunciado tienen epígrafe propio y van en el mismo orden. En «fuentes abiertas», el tema declara con honradez que no hay fuente, y lo que da tiene apoyo en la ley o en el Libro de estilo. Las dos lagunas son de estadística aplicada, no de las normas.

## Confirmado sin hallazgo

- LTAIBG: 2.1.d) y g), 2.2, 5.1-5.5, 12, 13, 14 (doce letras), 15.1-15.5, 16, 17.2-17.3, 18.1-18.2, 19.2-19.3, 20.1, 20.2, 20.4, 20.5, 22.1, 22.3, 22.4, 23.1, 24.1, 24.2, 24.4, 24.6, 33.1-33.2, DA 1.ª.3. La DF 8.ª no exceptúa el 20.4 (básico).
- LTPA: 2.a)-c), 3.1.b), c) e i), 6 (once principios), 7 (cuatro derechos), 8, 19, 24, 25.1-25.3, 26, 30, 31.2, 32, 33.1 (con la salvedad del artículo «la»), 34.1-34.2.
- LRISP: 1, 3.1.a) y b), 3.3.a), b), e), f) y j), 3.4, 4.1, 4.2, 4.5, 4.6, 4.7, 5.1, 5.3-5.5, 8, 9.1, 11.1, 11.3 y 11.4.
- Libro de estilo: 3.3, 3.12, 3.12.1, 3.16, 3.16.1, 3.16.2 («cama», claridad, orden, firma), 4.3.2, 4.3.2.1, 7.1.3 (puntos 1 a 3), 7.2.2 y 9.2.10.
- Ejemplo numérico: 0,05; 0,065; 0,02167 y 0,1472; 0,0325 y 0,1803. Es correcto.

## Preguntas

`34-T15-preguntas.md`: de 15 preguntas, 12 se contestan enteras con el tema, 1 a medias (11) y 2 no se pueden contestar (8 y 13).

Ficheros tocados: este informe y `34-T15-preguntas.md` (copia de trabajo del Libro de estilo en el scratchpad).
