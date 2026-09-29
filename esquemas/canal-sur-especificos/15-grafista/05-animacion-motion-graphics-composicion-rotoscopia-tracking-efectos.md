# Tema 5 del específico de Grafista · Animación 2D/3D, motion graphics, composición, rotoscopia, tracking y efectos visuales

**Siglas**: RTVA; LE (Libro de estilo, 2004); RD; RA; FK/IK; UV; RGBA; VFX; CGI; IA; W3C; PNG, TGA, TIF, JPG, EXR, MOV.

Esqueleto para repasar, no resumen: ante la duda, vuelve al tema.

<!-- indice -->
<!-- /indice -->

## 1. Animación 2D y 3D

- Ninguna norma regula animar; RD 1583/2011 y RD 1680/2011 = enseñanza, no obligan a la RTVA; manuales = definición técnica; no consta programa de Canal Sur.
- Blender: animar = mover o cambiar de forma un objeto en el tiempo (entero, deformarlo, heredada); lo corriente: fotogramas clave.
- RD 1583/2011 mód. 1087: «La persistencia retiniana»; «Temporalización (timing) y fragmentación del movimiento». TV europea 25 imágenes/s (oficio).
- Técnicas (oficio): stop motion (objeto real fotografiado y movido); pixilación (igual con PERSONAS); rotoscopia (dibujar sobre imagen real); animatrónica (muñecos con mecanismos, no fotograma a fotograma). Mód. 1087 RA 1: stop motion o pixilación.
- Fotograma clave = valor en un instante; interpolación = el programa calcula lo intermedio. Claves = qué y dónde; curva de velocidad = cómo.
- Blender: F-Curves; X = tiempo, Y = valor; pendiente = velocidad. Constante: escalón hasta la siguiente clave (*blocking*); Lineal: recta, sin saltos de valor pero sí de velocidad; Bézier: por defecto, suave en ambos.
- Easing (Blender): Ease In = arranca despacio y acelera; Ease Out = sale deprisa y frena; Ease In Out = despacio, acelera, frena. Bounce = rebote con decaimiento exponencial. Entrada: frena al final; salida: arranca despacio (oficio).
- 2D, RD 1583/2011 art. 5.c: animática (storyboard con tiempos y sonido), layout (encuadre, fondos), animación clave (poses), intercalación (intermedios), pintura, composición (reunión de capas).
- Mód. 1087 RA 3: carta de animación = tabla de tiempos por plano, personaje y/o decorado (3.a); claves por capas (3.b); intercalaciones según la carta (3.c). Hoy intercalación = interpolación; rótulos, cortinillas, cabeceras: 2D por claves (oficio).
- 3D, art. 5.d: diseño y modelado, setup, texturización, iluminación, animación, renderizado. Malla = vértices, aristas y caras. UV = relación superficie de malla–textura 2D.
- Mód. 1088: mapas UV (1.b planos, cilíndricos, esféricos, automáticos o basados en cámara); 2.c «especularidad, refracción y reflexión»; RA 3 «texturas procedurales 2D y 3D».
- Mód. 1086 RA 5: 5.c método «(nurbs, polígonos, subdivision surfaces)»; 5.a fijar antes tamaños, métodos, escala y movimiento. NURBS (*non-uniform rational basis spline*) = curvas y superficies matemáticas; subdivisión = malla de pocos polígonos a superficie suave.
- Rig (Blender): controles a objetos. Mód. 1087 RA 2: esqueleto por jerarquía de *joints* (2.b); FK e IK (2.c); *bind skin* (2.d); pesos (2.e).
- FK: padre → hijo (mueves hombro, la mano va detrás). IK: hijo → padre (colocas la mano, el brazo se acomoda). Mano en mesa = IK (oficio).
- Render = imagen 2D calculada desde geometría 3D. Trazado de rayos: reflexión, refracción o absorción al tocar objeto; más exacto y mucho más lento que *Scanline*.
- Mód. 1085: RA 4 «render final por capas»; 4.a granja de render (ordenadores en paralelo); 4.c integridad del fotograma, *flicker*. Cámara virtual, mód. 1087 RA 6.d: arranques y frenadas por claves.

## 2. Motion graphics

- Motion graphics: sin definición en norma ni manual; oficio = grafismo animado sin personajes (cabeceras, cortinillas, rótulos; temas 3 y 4); propiedades por capa animables por separado; plantillas Fusion (tema 9).
- Sonido (oficio): sincronía con el golpe visual; nivel de la emisión; silencio = pista muda.
- Entrega con transparencia: fichero con alfa, o relleno y recorte (*fill*, *key*). Apple: sólo ProRes 4444 y 4444 XQ admiten alfa (4444: sin pérdidas, hasta 16 bits); ningún ProRes 422. Emisión, zonas seguras = tema 8.

## 3. Composición

- Componer = reunir en una imagen elementos superpuestos. Mód. 0907 (común a ambos RD): «composición multicapa: … Gestión de capas. Creación de máscaras. Animación. Interpolación. Trayectorias»; «Efectos de key. Superposición e incrustación».
- 0907 RA 3.b: color, variación de velocidad, ocultación/difuminado de rostros, keys, seguimiento y estabilización. RA 3.c: keys «luminancia, crominancia, matte y por diferencia».
- Capa: subdivisión del diseño de un grafismo; orden decide qué tapa; propiedades animables por separado; no es el fotograma (*frame*). Precomposición: capas seleccionadas en composición nueva que actúa como una capa; efecto al conjunto; editable por dentro.
- Incrustar = sustituir parte de una imagen por otra. Familias (oficio): *chroma key* (color verde o azul); *luma key* (brillo); canal alfa; máscara o *roto* (forma dibujada).
- Verde/azul: los más alejados del tono de piel; verde por doble de fotositos verdes. Croma: fondo uniforme; submuestreo fuerte (tema 8) peor que 4:2:2 o 4:4:4.
- Color: un color y vecinos; plató; lo estropea ropa de ese color. Luminancia: lo más claro/oscuro de un umbral; rótulos blancos sobre negro, humo, fuego; lo estropea sujeto con brillo del fondo. Intruso: *time remapping* no es transparencia.
- Tres señales: fondo (*background*, debajo), relleno (*fill*, encima), recorte (*key*, forma del agujero; entrada propia en el mezclador). Alfa NO es cuarta señal: recorte pegado al relleno; con alfa hay tres igual.
- Alfa = cuarto canal (RGB + A): 0 transparente; intermedios semitransparente; máximo opaco. Intermedios = bordes sin escalones. 4:4:4:4 (tema 8): cuarta cifra = alfa.
- Ficheros: JPG nunca alfa; PNG sí, 32 bits (8 por canal); TIF sí, 32 o más; TGA sí, 32 (8+8+8+8; 24 sin alfa). Sin alfa = fondo negro en control.
- W3C PNG 3.ª ed. (24-VI-2025), 11.2.1 IHDR, tabla 12: profundidad por muestra, no por píxel; tipo 6 (*truecolor with alpha*): 8 o 16; PNG con alfa = 32 bits/píxel a 8, 16 × 4 = 64 a 16. Vídeo con alfa: ProRes 4444/XQ, normalmente MOV.
- Directo/premultiplicado (Blackmagic cap. 77 pp. 1726-1728). Directo (*straight*): RGB no afectado por el alfa (Blender: Photoshop, Gimp, PNG, BMP, TARGA). Premultiplicado: RGB multiplicado por el alfa, el alfa no (Blender: motores de render, OpenEXR; «Most computer-generated images are premultiplied», p. 1727).
  - Reglas (p. 1728): Merge siempre con premultiplicadas; color sólo en no premultiplicadas; filtrar y transformar premultiplicadas; nunca premultiplicar dos veces.
  - Fallo: no premultiplicada tratada como premultiplicada = «bright fringe» (halo claro); inverso oscurece bordes (oficio). Declarar el tipo al exportar e importar.
- Máscara: oculta o muestra partes de una capa sin eliminar contenido; grises (blanco se ve, negro no) = alfa dibujado a mano; mate = máscara. Borrar píxeles = no corregible.
- Modos de fusión (Fusion *Apply Mode*; Resolve cap. 94 pp. 2266-2267; castellano de Adobe, Photoshop, 2-XII-2025): Normal (alfa del primer plano decide qué tapa); Multiplicar (oscurece; blanco no cambia); Trama (siempre más claro; negro no cambia, blanco da blanco); Sobreexposición lineal/añadir (más que trama); Superponer (multiplica o trama según el fondo); Diferencia (blanco invierte; negro no cambia); Oscurecer/Aclarar (canal a canal). Oficio: multiplicar = sombras; trama y sobreexposición = brillos, fuego sobre negro.

## 4. Rotoscopia

- (1) Técnica de animación: mód. 1087 RA 7 «Realiza la captura de movimiento y rotoscopia en 2D y 3D»; 7.i dibujar «física o virtualmente» sobre imágenes de referencia respetando las hojas de modelo.
- (2) Composición (la del grafista): recortar a mano un objeto o persona con máscara ajustada fotograma a fotograma, sin croma (Blender: «manual rotoscoping»). Principio común: la imagen real manda.
- Herramienta: máscara vectorial Bézier con claves. Blackmagic: «Polygon masks… the basic workhorse of rotoscoping». Seguir al objeto: a mano o enlazada al seguimiento; el tracking mueve la máscara en bloque, el rotoscopista corrige la forma.
- IA: Resolve Magic Mask. Asistida no es revisada: comprobar fotograma a fotograma (pelo, manos, bordes). Garantías IA = tema 15.
- Oficio: varias máscaras sencillas; claves donde cambia el movimiento; borde difuminado.
- Captura de movimiento (pariente 3D): sensores en el actor, traslado al esqueleto. Mód. 1087 RA 7: 7.c ubicación de sensores, con ensayos; 7.d trasladar al setup; herramientas: software, cámaras y sensores.

## 5. Tracking

- Blackmagic: trayectoria analizando una zona del plano en el tiempo; usos: estabilizar, suavizar, casar movimiento.
- Tres tipos (Blackmagic cap. 81):
  - Punto (*Tracker*): rasgo pequeño identificable, trayectoria 2D; estabilizar, casar movimiento, *corner pin* (cuatro esquinas en cuatro puntos).
  - Planar (*Planar Tracker*): superficie plana invariable, «2 ½D» con perspectiva.
  - Cámara (*Camera Tracker*): muchos puntos comparados; recrea la cámara real en 3D virtual.
- Grados (oficio): un punto = posición; dos = posición, escala, rotación; plano = deformación de superficie; cámara = movimiento en el espacio.
- Cámara: enlace 2D–3D, integra CGI en planos reales; resultado: cámara 3D animada y nube de puntos. Fases: *Tracking* (análisis) y *Solving* (escena 3D).
- Condiciones: seguir sólo lo «nailed to the set» (coches, personas estropean; máscaras); metadatos (sensor, focal); Blender: toda cámara distorsiona, hacen falta focal y distorsión exactas.
- Estabilizar: recorta y amplía (oficio). Seguimiento falla si el punto no tiene contraste, sale de cuadro o se desenfoca.
- Preparación, mód. 0907: «Planificación de la grabación para efectos de seguimiento». Oficio: marcas (se borran); sin desenfoque ni movimientos rápidos; anotar focal y cámara. Seguimiento en directo (AR, escenarios virtuales) = tema 6.

## 6. Efectos visuales

- Sin definición normativa. Especiales = físicos ante la cámara; visuales o VFX = postproducción (composición, 3D, rotoscopia, tracking) (oficio). Mód. 1087: «incrustación de efectos especiales en películas de imagen real».
- Mód. 1087 RA 4, «leyes físicas al universo virtual»: partículas (4.b; emisores y campos de fuerza: gravedad, viento, turbulencia); sólidos rígidos (4.c; *rigid bodies* activos o pasivos, colisiones, sin deformarse); cuerpos blandos (4.d; *soft bodies*, influencias pintadas y tensores); multitudes (4.e; partículas sustituidas por modelos animados).
- Integración, mód. 1085 RA 5.c y 5.d: «efectos para la integración, movimiento de multiplanos y reencuadre». Casar (oficio): perspectiva y movimiento; luz (sombras); color y contraste; enfoque y desenfoque; grano. Borde: alfa bien premultiplicado y máscara suavizada.
- Libro de estilo (1.ª ed., marzo de 2004):
  - LE 9.9.2 p. 167: imágenes duras con «planos abiertos, impersonales y neutros» u ocultación parcial con medios técnicos; ralentización e imagen congelada = «efecto reprobable» si sólo acentúan la morbosidad.
  - LE 9.9 p. 166: menores, víctimas, testigos protegidos, fuerzas de seguridad y su familia: no se emitirán si hay factor de riesgo; rostros «cubiertos o tramados». Tramado = máscara con seguimiento; revisar giros y entradas/salidas (oficio).
  - LE 3.2.2 p. 46: rótulo «reconstrucción» mientras estén las imágenes «falsas». LE 9.9.1 p. 166: archivo sobre delincuencia, malos tratos o asuntos judiciales «también serán ‘tratados’», rótulo «Archivo». LE 3.3 p. 47: no abusar de «postproducciones o alardes técnicos».
  - Infografía animada de reconstrucción = rótulo (tema 4). Sin manual de efectos de Canal Sur.

## Aplicación práctica

- Rótulo: dos claves de posición (fuera y en su sitio); *ease out*; opacidad sube; salida *ease in*. Pegar a coche: dos puntos; pantalla o cartel: planar y *corner pin*; objeto 3D: cámara. Persona sin croma: máscaras con seguimiento. Rostro de menor (LE 9.9): máscara con seguimiento; un fotograma perdido = cara visible.
- Cortinilla: ProRes 4444 (o XQ) en MOV, o PNG, TGA, TIFF; nunca JPG ni ProRes 422; declarar tipo de alfa; probar sobre negro, blanco y gris (halo claro = alfa mal interpretado).
- Cuentas (25 imágenes/s): fotogramas = segundos × 25; 2 s = 50; 0,8 s = 20. Claves en 0 y 20: 19 interpolados (1 al 19). 1920 × 1080 × 4 bytes = 8.294.400 bytes (~8,3 MB); 10 s = 250 fotogramas = 2.073.600.000 bytes (~2,07 GB).

## Fuentes y huecos

- RD 1583/2011, de 4-XI (BOE núm. 301, 15-XII-2011), vigente a 24-09-2026: art. 5.c y 5.d; mód. 1085, 1086, 1087, 1088, 0907. RD 500/2024, de 21-V; RD 1085/2020, de 9-XII; corrección BOE núm. 61, 12-III-2012. RD 1680/2011, de 18-XI: mód. 0907.
- Fabricante: Blender 5.2 LTS; Resolve 21; ProRes (abril de 2022); W3C PNG; Adobe. Leídas 29-09-2026.
- No da: definición normativa de motion graphics o VFX; doce principios; After Effects, Mocha, Cinema 4D, Maya, Houdini, Nuke; programas de Canal Sur; emisión (tema 8); AR (tema 6); IA (tema 15); derechos (tema 11).
