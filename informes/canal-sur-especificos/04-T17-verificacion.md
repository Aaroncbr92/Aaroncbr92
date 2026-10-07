# 04 · Ayudante de Producción · Tema 17 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/17-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.
Fuentes leídas el 06-10-2026 (fecha del sistema; el encargo fija «hoy» en 24-09-2026; todas las
normas releídas tienen una sola redacción o una redacción vigente anterior a esa fecha, así que
la diferencia no cambia nada). Ficheros tocados: el tema y este informe.

## 1. Pasajes copiados: sólo comprobación de literalidad

- **De Productor/a T15**: `git diff --no-index --word-diff` entre los dos temas. Todo lo que el
  informe de redacción lista como «Copiado del común» sale igual, letra por letra. Las únicas
  diferencias son las que el redactor declara como adaptadas o nuevas. No hay cambios sin declarar.
- **De Productor/a T14** («Estudios y platós», «Exteriores y localizaciones», «Climatología»,
  «Manipulación de cargas»): cotejo frase a frase con un script. Las frases que no aparecen en T14
  son justo las que el informe declara adaptadas: la remisión al art. 20 LPRL, «epígrafe 3», el
  párrafo de oficio, el art. 4 y el art. 6 del RD 487/1997, la entrada y el cierre de cargas, el
  156.4 resumido y la aplicación al ayudante. Lo demás es literal.
- **Copiado de RTVE sin cambios**: no hay nada (el redactor tampoco lista nada).

## 2. Lo verificado en la fuente

| Pasaje | Fuente | Resultado |
|---|---|---|
| Ficha 5212705 (objeto, 10 tareas, cláusula final) | X Convenio, BOJA 240, p. 110 (`x-convenio…txt`, l. 4685-4719) | Literal. La página es correcta |
| Ficha 5331000: «Velar por…» y «Coordinar el equipo…» | Mismo BOJA, p. 194 (l. 6916-6945) | Literal. La página es correcta |
| Art. 28 del convenio (evaluación de riesgos) | Convenio, l. 721 | Correcto |
| RD 487/1997, arts. 4 y 6; «1 redacción (1997)» | BOE-A-1997-8670 y su `.redacciones.tsv` | Literal. Hay una sola redacción, vigente desde 13-05-1997 |
| RD 486/1997, anexo I.12 (2.º y 3.º); anexo I vigente desde 03-12-2004; DA única vigente desde 13-05-2023 | BOE-A-1997-8669 y su `.redacciones.tsv` | Correcto |
| LGSS, art. 156.4.a), salvedad de la insolación | `boe.py precepto BOE-A-2015-11724 a156` (vigente; vig. 02-01-2016) | Literal. La remisión «(epígrafe 4)» tiene su antecedente en el tema, en la l. 1130 |
| RD 773/1997, anexo III: «I. Riesgos físicos / Pies / Calzado con punteras / Manipulación de cargas»; «Falta de visibilidad» en «IV. Otros riesgos» | BOE-A-1997-12735, l. 274, 408-413 y 982-989 | Correcto. Las «tres filas» que anuncia el texto son tres en la tabla |
| «El art. 24 está en el tema 9 del común» | `temas/canal-sur-comun/09-ley-31-1995.md`, l. 954 | Correcto |
| Art. 20 LPRL (emergencia y evacuación) y art. 29.2.4.º | LPRL | Correcto |
| «Cinco rúbricas» en «De dónde sale» | Enunciado | Correcto: son 5 |
| Siglas nuevas MMC y AEMET | Lista de siglas | Se presentan antes de usarse |

## 3. Correcciones aplicadas

1. **Tabla de las cuatro disciplinas** (epígrafe 2). La manipulación manual de cargas estaba en
   «Seguridad en el trabajo». La he pasado a «Ergonomía y psicosociología aplicada». El tema la
   define por su riesgo **dorsolumbar** (art. 2 del RD 487/1997) y pone los TME en ergonomía. El
   portal TME del INSST (`fuentes/prl-especifico/portal-tme.txt`, l. 322) cuenta la manipulación
   manual de cargas entre los factores de los TME, y la Guía de 2024 la trata como riesgo
   ergonómico. Los «golpes» se quedan en seguridad. Tipo de error: 9 (clasificación sin apoyo e
   incoherente con el resto del tema).
2. **Epígrafe 4**, cierre del 156.5. Decía «Para quien **organiza** grabaciones y retransmisiones
   al aire libre». La frase venía de Productor/a. El ayudante no organiza: asiste («bajo la
   supervisión del productor»). Ahora dice «Para quien **trabaja en** grabaciones…». El pasaje es
   copiado, pero el error está en la adaptación al puesto, no en la norma.
3. **Manipulación de cargas**, último párrafo. Decía «El anexo del real decreto pone el foco en lo
   que el ayudante encuentra fuera del centro», y el anexo no dice tal cosa (error 9). Ahora es:
   «Entre los factores del anexo, fuera del centro el ayudante puede encontrar (es aplicación de
   este tema) el suelo irregular o resbaladizo, los desniveles…, el ritmo impuesto… y la
   temperatura inadecuada». Son los términos del anexo: «resbaladizo» y «temperatura… inadecuadas»
   en lugar de «mojado» y «calor».
4. **Portada**: la extensión pasa de 17.199 a 17.210 palabras (medida con `indice.py`).

He releído los tres pasajes cambiados. Cada remisión («en este epígrafe», «del anexo») tiene su
antecedente.

## 4. Lentes (el tema cita normas)

- `negritas.py`: 618 negritas cotejadas. Las que no aparecen son de documentos técnicos que no se
  pasaron a la herramienta (NTP, Guías del INSST, Anuario) o son rótulos y fechas. Las 4 «atribuidas
  a otro artículo» son falsos positivos: «e) asegurar que el mantenimiento» está bien en el art. 3
  del RD 773/1997, y las demás están en pasajes copiados de temas ya verificados.
- `refutar_exactitud.py`: los «no literales» son citas de NTP o del convenio con un salto de línea,
  o rótulos. Ninguno está en lo adaptado.
- `refutar_modo.py`: 4 hallazgos, todos falsos. Son artículos de la LGSS que se numeran igual que
  los de la LPRL (la propia herramienta avisa de ello).
- `refutar_prosa.py`: 0. `indice.py`: 38 epígrafes. El índice está bien.

## 5. Lo que no se pudo confirmar (sigue declarado en el tema)

- La evaluación de riesgos del puesto 5212705 y los EPI que se le asignan: no están publicados.
- La columna «riesgo concreto» de la fila «Calzado con punteras». El volcado de texto no la
  conserva, así que el tema cita sólo el bloque «I. Riesgos físicos». Es correcto y no afirma más.

Cero errores normativos en lo adaptado. Las tres correcciones son de aplicación al puesto y de
afirmaciones sin apoyo.
