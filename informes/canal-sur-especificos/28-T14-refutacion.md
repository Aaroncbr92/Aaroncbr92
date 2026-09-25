# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`
(801 líneas). Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). No se corrige
nada: sólo se informa. Ficheros tocados: este informe y `28-T14-preguntas.md`.

Resultado: **0 graves, 4 menores, 5 lagunas**. Preguntas: 8 enteras, 1 a medias, 6 no.

## Alcance y fuentes

- Exactitud: todo el tema salvo los 11 pasajes «Copiado de RTVE sin cambios» de
  `28-T14-redaccion.md` (no hay «Copiado del común»). Cobertura: el tema entero.
- Fuentes leídas el 25-09-2026: UIT-R BS.775-4 (PDF de itu.int, pasado a texto; recomienda 1-11,
  notas 1-5, anexos 2, 3, 4 —tabla 2 completa—, 5 y 7 con su adjunto 1); UIT-R BS.1770-5 (anexo 4 y
  remisiones a otras recomendaciones); EBU Tech 3343-2023 (`fuentes/normas-tecnicas/`, § 4.2, § 6,
  § 7.1, § 7.2); EBU Technical Review 2009-Q1; SMPTE RDD 19-2011; Dolby ED2 Technology Brief; guía
  del Dolby Atmos Renderer v3.0; RTW «Focus: The Multi Correlator». Las cinco últimas, en las copias
  de texto que dejó la verificación en el directorio de trabajo.
- Lentes automáticas: tema técnico sin norma legal; `refutar_prosa.py` e `indice.py` ya dieron 0 en
  verificación y no se ha tocado el tema desde entonces.

## Exactitud: lo comprobado sin hallazgo

Cotejadas contra la fuente todas las citas en negrita de BS.775-4 (resumen, considerandos,
recomienda 2-5, notas 4, anexos 2, 4 y 7, adjunto 1 —AC-3 «only 120 Hz», «10 dB of gain», cinco
canales de banda completa—), las de la Tech 3343 (LFE excluido, 5.0, *dialnorm* −27/−31 y descarte
de metadatos, dos vías del downmix, Lo/Ro y Lt/Rt con ±90°, cinco factores, lista de coeficientes,
+1,5/−3/4,5 dB, divergencia y 3 LU, preferencia Lo/Ro, saturación, perfiles y Extended BSI,
coeficientes por defecto de la BS.775-2, upmix), las de la *Technical Review* (definición, «up to
six», tramas y banda de guarda, trama no modificable, 40 ms, In-Sync/Advanced, «helpfully» y doble
retardo, ciclo decodificar-procesar-codificar), RDD 19 (diez ciclos, ocho señales, 30 cuadros,
cada dos cuadros P, «NOT a Standard»), ED2 (16 canales, 8 por subflujo, compatibilidad), Atmos
(7.1.2, 118 objetos, 128 entradas, 64 a 96 kHz) y RTW (−1/0/+1, 0,3-0,7, multicorrelador). Los
coeficientes 1/0, 2/0 y 3/0 del tema coinciden con la tabla 2 de la −4. Recuentos (cinco factores,
siete requisitos, tres planos, siete rúbricas) cuadran.

## Hallazgos menores (4)

1. **Cita cruzada (1/9)** — «Lo que este tema no da», primer punto (l. 754-756): «la UIT-R BS.2076
   (modelo de definición del audio para objetos): … sólo consta su existencia por la cita de la
   BS.1770-5». La BS.1770-5 no cita la BS.2076 (búsqueda de «2076» en el texto: 0); cita la BS.2051 y
   la BS.2127 (renderizador ADM de la UIT, anexo 4). Proponer: sustituir BS.2076 por BS.2127 o quitar
   la mención.
2. **Salvedad omitida (6)** — tabla «La colocación de los altavoces», fila «Altura de los frontales»
   (l. 428). La fuente sigue: «This implies an acoustically transparent screen. Where a
   non-acoustically transparent screen is used, the centre loudspeaker should be placed immediately
   above or below the picture. The height of side/rear loudspeakers is less critical». Es justo el
   caso de un control de televisión. Añadir.
3. **Salvedad omitida (6)** — «El retardo de un cuadro» (l. 306-307): «In-Sync Encoded» se queda en
   «en sincronía con el vídeo»; la fuente añade «The decode delay must be compensated for at the
   decode site by the use of an equivalent video delay». Sin esa frase, la aplicación práctica de
   l. 317-319 y el punto 6 de «Producir una señal multicanal compatible» quedan cojos.
4. **Salvedad omitida (6)** — «El canal LFE», último párrafo (l. 471-473): la opción 5.0 de la Tech
   3343 sigue con «This is typically the case for the majority of broadcast content with the notable
   exception of mainly action movies». Refuerza lo que el tema dice de la televisión; añadir la frase.

## Lagunas de cobertura (5)

Cada una sale de una pregunta contestada «no» o «a medias», y todas tienen fuente ya leída salvo la 5.

1. **Compatibilidad con los receptores existentes (BS.775-4, recomienda 6 y anexo 3)**. El tema trata
   la compatibilidad como downmix, transporte y metadatos, pero no cita los dos métodos que la propia
   BS.775 da para pasar de 2/0 a 3/2 sin dejar fuera receptores: el *simulcast* del servicio 2/0 (que
   luego puede suprimirse) y las matrices de compatibilidad (A y B por los canales L y R existentes,
   T, Q1 y Q2 por canales adicionales; menos capacidad). Tampoco el recomienda 7 (downmix «if
   required», antes de la transmisión o en el receptor) ni el 8 y anexo 5 (conversión ascendente de
   la UIT; el tema sólo da la UER). Ampliar en «La compatibilidad descendente como requisito». (P10.)
2. **Envolvente mono y resto de la tabla 2**. Falta que la señal MS **«is fed to both LS and RS
   loudspeakers»** (recomienda 3), la nota 5 (con más de dos traseros, LS a todos los de la izquierda
   y RS a los de la derecha, con la ganancia reducida para igualar potencia) y los destinos 2/1, 3/1
   y 2/2 de la tabla 2 (S = 0,7071 LS + 0,7071 RS; en 2/2, LS y RS a 1,0 y el central a 0,7071 en L y
   R). El tema anuncia los seis formatos reducidos y sólo da tres. Ampliar en «El mono y el
   envolvente mono» y «Los coeficientes de la UIT». (P7, P9.)
3. **Calibración del LFE**. Falta el anexo 7: los +10 dB se miden dentro de la banda de menos de
   120 Hz con medidor selectivo en frecuencia; con sonómetro de banda ancha el ruido rosa del LFE no
   leerá +10 dB; y «For broadcasting applications … positive offset gain of 10 dB». Es aplicación
   práctica directa (montar y calibrar una escucha). Ampliar en «El canal LFE». (P6.)
4. **LFE de Dolby E frente a LFE de AC-3** (BS.775-4, anexo 7, adjunto 1, § 6): el LFE del Dolby E
   admite más banda que el del AC-3, y una señal de banda ancha llegará filtrada al espectador; con
   PCM lineal el riesgo crece. Es una compatibilidad entre sistemas Dolby que el enunciado pide.
   Ampliar en «Dolby E y Dolby Digital» o en «El LFE no es el subgrave». (P13.)
5. **Emisión del audio inmersivo y del 5.1 más allá del AC-3**: el tema no dice con qué sistemas de
   emisión llega al público el Dolby Atmos (ni menciona Dolby Digital Plus o AC-4), y tampoco lo
   declara en «Lo que este tema no da». Un tribunal puede preguntarlo bajo «Dolby». No se ha leído
   fuente en esta fase: o se amplía con documentación de Dolby o de ETSI/DVB leída en su original, o
   se declara el hueco.

## Para el remate

Los hallazgos 2-4 y las lagunas 1-4 son citas de fuentes ya leídas (BS.775-4, Tech 3343, *Technical
Review*): remate con ampliación, por Opus, y 5 bis sobre los pasajes nuevos. La laguna 5 necesita
fuente nueva o, como mínimo, una línea en «Lo que este tema no da».
