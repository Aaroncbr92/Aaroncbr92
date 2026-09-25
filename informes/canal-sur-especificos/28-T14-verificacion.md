# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`.
Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Ficheros tocados: el tema y este informe.

## Fuentes releídas en el original (todas el 25-09-2026)

| Fuente | Cómo |
|---|---|
| UIT-R BS.775-4 (12/2022) | PDF de itu.int; estado «In force» y versiones −0 a −3 «Superseded» en itu.int/rec/R-REC-BS.775 |
| UIT-R BS.1770-5 (11/2023) | PDF de itu.int; «In force» en itu.int/rec/R-REC-BS.1770 |
| EBU Tech 3343-2023 (V4, nov. 2023) | `fuentes/normas-tecnicas/EBU_Tech3343-2023.txt` (historial: «November 2023 V4») |
| SMPTE RDD 19-2011 | PDF de pub.smpte.org (portada «NOT a Standard») |
| EBU Technical Review 2009-Q1, De Pomerai | PDF de tech.ebu.ch |
| Dolby ED2 Technology Brief | PDF de professional.dolby.com |
| Dolby Atmos Renderer Guide v3.0 (2-VIII-2018) | PDF de professional.dolby.com |
| RTW, «Focus: The Multi Correlator», T. Valter, 9-VIII-2019 | página de rtw.com |

Método: script que busca cada cita en negrita («…») del tema, normalizada, en el texto de las ocho
fuentes; las que no casaban se leyeron a mano (todas por defectos de extracción: el signo «°»,
«up to120», «±90°phase», la llamada de nota «BS.17703», el guion de «Stereo-downmix», o elisiones
«…» legítimas), salvo las ecuaciones de downmix (hallazgo 1). Después, lectura de cada afirmación
en redonda contra su fuente.

## Copiado del común y de RTVE sin cambios

Común: ninguno declarado. RTVE sin cambios: los 11 pasajes del informe de redacción (15 fragmentos,
incluidas las cuatro filas de la tabla) comprobados por script: sin `**` y con espacios normalizados,
cada uno es subcadena literal de `temas/sonido/15-audio-multicanal.md` y del tema. No se re-verifican.

## Hallazgos y correcciones (13)

1. **Negrita no literal (9)**. Las «ecuaciones» de downmix de la BS.775 (tabla 2) iban en negrita
   como cita, pero la fuente es una matriz de coeficientes, no ese texto. Pasadas a redonda y
   presentadas como «coeficientes escritos como ecuación, sin los términos a 0,0000»; se sitúa la
   tabla en el anexo 4. Los valores son correctos (la −4 da a estéreo L=1,0 L+0,7071 C+0,7071 LS).
2. **Salvedad omitida (6)**. LFE a 120 Hz: el punto 4 de la BS.775 lo pide en el intercambio
   internacional de programas; añadido con su cita.
3. **Salvedad omitida (6)**. Envolvente mono (MS): la BS.775 lo admite «In circumstances where
   transmission capacity or other constraints apply»; añadido.
4. **Afirmación contraria a la fuente (9)**. «Que un valor de fábrica sugiera que el metadato no se
   ajustó es lectura de oficio, no de la guía»: la Tech 3343 § 6 lo dice («chances are that Metadata
   have either not been looked at or been abused…»). Sustituido por la cita; quitado de «oficio».
5. **Afirmación sin fuente (9)**. Doble compensación del Dolby E: «si el audio ya venía adelantado…»
   no es el caso de la fuente; sustituido por el ejemplo de la Technical Review (desembebedor con
   retardo + retardo aparte = vídeo retrasado dos veces).
6. **Afirmación sin fuente (9)**. Que el decodificador de matriz «vuelve a separar un central y un
   envolvente» del Lt/Rt y que del Lo/Ro «no se puede extraer» central y envolventes: la Tech 3343
   sólo dice «better compatibility with matrix-surround playback systems». Quitado; la aplicación
   práctica se reescribe con lo que la fuente da.
7. **Cita mal atribuida en su alcance (9)**. «La Tech 3343 lo sitúa en el receptor»: la guía recoge
   dos vías (producción y receptor). Corregido con la cita de § 7.1.
8. **Hueco resuelto (6)**. «Hasta 3 LU»: el caso es la divergencia total de los tres frontales;
   dicho en el tema y quitado de «Lo que no da».
9. **Salvedad omitida (6)**. Atmos: 128 canales de entrada a 48 kHz (64 a 96 kHz); la plantilla, «depending
   on the template». Añadidos; la suma 10 + 118 = 128 queda a 48 kHz.
10. **Afirmación sin fuente (9)**. Tabla Dolby E/Dolby Digital: «Los propios» metadatos y reducción
    «la de un códec de emisión» → lo que dicen la Technical Review y el RDD 19.
11. **Cita compuesta (9)**. Factores de sonoridad del downmix: la negrita unía viñetas con «;»
    como si fuera texto; ahora una cita por viñeta.
12. **Precisión de fuente (8)**. «Más de dos traseros» es la nota 4 del punto 2, no el punto 2: indicado.
13. **Inferencia presentada como norma (9)**. «La escucha estéreo de referencia es la misma pareja
    frontal del 5.1»: reescrito como la pareja frontal de la disposición de referencia de la BS.775.

Trazabilidad y «Lo que no da» actualizados en consecuencia (fecha de relectura, anexo 4, alcance de
los 120 Hz, doble retardo, 64 canales a 96 kHz, divergencia).

## Confirmado sin cambios

Versiones y fechas de la ficha; resumen, palabras clave, considerandos c) y h), puntos 2-5 del
«recommends», anexo 2, anexo 7 y su adjunto 1 de la BS.775-4; ángulos 60°, 100°-120°, 60°-150°;
20-120 Hz, −10/+10 dB y excepción DVD-Audio/SACD; coeficientes 0,7071/0,5 y su igualdad con la
BS.775-2 citada por la Tech 3343; BS.1770-5 (BS.2051, anexo 4); Tech 3343 § 4.2, § 6, § 7.1, § 7.2
(+1,5/−3/4,5 dB, perfiles, Extended BSI, TS 101 154, −27/−31, Lo/Ro por defecto, upmix); RDD 19
(10 ciclos, 8 señales, 30 cuadros, conmutación cada dos cuadros P); Technical Review (40 ms a 25 Hz,
In-Sync/Advanced, banda de guarda, trama no modificable, «up to six»); ED2 (16 canales, 8 por
subflujo, compatibilidad); Atmos (7.1.2, 118); RTW (−1/0/+1, 0,3-0,7, multicorrelador). Recuentos:
cinco factores, siete requisitos, tres planos, 7 rúbricas: cuadran.

## Lentes

Tema técnico sin norma legal: `refutar_prosa.py` 0 hallazgos; `indice.py` 8.987 palabras, 38
epígrafes (el aviso «sin portada: es un esquema» sale igual en los temas 13 y 15; la portada está).
Índice sin cambios (no se tocó ningún rótulo).

## Para la refutación

Se mantiene declarado como oficio el «rasgo distintivo» de Dolby Atmos (adaptado del RTVE, sin cita).
