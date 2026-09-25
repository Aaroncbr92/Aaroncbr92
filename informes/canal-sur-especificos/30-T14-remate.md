# Puesto 30 · Tema 14 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Fuente: `30-T14-refutacion.md` y
`30-T14-preguntas.md`. Cada corrección comprobada en la fuente antes de aplicarla.

## Pasajes cambiados

1. **l. 84-85** (menor 1, segunda ronda). «Donde el Libro de estilo no llega (la última hora) se usa
   el Manual de estilo de RTVE» contradecía que el propio tema cita LE 3.9.1 (l. 170, «la inclusión de
   un elemento de última hora») y LE cap. 6, p. 88 («informaciones de última hora»). Comprobado el
   pasaje de p. 88 en `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` (l. 3063-3065).
   Aplicada la propuesta del informe: «Donde el Libro de estilo no desarrolla la noticia de última
   hora de gran repercusión, se usa el Manual de estilo de RTVE…».
2. **l. 493-494** (menor 2, segunda ronda; laguna, se amplía). «Lo que este tema no da» no remitía a
   la regla de horarios y turnos de cabina / entrega escalonada (LE cap. 6, p. 88), que sí desarrolla
   el tema 9 (§ «Tiempos, cabinas y entrega escalonada», comprobado en el fichero del tema 9,
   l. 253-257). Añadida una frase de remisión, sin tocar el resto del epígrafe.

No aplicadas: la observación sin hallazgo sobre XDCAM (l. 22) se deja tal cual, como recoge el propio
informe («inocuo»; no es un error, es una precisión opcional). Los cuatro menores de la primera ronda
(capítulos 3-8, BOJA en siglas, glosa de 6.5.1, atribución del aviso) ya estaban aplicados en el
tema antes de este remate; comprobado en la fuente el estado actual, no se repite el cambio.

## Comprobación de las lentes

- `python3 herramientas/indice.py` sobre el tema: 5.435 palabras, 26 epígrafes. Extensión de ficha
  («5.300 aproximadamente») sigue siendo correcta a efecto de orden de magnitud; no se toca.
- `python3 herramientas/refutar_prosa.py` sobre el tema: 1 hallazgo (sigla CSTV), el mismo falso
  positivo que documentó la refutación (se presenta en la misma frase, unas palabras después de donde
  la herramienta marca la primera aparición). Tema técnico sin norma: no proceden `negritas.py`,
  `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

- `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/14-urgencia-directos-ultima-hora-versionado.md`
  (los dos pasajes anteriores).
- Este informe.

## Respuesta al coordinador

Tema 14 rematado: 2 pasajes corregidos de la segunda ronda de refutación (l. 84-85, contradicción
interna sobre el alcance del Libro de estilo en última hora; l. 493-494, remisión añadida al tema 9
sobre horarios de cabina y entrega escalonada). Ambos comprobados en fuente antes de aplicar. Los
cuatro menores de la primera ronda ya constaban aplicados. `indice.py`: 5.435 palabras, 26 epígrafes.
`refutar_prosa.py`: 1 falso positivo ya documentado (sigla CSTV). Sí amplié contenido nuevo (frase de
remisión al tema 9 por laguna de remisión, no de contenido).
