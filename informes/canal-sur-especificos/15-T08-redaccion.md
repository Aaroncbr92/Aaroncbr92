# Grafista (15) · Tema 8 · Redacción (fase 2)

Tema: `temas/canal-sur-especificos/15-grafista/08-formatos-tecnicos-resolucion-codecs-alfa-zonas-seguras-colorimetria-hdr-entrega.md`
(unas 17.250 palabras con índice; 63 epígrafes). Fecha de trabajo del encargo: 24-09-2026; fecha de
sistema en que se redactó: 29-09-2026.

Estado de partida: los epígrafes 1 (Resolución), 2 (Códecs) y 3 (Alfa), la portada, las siglas y
«Qué se puede preguntar» ya estaban escritos y guardados en el commit 51862c0 (sesión anterior al
reinicio del contenedor), sin informe. Esta sesión los ha releído, ha cotejado su procedencia literal
con un script de comparación párrafo a párrafo (resultado abajo) y ha escrito los epígrafes 4 a 7, la
aplicación práctica, «Normas…», «Lo que este tema no da» y «Trazabilidad», guardando por partes.

Material: `15-investigacion-B-animacion-tiempo-real.md` §§ 8.1-8.4 (y 5.3 para el alfa
premultiplicado). Fuentes releídas por el redactor el 29-09-2026 para lo nuevo del epígrafe 5:
`fuentes/canal-sur/montador/itu/bt709.txt` (BT.709-6, puntos 1.3, 1.4 y 3.2),
`bt2020.txt` (BT.2020-2, tablas 3 y 4 y sus notas), `bt2100.txt` (BT.2100-3, tabla 2 y nota a las
tablas 6 y 7), `bt2408.txt` (BT.2408-9, §§ 5.1 y 9), `fuentes/normas-tecnicas/UIT-R_BT.601-7.txt`
(coeficientes 0,299/0,587/0,114) y `fuentes/normas-tecnicas/SMPTE_ST-2110-20-2022.txt` (desarrollo
de TCS, «Transfer Characteristic System», § 7.6).

Ficheros tocados: sólo el tema y este informe. `indice.py` generó el índice (no toca la portada).
`refutar_prosa.py`: 1 hallazgo, falso positivo (HDR en el título, antes del párrafo de siglas; se
presenta en «Los términos técnicos»). `negritas.py` contra BT.709/2020/2100/2408: todas las citas
nuevas de la UIT aparecen; las «NO ESTÁ» son de fuentes no pasadas a la herramienta (SMPTE ST 2046-1,
EBU, AMWA, fabricantes), que coteja el verificador.

Extensión: 17.250 palabras, muy por encima de los 7.000-12.000 de los demás temas del puesto. El
enunciado reúne siete materias técnicas (resolución, códecs, alfa, zonas seguras, colorimetría,
HDR/SDR, entrega) y la parte ya escrita en la sesión anterior tenía 8.800. Si el coordinador quiere
recortar sin perder datos, lo prescindible es: en el epígrafe 2, las tablas de DNxHD por variante y el
AVC-Intra (poco del grafista); en el 6, «Los metadatos de masterizado» y «Los perfiles de HDR»; y la
cita repetida de la regla TCS de la ST 2110-20 (está en el epígrafe 3 y otra vez en «Cómo se señala el
HDR»).

## Copiado del común

Literal de temas cerrados de Canal Sur (verificación y refutación lo saltan). Abreviaturas: M04 =
`30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`; R14 =
`33-realizador-a/14-formatos-video-resolucion-compresion-hdr-codecs-entregables.md`; R12 =
`33-realizador-a/12-grafismo-rotulacion-ra-decorados-pantallas.md` (cerrado del mismo puesto de
Realizador/a; no estaba en la lista del encargo, pero es la fuente cerrada de la EBU R 95 y del § 9 de
la BT.2408 que la investigación B señala; lo digo para que el coordinador decida). «Ajuste» = sólo
remisión interna reajustada o frase de remisión suprimida; el verificador comprueba que lo demás es
literal.

Epígrafe 1 · Resolución
1. «Resolución y relación de aspecto»: los cinco bloques (definición, tabla, BT.2100 píxel cuadrado,
   UHD ×4, cita de la BT.2020 sobre LSDI). M04/R14.
2. «Producir en alta y entregar en baja»: el párrafo con la nota 1b de la BT.2100-3. R14. (El párrafo
   «Aplicado al grafismo» es nuevo.)
3. «La relación de aspecto y sus arreglos»: desde «La relación de aspecto es la proporción…» hasta la
   lista *letterboxing*/*pillarboxing*. R14.
4. «El HD: la BT.709»: los cinco primeros bloques (hasta «…costumbre de fabricantes»). M04/R14.
5. «Lo que emite Canal Sur»: los dos párrafos del Contrato-programa (puntos 85 y 101). R14.

Epígrafe 2 · Códecs
6. «Qué es un códec y qué se pierde»: entero. M04/R14.
7. «El muestreo cromático»: la tabla de notaciones. M04/R14.
8. «La profundidad de bits y los niveles»: la línea «Lo que admite cada recomendación:». M04/R14.
9. «Los límites de la señal según la EBU»: entero salvo el último párrafo («Para el grafista…», nuevo,
   con las citas de Vizrt de la investigación). R14.
10. «Intracuadro y GOP largo», «H.264 y H.265», «AVC-Intra (Panasonic)», «Cuadro resumen»: enteros.
    M04/R14.
11. «Apple ProRes»: los dos primeros bloques (cita LOC y lista de rasgos). M04/R14.
12. «Avid DNxHD (SMPTE VC-3)»: los cinco primeros bloques. M04/R14.
13. «Los contenedores»: entero salvo el último párrafo («Para el grafista…», nuevo). M04/R14.

Epígrafe 3 · Alfa
14. «Los ficheros gráficos que llevan alfa»: la tabla JPG/PNG/TIF/TGA, el párrafo del JPG y la cuenta
    de los 32 bits del TGA (dos líneas). R12. El párrafo «Los 24 bits…» es de R12 con «(tema 14)»
    suprimido (ajuste).
15. «Los errores de entrega con el alfa», primera viñeta, segunda mitad («Un rótulo, una mosca o un
    logotipo… tapa la imagen»): R12, sin el «(oficio)».

Epígrafe 4 · Zonas seguras
16. «La EBU R 95»: entero (desde «Los rótulos se colocan dentro del cuadro…» hasta «…2592 en
    2160p.»). R12 § «Dónde va: las zonas seguras», sin su último párrafo (del realizador).

Epígrafe 5 · Colorimetría
17. «La gamma»: los dos primeros párrafos (definición y fórmula de la BT.709-6). R14.

Epígrafe 6 · HDR/SDR
18. «Qué es y qué recomendación lo fija»: entero. R14. Ajuste: «(§ 4)» → «(epígrafe 1)».
19. «Los metadatos de masterizado»: entero. M04/R14.
20. «Los perfiles de HDR», segundo párrafo («El manual no usa los rótulos…»): R14. Ajuste: «(oficio,
    sobre las citas de la tabla)» → «(oficio, sobre las citas del manual)», porque la tabla de R14 no se
    copió. El primer párrafo es un resumen nuevo con citas de R14 (se verifica).
21. «Cómo se señala el HDR»: entero. R14. Ajuste: «ST 2110-20 (tema 15):» → «ST 2110-20 (la misma norma
    que declara la señal de llave, epígrafe 3):».
22. «Los niveles del HDR»: entero. M04/R14.
23. «Mezclar SDR y HDR: las conversiones»: entero. M04/R14.
24. «El grafismo en HDR», primer párrafo: R12 § «El grafismo en alto rango dinámico», segundo párrafo.
    Ajuste: «Y el porqué, en el apartado de grafismo:» → «Por qué el rótulo va al blanco del grafismo y
    no al 100 % lo explica el Informe UIT-R BT.2408-9 en su apartado de grafismo:» (sin antecedente al
    cambiar de sitio).

Epígrafe 7 · Entrega para emisión
25. «Qué es un estándar de entrega»: el primer párrafo. R14 (M04 lo tiene igual).
26. «El MXF como base»: entero. R14. Ajuste: «citada en el § 7» → «citada en el epígrafe 2».
27. «AMWA AS-11»: entero. M04/R14.
28. «El control de calidad de cada entregable»: entero. R14. Ajustes: «(los límites de la R 103, § 3)»
    → «(… epígrafe 2)»; suprimido «(el tema 13 da la guía de la UIT)»; «(§ 2)» → «(epígrafe 1)»; «Algunos
    que tocan a lo que decide el realizador» → «Algunos que tocan a una pieza gráfica»; la última frase
    («La revisión de calidad final como procedimiento de la postproducción es el tema 13; aquí interesa
    que cada entregable tiene la suya.») → «Cada entregable tiene la suya, también la pieza gráfica
    (oficio).».
29. «La sonoridad de entrega: EBU R 128»: entero salvo la frase final «La mezcla y la revisión final, en
    el tema 13.», suprimida. M04/R14.
30. «Versiones para plataformas», primera frase («Una misma pieza sale a menudo…»). R14.

## Copiado de RTVE sin cambios

Fila 15-8 de `informes/canal-sur-reuso/*.tsv`: actualizar = «no». Pasajes cuyas palabras son las de
RTVE; la única intervención es quitar la negrita de énfasis de RTVE (aquí negrita = literal de fuente)
y los acentos graves de código (`PNG` → PNG). El verificador comprueba sólo que es literal.

- `diseno-grafico/02`, § 2: «Y el aviso de oficio que se deriva, porque es trabajo diario del
  grafista: cuando se mezcla material de 1.85…» (epígrafe 1, «La relación de aspecto y sus arreglos»).
- `diseno-grafico/02`, § 4: la tabla «Zona segura de acción / de títulos» y el párrafo «Por qué siguen
  existiendo si hoy las pantallas no recortan…» (epígrafe 4, primer subepígrafe).
- `diseno-grafico/10`, § 5: el cuadro completo de formatos (PSD…EPS) y «La regla que este cuadro deja
  para el examen…» (epígrafe 3).
- `diseno-grafico/10`, § 2: «Cian, magenta, amarillo y negro es el modelo de la tinta; rojo, verde y
  azul, el de la pantalla. Un formato pensado para la web no necesita el de la tinta, y por eso no lo
  lleva» (epígrafe 5; mayúscula inicial añadida).
- `diseno-grafico/11`, § 2: la tabla de valores del canal alfa y el párrafo «Por qué los grises son lo
  importante…» (epígrafe 3); y la frase «un grafismo entregado en un formato sin alfa llega al control
  con un fondo negro pegado. Es el error de entrega más frecuente, y no se ve hasta que el rótulo entra
  en emisión» (epígrafe 3, errores de entrega).
- `edicion-montaje/02`: § 1, «El ojo humano tiene tres tipos de conos…» y la frase de la primera ley de
  Grassmann (sin «Ésa es la respuesta oficial…»); § 3, «La televisión no transmite rojo, verde y azul…»,
  «La luminancia se construye pesando…» y la tabla de coeficientes BT.601/709/2020; § 4, la tabla
  CL/NCL; § 8, la tabla de tipos de LUT (epígrafe 5).

## Adaptado de RTVE (se verifica)

- Epígrafe 3, «Qué es el canal alfa», primer párrafo (de `diseno-grafico/11` § 2, fundidas dos frases).
- Epígrafe 5, «La luminancia constante y no constante», última frase (de `edicion-montaje/02` § 4,
  reescrita como consecuencia y marcada oficio); «Las LUT», primer párrafo (de § 8, fundido).
- Epígrafe 2, los párrafos del muestreo y de la profundidad de bits que no casan en el cotejo proceden
  de la sesión anterior y mezclan RTVE (`edicion-montaje/02` § 6, `diseno-grafico/02` § 4) con texto
  nuevo: se verifican enteros.

## Lo nuevo que el verificador debe cotejar

- Epígrafe 4: todo lo de la SMPTE ST 2046-1 (investigación B § 8.1; el PDF no está en el repositorio:
  https://pub.smpte.org/doc/st2046-1/20091123-pub/st2046-1-2009.pdf), la comparación EBU/SMPTE y las
  cuentas (1.280 × 720 al 90 % = 1.152 × 648, márgenes 64 y 36).
- Epígrafe 5: primarios y blanco (BT.709-6 §§ 1.3-1.4; BT.2020-2 tabla 3; BT.2100-3 tabla 2 con 630,
  532 y 467 nm); coeficientes (BT.709-6 § 3.2; BT.2020-2 tabla 4; BT.601-7); notas de la tabla 4 de la
  BT.2020-2 sobre CL y NCL; la frase de la BT.2100-3 sobre NCL por defecto; BT.2408-9 § 5.1 («may be
  placed in a BT.2020 container») y § 9 (imagen fija, CICP, rango completo y estrecho); la
  presentación de CICP como UIT-T H.273.
- Epígrafe 3 (sesión anterior): ProRes 4444 (Apple, 2022), alfa directo/premultiplicado (Resolve 21
  cap. 77; Blender 5.2), Vizrt (relleno, llave, Downscale Luma, Allow Super White…), ATEM (de R12).
- Epígrafe 7 y aplicación práctica: todo oficio salvo lo copiado; ítem 0021B citado de R14.

## Preguntas tipo test (comprobación de cobertura)

Diez preguntas repartidas por las siete rúbricas del enunciado, con teoría y aplicación práctica. Todas
se contestan enteras con el tema; no hizo falta ampliar.

1. (Resolución) Desde el 14 de febrero de 2024, el único sistema técnico de difusión de Canal Sur por
   TDT es: a) SD; b) HD ✔; c) UHD 4K; d) HD y UHD simultáneos. — Epígrafe 1, «Lo que emite Canal Sur»
   (Contrato-programa, punto 85). Entera.
2. (Códecs) Para un material que se va a editar y componer mucho conviene: a) GOP largo H.265; b)
   intracuadro ✔; c) 4:2:0 a 8 bits; d) tasa constante de distribución. — Epígrafe 2, «Intracuadro y
   GOP largo». Entera.
3. (Alfa) ¿Qué códecs de la familia ProRes admiten canal alfa? a) todos; b) 422 HQ y 4444; c) sólo
   4444 XQ; d) 4444 y 4444 XQ ✔. — Epígrafe 3, cita de Apple. Entera.
4. (Alfa, práctica) Un render 3D compuesto sobre vídeo muestra un halo claro en el borde. La causa más
   probable: a) falta de zona segura; b) tratar como premultiplicada una imagen que no lo está ✔; c)
   rango estrecho; d) submuestreo 4:2:2. — Epígrafe 3, «Alfa directo y alfa premultiplicado» (Resolve
   21, p. 1727; el tema da el caso y el halo). Entera.
5. (Zonas seguras) Según la SMPTE ST 2046-1, la Safe Title Area de un formato 1920 × 1080 mide: a) 1786
   × 1004; b) 1728 × 972 ✔; c) 1536 × 864; d) 1920 × 1004. — Epígrafe 4. Entera.
6. (Zonas seguras, práctica) En una pieza 3.840 × 2.160, el margen lateral de la zona segura de grafismo
   de la EBU R 95 es de: a) 96 píxeles; b) 134; c) 192 ✔; d) 268. — Epígrafe 4, tabla de la R 95 y
   «Cuentas que se piden». Entera.
7. (Colorimetría) La señal de luminancia de la BT.709 es: a) 0,299 R + 0,587 G + 0,114 B; b) 0,2126 R +
   0,7152 G + 0,0722 B ✔; c) 0,2627 R + 0,6780 G + 0,0593 B; d) 0,333 R + 0,333 G + 0,333 B. — Epígrafe
   5. Entera.
8. (Colorimetría / niveles) En la EBU R 103, el rango nominal de vídeo a 10 bits es: a) 0-1023; b) 4-1019;
   c) 20-984; d) 64-940 ✔. — Epígrafe 2, «Los límites de la señal según la EBU». Entera.
9. (HDR/SDR) Según el Informe UIT-R BT.2408-9, el blanco de un grafismo insertado en una señal HLG va
   al: a) 100 %; b) 75 % ✔; c) 58 %; d) 50 %. — Epígrafe 6, «Los niveles del HDR» y «El grafismo en
   HDR». Entera.
10. (Entrega) AMWA AS-11 es: a) un códec intracuadro; b) una familia de especificaciones de ficheros
    basados en MXF, restringidos, para entregar programas terminados a un difusor ✔; c) la norma de
    sonoridad de la EBU; d) un patrón operacional de MXF. — Epígrafe 7. Entera.
