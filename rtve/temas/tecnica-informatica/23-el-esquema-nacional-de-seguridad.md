# Tema 23 del específico de Técnica Informática · El Esquema Nacional de Seguridad

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 26 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad** |
| **Identificador** | `BOE-A-2022-7191` · BOE núm. 106, de 04/05/2022 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan literalmente **los apartados 1 y 2 del artículo 1** y **el apartado 2 del anexo I** |
| **Aviso de encaje** | **La norma es de 3 de mayo de 2022 y la fecha de corte es el 21 de diciembre de 2022**: estaba plenamente vigente |
| **Dos listas que se confunden** | **La enumeración del artículo 1.2 tiene siete palabras y las dimensiones del anexo I son cinco.** El acceso y la conservación son fines, no dimensiones |
| **Extensión** | **1.718 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el Esquema Nacional de Seguridad (**ENS**), que la
propia norma abrevia así; el Centro Criptológico Nacional (**CCN**) y sus guías (**CCN-STIC**); la
declaración de aplicabilidad (**DA**); y las cinco dimensiones de la seguridad, que la norma identifica
por su inicial en mayúscula: confidencialidad (**C**), integridad (**I**), trazabilidad (**T**),
autenticidad (**A**) y disponibilidad (**D**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 26):
> «Esquema Nacional de Seguridad (Real Decreto 311/2022, de 3 de mayo. BOE núm. 106, de
> 04/05/2022).»

**Una pregunta.** **Y su respuesta está literalmente en el anexo I de la norma**, que es la clase de
punto que este proyecto prefiere: **lo que se estudia se puede comprobar.**

**Un aviso de encaje**: **el enunciado cita el Real Decreto 311/2022, de 3 de mayo**, y **la fecha de
corte de este temario es el 21 de diciembre de 2022**, posterior. **La norma estaba en vigor a esa
fecha y es la que se estudia.**

<!-- indice -->

## Índice

- [1. Qué es y de dónde viene](#1-qué-es-y-de-dónde-viene)
- [2. Las cinco dimensiones de la seguridad](#2-las-cinco-dimensiones-de-la-seguridad)
- [3. Los niveles y las categorías](#3-los-niveles-y-las-categorías)
- [4. Lo que el punto pide y el examen no ha preguntado](#4-lo-que-el-punto-pide-y-el-examen-no-ha-preguntado)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué es y de dónde viene

**Artículo 1**, apartados 1 y 2:

> «**1. Este real decreto tiene por objeto regular el Esquema Nacional de Seguridad (en adelante,
> ENS), establecido en el artículo 156.2 de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del
> Sector Público.**
>
> **2. El ENS está constituido por los principios básicos y requisitos mínimos necesarios para una
> protección adecuada de la información tratada y los servicios prestados por las entidades de su
> ámbito de aplicación, con objeto de asegurar el acceso, la confidencialidad, la integridad, la
> trazabilidad, la autenticidad, la disponibilidad y la conservación de los datos, la información y
> los servicios utilizados por medios electrónicos que gestionen en el ejercicio de sus
> competencias.**»
>
> — Real Decreto 311/2022 (`BOE-A-2022-7191`), redacción vigente el 21 de diciembre de 2022

---

**Dos cosas de esa cita deciden cómo se estudia el punto.** **La primera**: **el Esquema no es una
recomendación**: **es un real decreto, y su cumplimiento es obligatorio** para las entidades de su
ámbito, **que incluye al sector público institucional y, por tanto, a la Corporación.**

**La segunda**: **el apartado 2 enumera lo que hay que asegurar** y **esa enumeración incluye siete
palabras**, no cinco. **Las cinco dimensiones del epígrafe siguiente son las que sirven para
categorizar un sistema**; **el acceso y la conservación aparecen aquí como fines, no como
dimensiones.** **Conviene no confundir las dos listas.**

## 2. Las cinco dimensiones de la seguridad

**La pregunta 91**: **las dimensiones de la seguridad que contempla el Esquema Nacional de Seguridad
son disponibilidad, integridad, confidencialidad, trazabilidad y autenticidad.** Ésa es la respuesta
oficial.

---

**Y está literalmente en el anexo I de la norma, en su apartado 2:**

> «2. Dimensiones de la seguridad
>
> A fin de determinar el impacto que tendría sobre la organización un incidente que afectara a la
> seguridad de la información tratada o de los servicios prestados y, en su consecuencia, establecer
> la categoría de seguridad del sistema de información en cuestión, se tendrán en cuenta las
> siguientes dimensiones de la seguridad, que se identificarán por sus correspondientes iniciales en
> mayúsculas:
>
> a) Confidencialidad [C].
> b) Integridad [I].
> c) Trazabilidad [T].
> d) Autenticidad [A].
> e) Disponibilidad [D].»
>
> — Real Decreto 311/2022, anexo I, apartado 2 (`BOE-A-2022-7191`), redacción vigente el 21 de
> diciembre de 2022

---

**El enunciado de la pregunta da cuatro y pide la quinta**, y **la que falta es la autenticidad.**
**Las tres opciones falsas —autoridad, legitimidad y responsabilidad— no figuran en la lista.**

**Qué significa cada una, porque las dos últimas se confunden:**

| Dimensión | Qué asegura |
|---|---|
| **Confidencialidad** | **Que sólo acceda quien está autorizado** |
| **Integridad** | **Que no se altere sin autorización** |
| **Trazabilidad** | **Que se pueda saber quién hizo qué y cuándo** |
| **Autenticidad** | **Que una entidad sea quien dice ser, o que se garantice el origen de los datos** ✔ |
| **Disponibilidad** | **Que esté accesible cuando se necesita** |

**Y la relación con las tres clásicas del tema 20**: **la familia ISO 27000 habla de confidencialidad,
integridad y disponibilidad.** **El Esquema añade dos: trazabilidad y autenticidad.** **Ésa es la
diferencia que el examen puede pedir**, y es la razón por la que la respuesta no es ninguna de las
tres primeras.

## 3. Los niveles y las categorías

**Son dos escalas distintas y se confunden**, así que conviene separarlas. **La primera mide cada
dimensión por separado y tiene tres peldaños —bajo, medio y alto—; la segunda mide el sistema entero
y tiene otros tres —básica, media y alta—.** **El anexo I escribe unos y otras en mayúsculas**, y así se
reproducen en los cuadros que siguen:

| Escala | A qué se aplica | Valores |
|---|---|---|
| **Nivel de seguridad** | **A cada dimensión, por separado** | **BAJO, MEDIO o ALTO**, o ninguno si la dimensión no se ve afectada |
| **Categoría del sistema** | **Al sistema entero** | **BÁSICA, MEDIA o ALTA** |

**Y la regla que va de una a otra, que es lo más preguntable del punto:**

| Categoría | Cuándo |
|---|---|
| **ALTA** | **Si alguna dimensión alcanza nivel ALTO** |
| **MEDIA** | **Si alguna alcanza nivel MEDIO y ninguna alcanza uno superior** |
| **BÁSICA** | **Si alguna alcanza nivel BAJO y ninguna alcanza uno superior** |

**La categoría la fija la dimensión más exigente**, y **basta una para arrastrar al sistema entero.**

**Y la consecuencia práctica que la norma anuda a la categoría:**

| Categoría | Cómo se acredita la conformidad |
|---|---|
| **BÁSICA** | **Autoevaluación**, sin perjuicio de someterse voluntariamente a auditoría |
| **MEDIA y ALTA** | **Auditoría de certificación** |

**El aviso que conviene llevar**: **la categoría se reevalúa anualmente**, o **siempre que haya
modificaciones significativas en los criterios de determinación.** **No es una etiqueta que se pone una
vez.**

## 4. Lo que el punto pide y el examen no ha preguntado

**El enunciado nombra la norma entera y ha caído una pregunta.** **Lo que un técnico informático debe
llevar visto:**

| Asunto | Qué es |
|---|---|
| **Principios básicos** | **La seguridad como proceso integral, la gestión de la seguridad basada en los riesgos, la prevención, detección y respuesta, y la existencia de líneas de defensa** |
| **Requisitos mínimos** | **La lista de exigencias que todo sistema debe cumplir**: política de seguridad, gestión de personal, autorización y control de accesos, protección de las instalaciones, adquisición de productos, seguridad por defecto, integridad y actualización, protección de la información almacenada y en tránsito, registro de actividad, incidentes de seguridad, continuidad y mejora continua |
| **Medidas de seguridad** | **El catálogo del anexo II**, agrupado en marco organizativo, marco operacional y medidas de protección, **y aplicable según la categoría** |
| **Declaración de aplicabilidad** | **El documento que dice qué medidas aplica cada sistema y por qué** |
| **Guías del Centro Criptológico Nacional** | **La serie de guías que desarrolla cómo se implantan las medidas.** **No son la norma: la desarrollan** |

**Y la relación con los otros dos temas de este bloque final**, que es lo que ordena la ocupación:
**el tema 15 describe una política de conservación como buena práctica**; **el 22 la exige por
protección de datos**; **y este la exige por seguridad de los sistemas públicos.** **Los tres piden lo
mismo desde tres sitios distintos.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 91 | Quinta dimensión de la seguridad del Esquema Nacional de Seguridad | a) Autenticidad ✔ **·** literal en el anexo I |

**La única respuesta oficial es correcta**, y **no descansa en la plantilla**: **está en el anexo I de
un real decreto, citado en este tema.**

**El aviso de estudio**: **una pregunta caída y una norma entera detrás.** **Lo que rinde es memorizar
las cinco dimensiones y la regla que va de niveles a categorías**, que es lo más preguntable y cabe en
dos tablas. **El catálogo de medidas del anexo II es demasiado extenso para memorizarlo y conviene
sólo saber cómo está organizado.**

## 6. Trazabilidad

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad** (`BOE-A-2022-7191`), **en su redacción vigente el 21 de diciembre de 2022** | **Los apartados 1 y 2 del artículo 1** y **el apartado 2 del anexo I**, citados literalmente. **Los apartados 1 y 3 del anexo I y el régimen de conformidad se resumen sin cita** |

**Cuatro declaraciones expresas:**

1. **La norma se publicó el 4 de mayo de 2022 y la fecha de corte de este temario es el 21 de
   diciembre de 2022**, de modo que **estaba plenamente vigente.** **Se ha volcado a esa fecha con la
   herramienta de este proyecto**, y **su disposición adicional segunda tiene dos redacciones, que se
   han leído enteras**: ninguna afecta a lo citado.
2. **La distinción entre las siete palabras del artículo 1.2 y las cinco dimensiones del anexo I es
   una observación del temario**, y **está sostenida por las dos citas literales.**
3. **La regla que va de niveles a categorías y el régimen de conformidad se resumen del apartado 3
   del anexo I y del artículo de conformidad**, **sin cita literal**, y **así se dice.** **Ninguna
   respuesta oficial depende de ellos.**
4. **Las guías del Centro Criptológico Nacional no se han consultado.** **El tema sólo afirma de
   ellas que desarrollan la implantación de las medidas**, que es su función declarada.

**El resto del tema va como oficio y así se declara**: la comparación con las tres propiedades de la
familia ISO 27000 del tema 20 y la observación de que los temas 15, 22 y 23 piden lo mismo desde tres
sitios distintos. **Nada de eso está en un boletín oficial más allá de lo citado**, y el tema no lo
presenta como si lo estuviera.
