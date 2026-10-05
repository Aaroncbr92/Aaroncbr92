# Remate · Oficial Técnico Electricista (27) · Tema 15 · Trabajos en instalaciones eléctricas

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/15-trabajos-en-instalaciones-electricas.md`.
Entradas: `27-T15-refutacion.md` (0 graves, 5 menores, 2 lagunas) y `27-T15-preguntas.md` (12 enteras, 1 a medias, 2 no).
Fecha del encargo: 24-09-2026. Fuentes releídas el 05-10-2026 (reloj del sistema): RD 614/2001 (BOE-A-2001-11881,
redacción única), guía técnica del INSST de riesgo eléctrico, edición de septiembre de 2020 (texto y, para la
tabla 2, la página 56 del PDF vista como imagen, porque el `.txt` desordena las columnas).

Ficheros tocados: el tema y este informe. Copia del tema previo en el scratchpad (no en el repositorio).

**Resultado: 5 hallazgos aplicados (todos confirmados en la fuente), 2 lagunas cubiertas ampliando 4.2. Se amplió contenido nuevo.**

## Hallazgos

| # | Comprobación en la fuente | Aplicado | Pasaje cambiado |
| --- | --- | --- | --- |
| 1 | La guía sólo dice «Edición: Madrid, septiembre 2020»; no «4.ª» | Sí | Portada, «Fuente»: «(edición de septiembre de 2020)» |
| 2 | Anexo V.A.2.2: «La vigilancia no será exigible cuando los trabajos se realicen fuera de la zona de proximidad o en instalaciones de baja tensión.» | Sí | 1.4, cuadro, fila «Trabajo en proximidad cuando las medidas no bastan»: BT «Autorizado, o bajo la vigilancia de uno; en BT la vigilancia no es exigible»; AT «… (no exigible fuera de la zona de proximidad)»; precepto «Anexo V.A.2.1 y 2» |
| 3 | Anexo II.B.4.1, párr. 2, primera frase literal confirmada | Sí | 3.5: la cita del transformador de intensidad empieza ahora en «Para trabajar sin tensión en un transformador de intensidad, o sobre los circuitos que alimenta, se dejará previamente sin tensión el primario.» |
| 4 | Guía, comentario al art. 4.6: «se transformarían respectivamente en un "trabajo en tensión" (si tuviera que ocuparse una zona de peligro) o en un "trabajo en proximidad" (si una zona de peligro pudiera invadirse accidentalmente)», reguladas por «los apartados 5 o 7 de este artículo»; art. 4.5 → anexo III, 4.7 → anexo V | Sí | 4.3, último párrafo: criterio doble ocupar → tensión, invadir accidentalmente → proximidad, apartados 5 o 7 del artículo 4 (anexos III y V) |
| 5 | Anexo II.B.3: «Para dejar sin tensión una instalación eléctrica con condensadores cuya capacidad y tensión permitan…» | Sí | 3.5: «*Condensadores (B.3)*: para dejar sin tensión una instalación con condensadores **«cuya capacidad…»**» |

## Lagunas (ampliación)

1. **Métodos de trabajo en tensión** (pregunta 9). Confirmado en la guía, comentarios al anexo III.A.2 (págs. 49-53):
   tres métodos literales (a potencial, a distancia, en contacto), procedimientos específicos por tipo de trabajo,
   escritos en AT; el método en contacto «se emplea principalmente en baja tensión»; precauciones en BT y EPI a
   considerar. Añadido en 4.2, antes del párrafo «La autorización por escrito…». Dos frases de la guía se dan en
   redonda por erratas del original («así mismo. aseguren», «U sar»).
2. **Clases de guantes aislantes y normas de equipos** (pregunta 10). Confirmado en la tabla 2 (pág. 56, vista como
   imagen): guantes UNE-EN 60903 y manguitos UNE-EN 60984, clases 00 a 4 con límites «<» (00: < 0,5 kV c.a., < 0,75 kV
   c.c.; 0: < 1 / < 1,5; 1: < 7,5 / < 11,25; 2: < 17 / < 25,5; 3: < 26,5 / < 39,75; 4: < 36 / < 54); casco UNE-EN 50365
   clase 0 (< 1000 V c.a., < 1500 V c.c.); ropa UNE-EN 50286 clase 00 (< 500 V / < 750 V). Cuadro 7: UNE-EN 60900
   hasta 1000 V c.a. y 1500 V c.c. Normas técnicas: «debe considerarse la última edición». La refutación escribía
   «hasta 500 V»: la tabla pone «< 0,5»; se ha seguido la tabla. Que la clase 00 cubra un cuadro de 400 V se declara
   lectura propia. Añadido en 4.2 tras los métodos, con tabla.
   «Lo que este tema no da»: la línea «clases de guantes… no leídas» pasa a «Las normas UNE-EN de EPI y de herramienta
   aislada, en su texto: no leídas; el tema da sólo lo que de ellas recoge la guía del INSST…».

## Otros pasajes cambiados

- «Qué se puede preguntar»: añadida la línea «los tres métodos de trabajo en tensión de la guía del INSST y las clases
  de los guantes aislantes;».
- Trazabilidad, fila de la guía: añadidos los comentarios al anexo III.A.2 y III.A.3 (tabla 2, cuadro 7) y el apartado
  de normas técnicas. Lista de oficio: «que la clase 00 de guantes cubre un cuadro de 400 V».
- Portada, «Extensión»: «Unas 16.600 palabras» (indice.py: 16 646; antes 15 874).

## Lentes

- `indice.py`: 38 epígrafes, índice sin cambios de rúbricas.
- `negritas.py` (RD 614/2001 y guía): las nuevas «NO ESTÁ» (los tres métodos, «Existen tres métodos…», «Dentro de cada
  uno…», «Vestir ropa…») son falsos negativos por guiones blandos, salto de página y un carácter de control (\x07)
  delante de «Método» en el `.txt`; comprobadas con cotejo normalizado y a la vista: literales.
- `refutar_exactitud.py`: sin novedades atribuibles al remate (las 12 «no literales» son las del 6.x copiado o citas
  de otra norma, ya vistas en refutación). `refutar_modo.py`: 0. `refutar_prosa.py`: 0 (siglas y negritas sin hallazgos).

Relectura de antecedentes: «la guía» (4.3 y 4.2) tiene antecedente en 1.1; «la tabla» en el párrafo que la presenta;
«del artículo 4» explícito. Sin referencias colgantes.

Para la fase 5 bis (sólo pasajes ampliados): 4.2 «Métodos de trabajo en tensión» y «Clases de los EPI y normas de los
equipos»; 4.3 último párrafo; fila del cuadro de 1.4.
