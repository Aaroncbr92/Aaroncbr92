# Informe de verificación · Cámara Operador (08) · Tema 12

Fase 3. Tema: `temas/canal-sur-especificos/08-camara-operador/12-derechos-de-imagen-privacidad-menores-victimas.md`.
Fecha de lectura de todas las fuentes: 24-09-2026.

## Alcance

- Saltado, por estar listado bajo «Copiado del común» en `08-T12-redaccion.md`: los trece pasajes de esa tabla.
- Copiado de RTVE: nada (el informe de redacción lo declara y el tema no lo contiene).
- Verificado: lo «Nuevo» y lo «Adaptado» (en lo adaptado, que cada remisión tenga delante su antecedente).

## Fuentes releídas

| Fuente | Cómo | Qué |
|---|---|---|
| LO 1/1982 (BOE-A-1982-11196) | `boe.py precepto` asegundo, acuarto, aquinto, aseptimo, anoveno; `.redacciones.tsv` | 2.1; 4.1-4.4; 5.1; 7.1, 7.2, 7.5, 7.7, 7.8; 9.1, 9.2; redacciones (art. 4: 2; art. 7: 3; art. 9: 2; vig. 23-12-2010 por BOE-A-2010-9953) |
| LO 5/2010, LO 10/2022, LO 2/2024, Ley 4/2015 | API de metadatos del BOE | Número y título |
| LOPSC (BOE-A-2015-3442) | `boe.py` a36, a39 | 36.23 (3 red., vig. 23-02-2021, notas SSTC 172/2020 y 13/2021, FJ 2.c); 39.1 |
| STC 172/2020 (BOE-A-2020-16819) | texto del BOE descargado hoy al scratchpad | Fallo 1.º y 2.º; FJ 7 C): censura previa, claves (i), (ii), (iii) |
| Ley 4/2015 (BOE-A-2015-4606) | `boe.py` a22, a34 | Literal y redacciones |
| LECrim (BOE-A-1882-6036) | `boe.py` a681, a682 | Literal; 4 y 2 redacciones; vigencias 22-08-2024 y 28-10-2015 |
| LOPDGDD (BOE-A-2018-16673) | `boe.py` a2-4 (art. 22) | Pasaje adaptado de Redactor 16 |
| Carta 2024-2029 (BOJA 247, 28-12-2023) | `.txt`, líneas 568-596 y 948-951 | 8.1.d) y n); 17.1 y su rúbrica |
| X Convenio (BOJA 240, 10-12-2014) | `.txt`, puesto 5341310 | Función básica y tres tareas |
| Libro de estilo 2004 (1.ª ed., marzo 2004) | `.txt` | 2.3.2.5, 2.3.2.10, 2.3.2.11, 5.1, 9.7, 9.7.1, 9.9, 9.9.1, 9.9.2; índice del cap. 9 (no hay epígrafe de catástrofes) |

## Hallazgos y correcciones aplicadas

| # | Error | Pasaje | Qué decía | Fuente | Corrección |
|---|---|---|---|---|---|
| 1 | 9 (dato no en la fuente) | Ep. 1, «Fallecidos», 4.3 | «podrá actuar de oficio o a instancia de persona interesada» | El BOE dice «podrá actuar de oficio a instancia de persona interesada», sin «o» | Se cita literal, en negrita, unido al inciso siguiente |
| 2 | 9 (menor) | Ep. 1, 9.2.a) | «publicación … de la sentencia» | «sentencia condenatoria» | Añadido «condenatoria» |
| 3 | 6 salvedad | Ep. 2, entrada de «Cámara oculta» | «sólo con autorización de la dirección y por interés público» | 2.3.2.5 admite además el peligro para la seguridad del informador | Reescrito con esa salvedad |
| 4 | 4 modo | Ep. 6, 9.9.2, el aviso | «no vale como única exculpación» | «Tampoco deberíamos recurrir, como única exculpación» | «no se debería recurrir» |
| 5 | prosa | Ep. 1, «Lo que la ley dice» | «Los verbos del 7.5 son tres» (son sustantivos) | — | «El 7.5 nombra tres conductas» |
| 6 | cita incompleta | «Normativa que el tema invoca» | Faltaban CE 20.1.d) y la DA 7.ª LOPDGDD, que el tema cita | — | Añadidas |

Todo lo demás de lo nuevo es literal o fiel: 2.1, 4.1-4.4, 5.1, 7.x, 9.1-9.2 de la LO 1/1982; 36.23 y 39.1 LOPSC;
fallo y FJ 7 C) de la STC 172/2020; 22 y 34 de la Ley 4/2015; 681 y 682 LECrim; Carta; Convenio; Libro de estilo.
Las remisiones adaptadas («en la tabla anterior», «en el epígrafe 3», «(epígrafe 1)», «vistos en el epígrafe 1»)
tienen su antecedente. «Epígrafe 5» (ep. 1 y 4) y «epígrafe 4» (ep. 5) también.

## Lentes

- `negritas.py` (15 fuentes, con la STC): 123 negritas; 12 «NO ESTÁ»: 9 del Libro de estilo por ligaduras «ﬁ/ﬂ» del
  `.txt` (cotejadas a ojo: literales), 3 en pasajes copiados del común; 681.3 LECrim sin volcado, cotejado con `boe.py`.
  Las 6 «atribuidas a otro artículo» son falsos positivos del anclaje (el artículo correcto está delante en la frase).
- `refutar_exactitud.py`: 20 «no literales», todos falsos positivos: el volcado de la LO 1/1982 usa artículos ordinales
  («Artículo séptimo») que la lente no ancla, y Libro/Carta no son volcados BOE. Cotejados a mano arriba.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 9.975 palabras, 36 epígrafes; índice sin cambios de rúbricas.

## Ficheros tocados

El tema 12 y este informe. STC 172/2020 descargada al scratchpad (fuera del repo).
