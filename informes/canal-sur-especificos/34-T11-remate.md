# 34 · T11 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/11-materias-sensibles.md`.
Entrada: `34-T11-refutacion.md` (1 grave, 4 menores, 6 lagunas) y `34-T11-preguntas.md` (8/2/5).
**Resultado: amplía contenido nuevo** (pasa a fase 5 bis). Extensión: de 6.030 a 7.171 palabras.

## Fuentes releídas antes de aplicar (todas el 24-09-2026)

- Libro de estilo, `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 3.2.2 (l. 1430-1438);
  9.2.10, 9.2.11.1 (l. 4574-4598); 9.2.12.2-9.2.12.4 (l. 4671-4718); 9.3.3.1, 9.3.4, 9.3.4.1 (l. 4990-5055);
  9.4.2-9.4.2.2 (l. 5462-5563); 9.5.4.1 (l. 5715-5742); 9.6.1.2, 9.6.2, 9.6.2.2 (l. 5789-5955);
  9.7, 9.7.1-9.7.2.3 (l. 6022-6135); 9.9-9.9.2 (l. 6203-6270).
- LGCA, `fuentes/canal-sur/BOE-A-2022-11311.md`: art. 7 (l. 190-193), art. 83 (l. 1132-1134), rúbricas
  de los títulos IV (l. 1052) y VI (l. 1270).
- CE, `boe.py precepto BOE-A-1978-31229 a20`: art. 20.4.

## Hallazgos: todos confirmados en la fuente; ninguno rechazado

| Id | Comprobación | Pasaje cambiado |
| --- | --- | --- |
| G1 | 9.5.4.1, último párrafo, y 3.2.2: literal confirmado | §6 Sucesos: viñeta nueva «Suicidio» (9.5.4.1 + 3.2.2). «Lo que este tema no da»: viñeta del suicidio reescrita |
| M1 | LGCA 7.2: «Se promoverá la autorregulación para garantizar que la presencia de personas con discapacidad sea proporcional…» | §4: suprimido el «se promoverá que su» sobrante |
| M2 | 9.9 (rostros «cubiertos o tramados»; ardid con autorización previa de la Dirección de Informativos) y 9.9.2 confirmados | §9: dos párrafos añadidos; «Lo que no da»: «se aplican el 9.9, el 9.9.1 y el 9.9.2» |
| M3 | 9.2.12.2 confirmado | §2, viñeta «La víctima»: «Sólo se emitirán con autorización…» y «Sólo se indicarán detalles de referencia…» |
| M4 | CE 20.4 confirmado | §12: fila nueva (CE, art. 20.4, remite al tema 1); Normativa y Trazabilidad; ficha «Fuente» |
| L1 | LGCA 83.1 y 83.2; 95-96 en el título VI («Obligaciones de los prestadores del servicio de comunicación audiovisual televisivo») | §3: viñeta nueva sobre la radio; §12, fila del 95.2 amplía a la radio; Normativa (art. 83) y Trazabilidad |
| L2 | 9.6.1.2, 9.6.2, resumen al final del 9.6.2.2 | §10: viñetas «Los agentes», tabla de sustituciones de 9.6.2 (con la salvedad de «tregua») y resumen de cinco puntos |
| L3 | 9.3.4 y 9.3.4.1 | §8: viñetas «Errores habituales» (moro, secta, integrismo) y «Confusiones» (árabe/musulmán/islamismo; gitano) |
| L4 | 9.2.10, 9.2.11.1, 9.2.12.4 | §2, Libro de estilo: viñetas «Estadísticas», «Noticia no convencional», «Recursos estéticos» |
| L5 | 9.4.2 (litigio, testimonio falso) y 9.4.2.2 (permiso obligatorio) | §3, párrafo del Libro: dos frases añadidas |
| L6 | 9.7 (silenciar el dato; autorización), 9.7.2.1, 9.7.2.3 normas 6-8; 9.5.4.1 «sospechoso» | §5: viñetas «Regla general» e «Imagen adecuada», normas 6-8 añadidas; §7, viñeta «Antecedentes»: «sospechoso» |

Matiz de la refutación, ajustado a la fuente: en L2, «tregua» no es sustitución sin más; el Libro
reconoce que, para hacerse entender, «ya estamos obligados» a usarla, **«aunque siempre es
preferible optar por la expresión adecuada»**. Se dice así. Y el «resumen en cinco puntos» está al
final del 9.6.2.2 («Tecnicismos»), no en el 9.6.2.

Otros pasajes: «Qué se puede preguntar» añade el art. 83.1 y el suicidio; Trazabilidad del Libro
añade 3.2.2, 9.3.4, 9.3.4.1 y 9.9.2; ficha: Extensión 7.171 palabras.

## Antecedentes releídos

«En el mismo epígrafe» (§3 → 9.4.2.2; §7 → 9.5.4.1), «El mismo 9.9» (§9) y «Los arts. 95 y 96»
(§3) tienen delante su antecedente.

## Lentes

- `indice.py`: 24 epígrafes, 7.171 palabras (la ficha no está en `portadas.tsv`; Extensión puesta a mano).
- `refutar_prosa.py`: 0.
- `negritas.py` (LGCA, CE, Libro normalizado NFKC): todas las negritas nuevas están en su fuente,
  salvo «jamás aludiremos…» (9.3.4.1), partida por un salto de página del volcado (l. 5051-5055),
  comprobada a mano; y el rótulo «Noticia no convencional», que es la rúbrica del 9.2.11.1. El resto
  de «no están» son los ya explicados en la verificación (rótulos, Guía de RTVE, común).
- `refutar_exactitud.py` / `refutar_modo.py`: no se corren; no cambia ningún pasaje de la LO 1/2004,
  Ley 13/2007 ni LO 1/1996, y los falsos positivos por la numeración 9.x del Libro ya están descritos.

## Preguntas tras el remate

Con el tema, las 15 quedan enteras (5, 8, 10, 11, 12 pasan de «no» a entera; 13 y 14, de «a medias»).

Ficheros tocados: el tema y este informe.
