# Puesto 28 · Operador/a de Sonido · Tema 3 · Fase 5, remate

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/03-microfonia.md`. Entrada:
`28-T03-refutacion.md` (5 menores, 2 lagunas) y `28-T03-preguntas.md`.

**Resultado: el remate AMPLÍA contenido nuevo** (epígrafe nuevo «La cinta y el micrófono de varios
patrones», con dos fuentes nuevas). Toca fase 5 bis sobre los pasajes listados abajo. De unas
11.600 a unas 12.300 palabras.

## Fuentes (todas leídas el 25-09-2026)

| Fuente | Copia local | Qué sostiene |
|---|---|---|
| Royer Labs, «Ribbon Basics», royerlabs.com/ribbon-basic/ (nueva) | `fuentes/canal-sur/sonido/fabricantes/royer-ribbon-basics.txt` (y `.html`) | Cinta como dinámico; membrana a uno o dos lados de la placa; ocho natural, contrafase trasera, mínimos a 90°; unidireccionales de cinta fabricados; ocho de los multipatrón con electrónica activa |
| Neumann, página de producto U 87 Ai (nueva) | `fuentes/canal-sur/sonido/fabricantes/neumann-u87ai.txt` | Doble membrana heredada del U 67; tres patrones; gradiente de presión |
| DPA *Mic University* (releídas): guía inalámbricos partes 2, 3 y 6; *Troubleshooting*; guía básica; viento/lluvia; fantasma | copias del verificador | Hallazgos 1-5 |

Copia en `.txt` por curl y limpieza de etiquetas; negritas cotejadas con `negritas.py`: todas las
citas nuevas son literales (las 34 «no está» son rótulos, citas del Libro de estilo y del tema 6
de Cámara, ya así antes del remate).

## Hallazgos de exactitud

1. **Antenas ¼ λ / ½ λ**: comprobado (parte 6, 6.10: «at least 1/4 wavelength»; *Troubleshooting*
   2.05: «1/2 wavelength … 25 cm»). **Aplicado**: la fila da las tres cifras de DPA literales y
   que la de media onda cumple las tres.
2. **Espuma y directividad**: **el informe se equivocó**. La página de viento sí lo dice: «cardioid
   mic performance can suffer if foam covers the front and rear inlet to the diaphragm, which can
   change the actual directivity of the mic». **No se quita**; se sustituye la paráfrasis por la
   cita literal y se añade que algunas espumas dejan aire junto a las entradas.
3. **«Limitador obligatorio»**: **el informe se equivocó en parte**. DPA parte 3 dice «the analog
   transmitter is always equipped with a limiter circuit in the AF chain» (la parte 2, «often
   included», habla del emisor en general). Se sustituye por las dos citas literales de la parte 3
   (límite de ±75 kHz que no debe superarse y limitador siempre presente en el analógico).
4. **Repetir por canal de receptor**: comprobado en la guía básica; **aplicado** con cita literal.
5. **Carga del micrófono**: comprobado en «Know the basics about phantom power»; **aplicado**: se
   quita el ejemplo propio de 200 Ω (y su fila de cálculo en Trazabilidad) y se ponen el ejemplo de
   DPA (100 Ω → 500-1.000 Ω; 3,4 kΩ) y la salvedad del dinámico, literales.

## Lagunas

| Pregunta | Qué se hizo |
|---|---|
| 2 (cinta, ocho) | Ampliada: epígrafe nuevo, párrafo «La cinta es un ocho por naturaleza» (Royer). Queda entera |
| 3 (multipatrón, doble membrana) | Ampliada: párrafo «El condensador de varios patrones lleva doble membrana» (Royer, Neumann). Queda entera en lo esencial (doble membrana, patrón seleccionable); cómo se combinan las membranas no lo detalla ninguna fuente leída y se declara hueco |

A medias no obligatorias: la 9 mejora con el ejemplo de 100 Ω de DPA; la 12 (hemisférico) sigue
sin fuente, no se toca.

## Pasajes cambiados

- Portada: «Fuente» (Royer, Neumann) y «Extensión» (12.300).
- «Qué se puede preguntar»: cinta y multipatrón.
- «Los micrófonos por su transductor», tabla, fila «De cinta»: «es también dinámico».
- **Epígrafe nuevo** «La cinta y el micrófono de varios patrones» (tras «El transductor no es la
  directividad»).
- «La carga del micrófono»: final del párrafo (hallazgo 5).
- «Analógico y digital», fila «Cómo modula» (hallazgo 3).
- «Bandas, grupos y canales», procedimiento rápido (hallazgo 4).
- «La recepción, lo básico», fila «Antenas del receptor separadas» (hallazgo 1).
- «Contra el viento», tabla, fila «Espuma» (hallazgo 2).
- «Lo que este tema no da»: se quita el hueco de la cinta; se declara el de la combinación de
  membranas.
- «Trazabilidad»: filas nuevas Royer y Neumann; ampliadas las de fantasma, guía partes 1-6, guía
  básica y viento; quitada la carga de 1 a 2 kΩ del cálculo.
- Índice regenerado.

Antecedentes releídos en cada pasaje cambiado: «esa regla», «En otra de sus páginas», «las dos
fuentes leídas» tienen su antecedente delante.

## Lentes

`indice.py`: 46 epígrafes, índice rehecho. `refutar_prosa.py`: 0 hallazgos. `negritas.py`: citas
nuevas literales. Sin lentes de norma (el tema no cita norma jurídica).

## Otros ficheros tocados

Nuevos en `fuentes/canal-sur/sonido/fabricantes/`: `royer-ribbon-basics.txt`, `.html`,
`neumann-u87ai.txt`. Nada más fuera del tema y este informe.
