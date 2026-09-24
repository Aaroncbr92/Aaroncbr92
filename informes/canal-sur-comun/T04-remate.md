# T04 · Remate (fase 5, modo ahorro) · Ley 13/2022 y Ley 10/2018

Tema: `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md`. Hallazgos aplicados:
`informes/canal-sur-comun/T04-refutacion.md` (C1, C2, E1 a E5, P1). Leídos antes `ENCARGO.md` y
`CICLO.md` enteros (con los dos modos ahorro). **Fecha de lectura de todos los preceptos:
24-09-2026**, redacción vigente ese día, con `boe.py precepto` (y `--fecha` para las redacciones
anteriores) o `grep` sobre los volcados de `fuentes/canal-sur/`. Las resoluciones del Tribunal
Constitucional (`BOE-A-2020-4873`, `BOE-A-2021-13034`) y la nota del bloque 37 las leí en el BOE
(XML del diario y API de legislación consolidada).

**Resultado: los ocho hallazgos se confirman en la fuente y se aplican.** Ninguno se rechaza. Dos
ajustes sobre el texto propuesto, explicados abajo (C1 y C2).

## 1. Correcciones

| # | Dónde | Comprobado en | Qué se hizo |
| --- | --- | --- | --- |
| C1 | Menores, Ley 13/2022 | 123.3.a, 123.4 a 123.8, 85.1, 158.16, 66.3.c.2.º (Ley 10/2018) | Nuevo epígrafe «Artículo 123. Franjas de la publicidad de esoterismo, juego y alcohol», con literales de 123.6, 123.7 (y su segundo párrafo), 123.8, 123.3.a, 123.4 y 123.5. Añadido que rige en radio salvo el 123.5 (85.1, literal). Infracción 158.16 añadida a la lista. En el 41.2.a) andaluz, frase que remite al 123.6-8 |
| C2 | Menores, Ley 13/2022 y 41.2.c) | 129.2, 131.3, 138.3, 85.3, 158.19, 158.20, 158.23 | Nuevo epígrafe «Artículos 129, 131 y 138. Los programas infantiles», con los tres literales; exclusión igual en radio (85.3); 138 solo televisión lineal (está en la sección 3.ª). Infracciones 158.19, 20 y 23 añadidas. En el 41.2.c), contraste con el 129.2 |
| E1 | Trazabilidad, punto 5 | `BOE-A-2020-4873` (admisión: art. 28, apdos. 4, 6, 11-15; 161.2 CE solo para 6 y 11-15), `BOE-A-2021-13034` (recurso contra art. 28.4 y 6; 11-15 por conexión), nota del bloque 37 («por el art. 28.3 y 4 del Decreto-ley 2/2020»), nota del bloque 40 (suspensión de la supresión por el 28.6) | Sustituida la frase «asocian ese recurso al artículo 40, no al 37» por la explicación de los dos preceptos |
| E2 | Art. 46, fila del Decreto-ley 3/2024 | 46.5 en 2019, 2022 y vigente | Añadido que el plazo de quince años pasa a ser solo del servicio local y que la condición de renovación pasa del art. 28 de la Ley 7/2010 al 29 de la Ley 13/2022 |
| E3 | «Cómo encajan las dos leyes» y art. 43 | 43.1 en 2019 («artículo 12 de la Ley 7/2010») y vigente; 54.1 en 2019 («artículo 40.2 de la Ley 7/2010») y vigente; 9.3 vigente | Lista completada: «entre otras (3.1, 9.3, 35.1, 43.1 y 54.1)»; «Donde pasa, el tema dice qué decía…». Línea de cambio de remisión en el 43.1 y en el 54.1 (esta, junto a E4) |
| E4 | «Otras piezas», art. 54.3 | 54.3 vigente | Añadida la segunda frase («No obstante, podrá recibir contribuciones…»), con dos incisos literales |
| E5 | Art. 109.1 | 109.1 | «**en lo estatal**» sustituido por el literal «**en lo referente a los servicios de comunicación audiovisual de ámbito estatal**» |
| P1 | Identificación de la Ley 13/2022 | tsv de redacciones (una por bloque) | Texto propuesto por el informe, sin «volcada» ni «bloques» |

Ajustes sobre lo propuesto:

- **C1, art. 41.2.a).** El informe proponía decir que la regla estatal es «más estricta». No lo
  pongo: la redacción andaluza de 2018 ya tenía la franja de 1:00 a 5:00 para esta publicidad en
  el art. 32.d) (leído con `--fecha 20190101`), y el 123.8 admite excepciones. El tema dice solo lo
  que la fuente sostiene: que rigen las franjas del 123 y que se aplican a toda la programación, no
  solo al horario de protección.
- **C2, art. 41.2.c).** No digo que la regla andaluza «vaya más allá»: digo que tiene otro alcance
  (programas con importante audiencia infantil, dentro del horario de protección de menores al que
  se refiere todo el 41.2).
- Por C1 y C2, en «Lo que este tema no da» se matiza «comunicaciones comerciales en general»: el
  tema sí da los arts. 123.3.a, 123.4 a 123.8, 124, 129.2, 131.3 y 138.3. En «Normativa que el tema
  invoca» y en la trazabilidad (punto 2), los arts. 43 y 54 pasan a tener cadena leída en su
  apartado 1.

La pregunta 9 de `T04-preguntas.md` se contesta ahora entera con el art. 123.7-8 del tema.

## 2. Pasajes cambiados (para la fase 5 bis)

Números de línea del tema rematado.

| Líneas | Sección | Cambio |
| --- | --- | --- |
| 12 | Portada | Extensión: 19.370 palabras (cifra de `indice.py`) |
| 89-92 | Normativa del sector › La Ley 13/2022 | P1 |
| 270-273 | Normativa del sector › Cómo encajan las dos leyes | E3 |
| 562-570 | Principios › Ley 10/2018 › Autorregulación (art. 43) | E3 (cambio de remisión del 43.1) |
| 758-765 | Protección de menores › En la Ley 13/2022 (entrada) | Anuncia 123, 129, 131 y 138 |
| 908-953 | Protección de menores › Ley 13/2022 › Artículo 123 y Artículos 129, 131 y 138 | C1 y C2 (epígrafes nuevos, `####`) |
| 955-966 | Protección de menores › Qué infracciones son y quién sanciona | 158.16, 19, 20 y 23 |
| 1052-1058 | Protección de menores › Ley 10/2018 › Artículo 41.2, letra a) | C1 |
| 1064-1067 | Ídem, letra c) | C2 |
| 1191-1196 | Accesibilidad › Artículos 105 a 109 | E5 |
| 1659 | Servicio público › Ley 10/2018 › Gestión (art. 46), tabla | E2 |
| 1719-1726 | Servicio público › Ley 10/2018 › Otras piezas | E4 y remisión del 54.1 |
| 1734 | Normativa que el tema invoca, fila de la Ley 10/2018 | Cadenas de 43 y 54 |
| 1768-1771 | Lo que este tema no da | Matiz de comunicaciones comerciales |
| 1798-1802 | Trazabilidad, punto 2 | 43 y 54 |
| 1811-1818 | Trazabilidad, punto 5 | E1 |

**Antecedentes comprobados** en esos pasajes y en los que remiten a ellos: la entrada de
«Protección de menores» (anuncia los nuevos artículos), el art. 83 y el 99.5-6 (a los que remite
«las mismas franjas»), el 41.2 («esa publicidad», «todo el artículo 41.2»), el 124 («El artículo
124 no fija franjas»), el párrafo de infracciones («todas ellas», dentro de 157 y 158.7 a 30 del
66.3.c), el 85.1 y 85.3 citados por su número, la tabla del art. 46 y la de reformas (que ya
nombraba el art. 40). Todos tienen delante su antecedente. El índice no cambia: los epígrafes
nuevos son `####` y el índice llega a `###`.

## 3. Lentes automáticas

Corridas sobre el tema rematado con `BOE-A-2022-11311`, `BOE-A-2018-15240`, `BOE-A-2005-655` y
`BOE-A-2007-5825`:

```
indice.py             19370 palabras · 22 epígrafes
refutar_prosa.py      hallazgos de prosa: 0
refutar_exactitud.py  negritas comprobadas: 465 ; no literales: 142
                      citas con el artículo entre paréntesis: 115 comprobadas ; no literales: 43
                      sin comprobar: 13 remiten a otra norma ; 0 con un artículo que no está en las fuentes dadas
refutar_citas.py      tramos de cita comprobados: 1 ; no literales: 0
refutar_modo.py       hallazgos: 21
refutar_documento.py  no aplica: el tema no se apoya en documentos fuera del BOE
```

Diferencia con la refutación (442/134, 114/43, 12, 21), obtenida corriendo las lentes sobre las
dos versiones y comparando las salidas:

- **Negritas: +23 comprobadas, +8 no literales netas.** Sale una: la de E5 («en lo estatal»),
  corregida. Entran nueve, todas falsos positivos: seis rótulos en negrita de los epígrafes nuevos
  («Esoterismo y paraciencias (123.6)», «Juegos de azar y apuestas (123.7)», «Excepciones a la
  franja del juego (123.8)», «Emplazamiento de producto (129.2)», «Televenta (131.3)»,
  «Interrupciones publicitarias (138.3)»), como los rótulos ya existentes del tema; dos literales
  del 131.3 y del 138.3 que la lente ancla en el art. 129 por el título «Artículos 129, 131 y 138»
  (cotejados a mano: literales); y el inciso del 85.1 («salvo la limitación horaria…»), anclado en
  el 123 por nombrarse antes en la frase (literal en el 85.1). Una negrita nueva no literal de
  verdad («entre las 20:30 y las 5:00 horas») la detectó la lente y la corregí al literal «entre
  las 20:30 horas y las 5:00 horas».
- **Paréntesis: +1 comprobada, sin nuevas no literales. Sin comprobar: +1**, remite a otra norma
  (la Ley 7/2010 o la Ley 13/2022 nombradas en los añadidos de E3/E4).
- **Modo: 21, idéntico** línea a línea a la salida anterior (salvo la lista de artículos con
  numeración coincidente del aviso inicial). Las 21 siguen explicadas en `T04-verificacion.md`.
- **Prosa y citas: 0**, sobre el tema entero.

## 4. Ficheros tocados

- Editado el tema 4 y creado este informe. No toqué `T04-preguntas.md` ni `fuentes/`.
- Una primera llamada a `indice.py` sin argumentos falló en su arranque sin escribir nada (`git
  status` limpio salvo el tema 4 justo después). Después apareció modificado
  `temas/canal-sur-comun/01-constitucion-espanola.md` (cambios de contenido en la LBRL): no es mío,
  es de otro agente.
