# T10 · Investigación · rúbricas «régimen jurídico» y «Normativa europea y nacional»

Punto 10 del temario común de Canal Sur: «El régimen jurídico de la protección de los datos de
carácter personal. Normativa europea y nacional. Especialidades en el sector Audiovisual.»
Este informe cubre solo las dos primeras rúbricas y trabaja sobre el texto que ya existe para RTVE.
La tercera está en `T10-investigacion-audiovisual.md`, de otro agente.

**Fecha de lectura de todo lo citado: 24-09-2026**, en la redacción vigente ese día
(`boe.py precepto`, `boe.py norma`, API de legislación consolidada del BOE, `doue.py` y el
servicio SPARQL de la Oficina de Publicaciones de la UE).

**Ficheros tocados**: he volcado `fuentes/canal-sur/BOE-A-2018-16673.md` y
`fuentes/canal-sur/BOE-A-2018-16673.redacciones.tsv` con `boe.py norma` (10:55). Estaba en la lista
de `fuentes/canal-sur/volcar.sh` y aún no se había volcado. El otro agente lo vio aparecer y lo
anota en su informe: fui yo. El volcado del RGPD que hice con `doue.py` está en mi scratchpad, no en
el repositorio. No he tocado ningún otro fichero.

---

## 1. Qué redacción estudia cada tema de RTVE

| Tema | Ficha: «Redacción que se estudia» | Normas |
|---|---|---|
| `temas/produccion-asistencia/17-proteccion-de-datos.md` (13.284 palabras según su ficha) | «La vigente el **21/12/2022**». Deja fuera del cuerpo el **art. 53 bis** y la **DA 23.ª**, «ambos desde el **10/05/2023**» | LOPDGDD (`BOE-A-2018-16673`) + RGPD (`DOUE-L-2016-80807`) con sus dos correcciones (`DOUE-L-2018-80845`, `DOUE-L-2021-80264`) |
| `temas/gestion/09-proteccion-de-datos.md` (2.088 palabras según su ficha) | «Las dos, en su redacción **vigente al 21/12/2022**» | LOPDGDD + **LO 7/2021** (`BOE-A-2021-8806`), y el RGPD solo para los principios y las bases de licitud |

Los dos estudian el 21-12-2022. Aquí se estudia lo vigente el 24-09-2026: todo lo que cambió entre
esas dos fechas hay que corregirlo en el cuerpo.

---

## 2. LOPDGDD: preceptos citados que cambiaron después del 21-12-2022

La API del BOE tiene esta ley como consolidada («Finalizado», última actualización el 20-07-2026).
Hoy la cadena da **15 bloques con dos redacciones** más **2 bloques añadidos**, y **ninguna reforma
cruzada**. La lista de «referencias posteriores» del BOE coincide con esa cadena:

- Ley 10/2025 modifica el art. 23.
- Ley 11/2023 modifica los arts. 48.2, 50, 64 a 67, 75 y 77, y añade el art. 53 bis y la DA 23.ª.
- Ley 2/2023 modifica el art. 24.
- LO 7/2021 modifica los arts. 2 y 44.3 y la DA 15.ª.
- LO 3/2020 modifica el art. 83.1.
- La STC 76/2019 anula en parte la DF 3.ª.

**Todos los demás bloques tienen una sola redacción**, en vigor desde el 07-12-2018. Por tanto no
cambió ningún otro precepto que citen los dos temas (1, 3 a 22, 25 a 47, 49, 51 a 63, 68 a 74, 76,
78 a 97 y DA 6.ª). En particular siguen iguales el **7** (catorce años), el **22** (un mes y setenta y
dos horas), el **34.3** (diez días) y el **88**, que son los que preguntó el examen de RTVE.

Los cambios de la LO 7/2021 (arts. 2, 44.3 y DA 15.ª), de la LO 3/2020 (art. 83) y de la STC 76/2019
son **anteriores al corte**: los temas de RTVE ya los tienen. Los que siguen son **posteriores**, y
cada uno se ha comparado con `--fecha 20221221`:

### 2.1 Art. 23 (sistemas de exclusión publicitaria). Bloque `a2-5`

Cadena: 07-12-2018 (texto original) → **28-12-2025**, por la **Ley 10/2025, de 26 de diciembre, por
la que se regulan los servicios de atención a la clientela** (`BOE-A-2025-26698`, DF 4.ª: «Se
modifica el apartado 1 del artículo 23»). Su DF 8.ª: «entrará en vigor el día siguiente al de su
publicación» (BOE de 27-12-2025).

Solo cambia el párrafo segundo del apartado 1. Hoy dice: «podrán crearse sistemas de información,
generales o sectoriales, **por parte de las asociaciones y organismos a los que se refiere el
apartado 2 del artículo 40 del Reglamento (UE) 2016/679** […] **que cuenten con una alta
representatividad** en los que solo se incluirán los datos imprescindibles para identificar a los
afectados. […] **Para la creación y mantenimiento de estos sistemas se observarán las medidas que se
establezcan mediante desarrollo reglamentario.**» Los apartados 2 a 4 no cambian, y tampoco la regla
que usa el tema (23.4: consulta previa salvo consentimiento).

**Efecto en el tema de RTVE (§5.3)**: lo que dice sigue siendo cierto, pero está incompleto. Hay que
añadir quién puede crear los sistemas.

### 2.2 Art. 24. Bloque `a2-6`. **Cambió entero**

Cadena: 07-12-2018 → **13-03-2023**, por la **Ley 2/2023, de 20 de febrero, reguladora de la
protección de las personas que informen sobre infracciones normativas y de lucha contra la
corrupción** (`BOE-A-2023-4513`). El título pasó de «Sistemas de información de denuncias internas»
a «**Tratamiento de datos para la protección de las personas que informen sobre infracciones
normativas**». Texto vigente, entero:

> «Serán lícitos los tratamientos de datos personales necesarios para garantizar la protección de
> las personas que informen sobre infracciones normativas.
> Dichos tratamientos se regirán por lo dispuesto en el Reglamento (UE) 2016/679 […], en esta ley
> orgánica y en la Ley reguladora de la protección de las personas que informen sobre infracciones
> normativas y de lucha contra la corrupción.»

**Efecto en el tema de RTVE (§5.3)**: el bloque del art. 24 es **derecho derogado** y hay que
quitarlo entero: entidad de Derecho privado, acceso de control interno, tres meses, anonimización y
extensión a las Administraciones. Parte de ese régimen sigue vigente, pero ahora está en la
**Ley 2/2023, art. 32** (bloque `a3-4`, una sola redacción):

- 32.1: acceso limitado a cinco sujetos, letras a) a e): Responsable del Sistema, RR. HH. solo si
  pudiera haber medidas disciplinarias, servicios jurídicos, encargados y **DPD**.
- 32.4: «transcurridos **tres meses desde la recepción de la comunicación sin que se hubiesen iniciado
  actuaciones de investigación**, deberá procederse a su supresión, salvo que la finalidad de la
  conservación sea dejar evidencia del funcionamiento del sistema. Las comunicaciones a las que no se
  haya dado curso solamente podrán constar de forma anonimizada, sin que sea de aplicación la
  obligación de bloqueo prevista en el artículo 32 de la Ley Orgánica 3/2018».

Ojo: el plazo ya no se cuenta desde «la introducción de los datos», sino desde «la recepción de la
comunicación», y se condiciona a que no se hayan iniciado actuaciones. El régimen de datos de esa ley
es su **Título VI, arts. 29 a 34** (29: régimen jurídico, que remite al RGPD, a la LOPDGDD y a la
LO 7/2021; 30: licitud; 31: información; 32: el Sistema interno de información; 33: identidad del
informante; 34: DPD).

### 2.3 Arts. 48, 50, 53 bis, 64, 65, 66, 67, 75, 77 y DA 23.ª. Todos por la Ley 11/2023

Todos entran en vigor el **10-05-2023** por la **Ley 11/2023, de 8 de mayo**, de trasposición de
Directivas de la Unión Europea en materia de accesibilidad de determinados productos y servicios,
migración de personas altamente cualificadas, tributaria y digitalización de actuaciones notariales y
registrales (`BOE-A-2023-11022`, BOE de 09-05-2023). Cadena de cada uno: 07-12-2018 → 10-05-2023.

| Precepto | Antes (21-12-2022) | Hoy (literal donde importa) | Lo que hay que tocar en RTVE |
|---|---|---|---|
| **48.2** (`a4-10`) | Solo el Adjunto, que puede recibir por delegación todo salvo lo del Título VIII | Añade tres párrafos. En ausencia, vacante, enfermedad, abstención o recusación de la Presidencia (art. 23 Ley 40/2015), **las competencias del Título VIII «serán asumidas por la persona titular del órgano directivo que desarrolle las funciones de inspección»**. Si ella tampoco puede, los subdirectores generales «por el orden establecido en el Estatuto». El resto de competencias, el Adjunto | §9: añadir la suplencia. Lo que dice sobre la delegación sigue bien |
| **50** (`a5-2`) | Se publicaban las resoluciones «que sancionen con apercibimiento a las entidades […] del artículo 77.1» | Se publican las que pongan fin «**a los procedimientos sancionadores y a los procedimientos de apercibimiento**» y «**las dictadas respecto de las entidades a que se refiere el artículo 77.1**» | RTVE no lo cita. Solo sirve si se trata la publicidad |
| **53 bis** (`a5-12`), nuevo | No estaba en vigor, y RTVE lo excluye a propósito | «Las actuaciones de investigación **podrán** realizarse a través de sistemas digitales», como la videoconferencia, con comunicación «bidireccional y simultánea». Su uso «se producirá cuando lo determine la Agencia y **requerirá la conformidad del inspeccionado** en relación con su uso y con la fecha y hora» | §9 (arts. 51 a 54): **añadirlo** |
| **64** (`a6-6`) | 64.2: sancionador de «**nueve meses**» desde el acuerdo de inicio «o, en su caso, del proyecto de acuerdo de inicio». 64.3: reclamación que llega de la autoridad de otro Estado miembro. 64.4: suspensión de plazos | **64.2**: «duración máxima de **doce meses** a contar desde la fecha del acuerdo de inicio», y el acuerdo de inicio «le será notificado al interesado». **64.3, nuevo**: «la Agencia […], previa audiencia al responsable o encargado del tratamiento, **podrá dirigir un apercibimiento**, así como ordenar […] que adopten las medidas correctivas», teniendo en cuenta los criterios del **art. 83.2 RGPD**. Ese procedimiento tiene una «duración máxima de **seis meses**» y, pasado el plazo, «caducidad». La antigua regla de otro Estado miembro pasa a ser el **64.4**, y la de suspensión el **64.5**. **64.6, nuevo**: los plazos se pueden suspender por resolución motivada «cuando resulte indispensable recabar información de un órgano jurisdiccional». El 64.1 no cambia en lo que importa (seis meses, estimación) | §10, tabla: **nueve → doce meses**. Añadir el procedimiento de apercibimiento (seis meses) y el 64.6 |
| **65** (`a6-7`) | 65.4: remisión al DPD o al organismo de supervisión | **65.4**: además, al «organismo que asuma las funciones de resolución extrajudicial de conflictos». Párrafo nuevo: si con la remisión el responsable «demuestra haber adoptado medidas», la Agencia «**podrá inadmitir**». **65.5**: mantiene los **tres meses**, pero ahora «sin perjuicio de la facultad de la Agencia de archivar posteriormente y de forma expresa la reclamación». En los casos del 64.4 el plazo corre desde que llega «toda la documentación necesaria», y la Agencia puede indicar el expediente ya abierto sobre los mismos hechos. **65.6, nuevo**: archivo tras la admisión si se han adoptado medidas y concurren circunstancias que aconsejan «soluciones más moderadas», siempre que no se hayan iniciado actuaciones previas ni procedimiento. 65.2 y 65.3 no cambian | §10: el art. 65 del tema sigue siendo cierto, pero incompleto. Añadir 65.4 in fine, 65.5 in fine y 65.6 |
| **66** (`a6-8`) | «Salvo en los supuestos […] del artículo **64.3**» | «Salvo en los supuestos […] del artículo **64.4**». Solo cambia la remisión | §10: **64.3 → 64.4**. Si no se corrige, es una cita cruzada (error 1) |
| **67.2** (`a6-9`) | «no podrán tener una duración superior a **doce meses**», incluido el caso de comunicación de otro Estado miembro (64.3) | «no podrán tener una duración superior a **dieciocho meses**» desde la admisión o desde el acuerdo de iniciación si la Agencia actúa por propia iniciativa. Desaparece la mención a otro Estado | §10, tabla: **doce → dieciocho meses** |
| **75** (`a7-7`) | Párrafo 2: en el procedimiento del art. 60 RGPD interrumpe «el conocimiento formal por el interesado del **proyecto de** acuerdo de inicio» | «[…] del **acuerdo de inicio**». El párrafo 1 no cambia | §11.1: la frase del tema (párrafo 1) sigue bien. Si se añade el párrafo 2, con la redacción nueva |
| **77.2** (`a7-9`) | La autoridad «dictará resolución **sancionando** a las mismas **con apercibimiento**» | «dictará resolución **declarando la infracción y estableciendo, en su caso, las medidas** que proceda adoptar para que cese la conducta o se corrijan los efectos de la infracción que se hubiese cometido, **con excepción de la prevista en el artículo 58.2.i** del Reglamento (UE) 2016/679». El 77.1 (once sujetos, a) a k)) y el 77.3 a 77.6 no cambian. El 77.3 sigue diciendo «en la resolución en la que se imponga la sanción» | §11.4: hay que **reescribir** «la autoridad no impone multa: dicta resolución sancionando con apercibimiento» y «España usó esa habilitación para sustituir la multa por el apercibimiento». Ahora es una resolución que declara la infracción y fija medidas, **y excluye la medida del 58.2.i RGPD**, que es «imponer una multa administrativa con arreglo al artículo 83» (art. 58.2.i RGPD, leído en `DOUE-L-2016-80807`). La palabra «apercibimiento» ya no está en el 77.2 |
| **DA 23.ª** (`da-23`), nueva | No estaba en vigor, y RTVE la excluye | La AEPD «**podrá** establecer modelos de presentación de reclamaciones», que serán «**de uso obligatorio para los interesados** independientemente de que estén obligados o no a relacionarse electrónicamente». Se publican en el BOE y en su sede electrónica, y son obligatorios «**al mes de su publicación** en el Boletín Oficial del Estado» | §10: **añadirla** |

**Un dato que no he podido confirmar**: por qué el 77.2 dejó de decir «sancionando con
apercibimiento». La corrección de errores de 2021 cambió el art. 58.2.a) y b) RGPD de «sancionar
[…] con apercibimiento» a «**dirigir** […] un apercibimiento» (`DOUE-L-2021-80264`, punto 16). Eso
cuadra con la reforma, pero ninguna norma lo dice. **No va al tema.**

### 2.4 Otros datos de los temas que siguen vigentes, pero que hay que vigilar

- **Art. 44.1 y 48.3**: siguen diciendo literalmente «**Ministerio de Justicia**» (bloques `a4-6` y
  `a4-10`, leídos hoy). La pregunta del examen de RTVE (la AEPD se relaciona con el Gobierno a
  través de Justicia) sigue siendo correcta. El nombre actual del departamento no lo he comprobado,
  y no hace falta: se cita la ley.
- **DT 1.ª**: sigue remitiendo al «Estatuto […] aprobado por Real Decreto 428/1993». Ese real
  decreto está **derogado** por el **Real Decreto 389/2021, de 1 de junio**, por el que se aprueba
  el Estatuto de la AEPD (`BOE-A-2021-9175`, disposición derogatoria única, 1). El BOE no registra
  ninguna modificación posterior del RD 389/2021. Ninguno de los dos temas lo menciona.

---

## 3. Reglamento (UE) 2016/679: correcciones y modificaciones

- **Correcciones de errores en español: siguen siendo dos**, `DOUE-L-2018-80845` (DOUE L 127, de
  23-05-2018) y `DOUE-L-2021-80264` (DOUE L 74, de 04-03-2021). Lo he comprobado de tres maneras:
  1. La página del BOE de `DOUE-L-2016-80807`, leída hoy: en «Referencias posteriores» solo aparecen
     esas dos «CORRECCIÓN de errores», y ninguna modificación.
  2. Un volcado nuevo con `doue.py`, que sale **idéntico** a `fuentes/corte-20221221/` en el
     Reglamento y en las dos correcciones (diff vacío).
  3. Cellar (SPARQL): hay tres correcciones, `32016R0679R(01)`, `R(02)` y `R(03)`. La `R(01)`, de
     22-11-2016, **no tiene versión española**; `R(02)` y `R(03)` son las dos de arriba.
- **Modificaciones del articulado: ninguna.** Cellar no devuelve ningún acto con la relación
  «amends» sobre 32016R0679.
- **Norma europea nueva que completa el RGPD**: **Reglamento (UE) 2025/2518 del Parlamento Europeo
  y del Consejo, de 26 de noviembre de 2025, por el que se establecen normas procedimentales
  adicionales sobre la garantía del cumplimiento del Reglamento (UE) 2016/679** (DO L de
  12-12-2025, ELI `http://data.europa.eu/eli/reg/2025/2518/oj`). Art. 1: se aplica a las
  reclamaciones e investigaciones «cuando dichos asuntos se refieran a tratamientos
  transfronterizos». Art. 37: «entrará en vigor a los veinte días de su publicación» y «**será
  aplicable a partir del 2 de abril de 2027**». **No modifica el texto del RGPD**: no lleva ningún
  artículo de modificación. **Hoy está en vigor pero todavía no se aplica.** El buscador del BOE no lo
  encuentra en su sección del DOUE (`boe_buscar.py`, sin resultados), así que no tiene identificador
  `DOUE-L`. Si entra en el tema, que sea en una línea y con esa salvedad.
- Del propio RGPD, para el marco (leído en la página del BOE): **considerando 1**, que invoca el
  «**artículo 8, apartado 1**, de la Carta» y el «**artículo 16, apartado 1**, del TFUE»; **art. 94**,
  que deroga la Directiva 95/46/CE «con efecto a partir del 25 de mayo de 2018»; **art. 95**, sobre
  la relación con la Directiva 2002/58/CE; y **art. 99**, en vigor a los veinte días, «aplicable a
  partir del **25 de mayo de 2018**» y «**directamente aplicable** en cada Estado miembro».
- No he comprobado si se ha adoptado el paquete «ómnibus digital» (propuestas de 2025). Cellar no
  devuelve ningún reglamento de 2024 a 2026 con «2016/679» en el título español, salvo el 2025/2518.
  **No se afirma nada sobre él.**

---

## 4. Lo que pide el enunciado de Canal Sur y los temas no dan, y lo que hay que quitar

### 4.1 Falta: el régimen jurídico (fundamento y naturaleza de las normas)

| Qué | Precepto, leído hoy |
|---|---|
| Fundamento constitucional, con su texto | **Art. 18.4 CE**: «La ley limitará el uso de la informática para garantizar el honor y la intimidad personal y familiar de los ciudadanos y el pleno ejercicio de sus derechos» (una redacción). RTVE solo lo nombra a través del art. 1 LOPDGDD |
| Fundamento europeo | Considerando 1 RGPD (art. 8.1 de la Carta y art. 16.1 TFUE). No he leído la Carta ni el TFUE en su fuente |
| Naturaleza de la LOPDGDD | **DF 1.ª**: es ley orgánica, pero tienen **carácter de ley ordinaria** el Título IV; el VII (salvo los arts. 52 y 53); el VIII; el IX; los **arts. 79, 80, 81, 82, 88, 95, 96 y 97**; las DA (salvo la 2.ª y la 17.ª); las DT; y las DF (salvo la 1.ª, 2.ª, 3.ª, 4.ª, 8.ª, 10.ª y 16.ª). Así se explica que una ley ordinaria (Ley 10/2025) haya modificado el art. 23, del Título IV |
| Título competencial | **DF 2.ª**: art. 149.1.1.ª CE. **DF 2.ª.2**: el **cap. I del Título VII, el Título VIII**, la DA 4.ª y la DT 1.ª «**sólo serán de aplicación a la Administración General del Estado** y a sus organismos públicos». **DF 2.ª.3**: los arts. 87 a 90 se dictan por el 149.1.7.ª y 18.ª |
| Lo que la LOPDGDD derogó | **Disposición derogatoria única**: la **LO 15/1999** (sin perjuicio de la DA 14.ª y la DT 4.ª) y el **Real Decreto-ley 5/2018, de 27 de julio** |
| Tratamientos policiales y penales | **LO 7/2021** (`BOE-A-2021-8806`), que transpone la Directiva (UE) 2016/680 (lo nombra el art. 22.6 LOPDGDD). Desde 2022 solo tiene un cambio: el **art. 61**, por la **LO 9/2022**, con efectos desde el 29-08-2022. Los **arts. 58 y 63** que usa Gestión no cambiaron |
| Estatuto de la AEPD | **RD 389/2021** (ver 2.4) |
| Jurisprudencia constitucional | La **STC 292/2000, de 30 de noviembre** existe (`BOE-T-2001-332`, BOE de 04-01-2001, «Vulneración del derecho fundamental a la protección de datos personales»). **No he leído el texto: no se puede afirmar nada de su doctrina.** La **STC 76/2019** anuló el art. 58 bis.1 LOREG, que había introducido la DF 3.ª LOPDGDD (`BOE-A-2019-9548`, título leído) |

### 4.2 Falta: la normativa nacional y la autonómica, que es la que importa a Canal Sur

- **Autoridad de control autonómica.** Art. **57.1 LOPDGDD**: las autoridades autonómicas ejercen
  los arts. 57 y 58 RGPD sobre los «tratamientos de los que sean responsables las entidades
  integrantes del **sector público de la correspondiente Comunidad Autónoma** […] o quienes presten
  servicios a través de cualquier forma de gestión directa o indirecta». En Andalucía:
  - **Estatuto de Autonomía** (`BOE-A-2007-5825`), **art. 82**: competencia ejecutiva sobre los
    datos «gestionados por las instituciones autonómicas de Andalucía, Administración autonómica,
    Administraciones locales, y **otras entidades de derecho público y privado dependientes de
    cualquiera de ellas**». **Art. 32**: derecho «al acceso, corrección y cancelación» de los datos
    en poder de las Administraciones públicas andaluzas. Los dos tienen una sola redacción.
  - **Ley 1/2014, de 24 de junio, de Transparencia Pública de Andalucía** (`BOE-A-2014-7534`),
    **art. 43.1**: «Se crea el **Consejo de Transparencia y Protección de Datos de Andalucía** […]
    como **autoridad independiente de control en materia de protección de datos** y de transparencia
    en la Comunidad Autónoma de Andalucía». 43.2: entidad pública con personalidad jurídica propia.
    43.4: se relaciona con la Junta «a través de la **Consejería de la Presidencia**». **Art.
    48.1.h)**: la Dirección desempeña «las funciones previstas en la legislación sobre protección de
    datos para su ejercicio por las agencias autonómicas». Ojo con este artículo: tiene dos
    redacciones. La **Ley 1/2026, de 20 de febrero, Universitaria para Andalucía**
    (`BOE-A-2026-6643`), en vigor desde el 26-03-2026, suprimió la antigua letra h) («instar la
    incoación de expedientes»), y la de protección de datos pasó de la i) a la **h)**. La misma ley
    suprime los arts. 51 a 58 de la Ley 1/2014. Los arts. 43 a 47 y 49 tienen una sola redacción.
  - De ahí sale una conclusión que **no he visto escrita en ningún precepto**: la autoridad de
    control de la RTVA y de sus sociedades sería el Consejo andaluz y no la AEPD. Es una inferencia
    del 57.1.a) LOPDGDD y del 82 EAA. Para afirmarla, hay que leer el Decreto 434/2015 (estatutos
    del Consejo, en BOJA), que no he leído.
- **Otras normas nacionales vigentes con reglas de protección de datos**. He comprobado en el BOE que
  existen y están vigentes; solo he leído los preceptos que se indican:
  - **Ley 2/2023**, Título VI (ver 2.2), y su Autoridad Independiente de Protección del Informante,
    cuyo Estatuto es el RD 1101/2024 (`BOE-A-2024-22298`, solo el registro de referencia).
  - **Ley 34/2002, LSSI** (`BOE-A-2002-13758`), **art. 22.2** (dispositivos de almacenamiento,
    «cookies»): se exige consentimiento después de dar «información clara y completa». Cuatro
    redacciones; la vigente es de 11-05-2014. **Aviso**: remite todavía a la «Ley Orgánica 15/1999»,
    que está derogada; se cita literal y se advierte.
  - **Ley 11/2022, General de Telecomunicaciones** (`BOE-A-2022-10757`), **art. 60, «Protección de
    los datos de carácter personal»**, y **art. 58**, «Secreto de las comunicaciones». Solo he
    leído los títulos.
  - **Ley 19/2013** de transparencia: la conecta la **DA 2.ª LOPDGDD** (publicidad activa y acceso
    se someten a los arts. 5.3 y 15 de la Ley 19/2013, al RGPD y a la LOPDGDD). DA leída; la
    Ley 19/2013 no.
  - **LO 1/1982** y **LO 2/1984** (rectificación) son de la rúbrica audiovisual (otro agente). El
    tema de RTVE ya cita la LO 2/1984 a través del art. 85 LOPDGDD.

### 4.3 Lo propio de RTVE que hay que quitar o sustituir

En `produccion-asistencia/17`:

- La ficha, el enunciado y la «Redacción […] 21/12/2022», con el aviso de los dos bloques no
  vigentes, que ahora sí lo están y entran en el cuerpo.
- **§11.4, último párrafo**: «Corporación RTVE es una sociedad mercantil estatal […] art. 5.1 de la
  Ley 17/2006». Hay que sustituirlo por lo de Canal Sur, leído en su fuente:
  - **Ley 18/2007** (`BOE-A-2008-1185`): la RTVA «es una **Agencia Pública Empresarial**» con
    «personalidad jurídica propia», y la prestación la hacen «**sociedad[es] mercantil[es] del sector
    público andaluz**» (art. 5.1 y 5.2, «Naturaleza jurídica y adscripción», y art. 9.1 y 9.2;
    volcado de `fuentes/canal-sur/`).
  - **Ley 9/2007**, art. **52.2**: las agencias «tienen **personalidad jurídica pública** y la
    consideración de Administración institucional dependiente». **52.3**: las sociedades mercantiles
    «tienen personalidad jurídica privada».
  - **Inferencia, no confirmada por ningún precepto**: la RTVA encaja en el **77.1.d)**
    («organismos públicos y entidades de Derecho público vinculadas o dependientes»), y las
    sociedades mercantiles no encajan en ninguna letra del 77.1.
  - **Además, no cuadra con la fuente**: el encargo habla de «Canal Sur Radio y Televisión, S.A.»,
    pero el art. 9.1 y 9.2 de la Ley 18/2007 vigente nombra **dos** sociedades, «Canal Sur Radio,
    Sociedad Anónima» y «Canal Sur Televisión, Sociedad Anónima».
- **§12.1**, comentario al 83.4: «estas pruebas son de una sociedad mercantil estatal». Hay que
  adaptarlo o quitarlo.
- **§12.2, art. 91**: «III Convenio Colectivo de la Corporación RTVE». Se quita.
- **§13** («Qué le toca a una producción de televisión») es del puesto de RTVE. Se decide con la
  rúbrica audiovisual.
- **§14** (preguntas de examen de RTVE) y **§15** (trazabilidad con cifras de RTVE): se quitan o se
  rehacen. Canal Sur no tiene exámenes anteriores.

En `gestion/09`:

- «Antes de empezar», el «Aviso sobre las fuentes», **§8** (tabla de examen de RTVE) y **§9**.
- «Enlazan directamente con el artículo 20 bis del Estatuto, que es el punto 8 de este mismo
  temario»: es una remisión al temario de RTVE.

---

## 5. Qué tema tomar como base

**Base literal: `produccion-asistencia/17`.** Por qué:

- Es el único que cubre las dos normas, el RGPD y la LOPDGDD, con el precepto pegado. El enunciado
  pide «Normativa europea y nacional», y Gestión solo trae del RGPD dos párrafos sin artículo.
- Ya resolvió el problema de que el RGPD no esté consolidado (cita corregida, artículo por artículo).
  Esa lista sigue valiendo: no hay correcciones nuevas.
- Recorre la ley entera por Títulos (I a X), que es lo que pide «régimen jurídico».
- Casi todo lo que hay que corregir por vigencia está en sus §5.3, §9, §10 y §11.4, y está acotado
  (sección 2 de este informe).

**Qué añadir de `gestion/09`**:

- **§7 (LO 7/2021)**: el ámbito, el art. 58 (letras a) a g)) y el art. 63.1 (seis meses, dos años y
  tres años). Se añaden como **normativa nacional**, que es lo que pide el enunciado de Canal Sur,
  sin el enfoque de «el examen se salió del programa». Hoy siguen iguales (solo cambió el art. 61).
- **§1**, la tabla «tres normas superpuestas»: sirve de arranque para la rúbrica «Normativa europea
  y nacional», ampliada con lo de la sección 4.
- Lo demás de Gestión (arts. 7, 22, 44 y Título X) **ya está en Producción-Asistencia** y con más
  detalle. No se duplica.
- Tampoco se toma de Gestión su «§2 Principios» (principios y bases sin artículo): la versión con
  precepto está en Producción-Asistencia, §2.1 y §3.1.

**Y, además, lo que no trae ninguno** (sección 4.1 y 4.2): el art. 18.4 CE con su texto; la DF 1.ª y
la DF 2.ª y la derogatoria de la LOPDGDD; el RD 389/2021; el Consejo de Transparencia y Protección de
Datos de Andalucía (arts. 32 y 82 EAA, arts. 43 y 48.1.h Ley 1/2014); la Ley 2/2023 en lugar del
viejo art. 24; y, en una línea, el Reglamento (UE) 2025/2518, aplicable desde el 02-04-2027.

## 6. Lo que queda sin confirmar

- La doctrina de la STC 292/2000: no está leída.
- Si el Consejo andaluz es la autoridad de control de la RTVA y de Canal Sur: es una inferencia; hay
  que leer el Decreto 434/2015 en el BOJA.
- Si la RTVA encaja en el art. 77.1.d): es una inferencia.
- Si se ha adoptado el paquete «ómnibus digital» que modificaría el RGPD: no lo he comprobado, más
  allá de que Cellar no da ninguna modificación.
- El texto de la Carta (art. 8) y del TFUE (art. 16): solo los he leído a través del considerando 1
  del RGPD.
- Los arts. 58 y 60 de la Ley 11/2022: solo he leído los títulos.
