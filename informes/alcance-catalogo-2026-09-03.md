# Alcance · las 53 ocupaciones tipo de RTVE y cuánto tenemos escrito

Hecho el **3 de septiembre de 2026**, con **ocho volúmenes cerrados**. Contesta a una
pregunta concreta: **cuántas ocupaciones tiene esta oposición, cuántos temas tiene cada
una y qué parte está escrita**, para saber qué falta para poder dar temario a todas.

**No es una estimación de despacho.** El catálogo se ha descargado entero —las **53
bases específicas del turno libre de la convocatoria 1/2022**—, se ha extraído el Anexo 2
de cada una y se han contado sus puntos con la misma herramienta. Los enunciados están
guardados en `../convocatoria/catalogo/ANEXOS-2-CATALOGO.md` y los números, en
`alcance-ocupaciones-2026-09-03.tsv`.

## Los cuatro números que resumen el alcance

| | |
|---|---:|
| Ocupaciones tipo convocadas | **53** |
| De ellas, **sin temario**: se cubren por concurso de méritos y no hay examen | **4** |
| Ocupaciones con temario | **49** |
| **Ocupaciones al 100 %** con los ocho volúmenes de hoy | **11** |
| Puestos convocados en total | **1.462** |
| De ellos, con examen | **1.115** |
| Puestos de las ocupaciones que ya cubrimos | **886** (61 %) |
| De ellos, con examen | **607** (54 %) |

**Las cuatro sin temario son Arquitectura Superior, Arquitectura Técnica, Diseño de
Escenografía y Proyectos, Edificación y Obra Civil**: seis puestos entre las cuatro, todos
por concurso de méritos. **No tienen Anexo 2**, así que no hay temario que escribir y
quedan fuera del alcance por definición, no por decisión.

## El hallazgo que más alcance añade sin escribir una línea

**El temario general sirve a las 49 ocupaciones que tienen examen.** Comparado carácter a
carácter tras normalizar espacios, el bloque general es **idéntico en 47** de ellas —los
mismos ocho puntos, las mismas normas, las mismas fechas—. Las otras dos no traen un
temario distinto: traen **menos**. **Gestión Abogado/a** lleva cinco de los ocho —se deja
fuera la Ley 17/2006, la Ley 8/2009 y la Ley 13/2022— y **Prevención de Riesgos
Laborales** lleva siete —se deja fuera la Ley 31/1995, porque es su bloque específico
entero—. **Los dos son subconjuntos del nuestro**, de modo que `libro-general` vale tal
cual para las 49.

**Y una segunda coincidencia, esta vez del específico**: el temario específico de
**Información y Contenidos** es **idéntico carácter a carácter** en las cuatro
especialidades de idioma —**Francés, Inglés, Portugués y Ruso**—: los mismos 2.105
caracteres. Lo que cambia entre ellas es la prueba de idioma, no el temario. **Un volumen
ya escrito cubre cinco ocupaciones tipo.**

## Qué está hecho

| Volumen | Ocupación tipo | Puestos | Con examen | Unidades del específico | Escritas |
|---|---|---:|---:|---:|---:|
| `libro-informacion` | Información y Contenidos | 474 | 270 | 11 | **100 %** |
| `libro-realizacion` | Realización - Asistencia | 129 | 104 | 39 | **100 %** |
| `libro-gestion-administrativa` | Gestión Administrativa | 98 | 80 | 13 | **100 %** |
| `libro-gestion` | Gestión | 60 | 52 | 31 | **100 %** |
| `libro-produccion-asistencia` | Producción - Asistencia | 54 | 40 | 18 | **100 %** |
| `libro-produccion` | Producción | 35 | 31 | 17 | **100 %** |
| `libro-documentacion` | Documentación | 30 | 24 | 21 | **100 %** |
| `libro-informacion` | Información y Contenidos FRANCÉS | 2 | 2 | 11 | **100 %** |
| `libro-informacion` | Información y Contenidos INGLÉS | 2 | 2 | 11 | **100 %** |
| `libro-informacion` | Información y Contenidos PORTUGUÉS | 1 | 1 | 11 | **100 %** |
| `libro-informacion` | Información y Contenidos RUSO | 1 | 1 | 11 | **100 %** |

**Ocho volúmenes cubren once ocupaciones tipo**, 886 puestos y 607 de los que tienen examen.

## Qué falta, ordenado por puestos con examen

La columna **«reutilizable»** es una estimación propia, hecha **punto por punto** contra
los 120 temas escritos: cuántas unidades del Anexo 2 de esa ocupación están ya cubiertas
por material existente. **Reutilizable no es hecho**: significa que la materia está
investigada y verificada, y que el trabajo pendiente es adaptarla y componer el volumen
—banco de preguntas propio, portadas, esquemas, informes y maquetación—, que en las
ocupaciones ya cerradas fue aproximadamente la mitad del esfuerzo.

| Ocupación tipo | Puestos | Con examen | Unidades | Reutilizable | % |
|---|---:|---:|---:|---:|---:|
| Sonido | 102 | 93 | 43 | 8 | 19 % |
| Técnica de equipos y sistemas electrónicos | 97 | 89 | 21 | 2 | 10 % |
| Información Gráfica y Captación de Sonido | 81 | 73 | 26 | 21 | 81 % |
| Edición, montaje y procesos audiovisuales | 50 | 36 | 30 | 25 | 83 % |
| Técnica Informática | 27 | 25 | 27 | 6 | 22 % |
| Ing. Sup. Informática | 25 | 24 | 33 | 4 | 12 % |
| Montaje equipos audiovisuales | 24 | 24 | 21 | 15 | 71 % |
| Realización | 30 | 23 | 24 | 17 | 71 % |
| Luminotecnia | 17 | 17 | 23 | 8 | 35 % |
| Imagen Personal | 10 | 10 | 10 | 3 | 30 % |
| Ing. Sup. Telecomunicación | 13 | 9 | 29 | 3 | 10 % |
| Diseño Gráfico | 12 | 9 | 14 | 8 | 57 % |
| Ing. Téc. Telecomunicación | 10 | 9 | 24 | 2 | 8 % |
| Información y contenidos RADIO CLÁSICA | 11 | 8 | 16 | 2 | 12 % |
| Técnica de equipos instal. y sist. eléctricos | 8 | 8 | 17 | 2 | 12 % |
| Iluminación | 7 | 7 | 52 | 28 | 54 % |
| Ambientación Vestuario | 5 | 5 | 8 | 3 | 38 % |
| Mecánica de equipo e instalaciones | 4 | 4 | 18 | 1 | 6 % |
| Ambientación Musical | 3 | 3 | 29 | 1 | 3 % |
| Diseño decorados | 3 | 3 | 14 | 4 | 29 % |
| Prof. Coro Bajo | 3 | 3 | 9 | 0 | 0 % |
| Prof. Coro Tenor | 3 | 3 | 9 | 0 | 0 % |
| Ambientación decorados | 2 | 2 | 8 | 3 | 38 % |
| Gestión Abogado | 2 | 2 | 29 | 10 | 34 % |
| Ing. Téc. Industrial | 2 | 2 | 22 | 1 | 5 % |
| Medicina de empresa | 2 | 2 | 33 | 1 | 3 % |
| Prevención Riesgos Laborales | 2 | 2 | 37 | 7 | 19 % |
| Prof. Coro Mezzosoprano | 2 | 2 | 9 | 0 | 0 % |
| Prof. Orq. Viola | 2 | 2 | 11 | 0 | 0 % |
| Ing. Sup. Industrial | 3 | 1 | 23 | 1 | 4 % |
| Efectos especiales | 1 | 1 | 15 | 3 | 20 % |
| Información y Contenidos METEOROLOGÍA | 1 | 1 | 28 | 4 | 14 % |
| Prof. Coro Soprano | 1 | 1 | 9 | 0 | 0 % |
| Prof. Orq. Clarinete | 1 | 1 | 11 | 0 | 0 % |
| Prof. Orq. Fagot | 1 | 1 | 11 | 0 | 0 % |
| Prof. Orq. Oboe | 1 | 1 | 11 | 0 | 0 % |
| Prof. Orq. Percusión | 1 | 1 | 11 | 0 | 0 % |
| Prof. Orq. Violín | 1 | 1 | 11 | 0 | 0 % |

**En conjunto**: de las **970 unidades de específico** que suma el catálogo entero,
**387 están escritas o son reutilizables** —el **40 %**—. Medido como
importa, **ponderando por puestos con examen**, la cobertura del específico es del
**71 %**: lo escrito no está repartido al azar, está en las ocupaciones grandes.

## Las cuatro que conviene escribir después, y por qué

**1 · Información Gráfica y Captación de Imagen y Sonido — 81 puestos, 73 con examen,
81 % reutilizable.** Es la mejor relación de todo el catálogo: la tercera ocupación más
grande de las que faltan y la que menos trabajo nuevo pide. Su Anexo 2 son 26 subpuntos y
veintiuno están cubiertos por Realización (Asistencia) y Producción —cámara, objetivos,
soportes, sensores, sonido, iluminación, lenguaje audiovisual, raccord, envíos y realidad
aumentada—. **Lo nuevo de verdad son cuatro cosas**: la cámara fotográfica, la operación
de cámara como oficio, los ajustes en producción ligera y los filtros de cámara.

**2 · Edición, montaje y procesos audiovisuales — 50 y 36, 83 % reutilizable.** Sus 30
subpuntos se solapan casi enteros con el bloque de postproducción de Realización
(Asistencia) y con el tratamiento de imagen y sonido de Producción: códecs, soportes,
ingesta, EDL, edición offline y online, código de tiempo, incrustaciones, etalonaje,
raccord y teoría del montaje. **Lo nuevo es la electrónica y la informática básicas** de
su bloque 1.

**3 · Realización Televisión — 30 y 23, 71 % reutilizable.** Es la hermana mayor de
Realización (Asistencia) y comparte con ella los diez subpuntos del bloque de realización
—lenguaje, cámara, mezclador, iluminación, sonido, directos, puesta en escena,
postproducción, producción online y propiedad intelectual—. **Lo nuevo es un bloque
entero y bien delimitado**: los siete subpuntos de **cultura audiovisual** —música,
televisión, artes escénicas, literatura, artes plásticas, fotografía y cine—.

**4 · Montaje de Equipos Audiovisuales — 24 y 24, 71 % reutilizable.** Todos sus puestos
tienen examen, cosa que no pasa en casi ninguna otra. Cámaras, soportes, pedestales,
grúas, travellings, cabeza caliente, micrófonos y enlaces están escritos; **lo nuevo es
el oficio de instalar**: planos de emplazamiento, líneas de audio y vídeo, conectores y
baja tensión.

**Las cuatro juntas suman 185 puestos y 156 con examen**, y **ninguna necesita una fuente
nueva de primer nivel**: su materia es la misma que ya se ha verificado.

## Las dos grandes que no se eligen, y por qué

**Sonido — 102 puestos, 93 con examen, y sólo el 19 % reutilizable.** Es la segunda
ocupación más grande que queda y la más cara de escribir: sus 43 subpuntos son
electricidad, electrónica, acústica arquitectónica, sonorización, radiofrecuencia,
medición de sonoridad, audio multicanal, audio sobre IP y protocolos digitales. **Y su
punto 15.1 pide por su nombre la norma AES10 del MADI**, que este proyecto ya se encontró
**detrás de un muro de pago** al escribir el tema 10 de Producción (Asistencia). Un
volumen entero apoyado en fuentes de ese tipo es el más difícil de verificar del catálogo.

**Técnica de Equipos y Sistemas Electrónicos — 97 y 89, 10 % reutilizable.** Veintiún
puntos de electricidad, componentes, electrónica de potencia, amplificadores
operacionales, digital, microprocesadores y mantenimiento. **No hay BOE detrás de casi
nada** y no reutiliza más que la señal SDI, la señal IP y el tema de prevención. Es el
mejor candidato del grupo «no reutiliza nada» si el criterio pasa a ser sólo el número de
plazas.

## Cómo se han contado las unidades

**Los anexos no están hechos con el mismo patrón, y contar «temas» sin decir qué es un
tema daría una cifra falsa.** Unos numeran de 1 a N y cada número es un tema —Producción,
17 puntos; Gestión, 31—. Otros agrupan en bloques con subpuntos, y ahí **el bloque no es
la unidad de estudio: lo es el subpunto** —Realización (Asistencia) tiene 8 bloques y 39
subpuntos, y este proyecto los convirtió en 21 temas—.

**La regla aplicada**: se cuenta el **subpunto** cuando el anexo tiene más subpuntos que
bloques, y el **punto de primer nivel** cuando no. Con esa regla, las cifras de las siete
ocupaciones ya escritas coinciden con los temas que tienen sus volúmenes, que es la
comprobación de que la regla mide lo que dice medir.

**Y un aviso sobre los números de puestos**: se toman de la frase «Del total de los N
puestos… convocados» de cada bases, y donde esa frase no existe —las ocupaciones de una o
dos plazas— de la tabla del Anexo 1. **Dos bases no cuadran consigo mismas**:
Documentación dice 30 puestos y su desglose suma 37; Información y Contenidos Radio
Clásica dice 11 y su desglose suma 12. **Se recoge el total que la propia base declara**,
y queda anotado que el desglose no cuadra.

## Fuentes

- **Las 53 bases específicas del turno libre de la convocatoria 1/2022**, descargadas el
  3 de septiembre de 2026 de la sección sindical de CCOO en RTVE
  (<https://www.ccoortve.es/bases-especificas/>), que publica el catálogo entero ocupación
  por ocupación. **Se guardan los enunciados de sus Anexos 2**, no los PDF: son 53
  documentos de una decena de páginas y lo que hace falta de ellos es el programa. Las
  bases completas de las siete ocupaciones que se preparan están en
  `../convocatoria/bases/`.
- **El propio repositorio**, para el recuento de lo escrito: **en la fecha de este informe**, 120
  ficheros de tema, 120 esquemas y ocho volúmenes compuestos. **Al cerrarse las cuatro ocupaciones
  que recomendaba**: 173 temas, 173 esquemas y doce volúmenes.

---

## Anotación posterior · las cuatro se escribieron el mismo día

**Las cuatro ocupaciones que este informe recomendaba están terminadas**, y **conviene dejar escrito
en qué acertó la estimación y en qué no**, porque es lo que permitirá afinar la próxima.

| Ocupación | Temas escritos | Preguntas del específico | Reutilización estimada |
|---|---:|---:|---|
| **Información Gráfica y Captación de Imagen y Sonido** | 11 | 94 | **81 %** |
| **Edición, Montaje y Procesos Audiovisuales** | 10 | 86 | **83 %** |
| **Realización Televisión** | 22 | **229** | **71 %** |
| **Montaje de Equipos Audiovisuales** | 10 | 75 | **71 %** |

**Dónde acertó la estimación**: **la reutilización se sostuvo en las cuatro**, y **el bloque nuevo de
Realización Televisión fue exactamente el que este informe anunció**: los siete subpuntos de cultura
audiovisual, que se llevaron **cuarenta preguntas** entre los dos llamamientos.

**Dónde se quedó corta, y es el dato que hay que llevarse**: **este informe midió las ocupaciones por
subpuntos de anexo y por puestos convocados, y no por preguntas de examen.** **Realización Televisión
aparecía aquí como la tercera de las cuatro**, con 30 puestos y 23 con examen. **Ha resultado ser la
que más trabajo pedía con diferencia**: **229 preguntas del bloque específico —el banco más grande del
proyecto, por delante de las 209 de Realización (Asistencia)—, veintidós temas y el volumen más largo,
con 354 páginas.** **Sus dos llamamientos completos con sus dos plantillas la ponen a otra escala que
las otras tres**, que se sostienen sobre un solo cuadernillo cada una.

**La regla que queda**: **el tamaño de trabajo de una ocupación lo fija el número de cuadernillos
disponibles, no el número de puestos convocados.** **Dos llamamientos con dos plantillas completas
duplican el banco**, y **el banco es lo que hay que contestar tema a tema.**

**Y un hallazgo de fuente que este informe no podía prever**: **las unidades fotométricas están en el
Boletín Oficial del Estado**, porque son unidades legales de medida. **Tres preguntas de Realización
Televisión que iban a declararse como oficio se contestan con el cuadro de un real decreto delante.**
**La pregunta que hay que hacerse antes de dar por oficio una materia técnica es si sus magnitudes
tienen unidad legal.**
