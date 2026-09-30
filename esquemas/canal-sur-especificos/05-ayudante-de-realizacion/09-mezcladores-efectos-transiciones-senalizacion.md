# Tema 9 del específico de Ayudante de Realización · Mezcladores de vídeo, efectos, transiciones, incrustaciones, chroma, DVE y señalización técnica

**Siglas**: RD; RA; CE; UC, RP, CR, MF; M/E; DVE; DSK, USK; PinP; FAM, NAM; GPI; PVW, PGM; SDI; FTB; fr; AFV; VANC; UMD; UDP; HDR; LE.

Esqueleto para repasar, no resumen: el tema entero es la fuente; aquí sólo el orden y los datos.

<!-- indice -->
- 1. Mezcladores de vídeo
- 2. Efectos
- 3. Transiciones
- 4. Incrustaciones
- 5. Chroma
- 6. DVE
- 7. Señalización técnica
<!-- /indice -->

## 1. Mezcladores de vídeo

- Sin norma; fuente de fabricante: manual ATEM (dic. 2024). Mezclador de Canal Sur: no consta.
- Oficio: conmutar, mezclar, combinar (incrustar); DVE = componer; macro = automatizar.
- Herramienta: figura = 18 formas sin DVE; varias ventanas = varios DVE o SuperSource; generadores de color (tono, saturación, luminancia).
- RD 1680/2011, 0905 RA 5: mezcla fuentes, transiciones, incrustaciones, efectos; crit. e) ajustado y prefijado (transiciones, cortinillas, efectos digitales, incrustaciones croma, luminancia o DSK); crit. c) entradas a los buses. RA 1 f): grabar master, señal sin incrustaciones, cámaras masterizadas (oficio: rehacer rótulos, remontar).
- 0910 RA 4 b) evaluar mezcladores (selección, sincronización, buses primarios/auxiliares, transiciones, incrustaciones, DSK, efectos digitales); g) escenografía virtual y mezclador.
- MF0217_3 (p. 18) CE1.5: «que el mezclador está preparado»; CE1.6: transiciones previstas, ritmo y tiempos adecuados. Contenidos (p. 20): 5 generadores de señales; 6 mezclador de vídeo, tituladora, generadores de efectos.
- UC0217_3 (p. 7): RP1 verificar duraciones, efectos, grafismos según parte de emisión, informar al realizador; CR1.2 coleos, avisar a mezclador y sonido; CR1.3 anotar duraciones; CR2.1 anticipar minutado y escaleta técnica. El ayudante comprueba, anota, anticipa; no mezcla.
- M/E: mezclador dentro del mezclador (PGM, PVW, transición, llaves); su salida es fuente. No lo son: bus de llave, previo, DSK. ATEM: dinámica M/E, evita errores en directo.
- Fuente: nombre largo (hasta 20 caracteres) y corto (4; ej. «Cámara 1»/CAM1; el manual se contradice en otro pasaje), llave asociada (autoselect), retardo, corrección de color, grupo de piloto, botón.
- Entradas: cámaras, servidores, exteriores, titulador (relleno+llave), fuentes internas (color, barras, clip store, bancos).
- Limpia 1 = programa sin superpuestos; limpia 2 incluye DSK 1, no DSK 2. ATEM: alfa por auxiliar en algunos modelos (croma en posproducción).

## 2. Efectos

- Preparar fuera del aire, comprobar en previo, guardar en memoria.
- Snapshot = estado en un instante; macro = instrucciones con tiempos (pausa en fr; puede contener snapshot); timeline = estados sobre línea de tiempo; shotbox = disparo rápido.
- ATEM macro: se graba con ATEM Software Control, Advanced Panel o ambos; se almacena en el mezclador; 100 espacios; ejecutable en directo.
- Efecto programado no se retoca en marcha: timeline lanzado se edita parado (cancelar o esperar); DVE suelto sí. Macro y timeline: misma limitación.
- Clip store: memoria de clips cortos y fijos, cada clip una fuente; alfa se carga solo; largo = servidor; botón o macro. Ensayar macro entera con el mezclador fuera del aire.

## 3. Transiciones

- Modos: CUT; MIX (encadenado); WIPE (cortinilla, borde con forma; la mezcla no tiene borde); fundido a color (DIP; SÚPER MIX si blanco); NAM; FAM; DVE wipe/DME.
- ATEM: disolvencia = interpolar y superponer ambas fuentes; fundido = fuente intermedia (blanco, logotipo de patrocinador); cortinilla = patrón (rombo, círculo). Botones MIX, DIP, WIPE, DVE, STING; según modelo.
- Cortinilla: forma; fuente del borde (cualquiera); simetría; posición; invertir dirección; alternar; ancho; atenuación. Con gráficos: pancarta ≤16 % del ancho.
- NAM = la más brillante en cada punto; FAM = suma luminancias, 100 % en el punto medio (destello). Ninguna es encadenado ni fundido a color.
- Ejecución PGM→PVW: CUT inmediata, sea cual sea el tipo; AUTO según duración; palanca (T-bar) manual. Duración en fr, por transición, guardada.
- BKGD, KEY 1 a 4 eligen elementos de la próxima transición (posible sólo superpuestos); mirar el previo. PREV TRANS ensaya con la palanca.
- FTB: última etapa, todas las capas; al inicio, final y antes de publicidad; no se ve por anticipado; audio con AFV.
- Animada (stinger): secuencia del reproductor de medios; a pantalla completa corta o disuelve el fondo; ATEM 1 M/E y 2 M/E; típica en repeticiones deportivas.
- Adobe (07-01-2026): unir clips = corte. Resolve 21 cap. 55 p. 1194: cambio de tiempo o lugar.
- Mateu Torres 3.2 (pp. 37-38): fundido acentúa elipsis, fade out/fade in; encadenado sobreimpresiona, carácter elíptico; «el fundido separa las secuencias, mientras que el encadenado y el corte las conectan» (Katz).
- Significado (oficio): corte = continuidad; encadenado = tiempo/lugar; FTB = fin de unidad; cortinilla = apartado, casi nunca en noticia; animada = firma; gafa = simultaneidad. Ayudante: transición anotada con duración; coleos bastantes; animadas y fundidos en minutado; anticipar con la orden (tema 6).

## 4. Incrustaciones

- Tres señales: fondo, relleno (fill), llave (key, alpha, grises). Siempre tres, aunque vengan por uno o dos cables.
- Fórmula: salida = relleno × llave + fondo × (1 − llave); 1 = relleno, 0 = fondo.
- Lineal: la fórmula anterior. Aditiva: salida = relleno + fondo × (1 − llave); el relleno se ve haya o no llave.
- Negro levantado 7 %: lineal no cambia; aditiva levanta el fondo. Llave que no cubre: lineal anula.
- Clip (nivel): gris opaco/transparente. Ganancia: pendiente = dureza del borde. Bordes = filete o sombra; saturación = color. ATEM: Nivel sube si el fondo se ve negro.
- Máscara rectangular (Superior, Inferior, Izquierda, Derecha) en lineal y luminancia; croma: tapa focos y bordes.
- Premultiplicada = relleno × llave ya hecho; declararla («composición precompuesta» ATEM) o bordes oscuros; si no, Recorte y Ganancia. No es recuadrar.
- Tipos: luminancia (brillo del relleno; ATEM: misma señal para alfa y primer plano); lineal (llave separada, mayor calidad); crominancia; figura; DVE key. Aditiva = modo, no máscara. Coring = reducción de ruido, no llave.
- Self key = relleno como llave (= luminancia); claro sobre negro; no con medios tonos. Show key = ver la llave en bruto (≠ previsualizar ajustes).
- ATEM: M/E 4 botones de llave (lineal, precompuesta, geométrica, croma, luminancia, DVE); módulo DSK 2 botones (lineal o luminancia).
- USK: dentro de cada M/E, sale en la limpia. DSK: tras el programa, no sale en la limpia; mosca, rótulos, créditos. Cadena: M/E → programa → DSK 1 y 2 → FTB.
- DSK: TIE vincula a la transición siguiente; ON AIR inmediato; AUTO propio sólo capas posteriores; TIE no cambia la limpia.
- Grafismo: titulador (lineal, DSK), clip store, plató virtual o RA. Primera prueba: premultiplicada o no. 0905 RA 6 d) señal del titulador incrustada bien; e) rótulos y claquetas, salida al mezclador.

## 5. Chroma

- Croma = llave por color del relleno. ATEM: meteorólogo ante fondo azul o verde; también inserción cromática, superposición por separación de colores.
- Cualquier color sirve (referencia y tolerancia). Verde/azul por costumbre: piel, canal verde con más resolución (doble de fotositos), azul si el vestuario lleva verde.
- ATEM sin croma avanzado: Matiz, Ganancia, límite de luminancia, espectro limitado; barras de fondo y vectorscopio.
- ATEM croma avanzado: muestra del fondo con mayor rango de luminancia. Primer plano (rellena transparencias); Fondo (artefactos menores); Borde (cabello); Rebase (tinte en contorno); Reflejo (tono general); Ajustes cromáticos.
- Rebase o reflejo cromático = contorno y matiz por la luz que rebota en el verde. ATEM: ventana del multipantalla para la máscara.
- Plató (oficio): fondo uniforme; sin ropa del fondo; submuestreo fuerte peor que 4:2:2 o 4:4:4 (tema 14).
- LE 8.6.1 (p. 122): p. 4 colores fuertes «impregnan de ‘croma’ el cuello y el mentón»; p. 9 Estilismo y Realización «deberán» tener en cuenta cromas, transparencias, decorado virtual.
- Directo: mezclador o sistema de plató virtual en tiempo real; el motor de render devuelve señal montada y el mezclador la conmuta. Mezclador sin croma puede usar decorado virtual; la sincronía hace falta siempre. Croma es una llave: «no se hace por key» es falso. Tema 12.

## 6. DVE

- Transforma antes de componer; trabaja como llave y como transición. ATEM: ventana con bordes 3D y sombras.
- Parámetros: traslación X, Y, Z; tamaño X, Y, Z; rotación X, Y, Z; aspecto (deforma); recorte; perspectiva; bordes; esquinas (corner pinning).
- Corner pinning: cuatro esquinas a las de la pantalla no frontal. Ampliar sin deformar: eje Z; tamaño sólo con X e Y iguales; rotación gira.
- PinP = una o varias ventanas con DVE; no es mosaico (pixela) ni multi-imagen (partes iguales).
- Gafa: vocabulario de plató; 50/50; 20/60/20. Tantos DVE como ventanas o SuperSource (ATEM, más de un M/E; una entrada; posición, tamaño, recorte); sale al aire, no es el multipantalla. Uso: dos personas en sitios distintos.

## 7. Señalización técnica

- Sin definición en norma. ATEM «Sistemas de señalización»: luz roja en cámara o monitor; SmartView Duo/HD, bordes de color para aire y anticipos.
- Piloto (tally) rojo = aire; verde = previo. Tres sitios: cámara (delante presentador, detrás/visor operador), multipantalla, plató.
- Compuesto: piloto en todas las cámaras que lo forman (marca lo que contribuye, no el bus PGM).
- Panel ATEM: botón rojo = aire (se emite inmediatamente); bancos A/B: rojo PGM, verde anticipos; software: barra «Al aire». PVW = verde en cámaras Blackmagic; CUT o AUTO = rojo.
- Tres vías: contacto (relé); datos en la señal; red (TSL UMD sobre UDP; NMOS IS-07 «Event & Tally»). Vía en Canal Sur: no consta.
- GPI and Tally Interface: 8 relés mecánicos, por Ethernet del mezclador, misma red; hasta 8 unidades (1 basta en 1 M/E); 2 M/E o 4 M/E: pilotos 1-8, 9-16, 17-24 por ATEM Setup. Entradas: interruptores ópticos a tierra, máx. 5 V a 14 mA; salidas: relés a tierra, máx. 30 V a 1 A.
- Datos: ATEM controla URSA Mini y Studio Camera por SDI de retorno. Blackmagic Embedded Tally Control Protocol v1.0 (30-04-2014): paquete SMPTE 291M, DID/SDID x51/x52, línea 15 VANC; 4 bits por estado, bit 0 programa, bit 1 previo. Protocolo de fabricante; SMPTE fija el paquete. El manual no dice expresamente que sus cámaras lo usen.
- CALL: mantener pulsado, parpadea el piloto de las cámaras, por SDI de retorno; refuerza el intercom (tema 4), no lo sustituye.
- 0905 RA 6 b) monitorizado multipantalla. ATEM: 8 ventanas pequeñas; Constellation 8K 4, 7, 10, 13 o 16; borde rojo = principal, verde = anticipo, blanco = ninguno; zonas seguras 16:9 o 9:16; vúmetros; cualquier señal interna. Orden: fuente pedida en verde antes, en rojo después.
- TSL UMD (19-09-2009; vigente: no consta): libre, sin cargo; no norma. V3.1: RS 422/RS 485, 38k4 baud, dirección 0-126 + 80 hex, 4 bits de piloto y 2 de brillo, 16 caracteres ASCII (todos), un solo sentido. V4.0: colores 0 OFF, 1 RED, 2 GREEN, 3 AMBER; V3.1 y V4.0 también sobre UDP/IP. V5.0: Ethernet, UDP máx. 2048 bytes, TCP/IP opcional, 65.535 direcciones por pantalla, ASCII o Unicode. Nombre de etiqueta = escaleta = el cantado.
- Sincronía: black burst (vídeo negro con sincronismos y salva de color; convencional, sirve en HD); tri-level (tres niveles; HD y UHD); genlock = engancharse. Sincronizador de cuadro retrasa uno o varios cuadros; tema 4 y tema 11.
- Generadores (MF0217_3 p. 20): sincronismos; logotipo; señales test; cartas de ajuste (sin fuente). Barras ATEM: comprobar señales; barras de cámara con tono.
- UIT-R BT.2111-3 (05/2025): barras HDR (BT.2100); HLG gama reducida, PQ gama reducida, PQ gama completa; 10 y 12 bits; 100 % y 75 %; controlar crominancia y luminancia, ajustar monitores, prueba general, circuito activo con audio; no para nivel de negro (PLUGE); fabricantes indican edición. No es la de HD sin HDR; BT.471 no leída.
- Comprobación (ATEM: tras el intercom; sin luz, número de cámara = entrada): cada cámara a PVW y PGM; compuestos; nombres iguales; bordes; llamada; barras. Fallo: al realizador y al técnico (tema 6).
- Incidencias: sin piloto = avisar, comprobar número y entrada; nombre distinto = corregir y avisar; bordes verdes = borde/rebase, plano sin croma; rótulo con borde oscuro = premultiplicada sin declarar; coleo corto = avisar a mezclador y sonido.
- Norma: RD 1680/2011 (BOE núm. 302, 16-XII-2011), texto de 2011; RD 500/2024 no toca los módulos citados.
- No consta: equipos de Canal Sur; identidad gráfica; otros fabricantes (DME, SÚPER MIX: oficio); NMOS IS-07 (título y objeto); LE 6.5 (Realizador/a).
