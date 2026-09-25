# Puesto 08 · Tema 1 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/01-camara-sensores-opticas-exposicion.md`
(≈9.800 palabras tras la verificación). Copiado del común: ninguno (según `08-T01-redaccion.md`), así que
se ha verificado todo, incluido lo copiado de RTVE (`informacion-grafica/03`, `04`, `08`).

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Cómo |
|---|---|
| EBU R 103 v3.0 (mayo 2020) | Descargada de tech.ebu.ch/docs/r/r103.pdf, pasada a texto con `documento.py` (copia en el scratchpad de la sesión, no en `fuentes/`) |
| EBU R 118 v2 (abril 2017) | tech.ebu.ch/docs/r/r118.pdf, ídem |
| EBU Tech 3335 (agosto 2014) | tech.ebu.ch/docs/tech/tech3335.pdf, ídem |
| Sony PXW-Z200 Help Guide 5-060-574-13(1) | Copia local `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt` |
| Sony PXW-FS5 Operating Guide 4-581-849-11(1) | Descargada (URL de Emory del informe de investigación) |
| Blackmagic URSA Broadcast G2, nov. 2021 | Descargada (URL de Markertek) |
| Canon XF605, PUB. DIE-0559-000B, especificaciones | Descargada (global.canon, dhc898_en.pdf) |
| Nota Fujifilm UA22x4.8BERD, 18-03-2026 | Copia local `fuentes/fabricantes/Fujinon_UA22x4.8_nota.txt` |

Resultado del cotejo literal: todas las negritas citadas de estas ocho fuentes aparecen tal cual (incluidas las erratas del
original «in used», «let down (or even…» y el título sin cerrar). Las versiones EBU descargadas son las que da el tema como
vigentes (R 103 v3.0, R 118 v2, Tech 3335 08/2014).

## Correcciones aplicadas

| Nº | Error | Pasaje | Qué había | Qué queda |
|---|---|---|---|---|
| 1 | 3 recuento | Niveles UHD (R 118 § 1.2) | «dos niveles por resolución» seguido de cuatro niveles | «dos niveles en cada una de sus dos resoluciones» |
| 2 | 9 / negrita no literal | Ídem | «**≥ 2715 x 1527**», «**≥ 5430 x 3054**» (el signo no está en la fuente) | «**at least 2715 x 1527**», «**at least 5430 x 3054**» (literal) |
| 3 | 6 salvedad | Tabla 2 de R 118 | «admite los dos diseños en todos sus niveles» | Salvo HD Tier 4 y Tier SP, para los que la tabla dice «Broadcaster to advise» |
| 4 | 6 salvedad / 4 modo | Tabla 6 de R 118 | «fija la relación señal/ruido mínima» | «da la relación señal/ruido apropiada», con «Guidance only» en 2L y 2J y «For guidance» en 3 |
| 5 | 6 salvedad | Método de sensibilidad R 118 § 3.1.2 | Sin la condición | Añadido: gamma desactivada o curva estándar sin *knee* (así lo exige la fuente) |
| 6 | 9 | Tech 3335 § 4.4 | «Cada 6 dB … cuestan un paso» | «aproximadamente» (la fuente: «about 1 stop per 6dB») |
| 7 | 9 | AF Z200 [Wide] | «busca el sujeto en todo el cuadro» | «en una zona amplia» (fuente: «over a wide angle of the image») |
| 8 | 9 | Preajustes de balance Z200 | «en modo estándar» (no existe ese nombre) | «modo de grabación personalizado (*Custom shooting mode*); en el logarítmico cambian» (log: 3200/4300/5500 K) |
| 9 | 6 salvedad | ND de la FS5 | «posiciones 1/4, 1/16, 1/64» | «posiciones con valores de fábrica» (la fuente: «Default is 1/4»…) |
| 10 | 9 | Ganancia | «Las cámaras dan la ganancia en conmutador de tres posiciones» | «Muchas cámaras» (generalización sin fuente) |
| 11 | 9 | Tabla de filtros | Polarizador «elimina» | «reduce» |
| 12 | 8 cita | Tech 3335 | Citas de margen sobre blanco (§ 2.4) y medida con log al 50 % (§ 2.3) atribuidas sin sección; trazabilidad «§ 2.9 y 4.4» | Secciones puestas en el texto; trazabilidad «§ 2.3, 2.4, 2.9 y 4.4» |
| 13 | redacción | Hiperfocal | «distancia de enfoque a partir de la cual» (sugiere un umbral) | «distancia de enfoque con la que» |
| 14 | redacción | Criterios R 118 | «se tratan más abajo, en su epígrafe» (son tres epígrafes) | «cada uno en su epígrafe» |

Cada corrección se comprobó en la fuente antes de aplicarla, y cada pasaje cambiado se releyó: todos los antecedentes
(«la tabla», «la fuente», «el 3») tienen delante su referente.

## Comprobado y sin cambios

- R 103 tabla 1 (8 y 10 bits), error de gama, 1 %, recortadores en directo, 0-700 mV: literales.
- R 118: finalidad de los niveles, SDR, 2J, 33 % del nivel 3, códec, cinco áreas, tamaños de sensor y
  procesado (10-bit/4:2:2; 8-bit (10-bit preferred)), píxel y resolución, § 3.1.3-3.1.5, ganancia negativa.
- Tech 3335 § 2.9 (persiana; 1/50, 1/60, 180°), § 4.4 (7,5 pasos, 1-3 extra, 12-13 pasos).
- Z200: sensor, zoom, diafragma, difracción, brida, estabilizador, foco manual, tiraje automático (2 m, F2.8, 0 dB,
  menú), realce, lupa ×3/×6, AF (fase+contraste, velocidad, sensibilidad, caras, push AF), FULL AUTO, push iris,
  obturación por ángulo, parpadeo (modos y 50/60 Hz), cebras (0-109 %, 70 %, 10 %, 2-20 %, 100 %), monitor de señal,
  aspectos base, balance (WHT BAL A/B/PRESET, 3200K de fábrica, WB SET), ATW y ATW Hold, ganancia −3/+36 dB y L/M/H,
  ajuste fino, ND (presets, variable, Auto ND, aviso de grabación), filtro 72 mm, píxeles blancos.
- FS5, URSA G2, XF605 y Fujinon: todas las citas, literales.
- Oficio revisado sin hallar error: CCD/CMOS, Bayer (½ verde, ¼ rojo, ¼ azul), focal y ángulo, escala f, velocidad,
  profundidad de campo y hiperfocal (focal, diafragma, círculo), sensor y PdC, cinco aberraciones de Seidel,
  adaptación por brida, dB/pasos (20·log₁₀2 ≈ 6), ND en pasos (1/4=2, 1/16=4, 1/64=6, 1/128=7), 1/50-1/100 con
  red de 50 Hz, polarizador a 90° del sol, bandera ajustada en angular.
- «*Back focus* o foco de carro»: término de la respuesta oficial de un examen de RTVE (pregunta 103 del tema RTVE
  de origen); se mantiene como denominación atestiguada.
- Siglas: todas presentadas en la entrada; las que sólo salen dentro de citas (LCD, HDMI, MF, S/N) no requieren
  presentación. «PUB» (señalada por `refutar_prosa.py`) es código de catálogo de Canon: falso positivo.

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (1 hallazgo, falso positivo «PUB») e `indice.py` (índice correcto,
52 epígrafes). No se pasan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py` (no cita normas del BOE/BOJA).

## Discrepancias con el encargo

Ninguna. Nota: las recomendaciones EBU y los manuales de FS5, URSA y XF605 no tienen copia en `fuentes/`; se
descargaron para esta verificación a un directorio temporal. Si se quieren conservar, habría que guardarlas en
`fuentes/normas-tecnicas/` y `fuentes/fabricantes/` (no lo he hecho por limitarme al tema).

## Otros ficheros tocados

Ninguno, salvo el tema y este informe. (`02-lenguaje-visual.md` y `15-…md` aparecen modificados en el árbol de
trabajo, pero no por esta verificación.)
