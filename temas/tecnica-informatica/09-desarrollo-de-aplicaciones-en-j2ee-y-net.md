# Tema 9 del específico de Técnica Informática · Desarrollo de aplicaciones en J2EE y .NET

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 11 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son dos plataformas empresariales, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Desajuste declarado** | **El enunciado pide dos plataformas y dos de las cuatro preguntas son de gestores de dependencias**, que es materia de alrededor |
| **Extensión** | **1.368 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la edición empresarial de la plataforma Java
(**J2EE**, *Java 2 Enterprise Edition*, hoy llamada **Jakarta EE**); la plataforma de Microsoft
(**.NET**, que se lee «punto net»); la página de servidor de Java (**JSP**, *Java Server Page*); el
servlet, que es la pieza Java que atiende una petición; el kit de desarrollo de Java (**JDK**), su
entorno de ejecución (**JRE**) y su máquina virtual (**JVM**); el gestor de paquetes de la biblioteca
comunitaria de PHP (**PECL**); el actualizador amarillo modificado (**YUM**), que es un gestor de
paquetes de sistema; y **Maven**, **Gradle**, **Ivy** y **Composer**, que son nombres de producto y no
siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 11):
> «Desarrollo de aplicaciones en J2EE y .NET.»

**Cuatro preguntas.** **Y sólo dos son de las dos plataformas que el enunciado nombra**: **las otras
dos son de gestores de dependencias**, que es materia de alrededor.

**Ese desajuste conviene decirlo**: **el enunciado pide dos plataformas empresariales y el examen ha
preguntado sobre todo por las herramientas con que se construyen sus proyectos.**

<!-- indice -->

## Índice

- [1. La plataforma Java empresarial](#1-la-plataforma-java-empresarial)
- [2. Los gestores de dependencias](#2-los-gestores-de-dependencias)
- [3. El entorno de ejecución de Java](#3-el-entorno-de-ejecución-de-java)
- [4. Los datos que el examen ha preguntado](#4-los-datos-que-el-examen-ha-preguntado)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. La plataforma Java empresarial

**La pregunta 74**: **una Java Server Page en J2EE es una tecnología que permite crear páginas web
dinámicas usando código Java.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son cada una otra cosa del mismo mundo**: **un gestor de bases de datos,
un protocolo de comunicación y un marco de pruebas.** **La pregunta se contesta traduciendo el
nombre**: *Java Server Page*, **página de servidor en Java.**

**Las piezas de la plataforma que conviene tener situadas:**

| Pieza | Qué hace |
|---|---|
| **Servlet** | **Clase Java que recibe una petición y devuelve una respuesta**: es la base de todo lo demás |
| **JSP** | **Página con marcado y trozos de Java dentro.** Al compilarse **se convierte en un servlet** ✔ |
| **Contenedor** | **El programa que ejecuta servlets y páginas**: Apache TomCat es el ejemplo del tema 1 |
| **Servidor de aplicaciones** | **Un contenedor con todo lo demás** de la plataforma empresarial |

**La relación entre las dos primeras es la que da sentido al conjunto**: **una JSP no es una
alternativa al servlet, es un servlet escrito de otra manera.** **Se inventó para no tener que generar
el marcado desde código Java, línea a línea.**

**La pregunta 68**: **el tipo del cual heredan todos los tipos de dato de la plataforma .NET es
`System.Object`.** Ésa es la respuesta oficial.

---

**Y ése es el rasgo que define el sistema de tipos de la plataforma**: **hay una raíz única.**
**Cualquier cosa —una clase, una estructura, un número entero— es en última instancia un
`System.Object`.**

**Las opciones falsas son tres tipos reales de la misma biblioteca, y ahí está la dificultad:**

| Tipo | Qué es realmente |
|---|---|
| **`System.Object`** | **La raíz de todo el sistema de tipos** ✔ |
| **`System.ValueType`** | **La raíz de los tipos por valor**, que a su vez hereda de `System.Object` |
| **`System.Type`** | **El tipo que describe a otros tipos**, para la reflexión |
| **`System.Class`** | **No existe** |

**La regla que la contesta sin memorizar**: **si la pregunta dice «TODOS los tipos», la respuesta
tiene que ser la raíz**, y **`ValueType` sólo cubre la mitad.** **Y de las cuatro, la única que puede
ser raíz de todo por su propio nombre es `Object`.**

**El equivalente en Java, porque el examen podría preguntarlo al revés**: **`java.lang.Object` cumple
el mismo papel.** **Las dos plataformas comparten esa idea de raíz única.**

## 2. Los gestores de dependencias

**Dos de las cuatro preguntas son de aquí**, y **las dos se contestan con la misma tabla:**

| Lenguaje o plataforma | Gestores de dependencias |
|---|---|
| **Java** | **Maven**, **Gradle**, **Ivy** |
| **PHP** | **Composer** ✔ |
| **JavaScript y nodeJS** | **npm**, **yarn** |
| **Python** | **pip** |
| **.NET** | **NuGet** |
| **El sistema operativo, que no es lo mismo** | **YUM**, **apt** |

**La pregunta 82 es negativa**: **de las enumeradas, la que NO es un gestor de dependencias de
paquetes Java es Composer.** Ésa es la respuesta oficial.

**La pregunta 94 es la misma al revés**: **el gestor de dependencias de paquetes PHP es Composer.**
Ésa es la respuesta oficial.

---

**Las dos preguntas se contestan con una sola fila de la tabla**, y **conviene notar que el examen ha
puesto la misma respuesta en las dos**, una vez como falsa y otra como verdadera.

**Y el distractor de la 94 merece un aviso**: **PECL sí es de PHP**, pero **no es un gestor de
dependencias de un proyecto: es el repositorio de extensiones del propio lenguaje escritas en C.**
**La distinción es la que separa «lo que mi programa necesita» de «lo que el intérprete trae
instalado».**

**Qué hace un gestor de dependencias, en una línea**: **lee un fichero donde el proyecto declara qué
bibliotecas necesita y en qué versión, las descarga y resuelve las dependencias de esas
dependencias.** **El fichero es `pom.xml` en Maven, `build.gradle` en Gradle y `composer.json` en
Composer.**

## 3. El entorno de ejecución de Java

**Aunque el examen lo pregunta en el tema 13**, **conviene dejar aquí la relación entre las tres
siglas, porque es de esta plataforma:**

| Sigla | Qué contiene |
|---|---|
| **JVM** | **La máquina virtual**: lo que ejecuta el código intermedio |
| **JRE** | **La máquina virtual más las bibliotecas**: lo mínimo para ejecutar |
| **JDK** | **El entorno de ejecución más el compilador y las herramientas**: lo necesario para desarrollar |

**La relación es de muñeca rusa**: **el kit contiene el entorno, y el entorno contiene la máquina
virtual.** **Para ejecutar basta el entorno; para compilar hace falta el kit.**

## 4. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 68 | Tipo del que heredan todos los tipos de .NET | d) `System.Object` ✔ |
| 74 | Qué es una Java Server Page en J2EE | a) Tecnología para crear páginas dinámicas con Java ✔ |
| 82 | Cuál NO es gestor de dependencias de paquetes Java | c) Composer ✔ |
| 94 | Gestor de dependencias de paquetes PHP | d) Composer ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la tabla de gestores por lenguaje contesta dos de las cuatro preguntas y es
lo más barato de memorizar del punto.** **De las plataformas, lo preguntable es la raíz única de tipos
y la relación entre servlet y página de servidor.**

## 5. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las especificaciones de la plataforma Java empresarial y de .NET no se han consultado.** **Lo que
   el tema afirma de una página de servidor y de la raíz del sistema de tipos es de uso universal**,
   y **coincide con las respuestas oficiales.**
2. **Maven, Gradle, Ivy, Composer, npm, yarn, pip, NuGet, YUM, apt, PECL y Apache TomCat son nombres
   de producto**, citados por su categoría. **No se ha consultado la documentación de ninguno**, y
   **el temario no les atribuye ninguna característica más allá de a qué lenguaje sirven.**
3. **Los nombres de fichero `pom.xml`, `build.gradle` y `composer.json` son de uso corriente**, dados
   como ejemplo. **Ninguna pregunta depende de ellos.**
4. **La relación entre máquina virtual, entorno de ejecución y kit de desarrollo se da como
   conocimiento común**, y **la pregunta que la usa está en el tema 13 de esta misma ocupación.**

**El resto del tema va como oficio y así se declara**: la explicación de que una página de servidor se
compila a servlet, la regla de que «todos los tipos» obliga a la raíz, el aviso sobre PECL frente a un
gestor de dependencias de proyecto y la imagen de la muñeca rusa. **Nada de eso está en un boletín
oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
