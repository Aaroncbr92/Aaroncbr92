# Esquema · Tema 8 del específico de Montaje de Equipos Audiovisuales · La cabeza caliente

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás ·
`[plan]` = plantilla oficial de respuestas, **sin documentación de fabricante que la contraste**.

**Siglas**: el conector de vídeo *Bayonet Neill-Concelman* (**BNC**); el conector
circular multipolo **LEMO**, que es una marca; la fibra óptica de la *Society of Motion Picture and
Television Engineers* (**SMPTE**); el conector de audio profesional de tres polos (**XLR**).

**Cabecera.** Enunciado: «4.4. Cabeza caliente: Componentes y cableado» · **2 preguntas** · **una
descansa sólo en la plantilla (72)**.

<!-- indice -->

## Índice

- [Qué es](#qué-es)
- [Los tres módulos](#los-tres-módulos)
- [Por qué los conectores van en el PAN](#por-qué-los-conectores-van-en-el-pan)
- [Las tres líneas y el par trenzado](#las-tres-líneas-y-el-par-trenzado)
- [El montaje, en orden](#el-montaje-en-orden)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es

- **CABEZA CALIENTE = CABEZA DE CÁMARA MOTORIZADA QUE SE MANEJA A DISTANCIA.** El operador está en un
  puesto de control, **no detrás de la cámara**.
- **POR QUÉ «CALIENTE»**: **va en el extremo de una máquina** —punta de grúa, carro de travelling,
  raíl de techo— **donde una persona no cabe o no debe estar**. En catálogo: *remote head*, *hot head*.

| | Cabeza de fluido | Cabeza caliente |
|---|---|---|
| **Quién mueve** | El brazo del operador | **MOTORES** |
| **Dónde está el operador** | Detrás de la cámara | **En un puesto de control remoto** |
| **Qué necesita** | Nivelado y equilibrado | **+ alimentación y línea de control** |

- **LAS TRES VENTAJAS**: **alcanza donde no cabe nadie** · **quita peso del extremo** · **un solo
  operador gobierna varias cámaras**.

## Los tres módulos

| Módulo | Eje | Qué hace |
|---|---|---|
| **PAN** | Vertical | **Gira a izquierda y derecha.** **ES EL MÓDULO DE ABAJO: EL QUE UNE AL SOPORTE** |
| **TILT** | Horizontal transversal | **Inclina arriba y abajo** |
| **ROLL** | El del eje óptico | **Balancea**, inclina el horizonte. **No lo llevan todas** |
| **Plataforma porta cámara** | — | **Sostiene la cámara.** **No es un eje: es la bandeja** |

- **EL ORDEN, DE ABAJO ARRIBA, SIEMPRE**: soporte → **PAN** → **TILT** → (**ROLL**) → plataforma →
  cámara.
- **LA REGLA QUE LO ORDENA TODO**: **el módulo de abajo carga con el peso de todo lo que tiene
  encima.** Por eso **el PAN es el grande**.

## Por qué los conectores van en el PAN

- **PREGUNTA 90** · **El módulo que permite la unión al soporte y en el que se sitúan todos los
  conectores es el MÓDULO PAN.**
- **EL PORQUÉ**: un cable que entrase por el TILT **cruzaría la articulación del PAN colgando**, y **el
  giro panorámico lo enrollaría en la columna hasta arrancarlo**.
- **QUÉ HAY EN SU PANEL**: **alimentación** · **línea de control** · **vídeo por BNC o fibra SMPTE** ·
  **audio por XLR** · **datos y red por RJ45** · **multipolo LEMO** para zoom y foco.
- **LAS TRES FALSAS SON PIEZAS REALES**: **plataforma porta cámara** (sostiene, no une) · **ROLL**
  (balancea) · **TILT** (inclina).

## Las tres líneas y el par trenzado

1. **ALIMENTACIÓN**: motores y, muchas veces, la cámara.
2. **LÍNEA DE CONTROL**: órdenes de *pan*, *tilt*, *roll*, zoom, foco e iris **de ida**, y posiciones
   de los ejes **de vuelta**.
3. **LÍNEA DE SEÑAL**: vídeo y audio hacia el control; retorno e intercomunicación hacia la cámara.

- **TRES CAMINOS PARA EL CONTROL**: **par trenzado** (barato, tiradas largas, instalación fija) ·
  **fibra** (distancia o ruido) · **inalámbrico** (máquina que no puede arrastrar cable).
- **POR QUÉ PAR TRENZADO Y NO COAXIAL**: es **transmisión serie diferencial tipo RS-422**: **la señal
  es la DIFERENCIA de tensión entre los dos hilos**, y **el ruido entra igual en los dos, así que la
  diferencia lo cancela**. **El trenzado sirve para que recojan la misma interferencia.**
- `[plan]` · **PREGUNTA 72** · **LONGITUD MÁXIMA DEL PAR TRENZADO HACIA EL CONTROL REMOTO: 1.000
  METROS.** Falsas: 2.000, 500 y 300.
- **LO QUE HAY QUE ENTENDER DE ESA CIFRA**: **el límite de una línea diferencial NO es absoluto: es un
  compromiso entre distancia y velocidad.** **A más metros, menos velocidad admisible.**
- **LOS TRES CUIDADOS DEL CABLEADO DE CONTROL**: **no compartir canaleta con líneas de fuerza** ·
  **rematar el apantallado en un solo extremo** (bucle de masa) · **dejar el bucle de servicio en la
  base, no en la punta**.

## El montaje, en orden

1. **Nivelar el soporte** —muchas cabezas calientes **no tienen bola niveladora propia**—.
2. **Anclar el PAN al soporte**, con la máquina descargada.
3. **Montar el TILT y, si lo hay, el ROLL.**
4. **Plataforma y cámara**, con óptica y accesorios: **se equilibra con la máquina completa**.
5. **Equilibrar el TILT** desplazando la cámara sobre la plataforma.
6. **Cablear por el PAN**: alimentación, control, señal.
7. **Comprobar recorridos en vacío** buscando dónde se tensa el cable: **ése es el límite real**.
8. **Encender y reglar** con el operador remoto.

- **EL ERROR CLÁSICO**: **dar por bueno el recorrido con la cámara apagada y sin cables.** **Con el
  cableado puesto el recorrido útil siempre es menor**, y el momento de descubrirlo no es el directo.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 72 | Longitud máxima del par trenzado al control remoto | a) 1.000 metros ✔ **·** sólo con la plantilla |
| 90 | Módulo que une al soporte y lleva los conectores | d) Módulo PAN ✔ |

**Las dos oficiales son correctas**, y **una descansa sólo en la plantilla**. · **Aviso de estudio**:
**el punto más corto del cuadernillo**, pero **la arquitectura PAN-TILT-ROLL se pregunta también en el
tema 4**: **estudiarla aquí sirve dos veces.**
