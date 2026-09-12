# Esquema · Tema 9 del específico de Técnica Informática · Desarrollo de aplicaciones en J2EE y .NET

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de desarrollo · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la edición empresarial de la plataforma Java (**J2EE**,
hoy **Jakarta EE**); la plataforma de Microsoft (**.NET**); la página de servidor de Java (**JSP**);
el servlet, que es la pieza Java que atiende una petición; el kit de desarrollo de Java (**JDK**), su
entorno de ejecución (**JRE**) y su máquina virtual (**JVM**); el gestor de paquetes de la biblioteca
comunitaria de PHP (**PECL**); el actualizador amarillo modificado (**YUM**), gestor de paquetes de
sistema; y **Maven**, **Gradle**, **Ivy** y **Composer**, que son nombres de producto y no siglas.

**Cabecera.** Enunciado: punto 11 del anexo · **4 preguntas** · **ninguna lleva figura** · **el
desajuste que conviene decir**: **el enunciado pide dos plataformas empresariales y dos de las cuatro
preguntas son de gestores de dependencias**, que es materia de alrededor.

<!-- indice -->

## Índice

- [La plataforma Java empresarial](#la-plataforma-java-empresarial)
- [La raíz de tipos de .NET](#la-raíz-de-tipos-de-net)
- [Gestores de dependencias](#gestores-de-dependencias)
- [El entorno de ejecución de Java](#el-entorno-de-ejecución-de-java)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La plataforma Java empresarial

- **PREGUNTA 74** · `[exam]` · **Una Java Server Page es una tecnología para crear páginas web
  dinámicas usando código Java.**
- **SE CONTESTA TRADUCIENDO EL NOMBRE**: *Java Server Page*, **página de servidor en Java.** **Las
  tres falsas son otra cosa del mismo mundo**: un gestor de bases de datos, un protocolo y un marco de
  pruebas.

| Pieza | Qué hace |
|---|---|
| **Servlet** | **Clase Java que recibe una petición y devuelve una respuesta**: la base de todo |
| **JSP** | **Página con marcado y trozos de Java.** Al compilarse **se convierte en un servlet** ✔ |
| **Contenedor** | **El programa que ejecuta servlets y páginas**: Apache TomCat, el del tema 1 |
| **Servidor de aplicaciones** | **Un contenedor con todo lo demás** de la plataforma |

- **LA RELACIÓN QUE DA SENTIDO AL CONJUNTO**: **una JSP no es alternativa al servlet: es un servlet
  escrito de otra manera.** **Se inventó para no generar el marcado desde código Java, línea a
  línea.**

## La raíz de tipos de .NET

- **PREGUNTA 68** · `[exam]` · **Todos los tipos de .NET heredan de `System.Object`.**

| Tipo | Qué es realmente |
|---|---|
| **`System.Object`** | **La raíz de todo el sistema de tipos** ✔ |
| **`System.ValueType`** | **La raíz de los tipos por valor**, que hereda de `System.Object` |
| **`System.Type`** | **El tipo que describe a otros tipos**, para la reflexión |
| **`System.Class`** | **No existe** |

- **LA REGLA QUE LA CONTESTA SIN MEMORIZAR**: **si la pregunta dice «TODOS los tipos», la respuesta es
  la raíz**, y **`ValueType` sólo cubre la mitad.** **De las cuatro, la única que puede ser raíz por su
  propio nombre es `Object`.**
- **EL EQUIVALENTE EN JAVA, POR SI LO PREGUNTAN AL REVÉS**: **`java.lang.Object` hace el mismo
  papel.** **Las dos plataformas comparten la idea de raíz única.**

## Gestores de dependencias

| Lenguaje o plataforma | Gestores |
|---|---|
| **Java** | **Maven**, **Gradle**, **Ivy** |
| **PHP** | **Composer** ✔ |
| **JavaScript y nodeJS** | **npm**, **yarn** |
| **Python** | **pip** |
| **.NET** | **NuGet** |
| **El sistema operativo, que no es lo mismo** | **YUM**, **apt** |

- **PREGUNTA 82** · `[exam]` · **La que NO es gestor de paquetes Java es Composer.**
- **PREGUNTA 94** · `[exam]` · **El gestor de paquetes PHP es Composer.**
- **LAS DOS SE CONTESTAN CON UNA SOLA FILA**, y **el examen ha puesto la misma respuesta en las dos**:
  una vez como falsa y otra como verdadera.
- **EL AVISO SOBRE EL DISTRACTOR DE LA 94**: **PECL sí es de PHP**, pero **no gestiona las
  dependencias de un proyecto: es el repositorio de extensiones del lenguaje escritas en C.** **La
  distinción separa «lo que mi programa necesita» de «lo que el intérprete trae instalado».**
- **QUÉ HACE UN GESTOR, EN UNA LÍNEA**: **lee el fichero donde el proyecto declara qué bibliotecas
  necesita y en qué versión, las descarga y resuelve las dependencias de esas dependencias.** **Es
  `pom.xml` en Maven, `build.gradle` en Gradle y `composer.json` en Composer.**

## El entorno de ejecución de Java

| Sigla | Qué contiene |
|---|---|
| **JVM** | **La máquina virtual**: lo que ejecuta el código intermedio |
| **JRE** | **La máquina virtual más las bibliotecas**: lo mínimo para ejecutar |
| **JDK** | **El entorno más el compilador y las herramientas**: lo necesario para desarrollar |

- **ES UNA MUÑECA RUSA**: **el kit contiene el entorno, y el entorno contiene la máquina virtual.**
  **Para ejecutar basta el entorno; para compilar hace falta el kit.**
- **LA PREGUNTA QUE LO USA CAE EN EL TEMA 13.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 68 | Tipo del que heredan todos los tipos de .NET | d) `System.Object` ✔ |
| 74 | Qué es una Java Server Page | a) Tecnología para páginas dinámicas con Java ✔ |
| 82 | Cuál NO es gestor de paquetes Java | c) Composer ✔ |
| 94 | Gestor de paquetes PHP | d) Composer ✔ |

**Las cuatro oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de gestores por lenguaje contesta dos de las cuatro y es lo más barato de memorizar.** **De
las plataformas, lo preguntable es la raíz única de tipos y la relación entre servlet y página de
servidor.**
