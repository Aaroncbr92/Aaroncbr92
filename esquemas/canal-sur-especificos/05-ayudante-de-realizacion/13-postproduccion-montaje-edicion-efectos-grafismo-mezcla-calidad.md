# Tema 13 del específico de Ayudante de Realización · Postproducción: montaje, edición, efectos, grafismo, mezcla y revisión de calidad final

**Siglas**: RTVA, CSRTV, RD, RA (resultado de aprendizaje), UIT-R, UER/EBU, QC (control de calidad), PPD, EDL, AAF, TC, LTC, VITC, DF/NDF, LUT, HDR, SDR, ADR, M&E, LUFS, LU, dBTP, AFD, PAM/MAM, LSM, CIE.

Esqueleto para repasar, no resumen: la fuente va delante; (o) = oficio, sin norma; (c) = cálculo propio.

<!-- indice -->
<!-- /indice -->

## Postproducción
- (o) Todo tras registrar y antes de entregar: ingesta, montaje, grafismo, efectos, etalonaje, sonido, máster. En directo no hay postproducción; lo más cercano, la repetición.
- X Convenio RTVA (BOJA 240, 10-12-2014, anexo III): Realizador (p. 196) «controlar la calidad y duración» y «Dirigir las tareas de montaje, postproducción y mezclas hasta su completo acabado»; Ayudante (p. 111) «Coordinar»; Encargado Operación y Montaje Vídeo 5212204 (p. 127) y Operador Montador 5212206 (p. 190) control técnico/calidad; Editor de Continuidad 5302010 (p. 125) calidad de la emisión. Fichas de 2014.
- RD 1680/2011 (BOE 302, 16-12-2011), módulo 0907: norma de enseñanza. RA 2 montaje, RA 3 efectos, RA 5 acabado. RD 500/2024 no toca estos módulos.

## Montaje
- RD 1680/2011, 0907 RA 2.g: verificar montaje contra documentación de rodaje; RA 2.h: valorar ritmo, claridad, continuidad, fluidez.
- Eisenstein, por J. M. Todd (Georgia Tech, 1989, p. 8): cinco métodos, cuatro fisiológicos y el intelectual dirige el pensamiento. Métrico (pp. 10-11): duración absoluta, contenido subordinado. Rítmico (p. 13): choque duración/movimiento interno. Tonal (p. 15): «emotional sound» (luz, ángulos). Sobretonal (p. 17): suma de los tres. Intelectual (p. 20): síntesis mental; león de *Potemkin* (1925). *Film Form* no leído.
- (o) Montaje preliminar: primer armado, sin efectos ni música; lo demás va después.
- (o) *Offline*: baja resolución, decide; *online*: acabado con resolución completa.
- Media Composer User's Guide (1999) p. 710: EDL = lista de cortes con TC para recrear la secuencia; «events». AAF/XML: tema 14.
- (o) Revisar contra guion y minutado (tema 7); reordenar tras etalonar obliga a rehacer.

## Edición
- (o) Lineal: cintas, secuencial, pierde generación. No lineal: archivos, acceso aleatorio. Se recodifica al calcular efectos o exportar.
- Programas: sistema de CSRTV no consta; Avid Media Composer, DaVinci Resolve 21, Adobe Premiere como ejemplo.
- Media Composer p. 447: tres puntos, la cuarta la calcula el sistema. Insertar (*splice-in*): desplaza, alarga (p. 447). Sobrescribir (*overwrite*): no alarga (p. 448). Reemplazar (*replace*): conserva IN/OUT (p. 449).
- *Trim* (pp. 522-523, modo *Trim*, *Big Trim*): un lado cambia duración; dos lados (*dual-roller*, p. 526; iconos p. 531) no. *Slip* y *slide* (p. 540) sin cambiar duración ni sincronía; *slip* cambia el contenido, *slide* recorta vecinos (p. 543).
- Corte partido (p. 502) = edición solapada (p. 537), índice «L-cut edit». *Trim* de dos rodillos en vídeo o audio, no ambos (p. 538); *extend edit*. L: imagen por delante; J: sonido por delante (guía de 1999 sólo L). Vista de cabezas pierde el desfase.
- Varias cámaras: clip de grupo (p. 268), sincroniza por TC (p. 662). Libro de Estilo 3.17.1.5 (p. 61): TC idéntico.
- *Match frame* (p. 431): localiza el original del cuadro; *Reverse Match Frame*.
- Coleo: RD 0905 RA 1.b «coleo de entrada, coleo de salida»; sin él, «a capón» (o).
- *Render*: Resolve p. 209 caché *Smart* o de usuario; p. 222 sólo sirve a su proyecto; desechable.
- Códec (o): captación (AVC-Intra, XDCAM, H.264/H.265), edición (DNxHD/DNxHR, ProRes), ligero (DNxHD 36, ProRes Proxy, DNxHR LB). Avid DNxHD Technology (2012): formatos de cámara no aguantan efectos multigeneración.
- TC (o): HH:MM:SS:CC. LTC como audio; VITC en el intervalo vertical; LTC 80 bits, 32 de usuario. DF sólo a 29,97/59,94; salta números, no imágenes.
- (c) 25 c/s, 00:47:17:23 a 01:23:54:00 = 00:36:36:02 (inclusiva 00:36:36:03). RA 2.f: offset de TC y sincronía.
- (o) PAM = producción; MAM = terminado (ninguna fuente lo define). Avid MediaCentral *Production Management* (25-09-2026): NEXIS, permisos, metadatos, Cloud UX. CSRTV no consta.
- Servidor de repetición (EVS, LSM; o): graba y reproduce a la vez, mando físico, clip con dos pulsaciones. Lista de reproducción: un canal, encadena. Línea de tiempo: dos canales, transiciones. *Ganged* (IPDirector 6.2, junio 2013, p. 30): «Synchronize the timecode on all the ganged channels». Volcado (*dump*, sin contrastar).

## Efectos
- Blackmagic cap. 56 p. 1213: parámetros Composite, Transform, Cropping. Familias (o): composición, transformación, tiempo, imagen, transición.
- RD 0907 RA 3.b: composición multicapa (color, velocidad, difuminado de rostros, keys, seguimiento, estabilización). RA 3.c: keys de luminancia, crominancia, matte y por diferencia.
- Incrustar (o): *chroma key*, *luma key*, alfa, máscara/*roto*. Verde/azul lejos de la piel; verde: doble de fotositos. Fondo uniforme, sin ropa del color, reflejos; submuestreo fuerte peor que 4:2:2/4:4:4. Mezclador: tema 9; alfa: tema 12.
- (o) Máscara: grises; blanco visible, negro oculto; no borrar píxeles.
- *Keyframe* fija qué y dónde; curva de velocidad fija cómo. Resolve *Ease* (p. 1199): None, In, Out, In & Out, Custom.
- Tiempo, Resolve cap. 58 (pp. 1254-1264): *Change Clip Speed*, *Retime Controls* (Comando-R), *Fit to Fill*, *Reverse Speed*, *Freeze Frame* (Mayúsculas-R); rampa mínimo dos puntos (p. 1259); *Retime Frame* (permite marcha atrás) y *Retime Speed* (no).
- *Retime Process* (p. 1265): *Nearest* (duplica o descarta), *Frame Blend* (mezcla), *Optical Flow* (mejor y más pesado; artefactos con cruces o cámara impredecible); *Standard*, *Enhanced*, *Speed Warp* (pp. 1265-1266). (c) 25 i/s al 50 % dura el doble.
- Adobe (07-01-2026): corte = último cuadro y primero del siguiente; transición = enlace animado. Blackmagic p. 1194: cambio de tiempo o lugar.
- Transiciones (o): fundido encadenado, a negro, cortinilla (casi nunca en noticia), audio. Resolve p. 1198: seis estilos, *Video* lineal, *Film* logarítmico, aditiva aclara, sustractiva oscurece.
- Colas (*handles*, o). Resolve p. 1196: un segundo por defecto o lo que permitan; p. 1197 (Comando-T) *Trim Clips*, *Skip Clips*, *Cancel*. Adobe: «Trim at least 15 frames off of each clip for a centered 1:00 transition». (c) D/2 por plano; a 25 i/s 1 s = 12-13 cuadros, 2 s = 25.
- Etalonaje (o): técnico/primario, igualación, creativo/secundario, comprobación. Cap. 125 (pp. 3086-3095). RD 0907 RA 5.c color y etalonaje; RA 3.e igualar.
- Monitores, cap. 127 (pp. 3150-3152): «five available video scopes»: forma de onda, desfile, vectorscopio, histograma, CIE. HDR sin gestión: «not be 100% accurate» (p. 3147). Desfile: altas = mucho contraste; dominante = gráfica que sobresale (o). Vectorscopio: ángulo = matiz, distancia = saturación; dianas 75 %, línea de piel.
- LUT (o): 1D por canal (curvas); 3D cubo RGB (tono y saturación); técnica o *look*. Cap. 150 p. 3545: CLF y DCTL son scripts. Mal expuesto se exagera (o); 3D recorta fuera de rango (p. 3546); *shaper LUT* 1D antes.
- Primaria (o): *lift*, *gamma*, *gain*, *offset*; secundaria: ventanas y cualificadores HSL/RGB/luminancia (p. 3090). Primero la primaria. Color de memoria: piel, follaje, cielo.
- Igualar (p. 3091): *Gallery*; copiar o agrupar (p. 3092). (o) Referencia primero; piel en el mismo punto del vectorscopio. Libro de Estilo 3.17.1.5 (p. 61) planos «compatibles y uniformes».
- Libro de Estilo (2004) y efectos: 9.9.2 (p. 167) ocultar con medios técnicos; 9.9 (p. 166) menores, víctimas, testigos protegidos, fuerzas de seguridad: rostros tramados si hay riesgo; 9.9.2 no acentuar morbosidad con ralentizado o congelado; 3.2.2 (p. 46) «reconstrucción»; 9.9.1 (p. 166) «Archivo»; 9.2.12.4 (p. 130) cámara en mano, música tópica, blanco y negro evocan ficción. Temas 1 y 16.

## Grafismo
- (o) Área de grafismo diseña; el montador inserta y rellena plantillas. Ficha del Grafista: tema 4. Dónde se incrusta no consta.
- RD 0907 RA 3.d integrar gráficos externos; RA 3.f archivar parámetros.
- Resolve cap. 56: título por defecto 5 s (p. 1213); *Lower 3rd* L/M/R, *Scroll*, *Text*, *Text+*, *Fusion Titles* (p. 1215).
- Libro de Estilo 3.16 (pp. 57-58): cuatro o cinco elementos por pantalla, mínimo ocho segundos; «cama» de audio; 3.6.1 (p. 50) rótulo = información.
- Tema 12: EBU R 95, alfa (JPG sin, TGA 32 bits), UIT-R BT.2408. (o) Zona segura de título; logo con alfa; HDR al blanco de referencia. Destellos: ver revisión.

## Mezcla
- (o) Orden: diálogos, ambientes, efectos, música, conjunto (sonoridad, pico). Procesos: operador de sonido. Capas: tema 11.
- RD 0907 RA 2.e: banda sonora con diálogos, efectos, músicas, locuciones. Convenio: Realizador dirige «mezclas».
- Limpiar (o): edición, paso alto, zumbido, ruido, sibilantes, ecualización y compresión; ambiente bajo los cortes.
- *Crossfade* (o): dos o tres fotogramas; en corte en L/J, en el punto del sonido.
- ADR (o): sustitución de diálogo en sincronía labial; sustituir, cambiar, añadir; *looping*.
- Tech 3343: mezclar «only by ear» con escucha fija.
- EBU R 128 (v5, nov. 2023): h) −23,0 LUFS, directo ±1,0 LU; i) ±0,2 LU de medida; m) pico ≤ −1 dBTP, medida ±0,3 dB; k) UIT-R BS.1770 y Tech 3341; n) LRA Tech 3342, no recomendada bajo 1 minuto; l) programa entero. «Programa» incluye anuncio, tráiler, promo.
- Tech 3343 (v4, 2023): postproducción ±0,2 LU; ganancia estática (§ 3.2); medidores offline (§ 3.1). (c) X dB = X LU y X dB de pico: −21,4 LUFS/−2,5 dBTP baja 1,6; −24,5/−1,8 sube 1,5 = −0,3 dBTP, no cumple: limitar ≥ 0,7 dB y remedir.
- (o) Pieza corta (R 128 s1 V3, agosto 2020): corto plazo ≤ −18 LUFS. Voz inteligible, mono sin pérdida, sin chasquidos ni silencios, sincronía.

## Revisión de calidad final
- (o) Técnico (señal, sonido, fichero) y editorial; sala de montaje, continuidad en emisión; responde el realizador.
- RD 0907 RA 5.e integración y pistas; 5.f normativas y formatos; 5.h cinta PPD con claquetas y pistas. Contenidos: «La banda internacional», «Normas PPD». 0906 RA 3.e.
- UER, *Quality Control* (01-09-2015): plantillas por destino; «Automated QC», «File Package Compliance» (AS11 DPP), «Manual QC», «File Structure Analysis»; informe con firma.
- qc.ebu.io: sonoridad, destellos, niveles de vídeo, imagen congelada, silencio, fase invertida, TC (inicio, discontinuidades, inválido, segundos = 80), subtítulos que faltan, AFD.
- UIT-R BT.1702-3 (11/2023), recomendación; sustituye a BT.1702-2. Destellos: < 160 cd/m² diferencia ≥ 20 cd/m² (SDR y HDR); ≥ 160 cd/m² > 1/17 Michelson (HDR); rojo saturado. No permitido: > 25 % de pantalla y > 3 destellos/s. Aceptables: aislados hasta triples; ≥ 360 ms (50 Hz) o ≥ 334 ms (60 Hz). Cortes rápidos igual; > 5 s riesgo.
- BT.1702-3, patrones: rayas > 5 pares, estáticas > 40 % o en movimiento/inversión > 25 %; mismo contraste que un destello; exento flujo suave en un sentido. Notas: 3 blanco SDR 200 cd/m², HLG 1.000; 5 analizadores; 1 variaciones. (c) 360 ms = 9 cuadros a 25 i/s. Norma de Canal Sur no consta.
- Máster (o): formato y códec, resolución y cadencia, color y niveles, pistas, sonoridad, estructura (barras, claqueta, cuenta atrás), subtítulos; uno por destino.
- Pista internacional: EBU R 123 (julio 2009) anexo 2.2, SMPTE: todo salvo el diálogo; 2.3 «qualifying explanation»; 2.3.1 *Documentary M&E* (*sync*, *un-dipped*); 2.3.2 *Fiction M&E* («footsteps»); 2.3.3 *Clean FX*, 2.3.4 *World Feed*. (o) Locución en pista propia.
- RD 0905 RA 1.f: máster, señal sin incrustaciones, cámaras dobladas o masterizadas. Libro de Estilo 3.17.1.5 (pp. 61-62): «falso directo»; sólo se manipula el «master» para defectos técnicos de fácil resolución.
- (o) Pasos: contenido, duración al cuadro, imagen, destellos, sonido (−23 LUFS ±0,2 LU, −1 dBTP), fichero, constancia (parte, firma). Fallo: a su fase de origen. Formatos: tema 14; parte: tema 7.

## Aplicación práctica y lo que no da
- Reportaje 5 min: estructura cerrada, igualar color, rótulos con plantilla, colas 12-13 cuadros, −23 LUFS ±0,2 LU, −1 dBTP, sin > 3 destellos/s en > 25 %. Partido: volcado, *ganged*, flujo óptico. Pieza devuelta (−24,5 LUFS, −1,8 dBTP, silencio 2 s, congelado 12 cuadros): limitar ≥ 0,7 dB, anotar lo voluntario.
- No constan: sistemas, entregas, plantillas y pistas de CSRTV; norma jurídica española sobre destellos (no buscada). No leídos: *Film Form*, Avid vigente (guía 1999), R 123 posterior, Tech 3363. Corte en J y *dump*: oficio.
- Remisiones: 1 lenguaje, 3 funciones, 4 grafista, 7 documentos, 9 mezclador, 11 sonido, 12 grafismo, 14 formatos, 16 accesibilidad, 17 derechos.
