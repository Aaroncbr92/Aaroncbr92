# Tema 6 del específico de Grafista · Escenarios virtuales, realidad aumentada, pantallas, videowalls y grafismo en tiempo real

**Siglas**: RTVA (Agencia Pública Empresarial de la Radio y Televisión de Andalucía); CSRTV (Canal Sur Radio y Televisión, S.A.); LE (*Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*); RA/RV/RM; LED; M/E; fps; LOD; SDI; DVI; OCIO; MOS.

Esqueleto para repasar, no resumen: fuente delante de cada línea; «oficio» = sin fuente.

<!-- indice -->
<!-- /indice -->

## 1. Escenarios virtuales

- Sin norma; fabricante = definición técnica. Sistemas de CSRTV: no constan.
- Oficio, tres técnicas. Decorado virtual: real = personas y objetos que tocan; fondo sintético por croma. RA: plató real entero + objetos superpuestos con llave. Pared de LED: fondo en pantallas reales, sin incrustación.
- Oficio, 3 piezas: plató de croma + motor de render en tiempo real + seguimiento (la clave; sin él, fondo plano).
- Oficio, datos: giro, inclinación, balanceo, 3 posiciones, focal, foco (6 grados + zum + foco).
- Oficio, familias: mecánica por codificadores; óptica con marcas retrorreflectantes; óptica sin marcas; ultrasonidos/radiofrecuencia; inercial (deriva).
- Mo-Sys, ficha StarTracker Max: marcas retrorreflectantes en techo, pared o suelo o marcadores de pared de LED; salida Mo-Sys F4 / FreeD / OpenTrackIO sobre IP; 6 ejes con zum y foco; «inside-out», inmune a oclusión frente a «outside-in».
- Mo-Sys, catálogo: StarTracker + vSLAM + codificadores; croma y pared de LED.
- Oficio, croma vs LED: croma = problema del recorte (bordes, *spill*, sombras), se compone en control; LED = luz y reflejos reales, sin derrame; problemas propios: moiré, parpadeo, retardo, ángulo.
- Epic (*In-Camera VFX Overview*, UE 5.8): frustum interior = FOV de la cámara según focal, se mueve con ella; exterior = luz y reflejos, «remains static».
- Epic: Composure = composición en tiempo real (vídeo en directo, RA, croma, garbage mattes, color, distorsión de óptica).
- Epic (*Recommended Hardware*): croma en directo exige tarjeta SDI (entrada, salida compuesta, código de tiempo).
- Epic: croma sólo en el FOV = menos verde = menos *spill*.
- Oficio, iluminación: personaje con dirección, dureza y temperatura del decorado; fondo uniforme sin sombras ni manchas; separar personaje y fondo (menos *spill*; permite desenfocar).
- LE 8.6.1 p. 122, punto 4: colores fuertes no aconsejables, «impregnan de ‘croma’ el cuello y el mentón».
- LE 8.6.1, punto 9: Estilismo y Realización «deberán» tener en cuenta cromas, transparencias y plató con decorado virtual. Oficio: nadie viste del color del fondo.
- Oficio, grafista: decorado que cabe en el fotograma; casa con escala, suelo y luz del plató; lo diario en plantilla (tema 9).
- Epic (*Best Practices*): objetivo 48-72 fps en 4K en puestos de artista, comprobar en equipo de destino; 2-3x de margen orienta, no basta; pruebas periódicas.
- Epic: LOD, algunos a mano; un material por elemento (cada ID añade draw calls); texturas en potencias de 2 (128 × 256 y 256 × 256 sí; 8080 × 8080 no); luz precalculada mejor que trazado de rayos.
- Epic: optimizado lo aprueba Dirección de Arte, Diseño de Producción o quien firme el aspecto. Válido para croma: oficio.

## 2. Realidad aumentada

- Oficio: RV sustituye el entorno; RA lo conserva y añade objetos delante; RM, objetos que interactúan (oclusión, sombra, apoyo). Prueba: ¿queda mundo real? Firma de RM = oclusión.
- Oficio: objeto que el presentador tapa = *foreground*.
- Epic (*Professional Video IO*): el motor recibe y compone vídeo en directo, aplica croma, corrección de distorsión y de color, sincroniza con código de tiempo y cadencia, y devuelve la señal al estudio.
- Oficio: distorsión corregida para que el objeto se deforme como la imagen.
- Oficio, *foreground*: tercera capa delante = máscara píxel a píxel; el motor entrega decorado y máscara; un motor basta con incrustador de varias máscaras; croma = condición previa, no solución.
- Oficio, retardo: todo se retrasa hasta el más lento; el sonido también; nada se adelanta.
- Oficio, caso: 7 cámaras, 2 con RA (retardo de 2 fotogramas), transiciones cámara/su versión aumentada = 9 entradas (7 directas + 2 aumentadas).
- Oficio, solución: 2 fotogramas de retardo en las 7 directas (también las de 1 y 2) + sonido retrasa 80 ms todas las fuentes. Se puede mezclar una cámara con su versión aumentada.
- Oficio, cuentas: 25 fps = 40 ms por fotograma (1.000 ÷ 25); 2 = 80; 3 = 120; 4 = 160 ms; 25 fps = familia europea; a 50 fps, 2 fotogramas = 40 ms.

## 3. Pantallas

- LE 6.5.2 p. 93: entre los recursos del informativo, «‘vidi wall’, pantallas de plasma...», uso que «precisa cierto sentido estético y de una capacidad notable para aprovechar y armonizar los recursos disponibles».
- LE 3.10 p. 53: cierre con vídeo final, «vidiwall, croma...» como variantes estéticas.
- Oficio, contenidos: grafismo de fondo, programa (aux o banco M/E), exterior (matriz, «ventana»), vídeo (servidor), marcador/datos.
- Oficio, cuatro problemas: moiré, retardo, realimentación, parpadeo.
- Oficio, moiré: trama pantalla/sensor; desenfocar o cambiar tamaño.
- Epic: paso de píxel = distancia entre LED, menor = más densidad; distancia, paso y sensor fijan la distancia mínima de rodaje; foco delante o detrás de la pared; cámara perpendicular. Menos paso, cámara más cerca: oficio.
- Oficio, realimentación: programa a secas a pantalla visible = túnel infinito.
- Oficio, parpadeo: refresco de LED frente a obturación.
- Oficio, caso deportivo: programa al pabellón sin repeticiones ni vídeos (protestas del público contra arbitraje). Solución: otro banco M/E, enlazado (*link*) al programa, mapeado cambiado (botón de repeticiones apunta a cámara máster).
- Oficio, no valen: tabla de sustitución en el enlace; macro a negro con vídeo en previo.
- Oficio, retardo: la pared recibe, escala, reparte y pinta = fotogramas.
- Oficio, caso: retardo de 4 fotogramas, exteriores en ventanas: retrasar 4 fotogramas su entrada al mezclador, mandarlos a pantallas por matriz, retrasar su sonido 4 fotogramas (160 ms a 25 fps).
- Oficio, por qué: matriz = camino corto, sólo el retardo del programa de pantallas; entrada retrasada = coincide con la pantalla filmada (si no, salto de 4 fotogramas); por aux se suma el del mezclador; adelantar es imposible.
- Vizrt, *Viz Multiplay User Guide* 3.3: controla contenido de pantallas de plató desde control o por el presentador; envía a varias pantallas; directo, vídeo, grafismo, fijas; listas de reproducción; «Uses Viz Engine for playout»; abre listas de redacción en MOS; plantillas de Pilot Data Server.
- Oficio: sale a paneles por salida de gráfica o SDI, sin relleno y llave.
- Oficio, preparación: lienzo con resolución y proporción reales (rara vez 16:9); qué muestra cada bloque y quién lo cambia; qué sale en plano de cada cámara; brillo y contraste contenidos; sin texto importante tras el rótulo; sin tramas finas ni rayados.

## 4. Videowalls

- Oficio: muchas pantallas como una; LED y LCD (LCD sin fuente). LE: «‘vidi wall’» (6.5.2, p. 93), «vidiwall» (3.10, p. 53).
- Epic (*In-Camera VFX Overview*): pared = conjunto de armarios (*cabinets*), resolución fija de 92×92 (rótulos exterior) a 400×450 píxeles (interior de muy alta resolución); tamaño físico según fabricante.
- Epic: procesador de LED combina armarios en una imagen; disposición libre en el lienzo; en plató grande, diez procesadores o más.
- Oficio, lienzo = suma de píxeles de armarios: 8 × 3 de 400 × 450 = 3.200 × 1.350.
- Epic, paso de píxel: menor = más densidad, resolución y calidad y más coste por armario; no basta: ángulo de visión, desplazamiento y uniformidad del color, disipación del calor.
- Epic (*nDisplay Overview*): un ordenador principal y nodos secundarios; cada instancia dibuja para una o más pantallas, LED o proyectores; mismo fotograma a la vez y frustum correcto; *Output Mapping* a lienzo 2D; NVIDIA Mosaic o AMD Eyefinity.
- Epic, *failover*: sólo fallos detectados por red; activar en el clúster («Drop S-node on fail»); nodo sin respuesta sale tras tiempo configurable; su trozo deja de actualizarse (oficio).
- Epic, genlock: reloj propio de cámara, ordenadores y seguimiento; sin unificar, *tearing*.
- Epic (*Recommended Hardware*): NVIDIA Quadro Sync en cada nodo además de la gráfica; procesadores de LED con sincronía externa o desde la señal de las gráficas.
- Epic, color: tonemapper desactivado, sRGB lineal a los paneles; OCIO gestiona el color; espacio concreto según fabricante (oficio); colorimetría de emisión = tema 8.
- Epic: evitar SSGI, SSAO, SSR, viñeteado, adaptación de exposición y *bloom* (juntas entre nodos); probar en la pared (oficio).
- Vizrt, Multiplay: hasta 4 salidas DisplayPort UHD por GPU de un Viz Engine; con Datapath Fx4, más; también SDI.
- Viz Engine *Administrator Guide* 5.4, «Video Output»: Video Wall/Multi-Display = salida principal a DVI, activo y formato FULLSCREEN. Oficio: sin relleno y llave.

## 5. Grafismo en tiempo real

- Oficio: motor dibuja a la cadencia del vídeo. Mo-Sys: seguimiento por IP (F4, FreeD, OpenTrackIO) a Unreal Engine.
- Oficio: diferido = antes de emitir (Blender, Cinema 4D); tiempo real = al emitir (Unreal, Unity, Vizrt, Chyron). After Effects: fichero, sin directo.
- Oficio, motores: uno por punto de vista/cámara que pueda salir al aire; 3 cámaras + cabeza caliente = 4. Cabeza caliente no pide dos motores sino más ejes de seguimiento. Un motor potente no basta (simultaneidad, previo); varias tarjetas en un chasis siguen contando uno por punto de vista.
- Oficio, dos exigencias: un cuadro por cadencia (caída = tirón); alinear retardos de motor y seguimiento (un cuadro = decorado flota).
- Oficio, 4 funciones: diseño, datos, reproducción (alfa), control (manual, escaleta, automatización). Reparto = tema 3; plantillas = tema 9.
- Oficio: relleno = imagen; llave = transparencia (alfa en entrega: tema 8).
- Viz Engine *Administrator Guide* 5.4: «Contains Alpha» = propiedad de cada salida que da llave; sin modo especial (oficio).
- Viz Engine 5.2, «Dual Channel Mode»: dos salidas de programa (relleno y llave en dos canales), exige dos tarjetas; control externo (Viz Trio, Viz Pilot).
- Vizrt, *Introduction to Viz Artist* 5.3: modos Viz Artist / Viz Engine / Configuration; diseño en Artist, emisión en Engine (oficio); funciones según licencia (dongle).
- Epic, Motion Design (UE 5.8, «experimental»): motion graphics (rigging, cloners, formas 2D/3D, Material Designer); Rundown + Transition Logic para grafismo en directo; emisión, datos en tiempo real, informativos, meteorología, deportes; visor con canal alfa y zona segura (tema 8).
- Chyron, PRIME CG: render 3D en tiempo real; lower thirds, over-the-shoulders, bugs; timelines, spline editor, keyframing; importa Photoshop, After Effects y Autodesk FBX; *Base Scenes* (plantillas); escenas lógicas actualizadas por datos; redacción vía CAMIO; plataforma con videowalls, mezcla, branding; PRIME 5.3 HTML Input (nota de prensa 12-II-2026).
- Oficio, común a los tres: diseño, motor, datos, salida.
- Oficio, conexiones: redacción (MOS), bases de datos, mezclador y automatización, pantallas, postproducción (alfa, tema 5).
- Oficio, reglas: dato tecleado una vez; plantillas del programa, no del operador; camino manual si falla la fuente.

## Aplicación práctica

- Oficio, plató 3 cámaras + cabeza caliente, RA en 2: 4 motores; seguimiento con zum y foco, ejes de brazo en la cabeza caliente; directas retrasadas hasta la más lenta; incrustador con máscaras si hay *foreground*; vestuario sin color del croma ni colores fuertes (LE 8.6.1).
- Oficio, ensayo: seguimiento calibrado y motor por cámara; zum y foco al motor; figura no pisa lo no dibujado; marcas y monitor de retorno; orden de capas; retardo de imagen y sonido; luz personaje = decorado; sin tirones; rótulos y objetos en zona segura; textos largos.
- Oficio, videowall de informativo: lienzo por armarios y planos; fondos a ese tamaño; plantillas con camino manual; exterior por matriz, entrada y sonido retrasados lo que pinte la pared; nunca programa a secas; ensayo con cámara.

## Lo que este tema no da

- Sistemas de CSRTV; Brompton y otros procesadores de LED; tabla de distancias mínimas por paso de píxel; videowalls LCD; Zero Density, Pixotope, Ross XPression, Ventuz, CasparCG; especificación de FreeD; «chyron» como nombre común: sin fuente leída.
- Remite: temas 1, 3, 4, 5, 7, 8 (alfa, zonas seguras, HDR), 9, 17, 18.
