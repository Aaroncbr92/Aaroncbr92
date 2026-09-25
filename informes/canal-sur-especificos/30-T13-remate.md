# Puesto 30 · Tema 13 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`.
Entrada: `30-T13-refutacion.md` (4 menores, 2 lagunas) y `30-T13-preguntas.md` (13 enteras, 1 a medias, 1 no).

**Se amplió contenido nuevo** (plantillas .mogrt de Premiere): procede la fase 5 bis sobre los pasajes 1 y 5.

## Fuentes releídas y fecha (todas el 25-09-2026)

- Manual de Resolve 21, `proxy.txt`, pp. 215-217 (estado *Waiting* p. 216; «Starting and Stopping» p. 217).
- X Convenio RTVA, ficha 5212206 (BOJA 240/2014, p. 190): lista completa de tareas.
- Ayuda de Premiere en helpx.adobe.com, cinco páginas con fecha «Last updated on Jan 7, 2026», bajadas
  hoy y guardadas como `fuentes/canal-sur/montador/web/adobe-mogrt-*.txt` (cinco ficheros): overview,
  install, add to sequence, export graphic, data-driven.
- Manfredi (2010): no está en `fuentes/`; el hallazgo 2 se comprobó contra el pasaje copiado del común
  en el § 4 del propio tema (ya verificado), que dice que Avid era el ejemplo del autor y estaba
  instalado en Canal Sur, y que los rótulos «irán directamente a la emisión» se refieren a iNews.

## Hallazgos: qué se hizo

| Nº | Hallazgo | Comprobado en | Resultado |
|---|---|---|---|
| 1 | Carpetas vigiladas sin la puesta en marcha (error 6) | proxy.txt pp. 216-217 | Aplicado; además paso 3 de la aplicación práctica y Trazabilidad (pp. 215-217) |
| 2 | Atribución de los rótulos a Canal Sur (error 9) | § 4 del tema (copiado del común) | Aplicado con la redacción propuesta |
| 3 | «El MAM no es otra pantalla» sin marcar | Resolve p. 4418 («several») | Aplicado: rebajado y marcado como oficio |
| 4 | Tarea «Grabar, emitir y reproducir…» ausente | Convenio, ficha 5212206 | Aplicado: frase tras la tabla con esa tarea y con «Repicar cintas…», que tampoco estaba |
| Laguna | Plantillas .mogrt (pregunta 15) | Ayuda de Premiere, 5 páginas | **Ampliado** § 2 |

El informe de refutación no se equivocó en ninguno.

## Pasajes cambiados

1. **§ 1, «Qué automatiza el propio sistema de edición», viñeta «Carpetas vigiladas»**: añadido al
   final «Nada de eso ocurre hasta que el programa se pone en marcha: configuradas la carpeta y el
   formato de la copia, se pulsa *Start* en el panel *Processing* para **«automatically transcode and
   monitor your watch folders»**, y *Stop* lo detiene en cualquier momento (la barra espaciadora
   alterna uno y otro). Mientras no arranca, la carpeta figura como *Waiting*, **«waiting for the
   Blackmagic Proxy Generator to be started or for a folder ahead of it in the queue to be
   finished»** (cap. 8, pp. 216-217).»
2. **§ 2, «Plantillas de rótulo», penúltimo párrafo**: «En Canal Sur, según la fuente de 2010 que se
   cita en el epígrafe 4, …» → «En iNews, según Manfredi (2010), cuyo ejemplo es el sistema entonces
   instalado en Canal Sur (epígrafe 4), …».
3. **§ 3, «El MAM desde la sala de edición», primera frase**: → «Para el montador, el MAM puede no ser
   otra pantalla, sino algo que ve dentro de su programa (oficio), cuando el MAM tiene módulo para ese
   programa. El manual de Resolve lo recoge:».
4. **§ 5, «El montador en el flujo integrado», tras la tabla**: añadido «La tabla elige las tareas que
   tocan el flujo; la ficha tiene otras dos: **«Grabar, emitir y reproducir videos para programas en
   todo tipo de eventos y producciones con selección alternativa a la realización»**, la más cercana a
   la emisión, y **«Repicar cintas orientadas a la producción, emisión y comercialización»**.»
5. **§ 2, «Plantillas de rótulo», párrafo nuevo tras la lista de Resolve** (≈ 230 palabras): qué es un
   .mogrt (literal), para qué sirve (**«titles, lower thirds, and buttons»**), panel *Graphics
   Templates* y tres procedencias; instalación en *My Templates*, instalación múltiple y la salvedad de
   Creative Cloud (literal); uso en la secuencia, pestaña *Edit* de *Properties* y fuentes que faltan;
   exportación desde Premiere con su salvedad (literal: no para .mogrt creados en After Effects) y
   no disponible con dos o más gráficos; plantillas con datos (texto, color, números; fijados en
   After Effects). Fecha de las páginas: 7-I-2026.
6. **Aplicación práctica, paso 3**: «si la casa usa carpetas vigiladas y el generador está en marcha».
7. **«Qué se puede preguntar»**: añadido «qué es un fichero .mogrt».
8. **«Lo que este tema no da»**: la viñeta de .mogrt y Media Encoder queda sólo para las carpetas
   vigiladas de Media Encoder y para el diseño de .mogrt en After Effects.
9. **Trazabilidad**: Resolve cap. 8 pp. 198, 215-217; fila nueva de las cinco páginas de Adobe.
10. **Ficha**: Extensión 8.400 → 8.900.

Antecedentes releídos: «Nada de eso» remite a la transcodificación automática de la frase anterior;
«esa pestaña», «ese panel» y «esas páginas» tienen su antecedente en el mismo párrafo; «la ficha» de
la frase nueva del § 5 es la 5212206 citada en la introducción de la tabla; «epígrafe 4» remite al
sistema de redacción en Canal Sur, donde está Manfredi.

## Preguntas tras el remate

14: entera (Start en *Processing*, estado *Waiting*). 15: entera (.mogrt). Resultado: 15 enteras.

## Lentes

- `indice.py`: 8.935 palabras, 35 epígrafes; índice regenerado.
- `refutar_prosa.py`: 1 hallazgo, el mismo falso positivo de la verificación (MAM en el título; se
  presenta en las siglas).
- `negritas.py` contra las fuentes nuevas de Adobe, `proxy.txt` y el convenio: todas las
  negritas nuevas se encuentran; las «no están» son las de fuentes no pasadas en esta corrida (ya
  cotejadas en la verificación).
- Tema sin norma legal: no proceden `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema 13; este informe; cinco fuentes nuevas `fuentes/canal-sur/montador/web/adobe-mogrt-*.txt`.
