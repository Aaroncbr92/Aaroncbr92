# Tema 15 del específico de Operador/a Informático · Normativa técnica básica de administración electrónica e interoperabilidad

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 15 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas; Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público; Real Decreto 203/2021, de 30 de marzo, Reglamento de actuación y funcionamiento del sector público por medios electrónicos; Real Decreto 4/2010, de 8 de enero, Esquema Nacional de Interoperabilidad; Real Decreto 311/2022, de 3 de mayo, Esquema Nacional de Seguridad; y las normas técnicas de interoperabilidad de Documento electrónico, Expediente electrónico, Digitalización de documentos, Catálogo de estándares, Política de firma y sello electrónicos y de certificados, y Modelo de datos para el intercambio de asientos registrales |
| Redacción que se estudia | La vigente según el texto consolidado del BOE, leído el 05-10-2026. Ninguna de esas normas cambió entre el 24-09-2026 (fecha del BOJA) y esa lectura. Las últimas reformas que se estudian son de 07-11-2024 (disposición adicional primera del Esquema de Interoperabilidad y segunda del de Seguridad) y de 02-04-2025 (artículo 27 del Reglamento de 2021) |
| Extensión | 15.500 palabras aproximadamente (con las siglas y los cuadros) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial del Estado (BOE) y Boletín Oficial de la Junta de Andalucía
(BOJA); Esquema Nacional de Interoperabilidad (ENI) y Esquema Nacional de Seguridad (ENS), que la propia
norma abrevia así; norma técnica de interoperabilidad (NTI), abreviatura que usa la de firma de 2016;
Centro Criptológico Nacional (CCN), su equipo de respuesta a incidentes (CCN-CERT, *Computer Emergency
Response Team*) y sus guías (CCN-STIC, «CCN-Seguridad de las Tecnologías de Información y la
Comunicación»); tecnologías de la información y la comunicación (TIC); Sistema de Interconexión de
Registros (SIR); Sistema de Información Administrativa (SIA); código seguro de verificación (CSV); Lista de servicios de confianza (TSL), que el ENI abrevia así; autoridad de sellado de tiempo (TSA); lista de revocación de certificados (CRL, *Certificate
Revocation List*) y protocolo de estado de certificados en línea (OCSP, *Online Certificate Status
Protocol*); identificador de objeto (OID, *Object IDentifier*) e identificador uniforme de recurso (URI,
*Uniform Resource Identifier*); lenguaje de marcas extensible (XML, *eXtensible Markup Language*) y
notación de sintaxis abstracta (ASN.1, *Abstract Syntax Notation One*); los formatos de firma avanzada
XAdES (*XML Advanced Electronic Signatures*), CAdES (*CMS Advanced Electronic Signatures*) y PAdES (*PDF
Advanced Electronic Signatures*), donde CMS es la sintaxis de mensajes criptográficos (*Cryptographic
Message Syntax*) y PDF el formato de documento portátil (*Portable Document Format*); ETSI, organismo
europeo de normalización que las normas citan sólo por su sigla, y sus especificaciones técnicas (TS) y
normas europeas (EN); la Licencia Pública de la Unión Europea (EUPL, *European Union Public Licence*);
el algoritmo de resumen seguro (SHA, *Secure Hash Algorithms*); el protocolo de Internet (IP); los
equipos de respuesta a incidentes de seguridad informática (CSIRT, *Computer Security Incident Response
Team*) y el Instituto Nacional de Ciberseguridad de España (INCIBE); el punto o persona de contacto
(POC); el documento nacional de identidad (DNI), el número de identidad de extranjero (NIE) y el número
de identificación fiscal (NIF); la Fábrica Nacional de Moneda y Timbre-Real Casa de la Moneda (FNMT); el
protocolo seguro de transferencia de hipertexto (HTTPS), la seguridad de la capa de transporte (TLS) y
la red privada virtual (VPN), que estudian los temas 13 y 14. Dos nombres que las normas no desarrollan:
la Red SARA, como el ENI llama a la red de comunicaciones de las Administraciones públicas españolas, y
los perfiles de firma BES y EPES, que la NTI de firma de 2016 sólo explica por su contenido (epígrafe 4).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 15): «Normativa técnica básica
> de administración electrónica e interoperabilidad.»

El enunciado no nombra ninguna norma. «Normativa técnica básica» no es una expresión definida en la
ley: este tema la entiende como las normas que fijan cómo funciona por dentro la Administración
electrónica (registro, documento, firma, expediente, archivo, sede) y las que fijan cómo se entienden
entre sí los sistemas (interoperabilidad) y cómo se protegen (seguridad). La selección es del temario,
no del BOJA, y se apoya en que las propias leyes enlazan esas piezas: la Ley 40/2015 crea los dos
esquemas en su artículo 156; el Real Decreto 203/2021 desarrolla las dos leyes «en lo referido a la
actuación y el funcionamiento electrónico del sector público»; y las normas técnicas de interoperabilidad
bajan al detalle (metadatos, formatos, resolución de escaneo, formatos de firma).

Qué se puede preguntar: qué norma crea el ENI y el ENS y cuál los regula; a quién se aplican y si
alcanzan a una agencia pública empresarial y a una sociedad mercantil pública; quién está obligado a
relacionarse electrónicamente; qué es una sede electrónica y qué certificado usa; qué sistemas de
identificación y firma admiten las Administraciones y cuáles se deben garantizar siempre; qué es el
sello electrónico, la actuación administrativa automatizada y el CSV; qué contiene un asiento de
registro y qué recibo se entrega; qué requisitos tiene un documento electrónico administrativo y qué
firmas no necesita; qué es una copia auténtica y la digitalización; qué es el índice electrónico del
expediente; qué exige el archivo electrónico único; qué dimensiones tiene la interoperabilidad y cuáles
son sus principios específicos; qué es un estándar abierto y cuándo se puede usar uno que no lo es; qué
son la Red SARA, el plan de direccionamiento y la hora oficial; qué cuatro libertades exige una licencia
de fuentes abiertas; qué es una política de firma, una firma longeva y un fichero de implementación; qué
NTI existen, quién las aprueba y cuáles se han publicado; cuántos metadatos mínimos lleva un documento
electrónico y cuáles; qué resolución mínima exige la digitalización; qué formatos de firma admite la
política de firma; cuáles son los siete principios básicos y los quince requisitos mínimos del ENS, las
cinco dimensiones, los tres niveles y las tres categorías; cada cuánto se audita y cómo se acredita la
conformidad; y qué papel tienen el CCN y sus guías. En la aplicación práctica: escanear bien un documento
para que sea copia auténtica, elegir el formato de conservación, saber por qué un sistema de registro
debe sincronizar la hora, o qué categoría ENS sale de una valoración dada.

<!-- indice -->

## Índice

- [1. El mapa de la normativa](#1-el-mapa-de-la-normativa)
  - [Las normas y lo que hace cada una](#las-normas-y-lo-que-hace-cada-una)
  - [El fundamento legal de los dos esquemas: artículo 156 de la Ley 40/2015](#el-fundamento-legal-de-los-dos-esquemas-artículo-156-de-la-ley-402015)
  - [A quién se aplica, y qué pasa con la RTVA y CSRTV](#a-quién-se-aplica-y-qué-pasa-con-la-rtva-y-csrtv)
  - [Lo que no cuadra en el texto vigente](#lo-que-no-cuadra-en-el-texto-vigente)
- [2. Administración electrónica: las piezas técnicas](#2-administración-electrónica-las-piezas-técnicas)
  - [Los principios de la actuación electrónica](#los-principios-de-la-actuación-electrónica)
  - [Quién está obligado a relacionarse electrónicamente](#quién-está-obligado-a-relacionarse-electrónicamente)
  - [La sede electrónica y el portal](#la-sede-electrónica-y-el-portal)
  - [La identificación y la firma de los interesados](#la-identificación-y-la-firma-de-los-interesados)
  - [Cómo se identifica y firma la propia Administración](#cómo-se-identifica-y-firma-la-propia-administración)
  - [El registro electrónico](#el-registro-electrónico)
  - [El documento electrónico y su referencia temporal](#el-documento-electrónico-y-su-referencia-temporal)
  - [Las copias auténticas y la digitalización](#las-copias-auténticas-y-la-digitalización)
  - [La notificación electrónica](#la-notificación-electrónica)
  - [El expediente electrónico](#el-expediente-electrónico)
  - [El archivo electrónico](#el-archivo-electrónico)
  - [El intercambio de datos entre Administraciones](#el-intercambio-de-datos-entre-administraciones)
- [3. Interoperabilidad: el Esquema Nacional de Interoperabilidad](#3-interoperabilidad-el-esquema-nacional-de-interoperabilidad)
  - [Qué es la interoperabilidad y qué comprende el Esquema](#qué-es-la-interoperabilidad-y-qué-comprende-el-esquema)
  - [Los tres principios específicos y las dimensiones](#los-tres-principios-específicos-y-las-dimensiones)
  - [Interoperabilidad organizativa y semántica](#interoperabilidad-organizativa-y-semántica)
  - [Interoperabilidad técnica: los estándares abiertos](#interoperabilidad-técnica-los-estándares-abiertos)
  - [Infraestructuras comunes, red, direccionamiento y hora](#infraestructuras-comunes-red-direccionamiento-y-hora)
  - [Reutilización y transferencia de tecnología](#reutilización-y-transferencia-de-tecnología)
  - [Firma electrónica y certificados en el ENI](#firma-electrónica-y-certificados-en-el-eni)
  - [Recuperación y conservación del documento](#recuperación-y-conservación-del-documento)
  - [Conformidad y actualización](#conformidad-y-actualización)
- [4. Las normas técnicas de interoperabilidad](#4-las-normas-técnicas-de-interoperabilidad)
  - [Qué son, cuántas hay previstas y quién las aprueba](#qué-son-cuántas-hay-previstas-y-quién-las-aprueba)
  - [Las que se han publicado](#las-que-se-han-publicado)
  - [Documento electrónico: componentes y metadatos mínimos](#documento-electrónico-componentes-y-metadatos-mínimos)
  - [Digitalización: la resolución mínima y la imagen fiel](#digitalización-la-resolución-mínima-y-la-imagen-fiel)
  - [Expediente electrónico: componentes e índice](#expediente-electrónico-componentes-e-índice)
  - [Catálogo de estándares: los formatos admitidos](#catálogo-de-estándares-los-formatos-admitidos)
  - [Política de firma y sello: formatos, perfiles y firmas longevas](#política-de-firma-y-sello-formatos-perfiles-y-firmas-longevas)
- [5. El Esquema Nacional de Seguridad](#5-el-esquema-nacional-de-seguridad)
  - [Objeto y ámbito](#objeto-y-ámbito)
  - [Los siete principios básicos](#los-siete-principios-básicos)
  - [Los cuatro responsables, y dónde está el operador](#los-cuatro-responsables-y-dónde-está-el-operador)
  - [La política de seguridad y los quince requisitos mínimos](#la-política-de-seguridad-y-los-quince-requisitos-mínimos)
  - [Dimensiones, niveles y categorías](#dimensiones-niveles-y-categorías)
  - [Las medidas del anexo II](#las-medidas-del-anexo-ii)
  - [Auditoría, conformidad e incidentes](#auditoría-conformidad-e-incidentes)
  - [El desarrollo del ENS y las guías del CCN](#el-desarrollo-del-ens-y-las-guías-del-ccn)
- [6. Aplicación práctica](#6-aplicación-práctica)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. El mapa de la normativa

### Las normas y lo que hace cada una

| Norma | Qué regula de este tema |
|---|---|
| Ley 39/2015, del Procedimiento Administrativo Común (BOE-A-2015-10565) | La relación electrónica con los interesados: derecho y obligación de relacionarse electrónicamente, identificación y firma de los interesados, registro, archivo, documento, copias, notificación electrónica y expediente |
| Ley 40/2015, de Régimen Jurídico del Sector Público (BOE-A-2015-10566) | El funcionamiento electrónico por dentro y entre Administraciones: sede, portal, sello y firma de la Administración, actuación automatizada, archivo; y en sus artículos 155 a 158, transmisión de datos, los dos esquemas y la reutilización de aplicaciones |
| Real Decreto 203/2021, Reglamento de actuación y funcionamiento del sector público por medios electrónicos (BOE-A-2021-5032) | Desarrolla las dos leyes en lo electrónico |
| Real Decreto 4/2010, Esquema Nacional de Interoperabilidad (BOE-A-2010-1331) | Cómo se entienden entre sí los sistemas: dimensiones, estándares, infraestructuras comunes, firma, conservación del documento, y la lista de NTI |
| Normas técnicas de interoperabilidad (resoluciones publicadas en el BOE) | El detalle: metadatos, formatos, digitalización, expediente, política de firma, intercambio registral |
| Real Decreto 311/2022, Esquema Nacional de Seguridad (BOE-A-2022-7191) | Cómo se protegen los sistemas: principios, requisitos mínimos, categorías, medidas, auditoría |

El Real Decreto 203/2021 lo dice de sí mismo en su artículo 1.1: **«Este Reglamento tiene por objeto el
desarrollo de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las
Administraciones Públicas, y de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público,
en lo referido a la actuación y el funcionamiento electrónico del sector público.»** Es un reglamento:
desarrolla las leyes, no las sustituye. El ENI y el ENS también son reales decretos, y las NTI son
resoluciones de una Secretaría de Estado: la jerarquía va, por tanto, de ley a real decreto y de real
decreto a resolución.

### El fundamento legal de los dos esquemas: artículo 156 de la Ley 40/2015

**«1. El Esquema Nacional de Interoperabilidad comprende el conjunto de criterios y recomendaciones en
materia de seguridad, conservación y normalización de la información, de los formatos y de las
aplicaciones que deberán ser tenidos en cuenta por las Administraciones Públicas para la toma de
decisiones tecnológicas que garanticen la interoperabilidad.**

**2. El Esquema Nacional de Seguridad tiene por objeto establecer la política de seguridad en la
utilización de medios electrónicos en el ámbito de la presente Ley, y está constituido por los
principios básicos y requisitos mínimos que garanticen adecuadamente la seguridad de la información
tratada.»**

Para recordarlo: el ENI son **«criterios y recomendaciones»**; el ENS, **«principios básicos y requisitos
mínimos»**. El ENS lo dice expresamente en su artículo 1.1: **«Este real decreto tiene por objeto regular
el Esquema Nacional de Seguridad (en adelante, ENS), establecido en el artículo 156.2 de la Ley 40/2015,
de 1 de octubre, de Régimen Jurídico del Sector Público.»**

Una salvedad que el texto vigente no ha corregido: el Real Decreto 4/2010 sigue diciendo en su artículo
1.1 que regula el ENI **«establecido en el artículo 42 de la Ley 11/2007, de 22 de junio»**, y su
artículo 3.1 fija el ámbito por remisión al **«artículo 2 de la Ley 11/2007, de 22 de junio»**. Esa ley
está derogada: la disposición derogatoria única, apartado 2, letra b), de la Ley 39/2015 deroga la
**«Ley 11/2007, de 22 de junio, de acceso electrónico de los ciudadanos a los Servicios Públicos.»** El
fundamento vigente del ENI es el artículo 156.1 de la Ley 40/2015, y así lo dice el preámbulo de la NTI
de 2021 sobre asientos registrales: el ENI **«se establece en el artículo 156 de la Ley 40/2015, de 1 de
octubre, de Régimen Jurídico del Sector Público, que sustituye al apartado 1 del artículo 42 de la Ley
11/2007»**. Y la misma disposición derogatoria de la Ley 39/2015 resuelve qué hacer con esas remisiones
(apartado 3): **«Las referencias contenidas en normas vigentes a las disposiciones que se derogan
expresamente deberán entenderse efectuadas a las disposiciones de esta Ley que regulan la misma materia
que aquéllas.»** Si una pregunta cita la Ley 11/2007 como norma vigente, está mal.

### A quién se aplica, y qué pasa con la RTVA y CSRTV

Las dos leyes tienen el mismo ámbito subjetivo. Artículo 2 de la Ley 40/2015:

- **«1. La presente Ley se aplica al sector público que comprende:**
- **a) La Administración General del Estado.**
- **b) Las Administraciones de las Comunidades Autónomas.**
- **c) Las Entidades que integran la Administración Local.**
- **d) El sector público institucional.**
- **2. El sector público institucional se integra por:**
- **a) Cualesquiera organismos públicos y entidades de derecho público vinculados o dependientes de las
  Administraciones Públicas.**
- **b) Las entidades de derecho privado vinculadas o dependientes de las Administraciones Públicas que
  quedarán sujetas a lo dispuesto en las normas de esta Ley que específicamente se refieran a las mismas,
  en particular a los principios previstos en el artículo 3, y en todo caso, cuando ejerzan potestades
  administrativas.**
- **c) Las Universidades públicas que se regirán por su normativa específica y supletoriamente por las
  previsiones de la presente Ley.»**

El apartado 3 añade quién es «Administración Pública»: la General del Estado, las de las comunidades
autónomas, las entidades locales **«así como los organismos públicos y entidades de derecho público
previstos en la letra a) del apartado 2.»** El artículo 2 de la Ley 39/2015 es igual en lo sustancial
(su letra b omite la referencia a los principios del artículo 3). El Reglamento de 2021 se remite a los
dos (artículo 1.2) y el ENS se aplica **«a todo el sector público, en los términos en que este se define
por el artículo 2 de la Ley 40/2015, de 1 de octubre, y de acuerdo con lo previsto en el artículo 156.2
de la misma»** (artículo 2.1).

Ninguna norma leída dice en qué letra encajan la RTVA y CSRTV. Lo que sí consta:

- De la RTVA, la Ley 9/2007, de la Administración de la Junta de Andalucía, define las agencias como
  «**entidades con personalidad jurídica pública dependientes de la Administración de la Junta de
  Andalucía para la realización de actividades de la competencia de la Comunidad Autónoma en régimen de
  descentralización funcional**» (artículo 54.1), y la Ley 18/2007 dice que la RTVA es una agencia
  pública empresarial con personalidad jurídica propia (artículo 5).
- De CSRTV, el acuerdo de fusión dice: «**La entidad mantendrá la naturaleza jurídica de sociedad
  mercantil del sector público andaluz**» y «**adoptará la forma jurídica de sociedad mercantil
  anónima**».

De ahí se deduce, sin que ninguna norma lo diga con estas palabras, que la RTVA (persona jurídica pública
dependiente de la Junta) estaría en la letra 2.a) y CSRTV (sociedad mercantil, de Derecho privado) en la
2.b). Para CSRTV la consecuencia es doble: las dos leyes sólo se le aplican en lo que se refiera
específicamente a esas entidades y cuando ejerza potestades administrativas; pero el ENS se aplica
«a todo el sector público» tal como lo define el artículo 2, que incluye la letra b). Y, al margen de esa
calificación, el ENS alcanza también al sector privado que trabaja para el público (artículo 2.3, en el
epígrafe 5).

### Lo que no cuadra en el texto vigente

Las normas de este tema arrastran remisiones a normas o a ministerios que ya no existen, y el BOE las
consolida tal cual. No es error del tema citarlas literalmente; sí lo sería presentarlas como vigentes:

- El ENI remite a la Ley 11/2007 (artículos 1.1, 3.1, 4, 8.1, 11.3.b y 13.1, y disposiciones transitorias
  primera y segunda) y
  a la Ley Orgánica 15/1999, de protección de datos (artículos 8.1 y 22.2), ambas derogadas.
- El Reglamento de 2021 remite al **«Real Decreto 3/2010, de 8 de enero»**, el ENS anterior (artículos
  5.3 y 29.4), que el ENS de 2022 deroga: **«Queda derogado el Real Decreto 3/2010, de 8 de enero, por
  el que se regula el Esquema Nacional de Seguridad en el ámbito de la Administración Electrónica»**
  (disposición derogatoria única).
- Varios preceptos nombran al **«Ministerio de Asuntos Económicos y Transformación Digital»** (por
  ejemplo, los artículos 9 y 10 de la Ley 39/2015, o el 12.4 y el 33.7 del ENS). Las dos disposiciones
  reformadas en 2024 ya nombran al **«Ministerio para la Transformación Digital y de la Función
  Pública»**, aunque el apartado 3 de la disposición adicional primera del ENI, que la reforma no tocó,
  sigue nombrando al anterior.

## 2. Administración electrónica: las piezas técnicas

### Los principios de la actuación electrónica

El Reglamento de 2021 abre con seis principios (artículo 2):

| Principio | Qué significa en la norma |
|---|---|
| a) Neutralidad tecnológica y adaptabilidad al progreso | **«el sector público utilizará estándares abiertos, así como, en su caso y de forma complementaria, estándares que sean de uso generalizado»**; las herramientas **«serán no discriminatorios, estarán disponibles de forma general y serán compatibles con los productos informáticos de uso general»** |
| b) Accesibilidad | Igualdad y no discriminación en el acceso, **«en particular de las personas con discapacidad y de las personas mayores»** |
| c) Facilidad de uso | Diseño centrado en las personas usuarias, **«de forma que se minimice el grado de conocimiento necesario para el uso del servicio»** |
| d) Interoperabilidad | **«la capacidad de los sistemas de información y, por ende, de los procedimientos a los que éstos dan soporte, de compartir datos y posibilitar el intercambio de información entre ellos»** |
| e) Proporcionalidad | **«sólo se exigirán las garantías y medidas de seguridad adecuadas a la naturaleza y circunstancias de los distintos trámites y actuaciones electrónicos»** |
| f) Personalización y proactividad | La Administración **«proporcione servicios precumplimentados y se anticipe a las posibles necesidades»** del usuario |

### Quién está obligado a relacionarse electrónicamente

La regla general es la elección de la persona física (Ley 39/2015, artículo 14.1): **«Las personas
físicas podrán elegir en todo momento si se comunican con las Administraciones Públicas para el
ejercicio de sus derechos y obligaciones a través de medios electrónicos o no, salvo que estén obligadas
a relacionarse a través de medios electrónicos»**. El artículo 14.2 enumera los obligados, **«al
menos»**:

- **«a) Las personas jurídicas.»**
- **«b) Las entidades sin personalidad jurídica.»**
- c) Quienes ejerzan una actividad profesional con colegiación obligatoria, en esa actividad (**«dentro
  de este colectivo se entenderán incluidos los notarios y registradores de la propiedad y
  mercantiles»**).
- d) Quienes representen a un interesado obligado.
- **«e) Los empleados de las Administraciones Públicas para los trámites y actuaciones que realicen
  con ellas por razón de su condición de empleado público, en la forma en que se determine
  reglamentariamente por cada Administración.»**

El artículo 14.3 permite ampliar la obligación por reglamento a colectivos de personas físicas que
tengan **«acceso y disponibilidad de los medios electrónicos necesarios»**. Y el Reglamento de 2021 fija
cuándo surte efecto el cambio de canal de una persona no obligada: **«a partir del quinto día hábil
siguiente a aquel en que el órgano competente para tramitar el procedimiento haya tenido constancia de
la misma»** (artículo 3.2).

### La sede electrónica y el portal

La Ley 40/2015 distingue dos cosas que el lenguaje corriente confunde:

- Sede electrónica (artículo 38.1): **«aquella dirección electrónica, disponible para los ciudadanos a
  través de redes de telecomunicaciones, cuya titularidad corresponde a una Administración Pública, o
  bien a una o varios organismos públicos o entidades de Derecho Público en el ejercicio de sus
  competencias.»** Su titular responde **«respecto de la integridad, veracidad y actualización de la
  información y los servicios»** (38.2).
- Portal de internet (artículo 39): **«el punto de acceso electrónico cuya titularidad corresponda a una
  Administración Pública, organismo público o entidad de Derecho Público que permite el acceso a través
  de internet a la información publicada y, en su caso, a la sede electrónica correspondiente.»**

En la sede se tramita y se responde de lo publicado; el portal informa y, en su caso, lleva a la sede.
Lo técnico de la sede está en tres apartados del artículo 38:

- Principios de creación (38.3): **«transparencia, publicidad, responsabilidad, calidad, seguridad,
  disponibilidad, accesibilidad, neutralidad e interoperabilidad»**.
- Comunicaciones seguras (38.4): **«Las sedes electrónicas dispondrán de sistemas que permitan el
  establecimiento de comunicaciones seguras siempre que sean necesarias.»**
- Certificado (38.6): **«Las sedes electrónicas utilizarán, para identificarse y garantizar una
  comunicación segura con las mismas, certificados reconocidos o cualificados de autenticación de sitio
  web o medio equivalente.»** Es el certificado de servidor que hace funcionar HTTPS en la sede (el
  protocolo y el certificado de sitio web se estudian en los temas 13 y 14).

### La identificación y la firma de los interesados

El tema 14 desarrolla la firma electrónica y los certificados; aquí basta lo que la ley exige a las
Administraciones. Para identificarse electrónicamente, el artículo 9.2 de la Ley 39/2015 admite tres
familias: **«a) Sistemas basados en certificados electrónicos cualificados de firma electrónica»**,
**«b) Sistemas basados en certificados electrónicos cualificados de sello electrónico»**, los dos
**«expedidos por prestadores incluidos en la ‘‘Lista de confianza de prestadores de servicios de
certificación’’»**, y c) cualquier otro sistema que la Administración considere válido con registro
previo del usuario y previa comunicación a la Secretaría General de Administración Digital (el Reglamento de 2021 nombra entre ellos los **«Sistemas de clave concertada»**,
artículo 26.2.c). Para firmar, el artículo 10.2 admite la firma cualificada y avanzada basada en
certificado cualificado, el sello cualificado y avanzado, y otros sistemas con registro previo. Los dos
artículos cierran con la misma garantía: **«Las Administraciones Públicas deberán garantizar que la
utilización de uno de los sistemas previstos en las letras a) y b) sea posible para todo
procedimiento, aun cuando se admita para ese mismo procedimiento alguno de los previstos en la letra
c).»** (9.2; el 10.2 dice **«para todos los procedimientos en todos sus trámites»**). Es decir: la
Administración puede ofrecer una clave concertada, pero no puede impedir que se use un certificado.

El Reglamento de 2021 fija qué tiene que llevar dentro el certificado de persona física que se usa
para identificarse (artículo 27.1, en su redacción vigente desde el 02-04-2025): **«al menos, su nombre y
apellidos y su número de Documento Nacional de Identidad, Número de Identificación de Extranjero, Número
de Identificación Consular Central o Número de Identificación Fiscal que conste como tal de manera
inequívoca.»** Para el sello de persona jurídica, **«como mínimo, su denominación y su Número de
Identificación Fiscal»** (27.3).

### Cómo se identifica y firma la propia Administración

Ésta es la parte que más toca a un servicio informático, porque son sistemas que alguien instala y
mantiene:

- Sello electrónico (Ley 40/2015, artículo 40.1): **«Las Administraciones Públicas podrán identificarse
  mediante el uso de un sello electrónico basado en un certificado electrónico reconocido o cualificado
  que reúna los requisitos exigidos por la legislación de firma electrónica.»** El certificado incluye
  **«el número de identificación fiscal y la denominación correspondiente»**, y la relación de sellos
  que usa cada Administración **«deberá ser pública y accesible por medios electrónicos»**.
- Actuación administrativa automatizada (artículo 41.1): **«cualquier acto o actuación realizada
  íntegramente a través de medios electrónicos por una Administración Pública en el marco de un
  procedimiento administrativo y en la que no haya intervenido de forma directa un empleado público.»**
  Antes de ponerla en marcha **«deberá establecerse previamente el órgano u órganos competentes»** para
  **«la definición de las especificaciones, programación, mantenimiento, supervisión y control de calidad
  y, en su caso, auditoría del sistema de información y de su código fuente»**, y el órgano responsable
  a efectos de impugnación (41.2).
- Firma de la actuación automatizada (artículo 42): **«a) Sello electrónico de Administración Pública,
  órgano, organismo público o entidad de derecho público, basado en certificado electrónico reconocido o
  cualificado»** o **«b) Código seguro de verificación vinculado a la Administración Pública, órgano,
  organismo público o entidad de Derecho Público, en los términos y condiciones establecidos,
  permitiéndose en todo caso la comprobación de la integridad del documento mediante el acceso a la sede
  electrónica correspondiente.»** El CSV es el código que permite cotejar en la sede un documento
  impreso con el original electrónico.
- Firma del personal (artículo 43.1): sin perjuicio de lo previsto en los artículos 38, 41 y 42, la actuación electrónica **«se realizará
  mediante firma electrónica del titular del órgano o empleado público»**; cada Administración decide
  qué sistema usa su personal, que puede identificar a la vez al titular del puesto y al órgano, y
  **«Por razones de seguridad pública los sistemas de firma electrónica podrán referirse sólo el número
  de identificación profesional del empleado público.»** (43.2).
- Interoperabilidad de la firma (artículo 45.2): cuando una Administración use firmas no basadas en
  certificado cualificado y tenga que remitir la documentación a otra, **«podrá superponer un sello
  electrónico basado en un certificado electrónico reconocido o cualificado»**, para que la otra pueda
  verificarla de forma automática.

### El registro electrónico

Artículo 16.1 de la Ley 39/2015: **«Cada Administración dispondrá de un Registro Electrónico General, en
el que se hará el correspondiente asiento de todo documento que sea presentado o que se reciba en
cualquier órgano administrativo, Organismo público o Entidad vinculado o dependiente a éstos. También se
podrán anotar en el mismo, la salida de los documentos oficiales dirigidos a otros órganos o
particulares.»** Los organismos pueden tener **«su propio registro electrónico plenamente interoperable e
interconectado con el Registro Electrónico General»** de su Administración, que funciona **«como un
portal que facilitará el acceso a los registros electrónicos de cada Organismo»**.

Lo que el sistema tiene que hacer, apartado por apartado:

- Orden (16.2): **«Los asientos se anotarán respetando el orden temporal de recepción o salida de los
  documentos, e indicarán la fecha del día en que se produzcan. Concluido el trámite de registro, los
  documentos serán cursados sin dilación a sus destinatarios»**. El registro no se ordena por materias:
  se ordena por el reloj. De ahí las dos funciones clásicas del registro: dar fe de la entrada y la
  salida, y encaminar lo presentado a su destino.
- Contenido del asiento (16.3): **«un número, epígrafe expresivo de su naturaleza, fecha y hora de su
  presentación, identificación del interesado, órgano administrativo remitente, si procede, y persona u
  órgano administrativo al que se envía, y, en su caso, referencia al contenido del documento que se
  registra.»**
- Recibo (16.3): **«se emitirá automáticamente un recibo consistente en una copia autenticada del
  documento de que se trate, incluyendo la fecha y hora de presentación y el número de entrada de
  registro, así como un recibo acreditativo de otros documentos que, en su caso, lo acompañen, que
  garantice la integridad y el no repudio de los mismos.»**
- Dónde presentar (16.4): en el registro electrónico de la Administración destinataria y en los de
  cualquier otra del artículo 2.1; en Correos; en representaciones diplomáticas u oficinas consulares;
  en las oficinas de asistencia en materia de registros; y en cualquier otro que establezcan las
  disposiciones vigentes.
- Interoperabilidad (16.4, párrafo final): **«Los registros electrónicos de todas y cada una de las
  Administraciones, deberán ser plenamente interoperables, de modo que se garantice su compatibilidad
  informática e interconexión, así como la transmisión telemática de los asientos registrales y de los
  documentos que se presenten en cualquiera de los registros.»**
- Presencial (16.5): lo presentado de manera presencial **«deberán ser digitalizados»** por la oficina de asistencia en
  materia de registros, **«devolviéndose los originales al interesado»**, salvo custodia obligatoria o
  soporte no digitalizable.

El Reglamento de 2021 añade el instrumento técnico de esa interconexión: **«Las interconexiones entre
Registros de las Administraciones Públicas deberán realizarse a través del Sistema de Interconexión de
Registros (SIR)»**, de acuerdo con el ENI **«y en la correspondiente Norma Técnica»** (artículo 60.2), que
es la NTI de modelo de datos para el intercambio de asientos (epígrafe 4). Y tres reglas de explotación
del artículo 39:

- Formatos: las Administraciones **«podrán determinar los formatos y estándares a los que deberán
  ajustarse los documentos presentados»** siempre que cumplan el ENI (39.1).
- Código malicioso: **«En el caso de que se detecte código malicioso susceptible de afectar a la
  integridad o seguridad del sistema en documentos que ya hayan sido registrados, se requerirá su
  subsanación al interesado que los haya aportado»** (39.2).
- Tamaño: si los documentos exceden la capacidad del SIR, su remisión **«podrá sustituirse por la puesta
  a disposición de los documentos, previamente depositados en un repositorio de intercambio de
  ficheros.»** (39.4).

El ENI, por su parte, fija la hora: **«Los sistemas o aplicaciones implicados en la provisión de un
servicio público por vía electrónica se sincronizarán con la hora oficial, con una precisión y desfase
que garanticen la certidumbre de los plazos establecidos en el trámite administrativo que
satisfacen.»** (artículo 15.1), y la sincronización **«se realizará con el Real Instituto y Observatorio
de la Armada»** (15.2). En un registro, la hora del asiento decide si un plazo se cumplió.

### El documento electrónico y su referencia temporal

Artículo 26 de la Ley 39/2015. Primero, la regla: **«Las Administraciones Públicas emitirán los
documentos administrativos por escrito, a través de medios electrónicos, a menos que su naturaleza exija
otra forma más adecuada de expresión y constancia.»** (26.1). Después, los cinco requisitos de validez
del documento electrónico administrativo (26.2):

1. **«a) Contener información de cualquier naturaleza archivada en un soporte electrónico según un
   formato determinado susceptible de identificación y tratamiento diferenciado.»**
2. **«b) Disponer de los datos de identificación que permitan su individualización, sin perjuicio de su
   posible incorporación a un expediente electrónico.»**
3. **«c) Incorporar una referencia temporal del momento en que han sido emitidos.»**
4. **«d) Incorporar los metadatos mínimos exigidos.»**
5. **«e) Incorporar las firmas electrónicas que correspondan de acuerdo con lo previsto en la normativa
   aplicable.»**

Y la excepción (26.3): **«No requerirán de firma electrónica, los documentos electrónicos emitidos por las
Administraciones Públicas que se publiquen con carácter meramente informativo, así como aquellos que no
formen parte de un expediente administrativo. En todo caso, será necesario identificar el origen de
estos documentos.»**

El Reglamento de 2021 concreta la referencia temporal (artículo 50.1), con dos modalidades:

| Modalidad | Definición | Cuándo se usa |
|---|---|---|
| Marca de tiempo | **«la asignación por medios electrónicos de la fecha y, en su caso, la hora a un documento electrónico»** | **«en todos aquellos casos en los que las normas reguladoras no establezcan la utilización de un sello electrónico cualificado de tiempo»** (50.2) |
| Sello electrónico cualificado de tiempo | **«la asignación por medios electrónicos de una fecha y hora a un documento electrónico con la intervención de un prestador cualificado de servicios de confianza que asegure la exactitud e integridad de la marca de tiempo del documento»** | Cuando la norma del procedimiento lo exija |

La diferencia está en el tercero: la marca la pone el propio sistema; el sello, un prestador cualificado.
Y una regla más: **«Los sellos electrónicos de tiempo no cualificados serán asimilables a
todos los efectos a las marcas de tiempo.»** (50.1.b).

### Las copias auténticas y la digitalización

La copia auténtica es la que hace el órgano competente garantizando **«la identidad del órgano que ha
realizado la copia y su contenido»**, y **«Las copias auténticas tendrán la misma validez y eficacia que
los documentos originales.»** (Ley 39/2015, artículo 27.2). El Reglamento añade que **«se expedirán siempre
a partir de un original o de otra copia auténtica»** (artículo 47.2). Para hacerlas, las Administraciones
**«deberán ajustarse a lo previsto en el Esquema Nacional de Interoperabilidad, el Esquema Nacional de
Seguridad y sus normas técnicas de desarrollo»** (27.3), y a cuatro reglas según el sentido de la copia:

| De / a | Regla (artículo 27.3) |
|---|---|
| Electrónico → electrónico | **«con o sin cambio de formato, deberán incluir los metadatos que acrediten su condición de copia y que se visualicen al consultar el documento»** (letra a) |
| Papel → electrónico | **«requerirán que el documento haya sido digitalizado»** y los mismos metadatos de copia (letra b) |
| Electrónico → papel | **«figure la condición de copia y contendrán un código generado electrónicamente u otro sistema de verificación, que permitirá contrastar la autenticidad de la copia mediante el acceso a los archivos electrónicos del órgano u Organismo público emisor»** (letra c) |
| Papel → papel | Copia auténtica en papel del documento electrónico que tenga la Administración, o puesta de manifiesto electrónica (letra d) |

La ley define la digitalización en la misma letra b): **«el proceso tecnológico que permite convertir un
documento en soporte papel o en otro soporte no electrónico en un fichero electrónico que contiene la
imagen codificada, fiel e íntegra del documento.»** Las condiciones técnicas (resolución, formatos,
metadatos) están en la NTI de digitalización (epígrafe 4).

### La notificación electrónica

Se practica **«mediante comparecencia en la sede electrónica de la Administración u Organismo actuante, a
través de la dirección electrónica habilitada única o mediante ambos sistemas»** (Ley 39/2015, artículo
43.1); se entiende practicada **«en el momento en que se produzca el acceso a su contenido»**, y, si es
obligatoria o elegida, **«se entenderá rechazada cuando hayan transcurrido diez días naturales desde la
puesta a disposición de la notificación sin que se acceda a su contenido.»** (43.2).

### El expediente electrónico

Artículo 70 de la Ley 39/2015. Definición (70.1): **«el conjunto ordenado de documentos y actuaciones que
sirven de antecedente y fundamento a la resolución administrativa, así como las diligencias encaminadas a
ejecutarla.»** Formato (70.2): **«Los expedientes tendrán formato electrónico»** y llevan **«un índice
numerado de todos los documentos que contenga cuando se remita»**. Remisión (70.3), que es la parte
técnica:

**«Cuando en virtud de una norma sea preciso remitir el expediente electrónico, se hará de acuerdo con lo
previsto en el Esquema Nacional de Interoperabilidad y en las correspondientes Normas Técnicas de
Interoperabilidad, y se enviará completo, foliado, autentificado y acompañado de un índice, asimismo
autentificado, de los documentos que contenga. La autenticación del citado índice garantizará la
integridad e inmutabilidad del expediente electrónico generado desde el momento de su firma y permitirá
su recuperación siempre que sea preciso, siendo admisible que un mismo documento forme parte de
distintos expedientes electrónicos.»**

El Reglamento de 2021 lo dice de otra forma: **«El foliado de los expedientes administrativos
electrónicos se llevará a cabo mediante un índice electrónico autenticado que garantizará la integridad
del expediente y permitirá su recuperación siempre que sea preciso.»** (artículo 51.1). Ese índice lo
firma el titular del órgano o **«podrá ser sellado electrónicamente en el caso de expedientes
electrónicos que se formen de manera automática»** (51.3). En papel, el foliado era numerar las hojas; en
electrónico, es firmar la lista de documentos con su huella digital (epígrafe 4, NTI de expediente). Y lo
que no forma parte del expediente (70.4): la información **«auxiliar o de apoyo, como la contenida en
aplicaciones, ficheros y bases de datos informáticas, notas, borradores, opiniones, resúmenes,
comunicaciones e informes internos»**, salvo los informes solicitados antes de la resolución.

### El archivo electrónico

Artículo 17 de la Ley 39/2015, entero:

**«1. Cada Administración deberá mantener un archivo electrónico único de los documentos electrónicos
que correspondan a procedimientos finalizados, en los términos establecidos en la normativa reguladora
aplicable.**

**2. Los documentos electrónicos deberán conservarse en un formato que permita garantizar la
autenticidad, integridad y conservación del documento, así como su consulta con independencia del
tiempo transcurrido desde su emisión. Se asegurará en todo caso la posibilidad de trasladar los datos a
otros formatos y soportes que garanticen el acceso desde diferentes aplicaciones. La eliminación de
dichos documentos deberá ser autorizada de acuerdo a lo dispuesto en la normativa aplicable.**

**3. Los medios o soportes en que se almacenen documentos, deberán contar con medidas de seguridad, de
acuerdo con lo previsto en el Esquema Nacional de Seguridad, que garanticen la integridad, autenticidad,
confidencialidad, calidad, protección y conservación de los documentos almacenados. En particular,
asegurarán la identificación de los usuarios y el control de accesos, así como el cumplimiento de las
garantías previstas en la legislación de protección de datos.»**

Tres cosas que no conviene dar por hechas: el archivo es **único** y electrónico; recoge
**procedimientos finalizados**, no expedientes vivos; y borrar un documento hay que **autorizarlo**. El
artículo 46 de la Ley 40/2015 extiende el almacenamiento electrónico a **«Todos los documentos utilizados en
las actuaciones administrativas»**, **«salvo cuando no sea posible»** (46.1), y añade, en su apartado 3, **«la recuperación y conservación a
largo plazo de los documentos electrónicos producidos por las Administraciones Públicas que así lo
requieran»**.

El Reglamento de 2021 define el archivo electrónico único como **«el conjunto de sistemas y servicios que
sustenta la gestión, custodia y recuperación de los documentos y expedientes electrónicos así como de
otras agrupaciones documentales o de información una vez finalizados los procedimientos administrativos o
actuaciones correspondientes.»** (artículo 55.1), y fija qué hay que conservar de cada documento:
**«La conservación de los documentos electrónicos deberá realizarse de forma que permita su acceso y
comprenda, como mínimo, su identificación, contenido, metadatos, firma, estructura y formato.»** (54.3).
Cuando un formato se queda viejo, hay que migrar: se habilitarán **«los medios tecnológicos para la
migración de los datos a otros formatos y soportes que permitan garantizar la autenticidad, integridad,
disponibilidad, conservación y acceso al documento cuando el formato de los mismos deje de figurar entre
los admitidos por el Esquema Nacional de Interoperabilidad y normativa correspondiente.»** (54.5). Y
bajo la supervisión de quién: **«de los responsables de la seguridad y de los responsables de la custodia
y gestión del archivo electrónico y de los responsables de las unidades productoras de la
documentación»** (54.5).

Un archivo electrónico no es un disco con carpetas. Ni el formato ni el programa garantizan por sí solos
la autenticidad: guardar en PDF no hace auténtico un documento, y poder abrirlo en cualquier sistema
operativo es interoperabilidad, que es otra cosa. La autenticidad y la integridad las sostienen la firma
electrónica, los metadatos y, para el largo plazo, el sellado de tiempo y las firmas longevas (epígrafes
3 y 4). La herramienta que hace todo eso de forma sistemática es el sistema de gestión documental:
captura el documento, le pone metadatos, lo clasifica según un cuadro de clasificación, controla
versiones y accesos, aplica el calendario de conservación y ejecuta la transferencia o la eliminación
autorizada. No es lo mismo que una base de datos relacional, aunque por dentro use una: la base de datos
guarda datos; el sistema de gestión documental guarda documentos con su contexto y su ciclo de vida.

### El intercambio de datos entre Administraciones

El ciudadano no tiene que aportar lo que la Administración ya tiene, y para eso las Administraciones se
pasan los datos. Ley 40/2015, artículo 155.1: **«cada Administración deberá facilitar el acceso de las
restantes Administraciones Públicas a los datos relativos a los interesados que obren en su poder,
especificando las condiciones, protocolos y criterios funcionales o técnicos necesarios para acceder a
dichos datos con las máximas garantías de seguridad, integridad y disponibilidad.»** El artículo 155.2
pone el límite: no cabe **«un tratamiento ulterior de los datos para fines incompatibles con el fin para
el cual se recogieron inicialmente»**.

El cauce técnico son las plataformas de intermediación. Reglamento de 2021, artículo 61.1: esas
transmisiones, **«mediante consulta a las plataformas de intermediación de datos u otros sistemas
electrónicos habilitados al efecto, tienen la consideración de certificados administrativos necesarios
para el procedimiento»**; y el artículo 62.1 exige que las plataformas dejen **«constancia de la fecha y
hora en que se produjo la transmisión, así como del procedimiento administrativo, trámite o actuación al
que se refiere la consulta.»** Cuando los participantes forman una red cerrada, la Ley 40/2015 da validez
a lo transmitido (artículo 44.1): **«Los documentos electrónicos transmitidos en entornos cerrados de
comunicaciones establecidos entre Administraciones Públicas, órganos, organismos públicos y entidades de
derecho público, serán considerados válidos a efectos de autenticación e identificación de los emisores
y receptores»**, con la condición de que **«En todo caso deberá garantizarse la seguridad del entorno
cerrado de comunicaciones y la protección de los datos que se transmitan.»** (44.4).

## 3. Interoperabilidad: el Esquema Nacional de Interoperabilidad

### Qué es la interoperabilidad y qué comprende el Esquema

El glosario del ENI (anexo) la define: **«Interoperabilidad: Capacidad de los sistemas de información, y
por ende de los procedimientos a los que éstos dan soporte, de compartir datos y posibilitar el
intercambio de información y conocimiento entre ellos.»** El objeto del Esquema (artículo 1.2):

**«El Esquema Nacional de Interoperabilidad comprenderá los criterios y recomendaciones de seguridad,
normalización y conservación de la información, de los formatos y de las aplicaciones que deberán ser
tenidos en cuenta por las Administraciones públicas para asegurar un adecuado nivel de interoperabilidad
organizativa, semántica y técnica de los datos, informaciones y servicios que gestionen en el ejercicio
de sus competencias y para evitar la discriminación a los ciudadanos por razón de su elección
tecnológica.»**

Y su rango frente a otros criterios (artículo 3.2): **«El Esquema Nacional de Interoperabilidad y sus
normas de desarrollo, prevalecerán sobre cualquier otro criterio en materia de política de
interoperabilidad en la utilización de medios electrónicos para el acceso de los ciudadanos a los
servicios públicos.»**

### Los tres principios específicos y las dimensiones

El artículo 4 enumera tres principios específicos: **«a) La interoperabilidad como cualidad integral.
b) Carácter multidimensional de la interoperabilidad. c) Enfoque de soluciones multilaterales.»**

- Cualidad integral (artículo 5): **«La interoperabilidad se tendrá presente de forma integral desde la
  concepción de los servicios y sistemas y a lo largo de su ciclo de vida: planificación, diseño,
  adquisición, construcción, despliegue, explotación, publicación, conservación y acceso o interconexión
  con los mismos.»**
- Carácter multidimensional (artículo 6): **«La interoperabilidad se entenderá contemplando sus
  dimensiones organizativa, semántica y técnica.»** Y cierra: **«Todo ello sin olvidar la dimensión
  temporal que ha de garantizar el acceso a la información a lo largo del tiempo.»**
- Soluciones multilaterales (artículo 7): **«Se favorecerá la aproximación multilateral a la
  interoperabilidad de forma que se puedan obtener las ventajas derivadas del escalado, de la aplicación
  de las arquitecturas modulares y multiplataforma, de compartir, de reutilizar y de colaborar.»**

Las dimensiones, con la definición del glosario:

| Dimensión | Definición (anexo del ENI) |
|---|---|
| Organizativa | **«Es aquella dimensión de la interoperabilidad relativa a la capacidad de las entidades y de los procesos a través de los cuales llevan a cabo sus actividades para colaborar con el objeto de alcanzar logros mutuamente acordados relativos a los servicios que prestan.»** |
| Semántica | **«Es aquella dimensión de la interoperabilidad relativa a que la información intercambiada pueda ser interpretable de forma automática y reutilizable por aplicaciones que no intervinieron en su creación.»** |
| Técnica | **«Es aquella dimensión de la interoperabilidad relativa a la relación entre sistemas y servicios de tecnologías de la información, incluyendo aspectos tales como las interfaces, la interconexión, la integración de datos y servicios, la presentación de la información, la accesibilidad y la seguridad, u otros de naturaleza análoga.»** |
| En el tiempo | **«Es aquella dimensión de la interoperabilidad relativa a la interacción entre elementos que corresponden a diversas oleadas tecnológicas; se manifiesta especialmente en la conservación de la información en soporte electrónico.»** |

El artículo 1.2 y el 6 nombran tres dimensiones (organizativa, semántica y técnica) y el 6 añade la
temporal con un «sin olvidar»; el glosario define las cuatro. Si una pregunta pide «las tres
dimensiones», son organizativa, semántica y técnica.

Para distinguirlas con un caso de oficio: que dos registros estén conectados por la misma red es
interoperabilidad técnica; que ambos entiendan igual el campo «fecha de presentación» es semántica; que
las dos Administraciones hayan acordado qué se envían y para qué es organizativa; y que el asiento se
pueda leer dentro de veinte años es la dimensión temporal.

### Interoperabilidad organizativa y semántica

- Servicios entre Administraciones (artículo 8.1): cada Administración publica las condiciones de
  acceso a sus servicios, datos y documentos (finalidades, modalidades, requisitos, perfiles,
  protocolos, gobierno y seguridad). Para ello **«Las Administraciones públicas podrán utilizar nodos de
  interoperabilidad, entendidos como entidades a las cuales se les encomienda la gestión de apartados
  globales o parciales de la interoperabilidad organizativa, semántica o técnica.»** (8.3).
- Inventarios (artículo 9.1): cada Administración mantiene **«al menos»** la relación de sus
  procedimientos y servicios, conectada con el Sistema de Información Administrativa, y la de sus órganos
  y oficinas, conectada con el **«Directorio Común de Unidades Orgánicas y Oficinas»**, que **«proveerá una
  codificación unívoca»**. Ese código es el que aparece en el metadato «Órgano» de cada documento.
- Activos semánticos (artículo 10): los modelos de datos de intercambio se publican **«a través del
  Centro de Interoperabilidad Semántica de la Administración»** (10.3). El glosario define el modelo de
  datos como **«Conjunto de definiciones (modelo conceptual), interrelaciones (modelo lógico) y reglas y
  convenciones (modelo físico) que permiten describir los datos para su intercambio.»**

### Interoperabilidad técnica: los estándares abiertos

Es el artículo central para un informático. Artículo 11.1 (redacción de 2021): **«Las Administraciones
públicas usarán estándares abiertos, así como, en su caso y de forma complementaria, estándares que
sean de uso generalizado por los ciudadanos»**, de forma que:

- **«a) Los documentos y servicios de administración electrónica que los órganos o Entidades de Derecho
  Público emisores pongan a disposición de los ciudadanos o de otras Administraciones públicas se
  encontrarán, como mínimo, disponibles mediante estándares abiertos.»**
- b) Los documentos, servicios y aplicaciones serán visualizables, accesibles y funcionalmente
  operables **«en condiciones que permitan satisfacer el principio de neutralidad tecnológica y eviten
  la discriminación a los ciudadanos por razón de su elección tecnológica.»**

La excepción (11.2): **«el uso en exclusiva de un estándar no abierto sin que se ofrezca una alternativa
basada en un estándar abierto se limitará a aquellas circunstancias en las que no se disponga de un
estándar abierto que satisfaga la funcionalidad satisfecha por el estándar no abierto en cuestión y sólo
mientras dicha disponibilidad no se produzca.»** Y el derecho del ciudadano (11.5): podrá elegir las
aplicaciones con las que se relaciona **«siempre y cuando utilicen estándares abiertos o, en su caso,
aquellos otros que sean de uso generalizado por los ciudadanos.»**

Las dos definiciones que hacen falta para aplicar el artículo:

- **«Estándar abierto: Aquél que reúne las siguientes condiciones: a) Que sea público y su utilización
  sea disponible de manera gratuita o a un coste que no suponga una dificultad de acceso, b) Que su uso y
  aplicación no esté condicionado al pago de un derecho de propiedad intelectual o industrial.»**
- **«Uso generalizado por los ciudadanos: Usado por casi todas las personas físicas, personas jurídicas
  y entes sin personalidad que se relacionen o sean susceptibles de relacionarse con las
  Administraciones públicas españolas.»**

Y **«Coste que no suponga una dificultad de acceso: Precio del estándar que, por estar vinculado al coste
de distribución y no a su valor, no impide conseguir su posesión o uso.»** Qué estándares concretos
cumplen esto lo dice la NTI de Catálogo de estándares (epígrafe 4).

### Infraestructuras comunes, red, direccionamiento y hora

- Infraestructuras comunes (artículo 12): las Administraciones **«enlazarán aquellas infraestructuras y
  servicios que puedan implantar en su ámbito de actuación con las infraestructuras y servicios comunes
  que proporcione la Administración General del Estado»**.
- Red (artículo 13.1): **«las Administraciones públicas utilizarán preferentemente la Red de
  comunicaciones de las Administraciones públicas españolas para comunicarse entre sí, para lo cual
  conectarán a la misma, bien sus respectivas redes, bien sus nodos de interoperabilidad»**; y **«La Red
  SARA prestará la citada Red de comunicaciones de las Administraciones públicas españolas.»** La norma
  no desarrolla la sigla SARA. Los requisitos para conectarse están en una NTI (13.2).
- Direccionamiento (artículo 14): **«Las Administraciones Públicas aplicarán el Plan de direccionamiento
  e interconexión de redes en la Administración, desarrollado en la norma técnica de interoperabilidad
  correspondiente, para su interconexión a través de las redes de comunicaciones.»** La NTI prevista
  **«tratará reglas aplicables a la asignación y requisitos de direccionamiento IP para garantizar la
  correcta administración de la Red de comunicaciones de las Administraciones Públicas españolas y
  evitar el uso de direcciones duplicadas.»** (disposición adicional primera, letra q). Es el mismo
  problema que el del tema 13 con las direcciones privadas: dos redes que usan el mismo rango no se
  pueden unir sin traducir direcciones.
- Hora oficial (artículo 15): sincronización con el Real Instituto y Observatorio de la Armada, ya vista
  en el registro.

### Reutilización y transferencia de tecnología

La Ley 40/2015 obliga a compartir aplicaciones. Artículo 157.1: **«Las Administraciones pondrán a
disposición de cualquiera de ellas que lo solicite las aplicaciones, desarrolladas por sus servicios o
que hayan sido objeto de contratación y de cuyos derechos de propiedad intelectual sean titulares, salvo
que la información a la que estén asociadas sea objeto de especial protección por una norma.»** Antes de
comprar o desarrollar, deben consultar el directorio general de aplicaciones (157.3), y **«En el caso de
existir una solución disponible para su reutilización total o parcial, las Administraciones Públicas
estarán obligadas a su uso, salvo que la decisión de no reutilizarla se justifique en términos de
eficiencia»** (157.3, párrafo tercero). Las aplicaciones **«podrán ser declaradas como de fuentes
abiertas»** (157.2) cuando de ello se derive más transparencia o se fomente la incorporación de los
ciudadanos a la sociedad de la información: es una facultad, no una obligación. La Administración General del Estado mantiene el
directorio general (158.2), y el ENI precisa que lo hace **«a través del Centro de Transferencia de
Tecnología»** (artículo 17.1).

El ENI fija qué debe garantizar una licencia de fuentes abiertas (artículo 16.2), cuatro condiciones:

- **«a) Pueden ejecutarse para cualquier propósito.**
- **b) Permiten conocer su código fuente.**
- **c) Pueden modificarse o mejorarse.**
- **d) Pueden redistribuirse a otros usuarios con o sin cambios siempre que la obra derivada mantenga
  estas cuatro garantías.»**

Y **«Para este fin se procurará la aplicación de la Licencia Pública de la Unión Europea, sin perjuicio de
otras licencias que garanticen los mismos derechos»** (16.3). En los contratos de desarrollo, la
Administración debe adquirir **«los derechos completos de propiedad intelectual de las aplicaciones»**
(16.4.a). Por defecto, el licenciamiento entre Administraciones se hace **«sin contraprestación y sin
necesidad de establecer convenio alguno»** (16.1.f).

### Firma electrónica y certificados en el ENI

Artículo 18.1: **«La Administración General del Estado definirá una política de firma electrónica y de
certificados que servirá de marco general de interoperabilidad para el reconocimiento mutuo de las firmas
electrónicas basadas en certificados de documentos administrativos en las Administraciones Públicas.»**
Todos los organismos y entidades de derecho público de la Administración General del Estado la aplican, y no
aplicarla exige justificación y autorización de la Secretaría General de Administración Digital (18.1,
párrafo segundo); **«Las restantes Administraciones Públicas podrán acogerse»**
a ella (18.2) o aprobar otras, que **«deberán ser interoperables con la política marco de firma
electrónica mencionada en el apartado 1, en particular, con sus ficheros de implementación»** (18.3). Los
procedimientos con certificados deben atenerse a la política aplicable **«particularmente en la
aplicación de los datos obligatorios y opcionales, las reglas de creación y validación de firma
electrónica, los algoritmos a utilizar y longitudes de clave mínimas aplicables.»** (18.7).

Tres definiciones del glosario:

- **«Política de firma electrónica: Conjunto de normas de seguridad, de organización, técnicas y legales
  para determinar cómo se generan, verifican y gestionan firmas electrónicas, incluyendo las
  características exigibles a los certificados de firma.»**
- **«Ficheros de implementación de las políticas de firma: Son la representación en lenguaje formal (XML
  o ASN.1) de las condiciones establecidas en la política de firma, acorde a las normas técnicas
  establecidas por los organismos de estandarización.»**
- **«Lista de servicios de confianza (TSL): Lista de acceso público que recoge información precisa y
  actualizada de aquellos servicios de certificación y firma electrónica que se consideran aptos para su
  empleo en un marco de interoperabilidad de las Administraciones públicas españolas y europeas.»**

Las plataformas de validación (artículo 20) dan **«en un único punto de llamada, todos los elementos de
confianza y de interoperabilidad organizativa, semántica y técnica necesarios para integrar los distintos
certificados reconocidos y firmas»** (20.2) e incorporan las listas de confianza (20.4). Un aviso: la
definición de firma electrónica del glosario del ENI (**«Conjunto de datos en forma electrónica,
consignados junto a otros o asociados con ellos, que pueden ser utilizados como medio de identificación
del firmante.»**) es de 2010; la que rige hoy es la del reglamento europeo eIDAS, que estudia el tema 14.

### Recuperación y conservación del documento

El artículo 21.1 enumera trece medidas, de la a) a la m), para conservar los documentos a lo largo de su
ciclo de vida. Entre ellas:

- **«a) La definición de una política de gestión de documentos»**.
- **«b) La inclusión en los expedientes de un índice electrónico firmado por el órgano o entidad
  actuante que garantice la integridad del expediente electrónico y permita su recuperación.»**
- **«c) La identificación única e inequívoca de cada documento»**.
- **«d) La asociación de los metadatos mínimos obligatorios y, en su caso, complementarios»**.
- g), acceso completo e inmediato, que termina: **«El sistema permitirá la consulta durante todo el
  período de conservación al menos de la firma electrónica, incluido, en su caso, el sello de tiempo, y
  de los metadatos asociados al documento.»**
- k), el borrado o la destrucción de soportes cuando lo diga la evaluación documental, **«dejando
  registro de su eliminación.»**

Para ello **«las Administraciones públicas crearán repositorios electrónicos, complementarios y
equivalentes en cuanto a su función a los archivos convencionales, destinados a cubrir el conjunto del
ciclo de vida de los documentos electrónicos.»** (21.2). La seguridad de lo conservado remite al ENS
(22.1), y la firma, a la política de firma y **«a través del uso de formatos de firma longeva que preserven la
conservación de las firmas a lo largo del tiempo.»** (22.4).

Los formatos (artículo 23): **«el documento se conservará en el formato en que haya sido elaborado,
enviado o recibido, y preferentemente en un formato correspondiente a un estándar abierto que preserve a
lo largo del tiempo la integridad del contenido del documento, de la firma electrónica y de los metadatos
que lo acompañan.»** (23.1). Y si el formato envejece (23.3): **«se aplicarán procedimientos normalizados
de copiado auténtico de los documentos con cambio de formato, de etiquetado con información del formato
utilizado y, en su caso, de las migraciones o conversiones de formatos.»** La digitalización de papel
(artículo 24.1) seguirá la NTI en cuatro aspectos: **«a) Formatos estándares de uso común para la
digitalización de documentos en soporte papel y técnica de compresión empleada»**, **«b) Nivel de
resolución.»**, **«c) Garantía de imagen fiel e íntegra.»** y **«d) Metadatos mínimos obligatorios y
complementarios, asociados al proceso de digitalización.»**

Dos definiciones del glosario cierran este apartado: **«Metadato: Dato que define y describe otros datos.
Existen diferentes tipos de metadatos según su aplicación.»** e **«Índice electrónico: Relación de
documentos electrónicos de un expediente electrónico, firmada por la Administración, órgano o entidad
actuante, según proceda y cuya finalidad es garantizar la integridad del expediente electrónico y
permitir su recuperación siempre que sea preciso.»**

### Conformidad y actualización

- **«La interoperabilidad de las sedes y registros electrónicos, así como la del acceso electrónico de los
  ciudadanos a los servicios públicos, se regirán por lo establecido en el Esquema Nacional de
  Interoperabilidad.»** (artículo 25).
- La conformidad con el ENI **«se incluirá en el ciclo de vida de los servicios y sistemas, acompañada de
  los correspondientes procedimientos de control.»** (artículo 26); cada órgano establece sus mecanismos
  de control (27) y publica en su sede **«las declaraciones de conformidad y a otros posibles distintivos
  de interoperabilidad»** (28).
- **«El Esquema Nacional de Interoperabilidad se deberá mantener actualizado de manera permanente.»**
  (artículo 29).
- Formación: **«El personal de las Administraciones públicas recibirá la formación necesaria para
  garantizar el conocimiento del presente Esquema Nacional de Interoperabilidad»** (disposición adicional
  segunda).

## 4. Las normas técnicas de interoperabilidad

### Qué son, cuántas hay previstas y quién las aprueba

Las prevé la disposición adicional primera del ENI, en su redacción vigente desde el 07-11-2024 (dada
por el Real Decreto 1125/2024, de 5 de noviembre). Apartado 1: **«Se desarrollarán las siguientes normas
técnicas de interoperabilidad que serán de obligado cumplimiento por parte de las Administraciones
Públicas:»**. Son de obligado cumplimiento, a diferencia de los «criterios y recomendaciones» con que el
artículo 156.1 de la Ley 40/2015 describe el Esquema.

La lista tiene veintitrés letras, de la a) a la v) con la ñ:

| Letra | Norma técnica |
|---|---|
| a) | Catálogo de estándares |
| b) | Documento electrónico |
| c) | Digitalización de documentos |
| d) | Expediente electrónico |
| e) | Política de firma electrónica y de certificados de la Administración |
| f) | Protocolos de intermediación de datos |
| g) | Relación de modelos de datos |
| h) | Política de gestión de documentos electrónicos |
| i) | Requisitos de conexión a la Red de comunicaciones de las Administraciones Públicas españolas |
| j) | Procedimientos de copiado auténtico y conversión entre documentos electrónicos |
| k) | Modelo de datos para el intercambio de asientos entre las entidades registrales |
| l) | Reutilización de recursos de información |
| m) | Inventario y codificación de objetos administrativos |
| n) | Transferencia e ingreso de documentos y expedientes electrónicos |
| ñ) | Valoración y eliminación de documentos y expedientes electrónicos |
| o) | Preservación de documentación electrónica |
| p) | Tratamiento y preservación de bases de datos |
| q) | Plan de direccionamiento |
| r) | Reutilización de activos en modo producto y en modo servicio |
| s) | Modelo de datos y condiciones de interoperabilidad de los registros de funcionarios habilitados |
| t) | Modelo de datos y condiciones de interoperabilidad de los registros electrónicos de apoderamientos |
| u) | Sistema de referencia de documentos y repositorios de confianza |
| v) | Política de firma electrónica y de certificados en el ámbito estatal |

Lo que dice la propia disposición de algunas:

- b) Documento electrónico: **«tratará los metadatos mínimos obligatorios, la asociación de los datos y
  metadatos de firma o de sellado de tiempo, así como otros metadatos complementarios asociados; y los
  formatos de documento.»**
- c) Digitalización: **«tratará los formatos y estándares aplicables, los niveles de calidad, las
  condiciones técnicas y los metadatos asociados al proceso de digitalización.»**
- e) Política de firma: incluye **«los formatos de firma, los algoritmos a utilizar y longitudes mínimas
  de las claves, las reglas de creación y validación de la firma electrónica, la gestión de las políticas
  de firma, el uso de las referencias temporales y de sello de tiempo»**.

Quién las aprueba (apartado 2): **«El Ministerio para la Transformación Digital y de la Función Pública, a
propuesta de la Comisión Sectorial de Administración Electrónica prevista en la disposición adicional
novena de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público, aprobará las normas
técnicas de interoperabilidad y las publicará mediante Resolución de la persona titular de la Secretaría
de Estado de Función Pública.»** Y quién manda en lo criptográfico (apartado 3, párrafo segundo): **«Para
garantizar la debida interoperabilidad en materia de ciberseguridad y criptografía, en relación con la
aplicación del Real Decreto 4/2010, de 8 de enero, por el que se regula el Esquema Nacional de
Interoperabilidad en el ámbito de la administración electrónica, el órgano competente será el Centro
Criptológico Nacional, adscrito al Centro Nacional de Inteligencia.»** El artículo 35.2 del ENS dice lo
mismo desde el lado de la seguridad.

El apartado 4 crea cuatro instrumentos para la interoperabilidad: **«a) Sistema de Información
Administrativa»** (inventario de procedimientos y servicios), **«b) Centro de interoperabilidad semántica
de la Administración»** (modelos de datos), **«c) Centro de Transferencia de Tecnología»** (directorio de
aplicaciones reutilizables) y **«d) Directorio Común de Unidades Orgánicas y Oficinas de las
Administraciones Públicas»** (códigos de órganos y oficinas).

### Las que se han publicado

Previstas no es lo mismo que aprobadas. Las publicadas en el BOE como resolución, según la búsqueda por
título en la legislación consolidada del BOE (05-10-2026):

| Norma técnica | Resolución | Estado |
|---|---|---|
| Digitalización de Documentos | 19-07-2011 (BOE de 30-07-2011) | Vigente |
| Documento Electrónico | 19-07-2011 | Vigente |
| Expediente Electrónico | 19-07-2011 | Vigente |
| Política de Firma Electrónica y de certificados de la Administración | 19-07-2011 | Sustituida en 2016 |
| Procedimientos de copiado auténtico y conversión entre documentos electrónicos | 19-07-2011 | Vigente |
| Requisitos de conexión a la red de comunicaciones de las Administraciones públicas españolas | 19-07-2011 | Vigente |
| Modelo de Datos para el intercambio de asientos entre las Entidades Registrales (SICRES3) | 19-07-2011 | Sustituida en 2021 |
| Política de gestión de documentos electrónicos | 28-06-2012 | Vigente |
| Protocolos de intermediación de datos | 28-06-2012 | Vigente |
| Relación de modelos de datos | 28-06-2012 | Vigente |
| Catálogo de estándares | 03-10-2012 | Vigente |
| Reutilización de recursos de la información | 19-02-2013 | Vigente |
| Política de Firma y Sello Electrónicos y de Certificados de la Administración | 27-10-2016 | Vigente |
| Modelo de Datos para el intercambio de asientos entre las Entidades Registrales (SICRES4) | 22-07-2021 | Vigente |

Catorce resoluciones, doce vigentes. Las dos sustituciones las dicen las propias resoluciones nuevas:
la de firma de 2016 **«sustituye a la anterior denominada de Política de Firma Electrónica y de
certificados de la Administración»** (preámbulo), y la de 2021 aprueba la NTI de asientos **«(SICRES4),
que sustituye a la anterior Norma Técnica de Interoperabilidad de Modelo de Datos para el intercambio de
asientos entre las Entidades Registrales (SICRES3) de 2011»** (apartado primero). Las letras m) a v),
añadidas en 2021 por el Real Decreto 203/2021 (la reforma de 2024 sólo cambió el ministerio del apartado 2), no constan publicadas en esa búsqueda; eso no prueba que no exista ninguna
publicada sin consolidar.

### Documento electrónico: componentes y metadatos mínimos

Los componentes (NTI de Documento electrónico, apartado III): **«a) Contenido, entendido como conjunto de
datos o información del documento. b) En su caso, firma electrónica. c) Metadatos del documento
electrónico.»** Y la firma (apartado IV): **«Los documentos administrativos electrónicos, y aquellos
susceptibles de formar parte de un expediente, tendrán siempre asociada al menos una firma electrónica
de acuerdo con la normativa aplicable.»**

Los metadatos mínimos obligatorios (anexo I) son nueve, más tres que sólo se ponen en ciertos casos:

| Metadato | Qué indica (anexo I) |
|---|---|
| Versión NTI | Identificador normalizado de la versión de la NTI conforme a la cual se estructura el documento |
| Identificador | **«Identificador normalizado del documento.»**, con la forma ES_<Órgano>_<AAAA>_<ID específico>, donde el tercer campo es el año de captura (cuatro cifras) y el cuarto un código alfanumérico único de treinta caracteres |
| Órgano | Código del órgano generador, **«extraído del Directorio Común»** |
| Fecha de captura | **«Fecha de alta del documento en el sistema de gestión documental.»** |
| Origen | **«Indica si el contenido del documento fue creado por un ciudadano o por una administración.»** (‘0’ ciudadano, ‘1’ Administración) |
| Estado de elaboración | Si es original o qué clase de copia es |
| Nombre de formato | **«Formato lógico del fichero de contenido del documento electrónico.»**, tomado del Catálogo de estándares |
| Tipo documental | Resolución, acuerdo, comunicación, notificación, acta, certificado, informe, solicitud, factura y otros |
| Tipo de firma | **«Indica el tipo de firma que avala el documento.»**: CSV o un formato de firma de la política de firma |
| Valor CSV y Definición generación CSV | Sólo si el tipo de firma es CSV |
| Identificador de documento origen | Sólo si es copia con cambio de formato o copia parcial |

Tres reglas sobre ellos (apartado V.1): los mínimos **«Estarán presentes en cualquier proceso de
intercambio de documentos electrónicos»** y **«No serán modificados en ninguna fase posterior del
procedimiento administrativo, a excepción de modificaciones necesarias para la corrección de errores u
omisiones en el valor inicialmente asignado.»**; y se pueden añadir metadatos complementarios (V.2). Al
mostrar un documento en la sede se enseña su contenido, la información básica de cada firma y la
**«Descripción y valor de los metadatos mínimos obligatorios.»** (apartado VIII).

Dos avisos de lectura: en el texto consolidado del BOE el primer metadato aparece rotulado «Versión
N11», errata evidente por «Versión NTI», que es como se rotula en la NTI de expediente; y los valores
del metadato «Estado de elaboración» siguen citando artículos de la Ley 11/2007, hoy derogada.

### Digitalización: la resolución mínima y la imagen fiel

La NTI de Digitalización de documentos (resolución de 19-07-2011) es la que se aplica cada vez que se
escanea papel para incorporarlo a un expediente:

- Componentes del documento digitalizado (III.1): la imagen electrónica, los metadatos mínimos de la NTI
  de documento electrónico y, **«Si procede, firma de la imagen electrónica»**. Para que sea copia
  auténtica hay que cumplir además la NTI de copiado auténtico (III.2).
- Formatos (IV.1): los de imagen del Catálogo de estándares.
- Resolución (IV.2): **«El nivel de resolución mínimo para imágenes electrónicas será de 200 píxeles
  por pulgada, tanto para imágenes obtenidas en blanco y negro, color o escala de grises.»**
- Fidelidad (IV.3): la imagen **«a) Respetará la geometría del documento origen en tamaños y
  proporciones. b) No contendrá caracteres o gráficos que no figurasen en el documento origen.»**
- Proceso (V.1): digitalización por medio fotoeléctrico; **«Si procede, optimización automática de la
  imagen electrónica para garantizar su legibilidad»** (**«umbralización, reorientación, eliminación de
  bordes negros, u otros de naturaleza análoga»**); asignación de metadatos; y, si procede, firma.
- Mantenimiento (V.2): **«un conjunto de operaciones de mantenimiento preventivo y comprobaciones
  rutinarias»** que garanticen que la aplicación y los dispositivos producen imágenes fieles.

### Expediente electrónico: componentes e índice

NTI de Expediente electrónico, apartado III.1. Los componentes son cuatro: **«a) Documentos
electrónicos»**, que pueden ir sueltos, en carpetas o en expedientes anidados; **«b) Índice
electrónico»**; **«c) Firma del índice electrónico por la Administración, órgano o entidad actuante»**; y
**«d) Metadatos del expediente electrónico.»** Los metadatos mínimos del expediente (anexo I) son la
versión de la NTI, el identificador (con «EXP»), el órgano, la fecha de apertura, la clasificación (el
procedimiento, codificado según el SIA), el estado (**«Abierto»**, **«Cerrado»** o **«Índice para remisión
cerrado.»**), el interesado y el tipo de firma del índice.

Lo que tiene que reflejar el índice cuando se intercambia (V.4): **«a) La fecha de generación del
índice.»**; **«b) Para cada documento electrónico: su identificador, su huella digital, la función resumen
utilizada para su obtención, que atenderá a lo establecido en la Norma Técnica de Interoperabilidad de
Catálogo de estándares, y, opcionalmente, la fecha de incorporación al expediente y el orden del
documento dentro del expediente.»**; y, en su caso, la disposición en carpetas. Ésa es la técnica que
hace funcionar el «foliado» electrónico: si alguien cambia un documento, su huella ya no coincide con la
del índice firmado. Al remitirlo se envía primero la estructura y luego cada documento **«en el orden
indicado en el índice»** (V.1), preferentemente, en la actuación automatizada, por la red de comunicaciones de las
Administraciones (V.5).

### Catálogo de estándares: los formatos admitidos

La NTI de Catálogo de estándares (resolución de 03-10-2012) clasifica cada estándar como **«Admitido»** o
**«En abandono»** (apartado III.d) y prevé su revisión **«con periodicidad anual»** (V.1). Su anexo
recoge, entre otros, estos estándares, todos en estado «Admitido» salvo los que se indican (de SHA el
texto consolidado no trae el estado). El catálogo no separa texto e imagen: los agrupa en una sola
categoría, «Imagen y/o texto»; el reparto en filas de este cuadro es del tema:

| Uso | Formatos del catálogo |
|---|---|
| Documentos de texto y ofimática | PDF (ISO 32000-1), PDF/A (ISO 19005, el formato **«for long-term preservation»**), OpenDocument (ISO/IEC 26300: .odt, .ods, .odp, .odg), Office Open XML en su variante *Strict* (ISO/IEC 29500-1:2012: .docx, .xlsx, .pptx), TXT, RTF (**«Uso generalizado»** y **«En abandono»**) |
| Imagen | JPEG (el catálogo cita la ISO/IEC 15444, JPEG 2000), PNG (ISO/IEC 15948), TIFF (ISO 12639), SVG |
| Web y datos | HTML, CSS, MHTML, CSV |
| Sonido y vídeo | MP3 (**«Uso generalizado»**), OGG-Vorbis, MPEG-4, WebM |
| Compresión | ZIP, GZIP |
| Firma | XAdES, CAdES, PAdES, XML-DSig y CMS (**«Admitido»**); PKCS#7 y la firma propia de PDF, «PDF Signature» (**«En abandono»**) |
| Integridad | SHA (*Secure Hash Algorithms*) |

El nombre común de cada estándar **«Define el valor a asignar al metadato mínimo obligatorio «Nombre de
formato» de los documentos electrónicos.»** (anexo, letra c). El texto consolidado del BOE trae erratas
en algunas filas (por ejemplo «PMG» por PNG o «BebM» por WebM): se citan aquí por su nombre correcto,
que es el de su especificación formal en la misma fila.

### Política de firma y sello: formatos, perfiles y firmas longevas

La NTI de Política de firma y sello electrónicos y de certificados de la Administración (resolución de
27-10-2016):

- Qué es una política de firma: repite la definición del ENI y añade que **«Es de aplicación tanto a las
  firmas como a los sellos electrónicos.»** (II.1). Se identifica por nombre, versión, **«Identificador
  (OID Object IDentifier) de la política»** y **«URI (Uniform Resource Identifier) de referencia de la
  política»**, entre otros datos (II.2); la política particular debe estar disponible **«en formato XML (eXtensible Markup
  Language) y ASN.1 (Abstract Syntax Notation One)»** (II.5.3.d).
- Formatos de firma de contenido (III.4): se ajustan a la Decisión de Ejecución (UE) 2015/1506; **«Por
  compatibilidad con las políticas de firma anteriores, se permitirán aunque no se recomiendan»** XAdES
  (**«ETSI TS 101 903»**), CAdES (**«ETSI TS 101 733»**) y PAdES (**«ETSI TS 102 778-3»**).
- Perfil mínimo (III.4.3): **«El perfil mínimo de formato que se utilizará para la generación de firmas de
  contenido en el marco de una política será «-EPES», esto es, clase básica (BES) añadiendo información
  sobre la política de firma y sello.»**
- Valores del metadato «Tipo de firma» (III.4.4.a): **«XAdES internally detached signature»**, **«XAdES
  enveloped signature»**, **«CAdES detached/explicit signature»**, **«CAdES attached/implicit
  signature»**, **«PAdES»** y sus variantes «(Decision 1506)».
- Antes de firmar, el servicio verifica la validez del certificado: si está revocado o suspendido, su
  periodo de validez, la cadena de certificación y que lo haya expedido **«un Prestador de Servicios de
  Confianza Cualificado, incluido en la TSL del país emisor.»** Si algo falla, **«el proceso de firma se
  interrumpirá.»** (III.6.2.b).
- Contrafirma (III.6.5): cuando un segundo firmante ratifica la firma del primero **«se utilizará la
  etiqueta correspondiente, CounterSignature»**; si las firmas son del mismo nivel, cada una se representa
  como firma independiente (III.6.6).
- Validación de la fecha (III.7.4.a): **«Si se ha realizado el sellado de tiempo, el sello de tiempo más
  antiguo dentro de la estructura de la firma se utilizará para determinar la fecha de la firma/sello.»**;
  sin sello de tiempo, **«la fecha y hora de la firma tendrán carácter indicativo»**.
- Periodo de precaución (IV.1.5): la política **«podrá establecer»** uno, que podrá ser **«como mínimo, el tiempo máximo permitido para el refresco completo de
  las CRLs (Certificate Revocation Lists) o el tiempo máximo de actualización del estado del certificado
  en el servicio OCSP (Online Certificate Status Protocol)»**.
- Firma longeva (IV.3.1): **«el firmante o el verificador de la firma incluirá un sello de tiempo que
  permita garantizar que el certificado era válido en el momento en que se realizó la firma.»** Para
  convertir una firma en longeva se verifica, se completa con las referencias a los certificados de la
  cadena y a sus informaciones de estado (CRL u OCSP) y se aplica el sellado de tiempo a esas referencias (IV.3.2). Su
  validez se mantiene **«resellando la firma/sello antes de la caducidad del certificado de la TSA
  (Autoridad de sellado de tiempo) que realizó el sello de tiempo anterior»** (III.7.7); y frente a la
  obsolescencia de algoritmos se usa el resellado **«con un algoritmo más robusto»** (II.7.5.a).
- Certificados (IV.1.2): **«Se presumirán válidos los certificados cualificados que usen los ciudadanos
  en las firmas y sellos electrónicos.»**
- Algoritmos (III.5.3): para entornos de alta seguridad, según el criterio del CCN, se aplican **«las
  recomendaciones revisadas de la CCN-STIC 405 así como en la norma CCN-STIC 807 del Esquema Nacional de
  Seguridad relativa al uso de criptografía.»**

Una salvedad: esta NTI remite todavía, para la seguridad de los depósitos de firmas, al **«Real Decreto
3/2010, de 8 de enero»** (II.7.2.b), el ENS derogado.

## 5. El Esquema Nacional de Seguridad

### Objeto y ámbito

Artículo 1.2 del Real Decreto 311/2022: **«El ENS está constituido por los principios básicos y requisitos
mínimos necesarios para una protección adecuada de la información tratada y los servicios prestados por
las entidades de su ámbito de aplicación, con objeto de asegurar el acceso, la confidencialidad, la
integridad, la trazabilidad, la autenticidad, la disponibilidad y la conservación de los datos, la
información y los servicios utilizados por medios electrónicos que gestionen en el ejercicio de sus
competencias.»** Esa enumeración tiene siete palabras; las dimensiones de seguridad que sirven para
categorizar un sistema son cinco (anexo I, más abajo). El acceso y la conservación aparecen en el
artículo 1.2 como fines, no como dimensiones.

Ámbito: todo el sector público del artículo 2 de la Ley 40/2015 (artículo 2.1, ya citado), los sistemas
que tratan información clasificada (2.2) y el sector privado que trabaja para el público (2.3): **«Este
real decreto también se aplica a los sistemas de información de las entidades del sector privado,
incluida la obligación de contar con la política de seguridad a que se refiere el artículo 12, cuando,
de acuerdo con la normativa aplicable y en virtud de una relación contractual, presten servicios o
provean soluciones a las entidades del sector público para el ejercicio por estas de sus competencias y
potestades administrativas.»** Por eso los pliegos de los contratos públicos **«contemplarán todos
aquellos requisitos necesarios para asegurar la conformidad con el ENS de los sistemas de información en
los que se sustenten los servicios prestados por los contratistas»** (2.3, párrafo tercero). Si el
sistema trata datos personales, se aplica además la normativa de protección de datos, y **«prevalecerán
las medidas a implantar como consecuencia del análisis de riesgos y, en su caso, de la evaluación de
impacto»** cuando resulten más exigentes (artículo 3.3; la protección de datos es el tema 10 del común).

### Los siete principios básicos

Artículo 5: **«a) Seguridad como proceso integral. b) Gestión de la seguridad basada en los riesgos.
c) Prevención, detección, respuesta y conservación. d) Existencia de líneas de defensa. e) Vigilancia
continua. f) Reevaluación periódica. g) Diferenciación de responsabilidades.»**

Lo que cada uno exige, en las palabras de la norma:

- Proceso integral (6.1): la seguridad la forman **«todos los elementos humanos, materiales, técnicos,
  jurídicos y organizativos relacionados con el sistema de información»**, y el principio **«excluye
  cualquier actuación puntual o tratamiento coyuntural.»**
- Riesgos (7.1): **«El análisis y la gestión de los riesgos es parte esencial del proceso de seguridad,
  debiendo constituir una actividad continua y permanentemente actualizada.»**
- Prevención, detección, respuesta y conservación (8): las de detección **«irán dirigidas a descubrir la
  presencia de un ciberincidente»** (8.3); las de respuesta, **«a la restauración de la información y los
  servicios»** (8.4).
- Líneas de defensa (9): **«múltiples capas de seguridad»**, de forma que, si una cae, se pueda reaccionar
  y minimizar el impacto; han de ser de **«naturaleza organizativa, física y lógica.»** (9.2).
- Vigilancia continua y reevaluación (10): la primera permite **«la detección de actividades o
  comportamientos anómalos y su oportuna respuesta»**; la segunda, reevaluar y actualizar las medidas.
- Diferenciación de responsabilidades (11.1): **«se diferenciará el responsable de la información, el
  responsable del servicio, el responsable de la seguridad y el responsable del sistema.»** Y (11.2)
  **«La responsabilidad de la seguridad de los sistemas de información estará diferenciada de la
  responsabilidad sobre la explotación de los sistemas de información concernidos.»**

### Los cuatro responsables, y dónde está el operador

Artículo 13.2, funciones:

| Responsable | Función |
|---|---|
| De la información | **«determinará los requisitos de la información tratada»** |
| Del servicio | **«determinará los requisitos de los servicios prestados.»** |
| De la seguridad | **«determinará las decisiones para satisfacer los requisitos de seguridad de la información y de los servicios, supervisará la implantación de las medidas necesarias para garantizar que se satisfacen los requisitos y reportará sobre estas cuestiones.»** |
| Del sistema | **«se encargará de desarrollar la forma concreta de implementar la seguridad en el sistema y de la supervisión de la operación diaria del mismo, pudiendo delegar en administradores u operadores bajo su responsabilidad.»** |

El operador informático aparece nombrado ahí: actúa por delegación del responsable del sistema. Y una
regla (13.3): **«El responsable de la seguridad será distinto del responsable del sistema,
no debiendo existir dependencia jerárquica entre ambos.»**, con medidas compensatorias si por falta
justificada de recursos no fuera posible. En los servicios externalizados, el contratista designa, **«salvo por causa justificada y
documentada»**, un **«POC (Punto o Persona de Contacto) para la seguridad de la información tratada y el servicio
prestado»** (13.5).

### La política de seguridad y los quince requisitos mínimos

La política de seguridad es **«el conjunto de directrices que rigen la forma en que una organización
gestiona y protege la información que trata y los servicios que presta»** (12.1). Cada entidad con
personalidad jurídica propia del ámbito del artículo 2 **«deberá contar con una política de seguridad
formalmente aprobada por el órgano competente»** (12.2), aunque puede quedar incluida en la de la
Administración de la que depende. Se desarrolla con quince requisitos mínimos (12.6):

- **«a) Organización e implantación del proceso de seguridad.**
- **b) Análisis y gestión de los riesgos.**
- **c) Gestión de personal.**
- **d) Profesionalidad.**
- **e) Autorización y control de los accesos.**
- **f) Protección de las instalaciones.**
- **g) Adquisición de productos de seguridad y contratación de servicios de seguridad.**
- **h) Mínimo privilegio.**
- **i) Integridad y actualización del sistema.**
- **j) Protección de la información almacenada y en tránsito.**
- **k) Prevención ante otros sistemas de información interconectados.**
- **l) Registro de la actividad y detección de código dañino.**
- **m) Incidentes de seguridad.**
- **n) Continuidad de la actividad.**
- **ñ) Mejora continua del proceso de seguridad.»**

Se exigen **«en proporción a los riesgos identificados en cada sistema»**, y alguno **«podrá obviarse en
sistemas sin riesgos significativos.»** (12.7). Para cumplirlos se aplican las medidas del anexo II según
los activos, la categoría y las decisiones de gestión de riesgos (artículo 28.1); las medidas
seleccionadas se formalizan **«en un documento denominado Declaración de Aplicabilidad, firmado por el
responsable de la seguridad.»** (28.2), y pueden sustituirse por medidas compensatorias justificadas
(28.3).

### Dimensiones, niveles y categorías

Las cinco dimensiones (anexo I, apartado 2), **«que se identificarán por sus correspondientes iniciales
en mayúsculas»**: **«a) Confidencialidad [C]. b) Integridad [I]. c) Trazabilidad [T]. d) Autenticidad
[A]. e) Disponibilidad [D].»** Frente a la tríada clásica de la seguridad de la información
(confidencialidad, integridad y disponibilidad, tema 14), el ENS añade la trazabilidad y la
autenticidad.

Son dos escalas distintas que se confunden:

| Escala | A qué se aplica | Valores (anexo I) |
|---|---|---|
| Nivel de seguridad | A cada dimensión, por separado | **«BAJO, MEDIO o ALTO»**; **«Si una dimensión de seguridad no se ve afectada, no se adscribirá a ningún nivel.»** |
| Categoría de seguridad | Al sistema entero | **«BÁSICA, MEDIA y ALTA»** |

El nivel depende del perjuicio que causaría un incidente: **«perjuicio limitado»** (BAJO), **«perjuicio
grave»** (MEDIO) o **«perjuicio muy grave»** (ALTO) sobre las funciones de la organización, sus activos o
las personas. Y si un sistema trata varias informaciones y servicios, **«el nivel de seguridad del
sistema en cada dimensión será el mayor de los establecidos para cada información y cada servicio.»**

La regla que va de niveles a categoría (anexo I, apartado 4.1):

- **«a) Un sistema de información será de categoría ALTA si alguna de sus dimensiones de seguridad
  alcanza el nivel de seguridad ALTO.»**
- **«b) Un sistema de información será de categoría MEDIA si alguna de sus dimensiones de seguridad
  alcanza el nivel de seguridad MEDIO, y ninguna alcanza un nivel de seguridad superior.»**
- **«c) Un sistema de información será de categoría BÁSICA si alguna de sus dimensiones de seguridad
  alcanza el nivel BAJO, y ninguna alcanza un nivel superior.»**

La categoría la fija la dimensión más exigente: basta una para arrastrar al sistema entero. Quién decide:
las valoraciones las hace el responsable de la información o del servicio, y **«la determinación de la
categoría de seguridad del sistema corresponderá al responsable o responsables de la seguridad.»**
(artículo 41.2). Y no es una etiqueta para siempre: **«Anualmente, o siempre que se produzcan
modificaciones significativas en los citados criterios de determinación, deberá re-evaluarse la
categoría de seguridad de los sistemas de información concernidos.»** (anexo I, apartado 1).

### Las medidas del anexo II

Las medidas se dividen en tres grupos (anexo II, 1.2): **«a) Marco organizativo [org]»**, relacionado con
la organización global de la seguridad; **«b) Marco operacional [op]»**, para proteger la operación del
sistema; y **«c) Medidas de protección [mp]»**, que protegen activos concretos. La selección sigue cinco
pasos (2.1): identificar los activos, determinar las dimensiones relevantes, el nivel de cada una y la
categoría del sistema, y elegir las medidas con sus refuerzos. El tema 14 recoge las medidas que tocan al
puesto (perímetro, VPN, correo, código dañino, firma).

### Auditoría, conformidad e incidentes

- Auditoría (artículo 31.1): **«Los sistemas de información comprendidos en el ámbito de aplicación de
  este real decreto serán objeto de una auditoría regular ordinaria, al menos cada dos años, que
  verifique el cumplimiento de los requerimientos del ENS.»** Además, auditoría extraordinaria
  **«siempre que se produzcan modificaciones sustanciales»**, que reinicia el cómputo de los dos años; el
  plazo **«podrá extenderse durante tres meses»** por fuerza mayor. El informe se presenta al responsable
  del sistema y al de la seguridad (31.5); en categoría ALTA, ante deficiencias graves, el responsable del
  sistema **«podrá suspender temporalmente el tratamiento de informaciones, la prestación de servicios o
  la total operación del sistema»** (31.6).
- Conformidad (artículo 38.1): **«los sistemas de categoría MEDIA o ALTA precisarán de una auditoría para
  la certificación de su conformidad»**, mientras que **«los sistemas de categoría BÁSICA solo requerirán
  de una autoevaluación para su declaración de la conformidad, sin perjuicio de que se puedan someter
  igualmente a una auditoria de certificación.»** Las declaraciones y certificaciones se publican en el
  portal o la sede (38.2).
- Incidentes (artículo 33): el CCN articula la respuesta **«en torno a la estructura denominada
  CCN-CERT»** (33.1), y **«las entidades del sector público notificarán al CCN aquellos incidentes que
  tengan un impacto significativo en la seguridad de los sistemas de información concernidos»** (33.2).
  Las empresas privadas que prestan servicios al sector público notifican al **«INCIBE-CERT»**, que lo
  pone en conocimiento del CCN-CERT (33.7). Tras el incidente, **«el CCN-CERT determinará técnicamente el
  riesgo de reconexión del sistema o sistemas afectados»** (33.6).

| Categoría | Cómo se acredita la conformidad | Auditoría regular |
|---|---|---|
| BÁSICA | Autoevaluación (o auditoría de certificación, si se quiere) | Al menos cada dos años |
| MEDIA y ALTA | Auditoría de certificación | Al menos cada dos años |

### El desarrollo del ENS y las guías del CCN

La disposición adicional segunda, en su redacción vigente desde el 07-11-2024: **«la persona titular del
Ministerio para la Transformación Digital y de la Función Pública, a propuesta de la Comisión Sectorial
de Administración Electrónica y a iniciativa del Centro Criptológico Nacional, aprobará las instrucciones
técnicas de seguridad de obligado cumplimiento, que se publicarán mediante Resolución de la persona
titular de la Secretaría de Estado de Función Pública.»** Y además: **«el CCN, en el ejercicio de sus
competencias, elaborará y difundirá las correspondientes guías de seguridad de las tecnologías de la
información y la comunicación (guías CCN-STIC), particularmente de la serie 800, que se incorporarán al
conjunto documental utilizado para la realización de las auditorías de seguridad.»**

La diferencia: las instrucciones técnicas de seguridad son de obligado cumplimiento y
las aprueba el Ministerio; las guías CCN-STIC las elabora el CCN y orientan cómo aplicar el ENS. El
artículo 34.1.b) lo dice así: **«las series de documentos CCN-STIC (CCN-Seguridad de las Tecnologías de
Información y la Comunicación), elaboradas por el CCN, ofrecerán normas, instrucciones, guías,
recomendaciones y mejores prácticas para aplicar el ENS»**. Por último, el ENS **«se mantendrá actualizado
de manera permanente»** (artículo 39), igual que el ENI.

## 6. Aplicación práctica

Casos de puesto, resueltos con lo que dicen las normas citadas:

*Hay que escanear un contrato en papel para incorporarlo a un expediente.* Resolución mínima de 200
píxeles por pulgada, sea en blanco y negro, color o escala de grises; formato de imagen del Catálogo de
estándares (por ejemplo PDF/A, PNG, JPEG o TIFF); la imagen debe respetar la geometría del original y no
añadir nada; se le asignan los metadatos mínimos y, si procede, se firma (NTI de digitalización). Para
que tenga valor de copia auténtica, además, la debe expedir el órgano competente con los metadatos que
acreditan su condición de copia (Ley 39/2015, artículo 27.3.b).

*El escáner del registro empieza a sacar imágenes con bandas o recortadas.* La NTI de digitalización
exige operaciones de mantenimiento preventivo y comprobaciones rutinarias que garanticen imágenes fieles;
una imagen que no respeta la geometría o que añade marcas no cumple el apartado IV.3.

*¿En qué formato guardar para conservar a largo plazo un informe ofimático?* En el formato en que se
elaboró y, preferentemente, en un estándar abierto que preserve contenido, firma y metadatos (ENI,
artículo 23.1). El Catálogo admite PDF/A, que su especificación formal describe como formato para la
conservación a largo plazo, OpenDocument y Office Open XML *Strict*; RTF está «En abandono». Si un
formato deja de estar admitido, hay que migrar con copia auténtica y cambio de formato (ENI, 23.3;
Reglamento de 2021, 54.5).

*El reloj del servidor del registro se ha desviado diez minutos.* El ENI obliga a sincronizar con la hora
oficial (Real Instituto y Observatorio de la Armada) con precisión suficiente para que los plazos sean
ciertos (artículo 15), y la Ley 39/2015 exige que cada asiento conste con fecha y hora en orden temporal
(artículo 16.2 y 16.3). Un asiento con la hora mal puede dar por presentado fuera de plazo un escrito que
llegó a tiempo.

*Un ciudadano presenta en el registro electrónico un fichero con código malicioso.* El Reglamento de
2021 manda requerir al interesado que lo subsane (artículo 39.2). El ENS exige, entre sus requisitos
mínimos, la detección de código dañino (artículo 12.6.l).

*Un documento firmado hace ocho años: el certificado del firmante ya ha caducado. ¿Sigue valiendo la
firma?* Si es una firma longeva, sí: lleva un sello de tiempo que prueba que el certificado era válido
cuando se firmó, y se mantiene resellándola antes de que caduque el certificado de la autoridad de
sellado (NTI de firma, IV.3 y III.7.7). Sin sello de tiempo, la fecha de la firma es sólo indicativa
(III.7.4.a).

*Se integra una aplicación de firma.* El perfil mínimo es -EPES; el servicio debe comprobar
antes de firmar que el certificado no está revocado ni suspendido, está en vigor y es de un prestador
cualificado incluido en la TSL, y si algo falla el proceso se interrumpe (NTI de firma, III.4.3 y
III.6.2). El metadato «Tipo de firma» del documento reflejará el formato (XAdES, CAdES o PAdES).

*Categorizar un sistema.* Un sistema de gestión de contenidos tiene, tras la valoración, confidencialidad
BAJO, integridad MEDIO, disponibilidad MEDIO, y trazabilidad y autenticidad BAJO. Ninguna dimensión llega
a ALTO y alguna llega a MEDIO: categoría MEDIA (anexo I, 4.1.b). Su conformidad exige auditoría de
certificación (artículo 38.1), y la auditoría regular, al menos cada dos años (artículo 31.1). Si en la
revisión anual la disponibilidad pasa a ALTO, el sistema entero pasa a ALTA.

*La empresa externa que mantiene el sistema de archivo de la RTVA, ¿tiene que cumplir el ENS?* Si la RTVA
está en el ámbito del ENS, el artículo 2.3 extiende el ENS a los sistemas del contratista que presta el
servicio, incluida la política de seguridad, y los pliegos deben exigir la conformidad. El contratista
designa, salvo causa justificada y documentada, un POC de seguridad (artículo 13.5) y, si sufre un incidente, notifica al INCIBE-CERT (artículo
33.7).

*¿Quién decide que un servidor se apaga tras una auditoría con deficiencias graves?* En un sistema de
categoría ALTA, el responsable del sistema, a la vista del dictamen (artículo 31.6). El operador actúa
por delegación del responsable del sistema (artículo 13.2.d); la decisión no es suya.

*Otra Administración pide a la RTVA una aplicación desarrollada a medida.* Si la RTVA es titular de los
derechos de propiedad intelectual y la información asociada no tiene especial protección, la Ley
40/2015 obliga a ponerla a disposición (artículo 157.1), y se puede acordar repercutir el coste. Si se
declara de fuentes abiertas, la licencia debe garantizar las cuatro libertades del artículo 16.2 del ENI,
y se procurará la EUPL. (Que esto alcance a la RTVA depende de su encaje en el artículo 2, que no
consta en ninguna norma leída: epígrafe 1.)

## Normativa que el tema invoca

| Norma | Qué se usa | Redacción |
|---|---|---|
| Ley 39/2015, de 1 de octubre (BOE-A-2015-10565) | Arts. 2, 9, 10, 14, 16, 17, 26, 27, 43 y 70; disposición derogatoria única | Arts. 9 y 10 vigentes desde 30-06-2022; los demás, originales (02-10-2016) |
| Ley 40/2015, de 1 de octubre (BOE-A-2015-10566) | Arts. 2, 38 a 46, 155 a 158 | Art. 155 vigente desde 06-11-2019; los demás, originales (02-10-2016) |
| Real Decreto 203/2021, de 30 de marzo (BOE-A-2021-5032) | Arts. 1 a 3, 5.3, 26, 27, 29.4, 39, 47, 50, 51, 54, 55, 60 a 62 | Art. 27 vigente desde 02-04-2025; los demás, originales (02-04-2021) |
| Real Decreto 4/2010, de 8 de enero, ENI (BOE-A-2010-1331) | Arts. 1, 3 a 18, 20 a 29; disposiciones adicionales primera y segunda; anexo (glosario) | Disposición adicional primera vigente desde 07-11-2024; arts. 9, 11, 14, 16, 17, 18 y anexo desde 02-04-2021; los demás, originales (30-01-2010) |
| Real Decreto 311/2022, de 3 de mayo, ENS (BOE-A-2022-7191) | Arts. 1 a 3, 5 a 13, 28, 31, 33 a 35, 38, 39 y 41; disposición adicional segunda; disposición derogatoria; anexos I y II (apartados 1 y 2) | Disposición adicional segunda vigente desde 07-11-2024; lo demás, original (05-05-2022) |
| Resoluciones de 19-07-2011 de la Secretaría de Estado para la Función Pública: NTI de Digitalización de Documentos (BOE-A-2011-13168), de Documento Electrónico (BOE-A-2011-13169) y de Expediente Electrónico (BOE-A-2011-13170) | Componentes, metadatos mínimos, resolución, proceso de digitalización, índice | Originales |
| Resolución de 03-10-2012, NTI de Catálogo de estándares (BOE-A-2012-13501) | Estados y formatos | Original |
| Resolución de 27-10-2016, NTI de Política de firma y sello electrónicos y de certificados de la Administración (BOE-A-2016-10146) | Formatos, perfil -EPES, creación, validación, firmas longevas | Original |
| Resolución de 22-07-2021, NTI de Modelo de datos para el intercambio de asientos entre las entidades registrales, SICRES4 (BOE-A-2021-13749) | Sustitución de SICRES3; preámbulo sobre el fundamento del ENI | Original |
| Ley 9/2007, de la Administración de la Junta de Andalucía, art. 54.1; Ley 18/2007, art. 5; acuerdo de fusión de CSRTV, apartado Primero.3 | Naturaleza de la RTVA y de CSRTV | Tomados de los temas 2 y 5 del común |

## Lo que este tema no da, y dónde está

- La firma electrónica en el Reglamento eIDAS, sus tres clases, los certificados, los prestadores de
  servicios de confianza, el sellado de tiempo como servicio y el software de la FNMT: tema 14. Las
  medidas concretas del anexo II del ENS sobre perímetro, VPN, correo y código dañino: también tema 14.
- HTTPS, TLS y el direccionamiento IP: tema 13.
- La protección de datos (Reglamento General de Protección de Datos y Ley Orgánica 3/2018): tema 10 del
  común.
- El procedimiento administrativo en sí (plazos, recursos, acto administrativo): no lo pide este
  enunciado.
- La normativa andaluza de administración electrónica (decretos de la Junta de Andalucía): no se ha
  volcado ni leído; el enunciado habla de «normativa técnica básica» y no la nombra.
- En qué letra del artículo 2 de las Leyes 39 y 40/2015 encajan la RTVA y CSRTV: ninguna norma leída lo
  dice; el tema da la deducción y la marca como tal.
- Si la RTVA o CSRTV tienen política de seguridad aprobada, sistemas categorizados en el ENS, declaración
  de conformidad, sede electrónica o registro electrónico propio: no consta en ningún documento
  publicado leído.
- El texto de las NTI de copiado auténtico, de política de gestión de documentos, de requisitos de
  conexión a la red, de intermediación de datos, de modelos de datos y de reutilización: no se han leído
  más allá de su título; el tema sólo dice que existen y están vigentes.
- Las NTI de las letras m) a v): no constan publicadas en la búsqueda del BOE consolidado.
- El contenido de las instrucciones técnicas de seguridad y de las guías CCN-STIC (salvo la mención de
  las guías 405 y 807 en la NTI de firma): no se han leído.
- El portal de administración electrónica del Gobierno (administracionelectronica.gob.es): no se pudo
  leer.

## Trazabilidad

Todas las fuentes se leyeron el 05-10-2026 en el texto consolidado del BOE (volcado con la herramienta
del proyecto), con la redacción vigente ese día. El encargo fija «hoy» en 24-09-2026; la tabla de
redacciones de cada norma muestra que la última reforma de cualquiera de ellas es de 02-04-2025, de modo
que el texto es el mismo en las dos fechas.

| Fuente | Qué sostiene |
|---|---|
| Ley 39/2015 (BOE-A-2015-10565) | Ámbito, identificación y firma de interesados, obligados a relacionarse electrónicamente, registro, archivo, documento electrónico, copias, notificación electrónica, expediente, derogación de la Ley 11/2007 |
| Ley 40/2015 (BOE-A-2015-10566) | Ámbito, sede y portal, sello, actuación automatizada, CSV, firma del personal, entornos cerrados, interoperabilidad de la firma, archivo, transmisión de datos, los dos esquemas, reutilización |
| Real Decreto 203/2021 (BOE-A-2021-5032) | Objeto, principios, cambio de canal, clave concertada, atributos de certificados, registro y SIR, referencia temporal, copias, índice del expediente, conservación y archivo electrónico único, intermediación de datos; remisiones al Real Decreto 3/2010 |
| Real Decreto 4/2010 (BOE-A-2010-1331) | Objeto, prevalencia, principios, dimensiones, nodos, inventarios, estándares, Red SARA, direccionamiento, hora oficial, licencias, política de firma, plataformas de validación, conservación, conformidad, lista de NTI y su aprobación, glosario; remisiones a la Ley 11/2007 y a la Ley Orgánica 15/1999 |
| Real Decreto 311/2022 (BOE-A-2022-7191) | Objeto, ámbito, principios, responsables, política y requisitos mínimos, declaración de aplicabilidad, auditoría, incidentes, conformidad, categorías, anexos I y II, desarrollo y guías |
| NTI de Digitalización, Documento electrónico, Expediente electrónico, Catálogo de estándares, Política de firma y sello (2016) y SICRES4 (2021), en el BOE | Componentes, metadatos, resolución mínima, proceso, índice, formatos y estados, perfiles y validación de firma, firmas longevas, sustituciones |
| Búsqueda por título «Norma Técnica de Interoperabilidad» en la legislación consolidada del BOE, con su campo de vigencia (05-10-2026) | Relación de NTI publicadas y vigentes |
| Temas 2 y 5 del común | Definición de agencia (art. 54.1 de la Ley 9/2007), naturaleza de la RTVA y de CSRTV |

Oficio sin norma detrás, y así se declara: la selección de normas que el tema entiende por «normativa
técnica básica»; las dos funciones clásicas del registro (dar fe y encaminar); la comparación
del ENS con la tríada clásica de la seguridad; la deducción sobre el encaje de la RTVA y CSRTV en el artículo 2; el ejemplo de las
cuatro dimensiones de la interoperabilidad con dos registros; la comparación del índice firmado con el
foliado en papel; el paralelo entre el plan de direccionamiento y las direcciones privadas del tema 13;
la explicación de qué es un archivo electrónico frente a un disco con carpetas y del sistema de gestión
documental; y los casos de la aplicación práctica, que aplican las normas citadas a supuestos inventados.
