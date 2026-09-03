# Tema 11 del específico de Técnica Informática · Arquitectura orientada a servicios y servicios web

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 13 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la arquitectura orientada a servicios, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Pregunta repetida** | **El cuadernillo pregunta dos veces por el mismo dato**, con otras palabras. Cuando eso ocurre, ese dato vale doble |
| **Extensión** | **1.317 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la arquitectura orientada a servicios (**SOA**,
*service oriented architecture*); el protocolo simple de acceso a objetos (**SOAP**); el lenguaje de
descripción de servicios web (**WSDL**, *web services description language*); la transferencia de
estado representacional (**REST**, *representational state transfer*); el esquema de XML (**XSD**);
el lenguaje de marcado extensible (**XML**) y la notación de objetos de JavaScript (**JSON**), los dos
del tema 10; el protocolo de transferencia de hipertexto (**HTTP**), cuyos cuatro verbos se
nombran por su palabra inglesa (`GET`, `POST`, `PUT` y `DELETE`); la descripción, descubrimiento e
integración universales (**UDDI**); el lenguaje de marcado inalámbrico (**WML**), que aparece como opción
falsa; y **WSLD**, que no abrevia nada: son las letras de **WSDL** cambiadas de orden para servir de
distractor.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 13):
> «Arquitectura SOA. Web Services.»

**Tres preguntas.** **Y dos de ellas son la misma**: **cómo se llama el lenguaje que describe un
servicio web.** **El examen la ha preguntado dos veces, con otras palabras y en el mismo
cuadernillo.**

**Eso conviene decirlo porque es un dato de estudio**: **si un cuadernillo repite una pregunta, ese
dato vale doble.**

<!-- indice -->

## Índice

- [1. Qué es una arquitectura orientada a servicios](#1-qué-es-una-arquitectura-orientada-a-servicios)
- [2. Los servicios web y su descripción](#2-los-servicios-web-y-su-descripción)
- [3. Los dos estilos de servicio web](#3-los-dos-estilos-de-servicio-web)
- [4. El software intermedio](#4-el-software-intermedio)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué es una arquitectura orientada a servicios

**La idea, en una línea**: **construir el sistema como un conjunto de servicios independientes que se
llaman entre sí por la red, con contratos bien definidos.**

**Sus cuatro rasgos, que es lo que el enunciado pide:**

| Rasgo | Qué significa |
|---|---|
| **Servicios con contrato** | **Lo que el servicio ofrece está descrito y es estable** |
| **Bajo acoplamiento** | **Quien llama no necesita saber cómo está hecho el servicio por dentro** |
| **Reutilización** | **El mismo servicio sirve a varias aplicaciones** |
| **Interoperabilidad** | **Da igual en qué lenguaje esté escrito cada parte** |

**Y el contraste con lo que vino después, porque el sector lo maneja a diario**: **los microservicios
son la misma idea llevada al extremo del tamaño**: **servicios muy pequeños, con su propio despliegue
y a menudo con su propia base de datos.** **La arquitectura orientada a servicios clásica solía
apoyarse en un bus de integración central; los microservicios prescinden de él.**

## 2. Los servicios web y su descripción

**La pregunta 51**: **el lenguaje que describe la interfaz —operaciones, mensajes y tipos de datos— de
un servicio web SOAP es WSDL.** Ésa es la respuesta oficial.

**La pregunta 61**: **el lenguaje de descripción de servicios web es WSDL.** Ésa es la respuesta
oficial.

---

**Son la misma pregunta**, y **la segunda es de memoria del orden de las letras**: **las tres opciones
falsas son WSLD —las dos últimas cambiadas de sitio—, WML y W3CC.** **El apoyo para no equivocarse es
traducir**: *web services description language*, **y las iniciales salen en ese orden.**

**Las piezas de un servicio web clásico, que es lo que la pregunta 51 enumera:**

| Pieza | Qué aporta |
|---|---|
| **SOAP** | **El sobre del mensaje**: cómo se empaqueta la llamada y la respuesta, en XML |
| **WSDL** | **El contrato**: qué operaciones hay, qué mensajes reciben y devuelven, con qué tipos ✔ |
| **XSD** | **Los tipos de dato** que el contrato usa |
| **UDDI** | **El directorio** donde publicar y buscar servicios. **Apenas se usa** |

**La opción XSD de la pregunta 51 es el buen distractor**, porque **sí describe tipos de dato**;
**lo que no describe son las operaciones ni los mensajes**, que es lo que la pregunta pide.

**Y la opción REST no es un lenguaje**: **es un estilo de arquitectura.** **Ésa es la distinción del
epígrafe siguiente.**

## 3. Los dos estilos de servicio web

| | **SOAP** | **REST** |
|---|---|---|
| **Qué es** | **Un protocolo** | **Un estilo de arquitectura** |
| **Formato** | **XML obligatorio** | **Cualquiera; en la práctica, JSON** |
| **Contrato** | **WSDL, formal y verificable** | **Documentación, o especificación abierta** |
| **Transporte** | **Varios, aunque en la práctica HTTP** | **HTTP, y usa sus verbos** |
| **Estado** | **Puede llevarlo** | **Sin estado por definición** |
| **Dónde se usa hoy** | **Integración entre empresas, banca, administración** | **Interfaces web y móviles** |

**Los cuatro verbos que REST aprovecha de HTTP, porque es lo preguntable del estilo:**

| Verbo | Qué hace |
|---|---|
| `GET` | **Consultar**, sin efectos |
| `POST` | **Crear** |
| `PUT` | **Sustituir** por completo |
| `DELETE` | **Borrar** |

**Y la idea que da nombre al estilo**: **cada recurso tiene su propia dirección y el verbo dice qué se
le hace.** **La operación no va en el nombre**, que es justo lo contrario de SOAP.

## 4. El software intermedio

**La pregunta 53**: **el software que conecta dos aplicaciones para compartir recursos de proceso de
datos se conoce como middleware.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son tres categorías de software que no son eso:**

| Opción | Qué es realmente |
|---|---|
| **Firmware** | **El programa grabado en el propio aparato**, entre el soporte físico y el sistema |
| **Middleware** | **La capa que conecta aplicaciones entre sí** ✔ |
| **Interfaz de usuario** | **La parte con la que habla la persona** |
| **Shareware** | **Un modelo de distribución**, no una categoría técnica |

**La regla que las separa**: **tres de las cuatro no describen dónde está el software, sino qué hace o
cómo se vende.** **La única que nombra una posición intermedia es la que la pregunta pide, y lo dice
en su propio nombre**: *middle*, **en medio.**

**Ejemplos de software intermedio, para fijar el concepto**: **un bus de integración, un gestor de
colas de mensajes, un servidor de aplicaciones o un controlador de acceso a bases de datos.**
**Ninguno es la aplicación y ninguno es el sistema operativo: todos están en medio.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 51 | Lenguaje que describe la interfaz de un servicio web SOAP | a) WSDL ✔ |
| 53 | Software que conecta dos aplicaciones | b) Middleware ✔ |
| 61 | Lenguaje de descripción de servicios web | a) WSDL ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **el cuadernillo repite la misma respuesta en dos preguntas**, lo que **hace
de WSDL el dato más rentable del punto.** **Y de lo que no ha caído, lo preguntable es la tabla que
enfrenta SOAP con REST.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Tres declaraciones expresas:**

1. **Las especificaciones de SOAP, WSDL, XSD y UDDI no se han consultado.** **La función de cada una
   es de uso universal**, y **coincide con las respuestas oficiales.**
2. **La forma larga de WSDL se toma del propio enunciado de la pregunta 61**, que la pide, y **la
   descripción de lo que el lenguaje contiene —operaciones, mensajes y tipos de datos— procede
   literalmente del enunciado de la pregunta 51.**
3. **La tabla que enfrenta SOAP con REST y la lista de verbos son oficio.** **Ninguna respuesta
   depende de ellas**, y el temario no las atribuye a ninguna fuente.

**El resto del tema va como oficio y así se declara**: los cuatro rasgos de la arquitectura orientada
a servicios, el contraste con los microservicios, el argumento que descarta XSD como respuesta de la
pregunta 51, la observación de que REST no es un lenguaje sino un estilo y la regla que separa el
software intermedio de las otras tres categorías. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
