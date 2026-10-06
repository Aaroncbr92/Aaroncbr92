# Puesto 29 · Tema 15 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real). Escrito
por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/15-normativa-tecnica-de-administracion-electronica-e-interoperabilidad.md`.
Material: `29-investigacion-C-datos-redes-seguridad.md` (§ Tema 15). Fila de `informes/canal-sur-reuso/informatica.tsv`:
RTVE `gestion-administrativa/01` y `tecnica-informatica/23`, 15 %, **«actualizar: sí»**. AGRUPACION.tsv: «nuevo».

## Avance

- Ficha, siglas, enunciado y «qué se puede preguntar» guardados.
- Epígrafe 1 (mapa normativo, art. 156 Ley 40/2015, ámbito y RTVA/CSRTV, remisiones caducas) guardado.
- Epígrafe 2 (principios RD 203/2021, obligados, sede y portal, identificación y firma, sello/actuación automatizada/CSV, registro, documento y referencia temporal, copias, notificación, expediente, archivo, intercambio de datos) guardado.
- Epígrafe 3 (ENI: definición, principios y dimensiones, organizativa y semántica, estándares abiertos, Red SARA/direccionamiento/hora, reutilización y licencias, firma, conservación, conformidad) guardado.
- Epígrafe 4 (NTI: lista de 23, aprobación, CCN, instrumentos; publicadas; documento, digitalización, expediente, catálogo, política de firma) guardado.
- Epígrafe 5 (ENS: objeto y ámbito, principios, responsables, política y requisitos, dimensiones/niveles/categorías, anexo II, auditoría/conformidad/incidentes, DA 2.ª vigente) guardado.
- Epígrafe 6 (aplicación práctica), normativa, «Lo que este tema no da» y trazabilidad guardados.
- Índice con `indice.py` (49 epígrafes). Extensión final: 15.435 palabras con siglas y cuadros (ficha: «15.500
  aproximadamente»). Es largo para un enunciado de una línea, pero el enunciado abarca dos esquemas, las NTI
  y las piezas electrónicas de las Leyes 39 y 40/2015; no se ha metido doctrina sin apoyo.

## Fuentes leídas y fecha

Todas el 05-10-2026, en volcados del BOE de `fuentes/canal-sur/` (redacción vigente ese día). Comprobado en
las tablas `.redacciones.tsv` que la última reforma de cualquiera de ellas es de 02-04-2025: el texto es el
mismo el 24-09-2026.

- Ya volcados por la investigación: BOE-A-2015-10565 (Ley 39/2015), BOE-A-2015-10566 (Ley 40/2015),
  BOE-A-2021-5032 (RD 203/2021), BOE-A-2010-1331 (RD 4/2010, ENI), BOE-A-2022-7191 (RD 311/2022, ENS).
- **Volcados en esta fase** con `boe.py norma … fuentes/canal-sur/`: BOE-A-2011-13168 (NTI Digitalización),
  BOE-A-2011-13169 (NTI Documento electrónico), BOE-A-2011-13170 (NTI Expediente electrónico),
  BOE-A-2012-13501 (NTI Catálogo de estándares), BOE-A-2016-10146 (NTI Política de firma y sello 2016),
  BOE-A-2021-13749 (NTI SICRES4). Todas con una sola redacción.
- Del común (sólo lectura): `temas/canal-sur-comun/02-estatuto-autonomia-andalucia.md` y `05-ley-18-2007-rtva.md`.

## Correcciones a la investigación (manda la fuente)

1. **Recuento de la DA 1.ª del ENI**: la investigación dice «22 letras (a-n, ñ, o-v)». Son **23**: a) a n) son
   14, más la ñ), más o) a v), que son 8. El tema dice veintitrés.
2. La deducción de la investigación sobre la NTI de firma de 2016 y la SICRES4 («se deduce de los títulos y
   del campo de vigencia») queda **confirmada en la fuente**: preámbulo de BOE-A-2016-10146 («sustituye a la
   anterior denominada de Política de Firma Electrónica…») y apartado Primero de BOE-A-2021-13749
   («(SICRES4), que sustituye a la anterior … (SICRES3) de 2011»).
3. La cita de la investigación del art. 22.4 ENI («a través del uso de formatos de firma longeva…») era
   correcta; el error de un «al uso» fue del redactor y lo detectó `negritas.py` (corregido).
4. Encaje de RTVA/CSRTV en el art. 2: la investigación lo dejó abierto. El tema lo da como **deducción
   declarada**, apoyada en dos literales del común (art. 54.1 Ley 9/2007: agencias = «entidades con
   personalidad jurídica pública…»; acuerdo de fusión: CSRTV «sociedad mercantil del sector público
   andaluz»). Ninguna norma lo dice expresamente; el verificador debe vigilar que el tema no lo afirme como
   dato.

## Errores de RTVE detectados (no se copian)

- `gestion-administrativa/01` § 4.1 cita el art. 17.2 y 17.3 de la Ley 39/2015 **truncados sin marca**: omite
  «que garanticen el acceso desde diferentes aplicaciones» (17.2) y «así como el cumplimiento de las
  garantías previstas en la legislación de protección de datos» (17.3). El tema cita el artículo entero del BOE.
- `tecnica-informatica/23` § 4 da como «principios básicos» sólo cuatro (proceso integral, riesgos,
  prevención/detección/respuesta, líneas de defensa); el art. 5 del ENS tiene **siete** y el tercero es
  «Prevención, detección, respuesta y conservación». Su lista de «requisitos mínimos» tampoco es la del art.
  12.6 (quince). El tema usa los literales del BOE.
- `tecnica-informatica/23` está a 21-12-2022: la DA 2.ª del ENS cambió el 07-11-2024 (RD 1125/2024). El tema
  cita la redacción vigente.

## Comprobaciones

- `negritas.py` con las 11 fuentes del BOE y los temas 2 y 5 del común: **332 negritas, 1 no encontrada**
  (la de «al uso de formatos…», corregida) y 16 «atribuidas a otro artículo», todas falsos positivos
  comprobados a mano: la herramienta toma el artículo más cercano y el tema rotula la cita antes o después
  (p. ej. «Cualidad integral (artículo 5): «…»» tras una mención al art. 6; art. 2.2.c de la Ley 40/2015
  junto a una mención al art. 3 dentro de la propia cita; art. 62.1 del Reglamento tras el art. 44 de la Ley
  40/2015).
- `refutar_exactitud.py` con los cinco volcados de leyes y reales decretos: 144 citas con artículo, 21 «no
  literales» = los mismos falsos positivos de atribución más las tres citas del común (Ley 9/2007 y acuerdo
  de fusión, que no están en esas fuentes). Ninguna cita falsa.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 7 siglas sin presentar en la primera pasada (FNMT, HTTPS, TLS, SARA, EPES, AAAA, ID);
  presentadas o explicadas. Quedan señaladas BES, EPES, AAAA e ID, que el tema explica por su contenido
  porque ninguna fuente leída desarrolla la sigla (la NTI de firma dice «clase básica (BES) añadiendo
  información sobre la política»; AAAA e ID son campos del identificador, explicados en la tabla).
- `indice.py`: índice regenerado; la portada no se toca (no está en `portadas.tsv`).

## Copiado del común

Literal, sin tocar (verificación y refutación lo saltan):

1. Epígrafe 1, «A quién se aplica, y qué pasa con la RTVA y CSRTV», primer guion: la cita «**entidades con
   personalidad jurídica pública dependientes de la Administración de la Junta de Andalucía para la
   realización de actividades de la competencia de la Comunidad Autónoma en régimen de descentralización
   funcional**» (artículo 54.1 de la Ley 9/2007), de `temas/canal-sur-comun/02-estatuto-autonomia-andalucia.md`,
   apartado «Las agencias: disposiciones comunes».
2. Mismo epígrafe, segundo guion: «**La entidad mantendrá la naturaleza jurídica de sociedad mercantil del
   sector público andaluz**» y «**adoptará la forma jurídica de sociedad mercantil anónima**» (acuerdo de
   fusión, Primero.3), de `temas/canal-sur-comun/05-ley-18-2007-rtva.md`.

Lo demás de ese guion sobre la RTVA (agencia pública empresarial con personalidad jurídica propia, art. 5
de la Ley 18/2007) es resumen del tema 5 del común, no cita.

## Copiado de RTVE sin cambios

**Ninguno.** La fila 29/15 de `informatica.tsv` marca los dos temas de RTVE con «actualizar: sí», así que
nada de ellos cabe en esta lista; además, los dos citan normas. Todo lo tomado de RTVE está abajo y **sí se
verifica**.

## Adaptado de RTVE (sí se verifica)

De `gestion-administrativa/01-gestion-administrativa.md`:
1. § 3.1 y § 3.2 → epígrafe 2, «El registro electrónico», guion «Orden»: «El registro no se ordena por
   materias: se ordena por el reloj.» y las dos funciones (dar fe de la entrada y la salida; encaminar),
   reescritas sin el «implícito» del recibo.
2. § 4.1 → epígrafe 2, «El archivo electrónico»: «Tres cosas que no conviene dar por hechas: el archivo es
   único y electrónico; recoge procedimientos finalizados…; y borrar un documento hay que autorizarlo.»
   (reescrito). La cita del art. 17 **no** se toma de RTVE (estaba truncada): se cita del BOE.
3. § 4.4 → mismo epígrafe: «Un archivo electrónico no es un disco con carpetas. Ni el formato ni el programa
   garantizan por sí solos la autenticidad: guardar en PDF no hace auténtico un documento, y poder abrirlo en
   cualquier sistema operativo es interoperabilidad, que es otra cosa.» (adaptado; RTVE decía «archivo
   digital» y «Ni el formato ni el programa garantizan nada»).
4. § 4.5 → mismo epígrafe: el párrafo del sistema de gestión documental («captura el documento, le pone
   metadatos… No es lo mismo que una base de datos relacional… con su contexto y su ciclo de vida.»), casi
   literal, sin negritas y sin la frase del procesador de texto.

De `tecnica-informatica/23-el-esquema-nacional-de-seguridad.md`:
5. § 1 → epígrafe 5, «Objeto y ámbito»: la observación de que el art. 1.2 enumera siete palabras, las
   dimensiones son cinco, y acceso y conservación son fines, no dimensiones (reescrita).
6. § 2 → «Dimensiones, niveles y categorías»: la comparación con la tríada clásica (ahora remite al tema 14,
   no al 20 de RTVE).
7. § 3 → mismo epígrafe: «Son dos escalas distintas que se confunden», el cuadro Escala / A qué se aplica /
   Valores (con los valores ahora entre comillas literales del anexo I), «La categoría la fija la dimensión
   más exigente: basta una para arrastrar al sistema entero» y la reevaluación anual (ahora con el literal
   del anexo I.1).
8. § 3 → «Auditoría, conformidad e incidentes»: el cuadro Categoría / Cómo se acredita la conformidad,
   ampliado con la columna de auditoría regular (art. 31.1).

## Salvedades de las fuentes que el tema avisa

- ENI: remisiones a la Ley 11/2007 (arts. 1.1, 3.1, 4, 8.1, 13.1, DT 1.ª) y a la LO 15/1999 (8.1, 22.2).
- RD 203/2021 (arts. 5.3 y 29.4) y NTI de firma 2016 (II.7.2.b): remisiones al RD 3/2010, derogado.
- Ministerio de Asuntos Económicos y Transformación Digital en preceptos no reformados.
- NTI Documento electrónico: «Versión N11» en el consolidado (errata por «Versión NTI»); valores de «Estado
  de elaboración» con artículos de la Ley 11/2007.
- NTI Catálogo de estándares: erratas de consolidación («PMG», «BebM», «.rff»); el estado de SHA no aparece.

## Ficheros tocados

- Creado: el tema 15 (ruta arriba) y este informe.
- Añadidos por `boe.py`: `fuentes/canal-sur/BOE-A-2011-13168.*`, `BOE-A-2011-13169.*`, `BOE-A-2011-13170.*`,
  `BOE-A-2012-13501.*`, `BOE-A-2016-10146.*`, `BOE-A-2021-13749.*` (`.md` y `.redacciones.tsv`).
- Copia de seguridad temporal en el scratchpad (fuera del repositorio).

## Diez preguntas tipo test y comprobación contra el tema

Repartidas por las dos rúbricas del enunciado (administración electrónica; interoperabilidad) y por las
piezas que el tema entiende dentro de «normativa técnica básica» (NTI y ENS), con tres de aplicación
práctica (5, 9 y 10). Cada una se ha contestado sólo con el tema.

1. Según el artículo 156.1 de la Ley 40/2015, el Esquema Nacional de Interoperabilidad comprende:
   a) los principios básicos y requisitos mínimos que garanticen la seguridad de la información;
   b) el conjunto de criterios y recomendaciones en materia de seguridad, conservación y normalización de la
   información, de los formatos y de las aplicaciones; c) las normas técnicas de obligado cumplimiento
   aprobadas por el CCN; d) la política de firma electrónica de la Administración General del Estado.
   **b)**. Tema, epígrafe 1, «El fundamento legal…» (cita literal del 156.1 y 156.2). **Entera.**
2. No está obligado a relacionarse electrónicamente con las Administraciones, según el artículo 14.2 de la
   Ley 39/2015: a) una persona jurídica; b) una entidad sin personalidad jurídica; c) una persona física que
   no ejerce actividad profesional colegiada ni representa a un obligado; d) un empleado público, para los
   trámites que realice por razón de su condición. **c)**. Epígrafe 2, «Quién está obligado…» (14.1 y
   14.2 a-e). **Entera.**
3. Las sedes electrónicas, para identificarse y garantizar una comunicación segura, utilizarán:
   a) un sello electrónico de órgano; b) un código seguro de verificación; c) certificados reconocidos o
   cualificados de autenticación de sitio web o medio equivalente; d) el certificado de empleado público
   del titular del órgano. **c)**. Epígrafe 2, «La sede electrónica y el portal» (art. 38.6). **Entera.**
4. En la actuación administrativa automatizada, el artículo 42 de la Ley 40/2015 permite usar como sistema
   de firma: a) la firma del empleado que supervisa el sistema; b) el sello electrónico basado en
   certificado reconocido o cualificado y el código seguro de verificación; c) sólo la clave concertada;
   d) sólo el sello de tiempo cualificado. **b)**. Epígrafe 2, «Cómo se identifica y firma la propia
   Administración». **Entera.**
5. (Práctica) Al digitalizar un documento en color para incorporarlo a un expediente, la NTI de
   Digitalización exige una resolución mínima de: a) 100 ppp; b) 150 ppp; c) 200 ppp, sólo en blanco y
   negro; d) 200 ppp, sea en blanco y negro, color o escala de grises. **d)**. Epígrafe 4, «Digitalización…»
   (IV.2, literal) y epígrafe 6, primer caso. **Entera.**
6. Según el artículo 6 del Real Decreto 4/2010, la interoperabilidad se entenderá contemplando sus
   dimensiones: a) física, lógica y organizativa; b) organizativa, semántica y técnica; c) jurídica,
   técnica y temporal; d) confidencialidad, integridad y disponibilidad. **b)** (con la dimensión temporal
   añadida «sin olvidar»). Epígrafe 3, «Los tres principios específicos y las dimensiones». **Entera.**
7. ¿Cuál de estos NO es un metadato mínimo obligatorio del documento electrónico según la NTI de Documento
   electrónico? a) Órgano; b) Fecha de captura; c) Tipo documental; d) Tamaño del fichero. **d)**.
   Epígrafe 4, «Documento electrónico: componentes y metadatos mínimos» (tabla con los nueve más los
   condicionales). **Entera.**
8. El artículo 11.2 del ENI permite usar en exclusiva un estándar no abierto: a) nunca; b) siempre que sea
   de uso generalizado; c) sólo cuando no se disponga de un estándar abierto que satisfaga la
   funcionalidad, y mientras esa disponibilidad no se produzca; d) cuando lo autorice el CCN. **c)**.
   Epígrafe 3, «Interoperabilidad técnica: los estándares abiertos». **Entera.**
9. (Práctica) Un sistema valorado con confidencialidad BAJO, integridad MEDIO y disponibilidad ALTO es, según
   el anexo I del ENS, de categoría: a) BÁSICA; b) MEDIA; c) ALTA; d) la media de las tres, MEDIA. **c)**.
   Epígrafe 5, «Dimensiones, niveles y categorías» (anexo I.4.1.a, literal). **Entera.**
10. (Práctica) Para un sistema de categoría BÁSICA, el ENS exige: a) auditoría de certificación cada año;
    b) autoevaluación para declarar la conformidad, sin perjuicio de someterse a auditoría de certificación,
    y auditoría regular al menos cada dos años; c) ninguna comprobación; d) sólo la aprobación de la
    política de seguridad por el CCN. **b)**. Epígrafe 5, «Auditoría, conformidad e incidentes» (arts. 31.1
    y 38.1 y cuadro). **Entera.**

Resultado: 10 de 10 contestadas enteras con el tema; no ha hecho falta ampliar. Durante la comprobación se
miró también si el tema contesta quién aprueba las NTI (Ministerio para la Transformación Digital y de la
Función Pública, publicadas por resolución de la Secretaría de Estado de Función Pública: epígrafe 4) y el
perfil mínimo de firma (-EPES: epígrafe 4): sí.
