# Esquema · Tema 3 del específico de Documentación · Internet

Telegrama. **Cada línea lleva delante de dónde sale**: `[RD635]` = Real Decreto 635/2015, depósito
legal en línea · `[STC27]` = Sentencia 27/2020 del Tribunal Constitucional · `[EBU]` = EBU Tech 3293,
EBUCore v1.10 · `[W3C]` = documentación de RDF del consorcio de la web · `[Google]` y `[DDG]` =
ayuda de los propios buscadores · `[uso]` = plantilla oficial, **sin documento**.

**Cabecera.** **8 preguntas** · **6 verificadas en documento** —dos en el BOE, una en la Unión
Europea de Radiodifusión, una en el W3C y dos en la ayuda de los buscadores— · **2 sólo con
plantilla**.

<!-- indice -->

## Índice

- [Lo que hay que llevar sabido](#lo-que-hay-que-llevar-sabido)
- [Buscar](#buscar)
- [RDF y los datos enlazados](#rdf-y-los-datos-enlazados)
- [EBUCore](#ebucore)
- [El archivo de la web](#el-archivo-de-la-web)
- [Lo que un usuario cuelga](#lo-que-un-usuario-cuelga)

<!-- /indice -->

## Lo que hay que llevar sabido

| Pregunta | Respuesta | De dónde |
|---|---|---|
| Teatro/novela + cine/televisión | **(teatro OR novela) AND (cine OR televisión)** | `[uso]` |
| Base de los datos enlazados | **RDF** | `[W3C]` |
| Contenido de usuario en redes | **Consentimiento previo y expreso** | `[STC27]` |
| Documentos PDF en Google | **filetype:pdf** | `[Google]` |
| Año de lanzamiento de «X» | **2006** | `[uso]` |
| EBUCore | **Conjunto abierto y adaptable** | `[EBU]` |
| Archivo de la Web Española | **Modelo mixto: masivas + selectivas** | `[uso]` + `[RD635]` |
| DuckDuckGo | **Motor de búsqueda con atajos «Bangs»** | `[DDG]` |

## Buscar

- `[uso]` · **TRADUCCIÓN DEL ENUNCIADO**: «obras de teatro **y** novelas» = **teatro OR novela** (una
  cosa **o** la otra) · «cine **o** televisión» = **cine OR televisión** · las dos condiciones **a la
  vez** = **AND** entre paréntesis.
- **LA TRAMPA ES DE LENGUA**: el «y» del castellano **no es el AND booleano**. «Teatro y novelas»
  quiere decir **cualquiera de las dos**.
- **Falsos**: **(teatro AND novela) AND (cine AND televisión)** = pide **las cuatro a la vez**, la más
  restrictiva · **sin paréntesis** = el orden de evaluación cambia el sentido; **el error son los
  paréntesis que faltan** · **NEAR** = operador de **proximidad**, ni hace falta ni hay paréntesis.
- **COMPROBACIÓN RÁPIDA: la buena tiene dos OR y un AND.**
- `[Google]` · «**Para encontrar documentos de un tipo de archivo concreto: escribe filetype: delante
  del tipo de archivo**». Ejemplo de la propia ayuda: «**efecto fotoeléctrico publicación
  filetype:pdf**».
- `[Google]` · Regla de sintaxis: «**No incluyas espacios entre el operador y el término de
  búsqueda**»; «**La búsqueda [ site:elmundo.es ] funciona, pero la búsqueda [ site: elmundo.es ],
  no**».
- **Falsos**: **site:pdf** → `site:` **existe**, pero restringe **por sitio**; es el fino ·
  **source:pdf** → no está en la ayuda de Búsqueda; existe en el buscador de noticias ·
  **format:pdf** → **el invento**, y el más lógico en castellano.
- `[DDG]` · «**Bangs are shortcuts that quickly take you to search results on other sites**».
  Ejemplo: «**A search for !w filter bubble will take you directly to Wikipedia**». Antigüedad:
  «**We've had bangs since 2008 as part of our geek roots**».
- `[DDG]` · **El aviso que se hace a sí mismo**: «**because your search is actually taking place on
  that other site, you are subject to that site's policies**».
- **POR QUÉ NO ES METABUSCADOR**: un metabuscador **consulta varios y agrega en su página**; el bang
  hace lo contrario, **te manda fuera**.

## RDF y los datos enlazados

- `[W3C]` · «**The Resource Description Framework (RDF) is a framework for expressing information
  about resources**»; «**Resources can be anything, including documents, people, physical objects,
  and abstract concepts**».
- `[W3C]` · **El enlace es literal**: «**Such uses of RDF are often qualified as Linked Data**».
- **REGLA DE LAS CUATRO SIGLAS**: **HTTP transporta · URL localiza · XML escribe · RDF significa.**
  La pregunta pide **el que da significado**.
- **AVISO**: la página del consorcio responde «prohibido»; se ha leído **su repositorio de edición**,
  que es la versión de trabajo posterior. **Lo citado no está entre los cambios.**

## EBUCore

- `[EBU]` · **ABIERTO Y ADAPTABLE**: «**'The EBUCore is a metadata specification designed for users
  with different needs'**»; «**EBUCore has been designed to support customisation in many ways**»;
  «**EBUCore provides two mechanisms for extensions**».
- **Falso «no permite audios»** → «**EBUCore has been designed to describe audio, video and other
  resources**», y además incorpora «**a unique representation of the ITU-R BS.2076 Audio Data Model
  (ADM)**».
- **Falso «sólo para archivos»** → los ámbitos son «**archives, exchange and production**»; y
  «**Beyond production, EBUCore can be used to describe content for distribution**».
- **Falso «no permite partes»** → «**Can I use the 'part' element to fragment my data? Yes.**»; «**The
  'part' element is extremely versatile**»; sirve hasta para series: «**each part describing an
  episode of that series or season**».
- **Gratis, y lo pide el temario**: «**EBUCore is based on the Dublin Core to maximise
  interoperability**»; «**The core set of metadata presented in EBUCore is the Dublin Core for
  media**»; la ontología se actualizó «**to match EBU's CCDM (Tech 3351) needs**».

## El archivo de la web

- **AVISO**: la página del archivo **no se ha podido consultar** —cinco rutas, agente de navegador—.
  Lo que sigue es **la norma que lo ordena**.
- `[RD635]` art. 3 · Objeto de depósito: «**todo tipo de sitios web**», «**cualquiera que sea el
  dominio que albergue la publicación**», con **una** de tres condiciones: **lengua española
  oficial**, **editor domiciliado en España** o **dominio vinculado al territorio español**.
  → **MATA la opción «sólo el dominio .es»**.
- `[RD635]` art. 4 · **Sólo tres exclusiones**: correspondencia privada · contenidos **sólo en red
  privada** · ficheros personales de acceso restringido. **Los medios NO están.** → **mata la opción
  «no recopila medios»**.
- `[RD635]` art. 1.3 · «**El depósito de una misma publicación en soporte tangible no exime del
  depósito de la misma en línea**».
- `[RD635]` art. 6.1 · Centros de conservación: «**la Biblioteca Nacional de España y los que
  determinen las Comunidades Autónomas**».
- `[RD635]` art. 6.2 · **EL CRITERIO**: «**siguiendo el criterio de lograr la mejor representatividad
  del mundo de Internet y de conseguir una recolección lo más completa posible**».
  → «**lo más completa posible**» = **MASIVA** · «**la mejor representatividad**» = **SELECTIVA**.
  **Las dos a la vez = modelo mixto.**
- `[RD635]` art. 7.3 · Los **procedimientos de selección y captura** y **la frecuencia** los fija
  «**la Biblioteca Nacional de España, centro de conservación de ámbito estatal**», y los centros
  autonómicos.
- `[RD635]` art. 2.a) · **Captura** = recolección «**a partir del empleo de programas informáticos
  que llevan a cabo un proceso de seguimiento de enlaces**».

## Lo que un usuario cuelga

- `[STC27]` · **Caso**: un diario ilustró un suceso con la foto de la víctima **tomada de su perfil de
  Facebook, abierto al público**. Alegó libertad de información. **Amparo desestimado.**
- **Tesis del diario**: publicar en una red social «**constituye una suerte de consentimiento tácito
  para su posterior utilización por terceros**».
- **Respuesta del Tribunal**: «**No podemos aceptar esta premisa. El consentimiento solo ampara
  aquello que constituye el objeto de la declaración de voluntad. El titular del derecho fundamental
  debe autorizar el concreto acto de utilización de su imagen y los fines para los que la otorga**».
- **Consecuencia práctica**: «**El consentimiento prestado, por ejemplo, para la captación de la
  imagen no se extiende a otros actos posteriores, como por ejemplo su publicación o difusión**».
- **Cuenta abierta ≠ permiso**: ver la foto en una cuenta abierta «**no conlleva la autorización para
  hacer uso de esa fotografía y publicarla o divulgarla de una forma distinta**», porque no es el
  «**consentimiento expreso**» del art. 2.2 de la Ley Orgánica 1/1982.
- **Matiz que evita el error contrario**: ese consentimiento «**no requiere que sea un consentimiento
  formal (por ejemplo, dado por escrito), sí exige que se trate de un consentimiento inequívoco**».
- **Falsos**: «consiente en ser observado **en cualquier soporte**» = **la tesis del diario,
  rechazada** · «**24 horas**» = **no hay plazo de gracia** en ninguna parte · «**rótulo con
  autoría**» = **citar la fuente no sustituye al consentimiento**.
- **REGLA DE OFICIO**: la foto que un particular cuelga en su perfil **no es material de archivo
  disponible**.
