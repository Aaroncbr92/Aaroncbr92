# Puesto 30 · Tema 8 · Preguntas tipo test (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Contestadas sólo con el tema 8. E = entera; M = a
medias; N = no. T = teoría; P = aplicación práctica.

1. (T, ingesta) La ingesta en directo de una señal de agencia se graba por partida doble porque:
   a) es la más lenta · b) es la única que no se puede repetir · c) exige transcodificar · d) no
   admite metadatos. → **b** (§ 1, «Qué es la ingesta»). **E**
2. (P, ingesta) Un compañero «importa» los clips en el proyecto directamente desde la tarjeta y la
   devuelve a la cámara. ¿Qué pasa? a) nada, el programa ya los copió · b) los clips quedan sin
   material al retirar el soporte · c) el proyecto se corrompe · d) se pierden sólo los metadatos.
   → **b** (§ 1, «Ingestar no es lo mismo que importar»). **E**
3. (T, ingesta) Según la ayuda de Adobe, ingestar en Premiere es: a) enlazar ficheros sin copiarlos ·
   b) copiar y, en su caso, transcodificar el material desde el soporte de origen al almacenamiento
   del proyecto o a la caché · c) sólo crear *proxies* · d) exportar a MXF. → **b** (§ 1, cita
   de Adobe). **E**
4. (T, digitalización) En la captura desde cinta de DaVinci Resolve 21, los formatos de fichero
   disponibles son: a) MXF y MP4 · b) DPX y QuickTime · c) ProRes y DNxHD · d) BWF y WAV. → **b**
   (§ 2, p. 561; ProRes y DNxHD son códecs). **E**
5. (P, digitalización) Se importa una EDL para recapturar un montaje y en el *Media Pool* ya hay clips
   con el mismo nombre de cinta y TC de inicio que algunos eventos. Resolve: a) los duplica · b) no
   crea clips nuevos para esos eventos · c) borra los existentes · d) aborta la importación. → **b**
   (§ 2, «Batch Capture Via EDL», p. 564). **E**
6. (P, digitalización) Sin control remoto del magnetoscopio, ¿qué método de captura queda?
   a) captura por lotes · b) registrar y capturar un clip · c) *Capture Now* · d) captura desde EDL.
   → **c** (§ 2, «Lo que se revisa al digitalizar», oficio declarado). **E**
7. (P, transferencia) Un fichero de 30 GB por una línea de 1 Gb/s tarda, como mínimo: a) 30 s ·
   b) 4 min · c) 30 min · d) 4 h. → **b** (30 × 8 = 240 Gb ÷ 1 Gb/s = 240 s; § 3, método del
   cálculo). **E**
8. (T, transferencia) Según el manual de la Sony Z200, para una transferencia segura se usa:
   a) FTP · b) FTPES (FTPS en modo explícito) · c) SMB · d) HTTP. → **b** (§ 3). **E**
9. (T, transferencia) Señale la correcta: a) en una SAN se pide un fichero · b) en un NAS se piden
   bloques · c) una SAN da a cada estación bloques de disco como si fueran suyos · d) NAS y SAN
   sustituyen al RAID. → **c** (§ 3, tabla y párrafo siguiente). **E**
10. (T, verificación) En el *Clone Tool* de Resolve, la opción más resistente a colisiones es:
    a) File Size · b) CRC 32 · c) MD5 · d) SHA 512. → **d** (§ 4, tabla). **E**
11. (T, verificación) En el modelo OAIS, la función que valida la transferencia correcta del SIP al
    almacenamiento temporal es: a) *Error Checking* · b) *Quality Assurance* · c) *Replace Media* ·
    d) *Disaster Recovery*. → **b** (§ 4, «La verificación en el archivo», § 4.2.3.3). **E**
12. (P, copias) Un proyecto se monta sobre un RAID 1 en la sala y no hay más copias. Según el tema:
    a) cumple la regla 3-2-1 · b) protege del fallo de un disco, pero no de un borrado ni de un
    incendio: no es copia de seguridad · c) protege de todo · d) es un RAID sin redundancia. → **b**
    (§ 5, «Lo que no es una copia de seguridad»). **E**
13. (T, metadatos) EBUCore es: a) un códec de archivo de la EBU · b) un conjunto de metadatos
    descriptivos y técnicos/estructurales como extensión del Dublin Core · c) el identificador
    único del MXF · d) una recomendación SMPTE retirada. → **b** (§ 6). **E**
14. (T, metadatos) En Premiere Pro, los metadatos de clip y de fichero se escriben en el esquema:
    a) EBUCore · b) XMP · c) ALE · d) EXIF. → El tema no lo da: dice sólo que Premiere tiene
    «columnas de metadatos» y remite a los temas 3 y 15, que tampoco tratan XMP. **N** (laguna)
15. (T, archivo) Una unidad LTO-10: a) lee dos generaciones atrás · b) lee y escribe una generación
    atrás · c) no tiene compatibilidad hacia atrás · d) lee cintas LTO-5 con LTFS. Y su capacidad
    nativa es: … → primera parte **c** (§ 7, tabla de compatibilidad); la capacidad nativa no la da
    (hueco declarado en «Lo que este tema no da»; sólo 100 TB comprimidos). **M**

Rúbricas: ingesta (1-3), digitalización (4-6), transferencia (7-9), verificación (10-11), copias
(12), metadatos (13-14), archivo (15; y 11). Teoría: 1, 3, 4, 8, 9, 10, 11, 13, 14, 15. Práctica: 2,
5, 6, 7, 12.

Resultado: 13 enteras, 1 a medias (15, hueco ya declarado), 1 no (14, laguna).
