# Realizador/a (puesto 33) · Tema 5 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo; fuentes locales releídas en esta sesión).
Tema: `temas/canal-sur-especificos/33-realizador-a/05-puesta-en-escena.md` (11.079 palabras según
`indice.py`, 49 epígrafes; antes 11.111).

## Fuentes releídas

| Fuente | Fichero | Qué se ha comprobado |
|---|---|---|
| RD 1680/2011 (BOE-A-2011-19599, texto original; BOE núm. 302, de 16-12-2011) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | Título y fecha; nombres de los módulos 0902-0905; 0902 RA 2 y 2.b-2.e; 0903 RA 3.c-3.f, 4.b, 4.c, 4.e; 0904 RA 4.b, 4.c y contenidos; 0905 RA 3.a-3.f, RA 4 y 4.a-4.f, contenidos («Coordinación de las actividades del plató», «previsión de maniobrabilidad», continuidad visual, efectos) |
| RD 500/2024 (BOE-A-2024-10685) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | Art. séptimo.Uno (sólo módulos transversales); «Cuarenta» y anexo XLI (profesorado); nota de afectados: arts. 2, 10, 12, 15, anexos I y III. Los módulos 0902-0905 no cambian |
| INCUAL IMS077_3 (publicación: Orden PCI/797/2019) | `fuentes/canal-sur/realizador/incual-IMS077_3.txt` | Título; «Publicación»; ámbito profesional («siempre bajo las órdenes…»); UC0216_3 RP1 y CR1.1, CR4.1-4.3, CR4.6-4.8, CR5.1-5.6; MF0216_3 CE5.1-5.3, C8, CE8.2 (siete comprobaciones), contenidos del apartado 7 |
| X Convenio RTVA, BOJA núm. 240, de 10-12-2014, anexo III | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Fichas y páginas: 5351000 (p. 196), 5353000 (p. 111), 5333000 (p. 123, «estenografía» [sic]), 5341111 (p. 133), 9540003 (p. 128), 5345100 (p. 129), 5341310 (p. 116); cláusula final común |
| Libro de Estilo, 1.ª ed., marzo de 2004 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` | 8.5 (cita en p. 121), 8.6 (p. 121), 8.6.1 (p. 122): nueve pautas, verbos de cada una |
| Ley 10/2018 (consolidada) | `fuentes/canal-sur/BOE-A-2018-15240.md` | Sólo la «Normativa»: DT 1.ª.5 existe con ese texto |

Todas leídas el 24-09-2026. `negritas.py` con las siete fuentes: 101 negritas (una nueva, «deberán
tener muy en cuenta»), 5 «no están»: las mismas cinco pautas de 8.6.1 con ligaduras (ﬁ, ﬂ);
cotejadas a mano, literales. `refutar_modo.py` (Ley 10/2018): 0. `refutar_exactitud.py`: no aplica
(sin articulado en volcado .md salvo la DT copiada del común). `refutar_prosa.py`: 0. `indice.py`: correcto.

## Lo copiado: sólo comprobación de literalidad

- **Copiado del común** (tema 32/07): extraídos los nueve epígrafes de ambos ficheros y comparados
  con `diff`. Idénticos salvo las supresiones declaradas (cláusula final de «Quién rige el plató»,
  último párrafo de «Entradas y salidas», segundo de «Cuando algo falla», frase final de «Los oficios
  del plató») y el tercer párrafo de «La accesibilidad del plató», nuevo, que sí se ha verificado
  (oficio declarado; remisión al tema 16 correcta).
- **Copiado de RTVE sin cambios**: cotejo frase a frase y fila a fila, sin negritas ni ✔, contra
  `temas/realizacion/19`, `temas/realizacion-tv/19` y `temas/realizacion/04`. Todo lo listado es
  literal. Lo no listado (ciclorama «Se estira…» y color, camafeo «El nombre viene…», decorado
  combinado, riostra, ferma, filas adaptadas) se ha verificado.

## Correcciones aplicadas

| # | Pasaje | Error | Antes → ahora | Fuente |
|---|---|---|---|---|
| 1 | Ficha, IMS077_3 | 9 | «actualización por Orden PCI/797/2019» → «publicación: Orden PCI/797/2019» | IMS077_3, p. 1 |
| 2 | Siglas | 5 (a la inversa) | Se quitan CAD y RP: presentadas y nunca usadas | — |
| 3 | 2, El ciclorama | 3 / 9 | «el gris o el blanco, la práctica más común; blanco, negro y verde, los colores más frecuentes» (recuento contradictorio y sin fuente) → gris o blanco, práctica común; también negro y verde; «(oficio)» | — (oficio) |
| 4 | 2, Estilos escenográficos | 9 | Se quita la etimología «El nombre viene de la joya: un camafeo es una figura clara… sobre fondo oscuro uniforme» (sin fuente leída) | — |
| 5 | 2, Vestuario | 4 | «las demás desaconsejan» incluía la 9, que es un deber («deberán tener muy en cuenta») → se separa la 9 | LE 8.6.1, punto 9 |
| 6 | 2, Vestuario | 1 (antecedente) | «El RD pone las dos cosas en los ensayos» remitía a las «dos razones técnicas» del maquillaje → vestuario, peluquería, maquillaje y caracterización | 0903 RA 3.d |
| 7 | 3, Qué se le dice al cámara | 9 | «que se fijen de antemano» → «que se determinen» (RA 4.e no dice «de antemano») | 0905 RA 4.e |
| 8 | 4, Movimiento de las personas | 6 | «el RD pide dirigir «la acción…»» → «al dirigir la grabación, coordinar «la acción…»» | 0903 RA 4.b |
| 9 | 5, Quién marca | 9 | «el primer paso del trabajo del ayudante» → «la primera realización profesional de la unidad UC0216_3» | UC0216_3, RP1 |
| 10 | 7, Norma de enseñanza | 9 | «pide al realizador, antes que nada» → «el primer criterio del RA 3 del mismo módulo pide» | 0905 RA 3.a |
| 11 | Aplicación práctica | 9 | «el supuesto práctico típico» y «Tres casos que se preguntan en una prueba práctica»: no hay exámenes anteriores → «un supuesto práctico del tipo…» y «Tres casos de prueba práctica» | ENCARGO |

Releídos los pasajes cambiados: cada remisión tiene su antecedente.

## Comprobado sin hallazgo

- Todas las citas del RD en su módulo y letra (0 cruzadas); seis criterios del RA 4 de 0905; tres
  comprobaciones 3.b-3.d; RA 2 de 0902 con 2.b-2.e.
- IMS077_3: CE5.2 y CE5.3 (ficción y variedades) piden las cuatro plantas; CE5.1 es de informativo;
  CE8.2 tiene siete comprobaciones y el tema lista seis y remite la primera (dos comprobaciones) a
  «Marcas»; cuatro reglas CR5.3-5.6.
- Convenio: siete códigos y páginas; «Localizar escenarios…» del Decorador omitido sin alterar sentido.
- LE: nueve pautas; 7 «está prohibido», 6 «no se utilizarán»; 8.5 dirigido al periodista en plató.
- Remisiones internas a temas 1, 2, 6, 8, 9, 12, 13 y 16: los epígrafes citados existen
  («El eje en multicámara», «Cómo se cruza el eje», «La composición en el plató», «La continuidad en el
  plató», «Movimientos de cámara», «El plano en la realización de televisión»; tema 2, orden
  decorado-personas-cámaras y marcas en la planta de cámaras).
- «Marcas en el suelo»: sólo en IMS077_3 (0 en el RD y en el LE); el hueco declarado se mantiene.

## Para la refutación

- Queda como oficio declarado el montaje del ciclorama con pesas y listón (sin fuente técnica leída;
  en RTVE procedía de una respuesta de examen).

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/05-puesta-en-escena.md`.
- Creado: este informe. Ninguno más.
