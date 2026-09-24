# T07 · Remate (fase 5) · X Convenio Colectivo de la RTVA

Tema: `temas/canal-sur-comun/07-x-convenio-colectivo.md`. Aplica `informes/canal-sur-comun/T07-refutacion.md`
(modo ahorro). Fecha de trabajo y de lectura de las fuentes: 24-09-2026.

## Hallazgos del informe de refutación: comprobación y aplicación

El informe de refutación solo trae **un hallazgo** (H1, prosa, menor); exactitud y cobertura salieron
sin hallazgos. Se comprueba antes de aplicar:

### H1 · DT 5.ª C, tramos T5 y T6 sin antecedente · APLICADO

- **Comprobación en la fuente**: `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`,
  cuadro de tramos (líneas 2458-2484): «T6 / 22.001 hasta 30.000»; «T5 / 30.001 hasta 40.000». Confirma
  la lectura del informe.
- **Corrección aplicada**: en «Disposiciones transitorias», *Quinta. Retribuciones*, apartado C, donde
  decía «…y medio punto menos para los temporales de los tramos T5 y T6.» ahora dice «…y medio punto
  menos para los temporales de los tramos T5 y T6 (de 30.001 a 40.000 € y de 22.001 a 30.000 €).»
- **Antecedente**: el pasaje va dentro del mismo apartado C, que ya presenta el sistema de tramos
  general dos frases antes («tipos medio de descuento» por tramos, sin descuento hasta 22.000 €, hasta
  8,30 % en el tramo de más de 60.000 €); la aclaración entre paréntesis no rompe nada alrededor.

No hay más hallazgos que aplicar: el informe de refutación cerró exactitud y cobertura en cero, y lo
dice expresamente («cero hallazgos es un buen resultado si el tema está bien»).

## Lagunas de las preguntas

`T07-preguntas.md` contestó las quince preguntas **enteras** con el tema delante (0 a medias, 0 no).
No hay laguna que cerrar ampliando el tema.

## Relectura de antecedentes

Releído el pasaje corregido y su entorno (todo el apartado *Quinta. Retribuciones*, letras A a D, y el
párrafo que sigue sobre la Cámara de Cuentas): cada «el apartado siguiente», «el complemento del
artículo 49.3» y «esa reducción» tiene delante el antecedente que le corresponde. No se ha tocado nada
más del tema.

## Lentes automáticas

- `python3 herramientas/indice.py temas/canal-sur-comun/07-x-convenio-colectivo.md`:
  `23002 palabras · 35 epígrafes (sin portada: es un esquema)`. La portada llevaba «22.991 palabras»;
  se actualiza a **23.002** (única otra edición de este remate, mecánica).
- `python3 herramientas/refutar_prosa.py temas/canal-sur-comun/07-x-convenio-colectivo.md`: 7 avisos,
  los mismos que ya explicó la refutación (siglas CEMAC, CSR, CSTV, RTVA y SERCLA presentadas en el
  párrafo de siglas o en su propio paréntesis; las dos frases repetidas cierran reservas distintas en
  epígrafes distintos). Ningún aviso nuevo.
- `python3 herramientas/negritas.py` con las cuatro fuentes del encargo
  (`x-convenio-rtva-boja-240-2014.txt`, `BOE-A-2015-11430.md`, `BOE-A-2012-13126.md`,
  `BOE-A-2026-945.md`) más los documentos citados por el tema (REGCON, Reglamento de la Mesa, fusión,
  Cámara de Cuentas, Ley 7/2024, Reglamento del Parlamento, bases y programa de la convocatoria de
  2026): **383 negritas cotejadas**; 1 «no está» (la etiqueta de forma «Enunciado del programa», ya
  declarada, no una cita); 4 «¿ART. N?», los mismos falsos positivos que explicó la refutación
  (numeración cruzada con el ET y con la Ley 8/2025: art. 67.18 del convenio nombrado bien; arts. 38.3
  del ET nombrados bien; art. 18.1 de la Ley 8/2025 nombrado bien). Nada por corregir.

## Fase 5 bis

El remate corrige un solo pasaje puntual (una aclaración entre paréntesis) y no amplía el tema con
contenido nuevo, así que, según CICLO («Fase 5 bis recortada»), no hace falta agente nuevo: basta con
que el coordinador revise lo que marcan `refutar_prosa.py`, `indice.py` y `negritas.py` sobre el tema
rematado, y ya se ha hecho arriba (nada nuevo que marcar).

## Pasajes cambiados (lista para el coordinador)

1. Portada, fila «Extensión»: `22.991 palabras` → `23.002 palabras` (recuento mecánico de `indice.py`
   tras el cambio de contenido).
2. «Disposiciones transitorias» → *Quinta. Retribuciones* → apartado C: se añade, entre paréntesis, el
   rango de cada tramo («T5 y T6» → «T5 y T6 (de 30.001 a 40.000 € y de 22.001 a 30.000 €)»), aplicando
   H1 de `T07-refutacion.md`, comprobado en `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`.

## Ficheros tocados

- `temas/canal-sur-comun/07-x-convenio-colectivo.md` (los dos pasajes de la lista).
- `informes/canal-sur-comun/T07-remate.md` (este informe).
- Ningún otro.
