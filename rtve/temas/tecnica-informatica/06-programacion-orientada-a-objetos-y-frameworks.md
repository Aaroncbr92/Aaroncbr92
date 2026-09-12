# Tema 6 del específico de Técnica Informática · Programación orientada a objetos y frameworks

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · puntos 7 y 8 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los conceptos de la programación orientada a objetos, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Salvedad declarada** | **El enunciado de la pregunta 5 afirma de Python algo que no es cierto**: en Python se instancian clases. **Se marca la opción de la plantilla**, que es la mejor de las cuatro, y el temario declara el defecto |
| **Extensión** | **1.719 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la programación orientada a objetos (**POO**); el
patrón modelo-vista-controlador (**MVC**); el lenguaje de consulta estructurado (**SQL**) y la
notación de objetos de JavaScript (**JSON**), que aparecen como opciones falsas; y **C**, **C++**,
**C#**, **Java** y **Python**, que son nombres de lenguaje y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, puntos 7 y 8):
> «7. Desarrollo y lenguajes de programación: Terminología y conceptos. Programación orientada a
> objetos.»
>
> «8. Frameworks en programación y desarrollo. Principales usos y tipos.»

**Seis preguntas.** **Y este punto reúne dos del anexo porque el examen los ha tratado como uno**:
**la terminología de la orientación a objetos y los marcos de trabajo que la aplican.**

**Su reparto**: **cuatro preguntas son de conceptos de orientación a objetos**, **una es de
estructuras de datos** y **una es de patrón de arquitectura.**

<!-- indice -->

## Índice

- [1. Los cuatro pilares de la orientación a objetos](#1-los-cuatro-pilares-de-la-orientación-a-objetos)
- [2. Qué lenguajes son orientados a objetos y cómo](#2-qué-lenguajes-son-orientados-a-objetos-y-cómo)
- [3. Las estructuras de datos](#3-las-estructuras-de-datos)
- [4. Los frameworks y sus patrones](#4-los-frameworks-y-sus-patrones)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Los cuatro pilares de la orientación a objetos

| Pilar | Qué significa |
|---|---|
| **Abstracción** | **Quedarse con lo que importa del problema y desechar el resto** |
| **Encapsulación** | **Esconder el estado interno y dar acceso sólo por métodos** |
| **Herencia** | **Que una clase reciba los atributos y métodos de otra** |
| **Polimorfismo** | **Que la misma llamada haga cosas distintas según el objeto que la reciba** |

**Y los dos términos que ordenan todo lo demás**: **la clase es el molde y el objeto es la pieza.**
**Instanciar es fabricar una pieza con el molde.**

**La pregunta 38**: **el lenguaje que incluye clases, objetos y herencia, conceptos esenciales de la
programación orientada a objetos, es Java.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas no son lenguajes orientados a objetos**, cada una por su motivo: **C es
un lenguaje estructurado y no tiene clases**; **SQL es un lenguaje de consulta, no de propósito
general**; **y JSON no es un lenguaje de programación: es un formato de datos**, como el tema 10
explica.

**La pregunta 92**: **en programación orientada a objetos, sobrecargar un método significa crear un
método con el mismo nombre pero diferentes argumentos.** Ésa es la respuesta oficial.

---

**Y hay dos palabras que se parecen y no son lo mismo**, y ésta es la distinción que el examen
persigue:

| Término | Qué es | Dónde ocurre |
|---|---|---|
| **Sobrecarga** (*overload*) | **Varios métodos con el mismo nombre y distintos argumentos** | **En la misma clase** ✔ |
| **Sobrescritura** (*override*) | **Un método que reemplaza al que se heredó, con la misma firma** | **En una clase hija** |

**La regla de memoria**: **sobrecargar es añadir versiones; sobrescribir es sustituir la heredada.**
**La opción a de la pregunta —«editarlo para modificar su comportamiento»— describe la sobrescritura**,
y por eso es el distractor bueno.

## 2. Qué lenguajes son orientados a objetos y cómo

**La pregunta 5 es negativa**: **de los lenguajes orientados a objetos enumerados, en el que NO es
posible instanciar una clase es Python.** Ésa es la respuesta oficial.

---

**Ésta es la pregunta más discutible del punto, y el temario lo dice**: **en Python se instancian
clases todos los días**, escribiendo el nombre de la clase seguido de paréntesis. **Lo que la
respuesta oficial parece perseguir es que Python no obliga a declarar clases** —permite programar sin
ellas—, **frente a Java, C# y C++, donde todo el código vive dentro de una clase.**

**La respuesta oficial es la de la plantilla y se marca**, y **el temario declara que su enunciado no
dice lo que la respuesta necesita.** **Es una pregunta que este proyecto no habría escrito así.**

**La pregunta 18 va del mismo lenguaje y está bien construida**: **Python, en el contexto de la
programación orientada a objetos, es compatible con ella y con la programación imperativa, entre
otras.** Ésa es la respuesta oficial.

---

**Y ahí está la clasificación que ordena el epígrafe:**

| Clase de lenguaje | Qué significa | Ejemplos |
|---|---|---|
| **Orientado a objetos puro** | **Todo es un objeto y no se puede programar de otro modo** | **Smalltalk** |
| **Multiparadigma** | **Admite objetos, imperativo, funcional y más** | **Python**, **C++**, **JavaScript** ✔ |
| **Orientado a objetos con clase obligatoria** | **Todo el código vive en una clase, aunque el paradigma no sea puro** | **Java**, **C#** |
| **Estructurado, sin objetos** | **Funciones y estructuras, sin clases** | **C** |

**Las dos preguntas juntas dicen algo útil**: **Python es multiparadigma, y eso es a la vez la
respuesta correcta de la 18 y lo que hace discutible la 5.**

## 3. Las estructuras de datos

**La pregunta 81**: **de los enumerados, el tipo de datos estructurado, dinámico y NO lineal es el
árbol.** Ésa es la respuesta oficial.

---

**La clasificación que la contesta:**

| Estructura | Lineal o no | Cómo se recorre |
|---|---|---|
| **Pila** | **Lineal** | **Último en entrar, primero en salir** |
| **Cola** | **Lineal** | **Primero en entrar, primero en salir** |
| **Lista** | **Lineal** | **De principio a fin, elemento tras elemento** |
| **Árbol** | **NO lineal** | **Por ramas: cada nodo puede tener varios hijos** ✔ |
| **Grafo** | **NO lineal** | **Por aristas, y puede tener ciclos** |

**La palabra que decide es «lineal»**: **tres de las cuatro opciones lo son.** **Una estructura es
lineal cuando cada elemento tiene como mucho un anterior y un siguiente**, y **en un árbol un nodo
puede tener varios siguientes.**

**Y «dinámico» añade el otro criterio**: **crece y mengua en tiempo de ejecución**, frente a un vector
de tamaño fijo. **Las cuatro opciones son dinámicas**, así que **esa palabra no distingue; la que
distingue es «no lineal».**

## 4. Los frameworks y sus patrones

**Qué es un framework, dicho con precisión**: **un armazón que ya trae resueltas las decisiones
repetitivas y que llama al código del programador**, no al revés. **Ésa es la diferencia con una
biblioteca**: **a una biblioteca la llamas tú; un framework te llama a ti.**

**La pregunta 86**: **Struts es un framework basado en el patrón de arquitectura de software
modelo-vista-controlador.** Ésa es la respuesta oficial.

---

**El patrón, en sus tres piezas:**

| Pieza | De qué se ocupa |
|---|---|
| **Modelo** | **Los datos y las reglas de negocio** |
| **Vista** | **Cómo se presentan al usuario** |
| **Controlador** | **Recibe la petición, pide al modelo y elige la vista** |

**Para qué sirve separarlos**: **para poder cambiar la presentación sin tocar las reglas, y al
revés.** **Es el patrón de casi todos los marcos web**, y por eso la pregunta es contestable aunque no
se conozca Struts: **si de cuatro opciones una es un patrón de presentación y las otras tres son
patrones de despliegue —cliente-servidor, capas, maestro-esclavo—, la respuesta es la primera.**

**Los tipos de framework que el punto 8 pide, con un ejemplo de cada uno:**

| Tipo | Para qué | Ejemplos |
|---|---|---|
| **Web de servidor** | **Generar respuestas y coordinar la lógica** | **Struts**, **Spring**, **Django**, **Laravel** |
| **Web de cliente** | **Construir la interfaz en el navegador** | **Angular**, **React**, **Vue** |
| **De persistencia** | **Traducir entre objetos y tablas** | **Hibernate**, **Entity Framework** |
| **De pruebas** | **Automatizar la comprobación del código** | **JUnit**, **pytest** |

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 5 | Lenguaje en el que NO se puede instanciar una clase | d) Python ✔ **·** enunciado discutible |
| 18 | Qué tipo de lenguaje es Python respecto de la orientación a objetos | d) Compatible con ella y con la imperativa ✔ |
| 38 | Lenguaje con clases, objetos y herencia | d) Java ✔ |
| 81 | Tipo de datos estructurado, dinámico y NO lineal | c) Árbol ✔ |
| 86 | Patrón de arquitectura en que se basa Struts | a) Modelo-Vista-Controlador ✔ |
| 92 | Qué significa sobrecargar un método | c) Mismo nombre, distintos argumentos ✔ |

**Las seis respuestas oficiales son correctas** en el sentido de ser la mejor de sus cuatro opciones,
**y ninguna descansa en la plantilla.** **Una lleva salvedad declarada**: la 5, cuyo enunciado afirma
algo que en Python no es cierto.

**El aviso de estudio**: **la pareja sobrecarga y sobrescritura, y la clasificación de estructuras en
lineales y no lineales, son las dos distinciones que este punto mide.** **Las dos caben en cuatro
líneas y contestan dos preguntas.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Los cuatro pilares de la orientación a objetos, la distinción entre sobrecarga y sobrescritura y
   la clasificación de estructuras de datos son teoría clásica de la programación**, presentada como
   conocimiento común. **Ninguna norma ni manual concreto se ha consultado.**
2. **La respuesta oficial de la pregunta 5 se sostiene con salvedad declarada.** **En Python se
   instancian clases**, y el temario lo dice. **Lo que se marca es la opción de la plantilla**, que es
   la mejor de las cuatro si se entiende que la pregunta persigue la obligatoriedad de la clase.
3. **Struts, Spring, Django, Laravel, Angular, React, Vue, Hibernate, Entity Framework, JUnit y
   pytest son nombres de producto**, citados como ejemplos corrientes de su categoría. **No se ha
   consultado la documentación de ninguno**, y **el temario no les atribuye ninguna característica
   más allá de su tipo.**
4. **De Struts, el temario afirma sólo lo que la respuesta oficial afirma**: que se basa en el patrón
   modelo-vista-controlador.
5. **La distinción entre biblioteca y framework —quién llama a quién— es de uso corriente en el
   oficio**, y **ninguna pregunta depende de ella.**

**El resto del tema va como oficio y así se declara**: la tabla de clases de lenguaje según su
paradigma, la razón por la que «dinámico» no distingue en la pregunta 81, el argumento que permite
contestar la 86 sin conocer Struts y la tabla de tipos de framework. **Nada de eso está en un boletín
oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
