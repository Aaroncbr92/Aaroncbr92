# Realizador/a (puesto 33) · Tema 9 · Refutación (fase 4)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/33-realizador-a/09-mezclador-recursos-realizacion.md`
(1.153 líneas). Leídos: ENCARGO, enunciado del puesto 33, informes de redacción y verificación del T9.
No se reverifica lo «Copiado del común» ni lo «Copiado de RTVE sin cambios» (lista del informe de
redacción); la cobertura mira el tema entero.

## Lente 1 · Exactitud (lo nuevo y lo adaptado)

Fuentes releídas el 24-09-2026: `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt`,
`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` (RD 1680/2011), `BOE-A-2024-10685.txt`
(RD 500/2024: título y fecha, «de 21 de mayo»), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`
(copia con ligaduras normalizadas en el scratchpad).

- `negritas.py` contra ATEM, RD y LE: 109 negritas, 9 no halladas, las mismas que en la
  verificación (8 del común sin volcado y la de 3.16.1, partida por el salto de página 57-58;
  comprobada a mano, l. «3.16.1. Redondeo…» / p. 58).
- RD 1680/2011: 0905 RA 1 f) (l. 636), RA 5 y c)/e) (l. 663-669), RA 6 b)/d)/e) (l. 673-676),
  «Tipos de grabación…» (l. 685), bloques «Realización de programas de televisión en multicámara»
  (l. 691-699) y «Mezcla de fuentes…» (l. 707-713), «Monitorizado en sistemas multipantalla…»
  (l. 720, bloque de operaciones auxiliares; el tema lo da como contenido del módulo, correcto);
  0910 RA 4 b) y g) (l. 1232, 1237). Todo en su RA, criterio y bloque.
- Manual ATEM, paráfrasis sin negrita cotejadas: transición animada «en los modelos ATEM 1 M/E y
  2 M/E» (l. 5400); AFV de la salida de audio principal con el FTB (l. 1805); 18 formas y alfa
  generado por el mezclador (l. 6183-6186); SuperSource en modelos con más de un M/E (l. 1824);
  ocho ventanas pequeñas y Constellation 8K con 4, 7, 10, 13 o 16 fuentes (l. 1660, 2728-2735);
  100 espacios de macro (l. 6810); limpia 1 y 2 (l. 6644-6648); TIE y señal limpia (l. 1777-1780);
  alfa por auxiliar sólo en 4 M/E Broadcast Studio 4K y Production Studio 4K, «algunos de sus
  modelos» (l. 5797); nombres de fuente y su contradicción (l. 707, 2773-2774). Correctos.
- Libro de Estilo: 3.16 a 3.16.2 (pp. 57-58, la «cama» de audio está en el texto de 3.16.2),
  6.5.1 y 6.5.2 (p. 93; «Tiene capacidad y autoridad…» y «funcionen con armonía…» son de 6.5.2,
  «el mismo epígrafe» del tema es correcto), 8.6.1 puntos 4 y 9 (p. 122). Literales.

### Hallazgos

| # | Línea | Tipo | Hallazgo | Propuesta |
|---|---|---|---|---|
| 1 | 509 | Menor (9, precisión) | «mirando el vectorscopio con barras de color como imagen»: el manual (l. 6055-6057, «Ajuste de parámetros mediante un vectorscopio») dice **«usando las barras de color como imagen de fondo y viendo el resultado en un vectorscopio»**. Tal como está, parece que las barras se ven en el vectorscopio. | «Esos parámetros se pueden ajustar poniendo las barras de color como imagen de fondo y mirando el resultado en un vectorscopio.» |

Graves: 0.

## Lente 2 · Cobertura del enunciado

Las once materias del enunciado (transiciones, efectos, incrustaciones, chroma, DVE, multipantalla,
macros, señales, keyers, grafismo en directo, criterios de uso narrativo) tienen epígrafe propio en su
orden, con aplicación práctica al final. Preguntas en `33-T09-preguntas.md`: 12 enteras, 1 a medias,
2 no.

### Lagunas

1. **Parámetros de la cortinilla** (preguntas 13, «no», y 14, «a medias»). El tema define la
   cortinilla y la da en la tabla de modos, pero no dice cómo se ajusta, que es lo que se pregunta en
   práctica. Manual ATEM, «Cortinillas» y «Opciones para fundidos» (l. 4719-4781, pp. 992-993 según
   los marcadores): pasos (**«Gire el mando para seleccionar la forma de la cortinilla.»**,
   **«Seleccione la fuente para el borde.»**); **«Es posible emplear cualquier fuente del mezclador
   para el borde de una cortinilla. Por ejemplo, se puede utilizar una imagen del reproductor
   multimedia en un borde ancho para destacar una marca o un patrocinador.»**; y los parámetros
   Simetría (**«Se utiliza para controlar la relación de aspecto de la forma geométrica. Por ejemplo,
   ajustando este valor, es posible transformar un círculo en una elipse.»**), Posición, Invertir
   dirección (**«Al invertirla, la transición comienza desde los bordes de la pantalla hacia el
   centro.»**), Alternar (**«la dirección de la transición alterna entre normal e inversa cada vez que
   se ejecuta.»**), Ancho (**«Permite ajustar el ancho del borde.»**) y Atenuación (**«Permite ajustar
   la definición de los bordes.»**). Si cabe, la cortinilla con gráficos (l. 4888-4910): pancarta
   vertical **«cuyo ancho no supere el 16 % del ancho total de la pantalla»**. Lugar: § 1, tras el
   párrafo de la cortinilla; y corregir en § 2 «de relleno de un borde» añadiendo que el borde admite
   cualquier fuente.
2. **La máscara rectangular de las llaves** (pregunta 15, «no»). Manual ATEM, «Máscaras»
   (l. 6380-6386): **«Las diferentes funciones para combinar imágenes cuentan con una máscara
   rectangular ajustable que puede utilizarse para eliminar bordes ásperos y otros artefactos de la
   señal. Al modificar el largo o el ancho de dicho rectángulo, es posible cubrir diversas partes de
   la imagen. Asimismo, se puede emplear como una herramienta creativa para ocultar diversos
   elementos.»**; en las opciones de la llave lineal y de luminancia, **«Permite crear una máscara
   rectangular que puede ajustarse modificando los campos Superior, Inferior, Izquierda y
   Derecha.»** (l. 5914-5916). Lugar: § 3 «Clip y ganancia» o § 4 «Los ajustes del croma»; uso de
   oficio en croma: tapar lo que queda fuera del ciclorama.

## Ficheros tocados

- Creados: `informes/canal-sur-especificos/33-T09-preguntas.md` y este informe. Copia normalizada del
  Libro de Estilo en el scratchpad. El tema no se ha modificado.
