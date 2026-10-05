# Verificación · Oficial Técnico Electricista (27) · Tema 7 · Grupos electrógenos, SAI y continuidad de servicio

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/07-grupos-electrogenos-sai-y-continuidad-de-servicio.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguna fuente usada cambia entre las dos fechas).

Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad (`t07-antes.md`).

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| ITC-BT-40 (BOE-A-2002-18099, `ib-40`, redacción RD 244/2019, vigente desde 07-04-2019) | `boe.py precepto`, apdos. 1, 2, 3, 4.1, 4.2, 5, 6, 7, 8.2.1, 8.2.2, 9 | Todas las negritas, literales y en su apartado. Apdo. 7 sin restricción a interconectadas: el tema no le da más alcance. «ordenn» confirmado en el BOE |
| ITC-BT-28 (`ib-28`, redacción única) | `boe.py precepto`, apdos. 2, 2.1, 2.2, 2.3, 3, 3.1.1-3.1.3, 4.g | Todo literal y bien atribuido |
| REBT, art. 10 (redacción única) | volcado, `grep -n` | Literal; 10.3 bien |
| ITC-BT-38, apdo. 2.2 | `boe.py precepto ib-38` | Leída para corregir el hallazgo 5 |
| RIPCI, anexo II apdo. 1 y tabla I (bloque `s1-3`, vigente desde 10-05-2025, BOE-A-2025-7190) | API de datos abiertos del BOE (XML con la tabla y sus celdas) | **Confirmada la columna «Tres meses»** para «Fuentes de alimentación» y para las tres operaciones de «Requisitos generales» citadas; la columna «Seis meses» está vacía en esas filas |
| Sölter, «A new International UPS Classification by IEC 62040-3» (PDF de scispace) | descargado y pasado por `documento.py texto` | Las cinco citas en inglés, literales; «Member of the IEC SC 22H», «First Edition 1999-03» confirmados |

Lentes: `negritas.py` (105 cotejadas; las 8 «no están» son rótulos y citas de Sölter, cotejadas
aparte), `refutar_exactitud.py` (12 «no literales»: son falsos positivos, porque la lente casa los
apartados de las ITC con los artículos del REBT; todas comprobadas a mano en su ITC),
`refutar_modo.py` (0), `refutar_prosa.py` (0), `indice.py` (11.644 palabras, 43 epígrafes).

## Copiado de RTVE sin cambios

Comprobado sólo que es literal: guion que normaliza (sin negritas, sin mayúsculas, sin puntuación)
y busca cada frase y cada celda de los pasajes listados en `teitse/11` + `teitse/12`. Todos los
pasajes listados están en RTVE. Lo que no casa queda fuera de la lista (y se ha verificado): la
frase de los coeficientes (1.2), el umbral de la fase 1 (1.5), el cierre «La selectividad … tema 3»
(2.4), la entrada de 5.3 y la última frase de 7.2. Fuera de la lista y adaptados de RTVE, también
verificados como oficio: tabla de partes de 1.1 (añade «máquina síncrona») y párrafos de 7.1 tras
la tabla.

## Hallazgos y correcciones

1. **Error 9** · 6.3 «El REBT sólo fija una autonomía»: falso; la ITC-BT-38, apdo. 2.2, fija
   **«una autonomía no inferior a 2 horas»** para el suministro especial complementario de
   quirófano. Corregido («de las ITC leídas… sólo la ITC-BT-28…», con la salvedad de la ITC-BT-38);
   añadida a «Normativa» y «Trazabilidad».
2. **Error 9** · 6.2: «a partir de cierto tamaño… instalación petrolífera…: la ITC-BT-40 lo dice»;
   la ITC sólo remite a los reglamentos específicos, sin umbral. Reescrito.
3. **Error 6** · 1.5: el umbral del 70 % de la ITC-BT-28 se daba para todo grupo de servicios de
   seguridad; la ITC es de locales de pública concurrencia. Añadida la salvedad.
4. **Error 6** · 4.3: el apdo. 9 de la ITC-BT-40 vale para asistidas **o interconectadas**. Añadido.
5. **Error 6** · 7.3: la tabla I del RIPCI la puede hacer el fabricante, la mantenedora **o** el
   personal del titular; el tema sólo nombraba a éste. Completado.
6. **Error 9** · 2 (entrada): «el SAI es el único que cumple “sin corte”» contradecía 2.2 (sólo la
   doble conversión). Corregido; remisión aclarada como «epígrafes 3.1 y 2.2».
7. **Error 9** · 2.3: «la edición vigente de la norma es posterior» no consta en ninguna fuente
   leída. Reescrito como hueco.
8. **Error 9** · «las cifras que más se preguntan», «la consecuencia que más se pregunta», «se
   preguntan juntas», «la que más se pregunta en la práctica», «el razonamiento que un tribunal
   espera»: no hay exámenes anteriores. Quitado.
9. **Error 5** · kWh usado (6.1) sin presentar: añadido. Quitadas de las siglas las que el tema no
   usa (r.p.m., VRLA, Li-ion, CC, CA, ms).
10. Cita entre comillas no literal en 3.3 («medio de producción propio» → «medios de producción
    propios»). Ficha: «ITC-BT-28 (apartado 2 y 3.1)» → «(apartados 2, 3 y 4)», que es lo que el tema
    cita.

Releídos los pasajes cambiados: cada remisión («esa ITC», «1.3», «epígrafes 3.1 y 2.2») tiene su
antecedente. Sin cambios en el índice.

## Lo que queda para refutación

- Todo el oficio (secuencia, topologías, maniobra del bypass, incidencias) sigue sin fuente técnica
  publicada y así se declara; no se ha encontrado nada falso.
- La tabla 3.1 de categorías por fuente es oficio declarado; coherente con Sölter (VFD conmuta en
  4-8 ms, que el tema no da como cifra de norma).
