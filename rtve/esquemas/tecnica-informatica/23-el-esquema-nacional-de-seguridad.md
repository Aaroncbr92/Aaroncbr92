# Esquema · Tema 23 del específico de Técnica Informática · El Esquema Nacional de Seguridad

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = norma del Boletín Oficial del Estado ·
`[of]` = oficio · `[exam]` = opciones del propio cuadernillo. **Siglas**: el Esquema Nacional de
Seguridad (**ENS**), que la propia norma abrevia así; el Centro Criptológico Nacional (**CCN**) y sus
guías (**CCN-STIC**); la declaración de aplicabilidad (**DA**); y las cinco dimensiones, que la norma
identifica por su inicial en mayúscula: confidencialidad (**C**), integridad (**I**), trazabilidad
(**T**), autenticidad (**A**) y disponibilidad (**D**).

**Cabecera.** Enunciado: punto 26 del anexo · **1 pregunta** · **no lleva figura** · **su respuesta
está literalmente en el anexo I de la norma**, que es la clase de punto que este proyecto prefiere:
**lo que se estudia se puede comprobar.** · **La norma es de 3 de mayo de 2022 y la fecha de corte es
el 21 de diciembre de 2022**: estaba en vigor.

<!-- indice -->

## Índice

- [Qué es y de dónde viene](#qué-es-y-de-dónde-viene)
- [Las cinco dimensiones](#las-cinco-dimensiones)
- [Niveles y categorías](#niveles-y-categorías)
- [Lo que el punto pide y no ha caído](#lo-que-el-punto-pide-y-no-ha-caído)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es y de dónde viene

- `[BOE]` · **Artículo 1.1**: **el real decreto regula el Esquema Nacional de Seguridad**,
  **«establecido en el artículo 156.2 de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del
  Sector Público».**
- `[BOE]` · **Artículo 1.2**: **está constituido por «los principios básicos y requisitos mínimos
  necesarios para una protección adecuada de la información tratada y los servicios prestados»**, con
  el objeto de asegurar **«el acceso, la confidencialidad, la integridad, la trazabilidad, la
  autenticidad, la disponibilidad y la conservación»** de los datos, la información y los servicios.
- **LA PRIMERA CONSECUENCIA**: **el Esquema no es una recomendación: es un real decreto**, y su
  cumplimiento es obligatorio para las entidades de su ámbito, **que incluye al sector público
  institucional y, por tanto, a la Corporación.**
- **LA SEGUNDA, Y ES LA QUE MÁS CONFUNDE**: **esa enumeración del apartado 2 tiene SIETE palabras, no
  cinco.** **Las cinco dimensiones son las que sirven para categorizar un sistema**; **el acceso y la
  conservación aparecen ahí como fines, no como dimensiones.** **No son la misma lista.**

## Las cinco dimensiones

- **PREGUNTA 91** · `[exam]` · **Son disponibilidad, integridad, confidencialidad, trazabilidad y
  autenticidad.**
- `[BOE]` · **Anexo I, apartado 2**: **las dimensiones «se identificarán por sus correspondientes
  iniciales en mayúsculas»**: **a) Confidencialidad [C] · b) Integridad [I] · c) Trazabilidad [T] ·
  d) Autenticidad [A] · e) Disponibilidad [D].**
- **EL ENUNCIADO DA CUATRO Y PIDE LA QUINTA**: **la que falta es la autenticidad.** **Las tres falsas
  —autoridad, legitimidad y responsabilidad— no figuran en la lista.**

| Dimensión | Qué asegura |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Trazabilidad** | **Que se pueda saber quién hizo qué y cuándo** |
| **Autenticidad** | **Que una entidad sea quien dice ser, o que se garantice el origen de los datos** ✔ |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

- **LA RELACIÓN CON LAS TRES CLÁSICAS DEL TEMA 20**: **la familia ISO 27000 habla de
  confidencialidad, integridad y disponibilidad.** **El Esquema añade dos: trazabilidad y
  autenticidad.** **Ésa es la diferencia que el examen puede pedir**, y la razón de que la respuesta
  no sea ninguna de las tres primeras.

## Niveles y categorías

- **SON DOS ESCALAS DISTINTAS Y SE CONFUNDEN.** **La primera mide cada dimensión por separado y tiene
  tres peldaños —bajo, medio y alto—; la segunda mide el sistema entero y tiene otros tres —básica,
  media y alta—.** **El anexo I escribe unos y otras en mayúsculas.**

| Escala | A qué se aplica | Valores |
|---|---|---|
| **Nivel de seguridad** | **A cada dimensión, por separado** | **BAJO, MEDIO o ALTO**, o ninguno si no se ve afectada |
| **Categoría del sistema** | **Al sistema entero** | **BÁSICA, MEDIA o ALTA** |

| Categoría | Cuándo |
|---|---|
| **ALTA** | **Si alguna dimensión alcanza nivel ALTO** |
| **MEDIA** | **Si alguna alcanza nivel MEDIO y ninguna alcanza uno superior** |
| **BÁSICA** | **Si alguna alcanza nivel BAJO y ninguna alcanza uno superior** |

- **LA REGLA EN UNA LÍNEA**: **la categoría la fija la dimensión más exigente**, y **basta una para
  arrastrar al sistema entero.**

| Categoría | Cómo se acredita la conformidad |
|---|---|
| **BÁSICA** | **Autoevaluación**, sin perjuicio de someterse voluntariamente a auditoría |
| **MEDIA y ALTA** | **Auditoría de certificación** |

- **EL AVISO**: **la categoría se reevalúa anualmente**, o **siempre que haya modificaciones
  significativas en los criterios de determinación.** **No es una etiqueta que se pone una vez.**

## Lo que el punto pide y no ha caído

| Asunto | Qué es |
|---|---|
| **Principios básicos** | **Seguridad como proceso integral, gestión basada en los riesgos, prevención, detección y respuesta, y líneas de defensa** |
| **Requisitos mínimos** | **Política de seguridad, personal, control de accesos, instalaciones, adquisición de productos, seguridad por defecto, integridad y actualización, protección de la información, registro de actividad, incidentes, continuidad y mejora continua** |
| **Medidas de seguridad** | **El catálogo del anexo II**: marco organizativo, marco operacional y medidas de protección, **según la categoría** |
| **Declaración de aplicabilidad** | **El documento que dice qué medidas aplica cada sistema y por qué** |
| **Guías del Centro Criptológico Nacional** | **Desarrollan cómo se implantan las medidas.** **No son la norma: la desarrollan** |

- **LA RELACIÓN CON LOS OTROS DOS TEMAS DEL BLOQUE FINAL**: **el 15 describe una política de
  conservación como buena práctica; el 22 la exige por protección de datos; y éste la exige por
  seguridad de los sistemas públicos.** **Los tres piden lo mismo desde tres sitios distintos.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 91 | Quinta dimensión de la seguridad del Esquema | a) Autenticidad ✔ **·** literal en el anexo I |

**La única oficial es correcta** · **no descansa en la plantilla**: **está en el anexo I de un real
decreto.** · **Aviso de estudio**: **una pregunta caída y una norma entera detrás.** **Lo que rinde es
memorizar las cinco dimensiones y la regla que va de niveles a categorías**: dos tablas. **El catálogo
del anexo II es demasiado extenso para memorizarlo**; basta saber cómo está organizado.
