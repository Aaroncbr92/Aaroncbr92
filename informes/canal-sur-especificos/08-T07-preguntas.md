# Puesto 08 · Tema 7 · Fase 4 · Preguntas de refutación (15)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Contestadas sólo con el tema. Clave: **entera** (el tema da la respuesta y descarta los distractores), **a medias**
(la orienta pero falta el dato), **no** (el tema no la da o induce a error). T = teoría; P = aplicación práctica.

1. **(T, formatos)** El MXF es: a) un códec intracuadro normalizado por la SMPTE; b) un contenedor, cuya
   especificación central es la SMPTE ST 377-1; c) un formato de proyecto como el AAF; d) un perfil de H.264.
   → b. «Los contenedores». **Entera.**
2. **(T, formatos)** En el patrón operacional MXF OP-Atom: a) todo va en un solo fichero; b) hay un fichero por
   pista (vídeo y cada canal de audio); c) sólo se graba el *proxy*; d) el audio va comprimido. → b. «Los
   contenedores» (ST 390; P2 de Panasonic). **Entera.**
3. **(T, formatos)** Según UIT-R BT.2020-2, el UHD de televisión de primer nivel tiene: a) 4.096 × 2.160;
   b) 3.840 × 2.160 y formato 16:9; c) 3.840 × 2.160 y 17:9; d) 2.048 × 1.080. → b. «Qué define un formato».
   **Entera.**
4. **(T, códecs)** El formato XAVC HS de Sony usa: a) H.264 intracuadro; b) H.265 (HEVC) en GOP largo;
   c) MPEG-2; d) ProRes. → b. «XAVC (Sony)». **Entera.**
5. **(T, códecs)** AVC-Intra 100 es: a) 4:2:0, 8 bits, GOP largo; b) 4:2:2, 10 bits, intracuadro, perfil High
   422 Intra de H.264; c) 4:4:4, 12 bits; d) un códec de Sony. → b. «AVC-Intra». **Entera.**
6. **(T, códecs)** Según Avid, la tasa de Avid DNxHD 444 es: a) 444 Mb/s; b) 440 Mb/s; c) 220 Mb/s; d) 36 Mb/s.
   → b (tabla de «Avid DNxHD encoding quality»: 36, 100, 145, 220 y 440 Mb/s). El tema afirma que «el documento
   no da la tasa de las demás variantes» y no da ninguna cifra para la 444. **No.**
7. **(T, códecs)** El formato MPEG HD 422 que ofrece como opción la PXW-Z200 comprime con: a) MPEG-2 en GOP
   largo; b) H.265; c) ProRes; d) JPEG 2000. → a (dato de oficio, no leído). El tema lo nombra en la lista de
   la Z200 y no dice qué es. **No.**
8. **(P, formatos)** ¿Cuántos minutos nominales caben en una tarjeta de 64 GB a 100 Mb/s? a) unos 43; b) unos
   85; c) unos 170; d) unos 640. → b (64 × 8.000 ÷ 100 = 5.120 s). «La tasa y la capacidad» (regla y dos
   cuentas). **Entera.**
9. **(P, tarjetas)** Para un formato de 200 Mb/s (25 MB/s) en SD, ¿basta una tarjeta V30? a) no, V30 son 30 Mb/s;
   b) sí, V30 garantiza 30 MB/s de escritura mínima; c) sólo si es de 256 GB; d) la clase no tiene que ver con la
   escritura. → b. El tema da que el número indica la escritura mínima y remite a la tabla del fabricante, pero
   no da las cifras en MB/s (hueco declarado). **A medias.**
10. **(P, tarjetas)** En la Z200 se activa el envío del *proxy* por trozos (***[Chunk]***). Consecuencia: a) no
    hay cambio; b) la ranura B se dedica al *proxy* y no hay relevo ni grabación simultánea; c) se desactiva el
    código de tiempo; d) sólo graba en HD. → b. «La ingesta desde el lugar» (p. 163). **Entera.**
11. **(T, metadatos)** Con la pregrabación (Picture Cache Rec) activada en la Z200, el código de tiempo se graba
    en: a) Rec Run; b) Regen; c) Free Run aunque se haya elegido Regen o Rec Run; d) Preset. → c. «El código
    de tiempo». **Entera.**
12. **(P, metadatos)** A 25 fps, duración de 09:58:30:10 a 10:00:00:00 (exclusiva): a) 00:01:29:15;
    b) 00:01:30:15; c) 00:01:29:25; d) 00:01:30:10. → a. «La aritmética del código de tiempo» (método de
    préstamo a 25). **Entera.**
13. **(T, copia)** Según la Digital Preservation Coalition, para detectar daños accidentales en los ficheros:
    a) hace falta SHA-256; b) MD5 es suficiente; c) basta comparar tamaños; d) basta un RAID 1. → b. «La copia
    comprobada». **Entera.**
14. **(P, copia/entrega)** Un cámara envía desde el lugar a un servidor de la casa. ¿Qué protocolo? a) FTP,
    porque es más rápido; b) FTPES, porque en FTP contenido, usuario y contraseña van sin cifrar; c) HTTP;
    d) cualquiera. → b. «El envío por red». **Entera.** (Variante: RAID 5, mínimo tres discos, y RAID no es copia
    de seguridad: en el tema.)
15. **(T, entrega)** El Libro de estilo de Canal Sur (2004), para la cinta: a) obligaba a treinta segundos de
    barras; b) consideraba conveniente una noticia por cinta tras un mínimo de treinta segundos de barras, y
    dos noticias en el mismo soporte debían separarse con un minuto de barras; c) no trataba las barras;
    d) pedía un minuto de barras al principio. → b. «Lo que recomendaba el Libro de estilo». **Entera.**

## Resultado

Enteras 12 · a medias 1 (9) · no 2 (6, 7).

- La 6 no es una laguna sino un error del tema (hallazgo G1 de la refutación): la fuente sí da la cifra.
- Lagunas: 7 (qué es el MPEG HD 422) y 9 (cifras de las clases de velocidad SD).

Cobertura por rúbrica: formatos 1-3, 8; códecs 4-7; tarjetas 9-10; metadatos 11-12; ingesta 10; copia 13-14;
entrega 14-15.
