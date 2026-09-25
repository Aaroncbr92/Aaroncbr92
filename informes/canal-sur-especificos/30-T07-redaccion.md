# Puesto 30 · Tema 7 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`.
Material: `30-investigacion-A-tecnica.md` (§ 7.1-7.4, más § 2.4 y § 4.1); `30-investigacion-B-montaje.md`
(§ 1.6, 9.4) y `30-investigacion-C-derechos-plataformas.md` (§ 11.1, subtítulos) para lo que el
bloque A no traía; cerrados de Canal Sur 28-05, 28-09 y 28-13 (Operador/a de Sonido); RTVE
`edicion-montaje/02`, `09`, `03` y `realizacion/20` («actualizar: no»).

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| *DaVinci Resolve 21 Reference Manual* (extractos guardados por la investigación, con marcas de página) | intro_color (pp. 3086-3093), primaries (pp. 3200-3204), scopes (pp. 3147, 3150-3152), luts (pp. 3545-3546), transitions (pp. 1194-1199), titles (pp. 1212-1215), fairlightfx (pp. 4091-4102, 4121-4122), render (p. 4193, 4198, 4204-4205), imf (p. 4219) | 25-09-2026 |
| Adobe, ayuda de Premiere (Wayback): «Transitions overview», «Audio editing with Essential Sound panel» (act. 07-01-2026) | Párrafos citados | 25-09-2026 |
| Informe UIT-R BT.2408-9 (txt) | Título, § 2.1 y § 9 «Graphics» | 25-09-2026 |
| Libro de Estilo de Canal Sur (txt) | 3.2.2, 3.6.1, 3.16, 9.2.12.3-4, 9.9, 9.9.1, 9.9.2, con su página impresa | 25-09-2026 |
| UBU, *Guía para elaborar Material Multimedia Accesible* (txt) | pp. 4-6, subtítulos | 25-09-2026 |

## Qué se hizo

Siete rúbricas en el orden del enunciado (color básico, corrección, efectos, grafismo, subtítulos,
transiciones, limpieza de audio), más una entrada sobre la postproducción en la sala y un supuesto
práctico. 49 epígrafes; `indice.py`: 12.214 palabras. `refutar_prosa.py`: 2 siglas sin presentar
(HVAC, SFX), corregidas; 0 hallazgos después. Tema técnico sin norma jurídica: no proceden
`negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

El reparto con temas vecinos: la colorimetría, los niveles legales y los monitores de medida van en
el tema 2 (que ya copió de RTVE 02 §§ 1-7); aquí se da RTVE 02 § 8 (LUT), que el tema 2 dejó para el 7,
y RTVE 03 §§ 5-6 (EQ, *ducking*). El *render* está en el tema 3 (RTVE 20 § 5) y no se repite.

Subtítulos: el encargo decía «subtítulos no» para RTVE; no había material RTVE, y se redactó con la
síntesis de la UNE 153010 del bloque C (UBU, fuente secundaria, dicho así en el tema) y el manual de
Resolve (salidas de subtítulos). El enunciado lo pide; no se deja fuera.

Negrita = literal de la fuente. Lo copiado de RTVE va en redonda (RTVE lo tenía en negrita sin ser
cita); lo copiado de los cerrados de Canal Sur conserva sus negritas, que sí son citas.

Comprobación de literalidad hecha por script (bloques del tema, normalizados los espacios y sin
negritas, buscados en la fuente): los 30 pasajes RTVE listados abajo aparecen tal cual.

## Copiado del común

Pasajes copiados de temas cerrados de Canal Sur (no se re-verifican). Lo único tocado son remisiones
a temas del puesto 28, que aquí no tienen antecedente: se quitan y se señalan.

`temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md`:

| Pasaje en 28-05 | Dónde va | Retoque |
|---|---|---|
| «Qué hace un ecualizador»: tabla de las tres formas y frase «La clasificación es de oficio, no de norma.» | § 7 «Ecualización» | En la celda del filtro de corte, «se desarrolla en «Filtros»» → «se desarrolla en «Los filtros de corte»» (título del epígrafe de este tema) |
| «Los filtros de corte», entero (párrafo de entrada, tabla, «Dos datos describen…», «*Rumble*…», «En la práctica…») | § 7 «Los filtros de corte» | Ninguno |
| «El filtro notch y el acoplamiento»: párrafo «Qué es un notch…» | ídem | Ninguno |
| «La clave externa y el *ducker*»: párrafo 1 entero y, del párrafo 2, las frases desde «En radio y televisión…» hasta el final | § 7 «La música bajo la voz» | Ninguno (se omiten las frases de megafonía y *talkover*) |

`temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`:

| Pasaje en 28-09 | Dónde va | Retoque |
|---|---|---|
| «Qué se limpia», entero | § 7 «Qué se limpia» | Se quitan «(tema 5)» de la celda de sibilantes, la frase «Los filtros (paso alto, ranura) y el reductor de sibilantes están explicados en el tema 5.» y «(temas 5 y 6)» |
| «La reducción de ruido por perfil», entero | § 7, epígrafe homónimo | Se quita «(tema 6)» |
| «Los artefactos», entero | § 7, epígrafe homónimo | Ninguno |
| «Limpieza de los diálogos, paso a paso», entero | § 7 «La limpieza de un diálogo, paso a paso» | Se quitan «(tema 5)» dos veces y «(tema 6)» |
| «La sonoridad del programa terminado», entero | § 7 «La sonoridad de la pieza terminada» | Se quitan «(tema 13)» dos veces |

`temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md`:

| Pasaje en 28-13 | Dónde va | Retoque |
|---|---|---|
| «Lo que fija la R 128»: primera tabla (h, i, m, k, n), la fila l) de la segunda tabla y la frase «Las tres cifras que hay que saber de memoria son −23 LUFS, ±1 LU y −1 dBTP.» | § 7 «La sonoridad de la pieza terminada» | Ninguno |
| Ídem, matices 2 y 3 | ídem | Numeración 2 y 3 pasada a viñetas |

## Copiado de RTVE sin cambios

Palabras sin tocar; sólo se quitó la negrita. Temas RTVE marcados «actualizar: no». Donde se omite una
frase entera (siempre la de «Ésa es la respuesta oficial…»), se dice.

`temas/realizacion/20-postproduccion.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 10, párrafo 1 («El etalonaje es la fase de posproducción…») | § 1 «Qué es etalonar» |
| § 10, las dos frases «Un etalonaje no toca sólo el color: … no todos.» (del segundo guion) | ídem |
| § 11, tabla de usos (cabecera y cuatro filas) | § 1 «Las LUT» |
| § 9, párrafos 1 y 2 («Un fotograma clave…», «Y la curva de velocidad…») y párrafo «Y por qué esto importa en un rótulo…» | § 3 «Fotogramas clave y curva de velocidad» |
| § 8, tabla de formatos gráficos, frase «El fichero gráfico que nunca tiene canal alfa es el JPG.» y línea de la suma de bits | § 4 «Los ficheros gráficos» |

`temas/edicion-montaje/02-colorimetria.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 8, frase «Las LUT son tablas de consulta…» (sin «Ésa es la respuesta oficial…»), párrafo «Cómo funcionan…» y tabla de tipos | § 1 «Las LUT» |

`temas/edicion-montaje/09-incrustaciones-grafismo-y-postproduccion.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 1, párrafo 1, tabla de familias y párrafo «Por qué el fondo es verde o azul…» | § 3 «Incrustar» |
| § 2, frase 1 (sin «Ésa es la respuesta oficial…»), tabla y párrafo «Y por qué no son cuatro…» | § 3 «Las tres señales de una incrustación» |
| § 3, párrafo 1 y tabla; del párrafo «Los valores intermedios…», sus dos primeras frases | § 3 «El canal alfa» |
| § 4, frase de la definición (sin «Ésa es la respuesta oficial…»), párrafo «Cómo funciona…» y párrafo «El aviso de oficio…» | § 3 «La máscara» |

`temas/edicion-montaje/03-conceptos-basicos-de-sonido.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 5, párrafo 1 («Ecualizar es cambiar…») y párrafo «La imagen que fija la definición…» | § 7 «Ecualización» |
| § 6, frase de la definición (sin «Ésa es…»), párrafo «Para qué sirve…», primera frase de «Cómo funciona…» y párrafo «Y una advertencia de oficio…» | § 7 «La música bajo la voz» |

## Adaptado de RTVE (sí se verifica)

- R20 § 10, tabla de fases del etalonaje: «rango legal del tema 5» → «del tema 2». Se añade «La tabla y
  la definición son de oficio».
- R20 § 11: «Una tabla de consulta es estática… ni del momento» reunido de la explicación de la
  pregunta 102.
- R20 § 9: «La curva de velocidad modifica… dos fotogramas clave» + «los fotogramas clave fijan el qué…»
  reunidos en una frase (sin «Ésa es la respuesta oficial…»).
- R20 § 8: primera frase («señal de llave del tema 10» → «señal de recorte del epígrafe 3»); razón del
  JPG, TGA de 32 bits, 24 bits y «bits por píxel/por componente», sin referencias a preguntas y
  «tema 5» → «tema 2».
- R02 § 8, aviso de oficio: se conserva «una LUT no corrige un plano mal expuesto… exagera el error»
  y se quita «Se aplica después de haber ajustado exposición y balance», que choca con el uso de
  normalización del material logarítmico que describe Blackmagic (manda la fuente). Se añade el aviso
  del recorte de la LUT 3D de Blackmagic.
- R09 § 1: «Las dos familias de incrustación» → «Las familias…» (error 3 de RTVE: la tabla tiene
  cuatro filas).
- R09 § 2: «Por qué son tres y no dos, que es todo el fondo de la pregunta:» → sin la cláusula.
- R09 § 3: se quita la frase del PNG/GIF («que se ve en el tema 5»); «notación 4:4:4:4 del tema 4» →
  «del tema 2».
- R03 § 6: se quita «Es un compresor con entrada lateral, y sus tres ajustes…»: Blackmagic dice del
  *ducking* **«This is achieved without compressing the incoming signals»** y los mandos del *ducker*
  según Rane (28-05) son ataque, mantenimiento y profundidad, no los de un compresor.
- No se copian de R09 los §§ 5-11 (After Effects, sin fuente: «sólo con la plantilla») ni de R20 los
  §§ 1-7 y 12-13 (otros temas o no pertinentes).

## Discrepancias encontradas (manda la fuente)

- RTVE 09 § 1 anuncia «dos familias» y tabula cuatro: se corrige.
- RTVE 03 § 6 presenta el *ducking* como compresor con entrada lateral; Blackmagic lo niega para su
  *ducker*. Se quita.
- RTVE 02 § 8 dice que la LUT «se aplica después» de ajustar exposición y balance; Blackmagic describe
  la LUT como punto de partida para normalizar material logarítmico. Se quita la frase.
- Libro de Estilo 9.2.12.4: la investigación B lo daba en pp. 130-131; la del virado está entera en la
  p. 130 y la de la música pasa a la 131 (se citan así). 9.9 («tramados») está en la p. 166 y 9.9.2
  («ocultar parcialmente», «ralentización») en la p. 167.
- UBU: la investigación C daba «p. 4» para abiertos/cerrados; en el texto el párrafo cae tras el pie
  «4»: se cita «pp. 4-5», y los requisitos «pp. 5-6».
- BT.2408-9: el título es *Guidelines for operational practices in high dynamic range television
  production* (corregido en el tema tras releer la portada).
- Adobe cuenta «15 frames» para una transición de «1:00» (un segundo a 30 imágenes por segundo); el
  tema da la cifra como de Adobe y hace la cuenta a 25 como cálculo propio.

## Ficheros tocados

- Creado: el tema `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`.
- Creado: este informe.
- Ningún otro (un borrador del epígrafe 7 en el directorio de trabajo temporal, fuera del proyecto).

## Preguntas de control (10) y cobertura

| Nº | Rúbrica | Pregunta y respuesta | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Color básico (teoría) | Si a una LUT 3D pensada para rango completo le llega vídeo con superblancos: a) los comprime suavemente; b) los recorta ✔; c) los ignora y pasa la señal sin transformar; d) los convierte a HDR | Entera, § 1 «Las LUT» (cita de Blackmagic y *shaper LUT*) |
| 2 | Color básico (aplicación) | En el vectorscopio, la gráfica de un plano está desplazada del centro hacia el verde. Indica: a) exceso de saturación general; b) una dominante verde ✔; c) negros recortados; d) contraste alto | Entera, § 1 «Medir antes de tocar» (centro = 0 saturación; desplazamiento = *color cast*) |
| 3 | Corrección (teoría) | El mando *gamma* de la corrección primaria actúa sobre: a) las sombras; b) los medios tonos ✔; c) las altas luces; d) todo el rango por igual (eso es el *offset*) | Entera, § 2 «*Lift*, *gamma* y *gain*» |
| 4 | Corrección (aplicación) | Plano con dominante verdosa por un tubo fluorescente. El ajuste más directo en Resolve: a) subir *Temp*; b) llevar *Tint* hacia magenta ✔; c) bajar la saturación; d) subir el *lift* | Entera, § 2 «Temperatura, matiz…» (el matiz hacia magenta es «menos verde» contra el fluorescente) y supuesto práctico |
| 5 | Corrección (teoría) | Un cualificador HSL es, en la práctica: a) una LUT 1D; b) un recorte por color (*chroma keyer*) que define dónde se corrige ✔; c) una ventana geométrica; d) un monitor de señal | Entera, § 2 «La corrección secundaria» |
| 6 | Efectos (teoría) | En una composición por incrustación intervienen: a) dos señales; b) tres: fondo, relleno y recorte ✔; c) cuatro, contando el alfa; d) una. (Variante: el formato gráfico que nunca lleva alfa es el JPG; un TGA con alfa tiene 32 bits) | Entera, § 3 «Las tres señales…» y § 4 «Los ficheros gráficos» |
| 7 | Efectos (Canal Sur) | Según el Libro de Estilo de Canal Sur, los rostros de menores, víctimas o testigos protegidos, si hay factor de riesgo: a) se emiten con permiso de la familia; b) serán cubiertos o tramados ✔; c) se emiten en plano general; d) se ralentizan | Entera, § 3 «Los efectos y la información» (9.9) |
| 8 | Grafismo (HDR y zonas) | En un programa HLG, el blanco de un rótulo se inserta, según el Informe UIT-R BT.2408: a) al 100 %; b) al 90 %; c) al 75 % ✔; d) al 58 % (el de PQ). (Variante: la zona segura de título de Resolve por defecto es el 90 % y la de acción el 93 %) | Entera, § 4 «El grafismo en alto rango dinámico» y «Las zonas de seguridad» |
| 9 | Subtítulos | Según la síntesis de la UNE 153010 de la Universidad de Burgos, el máximo de caracteres por línea y la velocidad recomendada son: a) 42 y 20 c/s; b) 37 y unos 15 c/s ✔; c) 32 y 12 c/s; d) 37 y 20 c/s. (Variante: el subtítulo abierto va incrustado y el espectador no lo controla; los formatos de fichero que da Resolve son IMSC1, DFXP, SRT y WebVTT) | Entera, § 5 |
| 10 | Transiciones y limpieza de audio (aplicación) | Al poner en Resolve un fundido de 1 s en un corte sin colas suficientes, el programa: a) lo pone igual con cuadros negros; b) ofrece recortar los planos (*Trim Clips*), saltar esos cortes (*Skip Clips*) o cancelar ✔; c) congela el último cuadro; d) alarga el plano con cámara lenta. (Variante de audio: un zumbido de red en España se quita en 50 Hz y sus armónicos con un filtro de ranura o un reductor de zumbido; la pieza terminada ha de medir −23 LUFS con pico verdadero no superior a −1 dBTP) | Entera, § 6 «Las colas» y § 7 «Qué se limpia», «Los filtros de corte», «La sonoridad de la pieza terminada» |

Resultado: 10 de 10 contestadas enteras con el tema; no hizo falta ampliar tras las preguntas (sí se
había ampliado antes, al redactar, el epígrafe 5 de subtítulos, que el reparto RTVE no cubría).
Cobertura: color básico (1, 2), corrección (3, 4, 5), efectos (6, 7), grafismo (8), subtítulos (9),
transiciones y limpieza de audio (10); aplicación práctica en 2, 4, 7, 8 y 10. Otras preguntas que el
tema también contesta: fases del etalonaje; fundido *Video* lineal frente a *Film* logarítmico; duración
por defecto de un título en Resolve (5 s); orden de limpieza de un diálogo; artefactos de la reducción
espectral; ±0,2 LU de la Tech 3343 en postproducción; promociones como «programa» en la R 128; máximo
de cuatro o cinco elementos y ocho segundos para un gráfico (Libro de Estilo 3.16).
