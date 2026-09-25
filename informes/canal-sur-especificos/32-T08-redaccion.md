# Productor/a (puesto 32) · Tema 8 · Redacción

Fase 2, redactar. Tema: `temas/canal-sur-especificos/32-productor-a/08-produccion-de-exteriores-retransmisiones-eventos-e-informativos.md`
(11.136 palabras según `indice.py`, índice incluido; 10 rúbricas `##` que siguen el enunciado, más
aplicación práctica y cierres; 61 epígrafes). Fecha de trabajo y de lectura de las fuentes:
25-09-2026 («hoy» del encargo: 24-09-2026; las fuentes son las mismas en ambas fechas, salvo las
páginas web, que sólo se pudieron leer el 25).

Ficheros tocados: el tema (nuevo) y este informe. Auxiliares en el scratchpad (`t08/`: partes
`p1-p4.md` con marcas de copia por rango de líneas, `cp.py` y `build.py`, que montan el tema
copiando literalmente de los ficheros de origen), fuera del repositorio. `indice.py` sólo sobre el
tema; `refutar_prosa.py`: 1 hallazgo (la Carta citada en portada y trazabilidad: aceptable).

## Avisos al coordinador (manda la fuente)

1. **RGC, anexo II, arts. 34 y 35**: redacción dada por BOE-A-2026-12035, vigente desde el
   06-06-2026 (leída con `boe.py`). No nombran los rodajes; el tema lo dice y los da para eventos
   que ocupan la vía. El art. 2 del anexo (pruebas deportivas: 30 días, competencia JCT/CA/ayuntamiento)
   tiene una sola redacción, de 2004.
2. **RD 517/2024**: arts. 53-58 anulados (STS 19-VI-2025, BOE-A-2025-14308); el art. 40 sigue en su
   redacción original. He añadido, leídos en el BOE, el **art. 60.1** (AESA autoridad competente)
   y el **art. 8** (seguro), que la investigación no traía: sustituyen al «en España la autoridad
   competente es AESA» que el tema de RTVE daba sin fuente.
3. **Reglamento (UE) 2019/947**: el pasaje de RTVE (arts. 3, 5.1-5.2, 14.1 y 14.5) viene del texto
   publicado sin consolidar. El reglamento tiene modificaciones posteriores que no he podido leer
   (EUR-Lex no devolvió el consolidado). **El verificador debe cotejar esos cuatro preceptos con la
   versión consolidada.**
4. **Páginas web releídas el 25-09-2026** (con lector web, que puede resumir): ADA confirma las dos
   frases de la investigación; para costa y patrimonio devolvió textos distintos de los de la
   investigación y he usado los nuevos («Será necesaria la obtención de la autorización de uso del
   dominio público marítimo terrestre.»; «Solicitud de autorización para la cesión de uso de bienes
   inmuebles (museos, conjuntos arqueológicos o enclaves)»). DGT confirma la frase literal y la
   competencia (vías interurbanas y travesías salvo País Vasco y Cataluña; urbanas, autoridades
   locales), dada en redonda. Las frases de «Ordenanzas y tasas» vienen de la investigación, no
   releídas. Conviene que el verificador las abra en navegador.
5. **Cuaderno ATA**: el tema de RTVE daba «doce meses, no prorrogables», «cámaras de comercio» y
   sus rasgos sin fuente (Convenio de Estambul no consultado). He sustituido el epígrafe por la
   página de la Cámara de Comercio de España (leída 25-09-2026): «Válido durante 12 meses», uso
   profesional. Quitado «no prorrogables» y la tabla de rasgos.
6. **Quitado de RTVE por ser de RTVE o de examen**: Monte de El Pardo, todas las referencias a
   preguntas y plantillas, Avid Command, LU800/LU300S, el recorrido Prado del Rey-Torrespaña, el
   convenio de la Corporación, el practicable (RD 486/1997, tema 14), el coordinador de estudio.
7. **Cruces de otros temas quitados** del texto de Cámara Operador 03 («es el tema 10», «el tema
   14, y ... el tema 11», «epígrafe «Estudio»», «epígrafe anterior»): cortados o adaptados (ver
   abajo). Las remisiones que quedan son a temas de este puesto (5, 6, 9, 10, 11, 12, 14, 15).
8. **Negritas**: las de RTVE se han quitado al copiar (palabras intactas); las de Canal Sur copiadas
   se conservan; las nuevas son literales de fuente. Las citas del Libro de estilo están escritas
   con «fi» normal donde el PDF trae la ligadura «ﬁ» (pasar `negritas.py` con NFKC).

## Copiado del común (no se re-verifica)

Literal, sin cambiar una palabra, de temas ya cerrados de Canal Sur (líneas del fichero de origen):

| Pasaje en el tema 32-T08 | Origen literal |
|---|---|
| «Qué cambia fuera del plató»: frase de entrada y tabla (sin la remisión final al tema 10) | `temas/canal-sur-especificos/08-camara-operador/03-captacion-eng-estudio-exteriores-um-directos.md`, l. 407-417 |
| «Qué es una retransmisión»: primer párrafo | `08/03`, l. 602-606 |
| «Las retransmisiones en el Libro de estilo y en la Carta»: primer párrafo (8.4 y 8.4.2) | `08/03`, l. 614-618 |
| «Eventos especiales: señal *pool*…»: párrafo y tabla | `08/03`, l. 706-716 |
| «Qué es una unidad móvil»: entero | `08/03`, l. 469-481 |
| «El montaje de una unidad móvil»: frase de entrada y lista de nueve pasos | `08/03`, l. 568-580 |
| «La regla del Libro de estilo» (Seguridad): 5.6 y 8.3.4, dos párrafos | `08/03`, l. 446-458 |
| «Contribución, distribución y control central»: entero | `08/03`, l. 637-652 |
| «Las vías de salida de la señal»: entero (tabla, satélite, mochila y los cuatro datos de la UIT-R SNG.770-2) | `08/03`, l. 531-564 |
| «La preparación» (Directos): los dos párrafos del Libro de estilo (8.3 y 8.1.6) | `08/03`, l. 725-737 |
| «La prueba de la señal y el retardo»: primer párrafo | `08/03`, l. 770-773 |
| «Grabar siempre»: entero | `08/03`, l. 809-817 |
| Carta, art. 16 (guion) | `temas/canal-sur-comun/06-carta-servicio-publico-y-estatuto-profesional.md`, l. 436-441 |
| Ley 18/2007, arts. 30 y 31 (dos guiones) | `temas/canal-sur-comun/05-ley-18-2007-rtva.md`, l. 772-778 |
| Convenio, art. 53, dieta de rodaje (guion) | `temas/canal-sur-comun/07-x-convenio-colectivo.md`, l. 1028-1030 |
| Convenio, art. 39, seguro de desplazamientos a zonas de riesgo (frase) | `07`, l. 847-848 |
| Ley 13/2022, art. 101.3 (guion) | `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md`, l. 1122-1125 |

**Adaptado de temas cerrados de Canal Sur** (se verifica): «Qué es una retransmisión», punto 2
(«del epígrafe anterior» → «del epígrafe «Telecomunicaciones»»); «El montaje de una unidad móvil»,
frase «Los dos puntos donde una retransmisión se rompe…» (`08/03`, l. 583-586) más una frase mía;
«La regla del Libro de estilo», párrafo final (primera frase de `08/03`, l. 460-461, más texto mío);
«La prueba de la señal y el retardo», segundo párrafo (`08/03`, l. 775-781 sin «(epígrafe
«Estudio»)»); «El falso directo» (cita de 8.3.3 releída en el Libro de estilo y frase mía).

## Copiado de RTVE sin cambios

Fila 32/8 de `produccion-informacion.tsv`: `actualizar = no`. Pasajes literales, sólo sin las
negritas de énfasis; ninguna palabra cambiada; ninguno cita norma:

| Pasaje en el tema 32-T08 | Origen (fichero RTVE, líneas) |
|---|---|
| «Qué es localizar»: entero | `temas/produccion/08-produccion-en-exteriores.md`, l. 51-63 |
| «Qué se comprueba en una localización»: tabla | `produccion/08`, l. 69-79 |
| «La regla: se pide a quien es titular»: frase de entrada y párrafo final (el cuadro de en medio está adaptado) | `produccion/08`, l. 122-123 y 136-137 |
| «El campamento base y el *compound*»: párrafo, tabla y lista de lo que se prevé | `produccion/08`, l. 95-101 y 109-116 |
| «Desplazamientos internacionales»: entero | `produccion/08`, l. 242-256 |
| «Lo que producción gestiona de un enlace por satélite»: primer párrafo | `temas/produccion/12-transporte-de-la-senal.md`, l. 125-128 |
| «Las mochilas de agregación»: dos párrafos | `produccion/12`, l. 139-145 |
| «La producción remota»: párrafo y tabla | `produccion/12`, l. 178-188 |
| «Eventos especiales…»: tabla señal internacional / personalizada / *host broadcaster* | `temas/realizacion-tv/18-produccion-de-programas-directos-y-grabados.md`, l. 240-244 |

**Copiado literal de RTVE que cita norma (sí se verifica)**: «El rodaje con dron: la norma
europea», los cuatro primeros párrafos (Reglamento (UE) 2019/947, arts. 3, 5 y 14), de
`produccion/08`, l. 170-205. Ver aviso 3.

**Adaptado de RTVE** (se verifica): cuadro de quién autoriza (fila «Espacio aéreo» cambiada); frase
de los requisitos eléctricos (`produccion/08`, l. 81-89, sin la pregunta); «Quién decide qué»
(`realizacion-tv/18`, l. 74-85, sin coordinador de estudio ni convenio de la Corporación); prosa de
la señal internacional, IBC, *running order* y canal de repeticiones (`realizacion-tv/18`,
l. 246-284, sin preguntas ni FORTA/BBC/OBS); párrafo de la UIT-R en el satélite (`produccion/12`,
l. 130-133); párrafo tras la tabla de producción remota (`produccion/12`, l. 190-199).

## Lo nuevo (se verifica entero)

Libro de estilo 4.4-4.4.4 (pp. 75-78) y 8.3.2-8.3.4, releídos en `libro-de-estilo-333233b.txt`
(l. 2605-2745, 4180-4212); RGC art. 55.1 y anexo II arts. 2.1, 2.3, 34 y 35; RD 517/2024 arts. 8,
40, 53 (nulidad) y 60.1; RD 393/2007 norma 3.1 y anexo I 1.d y 2.g (volcado local); ADA, DGT y
Cámara de Comercio (web); rúbricas de urgencias y coordinación institucional; aplicación práctica.

## Preguntas de control (10)

Contestadas sólo con el tema. Todas: **entera**.

1. Según el Libro de estilo de Canal Sur, ¿qué se canalizará siempre a través de los productores?
   a) Sólo los permisos y las acreditaciones; b) Las localizaciones, asistencias externas, gestión
   de medios propios, permisos, seguros, acreditaciones...; c) La escaleta; d) La contratación de
   personal propio. → b (rúbrica 1, 4.4.4 punto 9). Entera.
2. A la hora de elegir una localización, lo fundamental para el correcto funcionamiento del equipo
   técnico es: a) el presupuesto; b) la proximidad a zonas turísticas; c) los requisitos
   eléctricos; d) la luz natural. → c (Localizaciones). Entera.
3. Según la Junta de Andalucía, ¿quiénes son las autoridades competentes de las autorizaciones de
   rodajes? a) Las delegaciones del Gobierno; b) Los ayuntamientos; c) La ADA; d) La DGT. → b
   (Permisos). Entera.
4. Un operador de UAS obligado a registrarse que va a volar un dron sobre una procesión en una
   capital debe comunicarlo al Ministerio del Interior con una antelación mínima de: a) 24 horas;
   b) cinco días hábiles; c) cinco días naturales; d) diez días hábiles. → c (Permisos, RD 517/2024
   art. 40.3.a; supuesto 1). Entera.
5. (Práctica) Una prueba ciclista discurre íntegramente por carreteras de dos provincias andaluzas.
   ¿Quién la autoriza y quién la solicita? a) La DGT, a petición de la televisión; b) La comunidad
   autónoma, a petición del organizador, con al menos 30 días de antelación; c) Cada ayuntamiento;
   d) La Jefatura Central de Tráfico, con diez días hábiles. → b (Permisos, anexo II art. 2; supuesto
   3). Entera.
6. Una actividad de espectáculos públicos al aire libre está obligada, en general, a tener plan de
   autoprotección con un aforo igual o superior a: a) 2.000; b) 2.500; c) 10.000; d) 20.000
   personas. → d (Seguridad, RD 393/2007 anexo I 1.d). Entera.
7. La validez de un cuaderno ATA es de: a) 6 meses; b) 12 meses; c) 24 meses; d) se negocia en cada
   viaje. → b (Transporte). Entera.
8. La vía de contribución que llega desde cualquier sitio, pensada por la UIT-R para transmitir con
   escaso tiempo de aviso, es: a) la fibra óptica; b) el enlace de microondas; c) el satélite
   (DSNG); d) la red FTTH. → c (Telecomunicaciones). Entera.
9. Según el Libro de estilo, las peticiones a los productores se cursan: a) siempre de viva voz;
   b) por escrito, salvo razones infrecuentes y de extremada urgencia; c) por escrito, sin
   excepción; d) a través del realizador. → b (Urgencias, 4.4). Entera.
10. Según la Ley 18/2007, el órgano de comunicación con la Administración electoral durante los
    procesos electorales es: a) el Consejo de Administración; b) la persona titular de la Dirección
    General de la RTVA; c) el Consejo Audiovisual de Andalucía; d) la Dirección de Servicios
    Informativos. → b (Eventos especiales y Coordinación institucional, art. 30). Entera.

Reparto: rúbrica 1 (1, 10), localizaciones (2), permisos (3, 4, 5), seguridad (6), transporte (7),
telecomunicaciones (8), urgencias (9), coordinación institucional (10); logística y directos se
cubren en los supuestos prácticos (1 y 2) del tema. Sin lagunas: no ha hecho falta ampliar.
