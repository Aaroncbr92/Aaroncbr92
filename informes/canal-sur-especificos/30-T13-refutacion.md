# Puesto 30 · Tema 13 · Refutación (fase 4, segunda pasada)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`
(≈ 8.900 palabras), en su estado tras el remate y la revisión 5 bis. No se corrige el tema: sólo se
informa. La primera refutación (0 graves, 4 menores, 2 lagunas; todo aplicado según
`30-T13-remate.md` y `30-T13-final.md`) queda en git (commit b08a902).

Exactitud: se saltan «Copiado del común» (pasajes de Redactor/a T07 en § 4) y «Copiado de RTVE sin
cambios» (lista en `30-T13-redaccion.md`). Cobertura: el tema entero.

## Fuentes releídas (todas el 25-09-2026, sólo el pasaje)

- X Convenio RTVA (`documentos/x-convenio-rtva-boja-240-2014.txt`): ficha 5212204 (p. 127) y ficha
  5212206 (p. 190), completas.
- Resolve 21: `proxy.txt` pp. 198, 215-217; `render.txt` pp. 4185, 4193-4194, 4215; `vars.txt`
  pp. 345-346 (cap. 15); `titles.txt` p. 1215 (cap. 56); `integr.txt` p. 4418 (cap. 201).
- Adobe: `wb-ame.txt` (cola y *preset* por defecto), `wb-ingest-proxy-workflow.txt`, las cinco
  `adobe-mogrt-*.txt` (7-I-2026).
- MOS: `mos.txt`, `moscur.txt`, `mosfaq.txt`. Avid: `avnews.txt`, `avpm.txt`.
- EBU Tech 3293 v1.10 (abril de 2020), pp. 7-8.
- Libro de estilo, 6.3 (sólo la frase de la escaleta de planos).

## Lente 1 · Exactitud

Confirmado literal y con su página: fichas del convenio (las seis tareas de la tabla y las dos de la
frase siguiente; 6 + 2 = 8, cuadra); Proxy Generator (carpetas «constantly monitored», espacio para
original y copia, subcarpeta «Proxy», nombre reservado, *Start*/*Stop* y barra espaciadora, estado
*Waiting* tal como lo dejó la 5 bis); segundo plano (tareas *Transcription* y *Proxy Generation*,
«disabled by default»); cola, *presets* .xml y menú *Add to Render Queue Using*; tres condiciones del
*render* remoto; variables (%, «12_A_3», campo vacío, %date/%time); rótulos *M Lower 3rd*, *Text+*,
*Fusion Titles*; integraciones Studio y MAM (EditShare FLOW); Media Encoder («H.264 Match Source -
Adaptive High Bitrate» y su salvedad); .mogrt (tipo de fichero, tres procedencias, *My Templates*,
Creative Cloud sin instalar, pestaña *Edit* de *Properties*, fuentes que faltan, exportación y sus dos
límites, tres tipos de dato); MOS (definición, finalidad, FAQ, reparto «In General», tres mensajes,
objetivos, versiones con su transporte, 1998, «more than 150», carácter no oficial); Avid (iNEWS como
otro nombre de *Newsroom Management* consta en la propia página; citas de *Production Management*);
EBUCore (p. 7 y p. 8). Recuentos cuadran. Sin hallazgos graves.

Hallazgo menor:

1. **Error 6 (salvedad omitida).** § 5, «El montador en el flujo integrado», frase tras la tabla
   (l. 717-721): «la ficha tiene otras dos» presenta las ocho tareas como lista cerrada; la ficha
   5212206 termina con **«La presente definición no constituye una lista cerrada de funciones,
   debiendo realizar el trabajador asimismo, todas aquellas tareas que, de acuerdo a su cualificación
   profesional, le sean encomendadas por su inmediato superior.»** (p. 190). Es pregunta de test
   probable («¿es cerrada la lista de tareas?»). Propuesta: añadir al final de esa frase «y el
   convenio advierte que la definición **"no constituye una lista cerrada de funciones"**».

## Lente 2 · Cobertura del enunciado

Los cinco rótulos del enunciado (automatización, plantillas, MAM/PAM, *newsroom*, flujos integrados)
tienen epígrafe propio, en su orden, con aplicación práctica. Las dos lagunas de la primera pasada
(.mogrt; puesta en marcha del Proxy Generator) están cubiertas. Hueco que destapa el test:

- **Formato de los mensajes MOS** (pregunta 15, a medias). El tema da el objetivo literal «tagged text
  unicode format» y declara no leída la estructura de los mensajes; no puede decir en qué lenguaje de
  marcas van. Es pregunta de test plausible. Laguna: leer la especificación MOS 2.8.5 o 4.0 (PDF
  enlazados desde «Current Versions») y añadir una frase al § 4; si no se consigue, queda declarada
  como está.

## Preguntas

15 nuevas en `30-T13-preguntas.md`: 14 enteras, 1 a medias, 0 no.

## Recuento

Graves: 0. Menores: 1. Lagunas: 1 (formato de los mensajes MOS).

## Ficheros tocados

`30-T13-preguntas.md` y este informe (los dos reescritos; la primera pasada, en git). El tema no se ha
tocado.
