# Tema 4 del específico de Grafista · Infografía y visualización de datos: claridad, rigor, ética, fuentes y representación accesible

**Siglas**: RTVA; CSRTV; LE (Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía, 2004); W3C; WCAG; AF (Government Analysis Function, Reino Unido); IPC; LOPDGDD; INE; SVG; PNG; JPEG.

Esqueleto para repasar, no resumen: lo que no está aquí se estudia en el tema.

<!-- indice -->

- [1. Infografía y visualización de datos](#1-infografía-y-visualización-de-datos)
- [2. Claridad](#2-claridad)
- [3. Rigor](#3-rigor)
- [4. Ética](#4-ética)
- [5. Fuentes](#5-fuentes)
- [6. Representación accesible](#6-representación-accesible)
- [Aplicación práctica](#aplicación-práctica)

<!-- /indice -->

## 1. Infografía y visualización de datos

- Sin norma que regule la infografía. Fuentes: Carta y Contrato-programa (BOJA 247 y 245), LE, WCAG 2.2, AF, Ley 37/2007. Estadística = oficio.
- Infografía = información gráfica que se entiende más deprisa que leída; explicar, no ilustrar. Tipos: de datos (electorales, presupuestos); de proceso (vacuna, accidente); de situación (mapas, plantas).
- Carta 10.1: calidad «en todas sus vertientes», también «infográfica», conforme a deontología y códigos de autorregulación. Contrato-programa cláusula 3.ª punto 28: igual.
- Carta 7.1 y Contrato-programa 3.ª punto 48: web con contenidos «infográficos». Punto 16: «prestaciones infográficas» en informativos.
- LE 6.5.2: imagen al servicio de «la eficacia, la accesibilidad y la claridad»; infografías, «vidi wall», plasmas = recursos. LE 6.5.1: forma y estética supeditadas al mensaje. Realizador: «supremacía del sentido informativo».
- Variables: cualitativa nominal (sin orden; moda) / ordinal (orden sin distancia; moda, mediana, cuantiles) / cuantitativa discreta / continua (media, varianza, desviación típica). Nominal codificada con números sigue nominal.
- Comparar = barras; evolución = líneas; composición = sectores (pocas categorías); dos variables = dispersión; geografía = coropletas.
- AF: distribution = bar, population pyramid, box plot, dot plot; time series = line, calendar heat map; ranking = bar, lollipop, slope; deviation = bar, dot plot; correlation = scatterplot, line; magnitude = bar; spatial = map; part-to-whole = bar, pie, donut, tree map, bubble; flow = Sankey.
- AF: Visual Vocabulary del Financial Times ayuda a elegir. Más de una serie temporal: líneas, no barras.
- Por variable: barras (cualitativa o discreta, separadas); sectores (cualitativa, pocas categorías); histograma (continua agrupada, contiguas, área proporcional a la frecuencia); polígono de frecuencias; ojiva (acumuladas); caja y bigotes (mediana, cuartiles, recorrido, atípicos); dispersión (dos cuantitativas); pictograma (cualitativa).
- Histograma con amplitudes distintas: densidad de frecuencia; altura = frecuencia distorsiona.

## 2. Claridad

- AF: si el mensaje no cabe en unas pocas frases, replantear el gráfico. Buena práctica: «a headline title and a formal statistical subtitle»; subtítulo = qué dato, territorio, periodo. TV: subtítulo «Paro registrado. Andalucía. Agosto 2026» (oficio).
- LE 3.16: gráfico eficaz para IPC, inflación, hipotecas, tipo de interés, presupuesto de inversiones, índices de paro. Moderación; sin flash.
- LE 3.16: «no más de cuatro o cinco elementos por pantalla», presencia mínima recomendable de «ocho segundos».
- LE 3.16.1: gráfico dinámico; cada elemento en paralelo a la locución, «referencial», no exhaustiva.
- LE 3.16.2: «cama» de audio por el canal correspondiente, salvo sonido propio de la grabación. Claridad y precisión, sin aspectos técnicos o artísticos que dificulten. Orden alfabético, sobre todo topónimos andaluces, salvo mayor a menor o viceversa, comparación o evolución. «La información elaborada exclusivamente con gráficos no se firma.»
- LE 3.16.1 redondeo: exactitud en el gráfico; evitar cifras terminadas en 1 y 9; decenas, centenas, millares, millones; más redondeo cuanto más alta la cifra; vale para todo texto informativo. Preferir cuarta parte, tercio, mitad, nueve de cada diez a 26, 33, 51, 89 por ciento.
- LE 3.16.2: cifras microeconómicas (inflación, tipos, valores, combustibles): «no podemos tender al redondeo»; décimas o centésimas. Euribor: 25 centésimas preferible; «un cuarto de punto» admisible; 40 centésimas a «medio punto» = inexacto.
- LE 7.2.2: cifras de economía precisas, aunque redondeadas, e interpretadas; preferible «un cuarto de punto»; trasladar a la economía doméstica. Discrepa del 3.16.2 en la preferida; ambas descartan el redondeo que falsea.
- AF sectores: ≤5 categorías; suman un todo con sentido (agrupar sí, quitar nunca); categoría dominante (si parecidas, barras). Ordenar por tamaño desde las 12 en punto. Sin leyenda: rotular.
- AF líneas: máximo cuatro. Barras apiladas: máximo cuatro categorías por barra. Hueco entre barras menor que una barra.
- AF «Keep it simple», evitar: fondos sombreados, bordes innecesarios, cajas en leyendas, tramas/texturas/sombras, 3D, marcadores innecesarios en líneas, retículas gruesas u oscuras.

## 3. Rigor

- Tres reglas de honradez: barras con eje desde cero; el área representa el dato, no el lado (diámetro doble = cuádruple); misma escala en todo el gráfico.
- Barras 50 y 52 sobre eje desde 48 = barras de 2 y 4; real 4 %. Líneas: eje no cero puede justificarse, indicándolo.
- AF barras: cortar el eje «problematic and highly controversial»; alternativa: Cleveland dot plot. Ejemplo: Office for Statistics Regulation, 27-II-2023, a HM Treasury; eje desde 8 %; 11,1 % (oct. 2022) a 10,1 % (ene. 2023).
- AF líneas: cortar «acceptable», si necesario: símbolo de eje roto; desde número redondo (50-90 %, no 54,3-93,5 %); mencionarlo en la descripción; antes, plantear diferencias respecto de una media.
- TV (oficio): eje cortado = número de arranque visible; en barras, no cortar.
- Símbolo que crece en dos dimensiones: área cuatro veces.
- AF doble eje: no recomendado (se malinterpreta; la posición relativa manipula); mejor separar, cada uno con su eje. Pequeños múltiplos: todos los ejes con la misma escala.
- AF huecos: señalar siempre; no unir los puntos de los lados, ni discontinuo («Joining points implies we know something»).
- AF proporción: en líneas cambia la pendiente; sin proporción fija. Tema: de 16:9 a vertical, rehacer, no estirar.
- Puntos porcentuales: 10 % a 12 % = 2 puntos y +20 %; «un 2 %» es falso.
- Tasas: absolutos no comparan territorios; dividir por población × base fija (1.000 o 100.000); decir base y año. 10.000 hab. con 50 casos = 500 por 100.000; 200.000 con 200 = 100; cuatro veces más casos, tasa cinco veces menor. Coropletas: colorear con tasa (oficio).
- Real = nominal × (IPC año base / IPC año del dato). Variación real = (1 + nominal) / (1 + IPC) − 1. Salarios +3 %, IPC +4 %: 1,03/1,04 − 1 = −0,96 %; restar (−1) sólo aproxima con tasas pequeñas. Serie larga en euros: subtítulo dice corrientes o constantes y año.

## 4. Ética

- Obligan: Carta 10.1 y Contrato-programa 3.ª punto 28 (únicas dos menciones expresas); LE 3.16.2; LE 6.5.1.
- LE 3.2.2 («Imágenes ‘falsas’»): reconstrucciones y simulaciones prohibidas como norma general; si imprescindibles en noticia importante, rótulo «reconstrucción» todo el tiempo en pantalla; escrupulosos en muerte, heridas graves, suicidios, abuso.
- LE 9.2.12.3: reconstrucción poco recomendable, sobre todo en informativo diario; arriesgado usar escenas de cine; alternativa: cámara subjetiva por los escenarios sin personaje ni actor; montaje de ficción inevitable = rótulo «Reconstrucción» obligatorio todo el tiempo.
- No hacer: quitar una parte del todo (AF); unir puntos de un hueco (AF); escala, corte, doble eje o proporción para agrandar o achicar; redondeo artificioso (LE 3.16.2); elegir el periodo que conviene (oficio, sin regla escrita); relación como causa.
- Correlación no es causalidad (razonamiento propio): tercera variable, sentido inverso o casualidad; verbos «sugiere», «indica» (LE 7.1.3).
- LE 3.3 informe: datos «solventes u oficiales» o «nítidamente identificados como fuente»; no «sucesión de cifras»; tesis concreta; sin acumulación de datos sin conclusión; sin abuso de cifras, gráficos, postproducciones o alardes técnicos.

## 5. Fuentes

- LE 9.2.10: error no identificar con claridad el origen de una cifra; cada cifra a su tipología y vinculada a la fuente.
- LE 4.3.2: contrastar el dato en fuentes oficiales o citar con toda precisión su origen.
- LE 4.3.2.1: cifras dispares (huelga, manifestación): cifra propia, a razón de dos, tres o cuatro personas por m²; indicar cálculo propio y método, en miles o decenas de miles, sin excluir las de organizadores o policía local; manifestaciones pequeñas: siempre el dato propio junto a los demás.
- Gráfico (oficio): fuente dentro, con organismo y estadística; «Elaboración propia con datos del INE» si hay cálculo; fuentes distintas, no mezclar en una serie sin avisar. LE 3.16.2: no se firma (autor); la fuente, sí.
- AF: fuente concreta de cada gráfico, enlace directo; no «Office for National Statistics» con enlace a portada. Formato «[publicación, encuesta u otra fuente] from the [organisation]»; «Fuente: Encuesta de Población Activa, del INE».
- AF: datos del gráfico en descarga accesible; notas al pie evitan mal uso; en web, fuente en el texto de la página, no en la imagen. TV: rótulo legible todo el tiempo.
- Ley 37/2007, art. 8: condiciones «podrá estar sometida, entre otras» (las fija la Administración, p. ej. licencia): a) contenido y metadatos no alterados; b) no desnaturalizar el sentido; c) citar la fuente; d) fecha de última actualización; e) datos personales: finalidades concretas; f) si disociada aún identifica: prohibido revertir la disociación con nuevos datos.
- Art. 4.7: reutilizador «bajo su responsabilidad y riesgo»; responde en exclusiva frente a terceros. Art. 4.6: datos personales, LOPDGDD.
- Art. 11: leves 11.3.a (falta de fecha de actualización) y c (ausencia de cita, art. 8), multa 1.000-10.000 € (11.4.c). Muy grave 11.1.a: desnaturalizar el sentido bajo licencia; 50.001-100.000 € (11.4.a). Salvedad: apartado 1 referido al «ámbito de la Administración General del Estado».

## 6. Representación accesible

- WCAG 2.2, Recomendación W3C 12-XII-2024. Norma española y nivel obligado = tema 10.
- 1.1.1 (A): todo contenido no textual, alternativa textual equivalente; excepción «pure decoration».
- 1.3.3 (A): instrucciones sin depender sólo de forma, color, tamaño, posición, orientación o sonido.
- 1.4.1 (A): color no único medio de transmitir información o distinguir elementos.
- 1.4.3 (AA): texto 4,5:1; texto grande 3:1; grande = 18 puntos o 14 en negrita.
- 1.4.11 (AA): «Graphical Objects» (partes necesarias para entender) 3:1 frente a colores vecinos.
- Contraste = (L1 + 0.05) / (L2 + 0.05); L1 más claro, L2 más oscuro; rango 1 a 21.
- AF alternativa: tabla de datos o descripción del mensaje. Se espera leer los datos: tabla; idea general: descripción; ambas: las dos. Descripción: no repite título, no literal, no enumera cada dato. Si va en el cuerpo debajo, imagen decorativa (alt vacío).
- AF colores: limitar número; categóricos sin agrupar, un solo color; misma variable, mismo color; asociaciones culturales; tonos de un color sugieren relación.
- AF categórica: límite de cuatro categorías; «Ideally, use just the first four». Secuencial: un tono o pocos próximos, de claro a oscuro. Otra paleta, sólo «when absolutely necessary»: no cumple accesibilidad por sí sola.
- AF contraste: colores vecinos 3:1 (baja visión); líneas y sectores rotulados, sin leyenda; no «la línea verde» (1.3.3); texto en imagen 4,5:1 siempre que se pueda, aun grande (se reescala).
- AF: daltonismo 8 % hombres, 0,5 % mujeres (cifra de la guía, no contrastada). Comprobar en escala de grises. Nunca imagen de fondo.
- AF SVG: mejor formato; no pierde calidad; PNG o JPEG convertido a SVG no es escalable, exportar del original. Sectores: difíciles ampliados. Reino Unido: A y AA de WCAG 2.2.
- Emisión: WCAG para web; sin umbral para rótulos de TV; 4,5:1 en antena = analogía de oficio. LE 6.5.2 «accesibilidad».
- TV (oficio): luminosidad y no sólo tono; rotulación directa; texto en zona segura; la locución lleva el mensaje. Subtitulado, audiodescripción, lengua de signos = tema 10.

## Aplicación práctica

- Eje cortado: (52 − 50)/50 × 100 = 4 %. Área doble: diámetro × √2 ≈ 1,41; diámetro doble = 2² = 4.
- Tasa: 50 / 10.000 × 100.000 = 500 por 100.000. Valor real: 1,03 / 1,04 − 1 ≈ −0,96 %.
- Contraste máximo: (1 + 0,05)/(0 + 0,05) = 21; colores iguales 1:1.
- 16 puntos sin negrita: no es texto grande; 4,5:1.
- No lo da el tema: manual o código ético de Canal Sur; guía española de visualización; umbral en emisión; luminancia relativa; zona segura y formatos = tema 8; 3D = 5; tiempo real = 6; plantillas = 9; derechos = 11; IA = 15.
