# Grafista (puesto 15) · Tema 14 · Fase 5, remate

Tema: `temas/canal-sur-especificos/15-grafista/14-gestion-proyectos-graficos-briefing-propuesta-revision-aprobacion-calidad.md`.
Encargo fechado el 24-09-2026; fuentes leídas el 29-09-2026 (fecha del sistema). Entrada:
`15-T14-refutacion.md` (G1, M1, M2, laguna L1) y `15-T14-preguntas.md` (6, 11 y 15 en «no»).
**Amplía contenido nuevo: sí** (epígrafe L1), así que toca la fase 5 bis.

## Comprobaciones en la fuente antes de aplicar

| Hallazgo | Fuente releída (29-09-2026) | Resultado |
|---|---|---|
| G1 | Frame.io, artículo 9952618 «Comparison Viewer» (copia descargada) | Confirmado: la nota «Static assets must have the same dimensions…» va bajo «Overlay view», antes de «Pixel difference view». Se aplica |
| M1 | Design Council, «Framework for Innovation» y «The Double Diamond» | Confirmado: sólo la frase general sobre los dos diamantes; no hay reparto por fase. Se aplica |
| M2 | PDF *The Client Brief*; ipa.co.uk; isba.org.uk | Confirmado a medias. El PDF no desarrolla ninguna sigla. ipa.co.uk da «Institute of Practitioners in Advertising» (se mantiene y se cita). isba.org.uk no da el nombre desarrollado; sólo que representa a los anunciantes («representing the views of collective advertisers»). Se quita «Incorporated Society of British Advertisers» |
| L1 | A. Watt, *Project Management*, 2.ª ed. (BCcampus), en biz.libretexts.org, 1.2, 1.3, 1.4, 1.10 y 1.16 (opentextbc.ca devuelve 403, detrás de Cloudflare); APM, «What is a Gantt chart?»; LE 4.4.1 (volcado, pp. 75-76); *The Client Brief*, TIMINGS | Hay fuente publicada para todo lo añadido. ISO 21502 no se ha podido leer (iso.org da 403): sigue en «Lo que este tema no da» |

Cotejo por script de todas las negritas nuevas contra la unión de esas fuentes: 36 de 36 literales.

## Pasajes cambiados

1. **Siglas** (líneas 17-22). Antes: «Institute of Practitioners in Advertising (IPA) e Incorporated
   Society of British Advertisers (ISBA), dos de las cuatro entidades… (las otras dos, MCCA y PRCA, no
   se desarrollan…)». Ahora: IPA desarrollado, «la asociación británica de agencias», e ISBA «la de
   anunciantes», sin desarrollar (lo mismo MCCA y PRCA); se añade la APM, con su lema literal
   **«The Chartered Body for the Project Profession»**.
2. **El Doble Diamante**, entradilla de la tabla: se añade que el reparto de cada fase entre divergente
   y convergente es propio, a partir de la cita, porque el Design Council no lo hace fase por fase (M1).
3. **Revisar sobre la pieza**, viñeta «Comparar versiones» (G1). La condición de las mismas dimensiones
   pasa a la vista de superposición (**«Overlay view»**, con deslizador). La vista de diferencias
   (**«Pixel difference view»**) se describe aparte y sin condición, con la cita **«it will highlight
   the pixel differences between the two assets»**.
4. **Nuevo epígrafe `## La gestión del proyecto: fases, calendario y riesgos`**, entre «El marco» y
   «1. Briefing», unas 1.100 palabras (L1):
   - «Las cuatro fases de un proyecto»: iniciación, planificación, ejecución y cierre (Watt 1.3), con
     tabla. Incluye el plan de calidad y de aceptación y la revisión de cada entregable contra los
     criterios de aceptación, enlazado con los criterios de éxito del *brief*.
   - «La triple restricción»: alcance, plazo y coste; el triángulo; el ejemplo del manual; la lista
     ampliada de restricciones (Watt 1.2). Aplicación de oficio: una versión vertical añadida sin mover
     el estreno.
   - «El calendario: hitos, Gantt y camino crítico»: calendario de hitos (Watt 1.4), Gantt (Watt 1.10 y
     APM: definición, qué hace falta, reparto de responsables), dependencia fin-inicio, camino crítico,
     holgura; enlace con TIMINGS de *The Client Brief* y con LE 4.4.1 (**«Incluye el control de la
     puntualidad…»**, precedido de la definición de operatividad para que «Incluye» tenga antecedente).
   - «Los riesgos»: definición y cuatro respuestas (Watt 1.16); riesgos típicos del grafismo como oficio.
   - «Un calendario de ejemplo»: tabla de hitos de una cabecera, planificada hacia atrás (oficio).
5. **Portada**: Fuente (se añaden Watt y la APM), Redacción que se estudia, Extensión (6.300 → 8.000,
   según `indice.py`, que cuenta 8.008).
6. **Qué se puede preguntar**: fases del proyecto, triple restricción, hito, Gantt, camino crítico,
   riesgos; en la práctica, planificar un calendario de hitos.
7. **Normativa que el tema invoca**: LE añade 4.4.1; el párrafo final nombra el manual y la APM.
8. **Lo que este tema no da**: la viñeta ISO se reescribe (ISO 21500/21502 y el PMI siguen sin leer;
   la gestión se estudia con Watt y la APM; no consta cómo planifica la casa).
9. **Trazabilidad**: filas nuevas de Watt, APM, IPA/ISBA; la del LE añade 4.4.1 (pp. 75-76); la de
   Frame.io menciona las dos vistas; la lista de oficio añade lo nuevo que es lectura propia.

Relectura de antecedentes: «el manual» va siempre detrás de la presentación de Watt al abrir el
epígrafe; «la APM» está presentada en las siglas; «la guía británica del *brief*», «epígrafe 1» y
«epígrafe 5, "Cerrar el proyecto"» existen; «Incluye» (LE 4.4.1) lleva delante su sujeto.

## Preguntas tras el remate

La 6 (Gantt), la 11 (Overlay) y la 15 (triple restricción) quedan contestadas enteras. La 13 sigue a
medias por remisión al tema 8, como aceptó la refutación. Recuento: entera 14, a medias 1, no 0.

## Lentes

- `indice.py`: índice regenerado (36 epígrafes, 8.008 palabras). El tema no está en `portadas.tsv`
  (portada escrita a mano, como antes) y la herramienta avisa «sin portada: es un esquema»; la portada
  queda intacta.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py`, `refutar_exactitud.py` y `refutar_modo.py`: no aplican (sin articulado del BOE). Las
  negritas nuevas se han cotejado por script (36/36).

## Ficheros tocados

- El tema 14 (arriba).
- Este informe (nuevo).
- Copias de fuentes y del tema anterior en el directorio temporal de la sesión, fuera del repositorio.
