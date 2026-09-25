# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 5 bis, revisión de lo rematado

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`.
Fecha de trabajo y de lectura de todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).
Ficheros tocados: el tema y este informe.

Alcance: sólo los pasajes cambiados por el remate (`28-T14-remate.md`), localizados por diff entre la
copia previa al remate y el tema actual.

## Fuentes releídas (25-09-2026)

Copias de texto del directorio de trabajo del ciclo: UIT-R BS.775-4 (recomienda 2, 3, 6, 7, 8;
notas 4-5; anexo 3 § 1 y «Downward compatibility with low-cost receivers»; anexo 4, tabla 2 completa
y advertencia final; anexo 5 entero; anexo 7 y § 6-7 de su apéndice 1); UIT-R BS.1770-5 (apéndice 1
del anexo 4); EBU Tech 3343-2023 § 4.2; EBU Technical Review 2009-Q1 (In-Sync / Advanced); Dolby ED2
Technology Brief; Dolby Atmos Renderer Guide v3.0 § 24.3.3.

## Citas literales

Las 34 citas en negrita nuevas o cambiadas, cotejadas por script (normalizando espacios, guiones y
comillas) contra su fuente: 34 de 34 casan, cada una en la fuente que el tema le atribuye.

## Datos no literales, contra su fuente

- Tabla 2 (filas 2/1, 3/1, 2/2) y las tres reglas derivadas: coinciden coeficiente a coeficiente.
- Anexo 3: *simulcast*, matrices A/B y T/Q1/Q2, las dos vías de bajo coste (síntesis del decodificador):
  correctos.
- Anexo 5: seis pautas, incluidas decorrelación/atenuación y canal de datos: correctas.
- Nota 5 (ganancia para potencia de un solo altavoz), recomienda 2, 3, 6, 7 y 8: correctos.
- § 6 del apéndice 1 del anexo 7 (LFE Dolby E frente a AC-3, PCM de banda completa): correcto.
- Tech 3343 § 4.2 (5.0): correcto. In-Sync/Advanced y su aplicación: correctos.
- ED2 para emisión y tabla de TrueHD / Dolby Digital Plus (con pérdidas, núcleo compatible, capa 5.1
  por Pro Logic IIx o Lo/Ro, estéreo desde la 5.1): correctos.
- BS.1770-5 cita BS.2051 y BS.2127 (IAR) en el apéndice 1 del anexo 4: correcto.

## Hallazgos y correcciones (comprobadas en la fuente antes de aplicarlas)

1. **Afirmación sin fuente (9)**, siglas de entrada: «su sucesor **Dolby Digital Plus**». Ninguna
   fuente del tema califica al Dolby Digital Plus de sucesor del AC-3 (el ED2 Brief sólo lo llama
   «next-generation audio format»). Quitado «su sucesor»: queda «el **Dolby Digital Plus**».
2. **Salvedad omitida (6)**, «El canal LFE», calibración: el +10 dB en radiodifusión se daba sin su
   condición. La fuente: «For broadcasting applications where signal levels are compliant with these
   specifications, the level of LFE channel should be reproduced with positive offset gain of 10 dB…».
   Añadida la condición con su cita literal.

## Antecedentes

«El mismo documento» (ED2) → Technology Brief nombrado en el epígrafe; «El mismo apéndice» → apéndice
1 del anexo 7 del párrafo anterior; «Y añade» → Tech 3343 de la frase previa; «La recomendación
advierte» → BS.775 de la tabla anterior; «esas especificaciones» (nuevo) → el procedimiento del anexo
7 citado justo antes. Todos tienen su antecedente.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 10.959 palabras, 38 epígrafes (portada: 11.000
aproximadamente, cuadra).

Resultado: 2 correcciones menores; el tema queda cerrado.
