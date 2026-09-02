# Esquema · Tema 2 del específico de Documentación · Documentación y tecnologías de la información

Telegrama. **Cada línea lleva delante de dónde sale**: `[25964-1]` y `[25964-2]` = muestra oficial de
la norma de tesauros · `[15707]` = muestra oficial de la norma del código de obras musicales ·
`[NISO]` = página oficial de ISO 25964 · `[ISSN]` = lista de códigos del Centro Internacional del
ISSN · `[L16/85]` = Ley del Patrimonio Histórico Español · `[uso]` = plantilla oficial, **sin norma
leída**.

**Cabecera.** **9 preguntas** · **4 con norma internacional**, **1 con la ley del patrimonio detrás**,
**4 sólo con plantilla**. **El texto íntegro de las normas ISO es de pago**: se ha leído **su muestra
oficial**, que trae portada, índice, introducción, objeto y parte de las definiciones.

<!-- indice -->

## Índice

- [Lo que hay que llevar sabido](#lo-que-hay-que-llevar-sabido)
- [El documento](#el-documento)
- [El proceso documental](#el-proceso-documental)
- [Los lenguajes documentales](#los-lenguajes-documentales)
- [Los códigos de identificación](#los-códigos-de-identificación)
- [La redacción digital](#la-redacción-digital)

<!-- /indice -->

## Lo que hay que llevar sabido

| Pregunta | Respuesta | De dónde |
|---|---|---|
| Tesauro = ¿qué lenguaje? | **Combinatorio POSTcoordinado** | `[25964-1]` 2.43 |
| ¿Modelo con base en Bayes? | **Probabilístico** | `[uso]` |
| Tesauro multilingüe **nuevo** | **Unidad estructural** | `[25964-2]` 6.2 |
| Curación de contenidos | **Seleccionar y compilar, agregar valor, difundir** | `[uso]` |
| Resumen más breve | **Indicativo** | `[uso]` |
| Código de obras musicales | **ISWC** | `[15707]` |
| Redacción digital | **Aplicaciones que centralizan el control** | `[uso]` |
| Objetivo de la selección | **Mayor valor patrimonial y utilidad** | `[uso]` + `[L16/85]` |
| «Tesauros e interoperabilidad…» | **ISO 25964** | `[NISO]` |

## El documento

- `[25964-1]` 2.15 · **DOCUMENTO = «any resource that can be classified or indexed in order that the
  data or information in it can be retrieved»**. **No dice papel, ni texto, ni soporte**: dice
  **recurso indizable y recuperable**. Por eso el plano, el corte de voz y la foto fija **son
  documento igual que el guion**.
- `[L16/85]` art. 49.1 · **«toda expresión en lenguaje natural o convencional y cualquier otra
  expresión gráfica, sonora o en imagen, recogidas en cualquier tipo de soporte material, incluso los
  soportes informáticos»**. **Excluye: «los ejemplares no originales de ediciones».**
- `[L16/85]` art. 49.2 · **Patrimonio Documental**: lo generado por entidades públicas y por «**las
  personas jurídicas en cuyo capital participe mayoritariamente el Estado**» → **el archivo de RTVE
  lo es por ley**, no por decisión de la casa.
- `[L16/85]` art. 55 · **Eliminar exige autorización**; y **«En ningún caso se podrán destruir tales
  documentos en tanto subsista su valor probatorio de derechos y obligaciones»**.
- `[L16/85]` art. 58 · Califica una **Comisión Superior Calificadora de Documentos Administrativos**.
- **AVISO de método**: esta ley **numera los artículos con letra** («Artículo cuarenta y nueve»), así
  que las lentes por artículo no la reconocen. Se hizo una copia con los rótulos en cifra.

## El proceso documental

- `[uso]` · **SELECCIÓN → «identificar y conservar los documentos de mayor valor patrimonial y
  utilidad para los usuarios».** **Dos criterios**: el **patrimonial** mira al pasado, la **utilidad**
  al futuro.
- **Falsos y por qué caen contra la ley**: «conservar **todos**» = **no es selección**, y la ley
  regula la eliminación · «eliminar por **calidad técnica**» = **criterio equivocado**, la ley habla
  de **valor probatorio** · «**digitalizar todos**» = confunde **selección con preservación**; es la
  selección la que decide qué se digitaliza.
- `[uso]` · **RESUMEN: indicativo < informativo < analítico.** **Indicativo = de qué trata**, sin
  resultados → **el más breve**. **Informativo = el contenido**, puede sustituir a la lectura.
  **Analítico = añade valoración**. **«Objetivo» no es un tipo**: es una exigencia de todos.
- **AVISO**: la norma de resúmenes, **ISO 214**, **no se ha podido consultar** —de pago y sin
  muestra—.
- `[uso]` · **RECUPERACIÓN, los tres clásicos**: **booleano** = cumple o no, **conjunto sin orden** ·
  **vectorial** = ordena por **semejanza geométrica** (coseno) · **probabilístico** = ordena por
  **probabilidad de relevancia**, y **actualizarla con la evidencia es Bayes** ← **la respuesta**.
  **«Cognitivo» no es clásico**: es enfoque posterior centrado en el usuario.
- `[uso]` · **CURACIÓN = seleccionar + compilar + para un tema y un público + agregar valor +
  difundir.** **Los cuatro elementos sólo están en la correcta.**
- **Falsos**: «información **identificada como falsa**» = **verificación** · «**elaborar contenidos
  originales**» = **creación**, lo contrario: el curador **no crea, elige lo ajeno** · «conservar
  **soportes obsoletos**» = **preservación**.
- **TRAMPA DE IDIOMA**: *curación* aquí no es sanar: viene de *curation*, **lo que hace el
  conservador de un museo**. Quien piense en «curar» irá a la de conservación.

## Los lenguajes documentales

- `[25964-1]` 2.44 · **PREcoordinación = combinar «at the time of its construction or at the time of
  using it for indexing or classification»** → **al construir o al indizar**.
- `[25964-1]` 2.43 · **POSTcoordinación = combinar «at the time of searching»** → **al buscar**.
  **TODA LA DIFERENCIA ESTÁ EN EL MOMENTO.**
- **Ejemplo de la propia norma**: «**microwaves AND radiation**» recupera documentos sobre radiación
  de microondas **indizados por separado**.
- **TESAURO = POSTCOORDINADO**: guarda los conceptos sueltos y **el usuario los combina al
  consultar**.
- **Falsos**: «**precoordinado** y jerárquico» → **jerárquico sí, precoordinado no**; es el fino ·
  «precombinado» → lo mismo · «**libre** postcoordinado» → **postcoordinado acierta, «libre»
  falla**: un tesauro es **vocabulario controlado**, «**prescribed list of terms (2.61), headings or
  codes, each representing a concept (2.11)**» —los números son las remisiones internas de la
  norma—.
- `[NISO]` · **ISO 25964 = «Thesauri and interoperability with other vocabularies».** **Parte 1:
  Thesauri for information retrieval** (2011) · **Parte 2: Interoperability with other vocabularies**
  (2013). **Sustituyó a ISO 2788 y a ISO 5964** —monolingües y multilingües—, y **trae modelo de
  datos y esquema XML**.
- **Falsos de la pregunta de la norma**, y los tres existen: `[ISSN]` **ISO 2709** = formato de
  **registros bibliográficos** · **ISO 3297** = **ISSN** · **ISO 2108** = **ISBN**.
- `[25964-2]` cláusula 6, «**Structural models for mapping across vocabularies**»: **6.2 Model 1:
  Structural unity** · **6.3 Model 2: Direct-linked** · **6.4 Model 3: Hub structure** · **6.5
  Selective mapping** · 6.6 Choosing among the options.
- **LA CLAVE ESTÁ EN LA NUMERACIÓN**: la norma llama **«Model»** a los tres primeros y **al mapeo
  selectivo no**. El selectivo decide **cuánto** se mapea, no **cómo** se estructura.
- **POR QUÉ UNIDAD ESTRUCTURAL PARA UNO NUEVO**: los otros tres **parten de vocabularios que ya
  existen** y hay que unir. **La unidad estructural no une nada: hace una sola estructura con varias
  lenguas dentro.** `[25964-1]` 2.35 define el tesauro multilingüe como aquel en que **términos y
  estructuras de relaciones** están en dos o más lenguas. **La palabra «nuevo» del enunciado decide.**

## Los códigos de identificación

- `[ISWC]` · «**The ISWC (International Standard Musical Work Code) is a unique, permanent and
  internationally recognized reference number for the identification of musical works**» ← **el
  enunciado del examen es esta frase traducida**.
- `[15707]` · Norma **ISO 15707**; identifica la obra «**as intangible creations**», **no** sus
  manifestaciones, que tienen **sus propios códigos**: **ISRC** (grabación sonora), **ISMN** (música
  impresa), **ISAN** (obra audiovisual).
- `[ISSN]` · **ISO 10957 = ISMN** · **ISO 3901 = ISRC** · **ISO 2108 = ISBN** · **ISO 3297 = ISSN**.
- **LA DISTINCIÓN QUE MIDE LA PREGUNTA**: una misma canción tiene **un ISWC** (la obra), **un ISMN
  por edición de la partitura** y **un ISRC por cada grabación**. **El distractor fino es ISMN.**
- **Fecha**: la edición leída es la **segunda, de diciembre de 2022**; «**cancels and replaces the
  first edition (ISO 15707:2001), of which it constitutes a minor revision**». **El título del código
  es el mismo en las dos.**

## La redacción digital

- `[uso]` · **REDACCIÓN DIGITAL = «conjunto de aplicaciones que centralizan el control de todos los
  elementos de software y hardware del sistema».**
- **DOS SENTIDOS, y el examen usa el segundo**: **escritura** —«arte de crear y adaptar textos para
  medios digitales», que es la opción falsa **del diccionario**— y **instalación** —«la redacción»
  como **el sitio y el sistema donde se produce**, igual que «la redacción del telediario»—.
- **Falsos que ni juegan**: diseño de interfaces móviles · edición de vídeo para plataformas.
- **Por qué «no informativos»**: en informativos el sistema **tiene nombre propio** en la industria;
  fuera de ellos, **el mismo concepto sin ese nombre**, y de ahí la definición genérica.
