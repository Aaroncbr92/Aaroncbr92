# 34 · T20 · Revisión del remate (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/20-prevencion-riesgos-laborales.md`.
Alcance: sólo los pasajes que lista `34-T20-remate.md`. Otros ficheros tocados: sólo este informe
(una ejecución de `indice.py` sin argumentos, cortada, reescribió varios `temas/general/*.md`
sin cambiar su contenido: `git status` limpio en ellos).

## Fuentes releídas (24-09-2026)

- `boe.py precepto`: RD 486/1997 (BOE-A-1997-8669) art. 8, anexo III (vigente BOE-A-2023-11187) y
  anexo IV (1 redacción); RD 773/1997 art. 7; LGSS art. 156.2.g; ET (BOE-A-2015-11430) art. 36
  (1 redacción, vigente desde 13-11-2015).
- X Convenio (`documento.py seccion … 26`): art. 26.
- INSST: NTP 318, 443, 502, 1149, 1226 (`fuentes/salud-laboral/`); Guía técnica PVD y tema 69 TME
  (`fuentes/prl-especifico/`).

## Comprobación, pasaje por pasaje

| Pasaje | Resultado |
| --- | --- |
| G1: §2 tabla (fila Ergonomía) y 1.er párrafo de «Riesgos específicos» | Remisión correcta a «Otros riesgos del puesto»; antecedentes bien |
| M1: §3 TME, «Qué son» | Literal del tema 69 del INSST confirmado |
| M2: §2 Comités, art. 26.2 | Literal confirmado |
| M3: §5 art. 7 RD 773/1997 | 7.1, 7.2 a)-e) y 7.3 literales |
| M4: LGSS 156.2.g | Literal |
| M5 y «Lo que este tema no da» | NTP 926 (actualiza la 443, según la propia NTP), NTP 1148 (citada en la 1149) y 1213 (citada en la 1226): confirmadas |
| L1/L2: §2 «Otros riesgos del puesto» | Todas las negritas localizadas en NTP 318 (McGrath 1970, estresores, Selye 1936 y tres fases), 443 (factores psicosociales, consecuencias, aviso de no obligatoriedad), 502, 1149 (perfiles, nódulos/RD 1299/2006, evaluación, medidas), 1226 (disfonía, ORL, tres ocasiones, periodicidad) y Guía PVD; años de las NTP confirmados. **Un error, corregido** (abajo) |
| L3: §3 anexo, cifras | 100/200/500/1.000 lux (anexo IV.3), 300/500 lux SLL y rango 300-500 (Guía), 17-27 ºC (III.3.a vigente), 23-26/20-24 °C (Guía), 30-70 % y 50 % (III.3.b), sequedad (Guía): confirmados. **Una salvedad omitida, añadida** |
| Arrastre: portada, «Qué se puede preguntar», resumen de medidas, Normativa, Trazabilidad | Coherentes con el cuerpo |

## Correcciones aplicadas (comprobadas en la fuente)

1. **Error 9/6 · §2, frase de entrada de «Otros riesgos del puesto».** Decía que ninguno de los
   tres riesgos «tiene norma propia en materia preventiva». Falso para el trabajo nocturno y a
   turnos: el art. 36.4 ET exige nivel de protección adaptado y equivalente y evaluación gratuita
   de la salud de los nocturnos. Reescrita: sin reglamento preventivo propio como el de pantallas o
   EPI, y cita literal del art. 36.4 ET. Añadido el ET a portada (Fuente), Normativa y Trazabilidad.
2. **Error 6 · §3, iluminación.** Faltaba que los niveles del anexo IV se miden a la altura de la
   tarea y **deberán duplicarse** cuando un error de apreciación visual pueda suponer peligro o el
   contraste sea muy débil (anexo IV.3). Añadido, con su antecedente («en las zonas donde se
   efectúen tareas…») para que «las mismas» no quede suelto.
3. Portada, Extensión: 13.033 → 13.267 palabras (`indice.py`).

## Lentes

- `negritas.py` (ET art. 36, RD 486 anexo IV): las negritas nuevas, localizadas; sólo salen rótulos
  y un literal de NTP 502 fuera de las fuentes pasadas a esta ejecución (confirmado a mano en la NTP 502).
- `refutar_prosa.py`: 0. `indice.py`: 13.267 palabras, 34 epígrafes.
- Antecedentes releídos en los pasajes tocados: «los tres» → estrés, turnos y voz; «ese real
  decreto» → RD 486/1997; «las mismas» → tareas.

## Resultado

Pasajes del remate: correctos salvo 2 hallazgos, corregidos. Tema cerrado para esquema.
