# Puesto 08 · Tema 3 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/03-captacion-eng-estudio-exteriores-um-directos.md`
(≈8.800 palabras según `indice.py`; 6 epígrafes `##` en el orden del enunciado —ENG, estudio,
exteriores, unidades móviles, retransmisiones, directos informativos— más normas técnicas, huecos y
trazabilidad; 38 `###`). Escrito por partes, guardando cada `##`. Índice con `indice.py`.
`refutar_prosa.py`: quedan 2 avisos de siglas no aplicables (ENG en el título, antes del bloque de
siglas; «URSA», nombre de modelo explicado en la misma frase). No hay norma jurídica, así que no
proceden las lentes automáticas de norma.

## Fuentes (leídas el 24-09-2026)

- **Libro de estilo de Canal Sur** (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`),
  releído por mí en cada cita: Introducción p. 9; 3.17.1-3.17.1.5 (pp. 59-62); 5-5.6 (pp. 79-85);
  8.3-8.3.4 (pp. 116-118); 8.4-8.4.2 (pp. 119-120).
- **UIT-R SNG.770-2** (01/2012), `fuentes/normas-tecnicas/UIT-R_SNG.770-2.txt`: considerando c),
  recomienda 8 y 9, anexo 1, 1.1 y 2.2.1. **Vigencia comprobada** en `itu.int/rec/R-REC-SNG.770`
  el 24-09-2026: SNG.770-2 (01/2012) «In force»; la -1 (09/94), sustituida.
- **SMPTE 311-2009**, `fuentes/normas-tecnicas/SMPTE_ST-311-2009.txt`: cl. 1, 5.1, 6.1, 6.2.
- **Blackmagic ATEM**, manual en español (dic. 2024), `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt`:
  líneas ~1011-1024 (intercom, piloto verde/rojo), 1461-1463 (CALL), 2674-2677 (N-1), 7645
  (luz roja), 772 (control por retorno SDI).
- **LiveU LU800**, `fuentes/fabricantes/LiveU_LU800_ficha.txt` (descargada 03-09-2026): líneas 11,
  19-22.
- `08-investigacion-B-captacion.md` (§ 3.1-3.10, 13.1): guía; todas sus citas se cotejaron en la
  fuente local salvo las de LU800, que se cotejaron en el `.txt`.

## Copiado del común

Literal de `temas/canal-sur-especificos/34-redactor-a/10-coberturas-en-directo.md` (tema cerrado):

- «Cómo sale la señal» (en «Unidades móviles»): la tabla de cinco vías y las dos viñetas
  *Satélite* y *Mochila*, literales de su § 6 «Con los equipos técnicos: cómo llega la señal». La
  frase de entrada es mía, reescrita (la original se dirigía al redactor). Los tres datos
  SNG.770-2 que siguen a las viñetas son míos y sí se verifican.
- «La preparación» (en «Directos informativos»): el primer párrafo (cita de LE 8.3 hasta
  «celeridad») es literal del § 2 de ese tema, sin su última frase; y el párrafo del pacto (cita de
  LE 8.1.6) es literal de su § 6 «Con la redacción y el equipo». El párrafo final («El cámara es uno
  de los profesionales…») es mío.

**No** es copia literal (se verifica): «Los eventos no controlables: grabar siempre» parte del mismo
tema, pero adaptado al cámara (quitado «que el redactor debe conocer», «SIEMPRE» en minúscula,
añadida la cita de LE 5.4).

## Copiado de RTVE (a verificar; oficio, sin precepto que releer salvo SNG.770-2)

Quitada la negrita de énfasis, las respuestas oficiales, las tablas de opciones falsas, los «datos
que el examen ha preguntado» y todo lo propio de RTVE:

- `informacion-grafica/03` § 1: tabla de familias (sin la fila de cinematografía digital, que no pide
  el enunciado; ya está en el tema 1). § 10: sólo el principio de las tres igualaciones (TC, compás de
  cuadro, ajustes de imagen), sin rótulos de menú (*Free Run*, *Ext. Link*…) que RTVE sostenía sólo
  en la plantilla.
- `informacion-grafica/11`: § 3 (grabar para el montaje; quitado el «tres o cuatro segundos» de
  colchón, que contradice los diez segundos del Libro de estilo), § 5 (plató multicámara), § 6
  (deporte), § 7 (lista de comprobación; quitados chaleco, casco y botas como lista cerrada), § 8
  (situaciones), § 9 (jornada).
- `informacion-grafica/09` § 2 (retardo e inestabilidad de la mochila, sin la pregunta 84) y § 4-5
  (robotizadas y orden de corte, resumidos).
- `realizacion/12` § 1, 3, 5 (qué es la UM, zonas, montaje). **Quitado**: la tabla de tamaños con
  números de cámaras (el propio RTVE los declaraba orientativos, sin fuente) y la sigla PEL, que los
  temas RTVE desarrollan de dos formas incompatibles (IG/11: «producción electrónica ligera»;
  realización/12: «unidad móvil ligera»); no consta cuál usa CSRTV.
- `realizacion/14` § 1, 2, 4 (sin la columna de compresión HEVC), 6 (*pool*, sin preguntas) y 7.
  **Quitado entero** el § 3, cadena de señal Prado del Rey–Torrespaña (propio de RTVE) y el § 5 del
  *downlink* salvo el dato de zona de servicio, que se tomó de la propia SNG.770-2.

## Nuevo (hueco declarado por la agrupación: operativa de cámara en retransmisión)

- «La operativa del cámara en una retransmisión»: tabla de oficio declarada como tal + deporte.
- «El piloto: anticipo y aire», «La intercomunicación y el retorno» (ATEM, con la salvedad de que
  el verde de anticipo es de un fabricante).
- «El cable de cámara» (SMPTE 311-2009; triax sin cifras).
- «La coordinación con el control desde la mochila» (LU800).
- Lo propio de Canal Sur del Libro de estilo en cada rúbrica.

## Discrepancias y avisos para verificación

1. **Cita de la llamada ATEM**: el informe de investigación la cortaba en «camarógrafos»; el texto
   sigue «o de indicarles que la señal va a ser emitida al aire». Citada entera.
2. **Errata de la fuente** conservada: ATEM «uno de lo botones». LE 5.4 «Si las circunstancias lo
   permitan» (sic).
3. **LE 5.3.3**: el original dice «aunque también puede ser recomendable es el TC poniendo…»
   (construcción rota); se cita sólo desde «el TC poniendo el marcador…».
4. **«Falso directo» con dos sentidos** en el Libro de estilo (3.17.1.5, grabar de corrido en UM;
   8.3.3, hacer pasar lo grabado por directo): aclarado en el tema.
5. **Efecto Heisenberg**: la explicación física que da el Libro de estilo es inexacta; no se
   reproduce, sólo la frase operativa.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.

## Autocomprobación: 10 preguntas tipo test

| Nº | Rúbrica | Pregunta (respuesta) | ¿La contesta el tema? |
|---|---|---|---|
| 1 | ENG (teoría) | ¿Qué distingue una cámara ENG de una EFP o de estudio? (la ENG es autónoma y el operador ajusta; la EFP cuelga de una CCU y el control de imagen ajusta) | Entera: «Las familias de cámara…» |
| 2 | ENG (Canal Sur) | ¿Cuál NO es una de las cuatro condiciones mínimas del Libro de estilo: orden narrativo; alternancia de planos con nexo; número suficiente de planos; grabar siempre con zoom? (la última) | Entera: «La grabación adecuada…» |
| 3 | ENG (Canal Sur) | ¿Por qué canal se registran las declaraciones y por cuál el ambiente? (canal 1 declaraciones; canal 2 ambiente con el micrófono de cámara) | Entera: «El sonido en ENG…» |
| 4 | ENG (práctica) | Para una noticia de un minuto, ¿cuántos planos y cuántos minutos útiles pide el Libro de estilo? (20-25 planos en 3-4 secuencias; 4-8 minutos) | Entera: «Cuánto se graba y cómo» |
| 5 | Estudio | En un mezclador que distingue anticipo y aire, ¿qué indica el piloto rojo, y qué es un retorno N-1? (cámara al aire; retorno sin el audio de la propia fuente) | Entera: «El piloto…» y «La intercomunicación y el retorno» |
| 6 | Exteriores (Canal Sur) | ¿Qué plano pide el Libro de estilo para una entrevista en exteriores y qué debe usar siempre el equipo en una obra? (plano americano; casco) | Entera: «La luz y el sonido en exteriores» y «Situaciones extremas y seguridad» |
| 7 | Unidades móviles (técnica) | Según SMPTE 311-2009, ¿cuántas fibras lleva el cable híbrido de cámara y de qué tipo? (dos, monomodo) | Entera: «El cable de cámara» |
| 8 | Unidades móviles (norma) | Según la Rec. UIT-R SNG.770-2, ¿qué autorización requiere un satélite de cobertura regional y cuántas personas deben poder manejar el equipo DSNG? (sólo la del país del enlace ascendente; no más de dos, en tiempo razonablemente corto, p. ej. 1 h) | Entera: «Cómo sale la señal» |
| 9 | Retransmisiones | ¿Qué tres tipos de retransmisión nombra el Libro de estilo y qué es una señal *pool*? (deportivas, taurinas, fiestas populares; la de un evento, sobre todo institucional, que realiza una productora y distribuye al resto) | Entera: «Las retransmisiones en el Libro de estilo» y «La señal *pool*» |
| 10 | Directos (práctica) | En un directo desde un recinto cerrado sin referencias, ¿qué plano basta, y qué dice el Libro de estilo del falso directo? (plano medio; debe erradicarse y, si lo hay, se hace constar) | Entera: «El encuadre y el emplazamiento del directo» y «El falso directo» |

Resultado: 10 de 10 enteras; no ha hecho falta ampliar.
