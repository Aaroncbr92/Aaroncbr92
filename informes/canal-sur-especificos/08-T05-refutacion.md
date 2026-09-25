# Puesto 08 · Tema 5 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/05-iluminacion-basica.md`
(7.609 palabras según `indice.py`). Refuto, no corrijo.

## Fuentes releídas (todas el 24-09-2026)

- Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 (copia local en `.txt`): HVL-LBPC,
  Power Link/Rec Link, pre-lighting, preajustes Custom y Log, pasos de 20 K y «Values above [5600K]»,
  Tint −99/+99 y memoria A, 2000K-15000K, parpadeo, *Flicker Reduce* ([Auto]/[On]/[Off], [50Hz]/[60Hz],
  de fábrica [60Hz]). Todo literal.
- Astera, ficha del Titan Tube e informe IEC 62471 n.º 2602T58190E-SF (copias locales): 1340/2900/
  5800 lm, «CRI(Ra)/TLCI 3200-6500k*» ≥96, «*Typical values», RGBMintAmber, DMX, fecha 2026-05-29,
  «Exempt Group». Literal.
- UIT-R BT.709-6 y BT.2020-2, edición española (copias locales): D65 0,3127/0,3290; frase de la
  frecuencia de trama. Literal.
- EBU Tech 3355, marzo de 2017 (descargada de tech.ebu.ch): valor 50, dos escalas, salvedad,
  «Neither the CRI…», tabla de radiadores de luz de día (6500 → 0.312787, 0.329205). Literal, con M1.
- Blackmagic, *URSA Broadcast G2 Manual*, noviembre de 2021 (descargado de markertek): cinco
  preajustes, vela y cielo nublado, parpadeo en el apartado de cadencias altas, obturación sin
  parpadeo y su salvedad, cebra, 25→50 fps. Literal.
- Canon XF605, especificaciones PUB. DIE-0559-000B (descargadas de global.canon): «daylight, 5,600 K»,
  «tungsten lamp, 3,200 K», «2,000 K to 15,000 K», nota «approximate». Literal.
- Copiado del común: ninguno (informe de redacción). Lo copiado de RTVE es oficio y cálculo; rehechos
  los cálculos (mired, −134, ≈45 mired > 22.000 K, 1/9 ≈ 3,17 pasos, 16:1 = 4 pasos f/8→f/2, 4:1).

Lentes: `refutar_prosa.py` 3 avisos de siglas (PXW, URSA, PUB: códigos de producto, sin hallazgo);
`indice.py` no cambia el fichero. Sin normas jurídicas: no proceden las lentes de norma.

## Hallazgos de exactitud

Graves: ninguno. Menores: 3.

| Nº | Error | Línea / pasaje | Qué pasa | Propuesta |
|---|---|---|---|---|
| M1 | 6 salvedad omitida | l. 343-344, dos lecturas del TLCI | La primera escala es, en la EBU, «**Film-style production, where possibly different cameras, locations and lighting need to be intercut or mixed**», y la cita se corta tras «is involved» sin «**and pictures are required to match each other well**», que es el contrapunto de «only to be credible». El tema la resume como «producción con posproducción» | Nombrar la escala como la EBU y completar la cita |
| M2 | 9 sin fuente | l. 226, «el iluminante D65 de la CIE» | Las fuentes citadas dicen «D65» (UIT-R) e «Illuminant D65» (EBU); ninguna atribuye el iluminante a la CIE en el pasaje citado. Dato cierto de oficio, pero sin apoyo leído | «el iluminante D65» (EBU: «**Illuminant D65**»), o citar la fuente CIE |
| M3 | coherencia | l. 34, ***ATW*** | Se pone como ejemplo de rótulo de menú, pero no aparece en el tema | Quitarlo o sustituirlo por uno que se use |

Comprobado sin hallazgo (oficio y cálculo): magnitudes y luz incidente/reflejada, ley inversa del
cuadrado, mired y filtros, sentido de CTO/CTB, relación de contraste, ejemplo 16:1, tabla de
bajar/subir contraste, dureza y tamaño aparente, tres puntos, accesorios, interior con ventana,
regulador en tungsteno y LED, 1/50-1/100 con red de 50 Hz (declarado oficio con salvedad).

## Cobertura del enunciado

Los cinco elementos (temperatura de color, contraste, sombras, luz natural, luz artificial) tienen
epígrafe propio y en el orden del enunciado. Preguntas en `08-T05-preguntas.md`: 12 enteras,
1 a medias, 2 no.

Lagunas (3), a ampliar en el remate con fuente (si no se encuentra, declararlo como oficio o en «Lo
que este tema no da»):

| Nº | Rúbrica | Qué falta | Pregunta |
|---|---|---|---|
| L1 | Contraste | Clave alta y clave baja (*high key* / *low key*): qué son y su relación con la razón de contraste | 13 |
| L2 | Temperatura de color | Cómo se mide la temperatura de color de una fuente (termocolorímetro o medidor de color) antes de elegir gel | 14 |
| L3 | Luz natural | Altura del sol a lo largo del día: luz rasante y sombras largas al amanecer y al atardecer, dura y cenital a mediodía (hoy sólo el color y una mención de la dirección); de paso, el color de las lámparas de descarga del alumbrado público (sodio, mercurio), nombradas sólo en la cita de parpadeo (pregunta de reserva) | 15 |

## Otros ficheros tocados

Ninguno, salvo este informe y `08-T05-preguntas.md`. `indice.py` se ejecutó sin cambiar el tema.
PDF descargados sólo al scratchpad.
