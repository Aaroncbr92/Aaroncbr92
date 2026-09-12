# Cuaderno de pendientes · Correos

Cualquier sesión anota aquí lo que detecte, aunque no lo corrija en el momento.
Lo aplicado se tacha con su fecha, **no se borra**: el histórico es lo que deja
ver si un mismo error se repite.

Cada entrada, cinco campos:

- **Dónde**: tema y epígrafe.
- **Qué dice** hoy.
- **Qué debería decir**, ya redactado para pegar.
- **Fuente**: el precepto en su redacción vigente, citado literal. Si no se ha
  comprobado, se dice.
- **Gravedad**: cambia la respuesta / induce a error / menor.

---

## Abiertos

### 2026-09-12 · Falta el documento de referencia, que es lo que se examina

**Dónde.** Nueve de los doce temas: 3, 4, 5, 6, 7, 8, 9, 10 y 11.

**Qué pasa.** El ANEXO III de las bases no es el temario, es su índice, y remite a un documento de
referencia que Correos publica gratis en la zona de convocatorias de su web para las personas
admitidas al proceso. Desde aquí no se ha podido descargar: la zona está detrás del Portal de
Gestión de Convocatorias (`procesosmasivos.correos.es`).

**Qué debería pasar.** Que ese documento esté volcado en `fuentes/` con su fecha de descarga, como
está el Manual de estilo de RTVE.

**Fuente.** El propio ANEXO III, que lo dice con todas sus letras: «Este documento de referencia se
publicará en la Web de Correos, a lo largo del mes de noviembre de 2022, de forma gratuita y
estarán a disposición de las personas interesadas en el proceso.»

**Gravedad.** Bloqueante para nueve temas de doce. No induce a error a nadie porque no se ha escrito
nada de ellos, y ésa es justamente la decisión: no se escriben hasta tener la fuente.

### 2026-09-12 · El banco de preguntas está vacío

**Dónde.** `banco/`.

**Qué pasa.** No hay ni un cuadernillo de convocatorias anteriores con su plantilla. En RTVE el
banco es lo que permite calibrar qué pesa cada tema y comprobar que el cuerpo contesta lo que se
pregunta; aquí esa comprobación no se puede hacer.

**Qué debería pasar.** Conseguir los cuadernillos de los procesos anteriores —2019, 2021 y 2023— y
pasarlos por `herramientas/extraer_examen.py`.

**Fuente.** Pendiente de localizar. Correos no publica los cuadernillos en su web con la
regularidad con que RTVE publicó los suyos, y eso hay que comprobarlo antes de darlo por hecho.

**Gravedad.** Induce a error por omisión: un temario sin banco no puede prometer que cubre el
examen, y tiene que decirlo en su portada.

## Cerrados

_Ninguno todavía._
