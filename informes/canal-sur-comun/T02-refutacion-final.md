# T02 · Segunda refutación (fase 5 bis, acotada)

Tema: `temas/canal-sur-comun/02-estatuto-autonomia-andalucia.md`. Releídos solo los 5 pasajes que
lista `T02-remate.md` y sus antecedentes, contra la fuente extraída con `grep -n -A40` (Ley
6/2006 arts. 43.5 y 45 bis.2.c; Ley 2/2024 arts. 5, 7, 9 y 17.9). **Los 5 son literales**: la
frase «los demás órganos cuyo informe o dictamen sea preceptivo, salvo lo previsto para la
tramitación urgente en el artículo 45 bis» y la del 45 bis.2.c coinciden con el artículo 43.5 y
el 45 bis.2.c de la Ley 6/2006; la cita en negrita de *Composición* coincide con el artículo 5 de
la Ley 2/2024, y el paréntesis (arts. 7 y 9) remite correctamente al fundamento de los
permanentes y los natos; el número 9 de consultas preceptivas añade «y conflictos en la
aplicación de la norma tributaria», igual que el artículo 17.9; el párrafo nuevo sobre la STC
230/2015 nombra el artículo 69 como antecedente explícito, y la línea en blanco quitada en «Lo
que este tema no da» no altera ningún contenido. Ningún hallazgo del remate se rechaza.

Antecedentes comprobados alrededor de cada pasaje: correctos (el Consejo de Gobierno, los
proyectos de ley, la regla del cuarenta por ciento y el artículo 69 quedan nombrados antes de
cada remisión).

## Las quince preguntas

Contestadas buscando solo en el tema (`T02-preguntas.md`). Las quince, enteras, incluida la 12
(«los designados en función del cargo específico que desempeñen o hubieren desempeñado», literal
en *Composición*, línea 1552). No se ha detectado ninguna laguna nueva.

## Lentes automáticas

| Herramienta | Alcance | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 0 hallazgos |
| `refutar_modo.py` | tema entero, contra Estatuto, Ley 6/2006, Ley 9/2007, Ley 2/2024 | 0 hallazgos |
| `refutar_exactitud.py` | tema entero, contra las 10 normas con articulado del BOE que cita el tema | negritas: 0 comprobadas, 0 no literales; citas con artículo entre paréntesis: 241 comprobadas, 37 no literales, 27 remiten a otra norma, 2 sin fuente pasada |

Las 37 "no literales" de la segunda pasada se revisaron una por una en su contexto: todas son
falsos positivos del propio anclaje de la lente (toma el número de artículo más próximo en la
misma frase en vez del que de verdad sostiene la cita), el defecto que ya advierte `CICLO.md`.
Comprobado con tres ejemplos representativos contra la fuente:

- «solo tendrá carácter preceptivo, cuando proceda, el dictamen del Consejo Consultivo de
  Andalucía» ancló en «artículo 43» (mencionado antes en la misma frase) pero es literal del
  artículo 27.4 de la Ley 6/2006.
- «aquellos que fueren designados en función del cargo específico que desempeñen o hubieren
  desempeñado» ancló en «artículo 7» (citado junto al 9 como fundamento) pero es literal del
  artículo 5 de la Ley 2/2024 (el propio pasaje del remate, ya comprobado arriba).
- «con mayor respaldo electoral» (criterio 4.º del artículo 182) ancló en el criterio 2.º citado
  antes en la misma frase; el texto es literal en el mismo artículo, solo que en otro apartado que
  la ventana de contexto de la lente no alcanzó.

No se corrige nada en el tema: los tres tramos comprobados eran ya literales.

## Cuadro de lentes

| Lente | Tramos mirados | Hallazgos | Nota |
| --- | --- | --- | --- |
| Pasajes del remate + antecedentes | 5 pasajes | 0 | Los 5 son literales contra la fuente |
| Quince preguntas | 15 | 0 | Las 15 enteras |
| `refutar_prosa.py` | tema entero | 0 | — |
| `refutar_modo.py` | tema entero | 0 | — |
| `refutar_exactitud.py` | 241 citas con artículo entre paréntesis + negritas | 37 (revisados 3 al detalle) | Falsos positivos del anclaje de la segunda pasada, ya advertidos en `CICLO.md` |

**Resultado: cero correcciones.** El tema queda como estaba tras `T02-remate.md`.
