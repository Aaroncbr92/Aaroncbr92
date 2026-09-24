# Puesto 08 · Cámara Operador · Investigación del bloque C-sonido-formatos (temas 6, 7, 11)

Fase 1 · Investigar. Fecha de trabajo: 24-09-2026. Se escribe según avanza.

Alcance: **sólo lo que falta** tras el material RTVE ya localizado por el coordinador, que el
redactor copia literal (tema 6: `temas/informacion-grafica/06-el-sonido-en-eng.md`,
`temas/montaje-equipos/06-sonido-microfonos-y-altavoces.md`; tema 7:
`temas/informacion-grafica/03-la-camara-y-el-sensor.md`,
`temas/edicion-montaje/05-soportes-formatos-e-ingesta.md`,
`temas/realizacion-tv/12-formatos-y-procesos-de-registro.md`; tema 11:
`temas/montaje-equipos/03-camaras-tipos-y-manejo.md`,
`temas/montaje-equipos/10-asistencia-a-la-operacion-de-camara.md`,
`temas/informacion-grafica/11-teoria-de-la-informacion-audiovisual.md`). No se han releído esos
temas salvo sus rótulos, para no duplicar.

Regla de cita: **negrita entre comillas = literal de la fuente** (en su idioma original; la
traducción, cuando la hay, va en redonda detrás); redonda = paráfrasis o nota mía.

Lo propio de CSRTV: no consta publicado ningún manual técnico de cámara, de formatos de entrega,
de ingesta ni de mantenimiento de CSRTV (el informe del bloque B ya revisó el *Libro de estilo* de
2004; su parte técnica de cinta es histórica). Todo lo de abajo es fuente técnica general.

## Fuentes y fecha de lectura

| Clave | Documento | Dónde | Leído |
|---|---|---|---|
| **R128** | EBU R 128-2023, «Loudness normalisation and permitted maximum level of audio signals», Ginebra, noviembre 2023 (V5) | `https://tech.ebu.ch/docs/r/r128.pdf` (copia: `fuentes/normas-tecnicas/EBU_R128-2023.pdf`) | 24-09-2026 |
| **R68** | EBU Technical Recommendation R68-2000, «Alignment level in digital audio production equipment and in digital audio recorders» | `https://tech.ebu.ch/docs/r/r068.pdf` (copia: `fuentes/normas-tecnicas/EBU_R68-2000.pdf`) | 24-09-2026 |
| **T3341** | EBU Tech 3341-2023 (noviembre 2023), «Loudness Metering: ‘EBU Mode’ metering to supplement loudness normalisation» | `https://tech.ebu.ch/docs/tech/tech3341.pdf` (copia en `fuentes/normas-tecnicas/`) | 24-09-2026 |
| **T3343** | EBU Tech 3343-2023, «Guidelines for Production of Programmes in accordance with EBU R 128», noviembre 2023 | `https://tech.ebu.ch/docs/tech/tech3343.pdf` (copia en `fuentes/normas-tecnicas/`) | 24-09-2026 |
| **Z200** | Sony, *Help Guide Solid-State Memory Camcorder PXW-Z200/HXR-NX800*, «5-060-574-13(1) Copyright 2024 Sony Corporation» (versión impresa del manual web, v1, inglés) | `https://helpguide.sony.net/pro/z200nx800/v1/en/print.pdf` (copia: `fuentes/fabricantes/Sony_PXW-Z200_help-guide.pdf` y `.txt`) | 24-09-2026 |
| **SONY-FF** | Sony, *Help Guide ILCE-1*, «File Format (movie)» (página web del manual; explica XAVC HS / XAVC S / XAVC S-I) | `https://helpguide.sony.net/ilc/2040/v1/en/contents/TP1000409219.html` | 24-09-2026 |
| **SONY-HEVC** | Sony, «(Movie) Characteristics of each file format», ILCE-7SM3 (firmware 3.00 o posterior), web de soporte | `https://support.d-imaging.sony.co.jp/support/ilc/hevc/01/en/index.html` | 24-09-2026 |
| **LOC-PR** | Library of Congress, *Sustainability of Digital Formats*, «Apple ProRes 422 Codec Family», fdd000389, «Last significant FDD update: 2024-05-09» | `https://www.loc.gov/preservation/digital/formats/fdd/fdd000389.shtml` | 24-09-2026 |
| **LOC-MXF** | Library of Congress, *Sustainability of Digital Formats*, «Material Exchange Format (MXF)», fdd000013, «Last significant FDD update: 2024-05-09» | `https://www.loc.gov/preservation/digital/formats/fdd/fdd000013.shtml` | 24-09-2026 |
| **DNXHD** | Avid, *Avid DNxHD Technology* (libro blanco), «©2012 Avid Technology, Inc.» | copia servida por ARRI: `https://www.arri.com/resource/blob/31900/307a2e1b00ffc25f74b6ff7357af0bf9/avid-dnxhd-technology-white-paper-data.pdf` (copia: `fuentes/fabricantes/Avid_DNxHD_white-paper-2012.pdf`) | 24-09-2026 |
| **AVCI** | *AVC-Intra Frequently Asked Questions* (texto de Panasonic —«Panasonic is not replacing DVCPRO HD with AVC-Intra»— alojado por Avid; sin fecha impresa) | `https://resources.avid.com/SupportFiles/attach/FAQ_AVC-Intra.pdf` (copia: `fuentes/fabricantes/Panasonic_AVC-Intra_FAQ.pdf`) | 24-09-2026 |
| **SDA** | SD Association, «Speed Class» | `https://www.sdcard.org/developers/sd-standard-overview/speed-class/` (leída con WebFetch, resumen de modelo: cotejar a ojo antes de publicar) | 24-09-2026 |
| **DPC** | Digital Preservation Coalition, *Digital Preservation Handbook*, «Fixity and checksums» | `https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums` | 24-09-2026 |
| **INCIBE** | INCIBE (Instituto Nacional de Ciberseguridad), blog Ciudadanía, «Definiendo mi estrategia de copias de seguridad», 29-09-2021 | `https://www.incibe.es/ciudadania/blog/definiendo-mi-estrategia-de-copias-de-seguridad` (leída con WebFetch; curl directo falla por bucle de redirecciones: cotejar la cita a ojo) | 24-09-2026 |
| **SONY-A1** | Sony, *Help Guide ILCE-1*, páginas «On cleaning», «Notes on the battery pack and charging the battery», «Notes on memory card» | `https://helpguide.sony.net/ilc/2040/v1/en/contents/TP1000384647.html`, `…/TP1000384644.html`, `…/TP1000409205.html` (copia de texto: `fuentes/fabricantes/Sony_ILCE-1_help-guide_extractos.txt`) | 24-09-2026 |
| **IATA** | IATA, *Passengers Travelling with Lithium Batteries – Guidance Document*, «Revised for the 2026 Regulations», fechado 31/03/2026 (basado en las Instrucciones Técnicas OACI 2025-2026 y la 67.ª ed. del DGR de IATA) | `https://www.iata.org/contentassets/6fea26dd84d24b26a7a1fd5788561d6e/passengers_travelling_with_lithium_batteries.pdf` (copia: `fuentes/normas-tecnicas/IATA_pasajeros-baterias-litio-2026.pdf`) | 24-09-2026 |


Nota sobre el README de `fuentes/normas-tecnicas/`: dice que `ebu.ch`/`tech.ebu.ch` respondían
**403** el 02-09-2026. **El 24-09-2026 sí descargan** (HTTP 200, con agente de navegador). Manda la
fuente: el hueco «EBU no consultada» de otros temas ya se puede cerrar.

---

## Tema 6 · Captación de sonido asociada a cámara: microfonía, niveles, sincronía, ambiente y criterios básicos

Hueco declarado: los **niveles de grabación en cámara** (RTVE los trata de pasada) y los
**criterios básicos**; la norma de nivel (EBU R 68 / R 128) y los mandos de audio de la cámara.

### 6.1 Nivel de alineación digital: −18 dBFS (EBU R 68)

- R68, recomendación: **«its Members should use coding levels for digital audio signals which
  correspond to an alignment level which is 18 dB below the maximum possible coding level of the
  digital system, irrespective of the total number of bits available.»** Nota 2: **«corresponding
  to a ratio of 1:8 (18.06 dB)»**.
- R68, considerando: la alineación se define con **«a sine wave signal which has a level (the
  alignment level) which is 9 dB (or 8 dB in some organizations) below the permitted maximum level
  of the audio programme»**; y **«due to the characteristics of quasi-peak programme meters used by
  broadcasters, the true programme peaks can be 3 dB greater than those indicated; When operator
  errors are taken into account the true peaks may occasionally be 6 dB greater than indicated or
  15 dB above alignment level»**. (Es la razón del margen: 18 dB de reserva sobre el tono.)
- R68: grabación **«with linear coding using no pre-emphasis and with a resolution of at least 16
  bits in accordance with ITU-R Recommendation BS.646»** (el PDF extrae «161»: el «1» es la llamada
  de la nota 1; nota 1: **«16-bit recordings may not meet the requirements of some organizations
  regarding the signal-to-noise in production equipment»**).
- T3343 §8.1: **«An Alignment Signal in broadcasting consists of a sine-wave signal at a frequency
  of typically 1 kHz, which is used to technically align a programme’s audio path. In digital
  systems the level of such an Alignment Signal is 18 dB below the maximum coding level,
  irrespective of the total number of bits available (−18 dBFS).»**
- T3343 §8.1: **«The switch to loudness normalisation does NOT change this approach»** … **«electrical
  alignment for sound-programme exchange can be performed as usual, with a sine-wave signal of 1 kHz
  at a level of −18 dBFS.»**
- T3343 §8.1: con el paso al **«Maximum Permitted True-Peak Level» (−1 dBTP in production for generic
  PCM signals) the recommended PML of −9 dBFS in ITU-R BS.645 becomes obsolete»**.
- T3343 §8.1: **«The alignment level of −18 dBFS (1 kHz tone) will read as −18 LUFS on a loudness
  meter with the absolute scale (or +5 LU on the relative EBU mode scale)»** … **«The EBU therefore
  recommends using a peakmeter for alignment.»**
- Ya en el temario RTVE (`temas/ing-tec-teleco/12-sonido.md`): −18 dBFS Europa / −20 dBFS EE. UU.
  como respuesta de examen. El −20 dBFS estadounidense (SMPTE RP 155) **no lo he leído en su
  fuente**: si el redactor lo usa, que lo tome del tema RTVE declarándolo sin norma leída.

### 6.2 Sonoridad: EBU R 128 (lo que importa al cámara)

- R128 (V5, noviembre 2023). Historia: **«First published February 2010»**; revisiones 2011
  (**«relative gate changed from −8 to −10 LU»**), 2014 (**«Target level (−23 LUFS) tolerance changed
  to ± 0.5 LU (except Live-programmes)»**), 2020 y 2023.
- R128 considerando a) y b): **«peak normalisation of audio signals has led to considerable loudness
  differences between programmes and between broadcast channels»**; esas diferencias **«are the cause
  of the most viewer/listener complaints»**.
- R128 h): **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS. Where
  attaining the Target Level is not achievable practically (for example, live programmes), a
  tolerance of ±1.0 LU is permitted.»**
- R128 i): **«a tolerance of ±0.2 LU is allowed in order to take account of measurement errors»**.
  (Ojo: la ficha de historial dice que en 2014 la tolerancia pasó a ±0,5 LU; el texto vigente
  2023, punto h, sólo nombra ±1,0 LU para directos e i ±0,2 LU de medida. **Discrepancia interna del
  documento**: el historial menciona ±0,5 LU y el articulado de 2023 no; manda el articulado. Dudoso
  para test; no afirmar ±0,5 LU como vigente.)
- R128 k): medida con medidor **«compliant with ITU-R BS.1770 (including the level-gating method
  described in equation (7)) and EBU Tech 3341»**.
- R128 m): **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during
  production (linear audio)»**; tolerancia de medida **«±0.3 dB»**.
- R128 nota 1: **«LUFS’ is equivalent to ‘LKFS’ (which is used in ITU-R BS.1770)»**.
- R128 e): BS.1770 introduce **«the measures LU (Loudness Unit) and LUFS (Loudness Units, referenced
  to Full Scale)»**.
- R128 c): el **«QPPM (Quasi-Peak Programme Meter) specified in EBU Tech 3205-E [1] does not reflect
  the loudness of an audio signal»**.
- R128 n): **«Loudness Range»** (LRA) según EBU Tech 3342; nota 2: **«For programmes shorter than 1
  minute, the use of the measure Loudness Range is not recommended»** (**«Short-term-Loudness values
  (3-seconds-window)»**).
- T3341 (EBU Mode): **«The Momentary Loudness uses a sliding rectangular time window of length 0.4
  s. The measurement is not gated.»**; **«The Short-term Loudness uses a sliding rectangular time
  window of length 3 s.»**; **«The Integrated Loudness uses gating as described in ITU-R BS.1770.»**
  Abreviaturas: **«‘Momentary’, abbreviated ‘M’»**, **«‘Short-term’, abbreviated ‘S’»**,
  **«‘Integrated’, abbreviated ‘I’»**.
- T3343 (resumen True Peak): **«It is only necessary to leave a headroom of 1 dB below 0 dBFS to
  still accommodate the potential under-read of about 0.5 dB (for a 4x oversampling true-peak meter;
  basic sample rate: 48 kHz)»**; para MPEG1 Layer2 y Dolby AC-3: **«−2 dBTP»**.
- T3343: **«The greater headroom will be a welcome bonus for crowd noise, for example, of sports
  programmes»** (argumento para no saturar el ambiente en captación).
- **Aplicación al cámara (nota mía, costumbre de oficio, no norma)**: R 128 normaliza el
  *programa* terminado (post y emisión); en cámara el operador trabaja con el vúmetro de pico de la
  cámara, referido a la alineación −18 dBFS y dejando margen bajo 0 dBFS. Ninguna norma EBU leída
  fija «el nivel de la voz en cámara»; no inventar una cifra.

### 6.3 Los mandos de audio de una cámara de hombro/mano actual (Sony PXW-Z200, 2024)

Se toma un modelo concreto de fabricante como ejemplo de cómo son los mandos; **no consta qué
cámaras usa CSRTV**, así que el redactor debe presentarlo como «por ejemplo, en una cámara
Sony PXW-Z200», nunca como el equipo de Canal Sur. Número de página del PDF entre paréntesis.

- Conmutador de entrada (p. 13): **«INPUT 1/INPUT 2 (LINE/MIC/MIC+48V) switches»**; **«LINE:
  External audio device (e.g. mixer)»**; **«MIC: Dynamic microphone, battery-operated microphone»**;
  **«MIC+48V: +48 V phantom power microphone»**.
- Advertencia (p. 136): **«Selecting MIC+48V and connecting a microphone that is not compatible with
  a +48V source may damage the connected device. Check the setting before connecting the device.»**
  y **«If noise is a concern on connectors with no device connected, set the corresponding INPUT
  1/INPUT 2 (LINE/MIC/MIC+48V) switches to LINE.»**
- Automático / manual (p. 16): **«AUTO/MAN switch — Switches the CH-1/CH-2 audio recording level
  between auto mode and manual mode.»** Manual (p. 138): **«Set the CH1/CH2 (AUTO/MAN) switches for
  the channels to adjust to the MAN position.»** **«During shooting or standby, turn the AUDIO LEVEL
  dials (CH1)/(CH2) of the corresponding channels to adjust the audio level.»**
- Cuatro canales (p. 139): **«You can connect up to four channels of XLR audio devices to the unit at
  the same time by using an XLR-K2M XLR adaptor (not supplied) or XLR-K3M XLR adaptor (not
  supplied).»** Por defecto las cuatro pistas vienen del micro interno: menú [CH1…CH4 Input Select],
  valor de fábrica **«[Internal MIC]»** (p. 260).
- Menú [Audio] – [Audio Input] (pp. 260-261), con su valor de fábrica:
  - **«[INPUT1 MIC Reference] −80dB / −70dB / −60dB / −50dB / −40dB / −30dB»**, fábrica **«−50dB»**:
    **«Sets the reference recording level for XLR microphone input from INPUT 1.»**
  - **«[Line Input Reference] +4dB / 0dB / −3dB / [EBUL]»**, fábrica **«+4dB»**.
  - **«[Reference Level] −20dB / −18dB / −16dB / −12dB / [EBUL]»**, fábrica **«−20dB»**: **«Selects the
    recording level of the 1 kHz reference tone signal.»** (Nota mía: el valor de fábrica −20 es el
    estadounidense; para la alineación EBU R 68 se elige −18dB. «EBUL» no se desarrolla en el
    manual; no afirmar qué significa.)
  - **«[CH1 Wind Filter] [On] / [Off]»**, fábrica **«[Off]»**: **«Enables/disables the wind reduction
    filter for CH1.»**
  - **«[Limiter Mode] [Off] / −6dB / −9dB / −12dB / −15dB / −17dB»**, fábrica **«[Off]»**: **«Selects the
    limiter characteristic for large input signals when adjusting the audio input level
    manually.»**
  - **«[CH1&2 AGC Mode] [Mono] / [Stereo]»**: **«When [Stereo] is selected, auto gain control is linked
    between channels.»**
  - **«[1kHz Tone on Color Bars] [On] / [Off]»**: **«Turns the 1 kHz reference tone signal on/off when
    displaying color bars.»**
- Escucha (p. 99): **«Connecting a set of headphones to the headphone jack enables you to monitor the
  audio being recorded.»**; canal con **«[Monitor CH]»**.
- Nota del manual (p. 136): **«Audio is not recorded in Slow & Quick Motion mode.»** (Dato útil para
  el tema 15 y para avisar a redacción.)

### 6.4 Sincronía: código de tiempo entre cámara y equipo externo (Z200)

(La claqueta y la sincronía de doble sistema ya están en el tema RTVE; esto añade el bloqueo de TC.)

- p. 298: **«You can synchronize the timecode of the unit with an external device.»**
- **«supply a reference timecode for synchronizing the system frequency of the unit to the TC IN/OUT
  connector. The timecode generator of the unit acquires lock with the reference timecode, and
  “EXT-LK” is displayed on the screen.»**
- **«Once about ten seconds have elapsed after the timecode locks, the external lock state is
  maintained even if the external reference timecode source is disconnected.»**
- **«do not start recording immediately. Wait for a few seconds until the timecode generator
  stabilizes before recording.»**
- **«If the frequency of the reference timecode and the frame frequency on the unit are not the same,
  lock cannot be acquired»**; **«The timecode may shift by one frame per hour with respect to the
  reference timecode.»** (Por eso se re-sincroniza periódicamente: nota mía de oficio.)
- Para esclavizar otro equipo a la cámara: modo **«[Free Run] or [Clock]»**.
- Bits de usuario (p. 99): **«You can add an 8-digit hexadecimal number to a clip as user bits.»**

### 6.5 Criterios básicos: lo que queda sin norma

- No se ha encontrado norma (UIT, EBU, AES, UNE) que fije para ENG: cuántos canales, qué va en
  cada uno (p. ej. micro de mano en CH1 y ambiente en CH2), distancia del micro, ni un «pico de voz
  a −12 dBFS». Todo eso es **costumbre de oficio**; si el redactor lo incluye (o el tema RTVE lo
  trae), debe decirlo así. No inventar cifras.
- No consta documento publicado de CSRTV sobre asignación de pistas en ENG.

---

## Tema 7 · Formatos de grabación, códecs, tarjetas, metadatos, ingesta, copia de seguridad y entrega de material

Hueco declarado: los códecs de cámara por su nombre (XAVC, ProRes, DNxHD, AVC-Intra), las
tarjetas actuales, los metadatos que pone el cámara, la copia de seguridad con verificación y el
protocolo de entrega. Contenedor/códec, MXF y sus OP, proxy, SxS/P2 e ingesta ya están en RTVE.

### 7.1 XAVC (Sony): la familia y su códec

- SONY-FF: **«The XAVC HS format uses the HEVC codec, which has high compression efficiency.»**
  **«Long GOP compression is used for movies.»** (XAVC HS 4K/8K).
- SONY-FF: **«The XAVC S-I format uses Intra compression for movies. This format is more suitable for
  editing than Long GOP compression.»**
- SONY-FF (definición Intra / Long GOP, útil para el tema): **«Intra/Long GOP is a movie compression
  format. Intra compresses the movie by frame, and Long GOP compresses multiple frames. Intra
  compression has better response and flexibility when editing, but Long GOP compression has better
  compression efficiency.»**
- SONY-HEVC: XAVC S **«records movies in the widely used MPEG-4 AVC/H.264 codec»**; XAVC HS
  **«records high image quality movies with rich gradations and smaller file sizes using the MPEG-H
  HEVC/H.265 codec with 10-bit color sampling»**; para editar **«We recommend setting Record Setting
  to 10-bit 4:2:2 for editing movies since this setting assures rich gradation.»**
- Z200, especificaciones (p. 336): **«Recording format (video) MP4 format: XAVC HS Long
  422/420 · XAVC S Long 422/420 · XAVC S-I Intra · MXF format (PXW-Z200 only): XAVC Long 422/420 ·
  XAVC I Intra · MPEG HD 422 (license required)»**; **«Recording format (audio) LPCM 24-bit, 48 kHz,
  4-channel»**.
- Z200: el menú de códec de streaming ofrece **«[H.265/HEVC]»** y **«[H.264/AVC]»** (p. 202):
  **«When [Codec] is set to [H.265/HEVC], some receivers may not support playback
  correctly.»**
- **No confirmado en fuente primaria**: que XAVC (MXF, gama broadcast: XAVC Intra / XAVC Long) se
  base en H.264/MPEG-4 AVC nivel 5.2. `pro.sony` (XAVC explained, white paper, *XAVC Specification
  Overview* rev. 2.1) responde **403** el 24-09-2026. Lo afirman Wikipedia y buscadores; **no usar
  sin fuente**. El Z200 sólo dice «XAVC Long» / «XAVC I Intra», sin nombrar la norma de compresión.

### 7.2 Apple ProRes

- LOC-PR: **«Apple ProRes is a family of proprietary, lossy compressed, high quality video
  intermediate codecs primarily supported by the Final Cut Pro (FCP) suite»**; dos ramas: **«the
  Apple ProRes 422 Codec Family (described here) and the Apple ProRes 4444 Codec Family»**.
- LOC-PR, rasgos de la familia 422: **«4:2:2 source material»**, **«any frame size (including SD, HD,
  2K, 4K, and 5K) at full resolution»**, **«10-bit sample depth»**, **«intrafame (I-frame) only»** [sic],
  **«variable bit rate»**.
- LOC-PR: miembros 422: **«Apple ProRes 422 Proxy»**, **«Apple ProRes 422 LT»**, ProRes 422, **«Apple
  ProRes 422 HQ»**; y la rama 4444 (con **«4444 XQ»**).
- LOC-PR: **«ProRes codecs are usually contained within the QuickTime "mov" wrapper but starting with
  Final Cut Pro 10.3 released on October 27, 2016, the option for using ProRes in the MXF Generic
  Container was added»**; mapeo: **«SMPTE RDD 44:2017-11»**; sintaxis: **«SMPTE RDD 36-2015: Apple
  ProRes Bitstream Syntax and Decoding Process»**.
- LOC-PR citando el White Paper de Apple (junio 2014): **«PSNR for Apple ProRes 422 HQ is 15–20 dB
  higher than that for Apple ProRes 422 Proxy, but the Apple ProRes 422 HQ stream has nearly five
  times the data rate of the Apple ProRes 422 Proxy stream.»**
- **No usar**: el año de introducción. LOC-PR dice **«first supported in Final Cut 2 (2001)»**, lo que
  no cuadra (Final Cut *Studio* 2 es de 2007); dato ambiguo, fuera. Tasas en Mb/s por variante: no
  leídas en el White Paper de Apple (no descargado); no dar cifras.

### 7.3 Avid DNxHD (SMPTE VC-3)

- DNXHD: **«Avid DNxHD is a revolutionary 10 and 8-bit HD encoding technology that significantly
  reduces storage and bandwidth requirements while providing mastering-quality HD media.»**
- DNXHD: **«Codified by SMPTE as VC-3 standard»**; documentos: **«SMPTE 2019-1 VC-3 Picture
  Compression and Data Stream Format»**, **«SMPTE RP 2019-2 VC-3 Decoder and Bit stream
  Conformance»**, **«SMPTE 2019-3 VC-3 Type Data Stream Mapping over SDTI»**, **«SMPTE 2019-4 Mapping
  VC-3 Coding Units into the MXF Generic Container»**.
- DNXHD: **«Avid applications store Avid DNxHD material natively inside industry-standard MXF
  files»**; **«the source code for Avid DNxHD is licensable free of charge»**.
- DNXHD, familias: **«Avid DNxHD 444: … 10-bit 4:4:4 RGB»**; **«Avid DNxHD 220x: For superior
  quality image in a YCbCr-color space for 10-bit sources. … 220Mbps is the data rate for 1920 x 1080
  30fps interlace sources (60 fields) while progressive sources at 24fps will be 175Mbps»**; **«Avid
  DNxHD 220: For highest quality image when using 8-bit color sources»**; **«Avid DNxHD 145 … 145Mbps
  is the data rate for 1920 x 1080 30fps interlaced sources (60 fields). Progressive sources at 24fps
  will be 115Mbps and at 25fps will be 120Mbps.»**; **«Avid DNxHD 100 … Sub-samples the video raster
  from 1920 to 1440 or from 1280 to 960»**; **«Avid DNxHD 36: High-quality offline editing of HD
  progressive sources only.»** (Ojo: el número del nombre es la tasa a 1080i/30 —29,97—, no a 25 fps.)
- DNxHR (sucesor para >HD): **no leído en fuente de Avid**. El tema RTVE lo nombra; no ampliar.

### 7.4 AVC-Intra (Panasonic)

- AVCI, pregunta 1: **«AVC-Intra … is a professional intra-frame video codec with bit rates of 50 and
  100Mb/s, utilizing the High 10 Intra and High 422 Intra profiles of H.264 respectively.»**
  **«AVC-Intra provides high-quality 10-bit intra-frame encoding in two modes: AVC-Intra 100 … and
  AVC-Intra 50»**.
- AVCI, pregunta 4: **«With 4:2:2, 10-bit Intra-frame coding, in 1080 progressive or interlace
  systems, AVC-Intra 100 records the full 1920x1080 raster»**.
- AVCI, pregunta 2 (Intra frente a GOP largo): **«Inter-frame compression, (long GOP) is usually used
  for content delivery and packaged media»**; **«Intra frame compression processes the entire image
  within the boundaries of each video field or frame. There is zero interaction between adjacent
  frames»**.
- AVCI, pregunta 12: **«AVC-Intra is recorded as MXF»** … **«The MXF operating pattern is OP-ATOM»**;
  pregunta 13: **«AVC-Intra supports MXF metadata.»** Soporte: tarjetas **P2** (pregunta 8 y ss.).
- Nota: AVC-Intra 50 es 4:2:0 (High 10 Intra). El FAQ lo implica por el perfil pero **no lo escribe**
  con esas cifras; si se quiere «4:2:0», falta fuente literal.

### 7.5 MXF: lo que añade a RTVE

- LOC-MXF: **«Object-based file format that wraps video, audio, and other bitstreams ("essences"),
  optimized for content interchange or archiving by creators and/or distributors, and intended for
  implementation in devices ranging from cameras and video recorders to computer systems.»**
- LOC-MXF: **«most commentators say "MXF should be seen as the 'digital equivalent of
  videotape,'"»**.
- LOC-MXF: **«The central specification is SMPTE ST 377-1:2011, Material Exchange Format (MXF) --
  File Format Specification»**; OP1a = **«SMPTE ST 378:2004 (Archived 2010) … Operational Pattern 1a
  (Single Item, Single Package)»**; OP-Atom = **«SMPTE ST 390:2011 … Specialized Operational Pattern
  "Atom" (Simplified Representation of a Single Item)»**.
- LOC-MXF (código de tiempo en MXF): **«EBU … Recommendation R122-2010, Material Exchange Format -
  Timecode Implementation. This recommendation defines an encoding of source timecode into MXF
  files.»**
- LOC-MXF: **«Panasonic P2 digital video cameras can output MXF OP-Atom files»** (y el FAQ de
  AVC-Intra lo confirma, 7.4).

### 7.6 Tarjetas actuales (Z200 como ejemplo)

- Z200 p. 67: **«The unit records audio and video on CFexpress Type A memory cards (available
  separately) or SDXC memory cards (available separately) inserted in the card slots. The memory
  cards are also used for proxy recording and storing/loading settings, and when upgrading (software
  update).»**
- Z200 p. 68: **«The guaranteed operating conditions will vary depending on the [Rec Format] and
  recording settings.»** La tabla de tarjetas clasifica SDXC por **«Class 10 / U1 / U3 / VSC V10 / V30
  / V60 / V90»** y CFexpress Type A por **«VPG200 / VPG400»**.
- SDA (vía WebFetch): **«The Speed Classes defined by the SD Association are Class 2, 4, 6 and
  10.»**; **«The UHS Speed Classes … are UHS Speed Class 1 (U1) and UHS Speed Class 3 (U3).»**; **«The
  Video Speed Classes … are V6, 10, 30, 60 and 90.»**; **«Speed Class symbols with a number indicate
  minimum writing speed»**. Las cifras en MB/s de cada clase **no se leyeron**: no darlas.
- «VPG» (Video Performance Guarantee, de la CompactFlash Association): **sin fuente leída**; nombrar
  sólo como aparece en el manual.
- Extraer la tarjeta (p. 95): **«If the unit is turned off or the memory card is removed while the
  memory card is being accessed, the integrity of data on the card cannot be guaranteed. All data
  recorded on the card may be discarded. Always make sure the access indicator is green or off before
  turning off the unit or removing the memory card.»**; **«the memory card may be hot, but this does
  not indicate a problem.»**
- Formatear (p. 96): **«Formatting a memory card erases all data, including recorded video data and
  setup files.»**; **«[Full Format]: Initializes the memory card completely, including the data region
  and data management information. [Quick Format]: Initializes the data management information of
  the memory card only.»**; **«To use a memory card formatted on the unit in another device — First,
  make a backup of the card, then reformat the card in the device to be used.»**; aviso si hay
  pendiente de envío: **«A transfer target file exists.»**
- Protección (p. 31): **«(Protected) icon appears if the memory card is write-protected.»**
- Grabación en relevo (p. 98): **«When memory cards are inserted in both card slots A and B,
  recording automatically switches to the second memory card just before the remaining capacity on
  the first card reduces to zero (relay recording).»**
- Grabación simultánea (p. 153) —copia de seguridad en cámara—: **«You can record to both
  memory card A and memory card B simultaneously by setting [Simul Rec]»**; **«In 2-slot simultaneous
  recording, the generated clip will have the same clip name on both media.»**
- Avisos (p. 310): **«[Media Near Full] … Replace at the earliest convenience.»**; **«[Media
  Full] … Replace immediately.»**; **«[Media Temperature High] … The temperature of the CFexpress card
  is high. Replace the card or allow it to cool down before using it again.»**

### 7.7 Metadatos que pone el cámara (Z200)

- Clip (p. 99): **«When you stop recording, the video, audio, and accompanying data from the start to
  the end of the recording are saved as a single “clip” on a memory card.»** **«Each clip recorded by
  the unit is automatically assigned a name using the naming format set using [TC/Media] – [Clip Name
  Format]»**.
- Duración máxima de clip (p. 99): **«The maximum recording duration of a clip in XAVC S format is 13
  hours»** … **«In XAVC format (PXW-Z200 only), the maximum is 24 hours»**.
- Marcas: **«[Shot Mark1]: Adds shot mark1 to the currently recording or playing clip.»** (ídem
  Mark2); banderas de clip: **«You can add an [OK] clip flag to a clip being recorded or just
  recorded»**, y los botones **«[Clip Flag OK]» / «[Clip Flag NG]» / «[Clip Flag Keep]»**; **«The
  thumbnail screen can be displayed sorted by clip flag type»**.
- Código de tiempo y bits de usuario: ver 6.4 (**«8-digit hexadecimal number»**).
- Proxy (p. 161): **«This function allows you to simultaneously record a low-resolution proxy
  clip at the same time as recording a high-resolution original clip»**; **«The file name extension
  is “.mp4”.»**; **«The timecode is also recorded simultaneously.»**; nombre: **«the clip name recorded
  on the memory card + “S03” suffix»**; **«A proxy clip can be subdivided into chunks automatically at
  short intervals and the files can be transferred before the end of recording.»** (troceo 30 s, 1 min
  o 2 min, por defecto **«[30s]»**).
- **Sin fuente leída**: UMID (SMPTE ST 330) y metadatos de planificación de XDCAM. No afirmar.

### 7.8 Copia de seguridad, verificación e ingesta

- DPC: **«“Fixity, in the preservation sense, means the assurance that a digital file has remained
  unchanged, i.e. fixed.” (Bailey, 2014)»**; **«fixity of files can established and monitored through
  the use of checksums»**.
- DPC, para qué: **«To know that a file has been correctly received from a content owner or source
  and then transferred successfully to preservation storage»**; **«This allows a ‘chain of custody’ to
  be established between those who produce or supply the digital materials, those responsible for
  its ongoing storage, and those who need to use the digital material»**.
- DPC, algoritmos: **«There are several different checksum algorithms, e.g. MD5 and SHA-256 that can
  be used to generate checksums of increasing strength.»** **«if checksums are being used to detect
  accidental loss or damage to files, for example due to a storage failure, then MD5 is sufficient and
  has the advantage of being well supported in tools and is quick to calculate.»**
- DPC, copias múltiples: **«checksums can be used to monitor the fixity of each copy of a file and if
  one of the copies has changed then one of the other copies can be used to create a known good
  replacement»** (proceso **«known as ‘data scrubbing’»**).
- DPC, soporte original: **«Use write-blockers when working with original media»** (NDSA nivel 2);
  finalidad: **«to prevent write access to media that digital materials might be on prior to being
  copied»**. (Aplicación al cámara, nota mía: en ingesta, bloquear la tarjeta —pestaña de protección
  de la SD— antes de copiarla; es costumbre de oficio, no norma de televisión.)
- INCIBE (vía WebFetch, cotejar): la regla 3-2-1 **«se refiere a disponer siempre de tres copias de
  seguridad de un mismo tipo de información, en dos dispositivos distintos y, una de ellas,
  almacenarla en un lugar diferente a los demás»**.
- Z200 p. 96: antes de reutilizar una tarjeta en otro equipo, **«First, make a backup of the card»**.
- **Costumbre de oficio sin norma leída** (el redactor debe decirlo así): no formatear una tarjeta
  hasta confirmar la copia verificada; copiar la estructura completa de carpetas de la tarjeta, no
  sólo los ficheros de vídeo (para no perder metadatos y proxys); herramientas de copia con
  verificación por suma (xxHash, MD5). Ninguna de esas frases tiene fuente leída en esta fase.

### 7.9 Entrega de material

- **No consta** protocolo publicado de CSRTV para la entrega de material de cámara (nomenclatura,
  carpeta, formato de la casa, envío por FTP/nube). Lo que hay es fuente de fabricante:
  - Z200, envío seguro (p. 196): **«You can transfer files with encryption using FTPS in Explicit mode (FTPES)
    for the connection with the file transfer destination server.»**; **«In FTP, the contents, user
    name, and password are not encrypted. For secure data transfer, use FTPES (FTPS).»**
  - Z200: subida automática del proxy **«[Auto Upload (Proxy)]»**, con troceo (7.7).
- El Libro de estilo de CSRTV (2004) trata la entrega en cinta (ver informe del bloque B): histórico.
- Para la entrega de programa terminado hay especificaciones AMWA (LOC-MXF: **«AMWA Application
  Specification AS-11, MXF for Contribution»**); no aplican al cámara ENG y no se han leído.

---

## Tema 11 · Seguridad del equipo, transporte, montaje, verificación, mantenimiento básico y comunicación de incidencias

Hueco declarado: **mantenimiento básico** (limpieza, baterías, tarjetas, condensación,
almacenamiento), **transporte de baterías de litio** y los **mensajes de error** como base de la
comunicación de incidencias. Transporte y montaje seguro, lista de comprobación, verificación y
parte de averías ya están en RTVE.

### 11.1 Condiciones de uso y almacenamiento (Z200, pp. 9-10)

- Condensación: **«If the unit is suddenly taken from a cold to a warm location, or if ambient
  temperature suddenly rises, moisture may form on the outer surface of the unit and/or inside of the
  unit. This is known as condensation. If condensation occurs, turn off the unit and wait until the
  condensation clears before operating the unit. Operating the unit while condensation is present may
  damage the unit.»**
- Almacenamiento: **«Store in a level, ventilated place.»** Evitar: **«In excessive heat or cold
  (operating temperature range: 0 °C to 40 °C (32 °F to 104 °F)). Remember that in summer in warm
  climates the temperature inside a car with the windows closed can easily exceed 50 °C (122 °F).»**;
  **«In damp or dusty locations.»**; **«Locations where the unit may be exposed to rain»**;
  **«Locations subject to violent vibration»**; **«Near strong magnetic fields»**; **«Close to radio or
  TV transmitters producing strong electromagnetic fields»**; **«In direct sunlight or close to
  heaters for extended periods»**.
- Especificaciones (p. 335): **«Operating temperature 0 °C to 40 °C»**; **«Storage temperature −20 °C
  to +60 °C»**. (Nota: son del Z200; otra cámara tendrá otro margen. No generalizar.)
- Láser: **«Laser beams may damage the CMOS image sensor. If you shoot a scene that includes a laser
  beam, be careful not to let the laser beam be directed into the lens of the unit.»** (Útil en
  conciertos y actos: enlaza con el tema 10.)
- Píxeles del visor/pantalla: **«a functioning pixel ratio of at least 99.99%»**; los píxeles fijos
  **«are not a malfunction»**. Sensor: **«fine white flecks may be generated on the screen in rare
  cases, caused by cosmic rays, etc.»**, más visibles **«When operating at a high environmental
  temperature»** y **«When you have raised the gain»**. (Sirve para no dar parte de avería de lo que
  no lo es.)

### 11.2 Mantenimiento básico y piezas consumibles

- Z200 p. 10: **«The fan and battery are consumable parts that will need periodic replacement. When
  operating at room temperature, a normal replacement cycle will be about 5 years.»**
- Z200 p. 10: **«The battery terminal of this unit (the connector for battery packs and AC adaptors)
  is a consumable part. Power may not be supplied to the unit properly if the pins of the battery
  terminal are bent or deformed by shock or vibrations, or if they become corroded due to prolonged
  outdoor use.»**
- Z200 p. 10: **«Periodic inspections are recommended to keep the unit working properly and to
  prolong its usable lifetime.»**
- Z200, menú [Maintenance]: **«[Hours Meter] Displays the accumulated running time.»**; **«[All Reset]
  Resets settings to factory default values.»** (p. 280).
- Limpieza (SONY-A1, «On cleaning»): lente: **«Do not use a cleaning solution containing organic
  solvents, such as thinner, or benzine. When cleaning the lens surface, remove dust with a
  commercially available blower. In case of dust that sticks to the surface, wipe it off with a soft
  cloth or tissue paper slightly moistened with lens cleaning solution. Wipe in a spiral pattern from
  the center to the outside. Do not spray lens cleaning solution directly onto the lens surface.»**
  Soplador: **«Do not use a spray-type blower as doing so may cause a malfunction.»** Carcasa: **«Clean
  the product surface with a soft cloth slightly moistened with water, then wipe the surface with a
  dry cloth.»** (Es el manual de una cámara de óptica intercambiable Sony; que el redactor lo presente
  como pauta de fabricante, no como norma.)

### 11.3 Baterías: uso, carga y almacenamiento

- Z200 p. 42: **«For safety, use only the Sony battery packs and AC adaptors listed below.»**;
  **«Do not store battery packs in locations exposed to direct sunlight, flame, or high
  temperature.»**; **«Always set the power switch to the (standby) position before connecting or
  disconnecting a battery or AC adaptor.»**
- Z200 p. 43: **«Charging a battery pack while it is warm (for example, immediately after use) may not
  fully recharge the battery.»**
- SONY-A1 (notas de batería): **«We recommend charging the battery pack in an ambient temperature of
  between 10 °C and 30 °C»**; **«Battery performance decreases in low temperature environments»**
  (recomienda llevarla **«in your pocket close to your body to warm it up»** y avisa: **«If there are
  any metal objects such as keys in your pocket, be careful of causing a short-circuit.»**);
  **«Do not continuously or repeatedly charge the battery pack without using it if it is already
  fully charged or close to fully charged. Doing so may cause a deterioration in battery
  performance.»**; **«If the battery terminal is dirty … clean the battery by lightly wiping off any
  dust using a soft cloth or a cotton swab.»**; almacenamiento: **«charge the battery pack and then
  fully discharge it in the camera at least once a year before storing it. Store the battery in a
  cool, dry place after removing it from the camera.»**
- Ojo: es la nota de la batería pequeña de una cámara fotográfica Sony (ILCE-1; el modelo de batería no se ha comprobado); para baterías de
  cámara de hombro (BP-U, montura V, montura Gold) no se ha leído nota equivalente del fabricante.

### 11.4 Transporte de baterías de litio en avión (IATA 2026)

- IATA p. 1: basado en **«the 2025-2026 Edition of the ICAO Technical Instructions for the Safe
  Transport of Dangerous Goods by Air (Technical Instructions) and the 67th Edition (2026) of the IATA
  Dangerous Goods Regulations (DGR)»**; y advierte: **«The information in this document is intended
  for guidance purposes only. It should not be relied upon as a source of regulatory compliance.»**
- Vatios-hora: **«Watt-hour rating, expressed in Wh, shows the power of the lithium cell or battery,
  which is calculated by multiplying the rated capacity in ampere-hours by the nominal voltage (Wh = Ah
  x V).»** **«All lithium-ion batteries are required to have the Watt-hour rating marked on the outside
  of the battery case.»**
- Definición: **«Portable electronic device (PED) … Most of the consumer commodities can be listed as
  PED such as mobiles, laptops, cameras, radios, audio devices, watches.»**
- Repuestos: **«Spare batteries must be individually protected to prevent short circuits by placement
  in the original retail packaging or by otherwise insulating terminals, e.g. by taping over exposed
  terminals or placing each battery in a separate plastic bag or protective pouch and carried in
  carry-on baggage only.»**
- Consejo 8: **«For larger batteries (over 100 watt-hours, such as those used in larger cameras,
  drones, or power tools), check with your airline as approval may be required.»**
- Tabla 1 (p. 8), baterías de repuesto de ion-litio: **≤ 100 Wh** → cabina **«Yes²»**, facturado
  **«No»**, aprobación **«No²»**; **> 100 Wh y ≤ 160 Wh** → cabina **«Yes4»**, facturado **«No»**,
  aprobación **«Yes»**; **> 160 Wh** → **«Must be prepared and carried as cargo in accordance with the
  IATA Dangerous Goods Regulations»**. Notas: **«2. Each person is limited to a maximum of 20 spare
  batteries of any type. The operator may approve the carriage of more than 20 batteries.»**; **«4.
  Limited to a maximum of 2 spare batteries per device»**.
- Aprobación del operador: puede exigir **«additional separation between the batteries or that they
  are at a low state of charge (<25% indicated when inserted into the device)»**.
- Consejos: **«If a device is hot, smoking, or damaged, tell the crew (or airport staff)
  immediately.»**; **«Always carry phones, laptops, cameras … in your hand baggage, not in checked
  baggage.»**
- **Vigencia**: es la guía de 2026; su propio texto no fija fecha de fin (el dato de que el DGR 68.ª ed.
  entra el 1-1-2027 viene de un buscador y **no se ha leído en fuente**). Advertir al redactor de que
  la cifra se estudia «a 24-09-2026».
- Transporte por carretera (ADR) de baterías del equipo propio: **no investigado**; no afirmar nada.

### 11.5 Tarjetas: cuidado físico (SONY-A1, «Notes on memory card»)

- **«Do not remove the battery pack or the memory card, disconnect the USB cable, or turn the camera
  off while the access lamp is lit up. This may cause the data on the memory card to become
  damaged.»**; **«Be sure to back up the data for protection.»**
- **«If you repeatedly shoot and delete images for a long time, fragmentation of data in a file in the
  memory card may occur, and movie recording may be interrupted in the middle of shooting. If this
  happens, save your images to a computer or other storage location, then execute [Format] using this
  camera.»**
- **«Memory card formatted with a computer is not guaranteed to operate with the product. Be sure to
  format the memory card using this product.»**
- **«If you connect your camera to an incompatible device, you may be prompted to format the card.
  Never format the card in response to this prompt, as doing so will erase all data on the card.»**
  (**«exFAT is the file system used on SDXC memory cards or CFexpress Type A memory cards.»**)
- **«Do not expose the memory card to water. Do not strike, bend or drop the memory card.»**; **«Do not
  touch the terminal section of the memory card with your hand or a metal object.»**; **«Do not attach
  a label on the memory card itself nor on a memory card adaptor.»**; **«If the write-protect switch …
  of an SD memory card is set to the LOCK position, you cannot record or delete images.»**

### 11.6 Comunicación de incidencias: lo que dice la cámara (Z200, p. 310)

- **«If a warning/caution/operation that requires confirmation occurs on the unit, a message is
  displayed on the LCD monitor/viewfinder screen, tally lamp starts flashing, and a warning sound is
  emitted.»**
- Error de equipo: **«E + error code»** — **«Indicates an abnormality in the unit. Recording stops,
  even if [ Rec] is displayed on the screen. Turn off the unit, and check for any problem with
  connected devices, cables, or memory cards. If the error persists when the unit is turned on again,
  contact your Sony service representative.»** (Para el parte de averías, nota mía: anotar el código
  «E + …» tal cual aparece.)
- Avisos: **«[Battery Near End]»** (recargar cuanto antes), **«[Battery End]»** (**«Recording is
  disabled.»**), **«[Temperature High]»** (**«Turn off the unit and allow it to cool down»**),
  **«[Voltage Low]»** / **«[Insufficient Voltage]»**, **«[Media Near Full]»**, **«[Media Full]»**.
- **No consta** publicado el procedimiento de CSRTV para partes de avería o incidencias técnicas
  (ni en el Libro de estilo de 2004). Lo que ofrece el tema RTVE sobre el parte es de RTVE: quitar lo
  propio y declararlo como práctica general, no de Canal Sur.

---

## Lo que no se pudo confirmar (resumen para el redactor)

1. **Sony pro (`pro.sony`)** responde 403: sin fuente primaria de que XAVC-MXF se base en H.264 nivel
   5.2, ni del *XAVC H* (H.265 en MXF). Z200 y ayudas de cámaras sí confirman XAVC S (H.264), XAVC HS
   (HEVC/H.265) y XAVC S-I (Intra).
2. **Apple ProRes White Paper** no descargado: sin tasas por variante ni año de lanzamiento (el de
   LOC-PR, «Final Cut 2 (2001)», es dudoso).
3. **DNxHR**, **UMID (SMPTE ST 330)**, metadatos de planificación, **VPG** (CFexpress) y las cifras en
   MB/s de las clases de velocidad SD: no leídos.
4. **−20 dBFS de EE. UU. (SMPTE RP 155)**: no leído (sólo lo trae el tema RTVE como dato de examen).
5. **R128**: el historial dice tolerancia ±0,5 LU (2014) y el articulado 2023 no la recoge: no usar
   ±0,5 LU como vigente.
6. **INCIBE** (regla 3-2-1) y **SDA** leídos por WebFetch (resumen de modelo): cotejar la cita a ojo.
7. **Criterios de oficio** (asignación de pistas en ENG, pico de voz, no formatear sin copia
   verificada, copiar la estructura completa de la tarjeta): sin norma; decirlo como costumbre.
8. **CSRTV**: no consta publicado manual técnico de cámara, formatos de la casa, protocolo de entrega
   ni procedimiento de incidencias.
9. **Paginación del Z200**: tomada del pie de página del PDF extraído; las páginas marcadas son las
   del PDF de impresión (`print.pdf`), no las de la web.

## Ficheros tocados fuera de este informe

Copias de fuentes (sólo añadidos, nada modificado):
`fuentes/normas-tecnicas/EBU_R128-2023.{pdf,txt}`, `EBU_R68-2000.{pdf,txt}`,
`EBU_Tech3341.{pdf,txt}`, `EBU_Tech3343-2023.{pdf,txt}`,
`IATA_pasajeros-baterias-litio-2026.{pdf,txt}`, `LOC_fdd000389_ProRes422.txt`,
`LOC_fdd000013_MXF.txt`, `DPC_fixity-and-checksums.txt`;
`fuentes/fabricantes/Sony_PXW-Z200_help-guide.{pdf,txt}`, `Avid_DNxHD_white-paper-2012.{pdf,txt}`,
`Panasonic_AVC-Intra_FAQ.{pdf,txt}`, `Sony_ILCE-1_help-guide_extractos.txt`,
`Sony_ILCE-7SM3_formatos-fichero.txt`. No se han actualizado los README de esas carpetas.
