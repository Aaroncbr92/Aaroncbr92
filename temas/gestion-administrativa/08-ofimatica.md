# Tema 8 del específico de Gestión Administrativa · Ofimática y proceso de la información

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 8 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | **Ninguna**: es el único de los cinco puntos de informática que no cita ningún producto, y la terminología técnica no es contenido de una norma |
| **Identificador** | — |
| **Redacción que se estudia** | No procede |
| **Aviso sobre las fuentes** | **Dos preguntas, las dos de la última línea del enunciado**: seguridad informática. Las cinco primeras líneas —hardware, software, almacenamiento, sistemas operativos y dispositivos— **no han caído ni una vez**, y ocupan la mayor parte del tema por la regla del apartado 7 del manual |
| **Extensión** | **1.721 palabras** |

<!-- /portada -->

**Las siglas de este tema, presentadas de entrada**: unidad central de proceso (**CPU**), memoria de
acceso aleatorio (**RAM**), memoria de sólo lectura (**ROM**), unidad de estado sólido (**SSD**),
unidad de disco duro (**HDD**), sistema operativo (**SO**), entrada y salida (**E/S**), red de área
local (**LAN**), copia de seguridad (*backup*), la Agencia Española de Protección de Datos (**AEPD**),
el sistema de archivos de nueva tecnología (**NTFS**), la tabla de asignación de archivos (**FAT**,
de donde salen **FAT32** y **exFAT**), el sistema de archivos de Apple (**APFS**), el disco compacto
(**CD**), el disco versátil digital (**DVD**) y el servicio de mensajes cortos (**SMS**).

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 8):**
> «Ofimática y proceso de la información. Conceptos fundamentales sobre el hardware y el software.
> Sistemas de almacenamiento de datos. Sistemas operativos. Dispositivos. Nociones básicas de
> seguridad informática.»

<!-- indice -->

## Índice

- [Antes de empezar: el bloque de producto, y qué se puede afirmar de él](#antes-de-empezar-el-bloque-de-producto-y-qué-se-puede-afirmar-de-él)
- [1. Hardware](#1-hardware)
- [2. Software](#2-software)
- [3. El sistema operativo](#3-el-sistema-operativo)
- [4. Sistemas de almacenamiento](#4-sistemas-de-almacenamiento)
- [5. Nociones de seguridad informática](#5-nociones-de-seguridad-informática)
  - [5.1. Los tres principios](#51-los-tres-principios)
  - [5.2. Las amenazas que el examen nombra](#52-las-amenazas-que-el-examen-nombra)
  - [5.3. La brecha de seguridad](#53-la-brecha-de-seguridad)
  - [5.4. Medidas básicas](#54-medidas-básicas)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
  - [6.1. Una precisión sobre la pregunta 58](#61-una-precisión-sobre-la-pregunta-58)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## Antes de empezar: el bloque de producto, y qué se puede afirmar de él

**Los puntos 8 a 12 son el bloque de informática de esta ocupación**, y tienen una particularidad que
no se había dado antes en el proyecto: **el programa fecha las versiones**. El punto 9 dice «Windows
10 Pro, versión 22H2»; el 11, «Office Profesional Plus 2019»; el 12, «Teams versión 1.6.00.376».

**Eso convierte la documentación del fabricante en la fuente exigible**, que es el **cuarto nivel** de
la jerarquía de este proyecto, por debajo del BOE y de las normas de organismos de normalización.
Está descargada en `fuentes/ofimatica/`, con dos advertencias que valen para los cinco temas y se
dicen una sola vez:

1. **Son las páginas de hoy, no las de 2022.** Microsoft no publica versiones fechadas de su
   documentación de soporte: publica la página viva. Lo que estos temas afirman es lo que **no ha
   cambiado** entre aquella versión y ésta, y donde no se pueda asegurar, se dice.
2. **Este punto, el 8, es el único de los cinco que no cita ningún producto.** Habla de conceptos
   —hardware, software, almacenamiento, sistemas operativos, seguridad— que **no son de ningún
   fabricante**. Aquí no hay documentación que citar: hay terminología técnica común, y se expone
   como tal.

---

## 1. Hardware

**Hardware** es el conjunto de componentes físicos de un sistema informático. Se ordena en cinco
funciones:

| Función | Qué hace | Ejemplos |
|---|---|---|
| **Proceso** | Ejecuta las instrucciones | CPU, con su unidad de control y su unidad aritmético-lógica |
| **Memoria principal** | Guarda datos e instrucciones en uso | RAM (volátil), ROM (no volátil) |
| **Almacenamiento** | Guarda datos de forma persistente | Disco duro, SSD, memorias flash |
| **Entrada** | Introduce datos | Teclado, ratón, escáner, micrófono |
| **Salida** | Presenta resultados | Monitor, impresora, altavoces |

**La distinción que más se pregunta es memoria frente a almacenamiento.** La **RAM** es rápida y
**volátil**: al apagar el equipo pierde su contenido. El **almacenamiento** es más lento y
**persistente**: conserva los datos sin corriente. Un equipo con poca RAM va lento; un equipo con
poco disco no cabe.

**Y hay dispositivos que son de entrada y de salida a la vez**: la pantalla táctil, el módem, la
tarjeta de red, una unidad de disco.

---

## 2. Software

**Software** es el conjunto de programas, procedimientos y documentación que hacen funcionar el
hardware. Se clasifica en tres capas:

- **Software de sistema**: el sistema operativo, los controladores de dispositivo y las utilidades
  del sistema. Es el que hace utilizable la máquina.
- **Software de programación**: compiladores, intérpretes, entornos de desarrollo.
- **Software de aplicación**: el que resuelve tareas del usuario. **La ofimática es software de
  aplicación**: procesador de textos, hoja de cálculo, presentaciones, correo, base de datos.

**Por su licencia** se distingue el **propietario** —cuyo código no se distribuye y cuyo uso está
sujeto a una licencia— del **libre** —que permite usar, estudiar, modificar y redistribuir—, y el
**freeware** o el **shareware**, que son gratuitos o de prueba pero **no necesariamente libres**.
**Gratis y libre no son sinónimos**, y es la confusión más frecuente de este epígrafe.

---

## 3. El sistema operativo

**Es el programa que administra los recursos del equipo y sirve de intermediario entre el hardware y
las aplicaciones.** Sus funciones son cinco:

1. **Gestión de procesos**: reparte el tiempo de la CPU entre los programas en ejecución.
2. **Gestión de memoria**: asigna y libera memoria, y gestiona la memoria virtual.
3. **Gestión de archivos**: organiza los datos en un sistema de ficheros con carpetas y permisos.
4. **Gestión de dispositivos**: se comunica con el hardware a través de controladores.
5. **Interfaz de usuario**: gráfica o de línea de órdenes.

**Los sistemas de archivos** más habituales en el entorno de escritorio son **NTFS** —el de Windows,
con permisos y registro de transacciones—, **FAT32** y **exFAT** —usados en memorias extraíbles por
compatibilidad— y **ext4** o **APFS** en Linux y macOS.

---

## 4. Sistemas de almacenamiento

**Por la tecnología:**

- **Magnético**: el disco duro clásico, con platos giratorios y cabezales. Barato por unidad de
  capacidad, más lento y con partes móviles.
- **De estado sólido**: memoria flash sin partes móviles. Mucho más rápido, más caro y con un número
  finito de ciclos de escritura.
- **Óptico**: CD, DVD y Blu-ray. Prácticamente retirado del uso ofimático.

**Por la ubicación:**

- **Local**: en el propio equipo.
- **En red**: unidades compartidas, cabinas de almacenamiento.
- **En la nube**: alojado en servidores de un proveedor y accesible por internet.

**La copia de seguridad** es un concepto distinto del almacenamiento, aunque se confundan. Una copia
de seguridad es **una réplica de los datos destinada a recuperarlos si se pierden**, y para valer
tiene que cumplir tres condiciones: estar **separada** del original, ser **periódica** y haberse
**probado la restauración**. Una copia que nunca se ha restaurado no se sabe si sirve.

---

## 5. Nociones de seguridad informática

### 5.1. Los tres principios

Toda la seguridad de la información se ordena en tres propiedades que hay que preservar:

- **Confidencialidad**: que la información sólo sea accesible a quien está autorizado.
- **Integridad**: que no se altere sin autorización.
- **Disponibilidad**: que esté accesible cuando se necesita.

### 5.2. Las amenazas que el examen nombra

| Amenaza | Qué es |
|---|---|
| **Phishing** | Suplantación mediante un **mensaje** —correo, SMS— que induce a entregar credenciales o datos |
| **Pharming** | Suplantación **del destino**: se manipula la resolución de nombres o el equipo para que el usuario, escribiendo la dirección correcta, **acabe en un sitio falsificado** |
| **Troyano** | Programa que se presenta como legítimo y esconde una función dañina |
| **Ransomware** | Programa que **cifra los datos** y pide un rescate para devolverlos |
| **Spyware** | Programa que recoge información del usuario sin su conocimiento |
| **Gusano** | Programa que se replica y se propaga por la red por sí solo |
| **Bulo o *hoax*** | Mensaje falso y llamativo cuya finalidad es difundirse |

**La diferencia entre *phishing* y *pharming* es la que el examen pregunta, y se resume en una
línea**: en el *phishing* **el usuario acude al sitio falso porque le han dado el enlace**; en el
*pharming*, **acude porque el camino está desviado**, aunque él haya escrito bien la dirección. El
segundo es más difícil de detectar precisamente porque la dirección que el usuario ve es la buena.

### 5.3. La brecha de seguridad

**Una brecha de seguridad es un incidente que ocasiona la destrucción, pérdida o alteración
accidental o ilícita de datos, o la comunicación o el acceso no autorizados a ellos.** Es decir:
**no es una copia de seguridad, no es un bulo y no es un programa**: es **un suceso** en el que la
confidencialidad, la integridad o la disponibilidad se han visto comprometidas.

**Y tiene consecuencias jurídicas**, que enlazan con el tema 17 de Producción y el punto 9 de
Gestión: una brecha que afecte a datos personales obliga a **notificarla a la autoridad de control**
y, si el riesgo para los derechos de las personas es alto, **a comunicarla a los afectados**.

### 5.4. Medidas básicas

Contraseñas robustas y distintas por servicio; **doble factor de autenticación**; actualizaciones al
día; copias de seguridad probadas; cifrado de los soportes que salen de la oficina; principio de
**mínimo privilegio** —cada usuario, sólo los permisos que necesita—; y formación, que es la medida
que más rendimiento da contra el *phishing*.

---

## 6. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Dónde se contesta |
|---|---|---|
| 54 | Cómo se llama dirigir al usuario a un sitio falsificado | Epígrafe 5.2 |
| 58 | Qué es una brecha de seguridad | Epígrafe 5.3 |

**Dos preguntas, las dos de seguridad informática**, que es la última línea del enunciado del
programa. **Los conceptos de hardware, software, almacenamiento, sistemas operativos y dispositivos
—las cinco primeras líneas— no han caído ni una vez**, y ocupan la mayor parte de este tema por la
regla del apartado 7 del manual: la laguna se cierra ampliando el tema, nunca recortando la pregunta.

### 6.1. Una precisión sobre la pregunta 58

La opción que la plantilla da por buena describe la brecha como incidente de seguridad. **Las otras
tres describen cosas reales pero distintas**: una copia de seguridad, un bulo y —en la restante— un
programa malicioso. **La pregunta se contesta sabiendo que una brecha es un suceso y no un objeto**,
que es la distinción que el tema deja escrita.

---

## 7. Trazabilidad

**Este punto no tiene fuente que citar y es el único de los cinco de informática en esa situación.**
No nombra ningún producto, así que no hay documentación de fabricante aplicable; y la terminología
—hardware, software, RAM, sistema de archivos, *phishing*, *pharming*— es **vocabulario técnico
común**, no el contenido de una norma ni de un manual concreto.

**Lo que sí tiene norma es un extremo del epígrafe 5.3**: el concepto de brecha y las obligaciones de
notificación, que están en la normativa de protección de datos ya volcada para el tema 17 de
Producción (Asistencia) y para el punto 9 del temario de Gestión. Aquí se remite a ella y no se
duplica.

- **Cuadernillo `23_preguntas_gea`**, preguntas 54 y 58, con su plantilla oficial.
