# 04 · Ayudante de Producción · Tema 7 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/07-gestion-operativa-de-localizaciones-espacios-y-permisos.md`
(9.712 palabras tras la verificación; 35 epígrafes, sin cambios de rúbrica). Verificado el 06-10-2026.

Ficheros tocados: el tema y este informe. Ninguno más.

## Lo copiado: sólo comprobación de literalidad

Script de cotejo por frases (sin negritas, espacios normalizados) del tema contra Productor T08, T12
y T02 y contra RTVE `produccion-asistencia/05` y `produccion/08`.

- **Copiado del común**: todos los pasajes listados en `04-T07-redaccion.md` aparecen literales en
  Productor T08, T12 o T02. Las únicas frases que no coinciden son los cambios que el redactor
  declaró (remisiones al tema 11 y al tema 16, «materia de la rúbrica anterior», párrafo nuevo al
  final de «El proceso, paso a paso»). No se han vuelto a verificar.
- **Copiado de RTVE sin cambios** (§1, tabla de §2, «tres ojos», §4 del *cover set*): literal, con
  sólo las negritas de énfasis quitadas. No se han vuelto a verificar.

## Lo nuevo y lo adaptado: verificado en la fuente

Fuentes leídas hoy (06-10-2026):

| Fuente | Cómo | Resultado |
|---|---|---|
| X Convenio RTVA, BOJA 240/2014, ficha 5212705 | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Objeto, las diez tareas, cláusula de lista abierta y pág. 110: coinciden |
| Libro de estilo (PDF pasado a texto) | 4.4, 4.4.1, 4.4.4 (puntos 1 y 9), 5.6 | Las citas coinciden (con normalización de ligaduras) |
| Ley 39/2015, arts. 21, 24, 68 | `boe.py precepto`, redacción única (vig. 02-10-2016) | Citas literales; dos salvedades omitidas (abajo) |
| Decreto 15/2011, BOJA núm. 30 (PDF oficial descargado por el redactor, en el scratchpad; no está en `fuentes/`) | arts. 25, 27, 28, 29 y anexo | Citas literales; una salvedad omitida y un matiz del anexo (abajo) |
| Reglamento (UE) 2019/947, art. 19.2 | DOUE original y consolidado EUR-Lex 01-05-2025 | Igual en los dos (el consolidado sólo añade un apdo. 6) |
| RGC, anexo II, art. 35 | volcado BOE consolidado de 25-09-2026 | Coincide con lo que el tema afirma |

Todas las citas entre comillas del cuerpo se cotejaron con script: 0 sin fuente.

## Correcciones aplicadas

1. Error 9 (cita mal apoyada). «Quién va a localizar»: la ficha no nombra la localización. La cita
   de «colaborando en todo lo necesario con el productor» se presentaba como apoyo de la tarea de
   localizar. Ahora se dice que es oficio y que esa tarea se refiere a grabaciones, montajes y directos.
2. Error 6. Decreto 15/2011, art. 29.1: «La Delegación Provincial resuelve» omitía que resuelve la
   Dirección General cuando la actuación supera una provincia. Añadido.
3. Error 4 (podrá). Anexo del Decreto 15/2011: el procedimiento abreviado se da para actividades
   para las que «los interesados podrán solicitar» la autorización. Se cita esa frase y el cálculo del
   calendario queda condicionado a pedirla por esa vía.
4. Error 6. Ley 39/2015, art. 21.1: faltaba la excepción de los procedimientos sometidos sólo a
   declaración responsable o comunicación, que afecta a las comunicaciones que el tema trata.
5. Error 6. Ley 39/2015, art. 24.1: faltaba «excepto en los supuestos en los que una norma con rango
   de ley... establezcan lo contrario».
6. Error 9. «el silencio sólo se invoca con su certificado» chocaba con el 24.4, que admite
   cualquier medio de prueba. Ahora dice: «mejor con su certificado, aunque la ley admite cualquier
   medio de prueba».
7. Error 6. Tabla «La resolución que no llega»: «sólo cabe recurso» omitía el art. 24.3.b, que
   permite a la Administración resolver después sin quedar vinculada al silencio. También
   faltaba el límite del día anterior para el cierre de una vía (RGC 35). Añadidos los dos.
8. Error 9. «El parte de incidencias»: el Libro de estilo no pide que «los cambios vayan por
   escrito». Pide que se comuniquen «de manera rápida, fehaciente y simultánea». Corregido.
9. Portada, «Normativa» y «Trazabilidad»: el art. 19.2 del Reglamento 2019/947 ya consta cotejado
   con el consolidado. En la «Trazabilidad» del Libro de estilo se añade la relectura de hoy.

## Lentes

- `negritas.py` (BOE, DOUE, Decreto, Libro, convenio, DGT): 81 cotejadas. Hay 13 «no está». Son
  rótulos y supuestos (3), la página ADA, que no está guardada y viene del común (3), y citas del
  Libro cortadas por ligaduras o saltos de página. Esas citas sí están en el texto, comprobado con
  normalización. Atribuidas a otro artículo: 0.
- `refutar_exactitud.py` (fuentes BOE/DOUE): 16 «no literales», todas del Decreto 15/2011 o del Libro
  de estilo, que no son fuentes BOE de la lente; cotejadas a mano: literales.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0. `indice.py`: 35 epígrafes, índice sin cambios.

## Avisos que siguen abiertos (declarados en el tema)

- Tensión Decreto 15/2011 (29.2, silencio estimatorio) / Ley 39/2015 (24.1, desestimatorio si puede
  dañar el medio ambiente). El tema da los dos textos y no resuelve cuál prevalece.
- Que el abreviado alcance a toda grabación del 25.d: deducción, marcada como tal.
- El Decreto 15/2011 no está guardado en `fuentes/` (sólo en el scratchpad de la sesión). Conviene
  guardarlo si el refutador lo necesita.
- Líneas 324, 345, 474 y 742 quedaron más largas que el resto tras las correcciones. No afecta al
  contenido.
