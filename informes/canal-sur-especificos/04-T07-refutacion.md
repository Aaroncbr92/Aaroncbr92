# 04 · Ayudante de Producción · Tema 7 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/07-gestion-operativa-de-localizaciones-espacios-y-permisos.md`
(9.712 palabras, 35 epígrafes). Refutado el 06-10-2026. No se corrige: se informa.

Ficheros tocados: este informe y `04-T07-preguntas.md`. El tema, no. Fuera del repositorio, el PDF
del Decreto 15/2011 descargado hoy al scratchpad de la sesión (sigue sin estar en `fuentes/`).

Recuento: **1 grave, 3 menores, 2 lagunas.**

## Alcance

- **Exactitud**: sólo lo nuevo y lo adaptado de `04-T07-redaccion.md`. Se saltan los pasajes de
  «Copiado del común» y de «Copiado de RTVE sin cambios».
- **Cobertura**: el tema entero, contra el punto 7 del enunciado (BOJA núm. 186, anexo V, puesto 2.4).

## Fuentes leídas hoy (06-10-2026)

| Fuente | Cómo | Resultado |
|---|---|---|
| X Convenio RTVA, ficha 5212705 (BOJA 240/2014, pág. 110) | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Objeto, tres tareas citadas y cláusula de lista abierta: literales; diez tareas: cuadra |
| Ley 39/2015, arts. 14, 21, 24, 30 y 68 | `boe.py precepto` (redacción única, vig. 02-10-2016) | Citas literales; véanse G1 y L2 |
| Decreto 15/2011 (BOJA núm. 30, 11-02-2011) | PDF oficial `boja/2011/30/d3.pdf`, descargado hoy, `documento.py texto` | Arts. 25, 27.1-3, 29.1-3 y anexo (encabezamiento y puntos 3.b y 5): literales |
| Reglamento (UE) 2019/947, art. 19.2 | `fuentes/corte-20221221/DOUE-L-2019-81004.md` | Literal |

Lentes: `refutar_prosa.py` 0 hallazgos; `indice.py` 35 epígrafes, índice al día.

## Hallazgos graves

**G1. Presentación en papel para una persona jurídica (error 7/6: régimen de 2011 dado como vigente
sin la salvedad de la Ley 39/2015).** El epígrafe del Decreto 15/2011 (artículo 27.3, líneas
319-322) y, sobre todo, el supuesto 1, punto 2 (líneas 759-760) dicen que la solicitud «se puede
presentar en el registro de la oficina de la Dirección del parque o por vía telemática». Quien pide
es Canal Sur Radio y Televisión, S.A., persona jurídica. La Ley 39/2015, artículo 14.2:
**«En todo caso, estarán obligados a relacionarse a través de medios electrónicos con las
Administraciones Públicas para la realización de cualquier trámite de un procedimiento
administrativo, al menos, los siguientes sujetos: a) Las personas jurídicas.»** Y el 68.4: si uno
de esos sujetos **«presenta su solicitud presencialmente, las Administraciones Públicas requerirán
al interesado para que la subsane a través de su presentación electrónica. A estos efectos, se
considerará como fecha de presentación de la solicitud aquella en la que haya sido realizada la
subsanación.»** El decreto remite a la Ley 30/1992 y al Decreto 183/2003 (art. 27.3), y el tema ya
avisa de que nombra leyes derogadas, pero no saca la consecuencia. En la práctica, seguir el
supuesto le hace perder días a la producción: la fecha de entrada pasa a ser la de la subsanación,
y desde ella se cuentan los 15 días o los dos meses. **Propuesta**: en el epígrafe del decreto,
tras la cita del 27.3, añadir que la empresa, como persona jurídica, presenta por vía electrónica
(14.2.a) y qué pasa si presenta en papel (68.4). En el supuesto 1, punto 2, quitar el registro de la
oficina del parque o decir que no es para la empresa. Revisar con el mismo criterio el paso 4 de
«El proceso, paso a paso» y la tabla «Qué se presenta en cada trámite», si hace falta.

## Hallazgos menores

**M1. Supuesto 1, punto 6 (línea 771): salvedad omitida (error 6).** «diez días, ampliables hasta
cinco más (Ley 39/2015, artículo 68)». El 68.2 condiciona la ampliación: **«podrá ser ampliado
prudencialmente, hasta cinco días, a petición del interesado o a iniciativa del órgano, cuando la
aportación de los documentos requeridos presente dificultades especiales»**. El epígrafe «La
solicitud incompleta» lo da bien; el supuesto debe recoger el «podrá» y la condición.

**M2. Supuesto 1, punto 3 (líneas 761-763): «podrá» convertido en automático (error 4).** «están en
el anexo (puntos 5 y 3.b), con resolución en 15 días». El anexo dice que **«los interesados podrán
solicitar mediante el procedimiento abreviado la autorización»**. El epígrafe del decreto ya lo
condiciona (líneas 335-336 y 344-346); en el supuesto falta «si se pide por el procedimiento
abreviado».

**M3. «Qué le toca al Ayudante», párrafo 3 (líneas 114-116): deducción presentada como lectura de
las fuentes (error 9).** «Leídas juntas, la ficha y el Libro de estilo dan el reparto: el productor
decide y responde; el ayudante [...] prepara las solicitudes, sigue su estado, lleva los papeles al
lugar de grabación y los archiva». La ficha da la supervisión del productor, la tarea de efectuar los
permisos y la de registro y archivo. Pero ni la ficha ni el Libro de estilo dicen que el productor
«decide y responde» ni detallan las tareas del ayudante. Propuesta: marcarlo como oficio o
ceñirlo a lo que las fuentes dicen.

## Lagunas (pregunta contestada «no» o «a medias»)

**L1 (pregunta 13, no).** Obligación de la empresa de relacionarse electrónicamente (Ley 39/2015,
14.2.a y 68.4). Se arregla con G1.

**L2 (pregunta 14, no).** El cómputo de los plazos por días. El tema maneja plazos en días sin
decir cómo se cuentan: los 15 días del procedimiento abreviado, los diez de la subsanación y los
quince del certificado del silencio. Sólo los diez días hábiles del RGC y los cinco naturales del
RD 517/2024 llevan cómputo expreso. Ley 39/2015, artículo 30.2: **«Siempre que por Ley o en el
Derecho de la Unión Europea no se exprese otro cómputo, cuando los plazos se señalen por días, se
entiende que éstos son hábiles, excluyéndose del cómputo los sábados, los domingos y los declarados
festivos.»** Es lo que necesita el «calendario hacia atrás» de la prueba práctica. Propuesta: una
viñeta en «Plazos y silencio: la regla general de la Ley 39/2015».

**Pregunta 12, a medias (no cuenta como laguna).** La instrucción (art. 28 del decreto) la hace la
misma Delegación Provincial o Dirección General que resuelve. El tema no lo cita. Es opcional: una
frase en «Plazo y silencio».

## Cobertura del enunciado

El enunciado tiene cuatro partes. Las cuatro tienen su rúbrica, y en ese orden: localizaciones y
espacios; el proceso de obtención de autorizaciones y permisos; la documentación necesaria; la
gestión de incidencias. Además hay aplicación práctica con tres supuestos. Aparte de L1 y L2, no
falta nada que el enunciado pida.

Una observación, que no es hallazgo: «espacios» se trata sólo como espacio ajeno (vía pública,
parque, propiedad privada). La reserva de los espacios propios de la casa (platós, salas) no consta
en un documento publicado de la RTVA. El tema ya declara que no hay procedimiento interno publicado;
si el remate lo cree útil, puede nombrar los espacios propios en esa línea de «Lo que este tema no da».

## Comprobado sin hallazgo (lo nuevo)

- Ficha: objeto, tres tareas citadas y cláusula final, literales.
- Decreto 15/2011: 25 (encabezamiento, d, e), 27.1, 27.2 (dos párrafos), 27.3.a, 29.1 (con la
  Dirección General), 29.2, 29.3 y anexo (encabezamiento, 3.b, 5), literales. Las tres advertencias
  y la deducción sobre el abreviado están bien marcadas.
- Ley 39/2015: 21.1 (con la excepción), 21.2, 21.3.b, 24.1 (con la salvedad de norma con rango de
  ley), 24.2, 24.3.b, 24.4, 68.1-3, literales o bien parafraseados.
- Tabla «La resolución que no llega»: cuadra con 24.1, 24.2, 24.3.b, 29.2 del decreto y RGC 35.
- 2019/947, 19.2: literal; la obligación es del operador, bien dicho.
- Remisiones internas («citado en la rúbrica anterior», «citado en la primera rúbrica»): tienen
  su antecedente.
- Supuestos 2 y 3: coherentes con el cuerpo.
