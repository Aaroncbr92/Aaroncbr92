# Inteligencia artificial aplicada a contenidos sonoros y audiovisuales

Las fuentes del **tema 4 del específico de Documentación**. Son pocas, y eso es
**el dato**: **esta materia no tiene todavía norma publicada**. No hay ley en el
BOE que defina la diarización ni recomendación internacional que describa los
módulos de un sintetizador de voz.

Lo que sí hay son dos clases de documento fiable: **los programas de evaluación
de organismos públicos de normalización**, que definen las tareas porque tienen
que medirlas, y **los anuncios técnicos de quien construye los sistemas**.

| Fichero | Documento | Qué sostiene |
|---|---|---|
| `NIST_rich-transcription.txt` | «Rich Transcription Evaluation», del **instituto nacional de normas y tecnología de los Estados Unidos** (NIST), grupo de información multimodal | Que la tarea se llama «**"Who Spoke When" speaker diarization**» —quién habló cuándo—, y que existe además «**"Who Said What" speaker diarization**» —quién dijo qué—, que ya atribuye las palabras |
| `Google_blog_BERT.txt` | «Understanding searches better than ever before», blog oficial de **Google**, **25/10/2019** | El desarrollo de las siglas —«**Bidirectional Encoder Representations from Transformers**»—, qué son los transformadores —«**models that process words in relation to all the other words in a sentence**»— y qué significa mirar el contexto —«**by looking at the words that come before and after it**»—. Y su efecto declarado: «**one in 10 searches in the U.S. in English**» |
| `arXiv_BERT_1810-04805.txt` | Ficha del artículo «BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding», **arXiv 1810.04805** | El resumen, con el desarrollo de las siglas y el «**jointly conditioning on both left and right context in all layers**» |

## Lo que no se ha podido traer

- **Ninguna norma sobre la arquitectura de un sintetizador de voz.** La
  biblioteca de recomendaciones de la unión internacional de telecomunicaciones
  —de la que sí se descargaron recomendaciones para el bloque de Producción—
  **no respondió a ninguna de las tres consultas** hechas el 3 de septiembre de
  2026, y la recomendación del consorcio de la web sobre marcado de síntesis de
  voz responde «prohibido», igual que el resto de su sitio. Comprobado con agente
  de usuario de navegador.
- **Ninguna norma que defina «palabra token» frente a «palabra tipo».** Los cuatro
  términos de esa pregunta se han buscado en todo el corpus del proyecto,
  incluidas las normas de vocabulario documental del tema anterior, y **ninguno
  aparece**. La norma de vocabulario fundamental de información y documentación
  se vende **sin muestra utilizable**: su muestra oficial sólo trae portada e
  índice.
- **Los tres nombres falsos de la pregunta del modelo de lenguaje.** Dos son
  apodos de cambios de algoritmo que la propia empresa rara vez confirma, y el
  tercero es un sistema de indexación. **No se ha verificado ninguno**, y el tema
  lo dice.
