# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`
(8.400 palabras). Fecha de trabajo y de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en
24-09-2026). No corrijo: el remate aplica.

Fuentes releídas el 25-09-2026: Audinate, *Dante Controller User Guide* 4.18.x (6-V-2026);
SMPTE ST 2110-30:2025; ST 2022-7:2019. Del resto (ST 2110-10, ST 2059-1/-2) me fío de la verificación,
que las cotejó cita a cita; no he visto motivo para dudar.

Excluido de la lente de exactitud: nada «Copiado del común»; los 9 bloques «Copiado de RTVE sin
cambios» (informe de redacción). La cobertura mira el tema entero.

## Lente 1 · Exactitud

### Grave

1. **Error 9, afirmación contraria a la fuente** («Unicast y multicast», tabla, fila «Canales por
   flujo», columna multicast): el tema dice «La guía no da una cifra». La guía sí la da, en
   «Troubleshooting › Fanout › About Transmit Flows»: **«Multicast flows can be configured with up to
   64 channels (depending on the Dante device type).»** Corrección propuesta: sustituir la celda por
   esa cita. El mismo pasaje trae dos datos útiles para el epígrafe: **«100Mbps links in particular
   are easily saturated when large numbers of multicast flows exist (and would be overwhelmed by 1
   channel of video). Therefore, multicast flows should only be used when there is a good reason to
   do so.»** y, para unicast, **«support up to 4 channels of audio simultaneously […] If you were to
   then subscribe a fifth audio channel, a second flow would have to be created.»** (refuerza el
   «typically» del ejemplo de los diez canales).

### Menor

2. **Error 6, salvedad omitida** («SMPTE ST 2110-30», párrafo tras la tabla de niveles): el tema
   presenta las cifras de Audinate (AX hasta 8, CX hasta 64) como discrepancia y zanja «Manda la
   norma: 1 a 4 canales en AX y 9 a 32 en CX». La propia norma (cl. 7) añade: **«Senders and
   receivers may support more channels than required by Table 2, providing they are able to operate
   within the maximum number of channels required for the claimed conformance level.»** Es decir, un
   equipo con más canales no incumple por sí solo. Propuesta: citar esa salvedad y dejar la tabla 2
   como el mínimo que exige cada nivel, sin afirmar que Audinate contradice la norma.

Resto comprobado sin hallazgo: tabla 2 (seis niveles, cifras exactas); 48 kHz «shall» y 44,1/96
«should»; nota del SDI; límite UDP; clases A-D de la ST 2022-7 y sus PD; citas de Audinate sobre
latencia (1 ms, 150 µs, 100 Mbps, Ultimo 1 ms/2 ms ya declarado, multicast 1 ms), PTPv1/v2, EF/CS7,
dominio 0, redundancia; cálculos (1,152; 36,9; 73,7; 49,2; 11,5; 1.152 octetos).

## Lente 2 · Cobertura del enunciado

Las seis rúbricas (audio sobre IP, redes, sincronía, latencia, PTP, redundancia) tienen epígrafe
propio, en el orden del enunciado, con teoría y aplicación práctica. Preguntas: **12 enteras, 0 a
medias, 3 no** (`28-T15-preguntas.md`). Lagunas (se amplía el tema, con la fuente citada):

- **L1 · Niveles de los receptores** (preg. 5): el tema sólo da la tabla 2 (emisores). Falta la regla
  de la cl. 7 (**«receivers shall support all possible combinations of sampling clock rate, packet
  time and channel count within the ranges as defined in Table 3»**) y la tabla 3: un receptor de
  nivel superior admite también los inferiores (p. ej., C: 48 kHz con 1 ms y 1 a 8 canales, y con
  125 µs y 1 a 64).
- **L2 · Canales por flujo multicast** (preg. 6): la misma del hallazgo 1; al corregirlo se cubre.
- **L3 · Dominios de reloj por *pull-up/down*** (preg. 12, rúbrica «Sincronía»): Audinate DC 4.18,
  «Clock domains»: **«Dante devices can only transmit media to, and receive media from other devices
  on the same clock domain (whether that is PTPv1 or PTPv2)»**, con el ejemplo del +4,1667 % y el −1 %,
  y **«Up to 5 separate clock domains can be supported at any one time. All clock domains have their
  own leader clock.»** Encaja en «Sincronía» con una línea de aplicación práctica (dos equipos que no
  se oyen aunque la suscripción exista).

## Lentes automáticas

Tema técnico sin norma legal: la verificación pasó `refutar_prosa.py` e `indice.py` y no se ha
modificado el tema después; no se repiten.

## Resumen para el remate

1 grave (multicast «sin cifra»), 1 menor (salvedad de la cl. 7), 3 lagunas (una coincide con el
grave). Es ampliación con fuente: remate por Opus y revisión 5 bis de los pasajes cambiados.

## Aviso de reuso

El usuario da por hecho un 75 % de RTVE; la redacción midió ≈ 7 % literal y ≈ 5 % adaptado. El
reuso aquí casi no ahorra.

## Ficheros tocados

Creados `28-T15-preguntas.md` y este informe. Nada más; el tema no se ha tocado.
