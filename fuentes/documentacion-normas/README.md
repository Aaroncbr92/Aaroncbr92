# Normas de información y documentación

Las fuentes del **tema 2 del específico de Documentación**. Casi todas son
**normas ISO del comité técnico 46, de información y documentación**, y todas
tienen la misma peculiaridad: **su texto íntegro es de pago**.

## Qué se ha podido leer, y por qué basta

`iso.org` responde **403 «prohibido»** a toda consulta automática —también con
agente de usuario de navegador—, y su plataforma de consulta en línea, igual. Lo
que sí se publica gratis es **la muestra oficial** de cada norma: portada,
prólogo, **índice completo**, introducción, objeto y una parte de los términos y
definiciones. **Ahí están las respuestas de este examen**, y este tema no cita
ni una línea que no esté en la muestra.

| Fichero | Norma | Qué trae | Qué queda fuera |
|---|---|---|---|
| `ISO-25964-1-2011_muestra.pdf` / `.txt` | **ISO 25964-1:2011**, «Information and documentation — Thesauri and interoperability with other vocabularies — Part 1: Thesauri for information retrieval» | Objeto, índice completo y definiciones **2.1 a 2.47** —entre ellas **precoordinación (2.44)**, **postcoordinación (2.43)**, **vocabulario controlado (2.12)**, **documento (2.15)**, **indización (2.27)**, **recuperación de información (2.28)**, **interoperabilidad (2.29)**, **metadatos (2.33)** y **tesauro multilingüe (2.35)**— | **La definición de «tesauro»**, en un apartado posterior al corte |
| `ISO-25964-2-2013_muestra.pdf` / `.txt` | **ISO 25964-2:2013**, «… — Part 2: Interoperability with other vocabularies» | Objeto, introducción, índice completo —**con la cláusula 6, «Structural models for mapping across vocabularies», y sus apartados 6.2 a 6.6**— y definiciones **3.1 a 3.54** | El cuerpo de las cláusulas |
| `ISO-15707-2022_muestra.pdf` / `.txt` | **ISO 15707:2022**, «Information and documentation — International Standard Musical Work Code (ISWC)», **segunda edición, diciembre de 2022** | Prólogo con **los cambios respecto de la edición de 2001**, introducción, objeto y construcción del código | Los anexos |

**Nota de fecha.** La segunda edición de ISO 15707 es de **diciembre de 2022**, y
el corte de este proyecto es el **21 de diciembre de 2022**. Su propio prólogo
dice que «cancels and replaces the first edition (ISO 15707:2001), of which it
constitutes a minor revision», y enumera los cambios: **ninguno toca lo que el
examen pregunta**, y el título del código es el mismo en las dos ediciones.

## Documentación institucional

| Fichero | Página | Qué sostiene |
|---|---|---|
| `NISO_iso25964.txt` | **Página oficial de ISO 25964**, alojada por **NISO**, secretaría del ISO/TC46/SC9 | El resumen de las dos partes; que la parte 1 **sustituyó a ISO 2788 y a ISO 5964**; que incluye **modelo de datos y esquema XML**; y los **índices abreviados** de ambas partes |
| `ISSN-International_normalizacion.txt` | «ISSN, a standardised code», **Centro Internacional del ISSN** | La designación exacta de **ISO 2108 (ISBN)**, **ISO 3297 (ISSN)**, **ISO 3901 (ISRC)** e **ISO 10957 (ISMN)**, y la descripción de **ISO 2709** como formato de registros bibliográficos |
| `ISWC_portada.txt` | Portada del **ISWC**, gestionado por CISAC | «The ISWC (International Standard Musical Work Code) is a unique, permanent and internationally recognized reference number for the identification of musical works» —**el enunciado del examen es esta frase traducida**— |

A ellas se suma la **Ley 16/1985 del Patrimonio Histórico Español**, volcada en
`../corte-20221221/`, de la que este tema usa los artículos **cuarenta y nueve**,
**cincuenta y cinco**, **cincuenta y siete** y **cincuenta y ocho**.

**Aviso de método.** Esa ley **numera sus artículos con letra**, de modo que las
lentes por artículo no la reconocen y devolvían «0 comprobadas». Se construye una
copia con los rótulos en cifra con `herramientas/ordinales.py`, que **no toca el
cuerpo de los preceptos**.

## Lo que no se ha podido traer

- **ISO 214**, «Documentation — Abstracts for publications and documentation», que
  es la norma que clasifica los resúmenes en **indicativo, informativo y
  analítico**. Se vende **sin muestra**: el catálogo de ISO responde «prohibido»,
  la tienda de la asociación española de normalización también, y las tiendas
  nacionales la ofrecen sólo de pago. Comprobado con agente de usuario de
  navegador. El dato se recoge **de la plantilla oficial**, y va marcado.
- **El cuerpo de las cláusulas de ISO 25964**, en las dos partes. Se ha trabajado
  con **el índice y las definiciones**, que es lo que la muestra da.
