# Puesto 28 · Operador/a de Sonido · Tema 1 · Fase 4, refutación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/01-fundamentos-de-sonido.md`. No corrijo:
sólo informo. Preguntas en `28-T01-preguntas.md`.

Alcance de la exactitud: se saltan los pasajes listados en `28-T01-redaccion.md` como «Copiado del
común» (4) y «Copiado de RTVE sin cambios» (15). La cobertura mira el tema entero.

## Fuentes releídas

| Fuente | Fecha de lectura | Resultado |
|---|---|---|
| RD 2032/2009 (BOE-A-2010-927), `boe.py precepto` bloque `civ` (redacción única, vig. 22-03-2010) | 25-09-2026 | Apartado 4 literal (tres citas del tema); título de la tabla 8 «Otras unidades no pertenecientes al SI de aplicación exclusiva en sectores específicos»; fila del bar; nota (i) literal. Conforme |
| RD 2032/2009, bloque `cii` (vig. 30-04-2020, pub. 29-04-2020, BOE-A-2020-4707) | 25-09-2026 | Tabla 3 (título, hercio con nota (d), pascal); nota (d) cortada tras «periódicos» sin alterar el sentido. Portada y trazabilidad conformes |
| DPA «Polarity, phase and delay», DPA «Comb filtering», Rane RN155, RTW «Multi Correlator» | 25-09-2026, en los extractos literales de `28-investigacion-A-fundamentos.md` § 1.1-1.3, 13.7 (las webs las cotejó el verificador el mismo día) | Citas conformes; una salvedad omitida (hallazgo 1) |

Cálculos rehechos: tabla de periodos y λ; 20 × log 10⁶; tabla de aritmética (× 1,41 → 1,5 dB en
potencia); 6,02 dB/bit; 1 ms → 360°/180°/90°; 50 ms → 17 m; modo de 50 Hz a 3,4 m. Correctos.

## Hallazgos de exactitud

Graves: ninguno. Menores: 2.

1. **Error 6 (salvedad omitida), «Polaridad no es fase», líneas 340-342.** El tema generaliza a
   «el micrófono en conexión balanceada» que una presión creciente da tensión positiva creciente en
   la patilla 2. La fuente (DPA-PPD) lo limita: «This is true for balanced condenser microphones for
   professional audio …, while dynamic microphones behave a little differently». Propuesta: añadir
   la salvedad (condensador profesional; los dinámicos se comportan algo distinto).
2. **Inexactitud conceptual, «Polaridad no es fase», línea 333-334.** «un desfase de 180° por
   retardo sólo lo es a una frecuencia» es falso: un retardo t da contrafase en f = 1/(2t) **y en sus
   múltiplos impares** (1 ms: 500, 1.500, 2.500 Hz…), que son precisamente los huecos «regulares» del
   filtro en peine que el propio tema describe en la línea 349. Choca con el tema y hace fallar la
   pregunta 8. Propuesta: «sólo a unas frecuencias concretas (la de medio periodo y sus múltiplos
   impares)». Cálculo; no requiere fuente nueva.

Sin hallazgos en: citas del RD (literales y bien situadas), siglas (todas presentadas; «Unión
Europea de Radiodifusión» va con el nombre completo), remisiones internas (temas 2, 3, 5, 10, 11,
13, 14, 16), redacción vigente, negritas (sólo literales de fuente).

## Cobertura del enunciado

Las ocho rúbricas (ondas, frecuencia, amplitud, fase, dinámica, timbre, audición, acústica básica)
tienen epígrafe propio y en el orden del enunciado. Preguntas: **8 enteras, 3 a medias, 4 no**.

Lagunas (la fase 5 decide si hay fuente con la que ampliar; si no, se mantiene el hueco declarado):

1. **Onda longitudinal** (pregunta 1): el tema no dice que el sonido en el aire es onda longitudinal
   de compresiones y enrarecimientos. Es lo más básico de «ondas».
2. **Velocidad del sonido según el medio** (pregunta 3): declarada hueco; un test puede preguntar el
   orden aire < agua < sólidos sin cifras exactas.
3. **Fisiología del oído** (pregunta 12): declarada hueco; es núcleo de «audición».
4. **Localización biaural y efecto de precedencia o Haas** (pregunta 13): declarados hueco; enlazan
   con estéreo y con la frontera de los 50 ms que el tema ya da.
5. **Envolvente en el timbre** (pregunta 11): el tema lo liga sólo a los armónicos; falta el papel
   del ataque y los transitorios.
6. **Aislamiento frente a acondicionamiento** (pregunta 15): la acústica básica no separa impedir que
   entre el ruido (masa, estanqueidad) de tratar la sala (absorción, difusión). Menores de cobertura
   (no cuentan como laguna): la difracción no se nombra aunque se explique la «sombra»; la distancia
   crítica tampoco, aunque se describa.

## Otros ficheros tocados

Sólo `28-T01-preguntas.md` y este informe. El tema no se ha modificado.
