# Puesto 30 · Tema 2 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.
Entradas: `30-T02-refutacion.md` (2 hallazgos menores, 2 lagunas) y `30-T02-preguntas.md` (12 enteras,
1 a medias, 2 no).

## Comprobación en la fuente (todas releídas el 25-09-2026)

| Nº | Fuente releída | Resultado |
|---|---|---|
| H1 | EBU R 128-2023 (`montador/ebu/r128.txt`, líneas 98-125): i) «±0.2 LU … measurement errors», j) «lower than −23.0 LUFS on purpose… clearly indicated… not compensated», m) «The measurement tolerance is ±0.3 dB (for signals with a bandwidth limited to 20 kHz)» | Confirmado. Aplicado |
| H2 | EBU R 68-2000 (`montador/ebu/r068.txt`, l. 17-19): «It is of the opinion that recordings should be made…», en el preámbulo, no tras «recommends» | Confirmado. Aplicado |
| L1 | UIT-R BT.709-6, parte 6 (txt l. 820-880 y PDF con PyMuPDF para los signos «±», que el txt pierde): cita de la referencia, 6.1 0/700 mV, 6.2 ±350, 6.3 «Tri-level bipolar», 6.5 ±300 ± 2 %, 6.6 «Sync on all components» | Confirmado. Ampliado. *Genlock* y *black burst* no aparecen en ninguna fuente de `montador/`: van como oficio sin fuente |
| L2 | SMPTE ST 292-1:2018, 8.1.8 y tabla 3 con notas (txt l. 438-494): RP 184; B1 10 Hz, B2 100 kHz, B3 > 1/10 del reloj; A1 1 UI *timing*, A2 0.2 UI *alignment*; nota 2 barras de color | Confirmado. Ampliado |

Ninguna corrección del informe resultó errónea.

## Pasajes cambiados

1. **§ 1 «La interfaz digital serie (SDI)»**, tras el párrafo del *jitter* como ruido de fase: nuevo
   párrafo «Cómo se mide» (remisión a la RP 184, UI) y tabla de los dos *jitter* de la tabla 3, con el
   borde superior y la nota 2. La RP 184 declarada no leída. **Contenido nuevo.**
2. **§ 1, nuevo `###` «La referencia de sincronismo»** (entre SDI y § 2): la cita de la parte 6 de la
   BT.709-6, tabla con 6.1, 6.2, 6.3, 6.5 y 6.6, y la explicación de los tres niveles, *genlock* y
   *black burst* como oficio. **Contenido nuevo.**
3. **§ 2 «Del sonido analógico al digital»**, frase de los 16 bits: «las grabaciones se hacen» pasa a
   «que no lo recomienda en su parte dispositiva sino que lo da como su parecer: «It is of the opinion
   that recordings should be made…»; es decir, las grabaciones deben hacerse así, en opinión de la EBU».
4. **§ 2 «La sonoridad: EBU R 128»**: dos viñetas nuevas (tolerancia i) de ±0,2 LU, distinguida de la
   de ±1,0 LU; excepción j) por debajo de −23,0 LUFS) y la viñeta del pico con la tolerancia de medida
   de m) (±0,3 dB). **Contenido nuevo.**
5. **Qué se puede preguntar**: añadidas la medida del *jitter*, la señal de referencia de la HD y las
   tolerancias de la R 128.
6. **Recomendaciones y normas técnicas que el tema cita**: filas de la BT.709-6 (parte 6), R 68
   (parecer), R 128 (i, j, tolerancia de m) y SMPTE SDI (*jitter*); la RP 184 añadida a las no leídas.
7. **Trazabilidad**: BT.709-6 con la parte 6; R 128 con i, j y m; ST 292-1 con 8.1.8 y tabla 3; lista
   de oficio con el UI, la referencia común, la forma del pulso, *genlock* y *black burst*.
8. **Portada**: extensión 10.700 → 11.550 palabras. El índice lo regenera `indice.py`.

Relectura de antecedentes: «esa parte 6», «la tabla de esa parte 6», «la anterior» (±1,0 LU),
«Distingue dos» (la ST 292-1) y «el § 2» tienen delante su antecedente.

## Lentes

- `indice.py`: 29 epígrafes, 11.554 palabras; nueva entrada «La referencia de sincronismo».
- `refutar_prosa.py`: 1 aviso, «BC» sin presentar, falso positivo (fragmento de Y'C'BC'R dentro de
  una cita de la BT.2020, ya existente). Sin relleno ni repeticiones ni negritas rotas.
- Tema técnico sin norma jurídica: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Preguntas tras el remate

10, 11 y 13 pasan a enteras: 15 de 15.

## Resultado

El remate **amplió** (pasajes 1, 2 y 4): procede la fase 5 bis sobre ellos.

## Ficheros tocados

- El tema y este informe. Ningún otro.
