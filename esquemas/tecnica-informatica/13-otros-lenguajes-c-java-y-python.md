# Esquema · Tema 13 del específico de Técnica Informática · Otros lenguajes: C, C++, Java y Python

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de desarrollo · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la máquina virtual de Java (**JVM**), su entorno de
ejecución (**JRE**) y su kit de desarrollo (**JDK**); la interfaz de programación de aplicaciones
(**API**); el instalador de paquetes de Python (**PIP**); el preprocesador de hipertexto (**PHP**); y
**C**, **C++**, **Java**, **Python**, **Django**, **Composer** y **PyManager**, que son nombres de
lenguaje o de producto y no siglas —el último, además, **no existe: es un distractor del examen.**

**Cabecera.** Enunciado: punto 15 del anexo · **3 preguntas** · **ninguna lleva figura** · **las tres
son de Java o de Python**: **de C y de C++ no ha caído ninguna**, aunque el enunciado los nombra
primero.

<!-- indice -->

## Índice

- [Por qué Java corre en cualquier plataforma](#por-qué-java-corre-en-cualquier-plataforma)
- [Las tres siglas de Java](#las-tres-siglas-de-java)
- [Python y su gestor de paquetes](#python-y-su-gestor-de-paquetes)
- [Los cuatro lenguajes del enunciado](#los-cuatro-lenguajes-del-enunciado)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Por qué Java corre en cualquier plataforma

- **PREGUNTA 55** · `[exam]` · **Porque la máquina virtual de Java interpreta el programa para cada
  sistema operativo.**
- **LA CADENA COMPLETA**: **el compilador no produce código de la máquina, sino código intermedio, el
  mismo para todos los sistemas** → **ese código lo ejecuta la máquina virtual** → **la máquina
  virtual SÍ es distinta en cada sistema, y es lo único que hay que portar.**
- **LA FRASE QUE RESUME EL MODELO**: **se escribe una vez y se ejecuta en todas partes.** **Lo
  portable no es el programa: es que hay una máquina virtual en cada sitio.**

| Opción falsa | Por qué lo es |
|---|---|
| **La interfaz de programación se diseñó con ese fin** | **La biblioteca ayuda, pero no es lo que permite ejecutar el mismo binario en dos sistemas** |
| **Java deriva de C y C++** | **Cierto en la sintaxis y sin relación con la portabilidad**: C y C++ no son portables en binario |
| **Java es un lenguaje interpretado** | **A medias**: se compila a código intermedio, y ése se interpreta o se compila al vuelo |

- **EL AVISO DE PRECISIÓN, PORQUE LA ÚLTIMA ES BUEN DISTRACTOR**: **la oficial usa «interpreta» para
  lo que hace la máquina virtual y la falsa para calificar al lenguaje.** **Lo que se interpreta no es
  el código fuente: es el intermedio.**

## Las tres siglas de Java

- **PREGUNTA 75** · `[exam]` · **JDK es *Java Development Kit*.**
- **LAS TRES FALSAS SON LA MISMA EXPRESIÓN CON UNA PALABRA CAMBIADA** —*Developer* por *Development*,
  *Knowledge* por *Kit*—: **memoria literal.**

| Sigla | Qué es | Qué contiene |
|---|---|---|
| **JVM** | **La máquina virtual** | **El motor que ejecuta el código intermedio** |
| **JRE** | **El entorno de ejecución** | **La máquina virtual más las bibliotecas** |
| **JDK** | **El kit de desarrollo** | **El entorno más el compilador y las herramientas** ✔ |

- **LA REGLA QUE LAS FIJA**: **para ejecutar basta el entorno; para compilar hace falta el kit.**

## Python y su gestor de paquetes

- **PREGUNTA 84** · `[exam]` · **El gestor de dependencias de Python es PIP.**

| Opción | Qué es |
|---|---|
| **Composer** | **El gestor de PHP**, ya identificado en el tema 9 |
| **PIP** | **El de Python** ✔ |
| **Django** | **Un marco web de Python**, no un gestor |
| **PyManager** | **No existe** |

- **EL DISTRACTOR BUENO ES DJANGO**, porque **sí es de Python**: **lo descarta que un marco y un
  gestor no sean la misma clase de herramienta** —uno estructura el programa, el otro trae las
  bibliotecas.
- **EL DATO DE OFICIO** · `[of]` · **lo corriente en Python es combinar el gestor con un entorno
  virtual**, para que cada proyecto tenga sus versiones sin pisar las del sistema. **Instalar
  dependencias en el Python del sistema operativo es la fuente clásica de conflictos.**

## Los cuatro lenguajes del enunciado

| | **C** | **C++** | **Java** | **Python** |
|---|---|---|---|---|
| **Paradigma** | **Estructurado** | **Multiparadigma, con objetos** | **Objetos, clase obligatoria** | **Multiparadigma** |
| **Compilación** | **A código de la máquina** | **A código de la máquina** | **A código intermedio** | **Interpretado, con compilación intermedia** |
| **Tipado** | **Estático y débil** | **Estático** | **Estático** | **Dinámico** |
| **Memoria** | **Manual** | **Manual, con ayudas** | **Recolector de basura** | **Recolector de basura** |
| **Dónde se usa** | **Sistemas, controladores, empotrados** | **Aplicaciones exigentes, juegos** | **Aplicaciones empresariales** | **Automatización, datos, web** |

- **LAS DOS FILAS MÁS PREGUNTABLES SON COMPILACIÓN Y MEMORIA**, porque **explican los defectos típicos
  de cada lenguaje**: **en C hay fugas y desbordamientos de búfer porque la gestiona el programador;
  en Java y Python no los hay, y a cambio hay pausas del recolector.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 55 | Por qué un programa Java corre en cualquier plataforma | a) La máquina virtual lo interpreta para cada sistema ✔ |
| 75 | Qué significan las siglas JDK | d) *Java Development Kit* ✔ |
| 84 | Gestor de dependencias de Python | b) PIP ✔ |

**Las tres oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**una es memoria literal, otra es la cadena de la máquina virtual y la tercera está en la tabla de
gestores del tema 9.** **De lo que no ha caído, lo preguntable es la comparación de los cuatro
lenguajes.**
