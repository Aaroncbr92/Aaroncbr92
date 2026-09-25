# Puesto 28 · Tema 2 · Fase 4 · Refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/02-electricidad-y-electronica-aplicada-al-audio.md`.
Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). No corrijo: listo.

Exactitud: salto lo listado como «Copiado de RTVE sin cambios» en `28-T02-redaccion.md` (el común no
aporta nada). Cobertura: el tema entero. Preguntas: `28-T02-preguntas.md` (10 enteras, 2 a medias, 3 no).

## Fuentes releídas

| Fuente | Leída | Resultado |
|---|---|---|
| Rane, RaneNote 124 (ranecommercial.com/legacy/note124.html) | 25-09-2026 | 6 dB balanceado/desbalanceado con las excepciones de transformador y *cross-coupled*; «a gain of 12 dB, with all controls seemingly set for unity»; «turn the level control down 6 dB»; 100 Ω/100 Ω = 1/2; «creates many ills»: conforme |
| Rane, RaneNote 135 | 25-09-2026 | Crest factor de la senoide 1,4 (3 dB): conforme |
| Rane, RaneNotes 110 y 151 | 25-09-2026 | Consultadas para cobertura (masa en estrella en 151, § signal ground; ni 110 ni 151 nombran el CMRR) |
| DPA, «Know the basics about phantom power» | 25-09-2026 | La página no da el valor de las resistencias de inyección (confirma el hueco declarado) |

El resto de citas lo releyó la verificación el mismo día; no las repito.

## Hallazgos de exactitud

1. **Grave · error 9/6 (dato de fabricante falso sin salvedad).** 2.3, línea 301-303: la cita de Crown
   **«The 1.4V position corresponds to a +4 dBu level»** es literal, pero no cuadra con la definición
   del propio tema (0 dBu = 0,775 V, 2.1): +4 dBu = 0,775 × 10^(4/20) ≈ 1,23 V; 1,4 V ≈ +5,1 dBu
   (cuenta). El tema no da en ningún sitio +4 dBu en voltios, así que el alumno aprende 1,4 V
   (pregunta 3). Propuesta: añadir tras la cita que +4 dBu son 1,23 V por cálculo y que la posición
   de 1,4 V de Crown queda algo por encima (unos +5 dBu).
2. **Menor · error 9.** 1.5, tabla, fila C: «El más alto de las lineales». La clase C no es un
   amplificador lineal (conduce menos de medio ciclo y el propio tema dice que su distorsión es «muy
   alta» y exige un circuito resonante). Propuesta: «Más alto que A, B y AB» o «Alto».
3. **Menor · error 5.** «Lo que este tema no da» (líneas 733-734): EBU (en «EBU R 68»), MADI y Dante
   sin presentar en las siglas de entrada.
4. **Menor · error 1.** 3.2, línea 375: la DI «aísla masas (epígrafe 5.3)»; 5.3 no menciona la DI
   (habla del transformador de aislamiento). Remitir a 4.4, que sí la une al transformador, o decir
   en 5.3 que la DI con transformador es una forma de aislamiento.

Comprobado sin hallazgo: cuentas (0,775 V; +20 dBu = 7,75 V; 316 mV; 24 / 2,67 / 4 Ω; +16/+24 dBu;
6 dB), recuentos (cuatro magnitudes, tres despejes, tres pasos, tres masas, tres orígenes del ruido),
remisiones a epígrafes internos y a temas 1, 3, 4, 10, 11, 13 y 16, y la coherencia de 4.2 con 4.3
y 7.3.

## Cobertura del enunciado

Las seis rúbricas (niveles, impedancias, balanceado, masa, ruido, *phantom*) tienen epígrafe propio
en su orden. Lagunas que la fase 5 debe ampliar (con fuente):

1. **Masa en estrella** (pregunta 12): RaneNote 151, ya citada por el tema, la define («all
   "divisions" of signal ground connect together in one place. This is usually called a star
   grounding scheme») y da las dos escuelas (centro en la fuente de alimentación o en la masa del
   conector de entrada). Cabe en 5.2.
2. **Rechazo en modo común (CMRR)** (pregunta 11): nombre de la magnitud que mide lo que 4.2 explica.
   No está en las RaneNotes 110 ni 151; hace falta otra fuente de fabricante o universitaria. Si no
   se confirma, declararlo en «Lo que este tema no da».

A medias, sin ampliar: el nominal doméstico −10 dBV (pregunta 4) y el valor de las resistencias de
la P48 (pregunta 15) son huecos ya declarados; la DPA releída tampoco da las resistencias.

## Recuento

Graves 1 · menores 3 · lagunas 2.

## Otros ficheros tocados

Sólo `28-T02-preguntas.md` y este informe. Descargas de trabajo en el directorio temporal de la sesión.
