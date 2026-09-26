# 32 · T15 · Verificación (fase 3)

Fecha: 24-09-2026 (fecha del encargo; reloj del sistema: 25-09-2026, que es la fecha real de las
lecturas). Tema: `temas/canal-sur-especificos/32-productor-a/15-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.

## Literalidad de lo copiado (sin re-verificar)

- `diff` contra 34/20 (`34-redactor-a/20-prevencion-riesgos-laborales.md`): todas las diferencias
  caen en los pasajes que el informe de redacción declara nuevos o adaptados; el resto es literal
  (§1 entero, §2 riesgos generales salvo tabla, organización preventiva salvo «tocan al
  productor/a», estrés y turnos salvo las tres frases declaradas, §3 y §4 salvo los ejemplos,
  §5 RD 773/1997, resumen salvo la fila nueva).
- `grep` contra 28/16: el párrafo de los anexos I y III del RD 773/1997 y las filas «Falta de
  visibilidad» y «Frío» son literales (sólo cambia la columna de aplicación, que es nueva).
- «Copiado de RTVE sin cambios»: ninguno declarado; nada que comprobar.

## Verificado en fuente (pasajes nuevos)

| Dato | Fuente | Resultado |
| --- | --- | --- |
| Puesto 2.32, grupo B03, enunciado punto 15 | Enunciado del puesto (BOJA 186/2026) | Correcto |
| Ficha 5331000: objeto, 8 tareas, cláusula final | X Convenio, anexo III, pág. 194 (txt l. 6916-6947) | Literal |
| «cierra como todas las fichas» | Convenio: 114 fichas, 114 cláusulas | Correcto |
| Evaluación por comisiones técnicas; Servicio de Prevención de nivel superior | X Convenio art. 28.2 y 28.3 | Correcto |
| Plus de nocturnidad en el convenio | X Convenio (txt l. 1656-1662) | Existe; bien remitido |
| LPRL 21.2, 29.1 («aquellas otras personas…»), 29.2.4.º | BOE-A-1995-24292 vigente | Literal (ver corrección 1) |
| ET 36.1 define trabajo nocturno; antecedente «mismo Estatuto» (36.4) | BOE-A-2015-11430 | Correcto |
| RD 488/1997 art. 1.2.d (portátiles) y art. 2.c (trabajador) | BOE-A-1997-8671 | Correcto |
| LGSS 156.4.a (insolación, rayo) | BOE-A-2015-11724 vigente (precepto) | Correcto |
| RD 773/1997 art. 10 y anexos I y III (encabezado, nota, filas citadas) | BOE-A-1997-12735 | Correcto |
| LPRL art. 24 y RD 171/2004 = coordinación de actividades empresariales | BOE-A-1995-24292; BOE-A-2004-1848 | Correcto |
| Remisiones a tema 14 (producciones, coordinación, emergencias) y tema 5 (jornada, turnos) | Enunciado del puesto | Correcto |

## Correcciones aplicadas

1. §2 «Los riesgos específicos del productor/a»: «el camino de cualquier incidencia» ampliaba el
   supuesto del 29.2.4.º (error 6, salvedad omitida). Ahora: «ante cualquier situación que, a su
   juicio, entrañe por motivos razonables un riesgo para la seguridad y la salud de los trabajadores».
2. §5 «Los EPI en la RTVA…»: frase rota («y el plan de trabajo, que el productor/a hace la
   previsión de medios»). Ahora cita la tarea literal de la ficha: **«Realizar la previsión de medios
   humanos y materiales»**; «esa tarea» → «esas tareas» (antecedente doble).
3. Portada: extensión 13.802 → 13.817 palabras (`indice.py` tras las correcciones).

Nada quitado: todo dato nuevo se confirmó.

## Lentes

- `negritas.py` (LPRL, RD 488, 486, 773, ET, convenio, Carta): ninguna negrita de pasaje nuevo
  falta en fuente; los «NO ESTÁ» son rótulos, LGSS/RD 39/NTP no pasados y texto copiado.
- `refutar_exactitud.py`: 27 no literales, todos convenio (no es fuente BOE), rótulos o copiado;
  «(art. 10)» en las dos citas de la ficha es falso positivo (la frase dice «la ficha del puesto»).
- `refutar_modo.py`: 5 avisos, falsos positivos por numeración compartida LPRL/RD 39/1997.
- `refutar_prosa.py`: 0. `indice.py` (copia en scratchpad): 13.817 palabras, 35 epígrafes, índice
  coincide.

## Fuentes leídas en esta fase (25-09-2026 por reloj del sistema)

X Convenio RTVA (arts. 28, plus de nocturnidad, ficha 5331000); LPRL arts. 21, 24, 29; ET art. 36;
RD 488/1997 arts. 1-2; RD 773/1997 art. 10, anexos I y III; LGSS art. 156; RD 171/2004 (preámbulo).

## Avisos

- La Trazabilidad del tema declara 24-09-2026 para todo salvo la ficha (25-09-2026); se deja así.
- Otros ficheros tocados: sólo el tema y este informe (volcado de RD 39/1997 en scratchpad).
