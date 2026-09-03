# Tema 9 del específico de Gestión Administrativa · El entorno Microsoft Windows 10 Pro, versión 22H2

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 9 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | Documentación de soporte de Microsoft para **Windows 10 Pro, versión 22H2** |
| **Identificador** | `support.microsoft.com/es-es/windows/…dcc61a57` y `learn.microsoft.com/es-es/lifecycle/products/windows-10-home-and-pro` |
| **Redacción que se estudia** | **Las páginas de hoy, no las de 2022**: Microsoft publica la página viva y no una versión fechada. El tema afirma lo que **no ha cambiado** entre aquella versión y ésta |
| **Aviso sobre las fuentes** | **Primer tema del proyecto cuyo objeto de estudio ha quedado obsoleto por la fecha de corte, no su redacción**: Microsoft publica que **Windows 10 llegó al fin de soporte el 14 de octubre de 2025** y que la **22H2 es su versión final**, y la convocatoria congela el temario en el 21/12/2022. **Una sola pregunta**, la del atajo de pegar; el resto del enunciado no ha caído nunca |
| **Extensión** | **1.469 palabras** |

<!-- /portada -->

**Las siglas de este tema, presentadas de entrada**: sistema operativo (**SO**), interfaz gráfica de
usuario (**GUI**), unidad central de proceso (**CPU**), sistema de archivos de nueva tecnología
(**NTFS**), la orden de recorte de bloques de las unidades de estado sólido (**TRIM**), y las teclas que se
citan por su nombre —**Ctrl**, **Alt**, **Mayús** y la tecla del
logotipo de Windows, que la documentación del fabricante escribe **Win**—.

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 9):**
> «El entorno Microsoft Windows 10 (edición Windows 10 Pro, versión 22H2). Ventanas, iconos, menús
> contextuales, cuadros de diálogo. El escritorio y sus elementos. El menú inicio. El menú de
> configuración. El explorador de Windows. Gestión de carpetas y archivos. Operaciones de búsqueda.
> Herramientas "Este equipo" y "Acceso rápido". Accesorios. Herramientas del sistema.»

<!-- indice -->

## Índice

- [Antes de empezar: la versión que el programa fija, y lo que le ha pasado](#antes-de-empezar-la-versión-que-el-programa-fija-y-lo-que-le-ha-pasado)
- [1. El escritorio y sus elementos](#1-el-escritorio-y-sus-elementos)
- [2. Ventanas, menús y cuadros de diálogo](#2-ventanas-menús-y-cuadros-de-diálogo)
- [3. El menú Inicio y la Configuración](#3-el-menú-inicio-y-la-configuración)
- [4. El Explorador de archivos](#4-el-explorador-de-archivos)
  - [4.1. «Este equipo» y «Acceso rápido»](#41-este-equipo-y-acceso-rápido)
  - [4.2. Gestión de carpetas y archivos](#42-gestión-de-carpetas-y-archivos)
  - [4.3. Operaciones de búsqueda](#43-operaciones-de-búsqueda)
- [5. Accesorios y herramientas del sistema](#5-accesorios-y-herramientas-del-sistema)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## Antes de empezar: la versión que el programa fija, y lo que le ha pasado

**El programa no dice «Windows»: dice «Windows 10 Pro, versión 22H2».** Es la primera vez en este
proyecto que un temario fija una versión de producto, y tiene una consecuencia que el opositor debe
conocer.

**Microsoft publica que Windows 10 llegó al fin de soporte el 14 de octubre de 2025 y que la 22H2 es
su versión final.** La convocatoria congela el temario en el **21 de diciembre de 2022**, de modo que
**se estudia un sistema operativo que ya no recibe actualizaciones**.

**No es un error del programa: es la consecuencia de tener fecha de corte.** Y es el primer caso del
proyecto en que la fecha de corte deja obsoleto **el objeto de estudio** y no sólo la redacción de una
norma. Lo que este tema describe es la versión 22H2 tal como la documenta su fabricante.

---

## 1. El escritorio y sus elementos

El **escritorio** es la superficie de trabajo. Sus elementos:

- **Iconos**: representan archivos, carpetas, accesos directos o unidades. **Un acceso directo no es
  el archivo**: es un puntero a él, y se reconoce por la flecha de su esquina inferior izquierda.
  Borrar un acceso directo no borra el original.
- **Barra de tareas**: contiene el botón de **Inicio**, el cuadro de búsqueda, la vista de tareas,
  los botones de las aplicaciones abiertas y ancladas, y el **área de notificación** —el antiguo
  «bandeja del sistema»— con el reloj y los iconos de estado.
- **Papelera de reciclaje**: retiene lo eliminado del disco local hasta que se vacía. **Lo borrado de
  una unidad de red o de una memoria extraíble no pasa por ella.**

---

## 2. Ventanas, menús y cuadros de diálogo

- **Ventana**: el marco en que se ejecuta una aplicación o se muestra una carpeta. Se puede
  **minimizar**, **maximizar**, **restaurar** y **cerrar** con los tres botones de su esquina
  superior derecha, y **redimensionar** arrastrando sus bordes.
- **Menú contextual**: el que aparece **al pulsar el botón secundario del ratón** sobre un elemento.
  Su contenido **depende del elemento** sobre el que se pulse: eso es lo que lo hace «contextual».
- **Cuadro de diálogo**: una ventana que pide o comunica algo y que suele **detener la interacción con
  la ventana que lo abrió** hasta que se responde. Sus controles típicos son botones, casillas de
  verificación, botones de opción, listas desplegables y cuadros de texto.
- **Cinta de opciones**: la banda de pestañas y grupos que sustituyó a los menús clásicos en el
  explorador y en las aplicaciones de Office.

**Las combinaciones de teclado de uso general**, que son las que el examen pregunta y que la
documentación de Microsoft publica en su página de métodos abreviados de Windows:

| Acción | Combinación |
|---|---|
| **Copiar** | **Ctrl + C** |
| **Cortar** | **Ctrl + X** |
| **Pegar** | **Ctrl + V** |
| Deshacer | Ctrl + Z |
| Seleccionar todo | Ctrl + A |
| Cerrar la ventana activa | Alt + F4 |
| Cambiar de aplicación | Alt + Tab |
| Abrir el Explorador de archivos | Win + E |
| Bloquear el equipo | Win + L |

**Las tres primeras están una junto a otra en el teclado —C, X, V— y se confunden**: la pregunta del
examen ofrece precisamente esas tres más Ctrl+B, y sólo una pega.

---

## 3. El menú Inicio y la Configuración

**El menú Inicio** da acceso a la lista alfabética de aplicaciones, a los iconos anclados, al botón
de cuenta de usuario, a la Configuración y al botón de inicio/apagado.

**La aplicación Configuración** es la interfaz moderna de ajustes, organizada en categorías
—Sistema, Dispositivos, Red e Internet, Personalización, Aplicaciones, Cuentas, Hora e idioma,
Accesibilidad, Privacidad, Actualización y seguridad—. Convive con el **Panel de control** clásico,
que conserva algunas opciones que no se han migrado.

---

## 4. El Explorador de archivos

Es la herramienta de gestión de carpetas y archivos. Sus zonas:

- **Panel de navegación**, a la izquierda, con **Acceso rápido**, las unidades de **Este equipo**, la
  red y la papelera.
- **Panel de contenido**, en el centro.
- **Panel de vista previa o de detalles**, opcional, a la derecha.
- **Cinta de opciones**, arriba, con las fichas Archivo, Inicio, Compartir y Vista.

### 4.1. «Este equipo» y «Acceso rápido»

**Son dos cosas distintas y el programa las nombra por separado:**

- **Este equipo** muestra **las unidades del sistema** —discos locales, unidades ópticas, dispositivos
  extraíbles y unidades de red conectadas— y las carpetas de usuario. Es la vista **por estructura**.
- **Acceso rápido** muestra **las carpetas ancladas y los archivos usados recientemente**. Es la
  vista **por uso**, y su contenido cambia solo. Se puede **anclar** una carpeta para que permanezca,
  y se puede desactivar el registro de recientes.

### 4.2. Gestión de carpetas y archivos

- **Crear**, **renombrar** —tecla F2—, **copiar**, **mover**, **eliminar**.
- **Arrastrar dentro de la misma unidad mueve; entre unidades distintas, copia.** Es el
  comportamiento por defecto y la causa de la mitad de los sustos.
- **Mayús + Supr** elimina **sin pasar por la papelera**.
- **Propiedades** de un elemento: tamaño, ubicación, fechas, atributos y, en NTFS, la pestaña de
  **Seguridad** con los permisos.

### 4.3. Operaciones de búsqueda

El cuadro de búsqueda del Explorador busca en la carpeta actual y sus subcarpetas. Admite
**comodines** —el asterisco sustituye cualquier número de caracteres, la interrogación uno solo— y
**filtros** por tipo, tamaño o fecha de modificación. La búsqueda de la barra de tareas, en cambio,
busca en todo el equipo y en la web.

---

## 5. Accesorios y herramientas del sistema

**Accesorios**: Bloc de notas, Paint, WordPad, Calculadora, Recortes, Mapa de caracteres, Grabadora
de sonidos, Símbolo del sistema.

**Herramientas del sistema**: Liberador de espacio en disco, Desfragmentar y optimizar unidades,
Información del sistema, Monitor de recursos, Programador de tareas, Visor de eventos,
Administrador de tareas —que se abre con **Ctrl + Mayús + Esc**—, Restaurar sistema, Copias de
seguridad y Windows Defender.

**Una precisión sobre la desfragmentación**: tiene sentido en discos **magnéticos**, donde reordenar
los fragmentos reduce el movimiento del cabezal. En unidades **de estado sólido** no se desfragmenta:
el sistema ejecuta en su lugar la orden **TRIM**, que marca como libres los bloques borrados.

---

## 6. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Dónde se contesta |
|---|---|---|
| 67 | Con qué comando se pega | Epígrafe 2: **Ctrl + V** |

**Una sola pregunta**, y de las combinaciones de teclado. **Todo lo demás que el enunciado del
programa enumera —ventanas, iconos, menús contextuales, cuadros de diálogo, escritorio, menú Inicio,
Configuración, Explorador, gestión de archivos, búsqueda, Este equipo, Acceso rápido, accesorios y
herramientas del sistema— no ha caído ni una vez.** Va desarrollado igual, porque el programa lo
manda y porque una sola pregunta no dice nada sobre la siguiente convocatoria.

---

## 7. Trazabilidad

- **Métodos abreviados de teclado de Windows**, documentación de soporte de Microsoft, en
  `support.microsoft.com/es-es/windows/…dcc61a57`, descargada el 2 de septiembre de 2026. De ahí sale
  la tabla del epígrafe 2, y en ella está **Ctrl + V** como combinación de pegar.
- **Ciclo de vida de Windows 10 Home y Pro**, documentación de Microsoft, en
  `learn.microsoft.com/es-es/lifecycle/products/windows-10-home-and-pro`, misma fecha. De ahí salen el **fin de soporte del 14 de octubre de
  2025** y que la **22H2 es la versión final**.

**Lo que no se ha podido verificar y va dicho**: la documentación descargada es **la página viva de
hoy**, no una versión fechada en 2022. Lo que este tema afirma de la 22H2 es lo que **no ha cambiado**
—las combinaciones de teclado, la estructura del Explorador, la distinción entre «Este equipo» y
«Acceso rápido»—. **La descripción de la interfaz procede del conocimiento común del producto**, no de
un manual concreto, y se expone como tal.
