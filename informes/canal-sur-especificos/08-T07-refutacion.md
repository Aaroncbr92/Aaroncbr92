# Puesto 08 · Tema 7 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Leídos: `ENCARGO.md`, el enunciado del puesto 08, los informes de redacción y verificación de T07. No se ha
corregido el tema.

## Fuentes releídas (todas el 24-09-2026, copias locales)

`Sony_PXW-Z200_help-guide.txt` (pp. 97-99, 151, 163, 251-252, 298, 336), `Sony_ILCE-7SM3_formatos-fichero.txt`
(entero), `Panasonic_AVC-Intra_FAQ.txt` (preguntas 1, 2, 10, 12), `Avid_DNxHD_white-paper-2012.txt` (pp. 3-4, lista
de variantes y tabla de calidad), `LOC_fdd000389_ProRes422.txt`, `DPC_fixity-and-checksums.txt` (tabla de niveles y
nota sobre bloqueo de escritura), `libro-de-estilo-333233b.txt` (5.3.3, pp. 81-82).

## Método

- Lente de exactitud: cotejo automático de todas las citas en negrita «…» contra las copias locales (espacios y
  comillas normalizados, «…» como corte). Casan todas salvo las de web (SDA, INCIBE; ya releídas con WebFetch por
  redacción y verificación) y la de SMPTE 2019-4 (tabulador en la copia). Después, lectura del contexto de cada
  cita para buscar salvedades omitidas y afirmaciones que la fuente contradice. Cuentas rehechas: 85, 34 y 21 min;
  00:36:36:02.
- Lentes automáticas: sin norma jurídica; `refutar_prosa.py`: 0 hallazgos.
- Lente de cobertura: 15 preguntas en `08-T07-preguntas.md`.
- «Copiado del común»: ninguno (según la redacción); nada que saltar.

## Hallazgos

### Grave (1)

**G1 · error 9/3 · «Avid DNxHD (SMPTE VC-3)»**: el tema dice «el documento no da la tasa de las demás variantes».
Falso: la tabla «Avid DNxHD encoding quality» del mismo libro blanco da **«Bandwidth»** 36, 100, 145, 220 y
**«440 Mb/sec»** (la 444), con profundidad (8 bits en 36, 100 y 145; «8- and 10-bit» en 220; «10 bit» en 444) y
muestreo (4:2:2; 4:4:4 en la 444), y el texto habla de **«six user-selectable bit rates»**. La restricción la
introdujo la verificación (su hallazgo 4), que acertó en que sólo 220x/220/145 se refieren a 1080i30 pero se pasó
al negar las demás cifras. Propuesta: añadir a la tabla una columna con la tasa y el muestreo de la tabla de Avid;
señalar que en la 444 el número no es la tasa (440 Mb/s); mantener que la cadencia de referencia sólo se da para
220x, 220 y 145. Corregir también «Lo que este tema no da» si hiciera falta (hoy no lo menciona) y la fila DNxHD
de «Documentos técnicos» ya dice «variantes y tasas», que quedaría coherente.

### Menores (2)

**M1 · error 6 · «La ingesta de una tarjeta, paso a paso», paso 1**: «La guía de conservación digital lo pide en
su segundo nivel». La fuente dice que la NDSA **«recommends the use of write-blockers at level 2»**, que
**«Write blockers also don't exist for all types of media»** y que **«some organisations might consider use of
write blockers to be unnecessary or a level 3 or level 4 step»**. Propuesta: «lo recomienda en su segundo nivel»
y añadir la salvedad.

**M2 · error 9 · «La tasa y la capacidad»**: tras la cita de Panasonic (16 min reales frente a 21 nominales),
el tema atribuye la diferencia al audio, los metadatos, el *proxy* y el sistema de ficheros y la llama «algo
menor». La fuente no explica la diferencia (un 25 %), y en 1080 a 23,98p da 20 min con la misma tarjeta, lo que
indica que la tasa real depende de la cadencia. Propuesta: quitar la explicación causal aplicada a ese ejemplo o
declararla oficio, y decir sólo que la cifra del fabricante es menor que la cuenta nominal.

### Confirmado sin cambios

Citas de la Z200 en su contexto (nombre de clip, [Series]/[Reset], [Title Prefix] y [Number Set] sólo MXF,
sincronización externa en [Preset] + [Free Run], «([Free Run] or [Clock])», Picture Cache Rec y Free Run,
trozos de 30 s/1/2 min, aviso de 5 minutos, SD del mismo tipo en relevo); ILCE-7SM3 (200M y 500M 4:2:2 10bit a
50p); ProRes (ramas, rasgos, MXF desde FCP 10.3, PSNR); Panasonic (perfiles, OP-Atom, minutos); DPC (MD5,
niveles); Libro de estilo 5.3.3 (p. 81) y los dos párrafos de p. 82, que siguen dentro de 5.3.3 (el siguiente
rótulo es 5.4).

## Cobertura (15 preguntas)

Enteras 12 · a medias 1 · no 2. El «no» de la pregunta 6 es G1. Lagunas que piden ampliar el tema:

- **L1 · pregunta 7**: el tema nombra «MPEG HD 422 (license required)» de la Z200 sin decir qué es (MPEG-2, el
  formato de 50 Mb/s del XDCAM HD422). Es formato clásico de las cámaras ENG de televisión y pregunta probable.
  Ampliar sólo con fuente leída (Sony o la ficha LOC de MPEG-2); si no se confirma, declararlo en «Lo que este
  tema no da».
- **L2 · pregunta 9**: cifras en MB/s de las clases de velocidad SD (V6…V90, U1/U3, Class 2…10). Hueco ya
  declarado; se puede cerrar con otra página de la SD Association que dé la tabla, y convendría para la
  aplicación práctica (elegir tarjeta para una tasa dada, pasando de Mb/s a MB/s).

## Ficheros tocados

Sólo `08-T07-preguntas.md` y este informe. El tema no se ha modificado.
