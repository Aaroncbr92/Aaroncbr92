# 04 · Ayudante de Producción · Tema 5 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/05-documentacion-de-produccion.md`
(1.418 líneas, unas 15.100 palabras según la verificación, 68 epígrafes). Refutado el 06-10-2026
(el encargo dice «hoy es 24-09-2026»; el reloj marca 06-10-2026, fecha de lectura de cada fuente).
No se corrige: se informa.

Ficheros tocados: este informe y `04-T05-preguntas.md`. El tema, no.

Recuento: **0 graves, 4 menores, 1 laguna.**

## Alcance

- **Exactitud**: lo nuevo y lo adaptado según `04-T05-redaccion.md`, más los cambios declarados
  dentro de los pasajes copiados (remisiones renumeradas). Se saltan «Copiado del común» y
  «Copiado de RTVE sin cambios».
- **Cobertura**: el tema entero contra el punto 5 del enunciado (BOJA núm. 186, anexo V, puesto 2.4):
  planes y órdenes de trabajo, citaciones, partes, listados, escaletas, hojas de ruta, permisos,
  autorizaciones, necesidades técnicas y documentación de cierre. Las diez familias tienen rúbrica
  propia, en el orden del enunciado.

## Fuentes releídas hoy (06-10-2026)

| Fuente | Fichero | Resultado |
|---|---|---|
| X Convenio RTVA, ficha 5212705 | `documentos/x-convenio-rtva-boja-240-2014.txt`, l. 4689-4714 | Objeto, diez tareas y cláusula abierta: literales; art. 12 (l. 267-268) y DT 7.ª (l. 2596-2599): literales |
| IMS074_3 | `produccion/incual-IMS074_3.txt` | Ámbito (l. 41-42), ocupaciones (l. 52-78), UC0207_3 CR1.2-1.4, CR2.3 y productos; UC0208_3 CR3.1, CR4.6, CR4.7, productos e información; UC0209_3 CR1.2, CR1.5, CR1.6, RP2, CR2.1-2.2, CR3.1, productos e información; MF0207_3 CE3.2, CE6.1-6.3; MF0208_3 CE2.6, CE2.8; MF0209_3 contenidos: todo literal y bien atribuido (comprobada la pertenencia de cada CR/CE a su unidad o módulo por número de línea) |
| RD 1681/2011 | `radio/BOE-A-2011-19600.txt` | Art. 5.m, 7.2; 0915 RA 2.c, 2.f; 0916 RA 2.a, 2.e, 2.g, 3.b, 3.c, 4.f, 4.g, 4.h, 5.a, 5.g; 0917 RA 1.a, 1.g, 2.b, 5.b; 0918 contenidos; 0919 RA 2.f, 4.e, 5.a, 5.b, 5.d, 5.f y contenidos: literales, con RA y letra correctos (cotejados con los rótulos de cada RA) |
| Ley 3/2012 | `BOE-A-2012-13126.md` | Art. 3.c (l. 203) y art. 22 (l. 375): literales |
| Decreto 54/1989; Decreto 404/2000 | `produccion/decreto-54-1989-…txt`, `produccion/decreto-404-2000-…txt` | Art. 5.1 y 6 (erratas «ordenes», «trasporte» confirmadas); art. 39 nuevo: literal; fechas y BOJA de la portada y Trazabilidad: correctos |
| Orden de 16-XII-1987 | `documentos/BOE-A-1987-28546.txt` | Para L1: art. 3.º a) y b) (l. 112-116) y apartado de comunicación urgente (l. 126) |
| Tema 17 del puesto | `temas/…/17-prevencion-…md` | No trata la comunicación ni el parte de accidente (véase M2) |

Lentes: `refutar_prosa.py` 1 hallazgo («TAS», falso positivo, parte del nombre de la Orden);
`remisiones.py` sobre la carpeta: sin remisiones salientes del tema 5 a temas que no casen por título.

## Hallazgos graves

Ninguno. Todas las citas literales de lo nuevo están en su fuente y bien atribuidas.

## Hallazgos menores

**M1. «Cinco documentos a cinco escalas», párrafo final (línea 294): la ficha, resumida de más
(error 9/6).** «El plan de producción y el plan de trabajo los diseña el Productor/a; el Ayudante
colabora en los dos.» La ficha distingue: **«Colaborar con el productor en la definición del plan de
producción del programa y en la ejecución del plan de trabajo.»** En el plan de trabajo el Ayudante
colabora en la ejecución, no en el diseño (que la ficha del Productor/a le da a éste: «Diseñar y
elaborar el plan de trabajo…»). Un test que pregunte «en qué colabora el Ayudante respecto del plan
de trabajo» puede ofrecer «en su elaboración» como distractor, y esa frase lo avala (pregunta 1).
**Propuesta**: «…el Ayudante colabora en la definición del primero y en la ejecución del segundo.»

**M2. «Partes que no son de producción», primera viñeta (línea 657-658): remisión a un tema que no
lo trata (error 1).** «La comunicación de incidencias y accidentes en producción, en el tema 17.» El
tema 17 del puesto no menciona el parte de accidente, la Orden TAS/2926/2002, Delt@ ni plazo alguno
de comunicación (búsqueda de «parte de accidente», «TAS/2926», «Delt@», «comunicaci… accidente»: 0
resultados; sólo trata el concepto de accidente in itinere y en misión, art. 156 LGSS). Es un cambio
declarado del pasaje copiado de 32-12 («en los temas 14 y 15» → «en el tema 17»), así que entra en
la refutación. **Propuesta**: resolverlo con L1 (dar aquí lo mínimo) y dejar la remisión al tema 17
sólo para el accidente in itinere y en misión.

**M3. «Un documento sin definición publicada» (línea 823-825) y Trazabilidad (línea 1390): fecha de
lectura del Libro de estilo.** El tema dice que ninguna fuente «leída para este tema» define la hoja
de ruta, incluido el Libro de estilo, y la tabla de Trazabilidad lo pone entre las «Fuentes leídas
el 06/10/2026». El Libro de estilo no tiene volcado en el repositorio y no se ha releído en este
ciclo (lo dicen la redacción, aviso 2, y la verificación, «Para la refutación»): sus citas vienen de
temas cerrados. **Propuesta**: en la Trazabilidad, pasar el Libro de estilo a la lista «Tomado de temas
cerrados…»; en la hoja de ruta, decir «ni el Libro de estilo en los apartados citados» o quitarlo de
la enumeración.

**M4. Portada y «Normativa que el tema invoca»: omisiones de recuento (error 3).** (a) La tabla de
normativa no incluye el RD 1681/2011 (arts. 5.m y 7.2 y módulos 0915-0919) ni el RD 1680/2011
(módulo 0904), que son reales decretos y sostienen buena parte del tema, ni el Decreto 404/2000
como norma modificadora (sólo entre paréntesis). (b) La portada, en «Fuente», da del RGPD los
«artículos 5 y 7», pero el tema cita también el 28.3 (tabla de «Autorizaciones de menores…» y fila
del RGPD en la normativa). **Propuesta**: añadir las dos filas de RD a la tabla y «28» a la portada.

## Lagunas

**L1. El parte de accidente: plazo y vía (rúbrica «Partes»).** El tema dice que el parte de
accidente tiene modelo oficial y que se transmite por Delt@, pero no cuándo ni a quién se remite, y el
tema 17 tampoco lo da (M2). Es pregunta natural de aplicación práctica para quien lleva los partes de
una grabación y ayuda al productor en PRL (ficha: **«Ayudar al productor en el cumplimiento de la
legislación de prevención de riesgos laborales.»**). Fuente en el repositorio: Orden de 16-XII-1987
(`BOE-A-1987-28546`), cuyo modelo sustituyó la Orden TAS/2926/2002 sin derogar los plazos:
art. 3.º a), el parte se remite **«a la Entidad gestora o colaboradora que tenga a su cargo la
protección por accidente de trabajo, en el plazo máximo de cinco días hábiles, contados desde la
fecha en que se produjo el accidente o desde la fecha de la baja médica»**; art. 3.º b), la relación
de accidentes sin baja, mensual, **«en los cinco primeros días hábiles del mes siguiente»**; y la
comunicación urgente, **«en el plazo máximo de veinticuatro horas»**, a la autoridad laboral, en los
accidentes mortales, graves o muy graves o que afecten a más de cuatro trabajadores (l. 126).
**Propuesta**: tres o cuatro líneas en la viñeta, con estas citas (el rematador debe comprobar en el
texto consolidado del BOE que esos apartados siguen vigentes tras la Orden TAS/2926/2002) y dejar
claro que el parte lo cursa la empresa (recursos humanos o prevención); al Ayudante le toca dejar
el hecho en el parte del día, como ya dice el tema. Pregunta 15: **no**.

## Cobertura del enunciado

| Rúbrica del enunciado | Epígrafes | Juicio |
|---|---|---|
| Planes de trabajo y órdenes de trabajo | 7 | Completa (salvo M1) |
| Citaciones | 5 | Completa |
| Partes | 6 | Completa salvo L1 |
| Listados | 3 | Completa |
| Escaletas | 4 | Completa; remite lo de escritura al tema 4 |
| Hojas de ruta | 3 | Completa como oficio, declarado; sin fuente que la defina |
| Permisos | 2 | Completa en lo documental; proceso, tema 7 |
| Autorizaciones | 6 | Completa |
| Necesidades técnicas | 4 | Completa |
| Documentación de cierre | 8 | Completa |

Preguntas (`04-T05-preguntas.md`): **13 enteras, 1 a medias (14, analogía de espectáculos que el
tema cita truncada; no es laguna), 1 no (15, L1).**

## Para el remate

M1, M3 y M4 son correcciones de pasaje (Sonnet). L1 amplía (Opus) y arrastra M2; si se amplía,
corresponde 5 bis sobre la viñeta.
