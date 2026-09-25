# Puesto 28 · Operador/a de Sonido · Tema 8 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/08-sonido-en-television.md` (tras la
verificación, 9.220 palabras según `indice.py`; 47 epígrafes). Fecha de trabajo y de lectura de
todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).

## Fuentes releídas (25-09-2026)

| Fuente | Cómo |
|---|---|
| EBU Tech 3347 Rev. 1 (oct. 2012) | PDF de tech.ebu.ch; guardado en `fuentes/canal-sur/sonido/EBU_Tech3347.{pdf,txt}` |
| EBU Tech 3326 Rev. 4 (nov. 2014) | PDF de tech.ebu.ch; guardado en `fuentes/canal-sur/sonido/EBU_Tech3326.{pdf,txt}` |
| EBU Tech 3343-2023 | `fuentes/normas-tecnicas/EBU_Tech3343-2023.{txt,pdf}` (el PDF para situar notas al margen por página) |
| Clear-Com, *Interruptible Fold Back, AKA IFB* (16-03-2021) | Página web; texto en `fuentes/canal-sur/sonido/fabricantes/clearcom-ifb-2021.txt` |
| Clear-Com, *A Comprehensive Guide to … Partyline Systems* (feb. 2018) | PDF; texto en `fuentes/canal-sur/sonido/fabricantes/clearcom-partyline-guide-2018.txt` |
| Soundcraft, *Guide to Mixing* (© 2001) | PDF; texto en `fuentes/canal-sur/sonido/fabricantes/soundcraft-guide-to-mixing.txt` |
| Yamaha, *CL5/CL3/CL1 V5 Reference Manual* | PDF (14 MB, sólo en el directorio temporal de la sesión) |
| BOJA núm. 186, anexo I | `convocatoria/canal-sur/2026-bases-boja-186.txt` |

Método: script que extrae cada negrita del tema y la busca, normalizada, en todas las fuentes; las
que no casaban se leyeron a mano. Después, lectura de cada dato no literal (secciones, fechas,
títulos, condiciones «obligatorio/recomendado», cifras) en su contexto.

## Copiado del común y de RTVE sin cambios (sólo literalidad)

Comprobado por script frase a frase contra Cámara 03, 08 y 13 y contra RTVE realizacion-tv/18,
realizacion/09 y sonido/06: los cinco bloques del común y los doce pasajes RTVE listados en
`28-T08-redaccion.md` son literales (sin negritas de RTVE). No se re-verifican.

## Correcciones aplicadas

| # | Pasaje | Error | Qué dice la fuente | Cambio |
|---|---|---|---|---|
| 1 | Intercom por IP, latencia | 9 (negrita no literal) | Tech 3347 § 1.5: dos viñetas sin «;» | Dos citas separadas |
| 2 | Híbrido, «…most commonly used» | 9 (cita cortada sin marca) | La frase sigue: «to perform two-wire/four-wire conversion» | Añadido «[...]» |
| 3 | IFB, «la más precisa que hay publicada» | 9 (afirmación sin fuente) | — | Quitado |
| 4 | Mezclar de oído, «(§ 3.1)» | 8 (lugar mal) | La frase es una nota al margen de las páginas de § 2.4 (p. 10) y § 3.2 (p. 13), no de § 3.1 | Localización corregida, también en la tabla de recomendaciones |
| 5 | Procesador, «Muchas cadenas de emisión tienen…» | 9 | § 2.4 habla de instalar un procesador de seguridad a la salida de *Master Control* para lo no normalizado; no da frecuencia de uso | Reescrito según § 2.4 |
| 6 | CCU, «Parece una salida balanceada de audio» | 9 (salvedad torcida) | Clear-Com: el error común es creer que es un circuito de tres hilos (envío, recepción, común) | Corregido |
| 7 | «La norma de sonoridad… EBU R 128»; «tiene que cumplir una norma» | 2 (tipo de documento) | R 128 es una recomendación | «recomendación» |
| 8 | Comprobación de salida, «por debajo de −1 dBTP» | 9 (matiz) | «shall not exceed −1 dBTP» | «ajustado para no superar −1 dBTP» |
| 9 | Cita «broadcasters used to transport…» sin sección | 1 | Tech 3347 § 1.1 | Añadido «§ 1.1» |
| 10 | Trazabilidad | fecha de lectura | Leídas en la fuente el 25-09-2026, no sólo a través de la investigación | Frase actualizada |

## Confirmado sin cambios (lo principal)

- Tech 3347: portada Rev. 1, oct. 2012; § 1.1, 1.2 (tres tipos y usos cotidianos), 1.3 (cuatro
  ubicaciones de la interfaz), 1.5 (fuera de alcance; encuesta 100/50 ms; G.114), 2.2 (RTP sobre
  UDP), 3.1 obligatorios G.711 y G.722 a 64 kbit/s «SHALL», 3.2 recomendados Speex (8 y 16 kHz) y
  G.729 (8 kbit/s). Lo que pedía el redactor: sí, Speex y G.729 están en § 3.2.
- Tech 3326 Rev. 4 (nov. 2014): RTP sobre UDP «SHALL»; G.722 muestreo 16 kHz (también en Tech 3347
  § 3.1.2).
- Tech 3343-2023 (nov. 2023): ±0,2 LU y nota 2 (R 128 rev. 3, 2020); ±1,0 LU en directo; −1 dBTP
  (nota al margen literal); +3 dB desde −20 LUFS (§ 3.1); § 3.5.1 y 3.5.2; § 8.1 (1 kHz a −18 dBFS,
  medidor de pico, PML de −9 dBFS obsoleto); § 8.2 (73 dBC, C lenta, «should not exceed 1 dB SPL»
  —el «no más de 1 dB» del tema es correcto—, frontales <0,5 dB, LFE +10 dB). «LLISTref» es
  subíndice en el PDF: se deja.
- Clear-Com IFB: definición, tres elementos, equipo, atenuación de la escucha, usos. Clear-Com
  *Partyline*: dos hilos, siempre dúplex, no privada; patillas 1-2-3 y 30 V; cuatro hilos;
  híbrido, *trans-hybrid loss*, *null*; cámaras (sin diseño común, aislamiento, CCU a cuatro
  hilos, cada cámara por separado). Semidúplex = «two-way… one-way at a time» (glosario): cuadra.
- Soundcraft: «Pre-fade rather than post-fade auxiliaries must be used» (el «exige» es exacto).
- Yamaha CL V5: cita *Mix Minus* literal (el script falla sólo por el salto «MIX/¶MATRIX»).
- BOJA anexo I: 21 plazas del puesto (8 en Sevilla; resto en Algeciras, Almería, Cádiz, Córdoba,
  Granada, Jaén, Jerez y Málaga).
- Remisiones a los temas 3, 4 (DIM), 6 (dos micrófonos, reparto de canales, planos) existen.

## Aviso del redactor que se mantiene

«Dos líneas, dos caminos de vuelta»: el tema dice (oficio) que el retorno de cada línea quita las
dos; la plantilla RTVE de su pregunta 30 decía otra cosa. No hay fuente técnica que lo zanje; el
razonamiento del tema es coherente. Se deja como oficio, declarado.

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (1 aviso: «IFB» en el título antes de las
siglas, como en el tema 6; no se toca) e `indice.py` (9.220 palabras, 47 epígrafes).

## Ficheros tocados

El tema 8 y este informe. Añadidas fuentes: `fuentes/canal-sur/sonido/EBU_Tech3347.{pdf,txt}`,
`EBU_Tech3326.{pdf,txt}`, `fabricantes/clearcom-ifb-2021.txt`,
`fabricantes/clearcom-partyline-guide-2018.txt`, `fabricantes/soundcraft-guide-to-mixing.txt`.
