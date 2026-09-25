# Puesto 08 · Tema 17 · Fase 3 · Verificación

Tema: `temas/canal-sur-especificos/08-camara-operador/17-prevencion-riesgos-laborales.md`
(15.048 palabras tras la verificación, según `indice.py`; ficha actualizada). Fecha de trabajo y de
lectura de todas las fuentes: **24-09-2026**.

## Alcance

- Saltado, como manda el encargo: lo listado bajo «Copiado del común» (LPRL 14, 15, 17-22, 29 y
  párrafo de entrada).
- Copiado del tema 20 de Redactor/a (cerrado, enunciado idéntico): no re-verificado; comprobado
  que es literal con `diff` contra `34-redactor-a/20-…md`: todas las diferencias caen en los
  pasajes que la redacción declara «nuevo o adaptado».
- Nada copiado de RTVE (confirmado: la redacción no lista nada y el diff no muestra texto ajeno).
- Verificado dato a dato: todo lo nuevo o adaptado (hunks del diff).

## Fuentes releídas (24-09-2026)

- RD 1299/2006, `boe.py precepto BOE-A-2006-22169 an1codificacion` (vigente BOE-A-2018-6046, desde
  06-05-2018); metadatos BOE de BOE-A-2006-22169 y BOE-A-2018-6046 (RD 257/2018).
- RD 773/1997 (volcado vigente): art. 10; anexo I nota (*); anexo III título, nota, frío, «IV. Otros
  riesgos / Falta de visibilidad».
- RD 488/1997 (BOE-A-1997-8671): art. 1.3.d) y e); art. 2.c).
- LPRL art. 29.2.1.º (`boe.py precepto BOE-A-1995-24292 a29`).
- X Convenio RTVA (BOJA 240/2014, .txt): anexo III, puesto 5341310; art. 29.4 y 29.6.
- Libro de estilo 2004 (.txt): 5.2 y 5.6.
- INSST tema 69 (V. abril 2025): manguito, lista del paso 5, medidas organizativas.
- INSST Guía MMC (septiembre 2024): transporte, sujeción, ≤ 25 cm, 3-25 kg.
- Metadatos BOE: RD 614/2001 (BOE-A-2001-11881) y RD 286/2006 (BOE-A-2006-4414).
- Tema 14 de este temario (remisiones: rúbricas «Conducción», «Cargas», «En altura»,
  «Aglomeraciones»; RGC 118 y reforma del 1-10-2026; ET 36.1; plus del art. 50.1; PRENSA-PRESS;
  DA única del RD 486/1997): las cuatro rúbricas existen y lo remitido está allí.

## Hallazgos y correcciones aplicadas

| # | Error | Pasaje | Qué decía | Corrección (comprobada en la fuente) |
|---|---|---|---|---|
| 1 | 8 / 1 | Cámara al hombro, RD 1299/2006 | Los tres códigos «dentro» del agente D | Sólo 2D0101 es del agente D; 2E0101 es del agente E y 2F0501 del agente F («…parálisis de los nervios debidos a la presión»). Reescrita la entrada con cada agente y su rótulo literal; «Grupo 2» sacado de la negrita (no es literal) |
| 2 | 6 salvedad omitida | INSST tema 69, lista del paso 5 | «pregunta si el trabajo implica» | La pregunta es «¿El trabajo **repetitivo** implica…»; corregido y añadido «(paso 5)» |
| 3 | 6 / negrita no literal | EPI, efecto sobre TME | **«restringe … dificulta»** (singular, no literal) y «es factor de riesgo de TME» | Literal: **«EPI´s que restringen los movimientos o dificultan la actividad»**, como factor adicional del trabajo repetitivo |
| 4 | 6 salvedad omitida | LE 5.6 | Sólo las «situaciones extremas» | Añadido **«o bien como consecuencia de condiciones hostiles pero no infrecuentes»**, como un atasco |
| 5 | 6 salvedad omitida | LPRL 29.2.1.º | **usar adecuadamente** + objetos | Añadido **«de acuerdo con su naturaleza y los riesgos previsibles»** |
| 6 | 9 | Definición del puesto y §4 | «no incluye conducir»; «lo normal es que el cámara no sea conductor profesional en el sentido de la NTP» | La definición no es lista cerrada: «no nombra conducir» (como en el tema 14 verificado); «no es, por ella, conductor profesional en el sentido de la NTP 1090» (quita la conjetura y nombra la NTP) |

## Confirmado sin cambios

Convenio anexo III 5341310 (objeto, siete tareas y cláusula de lista no cerrada, literales); art.
29.4 (diez minutos, no acumulable, salvedad) y 29.6 (terapia rehabilitadora, 75 %/25 %). RD 1299/2006:
textos de 2D0101, 2E0101 y 2F0501 (con «Entre otros» por el inicio común de 2F0501), erratas
«tendidosa» y «maguito» del BOE, fecha de 10-11-2006, codificación desde 06-05-2018. RD 773/1997:
notas de los anexos I y III, título del anexo III, filas de falta de visibilidad y frío, art. 10.
RD 488/1997: 1.3.d) portátiles, 1.3.e), definición de trabajador. LE 5.2 (trípode/hombro, en 5.2 y
no en 5.1) y 5.6 (cita del periodista). INSST tema 69: manguito, cuatro preguntas, medidas
organizativas. Guía MMC 2024: definiciones, ≤ 25 cm, evaluación desde 3 kg. RD 614/2001 y RD
286/2006: número y objeto. Ficha, siglas (MMC presentada), Normativa y Trazabilidad cuadran.

## Lentes

- `negritas.py` (LPRL, RD 488, 486, 773, ET, RD 1299, convenio, LE, INSST tema 69, Guía MMC, Guía
  PVD, NTP 1090): 564 negritas, 138 no halladas y 4 «mal atribuidas». Las no halladas son rótulos o
  pasajes copiados de fuentes no pasadas (LGSS, Anuario, NTP 318/443/502, CNSST) del tema 20
  cerrado; la única nueva no literal era la del hallazgo 3, corregida. Las 4 atribuciones: en
  pasajes copiados o falso positivo (art. 21.2 citado bien).
- `refutar_exactitud.py`: 27 negritas y 34 citas «no literales»: rótulos y citas del convenio/LE
  con número de artículo de otra norma; falsos positivos revisados.
- `refutar_modo.py`: 3, todos del ET homónimo (arts. 15, 17, 29) que el tema no cita: falsos.
- `refutar_prosa.py`: 0. `indice.py`: regenerado (36 epígrafes).

## Otros ficheros tocados

Ninguno. Volcado auxiliar de RD 1299/2006 en el scratchpad (fuera del repo).
