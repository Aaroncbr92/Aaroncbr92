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
