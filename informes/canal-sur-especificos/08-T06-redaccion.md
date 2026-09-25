# Puesto 08 · Tema 6 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/06-captacion-de-sonido.md`.
Se escribe por partes, guardando cada epígrafe.

## Fuentes leídas (todas el 24-09-2026)

- `08-investigacion-C-sonido-formatos.md` § Tema 6 y «Lo que no se pudo confirmar».
- RTVE: `temas/informacion-grafica/06-el-sonido-en-eng.md`, `temas/montaje-equipos/06-sonido-microfonos-y-altavoces.md`.
- Citas releídas por mí en su fuente antes de escribirlas: EBU R 68-2000 (18 dB, 1:8, 9/8 dB, 15 dB),
  EBU R 128-2023 (h, i, m), EBU Tech 3343-2023 (§8.1, «crowd noise», §3.5.1 deportes), Sony PXW-Z200
  Help Guide (pp. 13, 16, 99, 136-139, 260-261, 297-298, 336-338), *Libro de estilo de Canal Sur* 2004
  (3.2.2, 3.17.1, 3.17.1.3, 5.3.3, p. 82, 5.4, 6.4, 8.3.2, 8.6.1).

## Progreso
- Epígrafes 1 (Captación: por qué, magnitudes, frecuencias, transductores, cadena) y 2 (Microfonía) guardados.
- Epígrafe 3 (Niveles) guardado.
- Epígrafe 4 (Sincronía) guardado.
- Epígrafe 5 (Ambiente) guardado.
- Epígrafe 6 (Criterios básicos), recomendaciones, huecos y trazabilidad guardados.
- Índice generado con `indice.py` (43 epígrafes; ≈9.300 palabras según la herramienta, 9.757 con `wc`).
  `refutar_prosa.py`: 0 de relleno, 0 repeticiones; siglas: ITU (presentada ahora junto a UIT-R) y PXW
  (código de producto de Sony, no sigla: sin cambio). Sin normas jurídicas: no proceden las lentes de norma.

## Estructura

Seis `##` de cuerpo en el orden del enunciado: introducción (Captación de sonido asociada a cámara),
Microfonía, Niveles, Sincronía, Ambiente, Criterios básicos; después recomendaciones citadas, «Lo que
este tema no da» y «Trazabilidad».

## Copiado del común

- Ninguno. El enunciado no pide ninguna norma que desarrolle `temas/canal-sur-comun/`.

## Copiado de RTVE (a verificar: adaptado, no literal)

Literal en lo sustancial, quitado lo propio de RTVE (números de pregunta, «respuesta oficial», tabla
«Los datos que el examen ha preguntado», avisos de cuadernillo, negritas de énfasis, que en este
proyecto sólo marcan literal de fuente). Por eso no va en «Copiado de RTVE sin cambios»: el
verificador debe comprobar lo adaptado.
- `informacion-grafica/06`: §1 → «Por qué el sonido es del operador de cámara»; §2 → «El margen de
  frecuencias audibles»; §3 → «Los transductores» (fusionado con montaje-equipos §2); §4 → «El margen
  dinámico»; §5 → «Los patrones polares»; §6 → «Los inalámbricos y los grupos de frecuencia»; §7 →
  «Dos inalámbricos en la misma cámara»; §8 → «La cámara fotográfica y el sonido aparte» y «La
  claqueta».
- `montaje-equipos/06`: §1 → «El sonido y sus magnitudes»; §3 → «Los patrones polares»
  (omnidireccional, bidireccional, direccional con ambiente); §4 → «Los micrófonos por su transductor»
  y «por su forma y su uso»; §5 → «Los soportes, el viento y el roce». Se dejó fuera altavoces y
  bafles, sonómetro y sonorización envolvente (no los pide el enunciado).

## Nuevo (de la investigación C y de lecturas propias)

- EBU R 68, R 128, Tech 3341, Tech 3343; Sony Z200 (conmutador de entrada, AUTO/MAN, menú de audio,
  cuatro canales, código de tiempo, bits de usuario, cámara lenta sin audio): de la investigación C,
  releídos en su fuente.
- Añadido por mí, releído en su fuente: Z200 especificaciones de audio (LPCM 24 bit 48 kHz 4 canales,
  p. 336; respuesta 20 Hz-20 kHz y margen dinámico 80/90 dB, p. 337; XLR hembra, minijack INPUT3,
  micrófono interno electret omnidireccional estéreo, referencia de micro −30 a −80 dBu, p. 338);
  Tech 3343 § 3.5.1 (comentaristas a −24 LUFS); Libro de estilo 3.2.2, 3.17.1, 3.17.1.3, 5.3.3,
  p. 82 (barras y revisión en el sitio), 5.4, 6.4, 8.3.2, 8.6.1; AES14 (sólo el nombre, de
  `fuentes/normas-tecnicas/AES-normas-de-audio.md`).

## Discrepancia con la investigación (manda la fuente)

- La investigación C (§ 6.5) dice que **no consta documento publicado de CSRTV sobre asignación de
  pistas en ENG**. Sí consta: el *Libro de estilo* de 2004, epígrafe 5.4 (p. 82), fija canal 1 para
  declaraciones, ruedas de prensa y periodista, y canal 2 para el ambiente del micrófono de cámara
  (lo cita también el tema 3 cerrado). El tema lo usa; sólo los canales 3 y 4 quedan como hueco.
- La Z200 tiene ***[CH1&2 AGC Mode]*** de fábrica en ***[Stereo]*** (p. 261); la investigación no
  daba el valor de fábrica. Añadido.

## Para el verificador

- Página exacta de 3.2.2 (índice: la sección empieza en p. 46) y de 8.6.1 (índice: p. 122): no
  puestas en el tema.
- La lista «LINE/MIC/MIC+48V» con dos puntos está en la descripción de partes del Z200 (entre las
  pp. 13 y 14 del PDF; la marca de página no es inequívoca en el `.txt`): el tema no da página y
  remite a p. 136, donde está la misma tabla.
- Oficio declarado como tal: colocación del corbata, procedimiento de nivel, lista de comprobación,
  errores típicos, claqueta, re-sincronización periódica, 3,5 mm de la entrada de consumo,
  retardo en directo.

## Otros ficheros tocados

Sólo el tema 6 (nuevo) y este informe.

## Preguntas tipo test de comprobación (contestadas sólo con el tema)

1. (Microfonía, teoría) Un micrófono de condensador sin pila, conectado por XLR a la cámara, necesita
   el conmutador en: a) LINE; b) MIC; c) MIC+48V; d) cualquiera. → c. «Los micrófonos por su
   transductor». **Entera.**
2. (Microfonía, teoría) El micrófono de corbata suele ser: a) bidireccional; b) omnidireccional;
   c) hipercardioide; d) cañón. → b. «Los patrones polares» y «por su forma y su uso». **Entera.**
3. (Microfonía, práctica) Dos inalámbricos de corbata a la vez en una cámara, sin interferencias:
   a) en grupos distintos; b) en el mismo grupo, cada emisor con su receptor/canal; c) los dos al mismo
   receptor; d) el grupo más bajo y el más alto. → b. «Los inalámbricos…» y «Dos inalámbricos…».
   **Entera.**
4. (Niveles, teoría) Según la EBU R 68, el nivel de alineación digital es: a) 0 dBFS; b) −9 dBFS;
   c) −18 dBFS; d) −23 dBFS. → c (18 dB bajo el máximo, 1:8). «El nivel de alineación». **Entera.**
5. (Niveles, teoría) La EBU R 128 fija para el programa: a) −18 LUFS; b) −23 LUFS, ±1 LU en
   directo; c) −23 dBFS de pico; d) −24 LUFS siempre. → b. «La sonoridad: EBU R 128». **Entera.**
6. (Niveles, teoría) El pico verdadero máximo en producción según R 128 es: a) 0 dBFS; b) −1 dBTP;
   c) −9 dBFS; d) −2 dBTP. → b (−2 dBTP para MPEG-1 L2/AC-3). «La sonoridad» y «Qué hace la
   sonoridad en la cámara». **Entera.**
7. (Niveles, práctica) Para alinear con el tono de 1 kHz, la EBU recomienda: a) un medidor de
   sonoridad en escala absoluta; b) un medidor de pico; c) el oído; d) un sonómetro. → b. «Qué hace la
   sonoridad en la cámara». **Entera.**
8. (Sincronía, práctica) Una DSLR y un receptor de corbata profesional: la máxima calidad se logra:
   a) adaptando XLR a jack de 6,35 mm; b) conectando por XLR al cuerpo; c) grabando aparte, con
   claqueta, y sincronizando en posproducción; d) grabando aparte y uniendo el grabador a la cámara por
   XLR para sincronizar. → c. «La cámara fotográfica y el sonido aparte». **Entera.**
9. (Sincronía/criterios, práctica) En la Z200, en modo cámara lenta (*Slow & Quick Motion*):
   a) el audio se graba a velocidad normal; b) no se graba audio; c) sólo se graba el canal 2;
   d) se graba el tono. → b. «Lo que rompe la sincronía». **Entera.**
10. (Ambiente y criterios básicos, Libro de estilo) En Canal Sur, en una declaración, por el canal 2
    se registra: a) el periodista; b) una copia del canal 1; c) el sonido ambiente del micrófono de
    cámara; d) nada si el lugar está en silencio. → c; y el ambiente se graba «siempre y en cualquier
    circunstancia», incluso en un museo. «El reparto de canales» y «El ambiente se graba siempre».
    **Entera.**

Otras cubiertas en la relectura (sin numerar): 20 Hz-20 kHz y la trampa de los µm; transductor
eléctrico-mecánico-acústico = altavoz; margen dinámico (máximo − ruido) y 6 dB por bit; hipercardioide
para sonidos lejanos; qué hace ***AUTO/MAN***, el limitador (sólo en manual) y el AGC enlazado;
salida de mesa en LINE (canal 1 de mesa, 5.4); enclavamiento de TC (EXT-LK, diez segundos, un cuadro
por hora); código de tiempo como acuerdo periodista-cámara (5.3.3); falseamiento del ambiente (3.2.2).

Resultado: 10 de 10 enteras; no hizo falta ampliar el tema tras las preguntas.
