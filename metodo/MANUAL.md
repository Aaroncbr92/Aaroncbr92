# Cómo hacer temarios de oposición con Claude

Manual de método. No habla de formato, ni de plantillas, ni de cómo se maqueta un documento: eso
cada uno lo resuelve como quiera. Habla de **cómo se consigue que un tema sea correcto**, que es
lo difícil y lo que casi nadie hace bien.

Está escrito a partir de la producción y revisión de unos doscientos temas de cuatro oposiciones
distintas. Todos los números que aparecen están medidos, no estimados. Sirve para cualquier
oposición cuyo temario se apoye en normas publicadas.

---

## 1. La idea de la que sale todo lo demás

Un modelo de lenguaje escribe temario jurídico **plausible** sin ningún esfuerzo. Plazos que
suenan bien, porcentajes redondos, enumeraciones completas y artículos que existen. Casi todo
correcto y un porcentaje pequeño mal, repartido al azar y sin marcar.

Ese porcentaje pequeño es exactamente lo que hace fallar una pregunta.

Así que la regla que ordena todo el trabajo es una sola:

> **Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de afirmarlo, y lo
> que no se puede confirmar se quita.**

No se suaviza, no se pone «aproximadamente», no se deja «según la doctrina». Se quita. Un tema
con un hueco reconocido vale más que uno completo con tres datos inventados dentro, porque el
hueco se ve y el dato inventado no.

De esa regla salen las demás.

---

## 2. Leer la ley bien, que es más difícil de lo que parece

Esto es lo más importante del manual y lo que más se falla. Si solo te llevas una cosa, que sea
esta.

### 2.1. Los textos consolidados encadenan redacciones

Cuando pides a un buscador oficial el artículo X de una ley, lo que suele devolverte no es «el
artículo X» sino **el artículo X en todas sus redacciones sucesivas**, una detrás de otra, cada
una con su fecha de entrada en vigor. Si te quedas con lo primero que ves, estás leyendo la
redacción **más antigua**, que a menudo es la derogada.

Un artículo cualquiera de una ley con veinte años encima puede tener seis redacciones. Y el
opositor que estudie por tu tema contestará con derecho muerto.

**Qué hacer:** obliga a Claude a extraer la redacción vigente de forma explícita, quedándose con
la versión cuya fecha de entrada en vigor sea la última ya cumplida, y a decirte cuántas
redacciones tiene el precepto. Si tiene más de una, que te enseñe la cadena.

### 2.2. Y aun así, la última por fecha tampoco vale siempre

Hay dos trampas por encima de la anterior. Las dos se descubrieron leyendo, no razonando.

**Reformas cruzadas.** Cada reforma guarda el texto tal como quedaba **cuando esa reforma se
aprobó**, y se fecha por su entrada en vigor. Si una reforma se publica antes pero entra en vigor
después que otra, su texto es anterior a la otra y **se la come**. El resultado es un artículo
«vigente» al que le falta lo que le añadió la reforma intermedia. Pasa poco, pero pasa: de 4.264
preceptos citados en tres temarios, **veinte estaban cruzados y quince traían texto distinto**.

**Normas que no llegaron a consolidarse.** Un decreto-ley que el parlamento no convalida sigue
apareciendo en la cadena de versiones, con su fecha, como si rigiera. No rige.

**Qué hacer:** cuando el precepto sea importante y tenga varias redacciones, que Claude contraste
la versión elegida con la página consolidada publicada, que siempre está bien. Y que te avise si
la redacción con la fecha más alta no es también la de la norma publicada más tarde: eso es
justamente la señal del cruce.

### 2.3. Los identificadores no siguen ninguna regla

Los sistemas de publicación oficial numeran sus fragmentos de forma irregular. En un mismo código
el artículo 1 puede ser `a1` y el artículo 2 `art2`. Hay leyes que numeran los artículos con
palabras. Hay normas cuyo contenido va en un anexo y no en artículos.

**Qué hacer:** no dejes que Claude deduzca el identificador por analogía. Que lo resuelva contra
el índice real de la norma, y que compruebe que el fragmento existe antes de darlo por bueno. Si
falla, que pruebe la otra forma antes de concluir que el precepto no está.

---

## 3. Antes de escribir una línea

Tres cosas, y ninguna se salta.

### 3.1. El programa oficial, literal

El temario sale de la convocatoria, no de un índice de manual ni de lo que se hizo el año pasado.
Baja la resolución de convocatoria y saca el anexo con el programa **tal como está redactado**.

Y una regla de oro que ahorra muchísimo trabajo después: **los epígrafes del tema reproducen el
enunciado de la convocatoria literalmente y en el mismo orden**. Ni se agrupan, ni se reordenan,
ni se «mejoran». Dentro de cada epígrafe el orden es libre, y el contenido que no case
literalmente con ninguna rúbrica va igualmente donde encaje, porque en el examen cae.

Cuando un tema no reproduce el enunciado, el opositor no sabe si lo ha cubierto todo. Y el
tribunal pregunta por rúbricas.

### 3.2. Los exámenes de convocatorias anteriores

Consíguelos y **transcríbelos enteros**. Valen para tres cosas distintas:

- **Calibrar el alcance.** Un enunciado de examen te dice cuánto detalle espera el tribunal. No
  es lo mismo «La persona jurídica» que «Enumere y explique brevemente los diferentes fondos de
  financiación de la política regional».
- **Calibrar el estilo** de las preguntas que vas a proponer tú.
- **Saber qué cae de verdad.** Con cuatro convocatorias en la mano se ve enseguida que hay temas
  que caen todos los años y temas que no han caído nunca. Eso decide dónde apretar.

Un ejemplo de lo que aparece al hacerlo: en una oposición, tres de las cuatro últimas
convocatorias preguntaron por el mismo epígrafe de un tema, siempre por lo mismo. Ese epígrafe
había que dejarlo impecable, y sin los exámenes delante no había forma de saberlo.

Ojo con una cosa tonta que despista: comprueba **de qué convocatoria es cada examen** leyendo la
portada, no el nombre del fichero. Los nombres mienten casi siempre.

### 3.3. Qué tienes ya escrito

Si estás haciendo el segundo temario, o el segundo tema, mira qué material tuyo ya verificado
sirve. Muchas oposiciones comparten bloques enteros: el derecho civil de un cuerpo se parece
mucho al de otro.

**Reutiliza el texto literal, no lo parafrasees.** El texto ya verificado pasó por el ciclo; si
lo reescribes, vuelves a meterle el riesgo que le habías quitado. Y cuando le pidas a Claude el
mapa de reaprovechamiento, pídele **el texto completo de lo que propone reutilizar**, no una
lista de referencias: si no se lo das al que redacta, lo escribirá de cero y el ahorro se pierde.

---

## 4. El ciclo, que son cinco fases y ninguna sobra

Escribir un tema en una pasada no funciona. Estos son los números, medidos tema a tema sobre un
temario heredado de treinta y cinco temas:

| Fase | Correcciones que encuentra |
|---|---|
| Verificación inicial | entre 25 y 60 por tema |
| Primer escéptico, sobre el tema ya «terminado» | entre 2 y 12 más |
| Segundo escéptico | todavía entre 0 y 6 |

Fíjate en la segunda fila. Sobre un tema que ya se había verificado y corregido, un lector
independiente encuentra **hasta doce cosas más**. Por eso hacen falta las cinco.

### Fase 1 — Investigar

De tres a seis agentes en paralelo, **uno por grupo de epígrafes**. Cada uno lee la fuente oficial
y devuelve entre 1.200 y 2.200 palabras de material denso, **con el precepto pegado a cada
afirmación** y la cita literal de lo que decide.

Dos detalles que importan más de lo que parece:

- **No les des los números de artículo.** Que los localicen ellos. Si se los das, los dan por
  buenos y no comprueban nada; y si tu número estaba mal, lo propagan.
- **Pídeles que digan lo que no pueden confirmar.** Un investigador que devuelve «esto es doctrina
  de manual y no tiene apoyo en un precepto» vale más que uno que rellena.

### Fase 2 — Redactar

**Un solo agente para todo el tema.** Si repartes la redacción, sale un tema cosido, con
repeticiones entre epígrafes y sin hilo. El opositor lo lee de corrido y se nota.

Ese agente recibe todo el material de la fase 1 y escribe con margen. Recortar es fácil; añadir
lo que nadie investigó, no.

**Que escriba por partes y las vaya guardando.** Un tema largo en una sola tirada se pierde
entero si algo falla a mitad. Guardando por epígrafes, lo que ya está hecho sobrevive. Esto no es
teórico: dos redactores se perdieron enteros por intentarlo de una sentada, y el que troceó
sobrevivió y salvó el trabajo de los otros dos.

### Fase 3 — Verificar

Un agente que relee cada precepto con el catálogo de errores típicos delante (apartado 6) y
**quita lo que no confirma**.

### Fase 4 — Refutar

Aquí está el valor. Uno o varios agentes cuyo encargo **no es revisar sino intentar tumbar el
tema**. La diferencia de encargo cambia el resultado por completo.

Funciona mucho mejor si les das **lentes distintas** en vez de repetir el mismo escéptico:

- **Exactitud normativa**: cada artículo, plazo, enumeración, requisito y cifra, contra la fuente.
- **Cobertura de examen**: ¿cubre el tema todo lo que anuncia el enunciado? ¿Contestaría las
  preguntas que han caído? Este es el que encuentra las lagunas de verdad.
- **Prosa y forma**: antecedentes rotos, repeticiones, relleno, frases que hay que releer.

Tres lentes distintas encuentran cosas que tres escépticos idénticos no encuentran.

**Y una frase que hay que decirles:** *«cero hallazgos es un buen resultado si el tema está
bien»*. Sin ella, inventan para justificar el turno. Con ella, algunos temas salen limpios y te
puedes fiar de que lo están.

### Fase 5 — Rematar, y una segunda refutación que tiene que salir limpia

La ronda que corrige **también estropea**. Ha pasado varias veces: al aplicar una corrección se
pierde el número de artículo y queda «el apartado 2» colgando de un precepto que no tiene
apartados. La ronda de corrección *introdujo* un error que antes no existía.

Por eso el encargo de rematar lleva siempre: *relee el resultado entero y comprueba que cada «ese
artículo», «dicha ley» o «el apartado X» tiene delante el antecedente que le corresponde*.

Y después, otra refutación que debe volver sin hallazgos.

---

## 5. Las cláusulas del encargo que de verdad cambian el resultado

Estas frases, literalmente, valen más que cualquier otra cosa que escribas en el prompt.

**«Si algo de este encargo no cuadra con la fuente, manda la fuente y dímelo.»**
Tres veces he dado una premisa falsa —un título de una ley que no existe, un artículo cambiado— y
las tres veces el agente comprobó, escribió bien y me avisó. Sin esa cláusula habría escrito lo
que yo le dije.

**«Comprueba cada corrección en la fuente antes de aplicarla. Si el informe se equivocó, no la
apliques y dilo.»**
El que detecta se equivoca. Ha pasado con un real decreto que el tema nunca citó y con un
reglamento que supuestamente suprimía un certificado cuando en realidad lo introdujo. Las dos
veces el agente que corregía tenía razón contra el que detectaba. **Sin esta cláusula habrías
metido el error por orden de quien estaba para evitarlo.**

**«Lo que no puedas confirmar, quítalo. No lo sustituyas por lo que recuerdes.»**

**«Limítate a tu tema y declara qué otros ficheros has tocado.»**
Un agente que revisaba un tema editó de paso otro ya entregado. Sin la declaración no te enteras.

**«Cero hallazgos es un buen resultado.»**

---

## 6. Los nueve errores que se repiten

Este catálogo va dentro del encargo del verificador, con un ejemplo de cada uno. No son errores
teóricos: son los que aparecen una y otra vez.

1. **Cita cruzada.** El texto nombra un artículo y la referencia apunta a otro. Es el más
   frecuente y el más invisible.
2. **Ley por reglamento**, o al revés. La regla existe, pero está en la otra norma.
3. **Recuentos que no cuadran.** «Tres requisitos» y detrás enumera cuatro. Se caza contando.
4. **Modo verbal cambiado.** Convertir en obligatorio lo que la norma deja potestativo, o al
   revés. Cambia la respuesta y no se ve leyendo por encima.
5. **Siglas sin presentar** la primera vez que aparecen.
6. **Requisito, excepción o salvedad omitida.** El caso típico: una regla que la ley da «salvo
   que…» y el tema convierte en absoluta. Es el error que más puntos cuesta.
7. **Redacción derogada citada como vigente** (apartado 2).
8. **Número de artículo mal.**
9. **Afirmación sin apoyo en la fuente.** Suele venir con un «la doctrina entiende» delante.

---

## 7. La prueba que decide si el tema está terminado

Cuando el tema esté escrito, redacta entre diez y quince preguntas **en el estilo real del
examen** y comprueba, una por una, si **se contestan con el cuerpo del tema delante y nada más**.

Tres respuestas posibles: entera, a medias, no.

Todo lo que salga «a medias» o «no» es una laguna. Y aquí está la regla que cierra el método:

> **La laguna se cierra ampliando el tema, nunca recortando la pregunta.**

Si la pregunta es realista y el tema no la contesta, el tema está incompleto, por muy largo que
sea. En un tema de treinta páginas ya revisado, esta prueba destapó cinco lagunas.

---

## 8. Extensión

No pongas un tope de palabras y lo defiendas. **La extensión la manda el enunciado.** Un enunciado
con cuatro rúbricas, una de ellas media docena de artículos densos, no cabe en las mismas páginas
que uno con dos.

Lo que sí sobra siempre, y hay que perseguir: la repetición entre epígrafes, el tejido conectivo
(«como hemos visto», «en síntesis», «cabe destacar»), la doctrina sin apoyo en un precepto, y lo
que no alimenta ninguna pregunta posible.

Dicho de otra forma: **se recorta la prosa, no el contenido normativo**.

Cuando tengas que decidir, mide en vez de opinar. Compara con temas hermanos del mismo asunto y
pide un juicio argumentado sobre qué sobra de verdad, con ejemplos concretos, antes de cortar.

---

## 9. Los esquemas

Un esquema es un **esqueleto**, no un resumen. Estilo telegrama, y el artículo delante de cada
línea.

Y aquí hace falta una cifra, porque sin ella no se sujeta: sin número, un agente entregó un
esquema de 8.341 palabras para un tema de 15.100. **Catorce veces** el que ya existía para ese
mismo tema.

**Da la horquilla en palabras y en líneas, y di expresamente que no crece en proporción al tema.**
Un tema de treinta páginas no lleva un esquema de quince. Como referencia de un corpus real: unas
2.000 palabras y unas 130 líneas.

La tensión con «no se recorta un precepto, ni un recuento, ni una cifra» se resuelve por un lado:
**se quita explicación, nunca el dato normativo**.

---

## 10. El fallo que no da error

Este es el que más veces me ha mordido, y no se parece a los demás.

Cuatro veces en un mes el problema no fue una comprobación mal hecha, **sino una comprobación que
no se estaba corriendo sobre todo**:

- Un temario entero que nunca pasó por el ciclo de refutación y se dio por revisado. Cuando por
  fin se le pasó una detección: **243 hallazgos en 35 temas, ninguno limpio**, doce de ellos
  capaces de hacer fallar una pregunta.
- Una herramienta de comprobación que recorría dos de los cuatro temarios. Los otros dos llevaban
  meses sin pasar por ella.
- Un arreglo que se aplicó en un sitio y no llegó al otro sitio que hacía lo mismo por su cuenta.
- Una ruta mal escrita que hacía que una comprobación no mirase nada, sin quejarse.

Las cuatro se descubrieron por casualidad, mirando otra cosa.

**Por qué es invisible:** un hueco de cobertura no da error. La herramienta funciona, informa, y
lo que no mira sencillamente no aparece. No hay traza, no hay excepción, no hay nada.

**Qué hacer:** pregúntate de vez en cuando, explícitamente, *¿qué comprobación pasa por qué
material?* Y si puedes, que lo responda algo automático y no tu memoria. Si mantienes una lista
escrita a mano de lo que hay que comprobar, esa lista se quedará vieja: es justo lo que se
degrada.

Un corolario: **cuando arregles algo, busca quién más hace ese mismo trabajo por su cuenta.**
Busca por el patrón, no por el nombre de la función.

---

## 11. Operativa

**De dos en dos.** Lanzar cinco temas a la vez agota el límite de la sesión y se pierden a medias.
Dos temas por tanda es lo que aguanta.

**No abarates la investigación.** Se probó usar un modelo más barato para investigar y salió
peor: tres omisiones y, encima, no bajó el consumo, porque hubo que repetir. Investigar, redactar
y verificar van con el modelo bueno. Lo mecánico puede ir barato.

**Todo a disco, según se produce.** Los avisos de fin de tarea se truncan, y un informe de catorce
hallazgos se pierde a la mitad. Que cada agente escriba su informe en un fichero. Si la sesión se
corta, el trabajo está.

**Cuenta con quedarte sin límite a mitad.** Va a pasar. Lo que lo hace soportable es que todo esté
en disco y que exista un fichero de estado —qué es este temario, dónde vive cada cosa, qué está
hecho, qué falta— que permita a otra sesión seguir sin reconstruir nada.

**Mira las marcas de tiempo antes de concluir que algo está parado.** Y antes de dar por perdido
un trabajo que falló: más de una vez el agente había escrito el fichero justo antes de caer.

---

## 12. El cuaderno de pendientes

Ten un único fichero donde **cualquier sesión anote lo que detecte, aunque no lo corrija en el
momento**. Es lo que evita que un hallazgo se pierda porque apareció en mal momento.

Cada entrada, cinco campos. Sin ellos no sirve, porque quien la aplique meses después no tendrá
el contexto:

- **Dónde**: tema y epígrafe.
- **Qué dice** hoy.
- **Qué debería decir**, ya redactado para pegar.
- **La fuente**: el precepto en su redacción vigente, citado literal. Y si no se ha comprobado, se
  dice.
- **La gravedad**: cambia la respuesta / induce a error / menor.

Lo aplicado se tacha con su fecha, no se borra. El histórico es lo que deja ver si un mismo error
se repite en varios temarios, que es cuando deja de ser un descuido y pasa a ser un patrón.

---

## 13. Antes de dar un tema por terminado

- [ ] Los epígrafes reproducen el enunciado de la convocatoria, literal y en orden.
- [ ] Cada dato tiene su precepto detrás, y ese precepto se ha leído en su redacción vigente.
- [ ] Los preceptos con varias redacciones se han releído enteros.
- [ ] El ciclo completo: investigar, redactar, verificar, refutar, rematar y refutar otra vez.
- [ ] La última refutación vuelve sin hallazgos.
- [ ] Las preguntas de examen se contestan con el cuerpo delante. Todas.
- [ ] Lo que no se pudo confirmar está fuera, y anotado en el cuaderno.
- [ ] Nada se ha tocado fuera de este tema.

---

## 14. Lo que no está en este manual

El formato. Cómo se maqueta, qué tipografía lleva, cómo se enlaza a la fuente oficial, cómo se
genera un índice o dónde se guarda. Todo eso es real y da trabajo, pero es intercambiable: se
resuelve una vez y ya no se piensa más en ello.

Lo de aquí no. Esto es lo que decide si el tema está bien.
