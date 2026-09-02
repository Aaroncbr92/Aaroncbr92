# Tema 12 del específico de Gestión Administrativa · Microsoft Teams, versión 1.6.00.376

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 12 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | Documentación de Microsoft sobre canales de Teams |
| **Identificador** | `learn.microsoft.com/microsoftteams/private-channels`, en `fuentes/ofimatica/` |
| **Redacción que se estudia** | Página viva, descargada el 02/09/2026 |
| **Aviso sobre las fuentes** | **La versión que el programa cita, la 1.6.00.376, no tiene documentación propia**: Microsoft documenta Teams como servicio, no compilación a compilación. El tema **no promete describir esa versión**; describe lo documentado y avisa de qué es configurable por cada organización. **Una sola pregunta**, la de los permisos del canal privado, cuya respuesta es correcta con un matiz: quien añade gente es el propietario **del canal**, no necesariamente el del equipo |
| **Extensión** | **1.261 palabras** |

<!-- /portada -->

**Las siglas de este tema, presentadas de entrada**: el identificador de usuario de la organización
(**cuenta corporativa**), el protocolo de voz sobre internet (**VoIP**), el fichero de documento
portátil (**PDF**) y la red privada virtual (**VPN**).

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 12):**
> «Microsoft Teams (versión 1.6.00.376). Configuración y personalización. Crear grupos, gestionar
> miembros, gestión de canales, trabajar con mensajes y publicaciones. Chats y llamadas. Configurar
> eventos en directo. Crear y administrar reuniones. Compartir documentos. Compartir pantalla.»

<!-- indice -->

## Índice

- [Antes de empezar: la versión que el programa cita no tiene documentación propia](#antes-de-empezar-la-versión-que-el-programa-cita-no-tiene-documentación-propia)
- [1. La estructura: equipos, canales y pestañas](#1-la-estructura-equipos-canales-y-pestañas)
- [2. Tipos de canal y reparto de permisos](#2-tipos-de-canal-y-reparto-de-permisos)
- [3. Mensajes y publicaciones](#3-mensajes-y-publicaciones)
- [4. Chats y llamadas](#4-chats-y-llamadas)
- [5. Reuniones y eventos en directo](#5-reuniones-y-eventos-en-directo)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## Antes de empezar: la versión que el programa cita no tiene documentación propia

**El Anexo 2 fija la versión 1.6.00.376.** Microsoft **no publica notas de una compilación de
escritorio con ese número**: documenta Teams como servicio, con páginas vivas que describen su
funcionamiento actual.

**Eso significa que este tema no puede prometer que describe esa compilación exacta**, y no lo
promete. Describe **el funcionamiento documentado de Teams** en lo que es estable —la estructura de
equipos y canales, los tipos de canal, el reparto de permisos—, señalando lo que es configurable por
la organización y por tanto variable de una casa a otra.

---

## 1. La estructura: equipos, canales y pestañas

- **Equipo**: el contenedor. Agrupa a un conjunto de personas y todo lo que producen.
- **Canal**: la subdivisión temática dentro de un equipo. Todo equipo tiene un canal **General** que
  no se puede eliminar.
- **Pestañas**: dentro de cada canal, las secciones —Publicaciones, Archivos y las que se añadan—.

**Cada canal tiene su propia carpeta de archivos**, y de ahí sale la regla de convivencia más útil:
**lo que se sube a un canal queda en la biblioteca de ese canal**, no en la del equipo entero.

---

## 2. Tipos de canal y reparto de permisos

**Es el epígrafe que el examen pregunta**, y conviene apoyarlo en la documentación literal.

| Tipo | Quién ve el contenido |
|---|---|
| **Estándar** | Todos los miembros del equipo |
| **Privado** | Sólo los miembros del canal, que son un subconjunto del equipo |
| **Compartido** | Miembros del canal, que pueden pertenecer a otros equipos o a otras organizaciones |

**Sobre el canal privado, la documentación de Microsoft dice:**

> «Los canales privados de Microsoft Teams crean espacios prioritarios para la colaboración de los
> equipos. **Solo los usuarios del equipo que sean propietarios o miembros del canal privado podrán
> acceder al canal.** Cualquier persona, incluidos los invitados, puede agregarse como miembro de un
> canal privado **siempre y cuando sean miembros existentes del equipo**.»

Y sobre quién manda dentro de él:

> «**La persona que crea un canal privado es el propietario del canal privado y solo el propietario
> del canal privado puede agregar o quitar personas directamente.** El propietario de un canal
> privado puede agregar cualquier miembro del equipo a un canal privado que haya creado, incluyendo
> invitados. Los miembros de un canal privado tienen un espacio de conversación seguro, y cuando se
> agregan nuevos miembros, **pueden ver todas las conversaciones (incluso las conversaciones
> antiguas)** en ese canal privado.»

**Y sobre quién puede crearlos:**

> «**De forma predeterminada, los miembros del equipo o el propietario del equipo pueden crear un
> canal privado. Los invitados no pueden crear canales privados.** La posibilidad de crear canales
> privados se puede administrar a nivel de equipo y de organización.»

**Tres consecuencias que hay que retener por separado:**

1. **Sólo el propietario del canal privado añade o quita gente directamente.** Los demás miembros del
   canal, no.
2. **Sólo se puede añadir a quien ya sea miembro del equipo.** Un canal privado no es una puerta de
   entrada al equipo.
3. **Un miembro del equipo puede crear canales privados por defecto**, no hace falta ser propietario
   del equipo ni administrador global. Pero eso **se puede restringir por directiva**, y ahí la
   respuesta depende de cómo lo tenga configurado cada organización.

**Un canal privado se identifica por un icono de candado**, y quien se incorpora **ve el historial
completo** de las conversaciones anteriores.

---

## 3. Mensajes y publicaciones

- **Publicación**: el mensaje en un canal, visible para quien tiene acceso a él. Genera **hilo**: las
  respuestas quedan colgadas de la publicación original, no sueltas.
- **Menciones**: `@persona`, `@canal` y `@equipo`, que notifican al destinatario.
- **Anuncio**: publicación con encabezado destacado.
- **Formato**: texto enriquecido, adjuntos, emojis, reacciones, marcado como importante o urgente.

---

## 4. Chats y llamadas

- **Chat**: conversación privada entre dos personas o en grupo. **Vive fuera de los canales**, y por
  tanto **fuera del equipo**: sus archivos van al almacenamiento personal de quien los comparte, no a
  la biblioteca del canal. Es la distinción práctica más importante y la que produce más archivos
  perdidos.
- **Llamadas**: de voz y de vídeo, entre personas o en grupo.
- **Estado de presencia**: disponible, ocupado, no molestar, vuelvo enseguida, ausente, sin conexión.

---

## 5. Reuniones y eventos en directo

**Reunión**: encuentro programado o instantáneo, con calendario, invitados, sala de espera, grabación
y transcripción si la organización lo permite. Sus roles son **organizador**, **moderador** y
**asistente**, y de ellos depende quién puede compartir, silenciar o admitir a alguien.

**Evento en directo**: es una emisión, no una reunión. **La distinción es de arquitectura**: en una
reunión todos pueden hablar y verse; en un evento en directo hay **un grupo que produce y emite** y
**una audiencia que recibe** y sólo interviene por un panel de preguntas y respuestas moderado.
Admite audiencias mucho mayores.

**Compartir pantalla** dentro de una reunión permite mostrar el escritorio completo, una ventana, una
pizarra o una presentación, y **dar el control** a otro participante.

**Compartir documentos**: los archivos de un canal se editan **en el propio Teams**, con coautoría en
tiempo real, y se guardan en la biblioteca del canal con su historial de versiones.

---

## 6. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Dónde se contesta |
|---|---|---|
| 76 | Cómo se gestionan los permisos al crear un canal privado | Epígrafe 2 |

**Una sola pregunta**, y su respuesta oficial es la que dice que **los propietarios del equipo pueden
crear un canal privado y asignarle miembros, y que los miembros del canal no pueden añadir a otros ni
modificar permisos**.

**Es correcta en lo que importa** —los miembros no añaden ni cambian permisos— y **la documentación
la matiza en un punto**: quien añade o quita directamente es **el propietario del canal privado**,
que es quien lo creó, y **no necesariamente un propietario del equipo**, porque **por defecto también
un miembro puede crear canales privados**. Las otras tres opciones son falsas sin matiz: los miembros
no invitan sin restricciones, no hacen falta administradores globales y **nadie convierte un canal
privado en estándar**.

**Queda anotado como matiz de la respuesta, no como errata**: la opción escogida es la única
marcable.

---

## 7. Trazabilidad

- **Canales privados en Microsoft Teams**, documentación de Microsoft, descargada el 2 de septiembre
  de 2026 y guardada en `fuentes/ofimatica/MS_teams-canales-privados.txt`. De ahí salen las tres
  citas literales del epígrafe 2.
- **Cuadernillo `23_preguntas_gea`**, pregunta 76, con su plantilla oficial.

**Lo que no se ha podido conseguir y va dicho**: la documentación de la versión 1.6.00.376 que el programa
cita **no existe como tal**. Microsoft documenta Teams como servicio y publica páginas vivas.
Este tema **no promete describir esa compilación**: describe el funcionamiento documentado del
producto y avisa de qué partes son configurables por cada organización.
