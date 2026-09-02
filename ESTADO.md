# Estado

Fichero de estado del apartado 11 del manual: qué es este temario, dónde vive
cada cosa, qué está hecho y qué falta. Se actualiza al final de cada sesión,
para que otra pueda seguir sin reconstruir nada.

**Última actualización:** 2026-09-02

## Qué es esto

Tres temarios de oposición de RTVE, por ocupación tipo: **Producción
(Asistencia)**, **Documentación** e **Información y Contenidos**. El programa
sale del ANEXO 2 de las bases, transcrito literal en `convocatoria/`.

Los tres comparten el mismo temario general y el mismo tema de prevención de
riesgos laborales, así que son **42 cuerpos de tema**, no 60. El reparto y el
orden están en `PLAN.md`.

**Convocatoria identificada**: son los anexos 2 de las **bases específicas de la
convocatoria 1/2022** (turno libre, adaptadas tras el acuerdo transaccional de la
Audiencia Nacional en los autos 154/2023) y de la **3/2022** (promoción interna y
cambio de ocupación tipo). El temario es el mismo en las dos. Las bases completas
están en `convocatoria/bases/` y los exámenes de octubre de 2024 en
`convocatoria/examenes/`.

**La prueba**: test de un mínimo de 80 preguntas más un 20 % de reserva, cuatro
opciones, acierto +1, error −1/3, blanco 0. En octubre de 2024 fueron 100
preguntas y 180 minutos en Información y Contenidos, y 80 preguntas y 120 minutos
en Documentación y en Producción (Asistencia).

## Hecho

- [x] Método y cláusulas de encargo en `metodo/`.
- [x] `herramientas/boe.py`: lector de legislación consolidada del BOE.
- [x] Programa transcrito literal: `convocatoria/PROGRAMA-GENERAL.md` y los tres
      `PROGRAMA-*.md` de específico.
- [x] Comprobado que el temario general es idéntico en los tres anexos, y que el
      tema de PRL también.
- [x] Identificadores del BOE de todas las fuentes del programa, localizados
      contra el BOE y no deducidos, en `convocatoria/FUENTES.md`.
- [x] Acceso probado fuente a fuente. Dos no se descargan (Manual de estilo de
      RTVE y el informe de la UNESCO): bloqueo del servidor, no del proxy.
- [x] Comprobado que el programa cita una foto de las normas anterior a la
      vigente, y en qué se nota (`convocatoria/FUENTES.md`).
- [x] `PLAN.md`: orden de trabajo y tratamiento de los temas sin norma detrás.
- [x] **Bases completas**: las específicas de las seis convocatorias que nos
      tocan y las generales de la 1/2022, con su transcripción, en
      `convocatoria/bases/`.
- [x] **87 exámenes de octubre de 2024 con sus plantillas de respuestas**,
      transcritos, en `convocatoria/examenes/`. El de Documentación es un
      escaneo y se pasó por OCR.
- [x] Calibración: reparto de preguntas por materia en las tres ocupaciones, en
      `informes/calibracion-examenes-2024.md`.
- [x] **Exámenes de convocatorias anteriores** en `convocatoria/examenes-antiguos/`:
      la convocatoria 1/2020 (pruebas de diciembre de 2021 y enero de 2022, con
      plantillas) y la de 2007, más sueltos de 1999, 2002, 2009, 2010 y 2011.
      Transcritos, con OCR los que hacía falta.
- [x] Comprobado que **las preguntas se repiten**: entre ocupaciones de la misma
      convocatoria y entre convocatorias, a veces palabra por palabra
      (`informes/preguntas-repetidas.md`).
- [x] **`banco/`: 510 preguntas reales** —480 del bloque común y 30 del tema de
      prevención del específico—, **todas con su respuesta oficial**. Y aparte,
      **123 del bloque específico de Producción (Asistencia)**, también todas con
      respuesta oficial.
      Sustituye a las preguntas inventadas del apartado 7 del manual.
- [x] **El volumen, listo para el opositor** (`informes/mejoras-formato-2026-08-30.md`):
      sin una sola referencia a ficheros del proyecto, con **encabezado y pie**
      —portada limpia—, **índice a tres niveles con número de página y clicable**
      en PDF y en Word, **marcadores** en el PDF, cuerpo justificado y preguntas
      sin la línea de procedencia.
- [x] **Las preguntas del banco tienen todas respuesta oficial.** Las tres plantillas cuyo PDF
      no lleva tabla de caracteres se leen **celda a celda**
      (`herramientas/plantilla_ocr.py`), contrastadas contra la imagen y contra
      preguntas repetidas. **El cuaderno de pendientes queda vacío.**
- [x] **Segunda prueba de cobertura**, sobre las **111 preguntas** que la pasada de
      verificación añadió y que nunca habían pasado el apartado 7 del manual
      (`informes/cobertura-nuevas-2026-08-30.md`): **102 se contestaban** y **9 no**.
      Las nueve lagunas, cerradas contra la fuente —**los artículos 10, 11 y 22 y el
      teletrabajo fuera de horario en el tema 5**; **la respuesta de la Guía a «¿y si la
      víctima es un hombre?» en el 6**; y **el múltiplex, el productor independiente y
      los artículos 145, 146.3 y 150 en el 7**—. **Con esto, las preguntas del banco se
      contestan todas con el tema delante.**
- [x] **Pasada de verificación sobre el banco**, leyendo las preguntas una a una
      (`informes/verificacion-banco-2026-08-30.md`): el salto de página fundía
      **83 preguntas** con la de al lado, cinco cuadernillos ilegibles no
      aportaban **93 más** y nada daba error, y **113 estaban en el cajón
      equivocado**. Las correcciones viven en `banco/reclasificadas.tsv`, que
      `banco.py` aplica al regenerar y cuyas filas huérfanas avisa.
- [x] `herramientas/word.py`: el mismo volumen en **.docx con estilos de Word con
      nombre** y **sin una sola línea de formato a mano**, para poder darle el formato
      en Word y devolverlo. Lo que vuelva en `word/styles.xml` se traslada al CSS de
      `libro.py`. `--temas 1` saca solo un tema.
- [x] `herramientas/boe.py --fecha AAAAMMDD`: lee la ley como estaba ese día.
- [x] Las tres lentes de refutación, automatizadas y reutilizables en cualquier
      tema: `refutar_exactitud.py`, `refutar_modo.py` y `refutar_prosa.py`.
- [x] **`boe.py` avisa de la vacatio**: si un bloque existe en el texto publicado pero su
      entrada en vigor es posterior a la fecha leída, el volcado deja **el rótulo con el
      aviso y la fecha**, y el resumen los enumera. Antes los omitía en silencio y el rastro
      quedaba solo en el `.tsv`: en la Ley 13/2022 eran **quince bloques**, dos de ellos
      preguntados en el examen.
- [x] `herramientas/refutar_documento.py`: cuarta lente, para temas cuya fuente **no es
      articulado** (un plan, una guía, un manual). Contrasta cada negrita y **cada cifra**
      contra el texto completo de las fuentes. Hace falta porque las lentes por artículo
      devuelven «0 comprobadas, 0 hallazgos» sobre un documento sin artículos, que se lee
      como un tema impecable y es un tema sin revisar.
- [x] `herramientas/convenio_dump.py`: reconstruye el articulado del convenio en
      vigor superponiendo el acuerdo de 2022 sobre el texto de 2020, con la forma
      que esperan las lentes. Hace falta porque **el convenio no es legislación
      consolidada**: el BOE no publica texto refundido y `boe.py` no sirve.
- [x] **Comprobados todos los acuerdos del Convenio Colectivo**, por el bloque de
      «referencias posteriores» de su ficha en el BOE. **Anteriores al corte son cuatro, no
      tres**: faltaba `BOE-A-2021-8252` (18/05/2021), que sustituye entero el anexo 7.
      Posteriores al corte hay otros cuatro (2023 ×2, 2024 y 2025), anotados como nota de
      actualización en el tema; el de agosto de 2023 toca los artículos 42, 50, 52, 57, 72
      y 91, así que **cualquier material posterior a esa fecha da cifras que no son las del
      examen**.
- [x] **Descubierto que partes del convenio solo existen como imagen** en el BOE:
      la tabla de niveles del artículo 65 y los anexos 1, 2 y 3 completos. No están
      en el HTML ni en la transcripción de texto, y su ausencia no da ningún aviso.
      Descargadas y **transcritas las cinco** en `fuentes/convenio/imagenes/`: la tabla
      del artículo 65 y los anexos 1, 2 y 3.
- [x] **Los nueve temas llevan portada e índice, y los nueve esquemas llevan índice**,
      generados con `herramientas/indice.py` y **regenerables**: un índice escrito a mano se queda viejo al
      primer epígrafe que se añade, y un índice viejo no da error, lleva a otro sitio. La
      portada dice bloque del programa, fuente, identificador, redacción que se estudia,
      extensión medida y dónde están el esquema y los informes. **El script comprueba que las
      rutas que cita existen**, y así se descubrió que **los temas 2 y 3 citaban un informe de
      refutación que nunca se había escrito**: reconstruido en
      `informes/refutacion-temas-02-03.md`, marcado como reconstrucción.
      El **esquema no lleva portada** —la ficha de la norma está en su tema y repetirla sería
      ruido—, y el **índice va justo antes del primer epígrafe**, para no enterrar la
      entradilla bajo veinte líneas de enlaces.
- [x] **Corregido cómo se miden las palabras.** Todas las cifras de extensión publicadas hasta
      el 2026-08-30 salían de `wc -w` **en locale C**, que **cuenta de menos en texto
      acentuado**: el esquema del tema 8 no eran 3.856 palabras sino **3.966**, y el del
      específico de PRL no 2.802 sino **2.937**. Las líneas se contaban además **con las
      vacías**. Corregidas en los informes, con la causa dicha. `indice.py` mide con separación
      de palabras Unicode, así que las portadas ya nacen bien.
- [x] **Las cuatro lentes ignoran la portada y el índice** (`herramientas/tema.py`, una sola
      función compartida). Sin eso, el envoltorio metía **ocho falsos «no literales» y una
      cifra huérfana por tema**: ruido que acaba enseñando a no mirar la lista.
- [x] **Cuaderno de pendientes vaciado (2026-08-30).** Los ocho hallazgos que había están
      cerrados: **cuatro investigados y aplicados** —la entrada en vigor de la DF cuarta de la
      Ley 13/2022, la fecha de cese del artículo 155, el número de senadores y el interruptor
      diferencial— y **cuatro que no eran trabajo pendiente** sino erratas comprobadas de
      plantillas y decisiones ya tomadas, mal archivadas bajo el epígrafe «Aplicados». El
      fichero se ha reorganizado en cuatro secciones y **conserva todo el histórico**.
      **Dos de las cuatro resoluciones fueron en contra de lo que la propia anotación decía**:
      la de la Ley 8/2009 la daba por irrelevante para el examen y sí lo era, y la del
      diferencial acusaba a la plantilla oficial de un error que no había.
- [x] **Bloque común cerrado: los 8 temas del general y el de PRL del específico**, que sirve
      para las tres ocupaciones como **P18 / D7 / I11**. Con eso está hecho todo lo que rinde
      por tres.
- [x] **`refutar_documento.py` cose las palabras que el PDF parte al final del renglón.**
      Cambiaba el guion por un espacio y una cita literal salía marcada como «no literal»; y la
      clase de caracteres era el rango `U+2010..U+2015`, que **no incluye el guion normal**, así
      que el primer arreglo no movió ni una cifra. Corregido: **26 falsos «no literales»** menos
      en el tema de PRL, y ninguno en el tema 6, que es el otro que usa esta lente.
- [x] **Fuentes del tema de PRL del específico** en `fuentes/prl-especifico/`: Guía Técnica de
      pantallas del INSST (junio 2021), documento del INSST sobre TME de la extremidad superior,
      NTP 536, NTP 1090 y 1091, informe de Seguridad Vial Laboral de la CNSST y la ficha de
      doctrina del Tribunal Supremo sobre in itinere y en misión, con sus transcripciones.
- [x] **Las lentes ven los artículos «bis»**: el patrón de la fuente estaba anclado en
      `Artículo (\d+)$` y **«Artículo 32 bis» no acaba en dígito**, así que no entraba en el
      diccionario, **no se comprobaba nunca** y además su texto en el tema se contrastaba
      contra el artículo 32, que dice otra cosa. Corregido en `refutar_exactitud.py` y
      `refutar_modo.py`, con las claves hechas cadenas.
- [x] **Una remisión dentro de una frase ya no abre epígrafe**: «conoce las actuaciones de los
      **artículos 7, 8, 9 y 11**» abría bloque y toda la explicación posterior se comprobaba
      contra el artículo 7. Ahora el marcador que **abre epígrafe** manda sobre su párrafo y el
      que va **dentro de una frase** se queda solo con su frase. El primer intento —descartar
      todos los marcadores de dentro de frase— dejó **catorce artículos del tema 7 sin mirar**,
      y se detectó porque **la cifra de negritas comprobadas bajó al «arreglarlo»**.
- [x] **Fase B arrancada. Tema 2 del específico de Producción (Asistencia)** —derechos de
      autor, Ley de Propiedad Intelectual y redes sociales— **cerrado**: 15.300 palabras sobre
      dos fuentes volcadas a la fecha de corte, el texto refundido `BOE-A-1996-8930` y el
      **Libro cuarto** del RDL 24/2021 (`BOE-A-2021-17910`), que es donde está el régimen de
      las plataformas y **no** en la ley que cita el enunciado. Las **nueve** preguntas reales
      de la materia se contestan con el tema delante
      (`informes/cobertura-produccion-tema-02.md`), y las cuatro lentes dejaron **once
      correcciones aplicadas** (`informes/refutacion-produccion-tema-02.md`). Con su **esquema
      de repaso**, 4.432 palabras y 117 líneas de telegrama, en el rango del de la Constitución
      y sin crecer en proporción al tema.
- [x] **Tema 17 del específico de Producción (Asistencia)** —Ley de Protección de Datos—
      **cerrado**: 13.282 palabras sobre **dos normas**, la LO 3/2018 (`BOE-A-2018-16673`) y el
      **Reglamento (UE) 2016/679**, que hizo falta traer entero porque la ley orgánica **no repite
      lo que el Reglamento dice** y remite a él en casi todos sus artículos. Las **cinco**
      preguntas reales se contestan con el tema delante
      (`informes/cobertura-produccion-tema-17.md`), y las lentes dejaron **nueve correcciones
      aplicadas** más dos arreglos de herramienta
      (`informes/refutacion-produccion-tema-17.md`). Con esquema de repaso.
- [x] `herramientas/doue.py`: lector de **normas de la Unión Europea publicadas por el BOE** en su
      sección del Diario Oficial. Trocea el articulado con la misma forma que espera `boe.py`, para
      que las lentes trabajen sobre un reglamento europeo igual que sobre una ley española;
      **recoge las correcciones de errores** que el BOE enlaza y las guarda enteras; y **dice en la
      cabecera que el texto no está consolidado**. Hacía falta porque `boe.py` sólo sirve para
      legislación española consolidada, y el Reglamento no lo es: sus **dos correcciones de
      errores** son documentos aparte que nadie incorpora al texto.
- [x] **Dos fallos de cobertura destapados y corregidos** al escribir este tema, los dos del
      apartado 10 del manual:
      **(a)** `refutar_modo.py` traía **«habrá de» en singular y no en plural**, así que marcaba
      como cambio de modo verbal el artículo 89.1 de la LO 3/2018, que dice «**habrán de
      informar**». Corregido y repasados los temas cerrados: no movió ninguna cifra.
      **(b)** Los **artículos 80 a 86** iban en una tabla cuya primera columna era un **número
      suelto en negrita**, que la lente no reconoce como marcador: **siete artículos se
      contrastaban contra el artículo 79** y no daba error, daba dieciocho «no literales» que
      parecían ruido. Arreglado escribiendo la columna como `**Art. 80**`.
- [x] **Comprobado que el enunciado y la fecha de corte coinciden en este tema**: la última
      reforma del texto refundido anterior al 21/12/2022 es la del **artículo 177**, publicada
      el **30 de marzo de 2022**, que es literalmente el «texto consolidado BOE 30 de marzo de
      2022» que cita el Anexo 2. Entre esa fecha y el corte la ley no se volvió a tocar.
- [x] **Tema 10 del específico de Producción (Asistencia)** —imagen y sonido: captación y
      tratamiento— **cerrado**: 5.228 palabras, con esquema de repaso. Es **el primer tema del
      proyecto sin norma jurídica detrás**, y por eso el primero que aplica entera la jerarquía de
      fuentes: **siete de sus diecisiete preguntas tienen norma o recomendación**
      —**UIT-R BT.601-7**, **UIT-R BT.2100-1**, **RD 2032/2009** y el **DB-HR** del Código
      Técnico— y **las diez restantes se apoyan en la plantilla oficial y el uso profesional,
      marcado una a una**. Las diecisiete se contestan con el tema delante
      (`informes/cobertura-produccion-tema-10.md`).
- [x] **Dos fuentes más, encontradas al escribirlo**: la definición del **tiempo de reverberación**
      —caída de **60 dB**— no necesitaba la ISO 3382, está en el **anejo de terminología del
      DB-HR** publicado en el BOE (`BOE-A-2007-18400`); y la **AES**, aunque no deja leer la
      AES10, publica la frase que identifica **MADI = AES10**.
- [x] **Cazado un error de la fuente, no del tema**: la extracción de texto del PDF de la
      BT.601-7 daba «**16,75 MHz**» donde la recomendación dice **6,75 MHz**. Saltó porque no
      cuadraba con el resto del cuadro —720 frente a 360 muestras—, y se confirmó **recortando y
      ampliando esa celda del PDF para leerla a ojo**. Con una norma técnica en PDF, **el texto
      extraído no es la fuente; la página lo es**.
- [x] **Quitadas del tema 10 dos cifras que no tenían fuente** —las frecuencias de muestreo de
      audio de estudio—: eran correctas y habrían pasado desapercibidas, pero **no estaban
      comprobadas** y ninguna pregunta las pedía. Apartado 1 del manual aplicado tal cual.
- [x] **Tema 9 del específico de Producción (Asistencia)** —escenografía e iluminación, nuevas
      tendencias— **cerrado**: 3.970 palabras, con esquema de repaso. Es **el tema más preguntado
      de todo el bloque específico** —**20 de las 123**, una de cada seis— y **el peor servido de
      fuentes**: sólo **cuatro preguntas tienen norma detrás** —el **RD 2032/2009** para el lumen,
      la **ITC-BT-24** del Reglamento electrotécnico para baja tensión para la toma de tierra del
      practicable, el **cuadro 1 de la UIT-R BT.601-7** para el complementario del magenta y la
      física para la transmisión de la luz—. **Las dieciséis restantes se apoyan en la plantilla
      oficial y el uso profesional, y el tema lo marca una a una y lo dice en su portada.** Las
      veinte se contestan con el tema delante (`informes/cobertura-produccion-tema-09.md`).
- [x] **Corregido un fallo de método que había cerrado tres fuentes buenas.** El tema 9 se cerró
      declarando que **las cuatro fichas de fabricante no se habían podido consultar**. Al empezar
      el tema siguiente se volvió a intentar y **tres estaban disponibles todo el tiempo**: la ruta
      de LiveU estaba mal escrita (`/products/lu300s` da error; `/lu300s`, no) y Astera **filtra
      por agente de usuario** (devuelve «prohibido» a la petición automática y la página entera a
      un agente de navegador). **Una conclusión negativa es la más cara de todas, porque cierra la
      búsqueda**: nadie vuelve a mirar donde ya está escrito que no hay nada.
      **Regla nueva, aplicable a todo lo que queda**: antes de escribir «no se ha podido
      consultar», dos rutas y un agente de navegador. Con la regla puesta se recomprobaron las tres
      que seguían declaradas inalcanzables y **esta vez la declaración se sostiene**: la **UER**
      responde «prohibido» también con agente de navegador, **DCI** es una aplicación de JavaScript
      que no sirve documentos por ruta estática, y de la **AES10** sólo hay la línea de identidad.
- [x] **Tema 9 rehecho con las fichas que sí existen** (`fuentes/fabricantes/`, con su README):
      **Mo-Sys resultó ser el fabricante del StarTracker**, de modo que el examen **pregunta dos
      veces por el mismo fabricante**; el enunciado del «sensor apuntando al techo» resultó ser
      **la ficha palabra por palabra** —estrellas retrorreflectantes, seguimiento absoluto «de
      dentro hacia fuera»—; y el adjetivo «**alemana**» de la respuesta del Titan Tube, que la
      primera versión había quitado por no poder confirmarlo, **tiene documento**: el informe de
      ensayo de seguridad fotobiológica identifica a **Astera LED Technology GmbH, de Múnich**.
      El tema pasa de «4 con norma, 16 con la plantilla» a **4 con norma, 3 con ficha, 13 con la
      plantilla**. **Sólo ORAD sigue sin ficha**, y es la respuesta más frágil del bloque.
- [x] **Señalado un enunciado invertido del examen** (77 · 78): pide la tecnología de «superponer
      una imagen real sobre el entorno virtual» cuando la realidad aumentada superpone **lo virtual
      sobre lo real**. El tema contesta lo que el tribunal corrige —realidad aumentada— **y avisa
      del error**, porque quien razone bien se bloquea ahí.
- [x] **Un dato sin fuente colado en una corrección de estilo, cazado a tiempo.** Al glosar la
      sigla ORAD se escribió «hoy integrado en Avid», que **no sale de ninguna fuente leída**: un
      dato de memoria metido en un arreglo de forma, que es donde menos se mira. Lección:
      **una corrección de forma introduce datos sin fuente igual que una redacción nueva.**
- [x] **Buscados y eliminados los homóglifos.** Una **«а» cirílica** se había colado en la palabra
      «visera» del tema 9. No la marca ninguna lente, el texto se ve idéntico y rompe cualquier
      búsqueda. Comprobación que conviene repetir en cada tema nuevo.
- [x] **Tema 11 del específico de Producción (Asistencia)** —medios de transmisión de señal, envío
      de imágenes y comunicaciones— **cerrado**: 4.529 palabras, con esquema de repaso. Es la
      **tercera materia más preguntada** del bloque —**10 preguntas**— y **la mejor servida de
      fuentes hasta ahora**: **siete de las diez** tienen norma, recomendación o ficha detrás
      —**Ley 11/2022**, **Plan Técnico Nacional de la TDT**, **Ley 13/2022**, **UIT-R S.673-2**,
      **UIT-R SNG.770-2**, **UIT-T G.984.1**, **ETSI EN 300 744** y **EN 302 755**, índice de la
      **SMPTE ST 2110** y ficha de **LiveU**—. Las tres restantes —streaming, señal Pool y los
      datos de acceso al satélite— se apoyan sólo en la plantilla, y van marcadas
      (`informes/cobertura-produccion-tema-11.md`).
- [x] **Tercera puerta abierta que estaba dada por cerrada: el ETSI.** Con la regla del tema 9
      —dos rutas y un agente de navegador— la norma europea del DVB **se descargó a la primera**.
      Y cambió el tema: la sigla **DVB** pasó de ser un dato de memoria a estar **en el título de
      la norma** («Digital Video Broadcasting»), y la asociación con el **MPEG-2** que el enunciado
      hace pasó de tratarse como imprecisión histórica a ser **literal de la norma** —«establecer
      el marco para la introducción de la televisión digital basada en MPEG-2»—. **Tres de tres**:
      durante buena parte del proyecto, «no se ha podido consultar» ha significado en realidad
      «no se ha sabido pedir».
- [x] **Un aviso sobre el alcance de la lente de documento**, anotado al refutar el tema 11: sólo
      mira **las negritas**, así que **una cifra en texto corriente pasa por delante sin sonar**.
      Los **36.000 km** de la órbita geoestacionaria son ese caso: se detectaron a mano, buscando
      en la recomendación las tres altitudes de la escala y viendo que sólo hay dos.
- [x] **Tema 13 del específico de Producción (Asistencia)** —equipos técnicos de exteriores—
      **cerrado**: 2.946 palabras, con esquema de repaso. Es **un tema partido en dos**: las **tres
      preguntas del dron y del estabilizador** se contestan con documento delante —**Reglamento
      (UE) 2019/947**, **reglamento del aire (SERA)**, **RD 1036/2017**, **AIP de España** y la
      **lista de compatibilidad de DJI**—, y las **cuatro de vocabulario** —*beauty shot*, *TV
      compound*, *mobycam*, *mojo*— **no tienen más autoridad que la plantilla**, y van marcadas.
- [x] **Estrenado el tercer nivel de la jerarquía de fuentes**, que estaba declarado desde el
      informe de fuentes y **no se había usado ni una vez**: `fuentes/institucionales/`, con el
      **AIP de España, sección ENR 5.1**, publicado por **ENAIRE**. Hacía falta porque el
      reglamento del aire define **qué es** una zona peligrosa pero **no dice con qué letras se
      rotula**: quien clasifica el espacio aéreo en **P**, **R** y **D** y numera las zonas
      peligrosas españolas **LED1, LED2…** es el AIP. **Dos fuentes para una pregunta**, y con las
      dos se contesta sin memorizar nada suelto.
- [x] **Corregida una atribución falsa antes de publicarla**: el primer borrador del tema 13 daba
      por dicho en el reglamento europeo que el operador de dron se registra **ante AESA**. El
      reglamento dice «**el Estado miembro**» y **no nombra a AESA**; el nombre lo pone el
      **RD 1036/2017**, artículo 6.1. La respuesta se parte en dos y **se enseña la costura**.
- [x] **Una cifra huérfana que era una comprobación positiva.** La lente marcó los **350 gramos**
      como cifra sin fuente, y eso era justo lo que el tema afirmaba: **ese umbral no existe en
      ninguna norma** —el reglamento maneja **250 g**—. Queda anotado que la lente **no dice «esta
      cifra está mal», dice «esta cifra no está en tus fuentes»**, y que a veces eso es la prueba
      que se buscaba.
- [x] **Cuarta fuente recuperada con la regla del agente de navegador: DJI.** Y dos que **sí están
      cerradas de verdad**, comprobadas con la regla puesta: las páginas de producto de **Sony** y
      la del fabricante de la **mobycam**, que responden «prohibido» también con agente de
      navegador.
- [x] **Tema 1 del específico de Producción (Asistencia)** —la producción: sistemas y métodos—
      **cerrado**: 2.133 palabras, con esquema de repaso. Entró en el reparto como **vocabulario
      puro sin fuente**, y resultó tener **dos preguntas con norma literal detrás**: el
      **artículo 8 del III Convenio Colectivo de la Corporación RTVE** recoge las definiciones de
      **producción interna, mixta y ajena** aprobadas por la comisión de producción interna, y la
      de **ajena** es **palabra por palabra la respuesta oficial**; el mismo artículo, al definir
      la interna, **enumera las tres fases** y contesta la otra pregunta.
- [x] **Regla nueva, hermana de la del agente de navegador**: antes de escribir «esto es
      vocabulario sin norma», **hay que buscar el término en las fuentes que ya están en casa**.
      Son ocho leyes, un convenio y una docena de normas técnicas; la búsqueda cuesta un minuto y
      **ya ha pagado**. Una conclusión negativa sin comprobar cierra la búsqueda igual que un
      «no se ha podido consultar» sin comprobar.
- [x] **Tema 3 del específico de Producción (Asistencia)** —el guion— **cerrado**: 2.226 palabras,
      con esquema de repaso. Es **el tema con peor respaldo documental de todo el temario**:
      **ninguna de sus 6 preguntas tiene norma detrás**. Y la declaración está **comprobada**, no
      supuesta: los seis términos se buscaron en todas las fuentes volcadas; **cinco no aparecen ni
      una vez** y el sexto, «secuencia», sólo dentro de «en consecuencia» o «secuenciación». El
      único apoyo normativo es el **artículo 87 de la Ley de Propiedad Intelectual**, y **no
      contesta ninguna pregunta**.
- [x] **Un cero de la lente que era un fallo de redacción, no de la herramienta.** La lente de
      exactitud devolvió **0 comprobadas** sobre el tema 3, que es el resultado engañoso del
      apartado 10. La causa: el tema citaba «**en su artículo 87**» **dentro de una frase**, y la
      lente sólo da su propia frase a los marcadores interiores para que una remisión no arrastre
      texto ajeno. Reescrito para que **el marcador abra párrafo**, pasó de **0 a 4 comprobadas**.
      **Cuando una lente devuelve cero, la primera sospecha es que no ha mirado.**
- [x] **Tema 7 del específico de Producción (Asistencia)** —equipos humanos— **cerrado**: 2.258
      palabras, con esquema de repaso. La regla del tema 1 volvió a pagar, **pero a medias, y hay
      que decir en qué mitad**: el **artículo 38 del III Convenio** da **los trece ámbitos
      ocupacionales** y su **anexo VIII** las **ocupaciones tipo**, lo que **prueba que vestuario,
      decorados, realización y documentación son ámbitos distintos** —el supuesto sobre el que dos
      preguntas están construidas—; pero **ninguno de los seis oficios está nombrado en el
      convenio**, buscados uno a uno. **La fuente sostiene el armazón de la pregunta, no la
      respuesta**, y el tema lo escribe tres veces para que no se pierda al resumir.
- [x] **Regla de escritura, no de herramienta, tras el segundo cero de lente en dos temas**: cuando
      un tema cite un artículo, **el marcador tiene que abrir el párrafo**. Enterrado en una
      subordinada —«en su artículo 38…»—, la lente sólo mira esa frase y **la cita que viene detrás
      no se comprueba y no se queja**. Corregido, el tema 7 pasó de **2 a 12 negritas comprobadas**.
- [x] **Enunciada como práctica constante lo que ya se venía haciendo**: cuando la respuesta oficial
      y la fuente no coinciden del todo —el enunciado invertido de la realidad aumentada, el MPEG-2
      del DVB, el mando del escenógrafo sobre vestuario frente a la clasificación del convenio—,
      **se contesta como corrige el tribunal y se escribe la discrepancia al lado**.
- [x] **Tema 8 del específico de Producción (Asistencia)** —formatos y soportes— **cerrado**: 2.734
      palabras, con esquema de repaso. **Tres de sus seis preguntas tienen norma o recomendación
      detrás**: la **UIT-R BT.2100-1** da la definición literal del **HDR** —«realces mucho más
      brillantes y mayor detalle en las zonas oscuras»— y los **tres cómputos de píxeles del
      contenedor**, y el **Plan Técnico Nacional de la TDT** exige **2 160 líneas activas** en
      ultraalta definición. Las tres restantes —**SxS Pro**, **internegativo** y el origen de las
      **24 imágenes por segundo**— se apoyan sólo en la plantilla.
- [x] **Un distractor que resultó no ser falso, y obligó a reescribir un epígrafe.** La opción c)
      de la pregunta de las 24 imágenes por segundo dice que es «un estándar temporal opcional que
      se utiliza en televisión», y **la recomendación incluye 24 y 24/1,001 entre sus frecuencias
      de trama**. La pregunta no se decide por verdad o falsedad, sino por **cuál de dos
      afirmaciones ciertas contesta lo preguntado**, y lo decide una palabra: **«tradicionalmente»**.
      El tema reconoce que el distractor es bueno y **explica la regla que lo desempata**, en lugar
      de simplificarlo hasta que parezca malo.
- [x] **Señalado otro enunciado confundido del examen**: pide «lo que la **DCI 4K** estandariza
      **para televisión**», y la DCI **estandariza cine**: su 4K es **4 096 × 2 160**, no
      **3 840 × 2 160**. El tema contesta lo que el tribunal corrige **y enfrenta las dos normas en
      una tabla**.
- [x] **La especificación DCI, recomprobada con cinco rutas y agente de navegador: sigue cerrada.**
      Su servidor responde pero es **una aplicación de JavaScript que no sirve documentos por ruta
      estática**. La cifra 4 096 × 2 160 queda **declarada sin respaldo en el propio párrafo donde
      se usa**, no sólo en la trazabilidad.
- [x] **Segundo caso de cifra huérfana que es comprobación positiva** —tras los 350 gramos del tema
      de exteriores—: la lente marcó **4 096** y **3 840 × 2 150** como cifras sin fuente, y eso era
      justo lo que el tema afirmaba de las dos. **Cuando el tema cita una cifra para negarla, la
      lente la marca, y esa marca es la prueba.**
- [x] **Tema 12 del específico de Producción (Asistencia)** —el estudio de televisión— **cerrado**:
      2.098 palabras, con esquema de repaso. **Cinco de sus seis preguntas se apoyan sólo en la
      plantilla** —los seis términos se buscaron en todo el corpus y no aparece ninguno—, y la
      sexta se salvó con **una ficha de fabricante encontrada con la regla del agente de
      navegador**: la portada de **Autocue** se titula «Autocue®: Innovating Prompting Since 1955»
      y **llama «teleprompters» a sus propios aparatos**, lo que convierte la respuesta «no se
      diferencian en nada» de dato que hay que creerse en **algo comprobable**: no son dos
      aparatos, son **un aparato y una marca**.
- [x] **Recuento de fuentes, al día**: **cinco recuperadas** con la regla del agente de navegador
      —LiveU, Astera, ETSI, DJI y Autocue— y **cuatro cerradas de verdad, comprobadas con la regla
      puesta** —UER, DCI, Sony y Avid, esta última con **ocho rutas probadas**—.
- [x] **Una lección menor sobre cómo se corre la lente de documento**: la primera pasada del tema 12
      devolvió **once cifras huérfanas**, y ninguna era un error: eran **designaciones de normas que
      el tema sólo menciona de pasada** y cuyas fuentes no se le habían pasado a la lente. Corregido
      el conjunto de fuentes, quedaron **dos**, las dos metadatos. **Cuando la lista de huérfanas
      incluye designaciones de normas, el problema está en qué se le ha dado a comparar.**
- [x] **Tema 14 del específico de Producción (Asistencia)** —documentación internacional para
      desplazamientos— **cerrado**: 2.521 palabras, con esquema de repaso. **Cuatro de sus seis
      preguntas son sobre el cuaderno ATA**, y las cuatro se contestan con documento delante: el
      **Convenio relativo a la importación temporal, hecho en Estambul** —anexo A, artículos 1, 5.1
      y 6— y las **fichas de la Cámara de Comercio de España**. Las dos restantes —el bono de
      exceso de equipaje y la tarjeta de prensa de Israel— se apoyan sólo en la plantilla, **y sus
      fuentes están cerradas**, comprobado con la regla del proyecto.
- [x] **Arreglado un fallo de las lentes que este tema destapó, y que no daba ningún error.**
      `refutar_exactitud.py` y `refutar_modo.py` indexaban la fuente **por número de artículo**, con
      un diccionario que sobrescribe. El **Convenio de Estambul no es una ley: es un tratado con
      anexos, y cada anexo numera desde 1** —hay **quince «Artículo 1»**—, así que sólo sobrevivía
      el último y **todo lo demás se contrastaba contra el artículo equivocado, en silencio**. Es
      el fallo del apartado 10, y la misma trampa que `herramientas/doue.py` ya evitaba con un aviso
      de números repetidos **que a las lentes se les había olvidado poner**. Ahora **guardan todas
      las versiones y las comprueban juntas**, y **avisan por escrito** de que la atribución por
      número no es fiable en esa fuente. Las no literales del tema 14 bajaron de **34 a 25**: nueve
      eran falsos positivos.
- [x] **Comprobado que el arreglo no mueve ninguna cifra anterior**: se revisaron todas las fuentes
      volcadas y **sólo el Convenio de Estambul repite números de artículo**. Ningún tema anterior
      lo usaba con las lentes por artículo.
- [x] **Una fuente de primer nivel que decía lo contrario, y cómo se resolvió.** La relación de
      **estados parte** que el BOE publicó con el Convenio de Estambul —**de 1997**— **no incluye a
      Irán** e incluye a **Ghana como firmante sin ratificar**, justo al revés de la respuesta
      oficial. No era un error del tribunal: era **una lista caducada**. La lista viva la lleva la
      **Cámara de Comercio**, y en su documento fechado el **20/08/2026** están los **82
      territorios**, con **Irán** y sin los otros tres. **Regla nueva: cuando una pregunta depende
      de una lista que cambia, el tratado no es la fuente; la fuente es el registro vivo, y se cita
      con su fecha.**
- [x] **Tema 15 del específico de Producción (Asistencia)** —organismos nacionales e
      internacionales de televisión— **cerrado**: 2.326 palabras, con esquema de repaso. **Tema
      partido por dónde deja leer cada organización**: **FORTA** y **UTECA** publican quiénes son
      —la primera da hasta **sus doce organismos**— y sus dos preguntas quedan documentadas; **la
      Unión Europea de Radiodifusión no deja leer nada**, y **sus tres preguntas —sede, tasa y
      Euroradio 2SEE— se recogen de la plantilla sin verificar**. No es pereza: **el examen
      pregunta el detalle interno de una organización que no publica accesiblemente su
      información**, y el tema lo dice en vez de rellenar el hueco con plausibilidad.
- [x] **La regla del agente de navegador, esta vez sin premio, y eso también es resultado.** Se
      probaron **seis rutas** del sitio de la UER —portada, página institucional, contacto, portal
      técnico, servicio de Eurovisión y cuatro rutas a sus estatutos— más dos caminos indirectos
      para la sede —**registro mercantil suizo**, que exige credenciales, y **registro cantonal de
      Ginebra**, que devuelve «no encontrado»—. **Nada.** La declaración se sostiene.
- [x] **Dos errores del enunciado del examen, comprobados**: cita «la **Ley 10/1998** de 3 de mayo
      de televisión privada» y esa ley es la **Ley 10/1988, de 3 de mayo** —`BOE-A-1988-11073`; el
      día y el mes coinciden, el año no—; y la **Ley 7/2010** que invoca **está derogada** por la
      disposición derogatoria única de la Ley 13/2022.
- [x] **Una pregunta que se contesta leyendo las opciones**: la 78·33 ofrece **EBU** y **UER**, que
      son **el mismo organismo con dos nombres**. En elección única **no puede haber dos respuestas
      correctas**, luego ninguna de las dos lo es; y FORTA ya estaba descartada por la otra pregunta
      del tema. **Queda ENEX, y se acierta sin saber qué es.**
- [x] **Tercer caso de cifra huérfana que es comprobación positiva**: la lente marcó **1998**, que
      es **el año equivocado del enunciado**, citado por el tema para señalarlo. **La lista de
      huérfanas se lee en dos columnas: las que faltan por descuido y las que faltan porque el tema
      dice que faltan.**
- [x] **Cerrados los cuatro temas cortos del específico de Producción**, y con ellos **el bloque
      entero**:
      **tema 4** —el desglose, 2 preguntas, 977 palabras—, **tema 5** —localización, 3 preguntas,
      1.316—, **tema 6** —plan y orden de trabajo, 4 preguntas, 1.630— y **tema 16** —gestión de
      servicios varios, 3 preguntas, 1.229—. Los cuatro con esquema y con sus dos informes.
- [x] **El tema 6 es el segundo del bloque sin ninguna fuente normativa**, tras el del guion, y con
      la ausencia **comprobada término a término**: de sus **seis documentos** —plan, orden y parte
      de trabajo, hoja de script, parte de producción y desglose—, **cinco no aparecen ni una vez**
      en todo el corpus y el sexto sale **cuatro veces y siempre en otro sentido**. Lo que ofrece a
      cambio es **la cadena de papeles** —guion → desglose → presupuesto → plan → orden → parte—,
      que **contesta tres de sus cuatro preguntas**.
- [x] **Una comprobación que no dio la fuente que buscaba y dio algo mejor**: «**semoviente**» se
      buscó en el **Código Civil**, que era el sitio evidente, y **no aparece ni una vez**. Tras la
      reforma que dio a los animales estatuto propio, **el Código ya no los clasifica como
      semovientes**. De modo que la palabra es **vocabulario de oficio y de tradición jurídica, no
      término legal vigente**, y el tema lo dice para que nadie la busque en vano.
- [x] **Un distractor que resultó ser copropietario de la respuesta**: la portada de **SNTV** dice
      que es «**una empresa conjunta entre The Associated Press e IMG**», y **AP es una de las
      opciones falsas** de esa misma pregunta. El tema lo cuenta para que la duda no pille a nadie.
- [x] **La lente de prosa cazando repetición perezosa, no sólo relleno**: en el tema 16 detectó la
      misma frase dicha dos veces —«las páginas de EFE y de Reuters no se han podido consultar»—, y
      al reescribir la segunda salió información nueva: **cuál de las cuatro agencias sí se pudo
      leer y qué respondió cada una de las otras tres**.
- [x] **El bloque específico de Producción (Asistencia), entregado como volumen imprimible**:
      `libro-produccion.pdf` —**221 páginas**, con encabezado, pie, «Página X de Y» e índice
      paginado y navegable— y `libro-produccion.docx`. **Diecisiete temas, diecisiete esquemas de
      repaso y las 123 preguntas reales**, con las respuestas al final del volumen.
- [x] **`libro.py`, `word.py` y `pdf.py` sirven ya para los dos bloques sin duplicar código.** Todo
      lo que cambia entre el general y el específico —qué temas, de qué carpeta, cómo se titula el
      volumen, qué pie lleva y qué avisos se imprimen con las respuestas— vive en un solo
      diccionario, `BLOQUES`. **Un volumen escrito dos veces se desincroniza a la primera
      corrección**, y cuando lleguen Documentación e Información y Contenidos bastará con añadir
      una entrada.
- [x] **Comprobado que el cambio no toca el volumen general**: regenerado con la herramienta nueva,
      su `.docx` sale con **exactamente los mismos 5.577 párrafos** salvo una frase que se
      generalizó a propósito, y su `.html` sólo difiere en dónde parte los renglones.
- [x] **El apéndice de respuestas del específico avisa de cinco enunciados defectuosos.** A
      diferencia del general, aquí **ninguna respuesta oficial está mal**; lo que está mal son
      **cinco enunciados**: el de la realidad aumentada, con los términos invertidos; el que pide
      lo que «la DCI 4K estandariza para televisión»; el que fecha la ley de televisión privada en
      1998; el de las 24 imágenes por segundo, cuyo distractor descartado **no es falso**; y el del
      Titan Tube, cuya «marca comercial alemana» sí está comprobada. Van impresos con su respuesta.
- [x] **Las 129 preguntas del bloque específico de Producción, repartidas a mano y con motivo**
      (`banco/especifico-produccion.tsv`): **123 quedan en el específico**, repartidas entre los
      diecisiete temas, y **seis vuelven al bloque común** —dos de la Ley 31/1995, dos del III
      Convenio, una del PRL del específico y una de la derogada Ley 7/2010, que queda fuera—.
      **Todas tienen respuesta oficial.** El reparto deja ver dónde está el examen: **el tema 9,
      escenografía e iluminación, con 20 preguntas, y el 10, imagen y sonido, con 17, son casi un
      tercio del bloque**.
- [x] **`banco_especifico.py` cuenta bien lo que falta.** Contaba como pendiente del específico
      toda pregunta que ninguna palabra clave reconociera, **incluidas las que ya estaban
      repartidas a mano en `reclasificadas.tsv`**: trabajo hecho que la cuenta pedía dos veces.
      Ahora lee las dos actas.
- [x] **Material reunido para los quince temas que quedan**
      (`informes/materiales-del-especifico-2026-09-02.md`), con inventario tema por tema de lo
      conseguido y lo que no:
      **del BOE** —RD 2032/2009 de unidades legales de medida (`BOE-A-2010-927`), Reglamento (UE)
      2019/947 de drones (`DOUE-L-2019-81004`), reglamento del aire SERA (`DOUE-L-2012-81859`),
      Convenio de Estambul sobre importación temporal, que es el del cuaderno ATA
      (`BOE-A-1997-21711`), y RD 1036/2017 (`BOE-A-2017-15721`)—;
      **de organismos de normalización** (`fuentes/normas-tecnicas/`) —**Recomendación UIT-R
      BT.2100-1 (06/2017)** y **UIT-R BT.601-7 (03/2011)**, las dos en español y en la edición que
      cita el examen, y el **índice de la familia SMPTE ST 2110** con los títulos oficiales de cada
      parte—.
      **No se han podido traer**, y queda dicho: DCI, EBU/UER (403), AES10, y las fichas de
      LiveU, Sony, DJI, Astera y Mo-sys.
- [x] **`herramientas/doue.py`, dos arreglos que salieron de usarlo con otras normas**: el patrón
      de artículos solo reconocía «Artículo 1. Objeto.» en una línea y **devolvía cero artículos**
      con los reglamentos que dejan el título en la línea siguiente; y ahora **avisa cuando los
      números de artículo se repiten** —un tratado numera desde 1 en cada anexo, y las lentes por
      artículo se quedarían solo con el último sin dar ningún error—.
- [x] **Medido de qué se puede escribir el bloque específico**
      (`informes/fuentes-del-especifico-2026-09-02.md`): de las **129 preguntas** específicas
      de los dos cuadernillos de Producción (Asistencia), **sólo 15 citan una norma del BOE**,
      y las quince caen en **dos temas**. Las otras **114** son jerga del oficio, normas
      técnicas (SMPTE, UIT-R), documentación de viaje (cuaderno ATA, MCO) y fichas de
      fabricante. **Sobre ellas las lentes por artículo devuelven «0 comprobadas, 0
      hallazgos»**, que es el fallo del apartado 10 del manual. Declarada una **jerarquía de
      fuentes de cinco niveles**, con la plantilla oficial como último recurso y con sus
      cautelas escritas.
- [x] `herramientas/banco_especifico.py`: el banco del bloque específico. **El reparto se
      escribe a mano**, en `banco/especifico-<ocupacion>.tsv` y con columna de motivo, porque
      clasificar por palabras clave preguntas sobre *beauty shot* o SMPTE 2110 no da un reparto
      discutible sino uno falso que nadie revisa. El script avisa de las **filas huérfanas** y
      cuenta **las preguntas específicas que todavía no se han repartido**, que es la cifra que
      no aparece sola.
- [x] **La ficha de portada admite ahora ocupación propia y normas complementarias**
      (columnas `sirve` y `extra` de `herramientas/portadas.tsv`): un tema del específico lo
      estudia una sola ocupación, no las tres. De paso se corrigieron las **dos fichas que
      citaban rutas del proyecto** —la de Igualdad y la del PRL del específico—, que el propio
      `indice.py` venía avisando sin que nadie lo aplicara.
- [x] Ley 17/2006 y Ley 5/2017 volcadas a `fuentes/`, en la redacción de hoy y en
      la del corte 21/12/2022. Entre una y otra cambian **11 bloques** de la Ley
      17/2006: arts. 4, 10, 11, 12, 15, 16, 20 y 24 y tres disposiciones
      transitorias.

## Decisiones tomadas

- **2026-08-29 · Qué redacción se estudia. Corregida el mismo día al leer las
  bases.** El cuerpo del tema se escribe con la redacción **vigente el 21 de
  diciembre de 2022**, que es la fecha de corte que imponen las bases (punto 6:
  «las pruebas se realizarán sobre su texto vigente a fecha de la primera
  publicación de las Bases Generales»). Donde la redacción de hoy sea distinta va
  una **nota de actualización** al final del epígrafe, marcada como tal y fuera
  del cuerpo examinable.
  La primera decisión de esta sesión fue la contraria —cuerpo con la redacción
  vigente hoy— y se tomó sin tener las bases delante. Las bases mandan.
  Excepción: en **Información y Contenidos**, los apartados 1, 2 y 3 del temario
  específico (actualidad, Unión Europea, instituciones) **sí** cuentan hechos
  posteriores al corte.

## Falta

- [ ] Los **anexos 5 y 6 de las Bases Generales** (baremos de méritos). La versión
      descargada no los trae. No afectan al temario.

- [ ] **Manual de estilo de RTVE** y **informe UNESCO 2021/2022**: conseguirlos
      por otra vía.
- [ ] **Fase B: los tres temarios específicos.** Documentación es el más corto (6 temas),
      Producción (Asistencia) el más largo (17) e Información y Contenidos el más entrelazado
      con el general (10). El orden y el tratamiento de los temas sin norma detrás, en `PLAN.md`.
      **Hechos los temas 2 y 17 de Producción**; el 18 ya venía hecho como tema de PRL común.
      **Con eso se cierran los dos únicos temas del específico de Producción que tienen norma del
      BOE detrás**, y con ellos las 15 de las 129 preguntas en que el método funciona entero.
      **Siguiente**: los quince restantes, que hay que documentar antes de escribir.
- [ ] **Escribir los catorce temas que quedan de Producción.** **Hecho el 10**; el siguiente es
      el **9**, el más pesado, con 20 preguntas. El inventario de lo que necesita cada uno está en
      `informes/materiales-del-especifico-2026-09-02.md`.
- [ ] **Rematar el material que falta**: probar la **ISO 3382** para el RT60, la **AES10** para
      MADI, las normas **ETSI** del DVB, y tirar del hilo del BOE para el tema 15 —Ley 46/1983,
      Ley 10/1998 y Ley 7/2010— antes de dar por perdidos FORTA y UTECA.
- [ ] **Un volumen imprimible del bloque específico.** `herramientas/libro.py` tiene hoy la
      lista de los ocho temas del general escrita dentro; para el específico hace falta que la
      lista salga del programa y no del código.

## Qué comprobación pasa por qué material

El apartado 10 del manual: un hueco de cobertura no da error, así que se
escribe. Se rellena desde los ficheros de `informes/`, no de memoria.

| Tema | Investigar | Redactar | Verificar | Refutar 1 | Rematar | Refutar 2 | Preguntas |
|---|---|---|---|---|---|---|---|
| General 1 · Constitución | sí | sí | sí | sí | sí | sí, limpia | 87 de 89 enteras |
| General 2 · Ley 17/2006 | sí | sí | sí | sí | sí | sí, limpia | 32 de 32 enteras |
| General 3 · Ley 5/2017 | sí | sí | sí | sí | sí | sí, limpia | incluidas en las 32 |
| General 4 · Ley 8/2009 | sí | sí | sí | sí | sí | sí, limpia | 23 de 23 enteras |
| General 5 · III Convenio Colectivo | sí | sí | sí | sí | sí | sí, limpia | 84 de 84 enteras |
| General 6 · Igualdad | sí | sí | sí | sí | sí | sí, limpia | 39 de 39 enteras |
| General 7 · Ley 13/2022 | sí | sí | sí | sí | sí | sí, con 11 salvedades declaradas | 34 de 34 enteras |
| General 8 · Ley 31/1995 | sí | sí | sí | sí | sí | sí, con 3 falsos positivos declarados | 49 de 52 enteras, 2 a medias |
| PRL del específico (P18/D7/I11) | sí | sí | sí | sí | sí | sí, limpia | 35 de 40 enteras, 1 con matiz, 5 fuera de tema |
| Producción 2 · Propiedad intelectual | sí | sí | sí | sí | sí | sí, 13 falsos positivos declarados | 10 de 10 enteras |
| Producción 17 · Protección de datos | sí | sí | sí | sí | sí | sí, 6 falsos positivos declarados | 5 de 5 enteras |
| Producción 10 · Imagen y sonido | sí | sí | sí | sí | sí | sí, limpia (lente de documento) | 17 de 17 enteras |
| Producción 9 · Escenografía e iluminación | sí | sí | sí | sí | sí, dos veces | sí, limpia (lente de documento) | 20 de 20 enteras |
| Producción 11 · Transmisión de señal | sí | sí | sí | sí | sí | sí, limpia (lente de documento) | 10 de 10 enteras |
| Producción 13 · Equipos de exteriores | sí | sí | sí | sí | sí | sí, limpia (lente de documento) | 7 de 7 enteras |
| Producción 1 · La producción | sí | sí | sí | sí | sí | sí, 1 salvedad de cobertura declarada | 6 de 6 enteras |
| Producción 3 · El guion | sí | sí | sí | sí | sí | sí, limpia (0 de 6 con norma, declarado) | 6 de 6 enteras |
| Producción 7 · Equipos humanos | sí | sí | sí | sí | sí | sí, limpia (1 tensión con el convenio declarada) | 6 de 6 enteras |
| Producción 8 · Formatos y soportes | sí | sí | sí | sí | sí | sí, limpia (9 huérfanas, todas metadatos o negaciones) | 6 de 6 enteras |
| Producción 12 · El estudio | sí | sí | sí | sí | sí | sí, limpia (2 huérfanas, metadatos) | 6 de 6 enteras |
| Producción 14 · Documentación internacional | sí | sí | sí | sí | sí | sí, limpia (0 huérfanas; lentes arregladas) | 6 de 6 enteras |
| Producción 15 · Organismos | sí | sí | sí | sí | sí | sí, limpia (3 respuestas sin verificar, declaradas) | 6 de 6 enteras |
| Producción 4 · El desglose | sí | sí | sí | sí | sí | sí, limpia | 2 de 2 enteras |
| Producción 5 · Localización | sí | sí | sí | sí | sí | sí, limpia (1 matización declarada) | 3 de 3 enteras |
| Producción 6 · Plan y orden de trabajo | sí | sí | sí | sí | sí | sí, limpia (0 de 4 con norma, declarado) | 4 de 4 enteras |
| Producción 16 · Gestión de servicios | sí | sí | sí | sí | sí | sí, limpia (5 huérfanas, metadatos) | 3 de 3 enteras |

**El tema 1 está cerrado**, con su esquema en `esquemas/general/`. La lista del
apartado 13 del manual, repasada punto por punto, está al final de
`informes/refutacion-tema-01.md`.

Lo del tema 1: investigado sobre el volcado del texto consolidado a la fecha de
corte; verificado con 28 comprobaciones de cifra contra el articulado y el
recuento de las enumeraciones; refutado con tres lentes distintas —exactitud
normativa, cobertura y prosa—, que sacaron **diez hallazgos reales** más
(`informes/refutacion-tema-01.md`); rematado revisando antecedentes; y la
**segunda refutación vuelve sin ningún hallazgo real**.

## Decisión de esta sesión

- **2026-08-29 · Cómo se verifica un tema cuya fuente no es legislación
  consolidada.** El III Convenio Colectivo no tiene texto refundido oficial: son
  tres documentos del BOE que hay que superponer. En vez de renunciar a las lentes
  o de darlas por pasadas, se construyó la fuente (`convenio_dump.py`) y se
  ejecutaron las tres sobre ella. Al hacerlo aparecieron **dos puntos ciegos en las
  propias lentes** —no reconocían la abreviatura «Art.» ni los rótulos de rango
  «Artículos 53 a 56»—, que dejaban artículos enteros sin comprobar devolviendo un
  resultado limpio. Corregidos y **repasados los cuatro temas ya cerrados**, lo que
  destapó un hallazgo real en el tema 2 (artículo 36: la presentación consolidada
  se suma a la individual, no la sustituye). Está contado en
  `informes/refutacion-tema-05.md`.
- **El tema 3 no pasa por la lente por artículo y se dice.** La Ley 5/2017 tiene
  «Artículo único» y el tema cita artículos de otra norma, así que la lente
  devuelve «0 comprobadas, 0 no literales», que **no es un aprobado**. Se verificó
  a mano y con un contraste contra el texto completo, y así consta en el informe.

- **2026-08-29 · Qué se hace cuando la fuente no está en el BOE.** El tema 6 son dos PDF
  publicados en `rtve.es`: sin identificador, sin texto consolidado y sin redacciones
  fechadas, de modo que **no se puede demostrar qué decían en una fecha pasada**. Se aplican
  tres reglas: **se versionan los PDF además de su transcripción**, para que quede la versión
  con la que se ha estudiado; se **verifica con `refutar_documento.py`** en vez de dar por
  buenas las lentes por artículo; y **se dice en el tema** que si RTVE sustituyera el fichero
  no quedaría rastro del anterior. Lo mismo valdrá para el Manual de estilo y el Código de
  autorregulación del menor de los temarios específicos.

- **2026-08-29 · Qué se hace cuando parte de la norma aún no estaba en vigor al corte.** La
  Ley 13/2022 escalona su entrada en vigor en ocho reglas (DF novena) y **quince bloques no
  eran exigibles el 21/12/2022**, entre ellos los artículos 102 y 115, que el tribunal
  preguntó en 2024. Se estudia **la ley entera**: la fecha de corte congela **el texto**, que
  en esta ley no ha cambiado ni una palabra desde su publicación, y lo diferido era la
  **exigibilidad**. El programa lo respalda al citar el «texto inicial». En el volcado al
  corte esos bloques llevan **aviso expreso**, y el tema explica la distinción.

- **2026-09-02 · La lente de exactitud no veía las citas repartidas en dos renglones.** Su
  expresión buscaba las negritas **sin `re.S`**, de modo que el punto no cruzaba el salto de línea:
  una cita larga —que en estos temas ocupa casi siempre tres o cuatro renglones— **no salía como no
  literal, salía como si no existiera**. Se descubrió porque el primer tema de Documentación devolvió
  «0 negritas comprobadas» sobre una ley que citaba entera. Corregido, el recuento sube en **todos**
  los temas cerrados con norma articulada: la Constitución pasa de **475 a 819** negritas
  comprobadas, la Ley 31/1995 de **557 a 858**, la Ley 13/2022 de **276 a 427** y la propiedad
  intelectual de **412 a 641**. Es decir, **en el tema de la Constitución había 344 citas que nunca
  se habían mirado**. Se pasó después por todos los temas cerrados una comprobación dirigida —cada
  negrita **dentro de comillas angulares**, contra el texto de sus normas— y **no apareció ninguna
  cita alterada**: lo recién visible es comentario en negrita, no citas. Está contado en
  `informes/refutacion-documentacion-tema-01.md`.

- **2026-09-02 · Empieza el bloque específico de Documentación, y su tema 1 deja tres reglas.**
  Primera: **una fuente puede estar dada por leída sin estarlo**. El inventario de fuentes daba por
  verificado el «Teatro Monumental» en la portada de la Orquesta y Coro, y al comprobarlo contra el
  fichero guardado **la palabra no aparecía**; se cerró con el programa de conciertos de la propia
  agrupación. Segunda: **cuando la fuente natural es la parte interesada, se busca fuera**. La fecha
  de La 2 no está en ninguna página de RTVE, y sí en una nota de prensa del portal público de
  televisión digital, que además explica el apodo «UHF» que usa el enunciado. Tercera: **un catálogo
  completo es una ruta**. Para «Cita con Pilar» se descargaron las **4.623 fichas** que RTVE publica
  y se buscaron una a una; el programa no está, y por eso ese año se marca como apoyado sólo en la
  plantilla.

- **2026-09-02 · Qué se hace cuando la fuente buena es de pago.** El tema 2 de Documentación se
  gobierna por **normas ISO**, que no están en el BOE y que `iso.org` no deja ni mirar: responde
  «prohibido» a toda consulta automática, también con agente de navegador. La ruta que funciona es
  **la muestra oficial que ISO publica de cada norma** —portada, prólogo, **índice completo**,
  introducción, objeto y parte de los términos—, y resulta que **ahí están las respuestas del
  examen**: los cuatro modelos de interoperabilidad que pregunta una de ellas son **títulos de
  apartado** de ISO 25964-2, y su numeración —«Model 1», «Model 2», «Model 3» y, sin numerar,
  «Selective mapping»— es la que decide cuál es la respuesta. Se versiona **el PDF de la muestra
  además de su transcripción**, y el tema **no cita ni una línea que no esté en ella**.

- **2026-09-02 · Las lentes por artículo no sabían leer las leyes que numeran con letra.** La Ley
  16/1985 del Patrimonio Histórico titula sus artículos «Artículo cuarenta y nueve», de modo que
  las lentes devolvían **«0 comprobadas, 0 no literales»**: el fallo del apartado 10 otra vez. En vez
  de renunciar a la lente, **se construye la fuente**, como se hizo con el convenio colectivo:
  `herramientas/ordinales.py` reescribe **sólo el rótulo del encabezado** —«Artículo 49»— y **no toca
  el cuerpo del precepto**. Reescribió **79 artículos** y la lente pasó de **0 a 11 negritas
  comprobadas** en el tema.

- **2026-09-02 · Quitar las remisiones internas de una norma rompe la cita.** ISO escribe
  «combination of preferred terms **(2.45)** of a controlled vocabulary **(2.12)** at the time of
  searching»: los números remiten al apartado donde define cada término. El borrador los había
  limpiado por estética, y la comprobación de citas entrecomilladas marcó **cuatro definiciones**
  como no literales. **Los paréntesis son parte del texto**: se reponen, y el tema explica qué son.

- **2026-09-02 · Un sitio cerrado puede tener una puerta abierta, y hay que probarla.** La
  especificación **EBUCore** parecía inalcanzable: la organización que la publica bloquea su sitio, y
  así constaba ya en el bloque de Producción. Cinco rutas devolvieron «prohibido» o «no existe»; **la
  sexta —el PDF servido directamente desde el subdominio técnico— devolvió 54 páginas**. Con el
  documento delante, las tres opciones falsas de la pregunta se desmienten **con frases suyas**, una
  de ellas una pregunta frecuente que parece escrita contra el examen. La regla del proyecto se
  amplía: **cuando el sitio bloquea, se prueba el fichero**.

- **2026-09-02 · Dónde se para una comprobación.** El año de lanzamiento de una red social tenía
  fuente documental evidente —el folleto de salida a bolsa, en el archivo del regulador de mercados
  estadounidense—, y ese archivo **exige identificarse con un correo de contacto** en cada consulta
  automática. La única dirección disponible es la del usuario del proyecto, y **no se envía la
  dirección de una persona a un servicio ajeno para resolver una pregunta de examen**. El dato se
  recoge de la plantilla y va marcado, con la razón escrita.

- **2026-09-02 · Las dos lentes se avisan la una a la otra.** Un criterio del archivo web estaba
  atribuido al artículo 7 del Real Decreto 635/2015 y era **del artículo 6**. La lente de exactitud lo
  marcó como cita **no literal** —la buscaba en el artículo equivocado— y la de modo avisó de una
  **salvedad del artículo 7 que el tema no recogía**, que es lo que ocurre cuando se cita un artículo
  sin haberlo leído entero. Corregida la atribución, **el tema mejoró**: el artículo 7 aportaba los
  «procedimientos de selección y captura» y la **frecuencia**, que son las palabras del modelo mixto.

- **2026-09-02 · Cuando la materia no tiene norma, eso es el hallazgo.** El tema 4 de Documentación
  —inteligencia artificial— tiene **4 preguntas y 2 fuentes**, la proporción más baja del bloque. Se
  probaron **cinco puertas** y se abrieron dos: no hay norma en el BOE que defina la diarización, ni
  recomendación que describa los módulos de un sintetizador, ni definición de «palabra token» en las
  normas de vocabulario documental. Las dos que sí valen son de clases distintas y así se marcan: **un
  programa público de evaluación** —el instituto de normas de los Estados Unidos define la tarea
  porque tiene que medirla, y la llama «Who Spoke When»— y **el anuncio de quien fabricó el sistema**.
  **Las lentes por artículo no se ejecutan** sobre un tema sin articulado: devolverían un cero limpio,
  que es peor que no ejecutarlas, y así consta en su informe.

- **2026-09-02 · Un sitio que bloquea la navegación puede servir los ficheros, y ya son dos.** La
  unión de radiodifusión responde **403** en casi todas sus páginas, pero su **directorio de
  documentos técnicos sirve los PDF**. Por esa puerta se han recuperado la especificación de
  metadatos (tema 3) y la del formato de audio de radiodifusión (tema 5). **Dos veces ya no es
  casualidad**: queda anotada como ruta del proyecto.

- **2026-09-02 · El corpus no se cierra tema a tema.** Una fuente reunida para el **tema 5** —el
  artículo de la responsable del Fondo Documental de RTVE— contestó, en el mismo párrafo, **una
  pregunta del tema 2** que se había dado por apoyada sólo en la plantilla: la de la «redacción
  digital». El tema 2 se reabrió para incorporarla. **Regla: cuando entra una fuente institucional
  nueva, se releen los temas anteriores**, porque lo que habla de la propia casa contesta lo que
  ninguna norma internacional podía.

- **2026-09-02 · Traducir dentro de las comillas es inventar la cita.** El borrador del tema 5
  entrecomillaba en español dos instrucciones de manejo de soportes que la fuente da en inglés. La
  traducción era fiel y el sentido no cambiaba, y aun así **las comillas decían que aquello era el
  texto de la fuente**. Se cita en inglés y se traduce fuera. Y un segundo caso del mismo linaje: una
  cita de un artículo de revista **llevaba el encabezado de página incrustado** por la extracción del
  PDF, y el borrador lo había quitado en silencio. Ahora va con puntos suspensivos y una nota.

- **2026-09-02 · La lente de prosa miraba el sitio equivocado.** Para saber si una sigla está
  presentada mira los 130 caracteres anteriores a su primera aparición, y localizaba esa aparición
  **con una búsqueda de trozo, no de palabra**: encontraba «SI» dentro de «MÚSICA» y «RD» dentro de
  «BORDER», de modo que **comprobaba la presentación donde la sigla no está** y el aviso se volvía
  **incorregible**. Corregida con límites de palabra: en el tema 6 de Documentación pasó de **trece
  avisos a uno**, y en el resto del proyecto **destapó avisos que un paréntesis mal situado daba por
  resueltos**. Casi todos son falsos positivos —mayúsculas de énfasis, trozos de «CC.AA.» y
  «NO-DO»—; uno era real y se corrigió; **quedan cuatro en un tema del bloque general**, anotados en
  `PENDIENTES.md` porque ese volumen ya está impreso.

- **2026-09-02 · Cuarenta preguntas de «actualidad», y quince tenían documento.** El punto 6 de
  Documentación no acota nada —nueve materias separadas por puntos— y parecía condenado a la
  plantilla. Tratando cada pregunta como **un dato que comprobar**, **quince quedaron atadas a un
  documento y nueve de ellas al BOE**. La ruta nueva es **el sumario diario del BOE por su API de
  datos abiertos**, que localiza nombramientos y decretos —que no están en la legislación
  consolidada— cuando se sabe la fecha aproximada. Y el caso más instructivo: **la sede de la Corte
  Penal Internacional se resolvió con derecho español**, porque su sitio responde «prohibido» y
  España publicó el Estatuto de Roma en el BOE, en español.

- **2026-09-02 · Cuando la respuesta no está en la norma, puede estar el descarte.** El curio no
  aparece en el real decreto español de unidades, porque no es unidad del sistema internacional. Pero
  el real decreto **define las tres opciones falsas** —amperio, kelvin y newton— como unidades de
  otras magnitudes, y dice que la unidad del sistema para esta magnitud es el becquerel. **Un
  descarte completo vale tanto como una cita**, y así se marca.

- **2026-09-02 · Cerrado el bloque específico de Documentación.** Seis temas, seis esquemas, doce
  informes y **82 preguntas contestadas con el tema delante**. El volumen imprimible sale en
  `libro-documentacion.pdf` —**96 páginas**—, con sus versiones en Word y HTML. **Ninguna respuesta
  oficial de este bloque está mal**; **dos enunciados cojean** y van avisados en el apéndice: uno
  fecha el estado de alarma de 2010 un día tarde —el real decreto se publicó el **4** de diciembre y
  entró en vigor «en el instante de su publicación»— y otro desarrolla unas siglas que la norma que
  las define **no desarrolla**.
  **El saldo de fuentes del bloque**: de las 82 preguntas, **56 se verifican en documento**. El
  tema 5 es **el único tema del proyecto con todas sus preguntas verificadas**; el tema 4 es **el que
  menos fuentes tiene, y no por descuido**: su materia no tiene norma publicada.

- **2026-09-02 · Las fechas de esta sección iban un día adelantadas.** Dieciséis entradas y una
  del cuaderno de pendientes decían **2026-09-02** en un trabajo que los commits fechan el **2**.
  Corregidas todas. No cambia ningún dato del temario, pero un histórico con la fecha mal es un
  histórico que no se puede cruzar con nada.

- **2026-09-02 · Repartido el bloque específico de Información y Contenidos, y descartado un
  cuadernillo entero.** La ocupación tiene **cuatro** cuadernillos y solo dos sirven:

  · el de la **prueba anulada por filtración** no aporta ninguna pregunta —el PDF guardado da
    **880 bytes de marca de agua** y ni un enunciado—;
  · el de **Radio Clásica** se descarta **entero**, y la comprobación que lo decide es contable:
    de los **siete documentos** que el Anexo 2 de la ocupación nombra con su enlace —Manual de
    Estilo, Código de autorregulación, RDL 4/2018, Directiva 2018/1808, Resolución del Parlamento
    Europeo de 25/11/2020, Informe UNESCO y Carta ética de la FIP—, ese cuadernillo **no pregunta
    por ninguno, ni una vez**, mientras que los otros dos preguntan por **cinco de los siete**.
    Sus 97 preguntas específicas son teoría de la música y repertorio —cadencia plagal, Cancionero
    de Upsala, séptima de dominante—: es el examen de los destinos de *Información y Contenidos
    (Radio Clásica)*, cuyo Anexo 2 no está en el repositorio. Sus preguntas del bloque **común** sí
    valen y ya estaban en `banco/g*.md`.

  Quedan **180 preguntas**, de las que **178 se reparten** entre los diez primeros temas y **2
  vuelven al banco general** por `reclasificadas.tsv` (Comité Intercentros y complemento de
  disponibilidad, las dos del III Convenio). Una tercera, la iluminación de los lugares de trabajo
  del cuadernillo de Radio Clásica, se va al banco de prevención.

- **2026-09-02 · Un descarte de cien preguntas no cabe en cien filas de acta, pero tampoco puede
  vivir fuera de ella.** `banco_especifico.py` acepta ahora una fila con **`*` en el número**, que
  descarta el cuadernillo entero con su motivo, y lo **imprime cada vez que se regenera el banco**.
  Así el motivo está donde se busca —el acta— y no escondido en el código, y un descarte no se
  vuelve invisible por ser grande. De paso, una tabla `MARCA` traduce el nombre de la ocupación al
  que llevan los ficheros: los cuadernillos se llaman `..._preguntas_iyc...` y el temario,
  «informacion». **Sin ella el script no fallaba**: repartía cero preguntas y lo decía sin alarma,
  que es la forma más silenciosa de dar un bloque por hecho.

- **2026-09-02 · El reparto de Información y Contenidos, y los dos temas que el examen no
  pregunta.** Con la regla que ordena los tres primeros puntos —**qué es una institución** va a su
  tema, **qué pasó** va a actualidad, y lo que contesta uno de los siete documentos va a su tema
  aunque parezca actualidad—, salen: **121** preguntas de actualidad, **21** de instituciones del
  Estado y organismos internacionales, **17** de la Unión Europea, **9** del Manual de Estilo,
  **5** del Informe UNESCO, **2** del Código de autorregulación, **2** de la Directiva 2018/1808 y
  **1** de la Resolución del Parlamento Europeo. **El RDL 4/2018 y la Carta ética de la FIP no
  tienen ni una pregunta**: sus temas se escribirán contra la norma y el documento, sin banco que
  los respalde, y su informe de cobertura lo dirá. Dos tercios del bloque son actualidad, que es
  justo la materia que no se estudia en una norma sino que se comprueba dato a dato.

- **2026-09-02 · Un script que escribe donde no debe y lo anuncia como éxito.** Componer el
  volumen de Documentación con `pdf.py libro-documentacion.html` **escribía encima de
  `libro-general.pdf`**, porque el destino era una constante y no salía de la entrada; y
  `word.py libro-documentacion.html` tomaba el nombre del **HTML** por nombre de salida y
  **guardaba un .docx encima del HTML del volumen**. Ninguno de los dos falló: los dos
  imprimieron una línea de éxito con el nombre del fichero equivocado. Corregidos: el destino
  del PDF sale ahora **de la entrada** y los dos **rechazan una salida con la extensión que no
  es**. Los cuatro ficheros se regeneraron desde cero.

- **2026-09-02 · Las fechas de lectura de las fuentes también iban un día adelantadas.**
  Cincuenta ficheros de `fuentes/`, seis fichas de tema y `portadas.tsv` sellaban las páginas
  como leídas el **03/09/2026**, un día que todavía no había llegado. Corregidos, y
  **regenerados los tres formatos del volumen de Documentación** para que el libro y los
  ficheros digan lo mismo.

- **2026-09-02 · Cerrado el pendiente de las cuatro siglas del tema 7 del general.** Se aplazaba
  porque tocar el tema desincronizaba un volumen ya impreso; pero el volumen **había que
  reimprimirlo igual**, porque el reparto de Información y Contenidos devolvió dos preguntas al
  banco del III Convenio y el general pasó de **479 a 481**. Dos de las siglas —**RFEF** y
  **FED**— van **dentro de una cita literal del artículo 146.3** y la ley **no las desarrolla**:
  se presentan **antes de la cita**, diciéndolo, porque meter el desarrollo entre las comillas
  habría sido reescribir la ley. El volumen general vuelve a salir con **254 páginas**.

- **2026-09-02 · Un 403 no dice quién bloquea, y el Manual de Estilo de RTVE no estaba bloqueado.**
  `convocatoria/FUENTES.md` daba por imposibles dos de los siete documentos del Anexo 2 de
  Información y Contenidos. **Uno era un error de lectura del error**: el programa da la dirección
  del manual en **`http://`**, y por ahí responde 403 —pero el 403 lo devuelve **la política de
  salida de este entorno**, que solo deja pasar `https`, no el servidor de RTVE—. Con `https://`, la
  misma dirección responde **200** y sirve el manual entero: **ocho páginas y unas 48.000 palabras**,
  que contestan las nueve preguntas del examen sobre él. **Regla nueva: antes de escribir "no se ha
  podido consultar", mirar el esquema de la dirección y quién firma la página de error.**

- **2026-09-02 · El informe de la UNESCO sí está bloqueado, y ahora se sabe por qué.** `unesdoc` está
  detrás de un **desafío de JavaScript de Cloudflare** —la página «Just a moment...»—, no de un
  bloqueo del proxy. Cinco rutas probadas: el enlace del programa, el visor de documentos, el fichero
  `.pdf.multi`, la consulta con agente y cabeceras completas de navegador, y **la navegación con
  Chromium real**. Las cuatro primeras dan 403; la quinta **no llega a salir**, porque en este
  entorno el navegador no atraviesa el proxy —falla con `ERR_CONNECTION_RESET` incluso contra sitios
  que `curl` sí alcanza—. Lo que sí publica la UNESCO es **el sitio oficial del propio informe en
  español**, con sus cuatro capítulos, y eso es lo que va, dicho en la cabecera de cada fichero.

- **2026-09-02 · Cuando EUR-Lex devuelve 202 con cero bytes, el Cellar sirve el documento.** El
  enlace del programa a la Resolución del Parlamento Europeo responde **202 Accepted y ningún byte**,
  en PDF y en HTML, tres intentos seguidos. El repositorio **Cellar** de la Oficina de Publicaciones
  sirve el mismo documento en `https://publications.europa.eu/resource/celex/<CELEX>` **si se le pide
  el idioma en la cabecera**; sin ella devuelve un 400 que, eso sí, **dice qué falta**. Por ahí
  salieron también la Directiva 2018/1808 y la Directiva 2010/13 consolidada.

- **2026-09-02 · Una norma modificativa no se lee sola.** La Directiva 2018/1808 dice «el artículo 23
  se sustituye por el texto siguiente». Lo que el examen pregunta —límites de publicidad, prohibición
  del tabaco— **está en la Directiva 2010/13 tal como queda tras la reforma**, no en la modificativa.
  Estudiar solo la modificativa obliga a **reconstruir la norma de cabeza**, que es lo que el
  apartado 1 del manual prohíbe. Se guardan las dos.

- **2026-09-02 · Faltaba entrar al BOE por el título, y era el caso más frecuente.** `boe.py` lee una
  norma **cuando ya se conoce el identificador**; la API de sumarios da el boletín **cuando ya se
  conoce la fecha**. **Entre las dos quedaba fuera lo normal en un temario de actualidad**: saber qué
  se busca y no saber ni una cosa ni la otra. Nuevo `herramientas/boe_buscar.py`. Su formulario tiene
  una trampa que **da cero resultados sin dar ningún error**: las **secciones son casillas**
  (`dato[0][1]`…`dato[0][T]`) y van todas marcadas por defecto; si se manda la consulta sin ellas, el
  buscador contesta «no se han encontrado documentos» —no «faltan campos»— y **una búsqueda que sí
  tenía respuesta se anota como camino cerrado**.

- **2026-09-02 · Una parte grande de la «actualidad» se publica en el BOE, y no lo parece.** Diez de
  las quince respuestas que el tema 1 de Información y Contenidos ata al Boletín **no parecen
  preguntas de derecho**: los **premios nacionales de cultura y de investigación** se conceden por
  orden ministerial con el nombre del premiado y la motivación del jurado; **la supresión de un
  premio**, también; los **nombramientos de ministros y de presidentes autonómicos**, por real
  decreto; y la **lista de zonas de alquiler tensionado**, por resolución trimestral que la propia
  Ley 12/2023 obliga a publicar. **El mapa queda escrito** en
  `informes/cobertura-informacion-tema-01.md`, porque la próxima convocatoria preguntará por otros
  premios publicados en el mismo sitio.

- **2026-09-02 · Volcar un precepto no es volcar la norma.** `boe.py precepto` da el artículo y su
  cadena de redacciones, que es lo que hace falta para estudiar; **no da el número del boletín ni la
  fecha de publicación**. Y una de las preguntas de este tema es justamente **qué día se publicó la
  ley de amnistía**. La lente de documento lo cazó como **cifra huérfana**: el «141» de «BOE núm. 141»
  no estaba en ninguna fuente. Se añadieron las fichas de publicación.

- **2026-09-02 · Una fuente estadística desmiente por primera vez a una plantilla oficial.** La
  respuesta oficial da **11,4 %** de tasa de paro en el segundo trimestre de 2024; el **INE** publica
  **11,27 %** en la nota de prensa de la EPA de ese trimestre. La sospecha se sometió al apartado 5
  del manual y no se sostuvo: es el trimestre correcto, la cifra se comprueba sola —11,27 + 1,02 =
  12,29, la del trimestre anterior— y el enunciado **no dice de quién es la tasa**. **El tema enseña
  el dato del INE.** Las tres erratas de plantilla anotadas hasta ahora eran de derecho; ésta es la
  primera de estadística.

- **2026-09-02 · Un dato verdadero escrito de memoria dentro de un tema que presume de citar.** El
  borrador del tema 1 afirmaba que «Amar es para siempre» continúa una serie anterior. **No salía de
  ninguna fuente: salía de saberlo**, y ninguna de las cuatro lentes lo habría cogido —no era una
  negrita ni una sigla—. Lo cogió **una comprobación hecha a propósito**: cada fragmento entre
  comillas del tema, buscado en el texto completo de las fuentes **y de los propios cuadernillos**.
  Esa comprobación queda como parte del ciclo de los temas sin norma.

- **2026-09-02 · Escrito el tema 1 del específico de Información y Contenidos.** **121 preguntas**,
  el punto más preguntado de todo el proyecto. **20 verificadas** —quince en el BOE, cinco en la
  fuente oficial, tres de ellas sólo en parte— y **101 apoyadas sólo en la plantilla**, listadas una
  a una. Con su esquema y sus dos informes.
