# Tema 7 del específico de Operador/a Montador/a de Vídeo · Postproducción

**Siglas**: RTVA; CSRTV; UIT-R; UER/EBU; RGB; Y/Cb/Cr; YRGB; LUT; CLF; DCTL; HSL; HDR (HLG, PQ); SDR; cd/m²; JPG/PNG/TIF/TGA; SRT/WebVTT/IMSC1/DFXP; CEA-608/708; MXF; IMF; SMPTE; Rec. 709; UNE; dB/dBFS/dBTP/LUFS/LU/LRA; SNR; VO; SFX; HVAC; IA.

Esqueleto para repasar, no resumen: cada línea remite al tema; sin el tema no se entiende.

<!-- indice -->
<!-- /indice -->

## 1. Color básico

- (Resolve) Etalonar=llevar a un patrón; 4 fases: técnico/primario, igualación, creativo/secundario, comprobación de entrega. (Blackmagic) Corregir=técnico; etalonar=+aspecto.
- (Resolve, 5 scopes) Forma de onda: negros/blancos y rango. Desfile: alturas R/G/B→dominante y contraste (alto=mucho contraste). Vectorscopio: matiz (ángulo) y saturación (distancia al centro); dianas al 75 %. HDR sin gestión de color→forma de onda no fiable 100 %.
- (Blackmagic) LUT=tabla de consulta, no calcula. Técnica/conversión vs. creativa/look. 1D (curvas por canal) vs. 3D (cubo RGB). Formato .cube (Resolve), 17/33/65 puntos; 17 no recomendado para gradar. No corrige mal expuesto, lo exagera. 3D recorta fuera de rango→shaper LUT (1D delante) lo evita.

## 2. Corrección

- (oficio) Primaria (imagen entera: negros, blancos, contraste, balance, saturación) antes que secundaria (zona/color/objeto).
- (Blackmagic) Lift=sombras; Gamma=medios; Gain=altas luces; Offset=todo el rango por igual. Zonas solapadas, escala 0-1023.
- (Blackmagic) Temp=ajuste de gain eje cálido-frío (−4000/+4000). Tint=ajuste de gain eje magenta-verde, fluorescente/sodio (−100/+100). Contraste/Pivot: separa/junta claros-oscuros sobre pivote, curva en S sin clip. Saturación: 50=unidad, 0=B/N, 100=doble. Color Boost=saturación no uniforme (vibrancia). (oficio) Dominante sólo en sombras→se corrige en lift, no en temp/tint (gain).
- (Resolve) Auto Color: balance automático negros/blancos sobre Rec. 709 y gamma 2.4; punto de partida, se comprueba en scopes.
- (Blackmagic) Secundaria=como EQ de audio: ventana (forma, sigue al sujeto) o cualificador HSL/RGB/luminancia. Color de memoria: piel, vegetación, cielo; ejemplos: piel verdosa, cielo lavado.
- (oficio) Igualar planos: referencia primero (total/presentador), comparar en Gallery o alternando, copiar corrección o agrupar; piel del entrevistado en mismo punto del vectorscopio en 2 cámaras.
- (Libro de Estilo, 9.2.12.4) Sucesos: cámara en mano, música tópica, virado B/N evocan ficción; información=realidad. (oficio) Extensión a toda la información; virado/dominante fuerte cabe en promo/cultural, no en informativo.

## 3. Efectos

- (oficio) Efecto=todo lo que no es corte simple; no existe como archivo, se renderiza (tema 3). Familias: composición (incrustación, capas, opacidad, fusión); transformación (tamaño/posición/rotación/recorte/estabilización); tiempo (lenta/rápida, congelado, marcha atrás); imagen (color, desenfoque, pixelado, nitidez, viñeta); transición.
- (oficio) Incrustar=sustituir parte de imagen. Familias: chroma key (color), luma key (brillo), alfa (4º canal), máscara/roto (forma dibujada). Verde/azul: colores más alejados de la piel; verde se impuso (sensor con doble de fotositos verdes, menos ruido). Croma: fondo uniforme, sujeto sin ropa del color del fondo, luz rebotada tiñe bordes; submuestreo fuerte (tema 2)→bordes peores.
- (oficio) 3 señales: fondo (background), relleno (fill), recorte (key); con alfa, key y fill comparten fichero, siguen siendo 3. Alfa=4º canal, opacidad por píxel: 0 transparente, máximo opaco, intermedios=mezcla; notación 4:4:4:4 (tema 2). Máscara de capa=alfa a mano en grises (blanco=ve, negro=no, gris=medias). (oficio) No se recorta borrando píxeles: los rótulos se retocan siempre.
- (oficio) Fotograma clave=valor en un instante, interpolación entre dos. Curva de velocidad=cómo se recorre (constante/acelera/frena). (Resolve, Ease) Suavizado: None/In/Out/In&Out/Custom con keyframes.
- (Resolve) Change Clip Speed/Speed %/Retime Controls/Fit to Fill (constante); Reverse Speed/Segment (marcha atrás); Freeze Frame (congelado); speed points, mín. 2 (rampa); Retime Frame con reversa, Retime Speed sin. <100 %: triángulos amarillos separados; >100 %: azules. Audio lineal cambia con vídeo (Pitch Correction opcional); variable→mudo. Nearest: dropea/duplica cuadros. Frame Blend: disuelve duplicados adyacentes. Optical Flow: genera cuadros nuevos, más calidad y carga; falla con movimientos cruzados.
- (Libro de Estilo, 9.9/9.9.2) Rostro cubierto/tramado si riesgo (menores, víctimas, testigos protegidos, fuerzas de seguridad); máscara sigue la cara fotograma a fotograma. Ralentización/congelado no para morbo. "Reconstrucción" mientras dure (3.2.2); "Archivo" en imágenes de archivo de delincuencia/malos tratos/judicial (9.9.1).

## 4. Grafismo

- (oficio) Grafismo de casa lo diseña grafismo; montador inserta y hace rótulos sencillos. No consta si CSRTV incrusta en sala o en emisión.
- (Resolve) Título=clip editable, 5 s por defecto. Generadores: L/M/R Lower 3rd (identificación); Scroll (créditos, duración=velocidad); Text; Text+ (más opciones, un solo estilo); Fusion Titles (plantillas a medida). (oficio) Plantilla=mismos tipografía/tamaño/posición en todo el programa (tema 13).
- (Resolve) Zonas: Action (movimiento dentro) y Title (texto dentro); origen TV de tubo, útiles también para móviles/redes; por defecto 93 % acción, 90 % título. (oficio) Ningún rótulo fuera de zona de título, nada tapando la cara. Guías Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9 (tema 12).
- Alfa en fichero=recorte guardado dentro. JPG: nunca alfa (3 canales, pérdidas). PNG/TIF/TGA: sí alfa, 32 bits (8+8+8+8); 24 bits=sin alfa. Bits/píxel (gráficos)≠bits/componente (vídeo, tema 2). (oficio) Rótulo/logo con transparencia→PNG o TIF con alfa, o par fill/key; JPG llega con fondo.
- (UIT-R BT.2408-9, § 2.1) Graphics White=blanco 100 % reflectancia=HDR Reference White; 75 % HLG, 58 % PQ, 203 cd/m² (tabla 1, tema 2). (§ 9) SDR mapeado a Graphics White para no deslumbrar ni apagar el vídeo. Display-light si se conserva color corporativo; scene-light si iguala con rótulo en escena.
- (Libro de Estilo, 3.16) Máx. 4-5 elementos/pantalla, mín. 8 s. (3.16.2) Cama de audio salvo sonido propio de la grabación. (3.6.1) Rótulo=información: brevedad, impacto, síntesis.

## 5. Subtítulos

- (Univ. Burgos, p. 4) Abierto=incrustado, sin control del usuario, se corrige rehaciendo el vídeo; uso en redes sin sonido y traducción de un total. Cerrado=se añade/quita a voluntad, más accesible, se corrige en el fichero; uso en accesibilidad/plataformas.
- (oficio) Informativo: total en otro idioma/ininteligible→incrustado como rótulo; accesibilidad de emisión va aparte, normalmente no la hace el montador.
- (Resolve) Fichero aparte: IMSC1, DFXP, SRT, WebVTT. Burn into video=abierto. Embedded: CEA-608 en MXF OP1A/QuickTime. Sin salida CEA-708 ni Line 21 vía Decklink/UltraStudio. IMF: subtitle tracks (data essences).
- (Univ. Burgos, síntesis UNE 153010, no leída) Centrado abajo, 2 líneas (excepc. 3); máx. 37 car/línea; no partir sílabas; línea nueva por personaje; ~15 car/s; sincronía con labios/corte/locución; 1 línea ~3 s, 2 líneas máx. 6 s (rango 1-6 s); pausas con comas/puntos.
- (Univ. Burgos, p. 4-5) Tipografía muy legible. Info contextual entre paréntesis, misma línea (p.4); en mayúsculas en "efectos sonoros" (p.6, inconsistente con p.5). Mayúsculas sólo título del programa y mayúsculas del original. Cursiva: voces TV/radio o fuera de pantalla, títulos, letras, otro idioma. Números: letras 0-10, arábigos el resto. Paréntesis mejor que corchetes.
- (Univ. Burgos, p.5) Colores por legibilidad: 1 amarillo/negro, 2 verde/negro, 3 cian/negro, 4 magenta/negro, 5 blanco/negro, 6 rojo/blanco, 7 azul/blanco, 8 azul/amarillo; mismo orden para personajes; prioridad color>etiqueta>guion (guion sólo si riesgo de confusión, pp. 6-7).
- (oficio) Subtítulo que cruza un corte de plano se nota: partir en el corte si se puede.

## 6. Transiciones

- (Adobe) Corte=por defecto, último cuadro de un clip seguido del primero del siguiente. Transición=efecto que crea enlace animado. (Blackmagic) Indica cambio de tiempo/lugar. (oficio) No se pone por adorno.
- (oficio) Corrientes: fundido encadenado (paso de tiempo/secuencia), a/desde negro (cierre/apertura), cortinilla (separadores/deportes/promos, casi nunca noticia), cruzado de audio (evitar golpe).
- (Resolve) 6 estilos de encadenado; Video=disolución lineal; Film=logarítmica (óptica de cine); otros 4: aditivo (aclara a mitad), sustractivo (oscurece a mitad), altas luces, sombras.
- (oficio) Colas (handles)=cuadros fuera del montaje, necesarios para la transición. (Resolve) Sin colas suficientes: Trim Clips (recorta)/Skip Clips (no añade)/Cancel.
- (Adobe) Recortar antes de aplicar transición; 15 cuadros/lado para centrada de 1:00. (cálculo) A 25 fps, 1 s centrado=12-13 cuadros/lado; 2 s=25.
- (Resolve) Duración por defecto 1/4, 1/2, 1, 2 s. Alineación Start/Center/End on Edit. Suavizado (Ease). Set as Standard Transition; (oficio) suele ir en la plantilla del programa.

## 7. Limpieza de audio

- (oficio) Limpiar=quitar lo que sobra sin tocar lo que sirve. Informativo: la cierra el montador; programa grande, sonido (tema 9). Lo no grabado no se limpia; limpieza fuerte deja huella.
- (oficio) Defecto→herramienta: ruido constante→reducción por perfil; zumbido de red→ranura en fundamental+armónicos o reductor de zumbido; chasquidos→reductor/edición de muestra; recorte→reconstrucción de onda (grave=sin arreglo); oclusivas→paso alto/reductor; sibilantes→de-esser; viento/roces→paso alto/reductores/edición; reverberación→reductor con límites. (iZotope RX 11, nombres, no norma) De-click, De-clip, De-crackle, De-ess, De-hum, De-plosive, De-reverb, De-rustle, De-wind, Spectral De-noise.
- (Resolve, Fairlight FX) Noise Reduction: De-Hiss/De-Rumble/ambos. De-Hummer: 50/60 Hz+armónicos. De-Esser: 5-8 kHz. Dialogue Leveler: sube flojas, baja fuertes y fondo no-diálogo. Voice Isolation (Studio, IA): 70-80 recomendado.
- (RD 842/2002, art. 4.4) Frecuencia de red España: 50 Hz → zumbido en 50 Hz y armónicos (100, 150, 200…). (Adobe, Essential Sound) Dialogue/Music/SFX/Ambience; diálogo: unifica sonoridad, reduce ruido de fondo, añade compresión y EQ.
- (oficio) Ecualizar, 3 motivos: defecto, voz sobre música, efecto. Campana/peaking (franja central); estantería/shelving (encima/debajo, plano tipo balda); filtro de corte (fuera de banda). Voz: EQ toca poco; sobre música se hace sitio, no se sube volumen.
- (oficio) Filtros: paso alto (graves: retumbar, golpes, viento, proximidad); paso bajo (agudos: siseo); paso banda (teléfono); notch (tono concreto: zumbido). Corte=donde cae −3 dB; pendiente dB/octava según orden. (Rane) Cada orden suma 6 dB/octava (20 dB/década): 1º 6; 2º 12; 3º 18; 4º 24 dB/oct (80 dB/década).
- (oficio) Rumble=ruido bajo de giradiscos. Notch=Q altísimo, franja estrecha, filtro del zumbido. Paso alto: primer proceso casi siempre en la voz.
- (iZotope RX 11) Spectral De-noise: aprende perfil y lo resta; útil hiss, HVAC, exterior, línea, ground loops, motores, ventiladores, viento, zumbido complejo. Trozo sólo de ruido; perfil manual=constante; adaptativo=cambiante (tráfico, olas); umbral alto=más reducción y más señal suprimida; reducción distinta tonal/aleatoria.
- (Resolve, Fairlight) Umbral según SNR, más alto si peor SNR. Sensibilidad alta exagera perfil: más ruido fuera, más diálogo afectado. Listen to Noise Only: comprueba qué se quita.
- (iZotope/Resolve) Sustracción fuerte→ruido musical "chirpy"/"watery"; puerta de banda ancha→ráfagas al caer bajo umbral; Artifact Control regula. (oficio) Reducir poco en varias pasadas; escuchar lo quitado; comparar a igual nivel.
- (oficio) Ducking: pista que manda controla ganancia de la que cede. Puerta de ruido cierra bajo umbral (distinto del ducker). (Rane) Ducker=al revés de la puerta: atenúa cuando el control (side-chain) supera umbral. Attack: rapidez de reducción. Hold: duración agachado tras caer bajo umbral. Profundidad: 0 a −80 dB.
- (oficio) TV: música por camino principal, voz por side-chain; baja al hablar, sube al callar. (Blackmagic) Sin comprimir; un ducker toma varias pistas de diálogo. Dialogue Leveler: iguala la voz consigo misma, sin "pumping". Mal ajustado: retorno rápido→música "respira". Alternativa manual (pieza corta): línea de volumen con puntos antes/después de la voz.
- (Libro de Estilo, 9.2.12.4) Música: aditamento impropio en informativos diarios; en extensos, con matices.
- (oficio) Orden diálogo: 1) edición, 2) paso alto, 3) zumbido, 4) reducción suave, 5) sibilantes/oclusivas, 6) EQ y compresión de mezcla; relleno de ambiente donde se corta.
- (EBU R 128-2023 v5) h) −23,0 LUFS objetivo; ±1,0 LU si no viable (directo). i) ±0,2 LU tolerancia de medida. m) pico ≤−1 dBTP en producción, tolerancia ±0,3 dB. k) medidor UIT-R BS.1770/Tech 3341. n) LRA según Tech 3342, no recomendado <1 min. l) se mide entero; "programa" incluye publicidad, promos, interstitials.
- (EBU Tech 3343-2023 v4, § 3.2-3.3) Postproducción: ±0,2 LU (vs. ±1 LU en directo); corrección con ganancia estática fija; medidores offline miden y corrigen a la vez.
- (cálculo) X dB de ganancia mueve X LU y X dB de pico. Ej.: −21,4 LUFS/−2,5 dBTP, −1,6 dB→−23,0/−4,1 (cumple). Ej.: −24,5 LUFS/−1,8 dBTP, +1,5 dB→−23,0 pero −0,3 dBTP (no cumple); limitar antes y remedir.

## Aplicación práctica: postproducción de una noticia

- (oficio) 1) Color: primaria con scopes, dominante en gain/matiz, igualar contra referencia. 2) Efectos: tramar cara de menor si riesgo (9.9); nada de cámara lenta/congelado para dramatizar. 3) Grafismo: rótulo en zona de título; gráfico ≤5 elementos, ≥8 s, cama de audio; blanco al 75 % si HLG. 4) Subtítulos: incrustado si no se entiende, ≤37 car/línea, ~15 car/s. 5) Transiciones: cortes; fundido corto sólo con salto de tiempo y colas suficientes. 6) Audio: paso alto, de-hum 50 Hz, reducción suave, relleno de ambiente, ducking sin que "respire". 7) Entrega: −23 LUFS ±0,2 LU, pico ≤−1 dBTP; limitar si hace falta antes de render/exportación (tema 3).

## Lo que este tema no da, y dónde está

- Sistema de edición, corrector de color, plantillas de grafismo y formatos de entrega de CSRTV; si el rótulo se incrusta en sala o en emisión: no consta.
- UNE 153010:2012: no leída (síntesis Univ. Burgos). After Effects/Photoshop: no consultados. Zonas de seguridad UER/SMPTE: no leídas (valores=defecto Resolve). Histograma/CIE: no desarrollados. BT.2408-9 sobre SDR-HDR y LUT en HDR: sólo títulos.
- Señal/colorimetría/niveles/HDR/sonoridad: tema 2. Render/conformado/exportación: tema 3. Formatos/códecs/IMF: tema 4. Narrativa corte/fundido/elipsis, imágenes duras: tema 1. Coordinación grafismo/sonido, Libro de Estilo de gráficos, circuito de rótulos: tema 9. Subtitulado/audiodescripción/lectura fácil: tema 11. Verticales/redes: tema 12. Plantillas/automatización: tema 13. Derechos de música/terceros: tema 10.
