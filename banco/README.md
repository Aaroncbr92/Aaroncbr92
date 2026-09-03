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

Hay uno por ocupación tipo. Los **nueve** que existen suman **975 preguntas**, todas con
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
