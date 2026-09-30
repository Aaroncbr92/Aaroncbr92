# Tema 12 del específico de Ayudante de Realización · Grafismo: rotulación, realidad aumentada, decorados virtuales, pantallas y elementos de continuidad visual

**Siglas**: RTVA, CSRTV, CSTV, RD, EBU, UIT, INCUAL, LE, RA (resultado de aprendizaje), RV/RM, LED, DSK, M/E, FTB, fr, fps, ms, HDR, SDR, HLG, PQ

Esqueleto para repasar, no resumen: el tema es lo que se estudia.

<!-- indice -->
<!-- /indice -->

## Fuentes y advertencia
- Sin norma sobre grafismo. LE 2004; EBU R 95 v1.1; UIT-R BT.2408-9; RD 1680/2011 (texto 2011; RD 500/2024 no toca esos módulos); IMS077_3; Vizrt, Mo-Sys, ATEM, Unreal Engine
- RD 0904: «Determinación del material de grafismo»; 0905: «Gestión, ajustes previos y lanzamiento de rótulos»

## Grafismo (base)
- Grafismo = lo añadido a la imagen que no sale de un objetivo (oficio)
- LE 3.16 p. 57: gráficos, formato más eficaz (IPC, inflación, hipotecas, paro); 3.16.2 p. 58: «claridad y precisión», palabras según LE
- RD 0904 RA 3 e) material gráfico en orden de escaleta; f) relación de rótulos en orden de escaleta
- RD 0905 RA 6 d) opciones y almacenamiento del titulador, señal incrustada; e) rótulos y claquetas, salida al mezclador
- IMS077_3 UC0216_3 RP3: CR3.5 relación de rótulos a infografía; CR3.6 grafismo 2D/3D minutado al grafista.
- Vizrt: Template Builder (diseño, import de Viz Artist, Typescript, datos en directo); redacción rellena, guarda data elements, a la escaleta; playout en control. Plantilla fija tipografía, color, tamaño, posición, animación (oficio). Quién diseña/rellena/lanza en RTVA: tema 4
- After Effects renderiza, sin directo; el control genera en el momento, relleno + llave (tema 9)
- ATEM: DSK «siempre se superpone… incluida la transición», ideal para logotipos y textos móviles; panel multimedia guarda imágenes con alfa; FTB funde todo lo al aire, gráficos incluidos
- Alfa = máscara de transparencia. JPG nunca (fotos, con pérdidas, 3 canales); PNG sí, 32 bits (8×4); TIF sí, 32 o más; TGA sí, 32; sin alfa 24. Gráficos: bits por píxel; vídeo (tema 14): por componente. Rótulo/mosca: PNG o TIF con alfa o par relleno-recorte; JPG tapa la imagen
- UIT-R BT.2408-9 § 2.1: Graphics White = HDR Reference White (blanco de tarjeta 100 % reflectante); tabla 1: 75 % HLG, 58 % PQ = 203 cd/m² (monitor PQ o HLG de 1.000 cd/m²)
- § 9: gráficos SDR a ese nivel, para no deslumbrar ni apagar el vídeo; color corporativo: «display-light mapping»; igualar con rótulo en escena: «scene-light mapping is usually preferred»

## 1. Rotulación
- LE 3.6.1 pp. 50-51: rótulo es información; brevedad, impacto, síntesis; sin tópicos; elemento fundamental que complemente locución e imagen
- Cuándo obliga:
  - LE 3.2.2: reconstrucción o simulación, «'reconstrucción'» todo el tiempo
  - LE 3.17.1.1 p. 59: entrevista, al menos una vez, sobre todo primeros planos
  - LE 3.13: intro, momento y lugar
  - LE 4.3 p. 68: declaración de líder político, sólo el rótulo
  - LE 3.7.1: total en lengua extranjera, subtítulos resumidos
  - LE 8.2.1: «Enviado especial» no vale para Andalucía ni corresponsalías o delegaciones estables
  - LE 9.2.12.3 p. 130: «obligatorio» «Reconstrucción» durante todo el tiempo de las imágenes
  - LE 9.9.1 p. 166: «Archivo» (delincuencia, malos tratos, judiciales) todo el tiempo, con margen para leerlo sin apremio
  - Lanzamiento (oficio): no quitar mientras dure la imagen
- Escritura:
  - LE 3.6.1 p. 51: verbo por coma, incluyéndola («Los aeropuertos, en alerta»)
  - LE 3.6.1 p. 50: sin títulos de canciones, películas, novelas, obras, dichos; sin siglas salvo sobradamente conocidas ni cifras de mucho detalle
  - LE 13.8.1 p. 267: fecha sin artículo ante el año («11 de junio de 2003»)
  - LE 11.2.6 p. 190: sigla sin plural («las ONG»)
  - LE «Siglas y acrónimos» p. 323: equivalente español (OTAN, ONU), «obligatoria en las rotulaciones»
  - LE 10 p. 169: sin tratamientos («José Antúnez. General Jefe de la Región Sur»)
  - LE 13.1.1.3 p. 259: sin signos ajenos al nombre extranjero; diacríticos «siempre que sea posible» (Schröder)
  - LE 11.3.1.1.1 p. 193: artículo del topónimo en mayúscula (El Salvador, La Carolina)
  - LE 13.3.1 p. 261: Jerusalén, no Jerusalem
- Zonas seguras, EBU R 95 v1.1 (16:9): acción esencial en Action Safe; grafismos en Graphics Safe; centro de imagen sin desplazar salvo razón creativa
- Nota 5: acción 3,5 %, grafismo 5 % por borde; restado 93 % y 90 % (resta, no cifra de la norma). Valores: 576i, 720p, 1080i/1080psf, 1080p, 2160p, 4320p (figs. 1-6)
- 1080p (fig. 4): acción 67 px por lado, 38 arriba y abajo, 1786 px, líneas 80-1083; grafismo 96 y 54, 1728 px, líneas 96-1067 (cuadro 1125, activas 42-1121)
- 2160p (fig. 5): acción 134 y 76, 3572 × 2008; grafismo 192 y 108, 3456 × 1944
- 1080i/1080psf (fig. 3): mismos anchos. Zona de rótulos 4:3 central: 1296 px en 1080, 2592 en 2160p
- Oficio: rótulo, mosca, marcador en zona de grafismo; sin tapar cara ni boca
- IMS077_3 UC0217_3 CR2.5: lanzamiento en códigos de tiempo de entrada y salida del parte de emisión. Identificación: entra con la persona asentada, sale antes del cambio de plano (oficio)
- LE 3.16 p. 57: no más de cuatro o cinco elementos por pantalla; mínimo recomendable ocho segundos. Animación por elementos (3.16.1), cama de audio (3.16.2): tema 9. Identificación: sin duración escrita en LE

## 2. Realidad aumentada
- Decorado virtual: real sólo personas y lo que tocan; fondo sintético; croma. AR: real el plató entero; objetos superpuestos con llave. Producción virtual en pared de LED: fondo en pantallas reales, sin incrustación
- RV sustituye el entorno; RA lo conserva y añade; RM añade objetos que interactúan (oclusión, apoyo, sombra): la oclusión es la firma. ¿Queda algo del mundo real?
- Seguimiento: 6 grados de libertad (3 posición, 3 orientación) más zum y foco, al motor en tiempo real
- Familias (oficio): mecánica por codificadores; óptica con marcas retrorreflectantes; óptica sin marcas; ultrasonidos o RF; inercial (deriva)
- Mo-Sys StarTracker Max: marcas retrorreflectantes o marcadores de pared de LED; salida Mo-Sys F4 / FreeD / OpenTrackIO sobre IP; «6-axis tracking with lens zoom and focus»; «inside-out», inmune a oclusión de sistemas «outside-in». Sin seguimiento: cámara fija (oficio)
- Motor de render: dibuja a la cadencia de fotogramas; Unreal Engine ejemplo
- Motores: uno por cámara que pueda salir al aire (oficio); 3 cámaras + cabeza caliente = 4; cabeza caliente = más ejes de seguimiento, no más render; un motor potente no basta (simultaneidad, previo)
- Foreground: tercera capa delante del presentador = máscara píxel a píxel; con un motor, incrustador con varias máscaras; dos motores otra vía; croma es condición previa, no solución
- Retardo (oficio): se retrasa todo hasta el más lento; nunca se adelanta; el sonido también
- Caso: 2 cámaras con AR (2 fr), 5 sin ella; 9 entradas (7 directas + 2 con AR). Solución: 2 fr en las 7 directas (también 1 y 2, para cortar entre directa y aumentada) y sonido 80 ms en todas las fuentes del plató
- 25 fps = 40 ms por fr (1.000 ÷ 25): 1 fr 40, 2 fr 80, 3 fr 120, 4 fr 160; a 50 fps, 2 fr = 40 ms. Sincronía: tema 11; 25 fps: tema 14

## 3. Decorados virtuales
- Fondo por motor de render, incrustación de crominancia; seguimiento dice desde dónde dibujar; mezclador incrusta o conmuta imagen compuesta (tema 9)
- RD 0904 «Escenografía virtual»; 0910 RA 4 g) capacidades de escenografía virtual y vinculación con cámaras y mezclador
- IMS077_3 UC0216_3 RP4 CR4.2: integración real y virtual adecuada a movimientos de cámara y personal artístico; MF0216_3 CE8.2: iluminación y atrezo no dificultan la integración
- Mismo seguimiento en croma y LED; StarTracker Max «equally at home» en ambos
- Croma: recorte (bordes, spill, sombras). LED: sin incrustación, luz y reflejos reales; moiré, parpadeo, retardo (oficio)
- Iluminación (oficio): personaje como en el decorado (dirección, dureza, temperatura de color); fondo uniforme, sin sombras ni manchas. Errores: no iluminar el fondo; pegar al personaje (más spill)
- LE 8.6.1 p. 122: punto 4, colores fuertes «se saturan e impregnan de 'croma' el cuello y el mentón»; punto 9, Estilismo y Realización «deberán» atender a cromas, transparencias, decorado virtual. Nadie viste del color del fondo (oficio). Croma: tema 9; luz: tema 10
- Ensayo (oficio): seguimiento y motor por cámara; zum y foco al motor; figura sin pisar lo no dibujado; marcas y monitor de retorno; capas y máscara; retardos; luz del personaje. Marcas: tema 5

## 4. Pantallas
- LE 6.5.2 p. 93: «vidi wall», pantallas de plasma, «cierto sentido estético»; LE 3.10 p. 53: cierre con «vidiwall, croma...»
- Contenido (oficio): grafismo de fondo (servidor propio); programa (auxiliar o M/E); exterior (matriz); vídeo (servidor); marcador o datos
- Problemas (oficio): moiré (desenfocar, cambiar tamaño); retardo; realimentación (túnel infinito: nunca el programa a secas); parpadeo si refresco no casa con obturación (temas 8 y 10)
- Unreal Engine (Epic): paso de píxel = distancia entre LED, «the closer… the lower the pitch… the higher the pixel density»; distancia de rodaje según distancia, paso y sensor; menor paso, cámara más cerca (deducido); foco delante o detrás de la superficie; cámara perpendicular
- RD 0905 RA 6 c): enrutamientos de vídeo y audio en matrices, switcher o preselectores hacia grabadores auxiliares y pantallas
- Caso deporte (pabellón sin repeticiones ni vídeos; protesta arbitral). Solución: otro M/E enlazado (link) al programa con mapeado distinto (botón del servidor apunta a cámara máster). No valen: tabla de sustitución en el enlace; macro a negro con vídeo en previo (no siempre pasa por previo)
- Caso LED 4 fr con exteriores en ventanas: exterior por matriz a pantallas; retrasar 4 fr su entrada al mezclador; retrasar 4 fr su sonido. Auxiliar del mezclador sumaría retardo; adelantar es imposible. 4 fr a 25 fps = 160 ms
- Por pantalla (oficio): qué muestra, de dónde, quién la cambia, planos en que sale

## 5. Elementos de continuidad visual
- Continuidad = área que emite el canal; hace lo que va entre programas; evita el negro. Sale: cortinillas e identidad (mosca, caretas, cabeceras); autopromociones; publicidad en bloques; enlace entre programas; avisos (señalización, rótulos de servicio)
- RD 0904, «Control de tiempos de emisión, publicidad y autopromoción»: escaleta de continuidad; elementos de puntuación; operación de equipos; comunicaciones y órdenes
- IMS077_3 UC0217_3 CR2.6: hora de entrada y tiempos de publicidad a continuidad, con cuenta atrás
- Elementos (oficio): mosca; careta; cortinilla; autopromoción; rótulos de servicio; paquete gráfico
- ATEM: transición con logotipo. Cortinilla: tema 9
- LE 6.5 p. 92: informativos CSTV y Canal 2 con marco «uniforme»; realizador «puede, y debe, aportar ideas propias». LE 6.5 p. 93: todo programa con intencionalidad, audiencia, concepto formal y criterio propio de realización
- LE 7.4 p. 104: desconexiones «están obligadas» a coherencia estética y conceptual con la edición general: mismo paquete gráfico (oficio). Herramienta: la plantilla
- LE 6.4 p. 92: raccord = «continuidad y uniformidad visual de los planos con sentido lógico»; cuatro aspectos (técnico, físico, sonoro, cinético); técnico: sin diferencias de color, brillo, contraste, tono, luz, altura de planos, calidad. Tema 1
- RD 0905 RA 4 b): atrezo y elementos móviles que comprometan la continuidad visual; contenido: supervisión en ficciones. IMS077_3 UC0216_3 CR4.3: detalles de continuidad en retomes
- Aplicado (oficio): rótulo y mosca fijos; decorado sin despegarse; mismo paquete plató y vídeo; HDR y SDR al Graphics White

## Normativa que el tema invoca
- RD 1680/2011 (BOE núm. 302, 16-XII-2011): 0904 RA 3 e), f); 0905 RA 4 b), RA 6 c), d), e); 0910 RA 4 g). IMS077_3: UC0216_3 (CR3.5, CR3.6, CR4.2, CR4.3, CE8.2); UC0217_3 (CR2.5, CR2.6)

## Lo que el tema no da
- Sistema de CSRTV; manual de identidad gráfica; especificación FreeD; distancias por paso de píxel; duración del rótulo de identificación
- Tema 4: quién diseña, rellena, lanza. Tema 9: llaves, croma. Tema 1: raccord. Tema 5: marcas. Tema 14: HDR

## Trazabilidad
- Fuentes leídas el 29-09-2026
