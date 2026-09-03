# Esquema · Tema 6 del específico de Técnica Informática · Programación orientada a objetos y frameworks

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de desarrollo · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la programación orientada a objetos (**POO**); el patrón
modelo-vista-controlador (**MVC**); el lenguaje de consulta estructurado (**SQL**) y la notación de
objetos de JavaScript (**JSON**), que salen como opciones falsas; y **C**, **C++**, **C#**, **Java** y
**Python**, que son nombres de lenguaje y no siglas.

**Cabecera.** Enunciado: puntos 7 y 8 del anexo, que el examen ha tratado como uno · **6 preguntas** ·
**ninguna lleva figura** · **una lleva salvedad declarada**: la 5, cuyo enunciado afirma de Python
algo que no es cierto.

<!-- indice -->

## Índice

- [Los cuatro pilares](#los-cuatro-pilares)
- [Sobrecarga y sobrescritura](#sobrecarga-y-sobrescritura)
- [Python, y la pregunta discutible](#python-y-la-pregunta-discutible)
- [Estructuras de datos](#estructuras-de-datos)
- [Frameworks y el patrón](#frameworks-y-el-patrón)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los cuatro pilares

| Pilar | Qué significa |
|---|---|
| **Abstracción** | **Quedarse con lo que importa y desechar el resto** |
| **Encapsulación** | **Esconder el estado interno y dar acceso sólo por métodos** |
| **Herencia** | **Que una clase reciba atributos y métodos de otra** |
| **Polimorfismo** | **Que la misma llamada haga cosas distintas según el objeto** |

- **LOS DOS TÉRMINOS QUE ORDENAN TODO**: **la clase es el molde y el objeto es la pieza.**
  **Instanciar es fabricar una pieza con el molde.**
- **PREGUNTA 38** · `[exam]` · **El lenguaje con clases, objetos y herencia es Java.**
- **LAS TRES FALSAS NO SON ORIENTADAS A OBJETOS**, cada una por su motivo: **C es estructurado y no
  tiene clases; SQL es de consulta, no de propósito general; JSON no es un lenguaje: es un formato de
  datos**, como explica el tema 10.

## Sobrecarga y sobrescritura

- **PREGUNTA 92** · `[exam]` · **Sobrecargar es crear un método con el mismo nombre y distintos
  argumentos.**

| Término | Qué es | Dónde ocurre |
|---|---|---|
| **Sobrecarga** (*overload*) | **Varios métodos, mismo nombre, distintos argumentos** | **En la misma clase** ✔ |
| **Sobrescritura** (*override*) | **Un método que reemplaza al heredado, con la misma firma** | **En una clase hija** |

- **LA REGLA DE MEMORIA**: **sobrecargar es añadir versiones; sobrescribir es sustituir la heredada.**
- **EL DISTRACTOR BUENO** —«editarlo para modificar su comportamiento»— **describe la
  sobrescritura.**

## Python, y la pregunta discutible

- **PREGUNTA 5** · `[exam]` · **El lenguaje en el que NO se puede instanciar una clase es Python.**
- **LA SALVEDAD, DECLARADA**: **en Python se instancian clases todos los días**, con el nombre de la
  clase y paréntesis. **Lo que la oficial parece perseguir es que Python no obliga a declarar
  clases**, frente a Java, C# y C++, donde todo vive dentro de una. **Se marca la de la plantilla**, y
  **el temario declara que su enunciado no dice lo que la respuesta necesita.**
- **PREGUNTA 18** · `[exam]` · **Python es compatible con la orientación a objetos y con la
  imperativa, entre otras.** **Ésta sí está bien construida.**

| Clase de lenguaje | Qué significa | Ejemplos |
|---|---|---|
| **Orientado a objetos puro** | **Todo es objeto y no cabe otro modo** | **Smalltalk** |
| **Multiparadigma** | **Objetos, imperativo, funcional y más** | **Python**, **C++**, **JavaScript** ✔ |
| **Con clase obligatoria** | **Todo el código vive en una clase** | **Java**, **C#** |
| **Estructurado, sin objetos** | **Funciones y estructuras, sin clases** | **C** |

- **LAS DOS PREGUNTAS JUNTAS DICEN ALGO ÚTIL**: **Python es multiparadigma**, y eso es a la vez la
  respuesta de la 18 y lo que hace discutible la 5.

## Estructuras de datos

- **PREGUNTA 81** · `[exam]` · **El tipo estructurado, dinámico y NO lineal es el árbol.**

| Estructura | Lineal | Cómo se recorre |
|---|---|---|
| **Pila** | **Sí** | **Último en entrar, primero en salir** |
| **Cola** | **Sí** | **Primero en entrar, primero en salir** |
| **Lista** | **Sí** | **Elemento tras elemento** |
| **Árbol** | **NO** | **Por ramas: cada nodo puede tener varios hijos** ✔ |
| **Grafo** | **NO** | **Por aristas, y puede tener ciclos** |

- **LA PALABRA QUE DECIDE ES «LINEAL»**: **lineal es que cada elemento tenga como mucho un anterior y
  un siguiente**, y **en un árbol un nodo tiene varios siguientes.**
- **«DINÁMICO» NO DISTINGUE**: **las cuatro opciones lo son.**

## Frameworks y el patrón

- **QUÉ ES UN FRAMEWORK, CON PRECISIÓN** · `[of]` · **un armazón que trae resueltas las decisiones
  repetitivas y que llama al código del programador**, no al revés. **A una biblioteca la llamas tú;
  un framework te llama a ti.**
- **PREGUNTA 86** · `[exam]` · **Struts se basa en el patrón modelo-vista-controlador.**

| Pieza | De qué se ocupa |
|---|---|
| **Modelo** | **Los datos y las reglas de negocio** |
| **Vista** | **Cómo se presentan al usuario** |
| **Controlador** | **Recibe la petición, pide al modelo y elige la vista** |

- **PARA QUÉ SEPARARLOS**: **para cambiar la presentación sin tocar las reglas, y al revés.**
- **SE CONTESTA SIN CONOCER STRUTS**: **si de cuatro opciones una es un patrón de presentación y las
  otras tres son de despliegue —cliente-servidor, capas, maestro-esclavo—, la respuesta es la
  primera.**

| Tipo | Para qué | Ejemplos |
|---|---|---|
| **Web de servidor** | **Generar respuestas y coordinar la lógica** | **Struts**, **Spring**, **Django**, **Laravel** |
| **Web de cliente** | **Construir la interfaz en el navegador** | **Angular**, **React**, **Vue** |
| **De persistencia** | **Traducir entre objetos y tablas** | **Hibernate**, **Entity Framework** |
| **De pruebas** | **Automatizar la comprobación del código** | **JUnit**, **pytest** |

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 5 | Lenguaje en el que NO se puede instanciar una clase | d) Python ✔ **·** enunciado discutible |
| 18 | Qué tipo de lenguaje es Python | d) Compatible con objetos e imperativa ✔ |
| 38 | Lenguaje con clases, objetos y herencia | d) Java ✔ |
| 81 | Tipo estructurado, dinámico y NO lineal | c) Árbol ✔ |
| 86 | Patrón en que se basa Struts | a) Modelo-Vista-Controlador ✔ |
| 92 | Qué significa sobrecargar un método | c) Mismo nombre, distintos argumentos ✔ |

**Las seis oficiales son la mejor de sus cuatro opciones** · **ninguna descansa en la plantilla** ·
**una lleva salvedad declarada.** · **Aviso de estudio**: **la pareja sobrecarga y sobrescritura, y la
división en lineales y no lineales, son las dos distinciones que este punto mide.** **Caben en cuatro
líneas y contestan dos preguntas.**
