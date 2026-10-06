# 29-T16 · Verificación · Operador/a Informático · Prevención de riesgos laborales aplicada al puesto

Fecha: 06-10-2026 (fuentes releídas ese día). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/16-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.
No se ha tocado ningún otro fichero del repositorio (salvo este informe).

## Lo copiado: sólo comprobación de literalidad

- Epígrafe 1 entero: `diff` contra el 32-15 (Productor/a), **idéntico**.
- Resto: cotejo por párrafo y por línea contra 32-15 y 27-19 (script en el scratchpad). Todo párrafo
  que no aparece literal en una de las dos fuentes coincide con lo que el informe de redacción declara
  como adaptado o nuevo; los cambios en lo copiado son sólo los declarados («productor/a» →
  «operador/a informático», ejemplos nuevos, frases suprimidas). Ningún cambio no declarado.
- Copiado de RTVE sin cambios: ninguno (declarado así).

## Verificado en su fuente (todo lo nuevo o adaptado)

| Pasaje | Fuente releída | Resultado |
| --- | --- | --- |
| Ficha 1324100: función básica, cinco tareas, cláusula de cierre | X Convenio, BOJA 240, pág. 189 (txt l. 6786-6808) | Literal |
| Art. 45, nivel B04 | txt l. 1520-1542 | Correcto |
| Anexo II: 9 puestos, RTVA, Sevilla | txt l. 2717-2726 (columnas «ESTRUC. IX CC / X CC») y l. 2946-2951 | Correcto (9 en ambas) |
| «otras fichas» con tareas preventivas | Anexo III (ficha de productor: «Ayudar al productor en el cumplimiento de la legislación de prevención») | Correcto |
| Art. 50.11, guardia localizable (cita y 1 % / 2,5 %) | txt l. 1737-1745 | Literal |
| Jefe de centro de proceso de datos | Anexo III, ficha 1320000, pág. 165 | Existe; corregido el alcance (ver abajo) |
| RD 614/2001, art. 4.3.a), anexo I.5, art. 5 | BOE-A-2001-11881 (1 redacción) | Literal |
| RD 842/2002, art. 2.1 y 2.6; redacción 2021 sólo cambia el apartado 2 | `boe.py precepto BOE-A-2002-18099 a2` | Literal; salvedad del 2.6 completa |
| RD 487/1997, anexo (factores), art. 3 | BOE-A-1997-8670 | Literal tras corrección |
| RD 488/1997, art. 2 (trabajador), anexo sin «ratón» | BOE-A-1997-8671 | Correcto |
| Guía PVD: portátiles; ratón; EN ISO 9241-410:2008; ISO/TS 9241-411:2012; «ñ» y RD 564/1993 | guia-tecnica-pvd.txt l. 324-334 y 1298-1325 | Literal |
| RD 773/1997: art. 2.2.a), 3.c) (gratuidad), 4, 10; anexo III, casco y calzado con punteras en «Manipulación de cargas…» | BOE-A-1997-12735 (anexo III en redacción BOE-A-2021-20261) | Literal |
| Trazabilidad: identificadores y redacciones de los RD 614, 842, 487, 773 | `.redacciones.tsv` y `boe.py` | Correctos |
| Guía MMC, septiembre de 2024 | guia-tecnica-mmc-2024.txt l. 14 y 42 | Correcto |

## Correcciones aplicadas

1. **Error 1 (cita cruzada)**, tabla de las cuatro disciplinas: «incendios y evacuación» remitían a
   «El riesgo eléctrico» y «La manipulación de cargas», donde no se tratan. Ahora remiten al
   epígrafe 1 (art. 20 de la Ley 31/1995), y cada riesgo lleva su propio apartado.
2. **Error 1/9**, tablas del epígrafe 2: «golpes y cortes» y «caídas al mismo nivel» remitían a
   apartados que no los desarrollan. Se dice que sólo se enuncian, y se añade a «Lo que este tema no
   da». En la fila de cargas, «Lesiones dorsolumbares; golpes y cortes» → «Lesiones, en particular
   dorsolumbares» (art. 1 del RD 487/1997).
3. **Error 9 (afirmación sin fuente)**, «Lo que esto significa para el puesto»: «Cualquier otro
   trabajo en la instalación… corresponde a trabajadores autorizados o cualificados» no lo dice el RD
   614/2001 (los trabajos sin tensión no exigen trabajador autorizado; sí la supresión y reposición de
   la tensión). Sustituido por las reservas literales: anexos II.A, III.A.1, IV.A.1 y V.B.1.
4. **Error 9**, cargas: «obligan a manipular en niveles diferentes» atribuía a los armarios un factor
   del anexo que se refiere a desniveles del suelo. Sustituido por el factor que sí encaja: **espacio
   libre, especialmente vertical**, insuficiente. «voluminoso» en negrita → «una carga
   **voluminosa…**» (literal).
5. Antecedente roto: «Ninguno de los dos tiene…» tras un rótulo con tres elementos → «Ni el estrés ni
   el trabajo a turnos tienen…».
6. Negrita no literal: «Al **ratón** … **no lo menciona**» → en redonda.
7. «el convenio nombra el puesto de jefe de CPD, lo que prueba que la unidad existe» → «el convenio
   (2014) define el puesto… (código 1320000)»: un convenio de 2014 no prueba que exista hoy.
8. Error 5 (sigla): ISO y EN presentadas antes de la norma EN ISO 9241-410:2008.
9. Extensión de la portada: 17.030 → **17.131** palabras (`indice.py`).

Pasajes cambiados releídos: cada «ese artículo», «el anexo» o «lo demás» tiene su antecedente.

## Lentes

- `negritas.py` (todas las fuentes de `fuentes/canal-sur/`, `fuentes/prl-especifico/`, convenio): sin
  hallazgos en lo nuevo, tras la corrección 6. Lo que marca son rótulos en negrita, LGSS (no hay
  volcado) y NTP: pasajes copiados del 32-15.
- `refutar_exactitud.py` y `refutar_modo.py` (RD 614, 487, 773, 488, 842): sus hallazgos caen en el
  epígrafe 1 o en el RD 773 copiados, y en su mayoría cruzan artículos de la Ley 31/1995 con los de
  un real decreto del mismo número. Ninguno en lo nuevo.
- `refutar_prosa.py`: un hallazgo (ISO sin presentar), corregido. `indice.py`: 38 epígrafes.

## No confirmado y no cambiado

- «Las baterías pesan mucho para su tamaño» y «los equipos que une se alimentan de la red de baja
  tensión» son lecturas de oficio, ya presentadas como aplicación del tema; se dejan.
- No se ha comprobado si hay convenio posterior al X: el tema sigue al común.
