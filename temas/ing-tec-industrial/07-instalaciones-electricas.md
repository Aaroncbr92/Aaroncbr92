# Tema 7 del específico de Ingeniería Técnica · Industrial · Instalaciones eléctricas

Las siglas de este tema, presentadas de entrada: el reglamento electrotécnico para baja tensión
(**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT 01** a **ITC-BT 52**); el reglamento
de instalaciones eléctricas de alta tensión (**RAT**) y sus instrucciones (**ITC-RAT 01** a
**ITC-RAT 23**); el reglamento de líneas eléctricas de alta tensión (**LAT**) y las suyas
(**ITC-LAT 01** a **ITC-LAT 09**); el voltio (**V**) y el kilovoltio (**kV**); el hercio (**Hz**); la
tensión nominal (**Un**); la Unión Europea (**UE**) y el Espacio Económico Europeo (**EEE**); y la
Asociación Española de Normalización (**UNE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Industrial, punto 7):
> «Instalaciones eléctricas. Cálculo, diseño, mantenimiento y normativa.
> 7.1. Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para
> baja tensión y sus Instrucciones técnicas complementarias ITC‐BT desde la 1 a la 52 (BOE núm. 224, de
> 18/09/2002. Texto consolidado: Última actualización publicada el 28/04/2021).
> 7.2. Real Decreto 337/2014, de 9 de mayo, por el que se aprueban el Reglamento sobre condiciones
> técnicas y garantías de seguridad en instalaciones eléctricas de alta tensión y sus Instrucciones
> Técnicas Complementarias ITC‐RAT 01 a 23 (BOE» núm. 139, de 09/06/2014. Texto consolidado: última
> actualización publicada el 11/10/2021).
> 7.3. Real Decreto 223/2008, de 15 de febrero, por el que se aprueba el reglamento sobre condiciones
> técnicas y garantías de seguridad en líneas eléctricas de alta tensión y sus instrucciones
> complementarias ITC‐LAT 01a 09 (BOE núm. 68, de 19/03/2008. Texto consolidado: última actualización
> publicada el 11/10/2021).»

**Tres reglamentos y ochenta y cuatro instrucciones técnicas.** **Es el punto más extenso del anexo**,
y **el que más peligro tiene de estudiarse mal**, porque **la tentación es leerse las ochenta y cuatro
instrucciones.**

**La estructura que este tema propone y que ordena el estudio**: **los tres reglamentos comparten el
mismo esqueleto —objeto, clasificación por tensión, documentación, ejecución, inspecciones,
cumplimiento y excepciones—, y lo que cambia es dónde ponen la frontera.** **Se estudian los tres a
la vez, comparándolos**; **por separado se estudian tres veces lo mismo.**

**Y el reparto entre ellos, en una línea**: **por debajo de mil voltios, el primero; por encima, el
segundo si es una instalación y el tercero si es una línea.**

<!-- indice -->

## Índice

- [1. La frontera entre los tres](#1-la-frontera-entre-los-tres)
- [2. El objeto de cada uno](#2-el-objeto-de-cada-uno)
- [3. La clasificación por tensión](#3-la-clasificación-por-tensión)
- [4. A qué instalaciones se aplican](#4-a-qué-instalaciones-se-aplican)
- [5. Los tipos de suministro](#5-los-tipos-de-suministro)
- [6. Ejecución y puesta en servicio](#6-ejecución-y-puesta-en-servicio)
- [7. Inspecciones, cumplimiento y excepciones](#7-inspecciones-cumplimiento-y-excepciones)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. La frontera entre los tres

| Reglamento | Qué regula | Umbral |
|---|---|---|
| **Baja tensión** | **Instalaciones que distribuyen energía, las generadoras para consumo propio y las receptoras** | **Alterna ≤ 1.000 V** y **continua ≤ 1.500 V** |
| **Instalaciones de alta tensión** | **Instalaciones**, no líneas | **Alterna trifásica de frecuencia < 100 Hz** y **tensión nominal eficaz entre fases > 1 kV** |
| **Líneas de alta tensión** | **Líneas** | **Alterna trifásica a 50 Hz** y **tensión nominal eficaz entre fases > 1 kV** |

**Y el artículo 2.1 del reglamento de instalaciones de alta tensión cierra el reparto por su lado**:
**no se aplica a líneas de alta tensión ni a lo que tenga reglamentación específica**, **salvo las
centrales nucleares, que se someten a este reglamento Y ADEMÁS a su normativa específica.**

**La excepción de las nucleares es la que se pregunta**, porque **es la única que suma en vez de
excluir.**

**Lo que el reglamento de instalaciones de alta tensión SÍ incluye y sorprende, del mismo artículo
2.1:**

| Elemento | Por qué entra |
|---|---|
| **Circuitos auxiliares de protección, medida, control, mando y señalización** | **Independientemente de su tensión de alimentación** |
| **Cuadros de distribución de BAJA tensión** | **Cuando puedan ser objeto de requisitos adicionales por estar dentro de una instalación de alta tensión** |

**Ésa es la trampa competencial del punto**: **un cuadro de baja tensión dentro de un centro de
transformación no se rige sólo por el reglamento de baja.** **El emplazamiento arrastra.**

**Y las tres exclusiones que hay que saber, una por reglamento:**

| Reglamento | Qué excluye |
|---|---|
| **Baja tensión** | **Minas, tracción, automóviles, navíos, aeronaves, sistemas de comunicación, usos militares** y lo sujeto a reglamentación específica |
| **Instalaciones de alta tensión** | **Líneas de alta tensión** y lo que tenga reglamentación específica, **salvo nucleares** |
| **Líneas de alta tensión** | **El tendido de TRACCIÓN propiamente dicho —línea de contacto— de ferrocarriles y otros medios de transporte electrificados** |

**Y los dos de alta tensión añaden una cláusula que el de baja no tiene y que un ingeniero debe tener
presente**: **sus prescripciones se aplican SIN PERJUICIO de la normativa de prevención de riesgos
laborales, y en particular del Real Decreto 614/2001 sobre riesgo eléctrico.** **La seguridad de la
instalación y la seguridad del trabajador son dos cosas y las dos obligan.**

## 2. El objeto de cada uno

**Artículo 1** del reglamento electrotécnico para baja tensión, entero:

> «**El presente Reglamento tiene por objeto establecer las condiciones técnicas y garantías que deben
> reunir las instalaciones eléctricas conectadas a una fuente de suministro en los límites de baja
> tensión, con la finalidad de:
> a) Preservar la seguridad de las personas y los bienes.
> b) Asegurar el normal funcionamiento de dichas instalaciones y prevenir las perturbaciones en otras
> instalaciones y servicios.
> c) Contribuir a la fiabilidad técnica y a la eficiencia económica de las instalaciones.**»
>
> — Real Decreto 842/2002, artículo 1 (`BOE-A-2002-18099`), redacción vigente el 21 de diciembre de
> 2022.

---

**Tres finalidades, y las dos últimas son propias de la electricidad**: **ninguna otra norma del anexo
se preocupa de que la instalación no PERTURBE a las demás, ni de su eficiencia económica.** **La razón
es que la red eléctrica es compartida**: **lo que un abonado hace mal se nota en la instalación del
vecino.**

**Los cuatro objetivos que comparten los dos reglamentos de alta tensión**, con la única diferencia
que hay entre ellos:

| Objetivo | Instalaciones de alta tensión | Líneas de alta tensión |
|---|---|---|
| **a)** | **Proteger las personas y la integridad y funcionalidad de los bienes** | **Igual** |
| **b)** | **Conseguir la necesaria CALIDAD en los suministros y promover la EFICIENCIA ENERGÉTICA** | **Conseguir la necesaria REGULARIDAD en los suministros** |
| **c)** | **Establecer la normalización precisa para reducir la extensa tipificación** en la fabricación de material | **Igual** |
| **d)** | **Facilitar desde el proyecto la adaptación a futuros aumentos de carga racionalmente previsibles** | **Igual** |

**La única diferencia está en la letra b)**, y **es la marca de los seis años que separan las dos
normas**: **la de 2008 habla de regularidad y la de 2014 añade calidad y eficiencia energética.**
**Es el vocabulario de su década, y conviene notarlo porque el examen podría cruzar las dos letras.**

**Qué es una instalación eléctrica, del artículo 3 del reglamento de baja tensión**: **todo conjunto de
aparatos y de circuitos asociados en previsión de un fin particular: producción, conversión,
transformación, transmisión, distribución o utilización de la energía eléctrica.** **Seis verbos**, y
**el reglamento de baja se aplica sólo a tres de esos fines** —distribución, generación para consumo
propio y recepción—.

## 3. La clasificación por tensión

**Ésta es la tabla que hay que saber sin dudar, y son DOS escaleras distintas** que se encuentran en
1 kV.

**Baja tensión, del artículo 4.1**, con sus tres escalones:

| Clase | Corriente alterna, valor eficaz | Corriente continua, valor medio aritmético |
|---|---|---|
| **Muy baja tensión** | **Un ≤ 50 V** | **Un ≤ 75 V** |
| **Tensión usual** | **50 < Un ≤ 500 V** | **75 < Un ≤ 750 V** |
| **Tensión especial** | **500 < Un ≤ 1.000 V** | **750 < Un ≤ 1.500 V** |

**La regla que ahorra memorizar la columna de continua**: **es siempre una vez y media la de
alterna.** **50 y 75, 500 y 750, 1.000 y 1.500.**

**Y el régimen singular de la muy baja tensión, del artículo 2.6**: **a las instalaciones o equipos de
muy baja tensión NO se les aplican las prescripciones generales, sino únicamente las específicas de
sus instrucciones técnicas** —el reglamento pone de ejemplo **las redes informáticas**—, **siempre que
su fuente de energía sea autónoma, no se alimenten de redes destinadas a otros suministros o sean
absolutamente independientes de las redes de baja tensión.**

**Ésa es la razón por la que una red de datos no lleva boletín eléctrico**, y **conviene saber la
condición: la independencia de la fuente.**

**Las tensiones nominales usuales de distribución, del artículo 4.2**, y la frecuencia:

| Red | Tensión |
|---|---|
| **Trifásica de tres conductores** | **230 V entre fases** |
| **Trifásica de cuatro conductores** | **230 V entre fase y neutro, y 400 V entre fases** |
| **Frecuencia de la red** | **50 Hz** — artículo 4.4 |

**La relación entre 230 y 400 es la raíz de tres**, y **eso explica por qué las dos cifras van juntas
en la misma fila.**

**Alta tensión: las cuatro categorías, IDÉNTICAS en los dos reglamentos**, del artículo 3 de cada uno:

| Categoría | Tensión nominal |
|---|---|
| **Especial** | **Igual o superior a 220 kV**, y las de tensión inferior que formen parte de la red de transporte |
| **Primera** | **Inferior a 220 kV y superior a 66 kV** |
| **Segunda** | **Igual o inferior a 66 kV y superior a 30 kV** |
| **Tercera** | **Igual o inferior a 30 kV y superior a 1 kV** |

**Las tres cifras que separan las categorías son 220, 66 y 30**, y **conviene notar que la escalera
está escrita al revés de como se lee**: **la categoría especial es la más alta y la tercera es la más
baja.** **Numeración descendente en tensión ascendente.**

**Y las dos reglas que los dos reglamentos repiten palabra por palabra:**

1. **Si hay circuitos o elementos con distintas tensiones, el conjunto se considera, a efectos
   administrativos, referido al de MAYOR tensión nominal.**
2. **Por encima de 400 kV, la Administración competente establece la tensión que deba autorizarse.**

**Lo único que cambia entre las dos normas en el artículo 3 es la remisión**: **el de instalaciones
remite a la Ley 24/2013 del Sector Eléctrico** y **el de líneas, al artículo 5 del Real Decreto
1955/2000.** **Es la misma diferencia de fecha del epígrafe anterior.**

## 4. A qué instalaciones se aplican

**Los tres reglamentos tienen el mismo esquema de tres o cuatro letras, y las diferencias son las que
un examen buscaría:**

| Caso | Baja tensión | Instalaciones de alta | Líneas de alta |
|---|---|---|---|
| **Nuevas, modificaciones y ampliaciones** | **Sí** | **Sí** | **Sí** |
| **Existentes que se modifican** | **Modificaciones, reparaciones y ampliaciones, sean o no de importancia, sólo en la parte afectada**, y garantizando la seguridad del conjunto | **Sólo la parte modificada** | **Sólo modificaciones CON VARIACIÓN DEL TRAZADO original, y sólo el tramo modificado** |
| **Existentes, régimen de inspecciones** | **Sí**, con los criterios técnicos de la reglamentación con que se aprobaron | **Sí**, sobre periodicidad y agentes | **Sí**, con un matiz propio para líneas aéreas de conductores desnudos |
| **Existentes con riesgo grave** | **Sí**, a juicio de la comunidad autónoma | **Sí**, salvo que el riesgo pueda subsanarse aplicando la reglamentación original | **No lo prevé** |

**El de baja tensión define qué es una modificación o reparación DE IMPORTANCIA, y su cifra es de las
más preguntables del punto:**

| Criterio | Umbral |
|---|---|
| **Por potencia** | **Las que afectan a más del 50 por 100 de la potencia instalada** |
| **Por alcance** | **Las que afectan a líneas completas de procesos productivos con nuevos circuitos y cuadros, **aun con reducción** de potencia** |

**El segundo criterio es el que se olvida**: **una reforma puede ser de importancia aunque BAJE la
potencia.** **Lo que la define entonces no es cuánto consume, sino cuánto cambia.**

**Y para qué sirve esa calificación**: **para determinar la documentación exigible y la obligatoriedad
de inspección inicial.** **No es una etiqueta: decide papeles.**

## 5. Los tipos de suministro

**El artículo 10 del reglamento de baja tensión es el que un ingeniero de una casa que emite tiene que
saber de memoria**, porque **es el que gobierna la continuidad del servicio.**

| Suministro | Qué es |
|---|---|
| **Normal** | **El efectuado a cada abonado por una sola empresa distribuidora, por la totalidad de la potencia contratada y con un solo punto de entrega** |
| **Complementario o de seguridad** | **El que, a efectos de seguridad y continuidad, complementa a un suministro normal** |

**Cómo puede realizarse el complementario, y es más flexible de lo que parece**: **por dos empresas
diferentes**, **por la misma empresa cuando haya medios de transporte y distribución independientes**,
o **por el usuario con medios de producción propios.** **Y el reglamento admite expresamente que
parta del MISMO transformador**, siempre que **disponga de línea de distribución independiente desde
su mismo origen en baja tensión.**

**Los tres tipos de complementario, con sus porcentajes**, que es la tabla que hay que memorizar:

| Tipo | Potencia mínima respecto a la total contratada |
|---|---|
| **De socorro** | **15 por 100** |
| **De reserva** | **25 por 100** |
| **Duplicado** | **Más del 50 por 100** |

**Y lo que cada uno persigue, que es lo que hace las cifras memorizables**: **el de socorro mantiene lo
imprescindible para salir del paso; el de reserva mantiene «un servicio restringido de los elementos
de funcionamiento indispensables»; y el duplicado mantiene más de la mitad de la casa en marcha.**

**La obligación técnica que los acompaña, del apartado 2**: **las instalaciones previstas para recibir
suministro complementario deben estar dotadas de los dispositivos necesarios para IMPEDIR EL
ACOPLAMIENTO entre ambos suministros**, salvo lo que digan las instrucciones técnicas. **Y si no hay
acuerdo con la suministradora sobre esos dispositivos, la comunidad autónoma resuelve en un plazo
máximo de 15 DÍAS HÁBILES.**

**El mismo plazo de quince días hábiles aparece en el apartado 4**, para cuando **la suministradora se
niegue a facilitar el complementario o no haya acuerdo sobre las condiciones técnico-económicas.**

**Y la facultad del apartado 3, que es la que afecta a un centro de emisión**: **las comunidades
autónomas pueden fijar, caso por caso, qué establecimientos industriales o de cualquier otra actividad
han de disponer de socorro, reserva o duplicado**, por sus características y circunstancias
singulares. **Un centro emisor o una continuidad de televisión son exactamente el supuesto que ese
apartado contempla.**

## 6. Ejecución y puesta en servicio

**El artículo 18 del reglamento de baja tensión da el procedimiento en cinco letras**, y **es el mismo
esqueleto que el artículo 5 del reglamento de gas del tema 5:**

| Letra | Qué exige |
|---|---|
| **a)** | **Documentación técnica previa a la ejecución**: **proyecto o memoria técnica, según determine la instrucción correspondiente** |
| **b)** | **Verificación por el INSTALADOR, con supervisión del director de obra en su caso** |
| **c)** | **Inspección inicial por un organismo de control**, cuando la instrucción lo determine |
| **d)** | **Certificado de instalación** de la empresa instaladora, que identifique y justifique las variaciones respecto a la documentación |
| **e)** | **Depósito ante la comunidad autónoma para registrar la instalación** |

**Y la consecuencia del apartado 3, que es la que da fuerza a todo lo anterior**: **la empresa
suministradora NO puede conectar la instalación receptora a la red si no se le entrega la copia del
certificado debidamente diligenciado.** **El certificado no es un trámite: es la llave del
suministro.**

**Las dos válvulas de escape que el reglamento prevé, y que un ingeniero de obra usa:**

| Situación | Qué permite |
|---|---|
| **Necesidad objetiva de suministro antes de culminar la tramitación** —apartado 4— | **La comunidad autónoma puede autorizar por RESOLUCIÓN MOTIVADA un suministro PROVISIONAL** para atender estrictamente esas necesidades, con garantías de seguridad |
| **Instalaciones temporales** —apartado 5— | **Tramitación CONJUNTA de las instalaciones parciales**, y **sustitución de la documentación por una declaración** en instalaciones repetitivas, diligenciada la primera vez |

**El apartado 5 nombra expresamente congresos y exposiciones con distintos estands, ferias ambulantes,
festejos y verbenas**, y **es el régimen bajo el que se monta la electricidad de un acontecimiento**:
**el caso más propio de una unidad móvil y de un despliegue de exteriores.**

**La información a los usuarios, del artículo 19**, con dos documentos que hay que saber nombrar:

| Documento | Qué es |
|---|---|
| **Esquema UNIFILAR** de la instalación | **Con las características técnicas fundamentales de los equipos y materiales** |
| **Croquis de su trazado** | **Por dónde va** |

**Los dos son anexo al certificado de instalación**, y **cualquier modificación o ampliación exige
completarlos.** **Es la misma exigencia del croquis del reglamento de gas del tema 5**, aquí con el
unifilar añadido.

**Y el deber del titular, del artículo 20, que se enuncia por lo que PROHÍBE**: **mantener las
instalaciones en buen estado, utilizarlas conforme a sus características y **abstenerse de intervenir en ellas
para modificarlas**.** **Si hacen falta modificaciones, las hace una empresa instaladora.**

## 7. Inspecciones, cumplimiento y excepciones

**El artículo 21 del reglamento de baja tensión no fija ni qué se inspecciona ni cada cuánto**:
**remite a la instrucción técnica los cuatro extremos**, y **eso hay que saberlo decir así:**

1. **Qué instalaciones y qué modificaciones deben tener INSPECCIÓN INICIAL antes de la puesta en
   servicio.**
2. **Qué instalaciones deben tener INSPECCIÓN PERIÓDICA.**
3. **Los criterios de valoración y las medidas a adoptar como resultado.**
4. **Los PLAZOS de las periódicas.**

**Y quién las hace**: **un organismo de control autorizado en este campo reglamentario**, sin perjuicio
de la facultad inspectora de la propia Administración por el artículo 14 de la Ley de Industria.

**Las dos vías de cumplimiento del artículo 23, con la condición propia de la electricidad:**

| Vía | Qué exige |
|---|---|
| **Aplicación directa de las instrucciones técnicas** | **Nada más** |
| **Técnicas de seguridad equivalentes** | **Nivel de seguridad equiparable Y SIN OCASIONAR DISTORSIONES en los sistemas de distribución de las compañías suministradoras**, justificado por el diseñador y **aprobado por la comunidad autónoma** |

**La condición de no distorsionar la red no aparece en ninguno de los otros reglamentos del anexo**, y
**vuelve a explicarse por lo mismo: la red es compartida.**

**Y la tercera vía, la excepción del artículo 24**, con dos rasgos que no tiene ninguna otra del anexo:

| Rasgo | Qué dice |
|---|---|
| **Límite de fondo** | **Las medidas alternativas EN NINGÚN CASO podrán rebajar los niveles de protección establecidos en el Reglamento** |
| **Silencio administrativo** | **Se entiende DESESTIMATORIO** |

**Ese silencio desestimatorio conviene contrastarlo con los quince días de silencio POSITIVO del
artículo 6 del reglamento de instalaciones petrolíferas del tema 4.** **Dos reglamentos del mismo
anexo y dos sentidos opuestos del silencio**, y **lo que los separa es qué se está pidiendo**: **allí,
comunicar una modificación menor; aquí, que se exceptúe una prescripción de seguridad.**

**Las empresas instaladoras, del artículo 22**: **el mismo régimen de declaración responsable que el
resto del anexo** —habilitación **por tiempo indefinido**, **desde el momento de su presentación** y
**para todo el territorio español, sin requisitos ni condiciones adicionales**—, **sin perjuicio del
proyecto y la dirección de obra por técnicos titulados competentes.**

**Y la remisión final del artículo 7, que cierra el círculo del epígrafe 1**: **si en una instalación
de baja tensión hay circuitos o elementos por encima de sus límites, y este reglamento no dice nada
específico, se cumple lo que establezcan los reglamentos de esas tensiones.** **Los tres reglamentos
se remiten unos a otros; ninguno se basta solo.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **El artículo 1 entero**, citado literalmente |
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 337/2014, de 9 de mayo, sobre condiciones técnicas y garantías de seguridad en instalaciones eléctricas de alta tensión** (`BOE-A-2014-6084`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal**: su contenido se resume, y sus artículos van identificados |
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 223/2008, de 15 de febrero, sobre condiciones técnicas y garantías de seguridad en líneas eléctricas de alta tensión** (`BOE-A-2008-5269`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal**: su contenido se resume, y sus artículos van identificados |

**Cinco declaraciones expresas:**

1. **Las ochenta y cuatro instrucciones técnicas complementarias de los tres reglamentos están
   volcadas y NO se citan literalmente.** **Ninguna de sus tablas de secciones, intensidades
   admisibles, distancias, coeficientes o plazos se reproduce aquí**, y **el temario no atribuye a
   ninguna un valor que no haya leído.** **Se nombran cuando un artículo citado las nombra.**
2. **Los artículos que se resumen en tabla y no se citan van identificados uno a uno** —del de baja
   tensión, el 2, el 3, el 4, el 7, el 10, el 18, el 19, el 20, el 21, el 22, el 23 y el 24; de los
   dos de alta tensión, el 1, el 2 y el 3—. **Todos están en las normas citadas arriba.**
3. **La comparación entre los tres reglamentos es del temario**: **las tres normas no se comparan a sí
   mismas.** **Cada fila de cada tabla comparativa procede del artículo que se identifica al lado**, y
   **la lectura que las une —qué cambia y por qué— se declara como oficio.**
4. **Las normas que estos reglamentos invocan se nombran y no se han consultado**: **la Ley 21/1992 de
   Industria** —sus artículos 12.3, 12.5 y 14—, **la Ley 24/2013 del Sector Eléctrico**, **el Real
   Decreto 1955/2000** y **el Real Decreto 614/2001 sobre riesgo eléctrico.** **De este último,
   además, hay cita literal verificada en el tema 17 del específico de Ingeniería Técnica ·
   Telecomunicación y en el homólogo de Técnica de Equipos y Sistemas Electrónicos**, escritos en este
   mismo proyecto.
5. **La relación de raíz de tres entre 230 y 400 voltios es aritmética elemental**, no una afirmación
   de la norma: **el reglamento da las dos cifras y no las relaciona.**

**El resto del tema va como oficio y así se declara**: la explicación de que las dos últimas
finalidades del artículo 1 son propias de la electricidad porque la red es compartida, la observación
de que la excepción de las centrales nucleares suma en vez de excluir, la advertencia sobre el cuadro
de baja tensión dentro de una instalación de alta, la regla de que la columna de continua es una vez y
media la de alterna, la nota sobre la numeración descendente en tensión ascendente de las categorías,
la lectura del artículo 10.3 como el supuesto de un centro emisor, la observación de que una reforma
puede ser de importancia aunque baje la potencia, la lectura del artículo 18.5 como el régimen de un
despliegue de exteriores y el contraste entre el silencio desestimatorio de este reglamento y el
positivo del de instalaciones petrolíferas. **Nada de eso lo dicen las normas con esas palabras**, y el
tema no lo presenta como si lo dijeran.
