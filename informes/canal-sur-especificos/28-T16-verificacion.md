# Verificación · Operador/a de Sonido (28) · tema 16 · Prevención de riesgos laborales

Fecha: 25-09-2026. Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/16-prevencion-riesgos-laborales.md`
(22.122 palabras tras la verificación, 40 epígrafes; índice regenerado con `indice.py`, sin cambios).

## 1. Lo copiado: sólo comprobación de literalidad (diff contra Cámara 17)

Comprobado con `diff` contra `08-camara-operador/17-prevencion-riesgos-laborales.md`:

| Pasaje (l. del tema) | Resultado |
|---|---|
| Epígrafe 1 entero (117-424) | Idéntico |
| Disciplinas, párrafo de entrada (427-433) | Idéntico; la tabla es nueva (verificada abajo) |
| Organización preventiva (445-495) | Idéntico salvo «operador de sonido» (l. 475) |
| Riesgo eléctrico (844-893) | Idéntico salvo las 5 frases de aplicación declaradas |
| Estrés y turnos (1011-1067) | Idéntico salvo l. 1020, 1024, 1051-1053, 1064-1065 (declaradas) |
| Epígrafe 3 (1068-1364) | Idéntico salvo entrada (1070-1077) y las cuatro frases declaradas |
| Epígrafe 4 (1397-1545) | Idéntico salvo 1447, 1493-1499 y 1543 (declaradas) |
| RD 773/1997 y art. 30 del convenio (1548-1634) | Idéntico salvo el nombre del puesto |

Discrepancia con el informe de redacción: dice que el párrafo de entrada de los EPI (l. 1636-1640) viene de Cámara 17; **no es así** (Cámara pone ahí el Libro de estilo). Por eso lo he verificado: anexos I y III del RD 773/1997, correcto.
Frases adaptadas: son sólo de aplicación y están marcadas como tales. Copiado de RTVE sin cambios: ninguno, así que no hubo nada que saltar.

## 2. Lo nuevo, verificado en su fuente (leída el 25-09-2026)

- **X Convenio, anexo III** (BOJA 240/2014, págs. 187-188): códigos 6211100 y 5212207, objeto, tareas y cláusula final de las dos definiciones: literales. Arts. 28, 29.4, 29.6 y 30: correctos.
- **RD 286/2006** (`boe.py`, una redacción desde 31-03-2006): arts. 1-12, DA 2.ª, DT única, anexos I-III. Valores del art. 5.1, salvedad del 5.2, 5.3, periodicidades de 6.4 y 11.2, 7.1-7.3, 8, 9, 10, 11.4 y 12: correctos.
- **RD 1299/2006**, anexo 1 (codificación de BOE-A-2018-6046): 2A01, 2A0109, 2A0113, 2D0101 y 2E0101, erratas incluidas: literales.
- **Protocolo de Sanidad (2022)**, 2.1.1 y 2.1.6: literales.
- **INSST, Código de conducta (2011)**: todas las citas están. **Guía técnica del ruido (2022)**: tipos de protector, 82 dB(A), tablas 16 y 17, ejemplo de 93 → 83 dB(A), Reglamento (UE) 2016/425 y uso personal: literales.
- **RD 487/1997** (arts. 2, 3 y anexo), **Guía MMC 2024** (3 kg, tablas 1 y 2, 25 cm, dos tercios), **RD 486/1997** (anexo I.A 3.1.º en la redacción de 2004, anexo II.1, DA única, art. 1.2), **RD 1215/1997** (anexo I 1.6, anexo II 4.1.6 y 4.2.3) y **RD 171/2004** (arts. 4, 7 y 9): correctos.
- **LPRL** 21.2 y 29.2.1.º: literales.

## 3. Correcciones aplicadas (10)

1. l. 590, LAeq,d: «promediado sobre la jornada» no está en el anexo I. Ahora: «de la exposición de la jornada, calculado con el tiempo de exposición en horas/día» (error 9).
2. l. 749-750: «Es la única actividad» tenía dos posibles antecedentes. Ahora: «El 2A0113 es la única…» (error 1).
3. l. 763: el que habla de estudios y de «emisión de música» es el **apéndice 4** del Código, no el Código entero (error 8/9).
4. l. 787-789: «no se deben confundir… con los protectores auditivos» se refiere en la fuente a los protectores «no pasivos» con restauración electrónica del sonido. Añadida esa salvedad y quitado «en general» (error 6).
5. l. 804: la fuente dice «**Muchos** trabajadores…, **como los intérpretes y técnicos de sonido**». Se había generalizado (error 9).
6. l. 812, fila «Pasivos»: mezclaba la clasificación por diseño con la del modo de funcionamiento. Rehecha con la definición de la Guía (error 9).
7. l. 962: DA única del RD 486/1997. Faltaba «y en los lugares de trabajo que… no puedan quedar cerrados» (error 6).
8. l. 974-976: «incluidos los del artículo 1.2» listaba sólo transporte y obras. Ahora da los cinco supuestos del art. 1.2 (error 3/6).
9. l. 991-993: RD 171/2004, art. 4.2. Faltaban los otros dos momentos de la información: cambio relevante y emergencia (error 6).
10. l. 1693, resumen: «informar de pérdida de audición o acúfenos» se atribuía al RD 286/2006. Viene del Código; el art. 9.f dice «detectar e informar sobre indicios de lesión auditiva» (error 9).
Además: en la ficha, extensión 21.987 → 22.122 (medida con `indice.py`).

## 4. Lentes

- `negritas.py` contra 15 fuentes (793 negritas): las «no están» son rótulos, citas de temas cerrados cuya fuente no se pasó (NTP, LGSS, Guía PVD, tema 69) o frases de las guías INSST partidas por guiones blandos. Las nuevas las cotejé a mano. Las «mal atribuidas» son falsos positivos: tablas o un artículo de otra norma citado cerca.
- `refutar_exactitud.py`: todos los «no literales» son rótulos del epígrafe 1 (copiado), negritas de anexos que la lente ancla a un artículo, o números de artículo del convenio confundidos con los de la LPRL. Ninguno es un error real.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos. `indice.py`: 40 epígrafes, índice sin cambios.

## Ficheros tocados

- Modificado: el tema 16 (10 pasajes y la ficha).
- Creado: este informe.
- Volcados BOE (RD 487/1997, 171/2004, 1215/1997, 1299/2006) y copia previa del tema, sólo en el scratchpad.
