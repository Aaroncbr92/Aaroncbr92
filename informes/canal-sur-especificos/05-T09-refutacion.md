# Ayudante de Realización (05) · Tema 9 · Fase 4 · Refutación

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/09-mezcladores-efectos-transiciones-senalizacion.md`
Fecha: 30-09-2026 (el encargo computado fija «hoy» en el 24-09-2026; manda la del sistema). Fuentes
releídas hoy: `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt`, `fuentes/fabricantes/TSL_UMD-protocol.txt`,
`fuentes/canal-sur/realizador/incual-IMS077_3.txt`, `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`.
No se ha corregido nada: sólo se informa.

Alcance de la exactitud: lo que el informe de redacción da como nuevo o adaptado. Se saltan lo
«Copiado del común» (tema 33/09) y lo «Copiado de RTVE sin cambios» (las tres piezas de «El piloto»).
La cobertura mira el tema entero.

## Lentes automáticas

- `negritas.py` (ATEM, TSL, IMS077_3, RD 1680/2011): 167 negritas, 10 no halladas, todas en texto
  copiado de 33/09 (Adobe, DaVinci Resolve, Mateu Torres, Libro de Estilo 8.6.1: fuentes no locales).
  Ninguna del texto nuevo falla.

## Exactitud: lo comprobado sin hallazgo

- IMS077_3: título, Orden PCI/797/2019, UC0217_3 RP1, CR1.2, CR1.3, CR2.1 (p. 7), MF0217_3 «Técnicas de
  realización en control», CE1.5 (cita parcial declarada como tal) y CE1.6 (p. 18), contenidos 5 y 6
  (p. 20): literales y bien paginados.
- ATEM, señalización (pp. 1066-1067): SmartView, ocho relés, puerto Ethernet, hasta ocho unidades,
  5 V a 14 mA y 30 V a 1 A; puesta en marcha (comprobación de pilotos, verde y rojo, avería típica,
  CALL por SDI de retorno); botones rojo/verde en los buses; «Al aire» en la ventana de cámara; barras de
  las cámaras con tono; brillo del piloto delante y detrás (SDI Camera Control Protocol 5.0-5.2);
  protocolo embebido v1.0 (30/04/14), SMPTE 291M, DID/SDID x51/x52, VANC línea 15, cuatro bits (0 programa,
  1 previo). Todo correcto.
- TSL (19/09/09): gratuidad, uso en multipantalla, V3.1 (RS 422/ RS 485, 38k4, dirección 0-126 + 80 hex,
  cuatro bits de piloto y dos de brillo, 16 caracteres, sentido único), V4.0 (0 OFF, 1 RED, 2 GREEN,
  3 AMBER), V5.0 (UDP, 2048 bytes, TCP/IP opcional, 65,535, ASCII o Unicode), V3.1/V4.0 sobre UDP/IP.
  Todo correcto. «UMD, sigla que el documento de TSL no desarrolla»: cierto.
- Remisiones internas a los epígrafes 1-7 del propio tema: correctas.

## Hallazgos

Graves: 0.

Menores: 3.

1. **Recuento de vías del piloto (errores 3 y 9), epígrafe 7 · «Cómo llega el piloto a la cámara y a
   los monitores»**, tabla y párrafo «Por el retorno SDI». El tema da «cuatro vías» y separa «Retorno
   SDI» de «Datos en la señal». La fuente citada para el retorno (manual ATEM, l. 1017-1023 del volcado)
   dice que el piloto de las cámaras Blackmagic se enciende verde y rojo, pero no por dónde va; el
   retorno SDI lo nombra sólo para la llamada (l. 1029-1030) y el control de cámara (l. 771-772). Y el
   protocolo embebido describe precisamente un mezclador que mete el piloto en su programa y lo manda a
   las cámaras: probablemente es el mismo camino, no dos. Propuesta: o presentarlas como una sola vía
   (el piloto viaja dentro de la señal que el mezclador devuelve a la cámara, según el protocolo
   embebido) y hablar de tres vías, o decir que el manual no aclara si el piloto del retorno usa ese
   protocolo. Verdict: plausible.
2. **Salvedad omitida (error 6), mismo apartado, «Por contacto»**: «con varias se reparten los
   pilotos: «se pueden asignar las luces piloto 1-8…»». El manual lo condiciona: **«Si se conecta un
   dispositivo GPI and Tally Interface a un mezclador ATEM 2 M/E o 4 M/E, es posible asignar distintas
   luces piloto a cada unidad a través del programa ATEM Setup.»** Propuesta: añadir «en los ATEM 2 M/E
   y 4 M/E, desde el programa ATEM Setup». Verdict: confirmado.
3. **Trazabilidad (redactada como nueva), fila del Libro de Estilo**: cita 3.6.1, 3.10, 3.16 a 3.16.2,
   6.5.1, 6.5.2, 8.6.1 y 9.9.2 y dice que sostienen «rótulo, cierres, gráficos, criterio de realización
   informativa, vestuario ante el croma, imágenes duras». El tema sólo usa 8.6.1 (vestuario ante el
   croma); lo demás es arrastre de la fila de 33/09, cuyo texto no se ha copiado aquí. Propuesta:
   dejar «8.6.1 · Vestuario ante el croma» (y, si se quiere, mencionar 6.5 como remisión de «no da»).
   Verdict: confirmado.

Nota sin contar (en texto copiado del común, que no se corrige por exactitud): la «Advertencia sobre las
fuentes» dice que el Libro de Estilo **da** el criterio de la casa sobre los recursos en informativos, y
«Lo que este tema no da» dice que ese criterio lo desarrolla el temario del Realizador/a. El rematador
puede ajustar la frase de la Advertencia para que no prometa lo que el tema remite.

## Cobertura del enunciado

«Mezcladores de vídeo, efectos, transiciones, incrustaciones, chroma, DVE y señalización técnica»: los
siete términos tienen su epígrafe, en el orden del enunciado, con teoría, lo que pide la cualificación
al ayudante y aplicación práctica. «Señalización técnica» se interpreta como piloto, llamada,
multipantalla, etiquetas, sincronismos y generadores de señales, y el tema declara que ninguna fuente la
define: es interpretación razonable.

Preguntas (`05-T09-preguntas.md`): 15; enteras 13, a medias 1 (transporte de IS-07, declarado en «no
da»), no 1 (norma de las barras de HD, declarada en «no da»).

Lagunas: 1. La norma de las barras de color de alta definición: el tema la declara no leída, pero la
recomendación UIT-R BT.2111 es de acceso libre; si se obtiene, una o dos líneas en «Los generadores de
señales del control» cerrarían la pregunta 15. No se amplía nada más.

## Ficheros tocados

- Creados: `informes/canal-sur-especificos/05-T09-preguntas.md` y este informe. El tema no se ha
  modificado. Ningún otro fichero.
