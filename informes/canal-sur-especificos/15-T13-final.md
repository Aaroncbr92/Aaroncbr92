# Grafista (15) · Tema 13 · Revisión del remate (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/13-diseno-redes-sociales-plataformas-verticales-miniaturas-piezas-cortas-marca.md`.
Encargo fechado el 24-09-2026; revisión hecha el 29-09-2026 (fecha de sistema).
Alcance: sólo los 11 pasajes que lista `15-T13-remate.md`.
Ficheros tocados: el tema 13 y este informe.

## Fuentes releídas (29-09-2026)

| Fuente | Cómo |
| --- | --- |
| Meta, *Facebook Ads Guide*, «Awareness Video Ad Specs on Instagram Reels» (facebook.com/business/ads-guide/update/video/instagram-reels) | Descargada y pasada a texto el 29-09-2026 |
| Meta, *Facebook Ads Guide*, «Awareness Image Ad Specs on Instagram Feed» (…/update/image/instagram-feed) | Descargada el 29-09-2026 |
| Meta, *Facebook Ads Guide*, «Awareness Image Ad Specs on Instagram Reels» (…/update/image/instagram-reels) | Descargada el 29-09-2026, para comparar «roughly» con «at least» |
| Contrato-programa RTVA 2024-2026 (BOJA núm. 245, de 2023), punto 46 | Volcado en texto, líneas 1316-1324 |
| Tema 2 de Grafista, tabla del manual, fila «Mosca» | Línea 261 |

## Comprobación, pasaje por pasaje

| N.º del remate | Pasaje | Resultado |
| --- | --- | --- |
| 1 | § 5, mosca «se ve durante la emisión, salvo donde el manual de la casa la retire (tema 2)» | Correcto: la fila «Mosca» del tema 2 incluye «cuándo desaparece». Es un pasaje de oficio y está rotulado así |
| 2 | Aplicación práctica, paso 1, Canal Sur Media | Se ajusta a la fuente (ver corrección B) |
| 3 | Portada, «Fuente» | Correcto: las tres guías existen con esos rótulos |
| 4 | Siglas, MP4 y MOV | Correcto |
| 5 | «Qué se puede preguntar» | Correcto: lo contestan los epígrafes 2 y 4 |
| 6 | «De dónde sale este tema» | Correcto |
| 7 | § 2, horquilla del *feed* | Todos los literales, tal cual: «Image File Type: JPG or PNG», «Ratio: 4:5» y «Resolution: 1440 x 1800 pixels» (bajo «Design Recommendations»); «Maximum File Size: 30MB», «Minimum Width: 500 pixels», «Minimum Aspect Ratio: 400 x 500», «Maximum Aspect Ratio: 191 x 100» y «Aspect Ratio Tolerance: 1%» (bajo «Technical Requirements»). La división entre «recomienda» y «requisitos técnicos» coincide con la página. Cuentas: 400/500 = 0,8 es el más alto; 191/100 = 1,91 el más apaisado; 9/16 = 0,5625 < 0,8, así que el 9:16 no entra. Correcto |
| 8 | § 2, guía de vídeo en Reels | Los literales son exactos («File Type: MP4, MOV», «Ratio: 9:16», «Resolution: 1440 x 2560 pixels», la frase «at least 14%…», «too close to the edges of devices with screens taller than a 9:16 aspect ratio»). Pero el verbo estaba mal (ver corrección A). El antecedente «La guía hermana» tiene delante la guía de imagen de Reels |
| 9 | § 4, duración del Reel | Literales exactos: «Similar to organic Reels, ads can be up to 15 minutes» y «Video Duration: 0 seconds to 15 minutes» (bajo «Technical Requirements»). También es exacto que los anuncios «inserted in between organic Reels content». El pasaje declara que la inferencia sobre lo orgánico se hace por comparación. Correcto |
| 10 | «Lo que este tema no da» | Correcto; «epígrafes 2 y 4» remite a donde están los datos |
| 11 | «Trazabilidad», dos filas nuevas | Las URL y los títulos coinciden con las páginas |

## Correcciones aplicadas (comprobadas en la fuente)

A. § 2, guía de vídeo. **Antes:** «pide **«File Type: MP4, MOV»**…». **Ahora:** «recomienda …».
   En la página, esos tres datos están bajo «Design Recommendations», no bajo «Technical Requirements».
   Es el error 4 del encargo: presentar como exigencia lo que es una recomendación. Así queda
   coherente con el pasaje hermano del *feed*.

B. Aplicación práctica, paso 1. **Antes:** «(la presencia en redes es, según el Contrato-programa, de
   Canal Sur Media; epígrafe 1)». **Ahora:** «(el Contrato-programa encarga a Canal Sur Media la
   «**presencia y contribución en redes sociales**»; epígrafe 1)».
   El punto 46 dice que Canal Sur Media está **«encargada de toda la aportación logística, productiva y
   funcional»** de los servicios digitales, y entre ellos la **«presencia y contribución en redes
   sociales»**. No dice que la presencia «sea de» Canal Sur Media. La nueva redacción usa el literal y
   lo marca en negrita.

## Sin cambios: justificación

- La frase «como los Reels orgánicos, un Reel puede durar hasta 15 minutos» es una lectura de «Similar
  to organic Reels, ads can be up to 15 minutes». Se mantiene porque la frase siguiente declara que el
  dato llega por comparación y desde una guía de anuncios.
- En la guía de vídeo, «Minimum Width: 250 pixels for ads less than 30 seconds; 500 pixels…» no se ha
  añadido. No lo pide el enunciado y el remate no lo introdujo.

## Lentes

- `refutar_prosa.py`: sin negritas rotas. Avisa de JPG, PNG, MOV y demás, que ya están declarados en las
  siglas: es un falso positivo.
- `indice.py`: 36 epígrafes; el índice no cambia. El aviso «sin portada» aparece igual en el tema 12,
  así que es cosa de la herramienta: el tema sí tiene sus marcas de portada.
- Lentes de norma: no se aplican; los pasajes no citan artículos.
- Extensión: unas 8.480 palabras.

## Veredicto

Tema 13 cerrado, con dos retoques de precisión. Queda para el coordinador lo que ya señaló el remate:
la observación sobre el común (§ 4, Libro de estilo y web).
