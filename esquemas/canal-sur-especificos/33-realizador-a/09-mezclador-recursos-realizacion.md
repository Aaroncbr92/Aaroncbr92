# Tema 9 del específico de Realizador/a · Mezclador de vídeo y recursos de realización: transiciones, efectos, incrustaciones, chroma, DVE, multipantalla, macros, señales, keyers, grafismo en directo y criterios de uso narrativo

**Siglas**: RTVA · CSRTV · RD · RA · LE (*Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA 2004) · ATEM (manual Blackmagic, dic. 2024) · M/E · DVE (DME) · USK/DSK · PinP · FAM/NAM · PVW/PGM · FTB · fr · AFV

Esqueleto para repasar, no resumen: la fuente delante de cada línea; el detalle, en el tema.

<!-- indice -->

- [1. Transiciones](#1-transiciones)
- [2. Efectos](#2-efectos)
- [3. Incrustaciones](#3-incrustaciones)
- [4. Chroma](#4-chroma)
- [5. DVE](#5-dve)
- [6. Multipantalla](#6-multipantalla)
- [7. Macros](#7-macros)
- [8. Señales](#8-señales)
- [9. Keyers](#9-keyers)
- [10. Grafismo en directo](#10-grafismo-en-directo)
- [11. Criterios de uso narrativo](#11-criterios-de-uso-narrativo)

<!-- /indice -->

## 1. Transiciones

- Sin norma del mezclador; ATEM única doc. de fabricante; mezclador CSRTV no consta. Oficio: conmutar, mezclar, combinar.
- RD 1680/2011 mód. 0905 RA 5 (crit. c entradas a buses; e «ajustado y prefijado» transiciones, cortinillas, efectos, croma/luminancia/DSK); contenidos: transiciones «usos expresivos y narrativos», montaje en vivo, incrustación, gráficos. Mód. 0910 RA 4 b: evaluar mezcladores.
- M/E = mezclador dentro del mezclador (PGM, PVW, transición, llaves); no son M/E bus de llave, previo ni DSK (ATEM: para evitar errores en directo).
- Modos: CUT; MIX (encadenado, sin borde); WIPE (borde con forma); fundido a color (DIP; SÚPER MIX si blanco); NAM (la más brillante); FAM (suma luminancias, 100 % a mitad, destello); DVE wipe.
- ATEM: cinco tipos (MIX, DIP, WIPE, DVE, STING) según modelo; fundido = fuente intermedia (blanco, logo patrocinador).
- ATEM cortinilla: forma; fuente del borde (cualquiera); simetría (círculo a elipse); posición; invertir dirección (bordes al centro); alternar; ancho; atenuación (definición); con gráficos: pancarta ≤16 % del ancho.
- ATEM: CUT inmediata, sea cual sea el tipo; AUTO según duración; palanca alternativa manual (oficio: ritmo de plató o música). Duración independiente por transición, guardada (fr).
- ATEM próxima transición: BKGD, KEY 1-4; sólo superpuestos posible; mirar previo. PREV TRANS ensaya con la palanca.
- ATEM FTB: última etapa, todas las capas; inicio, final, antes de publicidad; no se ve anticipado; sonido con AFV.
- ATEM animada (*stinger*, 1 M/E y 2 M/E): secuencia del reproductor de medios; a pantalla completa, corte o disolvencia del fondo; típica repeticiones deportivas.

## 2. Efectos

- ATEM: composición de imágenes = superponer capas de varias fuentes; visibles según transparencia.
- Oficio: llave (rótulo, mosca, presentador); llave de figura; DVE; varios DVE o SuperSource; transición; generadores de color; macro o *timeline*.
- ATEM generadores de color: tono, saturación, luminancia (fondo, fundido, borde).
- ATEM llave de figura: canal alfa generado por el mezclador, 18 formas; no gasta DVE (oficio).
- RD mód. 0905 RA 5 e: se prepara antes; oficio: probar en previo, guardar en memoria.

## 3. Incrustaciones

- Tres señales: fondo, relleno (*fill*), llave (*key*/alfa, máscara en grises); ATEM lineal: primer plano + alfa.
- Fórmula: salida = relleno × llave + fondo × (1 − llave); 1 relleno, 0 fondo, intermedio mezcla.
- Lineal: relleno atenuado por la llave; con 0 no aparece. Aditiva: salida = relleno + fondo × (1 − llave); todo lo que tenga señal el relleno se ve. Llave que no cubre parte del relleno: no aditiva. Alfa acoplado: decide la llave, no el brillo.
- Clip (nivel, *threshold*): gris donde recorta; ganancia: pendiente, dureza del borde. ATEM Nivel: sube si el fondo sale negro; Ganancia atenúa borde.
- ATEM máscara rectangular: Superior, Inferior, Izquierda, Derecha; quita bordes ásperos. Croma (oficio): tapa focos y bordes sin tocar ajustes.
- Premultiplicada: relleno ya × llave (bordes atenuados, fondo negro); no es recuadre. ATEM «Composición precompuesta»; sin declarar, doble multiplicación, bordes oscuros; si no, Recorte y Ganancia.

## 4. Chroma

- ATEM: uso principal el tiempo; elimina un color del primer plano; inserción cromática, pantalla azul o verde; llave del primer plano.
- Cualquier color sirve: color de referencia y tolerancia. Verde y azul: ausentes en la piel; verde más resolución (doble de fotositos, oficio); azul si vestuario verde. «Sólo verde» = costumbre hecha regla.
- ATEM sin croma avanzado: Matiz; ganancia; límite de luminancia; espectro limitado; barras y vectorscopio.
- ATEM croma avanzado: muestra de área con mayor rango de luminancia (por defecto si bien iluminado). Primer plano (rellena transparencias); Fondo (artefactos); Borde (cabello); Rebase (tinte en contorno); Reflejo (tonalidad general); Ajustes cromáticos.
- ATEM rebase o reflejo: luz rebotada en el verde; máscara en ventana del multipantalla.
- Oficio: fondo uniforme; sin ropa del color del fondo; submuestreo fuerte peor que 4:2:2 o 4:4:4 (tema 14).
- LE 8.6.1 (p. 122): p. 4 «Los colores fuertes tampoco son aconsejables. Se saturan e impregnan de ‘croma’ el cuello y el mentón.»; p. 9 Estilismo y Realización **«deberán»** tener en cuenta cromas, transparencias, decorado virtual.
- Oficio directo: mezclador o plató virtual en tiempo real; motor de render devuelve señal montada; mezclador sin croma puede usar decorado virtual; sincronía siempre; croma es clase de llave. RD mód. 0910 RA 4 g: escenografía virtual y cámaras/mezclador. Tema 12.

## 5. DVE

- ATEM: imagen pequeña en recuadro con bordes; giro, bordes 3D, sombras.
- Parámetros: traslación X Y Z (Z acerca/aleja); tamaño X Y Z; rotación X Y Z; aspecto (deforma); recorte (4 lados); perspectiva; bordes (anchura, color, sombra); esquinas (*corner pinning*).
- *Corner pinning*: cuatro esquinas a las de la pantalla en escena. Ampliar sin deformar: eje Z; aspecto deforma; rotación gira; tamaño sólo con X = Y.
- PinP: DVE que reduce y coloca; no es mosaico (pixela) ni multi-imagen (partes iguales).
- Gafa (plató, no normalizado): 50/50; 20/60/20; tantos DVE como ventanas o generador múltiple. ATEM SuperSource (más de un M/E): usa una entrada; formato predeterminado; posición, tamaño, recorte; fuente al aire, no monitor (oficio). Narrativa: dos personas en distinto sitio.

## 6. Multipantalla

- RD mód. 0905 RA 6 b: configuración idónea; contenido «Monitorizado en sistemas multipantalla».
- ATEM: ocho ventanas pequeñas; Constellation 8K 4, 7, 10, 13 o 16 fuentes.
- ATEM bordes: rojo = principal (al aire); verde = anticipo; blanco = ninguno. Marcadores de zona segura en previo (16:9 u 9:16); vúmetros (Activados); nombres de fuente; cualquier señal interna (máscara de llave, salida de banco).
- Oficio: cámaras en orden de uso; vídeos, gráficos y exteriores junto a ellas; ventana de máscara; verde antes de la transición, rojo después. Tema 4.

## 7. Macros

- Snapshot = estado en un instante (fotografía); macro = instrucciones con tiempos por botón (película); timeline = estados sobre línea de tiempo (efectos largos y precisos); shotbox = teclado de disparo.
- ATEM macro: transiciones, superpuestas, volumen, cámaras; se graba con Software Control, Advanced Panel o ambos; se almacena en el mezclador; 100 espacios; crear/ejecutar en directo. No es aparato ni objetivo macro.
- Oficio: macro = pausa en fr y snapshot dentro (ej. pausa de 15 fr, MIX de programa, llave 1 a apagado); memoria de llave = parámetros.
- Efecto programado no se retoca en marcha: *timeline* lanzado se cancela o se espera; DVE suelto sí; macro y *timeline* se editan parados.
- *Clip store*: memoria de clips y fijas (cabeceras, ráfagas, cortinillas animadas, grafismos); cada clip = fuente; alfa cargado solo (ATEM); corto, largo a servidor; botón o macro.
- Oficio ej.: cabecera, animada al general, mosca en posterior, presentador en previo; ensayada fuera de aire.

## 8. Señales

- Atributos de fuente: nombre largo y corto; llave asociada (*autoselect*); retardo; corrección de color; grupo de *tally*; botón.
- ATEM nombres: corto 4 caracteres, largo hasta 20 (el manual se contradice en otro pasaje); ej. CAM1.
- RD mód. 0905 RA 5 c: cámaras, servidores, exteriores, titulador (relleno + llave), internas (color, barras, *clip store*, salidas de bancos).
- Black burst: negro con sincronismos y salva de color; convencional, sirve en HD. Tri-level: tres niveles; HD y UHD; más precisa. Generador de sincronismos; *genlock* = engancharse. Fuera de fase: sincronizador de cuadro, retrasa cuadros, de ahí el retardo. Temas 4 y 11.
- Limpia = programa sin llaves posteriores. ATEM: limpia 1 sin superpuestos; limpia 2 con DSK 1, sin DSK 2.
- RD mód. 0905 RA 1 f: grabar master, señal sin incrustaciones, cámaras dobladas o masterizadas. Oficio: sin incrustaciones rehace rótulos.
- ATEM: alfa por auxiliar, fondo verde + alfa «útil… composiciones por crominancia en posproducción».

## 9. Keyers

- Luminancia: brillo del relleno, oscuro transparente (ATEM: misma señal para alfa y primer plano). Lineal: llave separada, mayor calidad. Crominancia: verde o azul. Figura: forma geométrica. DVE key: ventanas móviles, PinP.
- Aditiva = modo de combinar, no tipo. *Coring* NO es llave: reducción de ruido, sin máscara.
- *Self key*: relleno = llave, = luminancia; claro sobre negro; falla con medios tonos opacos; tres señales.
- *Show key*: llave sola en blanco y negro; no es previsualizar el compuesto.
- ATEM: M/E cuatro botones (lineal, precompuesta, geométrica, croma, luminancia, DVE); DSK dos (lineal o luminancia); paneles «Composición previa» y «posterior».
- USK: dentro de M/E, en limpia, imagen (presentador croma, ventana). DSK: tras programa, no en limpia (limpia 2 lleva DSK 1): mosca, rótulos, créditos. Cadena: M/E → programa → DSK 1, 2 → FTB.
- ATEM DSK: TIE vincula a la transición siguiente; ON AIR instantáneo; AUTO propio sólo capas posteriores; con TIE la limpia no cambia.

## 10. Grafismo en directo

- Caminos (oficio): titulador (relleno + llave, lineal, DSK); *clip store*; plató virtual o RA (se conmuta).
- RD mód. 0905 RA 6 d: opciones gráficas del titulador, incrustación comprobada; e: rótulos y claquetas, almacenamiento, salida al mezclador.
- Oficio: mosca y rótulos en posterior (fijos, fuera de limpia); ventana de datos en previa; corte, mezcla o AUTO; TIE; prioridad.
- Zona segura: tema 12; titulador: tema 4.
- LE 3.16 (p. 57): ≤4 o 5 elementos, mínimo recomendable 8 s. LE 3.16.1 (pp. 57-58): dinámico, en paralelo a la locución, «referencial». LE 3.16.2 (p. 58): «cama» de audio salvo sonido propio. LE p. 58: claridad y precisión. LE 3.6.1 (p. 50): rótulo = información, brevedad, impacto y síntesis.

## 11. Criterios de uso narrativo

- Adobe (Premiere, 07-01-2026): corte por defecto; transición = enlace animado. Blackmagic (*Resolve 21*, cap. 55, p. 1194): cambio de tiempo o lugar. Oficio: no por adorno.
- Mateu Torres (UMH 2024, 3.2): fundido (p. 37) elipsis, *fade out*, *fade in*; encadenado (p. 38) elíptico; Katz: «el fundido separa las secuencias, mientras que el encadenado y el corte las conectan».
- Oficio: corte continuidad (conversación, deporte); encadenado conecta y marca salto (música, reportaje); fundido a negro separa (bloques, publicidad); blanco = destello, patrocinio (ATEM); cortinilla = separadores, sumarios, no dentro de noticia; animada = firma (repeticiones); gafa = simultaneidad; croma = explicación; rótulo = identificación. El corte no se nota; lo que se nota debe significar.
- LE 6.5.1 (p. 93): forma supeditada al mensaje; información (editor) sobre técnica (realizador) si imperfecciones moderadas; «espectacularización» (conexiones, satélites, «vidi wall», plasma) con sentido estético; realizador decide, ceñido a producción y sentido informativo. LE 6.5.2 (p. 93): eficacia, accesibilidad, claridad. LE 3.10 (p. 53): cierres, variantes (vidiwall, croma). LE 9.9.2 (p. 167): ralentización o congelado no si acentúan la morbosidad.
- Género (oficio): informativo = corte, rótulo posterior, gafa conexiones; magacín = encadenados, animadas; deportes = repetición animada, marcador posterior; galas = encadenados con palanca; debate = corte a quien habla.
- Práctica: llave pareja; DSK 1 mosca, DSK 2 rótulos; croma con muestra en marca y luz final; snapshot gafa, macros de entrada y salida; encadenado 12 fr a sumarios; FTB final; limpia a grabador. Bordes verdes en pelo: borde o rebase, si no plano sin croma; borde oscuro: premultiplicada sin declarar; *timeline* lanzado: cancelar o esperar.
- Norma: RD 1680/2011 (BOE 302, 16-XII-2011), texto de 2011; RD 500/2024 no toca módulos citados; enseñanza, no RTVA.
- No consta: mezclador CSRTV; identidad gráfica; criterio CSRTV de cortinillas/DVE; otros fabricantes (DME, SÚPER MIX sin contrastar). Remite: temas 1, 4, 6, 11, 12, 13, 14.
- Lecturas: ATEM 03-09-2026, releído 24-09-2026; RD y LE 24-09-2026.
