# Esquema · Tema 4 del específico de Documentación · Inteligencia artificial

Telegrama. **Cada línea lleva delante de dónde sale**: `[NIST]` = evaluaciones de transcripción
enriquecida del instituto de normas de los Estados Unidos · `[Google]` = anuncio oficial de Google de
25/10/2019 · `[arXiv]` = ficha del artículo donde se presentó el modelo · `[uso]` = plantilla
oficial, **sin documento**.

**Cabecera.** **4 preguntas** · **2 con documento**, **2 sólo con plantilla**. **Es el tema con menos
respaldo documental del bloque**, y no por descuido: **la materia no tiene norma publicada**.

<!-- indice -->

## Índice

- [Lo que hay que llevar sabido](#lo-que-hay-que-llevar-sabido)
- [Síntesis frente a reconocimiento](#síntesis-frente-a-reconocimiento)
- [Diarización](#diarización)
- [Tipos y tokens](#tipos-y-tokens)
- [El modelo del buscador](#el-modelo-del-buscador)
- [Lo que el temario pide y no salió](#lo-que-el-temario-pide-y-no-salió)

<!-- /indice -->

## Lo que hay que llevar sabido

| Pregunta | Respuesta | De dónde |
|---|---|---|
| Módulo generativo prosódico | **Síntesis de voz** | `[uso]` |
| 3.000 palabras → 3.000 palabras | **Tokens** | `[uso]` |
| Diarización | **Dividir el audio por hablante** | `[NIST]` |
| Modelo de lenguaje de Google | **BERT** | `[Google]` |

## Síntesis frente a reconocimiento

- `[uso]` · **TRES ANALIZAN Y UNA FABRICA.** Reconocimiento de voz = audio → texto · Verificación del
  locutor = audio → sí/no · **Síntesis de voz = texto → audio**.
- **PROSODIA = entonación, acento, ritmo y pausas**, o sea **lo que no está en las letras**.
- **LA CLAVE ESTÁ EN «GENERATIVO»**: al **escuchar**, la prosodia **ya viene en la señal**; al
  **hablar** desde un texto, **hay que inventarla**. Sólo el sintetizador la **genera**.
- **Distractor de otra categoría**: el **sistema de respuesta vocal** **no es una tecnología del
  habla**, es **un servicio que las usa** —normalmente reconocimiento y síntesis a la vez—. Quien lo
  elige **elige el conjunto en vez de la pieza**.
- **AVISO**: la arquitectura del sintetizador **no está en ninguna norma reunida**. La biblioteca de
  la unión internacional de telecomunicaciones **no respondió** ese día y la recomendación de marcado
  de síntesis del consorcio de la web responde «prohibido».

## Diarización

- `[NIST]` · **La fórmula oficial: «"Who Spoke When" speaker diarization».** **Quién** = agrupar los
  segmentos de un mismo hablante · **cuándo** = marcar en qué tramos habla cada uno.
- `[NIST]` · **La otra tarea, que se confunde**: «**"Who Said What" speaker diarization**». **Quién
  habló cuándo SEPARA; quién dijo qué TRANSCRIBE Y ATRIBUYE.**
- **Falsos**: «**registrar en un diario**» = **juega con el sonido**; la palabra **no viene de
  diario**; es el fino · «mejorar **la calidad del sonido**» = restauración de audio · «reconocer el
  **idioma de un texto**» = identificación de idioma, y sobre **texto**, no sobre audio.
- **POR QUÉ IMPORTA EN UN ARCHIVO**: sin diarización, la transcripción de una tertulia es **un muro
  de texto**; con ella, **se puede buscar quién dijo cada cosa**.

## Tipos y tokens

- `[uso]` · **TOKEN = OCURRENCIA · TIPO = FORMA.** Si «de» sale 200 veces: **200 tokens, 1 tipo**.
- **Por qué la respuesta es tokens**: **es el único recuento que puede devolver el mismo número que
  entró**, porque **no agrupa ni descarta**.
- **Falsos**: **tipos** → saldrían **muchas menos** · **vacías** → sólo artículos, preposiciones y
  conjunciones: **un subconjunto** · **significativas** → el texto **menos** las vacías: **otro
  subconjunto**.
- **Van en pareja**: **vacías + significativas = el texto entero**. Y **tipos/tokens = medida clásica
  de riqueza léxica**.

## El modelo del buscador

- `[Google]` · «**Bidirectional Encoder Representations from Transformers, or as we call it--BERT,
  for short**».
- `[Google]` · **Qué son los transformadores**: «**models that process words in relation to all the
  other words in a sentence, rather than one-by-one in order**».
- `[Google]` · **Qué es «analizar el contexto»**: «**BERT models can therefore consider the full
  context of a word by looking at the words that come before and after it**». **Antes Y después: eso
  es lo bidireccional.**
- `[arXiv]` · «**jointly conditioning on both left and right context in all layers**».
- `[Google]` · **Efecto declarado**: «**one in 10 searches in the U.S. in English**», sobre todo en
  «**longer, more conversational queries**» y donde «**prepositions like "for" and "to" matter a lot
  to the meaning**».
- **Falsos**: dos son **apodos de cambios del algoritmo** y uno es **un sistema de indexación**.
  **Ninguno es un modelo de lenguaje**, y ésa es la distinción. **AVISO: ninguno se ha verificado.**

## Lo que el temario pide y no salió

- **Visión artificial**: **cara → lugar → escena** es **una escalera de dificultad** —objeto
  delimitado, conjunto, interpretación—. En un archivo sirven para **generar los puntos de entrada
  que marcaría a mano un documentalista**.
- **Las tres del habla no son sinónimas**: **reconocimiento** = señal → palabras · **transcripción** =
  ese resultado **puesto en documento**, con puntuación y formato · **diarización** = **quién habló
  cuándo**.
