# Cobertura · Enfermería de Empresa, los veinticinco temas del específico

**Siglas de este informe**: la Corporación de Radio y Televisión Española (**RTVE**); el Instituto
Nacional de Seguridad y Salud en el Trabajo (**INSST**), que hasta 2019 se llamó Instituto Nacional de
Seguridad e Higiene en el Trabajo (**INSHT**); sus notas técnicas de prevención (**NTP**); la
prevención de riesgos laborales (**PRL**); y la Ley de Prevención de Riesgos Laborales (**LPRL**), que
es la Ley 31/1995.

**Es la tercera ocupación del proyecto sin examen publicado**, después de Ingeniería Técnica ·
Industrial y de Técnica de Equipos, Instalaciones y Sistemas Eléctricos. **La prueba del apartado 7 del
manual —contestar preguntas reales con el tema delante— no se puede hacer aquí**, y este informe no
finge que sí. **Lo que se comprueba en su lugar es la cobertura del programa**: que cada punto del
anexo tenga su tema, que la fuente que el enunciado nombra esté volcada y citada, y que lo que no tiene
fuente se declare como oficio.

**No haber examen no es un hueco del proyecto: es un dato de la convocatoria**, y va escrito en la
portada del volumen en vez de disimulado. **Este volumen es además el primero del proyecto que se
imprime sin apéndice de respuestas**, y para eso hubo que enseñarle a `herramientas/libro.py` que un
bloque puede no tener examen.

## De qué programa está escrito este temario

**NO del Anexo 2 de la convocatoria 1/2022**, porque **esa convocatoria no tuvo esta ocupación tipo.**
**Está escrito del Anexo 1 de las Bases de la Convocatoria de Banco de Datos de RTVE**, que es **el
único programa oficial publicado para Enfermería de Empresa**. El documento está en el repositorio, en
`convocatoria/banco-datos/BasesBBDD_Enfermeria-Empresa.txt`, y de ahí sale literalmente el enunciado
que encabeza cada tema.

**La advertencia va escrita en el tema 1 y se remite a ella desde los otros veinticuatro**, y **la
portada del volumen la repite**: quien estudie esto tiene que saber que su programa no viene de donde
vienen los demás volúmenes del proyecto.

## Un tema por punto: ni uniones ni desdobles

**El anexo numera veinticinco puntos y este volumen tiene veinticinco temas, en correspondencia uno a
uno.** No es la regla general del proyecto —en otras ocupaciones un punto se desdobla o dos se unen—,
y **aquí se ha decidido así porque los veinticinco puntos tienen tamaños comparables y ninguno se
solapa con otro.**

**Esa decisión costó una corrección.** Durante la escritura del volumen convivieron dos numeraciones
—una que unía puntos y otra que no—, y **once remisiones internas quedaron apuntando al tema
equivocado.** Se corrigieron todas y **el episodio está anotado en `PENDIENTES.md`**, con la lección:
**ninguna de las cinco lentes comprueba a dónde apunta una remisión.** Al cerrar el volumen se escribió
`herramientas/remisiones.py` para eso, y **al pasarla aparecieron tres remisiones muertas más** que la
revisión manual no había visto.

## El reparto de los veinticinco puntos

| Punto | Tema | Fuente principal | Palabras |
|---:|---|---|---:|
| 1 | Marco normativo de los lugares de trabajo, indicadores y condiciones de trabajo | Real Decreto 486/1997 | 3.364 |
| 2 | Las cuatro disciplinas preventivas y la señalización | Real Decreto 485/1997 y Ley 31/1995 | 4.464 |
| 3 | El estrés, el desgaste profesional y el acoso | II Plan de Igualdad de RTVE | 3.122 |
| 4 | La enfermera del trabajo, la autonomía del paciente y la protección de datos | Reales Decretos 450/2005, Ley 41/2002 y Ley Orgánica 3/2018 | 3.623 |
| 5 | La vigilancia de la salud | Ley 31/1995 y Real Decreto 39/1997 | 4.054 |
| 6 | Accidente de trabajo y enfermedad profesional | Ley General de la Seguridad Social y Real Decreto 1299/2006 | 4.486 |
| 7 | La promoción de la salud en el trabajo | Ley 33/2011, Ley 31/1995 y Real Decreto 39/1997 | 5.747 |
| 8 | La espirometría en los exámenes de salud laboral | **NTP** 218, que el propio enunciado nombra | 7.272 |
| 9 | Patología de origen laboral | Cuadro de enfermedades profesionales y cuatro reales decretos | 6.148 |
| 10 | Técnicas y procedimientos en enfermería del trabajo | **NTP** 586 y 1.191, y Real Decreto 374/2001 | 6.196 |
| 11 | Inmunización en el ámbito laboral | Real Decreto 664/1997 y tres documentos del Ministerio de Sanidad | 5.634 |
| 12 | Demografía e indicadores de salud | Tres documentos del Ministerio de Sanidad | 5.187 |
| 13 | Estadística descriptiva e inferencial | **NTP** 1.211 | 5.169 |
| 14 | Epidemiología | Material docente del Instituto | 5.384 |
| 15 | Exposición profesional a agentes físicos | Cuatro reales decretos | 4.674 |
| 16 | Exposición profesional a agentes biológicos | Real Decreto 664/1997 y **NTP** 447 | 5.709 |
| 17 | Exposición profesional a agentes químicos | Real Decreto 374/2001 | 4.608 |
| 18 | Exposición profesional a agentes cancerígenos | Real Decreto 665/1997 | 3.950 |
| 19 | Trastornos musculoesqueléticos | Real Decreto 487/1997 y material del Instituto | 4.035 |
| 20 | Equipos de protección individual | Real Decreto 773/1997 | 3.973 |
| 21 | Uso de pantallas de visualización de datos | Real Decreto 488/1997 y Guía Técnica | 3.775 |
| 22 | Protección de la maternidad en el trabajo | Ley 31/1995, Real Decreto 39/1997 y Ley General de la Seguridad Social | 4.117 |
| 23 | Esfuerzos sostenidos de la voz | Cuadro de enfermedades profesionales y **NTP** 1.149 y 1.226 | 3.917 |
| 24 | Las drogodependencias en el medio laboral | Convenio colectivo de RTVE y ficha del Instituto | 3.393 |
| 25 | Primeros auxilios | Nueve **NTP** de la serie, una guía y cinco normas | 13.972 |

**Total: 125.973 palabras**, con una media de **5.039 por tema**.

**El tema 25 es el más largo del proyecto entero, y con distancia.** No es un desbordamiento: **su
enunciado pide veinte materias clínicas distintas**, de la reanimación a las picaduras, y cada una
lleva su fuente. **Se ha preferido un tema largo a dos temas que partirían un punto que el programa
numera como uno.**

## Qué se ha volcado para escribirlo

**Veintitrés normas del boletín**, todas leídas del texto consolidado en su redacción vigente al 21 de
diciembre de 2022, salvo una: **el Real Decreto 365/2009, sobre desfibriladores, que no está en la base
de legislación consolidada del BOE** y se ha leído de la publicación original del diario. Eso se declara
en el tema 25 y en el almacén de fuentes.

**Y un almacén de documentación técnica que este volumen ha creado casi entero**: reúne **dieciséis
notas técnicas de prevención**, **un material docente del Instituto**, **una guía de socorrismo
laboral**, **una ficha de campaña**, **seis documentos del Ministerio de Sanidad** y **el texto del
Real Decreto 365/2009 leído del diario**. Su fichero de procedencia documenta de dónde sale cada uno,
con la orden que lo baja, y advierte de las trampas de descarga del portal del Instituto: **la ruta
corta sirve para unas notas y no para otras**, y **cuando falla hay que pedir el enlace largo con
agente de navegador y con `Referer`**, porque si no el portal devuelve una página de error que `curl`
guarda con extensión de PDF sin protestar.

## Lo que este volumen declara que NO da

**Cada tema lleva su tabla de lagunas**, y conviene reunir aquí las que afectan a rúbricas expresas del
enunciado, porque son las que un opositor debe saber que tiene que buscar en otro sitio:

| Tema | Rúbrica del enunciado que queda abierta | Por qué |
|---:|---|---|
| 8 | **Contraindicaciones de la espirometría** y **mantenimiento del espirómetro** | La nota que el propio enunciado nombra no las trata |
| 11 | **Tipos de inmunidad, clases de vacunas, cadena de frío y técnica de administración** | Son vacunología; ningún manual consultado |
| 12 | **Indicadores de fecundidad** | Están en las estadísticas del Instituto Nacional de Estadística, no consultadas |
| 13 | **Las fórmulas de la estadística descriptiva** | El tema define en palabras; no se ha consultado ningún manual |
| 19 | **Ángulos y tiempos que definen una postura forzada** | Están en normas técnicas no consultadas. Laguna principal de ese tema |
| 21 | **Periodicidad y duración de las pausas** | La norma las remite al convenio colectivo |
| 24 | **Indicadores de consumo y cuestionarios de cribado** | Ninguna fuente consultada los publica. Laguna principal de ese tema |
| 25 | **Picaduras por animales concretos** y **lesiones oculares traumáticas** | Las fuentes del Instituto tratan la picadura sólo como intoxicación parenteral |

**Ninguna de estas lagunas se rellena con oficio plausible**, que es la tentación del apartado 7 del
manual. **Se declaran, se dice dónde está lo que falta, y se sigue.**

## La comprobación de las remisiones internas

**Al cerrar el volumen se pasó `herramientas/remisiones.py` sobre los veinticinco temas**: imprime cada
remisión con el título del tema al que apunta. **409 remisiones listadas**, y **tres apuntaban mal**:

1. **La tabla de contaminantes del tema 2** mandaba los agentes físicos, químicos y biológicos a los
   temas 14, 16 y 15, cuando son el 15, el 17 y el 16.
2. **El tema 12** mandaba el consumo de alcohol y el de otras drogas al tema 23, que es la voz, en vez
   de al 24.
3. **El tema 4** describía el área preventiva de la enfermería del trabajo como «los temas 1, 2 y 14 a
   19», y el 14 es epidemiología.

**Las tres se corrigieron.** **Ninguna de las cinco lentes las habría visto**, y ése es el motivo de que
la herramienta exista.
