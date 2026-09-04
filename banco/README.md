# Banco de preguntas del bloque común

**512 preguntas reales** —481 del temario general y 31 del tema de prevención del
específico— sacadas de los cuadernillos de la convocatoria 1/2022 (pruebas de
octubre y noviembre de 2024), **todas con la respuesta de la plantilla oficial**.

Se puede hacer porque el temario general es el mismo para las más de cincuenta
ocupaciones tipo convocadas, y porque las preguntas del bloque común se comparten
entre ocupaciones: está comprobado en `informes/preguntas-repetidas.md`.

| Fichero | Materia | Preguntas |
|---|---|---|
| `g1.md` | Constitución | 116 |
| `g2-g3.md` | Ley 17/2006 y Ley 5/2017 | 53 |
| `g4.md` | Ley 8/2009, financiación | 35 |
| `g5.md` | III Convenio Colectivo | 120 |
| `g6.md` | II Plan y Guía de Igualdad | 47 |
| `g7.md` | Ley 13/2022, General de Comunicación Audiovisual | 47 |
| `g8.md` | Ley 31/1995, prevención de riesgos | 63 |
| `prl-especifico.md` | Prevención en el temario **específico** (P18 · D7 · IyC11) | 31 |

Cinco de esas preguntas entraron el **2026-09-02**, al repartir a mano el bloque
específico: dos de la **Ley 31/1995** —el Comité de Seguridad y Salud y la
coordinación de actividades empresariales—, dos del **III Convenio** —las
comisiones de servicio y el artículo 107, que el examen llama «ley de
incompatibilidades»— y una del **PRL del específico** —el túnel carpiano—.

**Y esta tabla estaba mal, en dos filas que se compensaban.** Decía 114 en `g5.md`
cuando eran 116, y 48 en `g6.md` cuando eran 47: el **total de 505 salía bien** y
por eso nadie lo miró. Se descubrió al comparar los ficheros antes y después de
regenerarlos. La lección es del apartado 10 del manual: **un total correcto no
prueba que sus sumandos lo sean**, y la cifra que se publica hay que sacarla de
contar, no de copiar.

Y una salió el **2026-09-02**, al repartir el bloque específico de
**Documentación**: la pregunta 26 de su cuadernillo —la doctrina del Tribunal
Constitucional sobre el contenido generado por los usuarios en redes sociales—.
La clasificación por palabras clave la había puesto en Constitución, y **el propio
informe del tema 1 ya la declaraba «fuera del tema, con razón»**; pero seguía
imprimiéndose en el volumen general. Ahora está donde le toca: en el punto 3.8 del
temario de Documentación, «redes sociales y contenido generado por el usuario».

Y tres más, también el **2026-09-02**, al repartir el bloque de **Información
y Contenidos**: la composición del **Comité Intercentros** y el preaviso del
**complemento de disponibilidad**, las dos del III Convenio, y la **iluminación de
los lugares de trabajo** del cuadernillo de Radio Clásica, que es del RD 486/1997
y va al banco de prevención.

Se regenera con `herramientas/banco.py`. **Las correcciones no se hacen sobre
estos ficheros**, que se sobrescriben enteros: van en `reclasificadas.tsv`.

## Y el banco del bloque **específico**

Hay uno por ocupación tipo. Los **trece** que existen suman **1.498 preguntas**, todas con
su respuesta oficial.

### Producción (Asistencia)

**123 preguntas**, repartidas entre los diecisiete temas de su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `produccion-asistencia-01.md` | 1 · La producción: sistemas y métodos | 6 |
| `produccion-asistencia-02.md` | 2 · Derechos de autor. Propiedad intelectual | 10 |
| `produccion-asistencia-03.md` | 3 · El guion | 6 |
| `produccion-asistencia-04.md` | 4 · El desglose | 2 |
| `produccion-asistencia-05.md` | 5 · Localización | 3 |
| `produccion-asistencia-06.md` | 6 · Organización, plan y orden de trabajo | 4 |
| `produccion-asistencia-07.md` | 7 · Equipos humanos | 6 |
| `produccion-asistencia-08.md` | 8 · Formatos y soportes | 6 |
| `produccion-asistencia-09.md` | 9 · Escenografía e iluminación | **20** |
| `produccion-asistencia-10.md` | 10 · Imagen y sonido | **17** |
| `produccion-asistencia-11.md` | 11 · Medios de transmisión de señal | 10 |
| `produccion-asistencia-12.md` | 12 · El estudio de televisión | 6 |
| `produccion-asistencia-13.md` | 13 · Equipos técnicos de exteriores | 7 |
| `produccion-asistencia-14.md` | 14 · Documentación internacional | 6 |
| `produccion-asistencia-15.md` | 15 · Organismos | 6 |
| `produccion-asistencia-16.md` | 16 · Gestión de servicios varios | 3 |
| `produccion-asistencia-17.md` | 17 · Protección de datos | 5 |

### Documentación

**82 preguntas** del cuadernillo de octubre de 2024, repartidas entre los **seis
temas** de su Anexo 2 —el séptimo, el de prevención, es el que ya comparten las
tres ocupaciones y está en `prl-especifico.md`—.

| Fichero | Tema | Preguntas |
|---|---|---|
| `documentacion-01.md` | 1 · Historia de RTVE | 11 |
| `documentacion-02.md` | 2 · Documentación y tecnologías de la información | 9 |
| `documentacion-03.md` | 3 · Internet | 8 |
| `documentacion-04.md` | 4 · Inteligencia artificial | 4 |
| `documentacion-05.md` | 5 · Centros de documentación audiovisual | 10 |
| `documentacion-06.md` | 6 · Cultura y actualidad | **40** |

**El reparto de este cuadernillo es el más desequilibrado del proyecto**: casi la
mitad de sus preguntas —cuarenta de ochenta y dos— son de **cultura y actualidad**,
un epígrafe que no se estudia en una norma sino que se comprueba dato a dato.

**Y se comprobó.** De esas cuarenta, **quince quedaron atadas a un documento**
—nueve al BOE— y las **veinticinco restantes** van marcadas como apoyadas sólo en
la plantilla, listadas juntas en el propio tema. En el conjunto del bloque, **56
de las 82 preguntas se verifican en fuente**, y el tema 5 es el único del proyecto
con **todas** sus preguntas verificadas.

### Información y Contenidos

**178 preguntas** de los cuadernillos de octubre y noviembre de 2024, repartidas
entre los **diez primeros temas** de su Anexo 2 —el undécimo, el de prevención, es
el compartido y está en `prl-especifico.md`—.

| Fichero | Tema | Preguntas |
|---|---|---|
| `informacion-01.md` | 1 · Actualidad nacional e internacional | **121** |
| `informacion-02.md` | 2 · La Unión Europea y sus instituciones | 17 |
| `informacion-03.md` | 3 · Instituciones del Estado y organismos internacionales | 21 |
| `informacion-04.md` | 4 · Código de autorregulación (menores) | 2 |
| `informacion-05.md` | 5 · Real Decreto-ley 4/2018 | — |
| `informacion-06.md` | 6 · Manual de estilo de RTVE | 9 |
| `informacion-07.md` | 7 · Directiva (UE) 2018/1808 | 2 |
| `informacion-08.md` | 8 · Resolución del Parlamento Europeo de 25/11/2020 | 1 |
| `informacion-09.md` | 9 · Informe mundial de la UNESCO 2021/2022 | 5 |
| `informacion-10.md` | 10 · Carta ética mundial para periodistas (FIP) | — |

**Dos temas del programa no tienen ni una pregunta**, el 5 y el 10, y sus ficheros
no llegan a existir: el reparto no inventa un banco donde no lo hay. Se escriben
contra la norma y el documento, sin examen que los respalde, y su informe de
cobertura lo dice.

De los cuatro cuadernillos de la ocupación se usan **dos**. El de la prueba
anulada por filtración no aporta ninguna pregunta —el PDF guardado da 880 bytes
de marca de agua—, y el de **Radio Clásica se descarta entero**: su bloque
específico son 97 preguntas de teoría de la música y repertorio, y **no pregunta
ni una vez por ninguno de los siete documentos** que el Anexo 2 nombra con su
enlace, mientras que los otros dos preguntan por cinco de los siete. Es el examen
de otro Anexo 2. El motivo está en el acta, en una fila con `*` en el número, y el
script lo imprime cada vez que se regenera el banco.

### Gestión Administrativa

**75 preguntas** del cuadernillo de **26 de enero de 2025** —la prueba más tardía de todo el
proyecto—, repartidas entre los **doce primeros temas** de su Anexo 2. El decimotercero es el de
prevención, que ya comparten las otras tres ocupaciones.

| Fichero | Tema | Preguntas |
|---|---|---|
| `gestion-administrativa-01.md` | 1 · Documento, acto administrativo, registro y archivo | 7 |
| `gestion-administrativa-02.md` | 2 · El contrato de trabajo | 8 |
| `gestion-administrativa-03.md` | 3 · Seguridad Social | 9 |
| `gestion-administrativa-04.md` | 4 · Nóminas | 8 |
| `gestion-administrativa-05.md` | 5 · Contabilidad y Plan General de Contabilidad | **15** |
| `gestion-administrativa-06.md` | 6 · Matemática financiera | 10 |
| `gestion-administrativa-07.md` | 7 · Probabilidad y estadística | 11 |
| `gestion-administrativa-08.md` | 8 · Ofimática y proceso de la información | 2 |
| `gestion-administrativa-09.md` | 9 · Windows 10 Pro 22H2 | 1 |
| `gestion-administrativa-10.md` | 10 · La red Internet | 1 |
| `gestion-administrativa-11.md` | 11 · Office 2019 | 2 |
| `gestion-administrativa-12.md` | 12 · Microsoft Teams | 1 |

**Su plantilla estaba sin leer.** El PDF lleva la fuente incrustada sin tabla de caracteres, como las
tres que ya arregló `herramientas/plantilla_ocr.py`; pasada esa herramienta salen las **96
respuestas**. Es la cuarta plantilla que recupera y la primera de una ocupación nueva.

**Y es la ocupación con más respuestas oficiales equivocadas del proyecto: cuatro.** Van contadas en
los informes de refutación de sus temas 2, 3, 5 y 6.

### Producción

**66 preguntas** de un solo cuadernillo, `81_preguntas_produccion`, repartidas entre los dieciséis
temas de su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `produccion-01.md` | 1 · La producción: plan de trabajo, organización y fases | 2 |
| `produccion-02.md` | 2 · Ley de Propiedad Intelectual | 5 |
| `produccion-03.md` | 3 · La escaleta y el guion. Desglose | **6** |
| `produccion-04.md` | 4 · Géneros y formatos audiovisuales | 3 |
| `produccion-05.md` | 5 · Equipos humanos | 2 |
| `produccion-06.md` | 6 · Captación de imagen y sonido | **7** |
| `produccion-07.md` | 7 · El estudio de televisión | 1 |
| `produccion-08.md` | 8 · Producción en exteriores | 5 |
| `produccion-09.md` | 9 · Escenografía e iluminación | 5 |
| `produccion-10.md` | 10 · Medios artísticos | 3 |
| `produccion-11.md` | 11 · Tratamiento de imagen y sonido | **6** |
| `produccion-12.md` | 12 · Transporte de la señal | 4 |
| `produccion-13.md` | 13 · Control central | 3 |
| `produccion-14.md` | 14 · El presupuesto | 2 |
| `produccion-15.md` | 15 · Organismos nacionales e internacionales | 5 |
| `produccion-16.md` | 16 · Aspectos jurídicos de la producción | **7** |

**Ningún punto del anexo se queda sin preguntas**, cosa que no ocurre en Gestión —seis puntos a
cero— ni en Realización (Asistencia) —uno—. El reparto de este tribunal **cubrió el anexo entero**.

**Y una trampa de nombre que costó un reparto falso.** El cuadernillo se llama
`81_preguntas_produccion`, y los de la otra ocupación,
`77_preguntas_produccion_asist` y `78_preguntas_produccion_asist_2_llamamiento`.
**«produccion» está dentro de «produccion_asist»**, así que la selección por
subcadena metía el examen de una ocupación en el banco de la otra: Producción
(Asistencia) llegó a decir «123 de 189, quedan 66 sin clasificar» **contando
preguntas que no eran suyas**. Se arregló con una lista explícita —`SOLO` en
`herramientas/banco_especifico.py`— que **nombra los cuadernillos de cada
ocupación en vez de buscarlos por su nombre**. La misma trampa afectaba a
Realización (Asistencia), y se arregló igual.

**Una errata de plantilla y una respuesta mal enunciada.** La errata es la **nº 88**, sobre
subcontratación en los contratos públicos: **ninguna de las cuatro opciones dice lo que dice la Ley
9/2017**. La marcada exige informar «sólo por encima del 30 %» y obtener «siempre» autorización
expresa, y el artículo 215.2.b) obliga a comunicar por escrito **«en todo caso»**, mientras que el
215.2.d) reserva la autorización expresa a los contratos secretos o reservados; el 30 % y los cinco
millones son del artículo **217.2**, que mide cuándo **la Administración** tiene que comprobar los
pagos a los subcontratistas. La mal enunciada es la **nº 75**, que da por buena una afirmación que
dice «solo con consentimiento» cuando el artículo 6 del reglamento europeo prevé **seis bases de
licitud**. Las dos van contadas en `informes/refutacion-produccion.md`.

**Dos preguntas de este cuadernillo van al banco compartido de prevención de riesgos laborales** —la
29 y la 83— y por eso están en `reclasificadas.tsv` y no en el reparto de arriba.

### Realización (Asistencia)

**209 preguntas** de los dos llamamientos de octubre y noviembre de 2024: **es el banco más grande
del proyecto**, y el único con **dos cuadernillos completos de 120 preguntas cada uno y sus dos
plantillas oficiales**.

| Fichero | Tema | Preguntas |
|---|---|---|
| `realizacion-01.md` | 1 · Géneros y formatos televisivos | 2 |
| `realizacion-02.md` | 2 · El guion | 12 |
| `realizacion-03.md` | 3 · Organización general de la producción | 4 |
| `realizacion-04.md` | 4 · Decorados: planos y perspectivas | 3 |
| `realizacion-05.md` | 5 · La tecnología en el ámbito de la realización | **34** |
| `realizacion-06.md` | 6 · Lenguaje técnico y narrativo | 20 |
| `realizacion-07.md` | 7 · La cámara, accesorios y posibilidades | 12 |
| `realizacion-08.md` | 8 · La iluminación | 9 |
| `realizacion-09.md` | 9 · El sonido | 13 |
| `realizacion-10.md` | 10 · El mezclador de vídeo | **35** |
| `realizacion-11.md` | 11 · El estudio: controles y plató | 8 |
| `realizacion-12.md` | 12 · Las unidades móviles | 1 |
| — | 13 · La asistencia en grabación | **0** |
| `realizacion-14.md` | 14 · La retransmisión | 4 |
| `realizacion-15.md` | 15 · La emisión: pantallas, servidores y grafismo | 6 |
| `realizacion-16.md` | 16 · Realidad aumentada y producción online | 9 |
| `realizacion-17.md` | 17 · La asistencia en plató. Regiduría | 4 |
| `realizacion-18.md` | 18 · Canales online | 5 |
| `realizacion-19.md` | 19 · La puesta en escena | 6 |
| `realizacion-20.md` | 20 · Postproducción | **19** |
| `realizacion-21.md` | 21 · Prevención de riesgos laborales | 3 |

**Dos temas se llevan casi un tercio del banco**: el mezclador de vídeo con 35 preguntas y la
tecnología de la realización con 34. Son **los dos únicos temas de todo el proyecto que pasan de
treinta**.

**Y un tema se queda sin ninguna**: el 13, la asistencia en grabación, que es justamente el que
describe el oficio que da nombre a la ocupación. Se desarrolla igual y su ficha lo declara.

**Una errata de plantilla y una pregunta mal construida.** La errata es la **nº 46 del primer
llamamiento**, que pregunta qué sensorización corresponde al sistema free-d y marca una opción que
describe unos postes de croma: **la correcta es la a)**, la de la lectura de pequeñas marcas de
referencia. La mal construida es la **nº 47 del segundo llamamiento**, sobre la unidad de control de
cámara, donde **ninguna** de las cuatro opciones la define. Las dos van contadas en el informe de
refutación.

**Siete preguntas dependen de una imagen** que el texto del cuadernillo no conserva y se recogen sin
verificar. **Y dos se salen del programa**: la historia de la primera emisión televisada española y
la entidad de gestión de derechos de autor, materias que el Anexo 2 de esta ocupación no contiene.

**El texto del segundo cuadernillo hubo que rehacerlo.** Traía **252 fragmentos sobrantes** que el
banco recogía como si fueran opciones; se reextrajo con `herramientas/extraer_examen.py`, que
descarta el trozo repetido por su altura. Sin ese arreglo, un tercio de sus preguntas habría llegado
al banco con texto ajeno pegado detrás.

### Gestión

**81 preguntas** del cuadernillo de **Gestión** de 2024, repartidas entre los **treinta primeros
temas** de su Anexo 2. El trigésimo primero es el de prevención, que ya comparten las otras
ocupaciones específicas.

| Fichero | Tema | Preguntas |
|---|---|---|
| `gestion-03.md` | 3 · Convenios colectivos | 2 |
| `gestion-04.md` | 4 · El contrato de trabajo | **9** |
| `gestion-05.md` | 5 · Modificación de las condiciones | 4 |
| `gestion-06.md` | 6 · Tiempo de trabajo | 2 |
| `gestion-07.md` | 7 · El salario | 6 |
| `gestion-08.md` | 8 · Derechos y deberes | 1 |
| `gestion-09.md` | 9 · Protección de datos | 6 |
| `gestion-11.md` | 11 · Modelo contable y Plan General de Contabilidad | 3 |
| `gestion-12.md` | 12 · Proceso contable y cuentas anuales | 2 |
| `gestion-13.md` | 13 · El patrimonio y el balance | 4 |
| `gestion-14.md` | 14 · Gastos, ingresos, tesorería, existencias y acreedores | 2 |
| `gestion-15.md` | 15 · Inmovilizado material y amortización | 1 |
| `gestion-17.md` | 17 · Costes de producción y contabilidad de costes | 4 |
| `gestion-18.md` | 18 · La función de tesorería | 2 |
| `gestion-19.md` | 19 · La información financiera | 4 |
| `gestion-20.md` | 20 · Impuesto sobre el Valor Añadido | 3 |
| `gestion-21.md` | 21 · Planificación estratégica y control de gestión | 1 |
| `gestion-22.md` | 22 · Seguridad Social | 1 |
| `gestion-24.md` | 24 · Nómina | **7** |
| `gestion-25.md` | 25 · La empresa como organización | **6** |
| `gestion-26.md` | 26 · La gestión por competencias | 2 |
| `gestion-27.md` | 27 · El proceso de producción en televisión | 3 |
| `gestion-28.md` | 28 · Matemática financiera | 4 |
| `gestion-29.md` | 29 · Estadística descriptiva básica | 2 |

**Seis puntos no tienen ni una pregunta** —el 1, el 2, el 10, el 16, el 23 y el 30— y por eso no
tienen fichero de banco. Se desarrollan igual en el temario.

**Se descartan enteros los dos cuadernillos de Gestión Abogado/a**, primero y segundo llamamiento.
Es otra ocupación tipo con su propio Anexo 2: su bloque específico pregunta por propiedad
intelectual, Reglamento General de Protección de Datos y Ley 13/2022, materias que el Anexo 2 de
Gestión no contiene. El motivo está en el acta, en dos filas con `*` en el número, y el script lo
imprime cada vez que se regenera el banco.

**Una errata de plantilla y una pregunta rota.** La errata es la **nº 32**, que pide el indicador
que ignora los intereses y responde **BAI**, el único de los cuatro que sí los computa. La rota es
la **nº 83**, que pregunta por la prescripción de las faltas muy graves y cuyas cuatro opciones
hablan de la publicación en el BOE: **ninguna responde**. Las dos van contadas en los informes de
refutación.

Y **dos preguntas de este cuadernillo se apartan del programa**: la nº 6 y la nº 89 examinan de la
**Ley Orgánica 7/2021**, que el Anexo 2 no cita en ningún punto.

### Montaje de Equipos Audiovisuales

**75 preguntas** del cuadernillo de **Montaje de Equipos Audiovisuales** de 2024, repartidas entre
los **seis primeros puntos** de su Anexo 2, que aquí se desarrollan en **diez temas**. El séptimo
punto es el de prevención, que ya comparten las otras ocupaciones específicas.

| Fichero | Tema | Preguntas |
|---|---|---|
| `montaje-equipos-01.md` | 1 · Instalaciones de televisión y unidades móviles | 2 |
| `montaje-equipos-02.md` | 2 · Profesionales, roles y operativa de una grabación | 1 |
| `montaje-equipos-03.md` | 3 · Las cámaras: tipos, elementos externos y manejo seguro | 7 |
| `montaje-equipos-04.md` | 4 · Cabezas de cámara y soportes: instalación y nivelado | 8 |
| `montaje-equipos-05.md` | 5 · Conectores, cables y elementos de conexión | **17** |
| `montaje-equipos-06.md` | 6 · Sonido: micrófonos, altavoces y soportes | 11 |
| `montaje-equipos-07.md` | 7 · Maquinaria para el movimiento de cámaras | **13** |
| `montaje-equipos-08.md` | 8 · La cabeza caliente | 2 |
| `montaje-equipos-09.md` | 9 · Montaje de equipos en estudios y exteriores | **13** |
| `montaje-equipos-10.md` | 10 · Asistencia a la operación de cámara | 1 |

**Los dos puntos de conexión del Anexo 2 —el 2.4 y el 3.2— se han unido en un solo tema**, el 5,
porque preguntan de lo mismo: conectores y elementos de conexión. Con los dos juntos, **es el punto
más preguntado de la ocupación con diecisiete preguntas: casi una de cada cinco**.

**Siete de las trece preguntas del tema 9 no son de montaje audiovisual sino de electricidad
básica** —potencia, resistividad, ley de Ohm, aparatos de medida y protecciones del cuadro—, porque
el subpunto 5.6 del Anexo 2 dice «baja tensión» y el tribunal lo tomó al pie de la letra.

**Tres preguntas defectuosas, ninguna errata de plantilla.** La **nº 63** llama «fonómetro» al
**sonómetro**, y el nombre correcto no está entre las opciones. La **nº 9** pide el «rango dinámico»
del oído y responde con un **margen de frecuencias**, que se mide en hercios y no en decibelios. Y la
**nº 43 repite literalmente la nº 26**: **una sola respuesta vale dos preguntas de noventa y seis**.
Las tres van contadas en los informes de refutación.

**Y diez preguntas descansan sólo en la plantilla oficial**, que es la proporción más alta del
proyecto: son las que citan una máquina por su modelo o su referencia de catálogo, y esa
documentación no se ha podido consultar. Cada una va declarada en la trazabilidad de su tema.

### Edición, Montaje y Procesos Audiovisuales

**86 preguntas** del cuadernillo de **Edición, Montaje y Procesos Audiovisuales** de 2024, repartidas
entre los **seis primeros puntos** de su Anexo 2, que aquí se desarrollan en **diez temas**. El
séptimo punto es el de prevención.

| Fichero | Tema | Preguntas |
|---|---|---|
| `edicion-montaje-01.md` | 1 · Electrónica e informática aplicadas | 4 |
| `edicion-montaje-02.md` | 2 · Colorimetría y el color en televisión | 10 |
| `edicion-montaje-03.md` | 3 · Conceptos básicos de sonido | 4 |
| `edicion-montaje-04.md` | 4 · Tratamiento digital de la señal de televisión | **15** |
| `edicion-montaje-05.md` | 5 · Soportes, formatos, grabación e ingesta | 8 |
| `edicion-montaje-06.md` | 6 · Equipos de medida y control | 3 |
| `edicion-montaje-07.md` | 7 · Edición de vídeo: Avid Media Composer | **13** |
| `edicion-montaje-08.md` | 8 · Edición en directo y retransmisiones (EVS) | 9 |
| `edicion-montaje-09.md` | 9 · Incrustaciones, grafismo y postproducción | 8 |
| `edicion-montaje-10.md` | 10 · Lenguaje audiovisual y teoría del montaje | **12** |

**El punto 1 del Anexo 2 se ha repartido en tres temas** —electrónica e informática, colorimetría y
sonido—, porque sus cuatro subpuntos son cuatro materias distintas y **uno solo de ellos, el de
colorimetría, se lleva diez preguntas**. Y **el punto 5, el de edición de vídeo, se ha repartido en
tres**: el montador de Avid, el sistema de repetición en directo y la composición, que es como el
examen los pregunta.

**Este cuadernillo no tiene ni una pregunta de prevención de riesgos laborales**, aunque el punto 7
de su Anexo 2 la exija. **El tema compartido de prevención va igual en el volumen**, porque el
programa lo manda.

**Tres preguntas defectuosas, ninguna errata de plantilla.** La **nº 61 repite literalmente la nº
57**: los dos enunciados se diferencian en tres letras y tienen las mismas cuatro opciones en el
mismo orden. La **nº 5** escribe **«NFL»** donde la literatura escribe **«NCL»**. Y la **nº 50**
ofrece como opción falsa un «monitor con *Hybrid* Dynamic Range», **que no existe**: la palabra
pertenece a la curva **HLG**. Las tres van contadas en los informes de refutación.

**Y treinta y cinco preguntas descansan sólo en la plantilla oficial**, que es la cifra más alta del
proyecto en términos absolutos: **veintiocho salen del manejo de tres programas comerciales** cuya
documentación no se ha podido consultar. Cada una va declarada en la trazabilidad de su tema.

### Información Gráfica y Captación de Imagen y Sonido

**94 preguntas** del cuadernillo de **Información Gráfica y Captación de Sonido** de 2024, repartidas
entre los **seis primeros puntos** de su Anexo 2, que aquí se desarrollan en **once temas**. El
séptimo punto es el de prevención.

**Es el cuadernillo más largo de todos los que este proyecto ha trabajado**: **ciento seis
preguntas**, frente a las noventa o noventa y seis de los demás. Seis van al bloque común y dos al
banco compartido de prevención.

| Fichero | Tema | Preguntas |
|---|---|---|
| `informacion-grafica-01.md` | 1 · La luz, el color y la percepción visual | **13** |
| `informacion-grafica-02.md` | 2 · Señales y formatos: de la señal a la medida | 12 |
| `informacion-grafica-03.md` | 3 · La cámara de vídeo y el sensor | 8 |
| `informacion-grafica-04.md` | 4 · Los objetivos, los filtros y los accesorios | **15** |
| `informacion-grafica-05.md` | 5 · Soportes de cámara y estabilización | 9 |
| `informacion-grafica-06.md` | 6 · El sonido en reportaje y producción ligera | 8 |
| `informacion-grafica-07.md` | 7 · La iluminación en reportaje y producción ligera | 7 |
| `informacion-grafica-08.md` | 8 · Control de cámara y ajuste de imagen | 7 |
| `informacion-grafica-09.md` | 9 · Envíos, directos y cámaras robotizadas | 3 |
| `informacion-grafica-10.md` | 10 · Lenguaje audiovisual | **12** |

**El punto 11, el de teoría de la información audiovisual, no tiene ni una pregunta y por eso no
tiene fichero de banco.** Se desarrolla igual en el temario, contra el programa.

**El punto 3 del Anexo 2 se ha repartido en seis temas** —cámara y sensor, objetivos y filtros,
soportes, sonido, iluminación, control de cámara y envíos—, porque sus catorce subpuntos son
materias distintas y **uno solo de ellos, el de objetivos, se lleva quince preguntas**.

**Cuatro preguntas con defecto de construcción, ninguna errata de plantilla.** Las **nº 71 y 36
dependen enteramente de una imagen** —una señal de prueba y un plano de planificación— que un temario
escrito no puede reproducir: **son las dos primeras preguntas de esta clase que el proyecto
encuentra**, y su tratamiento está documentado en el informe de refutación. La **nº 39** ofrece las
cifras correctas del margen audible **con la unidad equivocada** —micrómetros por hercios—. Y la **nº
32** ofrece una opción **literalmente cierta que no responde a lo que se pregunta**.

**Y sólo siete preguntas descansan sólo en la plantilla oficial: el 7,4 %, la proporción más baja de
todas las ocupaciones audiovisuales del proyecto.** Ochenta y seis de las noventa y cuatro **se
contestan leyendo**.

### Sonido

**86 preguntas**, repartidas entre los diecisiete temas de su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `sonido-01.md` | 1 · Electricidad y electrónica básicas | **12** |
| `sonido-02.md` | 2 · Principios físicos del sonido y la audición | 6 |
| — | 3 · Música, instrumentos e historia de la música | **0** |
| `sonido-04.md` | 4 · Acústica arquitectónica | **1** |
| `sonido-05.md` | 5 · Micrófonos, soportes y accesorios | 8 |
| `sonido-06.md` | 6 · Señales de contribución | 4 |
| `sonido-07.md` | 7 · Mezcla y tratamiento del sonido | 7 |
| `sonido-08.md` | 8 · Postproducción, efectos y estación de trabajo | 2 |
| `sonido-09.md` | 9 · Grabación de sonido | 4 |
| `sonido-10.md` | 10 · Sonorización: altavoces y amplificadores | 6 |
| `sonido-11.md` | 11 · Líneas y conexiones | 8 |
| `sonido-12.md` | 12 · El sonido en la radio y la televisión | **1** |
| `sonido-13.md` | 13 · Radiofrecuencia | 3 |
| `sonido-14.md` | 14 · Medición y sonoridad | 6 |
| `sonido-15.md` | 15 · Audio multicanal | 4 |
| `sonido-16.md` | 16 · Audio sobre IP | **9** |
| `sonido-17.md` | 17 · Audio sobre protocolos digitales | 5 |

**Un solo cuadernillo**, `85_preguntas_sonido`, del proceso de 2024 y con su plantilla completa.

**El punto 1.6 —música e historia de la música— no ha dado ni una pregunta.** Es el **segundo caso del
proyecto**, después del punto 11 de Información Gráfica, y **el tema se ha escrito igual, contra el
programa**.

**El enunciado más largo de todo el anexo tiene UNA pregunta, y es sobre un gesto de la mano.** Es la
respuesta peor documentada de las 86: **los gestos del control son convenio de casa y no hay fuente
pública que los fije**, y el temario lo declara en lugar de inventar una.

**Cuatro salvedades sobre respuestas correctas, ninguna errata de plantilla.** La **nº 44** tiene
**dos opciones idénticas, palabra por palabra**; la **nº 36** trae una fórmula cuyas unidades no
encajan con su propio enunciado; la **nº 46** pide «lo más aproximado» y hace falta, porque el valor
exacto es 2,67 y la opción marcada es 2,5; y la **nº 82** llama al multímetro herramienta fundamental
para medir impedancia, cuando un multímetro corriente mide resistencia en continua. **Las cuatro
respuestas oficiales siguen siendo las correctas de sus cuatro opciones**, y **la cuenta de erratas de
plantilla del proyecto sigue en diez**.

**Un error de nomenclatura del propio anexo**: su punto 12 dice «Norma AES R-128», y **la R 128 no es
una norma de la Sociedad de Ingeniería de Audio: es una recomendación de la Unión Europea de
Radiodifusión**. El temario lo declara, porque quien busque «norma AES R 128» no encontrará nada.

### Técnica de Equipos y Sistemas Electrónicos

**114 preguntas**, repartidas entre los diecisiete temas de su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `tese-01.md` | 1 · Conceptos básicos de electricidad | 6 |
| `tese-02.md` | 2 · Componentes electrónicos | **12** |
| `tese-03.md` | 3 · Electrónica de potencia | 4 |
| `tese-04.md` | 4 · Amplificadores operacionales | 5 |
| `tese-05.md` | 5 · Electrónica digital | 6 |
| `tese-06.md` | 6 · Circuitos integrados y secuenciales | 4 |
| `tese-07.md` | 7 · Memorias, lógica programable y microprocesadores | **1** |
| `tese-08.md` | 8 · La señal audiovisual y sus sincronismos | **10** |
| `tese-09.md` | 9 · La señal audiovisual sobre redes | 7 |
| `tese-10.md` | 10 · Equipos utilizados en televisión y radio | **19** |
| `tese-11.md` | 11 · Control de iluminación escénica | **1** |
| `tese-12.md` | 12 · Comunicaciones y redes | **13** |
| `tese-13.md` | 13 · Equipos de medida y control | 8 |
| `tese-14.md` | 14 · Medidas de vídeo, audio y radiofrecuencia | 9 |
| `tese-15.md` | 15 · Mantenimiento preventivo y correctivo | 2 |
| `tese-16.md` | 16 · Mantenimiento en televisión | 3 |
| `tese-17.md` | 17 · Seguridad en instalaciones técnicas | 4 |

**Dos cuadernillos de tamaño muy distinto**: `70_preguntas_tese_a`, de **96 preguntas**, y
`71_preguntas_tese_b`, que **sus propias instrucciones describen como «30 preguntas (25 principales
más 5 de reserva)»**. **No es un fallo de extracción: es un examen más corto**, y se lee entero.

**Es la ocupación con más preguntas dependientes de una imagen de todo el proyecto: treinta.** Piden
leer un esquema de circuito, un símbolo de componente, la pantalla de un instrumento o una fotografía
de conectores. **Siete de esas treinta están en un solo tema**, el 14, que con siete de nueve tiene la
proporción más alta de la ocupación. El temario no describe lo que no ha visto: declara cada una y
aporta **la regla de su familia**.

**Ninguna respuesta oficial es errónea y ninguna es impugnable.** Es el único banco grande del
proyecto del que puede decirse sin salvedades.

**Cinco preguntas se han reclasificado a mano**: la nº 3 y la nº 6 del primer cuadernillo van al bloque
común —complemento de disponibilidad y definiciones de la Ley 13/2022—; la 22, la 47, la 51 y la 72
van al banco compartido de prevención; y la **nº 96, valores de alta tensión, vuelve al específico**,
porque es materia del punto 20 de esta ocupación y no del tema 8 del general. **De esas cuatro de
prevención, dos no tenían respuesta en el tema compartido** —la actuación ante una emergencia y la
iluminación de los lugares de trabajo—, **y el tema se ha ampliado con dos apartados nuevos**.


### Diseño Gráfico

**86 preguntas**, repartidas entre los trece temas de su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `diseno-grafico-01.md` | 1 · Óptica: la luz, el color y la imagen | 8 |
| `diseno-grafico-02.md` | 2 · Conocimientos básicos de televisión | 4 |
| `diseno-grafico-03.md` | 3 · Historia del diseño, el cine y la televisión | **15** |
| `diseno-grafico-04.md` | 4 · Composición, montaje, animación y géneros | 8 |
| `diseno-grafico-05.md` | 5 · Fundamentos del diseño y tipografía | 9 |
| `diseno-grafico-06.md` | 6 · Diseño audiovisual y sintaxis de la imagen | 2 |
| `diseno-grafico-07.md` | 7 · Procesos y métodos de diseño | 2 |
| — | 8 · Grafismo informativo, infografía e interfaz | **0** |
| `diseno-grafico-09.md` | 9 · La continuidad | 4 |
| `diseno-grafico-10.md` | 10 · Equipos y programas de diseño | **20** |
| `diseno-grafico-11.md` | 11 · Postproducción digital | 5 |
| `diseno-grafico-12.md` | 12 · La imagen corporativa | 6 |
| `diseno-grafico-13.md` | 13 · Legislación y derechos de autor | 3 |

**Un solo cuadernillo**, `07_preguntas_diseno_grafico`, de **96 preguntas —80 principales más 16 de
reserva—**. De ellas, **86 son del específico y 10 del bloque común**.

**El reparto es el más desigual del proyecto en un anexo pequeño**: **dos puntos se llevan 35 de las
86**, el 41 % del examen. El de equipos y programas se lleva **veinte** —nueve de ellas de un solo
programa de composición— y el de historia, **quince**. En el otro extremo, tres puntos se llevan dos
preguntas o menos y **uno no se lleva ninguna**.

**El punto sin preguntas es el 8** —grafismo informativo, infografía e interfaz—. **Su tema se escribe
igual, contra el programa**: es el quinto caso del proyecto, y **el único del anexo que habla de
producto digital.**

**Cinco preguntas dependen de una figura**: la 5, la 22, la 68, la 71 y la 87. **Son el 5,8 %**, una
proporción baja para una ocupación gráfica y muy inferior al 26 % de Técnica de Equipos.

**Ninguna respuesta oficial es errónea y ninguna es impugnable.** **Tres llevan aviso**: la **nº 9**
llama regla de composición al espacio en blanco, que es un elemento; la **nº 32** tiene dos opciones
defendibles; y la **nº 95** pregunta cuánto suman los ángulos interiores de un triángulo, **que no es
materia de ningún punto del anexo**. **En las tres, la opción de la plantilla sigue siendo la mejor de
las cuatro.**

**Ninguna pregunta se ha reclasificado a mano**: las diez del bloque común las coge el banco general
por sus palabras clave, y las ochenta y seis del específico se reparten a mano desde el principio.


### Técnica Informática

**90 preguntas**, repartidas entre los veintitrés temas en que este proyecto desarrolla su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `tecnica-informatica-01.md` | 1 · Bases de datos y el modelo relacional | 7 |
| `tecnica-informatica-02.md` | 2 · Comunicaciones y redes: modelos y direccionamiento | **8** |
| `tecnica-informatica-03.md` | 3 · Protocolos de red, conmutación y encaminamiento | **9** |
| `tecnica-informatica-04.md` | 4 · Internet: origen, servicios y protocolos seguros | 3 |
| `tecnica-informatica-05.md` | 5 · Elementos de interconexión y conmutación | 2 |
| `tecnica-informatica-06.md` | 6 · Programación orientada a objetos y frameworks | 6 |
| `tecnica-informatica-07.md` | 7 · Métrica V3, metodologías ágiles y el marco Scrum | 2 |
| `tecnica-informatica-08.md` | 8 · Desarrollo de aplicaciones web y programación de scripts | **8** |
| `tecnica-informatica-09.md` | 9 · Desarrollo de aplicaciones en las dos plataformas empresariales | 4 |
| `tecnica-informatica-10.md` | 10 · El lenguaje de marcado extensible y su familia | 4 |
| `tecnica-informatica-11.md` | 11 · Arquitectura orientada a servicios y servicios web | 3 |
| — | 12 · Desarrollo multimedia: difusión en continuo | **0** |
| `tecnica-informatica-13.md` | 13 · Otros lenguajes: C, C++, Java y Python | 3 |
| `tecnica-informatica-14.md` | 14 · Arquitectura y administración de sistemas operativos | 5 |
| — | 15 · Políticas de conservación de datos | **0** |
| `tecnica-informatica-16.md` | 16 · Sistemas operativos personales | 6 |
| `tecnica-informatica-17.md` | 17 · Arquitectura de ordenadores y virtualización | 2 |
| `tecnica-informatica-18.md` | 18 · Sistemas multimedia y codificación audiovisual | 4 |
| `tecnica-informatica-19.md` | 19 · Sistemas de producción digital audiovisual | 2 |
| `tecnica-informatica-20.md` | 20 · Marcos de gestión de la seguridad y del servicio | 3 |
| `tecnica-informatica-21.md` | 21 · La seguridad en redes | 5 |
| `tecnica-informatica-22.md` | 22 · Protección de datos personales | 3 |
| `tecnica-informatica-23.md` | 23 · El Esquema Nacional de Seguridad | 1 |

**Un solo cuadernillo**, `48_preguntas_tec_informatica`, que sus instrucciones describen como **96
preguntas —80 principales más 16 de reserva—**. De ellas, **90 son del específico y 6 del bloque
común**: la 2 y la 29 de la Ley 31/1995, la 21 y la 49 del II Plan de Igualdad, la 79 de la Ley 8/2009
y la 87 de la Constitución.

**Es el único banco específico del proyecto en el que NINGUNA pregunta depende de una imagen.** Donde
las demás ocupaciones técnicas obligan a leer un esquema o una pantalla, aquí **todo lo que se
pregunta está escrito**, y el temario contesta el examen entero sin remitir a la plantilla ni una vez.

**Dos puntos del anexo no han dado ni una pregunta** —el 14, formatos de difusión en continuo para
web, y el 18, políticas de conservación de datos—. **Sus temas se escriben igual, contra el
programa**: son el tercer y el cuarto caso del proyecto, tras el punto 11 de Información Gráfica y el
1.6 de Sonido.

**Ninguna respuesta oficial es errónea y ninguna es impugnable.** **Tres llevan salvedad o precisión
declarada**: la **nº 5** afirma que en Python no se pueden instanciar clases —y sí se pueden—; la
**nº 71** atribuye al protocolo web seguro (**HTTPS**) lo que Netscape creó en 1994, que fue la capa
de conexión segura (**SSL**); y la **nº 88** da 14 años cuando la ley dice «mayor de catorce años». **En las tres, la opción de la plantilla sigue siendo la mejor de
las cuatro**, que es lo que las separa de una errata.

**Ninguna pregunta se ha reclasificado a mano** en esta ocupación: las seis del bloque común las coge
el banco general por sus propias palabras clave, y las noventa del específico se reparten a mano
desde el principio.


### Ingeniería Técnica · Telecomunicación

**85 preguntas**, repartidas entre los diecinueve temas en que este proyecto desarrolla su Anexo 2.

| Fichero | Tema | Preguntas |
|---|---|---|
| `ing-tec-teleco-01.md` | 1 · Marco regulatorio de las telecomunicaciones | 2 |
| `ing-tec-teleco-02.md` | 2 · La señal y la conversión analógico-digital | 3 |
| `ing-tec-teleco-03.md` | 3 · La señal audiovisual y su sincronización | **14** |
| `ing-tec-teleco-04.md` | 4 · Televisión digital y compresión | 4 |
| `ing-tec-teleco-05.md` | 5 · Difusión terrestre y por satélite | 3 |
| `ing-tec-teleco-06.md` | 6 · Alta y ultraalta definición | 4 |
| `ing-tec-teleco-07.md` | 7 · Vídeo y audio sobre red | 5 |
| `ing-tec-teleco-08.md` | 8 · Equipamiento de televisión | 7 |
| — | 9 · Estudios, continuidades y salas técnicas | **0** |
| `ing-tec-teleco-10.md` | 10 · Sistemas de redacción digital | 3 |
| `ing-tec-teleco-11.md` | 11 · Postproducción de vídeo y audio | 1 |
| `ing-tec-teleco-12.md` | 12 · Sonido | **18** |
| — | 13 · Radio digital | **0** |
| `ing-tec-teleco-14.md` | 14 · Antenas, transmisores y propagación | 3 |
| `ing-tec-teleco-15.md` | 15 · Comunicaciones y redes | **18** |
| — | 16 · Ingeniería de implantación | **0** |
| — | 17 · Seguridad en las instalaciones técnicas | **0** |
| — | 18 · Seguridad de la información | **0** |
| — | 19 · Protección de datos personales | **0** |

**Un solo cuadernillo**, `50_preguntas_tec_teleco`, de **96 preguntas —80 principales más 16 de
reserva—**. De ellas, **85 son del específico y 11 del bloque común**.

**Una advertencia sobre la fuente**: **su PDF trae la fuente incrustada sin tabla de caracteres**, de
modo que el texto se extrae como glifos numerados. **Se lee de la transcripción por reconocimiento
óptico que está al lado**, y **los enunciados y las opciones se han contrastado uno a uno contra la
plantilla oficial.**

**El reparto es el más desigual de todo el proyecto**: **dos puntos —sonido y redes— se llevan
dieciocho preguntas cada uno**, el **42 %** del examen específico entre los dos; con el de la señal
audiovisual, **50 de 85: el 59 %**. En el otro extremo, **diez puntos del anexo no se llevan
ninguna**.

**Cuatro de esos diez son el corazón del oficio**: estudios, continuidades, salas técnicas e
ingeniería de implantación. **Sus temas se escriben igual, contra el programa**: lo que piden es saber
**dibujar** una instalación, y **eso es lo que un examen escrito no sabe preguntar bien.**

**Ninguna pregunta de este cuadernillo depende de una figura.** **Es el único examen técnico del
proyecto del que puede decirse eso.**

**Ninguna respuesta oficial es errónea y ninguna es impugnable.** **Seis llevan precisión, matiz u
observación**: la **nº 9** nombra un organismo que dejó de existir con ese nombre en 2013; la **nº
41** abrevia una codificación que en rigor es invertida y aleatorizada; la **nº 52** simplifica lo que
se hace en una batería real; la **nº 54** da la cifra de la suite empresarial de esa norma; la **nº
67** llama «balanceada» a una redundancia en la que las dos redes llevan el flujo completo; y la **nº
86** habla de un concentrador, que es equipo antiguo. **Y la nº 75, por el reóstato, no pertenece a
ningún punto del anexo**: se clasifica con las antenas y los transmisores por proximidad, **y se
declara.** **En todas, la opción de la plantilla sigue siendo la mejor de las cuatro.**

**Tres preguntas se han reclasificado a mano** en `reclasificadas.tsv`: la **nº 4** al banco
compartido de prevención —manipulación manual de cargas—, la **nº 43** al tema del convenio colectivo
—teletrabajo— y la **nº 49** al de la Ley 8/2009 —la principal fuente de financiación de RTVE—.
**Ninguna palabra clave las habría cogido bien**, y las tres son del bloque común.


### Realización Televisión

**229 preguntas** de los dos llamamientos de **Realización Televisión** de 2024, repartidas entre los
veintidós temas en que este proyecto desarrolla su Anexo 2. **Es el banco más grande del
proyecto**, por delante de las 209 de Realización (Asistencia).

**El reparto es extraordinariamente desigual, y es el dato que ordena el estudio de la ocupación.** El
punto 4.6 —producción de programas directos y grabados— se lleva **veintitrés preguntas**, que es **el
banco más grande de todo el proyecto en un solo punto de programa**; el 2.2, el guion, veintidós; el
4.1, el lenguaje técnico y narrativo, veinte; y el 4.5, el sonido, dieciocho. En el otro extremo, el
1.4 —la literatura— se lleva dos y el 4.10 —derechos de autor— tres.

**El bloque 1 del Anexo 2, la cultura audiovisual, es lo que distingue a esta ocupación de Realización
(Asistencia)**: música, televisión, artes escénicas, literatura, artes plásticas, fotografía y cine.
Sus siete subpuntos suman **cuarenta preguntas** entre los dos llamamientos.

**Y es la ocupación con más preguntas dependientes de una imagen de todo el proyecto: trece.** Piden
leer una planta de decorado, un esquema de posiciones de cámara, una captura de pantalla de un sistema
de minutado o una fotografía. **Cinco de esas trece están en un solo tema**, el del lenguaje técnico y
narrativo. El temario no describe lo que no ha visto: declara cada una y aporta **la regla de su
familia**.

**Dos preguntas con defecto de construcción, ninguna errata de plantilla.** La **nº 33** del primer
llamamiento —el récord de Óscar— tiene **tres respuestas igualmente correctas**, porque *Ben-Hur*,
*Titanic* y *El señor de los anillos: el retorno del rey* están empatadas a once y **tres de las cuatro
opciones son esas tres películas**: es la undécima costura documentada del proyecto y es
impugnable. **No es errata de plantilla** —*Ben-Hur* es correcta, sólo que no es la única—, así que
**la cuenta de erratas de plantilla sigue en diez**. Y
la **nº 67** pregunta qué **NO** se incluye en un magazine y se responde con una afirmación
materialmente cierta que no contesta a lo que se pregunta.

**Dos preguntas se han reclasificado a mano contra la apariencia de su enunciado**: la nº 108 del
primer llamamiento —la TSNR— parece de señal y **es narrativa**; la nº 101 del segundo —el punto
dulce— parece de sonido, porque está rodeada de preguntas de audio, y **es de óptica**.

**Y el cuadernillo se contradice con otro del mismo proceso**: su pregunta 38 ordena las fases del
guion poniendo la sinopsis después del argumento, y la 28 del cuadernillo de Información Gráfica las
ordena al revés. **Las dos respuestas oficiales son correctas dentro de su propio examen.** El temario
lo declara como dos escuelas, no como error, y sigue en cada ocupación la convención de su enunciado.

### Imagen Personal

**84 preguntas** del cuadernillo de **Imagen Personal** de 2024, repartidas entre los nueve temas en
que este proyecto desarrolla su Anexo 2. De las 96 del cuadernillo, **diez son del bloque común** —la
2, la 5 y la 7 de la Constitución; la 3, la 6, la 8, la 84 y la 87 del III Convenio; la 1 del II Plan
de Igualdad y la 4 de la Ley 8/2009— y **dos son del tema compartido de prevención**, la 40 y la 73,
repartidas a mano en `reclasificadas.tsv` porque el punto 10 del anexo las pide.

**El reparto es de los más desiguales del proyecto y ordena el estudio.** **Tres temas se llevan
cincuenta y cuatro de las ochenta y cuatro: el 64 %.** El de **terminología técnica de medios
audiovisuales**, con veinte; el de **historia del maquillaje y el peinado**, con diecinueve; y el de
**posticería**, con quince. En el otro extremo, **la piel se lleva cinco, la higiene una y la
recreación de personajes ninguna.**

**El punto que más puntúa es el que menos parece de la ocupación.** Las veinte preguntas del tema 6 no
son de maquillaje ni de peluquería: son de **plató** —planos, luz, color, rácord, chroma y quién es
quién—. Es lo que separa a quien maquilla de quien maquilla **para una cámara**.

**Una pregunta está ANULADA por la propia plantilla**: la **nº 57**, sobre la década del corte a lo
*garçon*. La respuesta que marcaba era correcta y la pregunta no puntúa igualmente. **Se reparte con su
aviso**, porque el dato sigue siendo materia del programa.

**Y seis llevan observación declarada, ninguna es errata de plantilla**: la **12** —el ojo encajado en
un círculo y no en un rombo—, la **22** —la «boca de asco» en los cuarenta y no en los treinta—, la
**30** —pelo de caballo frente al yak del taller—, la **43** —«camuflaje» frente a *peek-a-boo*—, la
**49** —pre-base anaranjada frente a malva para la piel cetrina— y la **69** —Toray frente a taklon—.
**No se declaran erratas y hay una razón**: **una errata se declara contra una fuente, y este anexo no
nombra ninguna.** Lo que hay es una discrepancia entre dos usos de la profesión, **y eso el temario lo
enseña en vez de corregirlo**.

**Ninguna pregunta de este cuadernillo depende de una figura.**


### Ingeniería Técnica · Industrial

**Ninguna pregunta, y hay que decirlo aquí antes que en ningún otro sitio.** **Es la primera ocupación
del proyecto sin examen publicado**: la convocatoria anterior no sacó cuadernillo de esta
especialidad, y **no hay por tanto banco específico que construir.** No existe
`especifico-ing-tec-industrial.tsv` y **no se ha inventado ninguno.**

**El volumen se publica igual**, con sus dieciséis temas propios y el compartido de prevención, y
**las únicas preguntas reales que lleva son las cuarenta y ocho de ese banco compartido**, tomadas de
los cuadernillos de 2024 de otras especialidades sobre la materia que todas comparten.

**Lo que ocupa el lugar de las preguntas es la norma citada literalmente**: **veintitrés reales
decretos y leyes volcados del boletín**, y **veintinueve citas verificadas una a una** contra el texto
de su artículo. **Es la ocupación más normativa del proyecto**, y la que mejor tolera no tener examen:
lo que puede caer está escrito con todas sus letras en un boletín oficial.

**Y el dato va escrito donde el opositor lo va a ver**: en la portada del volumen y en su apéndice de
respuestas. **No haber examen es un dato de la convocatoria, no un hueco del temario**, y disimularlo
sería el fallo del apartado 10 del manual otra vez: **un cero que no se explica se lee como si no
faltara nada.**


### Técnica de Equipos, Instalaciones y Sistemas Eléctricos

**Ninguna pregunta, por el mismo motivo y con el mismo aviso.** **Es la segunda ocupación del proyecto
sin examen publicado**: la convocatoria anterior tampoco sacó cuadernillo de esta especialidad. No
existe `especifico-teitse.tsv` y **no se ha inventado ninguno.**

**El volumen se publica con sus quince temas propios y el compartido de prevención**, y **las únicas
preguntas reales que lleva son las cuarenta y ocho de ese banco compartido.**

**Lo que ocupa el lugar de las preguntas es una sola norma leída hasta el fondo**: el **Reglamento
electrotécnico para baja tensión** y **sus cincuenta y dos instrucciones técnicas complementarias**,
más el **Real Decreto 614/2001** de riesgo eléctrico. **Treinta y ocho comprobaciones literales** —diez
por la lente de exactitud y veintiocho por la de citas— **y cero no literales.**

**Y este bloque ha obligado a escribir una lente nueva**, que es lo que más deja al método: **la de
exactitud ancla en «Artículo N» y una instrucción técnica numera por apartados**, así que **sobre doce
de los quince temas habría devuelto un cero vacío.** `refutar_citas` **comprueba cada tramo en negrita
de un bloque de cita como subcadena literal del volcado**, y **es la que sostiene este bloque.**

Se regenera con `herramientas/banco_especifico.py <ocupación>`, y **el reparto se
escribe a mano** en `especifico-<ocupación>.tsv`, una fila por pregunta y con el motivo al
lado. No se clasifica por palabras clave, y no por comodidad: las preguntas del
específico hablan de *beauty shot*, del cuaderno ATA o de SMPTE 2110, y muchas
podrían caer en dos temas a la vez. Una regla automática sobre eso no da un
reparto discutible, da **uno falso que nadie va a revisar**.

Y hay una razón más, que se vio al hacerlo: la pregunta «en una producción
interna, ¿qué derechos tiene la CRTVE?» **es de propiedad intelectual** —la
contesta el artículo 88 de la Ley— y **no nombra la ley ni ningún artículo**.
Ninguna palabra clave la habría cogido.

El script avisa de las **filas que ya no casan con ninguna pregunta**, no cuenta
como pendientes las que ya están repartidas a mano en `reclasificadas.tsv`, y
dice **cuántas preguntas específicas quedan sin repartir**: ahora mismo, **cero**.
