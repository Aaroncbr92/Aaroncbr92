# Grafista (15) · Tema 1 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/01-diseno-grafico-television-radio-visual-web-redes-plataformas.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas y descargadas el 29-09-2026 (fecha de sistema).
Entrada: `15-T01-refutacion.md` (0 graves, 5 menores, 1 laguna) y `15-T01-preguntas.md` (13 enteras, 1 a medias, 1 no).
Copia previa: `scratchpad/15t01-antes-remate.md`.

**Ficheros tocados**: el tema; este informe; `fuentes/canal-sur/grafista/` (nuevos: `hbbtv-org-overview.txt`,
`android-tv-design-for-tv.txt`, `android-tv-layouts.txt`, `android-tv-typography.txt`; línea añadida en `README.md`).

## Correcciones (cada una comprobada en su fuente antes de aplicarla)

| Hallazgo | Comprobación | Pasaje cambiado |
|---|---|---|
| M1 · 4:5 sin fuente | Ninguna fuente del tema da el 4:5 como formato de redes (sólo aparece en páginas ajenas al tema: miniatura automática de YouTube y anuncios de Meta). Se aplica: se quita | l. 184 «(9:16, 1:1)»; epígrafe «Relación de aspecto en redes» («o en cuadrado (1:1)»; TikTok, Instagram y Facebook «y con ellas cualquier otro formato intermedio que admitan; no se dan»); «Una identidad…» («redes en 9:16 o 1:1»); tabla práctica («1:1 si la red lo pide»); «Lo que este tema no da» |
| M2 · negativos absolutos | Correcto: no se pueden confirmar | «De dónde sale este tema» («no consta norma…», «No consta que Canal Sur haya publicado…»); «Qué es la radio visual» («No consta norma ni definición legal que la regule»); «Lo que este tema no da» (manual de identidad: «No consta…»; radio visual: «Tampoco se ha encontrado…») |
| M3 · siglas sin uso | IU, UX, PNG, JPEG, SVG: una sola aparición cada una, en las siglas | Siglas de entrada: quitadas |
| M4 · salvedad 1.4.11 | `wcag22.txt`, l. 532: «except for inactive components or where the appearance of the component is determined by the user agent and not modified by the author» | Tabla WCAG, fila 1.4.11, columna «Qué exige»: añadida la excepción (literal en negrita + redonda); rótulo «Tres precisiones de las propias pautas que se preguntan (dos definiciones y una exención)» |
| M5 · literal cortado | `radiovision.txt`: la frase sigue «that extends beyond the boundaries of traditional radio but does not fully align with the conventions of television.» | «Qué es la radio visual»: literal completado y traducción ampliada |

## Laguna: plataformas digitales (preguntas 14 y 15) — se amplía el tema

Nuevo epígrafe `### Plataformas OTT y televisión conectada` (epígrafe 4, entre «Reencuadrar» y «Una identidad, muchas
salidas»), unas 900 palabras:

- Qué es HbbTV (definición literal de la HbbTV Association), funciona mejor con emisión y banda ancha a la vez;
  qué ve el espectador (aviso con el botón rojo en una esquina), qué ofrece la aplicación, manejo con botones de
  colores, cursor y numéricos, usos enumerados, los televisores no se actualizan («In general no.»).
- Lo que toca al grafista (oficio declarado); no consta que Canal Sur emita hoy aplicaciones HbbTV.
- Tabla de diseño para TV según Android Developers: distancia de 3 m, cruceta y foco, aumento del elemento
  enfocado, 16:9 fijo, margen de en torno al 5 % (la guía da dos juegos de cifras, 48/27 y 58/28 dp, que no
  cuadran entre sí: no se copian) y «Most modern TVs no longer have overscan issues», tipografía, aparato compartido.
- Consecuencia para Canal Sur Más (oficio): dos interfaces, una identidad.

Pasajes derivados: la pauta «se diseña pensando en la salida más estrecha» se acota a piezas de vídeo e imagen,
y se remite al epígrafe nuevo para la interfaz de televisor (la refutación señaló que empujaba a la respuesta
errónea en la pregunta 15). También: portada (Fuente, Redacción que se estudia, Extensión 9.400), «Qué se puede
preguntar», índice, Trazabilidad (dos filas nuevas) y lista de oficio.

Con el tema ampliado, las preguntas 14 y 15 pasan a **enteras** (15/15).

## Fuentes leídas (29-09-2026)

- HbbTV Association, «HbbTV Overview», https://www.hbbtv.org/overview/ (definición, «How It Works - For Consumers», FAQ).
- Android Developers (Google), «Design for TV» (actualizada 08-05-2023), «Layouts» (09-05-2025), «Typography» (06-07-2026).
- Contrato-programa 2024-2026, punto 46 («servicios bajo estándar europeo HbbTV»): literal comprobado.
- WCAG 2.2 (`wcag22.txt`); Sánchez Cid y otros, *VISUAL Review* 17(1), 2025 (`radiovision.txt`).

No se usó la ETSI TS 102 796 que sugería la refutación: no se leyó; la definición sale de la página de la asociación.

## Lentes

- `indice.py`: índice regenerado, 9.409 palabras, 38 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (Contrato-programa, Carta, WCAG, HbbTV, Android, artículo de radio visual, BT.2408): 85 cotejadas;
  las 22 negritas nuevas o cambiadas, todas literales. Las 14 «no están» son pasajes no tocados cuyas fuentes
  (Libro de Estilo, MDN, YouTube) no se pasaron, más la enumeración del artículo partida por el PDF.
- Antecedentes relidos: «(puntos 45 y 46, arriba)» remite a «El servicio público digital de Canal Sur»;
  «(epígrafe anterior)» en «Una identidad…» remite al nuevo epígrafe, que va justo delante.

El remate amplió contenido: toca la fase 5 bis sobre el epígrafe nuevo y los pasajes de la tabla.
