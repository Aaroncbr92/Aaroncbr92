# Esquema · Tema 11 del específico de Producción (Asistencia) · Medios de transmisión de señal

**Siglas**: el periodismo electrónico digital por satélite (**DSNG**, *digital satellite news
gathering*); la difusión de vídeo digital (**DVB**); la fibra hasta el edificio (**FTTB**), hasta la
acometida (**FTTC**) y hasta la vivienda (**FTTH**); el protocolo de internet (**IP**); la órbita
baja (**LEO**) y la media (**MEO**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**); y
la Unión Internacional de Telecomunicaciones (**UIT**).

Telegrama. **Cada línea lleva delante de dónde sale**: `[LGT]` = Ley 11/2022, General de
Telecomunicaciones · `[TDT]` = Plan Técnico Nacional de la TDT, Real Decreto 391/2019 ·
`[LGCA]` = Ley 13/2022, General de Comunicación Audiovisual · `[S.673]` = Recomendación UIT-R
S.673-2 (03/2002) · `[SNG]` = Recomendación UIT-R SNG.770-2 (01/2012) · `[G.984]` = Recomendación
UIT-T G.984.1 (03/2003) · `[SMPTE]` = índice oficial de la familia ST 2110 · `[ficha]` = ficha de
LiveU, leída el 02/09/2026 · `[uso]` = plantilla oficial, **sin norma leída**.

**Siglas**: la Unión Internacional de Telecomunicaciones (**UIT**).

**Cabecera.** Enunciado **sin norma**: «MEDIOS DE TRANSMISIÓN DE SEÑAL, ENVIO DE IMÁGENES Y
COMUNICACIONES» · **10 preguntas**, la **tercera materia** del bloque · **7 con fuente detrás**,
**3 sólo con la plantilla** —streaming, señal Pool y los datos de acceso al satélite—.

<!-- indice -->

## Índice

- [Ancho de banda](#ancho-de-banda)
- [Fibra: FTTH y familia](#fibra-ftth-y-familia)
- [Órbita geoestacionaria](#órbita-geoestacionaria)
- [Acceso a una señal por satélite](#acceso-a-una-señal-por-satélite)
- [DSNG](#dsng)
- [SMPTE ST 2110](#smpte-st-2110)
- [La mochila LU300S](#la-mochila-lu300s)
- [DVB y la televisión digital terrestre](#dvb-y-la-televisión-digital-terrestre)
- [Streaming y señal Pool](#streaming-y-señal-pool)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Ancho de banda

- `[uso]` · **Margen de frecuencias que deja pasar un canal** → **LIMITA LA VELOCIDAD DE PROCESADO
  Y TRANSMISIÓN**. Es la respuesta.
- **Falsos**: velocidad de **grabación** (eso es soporte y códec) · «regula los megahercios» (la
  anchura **se mide** en hercios, no los regula) · **colorimetría** (nada que ver).
- `[LGT]` · **Red de ALTA capacidad** = «capaz de prestar servicios de acceso de **banda ancha a
  velocidades de al menos 30 Mbps**». **La ley define la banda ancha por la velocidad.**

## Fibra: FTTH y familia

- `[G.984]` · **FTTH = *fibre to the home*, FIBRA HASTA LA VIVIENDA.** Es la respuesta.
- `[G.984]` · La familia, ordenada de más a menos fibra: **FTTH** vivienda → **FTTB** *building*,
  edificio → **FTTC** *curb*, acometida → **FTTCab** *cabinet*, armario de calle.
- **Falsos del examen**: *Fibrescope To The Hondle*, *File To Transfer Home*, *Fiber To The High*
  — **no son siglas de nada**. La **H** final es de ***home***.
- `[LGT]` · **Red de MUY ALTA capacidad** = «**totalmente de elementos de fibra óptica, al menos
  hasta el punto de distribución**».

## Órbita geoestacionaria

- `[S.673]` · **Satélite sincrónico**: periodo de revolución sideral medio **igual al periodo de
  rotación sideral** del cuerpo primario.
- `[S.673]` · **Geosincrónico**: sincrónico **de la Tierra**. NOTA: el periodo de rotación sideral
  de la Tierra es de **≈ 23 h y 56 min**.
- `[S.673]` · **Estacionario**: **permanece fijo** respecto a la superficie. NOTA: órbita
  **circular, ecuatorial y directa**.
- `[S.673]` · **Geoestacionario**: estacionario **cuyo cuerpo primario es la Tierra**.
- **La pregunta pide la FALSA** → **«el período de su órbita es de 48 horas»**. Son **≈24 h**, no
  48.
- Verdaderas: **fijo respecto a la Tierra** (definición) · **sobre el ecuador** (nota) · **~36.000
  km** — **ATENCIÓN: esta altitud NO está en la recomendación leída**. Es la única de las cuatro
  sin fuente en este tema.
- `[S.673]` · Gratis: **LEO** < ~**2 000 km** · **MEO** ~**10 000 km** · **apogeo** máxima
  distancia, **perigeo** mínima · órbita **directa** / **retrógrada**.

## Acceso a una señal por satélite

- `[uso]` · Respuesta: **horario, satélite, posición orbital, transponder, FRECUENCIA DE BAJADA,
  symbol rate**.
- **Truco del enunciado**: las cuatro opciones repiten **cinco datos idénticos** y sólo cambian el
  sexto: banda / polarización / **frecuencia de bajada** / codificación. **Sólo hay que recordar
  cuál eligió el tribunal.**
- **Honradez**: los descartados no son absurdos. `[SNG]` exige documentar «**anchura de banda y
  polarización de transmisión**». La respuesta vale **porque la corrige así el tribunal**.

## DSNG

- `[SNG]` · **DSNG = *Digital Satellite News Gathering***, en español «**periodismo electrónico
  digital por satélite**». Es el **título de la recomendación**.
- **Falsos**: cambian *Digital*→*Direct* o *News*→*Now*. **Las cuatro palabras: digital,
  satellite, news, gathering.**
- `[SNG]` · **Definición (1.1)**: «transmisión **temporal y ocasional** de televisión o sonido
  radiofónico **con escaso tiempo de aviso** con fines de difusión, utilizando **estaciones
  terrenas de enlace ascendente portátiles o fácilmente transportables** que operan en el marco
  del **servicio fijo por satélite**».
- `[SNG]` · **Dos personas, una hora**: el equipo debe poder ajustarse y manejarse por **no más de
  2 personas** en un tiempo corto, «por ejemplo, 1 h».
- `[SNG]` · **Banda preferida: 14 GHz** (antena pequeña, transportable). En **6 GHz** la
  coordinación «resulta más difícil»: se comparte con muchos enlaces terrenales fijos.
- `[SNG]` · **Comunicaciones adicionales** que puede exigir: **microondas punto a punto**,
  **telefonía**, **micrófonos inalámbricos símplex/dúplex bidireccionales**, **terminales móviles
  de satélite** para voz y datos.

## SMPTE ST 2110

- `[SMPTE]` · Familia «**Professional Media Over Managed IP Networks**»: vídeo, audio y datos
  **viajan como flujos SEPARADOS** por la misma red.
- `[SMPTE]` · **-40 = DATOS AUXILIARES** (la ST 291-1). **Es la respuesta.**
- `[SMPTE]` · **-10** temporización · **-20** vídeo **sin comprimir** · **-21** conformado del
  tráfico · **-22** vídeo comprimido a tasa constante · **-30** **audio digital** · **-31**
  transporte de **AES3** · **-41** metadatos rápidos · **-43** rotulación y subtítulos.
- **LA «ST 2110-50» NO EXISTE.** Un distractor se tacha con seguridad.

## La mochila LU300S

- `[ficha]` · **LU300S de LiveU: hasta 30 Mbps.** Falsos: 120, 90, 60.
- `[ficha]` · **Algo más de 900 g** · **hasta seis conexiones IP**: **4 móviles + inalámbrica local
  + red de área local** · agregación (*bonding*) sobre **HEVC** · hasta **4 conexiones 5G/4G**, con
  **2 módems internos de doble tarjeta** y **2 externos**.
- `[uso]` · **Qué es una mochila**: un **codificador que parte la señal entre varias conexiones
  móviles y las suma**. Ninguna aguantaría sola; juntas, sí. Ventaja frente al satélite: **no
  necesita permiso de frecuencia ni ventana de segmento espacial**.
- **Apoyo de memoria, no argumento**: los **30 Mbps** coinciden con el umbral de «red de alta
  capacidad» de la Ley 11/2022. **No tienen relación.**

## DVB y la televisión digital terrestre

- `[uso]` · Respuesta: «**especificación EUROPEA de emisión digital para televisión**, asociada al
  formato de compresión **MPEG-2**».
- **La sigla NO la desarrolla ninguna fuente leída**, y el tema no la desarrolla.
- `[TDT]` · Los receptores deben poder recibir emisiones conformes a la **norma EN 302 755
  (DVB-T2)**. **Es norma europea, y el BOE la cita por su designación.**
- `[TDT]` · **AVISO: el MPEG-2 está desactualizado.** A la fecha de corte, la alta definición se
  codifica conforme a la **Recomendación UIT-T H.264 / ISO-IEC 14496-10 (H.264/MPEG-4 AVC)**. La
  respuesta oficial vale **como descripción histórica**.
- **Falsos**: recepción **directa por satélite** al domicilio · **satélites de banda Ku** (TDF, TV
  Satélite) · **estaciones terrenas transportables** ← **eso es el DSNG**, la otra pregunta.

## Streaming y señal Pool

- `[uso]` · **STREAMING**: transmisión de audio y vídeo **en tiempo real por internet SIN
  DESCARGAR EL ARCHIVO COMPLETO**. Falsos: descarga completa previa (**eso es descarga**) ·
  «exclusivamente juegos» · «requiere cable».
- `[LGCA]` · Por si cae el lado jurídico: **servicio televisivo A PETICIÓN** o **no lineal** = para
  el visionado **en el momento elegido por el espectador y a su propia petición**, sobre un
  **catálogo** seleccionado por el prestador.
- `[uso]` · **SEÑAL POOL**: señal de un evento que, por su importancia informativa, **se encarga a
  la producción de UNA ÚNICA televisión y ésta la distribuye al resto que la soliciten**.
- **Regla de lectura que deja esta pregunta**: las cuatro opciones son **la misma frase** con un
  añadido —«multicanal», «con rótulos», «con audio ambiente»— y **la buena es la que NO añade
  nada**. El *pool* se define por **el acuerdo**, no por cómo venga la señal.

## Lo que se ha preguntado

- `[G.984]` **FTTH = Fiber To The Home**.
- `[S.673]` **falso que el periodo geoestacionario sea de 48 horas**.
- `[SNG]` **DSNG = Digital Satellite News Gathering**.
- `[SMPTE]` **datos auxiliares embebidos = ST 2110-40**.
- `[ficha]` **LU300S: 30 Mbps**.
- `[TDT]` **DVB: especificación europea de emisión digital de televisión**.
- `[LGT]` **el ancho de banda limita la velocidad de procesado y transmisión**.
- `[uso]` **streaming sin descargar el archivo completo** · **señal Pool sin adjetivos** ·
  **frecuencia de bajada** entre los datos de acceso al satélite.
