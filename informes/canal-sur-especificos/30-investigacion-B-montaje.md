# Puesto 30 · Operador/a Montador/a de Vídeo · Investigación del bloque B-montaje (temas 1, 5, 6, 9, 14, 15)

Fase 1 · Investigar. Fecha de trabajo: 24/25-09-2026. Se escribe según avanza.

Alcance: sólo lo que **falta** para cubrir el enunciado después de lo reutilizable ya localizado
(RTVE: edicion-montaje/07, 08, 10; realizacion/02, 20. Redactor/a cerrado: 34/03, 34/07, 34/10).
Aquí no se repite lo que esos temas ya copian; se dice qué pasaje nuevo aporta cada fuente.

## Fuentes y fecha de lectura

| Clave | Documento | Dónde | Leído |
|---|---|---|---|
| **LE-CS** | *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo 2004, ISBN 84-609-0453-9 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` | 25-09-2026 |
| **CONV** | X Convenio colectivo RTVA y sociedades filiales, BOJA núm. 240, de 10-12-2014 (anexo III, fichas; disposición adicional segunda) | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | 25-09-2026 |
| **LGCA** | Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual (BOE-A-2022-11311), arts. 127 y 137 | `herramientas/boe.py precepto` contra la API del BOE, redacción vigente | 25-09-2026 |
| (web) | Las fuentes técnicas de fabricante y manuales se citan con su URL en cada tema | — | 25-09-2026 |

Advertencias generales:
- **LE-CS** es de 2004 y habla de cinta, *preroll*, barras, «cabinas de edición»; lo que describe como
  soporte (cinta) está superado, pero sus reglas de montaje (6.3), raccord (6.4), selección de planos
  (5.3) y tratamiento de imágenes duras (9.9) siguen siendo el único criterio publicado de la casa.
  Se cita con número de epígrafe y página impresa.
- **CONV**: la vigencia del X Convenio (ultraactividad, prórrogas) la trata el tema común del convenio;
  aquí sólo se usan sus fichas de puesto. Las fichas son de 2014.
- **Hallazgo sobre lo reutilizable de RTVE** (para el redactor y el verificador): el tema RTVE
  `edicion-montaje/10` **no cita ninguna fuente** («Este tema no cita ninguna norma… va entera como
  oficio», § 13). Su tabla de «estilos por género» (§ 5) va en negrita como si fuera literal, pero no
  tiene fuente: si se copia, hay que pasarla a redonda y declararla oficio, o sustituirla por lo que
  aquí se documenta. Lo mismo el `realizacion/20` salvo su epígrafe 13 (LPI).

---

## Tema 1 · Lenguaje y montaje audiovisual

Enunciado: «ritmo, continuidad, raccord, elipsis, eje, estructura narrativa y tratamiento
informativo. Estilos de edición según el género».

**Lo que ya está** (RTVE edicion-montaje/10, realizacion/20): raccord, eje, dónde cortar, ritmo,
transiciones, paralelo/alternado, Kuleshov. **Sin fuente** (ver advertencia arriba).
**Lo que falta**: (a) **elipsis** (no aparece ni una vez en los dos temas RTVE: `grep -c elipsis` = 0);
(b) una **fuente académica** que respalde eje, raccord y ritmo; (c) **estructura narrativa**;
(d) **tratamiento informativo** en el montaje (casi nada en RTVE); (e) el criterio **de la casa**
(LE-CS 6.3, 6.4, 5.3, 9.9). Lo de LE-CS 6.3 y 6.4 ya está copiado en Redactor/a T07 § 10
(«Las cuatro condiciones del montaje» y raccord): **se toma de allí, no de aquí**. Lo nuevo se da abajo.

Fuente académica añadida: **MATEU** = Francisco José Mateu Torres (Fran Mateu), *Fundamentos
teóricos de la edición y el montaje audiovisual*, Editorial UMH (Universidad Miguel Hernández de
Elche), 2024, ISBN 978-84-18177-76-7. PDF del editor:
https://innovacionumh.es/editorial/Fundamentos+te%C3%B3ricos+de+la+edici%C3%B3n+y+el+montaje+audiovisual.pdf
(ficha: https://editorial.umh.es/2024/07/26/fundamentos-teoricos-de-la-edicion-y-el-montaje-audiovisual/).
Copia local: `fuentes/montaje/UMH_Mateu-2024_fundamentos-edicion-montaje.{pdf,txt}`. Leído 25-09-2026.
Páginas = numeración impresa del libro.

### 1.1 Elipsis (MATEU 3.1, pp. 33-34; 3.2, p. 37; 5.1-5.2, pp. 54-55)

- Definición: «por elipsis se entiende el proceso de alterar el tiempo real de una narración
  audiovisual, pudiéndose llevar a cabo entre planos o escenas —las secuencias ofrecen elipsis
  autocontenidas—, omitiéndose determinas acciones mediante la compresión temporal
  (Fernández-Tubau, 1994, p. 55)» (p. 34) [sic «determinas»].
- Con el corte: «en el montaje por corte también es común que haya saltos, entendidos como elipsis
  temporales y/o espaciales —algunas más inherentes que otras—, donde desaparece la
  imperceptibilidad del corte» (p. 33). Ejemplo canónico: el hueso lanzado que se convierte en
  nave en *2001: Una odisea del espacio* (Kubrick, 1968) (p. 34).
- Con el fundido: «Fundido: es una transición empleada para acentuar el paso del tiempo —elipsis—,
  lo que denota a su vez un cambio temporal y/o espacial sustancial, dando paso de una secuencia a
  la siguiente»; fundido a negro = *fade out*, fundido de apertura = *fade in* (p. 37, cita Bordwell y
  Thompson 1995).
- Capacidad del montador: «Sintetizar: recordemos que el montaje tiene la capacidad de condensar el
  tiempo "real" dentro del tiempo fílmico o audiovisual a través de elipsis espaciales y/o
  temporales.» Lo contrario, «Expandir: … ralentizaciones, congelados, encadenados prolongados, etc.»
  (5.1, p. 54).
- En montaje lineal también hay elipsis: «aunque sea un montaje lineal habitualmente encontramos
  elipsis temporales y/o espaciales, en algunas ocasiones incluso imperceptibles por la audiencia»
  (5.2, p. 55).
- Complemento (diapositivas docentes, fuente secundaria): Emma Camarero, «El montaje audiovisual.
  Teoría y práctica», Universidad Loyola, repositorio
  https://repositorio.uloyola.es/bitstream/handle/20.500.12412/2351/7-CAV_El%20montaje%20y%20la%20Edici%C3%B3n.pdf :
  «La elipsis es la supresión de los momentos del tiempo ficcional que dramáticamente no son
  narrativos. La elipsis también puede ser de montaje.» Distingue **omisión**: «suprimir todas
  aquellas escenas o acciones que, a pesar de ser dramáticamente importantes, pueden
  sobreentenderse». «Si no hay continuidad daremos impresión de paso de tiempo»; «un encadenado
  significaba un paso de tiempo»; «el corte mantiene la línea de tiempo». Sin año ni paginación:
  usar sólo como apoyo, no como fuente principal.
- **En la noticia** (aplicación, LE-CS): la noticia de un minuto condensa horas de grabación; el
  límite ético de esa elipsis lo da LE-CS 6.2: «Si mostramos, por ejemplo, a un diputado bostezando
  o hurgándose la nariz en un vídeo de un minuto, estamos falseando la realidad si esa imagen de sólo
  unos segundos se extrae de una grabación de varias horas de sesión plenaria.» (p. 89). Y la
  ruptura del orden cronológico: la edición «tiene que presentar los acontecimientos de forma lineal,
  sin alteraciones chocantes de los planos, la música, los sonidos y los textos. Una ruptura en
  cualquiera de estos sentidos, o en el orden cronológico, no debe acometerse salvo que se haga con
  lógica y sin inducir a la confusión.» (6.3, p. 92). Este último párrafo **no** está en
  Redactor/a (grep «alteraciones chocantes» sin resultado): es nuevo.

### 1.2 Eje (MATEU 3.3, p. 44) — respaldo académico de lo que RTVE da sin fuente

- «Por eje se entiende la "línea imaginaria que divide el espacio en dos porciones"
  (Fernández-Tubau, 1994, p. 55).» Con dos personajes, trazando la línea de sus miradas, «"la cámara
  está situada en un punto de un círculo cuya línea recta es un diámetro" (Sherman, 1992, p. 57)».
- Salto de eje: rodar desde el otro semicírculo; «al llevar a cabo el montaje daría la sensación de
  que se están dando la espalda».
- Por qué es del montador: «es determinante en el montaje, ya que un posible salto de eje podría
  corregirse utilizando insertos, por ejemplo; o utilizando algún plano detalle u otro tipo de
  recursos visibles ante la audiencia, evitando así que esta se desoriente (Sherman, 1992, p. 58)».
- Es «ley» entre comillas: «esta puede quebrantarse siempre y cuando conozcamos su funcionamiento…
  el eje también puede saltarse si lo que se desea transmitir es cierta confusión».
- **Casa**: LE-CS 6.4 lo mete en el raccord «Cinético» (ya en Redactor T07). El nombre «regla de los
  180°» **no aparece** en MATEU (grep «180» sin ningún resultado): si el tema lo usa, que lo
  diga como nombre de oficio.

### 1.3 Raccord (MATEU 3.4, pp. 45-47) — cuatro tipos académicos frente a los cuatro de LE-CS

- «El raccord es la continuidad espacial y temporal existente entre un plano y el siguiente, teniendo
  en cuenta para ello aspectos tan diversos como la iluminación, el atrezzo, el movimiento de los
  personajes, etc.» (p. 45).
- Script/continuista: cita de Morales (2005, p. 38): «Durante el rodaje de una película el script o
  continuista se encarga de anotar exactamente la posición, dirección, velocidad de los
  desplazamientos de cada personaje…».
- Cuatro tipos (Martin, 2002): «"Raccord de contenido material"» (un elemento se mantiene igual);
  «"Raccord de movimiento"… "continuidad de contenido dinámico"» (misma dirección); «"Raccord de
  contenido estructural"» (composición semejante: mismo segmento del cuadro); «"Raccord de sonido"»
  (pp. 45-47).
- **Ojo para el test**: LE-CS 6.4 da otros cuatro: **Técnico, Físico, Sonoro, Cinético**. No son la
  misma clasificación; el tema debe dar las dos y decir de quién es cada una.

### 1.4 Ritmo (MATEU 4.2, pp. 49-50)

- «El ritmo se refiere a la sucesión de planos partiendo de sus relaciones de duración y escala…
  (Martin, 2002, p. 157). En este sentido, si disponemos de una mayor cantidad de planos de breve
  duración y una amplia variación de escalas en tales planos, mayor será el ritmo».
- Ritmo externo / interno: el externo es «aquel que podemos manipular a través del montaje
  (Fernández-Tubau, 1994, p. 144)»; el interno, «"la cadencia de una escena determinada por su nivel
  de actividad dentro de la misma" (Fernández-Tubau, 1994, p. 158); es decir, a los movimientos de
  cámara y a cualquier dinamismo que pueda suceder en el interior del plano».
- Ejemplo del libro: escena de un minuto con mucha acción montada en dos planos = ritmo externo
  lento, interno rápido; alguien leyendo montado en cuarenta planos = interno lento, externo rápido.
  «Un ritmo lento no ha de ser sinónimo de algo negativo» (pie fig. 4.3, *Barry Lyndon*).
- Tres funciones del montaje (Martin): «creación del movimiento, creación del ritmo y creación de la
  idea» (cap. 4, p. 48).
- **Casa**: LE-CS 6.3.2 «Agilidad y cadencia» (plano < 1 s inadmisible; recurso corto ≥ 2 s) y
  5.3.2 («la alternancia lógica de planos en un montaje da vivacidad, ritmo y atractivo a la
  información», p. 81). El primero ya está en Redactor T07; el segundo es nuevo (ver tema 5).

### 1.5 Estructura narrativa (MATEU 5.2, pp. 55-58; LE-CS 3.2 y 3.4)

- Montaje narrativo: «se basa "en reunir planos según una secuencia lógica o cronológica, con vista a
  relatar una historia" (Morales, 2005, p. 74)». Subtipos según el tiempo (Martin, 2002):
  - **Lineal**: «el montaje narrativo más común… siguiendo un orden espaciotemporal cronológico».
  - **Invertido**: modifica «"el orden cronológico a favor de una temporalidad muy subjetiva…"»;
    *flashback* y *flashforward*, internos o externos.
  - **Alternado** («montaje alterno o *cross-cut*»): líneas que «comparten tiempo pero no espacio»
    y suelen converger.
  - **Paralelo**: líneas «sin contemporaneidad temporal ni convergencia espacial», para que surja
    «un significado de su confrontación»; ejemplo *Intolerancia* (Griffith, 1916).
  - **Aviso**: MATEU (con Martin) separa alternado (simultáneo) y paralelo (no simultáneo). RTVE
    edicion-montaje/10 § 7 dice seguir un reparto parecido, «porque es el que el enunciado
    presupone». Coinciden; ahora con fuente.
- Montaje expresivo (5.3, pp. 58-60): no leído en detalle; si el tema lo necesita, leer p. 58 ss.
- Estructura narrativa **informativa** (casa): noticia de cuatro párrafos (LE-CS 3.2, p. 45: ya en
  Redactor T07 § 1); reportaje: «Precisa de un elemento conductor y es una narración clásica con
  presentación, nudo y desenlace.» y «La extensión y el estilo del reportaje permiten libertad de
  elaboración y montaje, aunque prevalecen las normas de cualquier formato propio de un
  informativo.» (3.4, pp. 47-48). «elemento conductor… presentación, nudo y desenlace» **ya está** en Redactor T05 (l. 152) y T07
  (l. 284); la frase de «libertad de elaboración y montaje» **no** está en Redactor (grep): es nueva.
- Captación con vistas al montaje (LE-CS 5.2, pp. 79-80): «Una grabación realizada en exteriores,
  para facilitar el posterior montaje y edición, se asienta en cuatro condiciones mínimas. 1. Grabar
  las imágenes y los testimonios con un orden narrativo lógico, sea de manera cronológica o temática.
  2. Captar la imagen prevista… con alternancia y asociaciones de planos que tengan un nexo común
  técnico, de situación o informativo. 3. Grabar el número suficiente de planos, sin desmesura, pero
  con la duración necesaria para facilitar la selección y el corte en la edición, y para crear un
  ritmo narrativo adecuado. … 4. Rodar siempre planos de recurso para no tener que recurrir al
  archivo…». **Nuevo** (no está en Redactor).

### 1.6 Tratamiento informativo en el montaje (LE-CS) — nuevo para este puesto

- Selección de planos y objetividad (6.2, p. 89): «La preeminencia de la imagen nos obliga a ser
  cuidadosos en la selección de planos. La elección no es inocua y debe ceñirse a los criterios
  generales de objetividad e imparcialidad. No usaremos planos ni sonidos que denigren a una persona o
  a un grupo social, ni que sitúen al protagonista en actitudes indecorosas o ridículas.»
- Montaje de imágenes duras (9.9.2, pp. 166-167): «En el proceso posterior de selección y edición
  recae la responsabilidad de elegir la imagen que aporte contenido sin incidir desmesuradamente en
  la figura de las víctimas o en aspectos escabrosos. El montaje también debe valorar lo
  imprescindible y descartar lo superfluo o excesivamente conmovedor. El contenido se puede
  presentar con planos abiertos, impersonales y neutros, o se pueden ocultar parcialmente con medios
  técnicos. Sin embargo, las posibilidades de edición (ralentización, imagen congelada...) pueden
  generar un efecto reprobable y no debemos optar por ello si sólo sirve para acentuar la morbosidad
  de una historia.»
- Límite (9.9, p. 166): «nunca ofreceremos planos cortos y nítidos del rostro de una persona muerta o
  que se encuentre gravemente herida, agonizante o presa de una tensión psicológica extrema.»;
  menores, víctimas, testigos protegidos, fuerzas de seguridad: «Sus rostros serán cubiertos o
  tramados y no se aportarán detalles sobre su identidad o paradero.»
- Archivo (9.9.1, p. 166): los recursos de archivo «también serán 'tratados' en el proceso de edición
  cuando sirvan para ilustrar reportajes sobre delincuencia, malos tratos, asuntos judiciales…»; en
  rotulación, «'Archivo'» todo el tiempo en pantalla (esto último ya en Redactor T04).
- Reconstrucciones y recursos estéticos (9.2.12.3-9.2.12.4, pp. 130-131): «cuando el recurso de un
  montaje de ficción sea inevitable, es obligatorio que, durante todo el tiempo de aparición de las
  imágenes en pantalla, figure el rótulo 'Reconstrucción'.» «La imagen oscilante 'cámara en mano',
  una música tópica, un virado a blanco y negro... evocan inevitablemente escenas ficticias de
  misterio, terror... o de una película. Y la información sólo habla de realidad.» «La música es un
  aditamento impropio en los informativos diarios y, en formatos más extensos, estos recursos deben
  manejarse con matices.» (Comprobar solapes con Redactor T11 «materias sensibles».)
- Sonido falseado (3.2.2, p. 46): «La música o el falseamiento del sonido ambiente también es un
  procedimiento reprobable… el 'falseamiento' se efectuará sólo con sonidos idénticos a los de la
  realidad, o lo más parecidos que sea posible.» (**Ya en Redactor T07**, l. 114: copiar de allí.)

### 1.7 Estilos de edición según el género

- La tabla de RTVE (§ 5) **no tiene fuente**. Lo que sí tiene fuente:
  - Informativo (LE-CS): corte, planos ≥ 1 s, recurso ≥ 2 s, concordancia, armonía, sin música
    salvo que sea noticia; cierre con música admitida (3.10, ya en Redactor T07).
  - Reportaje (LE-CS 3.4): «libertad de elaboración y montaje, aunque prevalecen las normas de
    cualquier formato propio de un informativo»; sugerencia en diario: no más de tres minutos.
  - Spot/publicidad (MATEU 8.1, pp. 85-86, citando a Martínez Sáez 2009): el corte debe ser «preciso,
    al fotograma, para acoplarse al tiempo del spot, a esos veinte o treinta segundos de gloria»;
    «La condensación temporal: rasgo específico del montaje publicitario»; el montaje del spot debe
    actuar como «"gancho"» desde los primeros segundos.
  - Tráiler (MATEU 8.2, pp. 86-87): «Por lo general, el tráiler ofrece un montaje de uno a dos minutos
    y medio de duración que nos anuncia un futuro contenido audiovisual (Chion, 1992, p. 469)»;
    *teaser*: «tráiler de menor duración que pretende transmitir sensaciones sin desvelar detalles de
    la trama»; *sneak peek*: «breve pieza que avanza lo que ocurrirá en el siguiente capítulo de una
    serie».
  - Deportes y retransmisiones: ver tema 6.

### 1.8 No confirmado (tema 1)

- «Regla de los 180°», «regla de los 30°» y «jump cut» como nombres: no los busqué en fuente
  publicada; si el tema los usa, oficio o buscar fuente.
- La tabla RTVE de estilos por género (documental «planos más largos», etc.): sin fuente localizada.

---

## Tema 5 · Montaje de noticias

Enunciado: «criterio editorial, selección de planos, colas, totales, entradillas, locución y cierre».

**Lo que ya está**: Redactor/a T07 (cerrado) cubre con LE-CS estructura de la noticia, entradilla
(= aparición del redactor, 8.2.2), paso de locutor, off, totales (3.7, incluida la pregunta que «no
aparecerá en el montaje final» y el canal 2 original / canal 1 doblaje), colas (3.9), intro, intro
colas, cierre (3.10), duraciones de referencia, gráficos (8 s), escaleta y las cuatro condiciones del
montaje (6.3) y el raccord (6.4). Redactor/a T03 cubre «el vídeo se adapta a lo que fija la edición»
y la entrega escalonada en cabinas. RTVE realizacion/02 § 8 da el vocabulario del minutado.
**Lo que falta**: lo que LE-CS dice **al montador sobre el material que recibe** (5.2-5.4), el
remate del cierre (3.10, 2.º párrafo), el papel del montador (6.3, 1.er párrafo) y el orden de
trabajo imagen/texto (6.2.1). Todo LE-CS, leído 25-09-2026.

### 5.1 Criterio editorial: quién decide y papel del montador

- «Como norma obligatoria, cada vídeo debe adaptarse, en primer lugar, a la orientación, duración y
  formato establecido por los editores, responsables de todo el proceso.» (cap. 6, p. 87) — ya en
  Redactor T03.
- **Nuevo**, 6.3 (p. 90): «La opinión técnica y la participación activa del montador son esenciales,
  aunque el periodista haya previsto el ritmo de la narración, el orden de las secuencias y la
  prioridad informativa. Es conveniente que, en caso de duda, el redactor consulte al realizador los
  problemas técnicos y estéticos.» Comprobado: «montador» no aparece en Redactor T07 (grep): este párrafo es **nuevo**.
- Orden de trabajo (6.2.1, p. 89): «El método más ortodoxo dice que la noticia debería editarse
  siempre —imagen, sonido ambiente y declaraciones— primero sólo con imágenes, para escribir después
  un texto adecuado y situarlo en donde sea preciso. La experiencia demuestra, sin embargo, que el
  sistema no es operativo en el trabajo diario… El modelo habitual es otro… el texto se escribe antes
  pero no puede hacerse nunca sin tener un conocimiento previo y preciso de la imagen, el sonido y los
  testimonios grabados». Y: «El periodista, finalmente, acudirá a la cabina de montaje con la imagen
  vista y el sonido escuchado.» (p. 90). El «método más ortodoxo» **ya está** en Redactor T07 § 3 (l. 190): copiar de allí.
- Criterio editorial en la selección: 6.2 (objetividad, planos que denigren) — dado en tema 1.6.

### 5.2 Selección de planos: el material que llega a la sala (LE-CS 5.3, pp. 80-81) — nuevo

- Cuántos planos: «Un vídeo de televisión convencional necesita entre veinte y veinticinco buenos
  planos diferentes y, generalmente, agrupados en tres o cuatro secuencias distintas, para obtener una
  edición correcta de un minuto.» (5.3.1, p. 80)
- Cuánto bruto: «El equipo debe captar un total de entre cuatro y ocho minutos de imagen útiles, según
  las circunstancias y la previsión, para la elaboración de una noticia tipo de un minuto o algo más.»
  (5.3.1, p. 80)
- El plano: «Es la unidad básica, el segmento de imagen que es útil para el montaje.» (5.3.2, p. 80)
- Escala y tono: «En la selección de planos hay que tener en cuenta el tono de la noticia y el foco de
  atención en el que nos vamos a centrar. Cuanto más personal e intimista sea el motivo sobre el que
  estamos trabajando, más cortos serán los planos y más abierto cuanto más coral sea la noticia y
  mayor el número de protagonistas, sin olvidar que la alternancia lógica de planos en un montaje da
  vivacidad, ritmo y atractivo a la información.» (5.3.2, p. 81)
- Movimientos: el zoom «sólo se usará en circunstancias excepcionales»; panorámicas y *travellings*
  «comenzarán y finalizarán con un plano fijo de suficiente duración —lo recomendable es, al menos,
  un margen de diez segundos— como para que pueda ser empleados por sí mismos e independientemente
  del movimiento, en la edición final»; y «seguir registrando la imagen al menos durante cinco
  segundos… Es el margen que se precisa para el 'preroll' en una edición convencional.» (5.3.2,
  p. 81). El *preroll* es de la edición lineal en cinta: decirlo como histórico.
- Recursos: «sin descuidar la grabación de recursos estáticos, fundamentales para el montaje.» (p. 81)
- Código de tiempo (5.3.3, p. 81): «un acuerdo básico entre periodista y cámara… puede usarse un
  código de tiempo real previamente acotado, aunque también puede ser recomendable es el TC poniendo el
  marcador a 00:00:00 al principio de la cinta. Esta referencia es generalmente mejor, sobre todo
  cuando el material va a ser usado por terceras personas.» [sic «recomendable es el TC»]
- Soporte (p. 82, histórico): «una sola noticia por cinta, después de un mínimo de treinta segundos de
  barras al principio de la misma. Si hay dos noticias en el mismo soporte deben separarse con un
  minuto de barras.» Útil sólo si preguntan por la práctica de cinta; con ficheros no aplica.

### 5.3 Sonido y locución (LE-CS 5.4, p. 82; 8.2.2, p. 116) — nuevo lo de 5.4

- Canales: «Como norma general, el sonido directo de declaraciones, ruedas de prensa o el del
  periodista ante cámara se registra por el canal 1. El canal 2 recoge el sonido ambiente, captado a
  través del micrófono de la cámara.»
- «El sonido ambiente tiene que ser registrado siempre y en cualquier circunstancia»; cuando el sonido
  es la base de la noticia, grabación específica «incluso por los canales 1 y 2 simultáneamente, en
  previsión de incluirlo en emisión como vídeo total».
- «El nivel y la calidad del sonido también deben vigilarse con rigor para evitar defectos y saltos de
  volumen que deban ser solucionados en la fase de montaje.»
- Locución: la entradilla en cámara se graba «en un tono de voz natural, que no tenga diferencias
  apreciables de entonación y volumen con el que luego use en cabinas para grabar el resto de la
  locución.» (8.2.2, p. 116: ya en Redactor T07). No he hallado en LE-CS por qué canal va la locución
  del redactor en el montaje: **no confirmado** (el 3.7.1 sólo dice doblaje por canal 1, original por
  canal 2 en totales subtitulados). No afirmarlo.
- Sin solapar locución y sonido con valor informativo (6.2.1, p. 90): «no debemos superponer una
  locución llena de adjetivos para calificar lo que el ojo capta adecuadamente y, menos aún, solapar
  con ello lo que se oye y que tiene un valor informativo.» **Ya en Redactor T07** § 3 (l. 198).

### 5.4 Colas, totales y cierre: sólo lo que falta

- Colas: ya en Redactor T07 § 5. Crónica telefónica (3.5, p. 49): «Si es posible, se hará un montaje
  con imagen vinculada a la noticia en forma de 'colas' para ilustrar la información, al menos
  parcialmente.» — nuevo.
- Cierre, segundo párrafo de 3.10 (p. 54), **nuevo**: «Los cierres suelen ir precedidos del paso de
  locutor, especialmente si sustituyen a la cabecera de salida. En este caso no es recomendable incluir
  locución en colas para evitar que el presentador despida sin presencia en pantalla, aunque el
  realizador puede arbitrar numerosas variantes estéticas (vidiwall, croma...). El coleo debe ser
  suficiente para incluir sin premura la despedida y los créditos.»
- Final que se puede cortar: 3.2.1 (encabalgar los planos de transición de los últimos párrafos): ya
  en Redactor T07 § 11.
- Vídeo promocional como noticia: ver tema 6 (LE-CS 9.10.1).
- Vocabulario del minutado: copiar de RTVE realizacion/02 § 8, quitando iNews/RTVE.

### 5.5 No confirmado (tema 5)

- Por qué canal va la locución (off) del redactor en la pieza montada en Canal Sur hoy: no consta.
- Cómo se nombran hoy en Canal Sur los formatos (si «entradilla» sigue siendo la aparición del
  redactor): sólo consta el uso de 2004 (LE-CS 8.2.2).

---

## Tema 6 · Montaje de programas, promociones, piezas culturales, deportes y contenidos digitales

**Lo que ya está**: RTVE edicion-montaje/10 § 5 (tabla de estilos por género, **sin fuente**) y
edicion-montaje/08 (EVS: repetición y retransmisión deportiva). Redactor T05 § 9 (narración deportiva,
LE-CS 8.4) y T07 (cierres con música, 3.10).
**Lo que falta**: promociones (definición legal y criterio de la casa), programas (quién dirige el
montaje en Canal Sur), piezas culturales (música en el montaje), deportes (el resumen de 90 s y lo que
espera el espectador) y contenidos digitales (remito a tema 12). Fuentes: LGCA (BOE, vigente,
25-09-2026), LE-CS, CONV, MATEU.

### 6.1 Programas: quién dirige el montaje (CONV, anexo III, fichas)

- **Realizador** (código 5351000): función básica «Diseñar, coordinar, supervisar y dirigir la
  realización de los programas audiovisuales.»; tarea: «Dirigir las tareas de montaje, postproducción
  y mezclas hasta su completo acabado.» y «controlar la calidad y duración de los mismos».
- **Ayudante de Realización** (5353000): «Realizar reportajes, bloques, microespacios,
  postproducciones y promociones de programas, bajo las directrices del Realizador.» y «Coordinar las
  tareas de montaje, postproducción y mezclas hasta el acabado del programa.»
- **Encargado Operación y Montaje Vídeo** (5212204, p. 127 del BOJA): «Realizar la edición y
  postproducción de reportajes, programas, y otros elementos audiovisuales con criterios técnicos y
  artísticos.»; tareas: «Realizar el montaje y postproducción de reportajes, programas y otros
  elementos audiovisuales.» «Realizar el control técnico y/o calidad aplicando las posibles
  correcciones para su correcta emisión o venta.» «Proponer al responsable del departamento nuevas
  formas de trabajo… y aportar soluciones técnicas y estéticas para mejorar la calidad del montaje.»
- **Operador Montador de Vídeo** (5212206, p. 190): ficha completa en tema 9.2 abajo; para programas,
  la tarea «Grabar, emitir y reproducir videos para programas en todo tipo de eventos y producciones
  con selección alternativa a la realización.»
- Música en programas: **Ambientador Musical** (5354000): «Seleccionar / montar estéticamente la música
  adecuada a cada escena o secuencia que lo precise, considerando la unidad de conjunto y la expresión
  conceptual de cada montaje.»; «Realizar la elección de sintonías, ráfagas, cortinillas, fondos y
  efectos musicales.»
- Montaje de programa frente a noticia: reportaje con «libertad de elaboración y montaje» (LE-CS 3.4,
  tema 1.7); «en formatos más extensos, estos recursos [música, etc.] deben manejarse con matices»
  (9.2.12.4). No hay en LE-CS pauta de montaje para programas de entretenimiento: **no consta**.

### 6.2 Promociones

- Definición legal — LGCA art. 127.1 (vigente, redacción única de 9-7-2022; leído con
  `boe.py precepto` el 25-09-2026): «Se considera autopromoción la comunicación comercial audiovisual
  que informa sobre el servicio de comunicación audiovisual, la programación, el contenido del
  catálogo del prestador del servicio de comunicación audiovisual, … sobre programas, o paquetes de
  programación determinados, funcionalidades del propio servicio de comunicación audiovisual o sobre
  productos accesorios derivados directamente de ellos o de los programas y servicios de comunicación
  audiovisual procedentes de otras entidades pertenecientes al mismo grupo empresarial audiovisual.»
- Art. 127.2: «Los mensajes audiovisuales o locuciones verbales ajenos a la programación o a los
  productos accesorios directamente derivados de programas incluidos en las autopromociones se
  considerarán anuncios publicitarios a todos los efectos.» → aplicación al montador: meter en una
  promo un mensaje ajeno la convierte en publicidad.
- Art. 137.2.b: la **autopromoción** se excluye del cómputo de los límites de 144 min (6-18 h) y
  72 min (18-24 h) de comunicaciones comerciales (137.1.a y b). (Si el tema del común sobre la
  LGCA ya lo desarrolla, copiar de allí.)
- Criterio de la casa, LE-CS 9.10.1 «Vídeos promocionales» (p. 167): «Está prohibido montar y emitir
  un vídeo informativo que tenga, en origen, una connotación promocional con el mismo material
  audiovisual de la inserción publicitaria convencional, y más aún hacerlo con idéntico orden,
  estructura y formato, o de manera tan similar que induzca a confusión. Sólo podrá usarse como un
  recurso y, aún así, de manera parcial y limitada. Si estamos obligados a diferenciar el dato de la
  opinión, también debemos diferenciar ante el espectador lo que es información de lo que es
  mercadotecnia.» Y (p. 168): «Es admisible la emisión de un vídeo que tenga un carácter de creación
  artística aunque su intención sea comercial. Lo más adecuado es ubicarlo al final del informativo, a
  modo de cierre, y sin referencia alguna en titulares.» No está en Redactor/a (grep «connotación promocional» sin resultado): **nuevo**.
- Separación (LE-CS 9.10, p. 167): «La inserción de publicidad es ajena a la información y está
  separada de ésta por medios acústicos y ópticos.»
- Técnica de montaje de la promoción: MATEU 8.1-8.2 (spot: corte «preciso, al fotograma», «condensación
  temporal», «gancho»; tráiler de 1 a 2,5 min; *teaser*; *sneak peek*) — citado en tema 1.7.
- Duraciones estándar de promos de Canal Sur (20", 30"…): **no constan** en fuente publicada.

### 6.3 Piezas culturales

- Música en el montaje (LE-CS 3.2.2, ya en Redactor T07): sólo si la música es la noticia, «y siempre
  que no perturbe la narración, ni anule por completo el sonido natural».
- Cierres culturales (3.10, ya en Redactor T07): «Suelen tratarse de muestras de exposiciones,
  actuaciones musicales, segmentos de películas o espectáculos... En estos casos, contra la norma
  general de este LIBRO DE ESTILO, sí puede ser oportuna la inclusión de música adecuada para
  embellecer el montaje.»
- Grabación de actuaciones (5.4, p. 82): grabación específica del sonido, «incluso por los canales 1 y
  2 simultáneamente, en previsión de incluirlo en emisión como vídeo total», con la imagen con «un
  valor subalterno en el montaje final». Canal 1 de mesa de sonido si es «actuación musical, discurso
  político, ensayo general...».
- Campañas de promoción cultural (7.3.4 «Consumo», pp. 103-104): «a veces somos rehenes irreflexivos
  de campañas de promoción ligadas a estrenos de cine, novedades discográficas, espectáculos o
  lanzamientos editoriales… No podemos hurtar el hecho a los espectadores pero hay que evitar que
  nuestras informaciones se conviertan… en una repetición, palabra por palabra, de lo que idean
  redactores de publicidad y expertos en técnicas de mercado.»
- LE-CS no tiene sección de Cultura (índice cap. 7: Política, Economía, Sociedad, Local, Deportes):
  comprobado en el índice, pp. 98-109.
- Derechos de la música y de fragmentos de obras: tema 10 (no aquí).

### 6.4 Deportes

- Resumen informativo de acontecimientos en exclusiva — LGCA art. 144 (vigente, redacción única;
  `boe.py precepto` 25-09-2026):
  - 144.1: el titular del derecho exclusivo «permitirá a los prestadores del servicio de comunicación
    audiovisual la emisión de un breve resumen informativo en condiciones razonables, objetivas y no
    discriminatorias.»
  - 144.2: «se podrá emitir únicamente en noticiarios y programas de contenido informativo de
    actualidad.»
  - 144.3: «No será exigible contraprestación alguna cuando el resumen informativo sobre un
    acontecimiento, sobre un conjunto unitario de acontecimientos o sobre una competición deportiva se
    emita en noticiarios y programas de contenido informativo de actualidad, en diferido y con una
    duración inferior a noventa segundos. La excepción de contraprestación no incluye, sin embargo,
    los gastos técnicos necesarios para facilitar la elaboración del resumen informativo.»
  - 144.4: «deberá garantizarse la aparición permanente del logotipo o marca comercial de la entidad
    organizadora y del patrocinador principal de la competición.» → el montador no puede recortar ni
    tapar ese logotipo.
  - Salvedad: el art. 144 habla de «acontecimiento de interés general para la sociedad»; no comprobé
    si el fútbol profesional tiene además régimen propio (RDL 5/2015): **no confirmado**, no afirmarlo.
- Lo que espera el espectador (LE-CS 7.5.1, p. 106): «1. Referencia sobre lo sucedido… lo que busca es
  rememorar lo que ya ha visto, revisar lo que no ha captado o ratificarse en sus apreciaciones. 2.
  Datos novedosos y anécdotas… jugadas discutibles que no han sido aclaradas, lances del juego… 3. Algo
  de diversión y distracción, sobre todo si el resultado favorable lo permite.»
- Ecuanimidad (7.5.1, pp. 106-107): el deporte enfrenta a «dos grupos humanos que merecen un
  tratamiento ecuánime y respetuoso»; «Es exigible un relato sencillo, ceñido al material disponible y
  ajustado a la realidad.»
- Retransmisión (8.4, ya en Redactor T05): juicios apoyados en «repeticiones, tomas diferentes,
  ralentizaciones» (LE-CS l. 4274). EVS: RTVE edicion-montaje/08.

### 6.5 Contenidos digitales

- Formatos verticales, clips, miniaturas: son el **tema 12** de este mismo puesto; aquí basta remitir.
- Carta del Servicio Público 2024-2029 y Contrato-programa 2024-2026: hablan de presencia en redes y
  plataformas, pero no dan pautas de montaje (grep «montaje», «vertical»: sin resultado útil). **No
  consta** criterio de montaje digital publicado por la RTVA.

---

## Tema 9 · Coordinación con redacción, realización, producción, documentación, grafismo y sonido

**Lo que ya está**: Redactor/a T03 (cerrado): editor manda sobre el contenido (7.4), realizador
supeditado al editor (6.5) e información sobre técnica (6.5.1, frase), consultar antes de decidir,
entrega escalonada en cabinas, productores y editores (4.4), peticiones por escrito, directos
pactados con el «equipo de edición» (8.1.6), fichas de Redactor y Secretario/a de Redacción (este
último: «Recepción de rótulos y comunicación a Realización»; «Minutar la recepción de imágenes»),
y la disposición adicional segunda del convenio (cuatro Operadores/as Montadores/as en las
desconexiones). **Lo que falta**: la ficha del propio puesto, las fichas de los puestos con los que
coordina (realización, producción, documentación, grafismo, sonido, música) y los pasajes de LE-CS
sobre el montador y la delegación del realizador. Fuentes: CONV y LE-CS, leídas 25-09-2026.

### 9.1 El reparto en la cabina (LE-CS)

- Montador: «La opinión técnica y la participación activa del montador son esenciales, aunque el
  periodista haya previsto el ritmo de la narración, el orden de las secuencias y la prioridad
  informativa. Es conveniente que, en caso de duda, el redactor consulte al realizador los problemas
  técnicos y estéticos.» (6.3, p. 90) — nuevo (ver tema 5.1).
- Lo que el redactor debe traer a la cabina (cap. 6, p. 88; ya en Redactor T03): «los textos ajustados
  y revisados, con la imagen estudiada y minutada, con un mínimo esquema narrativo y, en su caso, con
  el material de archivo que pueda necesitar».
- Delegación del realizador (6.5.1, p. 93) — **nuevo** (grep «actúa por delegación» sin resultado en
  Redactor): «El realizador actúa por delegación en profesionales que asumen funciones concretas y
  criterios particulares en cada fase de elaboración de la noticia. Cada uno conoce los procedimientos
  básicos de su función, lo cual hace innecesario aplicar lo que sería ideal en una situación de
  medios ilimitados: la presencia constante de un realizador en cada fase del proceso. En resumen, su
  función se ciñe a la coordinación y supervisión de la parte final del mismo.»
- Urgencia y calidad (6.5.2, p. 93) — nuevo: «En la realización informativa, la urgencia acaba
  imponiéndose a cualquier otra consideración aunque no puede hacerlo hasta el punto de anular un
  aceptable nivel de calidad.» (sirve también para tema 14).
- Realizador en la emisión: «responsable máximo de la corrección de la imagen y de la calidad de la
  emisión del programa» (6.5, p. 92). No está en Redactor T03 (grep «responsable máximo»): nuevo.

### 9.2 Ficha del puesto (CONV, anexo III, código 5212206, BOJA 240/2014, p. 190) — nuevo

- Denominación en la ficha: «OPERADOR MONTADOR DE VIDEO» (en el anexo de grupos: «OPERADOR/A
  MONTADOR/A DE VÍDEO», nivel **B04**, que coincide con el B04 del enunciado).
- «OBJETO O FUNCIÓN BÁSICA DEL PUESTO»: «Realizar todo tipo de procesos de grabación, reproducción,
  manipulación, edición y postproducción de la señal de audio y video con criterios técnicos y
  artísticos, en coordinación con otras áreas.»
- «TAREAS MÁS SIGNIFICATIVAS DEL PUESTO»: «Editar y postproducir material audiovisual con criterios de
  narrativa audiovisual. Configurar sistemas de edición y preparar los materiales a utilizar. Recibir
  y enviar enlaces. Compactar para el archivo de material audiovisual. Realizar el control técnico de
  calidad y corregir video y audio para su emisión y/o venta. Etiquetar, grabar e introducir en base
  de datos, la información para la emisión automatizada de programas y bloques publicitarios. Grabar,
  emitir y reproducir videos para programas en todo tipo de eventos y producciones con selección
  alternativa a la realización. Repicar cintas orientadas a la producción, emisión y
  comercialización.»
- Cierre común: «La presente definición no constituye una lista cerrada de funciones, debiendo
  realizar el trabajador asimismo, todas aquellas tareas que, de acuerdo a su cualificación
  profesional, le sean encomendadas por su inmediato superior.»
- Superior funcional: **Encargado Operación y Montaje Vídeo** (5212204; en el art. 45.1, «ENCARGADO/A
  OP.MONTAJE VÍDEO», al final del bloque **NIVEL B03** de la p. 73 del BOJA; la p. 74 repite el rótulo
  «NIVEL B03» y sigue la lista. El Operador/a está en **B04**, p. 74). Tarea de ese puesto: «Informar al
  responsable del departamento de los trabajos realizados diariamente, así como de las incidencias.»
- Desconexiones provinciales (DA 2.ª, ya en Redactor T03): añadir lo que T03 no copia: las tareas son
  «Coordinación de los elementos técnicos y humanos que intervienen en la emisión del programa.»,
  la escaleta técnica y «Montaje de vídeos y Postproducción de titulares.»; los cuatro reciben
  «complemento de especial responsabilidad… en la cuantía del 30% de su salario base en tanto
  desempeñen dichas funciones»; y los que hagan funciones distintas de su puesto, «el complemento de
  polivalencia»; ambos «no consolidable[s]». (Vigencia de la DA hoy: la dice el tema común del
  convenio; en 2014 el texto dice «actualmente».)

### 9.3 Con quién coordina: las fichas vecinas (CONV, anexo III) — nuevo

| Área | Puesto (código) | Pasaje literal relevante para el montaje |
|---|---|---|
| Realización | Realizador (5351000) | «Dirigir las tareas de montaje, postproducción y mezclas hasta su completo acabado.» |
| Realización | Ayudante de Realización (5353000) | «Coordinar las tareas de montaje, postproducción y mezclas hasta el acabado del programa.» |
| Producción | Productor/a (5331000) | «Realizar la previsión de medios humanos y materiales necesarios para la creación de un programa en coordinación con el director y/o el realizador del mismo.» «Diseñar y elaborar el plan de trabajo en la realización de programas y supervisar su cumplimiento.» |
| Documentación | Documentalista (5213209) | Función: «Seleccionar, catalogar, clasificar, analizar, indizar, conservar y difundir la documentación escrita y audiovisual o sonora, fijada en cualquier soporte, y efectuar la recuperación de la información y de sus soportes.» Tareas: «Normalizar el lenguaje y mantener los tesauros y clasificaciones actualizados.» «Asesorar a los usuarios sobre las fuentes de información internas y externas…» |
| Documentación | Ayudante de Archivo y Documentación (5213213) | «Facilitar , conservar y difundir la información audiovisual o documental.» [sic]; «Comprobar, identificar, verificar (mediante visionado) y registrar los soportes…»; «Gestionar el préstamo y devolución de la documentación.» |
| Grafismo | Grafista (5345100) | «Diseñar y realizar y todo tipo de imagen gráfica para programas y postproducciones, y otros fines promocionales.» [sic]; «Realizar el asesoramiento estético a otras áreas como rotulación o postproducción.» |
| Sonido | Operador de Sonido de Televisión (5212207) | Función: «Definir, coordinar y realizar la captación, registro, edición, tratamiento y reproducción del sonido en producciones y postproducciones audiovisuales…»; «Analizar los objetivos y criterios establecidos en el guión técnico o escaleta, con el director o realizador.» |
| Música | Ambientador Musical (5354000) | «Seleccionar / montar estéticamente la música adecuada a cada escena o secuencia que lo precise…» |
| Redacción | Redactor | «Coordinar y participar en el montaje y grabación de las noticias.» (ya en Redactor T03) |

Observación para el tema: la **compactación para el archivo** es tarea del montador (su ficha); la
catalogación e indización, del Documentalista. Es la frontera que el test puede preguntar.

### 9.4 Coordinación con grafismo y rótulos (LE-CS)

- Rótulos: el redactor fija en escaleta «sus textos definitivos (incluidos los rótulos con su orden y
  ubicación precisa)» (6.1.2, p. 89; ya en Redactor T07). La escaleta recoge «rótulos» y «vías de
  sonido, coleo del vídeo» en los partes de emisión (6.1, p. 88; ya en Redactor T03/T07).
- Gráficos: «llevarán una 'cama' de audio por el canal correspondiente, salvo que se respete el sonido
  propio de la grabación» (3.16.2, p. 58; ya en Redactor T15). Mínimo 8 s y 4-5 elementos (3.16; ya).
- Archivo en rótulo: 9.9.1 (ya en Redactor T04).

### 9.5 Coordinación con producción (LE-CS 4.4)

- Ya en Redactor T03 (4.4, 4.4.1, 4.4.3, 4.4.4). Añadir sólo (4.4, p. 75): «Cada productor adscrito a
  un espacio informativo… participa en la toma de decisiones al lado del equipo de edición y tiene que
  estar avisado al instante de sus intenciones» (4.4, p. 75).

### 9.6 No confirmado (tema 9)

- Organigrama actual de Canal Sur (departamento de montaje, dependencia de Informativos o de
  Producción): no hay documento publicado localizado.

---

## Tema 14 · Gestión de urgencia informativa, directos, cambios de última hora y versionado

**Lo que ya está**: Redactor/a T10 (coberturas en directo: última hora, preparación, coordinación con
técnicos, continuidad) y T03 (directos pactados con el «equipo de edición», 8.1.6; cambios de
escaleta «desde el origen de la decisión, inmediata y simultáneamente» y nombre del vídeo, 6.1-6.1.1;
versiones «con un formato pactado» y pervivencia de 24 h, 3.15; pruritos locales y «La repetición de
un vídeo es una mala costumbre», 7.4.1). Redactor T07: párrafos finales cortables y encabalgados
(3.2.1), colas «suficientemente holgada[s]» para la última hora (3.9.1). RTVE edicion-montaje/08: EVS
(grabar y reproducir a la vez, playlist, PGM+PRV). **Lo que falta**: la urgencia vista desde la
realización (LE-CS 6.5.2), la edición mientras se ingesta (*growing files*), el versionado como
concepto de metadatos (EBUCore) y la protección del trabajo compartido bajo presión (ver tema 15).

### 14.1 Urgencia (LE-CS 6.5.2, p. 93) — nuevo

- «La imagen y su manufacturación están siempre al servicio de la eficacia, la accesibilidad y la
  claridad de la comunicación, aunque sea con limitación de medios técnicos y de tiempo. En la
  realización informativa, la urgencia acaba imponiéndose a cualquier otra consideración aunque no
  puede hacerlo hasta el punto de anular un aceptable nivel de calidad.»
- Imperfección técnica tolerable (6.5.1, p. 93; frase ya en Redactor T03): «cuando haya
  imperfecciones técnicas moderadas, la información —competencia del editor— tendrá preeminencia
  sobre la técnica —atribución del realizador—.» Añadir lo que T03 no copia: «En todo caso, el
  criterio que se aplique tendrá en consideración su operatividad.»
- Demoras (cap. 6, p. 87; ya en Redactor T03 en parte): «Una demora imprevista no puede poner nunca en
  peligro la elaboración, montaje y emisión de una noticia en las condiciones preestablecidas. Si hay
  novedades al respecto, hay que comunicarlas de inmediato para prever una solución.» No está en Redactor T03 (grep «demora imprevista»): **nueva**.
- Vídeo que no llega entero: la noticia se escribe para poder «emitirse incompleto» (3.2.1; en T07) y
  «Cuando una noticia relevante no pueda ser ofrecida completa en un informativo, las posteriores
  ediciones se ocuparán de su seguimiento» (cap. 6; en T03).
- Directo: el reportero no introduce «variaciones que no hayan sido pactadas previamente con el
  equipo de edición, salvo que no haya posibilidad de aviso y sólo cuando se trate de cuestiones
  urgentes y elementales. Las indicaciones previas del editor deben acatarse obligatoriamente.»
  (8.1, punto 3, p. 113). **Ya en Redactor T10** (l. 209): copiar de allí.

### 14.2 Editar mientras se graba (*growing files*, *edit while ingest*) — nuevo, fuente de fabricante secundaria

- Softron (fabricante de MovieRecorder), «HOW TO: Do Edit-While-Ingest with MovieRecorder and Avid
  Media Composer», actualizado 11-01-2024,
  https://softron.zendesk.com/hc/en-us/articles/115005092493 (leído 25-09-2026):
  «Edit-while-ingest (sometimes called FrameChase edit, or support for growing files)»; en su producto,
  sólo con «MXF destinations using the XDCAM codec»; «Media Composer requires you to manually
  'refresh' the file to see the new frames. It won't grow automatically with this method.»; orden
  del menú: «Clip > Refresh In-progress Linked Clips».
- Es documentación de un tercero sobre su propio producto, no de Avid: vale para definir el concepto
  («fichero que crece», se edita mientras se ingesta) y el nombre *frame chase*; **no** para afirmar
  en general qué formatos admite Media Composer.
- Adobe (Premiere Pro, preferencias de medios, opción de refresco automático de *growing files*):
  helpx.adobe.com respondió **403** por WebFetch y por curl (25-09-2026). **No confirmado**: no citar
  Premiere.
- EVS: la grabación y reproducción simultáneas ya están en RTVE edicion-montaje/08 § 1 («desde
  cualquier punto mientras sigue grabando»), también sin fuente de fabricante.

### 14.3 Versionado — nuevo

- Concepto de versión en metadatos — EBU Tech 3293, *EBUCore Metadata Set* v1.10 (Ginebra, abril
  2020; es la última versión publicada según https://tech.ebu.ch/publications/tech3293, consultado
  25-09-2026), 3.5 «How can I describe versions of programmes?» (pp. 18-19; copia local
  `fuentes/internet/EBU_Tech3293_EBUCore.txt`): «There can be many reasons why a programme is declared
  to be a version of a particular source (e.g. a shorter version, a different language, with or without
  captioning, but also available on different mediums such as a file, a tape, a disk).» «The best
  approach to identify versions is to use relations such as hasVersion or hasSource. The relation links
  two instances and their respective descriptions highlighting differences such as given above as
  examples.»
- Aplicación al montaje (oficio, decirlo así): cada versión (corta, sin locución, subtitulada, para
  desconexión, para redes) es un objeto distinto ligado a su fuente, no una sobrescritura del master.
- Versiones en la casa: 3.15 y 3.15.1 (ya en Redactor T03); cadena frente a desconexión (7.4.1, en T03).
  Nomenclatura en cadena (6.1.2, en T03/T07): «el envío a los Servicios Centrales debe identificarse con
  el nombre de la escaleta de cadena, independientemente del método interno que se use para ello.»
- Duplicar la secuencia antes de versionar: Avid, *Audio-Video Editing Workflows* (2010), paso de su
  flujo de exportación: «Duplicate the finished video sequence and name it appropriately. For example,
  Sequence_ForMix.» (p. 25); y crear carpetas de intercambio, «one labeled 'To Audio Editor' and the
  other 'From Audio Editor'» (p. 25). Es consejo del fabricante en otro contexto (entrega a Pro Tools):
  usarlo como apoyo.
- Media Composer (guía de 1999, abajo tema 15): bin de archivo «for keeping the original version of
  each cut (sequence)».

### 14.4 No confirmado (tema 14)

- Procedimiento interno de Canal Sur para piezas de última hora (quién pisa, tiempos de cierre de
  cabina): no publicado.
- Soporte real de *growing files* en el sistema de edición de Canal Sur (no consta qué sistema usa).

---

## Tema 15 · Organización de proyectos, nomenclatura, trazabilidad y buenas prácticas colaborativas

**Lo que ya está**: RTVE edicion-montaje/07 § 3 (vistas del bin: Text, Frame, Script), § 10 (Dupe
Detection, Dynamic Relink). Redactor T03 (nombre del vídeo en escaleta, 6.1.1; cadena, 6.1.2).
**Lo que falta**: organización de bins con fuente de fabricante (RTVE declara que **no consultó**
la documentación de Avid: § 12), trabajo compartido (bloqueo de bins), copias de seguridad del
proyecto, nomenclatura de la casa y trazabilidad (identificadores). Fuentes: Avid (3 documentos),
LE-CS, EBU, SMPTE.

Documentos de Avid descargados de resources.avid.com el 25-09-2026 (copias en
`fuentes/fabricantes/`, ver «Ficheros tocados»):
- **MC-UG-1999**: *Avid Media Composer User's Guide*, Release 8.0 for the Macintosh, Part
  0130-04015-01 Rev. A, May 1999, https://resources.avid.com/SupportFiles/attach/MC_UserGuide.pdf .
  **Antigua** (1999): vale para principios de organización, no para menús actuales.
- **MC-WN-23.3**: *What's New for Avid Media Composer v2023.3*,
  https://resources.avid.com/SupportFiles/attach/WhatsNew_MediaComposer_v23.3.pdf
- **MC-WN-22.10**: *What's New in Media Composer v2022.10*,
  https://resources.avid.com/SupportFiles/attach/WhatsNew_MediaComposer_v22.10.pdf
- **AV-WF-2010**: *Avid Audio-Video Editing Workflows*, © 2010,
  https://resources.avid.com/supportfiles/attach/AudioVideo_Editing_Workflows.pdf

### 15.1 Organización del proyecto y de los bins (MC-UG-1999, «Managing Folders and Bins», pp. 72-73)

- «You can use the Project window to create hierarchies of folders and bins that reflect the specific
  workflow of the current project. This structure should provide both simplicity and backup security.»
- «Limit the number of sequences you create in each project. For instance, consider creating one new
  project for each show, episode, spot, or scene.»
- «Limit the number and complexity of clips in each bin by creating and organizing bins in three
  groups»: (1) «a set of bins for the digitizing stage», p. ej. «one bin for each source tape to be
  digitized to avoid slowing the system with large bins and causing confusion between tapes»;
  (2) «a second set of bins for organizing your project», p. ej. «a separate bin for each segment of a
  video project»; (3) «a third set of bins for the editing stage, including: A current cut bin for
  storing each work in progress (sequence) An archive bin for keeping the original version of each
  cut (sequence) A selects or storyboard bin for screening selected clips or cuts gathered from the
  source bins A format cuts bin for storing the final cuts with added format elements such as segment
  breaks, color bars and tone, slate, or countdown».
- Vistas del bin (confirma RTVE § 3 con fuente de fabricante): índice de MC-UG-1999: «Using Text View»
  (p. 287), «Using Frame View» (p. 306), «Using Script View» (p. 310).
- Copia de seguridad automática — la carpeta **Attic** («Retrieving Bin Files from the Attic Folder»,
  pp. 35-36): «The Attic folder… contains backup files of each bin in a project.»; se recurre a ella
  «When you want to replace current changes to a sequence or clip with a previous version» y «When the
  current bin file becomes corrupt»; «The system adds the file name extension .bak plus a version
  number to the bin name. The bin file with the highest version number represents the latest copy of
  the bin file.» Aviso: ubicación y extensión son de 1999; en versiones actuales **no comprobado**.

### 15.2 Trabajo colaborativo: bloqueo de bins (Avid) — nuevo

- MC-WN-23.3 (p. 2): «When you lock a shared project bin in Media Composer, it prevents other users
  from making changes to that bin. With the new "Protect Project Bin" command, which is accessed by
  right-clicking on a shared bin icon in the Bin Container, the bin is made read only for all users,
  even for the user protecting it. Owners of a locked bin ("Lock Project Bin") see a green bin icon.
  However, when a user chooses to "Protect Project Bin", it will appear red, even for that user, and
  will always open as locked. Once the bin is closed, the user who originated the "Protect Project Bin"
  command can choose to "Unlock Project Bin" using the same context menu.»
- MC-WN-22.10: en entorno NEXIS | EDGE proxy, «By default, for a locked bin, the bin lock icon color
  will appear red until you do a manual refresh… which updates the bin status and changes the icon
  color to yellow if the bin has been modified.» (detalle de versión: no llevarlo al test).
- Mecánica general (fuente **secundaria**, proveedor de almacenamiento ELEMENTS, Filip Milovanovic,
  24-01-2023, https://elements.tv/blog/bin-locking-overview-and-troubleshooting-in-avid-media-composer/ ,
  leído 25-09-2026 vía WebFetch, citas resumidas por la herramienta: **releer antes de copiar literal**):
  «Avid Bin Locking functions work on a first come, first served basis.»; el primero que abre el bin
  tiene escritura; «A green padlock symbol inside the bin indicates that the user has write access»,
  candado rojo = sólo lectura; se crea un fichero **.lck** al abrir el bin; «To use Avid Bin Locking,
  the storage that the project and the media files are stored on must support this feature.»
- Compartir entre versiones del programa (Avid Knowledge Base, «Precautions when sharing projects and
  bins between different versions of Avid Media Composer», act. 11-08-2023,
  https://kb.avid.com/pkb/articles/en_US/user_guide/en275293 ; vía WebFetch): comprobar compatibilidad
  de versiones, plug-ins y efectos; «Users will need to have access to all of the media files that are
  used in the project»; «Always create a backup of your projects and bins». (Resumen de herramienta:
  releer antes de copiar literal.)

### 15.3 Nomenclatura (LE-CS; casa)

- Ya en Redactor T03 (l. 288) y T07: 6.1.1 «Son inadmisibles los cambios en la identificación de un
  vídeo por la confusión y los errores que causan. El nombre de una noticia en escaleta debe respetarse
  por obligación.»; si el vídeo se terminó antes de la escaleta, «es el equipo de edición quien está
  obligado a trasladar a la misma el nombre asignado por el autor del trabajo o, en su caso,
  adaptarlo.» (6.1.1, p. 88). **Es la regla de nomenclatura de la casa que obliga al montador.**
- 6.1.2 (cadena), ver 14.3.
- Convención concreta de nombres de ficheros o clips en Canal Sur: **no publicada**.
- Código de tiempo como referencia compartida (LE-CS 5.3.3): ver tema 5.2 («sobre todo cuando el
  material va a ser usado por terceras personas»).

### 15.4 Trazabilidad: identificadores y relaciones — nuevo

- UMID — SMPTE ST 377-1:2019 (MXF), cláusula de definiciones (copia local
  `fuentes/archivos/SMPTE_ST377-1_MXF.txt`, descargada 02-09-2026): «UMID: Unique Material ID
  according to SMPTE ST 330. When used as a Package ID, only the 32-byte long Basic UMID shall be
  used.»; «Package ID: A basic UMID to uniquely identify a Package». Referencia normativa citada:
  «SMPTE ST 330:2011, Unique Material Identifier (UMID)». (ST 330 no leída: no dar su contenido.)
- Relaciones de versión/fuente — EBUCore 3.5 (`hasVersion`, `hasSource`), ver 14.3.
- Intercambio con sonido (AV-WF-2010, pp. 11 y 18-19): «The key to maintaining a high level of
  interoperability between Media Composer and Pro Tools is to use an AAF file.»; «AAF (Advanced
  Authoring Format) and OMF (Open Media Framework) are the two main industry-standard formats that you
  can use to exchange compositions and media between different applications and platforms.»; el
  fichero lleva «the editing information (metadata) for the selected sequence»; metáfora: «media files
  are the pieces of a puzzle and metadata is the set of instructions for assembling the puzzle.»;
  «AAF is a more comprehensive standard of exchange and amongst many other media formats, it can also
  embed/refer to MXF media files which the OMF format cannot.» Sirve para tema 9 (sonido) y 15.
- Metadatos, MAM y archivo en detalle: temas 8 y 13 de este puesto (otro bloque).

### 15.5 No confirmado (tema 15)

- Sistema de edición y almacenamiento compartido de Canal Sur: no consta en documento publicado.
- Ubicación actual de la carpeta Attic y comportamiento de copias en Media Composer vigente.
- El resto de la guía de Media Composer actual (*Editing Guide* 2024-2025): tres URLs probadas en
  resources.avid.com dieron 404; no localizada.

---

## Ficheros tocados

- Creado: `informes/canal-sur-especificos/30-investigacion-B-montaje.md` (este).
- Creados (fuentes): `fuentes/montaje/UMH_Mateu-2024_fundamentos-edicion-montaje.{pdf,txt}`,
  `fuentes/fabricantes/Avid_Audio-Video-Editing-Workflows-2010.{pdf,txt}`,
  `fuentes/fabricantes/Avid_Media-Composer-User-Guide-R8-1999.txt` (sólo texto; el PDF pesa 13 MB),
  `fuentes/fabricantes/WhatsNew_MediaComposer_v23.3.{pdf,txt}`,
  `fuentes/fabricantes/WhatsNew_MediaComposer_v22.10.{pdf,txt}`.
- Nada más. No se ha tocado ningún tema.
