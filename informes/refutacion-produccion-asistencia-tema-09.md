# Refutación del tema 9 del específico de Producción (Asistencia)

El tema **peor servido de fuentes de todo el temario**, y por eso el que más falta le hacía pasar
por las lentes. Cuatro de sus veinte preguntas tienen norma detrás, tres tienen ficha de fabricante
y trece no tienen ninguna de las dos cosas. **El hallazgo más caro de esta refutación no lo dio
ninguna lente**: lo dio volver a llamar a una puerta que se había dado por cerrada.

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
    fuentes/normas-tecnicas/UIT-R_BT.601-7.txt \
    fuentes/fabricantes/Astera_Titan-Tube_ficha.txt \
    fuentes/fabricantes/Astera_Titan-Tube_informe-62471.txt \
    fuentes/fabricantes/Mo-Sys_StarTracker-Max_ficha.txt \
    fuentes/fabricantes/Mo-Sys_camera-tracking_indice.txt
```

**Resultado**: **252 negritas comprobadas**, **217 no literales** y **4 cifras huérfanas**. Las
cuatro últimas fuentes se incorporaron a mitad de la refutación, por lo que se dirá.

## Las cuatro cifras huérfanas

| Cifra | Dónde | Qué es |
|---|---|---|
| **2032** (×4) | «Real Decreto 2032/2009», en la ficha, en el epígrafe 1.1, en la tabla de datos y en la trazabilidad | **El número de la propia norma.** El volcado consolidado del BOE no repite el título de la disposición dentro de su cuerpo, así que su número no aparece en el texto. Verificado contra el identificador `BOE-A-2010-927` |

Hubo una quinta, y **cambió el texto**. El párrafo que cuenta cómo se recuperaron las fichas decía
«un **404** o un **403** no son la prueba de que un documento no exista», y la lente marcó el **403**
como cifra sin fuente. Tenía razón por accidente: **un código de estado de un servidor no es un dato
que el tema pueda sostener con una fuente**, es una anécdota del método. Se reescribió sin cifras
—«un **error del servidor** no es la prueba de que un documento no exista»—, que además se entiende
sin saber qué es un 403.

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

## El hallazgo que ninguna lente da: una fuente dada por cerrada que estaba abierta

Este tema se cerró declarando que **las cuatro fichas de fabricante no se habían podido consultar**:
«los servidores devolvieron error en todas las rutas probadas». Al empezar el tema siguiente hizo
falta la ficha de otro producto, se volvió a intentar **con más cuidado**, y salió a la luz que
**tres de las cuatro estaban disponibles todo el tiempo**. Las causas, las dos evitables:

| Fabricante | Lo que se vio antes | Lo que pasaba en realidad |
|---|---|---|
| **LiveU** | `liveu.tv/products/lu300s` → **no encontrado** | La ruta buena es **`liveu.tv/lu300s`**, que responde con la ficha entera. Un «no encontrado» dice que **esa ruta** no existe, **no** que el documento no exista |
| **Astera** | `astera-led.com` → **prohibido** | El servidor **filtra por agente de usuario**. La misma petición con un agente de navegador corriente devuelve la página, la ficha del Titan Tube y hasta el informe de ensayo de seguridad fotobiológica |
| **Mo-Sys** | dado por perdido con los otros | `mo-sys.com` responde sin más. La página del *StarTracker* de siempre está retirada, pero **el catálogo de seguimiento de cámara y la ficha del StarTracker Max están publicados** |
| **ORAD** | sin ficha | **Sigue sin ficha.** Ésta sí era verdad |

**Por qué esto es un fallo del método y no mala suerte.** El apartado 5 del manual dice que *el que
detecta se equivoca*: quien encuentra el problema es quien lo ha creado. Aquí el problema era una
**conclusión negativa escrita sin comprobarla**. Y una conclusión negativa es la más cara de todas,
porque **cierra la búsqueda**: nadie vuelve a mirar donde ya está escrito que no hay nada. El tema
llegó a estar cerrado, con su esquema, sus dos informes y su acta, sobre una afirmación falsa.

**La regla que queda, y que se aplica desde aquí a todo lo que falta:** antes de escribir «no se ha
podido consultar» hay que haber probado **al menos dos rutas** y **un agente de usuario de
navegador**. Con esa regla puesta se volvieron a probar las tres fuentes que seguían declaradas
inalcanzables, y esta vez la declaración se sostiene: **EBU/UER** responde «prohibido» **también**
con agente de navegador; **DCI** responde, pero es una aplicación de JavaScript que **no sirve
ningún documento por ruta estática**; y de la **AES10** sólo hay la línea de identidad, porque el
texto **sigue tras el muro de pago**.

**Lo que el tema ganó con las tres fichas** está detallado en el informe de cobertura: Mo-Sys y
StarTracker resultaron ser **la misma casa** —el examen pregunta dos veces por el mismo fabricante—,
el enunciado del sensor al techo resultó ser **la ficha palabra por palabra**, y el adjetivo
«**alemana**» de la respuesta oficial, que la primera versión del tema había quitado por no poder
confirmarlo, **tiene ahora documento**: el informe de ensayo identifica a **Astera LED Technology
GmbH, de Múnich**.

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

- **Tres respuestas dependen de fichas de fabricante**, que ahora **sí** se han leído y guardado. La
  cautela no desaparece, sólo cambia de forma: **una ficha no es una norma**. No hay redacción
  consolidada ni fecha de vigencia; hay una página que el fabricante reescribe cuando quiere. Por
  eso van fechadas al **2 de septiembre de 2026**, y por eso **caducan** si el producto se retira o
  el tribunal cambia de proveedor.
- **Una respuesta —la de ORAD— no tiene ninguna ficha.** La única autoridad que la sostiene es la
  plantilla oficial, que dice qué dio por correcto el tribunal, no qué es verdad.
- **La regla del practicable no está en el reglamento eléctrico.** El tema pone el marco normativo
  —contactos indirectos, masas, puesta a tierra, 50 V— y **dice expresamente** que la aplicación
  concreta al practicable es práctica profesional. Es lo más honesto que se puede hacer con esa
  pregunta sin inventar un precepto.
- **Doce definiciones de vocabulario** no tienen ni pueden tener norma. Se marcan una a una en la
  tabla del epígrafe 4, columna «Nivel».
