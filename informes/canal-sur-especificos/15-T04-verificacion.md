# Grafista (15) · Tema 4 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/04-infografia-y-visualizacion-de-datos.md`. Fecha de
trabajo del encargo: 24-09-2026. Fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. Nada más.

## Pasajes copiados: sólo comprobación literal

Cotejo por script (sin negritas, espacios normalizados, ligaduras «ﬁ» → «fi») contra el original:

- **Copiado del común** (`34-redactor-a/15-periodismo-de-datos-informacion-publica.md`): los siete
  bloques de la lista del redactor son literales (tabla de variables y su párrafo; tabla de gráficos por
  variable y párrafo barras/histograma; «Los gráficos en televisión» hasta el penúltimo párrafo;
  «Las cifras en la noticia»; viñetas y párrafos de §3; párrafo de correlación y viñeta LE 3.3;
  viñetas LE 9.2.10, 4.3.2, 4.3.2.1, primera frase del recuento propio y bloque de la Ley 37/2007
  desde «El artículo 8…»). No se re-verifican. `negritas.py` marca dos citas de ese bloque (LE 3.16.1 y
  9.2.10) como no encontradas: es un salto de página del volcado (cabecera «LIBRO DE ESTILO…» y número
  de página en medio); leídas a mano, son literales.
- **Copiado de RTVE sin cambios** (`diseno-grafico/08-…`): definición, tabla de tipos, tabla
  «Qué se quiere mostrar / Gráfico», reglas 2 y 3 y el aviso final son literales.
- **Adaptado de RTVE**: los dos rótulos recortados y la regla 1 («En un gráfico de barras…»). La
  restricción a barras la sostiene la guía británica (*charts*, «Do not break the numerical axis on bar
  charts» / «it is acceptable to break a numerical y-axis on a line chart»). Correcto.

## Fuentes releídas

| Fuente | Qué se cotejó |
|---|---|
| Carta 2024-2029, BOJA 247/2023 (volcado .txt) | arts. 7.1 y 10.1 |
| Contrato-programa 2024-2026, BOJA 245/2023 (volcado .txt) | Acuerdo de 19-XII-2023; cláusula tercera, puntos 16, 28 y 48; definición de «Canal Sur» |
| Libro de estilo, 1.ª ed., marzo 2004 (volcado .txt) | 3.2.2, 3.16.2 (ubicación de las citas nuevas), 6.5.1, 6.5.2, 9.2.12.3; portadilla |
| WCAG 2.2, W3C Recommendation 12-XII-2024 (copia de la fase 1) | 1.1.1 (y excepción «pure decoration»), 1.3.3, 1.4.1, 1.4.3, 1.4.11, niveles A/AA, *contrast ratio*, *large scale* |
| Analysis Function, *Data visualisation: charts* (publicada 19-05-2022; copia de la fase 1) | todas las citas y sus glosas |
| Analysis Function, *Data visualisation: colours* (23-11-2021, act. 12-02-2026) | todas las citas y sus glosas |

Todas las negritas nuevas están en su fuente (script + `negritas.py`: 136 cotejadas, 0 atribuidas a
otro artículo). Cuentas de «Cuentas que se piden» rehechas: correctas.

## Correcciones aplicadas (12 pasajes; el 13 es comprobación sin cambio)

1. Siglas: la Carta **no** llama «Canal Sur» a CSRTV; lo hace el Contrato-programa («Canal Sur Radio y
   Televisión, Sociedad Anónima (Canal Sur)»). La Carta dice «los medios de Canal Sur». (error 9)
2. Portada, Fuente: Ley 37/2007 «(artículo 8)» → «(artículos 4, 8 y 11)», que son los que el tema usa. (3)
3. Visual Vocabulary: la cita empezaba con minúscula («the…»); el original es «The Visual Vocabulary tool
   from the Financial Times can help you choose the best chart». Cita completada. (literal)
4. Títulos: «la guía pide dos títulos» → la guía exige al menos uno y tiene por buena práctica dos
   («All charts need at least one title, but it is considered best practice to give them two»). (4)
5. «Do not use a key, label the categories themselves» está en el apartado de los sectores (*Formatting
   pie charts › Labels*), no es regla general: rótulo «Etiquetas de los sectores». (6)
6. Regulador británico: el 27-II-2023 es la fecha del tuit en que la OSR anuncia que ha escrito al
   Tesoro, no la de la carta. Reescrito. (9)
7. Proporción de las líneas: la «línea razonablemente neutra» la propone un artículo al que la guía
   remite, no la guía. (9)
8. Carta 10.1 en §4: la cita decía «siempre conforme»; el original es **«siempre conformes»**. Frase
   reescrita con el literal exacto. (literal)
9. LE 3.2.2: «sucesos con muerte… o abusos» → «sucesos o noticias con resultado de muerte… o
   situaciones de abuso», como el texto. (6)
10. LE 9.2.12.3: faltaba la salvedad «especialmente en un informativo diario» tras «poco recomendable». (6)
11. Notas al pie: la glosa «el cambio de metodología, la serie rota, el dato provisional» no está en la
    guía; quitada. (9)
12. Ley 37/2007, entrada (párrafo nuevo, no copiado): «Son las que un gráfico cumple si cita bien:»
    era inexacto (a, b, e y f no son de cita) y dejaba dos puntos sin lista; → «Varias de ellas las
    cumple un gráfico que cita bien la fuente y no altera el dato.» Quitada una línea en blanco doble.
13. (Revisado sin cambio) «Aim for a maximum for four lines»: errata del original, confirmada.

## Comprobado sin hallazgo

Carta 7.1 y 10.1 (salvo el n.º 8); Contrato-programa 16, 28, 48; LE 6.5.1, 6.5.2 («vidi wall», «con la
salvedad de que deberá…»), ubicación en 3.16.2 de «primar por su claridad», «no se firma» y el «redondeo
artificioso»; tabla de relaciones del *charts*; series temporales en barras sólo a intervalos iguales;
tres condiciones de los sectores; orden a las 12; «Keep it simple» con siete viñetas; hueco entre
barras; cuatro categorías por pila; corte del eje (barras, líneas, símbolo, número redondo, descripción,
diferencias respecto de una media); doble eje; pequeños múltiples; huecos en series; aspecto; fuentes,
descarga, notas, texto fuera de la imagen; alternativa textual y marcado decorativo con alt vacío; SVG;
sectores y ampliación; legislación británica A/AA; guía de colores (3:1 entre vecinos y su relación con
el 1.4.11, baja visión, leyendas, «the green line» bajo el 1.3.3, 4,5:1 por el reescalado, daltonismo
8 %/0,5 % dicho como cifra de la guía, escala de grises, fondo). WCAG: textos, niveles, fórmula, rango
1-21, texto grande 18/14 pt negrita, excepción decorativa.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 35 epígrafes, ~9.310 palabras. `negritas.py` contra
Carta, Contrato-programa, LE (sin ligaduras), WCAG, las dos guías y BOE-A-2007-19814: 2 «no está»,
ambos del bloque copiado y debidos a saltos de página (ver arriba). `refutar_exactitud.py` /
`refutar_modo.py` sólo tendrían objeto sobre la Ley 37/2007, que es bloque copiado del común: no se pasan.

Queda para refutación: la sigla LRISP se presenta y no se usa en el cuerpo (inocuo).
