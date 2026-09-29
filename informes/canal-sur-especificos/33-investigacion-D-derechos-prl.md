# Realizador/a (puesto 33) · Investigación del bloque D-derechos-prl (temas 16, 17, 19)

Fase 1. Fecha de trabajo: 24-09-2026 (fecha del encargo); las fuentes nuevas se descargaron y leyeron el
29-09-2026 (fecha del sistema), y así se declara junto a cada una. El texto consolidado del BOE se leyó con
`boe.py` («vigente hoy» = 29-09-2026). Aquí va sólo lo que falta sobre lo reutilizable que ya está localizado
en el encargo; el redactor copia esos ficheros aparte. Traducción entre paréntesis, en redonda.

## 0. Pasajes cerrados de otros puestos de Canal Sur que cubren huecos (copiables literal)

Además de los que da el encargo, hay en el repositorio temas **cerrados y verificados** de Canal Sur que
cubren buena parte del enunciado de estos tres temas. Se copian igual que los del encargo:

| Tema 33 | Fichero cerrado | Pasajes útiles |
|---|---|---|
| 16 | `temas/canal-sur-especificos/08-camara-operador/16-accesibilidad-y-diversidad-en-la-representacion-visual.md` | § 1 «Qué pide la accesibilidad a quien maneja la cámara»; § 2 entero (LGCA arts. 4, 6 y 7; LO 3/2007; Ley 4/2017 art. 67; **Guía del CAA 2025**; Libro de estilo sobre discapacidad, inmigración y minorías; «El plano: cómo se traduce en la cámara»); § 3 (diversidad territorial) |
| 16 | `temas/canal-sur-especificos/08-camara-operador/12-derechos-de-imagen-privacidad-menores-victimas.md` | § 3 Menores; § 4 Víctimas (con LO 1/2004 art. 14, **«especial cuidado en el tratamiento gráfico de las informaciones»**); § 6 «Uso ético de imágenes sensibles» (Libro de estilo 9.9, 9.9.1, 9.9.2; sucesos, suicidio, catástrofes) |
| 16 | `temas/canal-sur-especificos/34-redactor-a/11-materias-sensibles.md` | § 2 Violencia de género (LO 1/2004, Ley 13/2007 andaluza, Ley 12/2007 arts. 57-58, Libro de estilo 9.2); § 4 Discapacidad |
| 17 | `temas/canal-sur-especificos/08-camara-operador/12-...md` | § 1 (LO 1/1982) ya está también en 30/10 |
| 19 | `temas/canal-sur-especificos/28-operador-a-de-sonido/16-prevencion-riesgos-laborales.md` | «El ruido: el Real Decreto 286/2006»; «Auriculares, monitores y sala de control: lo que dice el INSST» (intercom, auriculares monoaurales, sala de control); «Cargas, cables y exteriores» |
| 19 | `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/16-prevencion-riesgos-laborales.md` | «La sala de edición: visionado crítico, varias pantallas y ratón» (UIT-R BT.2100-3 cuadro 3; varias pantallas; TME; RD 1299/2006; convenio art. 29.4 y 29.6) — sirve para el control de realización y la postproducción que dirige el realizador |
| 19 | `temas/canal-sur-especificos/08-camara-operador/17-prevencion-riesgos-laborales.md` | «Ruido y riesgo eléctrico» (plató) |

Con eso y lo que da el encargo (30/10, 30/11, 34/17, común 09, 32/15) queda cubierto casi todo. Lo que
sigue es sólo lo propio del realizador.

---

## Tema 16 · Accesibilidad y responsabilidad editorial en la realización

Falta sobre lo reutilizable: (a) la **lengua de signos** como norma propia (Ley 27/2007 y Ley andaluza
11/2011) y, sobre todo, **cómo se realiza** la lengua de signos (composición, tamaño, encuadre, luz,
vestuario, fondo), que 08/16 declara hueco («Qué superficie de la imagen ocupan el subtítulo o la ventana
del intérprete de signos no lo fija ninguna norma leída»); (b) un criterio técnico de **tratamiento
responsable de imágenes** propio de realización: la **fotosensibilidad** (UIT-R BT.1702).

### 16.1 Ley 27/2007, de lenguas de signos (BOE-A-2007-18476)

Fuente: texto consolidado BOE, leído con `boe.py` el 29-09-2026.

- **Art. 14** (redacción vigente desde 03-08-2011, dada por BOE-A-2011-13241; dos redacciones, la cadena la
  da `boe.py`). Rúbrica: **«Medios de comunicación social, telecomunicaciones y sociedad de la información.»**
  14.1: **«Los poderes públicos garantizarán las medidas necesarias para que los medios de comunicación
  social, de conformidad con lo previsto en su regulación específica, sean accesibles a las personas sordas,
  con discapacidad auditiva y sordociegas mediante la incorporación de las lenguas de signos españolas.»**
  14.2: **«Asimismo, los poderes públicos adoptarán las medidas necesarias para que las campañas de
  publicidad institucionales y los distintos soportes audiovisuales en los que éstas se pongan a
  disposición del público sean accesibles a estas personas.»** 14.6: **«Los mensajes relativos a la
  declaración de estados de alarma, excepción y sitio, así como los mensajes institucionales deberán ser
  plenamente accesibles a todas las personas sordas, con discapacidad auditiva y sordociegas.»**
  Ojo (error 4): 14.1 es «garantizarán» (poderes públicos), no obligación directa del medio.
- **Art. 23** (redacción original, vigente desde 25-10-2007), misma rúbrica, para los **medios de apoyo a la
  comunicación oral**: 23.1 **«Los poderes públicos promoverán las medidas necesarias para que los medios de
  comunicación social de titularidad pública o con carácter de servicio público, de conformidad con lo
  previsto en su regulación específica sean accesibles a las personas sordas, con discapacidad auditiva y
  sordociegas a través de medios de apoyo a la comunicación oral.»** 23.2: campañas institucionales
  accesibles **«mediante la incorporación del subtitulado»**. Contraste para el test: art. 14 (lengua de
  signos) **«garantizarán»**; art. 23 (apoyo oral: subtitulado) **«promoverán»**.
- **Art. 4.i)** (original): **«Intérprete de lengua de signos: Profesional que interpreta y traduce la
  información de la lengua de signos a la lengua oral y escrita y viceversa con el fin de asegurar la
  comunicación entre las personas sordas, con discapacidad auditiva y sordociegas, que sean usuarias de esta
  lengua, y su entorno social.»** 4.c) define **medios de apoyo a la comunicación oral** (**«aquellos
  códigos y medios de comunicación, así como los recursos tecnológicos y ayudas técnicas usados por las
  personas sordas…»**).
- Art. 22.1 (original), participación política: informaciones institucionales y **«programas de emisión
  gratuita y obligatoria en los medios de comunicación, de acuerdo con la legislación electoral y
  sindical»** plenamente accesibles **«mediante su emisión o distribución a través de medios de apoyo a la
  comunicación oral»** (útil: espacios electorales gratuitos que realiza la casa).

### 16.2 Ley 11/2011 de Andalucía, de lengua de signos española (BOE-A-2011-20375)

Ley 11/2011, de 5 de diciembre, por la que se regula el uso de la lengua de signos española y los medios de
apoyo a la comunicación oral de las personas sordas, con discapacidad auditiva y con sordoceguera en
Andalucía (BOE núm. 312, de 28-12-2011). Consolidado BOE leído el 29-09-2026: **una sola redacción**,
aplicable desde 15-01-2012. La cita la Ley 4/2017 andaluza (preámbulo y art. que remite a ella, en
`fuentes/canal-sur/BOE-A-2017-11910.md`, l. 35 y 163).

- **Art. 16.1**: **«Las Administraciones Públicas andaluzas garantizarán las medidas necesarias para que los
  medios de comunicación social, de conformidad con lo previsto en su regulación específica, sean
  accesibles a las personas sordas, con discapacidad auditiva y con sordoceguera, usuarias de la LSE y de
  la lengua oral.»**
- Art. 16.3, párrafo segundo: **«Se fomentará el desarrollo de soportes audiovisuales, como materiales
  didácticos y de difusión e información que incluyan la LSE, la subtitulación y la audiodescripción con
  objeto de facilitar el acceso y la accesibilidad en la Sociedad de la Información y del Conocimiento.»**
- Art. 16.4 (eventos): en congresos, jornadas y eventos organizados o subvencionados por las
  Administraciones andaluzas **«se garantizarán las condiciones técnicas adecuadas para el desempeño de los
  puestos de interpretación y guía-interpretación»**.
- Definiciones del **art. 5**: **«n) Subtitulado: Recurso de apoyo a la comunicación oral que transcribe a
  texto el mensaje hablado, garantizando el máximo acceso a la información de la persona sorda, con
  discapacidad auditiva o con sordoceguera.»**; **«ñ) Audiodescripción: Servicio de apoyo a la comunicación
  audiovisual consistente en un conjunto de técnicas y habilidades aplicadas para compensar la carencia de
  captación de la parte visual de un contenido audiovisual suministrando a las personas con discapacidad
  visual una adecuada información sonora por medio de la traducción, explicación o narración de los
  elementos visuales relevantes, con objeto de que perciban dicho contenido como un todo armónico y de la
  forma más aproximada p[osible]…»** (la línea viene cortada en la extracción; el redactor debe cerrar la
  cita con `boe.py precepto BOE-A-2011-20375 a5`). 5.h) intérprete de LSE y **teleintérprete**.
- Ninguna norma de la Ley 11/2011 fija cuotas para la RTVA: las cuotas son de la LGCA y la LAA (ya en 30/11 y 34/17).

### 16.3 Cómo se realiza la lengua de signos: Guía CNLSE (2017)

Fuente: Real Patronato sobre Discapacidad – Centro de Normalización Lingüística de la Lengua de Signos
Española (CNLSE), *Guía de buenas prácticas para la incorporación de la lengua de signos española en
televisión*, © Real Patronato sobre Discapacidad, 2017, NIPO 689-17-006-0; PDF en
https://cendocps.carm.es/documentacion/2017_Guia_incorporacion_lengua_signos_television.pdf (descargado y
leído el 29-09-2026; ficha en cnlse.es: año 2017, sin noticia de edición posterior). **Guía de buenas
prácticas, no norma.** En el grupo de trabajo figura la **Federación de Organismos de Radio y Televisión
Autonómicos** (FORTA; Alberto J. Marcos Calvo) y RTVE. Las siglas de la guía son **CNLSE** (el tema 30/11
escribe «CNSLE»; la LGCA art. 101 dice «Centro de Normalización Lingüística de la Lengua de Signos
Española»: el redactor debe unificar la sigla según la fuente que cite).

**Modalidades (cap. 5)**, según el *Informe sobre la presencia de la lengua de signos española en la
televisión* (CNLSE, 2015): **«(a) Copresentación en lengua de signos española, b) Lengua de signos española
insertada en la imagen con audio y c) Lengua de signos como imagen principal)»**. La insertada se hace como
**«Silueta de la persona que signa»** (5.3.1: **«la persona que signa se recorta contra el fondo»**,
**«Esta modalidad requiere la utilización de la técnica de croma o chroma-key»**) o **«Lengua de signos en
una ventana»** (5.3.2). Preferencia de usuarios (introducción): **«la preferencia por la silueta del
intérprete frente a la ventana»**. Copresentación (5.1): **«no se emplea en la actualidad en España»**;
**«puede resolver las necesidades de accesibilidad en espacios que puntualmente lo precisen, por ejemplo si
hay invitadas personas sordas o sordociegas usuarias de la lengua de signos al programa en entrevistas,
coloquios o concursos»**.

**Recomendaciones generales (6.1)**, literales:
- **«El servicio de interpretación en lengua de signos debe ser configurable, esto es, cada persona usuaria
  debe poder elegir la apariencia gráfica del servicio, así como activarlo y desactivarlo, en la medida en
  que las posibilidades tecnológicas lo permitan.»**
- **«Si un programa se ha ofrecido con lengua de signos en su emisión lineal en televisión, el servicio de
  lengua de signos debe preservarse en futuras formas de explotación del contenido»** (a la carta, HbbTV).
- **«De incluirse también el servicio de subtitulado en el programa, el subtitulado y la lengua de signos
  deben distribuirse en la pantalla de forma que no se interfieran entre ellos.»** y **«el subtitulado y el
  signado no son incompatibles entre sí, lo más recomendable es que compartan espacio en la pantalla, en
  ningún caso uno puede sustituir al otro.»**
- Sincronía: la señal de signos y el audio **«deben estar aproximadamente sincronizadas»**; la
  interpretación simultánea **«se caracteriza por un desfase»**.

**Recomendaciones técnicas (6.2)**:
- **«La adquisición y el procesamiento de la señal de vídeo deben preservar el contraste entre el color de
  piel de la persona que signa y su ropa, así como con el fondo.»**
- Luz y obturación (croma): **«una correcta iluminación del set de grabación con al menos cinco puntos de
  luz (dos para el fondo chroma y tres para la persona que signa)»**; **«unos valores de velocidad de
  obturación inferiores a 1/125 s suelen resultar adecuados, si bien es recomendable un valor de 1/250 s»**
  (para evitar el desenfoque de manos y el derrame verde del croma); **«Para compensar la pérdida de luz
  debida a una obturación con menor tiempo de apertura se puede modificar la apertura del iris»**.
- **«es recomendable utilizar formatos progresivos en lugar de formatos entrelazados»**.
- **«La composición del vídeo del programa y de la lengua de signos debe tener en cuenta las precauciones
  habituales relacionadas con los márgenes de seguridad»** (enlaza con EBU R 95, ya en el informe B).

**Composición (6.3.1)** — el dato que falta en 08/16:
- **«no es sencillo establecer un tamaño mínimo por defecto para la persona que signa que sea válido en
  cualquier circunstancia, si bien algunos documentos como el informe de CENELEC y las directrices de
  provisión de servicios de accesibilidad de Ofcom establecen un tamaño mínimo de 1/6 de la pantalla.»**
- Universidad Politécnica de Madrid (Conti, 2009): en definición estándar la ventana **«habría de ser de al
  menos 1/3 del total»** de columnas; **«Estas dimensiones pueden ser algo menores en el caso de la TV de
  alta definición (formatos 720p y 1080i) y situarse en 1/4 parte de las columnas.»**
- **«Se recomienda que el servicio de lengua de signos se incorpore en la parte izquierda de la pantalla, de
  no ser posible la personalización, de acuerdo con las preferencias mostradas de los usuarios.»**
- **«Las personas sordociegas pueden requerir un tamaño mayor de la persona que signa y una ventana cuyo
  fondo sea liso y de color oscuro»**.
- **«Se recomienda hacer desaparecer la figura del signante mientras no haya contenido verbal que traducir»**.
- **«Observar escrupulosamente que ningún detalle ni del grafismo, mosca, simbología, señalética, invada el
  espacio reservado a la lengua de signos. En este sentido, tanto el subtitulado como el signado ocuparán
  espacios diferenciados.»**
- **«Tener en cuenta que ambas ventanas (signado y contenido) se ubiquen a la misma altura»**.
- Tamaño según CENELEC (2003), citado por la guía: suficiente para **«mostrar todos los movimientos del
  tronco, los brazos, las manos, los dedos, los hombros y el cuello, así como todos los movimientos y
  expresiones faciales»** y **«permitir la lectura labial»**.

**Apariencia (6.3.2)**: ropa de **«alto contraste con su color de piel»**, **«color y una textura
uniformes»**, sin **«líneas finas muy juntas»** (efectos en la señal), **«no debe llevar joyas»**; para
sordociegos, **«ropa de color oscuro»**.

**Puesta en escena (6.3.3)** — lo más de realizador:
- Fondo **«liso y homogéneo, ofrecer un buen contraste con el color de la piel de la persona que signa y no
  resultar brillante»**; para sordociegos **«preferentemente de un tono azul oscuro»**.
- El intérprete **«debería contar con una visión completa del conjunto (…), monitores de apoyo, una señal de
  audio de calidad y algún sistema de comunicación visual o sonoro para sincronizar la lengua de signos»**;
  **«debe poder estar en contacto con el personal técnico antes y durante el signado»**; **«en programas con
  interpretación de lengua de signos en directo la realización debe tener en cuenta la demora que se produce
  en la interpretación»**.
- Encuadre: **«El encuadre debe coincidir con el espacio sígnico (…): en la parte superior necesita un palmo
  de aire por encima de la cabeza, en los laterales, espacio suficiente como para que quepan los brazos
  flexionados por el codo, y en la parte inferior el límite podría ser la altura en la que se colocan los
  bolsillos (un plano medio largo).»**
- **«Se recomienda un plano frontal, con la cámara a la altura de los ojos de la persona que signa.»** El
  semiperfil **«hace que se superpongan las manos, disminuyendo la inteligibilidad para las personas
  sordociegas»**.
- Luz: **«sin exceso de luz»**; evitar **«sombras en el rostro de la persona que signa cuando sus manos
  cruzan por delante de él»** y **«sombras en el fondo»**.

**Señalización (6.4)**: los programas con lengua de signos **«deben estar convenientemente identificados»**
en pantalla, teletexto, miniguías y EPG; la guía propone un icono (figura 32).

No confirmado: las directrices vigentes de Ofcom (el PDF de Ofcom devolvió **403** el 29-09-2026) y el
informe CENELEC 2003; el «1/6» se cita **sólo como lo recoge la guía CNLSE**, no de primera mano. Cómo
incorpora Canal Sur la LSE (silueta o ventana, lado, tamaño): **no consta en documento publicado leído**.

### 16.4 Tratamiento responsable de imágenes: fotosensibilidad (UIT-R BT.1702-3)

Fuente: Recomendación UIT-R BT.1702-3 (11/2023), *Directrices para reducir el riesgo de ataques de epilepsia
fotosensible causados por la televisión*, versión española, https://www.itu.int/rec/R-REC-BT.1702/en
(la página la marca **«In force»**; las -0, -1 y -2 **«Superseded»**), PDF descargado y leído el
29-09-2026. Recomendación, no norma obligatoria. Historial: **(2005-2018-2019-2023)**.

- Cometido: **«Se solicita a las organizaciones de radiodifusión que sensibilicen a los productores de
  programas sobre los riesgos que supone crear contenido de imágenes de televisión que puedan ocasionar
  ataques de epilepsia fotosensible en televidentes susceptibles a este tipo de imágenes.»**
- Considerando f): **«en el caso de alguna programación en directo, tales como los telediarios, a menudo la
  producción del programa escapa al control del radiodifusor»**; g) **«no se puede erradicar completamente
  el riesgo»**.
- **Directriz 1 (imágenes parpadeantes)**: **«Cuando la luminancia en pantalla de la imagen más oscura es
  inferior a 160 cd/m2, se produce una secuencia de intermitencias potencialmente peligrosas cuando hay una
  diferencia igual o superior a 20 cd/m2 entre la luminancia en pantalla de la imagen más oscura y más
  brillante»** (SDR y HDR); por encima de 160 cd/m², criterio de **«1/17 del contraste Michelson»** (sólo HDR).
  **«Independientemente de la luminancia, la transición al rojo saturado o desde ese color también es
  potencialmente peligrosa.»**
- **«Se permiten intermitencias aisladas sencillas, dobles o triples, pero no se permiten secuencias de
  intermitencias cuando»** **«el área de intermitencias combinadas que se producen simultáneamente ocupa más
  de un 25% de la pantalla»** **«y»** **«hay más de tres intermitencias (es decir, seis cambios de luminancia
  (…)) en el lapso de un segundo»**; separación aceptada **«360 ms o más (…) en un entorno de 50 Hz»**.
  Ojo: las dos condiciones van unidas por «y».
- Montaje: **«Las secuencias de imágenes que cambian rápidamente (por ejemplo, los cortes rápidos) pueden
  causar ataques si se producen en zonas de pantalla intermitentes, en cuyo caso se aplican las mismas
  restricciones que a las intermitencias.»** Y **«una secuencia de imágenes intermitentes que dura más de
  cinco segundos podría constituir un riesgo aun cuando sea conforme con las directrices»**.
- **Directriz 2 (imágenes estáticas)**: **«cuando una imagen contiene pares claros y oscuros de rayas
  claramente discernibles en cualquier orientación»**; **«Si las rayas cambian de dirección, oscilan,
  parpadean o invierten su contraste, es más probable que sean nocivas que si son fijas.»**
- Nota 5: **«La utilización de analizadores automáticos de señales de vídeo puede ser útil para alertar al
  personal de producción»**. Nota 3: SDR con blanco a **200 cd/m2**, HLG a **1 000 cd/m2**.
- Anexo 2: ejemplos reales: **«los destellos de los flashes de los fotógrafos o las luces estroboscópicas en
  una discoteca»**; objetivo: **«ayudar a los productores de programas a evitar la creación involuntaria de
  efectos de vídeo»**.
- Anexo 5: **«los niños y los jóvenes menores de 20 años constituyen la población más propensa»**; consejo al
  espectador: **«un cuarto bien iluminado y a una distancia de al menos dos metros»**.

Aplicación (lectura de oficio, no de la norma): ruedas de prensa con flashes, conciertos con estroboscopios,
transiciones y grafismo con destellos, promociones con cortes muy rápidos. Si Canal Sur exige BT.1702 en sus
entregas o usa analizador (tipo «Harding»): **no consta**. Normativa española que remita a BT.1702: **no
localizada**; no afirmar que sea obligatoria.

### 16.5 Resto del enunciado

Protección de menores, igualdad, diversidad, lenguaje inclusivo: cubiertos por 34/17 (§ 2, 4, 5, 7, 8) y
08/16 (§ 2). Imágenes de víctimas, violencia de género, sucesos: 08/12 § 4 y § 6 y 34/11 § 2. No se ha
investigado nada nuevo ahí.

---

## Tema 17 · Derechos de autor, imagen y uso de materiales de archivo en piezas realizadas

30/10 cubre casi todo (LPI arts. 1-51, 86-88, 92-93, duración, archivo, imagen LO 1/1982, créditos,
terceros). Falta lo que toca al realizador como **autor**: el resto del capítulo de la obra audiovisual
(arts. 89-91), la entidad que gestiona sus derechos, y la ficha del puesto.

### 17.1 LPI (RDL 1/1996, BOE-A-1996-8930), arts. 89 a 91, leídos el 29-09-2026

- **Art. 89** (una redacción, original). Rúbrica: **«Presunción de cesión en caso de transformación de obra
  preexistente.»** 89.1: **«Mediante el contrato de transformación de una obra preexistente que no esté en el
  dominio público, se presumirá que el autor de la misma cede al productor de la obra audiovisual los
  derechos de explotación sobre ella en los términos previstos en el artículo 88.»** 89.2: **«Salvo pacto en
  contrario, el autor de la obra preexistente conservará sus derechos a explotarla en forma de edición
  gráfica y de representación escénica y, en todo caso, podrá disponer de ella para otra obra audiovisual a
  los quince años de haber puesto su aportación a disposición del productor.»**
- **Art. 90** («Remuneración de los autores»). **Dos redacciones**; vigente desde **28-07-2006** (Ley
  23/2006, BOE-A-2006-12308). 90.1: la remuneración **«deberán determinarse para cada una de las modalidades
  de explotación concedidas»**. 90.3: proyección con precio de entrada, **«un porcentaje de los ingresos»**.
  90.4 ya está en 30/10. 90.5: **«el productor, al menos una vez al año, deberá facilitar a instancia del
  autor la documentación necesaria.»** 90.6: **«Los derechos establecidos en los apartados 3 y 4 de este
  artículo serán irrenunciables e intransmisibles por actos «inter vivos» y no serán de aplicación a los
  autores de obras audiovisuales de carácter publicitario.»** 90.7: **«Los derechos contemplados en los
  apartados 2, 3 y 4 del presente artículo se harán efectivos a través de las entidades de gestión»**.
  Relevante para promociones y spots: 90.6, exclusión de lo **publicitario**.
- **Art. 91** (original). **«Aportación insuficiente de un autor.»** **«Cuando la aportación de un autor no
  se completase por negativa injustificada del mismo o por causa de fuerza mayor, el productor podrá utilizar
  la parte ya realizada, respetando los derechos de aquél sobre la misma, sin perjuicio, en su caso, de la
  indemnización que proceda.»**

### 17.2 La entidad de gestión de los directores-realizadores

Resolución de 5 de abril de 1999, de la Secretaría de Estado de Cultura (BOE núm. 85, de 09-04-1999,
BOE-A-1999-8150), leída en boe.es el 29-09-2026: autoriza a **«Derechos de Autor de Medios Audiovisuales,
Entidad de Gestión (DAMA)»** **«para ejercer la gestión de los derechos de propiedad intelectual que
corresponden a los autores de la obra audiovisual enumerados en los puntos 1 y 2 del artículo 87»**
(director-realizador y guionistas). **No confirmado**: que la autorización siga vigente en 2026 y qué otras
entidades (SGAE) gestionan también a directores; la lista oficial del Ministerio no se ha consultado
(30/10 ya lo declara). No afirmar exclusividad.

### 17.3 La ficha del puesto en el convenio: el realizador dirige hasta la versión definitiva

X Convenio Colectivo de la RTVA y sus sociedades filiales, anexo III, BOJA núm. 240, de 10-12-2014,
página 196 (`fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`, l. 6987-7004), leído el
29-09-2026. Vigencia del convenio: la trata el tema 7 del común (no se re-verifica aquí).
**CÓDIGO PUESTO 5351000**, **«REALIZADOR»**. Objeto: **«Diseñar, coordinar, supervisar y dirigir la
realización de los programas audiovisuales.»** Tareas:
- **«Realizar la puesta en escena del guión y confeccionar el guión técnico.»**
- **«Concebir la atmósfera y estructura espacial del programa, y efectuar las localizaciones de escenarios
  naturales si los hubiese.»**
- **«Diseñar y coordinar todos los elementos técnicos-artísticos necesarios para la elaboración de programas
  y controlar la calidad y duración de los mismos.»**
- **«Coordinar al equipo humano técnico - artístico en los ensayos y grabación o emisión en directo.»**
- **«Dirigir las tareas de montaje, postproducción y mezclas hasta su completo acabado.»**
- Cierre común: **«La presente definición no constituye una lista cerrada de funciones…»**.
La ficha no menciona derechos de autor. Enlazar «hasta su completo acabado» con la **versión definitiva**
del art. 92.1 (**«de acuerdo con lo pactado en el contrato entre el director-realizador y el productor»**,
ya en 30/10) es lectura del tema, no del convenio. Plantilla: el anexo del convenio da, p. ej., **37**
realizadores B02 en CSTV Sevilla (l. 3042-3047); no usar cifras de plantilla de 2014 como actuales.
Ficha del **AYUDANTE DE REALIZACIÓN** (código **5353000**, l. 4724-4745), útil para el tema 3 y para piezas
realizadas: **«Realizar reportajes, bloques, microespacios, postproducciones y promociones de programas, bajo
las directrices del Realizador.»**

### 17.4 Estatuto profesional (texto de 2006, NO vigente)

`fuentes/canal-sur/documentos/estatuto-profesional-cgt.txt` (leído el 29-09-2026). El común (tema 6) lo
marca **no vigente** y describe sólo la figura; el texto vigente no está publicado. Su ámbito incluía
**«En TV, realizadores/as.»** (2.1) y su apartado 7 decía: **«Los/as profesionales de la información
incluidos dentro del ámbito del presente estatuto tienen derecho a la propiedad intelectual del producto de
su trabajo.»** y **«Mediante su vinculación salarial a la RTVA y SSFF ceden sus derechos de explotación
económica sobre el producto realizado.»** (7.1: derecho a que su nombre conste). **No usar como vigente**; si
el redactor lo menciona, con la misma advertencia del común.

---

## Tema 19 · PRL aplicada al puesto de realizador/a

32/15 y el común 09 cubren derechos/obligaciones (LPRL 14-22, 29), PVD (RD 488/1997 y Guía), TME, in
itinere y en misión (LGSS 156), EPI (RD 773/1997), estrés (NTP 318, 443) y turnos (ET 36.4, NTP 502). Falta:
**la ficha del puesto de realizador** (17.3, arriba; misma fuente) y **la tabla tarea-riesgo propia**.

### 19.1 Tabla tarea-riesgo (lectura del tema, no evaluación oficial; la RTVA no la ha publicado)

| Tarea del convenio (literal en 17.3) | Riesgo | Dónde está el pasaje reutilizable |
|---|---|---|
| «Coordinar al equipo humano técnico - artístico en los ensayos y grabación o emisión en directo» | Carga mental, estrés por responsabilidad sobre personas y tiempo real; trabajo a turnos y nocturno | 32/15 «Otros riesgos del puesto» (NTP 318, 443, 502; ET 36.4) |
| Idem, en el control de realización (multipantalla, intercom) | PVD, fatiga visual, varias pantallas; auriculares/intercom | 30/16 «La sala de edición…»; 28/16 «Auriculares, monitores y sala de control» |
| «Dirigir las tareas de montaje, postproducción y mezclas» | PVD, TME (ratón, postura estática) | 30/16 íd.; 32/15 § 3 |
| «efectuar las localizaciones de escenarios naturales»; retransmisiones | Accidente en misión; exteriores, cables, climatología | 32/15 § 4; 28/16 «Cargas, cables y exteriores» |
| «Realizar la puesta en escena» en plató | Ruido, riesgo eléctrico, cables, calor de focos | 08/17 «Ruido y riesgo eléctrico»; 28/16 «El riesgo eléctrico» |

Ninguna fuente leída trata el control de realización como puesto preventivo propio: **no consta** ni norma ni
NTP específica (no se ha localizado). EPI propios del realizador: ninguno específico en fuente publicada; en
exteriores, los del lugar (lectura de 32/15 § 5).

---

## Lo que no se pudo confirmar

- Directrices vigentes de Ofcom sobre signado (PDF 403 el 29-09-2026) e informe CENELEC 2003: sólo a través de
  la guía CNLSE.
- Cómo incorpora Canal Sur la LSE y si aplica BT.1702 en sus entregas: no consta publicado.
- Vigencia actual de la autorización de DAMA y lista completa de entidades que gestionan derechos de
  directores: no consultada.
- Estatuto profesional vigente: no publicado (sólo el de 2006, no vigente).
- Evaluación de riesgos del puesto de realizador en la RTVA: no publicada.
- Sigla CNLSE / «CNSLE»: la guía usa CNLSE; comprobar la forma que usa la LGCA antes de fijarla.

## Fuentes (leídas el 29-09-2026)

BOE consolidado vía `boe.py`: Ley 27/2007 (BOE-A-2007-18476) arts. 4, 14, 22, 23; Ley 11/2011 de Andalucía
(BOE-A-2011-20375) arts. 5, 16 (volcado en `fuentes/canal-sur/realizador/BOE-A-2011-20375.md`); RDL 1/1996
(BOE-A-1996-8930) arts. 89, 90, 91; LO 1/2004 (BOE-A-2004-21760) art. 14 (sólo para comprobar que ya está en
08/12). BOE-A-1999-8150 (texto del diario). UIT-R BT.1702-3 (11/2023), PDF español de itu.int. Guía CNLSE
2017 (PDF en cendocps.carm.es). X Convenio RTVA, BOJA 240/2014, anexo III. Estatuto profesional 2006 (CGT).

Ficheros tocados: este informe y, como fuentes nuevas, en `fuentes/canal-sur/realizador/`:
`bt1702-3-S.pdf`/`.txt`, `cnlse-guia-tv-2017.pdf`/`.txt` y `BOE-A-2011-20375.md`.
