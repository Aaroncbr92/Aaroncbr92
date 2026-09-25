# Productor/a (puesto 32) · Tema 6 · Verificación

Fase 3. Tema: `temas/canal-sur-especificos/32-productor-a/06-recursos-tecnicos-y-materiales.md`.
Fecha de trabajo y de lectura de todas las fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026).
Ficheros tocados: el tema y este informe. Auxiliares en el scratchpad (Libro de Estilo NFKC, texto
del RD 16/2023 sacado de `diario_boe/txt.php?id=BOE-A-2023-1192`, art. 10 del RD 250/2025,
guion de cotejo literal), fuera del repositorio.

## 1. Lo copiado: sólo literalidad

Guion propio de cotejo (normaliza NFKC, quita `*` y `>` y une renglones) de cada frase y cada
celda del tema contra los 11 ficheros de origen declarados (común 06, 08/13, 30/08, 30/13 y los
seis temas de RTVE). **Todos los pasajes listados bajo «Copiado del común» y «Copiado de RTVE sin
cambios» aparecen literales.** Lo que no casó (197 unidades) es exactamente lo nuevo o lo
declarado como adaptado; no hay ningún pasaje de las dos listas que haya cambiado. No se
re-verificó su contenido.

## 2. Lo verificado en fuente

- **Convenio, anexo III** (`x-convenio-rtva-boja-240-2014.txt`): releídas las 29 fichas en sus
  líneas; cada cita, en su ficha y en su sitio (objeto o tarea). Correctas.
- **Cámara de Cuentas** §§ 221-225 (l. 3750-3850). Correcto salvo el hallazgo 4.
- **Contrato-programa**: MANIFIESTAN 8 (l. 486-514), puntos 16, 45, 46, 119-122 y cláusula
  quinta 1-6 (l. 2711-2747). Correcto salvo los hallazgos 1 y 5.
- **Ley 13/2022, art. 156** (`boe.py precepto BOE-A-2022-11311 a1-68`): una redacción, vigente;
  cita literal.
- **Libro de Estilo** 6.1 (común), 8.1 punto 6 (l. 4039-4044) y 9.9.1 (l. 6241-6247).
- **RTVE adaptado**: control central (opciones falsas de `13`, l. 56-60), MCRP (`12 tr.`, l.
  190-199), postproducción (`11`, l. 62-65), EDL (`11`, l. 104-110), embebedor (`13`, l. 136-137),
  cabeza caliente, viento, alimentación fantasma y Haas (`06`, l. 12, 129-150, 182-194, 213, 297).
  Conformes, salvo el hallazgo 7.
- `negritas.py` contra convenio, Cámara, contrato-programa, Carta, Ley 13/2022, Libro (NFKC), RD
  16/2023 y RD 250/2025 art. 10: 124 cotejadas; las 25 no encontradas son rótulos, las citas UIT-R,
  SMPTE y Manfredi (vienen del común) y la escaleta (ligaduras; literal en el común).
- `refutar_exactitud.py` con la Ley 13/2022: 3 «no literales» por paréntesis, falsos positivos (son
  citas del contrato-programa y de la UIT-R con «(anexo 1, 1.1)», no de la Ley). `refutar_modo.py`: 0.
  `refutar_prosa.py`: 0. `indice.py`: índice sin cambios; 15.085 palabras.

## 3. Hallazgos y correcciones (aplicadas)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 7 redacción derogada como vigente | «Las líneas de inversión…» | El tema presentaba el RD 391/2019 como el Plan Técnico de la TDT en vigor. `boe.py precepto BOE-A-2019-9513 a7`: su art. 7 está **derogado desde el 27-03-2025** por la disposición derogatoria única.1 del **RD 250/2025** (`BOE-A-2025-6004`), que aprueba el nuevo Plan | Salvedad de vigencia; art. 10.1 (720 líneas, H.264, -23,0 LUFS ±1,0 LU) y 10.2 (literal) del RD 250/2025. Portada, Normativa y Trazabilidad al día |
| 2 | 8 artículo mal / hueco | Mismo epígrafe y «Lo que este tema no da» | El redactor no pudo leer el RD 16/2023. Localizado con `boe_buscar.py` (`BOE-A-2023-1192`, texto publicado): **artículo segundo, uno, modifica el art. 7.2** del RD 391/2019. La parte expositiva del contrato-programa (7.1) se equivoca; la cláusula quinta (7.2) acierta | Se cita el 7.2 con su texto literal y la discrepancia; se quita el hueco de «Lo que este tema no da» |
| 3 | 3 recuento | «Quién diseña la luz…» | «Tres puestos reparten la iluminación»: el anexo III tiene también **Eléctrico de iluminación** (l. 5121) | «Cuatro puestos», con su objeto literal; añadido a la aplicación práctica y a Normativa |
| 4 | 1/9 | «Los medios de la RTVA…» | «inversiones previstas para 2019-2021» que «la Cámara reproduce»: son **necesidades de inversión estimadas por la dirección técnica**, § 225, cuadro nº 16 (fuera de los §§ 221-224 citados) | Reescrito; §§ 221-225 en portada y Trazabilidad |
| 5 | 1 cita cruzada | Mismo epígrafe | «El punto 4 de la misma cláusula prevé un Plan Inversor»: el punto 4 **remite** al punto 119 de la cláusula tercera, que es el que lo estipula | Corregido; punto 119 en Normativa y Trazabilidad |
| 6 | 6 salvedad omitida | Tabla inicial y «Los enlaces en la RTVA» | La ficha de **J. Radiofrecuencia** (l. 5641) tiene, palabra por palabra, el mismo objeto y la misma tarea que el Jefe de radioenlaces y UM | Se dice en los dos sitios; el convenio no dice cómo se reparten |
| 7 | 9 sin fuente | «La producción remota» | «Donde esa infraestructura no existe, la producción remota no es viable»: la fuente dice que «puede generar dificultades» donde la red «no es adecuada o no existe» | Rebajado a la fuente |
| 8 | 9 sin fuente | «Quién hace el grafismo» | «los rótulos … los escribe el redactor en la escaleta»: el apartado al que remite no dice quién los escribe | «van, como oficio, en la escaleta del sistema de redacción» |
| 9 | 9 sin fuente | «Lo que hay que conservar…» | «Lo que se conserva es la emisión tal cual salió, no el máster»: el 156.2 no lo dice | «El plazo corre desde la primera puesta a disposición del público, no desde la producción» |
| 10 | 9 | «La continuidad…» / «La resolución» / «Qué se puede preguntar» | «emite sólo en HD»: la fuente da la obligación («ha [de] utilizar»), no el hecho | «ha de emitir» / «debe emitir» |
| 11 | literalidad | «El rótulo de archivo» | «manda «tratar»» entre comillas; la fuente dice «serán ‘tratados’ en el proceso de edición» | Cita literal |
| 12 | 9 (fuente sin declarar) | «Los enlaces en la RTVA» | Paráfrasis del Libro de Estilo sin apartado y con «presentador» por «presentador en plató» | Cita literal de 8.1, punto 6; 8.1 en portada y Trazabilidad |
| 13 | redacción | «El decorado…» | «y «Localizar…»» sin verbo que lo rija | «y entre sus tareas figura «Localizar…»» |
| 14 | precisión | «Lo que hay que conservar…» | 156.1 enumera responsables «de las infracciones previstas en esta ley» | Añadido |

Nuevas siglas LU y LUFS presentadas en las siglas de entrada. «Extensión» de la portada: 15.000.
Releídos los pasajes cambiados: cada «ese artículo», «la misma cláusula», «el apartado anterior»
tiene su antecedente (se cambió «la misma cláusula» por «la cláusula quinta» donde el antecedente
quedaba dos párrafos atrás).

## 4. Avisos al coordinador

- **Manda la fuente**: el aviso 2 del redactor («no he podido leer el RD 16/2023») queda resuelto:
  7.2. Y la vigencia cambia: el RD 391/2019, art. 7, ya no rige (RD 250/2025). Conviene revisar
  cualquier otro tema del puesto 32 (o del común) que cite el RD 391/2019 como vigente.
- Las siglas «PEL = pequeña unidad móvil / unidad móvil ligera» vienen de la respuesta oficial
  del examen de RTVE (copiado sin cambios, no re-verificado); otro tema del repositorio
  (`informacion-grafica/11`) desarrolla PEL como «producción electrónica ligera». No se toca.
- Tema largo (≈15.100 palabras); los recortes posibles que señaló el redactor siguen en pie.
