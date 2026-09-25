# Tema 1 del específico de Cámara Operador · La cámara de televisión y vídeo

**Siglas**: Unión Europea de Radiodifusión (**EBU**); captación electrónica de noticias (**ENG**); producción electrónica en campo (**EFP**); unidad de control de cámara (**CCU**); acoplamiento de carga (**CCD**); semiconductor complementario de óxido metálico (**CMOS**); conversor analógico-digital (**ADC**); tabla de consulta (**LUT**); interfaz digital serie (**SDI**); alta definición (**HD/HDTV**), ultra alta (**UHD/UHDTV**); rango dinámico estándar (**SDR**), alto (**HDR**); híbrida log-gamma (**HLG**); control automático de ganancia (**AGC**); Organización de Normalización (**ISO**); densidad neutra (**ND**); enfoque automático (**AF**); balance automático continuo (**ATW**); decibelio (**dB**); kelvin (**K**); lux (**lx**); cuadros/segundo (**fps**); rojo-verde-azul (**RGB**).

Esqueleto, no resumen. Telegrama, fuente delante de cada línea; se quita explicación, no el dato. Vigente el **24/09/2026**. Sin norma jurídica: solo recomendaciones EBU y manuales de fabricante (Sony, Canon, Blackmagic, Fujifilm/FUJINON) y oficio.

<!-- indice -->

## Índice

- [La cámara de televisión y vídeo](#la-cámara-de-televisión-y-vídeo)
- [Sensores](#sensores)
- [Ópticas](#ópticas)
- [Enfoque](#enfoque)
- [Exposición](#exposición)
- [Balance de blancos](#balance-de-blancos)
- [Ganancia](#ganancia)
- [Filtros](#filtros)
- [Fuentes citadas](#fuentes-citadas)
- [Lo que este tema no da](#lo-que-este-tema-no-da)

<!-- /indice -->

## La cámara de televisión y vídeo

- oficio — Familias: **ENG** (autónoma, un operador, al hombro) · **EFP/estudio** (cuelga de **CCU**, triax/fibra) · cine digital (autónoma, etalonaje).
- oficio — Operador: encuadre, foco, movimiento, ejecuta orden · Control de imagen: nivel, color, sombras, luces, detalle entre cámaras.
- EBU R 118 v2, § 1.2 — *Tiers* (EBU Tech 3335) por género; asume SDR salvo consulta a la emisora. HD T1 (hombro) · 2L (larga forma) · 2J (informativos, relajado) · 3 (semipro, **~33 %** máx.) · 4/SP (con aprobación) · UHD1 T1 **3840×2160**/T2 **≥2715×1527** · UHD2 T1 **7680×4320**/T2 **≥5430×3054**. Criterios: códec (si grabación propia), ruido, sensibilidad, margen, resolución y *aliasing*.
- oficio — Del fotón al fichero: fotosito (carga) → tensión amplificada → **ADC** digitaliza → procesador aplica ganancia, balance, curva y compresión.

## Sensores

- oficio — CCD: lectura pozo a pozo, obturación global, *smear*, más consumo, en desuso · CMOS: amplificador por fotosito, barrido, obturador de persiana, menos consumo, estándar hoy.
- Sony Z200 / Canon XF605 (fichas) — Sensor **1.0" CMOS** en ambas.
- EBU Tech 3335, § 2.9 — Persiana solo en CMOS: verticales inclinadas y distorsión en movimiento rápido.
- oficio — Color: **tres sensores + prisma dicroico** (bloque clásico 2/3") o **un sensor + máscara de Bayer** (mosaico RGB, 50 % verde, *demosaicing*, menos sensibilidad/resolución de color); distinta del filtro paso bajo (antimuaré, no da color).
- EBU R 118 v2, tabla 2 — Tamaño por nivel: UHD1T1 **1×1"**/3×2/3" · HDT1 **1×2/3"**/3×1/2" · T2L **1×1/2"**/3×1/3" · T2J **1×1/3"**/3×1/4"; T1 exige **10-bit 4:2:2**, T2L/2J **8-bit (10 preferente)**.
- EBU R 118 v2, § 3.1.4-3.1.5 — El recuento de píxeles no es la resolución; el *aliasing* se mueve al revés que la cámara y daña la compresión.
- Sony Z200 Help Guide — Puntos blancos aislados (rayos cósmicos), no avería; más con temperatura o ganancia altas.

## Ópticas

- oficio — Focal: mm del centro óptico al plano de imagen, al infinito; ángulo inverso a la focal, depende del sensor. Gran angular: focal corta, ángulo amplio · normal: focal ≈ diagonal · tele: focal larga, ángulo estrecho.
- Sony Z200 / Canon XF605 (fichas) — Equivalentes 35 mm: Z200 **24-480 mm** · XF605 **15x, F2.8-4.5**.
- convención del sector — Referencia de zoom: nº antes de «x» = relación; nº después = focal mínima; focal máxima = relación × mínima.
- Fujifilm, FUJINON UA22x4.8BERD (18/03/2026) — «4,8-106 mm»: 22×4,8=105,6≈106.
- oficio — Nº f = focal/diámetro de pupila; menor f = más luz. Escala: 1,4·2·2,8·4·5,6·8·11·16·22. Velocidad del objetivo = menor f.
- Sony Z200 / Canon XF605 (fichas) — Apertura variable en zoom: Z200 **F2.8-F4.5** (mín. F11) · XF605 **F2.8-4.5**.
- Fujifilm, especs. UA22x4.8BERD — Extensor 2x: 4,8-106→9,6-212 mm; ángulo tele de 5,2°×2,9° a 2,6°×1,5°.
- FUJINON, FAQ — Extensor 2x cuesta **2 pasos** de luz · Sony X400: indicador «EX» avisa del extensor puesto.
- Sony Z200 Help Guide — Cerrar mucho con mucha luz da difracción; se corrige con ND.
- oficio — Profundidad de campo: diafragma más cerrado → más · focal más larga → menos (misma distancia de enfoque) · más distancia → más. Solo vale a igual distancia de enfoque; si se retrocede al mismo encuadre, apenas cambia.
- oficio — Círculo de confusión: máximo desenfoque indistinguible de nítido, entra en profundidad e hiperfocal. Hiperfocal: enfoque con el que de su mitad al infinito queda nítido; factores: focal, diafragma, círculo (no la obturación).
- oficio — Sensor grande no reduce la profundidad por sí mismo: obliga a focal más larga para igual encuadre, y esa focal la reduce.
- oficio — Aberraciones de Seidel: esférica, coma, astigmatismo, curvatura de campo, distorsión (barril/corsé); aparte, la cromática.
- oficio — *Bokeh*: estética del desenfoque (láminas del diafragma), distinto de profundidad, *flare* y *knee* (electrónico).
- Sony Z200 Help Guide — Brida: de montura a sensor · oficio — 2/3" usa montura B4.
- FUJINON, FAQ — Brida corta se adapta a cuerpo de brida larga con anillo, al revés no; expansores B4-PL cuestan **1-1½ pasos**.
- Sony Z200 Help Guide / Canon XF605 (ficha) — Con trípode, apagar estabilización ([Active] cierra el plano) · XF605: óptica + digital.

## Enfoque

- Sony Z200 Help Guide — Manual necesario: cristal con gotas, bajo contraste, sujetos a distinta distancia, cambio brusco de temperatura.
- oficio — Técnica con zoom: cerrar a tele, enfocar, abrir al encuadre; con tiraje bien ajustado el foco se mantiene. Tiraje (*back focus*): distancia montura-sensor; 4 pasos: enfocar en tele → ir a angular sin tocar foco → corregir con anillo de tiraje → repetir el recorrido, diafragma abierto.
- Sony Z200 Help Guide — Autoajuste sobre carta a **~2 m**, F2.8, 0 dB, menú [Auto FB Adjust].
- Sony FS5 / Z200 Help Guide / Blackmagic — *Peaking*: color y sensibilidad ajustables, no se graba; Z200: High/Mid/Low, B&W/Red/Yellow/Blue; Blackmagic: «peaking» y «colored lines». Lupa: amplía zona, no se graba ni sale por SDI/HDMI; Z200 amplía **3x** y **6x**.
- Sony Z200 Help Guide / Canon XF605 — AF: fase (rápido)+contraste (preciso); XF605: Dual Pixel CMOS AF+contraste, detección de cara. Ajustes: zona (Wide/Zone/Flexible Spot), velocidad (1 lento-7 rápido), enganche al sujeto (1 fijo-5 sensible), detección de cara/ojo/cuerpo; momentáneo vuelve a manual al soltar.

## Exposición

- oficio — Cuatro mandos: diafragma (profundidad), obturación (nitidez de movimiento, parpadeo), ND (solo luz), ganancia (ruido). Orden con poca luz: diafragma → obturación → más luz → ganancia último.
- Sony Z200 Help Guide — AUTO activa ND, iris, AGC, obturador y ATW a la vez; diafragma automático momentáneo vuelve al valor previo.
- oficio / EBU Tech 3335, § 2.9 — Obturación en velocidad o ángulo (360°=cuadro, 180°=mitad); nominal **1/50 s a 50 Hz**, **1/60 s a 59,94 Hz**, o **180°**.
- oficio — Tiempo = ángulo/360 × cuadro: 180° a 25 fps=1/50 s; a 50 fps=1/100 s; 360° a 50 fps=1/50 s.
- Blackmagic URSA G2 — 25→50 fps reduce la luz a la mitad; compensar con un paso, 180°→360° o más luz.
- Sony Z200 Help Guide / oficio — Parpadeo bajo fluorescente/sodio/mercurio/LED; corrección 50/60 Hz; en Europa, 1/50 o 1/100 lo evita.
- Sony FS5 / Z200 Help Guide — Cebra no se graba; Z200: dos cebras 0-109 %, 1ª a 70 % (margen 10 %, 2-20 %), 2ª a 100 %; visor con onda, vectorscopio, histograma.
- Blackmagic URSA G2 — Falso color: rosa piel clara, verde piel oscura, amarillo→rojo sobreexpuesto; escala no normalizada.
- EBU R 103 v3.0, tabla 1 — Código: 8 bits nominal **16-235**, preferente **5-246**, total **1-254**; 10 bits **64-940**/**20-984**/**4-1019**; fuera de preferente = error de gama; no exceder el total; analógico 0-700 mV.
- EBU R 103 v3.0 — Directo con luz no controlada: recortadores al límite Preferente; pregrabado/etalonado: límite Nominal.
- oficio — Los porcentajes «−1 %/103 %» no están en la R 103 v3.0 vigente.
- oficio — *Knee*: comprime luces sobre el codo sin cambiar sensibilidad; punto, pendiente, recorte de blancos.
- EBU Tech 3335, § 2.4/4.4 — Margen sobre blanco **1-3 pasos**; cámara con ruido **-50 dB** capta **~7,5 pasos**; **-1 paso** cada **6 dB** de ruido; gamma/*knee* ganan **≥1 paso** (hasta 3, total 12-13).
- oficio — Log reparte valores en todo el rango; visor lavado sin LUT; LUT de monitorización recupera contraste sin tocar lo grabado, por salida.
- Sony Z200 Help Guide — LUT independiente SDI/HDMI y LCD/VF/Proxy/Stream, apagadas de fábrica, solo en log; aspectos: ITU709, S-Log3, HLG (Live/Mild/Natural).
- EBU R 118 v2, § 3.1.2 / EBU Tech 3335, § 2.3 — Sensibilidad: diafragma con pico blanco a **2000 lux**, 0 dB; en log, al **50 %** (~2 pasos bajo el pico).
- Canon XF605 (ficha) — Ejemplo: 2000 lux, 89,9 % reflectancia, 50,00P: **F13**.

## Balance de blancos

- oficio — Ajusta la cámara a la temperatura de color de la escena, sin cambiarla; iguala ganancia de R y B.
- Canon XF605 (ficha) — Preajustes **5.600 K** (día), **3.200 K** (tungsteno).
- oficio — Tres caminos: carta blanca (fiable, con tiempo) · preajuste 3200/5600 K (sin tiempo) · ATW (luz sin control, deriva de tono).
- Sony Z200 Help Guide — Procedimiento: memoria A/B (PRESET=3200K fábrica) → encuadrar blanco → ajustar brillo con diafragma manual → WB SET; preajustes **3200-4300-5600-6300 K** o manual **2000-15000 K**.
- Sony Z200 Help Guide — ATW falla con color dominante o temperatura extrema; función ATW Hold.
- oficio — ATW es enemigo del montaje; en multicámara el balance debe igualarse, a cargo del control de imagen.
- Sony X400 — Balance de negros: conmutador AUTO W/B BAL, posición BLACK; hace falta al primer uso, tras mucho sin usar, cambio grande de temperatura o cambio de ganancia; no por estar apagada.
- Sony X400 — Salida CAM, BLACK; ajusta negro y luego balance, diafragma se cierra solo («NG: Iris not Closed» si no); no funciona grabando ni en SLS; guarda en memoria.
- Sony Z200 Help Guide — Sin balance de negros automático; solo niveles Master/R/B Black manuales.

## Ganancia

- oficio — Amplificación electrónica en dB, con su ruido; no añade luz. **+6 dB=1 paso** (20·log₁₀2≈6); +3 medio paso, +12 dos, +18 tres (ya ruidosa).
- Sony Z200 (ficha) / Canon XF605 (ficha) — Z200: ISO/GAIN L/M/H, **−3 a +36 dB** · XF605: **ISO200-12800**, **−6 a 21,0 dB**.
- EBU R 118 v2, tabla 6 y texto — S/N: HD T1 **mejor de −48 dB** a 0 dB; T2L **mejor de −44 dB** (orientativo); T2J/T3 **mejor de −40 dB** (orientativo); ganancia negativa mejora S/N; cada 6 dB de ruido cuesta ~1 paso de margen; sube visibilidad de píxeles blancos.
- oficio — Levantado de negros abre sombras a costa de contraste y ruido; dependencia del nivel reduce el realce en zonas oscuras. Ganancia es el último recurso: el ruido no se quita después.

## Filtros

- Sony Z200 (ficha) / FS5 (ficha) / Canon XF605 (ficha) — ND interno: Z200 Clear/1(1/4)/2(1/16)/3(1/64), ajustable 1/4-1/128, variable 1/4-1/128; FS5 igual; XF605 Off/1/4/1/16/1/64 motorizado.
- oficio — Pasos: 1/4=2, 1/16=4, 1/64=6, 1/128=7 (2^pasos); «clear» no es filtro.
- Sony Z200 Help Guide — Auto ND permite exposición automática sin tocar diafragma ni profundidad.
- Sony FS5 / Z200 Help Guide — Cambiar ND grabando distorsiona imagen/sonido; Z200 graba el ruido del mecanismo al usar «clear».
- oficio — ND evita difracción con mucha luz y permite abrir diafragma (menos profundidad) sin sobreexponer; por sí solo no cambia la profundidad.
- oficio — Filtro de conversión cambia la temperatura de la luz; hoy se corrige sobre todo con balance electrónico.
- Sony Z200 (ficha) — Diámetro de filtro **72 mm**.
- oficio — Delanteros: polarizador (reduce reflejos, oscurece cielo a 90° del sol, nulo hacia él), degradado (oscurece parte del cuadro), difusor (suaviza), UV/protección (siempre); bandera francesa hace sombra al objetivo, se ajusta en angular.

## Fuentes citadas

- EBU R 103 v3.0, *Video Signal Tolerance in Digital Television Systems*, mayo 2020.
- EBU R 118 v2, *Tiering of Cameras for use in Television Production*, abril 2017.
- EBU Tech 3335, *Methods of measuring the imaging performance of television cameras*, agosto 2014.

## Lo que este tema no da

- Qué cámaras/ópticas usa CSRTV: no consta en documento publicado localizado.
- AF de doble píxel de Canon; obturador global en estudio actual: fuentes no leídas.
- Distancias de brida en mm por montura: no leídas. Nivel HDR en % (Informe UIT-R BT.2408): no leído.
- Temperatura de color y geles → tema 5 · profundidad narrativa → tema 2 · calidad de imagen → tema 9 · formatos/códecs → tema 7 · cámara lenta/*time lapse* → tema 15.
