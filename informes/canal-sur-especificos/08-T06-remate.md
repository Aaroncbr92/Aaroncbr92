# Puesto 08 · Tema 6 · Fase 5 · Remate

Fecha: 25-09-2026 (encargo fechado el 24-09-2026). Tema:
`temas/canal-sur-especificos/08-camara-operador/06-captacion-de-sonido.md`.
Base: `08-T06-refutacion.md` (4 menores, 2 lagunas y 1 de reserva) y `08-T06-preguntas.md`
(11 enteras, 1 a medias, 3 no). Copia previa en el scratchpad (`t06r/06-antes-remate.md`).
**Amplía contenido nuevo: sí** (procede 5 bis).

## Fuentes leídas

- EBU R 68-2000 (copia local), 24/25-09-2026: «can be 3 dB greater».
- *Libro de estilo de Canal Sur*, 2004 (copia `.txt`), p. 82: la frase de las dos noticias.
- Sony PXW-Z200 Help Guide (copia `.txt`), p. 261: nota de ***[1kHz Tone on Color Bars]***.
- DPA Microphones, *Mic University* y diccionario, leídos el 25-09-2026 con curl. Extractos literales
  guardados en `fuentes/fabricantes/DPA_mic-university_extractos.txt`: «Proximity effect in
  microphones explained», «Proximity Effect» (diccionario), «About balanced and unbalanced lines»,
  «Balanced and Unbalanced Lines» (diccionario), «Electromagnetic interference: EMC, RFI immunity and
  CMRR», «10 points on microphones in installed systems». La página de Shure devolvió 403 y otra URL
  de DPA, 404: no se usaron.

## Correcciones de exactitud

| Nº | ¿Se aplicó? | Comprobación | Pasaje cambiado |
|---|---|---|---|
| M1 | Sí | R 68: **«can be 3 dB greater»** | «Por qué 18 dB de reserva»: «suelen quedar» → «pueden quedar» |
| M2 | Sí | Libro de estilo, p. 82, frase siguiente confirmada | «Antes de grabar»: la cita de las barras añade «Si hay dos noticias en el mismo soporte deben separarse con un minuto de barras.» |
| M3 | Sí | Z200, p. 261, nota literal confirmada | «Los mandos de nivel de la cámara», fila ***[1kHz Tone on Color Bars]***: añade la nota y, en «Para qué», que los canales 3 y 4 llevan el tono aunque su entrada esté apagada |
| M4 | Sí (se quita) | Sin fuente leída | «Sonido en la cámara o sonido aparte»: se borra «Es como se ha trabajado en cine desde que existe el sonoro.» |

## Lagunas: se amplía el tema

| Nº | Epígrafe | Qué se añade | Fuente |
|---|---|---|---|
| L2 (p. 14) | Nuevo `### El conector XLR y la línea balanceada` (tras «La cadena de audio de una cámara», antes de `## Microfonía`) | Definición de línea balanceada; patillas 1, 2 y 3; tabla balanceada / no balanceada; rechazo en modo común y CMRR; impedancias iguales; fantasma sólo con línea balanceada; cable no balanceado corto; qué induce ruido | DPA (literal); la paráfrasis «la entrada se queda con la diferencia», resumen de la cita |
| L1 (p. 13) | Nuevo `### El efecto de proximidad` (tras «Los patrones polares») | Definición (dos de DPA) y ejemplo de la voz; tabla patrón / omni / distancia (<1 m) / ángulo (90° en cardioide); causa (gradiente de presión); respuesta plana de cerca y ficha; uso con el micrófono de mano | DPA (literal); el uso, oficio |
| Reserva (p. 15) | «Los ambientes ruidosos», ampliado | **«The SPL from point sources drops by 6 dB/doubling of distance.»**; de 40 a 20 cm, unos 6 dB; de 40 a 10 cm, unos 12 dB | DPA; las cifras, cálculo; boca como fuente puntual y ruido de fondo constante, oficio |

Quitado al releer, por no tener fuente: que un ruido de viento o de manipulación salga reforzado en
graves con un direccional cerca, y que un zumbido al mover el cable delate una soldadura o una
conexión no balanceada.

## Otros pasajes cambiados

- Siglas de entrada: EMI, CMRR y SPL.
- Portada: «Fuente» añade DPA Microphones; «Extensión» pasa a 10.700 palabras.
- «Qué se puede preguntar»: efecto de proximidad, línea balanceada, caída con la distancia.
- «Trazabilidad»: fila nueva de DPA (leída el 25/09/2026, y así se dice en la frase de fechas);
  la lista de oficio y la de cálculo, ampliadas.
- «Lo que este tema no da» y «Recomendaciones técnicas»: sin cambios (DPA no es una recomendación).
- Relectura de antecedentes: «Y en su diccionario» (DPA), «Para que funcione» (el rechazo en modo
  común), «Dicho de otro modo» (la tabla), «suma, además, el efecto de proximidad» (definido antes
  en el tema): todos con su antecedente.

## Lentes

`indice.py`: 10.676 palabras, 45 epígrafes; índice regenerado con los dos nuevos. `refutar_prosa.py`:
0 relleno, 0 repeticiones, 0 negritas rotas; 4 avisos de siglas: PXW (código de producto, ya
conocido), DPA (nombre de la empresa, no sigla) y EMC y RFI (sólo dentro del título en inglés de una
página, en «Trazabilidad»): sin hallazgo. Sin normas jurídicas: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema 6, este informe y `fuentes/fabricantes/DPA_mic-university_extractos.txt` (nuevo). Los
cambios en otros temas del puesto que aparecen en `git status` no son míos.
