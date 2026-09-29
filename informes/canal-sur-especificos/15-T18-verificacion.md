# Grafista (15) · Tema 18 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/18-prevencion-riesgos-laborales.md`. Fecha del
encargo: 24-09-2026; fuentes leídas en la verificación: **29-09-2026**.

Ficheros tocados: el tema y este informe.

## Lo copiado: sólo literalidad

Cotejo línea a línea del tema contra el tema 19 de Realizador/a, el tema 9 del común y
`temas/prl/prl-especifico.md` (RTVE). Todo lo listado bajo «Copiado del común» y «Copiado de RTVE sin
cambios» en `15-T18-redaccion.md` es literal: las únicas líneas que no están en ninguna de las tres
fuentes son la ficha, siglas, índice, rótulos de enlace («Cuándo una tarea es repetitiva», «Las
patologías…», «Artículo 4. Las definiciones…») y los pasajes declarados como adaptados o nuevos. No se
re-verificaron.

## Lo verificado en su fuente (29-09-2026)

- **Ficha 5345100** (X Convenio, BOJA 240/2014, p. 129; texto local l. 5195-5214): función básica,
  cuatro tareas (con «y todo tipo» tal cual) y cláusula de cierre, literales. **Grupo B03**:
  confirmado en el anexo II (Grafista CSTV Sevilla y Málaga, B03).
- **Art. 29.4 del convenio** y apartados 5 y 6: literales; tabla resumen correcta.
- **LPRL** (BOE-A-1995-24292): art. 18.1 («específicos que afecten a su puesto de trabajo o
  función», segundo párrafo del 18.1), 19.1 («se introduzcan nuevas tecnologías o cambios en los
  equipos de trabajo»), 21.2, 29.1 y 29.2 (obligaciones 2.ª, 3.ª y 4.ª): correctos.
- **RD 488/1997** (BOE-A-1997-8671): art. 1.2.d), art. 2, art. 4.3 (correctores especiales, dentro
  del artículo de vigilancia de la salud), art. 5.3, anexo («espacio suficiente delante del
  teclado»; el anexo no nombra el ratón): correctos.
- **RD 773/1997**, art. 2 (definición y exclusiones: no menciona correctores) y art. 4
  (subsidiariedad): la precisión sobre correctores es correcta.
- **Guía Técnica PVD (INSST, 2021)**, l. 1309-1326: cita sobre ratones, joysticks, EN ISO 9241-410:
  2008 e ISO/TS 9241-411: 2012, literal. La Guía no nombra tableta, lápiz ni puestos con varias
  pantallas (grep): lo que el tema dice como «lectura de este tema» está bien declarado.
- **INSST, TME extremidad superior**: la ISO 11228-3 menciona el índice OCRA y describe el Strain
  Index (l. 1272-1275): «Lo que no da» es correcto.
- Tabla de disciplinas, mapa tarea-riesgo, plató, ejemplos de estresores y turnos, portátil y
  salvedad del art. 29.4: son aplicación y están marcados como tal; no afirman norma.
- Normativa y Trazabilidad: coherentes con el cuerpo tras quitar ruido y exteriores (RD 286/2006 y
  disposición adicional única del RD 486/1997 sólo aparecen en «Lo que no da»).

## Correcciones aplicadas

1. Epígrafe 2, «El plató» (error 8, precisión): «la obligación de usar los equipos y dispositivos de
   seguridad (artículo 29.2)» → «utilizar correctamente los medios y equipos de protección y los
   dispositivos de seguridad (artículo 29.2, obligaciones 2.ª y 3.ª)».
2. Tabla resumen, fila de formación (error 9, paráfrasis inexacta del art. 5.3 RD 488/1997): «cada vez
   que el puesto cambie de manera apreciable» → «cada vez que la organización del puesto se modifique
   de manera apreciable».
3. Epígrafe 5, «Los EPI…» (error 9): se quita que la vigilancia de la salud sea «medida colectiva y
   organizativa» (ninguna fuente lo dice); queda «no con EPI», y «la ley» → «la Ley 31/1995».
4. Epígrafe 4: salto de línea roto («es\nin itinere; el\ndesplazamiento») unido.

## Lentes

`negritas.py` y `refutar_exactitud.py` (LPRL, RD 39, 486, 488, 773, LGSS, ET, convenio, Carta, Guía,
INSST, NTP, CNSST, Anuario, BT.2100): los «no está» son rótulos o pasajes copiados de Realizador/a;
ninguno en lo nuevo. `refutar_modo.py`: 3 avisos del ET (arts. 15, 17 y 29 del ET, choque de
numeración con la LPRL), falsos. `refutar_prosa.py`: 0. `indice.py`: 17.112 palabras, 37 epígrafes.

## Sin confirmar (sigue declarado en el tema)

Evaluación de riesgos del puesto, EPI asignados por el Comité de Salud Laboral, norma o NTP sobre
tabletas y varias pantallas: no publicados o no localizados.
