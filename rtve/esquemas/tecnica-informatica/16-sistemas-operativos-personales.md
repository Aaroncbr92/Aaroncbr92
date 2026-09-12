# Esquema · Tema 16 del específico de Técnica Informática · Sistemas operativos personales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de administración de puestos ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: el control de cuentas de usuario (**UAC**); la
convención universal de nomenclatura (**UNC**); el sistema de ficheros de nueva tecnología (**NTFS**);
el sistema de cifrado de ficheros (**EFS**); el módulo de plataforma segura (**TPM**); el acceso
protegido a redes inalámbricas en su tercera versión (**WPA3**); el instalador de Microsoft (**MSI**),
que da nombre a la extensión; el protocolo de control de transmisión (**TCP**); la configuración de
clave unificada de Linux (**LUKS**); y los nombres de orden y de ruta, que van en acentos graves
porque son código.

**Cabecera.** Enunciado: punto 19 del anexo · **6 preguntas** · **ninguna lleva figura** · **las seis
son de Windows**: **de Ubuntu, que el enunciado nombra, no ha caído ninguna.** · **El examen entiende
«sistema operativo personal» como Windows**, y pregunta por sus herramientas de administración
cotidiana.

<!-- indice -->

## Índice

- [Instaladores](#instaladores)
- [Órdenes de red](#órdenes-de-red)
- [Cifrado del disco](#cifrado-del-disco)
- [Control de cuentas de usuario](#control-de-cuentas-de-usuario)
- [Dependencias de un servicio](#dependencias-de-un-servicio)
- [Rutas de red](#rutas-de-red)
- [Ubuntu, que no ha caído](#ubuntu-que-no-ha-caído)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Instaladores

- **PREGUNTA 16** · `[exam]` · **La extensión del instalador de una aplicación es `msi`.**
- **LAS TRES FALSAS SON EXTENSIONES DE DOCUMENTO O DE MARCADO** —`xml`, `html`, `doc`—: **ninguna
  ejecutable.** **Sólo una de las cuatro puede instalar algo.**

| Formato | Qué es |
|---|---|
| **`.msi`** | **Paquete del instalador del sistema**: lo procesa Windows, admite instalación desatendida y se despliega por directiva de grupo ✔ |
| **`.exe`** | **Un programa que instala**: cada fabricante lo hace a su manera |
| **`.msix` y `.appx`** | **Los formatos modernos de aplicación empaquetada** |

- **POR QUÉ IMPORTA AL ADMINISTRADOR**: **un `.msi` se instala y desinstala igual en cientos de
  equipos; un `.exe` hay que estudiarlo caso por caso.**

## Órdenes de red

- **PREGUNTA 34** · `[exam]` · **Las conexiones TCP activas se ven con `netstat`.**

| Orden | Qué hace |
|---|---|
| **`netstat`** | **Enumera las conexiones abiertas del propio equipo** ✔ |
| **`tracert`** | **Enumera los saltos hasta un destino y dice en cuál se pierde** |
| **`services.msc`** | **Abre la consola de servicios**: no es de red |
| **`conexionList`** | **No existe** |

- **EL ATAJO**: **`netstat` es *network statistics*; `tracert` es *trace route*.**

## Cifrado del disco

- **PREGUNTA 37** · `[exam]` · **La tecnología de Windows 7 contra la extracción física del disco es
  BitLocker Drive Encryption.**

| Opción | Qué es realmente |
|---|---|
| **BitLocker** | **Cifra el volumen entero, sistema incluido.** **Si sacan el disco y lo pinchan en otro equipo, no se lee** ✔ |
| **TPM** | **Un chip que guarda claves y mide la integridad del arranque**: un componente que BitLocker usa, no cifrado de disco |
| **EFS** | **Cifra ficheros y carpetas concretos, por usuario**: no el volumen |
| **WPA3** | **Seguridad de red inalámbrica**: nada que ver con el disco |

- **EL DISTRACTOR BUENO ES EL MÓDULO DE PLATAFORMA SEGURA**, porque **aparece siempre junto al cifrado
  de volumen**: **guarda la clave para que el equipo arranque sin pedirla y detecta si alguien
  manipuló el arranque.** **Pero el chip no cifra: guarda la llave.**
- **LA DISTINCIÓN QUE HAY QUE LLEVAR**: **cifrado de volumen frente a cifrado de fichero.** **El
  primero protege del robo del soporte; el segundo, del vecino de escritorio.** **Son
  complementarios.**

## Control de cuentas de usuario

- **PREGUNTA 58** · `[exam]` · **Notifica y pide confirmación cuando se van a hacer cambios que
  requieren privilegios administrativos.**

| Opción falsa | Qué mecanismo es |
|---|---|
| **Aplicar directivas de grupo** | **El motor de directivas de grupo** |
| **Comprobar si una contraseña caducó** | **La política de contraseñas del dominio** |
| **Comprobar permisos de ficheros al acceder** | **El control de acceso del sistema de ficheros** |

- **LO QUE RESUELVE DE VERDAD**: **un administrador trabaja con una ficha de permisos reducida hasta
  que hace falta elevarla.** **Así un programa lanzado por error no hereda privilegios sin que nadie
  lo vea.** **La ventana no es un trámite: es el punto donde el usuario decide elevar.**

## Dependencias de un servicio

- **PREGUNTA 93** · `[exam]` · **Consola de administración de equipos y servicios → buscar el servicio
  → botón derecho, propiedades → pestaña de dependencias.**

| Opción falsa | Por qué lo es |
|---|---|
| **Una columna de dependencias en la consola** | **No existe**: hay nombre, descripción, estado, tipo de inicio y cuenta |
| **Inicio → sistema → servicios** | **Esa ruta no existe** |
| **`get-service` desde la consola avanzada** | **Lista servicios y estado**: las dependencias no salen en su listado básico |

- **POR QUÉ IMPORTA**: **un servicio puede necesitar que otro esté en marcha para arrancar.** **Cuando
  uno no arranca, lo primero es su pestaña de dependencias**: **el que falla suele ser el de abajo, no
  el que da el error.**

## Rutas de red

- **PREGUNTA 95** · `[exam]` · **La ruta que NO es correcta es `\\SRV7\C:\Repositorio\Video.mp4`.**

```
\\servidor\recurso\camino\dentro\del\recurso
```

- **EL SEGUNDO ELEMENTO ES EL NOMBRE DEL RECURSO COMPARTIDO, NO UNA UNIDAD LOCAL.** **Los dos puntos
  de `C:` no caben ahí**: **es la letra de unidad vista desde el propio equipo**, y **la ruta de red
  se escribe desde fuera.**

| Ruta correcta | Por qué vale |
|---|---|
| `\\SRV7\Repositorio\Video.mp4` | **Recurso compartido corriente** |
| `\\SRV7\C$\Repositorio\Video.mp4` | **`C$` es el recurso administrativo oculto** que el sistema crea por unidad; **el dólar lo oculta del listado** |
| `\\192.168.100.7\Repositorio\Video.mp4` | **El servidor se puede nombrar por dirección** |

- **EL BUEN DISTRACTOR ES `C$`**, que **se parece mucho a la incorrecta**: **la diferencia es el
  carácter**: **el dólar es parte del nombre del recurso y los dos puntos no.**

## Ubuntu, que no ha caído

| Tarea | En Windows | En Ubuntu |
|---|---|---|
| **Instalar una aplicación** | **Paquete `.msi` o `.exe`** | **Gestor de paquetes de la distribución** |
| **Elevar privilegios** | **Control de cuentas de usuario** | **`sudo`** |
| **Ver conexiones** | **`netstat`** | **`ss` y `netstat`** |
| **Gestionar servicios** | **Consola de servicios** | **`systemctl`** |
| **Cifrar el disco** | **BitLocker** | **LUKS** |
| **Compartir ficheros con Windows** | **Recurso compartido nativo** | **Samba** |

- **LAS VERSIONES DE SOPORTE EXTENDIDO SALEN CADA DOS AÑOS, EN ABRIL DE LOS AÑOS PARES**, y **se
  numeran por año y mes**: la de abril de 2024 es la 24.04.

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 16 | Extensión de un instalador | b) `msi` ✔ |
| 34 | Orden de conexiones TCP activas | b) `netstat` ✔ |
| 37 | Tecnología contra la extracción física del disco | a) BitLocker Drive Encryption ✔ |
| 58 | Qué hace el control de cuentas de usuario | c) Notifica y pide confirmación al elevar ✔ |
| 93 | Cómo ver las dependencias de un servicio | c) Propiedades, pestaña de dependencias ✔ |
| 95 | Ruta de convención universal incorrecta | c) `\\SRV7\C:\Repositorio\Video.mp4` ✔ |

**Las seis oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**las seis se contestan habiendo administrado un Windows.** **Es punto de oficio, no de teoría**, y el
que menos rinde de memoria. **Lo que sí conviene fijar es la distinción entre cifrado de volumen y de
fichero, y la forma de una ruta de red.**
