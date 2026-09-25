# Puesto 30 · Tema 4 · Preguntas tipo test (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`.
Contestadas sólo con el tema. E = entera · M = a medias · N = no.

1. (Contenedores) El MXF es: a) un códec de la SMPTE · b) un contenedor que puede envolver material de casi cualquier códec · c) un formato de proyecto como el AAF · d) un perfil de H.264. → **b** (§§ 1 y 9). **E**
2. (HD, teoría) En la BT.709-6, el sistema «50/I» corresponde a una captación: a) 50 progresiva · b) 25 progresiva en cuadro segmentado · c) 25 entrelazada · d) 50 entrelazada. → **c** (§ 4: «50/I», captación «25 interlace»). **E**
3. (HD, práctica) Un material 1080PsF25 que entra en una secuencia 1080p25: a) debe desentrelazarse · b) se trata como progresivo, porque los dos segmentos son del mismo instante · c) tiene 50 imágenes distintas por segundo · d) sólo puede transportarse como entrelazado. → **b** (§§ 4 y 7). **E**
4. (Compresión / profundidad) En rango estrecho a 10 bits, la BT.2100-3 sitúa el negro y el pico nominal en: a) 0 y 1.023 · b) 16 y 235 · c) 64 y 940 · d) 256 y 3.760. → **c** (§ 3). **E**
5. (HDR, teoría) Según el Informe BT.2408-9, una carta gris del 18 % en PQ va al: a) 26 % · b) 38 % · c) 58 % · d) 75 %. → **b** (§ 5, tabla). **E**
6. (HDR, práctica) Un plano SDR ya etalonado entra en una pieza HDR. Lo indicado por el Informe BT.2408 es: a) conversión por luz de escena · b) conversión por luz de pantalla, llevando el 100 % SDR cerca del blanco de referencia de 203 cd/m² · c) dejarlo sin convertir con TCS=SDR · d) convertirlo a HDR, luego a SDR y otra vez a HDR. → **b** (§ 5). **E**
7. (HDR) El formato comercial HDR10 se define por: a) HLG y metadatos dinámicos · b) PQ, 10 bits y metadatos estáticos del tipo ST 2086 · c) BT.709 a 10 bits · d) PQ y 12 bits obligatorios. → (b es la habitual). El tema da PQ, 10 bits y la ST 2086, pero declara expresamente que no desarrolla HDR10 por falta de fuente. **M**
8. (Códecs) El AVC-Intra 100 es: a) H.265 GOP largo · b) H.264 intracuadro, 4:2:2 y 10 bits · c) MPEG-2 422P@HL a 50 Mb/s · d) un contenedor de Panasonic. → **b** (§ 6). **E**
9. (Códecs, práctica) En 1080i/50, la variante DNxHD de 8 bits que Avid da a 121 Mb/s es la: a) 145 · b) 120 · c) 185 · d) 85. → **b** (§ 6). **E**
10. (Frame rate) Para una producción a 25 fps el código de tiempo es: a) DF, porque salta cuadros · b) NDF, porque la cadencia es entera · c) DF o NDF indistintamente · d) DF, para coincidir con el reloj de pared. → **b** (§ 7). **E**
11. (Bitrate, práctica) Una hora de material a 121 Mb/s ocupa aproximadamente: a) 15 GB · b) 54 GB · c) 121 GB · d) 436 GB. → **b** (§ 8: 121 × 3.600 ÷ 8 = 54.450 MB). **E**
12. (Formatos de audio) Una mezcla 5.1 tiene: a) cinco canales de rango completo y uno de efectos de baja frecuencia · b) seis canales estéreo · c) cinco canales y un canal de código de tiempo · d) un canal mono y cinco de ambiente. → El tema no trata las configuraciones de canales (estéreo, 5.1) ni el orden de pistas de entrega; sólo nombra el AC-3 como el de «la televisión multicanal». **N**
13. (SDI, teoría) Según la SMPTE ST 292-1, el receptor HD-SDI típico opera con pérdidas de cable, a la mitad de la frecuencia de reloj, de: a) hasta 20 dB · b) 20 a 30 dB · c) hasta 30 dB · d) hasta 40 dB. → (a, según la fuente). El tema no da el valor de la ST 292-1, y su regla «cuanto más rápida la interfaz, más pérdida admite» llevaría a responder c o d. **N**
14. (SDI/IP) En la ST 2110-30, la frecuencia de muestreo que todos los equipos deben admitir es: a) 44,1 kHz · b) 48 kHz · c) 96 kHz · d) 192 kHz. → **b** (§ 11). **E**
15. (Estándares de entrega) En IMF, la pieza que representa una versión concreta de la obra y sincroniza su esencia es: a) la OPL · b) la CPL · c) el OP-Atom · d) la AS-11. → **b** (§ 12). **E**

Recuento: 12 enteras, 1 a medias (7), 2 no (12 y 13).

Rúbricas: resolución (4 indirecta; tema cubre SD/HD/UHD/8K/DCI), compresión (4), HD (2, 3), UHD (vía 4, 5),
HDR (5, 6, 7), códecs (8, 9), frame rate (3, 10), bitrate (11), contenedores (1), audio (12, 14),
SDI/IP (13, 14), estándares de entrega (15).
