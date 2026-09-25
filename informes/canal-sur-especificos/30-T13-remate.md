# Puesto 30 · Tema 13 · Remate (fase 5, segunda pasada)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`.
Entrada: `30-T13-refutacion.md` (segunda pasada: 0 graves, 1 menor, 1 laguna) y `30-T13-preguntas.md`
(14 enteras, 1 a medias). El remate de la primera pasada queda en git (commit b08a902).

**Se amplió contenido nuevo** (formato de los mensajes MOS): procede la fase 5 bis sobre el pasaje 1.

## Fuentes releídas y fecha (todas el 25-09-2026)

- X Convenio RTVA, `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`, ficha 5212206
  (BOJA 240/2014, p. 190): lista de tareas y cláusula final.
- Especificación MOS, bajada hoy de mosprotocol.com (enlaces de «Current Versions») y pasada a texto con
  `documento.py`; guardada como `fuentes/canal-sur/montador/web/mos-protocol-2.8.5.txt` y
  `mos-protocol-4.0.txt`:
  - *MOS Protocol v2.8.5*, Document Revision 558, 7-IX-2017: «General Explanation of MOS message format
    and construction» (PDF p. 11) y «Message Transport» (PDF p. 13).
  - *MOS Protocol v4.0*, Document Revision 560, 7-VI-2019: canales mom/ro/aux (PDF p. 9) y el mismo
    apartado de formato (PDF p. 18). El PDF no numera páginas; se cita la del fichero.

## Hallazgos: qué se hizo

| Nº | Hallazgo | Comprobado en | Resultado |
|---|---|---|---|
| 1 | Ficha 5212206 presentada como lista cerrada (error 6) | Convenio, p. 190 | Aplicado; se añade también el resto de la cláusula (tareas encomendadas por el superior) |
| Laguna | Formato de los mensajes MOS (pregunta 15) | MOS 2.8.5 y 4.0 | **Ampliado** § 4: XML, DTD, bien formado sin exigir validez, raíz «mos», UCS-2 *big endian*, puertos 10540/10541 y canales de la 4.0 |

El informe de refutación no se equivocó. La clave de la pregunta 15 es a) XML.

## Pasajes cambiados

1. **§ 4, «El protocolo MOS», viñeta nueva «En qué va escrito cada mensaje»** (tras «Cómo viaja»,
   ≈ 150 palabras): «La especificación (versiones 2.8.5 y 4.0, apartado "General Explanation of MOS
   message format and construction") concreta ese "tagged text": **«The MOS Protocol is fundamentally a
   tagged text data stream»**, cuyos campos van delimitados **«using Extensible Markup Language (XML™)
   tags defined in the MOS Data Type Definition (DTD)»**; en las versiones 1.x el formato era propio.
   Los mensajes **«must be well formed XML, but are not required to be valid»**, y cada uno **«begins
   with the root tag ("mos")»**, seguido de los identificadores del servidor y de la redacción
   (**«"mosID" and "ncsID"»**) y del tipo de mensaje. La codificación es **«ISO 10646 (Unicode) in
   UCS-2»**, con el byte de mayor peso primero (*big endian*). En la versión 2.8.5 la redacción escucha
   en el puerto TCP/IP 10540 (**«"Media Object Metadata" port»**) y el servidor en el 10541
   (**«"Running Order" port»**); la 4.0 conserva esa lógica por *web sockets* con tres canales,
   **«mom = MOS Lower (10540)»**, **«ro = MOS Upper (10541)»** y **«aux = MOS Obj Req (10542)»**.»
2. **§ 5, «El montador en el flujo integrado», frase tras la tabla**: añadido «Y la ficha advierte que
   su definición **«no constituye una lista cerrada de funciones»**: el trabajador hace además
   **«todas aquellas tareas que, de acuerdo a su cualificación profesional, le sean encomendadas por su
   inmediato superior»**.»
3. **«Qué se puede preguntar»**: añadido «en qué formato van y por qué puertos» (MOS) y «qué tareas da
   la ficha del puesto y si son lista cerrada».
4. **«Lo que este tema no da»**: la viñeta MOS pasa a «De las especificaciones MOS se da sólo el formato
   general de los mensajes, su codificación y los puertos o canales; el catálogo de mensajes uno a uno,
   sus etiquetas y los esquemas de metadatos, no.»
5. **Trazabilidad**: fila nueva de las especificaciones 2.8.5 y 4.0 con revisión, fecha y páginas.
6. **Ficha**: «Redacción que se estudia» añade «y especificaciones 2.8.5 y 4.0»; Extensión 8.900 → 9.200.

Antecedentes releídos: «ese "tagged text"» remite a la viñeta anterior («tagged text unicode format»);
«esa lógica» remite a los dos puertos de la 2.8.5 de la misma frase; «la ficha» y «su definición»
remiten a la 5212206 citada en la entrada de la tabla. Reparto de puertos comprobado: 10540 es donde
**«the NCS will accept connections from MOS devices»** y 10541 donde **«the MOS will accept connections
from the NCS»** (2.8.5, PDF p. 13).

## Preguntas tras el remate

15: entera (clave a, XML). Resultado: 15 enteras.

## Lentes

- `indice.py` (sobre el tema 13): 9.222 palabras, 35 epígrafes; índice regenerado. Una primera
  llamada sin argumentos recorrió todos los temas del .tsv; sólo reescribe los bloques generados, y
  en el puesto 30 no cambió contenido de otros temas (los ficheros ya modificados en el árbol lo
  estaban antes, por otras fases).
- `refutar_prosa.py`: 1 hallazgo, el falso positivo de siempre (MAM en el título; se presenta en las
  siglas).
- `negritas.py` contra las dos especificaciones MOS y el convenio: todas las negritas nuevas se
  encuentran; las «no están» son de fuentes no pasadas en esta corrida (ya cotejadas antes).
- Tema sin norma legal: no proceden `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema 13; este informe; `30-T13-preguntas.md` (apartado final «Tras el remate»); dos fuentes nuevas
`fuentes/canal-sur/montador/web/mos-protocol-2.8.5.txt` y `mos-protocol-4.0.txt`.
