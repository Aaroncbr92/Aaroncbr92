# Grafista (15) · Tema 10 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/10-accesibilidad-contraste-legibilidad-tamano-lectura-facil-subtitulos-pictogramas-diseno-inclusivo.md`.
Entrada: `15-T10-refutacion.md` (5 hallazgos menores, 2 lagunas) y `15-T10-preguntas.md` (12 enteras,
1 a medias, 2 no). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha del
sistema). Ficheros tocados: el tema y este informe.

## Comprobación en la fuente (29-09-2026)

| Propuesta | Fuente | Resultado |
|---|---|---|
| H1 ARASAAC | `arasaac-condiciones.txt` l. 51: «Aragonese Center of Augmentative and Alternative Communication (ARASAAC)» | Confirmada, aplicada |
| H2 art. 4.2.a) 7.º | RD 707/2026, volcado vigente 02-01-2027, l. 261: sigue «o informa sobre las condiciones ambientales…» | Confirmada, aplicada |
| H3 «único requisito… en número» | WCAG 2.2, 1.4.12 (nota 1) y 1.4.8 (l. 493-506, nota 1) | Confirmada, aplicada |
| H4 EBU R 95 sin fila | Tema: sin fila en Normativa ni Trazabilidad | Aplicada (línea en Normativa, por remisión al tema 8) |
| H5 art. 7.2 «pide» | RD 707/2026 l. 310 («podrán regular», «se tendrán en cuenta») y l. 315 («pictogramas y señalizaciones») | Confirmada, aplicada |
| Laguna 1 WCAG 1.4.8 | `wcag22.txt` l. 493-506 | Ampliado §3 «El espaciado» |
| Laguna 2 WCAG 2.3.2 | `wcag22.txt` l. 712-716 | Ampliado §8 «Movimiento y destellos» |

Ninguna corrección del informe resultó equivocada. El 1.4.9 (opcional) no se añade.

## Pasajes cambiados

1. **Siglas (l. 39-41)**: «Aragonese Portal of…» → «Aragonese Center of Augmentative and Alternative
   Communication (ARASAAC), el portal de pictogramas del Gobierno de Aragón».
2. **§2 «La cifra que se puede medir», primera frase**: «El contraste es el único requisito de
   legibilidad en el que las WCAG fijan un mínimo que el propio contenido tiene que cumplir; las cifras
   de espaciado y de ancho de línea (1.4.12 y 1.4.8, epígrafe 3) son las que el usuario debe poder
   imponer. Tres criterios:».
3. **§3 «El espaciado», párrafo nuevo tras el 1.4.12** (laguna 1): criterio 1.4.8, Presentación visual
   (AAA), con cita literal del encabezado («a mechanism is available to achieve the following»), de los
   colores elegibles, los 80 caracteres (40 CJK), el texto sin justificar, el interlineado de espacio y
   medio y el espacio entre párrafos 1,5 veces, la ampliación al 200 % (en redonda) y la nota 1.
4. **§7 «Qué son y dónde están en la ley»**: «Lo que el reglamento propone para los pictogramas y la
   señalización de los espacios públicos (artículo 7.2: las Administraciones **«podrán regular»** la
   accesibilidad cognitiva en su planificación urbanística y, si lo hacen, **«se tendrán en cuenta»**
   estos criterios):».
5. **§8 «Diseño universal y ajustes razonables», viñeta 7.º**: cita completa del precepto, con «o
   informa sobre las condiciones ambientales para que las personas usuarias puedan usar sus propios
   recursos de apoyo.», y «Para el grafismo cuenta la primera alternativa, la personalización».
6. **§8 «Movimiento y destellos», tras el 2.3.1** (laguna 2): «El nivel AAA quita la alternativa de los
   umbrales: criterio 2.3.2, Tres destellos (AAA), **«Web pages do not contain anything that flashes
   more than three times in any one second period.»** (…)».
7. **Normativa que el tema invoca**: WCAG 2.2 añade 1.4.8 y 2.3.2; línea nueva «EBU R 95 (zona segura
   de grafismo): sólo por remisión al tema 8, donde se desarrolla con su fuente.»
8. **Portada, Extensión**: 16.000 → 16.500 palabras aproximadamente.

Antecedentes releídos: «estos criterios» (pasaje 4) precede a la cita de la letra e); «epígrafe 3»
(pasaje 2) lleva al 1.4.8 añadido; «Como en el 1.4.12» (pasaje 3) sigue al párrafo del 1.4.12.

## Lentes (29-09-2026)

- `indice.py`: 16.509 palabras, 51 epígrafes; índice sin cambios (no hay epígrafes nuevos).
- `refutar_prosa.py`: 1 aviso, AENOR (marca, ya discutido).
- `negritas.py` contra `wcag22.txt` y RD 707/2026: todas las negritas nuevas, encontradas; el resto de
  «no están» son de pasajes copiados o de otras fuentes, como en la refutación; el falso positivo de
  «Condiciones básicas de accesibilidad cognitiva», igual.
- `refutar_modo.py` contra RD 707/2026: 0 hallazgos. `refutar_exactitud.py`: ninguna de las citas
  cambiadas aparece como no literal (las 17 señaladas son de otras normas o pasajes copiados).

## Resultado

Se amplió contenido nuevo (1.4.8 y 2.3.2, unas 200 palabras): procede la fase 5 bis sobre los pasajes 3
y 6 (y, por ser citas nuevas, 4 y 5). Preguntas 5, 6 y 15 quedan contestables con el tema.
