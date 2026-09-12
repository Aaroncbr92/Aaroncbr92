# Tema 17 del específico de Ingeniería Técnica · Telecomunicación · Seguridad en las instalaciones técnicas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 21 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Tres normas del boletín, resumidas y no citadas aquí**: el Real Decreto 614/2001, el reglamento electrotécnico para baja tensión y el Real Decreto 299/2016. **Sus citas literales están en el tema homólogo de Técnica de Equipos y Sistemas Electrónicos** |
| **Identificador** | `BOE-A-2001-11881` · `BOE-A-2002-18099` · `BOE-A-2016-7303` |
| **Redacción que se estudia** | La vigente el **21/12/2022**, verificada en el tema homólogo |
| **Punto compartido** | **Este mismo punto es el 20 del anexo de Técnica de Equipos y Sistemas Electrónicos, y allí dio cuatro preguntas.** Es el único punto de aquella ocupación cuyas respuestas están en el Boletín Oficial del Estado |
| **Extensión** | **1.873 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la alta tensión (**AT**) y la baja tensión (**BT**);
la radiofrecuencia (**RF**); los equipos de protección individual (**EPI**); el reglamento
electrotécnico para baja tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**);
el voltio (**V**), en valor eficaz de alterna (**Vrms**) y en continua (**V cc**); el miliamperio
(**mA**); y el gigahercio (**GHz**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 21):
> «Seguridad en las Instalaciones técnicas. Conocimientos generales de elementos de protección en AT,
> BT, RF y su uso. Riesgo eléctrico. Equipos de protección individual (EPI). Dispositivos de
> protección diferencial y de cortocircuito.»

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo de esta ocupación**, y
**el tema se escribe igual, contra el programa.**

**Y hay una razón de peso para escribirlo bien**: **este mismo punto es el 20 del anexo de Técnica de
Equipos y Sistemas Electrónicos, y allí SÍ ha dado cuatro preguntas.** **Es, además, el único punto de
aquella ocupación cuyas respuestas están en el Boletín Oficial del Estado**, así que **la materia está
verificada contra norma y aquí se recoge con la misma verificación.**

<!-- indice -->

## Índice

- [1. Dónde empieza la alta tensión](#1-dónde-empieza-la-alta-tensión)
- [2. El riesgo eléctrico y sus formas](#2-el-riesgo-eléctrico-y-sus-formas)
- [3. Los dispositivos de protección](#3-los-dispositivos-de-protección)
- [4. Los equipos de protección individual](#4-los-equipos-de-protección-individual)
- [5. La radiofrecuencia y la salud](#5-la-radiofrecuencia-y-la-salud)
- [6. Lo que el examen ha preguntado](#6-lo-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Dónde empieza la alta tensión

**El dato es de norma y hay que ir a buscarlo en dos sitios**, y eso es lo que hace este epígrafe
distinto de un resumen:

**El Real Decreto 614/2001, sobre riesgo eléctrico, NO da la cifra: la remite.** **Su anexo I,
definición 5, dice que la alta tensión, la baja tensión y las tensiones de seguridad son «las
definidas como tales en los reglamentos electrotécnicos».**

**Y la cifra está en el reglamento electrotécnico para baja tensión**, cuyo artículo 2, apartado 1,
**fija el límite de la baja tensión en 1.000 voltios en corriente alterna y 1.500 en continua.**
**Por encima de esos valores empieza la alta tensión.**

| Régimen | Límite |
|---|---|
| **Baja tensión** | **Hasta 1.000 Vrms en alterna y 1.500 V cc en continua** |
| **Alta tensión** | **Por encima de esos valores** |

**El aviso que vale más que la cifra**: **la frontera legal no coincide con la sensación de peligro.**
**Una instalación de 400 voltios es baja tensión y mata igual.** **Lo que la clasificación cambia son
las exigencias, la cualificación exigida y los procedimientos**, no el riesgo físico.

**Y la consecuencia de personal que se deriva**, del anexo IV del mismo real decreto: **en baja tensión
basta con ser trabajador AUTORIZADO; en alta tensión hay que ser trabajador CUALIFICADO.**

| Figura | Qué exige |
|---|---|
| **Autorizado** | **Que el empresario lo haya autorizado según su capacidad** |
| **Cualificado** | **Autorizado y además con formación acreditada o experiencia certificada** |

## 2. El riesgo eléctrico y sus formas

**La definición legal incluye más de lo que nadie espera**, y está en el anexo I, definición 1, del
mismo real decreto: **choque eléctrico, quemaduras por choque o por arco, caídas o golpes como
consecuencia de choque o arco, e incendios o explosiones originados por la electricidad.**

**Los dos tipos de contacto, que es la distinción de la que cuelga toda la protección:**

| Tipo | Qué es |
|---|---|
| **Directo** | **Tocar una parte que está en tensión por diseño** |
| **Indirecto** | **Tocar una masa puesta en tensión por una avería** |

**Y las cinco reglas de oro del trabajo sin tensión, que es lo que un examen puede pedir en orden:**

1. **Desconectar.**
2. **Prevenir cualquier posible realimentación**, bloqueando y señalizando.
3. **Verificar la ausencia de tensión.**
4. **Poner a tierra y en cortocircuito.**
5. **Proteger frente a elementos próximos en tensión y señalizar la zona de trabajo.**

**El orden importa y no es arbitrario**: **verificar va DESPUÉS de bloquear, porque bloquear sin
verificar deja la duda, y verificar sin bloquear deja la posibilidad de que alguien reconecte
mientras se trabaja.**

## 3. Los dispositivos de protección

**El enunciado pide expresamente «dispositivos de protección diferencial y de cortocircuito», y son
dos cosas distintas que protegen a dos sujetos distintos:**

| Protección | Qué vigila | A quién protege |
|---|---|---|
| **Diferencial** | **La diferencia entre lo que entra y lo que vuelve** | **A las PERSONAS** |
| **Magnetotérmico** | **La intensidad**: sobrecarga y cortocircuito | **A la INSTALACIÓN** |
| **Fusible** | **La intensidad** | **A la instalación** |
| **Puesta a tierra** | **Nada por sí sola: da camino a la fuga** | **Es lo que permite que el diferencial actúe** |

**La regla de memoria**: **el diferencial protege a las personas y el magnetotérmico a los cables.**

**Cómo funciona el diferencial, en una línea**: **compara la corriente que entra por la fase con la que
vuelve por el neutro**; **si difieren más de su valor asignado, parte de la corriente se está yendo
por otro camino —posiblemente una persona— y abre.**

**Las dos sensibilidades que fija la instrucción técnica complementaria correspondiente:**

| Valor | Para qué |
|---|---|
| **30 miliamperios** | **Protección complementaria frente a contactos directos** |
| **300 miliamperios** | **Protección frente a contactos indirectos y contra incendios** |

**Y el matiz que conviene tener claro**: **el diferencial es protección PRINCIPAL contra los contactos
indirectos y sólo COMPLEMENTARIA contra los directos.** **Contra el contacto directo, lo que protege
de verdad es el aislamiento y la distancia.**

**La tensión límite convencional**, que la misma instrucción fija: **50 voltios eficaces en condiciones
normales**, y **24 en locales húmedos o conductores.** **Por debajo de esos valores no se considera
que haya riesgo de contacto indirecto.**

## 4. Los equipos de protección individual

**El anexo IV del Real Decreto 614/2001 enumera el material de seguridad en un orden que no es
casual**: **accesorios aislantes, útiles aislantes o aislados, pértigas aislantes, dispositivos
aislantes o aislados y equipos de protección individual.**

**La lista va de fuera hacia dentro**: **primero se aísla lo que está en tensión, después la
herramienta, después lo que separa del suelo, y sólo al final lo que el trabajador lleva puesto.**
**El equipo de protección individual es el ÚLTIMO recurso, no el primero.**

**Y ése es el principio general de la prevención que el tema compartido desarrolla**: **la protección
colectiva antes que la individual.** **Un equipo de protección individual protege a quien lo lleva; una
protección colectiva protege a todos, incluido al que se olvidó de ponerse el suyo.**

**Los equipos propios del trabajo eléctrico:**

| Equipo | Para qué |
|---|---|
| **Guantes aislantes** | **Contacto**, con su clase según la tensión |
| **Calzado aislante** | **Aislamiento respecto al suelo** |
| **Pantalla facial** | **Arco eléctrico** |
| **Ropa ignífuga sin partes conductoras** | **Arco eléctrico** |
| **Casco dieléctrico** | **Golpe y contacto** |

**El aviso de uso, que es donde fallan**: **un guante aislante tiene fecha de caducidad y necesita
verificación periódica.** **Un guante viejo o con un pinchazo invisible no protege, y quien lo lleva
cree que sí**, lo que **es peor que no llevarlo.**

## 5. La radiofrecuencia y la salud

**El enunciado nombra la protección en radiofrecuencia junto a la eléctrica**, y **es la parte propia
de una instalación de radiodifusión.**

**El Real Decreto 299/2016 enumera en su artículo 2 los efectos de los campos electromagnéticos**, y
**los separa en dos grupos**: **efectos directos** —entre ellos el calentamiento de los tejidos y las
corrientes inducidas en las extremidades— **y efectos indirectos** —entre ellos las corrientes de
contacto—.

**Y el dato que conviene tener y que allí se pregunta**: **la ionización de materia corporal NO figura
en esa lista**, y **el propio real decreto lo confirma sin decirlo**: **regula los campos de 0 hercios
a 300 gigahercios**, que es toda la región NO ionizante del espectro.

**El porqué físico, en una línea**: **ionizar es arrancar electrones**, y **hace falta energía de
ultravioleta duro para arriba.** **La radiofrecuencia no llega, por mucha potencia que tenga.**

**Las reglas de trabajo en un centro emisor, que es lo que un ingeniero necesita:**

| Regla | Por qué |
|---|---|
| **No subir a una torre con el transmisor emitiendo** | **Los límites de exposición se superan cerca del sistema radiante** |
| **Respetar las distancias señalizadas** | **La señalización marca la zona donde se superan los límites** |
| **No manipular guías ni conectores de salida con potencia aplicada** | **Riesgo de quemadura por radiofrecuencia y de arco** |
| **Coordinar el trabajo con la operación del emisor** | **Bajar potencia o parar es la única protección real** |

**Y la diferencia entre las dos clases de riesgo que este punto reúne, que conviene enunciar**: **el
riesgo eléctrico se nota; el de radiofrecuencia, no.** **Una descarga se siente en el instante; una
sobreexposición a campos no produce ninguna sensación inmediata**, y por eso **la protección es de
procedimiento y de señalización, no de percepción.**

## 6. Lo que el examen ha preguntado

**Ninguna pregunta en esta ocupación.**

**El aviso de estudio**: **este mismo punto ha dado cuatro preguntas en el examen de Técnica de
Equipos y Sistemas Electrónicos**, y **tres de sus cuatro respuestas están en el Boletín Oficial del
Estado.** **Lo razonablemente preguntable son las tres cifras —1.000 y 1.500 voltios, y 30
miliamperios—, la distinción entre diferencial y magnetotérmico, y que la ionización no figura entre
los efectos de la radiofrecuencia.**

## 7. Trazabilidad

**Este tema no cita ninguna norma de forma literal en su cuerpo**, y **remite a las que sí se citan
literalmente en el tema 17 del específico de Técnica de Equipos y Sistemas Electrónicos**, escrito en
este mismo proyecto.

**Cuatro declaraciones expresas:**

1. **Las tres normas que sostienen este punto están volcadas y verificadas en este proyecto**: el
   **Real Decreto 614/2001** sobre riesgo eléctrico, el **reglamento electrotécnico para baja
   tensión** y el **Real Decreto 299/2016** sobre campos electromagnéticos. **Sus citas literales
   están en el tema 17 del específico de Técnica de Equipos y Sistemas Electrónicos**, y **aquí se
   resumen sin cita para no repetirlas.**
2. **La cadena de dos normas para la definición de alta tensión es un hallazgo de método de este
   proyecto**, verificado allí: **la norma de prevención remite y el reglamento electrotécnico da la
   cifra.**
3. **Las cinco reglas de oro y la lista de equipos de protección individual proceden del anexo IV del
   Real Decreto 614/2001**, resumidas sin cita literal. **Su cita está en el tema compartido de
   prevención y en el ya mencionado.**
4. **Este punto no ha dado ninguna pregunta en esta ocupación**, así que **no hay ninguna respuesta
   oficial que sostener aquí.**

**El resto del tema va como oficio y así se declara**: el aviso de que la frontera legal no coincide
con la sensación de peligro, la razón del orden de las cinco reglas, la regla de memoria del
diferencial y el magnetotérmico, el aviso sobre la caducidad de los guantes aislantes, las reglas de
trabajo en un centro emisor y la diferencia entre un riesgo que se nota y otro que no. **Nada de eso
está en un boletín oficial más allá de lo que las normas citadas dicen**, y el tema no lo presenta
como si lo estuviera.
