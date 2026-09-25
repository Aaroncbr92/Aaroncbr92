# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.
Fecha de trabajo y de lectura de todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).

## Fuentes releídas (25-09-2026)

- Audinate, *Dante Controller User Guide* 4.18.x, AUD-MAN-DanteController-4.18.x-v1.0, publicada el 6-V-2026 (`fuentes/canal-sur/sonido/audinate/dc-latest.txt`).
- SMPTE ST 2110-30:2025 (aprobada 1-X-2025) y ST 2110-10:2022 (aprobada 28-III-2022) (`fuentes/normas-tecnicas/`).
- SMPTE ST 2059-2:2021, ST 2059-1:2021, ST 2022-7:2019 (`fuentes/canal-sur/sonido/smpte/`).

## Copiado sin reverificar

- «Copiado del común»: nada.
- «Copiado de RTVE sin cambios» (9 bloques, 29 fragmentos): comprobados por script contra
  `temas/sonido/16-audio-sobre-ip.md`, normalizando negrita, ✔ y espacios. Los 29 son literales en
  el tema y en el original. No se han reverificado en fuente.

## Método para lo demás

- Las 140 citas en negrita «…» se buscaron por script en los seis volcados (normalizando comillas,
  guiones de corte de línea y espacios): todas aparecen, cada una en la fuente que el tema le
  atribuye. Tres casos con corte de palabra en el PDF (`con-sume`, `fre-quency`, `audio-overIP`)
  revisados a mano: literales.
- Revisados a mano, en su fuente: tabla 2 de la ST 2110-30 (niveles y canales); tabla 1 de símbolos
  (M, DM, ST, LtRt, 51, 71, 222, SGRP, U01…U64) y ejemplo 1; fechas y títulos de las cinco normas;
  valores y rangos del perfil ST 2059-2 (§6.5: 128/0-255, 127/0-127, 0/−3…+1, 3/2-10, −3/−7…−1);
  ± 5 ppm (§6.7.1, para el *grandmaster* de referencia de la instalación); clases A-D de la ST 2022-7
  y definiciones SBR/HBR; límites UDP y anexo A de la ST 2110-10; IPv6 «should»; PTPv1
  desactivable (Audinate: «PTPv1 can be disabled if required»); criterios de elección del
  *leader*; aviso «Clock Sync Warning»; Wi-Fi y multicast.
- Cálculos rehechos: 1,152 Mbit/s; 36,9 y 73,7; 49,2 (16 bits); 11,5; 1.152 octetos en A, AX, C y
  CX; 64 × 48.000 × 24 = 73,7 Mbit/s; 2⁰ = 1 s y 2⁻³ = 1/8 s. Correctos.
- Lo adaptado de RTVE (lista del informe de redacción): verificado con lo anterior; sólo falló la
  frase del PTP (abajo, 4).

## Hallazgos y correcciones (aplicadas)

1. **Error 9, afirmación sin fuente** («AES67»): «los flujos AES67 son multicast» apoyado en
   «Multicast flows can carry … RTP audio». La cita dice que el multicast *puede* llevar RTP, no que
   AES67 sea sólo multicast (la guía tiene además un «Unicast Port: RTP unicast port number»).
   Reescrito: «los flujos multicast de Dante pueden llevar audio RTP».
2. **Error 4/6, «podrá» por «deberá» y salvedad omitida** («Por qué hace falta un reloj común»):
   el tema decía que la ST 2110-10 pide el reloj común sólo como recomendación. Proveerlo es
   «should», pero admitirlo es «shall» (§7.2: «All Devices conforming to this standard shall
   support a Common Reference Clock delivered via IEEE Std 1588-2008»). Añadido con la cita.
3. **Error 6, salvedad omitida** («Los valores de Dante»): la guía dice en otro pasaje que los
   Ultimo tienen 2 ms de mínimo (contradice el 1 ms del ejemplo) y que **«Multicast flows are
   automatically set to a minimum of 1ms»**. Añadidas las dos cosas; el ejemplo se conserva como
   mecanismo. Discrepancia interna de la guía: 1 ms (p. de latencia) frente a 2 ms (p. del
   histograma); además, en el histograma dice «multicast flows always use a latency of 1ms», y en la
   lista «a minimum of 1ms»: el tema cita la segunda.
4. **Error 9** («Qué es el PTP», adaptado de RTVE): «mide el retardo de la red y lo compensa». La
   ST 2059-2 §6.4 sólo dice que hay un mecanismo de *medida* del retardo; cómo se corrige es del
   IEEE 1588, no leído. Cambiado a «mide el retardo del camino» y se declara que el detalle de la
   corrección está en el IEEE 1588 no leído.
5. **Error 6, cita cortada** («ST 2022-7»): la cita de la ST 2110-10 terminaba en «ST 2022-7»; el
   texto sigue «and as constrained in section 8.5 of this standard». Completada; se dice que el 8.5
   regula la señalización de los flujos duplicados.
6. **Completitud, con fuente** («El conmutador de red»): añadido **«Dante audio and video
   transmission over Wi-Fi is not supported.»**, que responde a una pregunta obvia sobre Wi-Fi.
7. Trazabilidad actualizada (Audinate: 2 ms, multicast 1 ms, Wi-Fi; ST 2110-10: obligación de
   admitir el reloj y §8.5). Extensión de la ficha: 8.200 → 8.400 (`indice.py`: 8.397 palabras).

Cada pasaje cambiado se releyó: los antecedentes («la misma guía», «su apartado 8.5», «esa
medida») tienen delante su referente.

## Lentes (tema técnico sin norma legal)

- `refutar_prosa.py`: sin relleno, sin frases repetidas, sin negritas rotas; 3 avisos de siglas
  (IP y PTP en el título, TRUE dentro de una cita), falsos positivos ya declarados por la redacción.
- `indice.py`: índice sin cambios (no se tocó ningún epígrafe).
- No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Aviso al coordinador sobre el reuso

La persona usuaria cree que este tema tiene un 75 % de RTVE. Medido: el literal sin cambios son
unas 600 palabras de 8.400 (≈ 7 %) y el adaptado otras 400. El ahorro del reuso aquí es pequeño.

## Ficheros tocados

- Modificado el tema 15 (pasajes de los hallazgos 1-7).
- Creado este informe. Nada más.
