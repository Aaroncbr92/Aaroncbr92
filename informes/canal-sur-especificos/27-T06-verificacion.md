# Verificación · Oficial Técnico Electricista (27) · Tema 6 · Alumbrado interior, exterior y de emergencia

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/06-alumbrado-interior-exterior-y-de-emergencia.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguna fuente usada cambia entre las dos fechas).

Ficheros tocados: el tema y este informe. Copia previa del tema y textos de las fuentes en el
scratchpad (`27t06v/`).

## Exenciones

El informe de redacción declara **«Copiado del común»: ninguno** y **«Copiado de RTVE sin cambios»:
ninguno** (todo lo de RTVE está adaptado y cita norma). No había nada que comprobar sólo con diff:
se ha verificado el tema entero.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099): ITC-BT-09, 28 y 44 (redacción única, vig. 18-09-2003); art. 20 (`a2-2`, vig. 23-05-2010, BOE-A-2010-8190); ITC-BT-05 (vig. 30-06-2015, BOE-A-2014-13681) | `boe.py precepto`, texto entero de cada ITC | Todas las cifras de las tablas de 1.5, 2.1, 2.2, 2.3, 4.1-4.5 cotejadas con su apartado |
| RD 1890/2008 (BOE-A-2008-18634): arts. 1, 2, 4, 5, 12; ITC-EA-02, 04, 05, 06 | `boe.py precepto` | Redacción única salvo ITC-EA-02: `diff` con `--fecha 20220101` confirma que la 2.ª redacción sólo añade la nota del RDL 14/2022 (en el apartado 6) |
| RD 486/1997 (BOE-A-1997-8669): art. 8 y anexo IV | `boe.py precepto` | Redacción única; tabla y nota (*) literales |
| RD 314/2006 (BOE-A-2006-5515): art. 2 (vig. 28-06-2013) y disposición derogatoria única, 1.g | `boe.py precepto` | Confirmada la derogación de la NBE-CPI-96 |
| RD 513/2017 (BOE-A-2017-6606): anexo I s. 1.ª ap. 15, anexo II ap. 8, art. 22 (vig. 10-05-2025) | `boe.py precepto` y `--fecha 20250101` | Ap. 15 y ap. 8 idénticos en la redacción anterior. **Art. 22.2 sí cambió**: la exención del alumbrado de emergencia no existía antes de 2025 |
| CTE, DB SUA consolidado «14 junio 2022» y DB HE «14 Junio 2022» (PDF del Ministerio, pasados a texto en fase 2) | lectura de SUA 4 entero, HE 3 entero y anejo A | Todo literal; HE 3 cita el RD 450/2022 |
| Datos de publicación de los cinco RD | API XML del BOE | Números y fechas del BOE de «Normativa» correctos |

Lentes: `negritas.py` (319 cotejadas; 3 «no están»: dos rótulos y «e «Inspección inicial»», que es
un fragmento con letra del tema: el literal está en ITC-EA-05, 2.1.b); `refutar_exactitud.py` (32 «no
literales»: falsos positivos, casa los apartados de las ITC y del DB con artículos de los RD; todas
comprobadas a mano en su apartado); `refutar_modo.py` (0); `refutar_prosa.py` (0); `indice.py` (12.055
palabras, 31 epígrafes).

## Hallazgos y correcciones

1. **Error 7/3** · Ficha, «Redacción que se estudia»: decía que nada cambió desde 2015 salvo el anexo
   II del RIPCI; la ITC-EA-02 cambió en 2022 y el art. 22.2 del RIPCI en 2025 (con efecto en el tema).
   Reescrita; añadido a «Normativa» que la exención del art. 22.2 es de la redacción de 2025.
2. **Error 9** · 1.2: «la tabla del apartado 3, la única de cifras de la norma»: el RD 486/1997 tiene
   más cifras (otros anexos). → «la única tabla de cifras del anexo IV».
3. **Error 6 y 9** · 1.3: el anexo IV.5 exige alumbrado de emergencia sólo donde un fallo del normal
   suponga riesgo, y la ITC-BT-28 (3.3.1, último párrafo) sí alcanza fuera de la pública concurrencia
   (escaleras de incendios, riesgo especial). Añadidas la condición y la salvedad.
4. **Error 6** · 1.5: la ITC-BT-09, 3, pide niveles decrecientes **«siempre que sea posible»** y para
   el alumbrado público. Añadido.
5. **Error 6** · 2.2: ITC-EA-04, 3.1.3, **«siempre que resulte factible»**. Añadido.
6. **Error 9** · 3.3: «Ese "o luminarias" es propio de este reglamento» (comparación no comprobada) →
   «importa». El perímetro como alumbrado de vigilancia, marcado como lectura del caso.
7. **Error 9** · 4.1: «sólo obliga al reemplazamiento en hospitales»: 3.3.2 nombra salas de
   intervención, tratamiento intensivo, curas, paritorios y urgencias. Precisado.
8. **Error 9** · 4.4: «El DB SUA calcula la ocupación con las densidades del DB SI»: el SUA 4 no lo
   dice. Reescrito con lo que sí consta (SUA 5 remite al DB SI, sección SI 3, cap. 2).
9. **Error 9** · 5.1: «[las causas de la ITC-EA-06] valen también para el interior»: la ITC es de
   exterior. Marcado como lectura de oficio y añadido a la lista de oficio de «Trazabilidad».
10. **Error 3** · 5.1, ejemplo: 0,90 × 0,95 × 0,85 = 0,727; Ei = 27,5 lux (decía 27,4 por redondeo
    previo). Corregido.
11. **Error 6** · 5.4, regla 1: la «modificación de importancia» (art. 2.3.c) es de instalaciones
    anteriores al reglamento y sólo dentro del umbral de 1 kW (art. 2.1). Añadido; quitado «entero».
12. **Error 9** · «Lo que no da»: «UNE-EN 12464-1» y «la serie UNE-EN 50172 es la que suele citarse»
    se nombraban sin fuente leída. Quitados los nombres.
13. Menores: 4.5 «se pueden compartir» → «pueden servir también como fuentes de reemplazamiento»
    (lo que dice 2.1); 1.4, rótulo del DB («zonas de los establecimientos de uso pública
    concurrencia»); **error 5**: presentadas V, kV, A, Hz y cd/klm, quitada «lx», que no se usa;
    extensión de la ficha 11.800 → 12.000.

Sin hallazgo, comprobado: todas las cifras de ITC-BT-09 (3, 4, 5.1-5.2.3, 6.1, 6.2, 7.1, 7.2, 8, 9,
10), ITC-BT-44 (1-4), ITC-BT-28 (1-5), ITC-BT-05 (4.1, 4.2), arts. 1, 2, 4, 5, 12 y ITC-EA-02/04/05/06,
SUA 4 (1 y 2), HE 3 (1-5) y anejo A; los cálculos de 2.1 (2.088 VA; 9,1 A), 3.2 (VEEI 1,44; 7,2
W/m²), 4.2, 4.4 (200 personas) y 4.5 (3 líneas).

Pasajes cambiados releídos: cada «esa regla», «la ITC», «ese "o luminarias"» tiene su antecedente.
