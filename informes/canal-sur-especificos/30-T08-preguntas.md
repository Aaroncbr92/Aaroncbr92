# Puesto 30 · Tema 8 · Preguntas tipo test (fase 4, segunda ronda)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se contestan sólo con el tema 8 en su estado actual
(tras remate y 5 bis). La primera ronda (13 E, 1 M, 1 N; laguna XMP, ya cubierta) queda en el
historial de git (commit b08a902). Preguntas nuevas, para no repetir las ya pasadas.
E = entera; M = a medias; N = no. T = teoría; P = aplicación práctica.

1. (T, ingesta) La ingesta que graba automáticamente en un horario previsto, sin nadie delante y con
   recurrencia, es: a) de fichero · b) en directo (*crash record*) · c) programada · d) por lotes.
   → **c** (§ 1, «Qué es la ingesta», tabla). **E**
2. (P, ingesta) Antes de meter una SD en el lector, lo primero es: a) formatearla · b) poner el
   conmutador LOCK · c) renombrar los clips · d) copiar sólo la carpeta de vídeo. → **b** (§ 1, paso 1). **E**
3. (T, ingesta) Según la ayuda de Adobe, Premiere, al ingestar: a) no comprueba nada · b) verifica que
   no hay corrupción ni pérdida de datos, sin decir con qué algoritmo · c) usa SHA-512 · d) usa CRC32.
   → **b** (§ 1, «La ingesta en el programa de edición»). **E**
4. (P, digitalización) Digitalizar 90 minutos de cinta con captura normal lleva, como mínimo:
   a) unos 10 min · b) 45 min · c) 90 min · d) depende sólo del disco. → **c** (§ 2, «va en tiempo
   real»). **E**
5. (T, digitalización) En la captura desde cinta de Resolve 21, el número de pistas de audio
   capturables es: a) 2 · b) de 2 a 8 · c) de 2 a 16 · d) de 1 a 32. → **c** (§ 2, p. 561). **E**
6. (P, digitalización) Con *Capture Now* en Resolve, un clip capturado en TC 01:00:00:00 a 25 cuadros
   se llama: a) 01000000.dpx · b) 00090000.dpx · c) 00086400.dpx · d) reel01.dpx. → El tema da el
   ejemplo del manual (00086400.dpx, TC 01:00:00:00) y la regla (cuadros «based on the ingest frame
   rate»); 00086400 = 3.600 s × 24, así que a 25 cuadros serían 90.000 (b). El tema da la regla, pero
   no la cadencia del ejemplo: se deduce. **M** (no es laguna: el cálculo sale de la regla)
7. (P, transferencia) Un fichero de 45 GB por una línea de 300 Mb/s tarda, como mínimo: a) 2,5 min ·
   b) 20 min · c) 45 min · d) 2 h. → **b** (45 × 8 = 360 Gb = 360.000 Mb ÷ 300 = 1.200 s; § 3,
   método). **E**
8. (T, transferencia) Varias salas de informativos editan a la vez sobre el mismo material con
   caudal sostenido. El almacenamiento adecuado es: a) local · b) NAS · c) SAN · d) una memoria USB.
   → **c** (§ 3, tabla local/NAS/SAN). **E**
9. (T, verificación) En el *Clone Tool* de Resolve, la opción que el manual califica como «by far the
   fastest» es: a) CRC 32 · b) MD5 · c) SHA 256 · d) XXHASH64. → **d** (§ 4, tabla). **E**
10. (T, verificación) Dentro del *Archival Storage* del OAIS, la función que da «statistically
    acceptable assurance» de que el AIP no se ha corrompido es: a) *Replace Media* · b) *Error
    Checking* · c) *Disaster Recovery* · d) *Quality Assurance*. → **b** (§ 4, § 4.2.3.4). **E**
11. (T, copias) Un RAID 5 con tres discos de 4 TB da de capacidad útil y aguanta la caída de:
    a) 12 TB, ninguno · b) 8 TB, uno · c) 6 TB, dos · d) 4 TB, dos. → **b** (§ 5, tabla «Con tres
    discos»: dos discos de tres, pierde uno). **E**
12. (T, metadatos) La propiedad XMP que guarda el nombre de la cinta de la que se capturó el clip es:
    a) `dc:source` · b) `xmpDM:tapeName` · c) `xmpDM:logComment` · d) `xmpDM:good`. → **b** (§ 6, XMP). **E**
13. (T, archivo) Las cinco clases de la PDI del OAIS son procedencia, contexto, referencia, fijeza y:
    a) derechos de acceso · b) formato · c) resolución · d) autoría. → **a** (§ 7, «Access Rights
    Information»). **E**
14. (T, archivo) La LTFS está incluida en las cintas LTO: a) sólo en la LTO-10 · b) desde la LTO-5 ·
    c) desde la LTO-7 · d) nunca, es un programa aparte. → **b** (§ 7, LTFS). **E**
15. (T, archivo) Para conservar a largo plazo una cinta digitalizada, un archivo audiovisual suele
    usar un códec sin pérdidas de preservación como: a) H.264 · b) FFV1 o JPEG 2000 sin pérdidas ·
    c) ProRes Proxy · d) MP3. → El tema no habla de formatos de conservación (dice sólo que el formato
    que usa CSRTV no consta); el tema 4 tampoco. **N** (laguna)

Rúbricas: ingesta (1-3), digitalización (4-6), transferencia (7-8), verificación (9-10), copias
(11), metadatos (12), archivo (13-15). Teoría: 1, 3, 5, 8, 9, 10, 11, 12, 13, 14, 15. Práctica: 2,
4, 6, 7.

Resultado: 13 enteras, 1 a medias (6, se deduce de la regla), 1 no (15, laguna).
