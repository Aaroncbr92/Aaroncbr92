# Grafista (15) · Tema 4 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/04-infografia-y-visualizacion-de-datos.md`. Fecha de trabajo
del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema). No se corrige: sólo se informa.
Ficheros tocados: este informe y `15-T04-preguntas.md`.

Saltado en exactitud (según `15-T04-redaccion.md`): lo «Copiado del común» (Redactor/a, T15) y lo «Copiado
de RTVE sin cambios». La cobertura mira el tema entero.

## Método

- Todas las negritas cotejadas por script (normalización de comillas, guiones, ligaduras y espacios)
  contra: Carta 2024-2029 (`carta-servicio-publico-2024-2029-boja-247-2023.txt`), Contrato-programa
  2024-2026 (`contrato-programa-2024-2026-boja-245-2023.txt`), Libro de estilo (`libro-de-estilo-333233b.txt`),
  WCAG 2.2 y las dos guías del Analysis Function (copias de la fase 1 en el scratchpad, `g15a/`) y
  BOE-A-2007-19814. Tres «no encontradas»: LE 3.16.1 y 9.2.10 (bloque copiado, salto de página, ya
  explicado por el verificador) y la cita en bloque de la alternativa textual (sólo por el «>» del
  markdown; leída a mano, literal).
- Leídos a mano el contexto de Carta 7.1/10.1, Contrato-programa puntos 16, 28 y 48, LE 3.2.2, 6.5.1,
  6.5.2, 9.2.12.3 y el índice del capítulo 9; y en las guías: título(s), corte del eje y tuit de la OSR
  (27-II-2023), series temporales en barras, proporción, alternativa y marcado decorativo, SVG, legislación
  británica, contraste de texto 4,5:1 y su razón, daltonismo, escala de grises, fondo.

## Hallazgos de exactitud

### Graves (1)

- **G1 · §4 «Qué obliga a la casa», primera viñeta** (error 9, y contradice el §1). Dice que la Carta 10.1
  «Es la única mención expresa de la ética de lo infográfico en un documento de la casa». Falso: el
  Contrato-programa, cláusula tercera, punto 28, tras «argumentales, textuales, infográficos, o narrativos
  de tratamiento de redacción periodística», sigue **«estando siempre conformes con la deontología
  profesional y códigos de autorregulación profesional que rigen la actividad de los medios de Canal
  Sur.»** El propio §1 dice que el Contrato-programa «repite la fórmula». Propuesta: «La Carta (10.1) y el
  Contrato-programa (cláusula tercera, punto 28) son las dos menciones expresas…», o quitar la frase.

### Menores (3)

- **M1 · §4 «Reconstruir no es informar», segunda viñeta** (error 8/6, encuadre). «En los sucesos
  (9.2.12.3…)»: el 9.2.12.3 está dentro del 9.2 **«Malos tratos»** (9.2.12 «Los modelos informativos»), no
  en una regla general de sucesos. El propio tema, en §5, sitúa bien el 9.2.10 «dentro del apartado 9.2
  sobre malos tratos». Propuesta: «En la información sobre malos tratos (9.2.12.3, …)», o añadir que la
  regla, aunque escrita para ese apartado, se formula en términos generales.
- **M2 · misma viñeta** (error 6, salvedad omitida). El 9.2.12.3 da, antes del rótulo obligatorio, una
  alternativa: **«En caso necesario, podemos usar una imagen subjetiva de cámara para reconstruir los
  hechos a través de sus escenarios, sin la referencia principal de ningún personaje o actor.»** Y avisa de
  que **«También es arriesgado el recurso de usar escenas cinematográficas como ilustración»**. La
  alternativa es justo la que más interesa a una infografía de proceso (recorrer el escenario sin
  personajes). Añadirla.
- **M3 · Siglas** (error 5, inverso). Se presenta «LRISP» y no se usa en el cuerpo (el texto dice siempre
  «Ley 37/2007»). Quitarla de las siglas o usarla. Inocuo; ya lo anotó el verificador.

### Comprobado sin hallazgo

Carta 7.1 y 10.1 (rótulos y literales); Contrato-programa 16, 28 y 48; LE 3.2.2 (rótulo, literal, supuestos
de muerte, heridas, suicidios o abuso), 6.5.1 (rótulo «Delegación»), 6.5.2 (rótulo, «vidi wall», salvedad
«deberá»); tabla de relaciones y resto de literales de *charts*; fecha de publicación de *charts*
(19-05-2022) y de actualización de *colours* (12-02-2026); tuit de la OSR y cifras del 11,1 % y 10,1 %;
«at least one title… best practice… two»; barras en series sólo a intervalos iguales; «Do not use a key»
en el apartado de sectores; artículo externo de la proporción; marcado decorativo con alt vacío; WCAG 2.2
(fecha, 1.1.1 y excepción decorativa, 1.3.3, 1.4.1, 1.4.3, 1.4.11, fórmula, rango, texto grande). Cuentas
rehechas: correctas.

## Cobertura del enunciado

«Infografía y visualización de datos: claridad, rigor, ética, fuentes y representación accesible»: cada
elemento tiene su epígrafe y el orden es el del enunciado. Resultado del test (15 preguntas, en
`15-T04-preguntas.md`): 11 enteras, 1 a medias, 3 no. De los tres «no», dos se deben a M1 y M2 y uno a una
laguna.

### Laguna (1)

- **L1 · El color como codificación de datos** (claridad y representación accesible). El tema trata el
  contraste, el daltonismo y la escala de grises, pero no cómo se eligen los colores de un gráfico, que la
  guía *Data visualisation: colours* (la misma que ya cita) desarrolla y que es trabajo diario del
  grafista: **«Limit the number of colours you use»**; con datos categóricos que no se agrupan, un solo
  color (**«When you have categorical data that cannot be grouped, use a single colour.»**); **«Use colour
  consistently»**; **«Consider colour associations»**; paleta categórica y **«We recommend a limit of four
  categories as best practice for basic data visualisations.»**; paleta secuencial (**«it is best to use a
  single hue, or small set of closely related hues. You should change the lightness from pale to dark,
  rather than alternating between hues»**, que sólo se use **«when absolutely necessary»** porque sus
  contrastes **«do not meet accessibility standards on their own»**; ejemplo del mapa por quintiles, del
  azul más claro para las tasas más bajas al más oscuro). Encaja en §6 «Color, contraste y formato», o en
  §2, y conecta con el mapa de coropletas de §3. Unas 200-250 palabras. Preguntas 2 (a medias) y 12 (no).

## Resumen

Graves 1 · menores 3 · lagunas 1. El tema es sólido: negritas literales salvo las explicadas, cuentas correctas y oficio
declarado como tal. El remate es corto: corregir la frase de G1, reencuadrar y completar el 9.2.12.3
(M1, M2), resolver LRISP (M3) y ampliar L1 (esta ampliación exige fase 5 bis).
