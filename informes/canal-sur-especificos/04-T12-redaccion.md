# 04 · Ayudante de Producción · Tema 12 · Redacción (fase 2)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/12-documentacion-internacional-para-desplazamientos.md`
(unas 7.500 palabras, 29 epígrafes; índice generado con `indice.py`). Redactado el 06-10-2026 por
partes, guardando cada una: cabecera y rúbrica general; equipos técnicos (Convenio de Estambul y
cuaderno ATA); equipos humanos (pasaporte, visados, acreditaciones, A1, TSE, seguro, dietas);
actividad, paso a paso, supuestos y cierre. Material: `04-investigacion-B-campo.md` §5; Productor
T08 (cerrado); RTVE `produccion-asistencia/14` y `produccion/08` (fila 4·12 de
`produccion-informacion.tsv`: 75 %, actualizar = no).

Ficheros tocados: el tema (nuevo) y este informe. Ninguno más. (`indice.py` se corrió una vez sin
argumentos por error; recorre los temas del `.tsv` y no modificó ninguno: `git status` sin cambios
en ficheros versionados.)

Lentes: `refutar_prosa.py`: 4 hallazgos, corregidos los de siglas (IVA presentada; «RED» es nombre
del sistema, no sigla que haya que desarrollar); las dos frases repetidas son de portada/normativa y
trazabilidad, inevitables. `negritas.py` (Convenio, RD 896/2003 releído, convenio RTVA, fichas de la
Cámara, Productor T08 e investigación): 135 cotejadas; 4 «no están» = 3 rótulos de supuestos + la
del art. 4.1 RD 896/2003, que sí está (la descarga de ese artículo falló por red en el lote del
cotejo; leído antes el mismo día); 1 «mal atribuida» falsa (la definición de cadena de garantía
está en el art. 1, que es donde la sitúa el tema). Quitada una negrita de entrada en vigor del
Convenio porque el BOE trae una errata («8para España»): ahora va en redonda.

## Fuentes releídas hoy (06-10-2026)

- Convenio de Estambul, BOE-A-1997-21711 (`fuentes/corte-20221221/`, texto no consolidado, sin
  correcciones de errores registradas): anexo A, arts. 1-6; anexo de material profesional, arts.
  1-8 y apéndice I; anexos II-IV (declaraciones de la Comunidad Europea); Estados firmantes y parte;
  entrada en vigor. Coincide con lo que da RTVE T14, y añade arts. 2.4, 3.1, 5.3, mat. prof. 3 y 4.
- RD 896/2003 con `boe.py` (vigente): arts. 1, 3, 7 (originales), 4, 5, 8 (vig. 26-06-2014). La
  norma modificadora BOE-A-2014-6663 es el **Real Decreto 411/2014, de 6 de junio** (comprobado en
  el BOE). Coincide con la investigación.
- Copias guardadas de la Cámara de Comercio (leídas allí el 02-09-2026): ficha ATA (añade precio
  205 €, eATA, cuaderno digital, seguro ATA y países excluidos del seguro) y fichas país (82
  territorios; campos de la ficha de Irán). Ojo: el literal es «5.800 cuadernos emisores», no
  «emitidos» como dice RTVE T14; el tema no usa esa cifra.
- X Convenio RTVA (BOJA 240/2014): ficha 5212705, art. 39, art. 53.1.2 y 53.3.
- 883/2004, 987/2009, PAG (A1), guía TSE, MAEC y GOV.UK: no releídos (EUR-Lex no respondió); se
  toman de la investigación del bloque, leída el 06-10-2026. **Verificar.**

## Copiado del común

Literal de `32-productor-a/08-produccion-de-exteriores-retransmisiones-eventos-e-informativos.md`
(cerrado; no se reverifica). Entre corchetes, el cambio:

- «Las tres clases de papeles» = «Desplazamientos internacionales» de Productor (entero: frase
  inicial, tabla y dos avisos) [título nuevo; añadido un párrafo final nuevo sobre A1 y TSE, a
  verificar].
- «Las frecuencias», primer párrafo [quitado «(epígrafe «Transporte»)»]; los dos párrafos
  siguientes son nuevos (el de la UIT-R SNG.770-2 es literal de «Las vías de salida de la señal»
  de Productor: «Recomienda también… recomienda 9»; la frase «la autorización se da por supuesta, y
  la Recomendación sólo limita qué país ha de darla», literal).
- «Las acreditaciones de prensa», segunda frase del primer párrafo = «Las acreditaciones» de
  Productor [quitada la cita «(Libro de estilo, 4.4 y 4.4.4, punto 9)», sustituida por la de la
  ficha del Ayudante].
- «Cuánto dura», último párrafo = frase de «El cuaderno ATA» de Productor («Dentro de su año de
  validez…plazo de permanencia que fije cada país (oficio)»).
- «Seguro, Registro de viajeros…», párrafo del art. 39 [reescrito con la cita literal del convenio
  en vez de la paráfrasis de Productor; a verificar sólo la cita] y párrafo de oficio de seguros
  [adaptado: añadido el seguro ATA; quitada la referencia al operador de dron].

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra (sólo se quitó la negrita de énfasis, que en Canal
Sur se reserva al literal):

- `produccion/08-produccion-en-exteriores.md`, §8, tabla de rasgos del cuaderno ATA: filas «Qué
  lleva», «Cómo funciona» y «Ámbito» (en «Qué lleva: la lista general», tabla final). Se dejaron
  fuera las filas «Validez» («no prorrogables» no está en el Convenio), «Quién lo expide» y «Qué
  ampara» (sustituidas por las fuentes).
- `produccion-asistencia/14-documentacion-internacional.md`, §1.3: «Los doce meses están en el
  tratado y en la ficha, que dicen lo mismo por dos caminos:».

## Copiado de RTVE con cambios (se verifica)

De `produccion-asistencia/14`: el bloque de definiciones del anexo A (ahora con la cita entera de
cada letra, incluido «(incluidos los medios de transporte)» que RTVE elidía); «Tres cosas que hay
que sacar de ahí» [«pasaporte aduanero» marcado como oficio]; las definiciones de asociación
expedidora y garantizadora [añadida la de cadena de garantía]; «La regla» [reescrita]; art. 5.1 y
material profesional art. 5; «techo, no un suelo»; «Los doce meses aparecen, pues, por los dos
lados». Quitado lo propio de RTVE: preguntas de su examen, distractores, «respuesta oficial»,
plantilla, el bono de cargos varios y la GPO de Israel (sin fuente consultada; declarados en «Lo que
este tema no da»), Irán/Ghana como pregunta (queda la idea de que la lista cambia).

## Nuevo, a verificar entero

Convenio de Estambul (fechas, declaraciones de la Comunidad, arts. 2.4, 3.1, 5.3, 6, material
profesional 1, 3, 4 y apéndice I); ficha de la Cámara (eATA, precio, seguro, excluidos) y campos de
la ficha país; RD 896/2003 entero; A1 (883/2004 art. 12.1, 987/2009 arts. 15.1 y 19.2, PAG); TSE
(883/2004 art. 19.1, 987/2009 art. 25, guía); MAEC; ETA; convenio arts. 39 y 53; tabla «Dentro y
fuera de la UE»; «La preparación de un viaje, paso a paso»; supuestos 1 a 3.

Dudas para el verificador:
- Tabla «Dentro y fuera de la UE»: celda «Seguridad Social del trabajador» fuera del ámbito del A1
  dice «Este tema no lo trata» (no hay fuente leída sobre convenios bilaterales).
- A1, fila «Cuánto dura»: lo de indefinidos / fin de contrato y Reino Unido 24 meses viene de la
  investigación (paráfrasis del PAG); «máximo 5 años» va en negrita como literal del PAG.
- Supuesto 1: que Francia figura en las fichas país (sí, comprobado en el índice guardado).

## Diez preguntas de tribunal y comprobación

| # | Pregunta (respuesta correcta) | Rúbrica | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Según el Convenio de Estambul, el cuaderno ATA es: a) un visado de trabajo; b) el título de importación temporal de las mercancías, con exclusión de los medios de transporte ✔; c) el título para los medios de transporte; d) un permiso de rodaje | Técnicos · teoría | Entera («El cuaderno ATA: qué es», art. 1 b y c) |
| 2 | En España, ¿quién emite el cuaderno ATA? a) la Agencia Tributaria; b) la aduana de salida; c) la Cámara de Comercio ✔; d) la embajada del país de destino | Técnicos · teoría | Entera («Quién lo expide», y «La regla») |
| 3 | El período de validez de un cuaderno ATA: a) mínimo seis meses; b) no puede exceder de un año desde su expedición ✔; c) 24 meses; d) se negocia en cada frontera | Técnicos · teoría | Entera («Cuánto dura», anexo A art. 5.1 y ficha de la Cámara) |
| 4 | Expedido el cuaderno, se decide llevar un objetivo más. a) se añade en la aduana; b) se añade en una hoja adicional; c) no puede añadirse ninguna mercancía a la lista general ✔; d) basta comunicarlo a la Cámara | Técnicos · práctica | Entera («Qué lleva: la lista general», art. 5.3) |
| 5 | Una cámara averiada se envía al fabricante en otro país para repararla. ¿Puede viajar con cuaderno ATA? a) sí, siempre; b) sí, si vuelve antes de un año; c) no: lo que deba ser objeto de reparación no puede importarse al amparo de un título de importación temporal ✔; d) sólo con CPD | Técnicos · práctica | Entera («El cuaderno ATA: qué es», art. 2.4) |
| 6 | El pasaporte de una persona de 35 años tiene una validez: a) de cinco años prorrogables; b) de diez años improrrogable ✔; c) de dos años; d) indefinida | Humanos · teoría | Entera («El pasaporte», art. 5.1) |
| 7 | En el extranjero, una persona del equipo pierde el pasaporte. a) puede esperar a volver para denunciarlo; b) deberá darse cuenta de manera inmediata a la Representación Diplomática o Consular, que podrá expedir un pasaporte provisional ✔; c) la Policía de España le envía un duplicado; d) viaja con la fotocopia | Humanos · práctica | Entera (supuesto 3; arts. 7 y 5.8) |
| 8 | El formulario A1 de un trabajador de alta en España que va a grabar a otro Estado de la UE: a) lo expide el país de destino; b) lo emite la TGSS y acredita que sigue sujeto a la Seguridad Social española ✔; c) sólo hace falta si el viaje supera un mes; d) es la Tarjeta Sanitaria Europea | Humanos · teoría | Entera («El formulario A1»; incluye «aunque sea de corta duración») |
| 9 | Un técnico se va mañana y no tiene Tarjeta Sanitaria Europea. a) no puede viajar; b) se pide el Certificado Provisional Sustitutorio, con la misma cobertura, por un máximo de 90 días al año ✔; c) la tarjeta se recoge en mano en el INSS; d) basta el documento nacional de identidad | Humanos · práctica | Entera («La Tarjeta Sanitaria Europea»: entrega en unos 5 días, nunca en mano, CPS) |
| 10 | Un equipo va a grabar a Qatar con cuaderno ATA y se pensaba garantizar con el seguro ATA. a) no hay problema; b) Qatar está entre los países excluidos de la cobertura del seguro como garantía, y hay que prever otra garantía ✔; c) Qatar no necesita garantía; d) el seguro lo da el convenio colectivo | Técnicos · práctica | Entera («Cómo se pide y cuánto cuesta», supuesto 2) |

Resultado: las diez se contestan enteras con el tema. No hizo falta ampliar: las preguntas 5 y 10
descansan en dos puntos que el tema ya incluyó al redactar, y que RTVE no traía: el artículo
2.4 del anexo A (reparación) y la ficha de la Cámara (eATA, precio, seguro ATA y países excluidos).
