# Tema 8 del específico de Técnica Informática · Desarrollo de aplicaciones web y programación de scripts

Las siglas de este tema, presentadas de entrada: el lenguaje de marcado de hipertexto (**HTML**), en
su quinta versión (**HTML5**) y en su variante bien formada (**XHTML**); las hojas de estilo en
cascada (**CSS**), en su tercera versión (**CSS3**); el estándar del lenguaje en que se basa
JavaScript (**ECMAScript**, y de ahí **ECMAScript6**); el modelo de objetos del documento (**DOM**);
la señal web en formato de objeto de JavaScript (**JWT**, *JSON web token*); la aplicación de página
única (**SPA**, *single page application*); el preprocesador de hipertexto (**PHP**); el protocolo de transferencia de
hipertexto (**HTTP**); el lenguaje de marcado extensible (**XML**); la plataforma de Microsoft
(**.NET**, que se lee «punto net»); y **nodeJS**,
**Angular**, **jQuery**, **Laravel**, **Spring** y **VBScript**, que son nombres de producto o de
lenguaje y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 10):
> «Desarrollo de aplicaciones web y programación de scripts: HTML, XHTML, CSS3, Javascript
> (ECMAScript6), Asincronía, Web Sockets, nodeJS, PHP.»

**Ocho preguntas: el segundo banco de la ocupación**, empatado con el punto de redes.

**Su reparto**: **dos preguntas son de hojas de estilo**, **una de marcado**, **tres de JavaScript**,
**una de dónde se ejecuta cada lenguaje** y **una de marcos de trabajo.**

<!-- indice -->

## Índice

- [1. Dónde se ejecuta cada lenguaje](#1-dónde-se-ejecuta-cada-lenguaje)
- [2. Las hojas de estilo](#2-las-hojas-de-estilo)
- [3. El marcado](#3-el-marcado)
- [4. JavaScript: objeto global, asincronía y señales](#4-javascript-objeto-global-asincronía-y-señales)
- [5. Los marcos de trabajo del cliente](#5-los-marcos-de-trabajo-del-cliente)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Dónde se ejecuta cada lenguaje

**Es la división que ordena el punto entero, y la que el examen pregunta primero:**

| Lado | Qué corre ahí | Quién lo ve |
|---|---|---|
| **Cliente, el navegador** | **HTML**, **CSS**, **JavaScript** | **El usuario puede leer todo el código** |
| **Servidor** | **PHP**, **Java**, **Python**, **nodeJS**, **.NET** | **El usuario sólo recibe el resultado** |

**La pregunta 46**: **en la arquitectura cliente-servidor, el lenguaje que se ejecuta únicamente en el
lado del servidor es PHP.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas están cada una en el otro lado**: **HTML es marcado que interpreta el
navegador**; **JavaScript se ejecuta en el navegador**, y aunque con nodeJS también corre en el
servidor, **la palabra «únicamente» lo descarta**; **y VBScript era un lenguaje de guiones de
navegador, hoy retirado.**

**La consecuencia de seguridad que se deriva y conviene tener presente**: **todo lo que se valida en
el cliente se puede saltar**, porque el usuario controla su navegador. **La validación del cliente es
para comodidad; la que protege es la del servidor.**

## 2. Las hojas de estilo

**La pregunta 50**: **la propiedad CSS que establece la alineación horizontal del texto dentro de un
elemento es `text-align`.** Ésa es la respuesta oficial.

**La pregunta 4**: **la pseudoclase de CSS que permite seleccionar los elementos pares es
`:nth-child(2n)`.** Ésa es la respuesta oficial.

---

**Las dos son de memoria de sintaxis**, y **las opciones falsas de las dos son nombres inventados que
suenan bien**: `horizontal-justify` y `justify` no existen como propiedades; `:even`, `:is(even)` y
`:even()` no existen como pseudoclases.

**Lo que sí conviene entender de la segunda, porque es lo que la hace razonable**: **`:nth-child()`
recibe una fórmula en la forma `an+b`**, y **`2n` genera 2, 4, 6, 8…**, que son los pares. **Con `2n+1`
salen los impares.** **No hay que memorizar `:even` porque no existe; hay que saber leer la fórmula.**

**Las propiedades de alineación que se confunden entre sí:**

| Propiedad | Qué alinea |
|---|---|
| **`text-align`** | **El texto dentro de su caja**: izquierda, derecha, centro, justificado ✔ |
| **`vertical-align`** | **La alineación vertical de elementos en línea** |
| **`justify-content`** | **El reparto en el eje principal de un contenedor flexible** |
| **`align-items`** | **El reparto en el eje transversal de un contenedor flexible** |

## 3. El marcado

**La pregunta 40**: **el elemento que se utiliza en HTML5 para reproducir audio sin recurrir a
complementos es la etiqueta `audio`.** Ésa es la respuesta oficial.

---

**Y ése es precisamente el cambio que trajo la quinta versión**: **antes hacía falta un complemento
externo para reproducir medios**, y **HTML5 incorporó `audio` y `video` como elementos nativos.**

**Los elementos que HTML5 añadió y que conviene tener vistos:**

| Elemento | Para qué |
|---|---|
| **`audio` y `video`** | **Reproducir medios sin complementos** ✔ |
| **`canvas`** | **Dibujar por programa** |
| **`header`, `footer`, `nav`, `section`, `article`, `aside`** | **Estructura semántica**: decir qué es cada parte, no sólo cómo se ve |

**Y la diferencia entre HTML y XHTML que el enunciado nombra**: **XHTML es HTML escrito con las reglas
estrictas de XML** —toda etiqueta se cierra, todo atributo va entrecomillado, todo en minúscula—.
**HTML5 es más tolerante**, y por eso es el que se usa.

## 4. JavaScript: objeto global, asincronía y señales

**La pregunta 66**: **en JavaScript dentro de un documento HTML, el objeto global que actúa como
ámbito global para las variables creadas y en el que los elementos del modelo de objetos del documento
son accesibles por su identificador es `window`.** Ésa es la respuesta oficial.

---

**Y la distinción que la pregunta persigue es ésta:**

| Objeto | Qué representa |
|---|---|
| **`window`** | **La ventana del navegador**: es el ámbito global del navegador ✔ |
| **`document`** | **El documento cargado dentro de esa ventana**: la raíz del modelo de objetos |
| **`global`** | **El ámbito global de nodeJS**, no el del navegador |
| **`body`** | **Un elemento del documento**, no un ámbito |

**La opción `document` es el buen distractor**, porque **es donde vive el árbol de elementos**; **pero
lo que la pregunta pide es el ámbito global de las variables**, y ése es `window`.

**La pregunta 59**: **los WebSockets de JavaScript notifican la recepción de mensajes, la gestión de
errores y el cierre de conexión mediante eventos (`addEventListener()`) y retrollamadas
(`onmessage()`).** Ésa es la respuesta oficial.

---

**Los tres mecanismos de asincronía que el punto pide, por orden de aparición histórica:**

| Mecanismo | Cómo se escribe | Qué problema tiene |
|---|---|---|
| **Retrollamada** | **Se pasa una función que se llamará después** | **Anidarlas produce el «infierno de retrollamadas»** |
| **Promesa** | **`then()`, `catch()`, `finally()`** | **Encadena en lugar de anidar** |
| **`async` / `await`** | **Escribe lo asíncrono como si fuera secuencial** | **Es azúcar sobre las promesas** |

**Y lo que decide la pregunta 59 es que los WebSockets no usan promesas**: **su interfaz es de eventos
y retrollamadas.** **Las opciones que meten promesas o excepciones son las falsas**, y **la excepción
`try / catch / finally` no es un mecanismo de notificación asíncrona**: es de manejo de errores
síncronos.

**Qué es un WebSocket, en una línea**: **una conexión permanente y bidireccional entre navegador y
servidor**, frente al modelo de petición y respuesta de HTTP. **Es lo que permite que el servidor
hable primero.**

**La pregunta 20 va de señales de sesión**: **de las afirmaciones sobre un JWT, la correcta es que
consta de tres partes separadas por un punto.** Ésa es la respuesta oficial.

---

**Las tres partes, que es todo lo que hay que saber:**

| Parte | Qué lleva |
|---|---|
| **Cabecera** | **El algoritmo de firma y el tipo** |
| **Cuerpo** | **Las afirmaciones**: quién es el usuario, hasta cuándo vale, qué puede hacer |
| **Firma** | **Lo que impide modificar las dos anteriores sin que se note** |

**Y las tres opciones falsas se desmontan con una idea**: **un JWT no se guarda en el servidor.**

- **La a dice que revocarlo es más fácil que con cookies**: **es al revés, y es su mayor
  inconveniente.** **Como el servidor no guarda estado, un token válido lo sigue siendo hasta que
  caduca**, salvo que se monte una lista de revocación, que es justo lo que el modelo quería evitar.
- **Las c y d lo restringen a un uso concreto** —cliente-servidor o servidor-servidor—, **y sirve para
  los dos.**

**El aviso que conviene añadir**: **el cuerpo de un JWT va codificado, no cifrado.** **Cualquiera
puede leerlo**; lo que la firma impide es cambiarlo. **No se meten datos sensibles en un token.**

## 5. Los marcos de trabajo del cliente

**La pregunta 73**: **el marco de trabajo de JavaScript basado en componentes conocido por su eficacia
en la creación de aplicaciones de página única es Angular.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas se descartan sin conocer ninguno de los cuatro**, sólo por su lenguaje:

| Opción | Qué es |
|---|---|
| **Laravel** | **Marco de PHP**, de servidor |
| **Spring** | **Marco de Java**, de servidor |
| **Angular** | **Marco de JavaScript de cliente, basado en componentes** ✔ |
| **jQuery** | **Biblioteca de JavaScript, no un marco**, y no está basada en componentes |

**El distractor bueno es jQuery**, porque **sí es de JavaScript y sí es de cliente.** **Lo que lo
descarta son las dos condiciones que la pregunta añade**: **basado en componentes** —jQuery manipula
el árbol del documento directamente— **y aplicaciones de página única**, que no es lo suyo.

**Qué es una aplicación de página única**: **una en la que el navegador carga una sola página y a
partir de ahí sustituye trozos sin volver a pedir el documento entero.** **La navegación la gestiona
el propio JavaScript**, y el servidor sólo envía datos.

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 4 | Pseudoclase de CSS que selecciona los elementos pares | c) `:nth-child(2n)` ✔ |
| 20 | Afirmación correcta sobre un JWT | b) Consta de tres partes separadas por un punto ✔ |
| 40 | Elemento de HTML5 para reproducir audio sin complementos | b) La etiqueta `audio` ✔ |
| 46 | Lenguaje que se ejecuta únicamente en el servidor | b) PHP ✔ |
| 50 | Propiedad CSS de alineación horizontal del texto | b) `text-align` ✔ |
| 59 | Lógica que usan los WebSockets para notificar | d) Eventos y retrollamadas ✔ |
| 66 | Objeto global de JavaScript en un documento HTML | a) `window` ✔ |
| 73 | Marco de JavaScript por componentes para aplicaciones de página única | c) Angular ✔ |

**Las ocho respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **tres de las ocho son memoria de sintaxis** —la pseudoclase, la propiedad y
la etiqueta— **y las otras cinco se razonan.** **La tabla de qué se ejecuta en cada lado contesta una
pregunta entera y ayuda en la de los marcos de trabajo.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las especificaciones de HTML, CSS, ECMAScript y WebSockets no se han consultado.** **Los nombres
   de propiedad, pseudoclase y etiqueta que el tema da son de uso universal**, y **coinciden con las
   respuestas oficiales.**
2. **La estructura de tres partes de un JWT y la advertencia de que su cuerpo va codificado y no
   cifrado son de uso corriente.** **El documento que define el formato no se ha consultado**, y **la
   respuesta oficial sólo pide el número de partes.**
3. **Angular, jQuery, Laravel, Spring, nodeJS, PHP y VBScript son nombres de producto o de lenguaje**,
   citados por su categoría. **No se ha consultado la documentación de ninguno**, y **de Angular el
   temario afirma sólo lo que la respuesta oficial afirma.**
4. **La clasificación de mecanismos de asincronía del epígrafe 4 y su orden histórico son
   conocimiento común de la materia**, y **lo que la pregunta 59 mide es cuál de ellos usa la interfaz
   de WebSocket**, que queda razonado.

**El resto del tema va como oficio y así se declara**: la consecuencia de seguridad de validar en el
cliente, la lectura de la fórmula `an+b`, la tabla de propiedades de alineación que se confunden, la
diferencia entre HTML y XHTML, la distinción entre `window` y `document`, el desmontaje de las
opciones falsas del JWT y el argumento que descarta jQuery. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
