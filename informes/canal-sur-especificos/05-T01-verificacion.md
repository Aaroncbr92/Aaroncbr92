# Verificación · Ayudante de Realización (05) · Tema 1 · Lenguaje audiovisual aplicado a televisión

Fase 3. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/01-lenguaje-audiovisual-television.md`.
Fuentes releídas el 30-09-2026 (reloj del sistema; el encargo fecha el trabajo el 24-09-2026).

## 1. Lo copiado: sólo comprobación de literalidad

Método: el tema se partió en párrafos, viñetas y filas de tabla, y cada uno se buscó normalizado
(espacios; para RTVE, sin `**`) en `33-realizador-a/01` y `03` y en `temas/edicion-montaje/10`. Lo
que no apareció se comparó palabra a palabra con el pasaje de origen.

- **Copiado del común** (33/01 y 33/03): literal. Las únicas diferencias son las declaradas en la
  redacción: siglas (C) y (CE); *match cut* y multipantalla en los términos; advertencia extendida a
  la IMS077_3; columna «Rúbrica de este tema» del RA 1 (0902); «(tema 3)» quitado tras la cámara
  máster; «Continuidad» → «Raccord» en el salto de eje; «(oficio)» en el decorado circular;
  «Plano» → «Encuadre» y remisión al tema 16 quitada en «Imagen y realidad» (el antecedente, «El
  encuadre como selección», abre la rúbrica). La función básica y las tres tareas de la ficha 5353000
  y la tarea 1 de la 5351000 son literales de 33/03. No se re-verifica.
- **Copiado de RTVE sin cambios** (`edicion-montaje/10`, §5 y §6): la tabla de los cinco géneros y la
  definición y los tres elementos del *match cut* son literales sin las negritas.

## 2. Lo nuevo y lo que cita normas: verificado en su fuente

- **IMS077_3** (`incual-IMS077_3.txt`; las cabeceras «Página: N de 25» abren cada página): «siempre
  bajo las órdenes y supervisión…», p. 1; título de UC0218_3 literal; CR4.3, CR4.4 y CR4.5 de
  UC0216_3, p. 4; MF0216_3, «2 El lenguaje narrativo audiovisual» y sus cinco contenidos, p. 16;
  «Movimiento de los personajes…», p. 17; MF0217_3, C1 y CE1.1, CE1.2, CE1.4, CE1.6, CE1.7 y CE1.8,
  p. 18; MF0218_3, CE1.3, p. 22; CE3.6, p. 23; «Movimiento y ritmo audiovisual.» y «Los principios
  básicos de la edición…», p. 24. Todo literal y bien paginado. Publicación: Orden PCI/797/2019;
  referencia normativa: RD 295/2004. El título de la Orden (BOE-A-2019-10917, BOE núm. 178, de
  26-VII-2019, buscado el 30-09-2026) confirma que **actualiza** cualificaciones «establecidas por el
  Real Decreto 295/2004».
- **Convenio**: fichas en el Anexo III, pp. 111 y 196 (como 33/03 y la verificación de 05-T02).
- **RD 500/2024**: «de 21 de mayo», confirmado en `BOE-A-2024-10685.txt`.
- **Libro de estilo**: «sólo pone cifras al ritmo del informativo»: las cifras de duración del libro
  (`grep segundo`) son todas de informativos (titulares, gráficos, declaraciones, panorámicas,
  presencia en vídeo, planos de 6.3.2). Se mantiene.
- **Remisiones internas de lo nuevo**: «par de escalas y treinta grados» está en «El corte que no se
  ve»; el plano de recurso, en «El tiempo del relato»; el plano de seguridad y la cámara máster, en «El
  plano en la realización de televisión»; los «dos epígrafes que siguen» y «los dos últimos de esta
  rúbrica» cuadran; el CR4.3 está citado en «La continuidad en el plató», que es el epígrafe anterior;
  la «tarea 2 de su ficha» es la del plató (orden del convenio en 33/03).
- **Siglas**: todas las que usa el tema están presentadas.

## 3. Correcciones aplicadas

| Línea | Error | Antes | Ahora | Fuente |
|---|---|---|---|---|
| 10 (ficha) | redacción | «(actualización de la Orden PCI/797/2019)» | «(actualizada por la Orden PCI/797/2019)» | Título de la Orden PCI/797/2019; igual que en «Normativa» |
| 1449 | 9 | «Una transición de continuidad por semejanza que los manuales de montaje recogen, y que es oficio sin norma detrás:» | «Una transición por semejanza que ninguna norma fija; es oficio:» | Ningún manual citado sostiene el *match cut*; RTVE lo daba como oficio sin norma. «De continuidad» no casa con planos de espacios y tiempos distintos |
| 1695 | coherencia del caso | «En directo continuo la simultaneidad da…» | «Mientras se graba cada bloque, la simultaneidad de las cámaras da…» | El caso es una grabación en dos bloques, no un directo |

No se quitó ningún dato. Las tres frases cambiadas se releyeron: sin remisiones sueltas.

## 4. Lentes

- `negritas.py` contra IMS077_3, RD 1680/2011, Libro de estilo, convenio, EBU R 95 e INTEF: 244
  cotejadas; 118 «no están», **todas** heredadas de 33/01 (Mateu Torres, sin volcado local, y tres del
  Libro de estilo con ligaduras o `[...]`), comprobado por búsqueda en 33/01. Las negritas nuevas
  están todas en su fuente.
- `refutar_exactitud.py` y `refutar_modo.py` contra el RD: 0 hallazgos.
- `refutar_prosa.py`: 0. `indice.py`: regenerado; 20.276 palabras, 79 epígrafes.

## 5. Ficheros tocados

- `temas/canal-sur-especificos/05-ayudante-de-realizacion/01-lenguaje-audiovisual-television.md`
- `informes/canal-sur-especificos/05-T01-verificacion.md` (este)
