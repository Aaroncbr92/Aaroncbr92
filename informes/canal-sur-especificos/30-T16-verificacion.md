# Puesto 30 · Tema 16 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Todas las fuentes se releyeron el 25-09-2026.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/16-prevencion-riesgos-laborales.md`.

## 1. Lo copiado: sólo literalidad

Comprobado con un script que compara línea a línea el tema con 28/16
(`temas/canal-sur-especificos/28-operador-a-de-sonido/16-prevencion-riesgos-laborales.md`): de 1.623
líneas, **315 no están literalmente en 28/16**, y todas caen en los pasajes que el informe de
redacción declara nuevos o adaptados (portada, siglas, «Qué se puede preguntar», «De dónde sale»,
tabla de disciplinas, ficha 5212206 y DA 2.ª, tabla de riesgos, intros de auriculares, ejemplos
sustituidos, definición de pantalla, calidad de imagen, ROSA/ESCAM, «La sala de edición», EPI del
montador, resumen, normativa, «Lo que no da», trazabilidad). El resto (bloques «Copiado del común»)
es literal y no se re-verifica. «Copiado de RTVE sin cambios»: ninguno.

## 2. Lo nuevo y lo adaptado: releído en su fuente

| Fuente | Qué se cotejó | Resultado |
|---|---|---|
| X Convenio, BOJA 240/2014 (txt), p. 190 | Ficha 5212206: código, denominación, objeto, ocho tareas, cláusula de cierre | Literal |
| Id., l. 1540 | «* OPERADOR/A MONTADOR/A DE VÍDEO» en la relación por niveles | Consta; el nivel no se atribuye al convenio (correcto) |
| Id., DA 2.ª | Centros, «a título enunciativo», tres tareas, cuatro trabajadores, rotatoria, 30 %, no consolidable | Literal |
| Id., art. 29.1, 29.4-29.6 | Planificación anual, descanso, drogodependencias, terapia 75/25 % | Literal |
| Ley 31/1995 (BOE-A-1995-24292) | Arts. 21.2, 29.1, 29.2.1.º | Literal |
| RD 286/2006 (BOE-A-2006-4414) | Art. 3.1; fecha 10-III-2006; DA 2.ª (Guía y Código de conducta) | Correcto |
| RD 488/1997 (BOE-A-1997-8671) | Art. 1.3 d) y e), 2 c), 4.3 | Literal |
| Guía técnica PVD, INSST, junio 2021, NIPO 118-21-032-5 | Definición de pantalla; «elemento mínimo indispensable»; 90 %; acabado mate; «no ofrece una metodología específica»; ROSA; ESCAM; cuestionario de iluminación; 300-500 lux; 0°-25°; luz sobre la pantalla; correctores y gafas antirreflejo; ausencia de trato de varias pantallas (búsqueda de «varias/dos/segunda pantalla», «monitores») | Literal / confirmado |
| UIT-R BT.2100-3 (02/2025) | Título, texto previo al cuadro 3, cuadro 3, nota 3a | Literal |
| RD 1299/2006 (anexo 1, 2D0101) | Denominación [sic] y actividades | Literal |
| RD 773/1997 (BOE-A-1997-12735) | Anexo III, filas de visibilidad y frío; notas de anexos I y III | Literal |
| Tema 7 del común | Qué dice de la DA 2.ª | Sólo la resume; no trata su vigencia actual |

`negritas.py` contra esas fuentes: las negritas de los pasajes nuevos que no aparecen son rótulos, la
definición de pantalla de la Guía (partida por un salto de página en el txt; cotejada a mano,
literal) y las cifras del cuadro del RD 286/2006 (atribuidas al 5.1 en la tabla: falso aviso).
`refutar_modo.py`: 0 hallazgos. `refutar_exactitud.py`: avisos sólo por cruce de numeraciones
(artículos del convenio contra la LPRL) y rótulos. `refutar_prosa.py`: 0. `indice.py`: 39 epígrafes,
19.558 palabras.

## 3. Correcciones aplicadas

1. **Error 9 (cita cruzada al común).** «Si esa disposición sigue aplicándose hoy… lo trata el tema
   del temario común dedicado al convenio»: el tema 7 del común sólo la resume. Ahora: «no consta en
   las fuentes leídas; el tema del temario común dedicado al convenio la resume». Igual en «Lo que
   este tema no da».
2. **Error 8.** La frase de la Guía sobre el «elemento mínimo indispensable» está en el comentario de
   la letra b) (puesto de trabajo), no de la a). Se precisa.
3. **Error 6/9.** «El montador no figura entre los ejemplos» del 2D0101 era ambiguo (los ejemplos
   incluyen **montadores de estructuras**). Ahora «El montador de vídeo» y se citan los ejemplos.
4. **Error 6.** Cuadro 3 de la BT.2100-3: se añade que da también el formato 7 680 × 4 320.
5. **Error 9.** «Enchufar un equipo… es una operación de ese tipo» (art. 4.3.a RD 614/2001): la
   norma exige material **concebido para su utilización inmediata y sin riesgos por parte del público
   en general**; se rebaja a lectura del tema («a una toma ordinaria… encaja, en lectura de este
   tema»).
6. Portada: extensión 19.509 → 19.558 palabras.

Releídos los pasajes cambiados: «esa disposición», «la letra b)», «ese supuesto» tienen antecedente.

## 4. Sin cambio

Nivel B04 atribuido al enunciado (correcto). Las diez preguntas del informe de redacción siguen
contestándose enteras.

## Ficheros tocados

El tema y este informe. Script de comparación en el scratchpad.
