# Refutación del tema 7 del específico de Producción (Asistencia)

Un tema de **seis oficios**, ninguno de los cuales está nombrado en norma alguna, y sin embargo
**con norma real detrás de la mitad de la pregunta**. La refutación tenía que comprobar dos cosas
distintas: **que la parte con norma es literal** y **que la parte sin norma no aparenta tenerla**.

## Qué lente sirve aquí

| Lente | Contra qué | Resultado |
|---|---|---|
| Exactitud | III Convenio Colectivo | **12 negritas comprobadas, 7 no literales** |
| Modo verbal | III Convenio Colectivo | **0 hallazgos** |
| Documento | Convenio + acuerdo de modificación | **178 negritas, 133 no literales, 0 cifras huérfanas** |
| Prosa | El tema | **0 hallazgos** |

**Las siete no literales de la lente de exactitud son el comentario del tema sobre el artículo 38**
—«para qué sirve esto en el examen», «prueba que esos departamentos existen y son distintos entre
sí», «en cuál cae cada oficio»—, es decir, **lo que el tema dice de la norma**, no lo que dice la
norma. La cita del artículo, con sus trece ámbitos, **pasó entera**.

## El mismo cero de lente que en el tema 3, y ya con remedio conocido

La primera pasada de `refutar_exactitud.py` devolvió **2 negritas comprobadas**, cuando el tema
transcribe **la lista completa de los trece ámbitos ocupacionales**. La causa fue la misma que en
el tema del guion: el marcador iba **dentro de una frase** —«El **artículo 38 del III Convenio
Colectivo de la Corporación RTVE** establece los ámbitos ocupacionales»—, y a los marcadores
interiores la lente les da **sólo su frase**, para que una remisión no arrastre texto ajeno.

Reescrito para que **el marcador abra párrafo** —«**Artículo 38**, "Ámbitos ocupacionales":» y
debajo la cita—, la lente pasó de **2 a 12 comprobadas**.

Es la segunda vez en dos temas. **Queda como regla de escritura, no de herramienta**: cuando un
tema vaya a citar un artículo, **el marcador tiene que abrir el párrafo que lo cita**. Si va
enterrado en una subordinada, la cita que viene detrás **no se comprueba y no se queja**.

## Una fuente que sostiene la mitad, y el cuidado que eso exigió

El hallazgo del tema es que el convenio **sirve, pero no para lo que parecía**. Es fácil escribir
«el figurinista es del equipo de vestuario **según el convenio**», y sería falso: **el convenio no
nombra al figurinista**. Lo que hace es **probar que "Vestuario e imagen personal" es un ámbito
ocupacional distinto de "Decorados", de "Realización y edición audiovisual" y de "Información y
documentación"**, que son las otras tres opciones de la pregunta.

La distinción se ha escrito **tres veces** en el tema —en la tabla de niveles, en el epígrafe 1 y
en la trazabilidad— porque es exactamente el tipo de matiz que se pierde al resumir, y perderlo
convierte una plantilla en una norma.

**La comprobación**: los seis oficios se buscaron uno a uno en los cuatro documentos del convenio y
en el resto del corpus. **Cero apariciones**, incluidos *fotofija* y *escenógrafo*.

## Una tensión con la norma que el tema no resuelve, y hace bien

La respuesta oficial del escenógrafo —que supervisa **decorados, maquillaje, peluquería y
vestuario**— **no cuadra con la organización del convenio**, que separa esos ámbitos. El tema no
elige entre las dos: **da la respuesta del tribunal y señala la discrepancia**.

Es la misma decisión que se tomó con el enunciado invertido de la realidad aumentada en el tema 9 y
con el MPEG-2 del tema 11. La regla que ya se puede enunciar como práctica constante del proyecto:
**cuando la respuesta oficial y la fuente no coinciden del todo, se contesta como corrige el
tribunal y se escribe la discrepancia al lado**. Nunca se recorta la pregunta, y nunca se disfraza
la costura.

## Lo que este tema no puede sostener

- **Las seis respuestas son plantilla.** El convenio sostiene el mapa de departamentos, no los
  oficios.
- **La atribución del maquillaje y el vestuario al escenógrafo choca con la clasificación del
  convenio.** Declarado en el tema y aquí.
- **El lector de partituras y el *fixer* no son ocupaciones de plantilla**, sino encargos; su
  ausencia del convenio no es una laguna, es lo esperable.
- **Ninguna norma entra en productos de maquillaje**, de modo que lo del **pancake** es uso
  profesional y nada más.
