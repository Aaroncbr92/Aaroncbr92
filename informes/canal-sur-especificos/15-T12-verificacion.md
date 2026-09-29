# Grafista (15) · Tema 12 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/12-archivo-catalogacion-reutilizacion-elementos-graficos-plantillas-proyectos.md`
(12.756 palabras tras la verificación; 37 epígrafes). Fecha del encargo: 24-09-2026; fuentes leídas el
29-09-2026 (fecha de sistema). Copia previa: `15t12-antes-verif.md` en el directorio temporal de la sesión.

Ficheros tocados: el tema y este informe.

## Lo copiado: sólo comprobación de literalidad

Script de cotejo frase a frase contra Montador 08, 13 y 15 y Realizador 04: los 19 pasajes de
«Copiado del común» son literales. Sólo difieren los adaptados que declara el redactor (regla 2 de las
sumas, dos expresiones del OAIS, final del UMID), y se verificaron: los tres rótulos a los que remiten
(«El modelo de referencia: OAIS», «La copia comprobada», el UUID de Graphic Hub) existen y están antes
o después en el tema. «Copiado de RTVE sin cambios»: no hay nada. No se re-verificó el contenido de lo copiado.

## Verificado en la fuente (29-09-2026)

| Dato | Fuente | Resultado |
|---|---|---|
| Ficha 5345100: función básica, tarea «Mantener el archivo de imagen…», cláusula; p. 129 | X Convenio, texto local | Confirmado. La cláusula está en las 114 fichas (114 «CÓDIGO PUESTO» / 114 cláusulas): «como todas las del anexo» es exacto |
| Nivel B03 | X Convenio, art. 45.1 (p. 73) | Confirmado, pero la ficha del anexo III no da el nivel: **corregido** (error 8) |
| Ficha 9420000: denominación, objeto, dos tareas; p. 153 | X Convenio | Confirmado literal |
| Resolve 21: Archive/Restore, pp. 95-96 | Manual PDF (julio de 2026), páginas por pymupdf | Citas confirmadas. **Salvedad omitida** (error 6): al restaurar, la carpeta .dra no se mueve; hay que copiarla antes al volumen de trabajo. Añadida con cita literal en el texto, en la tabla y en el supuesto práctico. «Capítulo 3, "Archiving and Restoring Projects"» → «capítulo 3, apartado…» (el capítulo se titula «Managing Projects and Project Libraries») |
| «que se reabre sin recalcular» (medios optimizados y caché) | El manual no lo dice | Marcado como oficio |
| Power Bins, pp. 390 y 392 | Manual | Confirmado. «cap. 17, "Sharing Media…"» → «cap. 17, apartado…». En la p. 392 se lee «multi-/user» con guion de fin de línea: «multi-user» se deja |
| Macro de Fusion: Macro Editor y «quit and reopen», p. 1483; carpeta Templates/Edit/Titles y Effects Library > Titles, pp. 1483-1484 | Manual | Confirmado |
| Graphic Hub 3.9: 11 citas de «Overview» y «General Database Information» | documentation.vizrt.com/graphic-hub-guide/3.9/ (descarga directa de las páginas HTML) | Todas literales. Queda resuelta la salvedad del investigador: ya no dependen de la herramienta de consulta. Nota: una copia antigua del directorio temporal era de la 3.3 (2019); el tema cita la 3.9, que es la que se ha leído |
| Rótulos del índice de Graphic Hub | toc de la 3.9 | Confirmados los ocho |
| Lectura de rótulos: «se copia a diario en un segundo servidor», «principal y réplica que lo sustituye si falla» | Páginas leídas | **Inexacta** (error 9): la copia es periódica, «once per day or once per week», y el relevo lo hacen servidores *failover* del *cluster*, que ya tiene servidores principal y de réplica. Sustituida por tres citas literales de «Daily Backup…», «Main and Replication Servers with Failover» y «Graphic Hub Archives» |
| EBU Tech 3293 v1.10: «"If you can't find it, you don't have it!"», p. 7 | PDF local | Confirmado |
| Libro de estilo 9.9.1, p. 166, con su salvedad; 9 «Asuntos comprometidos», 9.9 «Material objetable»; 1.ª ed., marzo de 2004 | Texto local | Confirmado |
| Avid 1999, p. 73, «Save these files as a template…» | Montador 15 (literal) | Confirmado |
| Remisiones internas y a temas del puesto (2, 7, 8, 9, 11, 17) | Tema y enunciado | Todas tienen su antecedente o existen en el enunciado |

## Cambios en el tema

1. Nivel B03 atribuido al art. 45.1 (p. 73), no a la ficha.
2. Salvedad de Restore (cita p. 96) en el texto, en la tabla y en el supuesto práctico.
3. Tabla de Resolve: «sin recalcular» pasa a oficio.
4. «Capítulo 3/17, "…"» → «apartado "…"» (dos sitios).
5. Graphic Hub: la lectura de los rótulos pasa a tres citas leídas; se ajustan «Documentos técnicos», «Lo que este tema no da» (sin leer sólo quedan duplicados, metadatos y sustitución de referencias) y el párrafo de oficio de Trazabilidad.
6. Trazabilidad: fechas propias (29-09-2026) para convenio, Libro de estilo y Graphic Hub; fila nueva para EBU Tech 3293.

Pasajes cambiados releídos: cada «ese», «dicha» o «esas páginas» tiene delante su antecedente.

## Lentes

Tema sin norma legal: `refutar_prosa.py` da 0 hallazgos e `indice.py` da 37 epígrafes. Extra: `negritas.py`
contra convenio, Libro de estilo, Resolve 21, páginas de Graphic Hub 3.9, EBU Tech 3293, OAIS y los
temas cerrados copiados da 165 negritas y 6 fuera de fuente: la de «multi-user» (guion de fin de línea)
y 5 rótulos en negrita de «Lo que este tema no da», que siguen la forma de los temas cerrados.

## No confirmado y quitado

Nada más. Lo que no se pudo leer (Adobe *Collect Files*, formato de archivo de Graphic Hub, capacidad
nativa de LTO-10, ST 330) ya estaba declarado en «Lo que este tema no da».
