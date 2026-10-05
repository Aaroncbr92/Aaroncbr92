# Puesto 27 · Tema 19 · Fase 5 bis (revisión de lo rematado)

Fecha de trabajo y de lectura de las fuentes: **05-10-2026** (el encargo fija «hoy» en 24-09-2026;
ninguna redacción usada cambia entre ambas fechas). Alcance: sólo los pasajes que lista
`27-T19-remate.md` (comparados con `git diff` contra el tema verificado).

## Fuentes releídas

| Fuente | Volcado | Qué se comprobó |
|---|---|---|
| RD 286/2006, ruido | BOE-A-2006-4414 (1 redacción, vigente desde 31-03-2006); título en la API del BOE | Arts. 4.1, 4.2, 5.1, 5.2, 7.1 |
| RD 614/2001 | BOE-A-2001-11881 | Art. 3.1; anexos III.A.1, III.C.1.a), IV.A.2 |
| X Convenio RTVA | BOJA 240/2014, ficha 9311200 y art. 30 | M4, «homologadas» |
| NTP 223 (INSST) | `tecnica/insst-ntp-223.txt` | Las 20 citas literales, la advertencia y la serie (6.ª, 1989) |
| Ley 31/1995 | art. 15.1.a) | «Evitar los riesgos» |
| RD 773/1997 | art. 5.3 | Remisión a «cualquier disposición legal o reglamentaria» |
| Reglamento (UE) 2016/425 | DOUE-L-2016-80531 | Arts. 1, 3.18, 8.2, 8.7, 17.1-17.3, 19, 47.2; anexo I; referencias posteriores |
| Reglamento (UE) 2024/2748 y su corrección | DOUE-L-2024-81663, DOUE-L-2025-80611 | Art. 3 (lo que añade al 2016/425), fecha de aplicación |

Todo lo citado en negrita en los pasajes nuevos es literal. Cifras confirmadas: 87/85/80 dB(A),
140/137/135 dB(C); 20,5 % de O2; 25 % y 5 % del LII; una jornada; 50 °C; letras a, b, g, h, m de la
categoría III; módulos A, B+C, B+C2/D; 21-04-2018; 29-05-2026. Antecedentes: cada «(5.2)», «7.1.a»,
«17.2», «en ese apartado» tiene su norma o anexo delante.

## Correcciones aplicadas (4)

1. **Trazabilidad, fila del Reglamento 2016/425 (error 8/1).** DOUE-L-2025-80611 corrige el
   Reglamento 2024/2748, no el 2016/425 («corrección de errores de DOUE-L-2024-81663»). Reescrita:
   «revisados su modificación por el Reglamento (UE) 2024/2748 y la corrección de errores de este
   (…que en el 2016/425 sólo toca el artículo 41 bis añadido)».
2. **Resumen de medidas, fila «Ruido» (error 6, salvedad omitida).** Daba sólo los dB(A) y omitía
   el pico y la condición del 7.1.b («mientras se ejecuta el programa de medidas»). Ahora: valores
   inferiores 80 dB(A) o 135 dB(C); superiores 85 dB(A) o 137 dB(C), con la condición.
3. **Normativa que el tema invoca, RD 286/2006.** Añadido el art. 4, que el texto cita (4.2) y la
   tabla de resumen invoca.
4. **Espacios confinados, prosa.** «Y pide tener en cuenta su fecha de edición:» dejaba los dos
   puntos colgando sobre la lista; ahora «…fecha de edición. Sus medidas:».

Ficha: Extensión 22.850 → 22.879 (`indice.py`). `refutar_prosa.py`: 0 hallazgos.

## Sin cambios, para constancia

- M1-M5 del remate: correctos contra la fuente.
- Rótulos en negrita no literales («Autorización de entrada.», «Marcado CE.», «Tres categorías de
  riesgo», «Qué exige hoy la norma…»): siguen la convención de rótulos ya existente en el tema; no
  se tocan.
- La afirmación de que guantes, casco y calzado aislantes, anticaídas, respiratorios y protectores
  auditivos son de categoría III es lectura del anexo I (riesgos h, g, b, m); se presenta como tal.
- Pregunta 7 del banco: su opción correcta debe ser 20,5 % (aviso del remate, confirmado en la NTP).

## Ficheros tocados

Tema 19 y este informe. Nada más.
