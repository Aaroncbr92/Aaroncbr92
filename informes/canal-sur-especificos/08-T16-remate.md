# Puesto 08 · Tema 16 · Fase 5 · Remate

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/16-accesibilidad-y-diversidad-en-la-representacion-visual.md`.
Entrada: `08-T16-refutacion.md` y `08-T16-preguntas.md`.

## Fuente releída (24-09-2026)

*Libro de estilo* de Canal Sur (2004), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`:
índice (3.17.1.1 «Plano y encuadre»), 9.3.4.1 (l. 5033-5055), 9.3.5.1, 9.7 entrada, 9.7.1,
9.7.2.1, 9.7.2.2, 9.7.2.3 (norma 6), 9.7.3 (l. 6022-6160). Todas las propuestas del informe se
confirmaron en la fuente; ninguna se descartó.

## Pasajes cambiados

| # | Origen | Dónde | Antes | Después |
|---|---|---|---|---|
| 1 | E1 | § 2 «Pautas por situación», fila minoría/inmigración | «Imágenes de esa noticia, no de archivo ni de otra historia» | «Sólo imágenes de esa noticia (actuales o de archivo), no de otra historia» (9.3.5.1: «sean de acontecimiento actual o material de archivo») |
| 2 | E2 | § 2 «La mirada de la cámara en el Libro de estilo» | «Plano y entorno (3.17.1.1)» | «Plano y encuadre (3.17.1.1)», rótulo del Libro |
| 3 | L1 (amplía) | § 2 «El Libro de estilo: personas con discapacidad», al principio | — | Bloque nuevo sobre el capítulo 9.7 «Patologías físicas y psíquicas»: entrada (no usar imágenes que fomenten la confusión; pedir siempre autorización para grabar a la persona enferma, su entorno y quienes la atienden), 9.7.1 (imágenes alarmistas, morbosas o de lástima), 9.7.2.1 (no confundir en imagen patología mental con síndrome de Down o paraplejía), 9.7.2.2 (ejemplo del Día Mundial de la Salud Mental, «extraordinariamente grave»), 9.7.2.3 norma 6 (imágenes adecuadas). Todo en negrita literal. La frase que abre lo ya existente pasa a «Para las personas con discapacidad, el mismo capítulo (9.7.3…) dice:» |
| 4 | L1 (amplía) | § 2 «Pautas por situación» | — | Dos filas: «Persona enferma u hospitalizada» (9.7 entrada) y «Pieza sobre salud mental» (9.7.2.1-9.7.2.3, norma 6) |
| 5 | L2 (amplía) | § 2 «El Libro de estilo: inmigración y minorías», tras 9.3.2 | — | Viñeta del pueblo gitano (9.3.4.1, «Confusiones»): «una minoría que no lo es tanto en Andalucía», sólo se alude a la etnia si es relevante; ejemplo del cantaor y «jamás» en actividad laboral, social o política |
| 6 | Consecuencia | «Qué se puede preguntar» | «…los fondos y las personas con discapacidad;» | «…los fondos, las personas con discapacidad, la salud mental y el pueblo gitano;» |
| 7 | Consecuencia | Trazabilidad, fila del Libro | …9.3.2, 9.3.5.1-9.3.5.3…, 9.7.3.1 | añade 9.3.4.1, 9.7 (entrada), 9.7.1, 9.7.2.1-9.7.2.3, 9.7.3 |
| 8 | Consecuencia | Portada, Extensión | 10.700 palabras | 11.200 palabras |

El ejemplo del 9.7.2.2 se da sin el nombre propio de la persona que cita el Libro (paráfrasis en
redonda; lo literal va en negrita). Antecedentes releídos: «el mismo capítulo» remite al 9.7 del
bloque anterior; «Puede serlo» a «si es relevante».

## Preguntas tras el remate

La 4 (gitano), la 10 (archivo), la 11 (salud mental) y la 12 (autorización en hospital) pasan a
«entera». Recuento: entera 15 de 15.

## Lentes

- `indice.py`: 24 epígrafes, índice regenerado sin cambios de rúbricas.
- `negritas.py` contra el Libro: todas las negritas nuevas encontradas salvo la de 9.3.4.1 «pero
  jamás aludiremos…», que cruza un salto de página (pie «1 / 139 / LIBRO DE ESTILO…»); comprobada
  a mano, es literal.
- `refutar_prosa.py`: sin relleno ni repeticiones; avisa de «DAR», «LOGROS», «ROMPER» como siglas,
  que son mayúsculas literales de los rótulos de la Guía del CAA (preexistentes, no siglas).
- `refutar_exactitud.py` y `refutar_modo.py`: no se corren; los pasajes cambiados no citan
  ninguna norma del BOE/BOJA, sólo el Libro de estilo.

## Resultado

Se amplió contenido nuevo (L1 y L2): procede la fase 5 bis sobre los pasajes 3, 4 y 5.

## Ficheros tocados

El tema 16 y este informe.
