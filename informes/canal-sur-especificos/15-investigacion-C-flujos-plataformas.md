# Grafista (puesto 15) · Investigación del bloque C-flujos-plataformas (temas 7, 12, 13, 14, 17)

Fase 1 · Investigar. Fecha de trabajo: 29-09-2026 (el encargo fija «hoy» el 24-09-2026; las fuentes se
leyeron el 29-09-2026 y así se declara en cada una). Sólo lo que falta para cubrir el enunciado: lo
reutilizable (RTVE y temas cerrados de Canal Sur) ya está localizado y lo lee el redactor.

Convención: **negrita entre comillas = literal de la fuente**; lo demás, lectura propia o traducción.
«Oficio» = práctica de oficio sin norma que la fije. Cada dato lleva su fuente al lado.

Aviso sobre lo reutilizable de RTVE (diseno-grafico/07 y 09): sus propios «Trazabilidad» declaran que
**no citan ninguna fuente de forma literal** y que van enteros como oficio. Lo que se copie de ellos va
como oficio; este informe aporta fuentes publicadas para las fases del proceso (tema 14).

Tema cerrado no asignado pero útil (el redactor puede copiarlo literal): Montador/a 13
(`30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`) ya da, con
fuente, el protocolo MOS (mosprotocol.com, v2.8.5 y v4.0), las plantillas .mogrt de Premiere (ayuda
de Adobe), las plantillas de rótulos de DaVinci Resolve 21, MAM/PAM, EBUCore como «glue» y el iNews de
Avid en Canal Sur (Manfredi, 2010). No se repite aquí.

---

## Tema 13 · Diseño para redes sociales y plataformas: formatos verticales, miniaturas, piezas cortas y coherencia de marca

Lo que ya da Montador/a 12 (copiar literal, no se repite): marco de la Carta (art. 7) y servicio
público digital; relaciones de aspecto de YouTube y barras en 9:16; qué es un Short (vertical o
cuadrado de hasta 3 min); guías de redes de DaVinci Resolve 21 (**«Social Media: 1:1, 4:5, 9:16, 1.91:1,
16:9.»**); reencuadre 16:9→9:16 (cálculo 3413 × 1920); miniaturas de YouTube (resolución, formato, peso,
qué no se puede poner); codificación recomendada; música y reclamaciones; *Digital News Report 2026*;
advertencia de que **los rótulos y el grafismo de emisión no sirven tal cual** en vertical.

Lo propio del grafista que falta: la identidad del canal en la plataforma (avatar, banner, marca de agua)
y las zonas seguras frente a la interfaz de la aplicación en vertical.

### 13.1 Identidad del canal en YouTube: foto de perfil, banner y marca de agua

Fuente: Ayuda de YouTube, «Manage your channel branding» (https://support.google.com/youtube/answer/10456525?hl=en),
leída el 29-09-2026 (página sin fecha visible).

- Qué es la marca del canal: **«Brand your YouTube channel's identity by updating your profile picture,
  channel banner, and video watermark.»** Tres piezas gráficas: foto de perfil, banner, marca de agua.
- Foto de perfil: **«Your profile picture is the image shown to viewers on your channel, videos, and
  publicly attributable actions across YouTube.»** Requisitos: **«JPG, GIF, BMP, or PNG file (no animated
  GIFs)»**; **«Image size should not exceed 15 MB.»**; **«Image that renders at 98 X 98 px.»** Consecuencia
  de oficio: el logotipo del canal se ve a 98 × 98, así que se usa la versión reducida de la marca, no la
  completa con texto (oficio; la página no lo dice).
- Banner: **«Your banner image shows as a background at the top of your YouTube page.»**; **«The same
  banner image is used across computer, mobile, and TV displays, but it shows differently depending on
  your device.»** Recomendaciones (**«Follow these recommendations for your banner to render properly»**):
  - **«Minimum dimension for upload: 2048 x 1152 px with an aspect ratio of 16:9.»**
  - **«At the minimum dimension, the safe area for text and logos: 1235 x 338 px.»**
  - **«Recommended dimension (especially for TV): 2560 x 1440 px.»**
  - **«Images should accommodate the entire screen for larger devices but will get cropped on certain
    views and devices.»**
  - **«Do not include any additional file embellishments (e.g. shadows, borders, and frames).»**
  - **«File size: 6 MB or smaller.»**
  - Ojo: la página da la zona segura **sólo a la dimensión mínima** (1235 × 338 sobre 2048 × 1152). Las
    cifras que circulan para 2560 × 1440 (1546 × 423) son de blogs, no de YouTube: no usar.
- Marca de agua de vídeo: **«You can add a video watermark to your video to promote your channel’s
  branding.»** Tiempos de aparición: **«End of video: The video watermark will show for the last 15
  seconds of the video.»**; **«Custom start time: The video watermark will begin showing at a time you
  choose.»**; **«Entire video: The video watermark will show throughout the entire video.»** Requisitos
  (**«must meet the following criteria»**): **«Minimum 150x150 pixels.»** y **«Square image less than 1 MB
  in size.»** Salvedades: **«Video watermarks aren’t available on videos set as made for kids.»**; **«The
  channel watermark is available in landscape view on computers and mobile devices (not clickable on
  mobile).»** Métrica: en el informe **«Subscription source»** de YouTube Analytics.
- Diferencia con la mosca de emisión (oficio): la marca de agua la superpone la plataforma y es un
  botón de suscripción; la mosca de emisión va incrustada en la señal. Si un vídeo de emisión se sube con
  su mosca y además lleva marca de agua, la marca aparece dos veces (oficio, sin fuente).

### 13.2 Zonas seguras en vertical frente a la interfaz de la aplicación (Meta, Reels)

Fuente: Meta, *Facebook Ads Guide*, «Awareness Image Ad Specs on Instagram Reels»
(https://www.facebook.com/business/ads-guide/update/image/instagram-reels), leída el 29-09-2026.
**Salvedad importante: es la especificación de anuncios**, no de publicaciones orgánicas; Meta no
publica en su ayuda de Instagram (página de resolución, JS, sólo legible su descripción) una zona segura
para Reels orgánicos. Se usa como referencia de oficio, declarándola.

- Especificación: tipo de fichero **«JPG or PNG»**; relación **«9:16»**; resolución **«1440 x 2560
  pixels»**; tamaño máximo 30 MB, anchura mínima 500 px, tolerancia de relación de aspecto 1 %
  (lectura de la página por la herramienta de consulta; no se ha podido copiar literal la tabla).
- Zona segura (literal, del HTML de la página): **«Consider leaving roughly 14% of the top, 35% of the
  bottom, and 6% on each side of your asset free from text, logos, or other key creative elements to avoid
  cropping key elements or covering them with the profile icon or call-to-action.»**
- Cálculo (propio) sobre 1080 × 1920: arriba 14 % ≈ 269 px; abajo 35 % = 672 px; lados 6 % ≈ 65 px cada
  uno. Queda útil para texto y logo una franja de unos 950 × 979 px. Sobre 1440 × 2560: 358 / 896 / 86 px.
- Idea de fondo (oficio): en vertical la «zona segura» no la fija la pantalla, como en EBU R 95 o SMPTE
  ST 2046-1 (tema 8), sino la interfaz de la aplicación (nombre de la cuenta, descripción, botones), que
  ocupa sobre todo la parte baja y el lateral derecho.

### 13.3 Instagram: lo único legible de su ayuda

Fuente: Instagram Help Centre, «Photo resolution…» (https://help.instagram.com/1631821640426723), leída el
29-09-2026. La página se genera con JavaScript; sólo se ha podido leer su descripción: **«When you share
a photo on Instagram, regardless of whether you're using Instagram for iPhone or Android, we make sure to
upload it at the best quality resolution possible (up to 1080x1080 pixels).»** No confirmado: la horquilla
de relaciones de aspecto del *feed* (1.91:1 a 4:5, 1080 px de ancho) que repiten blogs. **No usar sin
leerlo en la ayuda de Instagram.**

### 13.4 Coherencia de marca en redes: lo que da la casa

- Plantilla de puestos: la ficha del Grafista no menciona redes (convenio, ficha 5345100, p. 129: ver tema
  7). La tarea **«Diseñar y realizar y todo tipo de imagen gráfica para programas y postproducciones, y
  otros fines promocionales.»** es la que cubre, por lectura, las piezas para redes (lectura propia).
- La Carta y el manual de marca: el bloque A (tema 2) ya consigna que **no hay manual de marca de Canal
  Sur/RTVA publicado**; la coherencia se razona con los principios del tema 2 (oficio).
- El Libro de estilo pide coherencia estética a las desconexiones, que vale como criterio de casa para
  cualquier versión derivada: **«Las desconexiones, como meta del trabajo informativo local, están
  obligadas a aplicar un criterio de coherencia estética y conceptual con la edición general en la que se
  integran y de la que son tributarias.»** (LE, 7.4, p. 104; leído el 29-09-2026). Aplicarlo a redes
  es extensión propia: dígase así.

### No confirmado (tema 13)

- Medidas y zonas seguras de TikTok y de Shorts (YouTube no da zona segura de Shorts en las páginas
  leídas; Montador 12 tampoco). No se han leído fuentes oficiales de TikTok.
- Relaciones de aspecto del *feed* de Instagram y portadas de Reels (ayuda no legible).
- Duración máxima de un Reel: no leída.

---

## Tema 12 · Archivo, catalogación y reutilización de elementos gráficos, plantillas y proyectos

Lo que ya dan los temas cerrados (copiar literal): Montador 08 (verificación con suma, regla 3-2-1,
RAID no es copia, metadatos, XMP, EBUCore, OAIS, LTO/LTFS, códecs sin pérdidas); Montador 15
(proyecto frente a material, *bins*, *Attic*, bibliotecas y Live Save de Resolve 21, nomenclatura,
UMID, AAF/OMF, versiones, bloqueo de *bins*); Montador 13 (plantillas .mogrt, Creative Cloud Libraries:
**«Any Motion Graphics template stored in your Creative Cloud Libraries is automatically available for
use in Premiere. It doesn't need to be installed.»**, fichero local `adobe-mogrt-install…`, leído por
Montador el 25-09-2026). Bloque B, tema 9.2: plantillas de título de Fusion (macros). Aquí, lo propio
del grafista.

### 12.1 La casa: el archivo de imagen es tarea de la ficha

Fuente: X Convenio Colectivo de la RTVA (BOJA núm. 240, de 10-XII-2014), leído el 29-09-2026.

- Ficha 5345100 GRAFISTA (p. 129), última tarea: **«Mantener el archivo de imagen del departamento
  gráfico.»** Es la base de casa del tema 12 (archivo y reutilización son funciones del puesto).
- No confundir con la ficha 9420000 **«J. SEC. DISEÑO ASISTIDO»** (p. 153), cuyo objeto es **«Organizar,
  coordinar y supervisar el soporte gráfico de la documentación técnica de las instalaciones de RTVA y
  SSFF.»** y cuyas tareas son **«Definir, desarrollar, implementar y mantener los sistemas de archivo
  gráfico.»**, **«Crear librerías electrónicas para facilitar trabajos gráficos. Estructurar el sistema de
  almacenamiento de planos y referencias.»**: es archivo de planos técnicos, no de grafismo de antena
  (lectura del objeto del puesto). Pregunta trampa posible.
- La casa no ha publicado cómo cataloga su grafismo (sistema, campos, tesauro): no consta.

### 12.2 Base de datos de grafismo en directo: Viz Graphic Hub (Vizrt)

Fuente: Vizrt, *Graphic Hub Administrator Guide* 3.9 (documentation.vizrt.com/graphic-hub-guide/3.9/),
páginas «Overview» (descarga directa) y «General Database Information» (vía herramienta de consulta),
leídas el 29-09-2026. La 3.9 es la última publicada en el centro de documentación (3.10, 3.11, 3.12 y 4.0
dan 404, comprobado el 29-09-2026). Es ejemplo de mercado: **no consta** que Canal Sur use Vizrt.

- Qué es: **«The Graphic Hub is a database solution where all Viz Artist elements are stored. Files can
  be Scenes, Geometries, Images, Materials, Fonts, and so on.»** (Overview, literal de la descarga).
- Dependencia: **«To start Viz Artist successfully, a Graphic Hub must be running. The Graphic Hub can
  either be a local instance, where only one User can log in, or it can be a Multi-User database»**
  (Overview).
- Referencias entre ficheros (la clave de la reutilización): **«In the database, files are linked and
  referenced. Every file knows which folder it is placed in, which other files it uses, and also by which
  other files it is used.»**
- Identificador único: **«The database manages the files in terms of properties and Universally Unique
  Identifiers (UUIDs).»**; **«The UUID of the file is identical in all folders.»** (enlace con el UMID
  de Montador 15, misma idea: identificador que no depende del nombre; comparación propia).
- Borrado: **«If a file is deleted within a folder, only the folder-link to this folder is removed. The
  file remains in the database, unless every folder-link is removed.»**
- Bloqueo para trabajo en equipo: **«The check out of a file is valid until it is checked in again. Check
  in can be performed by the user who checked out the file, or the check out can be canceled by the
  administrator.»**
- Catalogación: **«Up to 20 keywords can be applied to each file. Every file holds a list of keywords in
  its properties.»**; **«Keywords can be used as a database search criteria.»**
- Índice de la guía (descarga directa, rótulos literales): «Locate Duplicate Files», «Add Metadata»,
  «Replace File References», «Daily Backup Using a Second Graphic Hub», «Main and Replication Servers
  with Failover», «Graphic Hub Archives» (con «Import Archives» / «Export Archives»). Sólo rótulos: su
  contenido no se ha leído. La consulta de «Graphic Hub Archives» no dio definición del formato de
  archivo: no afirmar su extensión.
- Salvedad: las citas de «General Database Information» proceden de la herramienta de consulta (la
  página exige JavaScript); el verificador debe releerlas en navegador.

### 12.3 Archivar un proyecto con todos sus medios: DaVinci Resolve 21

Fuente: Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, July 2026 (PDF), leído el 29-09-2026.

- Qué hace (cap. 3, «Archiving and Restoring Projects», p. 95): **«DaVinci Resolve has a convenient
  feature for quickly archiving every single media file used by a project, including subtitle files,
  along with the project itself, to a single location. This can be done to hand a project off to another
  DaVinci Resolve user, or to bundle a project and its media up for either short- or long-term archiving
  using the backup methodology of your choice.»**
- Pasos (p. 95): en el *Project Manager*, clic derecho sobre el proyecto y **«Archive»**; elegir un
  volumen **«large enough to accommodate the size of all the media from the project»**; opcionalmente
  **«You can optionally save Optimized media and/or Render Cache media associated with a project.»**;
  **«If any errors come up, resulting from missing or offline media, they’ll be presented at the end of the
  process.»**
- Resultado (p. 96): **«The resulting archive that is written is a directory with the .dra file
  extension. Inside this folder are a series of subdirectories containing all of the media that’s used by
  the archived project. Each directory of media files used is saved within a directory path that mirrors
  the exact path it came from, so you have a reference for where each clip came from originally.»**
- Restaurar (p. 96): **«Restore»** en el menú contextual del *Project Manager*; el proyecto **«remains
  linked to the media located inside the .dra archive.»**; o arrastrar la carpeta .dra al *Project
  Manager*.
- Equivalente en Adobe (After Effects: *File > Dependencies > Collect Files*, *Reduce Project*,
  *Consolidate All Footage*; Premiere: *Project Manager*): **no confirmado**. helpx.adobe.com devolvió 403
  el 29-09-2026; sólo se vio por buscador. No citar sin leer.

### 12.4 Elementos que se reutilizan en todos los proyectos: Power Bins (Resolve 21)

Fuente: *DaVinci Resolve 21 Reference Manual*, cap. 17, «Sharing Media Among Projects Using Power Bins»,
p. 392, leído el 29-09-2026.

- **«Power Bins provide a way of importing and organizing media that you want to be available to all
  projects in DaVinci Resolve.»**
- **«whatever clips you import into Power Bins are shared among all projects in a single-user
  installation, or all projects belonging to a particular user in a multi-user installation.»**
- Para qué (la frase que describe el grafismo de cadena): **«This makes Power Bins ideal for storing
  shared media that’s re-used often, such as stock video, sound effects, stills, and things like company
  slates and network graphics and animations that go into every show of a series.»**
- Exportables: **«You can import and export Power Bins (bins that persist from project to project) as
  .drb files»**; están **«hidden by default»** (cap. 17, p. 390).

### 12.5 Plantillas de título reutilizables (remisión)

Plantillas de Fusion guardadas como macro en `…/Fusion/Templates/Edit/Titles` y visibles en *Effects
Library > Titles* (cap. 67, pp. 1480-1484 del manual de Resolve 21): ya en el bloque B, tema 9.2. Dato
que añade aquí: el macro deja elegir qué parámetros son editables (**«The Macro Editor is designed to let
you choose which parameters you want to expose as custom editable controls for that macro.»**, p. 1483)
y, tras guardarlo, **«you’ll need to quit and reopen DaVinci Resolve»** (p. 1483). Idea de oficio para
el tema: una plantilla bloquea el diseño (tipografía, color, posición) y deja abierto sólo el texto,
lo que da coherencia de marca a quien la usa sin ser grafista (lectura propia).

### No confirmado (tema 12)

- Sistema de archivo o MAM de grafismo de Canal Sur (no publicado).
- Funciones de Adobe para recopilar y archivar proyectos (403 en helpx).
- Formato de archivo de Graphic Hub (extensión y contenido).
- Norma de catalogación específica para grafismo: no se ha encontrado; EBUCore (Montador 08) es la
  referencia general de metadatos audiovisuales.

---

## Tema 14 · Gestión de proyectos gráficos: briefing, propuesta, revisión, aprobación y control de calidad

RTVE diseno-grafico/07 (50 % del enunciado) da fases, *brainstorming*, producción y evaluación, pero
**todo sin fuente** (su Trazabilidad: **«Este tema no cita ninguna fuente de forma literal.»**). Aquí:
un modelo de proceso publicado (Doble Diamante), una guía publicada de *briefing* y la mecánica de
revisión y aprobación en una herramienta. La tabla de cinco fases de RTVE (investigación → ideas →
prototipos → implementación → evaluación) sigue siendo oficio; el Doble Diamante es la referencia
publicada que la respalda en lo esencial (comparación propia).

### 14.1 El proceso: el Doble Diamante (Design Council, Reino Unido)

Fuentes: Design Council, «The Double Diamond» (https://www.designcouncil.org.uk/our-resources/the-double-diamond/)
y «Framework for Innovation» (https://www.designcouncil.org.uk/our-resources/framework-for-innovation/),
descargadas y leídas el 29-09-2026. Licencia: **«The Double Diamond by the Design Council is licensed under a CC
BY 4.0 license»**.

- Definición: **«The Double Diamond is a visual representation of the design and innovation process. It’s a
  simple way to describe the steps taken in any design and innovation project, irrespective of methods and
  tools used.»** (Double Diamond).

- Qué es y fecha: **«At the heart of the framework for innovation is Design Council’s design
  methodology, the Double Diamond – a clear, comprehensive and visual description of the design process.
  Launched in 2004, the Double Diamond has become world-renowned with millions of references to it on the
  web.»** (Framework).
- Los dos diamantes: **«The two diamonds represent a process of exploring an issue more widely or deeply
  (divergent thinking) and then taking focused action (convergent thinking).»** (Framework).
- Las cuatro fases (literal, ambas páginas):
  - **Discover**: **«The first diamond helps people understand, rather than simply assume, what the
    problem is. It involves speaking to and spending time with people who are affected by the issues.»**
  - **Define**: **«The insight gathered from the discovery phase can help you to define the challenge in a
    different way.»**
  - **Develop**: **«The second diamond encourages people to give different answers to the clearly defined
    problem, seeking inspiration from elsewhere and co-designing with a range of different people.»**
  - **Deliver**: **«Delivery involves testing out different solutions at small-scale, rejecting those that
    will not work and improving the ones that will.»**
- No es lineal: **«This is not a linear process as the arrows on the diagram show. Many of the
  organisations we support learn something more about the underlying problems which can send them back to
  the beginning. Making and testing very early stage ideas can be part of discovery. And in an
  ever-changing and digital world, no idea is ever ‘finished’. We are constantly getting feedback on how
  products and services are working and iteratively improving them.»** (Framework).
- Origen: **«In 2003, the Design Council was promoting the positive impact of adopting a strategic
  approach to design and the value of ‘design management’ as a practice. However, they had no standard
  way of describing the supporting process.»** (Double Diamond, «The history…»).
- Casación con el enunciado (lectura propia): *briefing* y propuesta ≈ primer diamante (descubrir y
  definir: el *brief* fija el problema); propuesta, revisión y aprobación ≈ segundo diamante (desarrollar
  alternativas, probar y descartar); control de calidad ≈ final de *Deliver*. Traducción de los nombres
  (descubrir, definir, desarrollar, entregar): propia.

### 14.2 El *briefing*: guía conjunta de la industria británica

Fuente: *The Client Brief. A best practice guide to briefing communications agencies. Joint industry
guidelines for young marketing professionals in working effectively with agencies*, IPA, ISBA, MCCA,
PRCA (con la Communications Agencies Federation, CAF). PDF de 10 páginas sin fecha impresa; la
investigación que cita es **«(‘BRIEFING’ RESEARCH 2002 …)»** y el pie menciona, sin que quede claro si se refiere a este folleto o a la versión en línea, **«(This will be a revised version of
‘The Guide’ summary published in July 2002, which is still available online.)»**. Fecha de edición: no confirmada. Copias leídas el 29-09-2026: https://www.studiowide.co.uk/assets/how-to-write-a-brief.pdf
(también en https://www.acaweb.ca/en/wp-content/uploads/sites/2/2016/09/THE-CLIENT-BRIEF-FINAL-Eng-July-18-06.pdf,
no abierta). Es guía de publicidad (cliente-agencia), no de televisión: se aplica por analogía al
encargo que recibe grafismo de un programa o de promociones (lectura propia). Siglas: Institute of
Practitioners in Advertising (IPA); Incorporated Society of British Advertisers (ISBA); las otras dos
no se desarrollan en el PDF: no presentarlas desarrolladas sin fuente.

- Qué es el *brief*: **«The brief is the most important bit of information issued by a client to an
  agency. It’s from the brief that everything else flows. Indeed written briefs are a point of reference
  that can be agreed at the outset and therefore, to some extent, form a contract between client and
  agency.»**
- Por qué por escrito (tres razones): **«1 It leads to better, more effective and measurable work / 2 It
  saves time and money / 3 It makes remuneration fairer»**.
- El coste de no hacerlo: **«not writing a brief to save time is a false economy, as more often than not
  it leads to re-working.»**; **«75% of agencies and 55% of clients agreed that: “The briefs that we work on
  are often changed once the project has started”.»**; **«99% of agencies and 98% of clients agreed that:
  “Sloppy briefing and moving goal posts wastes both time and money”.»**
- Escrito y hablado: **«94% of clients and 98% of agencies believe: “A combination of written and verbal
  briefing is the ideal”.»**
- Breve: **«Briefs are called ‘briefs’ because they are meant to be brief. They are a summation of your
  thinking. Try to attach all relevant supporting information as appendices.»**
- Objetivos: **«Use concrete business objectives rather than vague terms such as ‘to improve brand
  image’.»**; **«clearly defining the objectives to establish the project’s ‘success criteria’ (what will
  success look like and how will it be measured?) is the number one principle of writing a good brief.»**
- Los dos extremos del puente: **«Generally your brief should focus on defining the ‘two ends of the
  bridge’: “Where are we now?” and “Where do we want to be?”»**
- Los ocho apartados: **«THE KEY SECTION HEADINGS OF A BEST PRACTICE CLIENT BRIEF ARE AS FOLLOWS: 1 Project
  management 2 Where are we now? 3 Where do we want to be? 4 What are we doing to get there? 5 Who do we
  need to talk to? 6 How will we know we’ve arrived? 7 Practicalities 8 Approvals»** (orden de la
  numeración; en el PDF van a dos columnas).
- Gestión (apartado 1): **«DATE; PROJECT NAME; PROJECT TYPE; PURCHASE ORDER; JOB NUMBER»**, equipos y
  contactos.
- Aspectos prácticos (apartado 7): presupuestos, **«TIMINGS: What are the key delivery dates? […] When
  should the key project milestones be set?»** y otras restricciones: **«Does the brand or corporate
  identity have guidelines or other mandatories?»** (enlace con el manual de marca, tema 2).
- Aprobación (apartado 8, clave para el enunciado): **«The final piece of detail needed in the brief is who
  has the authority to sign off the work that the agency produces. This person (or people) should also be
  the one(s) to sign off the brief before it is given to the agency.»** Es decir: quien aprueba el
  trabajo aprueba antes el *brief*.
- Medir (apartado 6): **«How will the campaign be measured? When will it be measured? Who will measure
  it?»**
- Estrategia usada como *brief*, el vicio: **«79% of agencies reported that: “Clients often use the
  creative process to clarify their strategy”, and even 35% of clients agreed with this.»**

### 14.3 Revisión y aprobación sobre la pieza: Frame.io (Adobe)

Fuente: Frame.io V4 Knowledge Center, artículos «Player page features» (9105311), «Commenting on your
media» (9105251), «Versioning in Frame.io» (9101068) y «Comparison Viewer» (9952618), descargados y
leídos el 29-09-2026 (fechas relativas en la página: «Updated this week» / «Updated over 2 weeks ago»).
Ejemplo de mercado: **no consta** que Canal Sur lo use.

- Estados de aprobación: **«To adjust the status label, open the “Properties” panel and edit the
  “Status” field. You can pick from “Needs Review”, “In Progress”, or “Approved”. Once you select one of
  these labels, a notification will be sent to all the project users.»** Se pueden crear campos propios
  (**«Manage Fields»**).
- Comentario a un fotograma: **«you can pause the video at the exact timecode of your note and type in
  the comments box […] the comment will be posted as a comment card and comment bubble marking the
  timecode position.»**; **«This timecode is exactly what the editor needs to be accurate and know where to
  make edits in the next version of this video.»**
- Comentario de rango: **«range-based comments […] showing a “point A to point B” area the comment is
  relevant for»**; con las teclas **«“I” and “O”»**.
- Comentario anclado en un punto de la imagen (**«Anchored comments»**) y anotación dibujada: **«You can
  add an arrow, draw a line, draw a box, or free draw any way you want.»**
- Comentarios internos: **«Internal Comments introduces a new private comment system that allows
  Workspace and Project members to have internal discussions that are never visible to external Share
  reviewers.»**
- Versiones: **«Create Version Stacks and manage your Version Saves to organize your clips' revisions
  rather than having multiple versions as individual files in your project.»**; **«the newest version
  will be ready to view»**; **«Access all of the versions by clicking the version number at the top of the
  page.»**; **«all asset types can be stacked in Frame.io.»**
- Comparar versiones: **«The Comparison Viewer in Frame.io V4 is the best way to compare all your assets
  side-by-side»**; en imágenes fijas, **«Pixel Difference»**: **«it will highlight the pixel differences
  between the two assets and letting you know exactly what has changed between them.»** (errata en el
  original); **«Static assets must have the same dimensions to use this feature.»**
- Guías de aspecto en el reproductor: **«you can use the frame guides to see what your asset would look
  like in different aspect ratios»**; **«The guides only impact the playback of your file and won’t alter
  the downloaded or uploaded file in Frame.io.»** (útil para revisar versiones de redes, tema 13).
- Lectura propia para el tema: la revisión eficaz es la que se ancla a un punto exacto (código de tiempo,
  zona de la imagen) y a una versión identificada; la aprobación es un estado explícito, no un «me
  parece bien» en un pasillo. Oficio.

### 14.4 Control de calidad: lo que da la casa

Fuente: X Convenio (BOJA 240, 10-XII-2014), leído el 29-09-2026. La ficha del Grafista no menciona el
control de calidad; sí las fichas por las que pasa su trabajo antes de emitirse:
- Secretario de Emisiones (5301010, p. 201): **«Coordinar los recursos técnicos y operacionales
  necesarios para el control de la calidad técnica del material audiovisual exigida para su emisión.»** y
  **«Recepcionar, comprobar y archivar el material programado.»**
- Editor de Continuidad (5302010, p. 125): **«Controlar la calidad de la imagen y del sonido de la
  emisión.»**
- Lo que se comprueba en grafismo (zonas seguras EBU R 95 y SMPTE ST 2046-1, niveles EBU R 103, alfa,
  HDR): bloque B, tema 8, y Realizador 12/14. El control ortográfico de rótulos: LE (tema 17 de este
  informe). No se ha encontrado una norma de control de calidad específica del grafismo.

### No confirmado (tema 14)

- Procedimiento de encargo y aprobación del grafismo en Canal Sur (no publicado).
- Normas de gestión de proyectos (ISO 21500/21502, PMBOK) no leídas: no citarlas.
- Versión completa en línea de la guía *The Client Brief* (anunciada en el PDF, no localizada).

---

## Tema 7 · Flujos de trabajo con realización, edición, producción, documentación y continuidad

Lo que ya dan los temas cerrados (copiar literal, no se repite):
- Montador 09 (asignado): ficha del Grafista (5345100, p. 129) y sus cuatro tareas; LE 3.16 «Gráficos»
  (pp. 57-58: cuatro o cinco elementos, ocho segundos, dinamismo, cama de audio, orden alfabético, texto
  rotulado, no se firma); circuito de rótulos escaleta → partes → Secretario/a de Redacción (**«Recepción
  de rótulos y comunicación a Realización.»**); rótulo «Archivo» (9.9.1); desconexiones provinciales;
  reparto editor/realizador/producción/documentación.
- **Realizador 12** (no asignado, muy útil): «Diseñar, rellenar y lanzar» (Viz Pilot Edge 3.5: diseño
  hace plantillas, redacción las rellena, control las emite), grafismo de directo frente a
  postproducción, tabla de reglas de rotulación del LE (3.6.1, 13.8.1, 11.2.6, «Siglas…», 10, 13.1.1.3,
  11.3.1.1.1, 13.3.1, 3.16.2, con páginas), zonas seguras, continuidad de la cadena y sus elementos
  (mosca, careta, cortinilla, autopromoción, rótulos de servicio, paquete gráfico), módulo 0904 del
  RD 1680/2011 e IMS077_3 UC0217_3 CR2.6; también cita UC0216_3 CR3.5 y CR3.6 (encargo del grafismo).
- Montador 13: MOS, NRCS (iNews de Avid en Canal Sur, Manfredi 2010), MAM.
- RTVE diseno-grafico/09 (continuidad) y 07: oficio sin fuente.

Lo que falta y se aporta: las fichas del convenio que tocan al grafismo desde las otras áreas, la
plantilla de grafistas, los criterios de la cualificación sobre verificación de grafismo en emisión y
en edición, y el operador de grafismo en directo (Viz Trio).

### 7.1 Las otras fichas: dónde entra el grafismo en el convenio

Fuente: X Convenio (BOJA 240, 10-XII-2014), anexos II y III, leído el 29-09-2026.

- Continuidad. Editor de Continuidad (5302010, p. 125): **«Participar a instancias de su superior en el
  diseño de elementos de continuidad.»** Y su objeto: **«Realizar la continuidad de la emisión siguiendo
  las pautas de la escaleta de continuidad.»** Es la única ficha, fuera de la del Grafista, que habla de
  diseñar elementos de continuidad: el grafista los diseña y realiza (**«todo tipo de imagen gráfica
  para programas y postproducciones, y otros fines promocionales»**), continuidad participa y los emite
  (lectura propia).
- Emisiones. Secretario de Emisiones (5301010, p. 201): **«Organizar, supervisar y gestionar la emisión,
  parrillas de programación y la escaleta de continuidad, así como los productos audiovisuales
  programados.»**; **«Recepcionar, comprobar y archivar el material programado.»** Por lectura, las
  piezas de continuidad y promoción que hace grafismo entran en emisión por esta vía.
- Desconexiones provinciales (convenio, disposición adicional segunda, «Desconexiones provinciales»,
  p. 86): entre las tareas **«Siguiendo las indicaciones del editor del informativo confección
  de la escaleta técnica y sus alteraciones, movimientos de cámara, iluminación, cabeceras, transiciones y
  rotulación.»** y **«Montaje de vídeos y Postproducción de titulares.»** (Montador 09 ya lo recoge como
  epígrafe del puesto; aquí interesa que cabeceras y rotulación de las desconexiones se operan en los
  centros provinciales, con el diseño que llega de grafismo: lectura propia, no dicho en el texto).
- Plantilla (anexo II, estructura IX CC / X CC): **GRAFISTA, CSTV, SEVILLA, B03, 9, 9** (p. 94) y
  **GRAFISTA, CSTV, MALAGA, B03, 1, 1** (p. 99). Es decir, diez grafistas en 2014, nueve en Sevilla y
  uno en Málaga. La plantilla actual no consta.
- Pregunta trampa: el Jefe/a de Sección de Diseño Asistido (9420000, p. 153) no es grafismo de antena
  (ver tema 12).

### 7.2 El grafismo en la cualificación de asistencia a la realización (INCUAL)

Fuente: INCUAL, cualificación profesional IMS077_3 «Asistencia a la realización en televisión», nivel 3
(fichero local del puesto de Realizador; publicación citada por Realizador: Orden PCI/797/2019), leída el
29-09-2026. Realizador 12 ya usa UC0216_3 CR3.5 y CR3.6; añadir:

- Encargo a grafismo (UC0216_3; si Realizador 12 lo tiene, copiar de allí): **«CR3.5 La relación de
  rótulos, las consideraciones formales marcadas por el realizador y el orden que presenta en la escaleta
  técnica se traslada al departamento de infografía supervisando el acabado y controlando que se ajuste a
  las necesidades y criterios marcados.»**; **«CR3.6 El material gráfico se captura y/o digitaliza,
  elaborando el grafismo 2D y/o 3D, minutándolo, organizándolo y trasladándoselo al grafista y
  supervisando el acabado.»**; **«CR3.7 El estado de las tareas se traslada al realizador y a producción
  evaluando con precisión si el proceso se encuentra dentro de los tiempos y medios estimados.»**
- Escaleta técnica (UC0216_3 CR1.3): **«La relación de músicas, efectos de sonido y luz, transiciones,
  gráficos, rótulos, envíos de señal a plató, necesidades de escenografía y atrezzo y demás aspectos
  formales previsibles, se elabora según las instrucciones que marca el realizador, incluyendo cada uno
  de los elementos en la escaleta técnica en el orden y posición indicados, reflejando los tiempos de
  duración de cada uno de ellos»**.
- Derechos de lo gráfico (UC0216_3 CR3.3): **«La gestión de los derechos de autor o de la propiedad
  intelectual de los recursos audiovisuales y gráficos se supervisa consiguiendo la titularidad de los
  mismos según la cobertura y el tipo de emisión del programa.»** (enlace con el tema 11).
- Verificación en emisión (UC0217_3, RP1): **«Verificar que las duraciones, calidades, efectos,
  grafismos, titulaciones, músicas, efectos de sonido e iluminación del programa de televisión son las
  previstas en el parte de emisión, informando de cualquier incidencia al realizador.»**; **«CR1.3 Las
  duraciones de videos, músicas, gráficos, rótulos y efectos de imagen y sonido se comprueban, anotándolo
  en el parte de emisión según criterio marcado por el departamento de realización.»**; **«CR1.6 La
  disponibilidad de la infografía necesaria para la rotulación de presentadores, invitados y totales se
  comprueba verificando que se trate de la plantilla empleada según el programa televisivo pertinente.»**
- Con edición y documentación (UC0218_3): **«CR1.2 La música, efectos de sonido, grafismo, y otros,
  solicitados por el realizador se identifican comunicando su ubicación y código de tiempo al equipo de
  realización mediante el protocolo establecido.»**; **«CR1.3 Los soportes de grabación se ingestan en el
  servidor en entornos digitales, cuando éstos existan, asociando su contenido al nombre dado en la
  escaleta técnica.»**
- Entorno: la cualificación nombra entre los sectores **«salas de postproducción y grafismo, archivos
  televisivos, departamentos de redacción»** (p. 1 de 25) y, entre las ocupaciones,
  **«Rotulistas»** (p. 2). Productos: **«Piezas de video, colas y totales, rótulos, grafismos,
  animaciones 2D y 3D»** (p. 5). Páginas del PDF: UC0216_3 CR1.3 p. 3, CR3.3-CR3.7 p. 4; UC0217_3 RP1 y
  CR1.3-CR1.6 p. 7; UC0218_3 CR1.2-CR1.3 p. 10.
- Lectura para el tema (propia): el flujo con realización va escaleta técnica → encargo con relación de
  rótulos y criterios formales → grafismo produce sobre plantilla → ayudante supervisa acabado y comprueba
  plantilla y duraciones en el parte → incidencias al realizador. El nombre en escaleta es la llave para
  que edición y documentación encuentren el gráfico.

### 7.3 Documentación: rótulos de advertencia que el LE obliga a poner

Fuente: LE (1.ª ed., 2004), leído el 29-09-2026 (Realizador 12 ya tiene «Reconstrucción» y «Archivo»:
comprobar y copiar de allí si coincide).
- **«quedan prohibidas, como norma general, las reconstrucciones y las simulaciones. Si son
  imprescindibles para la comprensión de una noticia importante, deberá hacerse constar mediante el
  rótulo 'reconstrucción' durante todo el tiempo en el que las imágenes ‘falsas’ estén en pantalla.»**
  (3.2.2, p. 46).
- Sucesos: **«cuando el recurso de un montaje de ficción sea inevitable, es obligatorio que, durante todo
  el tiempo de aparición de las imágenes en pantalla, figure el rótulo ‘Reconstrucción’.»** (9.2.12.3,
  «Reconstrucciones», p. 130).
- Archivo: **«En rotulación debe hacerse constar claramente que es material de ‘Archivo’ durante todo el
  tiempo en que la imagen permanezca en pantalla, al menos con suficiente margen como para ser leído sin
  apremio por el espectador.»** (9.9.1, p. 166).

### 7.4 Realización y grafismo en el LE: recursos y separadores

- **«En ello tienen gran importancia las crecientes posibilidades del medio: conexiones en directo, uso
  normalizado de satélites, presencia de otros centros de producción, infografías, ‘vidi wall’, pantallas
  de plasma... cuyo uso precisa cierto sentido estético y de una capacidad notable para aprovechar y
  armonizar los recursos disponibles.»** (6.5.2, p. 93).
- El realizador **«Tiene capacidad y autoridad para tomar, en cualquier momento, decisiones concretas
  referentes al modo, la forma y el diseño del informativo, con la salvedad de que deberá ceñirse a
  criterios de producción y a la supremacía del sentido informativo.»** (6.5.2, p. 93; ya en Realizador
  03).
- Piezas gráficas que nombra el LE: titulares **«montados en batería sobre una base de posproducción»**
  (3.6, p. 50); breves **«sobre una base de postproducción, con un efecto o ráfaga de separación de las
  informaciones»** (3.8, p. 52); colas **«separadas por un efecto visual generado desde el control de
  realización»** (3.9, p. 53); cierres: **«El coleo debe ser suficiente para incluir sin premura la
  despedida y los créditos.»** (3.10, p. 53).
- Coherencia de las desconexiones: **«están obligadas a aplicar un criterio de coherencia estética y
  conceptual con la edición general en la que se integran y de la que son tributarias.»** (7.4, p. 104).

### 7.5 Edición: entrega de gráficos a la sala

Remisión: alfa, ProRes 4444, TGA 32 bits (Realizador 12; Montador 04), .mogrt y Creative Cloud Libraries
(Montador 13), plantillas de Fusion (bloque B 9.2). No se aporta nada nuevo.

### No confirmado (tema 7)

- Cómo se piden y se entregan los gráficos en Canal Sur (sistema de pedidos, NRCS, servidor de grafismo):
  no publicado. El iNews de 2010 (Manfredi) es lo único con fuente (Montador 13).
- Si la casa tiene un departamento o área de Grafismo con ese nombre: el convenio sólo dice **«archivo de
  imagen del departamento gráfico»** (ficha 5345100).

---

## Tema 17 · Buenas prácticas de colaboración en plazos cortos y entornos de directo

Lo que ya dan los temas cerrados: Realizador 18 (asignado: comunicación, intercom, barreras, pacto y
ensayo, anticipar, estrés, decidir con presión, anotar y revisar); **Montador 14** (no asignado:
urgencia frente a calidad, demoras, cambios de última hora, cómo se comunican, versionado cadena/
desconexión, con LE 6.5.2 **«la urgencia acaba imponiéndose a cualquier otra consideración aunque no
puede hacerlo hasta el punto de anular un aceptable nivel de calidad»**); Realizador 12 (reglas de
rotulación del LE; plantillas; grafismo de directo); bloque B § 6.3-6.4 (Vizrt, Unreal Motion Design,
Chyron PRIME).

### 17.1 Urgencia y rótulo en el LE (lo propio del grafista)

Fuente: LE, leído el 29-09-2026.
- **«Los titulares, montados en batería sobre una base de posproducción, son la referencia de lo más
  importante, relevante y sugestivo de un informativo. Su elaboración, a causa de la urgencia, puede ser
  ardua y compleja, pero estas condiciones no deben servir como excusa para que dejen de ser una pieza
  precisa, veraz y breve, en la que se deben ahorrar palabras pero no se puede escatimar el rigor.»**
  (3.6, p. 50).
- **«El rótulo que acompaña es también información. Reúne brevedad, impacto y síntesis.»** (3.6.1,
  p. 50).
- Rotular previsto: **«Es necesario prever la inclusión de rótulos, al menos en una ocasión, muy
  especialmente cuando registremos primeros planos.»** (3.17.1.1, p. 59).
- Intro: **«Suele ser necesaria la rotulación con el dato del momento y el lugar donde se ha producido el
  hecho que mostramos.»** (3.13, p. 55).
- Totales en otra lengua: **«Es preferible que en un ‘total’ con una duración de diez o quince segundos,
  optemos por la rotulación a modo de subtítulos resumidos, especialmente en asuntos de especial gravedad
  o emotividad.»** (3.7.1, p. 52); **«En el caso de los subtítulos, eliminaremos interjecciones u
  onomatopeyas y el texto tendrá un carácter de síntesis que permita oír la voz original durante unos
  segundos, al menos al principio y al final de cada frase.»** (3.7.1, p. 52). (Realizador 12 cita estos
  dos últimos: comprobar.)
- Lectura propia: en plazo corto se sacrifican adornos, no la corrección del rótulo: todas las reglas de
  escritura de la tabla de Realizador 12 siguen obligando.

### 17.2 La plantilla como herramienta del plazo corto: el operador de grafismo en directo (Viz Trio)

Fuente: Vizrt, *Viz Trio User Guide* 4.6, «Introduction» (https://documentation.vizrt.com/viz-trio-guide/4.6/Introduction.html),
descargada y leída el 29-09-2026. La 4.6 es la última publicada (4.7, 4.8 y 5.0 dan 404 el 29-09-2026).
Ejemplo de mercado: **no consta** que Canal Sur use Vizrt.

- Qué es: **«Viz Trio provides all the features of a typical CG (Character Generator) system and
  more.»**
- Qué permite (literal, lista): **«Trigger graphical elements stored as pages in a show structure, with
  each page utilizing a unique call-up code.»**; **«Fill in data fields for graphics.»**; **«Quickly
  import or re-import new graphics into a show, no need for a template redesign, everything happens
  automatically.»**; **«Play clips with a timeline editor.»**; **«As a graphics playout server, integrate
  with third-party system, using macro commands over TCP/IP.»**; **«Customize the Viz Trio interface, with
  macros and scripting.»** Avanzado: **«Connect to multiple newsroom systems.»**; **«Perform seamless
  context switches on graphics (Transition Logic).»**; **«Produce on-the-fly graphics with the inbuilt
  design tool»**.
- Página y plantilla: **«The Viz Trio operator creates pages, most often from existing templates.»**;
  **«A page is an instance of a template, customized with data values, like sports results or election
  data.»**; **«When the page is ready, the Viz Trio operator simply sends the page and accompanying
  information, to air.»**
- Arquitectura: **«Viz Engine is the graphics rendering output system and Media Sequencer controls the
  playout of media elements.»**; **«Whilst Viz Trio, Media Sequencer and Viz Engine can be installed and
  operated on a single machine, for performance and security reasons they are usually installed on
  separate servers.»**
- Con la redacción: **«Viz Gateway can be used to connect Viz Trio to most newsroom systems using the MOS
  protocol.»** (MOS: Montador 13).
- Lectura propia para el tema: en directo, el grafista trabaja antes (plantillas, páginas preparadas con
  código de llamada) para que durante la emisión sólo haya que rellenar y lanzar; los resultados
  deportivos o electorales entran como datos, no como diseño nuevo.

### 17.3 Revisión rápida y trazable

Remisión al tema 14.3 (Frame.io: comentarios con código de tiempo, anotación sobre la imagen, versiones
apiladas, estados «Needs Review / In Progress / Approved» con aviso a todo el proyecto). En plazos cortos,
un estado explícito y una nota anclada al fotograma evitan la cadena de mensajes (lectura propia).

### No confirmado (tema 17)

- Protocolos internos de Canal Sur para grafismo en directo (elecciones, especiales): no publicados. El
  bloque A (tema 3, «Eventos especiales: casa y ley») tiene lo que consta.
- Una norma o guía publicada sobre «buenas prácticas de colaboración» específica de grafismo: no
  encontrada. Lo demás, oficio.

---

## Trazabilidad (fuentes de esta fase, todas leídas el 29-09-2026)

Orden de los temas en este informe: 13, 12, 14, 7, 17 (orden en que se investigaron).

| Fuente | Dónde | Temas |
|---|---|---|
| X Convenio Colectivo RTVA (BOJA 240, 10-XII-2014): anexo II (pp. 94, 99), disp. adic. 2.ª (p. 86), fichas 5302010 (p. 125), 5345100 (p. 129), 9420000 (p. 153), 5301010 (p. 201) | local | 7, 12, 14 |
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (RTVA, 1.ª ed., 2004): 3.2.2 (p. 46), 3.6 y 3.6.1 (p. 50), 3.7.1 y 3.8 (p. 52), 3.9 y 3.10 (p. 53), 3.13 (p. 55), 3.17.1.1 (p. 59), 6.5.2 (p. 93), 7.4 (p. 104), 9.2.12.3 (p. 130), 9.9.1 (p. 166) | local | 7, 13, 17 |
| INCUAL, IMS077_3 Asistencia a la realización en televisión: UC0216_3, UC0217_3, UC0218_3 | local (puesto Realizador) | 7 |
| Ayuda de YouTube, «Manage your channel branding» (answer/10456525) | support.google.com | 13 |
| Meta, Facebook Ads Guide, «Awareness Image Ad Specs on Instagram Reels» | facebook.com/business/ads-guide | 13 |
| Instagram Help Centre 1631821640426723 (sólo meta-descripción) | help.instagram.com | 13 |
| Vizrt, Graphic Hub Administrator Guide 3.9: «Overview», «General Database Information», índice | documentation.vizrt.com | 12 |
| Blackmagic Design, DaVinci Resolve 21 Reference Manual (julio 2026): pp. 95-96, 390, 392, 1480-1484 | PDF (copia en el directorio temporal de la sesión) | 12 |
| Design Council, «The Double Diamond» y «Framework for Innovation» | designcouncil.org.uk | 14 |
| IPA/ISBA/MCCA/PRCA, *The Client Brief* (PDF, s. f., investigación de 2002) | studiowide.co.uk (copia) | 14 |
| Frame.io V4 Knowledge Center: 9105311, 9105251, 9101068, 9952618 | help.frame.io | 14, 17 |
| Vizrt, Viz Trio User Guide 4.6, «Introduction» | documentation.vizrt.com | 17 |

Intentadas sin éxito: helpx.adobe.com (After Effects *Collect Files*, Premiere *Project Manager*): 403
el 29-09-2026. Ayuda de Instagram: contenido por JavaScript. TikTok: no consultado.

Oficio declarado como tal en el informe: traducciones de los nombres de fases, la casación del Doble
Diamante con el enunciado, la diferencia marca de agua / mosca, la lectura de flujos a partir de las
fichas y la cualificación, y las «lecturas propias» marcadas.

Ficheros tocados: sólo este informe.
