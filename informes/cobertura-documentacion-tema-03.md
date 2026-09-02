# Cobertura del tema 3 del específico de Documentación

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y
donde el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

- **Tema**: Internet.
- **Preguntas de la materia**: **8**.
- **Contestadas con el tema delante**: **8**.
- **Lagunas que hubo que cerrar**: **dos**, la de EBUCore y la del archivo de la web (abajo).
- **Preguntas verificadas en la fuente**: **6 de 8**.

## Una por una

| Cuadernillo · nº | Respuesta | Qué la sostiene | Nivel de la fuente | Epígrafe |
|---|---|---|---|---|
| 09 · 16 | b | Sólo la plantilla oficial | **Plantilla** | 1.1 |
| 09 · 25 | a | «The Resource Description Framework (RDF) is a framework for expressing information about resources» / «Such uses of RDF are often qualified as Linked Data» | **W3C** | 2 |
| 09 · 26 | b | «El titular del derecho fundamental debe autorizar el concreto acto de utilización de su imagen» | **BOE**, Sentencia 27/2020 | 5 |
| 09 · 46 | b | «Para encontrar documentos de un tipo de archivo concreto: escribe filetype: delante del tipo de archivo» | **Google**, ayuda oficial | 1.2 |
| 09 · 77 | c | Sólo la plantilla oficial | **Plantilla** | 6 |
| 09 · 85 | b | «EBUCore has been designed to support customisation in many ways» | **EBU Tech 3293** | 3 |
| 09 · 86 | c | «El criterio de lograr la mejor representatividad del mundo de Internet y de conseguir una recolección lo más completa posible» | Plantilla (**RD 635/2015** para el marco) | 4 |
| 09 · 96 | c | «Bangs are shortcuts that quickly take you to search results on other sites» | **DuckDuckGo**, página oficial | 1.3 |

## La pregunta que venía del volumen general

**La 26 estaba impresa en el bloque general y no era suya.** Su propio informe de cobertura la había
declarado «fuera del tema, con razón», anotando que **la doctrina del Tribunal Constitucional sobre
contenido generado por usuarios no es texto de la Constitución**. Pero es exactamente **el último
epígrafe del enunciado de este punto** —«redes sociales, YouTube y contenido generado por el usuario
(UGC)»—, de modo que aquí sí es suya. Se ha movido, y el banco general baja en una pregunta.

**Y al traerla se ha podido cerrar en su fuente**, que en el bloque general nunca se hizo. La
doctrina está en la **Sentencia 27/2020, de 24 de febrero**, publicada en el BOE: un diario ilustró
la noticia de un suceso violento con la fotografía de la víctima **tomada de su perfil de Facebook,
abierto y accesible al público**, y el Tribunal **desestimó su amparo**. La frase que contesta la
pregunta es literal: «**El titular del derecho fundamental debe autorizar el concreto acto de
utilización de su imagen y los fines para los que la otorga**».

## Las dos lagunas que hubo que cerrar

**1. EBUCore, tras seis rutas.** La organización que publica la especificación **bloquea su sitio a
toda consulta automática** —así consta ya en otro tema de este proyecto—, y las cinco primeras rutas
probadas devolvieron «prohibido» o «no existe»: la página de la publicación, la de la ontología, la
del área de metadatos, un servicio hermano y una ruta de descarga alternativa. **La sexta abrió**:
el PDF de la especificación, servido directamente desde el subdominio técnico. **Cincuenta y cuatro
páginas, versión 1.10, de abril de 2020**, anteriores al corte.

**Y con ella la pregunta cambió de naturaleza.** Sin fuente, era una pregunta de opinión sobre un
conjunto de metadatos; con la especificación delante, **las tres opciones falsas se desmienten una
por una con frases del propio documento**: que no describe audio lo niega su segunda línea, que sólo
sirve para archivos lo niega la enumeración «archives, exchange and production», y que no describe
partes lo niega **un apartado entero dedicado al elemento «part»**, con una pregunta frecuente que
dice literalmente «**Can I use the 'part' element to fragment my data? Yes.**».

**2. El archivo de la web, por la puerta de al lado.** La página del Archivo de la Web Española **no
se ha podido consultar**: la biblioteca que lo mantiene responde «prohibido» a toda consulta
automática, comprobado por **cinco rutas** con agente de usuario de navegador.

La ruta que sí funcionó fue **la norma que lo ordena**, que está en el BOE: el **Real Decreto
635/2015** del depósito legal de las publicaciones en línea. Y resultó dar **más de lo que la página
habría dado**, porque permite **descartar las tres opciones falsas con texto delante**:

- «Sólo recopila lo alojado en el dominio `.es`» → el artículo 3 dice «**cualquiera que sea el
  dominio que albergue la publicación**», y da **tres condiciones alternativas**, de las que el
  dominio español es sólo una.
- «No recopila medios de comunicación porque mantienen sus propios archivos» → el artículo 4 enumera
  **sólo tres exclusiones**, y los medios no están en ellas. Y el artículo 1 añade que tener el papel
  depositado **no exime del depósito en línea**.
- «Recopila archivos en la nube» → confunde el objeto con el sitio donde se guarda.

Y el criterio del **artículo 6.2** es literalmente el modelo mixto de la respuesta correcta:
«**lograr la mejor representatividad del mundo de Internet**» —lo selectivo— «**y conseguir una
recolección lo más completa posible**» —lo masivo—. El **artículo 7.3** lo remata encargando a la
Biblioteca Nacional los «**procedimientos de selección y captura**» y «**la frecuencia con la que se
realizarán dichas capturas**».

## Dónde el tema tuvo que ampliarse

**La expresión booleana** se contestaba con la plantilla, pero el tema añade **la razón por la que se
falla**: el «y» del castellano corriente no es el AND booleano. «Obras de teatro y novelas» significa
**cualquiera de las dos**, no las dos a la vez, y quien lo traduzca por AND pide documentos que
traten simultáneamente de teatro y de novela. El tema da además **una comprobación rápida de
examen**: la expresión correcta para este enunciado **tiene dos OR y un AND**, y sólo una opción lo
cumple.

**Los operadores de Google** se verifican en su ayuda, pero el tema explica **por qué el distractor
bueno es `site:pdf`**: `site:` **existe y funciona**, pero restringe por sitio, no por formato. De
las cuatro opciones, **sólo una está inventada** —`format:`—, y es precisamente la que suena mejor en
castellano.

**DuckDuckGo** se verifica en su página, y el tema añade **por qué no es un metabuscador**, que es la
opción falsa fina: un metabuscador **consulta varios buscadores y agrega los resultados en su propia
página**; el bang hace lo contrario, **manda al usuario fuera**. Y lo dice la propia página al
advertir que, al usarlo, «**you are subject to that site's policies**».

## Lo que este tema deja dicho que no puede sostener

- **El año de lanzamiento de la red social se apoya sólo en la plantilla.** La página institucional
  de la compañía abre y no da la fecha; la antigua página corporativa responde «no existe»; y el
  archivo del regulador de mercados que tendría el folleto de salida a bolsa **exige identificarse
  con un correo de contacto**, y **este proyecto no envía la dirección de su usuario a servicios
  ajenos**.
- **La página del Archivo de la Web Española no se ha podido consultar**, cinco rutas. El modelo
  mixto se sostiene en **los artículos 6 y 7 del real decreto**, no en la descripción del archivo.
- **La documentación del W3C se ha leído en el repositorio de edición del consorcio**, no en su
  página, que responde «prohibido». Es la **versión de trabajo posterior** a la vigente al corte, y
  el propio texto remite los cambios a otro documento: **lo que aquí se cita no está entre ellos**.
- **La expresión booleana se apoya en la plantilla**; lo que el tema añade es razonamiento.
- **Lo que el tema dice de `source:` en el buscador de noticias es uso profesional.**

## Lo que no se ha preguntado y conviene no descuidar

Que en Google **no puede haber espacio entre el operador y el término**; que **RDF puede escribirse
en XML pero no es XML**, y que las cuatro siglas de esa pregunta se ordenan como «**HTTP transporta,
URL localiza, XML escribe, RDF significa**»; que **EBUCore se basa en Dublin Core** y que su ontología
se actualizó para encajar con el **modelo conceptual de datos** que el propio temario cita en el
punto siguiente; que el depósito legal **no asigna número a las publicaciones en línea**, aunque su
editor pueda pedir un **ISBN**; y que el consentimiento del artículo 2.2 de la Ley Orgánica 1/1982
**no tiene que ser escrito, pero sí inequívoco**.
