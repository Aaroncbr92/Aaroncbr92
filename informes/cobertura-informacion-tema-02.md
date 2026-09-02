# Cobertura del tema 2 del específico de Información y Contenidos

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y donde
el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

- **Tema**: La Unión Europea y sus Instituciones.
- **Preguntas de la materia**: **17**.
- **Contestadas con el tema delante**: **17**.
- **Preguntas verificadas en la fuente**: **10 de 17** —cuatro en el BOE, dos en el Diario Oficial de
  la Unión Europea, tres en la tabla de tipos del Banco Central Europeo y una en Eurostat—.
- **Preguntas apoyadas sólo en la plantilla**: **7**.

**Es la mejor proporción de los tres primeros puntos de este temario** —el 59 %, frente al 17 % del
tema 1— y la razón es sencilla: **las instituciones europeas publican**.

## El enunciado promete una cosa y el examen pregunta otra

«La Unión Europea y sus Instituciones» hace esperar un tema de Tratados: competencias, procedimiento
legislativo ordinario, composición del Consejo. **El examen no pregunta nada de eso.** De las
diecisiete preguntas:

- **Diez son hechos europeos de 2024**: unas elecciones, dos decisiones de tipos, una tasa de
  inflación, un arancel, una reforma agraria y dos nombramientos.
- **Cuatro son de estructura**: quién preside el Parlamento, quién es el Alto Representante, qué
  Estados quedan fuera de Schengen y cuántos no tienen el euro.
- **Tres son de historia y de grupos parlamentarios**: el año de la adhesión, la cabeza de lista de
  una candidatura y el grupo de un eurodiputado.

**Eso decide dónde se busca**, y es el hallazgo de método de este tema: no en los Tratados, sino en
**el Diario Oficial**, en **el BOE** y en **las páginas de las instituciones que publican con
fecha**.

## Las cuatro vías que funcionaron

| Vía | Qué resolvió |
|---|---|
| **BOE** | El tratado de adhesión —con sus cuatro fechas— y **tres preguntas de las elecciones europeas**: la Junta Electoral Central publica los resultados por mandato del artículo 108.6 de la ley electoral y proclama a los electos por el 224.1 |
| **Cellar de la Oficina de Publicaciones de la UE** | Los dos reglamentos, en español y en su texto publicado |
| **Banco Central Europeo** | La **tabla histórica de tipos oficiales**, que resuelve tres preguntas de una vez porque da fecha y valor de cada cambio desde 1999 |
| **Eurostat** | La estimación de avance de la inflación, con el reparto por componentes |

**La tabla del Banco Central Europeo merece una nota**: es el ejemplo más limpio del proyecto de una
fuente institucional que **no caduca**. No dice «hoy los tipos están en X»; dice **qué valor tuvo
cada tipo desde cada fecha**, y por eso sirve igual para una pregunta de 2024 leída en 2026.

## Lo contrario: la fuente que sí caduca

**La página de la Unión Europea sobre los países que usan el euro dice hoy «21 de los 27».** En
octubre de 2024, cuando se hizo el examen, eran veinte, y por eso la respuesta oficial —**siete**
países fuera— era correcta y hoy no lo parece.

**No se forzó la página para que dijera lo de anteayer.** La pregunta va marcada como apoyada sólo
en la plantilla, con la explicación al lado, y el tema aprovecha para enseñar **el mecanismo**, que
es lo que no cambia: los países que aún no lo han adoptado y el que tiene cláusula de exclusión
voluntaria.

**Es la segunda vez que el proyecto tropieza con esto** —la primera fue el medallero paralímpico del
tema 1— y ya se puede enunciar como regla: **una página institucional sirve para lo que está hoy en
ella; si la pregunta es de un año concreto, hace falta una fuente fechada**.

## Las siete lagunas, y qué se intentó

| Pregunta | Qué se intentó | Qué contestó |
|---|---|---|
| Nacionalidad de Metsola | Página de la presidencia del Parlamento Europeo; ficha de eurodiputada | 404 la primera; **200 con armazón vacío** la segunda |
| Grupo de Puigdemont | Ficha de eurodiputado | **404** |
| Estados fuera de Schengen | Página del Consejo sobre el espacio Schengen; página de la Comisión sobre Schengen | **403** la del Consejo; la de la Comisión, 200 pero sin el contenido |
| Consejo Europeo de Granada | Página del Consejo de octubre de 2023 y su sala de prensa | **403** |
| Alto Representante | Página del Servicio Europeo de Acción Exterior | **404** |
| Cartera de Teresa Ribera | — | *(la proclamación de electos la sitúa como eurodiputada electa; el nombre de la cartera, no)* |
| Países sin el euro | Página oficial de la zona del euro | 200, **pero con la cifra de hoy** |

**Se probó además con un navegador real**, para las páginas que cargan su texto con JavaScript. **En
este entorno el navegador no atraviesa el proxy de salida**: falla con `ERR_CONNECTION_RESET` incluso
contra sitios que `curl` sí alcanza. Eso está anotado en `ESTADO.md` como límite del entorno, no de
las fuentes.

## Lo que este tema añade al proyecto

1. **La Junta Electoral Central como fuente de primer nivel para resultados electorales.** Publica en
   el BOE los resultados con votos y escaños por provincia y la proclamación de electos por orden de
   atribución. Sirve para cualquier pregunta de resultados de cualquier convocatoria futura.
2. **La regla de las fuentes que caducan**, ya enunciada arriba.
3. **Una comprobación doble**: los 61 escaños están publicados **y** la suma de la tabla los da. Que
   las dos cosas ocurran a la vez es lo que hace una respuesta indiscutible, y conviene buscarlo
   siempre que la fuente traiga la descomposición.
