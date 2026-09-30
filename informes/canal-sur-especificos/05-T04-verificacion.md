# Verificación · Ayudante de Realización (05) · Tema 4 · Asistencia a la organización del control de realización

Fase 3. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/04-asistencia-organizacion-control-realizacion.md`.
Fuentes leídas en esta sesión: 30-09-2026 (reloj del sistema; el encargo dice que hoy es 24-09-2026).
La página de Fairlight Live se ha releído en la copia bajada el 29-09-2026. Las fechas de la portada y
de «Trazabilidad» se dejan como las puso el redactor. Copia previa: scratchpad `05t04-antes-verif.md`.

## 1. Pasajes copiados: sólo se ha comprobado que son literales

Se ha cotejado frase a frase (texto normalizado, sin negritas) contra `33-realizador-a/04` y `03`,
`realizacion/11`, `realizacion/15` y `realizacion-tv/18`.

- **Copiado del común (33-04)**: todo es literal. Las únicas diferencias son los cambios que declara
  el informe de redacción: la tabla de equipos, las remisiones a epígrafes y temas, «(tema 3)» quitado
  tras «señal personalizada», la remisión a la señalización técnica del tema 9 en «El piloto» y en el
  mezclador, y la frase del tema 6 en «La comunicación de los cambios». Todas las remisiones nuevas
  llevan a un tema cuyo enunciado 05 contiene la materia: el tema 6 (órdenes, incidencias), el 9
  (señalización técnica), el 11 (sincronía) y el 16 (comunicación entre control y plató).
- **Copiado de RTVE sin cambios**: literal. Son los dos criterios de las cajas de plató y el N-1 con
  su «Por qué».
- **Adaptado de RTVE** (verificado):
  - La regla «sincronizar es siempre retrasar…» y la cuenta de 40 ms: 1/25 s = 40 ms.
  - La realimentación de las pantallas: el «nunca» de RTVE se rebaja a «a secas», con la marca de
    oficio. Correcto.

## 2. Lo verificado en su fuente

- **IMS077_3** (`incual-IMS077_3.txt`). Cada literal nuevo y cada número de página coinciden con la
  fuente:
  - UC0217_3: título, RP1 a RP3, CR1.1 a CR1.8 (p. 7), CR2.1 (p. 7), CR2.2 a CR2.7 y CR3.1 a CR3.5
    (p. 8). Los medios pasan de la p. 8 a la 9, cortados por el salto de página: por eso `negritas.py`
    no los encuentra, pero sí son literales. La información utilizada está en la p. 9.
  - UC0216_3: CR3.2 y CR3.5 (p. 4); CR5.2, CR5.6, «telepromter», «servidores de video y/o audio» y
    «reproductores de CD, reproductores DAT, reproductores multimedia» (p. 5).
  - UC0218_3: CR3.2 y «servidores de video y audio» (p. 11).
  - MF0217_3: 180 h; C1, CE1.5, CE1.6 y CE1.7 (p. 18); contenidos 2 a 6 (p. 20).
  - RD 295/2004 y Orden PCI/797/2019.
- **Convenio**: la ficha 5353000 (p. 111) tiene la función básica y cinco tareas, y el control está en
  la 2.ª y la 3.ª.
- **RD 1680/2011**: 0910, RA 4 y su letra d), el esquema de intercomunicación.
- **Libro de Estilo**: 6.1.2, «los rótulos con su orden y ubicación precisa» (p. 89).
- **Manual ATEM** (es):
  - l. 2434-2438, audio en los clips.
  - l. 7920-7928, salida MADI 1: canal 11 «Audio del reproductor multimedia», del modelo ATEM
    Constellation 8K.
- **Fairlight Live** (página de producto): las dos citas son literales. La página lo presenta como
  «audio mixing solution for broadcast».
- **MOS** (`mos.txt`): «Audio Servers».

## 3. Correcciones aplicadas

| Pasaje | Error | Antes → después |
|---|---|---|
| Siglas | 5 | Se quita M/E, que se presentaba y no se usaba |
| «Lo que la ficha del ayudante dice del control» | 1/8 | «en dos de sus cinco tareas… En la primera… En la segunda» → «en la segunda y la tercera de sus cinco tareas… En la segunda… En la tercera». Es su orden en la ficha |
| «El sonido en la asistencia» | 3 | «por cuatro caminos» con cinco filas → «en cuatro momentos», que son los que da la tabla |
| «La iluminación en la asistencia» | 6/9 | «nunca por operación» → «no por operación: ningún criterio… le da el manejo de la mesa de luces (lectura…)». Se añade la salvedad de CE1.7: la observación sirve también para «dar instrucciones a los equipos» |
| «Los servidores de audio» | 9 | «Tres posibilidades documentadas, como ejemplos de fabricante» → dos documentadas por fabricante y la tercera de oficio (la del servidor de vídeo no tiene fuente) |
| Ídem, ATEM | 9 | «en alguno de sus modelos… su salida MADI» → «en el ATEM Constellation 8K, la salida MADI 1» |
| Ídem, comprobación 2 | 1 | «(RP1; CR1.3)», justo detrás de una cita de UC0216_3 → «(UC0217_3, RP1 y CR1.3)» |
| «Lo que comprueba el ayudante del grafismo» | 1 | «(CR3.1)», justo detrás de un CR3.5 de UC0216_3 → «(UC0217_3, CR3.1)» |
| Aplicación práctica, pasos 7, 8 y 9 | 1 | Los CR de las dos unidades quedaban ambiguos (UC0216_3 y UC0217_3 tienen los dos un CR3.2 y un CR3.5): se pone la unidad en cada uno |
| Ídem, paso 9 | 6 | «y el prompter su velocidad» → «y, si el programa lleva prompter, su velocidad». Así lo condiciona CE1.5 |
| Casos: retorno de plató y rótulo en directo | 1 | «CR3.2» → «UC0217_3, CR3.2» y «IMS077_3, CR3.5» → «IMS077_3, UC0217_3, CR3.5» |

Se han releído los pasajes cambiados. Cada «CE1.7», «CR1.3» o «la segunda» tiene delante su
antecedente.

## 4. Lentes

- `negritas.py` (IMS077_3, convenio, RD 1680/2011, manual ATEM, Fairlight, LE y MOS): 201 cotejadas y
  36 no encontradas. De esas 36:
  - Dos son de UC0217_3 cortadas por el salto de página; ya se han comprobado a mano.
  - Una es CR3.4 con elisión […]; es correcta.
  - El resto (Autocue, Vizrt, ANSI E1.11, Clear-Com, LE con elisión y MOS «P rotocol») está en texto
    copiado de 33-04 sin volcado de la fuente.
- `refutar_exactitud.py` y `refutar_modo.py` contra el RD: 0 hallazgos. El tema no cita artículos,
  sólo el anexo.
- `refutar_prosa.py`: sólo la CCU en el título, igual que en 33-04, y está presentada en las siglas.
- `indice.py`: 17.454 palabras, 61 epígrafes, sin cambios de rúbricas.

## 5. Ficheros tocados

Sólo el tema y este informe. El árbol tiene cambios en los temas 01, 02, 03, 06 y 16 del mismo puesto,
que no son de esta fase.
