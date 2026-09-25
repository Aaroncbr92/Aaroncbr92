# Puesto 30 · Tema 2 · Preguntas de refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.
Quince preguntas tipo test, contestadas **sólo con el tema**. La clave de las que el tema no contesta
se ha leído en la fuente (se indica).

| Nº | Tipo | Pregunta (✔ = correcta) | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Teoría | La luminancia de la HD según la UIT-R BT.709-6 es: a) 0,299 R + 0,587 G + 0,114 B; b) 0,2627 R + 0,6780 G + 0,0593 B; c) 0,2126 R + 0,7152 G + 0,0722 B ✔; d) 0,2126 R + 0,7152 G + 0,0593 B | Entera (§ «La colorimetría de referencia»; d se descarta con la regla de la suma) |
| 2 | Aplicación | Un material rotulado 1080i50 tiene por segundo: a) 50 cuadros; b) 50 campos, 25 cuadros ✔; c) 25 campos; d) 100 campos | Entera (§ «El barrido») |
| 3 | Teoría | En la BT.709-6, la frecuencia de muestreo de la luminancia del sistema 50/I es: a) 13,5 MHz; b) 37,125 MHz; c) 74,25 MHz ✔; d) 148,5 MHz | Entera (§ «El muestreo de la señal», punto 5.8) |
| 4 | Teoría | Un 25PsF es: a) una imagen entrelazada de 25 cuadros; b) una imagen progresiva transportada en dos segmentos por la misma interfaz que un entrelazado ✔; c) un formato de captación de 50 campos; d) un 1080p50 comprimido | Entera (§ «El barrido», anexo 2 de la BT.709-6) |
| 5 | Aplicación | En la forma de onda de una pieza en 10 bits el negro está en 64 y el blanco en 940. Según la BT.709-6 y la EBU R 103: a) negro y blanco nominales, pieza correcta ✔; b) fuera del rango preferente; c) error de gama; d) rango completo | Entera (§§ «La cuantificación» y «Los límites de la señal según la EBU») |
| 6 | Aplicación | Un material se ve lavado tras pasar por otro programa. La causa más probable es: a) submuestreo 4:2:0; b) confusión entre rango estrecho y completo ✔; c) *jitter*; d) cadencia 29,97 | Entera (§ «La cuantificación», oficio declarado) |
| 7 | Aplicación | Al insertar un rótulo blanco en un programa PQ, su nivel de señal según el Informe UIT-R BT.2408-9 es: a) 100 %; b) 75 %; c) 58 % ✔; d) 38 % | Entera (§ «El alto rango dinámico», tabla 1) |
| 8 | Teoría | El pico de luminancia ≥ 1 000 cd/m² que la BT.2100-3 pide al monitor de referencia HDR se exige: a) para pantalla completa en blanco; b) para brillos de área pequeña ✔; c) sólo en HLG; d) sólo en PQ | Entera (§ «El alto rango dinámico», nota 3c) |
| 9 | Aplicación | Un 1080p50 sin comprimir en 4:2:2 y 10 bits necesita como mínimo: a) SD-SDI; b) HD-SDI; c) 3G-SDI ✔; d) 12G-SDI | Entera (§ «La interfaz digital serie (SDI)») |
| 10 | Teoría | La SMPTE ST 292-1 expresa las tolerancias de *jitter* de la salida HD-SDI en: a) dB; b) intervalos unitarios (UI) ✔; c) mV; d) LUFS | A medias: el tema explica que el *jitter* es variación del instante de llegada de cada bit (descarta mV, dB y LUFS por razonamiento), pero no da la unidad ni los dos tipos (temporización, 1 UI; alineación, 0,2 UI; ST 292-1, tabla 3) |
| 11 | Teoría | Para sincronizar los equipos que trabajan con la BT.709-6, la propia recomendación prevé como señal de referencia: a) el código de tiempo LTC; b) el sincronismo analógico de tres niveles (*tri-level*) ✔; c) el reloj de palabra de 48 kHz; d) la subportadora PAL | No: el tema no trata la referencia de sincronismo de vídeo (BT.709-6, parte 6: «The tri level sync signal may be used as a reference signal for synchronization of devices…») |
| 12 | Aplicación | El tono de 1 kHz de las barras de una pieza, según la EBU R 68, debe leerse en: a) 0 dBFS; b) −9 dBFS; c) −18 dBFS ✔; d) −23 LUFS | Entera (§ «Los niveles del audio digital») |
| 13 | Aplicación | En el control de calidad de sonoridad, la EBU R 128-2023 admite por errores de medida una tolerancia de: a) ±1,0 LU; b) ±0,2 LU ✔; c) ±0,5 LU; d) ±2,0 LU | No: el tema sólo da la de ±1,0 LU de h), y el opositor marcaría a). La tolerancia de i) («±0.2 LU»), la de medida del pico (±0,3 dB) y la excepción j) no están |
| 14 | Teoría | En un HD-SDI a 48 kHz caben embebidos como máximo: a) 2 canales; b) 8; c) 16, en cuatro grupos ✔; d) 32 | Entera (§ «El audio dentro del vídeo») |
| 15 | Aplicación | Una secuencia de 25 fps usa código de tiempo: a) DF, porque corrige 3,6 s por hora; b) NDF ✔; c) DF que tira cuadros; d) indistintamente | Entera (§ «El código de tiempo») |

## Resultado

- Enteras: 12 (1-9, 12, 14, 15).
- A medias: 1 (10, *jitter*).
- No: 2 (11, sincronismo de referencia; 13, tolerancia de medida de la R 128).
- Aplicación práctica: 2, 5, 6, 7, 9, 12, 13 y 15.
