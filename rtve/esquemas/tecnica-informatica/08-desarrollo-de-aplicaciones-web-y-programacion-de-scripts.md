# Esquema · Tema 8 del específico de Técnica Informática · Desarrollo de aplicaciones web y programación de scripts

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de desarrollo web · `[exam]` =
opciones del propio cuadernillo. **Siglas**: el lenguaje de marcado de hipertexto (**HTML**), en su
quinta versión (**HTML5**) y en su variante bien formada (**XHTML**); las hojas de estilo en cascada
(**CSS**), en su tercera versión (**CSS3**); el estándar en que se basa JavaScript (**ECMAScript**, de
ahí **ECMAScript6**); el modelo de objetos del documento (**DOM**); la señal web en formato de objeto
de JavaScript (**JWT**); la aplicación de página única (**SPA**); el preprocesador de hipertexto
(**PHP**); el protocolo de transferencia de hipertexto (**HTTP**); el lenguaje de marcado extensible
(**XML**); la plataforma de Microsoft (**.NET**); y **nodeJS**, **Angular**, **jQuery**, **Laravel**,
**Spring** y **VBScript**, que son nombres de producto o de lenguaje y no siglas.

**Cabecera.** Enunciado: punto 10 del anexo · **8 preguntas: el segundo banco de la ocupación**,
empatado con el de redes · **ninguna lleva figura** · **tres son memoria de sintaxis y cinco se
razonan.**

<!-- indice -->

## Índice

- [Dónde se ejecuta cada lenguaje](#dónde-se-ejecuta-cada-lenguaje)
- [Hojas de estilo](#hojas-de-estilo)
- [Marcado](#marcado)
- [JavaScript: ámbito, asincronía y señales](#javascript-ámbito-asincronía-y-señales)
- [Marcos de trabajo del cliente](#marcos-de-trabajo-del-cliente)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Dónde se ejecuta cada lenguaje

| Lado | Qué corre ahí | Quién lo ve |
|---|---|---|
| **Cliente, el navegador** | **HTML**, **CSS**, **JavaScript** | **El usuario lee todo el código** |
| **Servidor** | **PHP**, **Java**, **Python**, **nodeJS**, **.NET** | **El usuario sólo recibe el resultado** |

- **PREGUNTA 46** · `[exam]` · **El que se ejecuta únicamente en el servidor es PHP.**
- **LAS TRES FALSAS ESTÁN EN EL OTRO LADO**: **HTML es marcado que interpreta el navegador**;
  **JavaScript corre en el navegador y, con nodeJS, también en el servidor —la palabra «únicamente» lo
  descarta—**; **VBScript era de guiones de navegador, hoy retirado.**
- **LA CONSECUENCIA DE SEGURIDAD** · `[of]` · **todo lo que se valida en el cliente se puede saltar**,
  porque el usuario controla su navegador. **La validación del cliente es comodidad; la que protege es
  la del servidor.**

## Hojas de estilo

- **PREGUNTA 50** · `[exam]` · **La alineación horizontal del texto es `text-align`.**
- **PREGUNTA 4** · `[exam]` · **La pseudoclase de los pares es `:nth-child(2n)`.**
- **LAS DOS SON MEMORIA DE SINTAXIS**, y **las falsas son nombres inventados que suenan bien**:
  `horizontal-justify` y `justify` no son propiedades; `:even`, `:is(even)` y `:even()` no son
  pseudoclases.
- **LO QUE HACE RAZONABLE LA SEGUNDA**: **`:nth-child()` recibe una fórmula `an+b`**, y **`2n` genera
  2, 4, 6, 8…** **Con `2n+1` salen los impares.** **No hay que memorizar `:even`: hay que saber leer
  la fórmula.**

| Propiedad | Qué alinea |
|---|---|
| **`text-align`** | **El texto dentro de su caja** ✔ |
| **`vertical-align`** | **Los elementos en línea, en vertical** |
| **`justify-content`** | **El eje principal de un contenedor flexible** |
| **`align-items`** | **El eje transversal de un contenedor flexible** |

## Marcado

- **PREGUNTA 40** · `[exam]` · **El elemento de HTML5 para reproducir audio sin complementos es la
  etiqueta `audio`.**
- **ÉSE ES EL CAMBIO QUE TRAJO LA QUINTA VERSIÓN**: **antes hacía falta un complemento externo.**

| Elemento | Para qué |
|---|---|
| **`audio` y `video`** | **Medios sin complementos** ✔ |
| **`canvas`** | **Dibujar por programa** |
| **`header`, `footer`, `nav`, `section`, `article`, `aside`** | **Estructura semántica**: decir qué es cada parte |

- **HTML FRENTE A XHTML**: **XHTML es HTML con las reglas estrictas de XML** —toda etiqueta cerrada,
  todo atributo entrecomillado, todo en minúscula—. **HTML5 es más tolerante**, y por eso es el que se
  usa.

## JavaScript: ámbito, asincronía y señales

- **PREGUNTA 66** · `[exam]` · **El objeto global que actúa como ámbito de las variables es
  `window`.**

| Objeto | Qué representa |
|---|---|
| **`window`** | **La ventana del navegador**: el ámbito global ✔ |
| **`document`** | **El documento cargado**: la raíz del modelo de objetos |
| **`global`** | **El ámbito global de nodeJS**, no el del navegador |
| **`body`** | **Un elemento del documento**, no un ámbito |

- **EL BUEN DISTRACTOR ES `document`**, porque **ahí vive el árbol de elementos**; **pero lo que se
  pide es el ámbito global de las variables.**
- **PREGUNTA 59** · `[exam]` · **Los WebSockets notifican mediante eventos (`addEventListener()`) y
  retrollamadas (`onmessage()`).**

| Mecanismo | Cómo se escribe | Qué problema tiene |
|---|---|---|
| **Retrollamada** | **Se pasa una función que se llamará después** | **Anidarlas da el «infierno de retrollamadas»** |
| **Promesa** | **`then()`, `catch()`, `finally()`** | **Encadena en vez de anidar** |
| **`async` / `await`** | **Lo asíncrono escrito como secuencial** | **Es azúcar sobre las promesas** |

- **LO QUE DECIDE LA 59**: **los WebSockets no usan promesas: su interfaz es de eventos y
  retrollamadas.** **Y `try / catch / finally` no es notificación asíncrona**: es manejo de errores
  síncronos.
- **QUÉ ES UN WEBSOCKET, EN UNA LÍNEA**: **una conexión permanente y bidireccional entre navegador y
  servidor**, frente al modelo de petición y respuesta de HTTP. **Es lo que permite que el servidor
  hable primero.**
- **PREGUNTA 20** · `[exam]` · **Un JWT consta de tres partes separadas por un punto.**

| Parte | Qué lleva |
|---|---|
| **Cabecera** | **El algoritmo de firma y el tipo** |
| **Cuerpo** | **Quién es el usuario, hasta cuándo vale, qué puede hacer** |
| **Firma** | **Lo que impide modificar las dos anteriores sin que se note** |

- **LAS TRES FALSAS SE DESMONTAN CON UNA IDEA**: **un JWT no se guarda en el servidor.** **Revocarlo
  NO es más fácil que con cookies: es al revés, y es su mayor inconveniente** —un token válido lo
  sigue siendo hasta que caduca—; **y no está restringido a cliente-servidor ni a servidor-servidor:
  sirve para los dos.**
- **EL AVISO**: **el cuerpo va codificado, no cifrado.** **Cualquiera puede leerlo**; la firma sólo
  impide cambiarlo. **No se meten datos sensibles en un token.**

## Marcos de trabajo del cliente

- **PREGUNTA 73** · `[exam]` · **El marco de JavaScript por componentes para aplicaciones de página
  única es Angular.**

| Opción | Qué es |
|---|---|
| **Laravel** | **Marco de PHP**, de servidor |
| **Spring** | **Marco de Java**, de servidor |
| **Angular** | **Marco de JavaScript de cliente, por componentes** ✔ |
| **jQuery** | **Biblioteca, no marco**, y no va por componentes |

- **LAS TRES FALSAS SE DESCARTAN SIN CONOCER NINGUNO**, sólo por su lenguaje.
- **EL DISTRACTOR BUENO ES JQUERY**, que **sí es de JavaScript y de cliente**: **lo descartan las dos
  condiciones añadidas** —por componentes y página única—.
- **QUÉ ES UNA APLICACIÓN DE PÁGINA ÚNICA**: **el navegador carga una sola página y después sustituye
  trozos sin volver a pedir el documento entero.** **La navegación la lleva el propio JavaScript** y
  el servidor sólo manda datos.

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 4 | Pseudoclase de los elementos pares | c) `:nth-child(2n)` ✔ |
| 20 | Afirmación correcta sobre un JWT | b) Tres partes separadas por un punto ✔ |
| 40 | Elemento de HTML5 para audio | b) La etiqueta `audio` ✔ |
| 46 | Lenguaje sólo de servidor | b) PHP ✔ |
| 50 | Propiedad de alineación horizontal | b) `text-align` ✔ |
| 59 | Cómo notifican los WebSockets | d) Eventos y retrollamadas ✔ |
| 66 | Objeto global de JavaScript | a) `window` ✔ |
| 73 | Marco por componentes para página única | c) Angular ✔ |

**Las ocho oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de qué se ejecuta en cada lado contesta una pregunta entera y ayuda en la de los marcos.**
