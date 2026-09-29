# Grafista (15) · Tema 1 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/01-diseno-grafico-television-radio-visual-web-redes-plataformas.md`.
Fecha de trabajo del encargo: 24-09-2026. Todas las fuentes se releyeron el 29-09-2026 (fecha de sistema).

Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad (`v15/01-antes-verif.md`).

## Lentes

Tema sin normas con articulado del BOE: no proceden `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`. `refutar_prosa.py`: 0 hallazgos; negritas rotas: ninguna. `indice.py`: 8.381
palabras, 37 epígrafes, índice sin cambios.

## Copiado: sólo comprobación de literalidad

- **Del común (Montador/a T12)**: «El servicio público digital de Canal Sur», «La expansión digital en
  la Carta…», «Multiplataforma, transmedia y gestor…», «Reencuadrar: oficio»: `diff` por epígrafe,
  idénticos (408, 181, 316 y 207 palabras).
- **Del común (Realizador/a T12)**: primer párrafo de «Qué es el grafismo» y los dos de HDR: literales;
  única diferencia, la remisión «tema 14» → «tema 8», correcta (el tema 8 de Grafista trata HDR/SDR,
  BT.2408-9 y EBU R 95).
- **De RTVE sin cambios** (02, 06, 08): cotejo automático fila a fila y párrafo a párrafo, sin negrita
  ni ✔: todas las tablas y frases listadas son literales. Diferencias encontradas, todas simples
  supresiones de incisos propios de RTVE: las ya declaradas como adaptadas y además tres no declaradas,
  inocuas: «que explica por qué esto se pregunta» (consecuencia práctica, UHD), «que es lo más útil
  de todo el punto» (zonas seguras) y «del tema 1» (monitor calibrado).
- **Adaptado de RTVE**: sólo quita remisiones al examen o a temas RTVE; el contenido es oficio y así lo
  declara la Trazabilidad. Sin dato nuevo que verificar. Añadido nuevo en el párrafo de zonas seguras
  («Recomendación EBU R 95 … tema 8»): confirmado en Realizador/a T12 (EBU R 95 v1.1, zonas seguras) y
  en el tema 8 de Grafista.

## Verificado en la fuente (todo confirmado salvo lo corregido)

| Fuente (leída 29-09-2026) | Datos comprobados |
|---|---|
| Carta del Servicio Público, BOJA 247, 28-XII-2023 (volcado local) | art. 6.8 (agregadores, radio y TV digital híbrida), 7.1 (páginas web con infográficos), 7.6 (TDT HD exclusiva desde 14-II-2024; cooperación UHD 4K); numeración de artículos y apartados |
| Contrato-programa, Acuerdo de 19-XII-2023, BOJA 245, 26-XII-2023 (volcado local) | cláusula tercera, apartado 3.5; puntos 46 (Canal Sur Media, agregadores, HbbTV, radio online), 47 (incluida la errata «interoperablidad», que es del BOJA) y 48 |
| Sánchez Cid y otros, *VISUAL Review* 17(1), 2025, pp. 179-192, DOI 10.62161/revvisual.v17.5410 (PDF del editor) | autores, título, volumen, páginas; los seis literales (nombres, rechazo de «televised radio», Ala-Fossi, debate, cuatro posibilidades, YouTube preferido por la muestra) |
| W3C, WCAG 2.2, Recommendation 12 December 2024 (w3.org/TR/WCAG22) | 1.1.1 (A), 1.4.1 (A), 1.4.3 (AA), 1.4.11 (AA): textos y niveles; fórmula de contraste y rango 1-21; texto grande 18 pt / 14 pt negrita; exención del logotipo; luminancia relativa normalizada de 0 (negro) a 1 (blanco): confirma la cuenta del 21:1 |
| MDN, «Diseño receptivo» (versión española, modificada 12-09-2026) | los seis literales (RWD, Marcotte 2010, tres técnicas, `max-width` al 100 %, «no es una tecnología independiente», m.example.com, director artístico); `<picture>`, `srcset`, `sizes`; tercera técnica «consulta a los media» |
| YouTube (vía Montador/a T12, cerrado) | las tres citas del epígrafe adaptado de relación de aspecto en redes, literales |

Cuentas rehechas: 8.294.400 y 2.073.600 píxeles (cuatro); 1,78 y 1,90; 1080 × 9/16 = 607,5 ≈ 608;
1,05 / 0,05 = 21. Remisiones a los temas 2, 4, 6 y 8: comprobadas en esos temas; 9, 10 y 13 aún no
redactados (coinciden con el enunciado).

## Correcciones aplicadas

1. **Error 5 (siglas sin presentar)**: «EBU» se usaba sin presentar (zonas seguras y «Lo que este tema no
   da»). Añadida a las siglas: Unión Europea de Radiodifusión (EBU, del inglés *European Broadcasting Union*).
2. **Error 1/9 (atribución)**: el tema decía que el artículo «atribuye» a Cavia Fraile (2016) la frase
   sobre si la radio con vídeo sigue siendo radio. En el PDF la cita de Cavia Fraile cierra la frase
   anterior; la dudosa no lleva cita. Cambiado a «lo plantea justo después de citar a Cavia Fraile, 2016».
3. **Negrita = literal**: en 1.4.11, «Graphical Objects: Parts of…» no es literal (los dos puntos son de
   maquetación; en el W3C es un rótulo y su texto). Separado en «Graphical Objects» y el literal.
4. **Error 6 (salvedad omitida)**: el 1.4.3 exime del contraste, además del logotipo, el texto
   incidental. Añadida una frase en redonda con las cuatro clases que enumera el criterio.
5. Trazabilidad: WCAG, MDN y *VISUAL Review* pasan a «29-09-2026 (investigación y verificación)».

## Sin corregir, a la vista

- El título del artículo va en minúsculas de frase; la revista lo imprime en mayúsculas de título. No
  es un error de dato.
- «No tiene norma ni definición legal» (radio visual): negativo que coincide con la investigación; no
  se ha encontrado nada que lo contradiga.
