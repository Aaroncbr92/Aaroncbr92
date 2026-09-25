# Puesto 28 · Operador/a de Sonido · Tema 4 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/04-consolas-de-mezcla-analogicas-y-digitales.md`.

## Pasajes copiados: sólo comprobación de literalidad

Script de cotejo (párrafos y filas de tabla, sin `**` ni ✔ ni número de lista, espacios
normalizados) contra Cámara `08-camara-operador/06-captacion-de-sonido.md` y los cuatro temas RTVE.

- **Copiado del común** (1 bloque: «En digital, el máximo…», párrafo de R 68/Tech 3343 y «Es decir: el
  tono…»): literal. No se re-verifica.
- **Copiado de RTVE sin cambios** (9 pasajes, incluidas las tablas de siete bloques, PFL/AFL, mandos
  de escucha y matriz de conmutación): todos literales. No se re-verifican.
- Lo adaptado de RTVE y lo nuevo se verificó entero.

## Fuentes releídas (todas el 25-09-2026, descargadas de nuevo con curl y pasadas a texto con `documento.py texto`)

Yamaha *CL5/CL3/CL1 V5 Reference Manual*; Yamaha/D. Gould, *Get on the Bus*; *The Soundcraft Guide
to Mixing* (ZL0439, E&OE 08/01, © 2001: confirmado); Avid *Pro Tools Reference Guide* Version
2025.12, cap. 55 (confirmado); EBU R 68-2000 y Tech 3343-2023 (V4, nov. 2023) de `fuentes/normas-tecnicas/`.

Resultado: todas las citas en negrita están en su fuente (las únicas que no casan por script son
listas con viñetas unidas —procedimiento PFL de Soundcraft, contenido de escena de Yamaha— y los saltos
de línea de R 68/Tech 3343: comprobadas a mano). Cifras (1000 ms, 16 DCA, 8 grupos de silencio,
000-300, V3.0, 1:8 = 18,06 dB) y cálculos (−3 + 4 = 1; 40 + 3 − 5 = 38): conformes. Remisiones a
los temas 2, 5, 7, 8, 10, 13, 14 y 15: existen (tema 2 sostiene la ganancia «all at once at the
input mic stage»; tema 5 tiene «Por qué 18 dB de reserva»). Avisos del redactor: la fila de envíos
del DCA se sostiene como deducción declarada (Get on the Bus: el VCA manda **«control voltages to the
faders or gain stages»** de los canales); «CL V3.0» es versión de la consola: conforme.

## Hallazgos y correcciones aplicadas

1. **Error 3 (recuento).** El canal de entrada de la CL tiene diez bloques, no nueve: faltaba
   **«LEVEL/DCA 1-16»** entre INPUT DELAY y ON. Añadido (con la descripción literal del manual, que
   no casa, declarado); «nueve» → «diez» en tabla y Trazabilidad; «Después vienen el fader…» → «el
   panorama y los envíos».
2. **Error 9.** DIGITAL GAIN sin definición: añadida **«Attenuates/boosts the level of the input
   signal»**. El previo «está en la caja de entrada»: también en OMNI IN de la consola y en tarjetas
   (cita añadida).
3. **Error 9 (LCR).** El modo ST/MONO o LCR se elige canal a canal, no para la salida principal, y
   en LCR reparte el panorama más el mando CSR. Reescrito con cita.
4. **Error 9 (generalización).** «En una consola digital, cada bus tiene su canal de salida» → «En la
   Yamaha CL».
5. **Error 6.** VCA/DCA **«function similarly in most mixing consoles»**: la cita cortaba la salvedad.
6. **Error 6.** Trim, como Touch/Latch, es sólo de Pro Tools Ultimate y Studio. Añadido.
7. **Error 9.** El porqué de Latch en mandos giratorios era deducción; sustituido por el de Avid
   (**«since it does not time out and revert…»**).
8. **Error 6.** Write: añadida la preferencia **«After Write Pass, Switch To»** (Touch, Latch, No Change).
9. **Negrita no literal.** Cinco entradas de glosario/manual llevaban dos puntos dentro de la cita
   (BUS or BUSS, EFFECTS SEND, FOLDBACK SEND, MUTE GROUPS, PRE/POST button): separado el rótulo.
10. Apoyo añadido donde había inferencia: finalidad del oscilador (Yamaha) y uso de la ganancia
    digital con compensación de ganancia (Yamaha). Trazabilidad y extensión (9.500) actualizadas.

Relectura de los pasajes cambiados: cada remisión tiene antecedente; «Por eso» sin causa quitado.

## Lentes

Sin normas legales: sólo `refutar_prosa.py` e `indice.py`. Prosa: 8 «siglas», todas dentro de citas
inglesas o nombres de mando (BUSS, LOW, MID, NB, NOTE, OMNI, VARI) salvo ST, que se presenta ahora
(«ST/MONO (estéreo y mono)»). Índice regenerado: 9.513 palabras, 58 epígrafes.

## Otros ficheros tocados

Ninguno fuera del tema y este informe (copias de trabajo de los manuales en el scratchpad).
