# Operador/a de Sonido (28) · Tema 12 · Remate

Fase 5. Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`.
Parte de `28-T12-refutacion.md` y `28-T12-preguntas.md`. Del método sólo se ha leído `ENCARGO.md` y el
enunciado del puesto. Fuentes releídas el **25-09-2026** (el encargo fija el día de trabajo en el 24-09-2026):
Orden TDF/732/2026 (BOE-A-2026-15661, volcado `fuentes/canal-sur/sonido/BOE-A-2026-15661.txt`), notas
UN-17 y UN-105; Shure, *Selection and Operation of Wireless Microphone Systems* (`shure-selection.txt`,
líneas 1078-1088 y 2355-2400). Las expansiones de DAB+, RDS y WMAS se toman de los temas del mismo
temario que ya las presentan (tema 3 de este puesto para WMAS).

**Se amplió contenido nuevo: sí** (tres lagunas). Procede fase 5 bis sobre los pasajes 4 a 6.

## Comprobación de cada corrección en la fuente

| # | Hallazgo | En la fuente | Aplicado |
|---|---|---|---|
| E1 | Silenciador de tono sin la salvedad «non-tone-key» | Shure, l. 1084-1085: **«even in the presence of a (non-tone-key) interfering signal at the same frequency»**. Confirmado | Sí |
| E2 | WMAS, DAB+ y RDS sin presentar | Aparecen sólo en «Lo que este tema no da». Confirmado | Sí, en las siglas de entrada |
| L1 | UN-17 (micro-transmisores de 50 nW) y UN-105 (ayudas auditivas) | UN-17: texto literal confirmado, ETSI EN 301 357-2, sin derecho a protección. UN-105: diez canales de 50 kHz, 174,050-174,500 MHz, 2 mW p.r.a., ETSI EN 300 422; incluye 174,100 y 174,300. Confirmado | Sí |
| L2 | Margen de 250 kHz respecto de la imagen | Shure, l. 2372-2376. Confirmado | Sí |
| L3 | Espurias del emisor de cristal | Shure, l. 2377-2391 (ejemplo ×9, 180 MHz, 20 MHz, espurias en 160/200 y 140/220 MHz; 250 kHz; sintetizados sin multiplicadores); l. 2392-2398 (FI y multiplicadores distintos entre marcas). Confirmado | Sí |

Ningún hallazgo del informe resultó equivocado.

## Pasajes cambiados

1. **Portada, Extensión**: 9.300 → 9.800 palabras (`indice.py`: 9.250 antes, 9.774 después).
2. **Siglas de entrada**: tras DAB, «y su versión mejorada (**DAB+**); sistema de datos por radio
   (**RDS**, *radio data system*); sistema multicanal de audio inalámbrico (**WMAS**, *wireless
   multichannel audio system*)».
3. **«El receptor por dentro»**, silenciador de tono: «Este último evita el ruido aun con otra señal
   en la misma frecuencia si esa señal no lleva tono (Shure: **«(non-tone-key) interfering signal at the
   same frequency»**). También hace silencioso el encendido y apagado del emisor.» Y en la tabla, la
   remisión al epígrafe renombrado.
4. **«Qué bandas puede usar un micrófono…»**, tras el párrafo del DECT (nuevo): dos viñetas, UN-17
   (micro-transmisores portátiles de audio de uso común, 50 nW, sin protección, ETSI EN 301 357-2) y
   UN-105 (diez canales de 50 kHz para ayudas auditivas, 174,050-174,500 MHz, 2 mW p.r.a., ETSI
   EN 300 422; 174,100 y 174,300 coinciden con los canales 1 y 2 de micrófonos de la UN-95).
5. **Epígrafe renombrado** «Las frecuencias internas del receptor y del emisor» (y su entrada en el
   índice, regenerado con `indice.py`); frase de entrada «…y el emisor de cristal añade las suyas»;
   **fila nueva** «Espurias del emisor de cristal» con el ejemplo literal de Shure.
6. **Párrafo nuevo** tras el del oscilador local: 250 kHz respecto de la imagen (con el rechazo de
   la etapa de entrada), 250 kHz respecto de las espurias, emisores sintetizados sin multiplicadores,
   y mezcla de marcas con FI o multiplicadores distintos. La frase «Y que el programa de coordinación…»
   se mantiene en su sitio, al final del párrafo del oscilador local.
7. **«De dónde vienen»**, fila «Frecuencias internas»: añade «espurias de un emisor de cristal» y
   «(250 kHz)».
8. **Trazabilidad**: fila del CNAF (UN-17 micro-transmisores; UN-105 ayudas auditivas) y fila de
   Shure *Selection* (250 kHz respecto de imagen y espurias, rechazo en la entrada, espurias del
   emisor de cristal, sintetizados, marcas distintas, tono frente a señal sin tono).

Releídos todos: cada «ese», «la misma», «Lo que lo reduce» y «el margen es el mismo» tiene delante
su antecedente (este último, los 250 kHz del oscilador local del párrafo anterior).

## Lentes

- `indice.py`: índice regenerado, 32 epígrafes.
- `negritas.py` (BOE + dos guías Shure): 180 negritas, 10 «no están», las mismas 10 ya explicadas
  en verificación y refutación; ninguna de las nuevas falla.
- `refutar_modo.py` y `refutar_exactitud.py` (BOE): 0 hallazgos.
- `refutar_prosa.py`: 1, «ETD» sin presentar; es parte del nombre oficial de la Orden ETD/1449/2021
  dentro de una cita literal, preexistente. No se toca.

Preguntas afectadas: 4, 11, 12 (lagunas) y 13 (a medias) quedan contestables enteras con el tema.

## Ficheros tocados

- El tema 12 y este informe. Nada más.
