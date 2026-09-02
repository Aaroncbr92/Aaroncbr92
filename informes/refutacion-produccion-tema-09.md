# Refutación del tema 9 del específico de Producción (Asistencia)

El tema **peor servido de fuentes de todo el temario**, y por eso el que más falta le hacía pasar
por las lentes. Cuatro de sus veinte preguntas tienen norma detrás; dieciséis, no.

## Qué lente sirve aquí, y por qué

**Las lentes por artículo no sirven.** `refutar_exactitud.py` y `refutar_modo.py` trocean el tema
por «Artículo N» y contrastan cada trozo con su precepto. Este tema **no cita artículos**: cita
**una tabla de unidades** del RD 2032/2009, **un capítulo sin numeración de artículo** de la
ITC-BT-24 y **un cuadro de una recomendación** de la UIT-R. Correrlas devolvería «**0 comprobadas,
0 no literales**», el resultado engañoso contra el que avisa el apartado 10 del manual.

Se ha usado **la lente de documento**, contrastando cada negrita y cada cifra en negrita contra el
texto completo de las tres fuentes a la vez:

```
refutar_documento.py temas/produccion/09-escenografia-e-iluminacion.md \
    fuentes/corte-20221221/BOE-A-2010-927.md \
    fuentes/corte-20221221/BOE-A-2002-18099.preceptos.md \
    fuentes/normas-tecnicas/UIT-R_BT.601-7.txt
```

**Resultado**: **207 negritas comprobadas**, **179 no literales** y **4 cifras huérfanas**.

## Las cuatro cifras huérfanas

| Cifra | Dónde | Qué es |
|---|---|---|
| **2032** (×4) | «Real Decreto 2032/2009», en la ficha, en el epígrafe 1.1, en la tabla de datos y en la trazabilidad | **El número de la propia norma.** El volcado consolidado del BOE no repite el título de la disposición dentro de su cuerpo, así que su número no aparece en el texto. Verificado contra el identificador `BOE-A-2010-927` |

**Ninguna cifra del cuerpo quedó sin fuente.** Las que importan —**683 lm/W**, **540 × 10¹² Hz**,
los **50 V** de tensión límite convencional, los valores **1,0 / 0 / 1,0** del magenta— aparecen
las cuatro en su fuente y la lente las dio por buenas.

## Las 179 negritas no literales

Es una proporción altísima —el 86 %—, y **es la medida exacta del problema de este tema**: la
mayor parte de su texto **no puede ser literal de ninguna fuente porque no hay fuente que copiar**.
Revisadas una a una, se reparten así:

- **Rótulos propios del tema** y encabezados de tabla: «Nivel de la fuente», «Aviso de nivel»,
  «La pregunta del examen es la del flujo luminoso».
- **Definiciones de oficio** que el tema redacta y **marca como tales**: tronera, limbo, forillo,
  alzado, utilería, props, practicable, banner, dimmer, set y decorado.
- **Enunciados y opciones del examen** citados para explicarlos: «Aletas metálicas negras con
  bisagras…», «Piezas estructurales de madera o metal…».
- **Nombres comerciales**: Astera Titan Tube, Mo-sys, Star Tracker, ORAD.
- **Las advertencias del propio tema** sobre lo que no puede sostener, que por definición no están
  en ninguna norma.

**Ninguna paráfrasis se presenta como cita**, y ese es el punto: la lente no dice que el tema esté
mal, dice **cuánto de él se apoya en algo que no es una norma**. Esa cifra está escrita en la ficha
del tema y en la tabla del epígrafe 4, para que el opositor la vea antes de estudiarlo.

## Lo que la lente de prosa encontró

`refutar_prosa.py` devolvió **seis hallazgos** en el primer paso, todos de siglas sin presentar.
Corregidos: **RD** (real decreto), **UIT-R** (Sector de Radiocomunicaciones de la Unión
Internacional de Telecomunicaciones), **LED** (diodo emisor de luz), **ALTA/BAJA** en versalitas
—que la lente leía como siglas y se pasaron a caja normal— y **ORAD**.

**El caso de ORAD merece nota**, porque es un fallo del que hay que aprender. La primera corrección
escribió «el sistema de la casa **ORAD** (hoy integrado en Avid)»: un paréntesis, pero **detrás** de
la sigla, y la lente exige que la presentación vaya **delante**. Al ir a darle la vuelta apareció el
problema de fondo: **«hoy integrado en Avid» no salía de ninguna fuente leída**. Era un dato de
memoria colado en una corrección de estilo, exactamente lo que prohíbe el apartado 1 del manual. La
redacción final dice lo único verificable —**«y (así lo escribe la plantilla, sin desarrollarlo)
ORAD»**— y de paso satisface a la lente. **Segundo paso: 0 hallazgos.**

La lección: *una corrección de forma es tan capaz de introducir un dato sin fuente como una
redacción nueva, y nadie la mira con la misma desconfianza.*

## Dos correcciones de escritura

- **Una «а» cirílica** se había colado en la palabra «visera» del epígrafe 1.6. No la marca ninguna
  lente —el texto se ve idéntico— y rompe cualquier búsqueda sobre el tema. Se buscó a propósito,
  recorriendo el fichero carácter a carácter en busca de caracteres griegos o cirílicos, y se
  cambió. **Conviene repetir esa comprobación en cada tema nuevo.**
- **«son las balastos»** → **«son los balastos»**. Concordancia.

## Un error del examen que el tema no arregla, pero declara

La pregunta **77 · 78** dice: «¿cómo se le denomina a la tecnología de **superponer una imagen real
sobre el entorno virtual**?». La respuesta oficial es **realidad aumentada**, y es la única posible
entre las cuatro opciones. Pero **el enunciado tiene los términos invertidos**: la realidad
aumentada superpone **lo virtual sobre lo real**.

Aquí el manual manda no recortar la pregunta. Lo que el tema hace es **contestarla como el tribunal
la corrige y decir en el mismo párrafo que el enunciado está al revés**, porque un opositor que
razone bien se bloqueará ante ella y necesita saber de antemano que el bloqueo no es suyo.

## Lo que este tema no puede refutar

Y conviene que quede escrito, porque es la parte que ninguna lente alcanza:

- **Cuatro respuestas dependen de fichas de fabricante que no se han podido consultar.** No hay
  contra qué contrastarlas. La única autoridad que las sostiene es **la plantilla oficial**, que
  dice qué dio por correcto el tribunal, no qué es verdad. Si la próxima convocatoria cambia de
  proveedor, **caducan**.
- **La regla del practicable no está en el reglamento eléctrico.** El tema pone el marco normativo
  —contactos indirectos, masas, puesta a tierra, 50 V— y **dice expresamente** que la aplicación
  concreta al practicable es práctica profesional. Es lo más honesto que se puede hacer con esa
  pregunta sin inventar un precepto.
- **Doce definiciones de vocabulario** no tienen ni pueden tener norma. Se marcan una a una en la
  tabla del epígrafe 4, columna «Nivel».
