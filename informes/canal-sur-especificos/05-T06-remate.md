# Remate · Ayudante de Realización (05) · Tema 6 · Realización multicámara en directo

Fase 5. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/06-realizacion-multicamara-directo.md`.
Entrada: `05-T06-refutacion.md` (0 graves, 2 menores, 1 laguna) y `05-T06-preguntas.md` (14 enteras,
1 a medias). Fuentes releídas el 30-09-2026 (reloj del sistema; el encargo dice 24-09-2026):
IMS077_3 (`fuentes/canal-sur/realizador/incual-IMS077_3.txt`, líneas 336-344: CR2.5 a CR2.7) y
RD 1680/2011 (`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`, líneas 653-654 y 662: 0905 RA 3.g,
3.h y RA 4.f).

## Correcciones aplicadas (las tres comprobadas; el informe de refutación acertaba)

### Menor 1 · Cita cruzada (error 1)

El tema no tiene epígrafe «3. Órdenes»; es «## 2. Coordinación de órdenes». Y el índice del tema sigue
el enunciado, no el RA 3 del 0905.

- «Qué es realizar en multicámara», frase de entrada: «Sus ocho criterios son el índice de este tema»
  → «Sus ocho criterios se reparten así por este tema». (Ocho criterios, a) a h): comprobado.)
- Tabla del RA 3, filas e) y f), columna «Dónde se estudia»: «3. Órdenes» → «2. Coordinación de
  órdenes».

### Menor 2 · Repeticiones

- «Qué es seguir las cámaras desde el control»: el RA 4.f del 0905 deja de citarse en negrita; queda
  «el RD pide un sistema para comprobar las ubicaciones de las cámaras, sus movimientos y los tiempos
  de desplazamiento entre sets (módulo 0905, RA 4.f, citado en el epígrafe 1)». El literal sigue
  entero en «Qué se comprueba desde el control» (epígrafe 1).
- «Los movimientos en multicámara»: igual, «en la coordinación del plató, con la comprobación de las
  ubicaciones de las cámaras, sus movimientos y los tiempos de desplazamiento entre sets (módulo 0905,
  RA 4.f, citado en el epígrafe 1)».
- «La entrada en antena»: el CR2.6 deja de citarse entero; queda «la hora de entrada y los tiempos de
  publicidad se comunican al control de continuidad (UC0217_3, CR2.6, citado entero en «Las llamadas
  de tiempo»)». Antecedentes comprobados: el epígrafe 1 y «Las llamadas de tiempo» están antes.

## Laguna 1 · Ampliación (pregunta 13)

Nuevo `###` «El cálculo hacia atrás desde la hora de salida», en «5. Control de tiempos», entre «Las
llamadas de tiempo» y «La entrada en antena». Declarado oficio (ninguna fuente publicada leída da el
método); se ancla en dos literales comprobados: **«el tiempo acumulado se ajusta a las indicaciones
del control de continuidad»** (CR2.7) y **«la cuenta atrás y tiempos parciales»** (CR2.6). Contiene:

- La regla: arranque previsto = hora de salida − (duración del bloque + bloques siguientes); desfase =
  arranque real − previsto (positivo, largo; negativo, corto); tiempo acumulado frente al previsto.
- Tabla de ejemplo, salida 21:30:00, cinco bloques (3'00'', 8'00'', 4'30'', 4'00'', 4'30''),
  arranques previstos 21:06:00, 21:09:00, 21:17:00, 21:21:30, 21:25:30, con arranque real y desfase.
  Aritmética revisada fila a fila; la conexión arranca a 21:22:10 y dura 4'00'', de modo que a las
  21:26:10 la despedida no ha empezado: 40'' largo, que se canta al realizador y al director (CR2.7),
  como pide la pregunta 13.
- Por qué cantarlo pronto (oficio).

El párrafo ya existente «Corregir un desfase…» queda al final del nuevo `###`, sin cambios.
La pregunta 13 no se ha tocado; ahora se contesta entera.

## Otros cambios

- Ficha: Extensión 15.400 → 15.900 palabras (indice.py: 15.909).
- Trazabilidad, fila «Oficio»: se añade «cálculo de tiempos hacia atrás desde la hora de salida y su
  ejemplo».

## Lentes

- `indice.py`: índice regenerado, 64 epígrafes (incluye el nuevo).
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` con IMS077_3 y RD 1680/2011: las dos negritas nuevas están en la fuente; los 48 «no
  está» son del Libro de Estilo, convenio, NTP y Autocue, fuentes no pasadas y sin tocar en este remate.
- `refutar_modo.py` con las mismas fuentes: 0 hallazgos.
- `refutar_exactitud.py`: no se corre; no cambia ninguna cita de precepto del BOE.

## Ficheros tocados

El tema 06 y este informe. (02 y 03 del mismo puesto aparecen modificados en el árbol por otros
agentes; no los he tocado.)

## Para la fase 5 bis

Sólo revisar el `###` «El cálculo hacia atrás desde la hora de salida» (nuevo).
