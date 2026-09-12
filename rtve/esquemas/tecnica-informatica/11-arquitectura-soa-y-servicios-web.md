# Esquema · Tema 11 del específico de Técnica Informática · Arquitectura orientada a servicios y servicios web

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de integración · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la arquitectura orientada a servicios (**SOA**); el
protocolo simple de acceso a objetos (**SOAP**); el lenguaje de descripción de servicios web
(**WSDL**); la transferencia de estado representacional (**REST**); el esquema de XML (**XSD**); el
lenguaje de marcado extensible (**XML**) y la notación de objetos de JavaScript (**JSON**), los dos
del tema 10; el protocolo de transferencia de hipertexto (**HTTP**), con sus verbos `GET`, `POST`,
`PUT` y `DELETE`; la descripción, descubrimiento e integración universales (**UDDI**); el lenguaje de
marcado inalámbrico (**WML**), que sale como opción falsa; y **WSLD**, que no abrevia nada: son las
letras de **WSDL** cambiadas de orden para servir de distractor.

**Cabecera.** Enunciado: punto 13 del anexo · **3 preguntas** · **ninguna lleva figura** · **dos de
las tres son la misma**: **cómo se llama el lenguaje que describe un servicio web.** **Si un
cuadernillo repite una pregunta, ese dato vale doble.**

<!-- indice -->

## Índice

- [La arquitectura orientada a servicios](#la-arquitectura-orientada-a-servicios)
- [Los servicios web y su contrato](#los-servicios-web-y-su-contrato)
- [SOAP frente a REST](#soap-frente-a-rest)
- [El software intermedio](#el-software-intermedio)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La arquitectura orientada a servicios

- **LA IDEA, EN UNA LÍNEA**: **construir el sistema como un conjunto de servicios independientes que
  se llaman entre sí por la red, con contratos bien definidos.**

| Rasgo | Qué significa |
|---|---|
| **Servicios con contrato** | **Lo que ofrece está descrito y es estable** |
| **Bajo acoplamiento** | **Quien llama no necesita saber cómo está hecho por dentro** |
| **Reutilización** | **El mismo servicio sirve a varias aplicaciones** |
| **Interoperabilidad** | **Da igual en qué lenguaje esté escrito cada parte** |

- **EL CONTRASTE CON LO QUE VINO DESPUÉS** · `[of]` · **los microservicios son la misma idea llevada
  al extremo del tamaño**: **muy pequeños, con su propio despliegue y a menudo con su propia base de
  datos.** **La orientación a servicios clásica se apoyaba en un bus central; los microservicios
  prescinden de él.**

## Los servicios web y su contrato

- **PREGUNTA 51** · `[exam]` · **El lenguaje que describe la interfaz —operaciones, mensajes y tipos
  de datos— de un servicio web SOAP es WSDL.**
- **PREGUNTA 61** · `[exam]` · **El lenguaje de descripción de servicios web es WSDL.**
- **LA SEGUNDA ES MEMORIA DEL ORDEN DE LAS LETRAS**: **las falsas son WSLD —las dos últimas cambiadas
  de sitio—, WML y W3CC.** **El apoyo es traducir**: *web services description language*, **y las
  iniciales salen en ese orden.**

| Pieza | Qué aporta |
|---|---|
| **SOAP** | **El sobre del mensaje**: cómo se empaqueta la llamada y la respuesta, en XML |
| **WSDL** | **El contrato**: qué operaciones hay y qué mensajes reciben y devuelven ✔ |
| **XSD** | **Los tipos de dato** que el contrato usa |
| **UDDI** | **El directorio** donde publicar y buscar servicios. **Apenas se usa** |

- **EL BUEN DISTRACTOR DE LA 51 ES XSD**, porque **sí describe tipos de dato**: **lo que no describe
  son las operaciones ni los mensajes.**
- **Y REST NO ES UN LENGUAJE**: **es un estilo de arquitectura.**

## SOAP frente a REST

| | **SOAP** | **REST** |
|---|---|---|
| **Qué es** | **Un protocolo** | **Un estilo de arquitectura** |
| **Formato** | **XML obligatorio** | **Cualquiera; en la práctica, JSON** |
| **Contrato** | **WSDL, formal y verificable** | **Documentación, o especificación abierta** |
| **Transporte** | **Varios, en la práctica HTTP** | **HTTP, y usa sus verbos** |
| **Estado** | **Puede llevarlo** | **Sin estado por definición** |
| **Dónde se usa hoy** | **Integración entre empresas, banca, administración** | **Interfaces web y móviles** |

| Verbo | Qué hace |
|---|---|
| `GET` | **Consultar**, sin efectos |
| `POST` | **Crear** |
| `PUT` | **Sustituir** por completo |
| `DELETE` | **Borrar** |

- **LA IDEA QUE DA NOMBRE AL ESTILO**: **cada recurso tiene su propia dirección y el verbo dice qué se
  le hace.** **La operación no va en el nombre**, que es lo contrario de SOAP.

## El software intermedio

- **PREGUNTA 53** · `[exam]` · **El software que conecta dos aplicaciones para compartir recursos de
  proceso de datos es el middleware.**

| Opción | Qué es realmente |
|---|---|
| **Firmware** | **El programa grabado en el aparato**, entre el soporte físico y el sistema |
| **Middleware** | **La capa que conecta aplicaciones entre sí** ✔ |
| **Interfaz de usuario** | **La parte con la que habla la persona** |
| **Shareware** | **Un modelo de distribución**, no una categoría técnica |

- **LA REGLA QUE LAS SEPARA**: **tres de las cuatro no dicen dónde está el software, sino qué hace o
  cómo se vende.** **La única que nombra una posición intermedia lo dice en su nombre**: *middle*, en
  medio.
- **EJEMPLOS, PARA FIJARLO**: **un bus de integración, un gestor de colas de mensajes, un servidor de
  aplicaciones, un controlador de acceso a bases de datos.** **Ninguno es la aplicación y ninguno es
  el sistema operativo: todos están en medio.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 51 | Lenguaje que describe la interfaz de un servicio web SOAP | a) WSDL ✔ |
| 53 | Software que conecta dos aplicaciones | b) Middleware ✔ |
| 61 | Lenguaje de descripción de servicios web | a) WSDL ✔ |

**Las tres oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**el cuadernillo repite la misma respuesta en dos preguntas**, lo que **hace de WSDL el dato más
rentable del punto.** **De lo que no ha caído, lo preguntable es la tabla que enfrenta SOAP con
REST.**
