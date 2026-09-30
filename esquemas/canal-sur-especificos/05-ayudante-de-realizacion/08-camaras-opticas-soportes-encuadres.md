# Tema 8 del específico de Ayudante de Realizacion · Cámaras, ópticas, soportes, encuadres, profundidad de campo, filtros, estabilización y criterios visuales

**Siglas**: RTVA · CSRTV · RD · EBU · UIT-R · ENG · EFP · CCU · RCP · CCD · CMOS · OLPF · ND · PTZ · POV · ATW · TLCI · RA · Conv. (X Convenio RTVA) · LE (*Libro de Estilo de Canal Sur*, RTVA 2004)

Esqueleto para repasar, no resumen: la fuente delante de cada línea; el detalle, en el tema.

<!-- indice -->

## Índice

- [Cámaras](#cámaras)
- [Ópticas](#ópticas)
- [Soportes](#soportes)
- [Encuadres](#encuadres)
- [Profundidad de campo](#profundidad-de-campo)
- [Filtros](#filtros)
- [Estabilización](#estabilización)
- [Criterios visuales](#criterios-visuales)

<!-- /indice -->

## Cámaras

- Sin norma sobre la cámara. RD 1680/2011: enseñanza; LE 2004: recomendaciones; fabricantes: ejemplos.
- Conv. anexo III: 5351000 Realizador (p. 196) puesta en escena, guion técnico, atmósfera; 5341310 Cámara (p. 116) tomas en coordinación con realizador. LE 3.17.1.5 (p. 61): entrevista, una cámara, plano que fija el realizador. LE 5.1 (p. 79): sin realizador, criterio del cámara.
- RD 1680/2011: 0903 RA 1.b (emplazamiento, altura, movimiento); 0904 RA 4.c (planificación de cámaras); 0910 RA 2, 2.c (formato, aspecto, definición, exploración, imágenes/s), 2.d (sensibilidad, ganancia, temperaturas de color, obturación, negros, matriz, visor).
- Oficio: ENG autónoma, hombro; EFP/estudio en cadena (triax o fibra), control en CCU; cine digital autónoma. Operador: encuadre, foco, movimiento. Control de imagen: nivel, color, sombras, altas luces, detalle. Cabeza + CCU + RCP (diafragma, color, obturación, negro, ganancia); manos: zoom y foco.
- EBU R 118 v2: *Tiering* (Tech 3335); supone SDR; HDR (BT.2100) se consulta a la emisora. HD § 1.2: Tier 1 hombro/mano 1 o 3 sensores; 2L long-form; 2J journalism; 3 semiprofesional pequeña; 4 consumo (aprobación); SP especial (aprobación).
- UHD1 T1 3840x2160, T2 ≥2715x1527; UHD2 T1 7680x4320, T2 ≥5430x3054. 2J relaja por velocidad; Tier 3 ≈33 % HD; el códec puede rebajar la cámara. Criterios: ruido, sensibilidad, rango de exposición, resolución espacial, aliasing (+ códec, salvo cámaras de sistema).
- Tabla 2 (un sensor / tres): UHD1 T1 1x1" / 3x2/3"; HD T1 1x2/3" / 3x1/2"; 2L 1x1/2" / 3x1/3"; 2J 1x1/3" / 3x1/4". T1 10 bit 4:2:2; 2L y 2J 8 bit (10 preferido).
- R 118 § 2.6 Tier SP: alta cadencia, minicámaras, macro; uso limitado; no suele contar en el % de menor resolución. Minicámara: POV.
- Cámara lenta: más cadencia de sensor (Blackmagic URSA G2): 25→100: 1/4. FS5 (50i): 100/200/400/800 fps, sin sonido (Sony). Doblar cadencia: mitad de luz (25→100: 2 pasos; 25→200: 3). LE 8.4.1 (p. 120): repeticiones y ralentizaciones dan ecuanimidad; LE 8.4 (p. 119): manda la imagen.
- CCD: global, *smear* vertical, consumo mayor, estudios antiguos. CMOS: barrido, *rolling shutter*, consumo menor (Z200 1.0" stacked; XF605 1.0"). Tech 3335 § 2.9: verticales inclinadas, bordes distorsionados, imagen gelatinosa.
- Color: prisma con tres sensores, o máscara de Bayer (mitad verdes, 1/4 rojos, 1/4 azules; *demosaicing*; menos sensibilidad). OLPF evita muaré. *Blooming*: halo en todas direcciones; *smear*: raya vertical; muaré: trama fina.
- Mandos: diafragma (profundidad); obturación (movimiento, parpadeo); ND (nada más); ganancia (ruido). Falta luz: diafragma, obturación, luz, ganancia. Sobra: ND antes de cerrar hasta difracción. Z200 AUTO: ND, iris, ganancia, obturador, ATW; iris automático momentáneo vuelve al soltar; el permanente «respira».
- Obturación: 360°: cuadro, 180°: mitad. Tech 3335 § 2.9: nominal 1/50 (50 Hz), 1/60 (59,94), 180°. Tiempo: ángulo/360 x cuadro: 25 fps 180°: 1/50; 50 fps 180°: 1/100, 360°: 1/50. Blackmagic: 25→50 fps: mitad de luz; +1 paso, 180°→360° o luz.
- Parpadeo (Z200): fluorescentes, sodio, mercurio, LED; puede no verse en visor (Blackmagic: prueba); [Auto]/[On]/[Off], [50Hz]/[60Hz]. Europa: 1/50 o 1/100.
- Ganancia: +3 dB: 1/2 paso; +6: 1; +12: 2; +18: 3. Último recurso.
- Balance de blancos: ajusta la cámara a la luz; iguala R y B. Tungsteno ≈3.200 K, día ≈5.600 K (XF605). ATW (Z200) falla con color dominante (cielo, mar, suelo, flores) o luz extrema; *ATW Hold*.
- Balance sobre color: empuja al complementario. Blanco/gris neutra; azul cálida; naranja/ámbar fría; verde magenta.

## Ópticas

- RD 0910 RA 2.a: parámetros del objetivo y elementos morfológicos del encuadre.
- Focal: centro óptico→plano de imagen, al infinito. Más focal, menos ángulo. Z200 f: 7.71-154.21 mm: 24-480 mm (35 mm); XF605 f: 8.3-124.5 mm, F/2.8-4.5, 15x, 9 láminas.
- Ángulo (convención): gran angular >60º; normal 60º-25º; tele 25º-10º; supertele <10º. Normal ≈ diagonal del sensor: 2/3" ≈12 mm; 35 mm ≈50 mm.
- «22x4.8»: relación x focal mínima (mm); máxima: producto. Fujinon UA22x4.8BERD (2/3"): 4.8-106 mm (105,6). Más tele: multiplicar.
- Número f: focal/pupila; menor: más abierto. 1,4; 2; 2,8; 4; 5,6; 8; 11; 16; 22 (cada paso x2 luz); f/1,4→f/22: 8 pasos: 256 veces. Velocidad: menor f. Z200 F2.8-4.5, mínima F11; mayor cifra en tele.
- Número T: luz real transmitida; T > f (f/2 ≈ T2,2); cine.
- Extensor UA22x4.8BERD 2x: [1x] 4.8-106, [2x] 9.6-212 mm; 5.2°x2.9°→2.6°x1.5°; pierde 2 pasos (FUJINON); abre 1:1.8 (4.8-61 mm), 1:3.15 (106 mm). X400 indicador «EX».
- Difracción (Z200): cerrar demasiado desenfoca; remedio ND. Punto dulce (oficio): 2-3 pasos bajo la máxima (f/2→f/5,6; f/2,8→f/8); máxima: aberraciones; mínima (f/16, f/22): difracción.
- Seidel: esférica, coma, astigmatismo, curvatura de campo, distorsión (barril, corsé); cromática aparte.
- Foco manual (Z200): gotas en ventana, bajo contraste, sujetos lejanos, cambio de temperatura.
- Tiraje (Z200, «Flange Focal Distance»): montura-sensor; foco no se mantiene entre tele y angular. Al cambiar objetivo o cuerpo, golpe, temperatura. Tele enfocar→angular sin tocar foco→anillo de tiraje→repetir; diafragma abierto. «Cerrar» zoom: tele; «abrir»: angular.
- Φ: plano focal; medir el foco desde ahí.

## Soportes

- RD 0910 RA 2.h (soportes y fundamentos narrativos); contenidos: steadycam, bodycam; travelling, dollies, plumas, grúas, cabezas calientes; cámaras robotizadas. 0903: movimientos de maquinaria y soportes.
- Cadena: soporte + cabeza/rótula/cabezal (panorámica y cabeceo) + anclaje (placa, cuña, cola de milano). Se monta de abajo arriba; se desmonta al revés.
- Mano; hombro; trípode; pedestal; dolly y raíles; grúa y pluma; cabeza caliente; robotizada. Hasta el pedestal, operador detrás. Cable aéreo: deportes. Gimbal: 3 ejes.
- Cabezas: fricción; fluido (estándar TV); engranaje (cine); contrapeso (estudio grande); remota; caliente.
- LE 5.2 (p. 80): trípode «en circunstancias normales»; hombro para recursos (rueda de prensa, entrevista); eludir encuadres, composiciones y perspectivas extravagantes; óptica a la altura de la teórica mirada del espectador. LE 3.17.1 (p. 59): luz suficiente preferiblemente natural, trípode, micrófono de corbata; llevar auriculares, antorcha, iluminación básica, filtros, micrófonos.
- LE 9.2.12.4 (p. 130): cámara en mano evoca ficción; «la información sólo habla de realidad». LE 2004 no nombra cardán, *slider* ni PTZ.
- Trípode: copa, *spreader*/araña, cangrejo, gancho central. Cangrejo, dos acepciones (cuestionarios RTVE): soporte antideslizante o base con ruedas (no sustituye al pedestal).
- Pedestal: columna regulable + base con ruedas; sube y baja en plano sin perder horizontal; panorámica y cabeceo, la cabeza.
- Grúa (giro 360º): *mini jib* pequeña; *jib*/pluma brazo rígido. Paralelogramo: cámara nivelada. Nivelador de cabeza: horizonte real o deseado. Fija: arco; telescópica: sin arco.
- Corporal (chaleco, brazo de muelles, poste): Steadicam: marca de Tiffen. Modos: normal/*operating*, bajo/*low mode*, *Don Juan* (retroceso caminando hacia delante), misionero, *goofy*.
- *Slider*: raíl corto; *dolly*: carro; *travelling*: movimiento; lateral ≠ panorámica; circular: 360º alrededor del sujeto, vía curva nivelada.
- Remotos: cabeza caliente (*hot/remote head*; nivelada, equilibrada, alimentación y control; sitios inaccesibles, menos peso, un operador varias cámaras); PTZ (joystick, mando, mezclador, programa, red IP); CCU/RCP ajustan imagen.

## Encuadres

- LE 5.3.1 (p. 80): encuadre «fundamental porque a través de él se selecciona y ordena lo que aparece». RD 0904 RA 4.c; 0905 RA 3.c y 3.d.
- Tamaño de plano: distancia + focal. Zoom: tamaños consecutivos; más abierto, retroceder; más cerrado, acercar o extensor.
- Retransmisión (oficio): 4,5x angular fijo (portería, raíl); 23x portátil (máster, seguimiento); 72x caja (cerradas); 100x caja de gran alcance. Máster: elevada, centro del campo, extremo angular: portátil UA22x4.8 (4.8-106 mm), no caja UA94x8.7 (8.7-818 mm). Gama: UA70x8.7 compactos, UA94x8.7 medio, UA107x8.4 más alcance.
- Planta: vértice estrecho: tele; abierto: angular. Más lejos, más focal (fondo: tele; primera fila: angular). General abierta y cerca del eje; recurso y detalle lejos y cerradas.
- UIT-R BT.709-6 apdo. 2: 16:9, 1920 muestras, 1080 líneas activas, píxel 1:1.
- EBU R 95 v1.1 (jun. 2017): acción esencial en Action Safe Area; grafismos en Graphics Safe Area; centro sin desplazar. Acción 3,5 %; grafismo 5 % por borde (nota 5): central 93 % y 90 % (resta). Valores en líneas y píxeles: 576i, 720p, 1080i/psf, 1080p, 2160p, 4320p (figuras 1 a 6).
- LE 5.3.2 (p. 81): íntimo, planos cortos; coral, abiertos; alternancia da ritmo; plano con calidad, profundidad y capacidad de mostrar la realidad. LE 3.17.1.1 (p. 59): entrevistado, plano medio o primer plano en interior, americano en exterior si el fondo informa; prever rótulos.

## Profundidad de campo

- Más con: diafragma cerrado, focal corta, más distancia de enfoque. Círculo de confusión: criterio de nitidez.
- Hiperfocal: nítido desde la mitad hasta el infinito; factores: focal, diafragma, círculo de confusión; no la obturación.
- Sensor grande: menos profundidad a igual encuadre, por la focal más larga. Diagonales (aprox.): 2/3" 11 mm; Súper 16 14,5 mm; Súper 35 28 mm; Full Frame 43 mm.
- Reducida (aísla): diafragma abierto (ND), focal larga, sujeto cerca, fondo lejos. Amplia (contexto): cerrado, angular, más distancia.
- LE 3.17.1.2 (p. 59): fondo superfluo, neutro y, si hace falta, fuera de foco. Cambio de foco («doble foco»): poca profundidad y marcas; LE 5.2 (p. 80): «intención previa».
- Muaré en pared LED (oficio): desenfocar la pantalla: menos profundidad, tele + ND con diafragma abierto, presentador lejos de ella. No enfocarla, no acercar al presentador, no hiperfocal.

## Filtros

- ND quita luz sin color: 1/4: 2 pasos; 1/16: 4; 1/64: 6; 1/128: 7. «Clear» no es filtro.
- Z200: 1/4, 1/16, 1/64 (menú 1/4-1/128); variable 1/4-1/128; [Auto ND Filter]. FS5: 1/4, 1/16, 1/64; variable 1/4-1/128. XF605: Off, 1/4, 1/16, 1/64, motorizado. Cambiar ND grabando distorsiona imagen o sonido (FS5; Z200 a «clear»).
- ND no cambia la profundidad: permite abrir el diafragma; evita difracción; más denso: más abierto.
- Delanteros (Z200: 72 mm): polarizador (cielos, reflejos; máximo a 90º del sol, nulo hacia el sol; ND y degradado no separan nubes); degradado; difusor; UV/protección. Bandera francesa: se ajusta con zoom en angular.

## Estabilización

- Cinco familias (oficio): pasiva (masas, muelles, contrapesos: corporal, hombro); activa (sensores y motores: cardán); híbrida; óptica (grupo de lentes móvil); digital (recorta).
- Activa: mantiene orientación, no posición; en el soporte, no en la óptica. Corporal clásico: pasivo; equilibrio estático (quieto y a nivel) y dinámico (giro estable).
- Z200: en trípode, [Off] (panorámicas lentas distorsionan con [Standard]/[Active]); [Active] desplaza el encuadre hacia tele. XF605: óptico de desplazamiento + digital (Standard, Dynamic, Powered IS); lo digital recorta.
- LE 5.3.2 (p. 81): «paneo», «travelling», «zoom» con prudencia y moderación; vale para cardán y corporal.

## Criterios visuales

- Conv. 5351000 (p. 196): coordinar elementos técnico-artísticos y controlar calidad y duración. Sin realizador, el cámara (LE 5.1).
- LE 5.2 (p. 80): sin «estética de ficción»; innovaciones (barridos, doble foco, zoom rápido) con «intención previa», sólo en determinados formatos. LE 5.3.2 (p. 81): zoom sólo en circunstancias excepcionales; «muy poco natural».
- LE 6.4 (p. 92): *raccord*: continuidad y uniformidad visual; técnico: sin diferencias de color, brillo, contraste, tono, luz, altura de planos, calidad. LE 6.3.4 (p. 91): imágenes y sonidos homogéneos.
- Una cámara: balance fijo, diafragma manual, misma ganancia, archivo de escena.
- Entre cámaras: control de imagen en CCU (tema 4); RD 0905 RA 5.b: monitor, forma de onda, vectorscopio, rasterizador. Reportaje: mismos ajustes (Z200 [Save to Media(B)]/[Load from Media(B)]; no reproduce del todo), misma carta, luz, cadencia y obturación; nivel parecido.
- EBU Tech 3355: escala TLCI para multicámara en directo («credible»); «do not form hard definitions».
- LE 3.17.1.5 (p. 61): dos o más cámaras ENG: planos técnicamente compatibles y uniformes; código de tiempo idéntico. Igualar: código de tiempo, *genlock*, ajustes.
- RD 0905 RA 3.c (cámaras y elementos impropios) y 3.d (escenografía, iluminación, vestuario, peluquería, maquillaje). LE 8.6 y 8.6.1 (pp. 121-122): blusas y camisas blancas saturan; telas brillantes, satenes y sedas reflejan color; rayas finas: muaré.
