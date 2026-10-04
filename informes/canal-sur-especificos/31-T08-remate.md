# Puesto 31 · Tema 8 · Fase 5, remate

Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/08-autocontrol-y-operacion-basica.md`.
Rematado el 4-X-2026 (fecha de referencia: 24-IX-2026), con `31-T08-refutacion.md` y `31-T08-preguntas.md`.
Cada corrección se comprobó en la fuente antes de aplicarla. **Amplía contenido nuevo: sí** (procede 5 bis).

## Hallazgos de la refutación

| N.º | Comprobación en la fuente (4-X-2026) | Aplicado |
|---|---|---|
| Menor 1 (viñeta) | López Vigil, cap. 10, l. 12218: «La mayoría de las cuñas se han convertido en simples viñetas pregrabadas con fondo musical.» Literal | Sí |
| Menor 2 (nexo) | Manual de RTVE, RNE 3.2.1.1, l. 66: «Este tipo de transición … continuidad forzada.» Literal | Sí |
| Menor 3 (ráfaga y UER) | R 128 s1 no nombra la ráfaga (el propio tema lo dice). Atribución corregida | Sí |
| Prosa (redundancia) | Frase «Y la particularidad que más define…» quitada; el resto del párrafo copiado de RTVE queda literal | Sí |

## Lagunas

1. **Indicativo y punto** (preg. 13): glosario 7.5 del Manual de RTVE, l. 258-269, literales. Añadido
   un párrafo al final de «Las piezas cortas y cómo las llama la UER».
2. **Nexo de las continuidades** (preg. 14): cubierta con el menor 2.
3. **Automatismos de la mesa de autocontrol** (preg. 15): localizada documentación de fabricante y
   descargada a `fuentes/canal-sur/sonido/fabricantes/` (PDF + .txt por `documento.py texto`):
   - Audioarts (Wheatstone), *AIR 1 Radio Mixing Console Technical Manual*, dic. 2007
     (bgs.cc/content/AUD-AIR1 MANUAL.pdf): «Monitor Mute» y «On Air Tally» (cap. 2), «On Air LED» (cap. 3).
   - Audioarts, *AIR 4 Radio Console Technical Manual*, jun. 2012 (bgs.cc/content/AUD-AIR4 MANUAL.pdf):
     «CR Mutes», «On Air Tally», «ON Button» (arranque de equipos externos, arranque del híbrido).
   - D&R, *AIRENCE-USB Manual* v1.11 (broadcastpartners.nl): «FADER» (fader start), «Mute by Mic»
     (relé de luz roja), «Mute-Act» (20 dB), «CRM SECTION (Control Room Monitor)».
   Nuevo epígrafe `### Lo que hace sola una mesa de autocontrol`, al final de «Autocontrol y operación
   básica». Las mesas se dan como ejemplo, no como las de CSRTV. Lo que sigue sin fuente (encadenado
   automático en el sistema de emisión) se mantiene declarado.

## Pasajes cambiados

1. Portada, «Fuente»: añadidos «y Audioarts y D&R (mesas de radio)». «Extensión»: 14.400 palabras.
2. Siglas: «Yamaha, Soundcraft, Rane, Audioarts y D&R».
3. «Qué se puede preguntar»: añadidas la mesa de autocontrol al abrir el micrófono, el arranque por
   fader y el indicativo frente al punto.
4. «Qué es el autocontrol»: quitada la frase redundante inicial del párrafo copiado.
5. Nuevo epígrafe «Lo que hace sola una mesa de autocontrol» (cuatro párrafos; once citas literales
   de los tres manuales; la consecuencia práctica, marcada como oficio).
6. «Qué es una cuña», final: la viñeta y la cita de las «simples viñetas pregrabadas».
7. «Las piezas cortas y cómo las llama la UER»: párrafo nuevo con indicativo y punto (glosario 7.5).
8. «La ráfaga como pieza corta»: «La UER no nombra la ráfaga, pero una ráfaga encaja en lo que la R 128 s1 llama…».
9. «Tres sentidos de "continuidad"»: la condición del nexo y la «continuidad forzada».
10. «Lo que este tema no da»: el punto de la Yamaha CL ya no dice que no se ha leído ningún manual de
    mesa de autocontrol; el de automatismos se reduce al encadenado automático.
11. «Trazabilidad»: tres filas nuevas (AIR 1, AIR 4, AIRENCE-USB), leídas el 04-10-2026.

Antecedentes releídos: «el mismo manual» (AIRENCE-USB), «el mismo apartado» (3.2.1.1), «el autor»
(López Vigil) y «esos manuales» tienen delante su referente.

## Lentes

- `indice.py` sobre el tema: 14.443 palabras, 67 epígrafes; índice regenerado con el epígrafe nuevo
  (el tema no está en `portadas.tsv`; extensión de la ficha puesta a mano).
- `negritas.py` contra los tres manuales, López Vigil y el Manual de RTVE (anexos y RNE): todas las
  negritas nuevas, literales. Las «no está» restantes son de fuentes no pasadas en esta corrida (EBU,
  Yamaha, Soundcraft, Rane, AES), sin cambios desde la refutación.
- `refutar_prosa.py`: 7 (los 6 previos de mayúsculas en citas inglesas y «CRM», presentada en el
  propio párrafo). Sin norma legal: no proceden `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

- El tema (arriba).
- Creados: este informe; `fuentes/canal-sur/sonido/fabricantes/audioarts-air1-manual-2007.{pdf,txt}`,
  `audioarts-air4-manual.{pdf,txt}`, `dr-airence-usb-manual-1.11.{pdf,txt}`.
