# Tema 16 del específico de Técnica Informática · Sistemas operativos personales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 19 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los sistemas operativos de puesto, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Desajuste declarado** | **El enunciado nombra Ubuntu y las seis preguntas son de Windows.** El examen entiende «sistema operativo personal» como Windows |
| **Extensión** | **1.922 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el control de cuentas de usuario (**UAC**, *user
account control*); la convención universal de nomenclatura (**UNC**, *universal naming convention*);
el sistema de ficheros de nueva tecnología (**NTFS**); el sistema de cifrado de ficheros (**EFS**,
*encrypting file system*); el módulo de plataforma segura (**TPM**, *trusted platform module*); el
acceso protegido a redes inalámbricas en su tercera versión (**WPA3**); el instalador de Microsoft
(**MSI**), que da nombre a la extensión; el protocolo de control de transmisión (**TCP**); la configuración de clave unificada de Linux
(**LUKS**, *Linux unified key setup*); y los
nombres de orden y de ruta, que van en acentos graves porque son código.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 19):
> «Sistemas operativos personales: Windows 10. Windows 11. Ubuntu.»

**Seis preguntas.** **Y las seis son de Windows**: **de Ubuntu, que el enunciado nombra, no ha caído
ninguna.**

**Eso conviene decirlo de entrada porque orienta el estudio**: **el examen entiende «sistema operativo
personal» como Windows**, y **lo que ha preguntado son sus herramientas de administración cotidiana.**

<!-- indice -->

## Índice

- [1. Las extensiones y los instaladores](#1-las-extensiones-y-los-instaladores)
- [2. Las órdenes de red](#2-las-órdenes-de-red)
- [3. El cifrado del disco](#3-el-cifrado-del-disco)
- [4. El control de cuentas de usuario](#4-el-control-de-cuentas-de-usuario)
- [5. Los servicios y sus dependencias](#5-los-servicios-y-sus-dependencias)
- [6. Las rutas de red](#6-las-rutas-de-red)
- [7. Ubuntu, que el enunciado nombra y el examen no ha preguntado](#7-ubuntu-que-el-enunciado-nombra-y-el-examen-no-ha-preguntado)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Las extensiones y los instaladores

**La pregunta 16**: **en los sistemas Microsoft Windows, la extensión asociada a un archivo que
contiene un instalador de una aplicación es `msi`.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son extensiones de documento o de marcado** —`xml`, `html`, `doc`—,
**ninguna ejecutable.** **La pregunta se contesta reconociendo que sólo una de las cuatro puede
instalar algo.**

**Los formatos de instalación de Windows, que es lo que hay detrás:**

| Formato | Qué es |
|---|---|
| **`.msi`** | **Paquete del instalador del sistema.** **Lo procesa el propio Windows**, admite instalación desatendida y se puede desplegar por directiva de grupo ✔ |
| **`.exe`** | **Un programa que instala.** **Cada fabricante lo hace a su manera** |
| **`.msix` y `.appx`** | **Los formatos modernos de aplicación empaquetada** |

**Por qué la distinción importa al administrador**: **un `.msi` se puede instalar y desinstalar de
forma uniforme en cientos de equipos**; **un `.exe` hay que estudiarlo caso por caso.** **Ésa es la
razón de que el despliegue corporativo prefiera el primero.**

## 2. Las órdenes de red

**La pregunta 34**: **en Windows 11, la orden que muestra las conexiones TCP activas es `netstat`.**
Ésa es la respuesta oficial.

---

**Y las cuatro herramientas de la pregunta, con su cometido**, que **es el mismo cuadro que el tema 12
del específico de Técnica de Equipos y Sistemas Electrónicos:**

| Orden | Qué hace |
|---|---|
| **`netstat`** | **Enumera las conexiones abiertas del propio equipo** ✔ |
| **`tracert`** | **Enumera los saltos hasta un destino y dice en cuál se pierde** |
| **`services.msc`** | **Abre la consola de servicios**: no es de red |
| **`conexionList`** | **No existe** |

**El atajo de memoria**: **`netstat` es *network statistics*, estadísticas de red.** **`tracert` es
*trace route*, trazar la ruta.**

## 3. El cifrado del disco

**La pregunta 37**: **la tecnología que se implementó en Windows 7 para prevenir el robo de
información mediante la extracción física del disco es BitLocker Drive Encryption.** Ésa es la
respuesta oficial.

---

**Y las tres opciones falsas son tres tecnologías reales de seguridad que hacen otra cosa**, lo que
convierte la pregunta en un buen ejercicio de distinguir:

| Opción | Qué es realmente |
|---|---|
| **BitLocker** | **Cifra el volumen entero, incluido el sistema.** **Si sacan el disco y lo pinchan en otro equipo, no se lee** ✔ |
| **TPM** | **Un chip que guarda claves y mide la integridad del arranque.** **Es un componente que BitLocker usa, no una tecnología de cifrado de disco** |
| **EFS** | **Cifra ficheros y carpetas concretos, por usuario.** **No protege el volumen entero** |
| **WPA3** | **Seguridad de red inalámbrica.** **No tiene nada que ver con el disco** |

**El distractor bueno es el módulo de plataforma segura**, porque **aparece siempre junto al cifrado de
volumen**: **es donde se guarda la clave para que el equipo arranque sin pedirla, y a la vez lo que
detecta si alguien ha manipulado el arranque.** **Pero el chip no cifra el disco: guarda la llave.**

**Y la distinción que hay que llevar aprendida**: **cifrado de volumen frente a cifrado de fichero.**
**El primero protege del robo del soporte; el segundo, del vecino de escritorio.** **Son
complementarios y resuelven amenazas distintas.**

## 4. El control de cuentas de usuario

**La pregunta 58**: **el control de cuentas de usuario de Windows notifica y pide confirmación al
usuario cuando se van a realizar cambios que requieren privilegios administrativos.** Ésa es la
respuesta oficial.

---

**Y las tres opciones falsas nombran tres mecanismos distintos del mismo sistema:**

| Opción | Qué mecanismo es |
|---|---|
| **a) Aplicar las directivas de grupo del usuario** | **El motor de directivas de grupo** |
| **b) Comprobar si una contraseña ha caducado** | **La política de contraseñas del dominio** |
| **d) Comprobar los permisos de ficheros al acceder** | **El control de acceso del sistema de ficheros** |

**Lo que el mecanismo resuelve de verdad, y es lo que hay que entender**: **un administrador trabaja
con una ficha de permisos reducida hasta que hace falta elevarla.** **Así, un programa lanzado por
error no hereda privilegios administrativos sin que nadie lo vea.** **La ventana que aparece no es un
trámite: es el punto donde el usuario decide elevar.**

## 5. Los servicios y sus dependencias

**La pregunta 93**: **para ver las dependencias de un servicio en Windows se entra en la consola de
administración de equipos y servicios, se busca el servicio, se abre con el botón derecho la ventana
de propiedades y allí aparece una pestaña de dependencias.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas describen caminos que no existen o que no llevan a las dependencias:**

| Opción | Por qué es falsa |
|---|---|
| **a) Buscar «servicios y dependencias» y ver una columna de dependencias** | **La consola de servicios no tiene columna de dependencias**: tiene nombre, descripción, estado, tipo de inicio y cuenta |
| **b) Inicio → sistema → servicios** | **Esa ruta no existe** |
| **d) `get-service` desde la consola de órdenes avanzada** | **La orden lista servicios y su estado.** **Las dependencias no salen en su listado básico** |

**Qué es una dependencia de servicio y por qué importa**: **un servicio puede necesitar que otro esté
en marcha para arrancar.** **Cuando un servicio no arranca, lo primero que se mira es su pestaña de
dependencias**, porque **el que falla suele ser el de abajo, no el que da el error.**

## 6. Las rutas de red

**La pregunta 95 es negativa**: **de las rutas de convención universal de nomenclatura enumeradas, la
que NO es correcta es `\\SRV7\C:\Repositorio\Video.mp4`.** Ésa es la respuesta oficial.

---

**La forma de una ruta de este tipo es siempre la misma:**

```
\\servidor\recurso\camino\dentro\del\recurso
```

**Y de ahí se resuelve la pregunta**: **el segundo elemento es el nombre del recurso compartido, no
una unidad local.** **Los dos puntos de `C:` no caben ahí**: **es la letra de unidad vista desde el
propio equipo**, y **la ruta de red se escribe desde fuera.**

**Las tres opciones correctas, y por qué lo son:**

| Ruta | Por qué vale |
|---|---|
| `\\SRV7\Repositorio\Video.mp4` | **Recurso compartido corriente** |
| `\\SRV7\C$\Repositorio\Video.mp4` | **`C$` es el recurso administrativo oculto** que el sistema crea para cada unidad. **El dólar lo oculta del listado**, y es válido |
| `\\192.168.100.7\Repositorio\Video.mp4` | **El servidor se puede nombrar por dirección en vez de por nombre** |

**La opción `C$` es el buen distractor**, porque **se parece mucho a la incorrecta.** **La diferencia
es el carácter**: **el dólar es parte del nombre del recurso compartido y los dos puntos no lo son.**

## 7. Ubuntu, que el enunciado nombra y el examen no ha preguntado

**Lo mínimo que conviene llevar visto, con su equivalencia:**

| Tarea | En Windows | En Ubuntu |
|---|---|---|
| **Instalar una aplicación** | **Paquete `.msi` o `.exe`** | **Gestor de paquetes de la distribución** |
| **Elevar privilegios** | **Control de cuentas de usuario** | **`sudo`** |
| **Ver conexiones** | **`netstat`** | **`ss` y `netstat`** |
| **Gestionar servicios** | **Consola de servicios** | **`systemctl`** |
| **Cifrar el disco** | **BitLocker** | **LUKS** |
| **Compartir ficheros con Windows** | **Recurso compartido nativo** | **Samba**, que habla el mismo protocolo |

**Y el rasgo de las versiones de Ubuntu que se pregunta a veces**: **las de soporte extendido salen
cada dos años, en abril de los años pares**, y **se numeran por año y mes**: la de abril de 2024 es la
24.04.

## 8. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 16 | Extensión de un instalador en Windows | b) `msi` ✔ |
| 34 | Orden que muestra las conexiones TCP activas | b) `netstat` ✔ |
| 37 | Tecnología de Windows 7 contra la extracción física del disco | a) BitLocker Drive Encryption ✔ |
| 58 | Qué hace el control de cuentas de usuario | c) Notifica y pide confirmación al elevar privilegios ✔ |
| 93 | Cómo ver las dependencias de un servicio | c) Propiedades del servicio, pestaña de dependencias ✔ |
| 95 | Ruta de convención universal que NO es correcta | c) `\\SRV7\C:\Repositorio\Video.mp4` ✔ |

**Las seis respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **las seis se contestan habiendo administrado un Windows.** **Es un punto de
oficio, no de teoría**, y **el que menos rinde estudiando de memoria.** **Lo que sí conviene fijar es
la distinción entre cifrado de volumen y de fichero, y la forma de una ruta de red.**

## 9. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La documentación de Microsoft y la de Ubuntu no se han consultado.** **Lo que el tema afirma del
   instalador, de las órdenes, del cifrado de volumen, del control de cuentas y de las rutas de red es
   de uso corriente en la administración de esos sistemas**, y **coincide con las respuestas
   oficiales.**
2. **BitLocker, EFS, el módulo de plataforma segura, WPA3, Samba y LUKS son nombres de producto o de
   tecnología**, citados por su función. **El temario no les atribuye ninguna característica más allá
   de la que la respuesta oficial exige.**
3. **La afirmación de que la consola de servicios no tiene columna de dependencias sostiene el
   descarte de la opción a de la pregunta 93**, y **es comprobable abriendo esa consola.** **No
   procede de ninguna documentación consultada.**
4. **La cadencia de las versiones de soporte extendido de Ubuntu del epígrafe 7 es de uso
   corriente**, y **ninguna pregunta depende de ella.**

**El resto del tema va como oficio y así se declara**: la razón de que el despliegue corporativo
prefiera un formato de instalación sobre otro, los atajos de memoria de las órdenes, la distinción
entre cifrado de volumen y de fichero, la explicación de para qué sirve de verdad la elevación de
privilegios, el consejo de mirar las dependencias cuando un servicio no arranca y la tabla de
equivalencias con Ubuntu. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
