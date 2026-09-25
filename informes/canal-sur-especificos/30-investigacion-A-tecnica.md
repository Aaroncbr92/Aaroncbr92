# Puesto 30 · Operador/a Montador/a de Vídeo · Investigación del bloque A-técnica (temas 2, 3, 4, 7, 8 y 13)

Fase 1 · investigar. Fecha de trabajo: 24/25-09-2026. Sólo lo que falta para cubrir el enunciado; lo
reutilizable (común de Canal Sur, puestos 08 y 28, y RTVE) lo lee el redactor en sus ficheros.
Cada dato lleva su fuente y, entre «», la cita literal leída en esa fuente, con la fecha de lectura.
Las citas en inglés se dejan en su lengua; la traducción, si hace falta, la hace el redactor.

Nota de método: los PDF se descargaron y se pasaron a texto con `herramientas/documento.py texto`;
las páginas web se leyeron con descarga directa. Donde se dice «no confirmado», el dato se quita.

## Tema 2 · Señal de vídeo y audio (y parte común con el tema 4)

Lo que falta frente a RTVE 04/03/02 y a los temas cerrados 08-09 y 28-11: las cadencias normalizadas,
la profundidad y los niveles de cuantificación de la BT.2100, las velocidades de la interfaz SDI y
el nivel de alineación del audio digital. Primarios, blanco D65, PQ/HLG y blanco de referencia HDR
ya están en 08-09 (BT.709-6, BT.2020-2, BT.2100-3): no se repiten.

### 2.1 Cadencias (frame rate) de la UIT-R

- **UIT-R BT.709-6 (06/2015)**, parte 2 (leída 25-09-2026, PDF itu.int): «The following picture rates
  are specified: 60 Hz, 50 Hz, 30 Hz, 25 Hz and 24 Hz. For the 60, 30 and 24 Hz systems, picture rates
  having those values divided by 1.001 are also specified». «Pictures are defined for progressive (P)
  capture and interlace (I) capture. Progressive captured pictures can be transported with progressive
  (P) transport or progressive segmented frame (PsF) transport. Interlace captured pictures can be
  transported with interlace (I) transport.» La tabla de combinaciones incluye **50 progressive**,
  **25 progressive (Progressive / Segmented frame)** y **25 interlace**.
- **UIT-R BT.2020-2 (10/2015)**, tabla 2 «Picture temporal characteristics»: «Frame frequency (Hz) 120,
  120/1.001, 100, 60, 60/1.001, 50, 30, 30/1.001, 25, 24, 24/1.001»; «Scan mode Progressive». Y: «The
  choice of frame frequency may be influenced by the frequency of the mains power and the type of scene
  lighting in use».
- **UIT-R BT.2100-3 (02/2025)**, tabla 1: formatos «7 680 × 4 320 / 3 840 × 2 160 / 1 920 × 1 080»,
  «Pixel aspect ratio 1:1 (square pixels)», «Frame frequency (Hz) 120, 120/1.001,100, 60, 60/1.001,
  50, 30, 30/1.001, 25, 24, 24/1.001», «Image Format Progressive». Nota 1b: «Productions should use
  the highest resolution image format that is practical. […] producing in a higher resolution format,
  and then electronically down-sampling for distribution, yields superior quality than producing at the
  resolution used for distribution.»
  → Dato útil: en BT.2020/BT.2100 **no hay entrelazado**; el entrelazado sólo aparece en BT.709
  (25 interlace = 1080i25, lo que el oficio llama «1080i50» por campos: esa equivalencia es oficio,
  no cita).

### 2.2 Profundidad y niveles de cuantificación (BT.2100-3, tabla 9)

- «Coding format n = 10, 12 bits per component».
- Negro (narrow range): **64** en 10 bits, **256** en 12 bits; pico nominal: **940** y **3 760**.
  Full range: negro 0, pico 1 023 (10 bits) y 4 095 (12 bits).
- «The narrow range representation is in widespread use and is considered the default. The full range
  representation is newly introduced in this Recommendation and should not be used for programme
  exchange unless all parties agree.»
- Nota 9a: «Narrow range signals may extend below black (sub-blacks) and exceed the nominal peak
  values» (texto cortado ahí en la lectura; el resto habla de las interfaces).
- Submuestreo en la misma recomendación: 4:4:4 «same number of horizontal samples»; 4:2:2
  «Horizontally subsampled by a factor of two»; 4:2:0 «Horizontally and vertically subsampled by a
  factor of two with respect to the Y' or I component».
- PQ: la EOTF de la tabla 4 lleva el valor **10000** (cd/m²) como luminancia máxima de la fórmula
  (se lee «10000» en la ecuación; sin frase literal que lo diga en prosa). NOTA de la BT.2100-3: «The
  PQ specification achieves a very wide range of brightness levels for a given bit depth using a
  non-linear transfer function that is finely tuned to match the human visual system. The HLG
  specification offers a degree of compatibility with legacy displays by more closely matching the
  previously established television transfer curves.»

### 2.3 Interfaz SDI: velocidades (normas SMPTE, leídas 25-09-2026 en pub.smpte.org)

| Norma | Título en el catálogo SMPTE | Estado | Cita de velocidad |
|---|---|---|---|
| SMPTE ST 259:2008 | «Television - SDTV Digital Signal/Data - Serial Digital Interface» | stabilized | «a 10-bit serial digital interface operating at 143/270/360 Mb/s»; «nominally 270 Mb/s for 13.5-MHz luma sampling and 360 Mb/s for 18-MHz luma sampling»; niveles «Level A – 143 Mb/s, Level B – 177 Mb/s, Level C – 270 Mb/s, Level D – 360 Mb/s» |
| SMPTE ST 292-1:2018 | «Serial Digital Interface 1.5 Gb/s — 1.5 Gb/s Signal/Data Serial Interface» | stabilized | «The total data rate shall be either 1.485 Gb/s or 1.485/1.001 Gb/s» |
| SMPTE ST 424:2012 | «3 Gb/s Signal/Data Serial Interface» | stabilized | «total payload of 2.970 Gb/s or 2.970/1.001 Gb/s»; el mapeo de formatos, en «The SMPTE ST 425 set of standards» |
| SMPTE ST 2082-1:2023 | «12G-SDI — Electrical» | active | «a bit-serial data interface for the transport of 12 Gb/s [nominal] component digital signals or packetized data»; «serial data rate of 11.88 Gb/s or 11.88/1.001 Gb/s»; conector: «the 75-ohm connector defined in Annex A of IEC 61169-8» |

- Atenuación admisible: ST 259 «Typical loss amounts may be in the range of 20 dB to 30 dB at one-half
  clock frequency»; ST 424 «up to 30 dB at one-half the clock frequency»; ST 2082-1 «up to 40 dB at
  one-half the clock frequency».
- Codificación de canal (ST 424 y ST 2082-1): «The channel coding scheme shall be scrambled NRZI (non-return
  to zero inverted)».
- No confirmado (no leído): 6G-SDI (ST 2081), quad-link 3G para UHD (ST 425-5). Si el redactor quiere
  decir cómo se lleva el UHD por 4 × 3G, ha de leer la ST 425-5 o quitarlo.

### 2.4 Nivel de alineación del audio digital (EBU R 68-2000, leída 25-09-2026, tech.ebu.ch)

- «The EBU recommends that, in digital audio equipment, its Members should use coding levels for
  digital audio signals which correspond to an alignment level which is 18 dB below the maximum
  possible coding level of the digital system, irrespective of the total number of bits available.»
  Nota 2: «corresponding to a ratio of 1:8 (18.06 dB)».
- El nivel de alineación es «a sine wave signal which has a level (the alignment level) which is 9 dB
  (or 8 dB in some organizations) below the permitted maximum level of the audio programme».
- «recordings should be made with linear coding using no pre-emphasis and with a resolution of at
  least 16 bits in accordance with ITU-R Recommendation BS.646» (el PDF pone «161» por la llamada de
  nota 1 pegada al 16).
- Sonoridad (EBU R 128): los temas cerrados del puesto 28 (13-medicion-y-sonoridad, 05, 08, 09) ya la
  desarrollan con redacción vigente (R 128-2023, V5). Para el montador basta: «the Programme Loudness
  Level shall be normalised to a Target Level of −23.0 LUFS. Where attaining the Target Level is not
  achievable practically (for example, live programmes), a tolerance of ±1.0 LU is permitted»; «the
  True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during production»; «the
  audio signal shall generally be measured in its entirety, without emphasis on specific foreground
  elements such as speech, music or sound effects». Copiar del tema 28-13 mejor que citar de nuevo.

## Tema 3 · Sistemas de edición no lineal

RTVE 07 cubre Avid (offline/online, bin, timeline, AAF/EDL, Dynamic Relink) y realización 20 el
render y lo general. Falta: los otros dos sistemas que nombra el encargo (Premiere Pro y DaVinci
Resolve), los *proxies*, el conformado como operación y la exportación.

Fuentes leídas el 25-09-2026:
- Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (PDF de documents.blackmagicdesign.com,
  4 444 págs.; la página citada es la del PDF).
- Adobe, ayuda de Premiere (helpx.adobe.com/premiere/desktop/…). **helpx.adobe.com devuelve 403 a la
  descarga directa**: se leyó la copia de Wayback Machine (web.archive.org) de la fecha indicada en
  cada cita; cada página lleva su «Last updated on».

### 3.1 La estructura del programa: proyecto, *bins*, línea de tiempo

**DaVinci Resolve 21** (cap. 1, p. 13-23):
- Las páginas: «the highly focused and tightly integrated Media, Edit, Fusion, Color, Fairlight, and
  Deliver pages work together» (p. 13). [La Cut page existe también; el manual la presenta aparte.]
- Página Media: «The Media page is the primary interface for clip import, media management, and clip
  organization in DaVinci Resolve. It's central to the way DaVinci Resolve works that the source media
  used by a project is organized separately from the project data that you import and manage in the
  Edit page.» (p. 21)
- Media Pool y *bins*: «The Media Pool contains all of the video, audio, and still image media that you
  import into the current project. […] Ordinarily, all media imported into a project goes into the
  Master bin. However, your media pool can be organized into as many user-definable bins as you like
  […]. It also appears on the Edit, Fusion, Color, and Fairlight pages» (p. 23).
- Intercambio: «importing projects and exporting project exchange formats […] among applications such
  as Apple's Final Cut Pro X, Adobe's Premiere Pro, Avid's Media Composer and Pro Tools […] via robust
  support of XML, AAF, and EDL import and export workflows» (p. 13).
- Proyecto: «DaVinci Resolve projects are saved with the file extension .drp and enable you to
  exchange files with other DaVinci Resolve users» (cap. «Managing Projects and Project Libraries»).

**Premiere** (ayuda de Adobe):
- *Bins* («Add and delete bins», copia Wayback 14-11-2025): «To add a new bin, right-click on the
  Project panel and select New Bin from the context menu, or Control + / (Windows) or command + /
  (macOS).» «To delete bins, select one or more bins in the Project panel and use your keyboard's
  Delete key.»
- Secuencia («Sequence presets and settings», Last updated Aug 22, 2025; copia 05-01-2026): «The
  sequence settings must be correct when you create the sequence. Sequence settings like time base
  are locked once the sequence is created.» «Premiere Pro performs best when the settings for a
  sequence match the parameters of most of the assets used in that sequence.» Parámetros del
  material que hay que conocer: formato de grabación, «Frame aspect ratio», «Pixel aspect ratio»,
  «Frame rate», «Time base», «Fields (for example, progressive or interlaced)», códecs de vídeo y
  audio. «A single project can contain multiple sequences with different settings.» Aviso: la página
  pone «Audio sample rate (for example, 32 Hz or 48 Hz)» — errata de Adobe (son kHz): no citar esa línea.

### 3.2 *Proxies* y medios optimizados

- **Premiere** («Ingest and Proxy workflow», Last updated Jan 7, 2026; copia 18-09-2026):
  «Ingesting in Premiere refers to the process of copying and transcoding media files from your
  source storage (such as memory cards, external hard drives, or network drives) to your project's
  local storage or designated media cache location.» «Premiere verifies to ensure that there is no
  data corruption or loss while copying media.» «Proxy workflows in Premiere involve creating
  lower-resolution, lightweight copies of your high-resolution video files. These lower-resolution
  copies, known as proxy files, are used for editing instead of the original high-res files.» «When
  working with proxies, you first create proxy files, edit these proxies, and then convert to full
  resolution media when you need the full resolution files.» «You can also work with proxies that are
  created outside of Premiere (for example, proxies created using other applications, or cameras). In
  this case, you need to attach proxies to the full resolution media files». «After editing is
  complete, you can switch back to the original media for final export.» Salvedades: «The proxy
  functionality in Premiere is not compatible with the proxy functionality in After Effects.»
  «Editing audio in Adobe Audition is also not supported for proxy workflows.»
- **Resolve 21**, cap. 8 (p. 202-221):
  «Proxy Media is essentially more highly compressed (and potentially lower resolution) versions of
  your source media that are linked to your source media in DaVinci Resolve via metadata.» «this lets
  you use lower bandwidth proxy media for increased real-time effects performance and full speed
  playback while editing, while easily reverting back to more bandwidth and processor-intensive source
  media for color correction, finishing, and final output.» Resolución del proxy: «Original», «Half,
  Quarter, Eighth, or Sixteenth» o «Choose Automatically». Entrega: «By default, the Deliver page
  always reverts proxies to the original source media for final output to ensure the highest quality
  render. Checking the "Use proxy media" box […] overrides this». Aviso en línea de tiempo: «a purple
  line on your timeline indicates the original media is missing».
  Medios optimizados (distintos de los *proxies*): «Resolve automatically manages the relationship
  between source clips and the optimized media you create»; «Optimized media is not included in Media
  Management operations, nor is it included as part of Archive operations in the Project Manager.»
  Y: «Timeline Proxy Mode and Proxy Media, have no relation to each other.»

### 3.3 Conformado y reenlace (relink)

- **Resolve 21**, cap. 22 (p. 476): «Generally speaking, "conforming" a project describes the process
  of importing a project exchange file from another post-production application, and automatically
  relinking each clip in the imported timeline to the high-quality media files each clip corresponds
  to.» «you can import via the EDL, AAF, or XML project exchange formats». Preparación (p. 479):
  mover a V1 los clips no superpuestos, porque las pistas múltiples son cómodas «for offline editorial,
  [but] less convenient when you're trying to conform, grade, finish, and render»; y crear una
  «offline reference movie» para comparar tras el conformado («After project conform, you can compare
  the project as seen in the Record Viewer with the [offline reference]»).
- **Premiere**, reenlace automático («Relink offline media automatically», Last updated Apr 15, 2026;
  copia 12-05-2026): «Premiere attempts to reconnect media using two main methods: Historical path
  tracking; Automated search logic». «Standalone projects store: The current file path; Up to two
  historical paths». Manual: menú «Link Media» (dato del buscador sobre la página «Manually locate and
  relink offline media»; la copia no se pudo descargar —conexión cortada—: confirmar antes de citar).

### 3.4 Exportación

- **Premiere** («Export directly to Adobe Media Encoder», Last updated Apr 1, 2026): «Adobe Media
  Encoder lets you queue multiple exports, use custom presets, and render files without interrupting
  your editing workflow.» Vía: «File > Export > Send to Adobe Media Encoder». «Export options in
  Premiere» (Last updated Aug 18, 2026): «Direct export generates files immediately from within
  Premiere»; «Exporting through Adobe Media Encoder sends your asset to the Media Encoder queue, where
  you can continue editing in Premiere while the file is being rendered.» Proyecto para otros
  sistemas: «Premiere supports exporting to AAF, which can be imported into various third-party
  editing systems»; hay también EDL y Final Cut Pro XML (títulos de páginas de la misma ayuda:
  «Export a project as an EDL file», «Export a project as a Final Cut Pro XML file», «Export OMF files
  for Pro Tools»).
- **Resolve 21**, página Deliver (cap. «Rendering Media», p. 4196): dos modos. «Single Clip […] all
  clips in the session are output together, as a single media file […] to a single MXF or QuickTime
  file, or as a single collection of image sequences»; «Individual clips […] each clip is rendered as
  an individual media file»; en este modo «The timecode written to each clip is cloned from the
  original source media, making it easy to reconform media for projects being passed between DaVinci
  Resolve and NLEs.» Cola: «click the Add to Render Queue button».
- Entrega IMF desde Resolve (p. 4219): «a native IMF option that lets you export to the SMPTE ST.2067
  Interoperable Master Format (IMF) for tapeless deliverables to networks and distributors»; «wrapping
  a timeline's different video and audio tracks (media essences) and subtitle tracks (data essences)
  into a "composition" within the Material eXchange Format (MXF)». (Studio Version Only.)

### 3.5 No confirmado en el tema 3
- Flujo de *proxies* de Avid Media Composer (no se leyó documentación de Avid en esta fase; RTVE 07
  no lo trae). Si el redactor lo quiere, ha de leerlo en la ayuda de Avid; si no, se omite.
- Nombres de pantallas/versiones de Premiere 2026 más allá de lo citado.

## Tema 4 · Formatos de vídeo y audio: lo que falta (HDR operativo, SDI, estándares de entrega)

Resolución, cadencias, profundidad, submuestreo y SDI: ver §§ 2.1-2.3 (valen para el tema 4). Códecs,
contenedores, tasas y *proxy*: tema cerrado 08-07 y RTVE. Aquí sólo lo que falta.

### 4.1 HDR en producción: niveles (UIT-R Informe BT.2408-9, 03/2026, leído 25-09-2026)

Edición vigente: la página de la UIT lista las ediciones 1 a 9; la 9 «Approved in 2026-03».
(El tema cerrado 08-09 declaraba no haber leído la BT.2408: esto lo completa.)

- «HDR Reference White, is defined in this Report as the nominal signal level obtained from an HDR
  camera and a 100% reflectance white card resulting in a nominal luminance of 203 cd/m2 on a PQ
  display or on an HLG display that has a nominal peak luminance capability of 1 000 cd/m2.»
- Grafismo: «Graphics White is defined within the scope of this Report as the equivalent in the
  graphics domain of a 100% reflectance white card […]. It therefore has the same signal level as HDR
  Reference White, and graphics should be inserted based on this level.»
- Tabla 1 «Nominal levels for PQ and HLG production» (luminancia cd/m² · %PQ · %HLG):
  | Referencia | cd/m² | %PQ | %HLG |
  |---|---|---|---|
  | Grey Card (18%) | 26 | 38 | 38 |
  | Greyscale Chart Max (83%) | 162 | 56 | 71 |
  | Greyscale Chart Max (90%) | 179 | 57 | 73 |
  | HDR Reference White (100%), también diffuse white y Graphics White | 203 | 58 | 75 |
  Notas: «(1) The actual signal levels for an 18% grey card may differ significantly where camera
  painting controls have been applied.» «(2) The signal level of 'HDR Reference White' is not directly
  related to the signal level of SDR 'peak white'.»
- «For PQ, the nominal luminance values are consistent on PQ reference displays. For HLG, the nominal
  luminance values will differ from those in Table 1 when the display's peak luminance is lower or
  higher than 1 000 cd/m2. The nominal signal levels in Table 1 do not change.»
- El índice del Informe tiene apartados sobre «SDR-HDR and HDR-SDR format conversion», «SDR-HDR-SDR
  'Round-Tripping'» y «Look-up Table (LUT) conversions in HDR television production» (sólo títulos
  leídos; si el redactor quiere contenido, ha de leerlos).

### 4.2 Metadatos HDR y curva PQ en SMPTE (catálogo pub.smpte.org, leído 25-09-2026)

- «ST 2084, High Dynamic Range Electro-Optical Transfer Function of Mastering Reference Displays» —
  publicación 2014-08-16, estado «stabilized».
- «ST 2086, Mastering Display Color Volume Metadata Supporting High Luminance and Wide Color Gamut
  Images» — publicaciones 2014-10-13 y 2018-04-09, «stabilized».
- No confirmado: definición de «HDR10», «HDR10+» y «Dolby Vision» (no hay fuente normativa leída;
  si se nombran, sólo como marcas/perfiles comerciales y sin cifras).

### 4.3 Estándares de entrega

- **MXF**: «ST 377-1, Material Exchange Format (MXF) — File Format Specification», activa, última
  publicación 2019-11-28 (catálogo SMPTE). RTVE 05 trae los perfiles operacionales.
- **AMWA AS-11** (amwa.tv/as-11, leído 25-09-2026): «The AMWA AS-11 family of Specifications define
  constrained media file formats (based on MXF) for the delivery of finished media assets to a
  broadcaster or publisher. Each Specification is developed for a particular business purpose.» «The
  AS-11 UK DPP HD & SD Specifications are well established for the delivery of finished programs to
  media companies within the UK.» Ampliaciones: «Meet the requirements of broadcasters in the Nordic
  countries, Australia and New Zealand, as well as broadcasters represented by the North American
  Broadcasters Association (NABA) and the DPP»; «Add support for UHD and HDR content»; «Cater for
  delivery of short-form content in addition to full-length programs (such as commercials,
  promotions, and music videos)».
- **IMF (SMPTE ST 2067)** (smpte.org/standards/st2067, leído 25-09-2026): «IMF is a file-based media
  format that simplifies the delivery and storage of audio-visual masters intended for multiple
  territories and platforms.» «IMF is a file-based framework for the exchange and processing of
  multiple content versions (airline edits, special edition, languages…) of the same high-quality
  finished work […]. Provisions common to all IMF Applications are specified in SMPTE ST 2067-2 ("Core
  Constraints")». CPL: «The Composition Playlist is a representation of a single version of a finished
  IMF composition […]. It contains the information necessary to describe the composition and
  synchronize its underlying essence; e.g., for playout or transcoding.» OPL: «An Output Profile List
  (OPL) defines the transformation of selected virtual tracks of a single Interoperable Master Format
  (IMF) Composition into deliverables appropriate for downstream distribution channels.» Aplicación
  para radiodifusión: «RDD 59-1 Application DPP (ProRes)», desarrollada por «the DPP and the North
  American Broadcasters Association (NABA)», «based on the image formats referred to in ITU-R BT.2100».
  ST 2067-2: publicaciones 2013, 2016 y 2020-04-07, «active».
- **Sonoridad de entrega**: EBU R 128-2023, ver § 2.4 (−23,0 LUFS; −1 dBTP).
- No confirmado: que Canal Sur/RTVA exija AS-11, IMF o una ficha técnica de entrega concreta. Nada
  publicado leído lo dice → «Lo que este tema no da».

### 4.4 SDI/IP
- SDI: § 2.3. IP: RTVE ing-tec-teleco/07 (ST 2110/2022) y 28-11 (AES67/ST 2110-30) lo cubren. Estado
  de la ST 2110-10 en el catálogo SMPTE: «active», publicaciones 2017-09-18 y 2022-03-28 (título
  «Professional Media Over Managed IP Networks — System Timing and Definitions»). Si RTVE 07 cita la
  edición de 2017, actualizar a 2022.

## Tema 7 · Postproducción: color, efectos, transiciones y limpieza de audio (subtítulos: no)

RTVE 02 (colorimetría, LUT), 09 (incrustaciones, grafismo), 03 (EQ, *ducking*) y realización 20
(etalonaje) cubren la base; 08-09 cubre los monitores de forma de onda/vectorscopio desde la cámara.
Falta: los controles de la corrección primaria/secundaria, los monitores en la sala de postproducción,
las transiciones y sus «colas» (*handles*) y las herramientas de limpieza de audio. Fuentes: *DaVinci
Resolve 21 Reference Manual* (PDF, leído 25-09-2026) y ayuda de Premiere (copias Wayback indicadas).

### 7.1 Corrección de color primaria y secundaria (Resolve 21)
- Primaria (cap. 125, p. 3087-3088): «Color balance wheels let you adjust all three color channels at
  once, altering the color temperature of the scene at specific ranges of tonal detail referred to as
  lift, gamma, and gain.» «All of these controls let you adjust the color tone of the shadows,
  midtones, and highlights independently from each other.» «the Master Lift, Gamma, and Gain wheels
  work together to let you alter image contrast in different ways: deepening shadows, lightening
  highlights, and brightening or darkening the midtones in between».
- Rangos (cap. 131, p. 3202-3203): «three overlapping tonal ranges referred to as Lift, Gamma, and
  Gain»; «These tonal ranges are defined by image lightness, on a scale where 0 is absolute black and
  1023 is absolute white.» Temperatura y matiz: «Temp: A specifically constrained Gain color balance
  adjustment»; «Raising this parameter performs a Gain color balance adjustment toward orange»; «Tint
  […] toward magenta […] toward green».
- Secundaria (cap. 125, p. 3089-3090): ventanas para aislar una zona («surrounding a specific part of
  the image with a window, which lets you restrict specific adjustments made to the inside and outside
  of the window's shape»); «HSL Qualification is effectively a chroma keyer that lets you sample the
  image to create a key that's used to define where to apply a specific correction.» «memory color»:
  «people have finely tuned expectations for the hues of particular subjects, such as flesh tone,
  foliage greens, and sky blues».
- LUT (cap. «Using LUTs», p. 3544-3545): «LUTs are simply files, similar to plugins but far more focused
  and with no user interface, that specify image processing operations. […] The traditional approach is
  to use a 1D table or 3D "cube" of pre-calculated values to perform an image color transform.» «The
  .cube format can be used as either a simple 33x33x33 3D LUT, or as a shaper LUT». «when a 3D LUT is fed
  values that are outside of the range that LUT is designed to handle, the out-of-range data will be
  clipped.»

### 7.2 Monitores de señal en la corrección (Resolve 21, cap. 127, p. 3150-3152)
- «There are five available video scopes» [índice del capítulo: «Waveform Monitor», «Parade»,
  «Vectorscope», «Histogram (RGB/YRGB parade histogram)», «CIE Chromaticity Scope»; sólo los tres
  primeros leídos al detalle].
- Waveform: «Overlays waveform analyses of the Y (luma/luminance), CBCR […], or RGB (red, green, and
  blue) channels over one another so that you can see how they align.»
- Parade: «shows separate waveforms side by side that analyze the strength of individual video signal
  components. The Parade scope can be set to analyze RGB, YRGB, and Y'CBCR.» Sirve para comparar
  altas luces, sombras y medios tonos «for the purposes of identifying color casts and performing
  scene-by-scene correction». «Tall parade graphs indicate a wide contrast ratio, while short parade
  graphs indicate a narrow contrast ratio.»
- Vectorscope: «Measures the overall range of hue and saturation within an image»; «75 percent color
  bar targets indicating the angle of each of the primary and secondary colors around the edge of the
  graph, and an optional skin tone reference graticule (otherwise known as the In-phase reference)»;
  «less saturated colors remain closer to the center of the vectorscope, which represents 0
  saturation»; si el centro del gráfico no está centrado, «color imbalance».
- En HDR (p. 3147): «If you are working in a non-DaVinci Resolve Color managed workflow and activate the
  HDR (ST.2084/HLG) scopes, the waveform will always reflect HDR levels, even if you've manually
  selected the output color space as Rec.709, and thus not be 100% accurate.»
- Grafismo en HDR: nivel de inserción = HDR Reference White (75 % HLG / 58 % PQ), § 4.1.

### 7.3 Transiciones y colas (handles)
- Premiere («Transitions overview», Last updated Jan 7, 2026; copia 16-09-2026): «A transition is an
  effect added between pieces of media to create an animated link between them.» «By default, placing
  one clip next to another in the Timeline panel results in a cut, where the last frame of one clip is
  followed by the first frame of the next.» «Before you apply a transition, trim the clips. Then, apply
  the transition. The more you trim, the more availability of frames you can use in the transition.»
  Consejo: «Trim at least 15 frames off of each clip for a centered 1:00 transition.» [el «1:00» es un
  segundo a 30 fps: la cifra de 15 cuadros es de Adobe; a 25 fps serían 12-13, cálculo propio, no citar].
- Resolve 21 («Using Transitions», p. 1193-1197): «Transitions provide another way of bridging the change
  from one clip to another, and are often used to indicate a change in time or location when changing
  scenes.» Duración por defecto: «which defaults to one second, or however long the overlapping handles
  of the selected edit point allow.» Sin colas suficientes, el programa ofrece «Trim Clips», «Skip Clips»
  o «Cancel». Estilos de fundido: «Video: A simple linear dissolve; the outgoing clip fades out as the
  incoming clip fades in.» «Film: A logarithmic dissolve, simulating film dissolves».

### 7.4 Limpieza de audio (Resolve 21, cap. 181 «Fairlight FX»; Premiere «Essential Sound»)
- Noise Reduction (p. 4121-4122): «A repair plugin designed to reduce a wide variety of noise in all
  kinds of recordings.» «There are three default presets: De-Hiss, De-Rumble, and De-Rumble and Hiss.»
  «Listen to Noise Only […] very useful to determine if too much signal is being removed». «Threshold
  (in dB): Relates to the signal-to-noise ratio (SNR) in the source recording. Recordings with a poor
  signal-to-noise ratio will require a higher threshold value». «Sensitivity: Higher sensitivity values
  […] more noise will be removed, but more of the dialogue you want to keep may be affected.»
- De-Hummer (p. 4102): «Eliminates hum noise that often stems from electrical interference with audio
  equipment due to improper cabling or grounding. Typically 50 or 60 cycle hum is a harmonic noise,
  consisting of a fundamental frequency and subsequent partial harmonics».
- De-Esser (p. 4101): «designed to reduce excessive sibilance, such as hissing "s" sounds or sharp "ts"
  sounds, in dialogue or vocals.»
- Dialogue Leveler (p. 4091): «analyzes source material to detect dialogue and then "rides down" louder
  areas, "lifts up" softer areas, and lowers background sounds that are not dialogue.»
- Ducker (p. 4094): «a common use of "ducking" is automatically lowering a music or sound effects bed
  so that dialogue or a VO track can be heard more prominently in a mix. This is achieved without
  compressing the incoming signals.»
- Voice Isolation (p. 4096, «Studio Version Only»): «uses an AI model trained for any type of human
  voice»; «Values between 70 and 80 work well for natural results».
- Premiere, Essential Sound («Audio editing with Essential Sound panel», Last updated Jan 7, 2026;
  copia 26-08-2026): tipos «Dialogue, Music, SFX, and Ambience»; para diálogo, «unifying the different
  recordings to a common loudness, reducing background noise, and adding compression and EQ».
- Sonoridad final: EBU R 128 (§ 2.4).

## Tema 8 · Ingesta, digitalización, transferencia, verificación, copias, metadatos y archivo

Tema cerrado 08-07 (ingesta de tarjeta, MD5, 3-2-1, RAID, LTO sin cifras) y RTVE 05/01 (MXF, LTO, RAID)
cubren la base. Falta: la digitalización desde cinta, la verificación con más algoritmos que el MD5, la
norma de metadatos del sector (EBUCore/Dublin Core), el modelo de archivo (OAIS) y cifras vigentes de
la LTO y la LTFS.

### 8.1 Digitalización desde cinta (Resolve 21, cap. 24 «Ingesting From Tape», p. 558-562)
- «DaVinci Resolve is capable of capturing media from tape using a compatible video input device, such
  as a Blackmagic Design UltraStudio or DeckLink card. Device control is supported.»
- «you can use the Media page in Capture mode to capture from any device-controllable deck via a
  compatible video interface.» Se captura con metadatos: «the Audio panel is replaced by a dedicated
  set of capture metadata and controls to help you track the resulting clips».
- Tres métodos: «Using Capture Now», «Logging and Capturing Individual Clips» / «Multiple Clips» y
  «Batch Capture Via EDL» (índice); ajustes previos mínimos: «"Video Capture and Playback," "Capture
  Clips Saved to," and Apply Reel Name to"»; «media can be ingested as QuickTime Movies or DPX image
  sequences.»
- La ingesta de señal en directo (agencia, satélite) la trae RTVE ing-tec-teleco/10.

### 8.2 Copia verificada: sumas de comprobación (Resolve 21, cap. 17, p. 373-374, «Clone Tool»)
- «the Clone Tool in the Media page lets you safely and accurately copy media from SD cards, SSDs, or
  disk drives, to multiple destinations, with a checksum report (based on a choice of six checksum
  options) written to the root of each destination volume that verifies the absolute accuracy of the
  duplicate media». Antes de nada: «clone all camera original media onto a safe set of backup volumes,
  for redundancy in case any one volume fails. Additionally, you should consider cloning all media to
  an off-site backup as well.»
- «Each option is a tradeoff between the speed of your file copy operation and the security of the
  verification process.» Opciones:
  - «None: Disables data verification, sacrificing safety for speed.»
  - «File Size: Fast, but minimal data verification. […] minimally collision resistant.»
  - «CRC 32: Faster than MD5, but less secure. An error-detecting code rather than the hash […]
    significantly less collision resistant.»
  - «MD5: This is the default setting. […] A hash function generates a 128-bit value that's unique to a
    particular file; Data integrity is checked by comparing the hash value generated by the original
    file to that generated by the copied file.»
  - «SHA 256, SHA 512: Slower, but more secure. SHA is a more collision resistant hash function than
    MD5».
  - «XXHASH64: This is by far the fastest checksum method and also provides good collision protection.»
  («Collision resistance» se define ahí mismo: si dos ficheros distintos pueden dar por casualidad el
  mismo valor de comparación.)
- Premiere también verifica en su ingesta: «Premiere verifies to ensure that there is no data
  corruption or loss while copying media» (§ 3.2). No se leyó qué algoritmo usa: no afirmarlo.

### 8.3 Metadatos: EBUCore (EBU Tech 3293, v. 1.10, abril 2020; PDF tech.ebu.ch leído 25-09-2026)
- «EBUCore has been designed to describe audio, video and other resources for a wide range of
  broadcasting applications including archives, exchange and production». «EBUCore is based on the
  Dublin Core to maximise interoperability with the community of Dublin Core users such as the European
  Digital Library 'Europeana'.»
- «Metadata is the glue between production operations particularly when moving towards Service
  Oriented Architecture and file-based production. Documenting audiovisual resources with EBUCore
  information is a minimum requirement».
- «This specification addresses the creation, management, and preservation of audiovisual material.»
  «EBUCore is a collection of basic descriptive and technical/structural metadata elements used to
  describe audiovisual content as an extension of the Dublin Core.» «EBUCore is the Dublin Core for
  media.» «EBUCore is fully compatible with IMF in its different representation formats».
- Vigencia: el PDF descargado del enlace estable de la EBU es la v. 1.10 (2020). No se confirmó si hay
  una versión posterior en la web de la EBU (la página de publicación no dio texto legible): el
  redactor dirá «versión 1.10» sin afirmar que sea la última, o lo comprueba.
- SMPTE RP 210 «Metadata Element Dictionary»: el catálogo SMPTE la marca «withdrawn» (versiones 2007
  y 2012). No citarla como vigente.

### 8.4 Archivo: el modelo OAIS (CCSDS 650.0-M-3, «Magenta Book», diciembre 2024; PDF public.ccsds.org)
- Naturaleza: «The purpose of this document is to define the CCSDS and International Organization for
  Standardization (ISO) Reference Model for an Open Archival Information System (OAIS).» [La edición
  ISO equivalente (ISO 14721) y su año vigente no se confirmaron: citar el documento CCSDS.]
- «An OAIS is an Archive system consisting of hardware, software, information, and policy-based
  processes and procedures put in place and operated by an organization and its staff. The
  organization has accepted the responsibility to preserve information and make it available for a
  Designated Community.»
- Alcance: «a full range of archival information preservation functions including ingest, archival
  storage, data management, access, and dissemination. It also addresses the migration of digital
  information to new media and forms».
- Paquetes: «Submission Information Package (SIP): An Information Package that is delivered by the
  Producer to the OAIS»; «Archival Information Package (AIP): An Information Package, consisting of the
  Content Information and the associated Preservation Description Information (PDI), which is
  preserved within an OAIS»; «Dissemination Information Package (DIP): An Information Package, derived
  from one or more AIPs, and sent by Archives to the Consumer in response to a request».
- «Fixity Information: The information which documents the mechanisms that ensure that the Content Data
  Object has not been altered in an undocumented manner.» (enlaza con las sumas de § 8.2).
- «Long Term: A period of time long enough for there to be concern about the impacts of changing
  technologies, including support for new media and data formats».
- Entidades funcionales: «six functional entities» (§ 4.2.2); por los rótulos de § 4.2.3: Ingest,
  Archival Storage, Data Management, Administration, Preservation Planning y Access.

### 8.5 LTO y LTFS (lto.org, leído 25-09-2026)
- Roadmap (lto.org/roadmap; lectura con resumen automático, citas a confirmar al pie de la letra):
  «LTO technology is currently in its 10th generation»; «LTO-10 specifications support tape cartridge
  storage with a compressed capacity of up to 100 TB», con la nota «Assuming a 2.5:1 compression»;
  «data transfer rates of up to 1200 MB/s»; «The 10th generation of LTO Ultrium tape drives does not
  support backwards compatibility due to a redesign of the drive head to eliminate the need for
  initialization.» La página no da la capacidad nativa en texto: 100 / 2,5 = 40 TB es cálculo, no cita.
  (La descarga directa con curl devolvió 202 vacío; se leyó con WebFetch.)
- LTFS (lto.org/linear-tape-file-system, descarga directa): «The Linear Tape File System (LTFS) makes it
  easy to quickly and precisely locate and retrieve any item of data stored on an LTO Ultrium tape
  cartridge.» «[it] is included with all generations since LTO-5». «LTFS partitioning allows a portion
  of the tape to be reserved for indexing, which tells the drive precisely where in the tape a file is
  stored. The second partition holds the actual file.» «allows for drag-and-drop capabilities».

## Tema 13 · Automatización, plantillas, MAM/PAM, newsroom y flujos integrados

RTVE ing-tec-teleco/10 y ing-sup-teleco/14 dan el flujo ingesta-gestión-edición-emisión y nombran
NRCS y MOS, pero sin fuente primaria. Falta: el protocolo MOS en su fuente, qué es un PAM frente a un
MAM en documentación de fabricante, y ejemplos documentados de plantillas y automatización.

### 13.1 El protocolo MOS (mosprotocol.com, leído 25-09-2026)
- Definición (portada): «Media Object Server Communications Protocol (MOS): An evolving protocol for
  communications between Newsroom Computer Systems (NCS) and Media Object Servers (MOS) such as Video
  Servers, Audio Servers, Still Stores, and Character Generators. This protocol is supported and
  developed through cooperative collaboration among equipment vendors, software vendors and end users.»
  [Ojo a la sigla: la fuente dice **NCS**; RTVE usa **NRCS**, y Avid también dice «newsroom computer
  system (NRCS)». Las dos formas constan.]
- Versiones vigentes (página «Current Versions»): «MOS Version 4.0 was published on June 7th, 2019.»
  («Secure Web Sockets»); «MOS Version 2.8.5 was published on September 7, 2017.» («Socket»); «MOS
  Version 3.8.4 was published on February 11, 2011.» («Web Services»).
- FAQ: «MOS is short for Media Object Server Communication Protocol. The MOS Protocol is intended to be
  a global industry solution to the problem of "How do I get my brand-X computer system to communicate
  with my brand-Y media server?"» Mensajes que intercambia: «Descriptive Data for Media Objects. The MOS
  "pushes" descriptive information and pointers to the NCS as objects are created, modified, or
  deleted in the MOS»; «Playlist Exchange. The NCS can build and transfer playlist information to the
  MOS. This allows the NCS to control the sequence that media objects are played or presented by the
  MOS»; «Status Exchange. The MOS can inform the NCS of the status of specific clips or the MOS system
  in general. The NCS can notify the MOS of the status of specific playlist items or running orders.»
- «A Media Object Server (MOS) is any device capable of storing Media Objects.» Objetos: «CGs (Character
  Generator Objects), Audio, Still Store, Video».
- Reparto: «the Newsroom Computer System is responsible for the creation, modification, and deletion
  of editorial information, including playlists.» «the Media Object Server is responsible for the
  creation, modification, and deletion of media objects and their associated meta-data.»
- Origen: «The first meeting of the group was held in Orlando, Florida during the late summer of 1998
  at the AP's ENPS developer's conference»; «As of 2021 more than 150 companies participate».
- Salvedad importante (no es norma oficial): «The protocol will be presented to appropriate standards
  bodies at a later date. […] our work should not be slowed nor the implementation of our work
  predicated on the official "blessing" of a standards body.» Objetivos: «Common implementation of the
  protocol will be over a TCP/IP network via socket communication»; «Messages will make use of a tagged
  text unicode format»; «Each new version of the protocol will be a "super set" of the previous
  version». → El redactor no debe llamarlo «norma» ni atribuirlo a SMPTE/EBU.

### 13.2 PAM, MAM y NRCS en documentación de fabricante (Avid, avid.com, leído 25-09-2026)
Fuente de fabricante, no norma: se cita como ejemplo de producto, no como definición oficial. No se
halló definición normalizada (UIT/EBU/SMPTE) de «PAM» ni de «MAM»: las definiciones de blogs de
proveedores encontradas no se usan. Las páginas avid.com/solutions/production-asset-management y
/media-asset-management devolvieron 403.
- MediaCentral | Newsroom Management (/products/mediacentral/mediacentral-newsroom-management): «is the
  newsroom computer system (NRCS) you need to break stories on-air faster»; «Build rundowns, adjust
  timing, go live and make real-time changes—even on-air»; «Streamline your control room operations by
  integrating your rundown with studio automation, teleprompters, graphics, and video playout servers.»
  (Producto también llamado «iNEWS» en la misma página.)
- MediaCentral | Production Management (/products/mediacentral/mediacentral-production-management) — la
  capa de producción (lo que el oficio llama PAM): «Take control of your valuable media assets, tracking
  them from ingest to archive and every step in-between. From single resolution to multi-resolution»;
  «From journalists working on news packages to researchers putting together roughcuts to craft editors
  delivering the final edit, scale up to hundreds of users»; «integrated media services such as
  transcoding, archiving, restoring, and more to automate manual processes»; «Production Management is
  driven by Avid NEXIS shared storage»; «system and user generated metadata for ultra-fast searching
  across connected clients such as Media Composer, Adobe Premiere Pro and the web-based MediaCentral |
  Cloud UX.»
- MediaCentral | Asset Management: sólo por el resultado del buscador (no leído en la página): «integrated
  management of finished media […] orchestration and archive management tools». Confirmar o quitar.
- Distinción PAM (material en producción) / MAM (material terminado y archivo): es costumbre de oficio;
  la página de Avid la sugiere por el nombre de los módulos, pero no la define. Decirlo como oficio.

### 13.3 Plantillas y automatización en el sistema de edición (Resolve 21)
- Plantillas de rótulos (p. 1215): «Fusion Titles: A variety of pre-built title templates assembled in
  Fusion. DaVinci Resolve comes with a library of pre-assembled Fusion titles, but you can also create
  your own to appear in this category of the Effects browser.» «Text+: […] An advanced title generator
  […] but all title text shares a single style.»
- Variables de metadatos (cap. 15, p. 345): «you can use "metadata variables" that you can add into
  supported text fields that let you reference other metadata for that clip»; «can be used to
  procedurally add metadata to several functions»; p. ej. «Clip names: You can use variables in the
  Clip Name column of the Media Pool […] to use each clip's metadata to generate a more readable and
  useful display name.»
- Integraciones (p. 4418, «Studio Version Only»): «DaVinci Resolve allows third parties to create their
  own custom interface plugins using scripting languages»; «Users can write their own Workflow
  Integration Plugin (an Electron app), using Resolve Javascript's API, and Python or Lua scripts.»
- Cola de render y *presets* (tema 3, § 3.4) y Media Encoder (cola con *presets*) son la otra
  automatización documentada. Plantillas de grafismo de Premiere (.mogrt) y carpetas vigiladas de Media
  Encoder: **no leídas** (Adobe y Wayback cortaron la conexión); no afirmar nada de ellas sin leerlas.

### 13.4 No confirmado en el tema 13
- Qué NRCS, MAM o servidor de emisión usa CSRTV: nada publicado leído. → «Lo que este tema no da».
- Definición normalizada de PAM/MAM (ninguna encontrada).

## Avisos para el redactor y el verificador

1. **Fuentes guardadas** para la verificación en `fuentes/canal-sur/montador/`: UIT (BT.709-6,
   BT.2020-2, BT.2100-3, Informe BT.2408-9), EBU (R 68, R 128-2023, Tech 3293 v1.10), SMPTE (ST 259:2008,
   ST 292-1:2018, ST 424:2012, ST 2082-1:2023 y fichas del catálogo de ST 2084, 2086, 377-1, 2067-2,
   2110-10 y RP 210), CCSDS 650.0-M-3 (OAIS), extractos de texto del manual de DaVinci Resolve 21 (el
   PDF entero pesa 187 MB y no se guarda; cada extracto lleva las marcas `[[pNNNN]]` de página) y texto
   de las páginas web leídas (Adobe vía Wayback, AMWA, SMPTE IMF, LTO/LTFS, MOS, Avid). La página LTO
   «roadmap» no se guardó (sólo se leyó con WebFetch).
2. **Discrepancias con lo reutilizable**:
   - El tema cerrado 08-09 dice que el nivel HLG del blanco de referencia «está en el Informe UIT-R
     BT.2408» sin leerlo: aquí está leído (75 % HLG, 58 % PQ, 203 cd/m²; BT.2408-9, 03/2026).
   - Sigla del sistema de redacción: MOS dice «NCS»; RTVE y Avid, «NRCS». Presentar las dos.
   - MOS no es norma de un organismo de normalización (lo dice su propia FAQ).
   - SMPTE RP 210 está retirada; ST 2110-10 tiene edición de 2022.
   - Adobe escribe «32 Hz or 48 Hz» por kHz en la página de secuencias: no copiar.
3. **Fuera del alcance de esta fase y no confirmado**: 6G-SDI (ST 2081) y quad-link (ST 425-5);
   HDR10/HDR10+/Dolby Vision; proxies de Avid; plantillas .mogrt y carpetas vigiladas de Adobe; capacidad
   nativa de la LTO-10; edición ISO vigente de la OAIS (ISO 14721); versión posterior de EBUCore;
   sistemas concretos de CSRTV (NRCS, MAM, servidores, ficha de entrega). Todo esto va a «Lo que este
   tema no da» o se lee antes de escribirlo.
4. **Tema 2 y tema 4 comparten** §§ 2.1-2.3; el redactor decide dónde va cada dato para no duplicar
   (sugerencia: cadencias, cuantificación y audio en el 2; SDI, HDR operativo y entrega en el 4).

Ficheros tocados en esta fase: este informe y la carpeta nueva `fuentes/canal-sur/montador/`.
