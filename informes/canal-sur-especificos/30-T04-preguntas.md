# Puesto 30 · Tema 4 · Preguntas tipo test (fase 4, segunda refutación)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se contestan sólo con el tema
`04-formatos-de-video-y-audio.md` en su estado tras el remate y la revisión 5 bis. La tanda de la
primera refutación (anterior al remate) queda en el historial de git (commit b08a902).

Clave: E = entera · M = a medias · N = no.

1. (Contenedores, teoría) El MXF es: a) un códec de Sony · b) un contenedor que puede llevar
   esencia de casi cualquier códec · c) un formato de proyecto como el AAF · d) una norma de
   compresión intracuadro. → b (§§ 1 y 9). **E**
2. (HD, teoría) Un 1080PsF25 es: a) entrelazado a 50 campos · b) captación progresiva a 25 cuadros
   transportada en dos segmentos por cuadro · c) progresivo a 50 cuadros · d) un formato de la
   BT.2020. → b (§ 4, tabla y «25/PsF»). **E**
3. (UHD / frame rate, teoría) Según la UIT-R BT.2100-3, el barrido de sus formatos es: a) progresivo
   o entrelazado · b) sólo entrelazado a 50 Hz · c) sólo progresivo · d) progresivo segmentado.
   → c (§§ 4 y 7). **E**
4. (HDR, práctica) En una pieza PQ, el blanco de un rótulo va, según el Informe BT.2408-9: a) al
   100 % · b) al 75 % · c) al 58 % · d) al 38 %. → c (§ 5, tabla 1). **E**
5. (Compresión / profundidad, teoría) En rango estrecho de 10 bits (BT.2100-3, tabla 9), el negro
   está en el código: a) 0 · b) 16 · c) 64 · d) 256. → c (§ 3). **E**
6. (SDI, práctica) Un 1080p50 4:2:2 de 10 bits necesita como mínimo: a) SD-SDI · b) HD-SDI a
   1,485 Gb/s · c) 3G-SDI · d) 12G-SDI. → c (§ 11; 2.074 Mb/s de imagen activa). **E**
7. (Bitrate, práctica) Una hora de material a 50 Mb/s ocupa, en cuenta nominal: a) 22,5 GB ·
   b) 180 GB · c) 6,25 GB · d) 50 GB. → a (§ 8: 50 × 3.600 ÷ 8 = 22.500 MB, misma cuenta que la de
   los 54 GB). **E**
8. (Frame rate, teoría) A 25 fps el código de tiempo es: a) DF · b) NDF · c) DF o NDF indistintamente
   · d) no lleva código de tiempo. → b (§ 7). **E**
9. (Contenedores, práctica) Una tarjeta P2 con AVC-Intra en MXF OP-Atom guarda: a) un solo fichero
   con vídeo y audio · b) un fichero por pista, el sonido aparte · c) sólo el vídeo · d) un MOV por
   clip. → b (§ 9). **E**
10. (SDI/IP, teoría) La ST 2110-30 obliga a admitir la frecuencia de muestreo de: a) 44,1 kHz ·
    b) 48 kHz · c) 96 kHz · d) 32 kHz. → b (§ 11). **E**
11. (Entrega, audio) En la asignación 8b de la EBU R 123, las pistas 7 y 8 llevan: a) el LFE ·
    b) el estéreo · c) la audiodescripción · d) el sonido internacional. → b (§ 12, tabla). **E**
12. (Entrega, sonoridad) La EBU R 128 permite una tolerancia de ±1,0 LU: a) siempre · b) sólo en
    publicidad · c) cuando alcanzar el nivel objetivo no es viable en la práctica, por ejemplo en
    directos · d) nunca. → c (§ 12). **E**
13. (HDR, práctica) Un plano SDR ya etalonado que entra en una pieza HDR se convierte
    preferentemente: a) por luz de escena, llevando el 100 % SDR a 1.000 cd/m² · b) por luz de
    pantalla, llevando el 100 % SDR cerca de 203 cd/m² · c) sin conversión · d) por *up-mapping*
    siempre. → b (§ 5). **E**
14. (HDR, teoría) El perfil HDR10 combina: a) curva HLG y metadatos dinámicos · b) curva PQ, 10 bits
    y metadatos estáticos (ST 2086, MaxCLL, MaxFALL) · c) curva SDR y 12 bits · d) curva PQ y
    metadatos dinámicos por escena. → **N**: el tema da el título de la ST 2086 pero declara en «Lo que
    este tema no da» que HDR10, HDR10+ y Dolby Vision no tienen fuente normativa leída. Hueco
    declarado, no laguna.
15. (Bitrate / compresión, práctica) Relación de compresión de un DNxHD 120 (8 bits, 121 Mb/s) sobre
    un 1080i/50 4:2:2 de 8 bits: a) unas 4 veces · b) unas 6,9 veces · c) unas 8,5 veces · d) unas
    20 veces. → b (1.920 × 1.080 × 2 × 8 × 25 = 829 Mb/s; ÷ 121). **M**: el tema da la fórmula y
    los datos para hacerla, pero su propio ejemplo (§ 8) dice «unas 8,5 veces» calculando sobre
    10 bits, y lleva a la opción c. Es el hallazgo 1 de la refutación.

Resumen: 13 E · 1 M · 1 N.

Rúbricas del enunciado: resolución (—, cubierta por 2, 3), compresión (5, 15), HD (2), UHD (3), HDR
(4, 13, 14), códecs (1, 9, 15), frame rate (3, 8), bitrate (7, 15), contenedores (1, 9), SDI/IP (6,
10), estándares de entrega (11, 12); audio (10, 11, 12).
