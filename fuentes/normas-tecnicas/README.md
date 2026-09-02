# Normas y recomendaciones técnicas

**Segundo nivel de la jerarquía de fuentes del bloque específico**
(`informes/fuentes-del-especifico-2026-09-02.md`): norma o recomendación de un
organismo de normalización, citada **por su designación exacta y su año de
edición**, y verificada con la lente de documento, no con las lentes por artículo.

Aquí no vale «según la UIT». Vale «**Recomendación UIT-R BT.2100-1 (06/2017),
cuadro 3**», que es lo que se puede comprobar y lo que el tribunal cita.

## Lo que hay

| Fichero | Designación exacta | Edición | De dónde sale | Leído |
|---|---|---|---|---|
| `UIT-R_BT.2100-1.pdf` y `.txt` | **Recomendación UIT-R BT.2100-1**, «Valores de los parámetros de imagen de los sistemas de televisión de elevada gama dinámica para la producción y el intercambio internacional de programas» | **06/2017** | Biblioteca pública de la UIT, `itu.int`, **versión en español** | 02/09/2026 |
| `UIT-R_BT.601-7.pdf` y `.txt` | **Recomendación UIT-R BT.601-7**, «Parámetros de codificación de televisión digital para estudios con formatos de imagen normal 4:3 y de pantalla ancha 16:9» | **03/2011** | Biblioteca pública de la UIT, `itu.int`, **versión en español** | 02/09/2026 |
| `SMPTE-ST-2110-indice.md` | Familia **SMPTE ST 2110**, índice con los títulos oficiales de cada parte | Índice vivo | Biblioteca abierta de la SMPTE, `pub.smpte.org/doc/2110/` | 02/09/2026 |
| `AES-normas-de-audio.md` | La frase de la **AES** que identifica **AES3**, **AES10 (MADI)**, **AES14** y **AES67** | Página viva | `aes.org/publications/standards/` | 02/09/2026 |

**Y una advertencia que salió de usarlas.** Al leer el cuadro 3 de la BT.601-7, la extracción
automática de texto devolvía «**16,75 MHz**» donde la recomendación dice **6,75 MHz**: el «1»
venía pegado de la fila superior. Se detectó porque **no cuadraba con el resto del cuadro** —720
muestras de luminancia frente a 360 de cada diferencia de color exigen la mitad exacta de
frecuencia— y **se confirmó recortando esa celda del PDF y ampliándola para leerla a ojo**.

**Con una norma técnica en PDF, el texto extraído no es la fuente; la página lo es.** Los ficheros
`.txt` de esta carpeta están para buscar; **la cifra que se publique hay que verla en el PDF**.

## Por qué justamente éstas

Porque **el examen las cita por su nombre**, y sin ellas no hay manera de
contestar sin inventar:

- La pregunta 42 del segundo cuadernillo dice literalmente «**la recomendación
  UIT-R BT 2100-1 (06/2017)** determina que el muestreo reticular de la imagen
  debe ser», con cuatro opciones geométricas. La recomendación, en su cuadro de
  parámetros, dice **«Muestreo reticular: Ortogonal»**. Es la respuesta oficial, y
  ahora está leída en la fuente y en la edición exactas que cita el enunciado.
- La pregunta 38 pregunta por «**la nomenclatura 4:2:2 definida en la norma CCIR
  601**». La CCIR es la antecesora de la UIT-R, y esa norma es hoy la
  **Recomendación UIT-R BT.601**, aquí en su versión **-7**.
- La pregunta 36 del primer cuadernillo pregunta **qué parte de la SMPTE ST 2110
  cubre los datos auxiliares embebidos**. El índice de la SMPTE lo responde por su
  título: la **ST 2110-40, «SMPTE ST 291-1 Ancillary Data»**. Y de paso deja ver
  que **la «ST 2110-50» de la opción d) no existe**.

## Lo que no se ha podido traer, y se dice

- **DCI, «Digital Cinema System Specification»**. El servidor de `dcimovies.com`
  responde 404 a las rutas de descarga. La resolución 4096 × 2160 que pregunta el
  examen queda **sin fuente de primer o segundo nivel**.
- **EBU/UER**. `ebu.ch` responde **403** a cualquier petición automática. Ni los
  estatutos ni la sede ni el régimen de cuotas se han podido leer en su fuente.
- **AES10 (MADI)**, su **texto**. El buscador de normas de la AES devuelve 404 y el documento
  está tras un muro de pago. Lo que **sí** se consiguió es la **identidad** de la norma, publicada
  por la propia AES: está en `AES-normas-de-audio.md`, con lo que se puede afirmar y lo que no.
- **Fichas de fabricante**: LiveU (LU300S), Sony (HXR-NX80), DJI (RS 4 Pro),
  Astera (Titan Tube), Mo-sys. Las páginas de producto devuelven 404 en las rutas
  probadas.

Lo que salga de esas cinco líneas, mientras no haya fuente, **se apoya en la
plantilla oficial y el tema lo dirá**, que es el quinto nivel de la jerarquía y su
única cautela sensata.
