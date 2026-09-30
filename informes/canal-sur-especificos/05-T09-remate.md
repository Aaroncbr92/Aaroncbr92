# Ayudante de Realización (05) · Tema 9 · Fase 5 · Remate

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/09-mezcladores-efectos-transiciones-senalizacion.md`
Fecha: 30-09-2026 (el encargo computado fija «hoy» en el 24-09-2026; manda la del sistema).
Entrada: `05-T09-refutacion.md` (3 hallazgos menores, 1 nota, 1 laguna) y `05-T09-preguntas.md`.
Fuentes releídas hoy: `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt` (l. 768-773, 1015-1032,
7655-7670, 9230-9249). Fuente nueva, descargada y leída hoy: Recomendación UIT-R BT.2111-3 (05/2025),
versión en español, `fuentes/normas-tecnicas/UIT-R_BT.2111-3.pdf` y `.txt` (la vigente según la
página de la UIT; la URL de la edición -2 que se probó primero ya no sirve).

**Amplió contenido nuevo: sí** (barras HDR). Procede 5 bis sobre los pasajes 1, 2 y 5.

## Correcciones, comprobadas en la fuente

1. **Hallazgo 1 (vías del piloto) · aplicado.** Confirmado: el pasaje de la puesta en marcha
   (l. 1017-1023) dice que el piloto se enciende verde y rojo, no por dónde va; el retorno SDI sólo
   se nombra para la llamada (l. 1029-1030) y el control de cámara (l. 771-772). Pasajes cambiados
   (epígrafe 7, «Cómo llega el piloto a la cámara y a los monitores»):
   - «una de cuatro vías» → «una de tres vías»; tabla sin la fila «Retorno SDI»; la fila «Datos en la
     señal» dice ahora «dentro del programa que el mezclador manda a las cámaras».
   - Párrafo «Por el retorno SDI» fundido con «Como datos dentro de la señal»: nuevo arranque «Como
     datos dentro de la señal que vuelve a la cámara. Con cámaras del mismo fabricante, el manual
     cuenta en la puesta en marcha cómo se enciende su piloto:»; tras la cita, «Ese pasaje no dice por
     qué cable llega el piloto; el manual sí dice que por la señal SDI de retorno van la llamada […] y
     el control de las cámaras: **«El mezclador permite controlar unidades URSA Mini y Blackmagic
     Studio Camera mediante la señal SDI de retorno.»**»; al final del protocolo embebido, «Que el
     piloto de las cámaras del fabricante viaje con este protocolo en la señal de retorno es lo que el
     anexo describe en general, pero el manual no lo dice expresamente de sus cámaras.»
   - «Qué se puede preguntar»: «(contacto, retorno SDI, señal, red)» → «(contacto, señal de vuelta a
     la cámara, red)».
   - Trazabilidad, fila del manual ATEM (señalización): «vías del piloto (contacto, datos en la señal
     de vuelta a la cámara); control de cámara por la señal SDI de retorno».
2. **Hallazgo 2 (salvedad) · aplicado.** Literal en l. 7664-7667. «y con varias se reparten los
   pilotos: «se pueden asignar…» → «y en los ATEM de dos y cuatro bancos se reparten los pilotos:
   **«Si se conecta un dispositivo GPI and Tally Interface a un mezclador ATEM 2 M/E o 4 M/E, es
   posible asignar distintas luces piloto a cada unidad a través del programa ATEM Setup. Por
   ejemplo, se pueden asignar las luces piloto 1-8 […]»**».
3. **Hallazgo 3 (Trazabilidad del Libro de Estilo) · aplicado.** Fila: «8.6.1 (p. 122); 6.5, sólo
   como remisión | Vestuario ante el croma; el criterio sobre los recursos en informativos, que se
   remite». Comprobado en el tema: sólo 8.6.1 se usa en el cuerpo; 6.5 aparece en «no da».
4. **Nota (Advertencia) · aplicada.** «El Libro de Estilo de Canal Sur da el criterio de la casa…» →
   «Del Libro de Estilo de Canal Sur se toma aquí lo que pide al vestuario ante el croma; su criterio
   sobre el uso de los recursos en los informativos lo desarrolla el temario del Realizador/a.»

## Laguna (pregunta 15) · ampliada

5. **«Los generadores de señales del control»**: la frase «La norma que define las barras de color
   de alta definición no se ha podido leer…» se sustituye por un párrafo sobre la **Recomendación
   UIT-R BT.2111-3 (05/2025)**: título, cometido (carta de barras para HDR según BT.2100), sistemas
   HLG y PQ con sus tres cartas, valores de 10 y 12 bits, barras al 100 % y al 75 %, los cuatro
   objetivos (Anexo 1, ap. 2), la salvedad del PLUGE (sigla que la recomendación no desarrolla), el
   «recomienda además» sobre la edición implementada por el fabricante y la referencia normativa a
   BT.471 (no leída). Cierra: «La BT.2111 no es la norma de las barras de alta definición sin HDR:
   esa no se ha podido leer para este tema, y no se cita.»
   - **La clave de la pregunta 15 no cuadra con la fuente**: BT.2111 es la carta HDR, no la de HD. No
     se recorta la pregunta; el tema contesta ahora la parte HDR y declara lo que falta. Manda la fuente.
   - «No da»: «La norma de las barras de color de alta definición sin HDR, la Recomendación UIT-R
     BT.471 y la de las cartas de ajuste que no son de HDR: no se han podido leer. De la carta HDR
     (UIT-R BT.2111-3) se dan su objeto, sus sistemas y sus usos; no sus valores de código ni las
     medidas de cada barra.»
   - Ficha: BT.2111-3 añadida a «Fuente» y a «Redacción que se estudia» (leída el 30-09-2026);
     «Qué se puede preguntar» añade «qué recomendación fija la carta de barras de la televisión de
     elevada gama dinámica (HDR)»; Trazabilidad, fila nueva de BT.2111-3; Extensión 16.900 palabras.
   - Pregunta 14 (transporte de IS-07): no se amplía; el texto de IS-07 sigue sin leerse y está
     declarado en «no da».

Antecedentes releídos en cada pasaje cambiado: «Ese pasaje» (la cita de la puesta en marcha),
«este protocolo» (el Embedded Tally), «La recomendación» y «La BT.2111» (la BT.2111-3 nombrada
antes): todos tienen su antecedente.

## Lentes

- `indice.py`: índice regenerado, 64 epígrafes, 16.888 palabras (la portada es manual: no está en
  `portadas.tsv`, igual que antes).
- `negritas.py` (ATEM, BT.2111-3, TSL, IMS077_3, RD 1680/2011): 180 cotejadas, 10 no halladas, las
  mismas 10 de texto copiado del común (Adobe, Mateu Torres, Libro de Estilo 8.6.1). Todas las negritas
  nuevas, halladas.
- `refutar_prosa.py`: sin frases repetidas ni negritas rotas; siglas: DVE (enunciado), GREEN/AMBER
  (literal TSL), PLUGE (declarada no desarrollada por la fuente). HDR, HLG y PQ, presentadas.
- `negritas`/`refutar_exactitud`/`refutar_modo` por artículo: no aplican a lo cambiado (sin norma
  articulada).

## Ficheros tocados

- El tema 09 (pasajes arriba).
- Creados: `fuentes/normas-tecnicas/UIT-R_BT.2111-3.pdf` y `.txt`; este informe.
- `fuentes/normas-tecnicas/README.md`: una fila para BT.2111-3.
