# Puesto 28 · Operador/a de Sonido · Tema 3 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/03-microfonia.md`. Fecha de trabajo y de
lectura de fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026). No se corrige el tema.

## Fuentes releídas

Páginas de DPA *Mic University* descargadas por el verificador el 25-09-2026 (texto limpio del
directorio de trabajo de la sesión, `v03/`), releídas el 25-09-2026: las 19 que lista
«Trazabilidad» (transductores, alimentación fantasma, especificaciones, direccional/omni, patrones,
cañón, miniatura, colocación en la voz, mano, estéreo, inmersivo ×2, viento/lluvia, inalámbricos
partes 1-6, primer sistema, *Troubleshooting*).

Exentos de la lente de exactitud: los 12 pasajes «Copiado del común» y los 6 «Copiado de RTVE sin
cambios» de `28-T03-redaccion.md`.

## Lente 1 · Exactitud

Cotejo por script de todas las citas «…» contra las páginas: las que no casan son todas del común,
del Libro de estilo o rótulos en español. Rehechos a mano los datos en redonda atribuidos a DPA:
tabla −3/−6 dB, polaridad del lóbulo trasero (super, hiper y ocho), tabla DSF/DF/DI, ángulos del
2017 (105→25°), 130°/30 dB, cifras estéreo (15 dB, 1,1 ms, 0,5 ms/6 dB; ORTF 17 cm, DIN 20 cm/90°,
NOS 30 cm/90°), decodificación MS con mesa, 8-64 cápsulas, bandas europeas, DECT, ±40/±75 kHz,
50 µs, 15-25 dB, >90 dB, 100-125 dB, 6:1-8:1, 1,6 Mbit/s (cifra de DPA), WMAS, 4 m, 10 mW, pilas,
27 dB(A), 20-30 dB omni/cardioide, 3-4 kHz de la espuma mojada, bolsa antes de la lluvia,
logotipos 2-4 kHz, posiciones del miniatura. Conformes salvo lo que sigue.

### Graves

Ninguno.

### Menores (5)

1. **Contradicción de la fuente no declarada (error 6)**, «La recepción, lo básico», l. 821. El
   tema da como regla de DPA separar las antenas de diversidad **al menos media longitud de onda**
   (*Troubleshooting*, 2.05). Pero la parte 6 de la guía, 6.10, dice **«Diversity antennas should
   be placed at least 1/4 wavelength apart.»** La verificación cambió ¼ por ½ sin ver la parte 6.
   Remate: dar las dos cifras de DPA (¼ λ en la guía, ½ λ ≈ 25 cm a 600 MHz en *Troubleshooting*)
   y los 30 cm de la guía básica.
2. **Afirmación sin fuente (error 9)**, tabla de protecciones, l. 872: «En un cardioide, mal
   diseñada, puede cambiar la directividad si tapa las entradas traseras» (espuma). La página del
   viento no lo dice; lo que cambia la directividad, según DPA, es la bolsa de plástico ceñida
   (ya en l. 916). Remate: quitar la frase o marcarla como oficio.
3. **«Obligatorio» sin apoyo (error 4)**, tabla «Analógico y digital», l. 756: «limitador
   obligatorio para no invadir el canal vecino». DPA (parte 3) dice que el límite de ±75 kHz
   **«must not be exceeded as it may cause interference to neighboring channels»**, y (parte 2) que
   el limitador **«is often included»**. Remate: «el límite de ±75 kHz no debe superarse; de ahí el
   limitador que suele llevar el emisor».
4. **Salvedad omitida (error 6)**, «Bandas, grupos y canales», l. 804-807. Tras el procedimiento
   rápido, DPA añade: **«You may have to repeat it for each of the receiver channels, leaving the
   previously calculated transmitters ON.»** Remate: una frase.
5. **Salvedad omitida (error 6)**, «La carga del micrófono», l. 505-512. En «Know the basics about
   phantom power» DPA da la misma regla con su propio ejemplo (100 Ω → 500-1.000 Ω; la entrada con
   fantasma tiene 3,4 kΩ) y añade que el dinámico, por su bobina, **«usually prefers a much higher
   input impedance»**. El tema usa un ejemplo propio (200 Ω) y omite la salvedad. Remate: añadir la
   salvedad (y, si se quiere, el ejemplo de DPA en lugar del propio).

Nota (no hallazgo): los 1,6 Mbit/s son la cifra de DPA, aunque 1,152 × 1,5 dé 1,73; el tema la
atribuye bien.

## Lente 2 · Cobertura del enunciado

Las siete materias (tipos, patrones polares, sensibilidad, colocación, soportes, inalámbricos y
accesorios) tienen rúbrica propia y en su orden. Preguntas en `28-T03-preguntas.md`: **entera 11 ·
a medias 2 · no 2**.

### Lagunas (2) · se amplía el tema

1. **Patrón del micrófono de cinta** (pregunta 2, «no»): la cinta es bidireccional por
   construcción; pregunta clásica de «tipos». El tema lo declara hueco. Remate (Opus): buscarlo en
   fabricante de cintas o manual universitario y añadirlo con cita; si no se confirma, sigue hueco.
2. **Micrófono de patrón variable (doble membrana)** (pregunta 3, «no»): ni se menciona. Remate
   (Opus): fuente de fabricante (p. ej., ficha técnica de un multipatrón) y una fila en «Tipos» o
   «Patrones»; si no se confirma, declararlo en «Lo que este tema no da».

### A medias (2, no obligan)

- Pregunta 9: impedancia típica de salida (remite al tema 2; sólo con fuente).
- Pregunta 12: patrón hemisférico de la capa límite (sólo con fuente).

## Lentes automáticas

`refutar_prosa.py`: 0 hallazgos. Índice: 45 entradas para 45 epígrafes, en orden (no se ejecutó
`indice.py`, que reescribe el fichero). Sin lentes de norma: el tema no cita norma jurídica.

## Otros ficheros tocados

Sólo `28-T03-preguntas.md` y este informe. El tema no se ha tocado.
