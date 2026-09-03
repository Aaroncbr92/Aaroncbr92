# Tema 13 del específico de Técnica Informática · Otros lenguajes: C, C++, Java y Python

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 15 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son cuatro lenguajes de programación, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Desajuste declarado** | **El enunciado nombra C y C++ primero, y de los dos no ha caído ninguna pregunta.** Las tres son de Java o de Python |
| **Extensión** | **1.290 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la máquina virtual de Java (**JVM**, *Java Virtual
Machine*), su entorno de ejecución (**JRE**) y su kit de desarrollo (**JDK**, *Java Development Kit*);
la interfaz de programación de aplicaciones (**API**); el instalador de paquetes de Python (**PIP**); el preprocesador de hipertexto (**PHP**);
y **C**, **C++**, **Java**, **Python**, **Django**, **Composer** y **PyManager**, que son nombres de
lenguaje o de producto y no siglas —el último, además, **no existe: es un distractor del examen.**

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 15):
> «Otros lenguajes de programación: C, C++, Java y Python.»

**Tres preguntas.** **Y las tres son de Java o de Python**: **de C y de C++ no ha caído ninguna**,
aunque el enunciado los nombra primero.

**Su reparto**: **dos son del entorno de Java** y **una del gestor de paquetes de Python.**

<!-- indice -->

## Índice

- [1. Por qué Java se ejecuta en cualquier plataforma](#1-por-qué-java-se-ejecuta-en-cualquier-plataforma)
- [2. Las tres siglas de Java](#2-las-tres-siglas-de-java)
- [3. Python y su gestor de paquetes](#3-python-y-su-gestor-de-paquetes)
- [4. Los cuatro lenguajes del enunciado, uno frente a otro](#4-los-cuatro-lenguajes-del-enunciado-uno-frente-a-otro)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Por qué Java se ejecuta en cualquier plataforma

**La pregunta 55**: **un programa escrito en Java puede ejecutarse en cualquier plataforma porque la
máquina virtual de Java interpreta el programa para cada sistema operativo.** Ésa es la respuesta
oficial.

---

**La cadena completa, que es lo que hay que entender:**

1. **El compilador de Java no produce código de la máquina**: **produce código intermedio**, el mismo
   para todos los sistemas.
2. **Ese código intermedio lo ejecuta la máquina virtual.**
3. **La máquina virtual SÍ es distinta en cada sistema operativo**, y es lo único que hay que portar.

**De ahí la frase que resume el modelo**: **se escribe una vez y se ejecuta en todas partes.** **Lo
portable no es el programa: es que hay una máquina virtual en cada sitio.**

**Y las tres opciones falsas se desmontan una a una:**

| Opción | Por qué es falsa |
|---|---|
| **b) La interfaz de programación se diseñó con ese fin** | **La biblioteca ayuda, pero no es lo que permite ejecutar el mismo binario en dos sistemas** |
| **c) Java deriva de C y C++** | **Cierto en la sintaxis y sin relación con la portabilidad**: C y C++ no son portables en binario |
| **d) Java es un lenguaje interpretado** | **Es a medias**: se compila a código intermedio y ese código se interpreta o se compila al vuelo. **No es interpretado en el sentido en que lo es un guion** |

**El aviso de precisión, porque la opción d es un distractor bueno**: **la respuesta oficial usa la
palabra «interpreta» para lo que hace la máquina virtual**, y **la opción d la usa para calificar al
lenguaje.** **Lo que se interpreta no es el código fuente: es el intermedio.**

## 2. Las tres siglas de Java

**La pregunta 75**: **las siglas JDK significan *Java Development Kit*.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son la misma expresión con una palabra cambiada** —*Developer* en vez de
*Development*, *Knowledge* en vez de *Kit*—, **lo que la convierte en memoria literal.**

**Las tres siglas, con la relación de muñeca rusa que las ordena:**

| Sigla | Qué es | Qué contiene |
|---|---|---|
| **JVM** | **La máquina virtual** | **El motor que ejecuta el código intermedio** |
| **JRE** | **El entorno de ejecución** | **La máquina virtual más las bibliotecas** |
| **JDK** | **El kit de desarrollo** | **El entorno de ejecución más el compilador y las herramientas** ✔ |

**La regla que las fija**: **para ejecutar basta el entorno; para compilar hace falta el kit.**

## 3. Python y su gestor de paquetes

**La pregunta 84**: **el gestor de dependencias de paquetes de Python es PIP.** Ésa es la respuesta
oficial.

---

**Y las tres opciones falsas se descartan cada una por un motivo distinto**, lo que hace de ésta una
buena pregunta:

| Opción | Qué es |
|---|---|
| **Composer** | **El gestor de PHP**, que el tema 9 ya identificó |
| **PIP** | **El de Python** ✔ |
| **Django** | **Un marco web de Python**, no un gestor de paquetes |
| **PyManager** | **No existe** |

**El distractor bueno es Django**, porque **sí es de Python.** **Lo que lo descarta es que un marco de
trabajo y un gestor de dependencias no son la misma clase de herramienta**: uno estructura el
programa, el otro trae las bibliotecas.

**Y el dato de oficio que conviene añadir**: **lo corriente en Python es combinar el gestor con un
entorno virtual**, de modo que cada proyecto tenga sus propias versiones de biblioteca sin pisar las
del sistema. **Instalar dependencias en el Python del sistema operativo es la fuente clásica de
conflictos.**

## 4. Los cuatro lenguajes del enunciado, uno frente a otro

**El punto los nombra y el examen sólo ha entrado por dos**, así que **conviene tener la comparación
hecha:**

| | **C** | **C++** | **Java** | **Python** |
|---|---|---|---|---|
| **Paradigma** | **Estructurado** | **Multiparadigma, con objetos** | **Orientado a objetos, clase obligatoria** | **Multiparadigma** |
| **Compilación** | **A código de la máquina** | **A código de la máquina** | **A código intermedio** | **Interpretado, con compilación intermedia** |
| **Tipado** | **Estático y débil** | **Estático** | **Estático** | **Dinámico** |
| **Gestión de memoria** | **Manual** | **Manual, con ayudas** | **Recolector de basura** | **Recolector de basura** |
| **Dónde se usa** | **Sistemas, controladores, empotrados** | **Aplicaciones exigentes, juegos** | **Aplicaciones empresariales** | **Automatización, datos, web** |

**Las dos filas que más se preguntan son la de compilación y la de gestión de memoria**, porque **son
las que explican los defectos típicos de cada lenguaje**: **en C hay fugas de memoria y
desbordamientos de búfer porque la gestiona el programador**; **en Java y Python no los hay, y a
cambio hay pausas del recolector.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 55 | Por qué un programa Java se ejecuta en cualquier plataforma | a) La máquina virtual lo interpreta para cada sistema ✔ |
| 75 | Qué significan las siglas JDK | d) *Java Development Kit* ✔ |
| 84 | Gestor de dependencias de paquetes de Python | b) PIP ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **una es memoria literal, otra es la cadena de la máquina virtual y la
tercera es una tabla de gestores que el tema 9 ya trae.** **De lo que no ha caído, lo preguntable es
la comparación de los cuatro lenguajes del epígrafe 4.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Tres declaraciones expresas:**

1. **Las especificaciones de Java y de Python no se han consultado.** **El funcionamiento de la
   máquina virtual, la relación entre sus tres siglas y el nombre del gestor de paquetes de Python son
   de uso universal**, y **coinciden con las respuestas oficiales.**
2. **La forma larga de JDK procede de la propia respuesta oficial de la pregunta 75.**
3. **Composer, Django, PIP y PyManager se reproducen de las opciones del examen.** **De PyManager el
   temario afirma que no existe**, que es lo que hace correcta la respuesta marcada.

**El resto del tema va como oficio y así se declara**: la cadena de compilación y ejecución de Java,
el desmontaje de sus tres opciones falsas, la precisión sobre qué se interpreta, el aviso sobre los
entornos virtuales de Python y la tabla comparativa de los cuatro lenguajes. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
