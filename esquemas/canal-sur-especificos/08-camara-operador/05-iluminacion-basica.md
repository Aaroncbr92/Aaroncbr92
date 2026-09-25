# Esquema · Tema 5 del específico de Cámara Operador · Iluminación básica para cámara

**Siglas**: Radiocomunicaciones de la UIT (**UIT-R**); Unión Europea de Radiodifusión (**EBU**); captación electrónica de noticias (**ENG**); diodo emisor de luz (**LED**); haluros metálicos (**HMI**); filtro naranja (**CTO**) y azul (**CTB**); densidad neutra (**ND**); reproducción cromática (**IRC/Ra**); consistencia de iluminación para TV (**TLCI**); protocolo DMX; kelvin (**K**); lux (**lx**), lumen (**lm**), candela (**cd**); mired.

Esqueleto para repasar. Todo desarrollado y verificado en el tema. Se quita explicación, nunca el dato.

<!-- indice -->

## Índice

- [Qué decide la luz y sus magnitudes](#qué-decide-la-luz-y-sus-magnitudes)
- [Ley inversa del cuadrado y equipo ligero](#ley-inversa-del-cuadrado-y-equipo-ligero)
- [Temperatura de color](#temperatura-de-color)
- [El mired y los filtros de conversión](#el-mired-y-los-filtros-de-conversión)
- [Medir el color, dominante verde, IRC y TLCI](#medir-el-color-dominante-verde-irc-y-tlci)
- [Contraste](#contraste)
- [Clave alta y clave baja](#clave-alta-y-clave-baja)
- [Sombras](#sombras)
- [Luz natural](#luz-natural)
- [Luz artificial](#luz-artificial)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)

<!-- /indice -->

## Qué decide la luz y sus magnitudes

- Oficio: la luz decide 4 cosas a la vez — exposición, modelado, separación, atmósfera; plató sirve a todas las cámaras a la vez, más blanda y frontal; reportaje, maletín versátil y poca luz.
- Oficio, magnitudes: flujo luminoso (lm, toda la luz de la fuente); intensidad (cd, en una dirección); iluminancia (lx, la que llega, luz incidente); luminancia (cd/m², la que devuelve el sujeto, luz reflejada = lo que ve la cámara).
- Astera, ficha Titan Tube: **1340/2900/5800 lm** según longitud, «Typical values».

## Ley inversa del cuadrado y equipo ligero

- Cálculo: iluminancia ∝ 1/distancia². Duplicar distancia = 1/4 de luz (2 pasos menos); triplicar = 1/9 (algo más de 3 pasos); mitad de distancia = ×4 (2 pasos más). Oficio: luz cercana castiga el movimiento del sujeto; luz lejana perdona; fondo alejado queda más oscuro con la misma luz.
- Oficio, maletín: panel LED (principal de entrevista); foco de zapata (relleno de urgencia); Fresnel ligero (recorte/contraluz); foco abierto (mucha luz, poco peso); reflector/rebote y difusores/sedas (suavizar); banderas/recortadores (quitar luz); filtros de color. 2 decisiones: dura/difusa (tamaño de fuente) y corregir/no corregir temperatura.
- Sony, *PXW-Z200 Help Guide*: luz de zapata HVL-LBPC con **[Power Link]** y **[Rec Link]**; función de preiluminación en grabación por intervalos.

## Temperatura de color

- Oficio: temperatura de un cuerpo negro con el mismo tono. Escala inversa: más K, más azul; menos K, más rojo.
- Fabricantes (Canon XF605, Blackmagic URSA Broadcast G2): **3.200 K** tungsteno/interior; **4.000 K** fluorescente; **4.500 K** luz mezclada; **5.500-5.600 K** día/exterior; **6.500 K** cielo nublado. Sony log: **5.500 K** día. Dos patrones de oficio, sin margen de duda: **3.200 K** y **5.500-5.600 K**.
- UIT-R BT.709-6 y BT.2020-2: blanco de referencia D65, «Cromaticidad... (Blanco de referencia) D65», **x = 0,3127**, **y = 0,3290**.
- EBU Tech 3355, tabla de radiadores de luz de día: a **6500 K**, x = **0.312787**, y = **0.329205** (equivale a D65).
- Regla: iluminar → 5.500-5.600 K; blanco de señal/monitor → D65 (~6.500 K).
- Canon XF605: recorrido **2.000-15.000 K**; Sony PXW-Z200: **2000K to 15000K**, eje verde-magenta ***Tint*** −99 a +99 en memoria de balance; balance corrige una sola temperatura a la vez, mezcla se corrige en la luz.

## El mired y los filtros de conversión

- Cálculo: mired = 1.000.000 / K. Tabla: 1.800 K=556; 2.700 K=370; 3.200 K=312,5; 4.000 K=250; 5.600 K=178,6; 6.000 K=166,7; 6.500 K=153,8; 10.000 K=100.
- Cálculo: tungsteno→día (3.200→5.600 K) = **−134 mired** (filtro azul, sube K); esos −134 mired sobre 5.600 K dan ~**45 mired** (>22.000 K): el mired funciona con cualquier fuente, el kelvin no.
- Sony PXW-Z200: pasos de 20 K hasta 5.600 K; por encima, paso = salto de K con igual cambio de color.
- Oficio: gel CTO (naranja) baja K/suma mired, tungsteno cálido; gel CTB (azul) sube K/resta mired, lleva a día; corrección de verde (magenta/verde); difusión (no cambia color); ND (gris, quita luz, no cambia color).
- Oficio: azul sube K, naranja baja K; todo filtro quita luz, ninguno añade.

## Medir el color, dominante verde, IRC y TLCI

- Sekonic, ficha SpectroMaster C-800: «Spectrometer (Color Meter)» + «Illuminance Meter»; mide K, da compensación y filtro, modo «Filter (Lighting/Camera)», selección de marca de filtro, mide LED/HMI/fluorescente/natural, da IRC y TLCI.
- Oficio: fotómetro mide cantidad, medidor de color mide tono; se mide cada fuente, se elige cuál manda, corrección en mired o gel.
- Oficio: LED/descarga con dominante verde/magenta; remedio en fuente (gel magenta/verde) o en cámara (Tint, solo si dominante uniforme).
- Sony PXW-Z100: preajuste bajo sodio/mercurio, avisa «may flicker or change colors».
- EBU Tech 3355 (marzo 2017): Qa/TLCI calibrado a **50** para tubo fluorescente típico de día, frontera corregible/no corregible; 2 lecturas — film-style (imágenes deben casar) vs multicámara en directo (basta creíble), «considerable overlap»; sin sentido absoluto de Ra ni Qa.
- Astera, ficha Titan Tube: «CRI(Ra)/TLCI 3200-6500k* ≥96», «Typical values».

## Contraste

- Oficio: relación de contraste = luz zona iluminada / luz zona en sombra (o sujeto/fondo); en pasos de diafragma. Cálculo: 2:1=1 paso; 4:1=2; 8:1=3; 16:1=4; 32:1=5. Relación = 2^pasos.
- Escala de f memorizada: 1 · 1,4 · 2 · 2,8 · 4 · 5,6 · 8 · 11 · 16 · 22.
- Cálculo, ejemplo: rostro f/8, fondo a 16:1 (4 pasos menos luz) → f/8→f/5,6→f/4→f/2,8→**f/2**.
- Oficio: bajar contraste = subir relleno (no bajar principal); subir principal sube contraste; bandera/reflector negro en sombra sube contraste; contraluz no toca la razón del rostro.
- Tema 1 (remite): margen de exposición, *knee*, cebra, falso color.
- Blackmagic, URSA Broadcast G2: 25→50 fps = mitad de luz al sensor; compensar con 1 paso más, obturación 180º→360º o luz extra.

## Clave alta y clave baja

- Adobe, *High key lighting vs low key lighting in videography*: clave alta «reduces the lighting ratio», menos contraste, más relleno y sombras más suaves; clave baja «greater contrast... a majority of the scene in shadow», poco relleno, luz dirigida.
- Oficio: clave alta ≈ 2:1 o menos, tonos claros, propia de informativos/magacín; clave baja ≈ 8:1 y más, propia de ficción/efecto.

## Sombras

- Oficio: dureza depende del tamaño aparente de la fuente, no de la potencia; más grande vista desde el sujeto = más suave. Sol lejano = dura; cielo cubierto = la más suave.
- Oficio, esquema de tres puntos: principal/llave, frontal-cruzada a 30-45°, algo elevada, define exposición y sombras; relleno, otro lado, más baja y suave, aclara sombras; contraluz, detrás, hacia el sujeto, elevado, separa del fondo. Añadidos: luz de fondo, luz de ojos, luces de efecto.
- Oficio, posición de la principal: cenital = ojos hundidos; desde abajo = inquietante, se evita; lateral 90° = máximo modelado; en eje de cámara = sin sombras ni volumen.
- Oficio, entrevista: principal del lado hacia el que mira; separar del fondo y elevar principal evita sombra proyectada en pared.
- Oficio, accesorios: bandera (tela negra, corta luz); velo/seda (translúcida blanca, difunde); rejilla/net (malla, baja intensidad sin cambiar dureza); pulmón/butterfly (área amplia, exterior); viseras/barn doors (recortan haz); cortadores (franjas); rebotador (blanco/plata/oro, relleno); ceferino/brazo articulado (sujeción, no normalizado).
- Prevención (tema 14): brazo articulado poco peso, cable de seguridad, pie lastrado con saco de arena.
- Oficio: luz por eje óptico (cristal a 45°) para reproducción sin sombra; montaje = «fantasma de Pepper»; mismo montaje con texto = teleprónter.

## Luz natural

- Oficio: exterior no se ilumina, se corrige; fuente dominante = sol/cielo, no controlables; problema = que la luz cambia en la jornada; temperatura = la del sol, variable; herramienta clave = rebotador, difusión grande, HMI de relleno.
- Oficio: sol detrás/lado como contraluz + rebotador en rostro; sombra abierta + rebalance si no se mueve al sujeto; con mucha luz, ND de cámara (tema 1), no cerrar más el diafragma.
- Cálculo: longitud de sombra = altura del objeto / tan(altura del sol). Amanecer/atardecer, sol a ~10°, sombra ~5,7h, luz rasante y cálida; media mañana/tarde, ~30-45°, sombra 1,7h a h, lateral alta; mediodía, ≥60°, sombra ≤0,6h, cenital dura.
- Sony PXW-Z100: preajuste exterior «Outdoor (5.600K)» para amanecer/atardecer, sin compensar el cálido.
- Blackmagic, URSA Broadcast G2: con cielo variable, bajar el umbral de cebra por debajo de 100.
- Oficio: balance se rehace cuando cambia la luz, no en automático continuo si se monta (tema 1); plano/contraplano con horas de diferencia = problema de continuidad, se resuelve con orden de rodaje.
- Oficio, ventana + tungsteno: problema de color (5.600 K vs 3.200 K, corrige CTB en focos o CTO en ventana) y de intensidad (ventana da más luz, corrige ND en ventana, no subiendo focos). CTB en focos corrige color, no intensidad. Remedio completo: ND en ventana + CTO o CTB según destino. Alternativas de reportaje: LED de día, encuadrar sin ventana o de lado, silueta.

## Luz artificial

- Oficio, aparatos: Fresnel (lente escalonada, dura/controlable); foco abierto/*open face* (sin lente, más luz por vatio); recortador/elipsoidal (muy dura, borde dibujable); panel LED (suave, ajustable sin gel); tubo LED (suave, batería); *softbox* (suave por construcción); fluorescente de estudio (suave, poco calor); HMI (mucha potencia, luz de día, aparato de exterior).
- Oficio: HMI y LED nombran la fuente, no el mecanismo.
- Astera, ficha Titan Tube: «tunable whites... RGBMintAmber», batería interna, control por app y DMX con/sin cable.
- Oficio, regulador: en tungsteno, bajar regulador enrojece (filamento se enfría), efecto colateral, se evita regular mucho; en LED, en principio no mueve el color, depende del aparato; foco sin regulador: distancia, rejilla, difusión o ND.
- Sony, *PXW-Z200 Help Guide*: fluorescente/sodio/mercurio/LED «may flicker or change colors».
- Blackmagic, URSA Broadcast G2: tungsteno/fluorescente/LED «may introduce some flicker» en cadencias altas; puede no verse en visor, probar antes; obturación afecta visibilidad; red europea 50 Hz, obturación 1/50 o 1/100 suele evitarlo (oficio, tema 1); calcula obturaciones sin parpadeo, con salvedad de que fuentes concretas aún pueden parpadear.
- Sony PXW-Z200: ***Flicker Reduce***, modo Auto/On/Off, frecuencia 50Hz/60Hz, de fábrica 60Hz, en Europa pasar a 50Hz.
- UIT-R BT.2020-2: frecuencia de trama influida por frecuencia eléctrica y tipo de iluminación.
- Norma «IEC 62471:2006 and EN 62471:2008», seguridad fotobiológica de lámparas; informe de ensayo Astera Titan Tube (29-05-2026): clasificación «Exempt Group». Resto de riesgos (calor, cables, caídas), temas 11 y 14.

## Recomendaciones técnicas que el tema cita

- UIT-R BT.709-6: D65, x=0,3127, y=0,3290.
- UIT-R BT.2020-2: mismas coordenadas D65; frecuencia de trama e iluminación.
- EBU Tech 3355 (marzo 2017): TLCI, valor 50, dos lecturas por tipo de producción, salvedad de sentido de la cifra.
- IEC 62471:2006 / EN 62471:2008: seguridad fotobiológica de lámparas.

## Lo que este tema no da, y dónde está

- Equipos de iluminación propios de CSRTV: no consta documento publicado localizado.
- Espectro/K de sodio y mercurio del alumbrado público: sin fuente leída, solo preajuste Sony.
- Altura del sol en Andalucía por hora/estación: depende de fecha/latitud, no dado.
- K de vela/bombilla/amanecer/cielo cubierto/sombra abierta en cifra: tablas no coincidentes, sin norma localizada.
- Umbrales por tramos del TLCI: en figura EBU no legible como texto; solo valor 50 y 2 lecturas.
- Pérdida de luz/mired de cada gel comercial: en cartas de fabricante no leídas; solo cálculo.
- Cifras de contraste por género y ángulo 30-45° de la principal: costumbre de oficio, sin norma.
- Balance de blancos, cebra, falso color, obturación, ND de cámara: tema 1. Calidad técnica de imagen: tema 9. Prevención con focos/cables/electricidad: temas 11, 14, 17.
- Aparatos de plató (parrillas, cicloramas, mesas de iluminación) y diseño por género: fuera del enunciado, materia del iluminador.
