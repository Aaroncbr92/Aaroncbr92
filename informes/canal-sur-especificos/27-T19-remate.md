# Puesto 27 · Tema 19 · Remate

Fase 5 · Rematar. Fecha de trabajo y de lectura de las fuentes: **05-10-2026** (el encargo fija «hoy»
en 24-09-2026; ninguna redacción usada tiene vigencia entre ambas fechas).

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/19-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.
Entrada: `27-T19-refutacion.md` (5 menores, 3 lagunas) y `27-T19-preguntas.md` (4 «no»).

**Resultado: 5 correcciones aplicadas, 3 lagunas cerradas ampliando el tema.** Amplió contenido nuevo:
sí (procede la fase 5 bis sobre los pasajes listados abajo).

## Ficheros tocados

- Tema 19 (editado).
- Creados: este informe; `fuentes/canal-sur/DOUE-L-2016-80531.md` (Reglamento (UE) 2016/425),
  `fuentes/canal-sur/DOUE-L-2025-80611.md` (su corrección de errores) y
  `fuentes/canal-sur/DOUE-L-2024-81663.md` (Reglamento (UE) 2024/2748, que lo modifica), los tres con
  `doue.py`; `fuentes/canal-sur/tecnica/insst-ntp-223.html` (página del INSST, descarga del 05-10-2026)
  y `insst-ntp-223.txt` (con `documento.py texto`).
- No he tocado `fuentes/canal-sur/DOUE-L-2019-81880.md`, que ya estaba sin seguimiento en git y es de
  otro tema.

## Correcciones (comprobadas en la fuente antes de aplicarlas)

| # | Fuente releída | Veredicto | Pasaje cambiado |
|---|---|---|---|
| M1 | RD 614/2001, anexo III.C.1.a) | Correcto | Tabla «Quién puede hacer qué», fila «Trabajos en tensión»: añadida la salvedad literal de la reposición de fusibles en BT por trabajador autorizado, con remisión al tema 15 |
| M2 | Título del epígrafe en el tema | Correcto | Tabla de «Los riesgos específicos…»: «La manipulación manual de cargas» → «La manipulación de cargas» |
| M3 | RD 614/2001, anexo III.A.1 y art. 3.1 | Correcto: ambas frases siguen | «…ensayado sin tensión [...]»** y «…ambientes corrosivos [...]»** |
| M4 | X Convenio, ficha 9311200 | Correcto: «habitualmente» no consta | «el oficial trabaja habitualmente en pareja con su ayudante» → «el oficial puede trabajar con su ayudante, al que la ficha encarga auxiliarle y colaborar con él» |
| M5 | RD 614/2001, anexo IV.A.2 | Correcto: el sujeto es el método y los equipos y materiales | «Los EPI en la RTVA…»: ahora cita el sujeto literal y aclara que el EPI protege junto con el método y los demás equipos |

## Ampliaciones (lagunas)

- **L3 · Ruido** (pregunta 14). En «Los riesgos generales: las cuatro disciplinas preventivas», tras la
  tabla: párrafo y tabla del RD 286/2006 (BOE-A-2006-4414, una redacción, vigente desde 31-03-2006),
  art. 5.1 (87/85/80 dB(A); 140/137/135 dB(C)), art. 5.2 (atenuación de protectores sólo para el valor
  límite) y art. 7.1.a) y b) (protectores a disposición / de uso). Título de la norma comprobado en
  boe.es. La pregunta 14 queda **entera**.
- **L1 · Espacios confinados** (pregunta 7). La NTP 223 sí se obtuvo (enlace actual del portal del
  INSST). En «Los espacios confinados» se sustituye el párrafo «Como práctica de oficio…» por las medidas
  de la NTP 223, con su advertencia literal de que no es obligatoria: autorización de entrada (válida
  una jornada), medición previa y continuada, tabla de valores (**oxígeno no inferior al 20,5 %**;
  «muy peligroso» por encima del 25 % del límite inferior de inflamabilidad; control continuo si puede
  superarse el 5 %), aislamiento y bloqueo, ventilación forzada (nunca con oxígeno), vigilancia externa
  y rescate. «Evitar la entrada» se presenta como aplicación del art. 15 de la Ley 31/1995. Los umbrales
  de alarma del explosímetro no se dan: el texto extraído sale corrupto («el 10% y el 2025%»).
  **Aviso sobre la pregunta 7**: ninguna de sus opciones (15 / 19,5 / 21 / 23,5 %) coincide con la
  fuente (20,5 %). No la recorto; quien la use en el banco debe poner 20,5 % como opción correcta.
  Con esa opción, queda **entera**.
- **L2 · EPI, comercialización** (pregunta 13). En «Los EPI en la RTVA…», nuevo bloque «Qué exige hoy
  la norma al EPI que se compra»: enlace art. 5.3 RD 773/1997 → Reglamento (UE) 2016/425 (art. 1;
  aplicable, con excepciones, desde 21-04-2018 según la ficha del BOE); marcado CE (arts. 3.18, 8.2,
  8.7, 17.1-17.3); tres categorías (art. 18 y anexo I, con las letras a, b, g, h y m de la categoría
  III); módulos de evaluación (art. 19). Revisadas su única modificación (Reglamento (UE) 2024/2748,
  aplicable desde 29-05-2026: añade puntos 19 y 20 al art. 3 y el capítulo VI bis) y su corrección de
  errores (DOUE-L-2025-80611: toca el art. 41 bis añadido): no afectan a lo citado. La pregunta 13 queda
  **entera** (c, categoría III).

## Otros pasajes cambiados por arrastre

- Ficha: «Fuente» (añadidos Reglamento (UE) 2016/425, RD 286/2006, NTP 223), «Redacción que se
  estudia» (2016/425 no consolidado), «Extensión» 21.305 → 22.850 palabras (cuenta de `indice.py`).
- «Qué se puede preguntar»: NTP 223, ruido y marcado CE / categorías.
- «Las medidas preventivas del puesto, en resumen»: filas nuevas de espacios confinados (NTP 223) y
  ruido; fila de EPI con marcado CE.
- «Normativa que el tema invoca»: filas del Reglamento (UE) 2016/425 y del RD 286/2006.
- «Lo que este tema no da»: reescrita la entrada de espacios confinados; nuevas de ruido y de EPI.
- «Trazabilidad»: filas del Reglamento (UE) 2016/425, RD 286/2006 y NTP 223; frase final.

Releídos todos los pasajes cambiados: cada «ese apartado», «artículo 7.1», «(5.2)» tiene delante su
norma; ninguna remisión queda sin antecedente.

## Lentes

- `indice.py`: 22.850 palabras, 42 epígrafes; índice sin cambios (no hay epígrafes nuevos). Avisa
  «sin portada: es un esquema» porque el tema no está en `portadas.tsv`; la ficha es manual y la he
  actualizado a mano.
- `negritas.py` (RD 614/2001, RD 286/2006, Reglamento 2016/425, RD 773/1997, NTP 223): ninguna negrita
  nueva fuera de fuente salvo los rótulos de entrada («Qué exige hoy…», «Tres categorías de riesgo»),
  igual que los rótulos ya existentes; el arranque del párrafo del ruido, que no es literal, se pasó a
  redonda. Las demás «no está» son de fuentes no pasadas a esta corrida (ya verificadas en fase 3).
- `refutar_exactitud.py` (RD 286/2006, RD 614/2001): ninguna cita nueva no literal. El volcado del
  2016/425 repite números de artículo por anexos y la lente no sirve sobre él (lo avisa `doue.py`):
  sus nueve citas se han comprobado una a una con `grep` (todas presentes).
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos.
