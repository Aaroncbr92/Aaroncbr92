# Puesto 30 · Tema 12 · Preguntas de refutación

Fase 4 · Refutar. 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Quince preguntas tipo test de
cuatro opciones, contestadas **sólo con el tema**
(`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`).
La respuesta correcta va en negrita. T = teoría; P = aplicación práctica.

| # | Tipo | Pregunta y opciones | Dónde lo da el tema | Resultado |
| --- | --- | --- | --- | --- |
| 1 | T | Según el Contrato-programa 2024-2026, la presencia en redes sociales, las OTT y el pódcast corresponde a: a) la Dirección de Informativos; **b) Canal Sur Media**; c) la Dirección Técnica; d) Canal Sur Más | § 1 «El servicio público digital» (punto 46) | Entera |
| 2 | T | Repartir una historia de modo que cada medio cuente una parte que los demás no cuentan es: a) multiplataforma; **b) transmedia**; c) *crossposting*; d) versionado | § 1 «Vocabulario de oficio» | Entera |
| 3 | T | Según el DNR 2026 (media global), las redes sociales y de vídeo como vía de acceso a noticias en línea: a) 43 %; b) 51 %; **c) 54 %, por primera vez por delante de webs y apps propias (51 %)**; d) 77 % | § 1 «Dónde se ve hoy» | Entera |
| 4 | T | YouTube, ante un vídeo con relación de aspecto distinta de 16:9, recomienda: a) añadir barras negras hasta 16:9; **b) no añadir márgenes ni barras: el reproductor se adapta**; c) subirlo como Short siempre; d) reescalarlo a 1920 × 1080 | § 2 «Relación de aspecto» | Entera |
| 5 | P | Un canal estándar sube hoy un vídeo cuadrado de 2 min 40 s. YouTube lo clasifica como: a) vídeo largo, por pasar de 60 s; **b) Short**; c) vídeo largo, por ser cuadrado; d) lo rechaza | § 2 «Qué vídeo es un Short» | Entera |
| 6 | P | Se quiere montar una pieza vertical de 90 s en DaVinci Resolve, en su propia línea de tiempo 1080 × 1920, dentro del proyecto de emisión: a) se cambia la resolución del proyecto; **b) se crea una línea de tiempo desmarcando *Use Project Settings***; c) se exporta la horizontal con otro tamaño; d) no es posible en el mismo proyecto | § 2 «Montar en vertical»; supuesto, paso 2 | Entera |
| 7 | T | Guías de encuadre «Social Media» del visor de Resolve 21: a) 1:1, 4:5, 9:16; **b) 1:1, 4:5, 9:16, 1.91:1, 16:9**; c) 1.33, 1.66, 1.77, 1.85, 2.35; d) 9:16 y 16:9 | § 2 «Montar en vertical» | Entera |
| 8 | P | Al reencuadrar 16:9 → 9:16 con el horizontal escalado a 1920 px de alto, ¿qué parte del ancho se conserva? a) la mitad; b) dos tercios; **c) en torno al 32 % (1080 de 3413)**; d) el 56 % | § 2 «Reencuadrar: oficio» | Entera |
| 9 | T | Para la LGCA (art. 2.18), un vídeo corto del catálogo del prestador: a) no es programa por su duración; **b) es programa, con independencia de su duración**; c) es vídeo generado por usuarios; d) es comunicación comercial | § 3 «Qué es un clip» | Entera |
| 10 | P | En DaVinci Resolve, para sacar como fichero sólo un fragmento de la línea de tiempo (el total de 40 s que será el clip) se: a) exporta la línea entera y se recorta en la red; **b) marcan puntos de entrada y salida en la regla de la línea de tiempo y se renderiza ese rango (en modo *Single Clip*)**; c) duplica el proyecto; d) usa el preajuste de TikTok | § 3 dice que cada clip es un fichero y una publicación distintos; no dice cómo se exporta un rango | A medias (laguna 1) |
| 11 | T | Miniatura recomendada por YouTube para un Short: a) 1280 × 720, 16:9; b) 3840 × 2160, 16:9; **c) 2160 × 3840, 9:16, al menos 640 px de alto, JPG o PNG**; d) 1080 × 1080, 1:1 | § 4 tabla y citas | Entera |
| 12 | P | Un vídeo vertical se publica con miniatura personalizada 16:9. En la página principal, exploración y suscripciones: a) se ve recortada a 9:16; **b) se sustituye por una automática 4:5**; c) se rechaza y el canal recibe una falta; d) se ve con barras | § 4 «Lo que recomienda YouTube» (trampa) | Entera |
| 13 | P | Material de emisión 1080i a 50 campos para YouTube: a) subirlo entrelazado; b) 1080p50 duplicando campos; **c) desentrelazar a 25 fotogramas progresivos (misma regla que 1080i60 → 1080p30)**; d) 1080i25 | § 6 «Exportar para YouTube»; supuesto, paso 6 | Entera |
| 14 | T | Qué nivel de sonoridad atribuye Blackmagic a YouTube en el manual de Resolve 21, frente a su objetivo por defecto: a) −23 frente a −14 LUFS; **b) −14 LUFS frente a −23 LUFS**; c) −16 frente a −24 LUFS; d) −18 frente a −23 LUFS | § 6 «Los preajustes», Sonoridad | Entera |
| 15 | T | Duración máxima de un Reel de Instagram y resolución recomendada por Instagram: a) 60 s, 1080 × 1920; b) 90 s, 1080 × 1350; c) 3 min, 1080 × 1920; d) 15 min, 720 × 1280 | «Lo que este tema no da»: especificaciones de Instagram no leídas, no se dan | No (hueco declarado; no se propone ampliar sin fuente oficial legible) |

Resultado: 13 enteras, 1 a medias, 1 no. La 10 es laguna ampliable con fuente ya disponible (manual
de DaVinci Resolve 21, cap. 187, p. 4211, «To define a continuous range of clips to render», con puntos In/Out). La 15 es un hueco
declarado en el tema; sólo se cubriría si se consigue leer la página oficial de Instagram.
