# Realizador/a (puesto 33) · Tema 19 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo; reloj del sistema y fecha de lectura de las
fuentes: 29-09-2026). Tema: `temas/canal-sur-especificos/33-realizador-a/19-prevencion-riesgos-laborales.md`.

## Lo copiado: sólo literalidad

Script de párrafos (normalizando espacios) contra 32/15, 30/16 y 28/16, y `difflib` por palabras en
los párrafos que no son subcadena exacta. Resultado: todo lo listado bajo «Copiado del común» en
`33-T19-redaccion.md` es literal salvo exactamente los cambios que el redactor declara
(productor/a → realizador/a; ejemplos; rótulo y primera frase del bloque del control; tres filas
del resumen). §1 entero: 0 diferencias. «Copiado de RTVE sin cambios»: ninguno declarado. No se
re-verificó el contenido de esos pasajes.

## Lo nuevo o adaptado: verificado en la fuente (29-09-2026)

| Pasaje | Fuente | Resultado |
| --- | --- | --- |
| Ficha 5351000 (objeto, cinco tareas, cláusula final, pág. 196) | X Convenio, BOJA 240/2014, txt l. 6980-7004 | Literal |
| Citas de 21.2, 29.1 y paráfrasis de 29.2.4.º en «Riesgos específicos» | BOE-A-1995-24292 (idénticas a §1) | Correcto |
| «Aglomeraciones y recintos ajenos»: arts. 15, 21, 29.2 y 24 LPRL | BOE-A-1995-24292, art. 24.1-24.2 | Correcto |
| DA segunda RD 286/2006 prevé el Código de conducta; art. 3.1 | BOE-A-2006-4414 | Correcto |
| Fila resumen «Exteriores con aviso naranja o rojo» | RD 486/1997, DA única, ap. 3 (BOE-A-2023-11187) | Correcto |
| Art. 10 RD 773/1997 (a, b, c) en el párrafo de EPI | BOE-A-1997-12735 | Correcto |
| RD 487/1997 = cargas; RD 614/2001 = riesgo eléctrico | Guía técnica MMC 2024; BOE-A-2001-11881 | Correcto |
| Normativa: RD 486/1997 arts. 7, 8, anexos III-IV, DA única; redacciones de la trazabilidad | BOE-A-1997-8669.redacciones.tsv; RD 286/2006 y RD 488/1997 con 1 redacción en todos los bloques | Correcto |
| Remisiones al tema 18 (art. 24, grúa/travelling, presión del directo) | Tema 18 del realizador, l. 241, 306, 780 | Existen |

## Correcciones aplicadas

1. **Error 9.** «En el control de realización y en la sala de edición el realizador/a no necesita
   EPI»: afirmación sin fuente. Pasa a «ninguna fuente leída señala un EPI (el auricular no lo es…)».
2. **Error 9 / 2.** Resumen, fila «Intercom y auriculares»: las medidas (nivel bajo, limitador,
   alternar, no compartir) salen del Código de conducta, no de los arts. 5 a 8 del RD 286/2006.
   Fuente reescrita: «Código de conducta del INSST (los umbrales, RD 286/2006, art. 5)».
3. **Fechas de lectura.** Trazabilidad atribuía al 25-09-2026 «RD 486/1997 en la parte de la luz»
   (30/16 dice Guía Técnica) y omitía RD 286/2006 y Código (25-09-2026 según 28/16). Reescrita, con
   las relecturas de esta fase.
4. Portada: extensión 16.870 → 16.934 palabras (`indice.py`).

Antecedentes de los pasajes cambiados comprobados.

## Lentes

- `refutar_exactitud.py` (LPRL, RD 488, 486, 286, 773): 27 negritas «no literales», todas en pasajes
  copiados o de otra fuente (convenio, Carta, ET, Guía), mal anclados por el guion; ninguna en lo nuevo.
- `negritas.py` (LPRL, convenio, RD 486): la ficha, hallada; los «NO ESTÁ» son rótulos de «Lo que
  este tema no da» (estilo de 32/15).
- `refutar_prosa.py`: 0. `indice.py`: 38 epígrafes.

## Pendiente fuera del tema

Heredado de la redacción: el tema 18 remite al 19 el acoso y el *burnout*, que el 19 no da.

Ficheros tocados: el tema y este informe.
