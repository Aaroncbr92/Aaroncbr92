# Qué material hace falta para los quince temas que quedan

Segunda mitad del hallazgo del 2 de septiembre: **de las 129 preguntas
específicas de Producción (Asistencia), sólo 15 tienen una norma del BOE detrás**
(`informes/fuentes-del-especifico-2026-09-02.md`), y esos dos temas —el 2 y el
17— ya están escritos. Este informe es el inventario de lo que necesitan **los
quince restantes**: qué fuente pide cada pregunta, cuál se ha conseguido y cuál
no.

## Antes que nada, el reparto

Las **129** preguntas específicas están ahora **todas clasificadas**, a mano y con
motivo, en `banco/especifico-produccion.tsv`. Seis de ellas **no eran del bloque
específico** y se han devuelto al del temario general:

| Cuadernillo · nº | Iba a | Por qué |
|---|---|---|
| 77 · 20 | `g8` | Comité de Seguridad y Salud a partir de 50 trabajadores: **art. 38.2 de la Ley 31/1995** |
| 78 · 3 | `g5` | Comisiones de servicio y pernocte: **III Convenio Colectivo** |
| 78 · 16 | `prl-especifico` | Síndrome del túnel carpiano |
| 78 · 47 | `g8` | Coordinación de actividades empresariales: **art. 24 de la Ley 31/1995** |
| 78 · 67 | `g5` | Incompatibilidades: es el **art. 107 del III Convenio**, aunque el enunciado lo llame «ley de incompatibilidades» |
| 78 · 24 | `fuera` | Señalización y clasificación por edades del **art. 7 de la Ley 7/2010**, derogada y fuera del programa |

Quedan **123** en el banco del específico, **todas con su respuesta oficial**, y
así se reparten:

| Tema | Preguntas | Estado |
|---|---|---|
| 9 · Escenografía e iluminación | **20** | Por escribir |
| 10 · Imagen y sonido | **17** | **Escrito** |
| 2 · Propiedad intelectual | 10 | **Escrito** |
| 11 · Medios de transmisión de señal | 10 | Por escribir |
| 13 · Equipos técnicos de exteriores | 7 | Por escribir |
| 1 · La producción | 6 | Por escribir |
| 3 · El guion | 6 | Por escribir |
| 7 · Equipos humanos | 6 | Por escribir |
| 8 · Formatos y soportes | 6 | Por escribir |
| 12 · El estudio de televisión | 6 | Por escribir |
| 14 · Documentación internacional | 6 | Por escribir |
| 15 · Organismos | 6 | Por escribir |
| 17 · Protección de datos | 5 | **Escrito** |
| 6 · Organización, plan y orden de trabajo | 4 | Por escribir |
| 5 · Localización | 3 | Por escribir |
| 16 · Gestión de servicios varios | 3 | Por escribir |
| 4 · El desglose | 2 | Por escribir |

**Los temas 9 y 10 son casi un tercio del examen específico**: 37 preguntas de
123. Son los dos por los que hay que empezar.

## Lo que se ha conseguido en esta pasada

### Del BOE, y por tanto de primer nivel

| Norma | Identificador | Para qué tema |
|---|---|---|
| **Real Decreto 2032/2009**, unidades legales de medida | `BOE-A-2010-927` | **9** — define la **candela** y el **kelvin** en el articulado, y da en su cuadro de unidades derivadas el **lumen** (flujo luminoso, cd·sr) y el **lux** (iluminancia, lm/m²) |
| **Reglamento de Ejecución (UE) 2019/947**, utilización de sistemas de aeronaves no tripuladas | `DOUE-L-2019-81004` | **13** — el **artículo 14** es el del registro de operadores de UAS |
| **Reglamento de Ejecución (UE) 923/2012**, reglamento del aire (**SERA**) | `DOUE-L-2012-81859` | **13** — su **definición 65** es la de **«zona peligrosa»**, que es lo que significa la etiqueta LE-D del espacio aéreo |
| **Convenio relativo a la importación temporal**, hecho en **Estambul** el 26/06/1990 | `BOE-A-1997-21711` | **14** — su **anexo A** define el **cuaderno ATA** y regula su validez y su garantía |
| **Real Decreto 1036/2017**, utilización civil de aeronaves pilotadas por control remoto | `BOE-A-2017-15721` | **13** — el marco español, con dos avisos de derogación parcial que el volcado recoge |

Los cinco están volcados **a la fecha de corte, 21 de diciembre de 2022**, en
`fuentes/corte-20221221/`.

### De organismos de normalización, y por tanto de segundo nivel

Están en `fuentes/normas-tecnicas/`, con su designación exacta, su edición y la
fecha en que se leyeron:

- **Recomendación UIT-R BT.2100-1 (06/2017)**, en español. Es **la que cita el
  enunciado de la pregunta 42**, con esa misma edición, y dice **«Muestreo
  reticular: Ortogonal»**.
- **Recomendación UIT-R BT.601-7 (03/2011)**, en español. Es la antigua **norma
  CCIR 601** por la que pregunta la 38, con la familia **4:2:2**.
- **Índice de la familia SMPTE ST 2110**, de la biblioteca abierta de la SMPTE,
  con **los títulos oficiales de cada parte**: la **40** es la de los datos
  auxiliares —*ST 291-1 Ancillary Data*—, y **la «2110-50» de la opción d) no
  existe**.

### Un hallazgo del reparto

La pregunta **77 · 30** —«en una producción interna, ¿qué derechos tiene la
CRTVE?», respuesta **los derechos de explotación**— **es del tema 2**, no de un
tema técnico: la contesta el **artículo 88 de la Ley de Propiedad Intelectual**,
que ya está escrito. Se ha añadido al banco del tema 2, que pasa de **9 a 10
preguntas**, y el tema las contesta las diez.

## Lo que no se ha podido traer

Probado y fallido, con el motivo:

| Fuente | Qué pregunta sostiene | Qué pasa |
|---|---|---|
| **DCI, Digital Cinema System Specification** | La resolución **4096 × 2160** del DCI 4K (tema 8) | `dcimovies.com` devuelve **404** en las rutas de descarga |
| **EBU/UER**, estatutos | Sede en Ginebra, tasa anual de los miembros activos, Euroradio (tema 15) | `ebu.ch` devuelve **403** a toda petición automática |
| **AES10 (MADI)** | Qué es el protocolo MADI (tema 10) | El buscador de normas de la AES no responde |
| **LiveU LU300S** | Caudal máximo de la mochila (tema 11) | Página de producto, **404** |
| **Sony HXR-NX80** y **DJI RS 4 Pro** | Compatibilidad entre cámara y estabilizador (tema 13) | Fichas de producto, **404** |
| **Astera Titan Tube**, **Mo-sys**, **Stype Star Tracker**, **ORAD** | Marcas citadas en cuatro preguntas del tema 9 | No probadas aún una a una; el patrón de las anteriores no invita al optimismo |
| **Cámara de Comercio de España** | Quién expide el cuaderno ATA (tema 14) | `camara.es`, **404** en la ruta probada. El **Convenio de Estambul** sí regula la **asociación garantizadora**, que es la figura de fondo |
| **Manual de estilo de RTVE** | Pendiente desde la Fase A | Sigue sin descargarse |

## Qué necesita cada tema, uno a uno

### Tema 9 · Escenografía e iluminación (20 preguntas)

**El más pesado del examen.** Se reparte en tres bloques muy distintos:

- **Luminotecnia con unidades medibles** —flujo luminoso en lúmenes, temperatura
  de color, dimmer, luz estroboscópica—. **Fuente conseguida**: el RD 2032/2009
  para las unidades. Lo demás es práctica profesional.
- **Escenografía clásica** —tronera, alzado, limbo, forillo, practicable,
  utilería, props—. **Sin fuente normativa**. Vocabulario de oficio; se apoyará en
  la plantilla oficial y en los usos, diciéndolo.
  Excepción: el **practicable y su toma de tierra** es materia eléctrica, y ahí
  hay norma —el **RD 842/2002** y sus instrucciones técnicas, que el proyecto ya
  usó para el tema de prevención—.
- **Escenografía virtual y realidad aumentada** —ORAD, Mo-sys, Star Tracker, los
  360 grados—. **Marcas comerciales**. Cuarto nivel de la jerarquía, y frágil.

### Tema 10 · Imagen y sonido (17 preguntas)

El mejor servido de los quince, porque casi todo tiene norma técnica:

- **Vídeo**: 4:2:2 y CCIR 601 → **UIT-R BT.601-7**, conseguida. HDR y muestreo
  ortogonal → **UIT-R BT.2100-1**, conseguida. Vectorscopio, luminancia y
  crominancia → las mismas recomendaciones definen Y, C'B y C'R.
- **Audio**: patrones polares, impedancia, muestreo de Nyquist, tiempo de
  reverberación (la caída de **60 dB**), trémolo. La caída de 60 dB es la
  definición **RT60** de la **ISO 3382**; conviene intentar esa norma. **MADI**
  necesita la **AES10**, que no se ha podido traer.
- **Óptica**: distancia focal y profundidad de campo. Física, no norma.

### Tema 11 · Medios de transmisión de señal (10 preguntas)

- **SMPTE ST 2110-40** → conseguido el índice con los títulos oficiales.
- **DVB**, **DSNG**, **FTTH**, **señal Pool**, parámetros de acceso a un
  transpondedor de satélite, órbita geoestacionaria: vocabulario técnico de
  difusión. El **DVB** tiene normas **ETSI** públicas y descargables; merece la
  pena probarlas.
- **Mochila LU300S**: ficha de fabricante, no conseguida.

### Tema 13 · Equipos técnicos de exteriores (7 preguntas)

**El mejor resuelto de los pendientes**, gracias a los drones: dos de sus siete
preguntas —el registro de operadores de UAS y la zona **LE-D**— tienen ahora
**norma europea detrás**, la 2019/947 y la SERA. El resto —TV Compound, mobycam,
Mojo, beauty shot, compatibilidad Sony/DJI— es oficio y fabricante.

### Tema 14 · Documentación internacional (6 preguntas)

**Cuatro de las seis son sobre el cuaderno ATA**, y ahora hay **convenio
internacional publicado en el BOE**: el de Estambul, cuyo anexo A lo define, fija
su **validez** y regula la **asociación garantizadora**. Falta la fuente española
sobre **quién lo expide** —las Cámaras de Comercio— y la del **MCO** de IATA.

### Tema 15 · Organismos (6 preguntas)

**El peor servido.** Las seis preguntan por EBU/UER, FORTA, UTECA, ENEX y
Euroradio, y **ebu.ch responde 403**. FORTA y UTECA tienen estatutos y, sobre
todo, **norma de creación**: las televisiones que integran **FORTA** nacen al amparo de la
**Ley 46/1983, del tercer canal**, y **UTECA** aparece citada en el propio
enunciado del examen junto con la **Ley 10/1998** y la **Ley 7/2010**.
Por ahí sí hay BOE, y conviene tirar de ese hilo antes de darse por vencido.

### Temas 1, 3, 4, 5, 6, 7, 12 y 16 (36 preguntas entre los ocho)

**Ninguna pregunta con norma detrás.** Son fases de la producción, documentos de
rodaje, oficios, controles del estudio y proveedores. Aquí la jerarquía cae al
tercer nivel —documentación institucional— y al quinto —la plantilla oficial—.

Dos anclas que sí existen y hay que aprovechar:

- El **anexo 3 del III Convenio Colectivo** —clasificación profesional: grupos,
  ámbitos ocupacionales y ocupaciones tipo— ya está transcrito en el proyecto y
  **nombra oficialmente** «Ambientador musical», «Estilismo (vestuario-maquillaje
  y caracterización)», «Ambientación decorados» y «Producción (asistencia)». No
  llega al detalle de «figurinista» o «forillista», pero sitúa el marco.
- El **artículo 38 del mismo convenio**, con los **trece ámbitos ocupacionales**.

## Actualización del mismo día: el tema 10, escrito

**Hecho el primero de los quince.** Al escribirlo aparecieron dos fuentes más y se
cerró una duda del inventario:

- **El tiempo de reverberación no necesitaba la ISO 3382.** La definición —caída
  de **60 dB**— está publicada en el BOE: es el **anejo de terminología del
  Documento Básico DB-HR** del Código Técnico de la Edificación, aprobado por el
  **Real Decreto 1371/2007** (`BOE-A-2007-18400`). Guardado el extracto en
  `fuentes/corte-20221221/BOE-A-2007-18400.preceptos.md`, con los dos avisos que
  hay que dar: **regula edificios, no platós**, y es **el texto de 2007**, cuyas
  dos modificaciones se han revisado y **no tocan esta definición**.
- **La AES10 sigue tras un muro de pago**, pero la **propia AES** publica en la
  presentación de sus normas la frase que basta para lo que el examen pregunta:
  «AES3 (2-channel digital audio), **AES10 (MADI)**, AES14…». Guardada en
  `fuentes/normas-tecnicas/AES-normas-de-audio.md`, con lo que **sí** y lo que
  **no** se puede afirmar con ella.
- **Un error de extracción, cazado y corregido.** El texto sacado del PDF de la
  BT.601-7 daba «16,75 MHz» donde la recomendación dice **6,75 MHz**. Saltó porque
  no cuadraba con el resto del cuadro, y **se confirmó recortando y ampliando esa
  celda para leerla a ojo**. Lección para este nivel de la jerarquía: **con una
  norma técnica en PDF, el texto extraído no es la fuente; la página lo es**.

De las **17 preguntas** del tema, **7 tienen norma o recomendación detrás** y las
otras **10 se apoyan en la plantilla oficial y en el uso profesional**, marcado una
a una. Es exactamente la proporción que este informe anticipaba.

## Segunda actualización del mismo día: el tema 9, escrito

**Cerrado con 3.970 palabras**, esquema e informes. Lo que este informe anticipaba
se cumplió al pie de la letra: de las **20 preguntas**, **4 tienen norma detrás**
—**RD 2032/2009** para el lumen, **ITC-BT-24** del RD 842/2002 para la toma de
tierra, **cuadro 1 de la UIT-R BT.601-7** para el complementario del magenta, y
física demostrable para la transmisión de la luz— y **16 se apoyan en la plantilla
oficial**. El tema **lo dice en su portada** en lugar de aparentar uniformidad.

**Las cuatro fichas de fabricante siguen sin traerse**, y ya no se van a esperar:
las respuestas se recogen con el nivel marcado y con el aviso de que **caducan** si
la próxima convocatoria cambia de proveedor.

## Lo siguiente

1. **Escribir los nueve temas que quedan**, por peso de examen: **7**, **8**, **12**,
   **14** y **15** (6 cada uno), **6** (4), **5** y **16** (3) y **4** (2).
   *(Cerrados: **1**, **2**, **3**, **9**, **10**, **11**, **13** y **17**.)* Y en cada
   uno, **buscar el vocabulario en las fuentes que ya están en casa antes de darlo por
   huérfano**: el tema 1 tenía dos preguntas con norma literal en el propio convenio, y
   el tema 3 **ninguna, comprobado término a término**.
2. **Tirar del hilo del BOE para el tema 15** antes de resignarse: Ley 46/1983,
   Ley 10/1998 y Ley 7/2010 pueden sostener FORTA y UTECA.
3. ~~Probar **ETSI** para el DVB~~ y ~~las fichas de **Sony** y **DJI**~~ →
   **hecho**. El ETSI y **DJI** estaban abiertos con agente de navegador; **Sony** y
   el fabricante de la **mobycam** están cerrados de verdad, comprobado con la regla
   puesta.

## Tercera actualización del mismo día: el tema 11, escrito

**Cerrado con 4.529 palabras**, esquema e informes, y es **el mejor servido de todo el bloque**:
**siete de sus diez preguntas** tienen norma, recomendación o ficha detrás. La razón no es que la
materia sea más normativa que las otras —lo es un poco—, sino que **se probaron otra vez las
puertas dadas por cerradas**.

**Lo que se trajo en esta pasada:**

- **Recomendación UIT-R S.673-2 (03/2002)**, términos de radiocomunicaciones espaciales: contesta
  entera la pregunta de la órbita geoestacionaria y regala **LEO**, **MEO**, apogeo y perigeo.
- **Recomendación UIT-R SNG.770-2 (01/2012)**: **el título es la respuesta** a la pregunta del
  DSNG, y el cuerpo da la definición formal, el listón de las dos personas en una hora y la banda
  de 14 GHz.
- **Recomendación UIT-T G.984.1 (03/2003)**: desarrolla **FTTH** y toda su familia.
- **Normas europeas ETSI EN 300 744 y EN 302 755**: desarrollan **DVB** en su propio título y
  sostienen, literalmente, la asociación con el **MPEG-2** que el enunciado hace.
- **Ley 11/2022** y **Plan Técnico Nacional de la TDT** (`BOE-A-2019-9513`), del BOE.
- **Ficha de LiveU del LU300S**, que es la que destapó todo lo demás.

**Lo que sigue sin fuente en este tema**: la altitud de **36.000 km** de la órbita geoestacionaria
—la recomendación da las otras dos de la escala, no ésa—, el **streaming**, la **señal Pool** y
cuál de los seis datos de acceso a una señal por satélite es el imprescindible.

## Cuarta actualización del mismo día: el tema 13, escrito

**Cerrado con 2.946 palabras**, esquema e informes. Es **el primero que estrena el tercer nivel de
esta misma jerarquía**: `fuentes/institucionales/`, con el **AIP de España, sección ENR 5.1**,
publicado por **ENAIRE**. Hizo falta porque el reglamento del aire define **qué es** una zona
peligrosa pero **no dice con qué letras se rotula**, y sin eso la etiqueta **LED** del enunciado se
quedaba sin explicar.

**El recuento de fuentes recuperadas por la regla del agente de navegador va por cuatro**: LiveU,
Astera, ETSI y DJI. Y hay **dos cerradas de verdad**, comprobadas con la regla puesta: **Sony** y
el fabricante de la **mobycam**.
