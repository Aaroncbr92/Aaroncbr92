# Tema 15 del específico de Operador/a Montador/a de Vídeo · Organización de proyectos, nomenclatura, trazabilidad y buenas prácticas colaborativas

**Siglas**: RTVA; CSRTV; BOJA; SMPTE; EBU; MXF; UMID; AAF; OMF; EDL; TC; ENG; MAM; LAN; SAN.

Esqueleto para repasar, no resumen: refresca cada dato con la fuente que va delante; no sustituye la lectura del tema.

<!-- indice -->
<!-- /indice -->

## El punto en la ficha del puesto
- Convenio, anexo III, ficha 5212206: «Configurar sistemas de edición y preparar los materiales a utilizar.»
- Convenio, ficha 5212206: «Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de programas y bloques publicitarios.»
- Convenio, objeto del puesto: edición y postproducción «en coordinación con otras áreas» (reparto en tema 9).

## 1. Organización de proyectos
- Advertencia: no hay norma legal ni documento publicado de CSRTV sobre su sistema, organización o nombres. Fuente = documentación de fabricante (Avid 1999 + Resolve 21) y oficio declarado.
- Avid 1999 p.33/66/211: proyecto y material separados; *bin* = clips+secuencias; *master clip* vinculado al material; *subclip* = trozo marcado.
- Avid 1999 p.72: «un proyecto nuevo por cada programa, episodio, anuncio o escena».
- Avid 1999 pp.72-73: tres juegos de *bins* — 1) ingesta (un *bin* por cinta/origen); 2) organización (por segmento); 3) montaje: bin de montaje en curso, de archivo (versión original), de selección, de cortes con formato.
- Avid 1999 p.73: guardar la estructura como plantilla; dos juegos de *bins* activos (ingesta/organización vs. montaje) reducen desorden.
- Oficio: aplicado a ficheros — 1er juego por tarjeta/cámara/enlace/agencia; 2º por bloque o tipo de material; 3er juego separa en curso / versiones anteriores / selección / emisión.
- Avid 1999 p.261/269-270: tres vistas de *bin* — Text (tabla, ordena/filtra), Frame (fotogramas, contactos), Script (Text+Frame+notas, ficción).
- Oficio: la vista Text es la que más rinde para organizar (columnas comunes de sala).
- Avid 1999 pp.73-74: guardado automático periódico; copias en carpeta *Attic*.
- Avid 1999 pp.35-36: *Attic* en el nivel superior del disco Avid, una carpeta por proyecto; extensión .bak + número de versión; la de versión más alta es la más reciente.
- Avid 1999 p.74: se recurre a *Attic* para volver a una versión anterior o si el *bin* actual se corrompe; guardado manual recomendado tras un cambio importante.
- Salvedad: ubicación/extensión/nº de copias de *Attic* son de la guía de 1999; versión vigente del programa no comprobada.
- Resolve 21 Ref. Manual (2026) cap.3 p.82: bibliotecas de proyectos (no ficheros sueltos); tipos local, de red, en la nube (Blackmagic Cloud); exportación a otro usuario = fichero .drp.
- Resolve 21 pp.89-93: Live Save (incremental, por defecto activado); *Project Backups* (esquema GFS, excluye *stills* y LUTs, se abren como proyectos independientes); *Timeline Backups* (mismo esquema, restaurar no sobrescribe, añade «Backup» al nombre).
- Resolve 21 pp.90/93: copia cada 10 min → seis en la última hora; carpeta «ProjectBackup», configurable.
- Resolve 21 p.89: aviso «Edited» junto al nombre; amarillo a los 15 min, rojo a los 30 min sin guardar.
- Resolve 21 p.92: antes de un cambio radical, duplicar el *timeline* (más seguro) o fijar un punto de retorno manual.

## 2. Nomenclatura
- Libro de Estilo CSTV/C2A (2004) 6.1 p.88: la escaleta fija hecho, formato/número/clave, tiempos, autor, procedencia, presentador y acotaciones técnicas; se refleja en los partes de emisión (vías de sonido, coleo, rótulos, observaciones, pie de texto).
- Libro de Estilo 6.1: cualquier cambio de la escaleta se comunica «desde el origen de la decisión, inmediata y simultáneamente, a todas las personas y departamentos afectados».
- Libro de Estilo 6.1.1 p.88: «Son inadmisibles los cambios en la identificación de un vídeo»; «Si un vídeo se llama de un modo concreto, no podrá modificarse su denominación aleatoriamente.»
- Libro de Estilo 6.1.1: única excepción — vídeo terminado antes de elaborar la escaleta: el equipo de edición traslada o adapta el nombre del autor.
- Libro de Estilo 6.1.2 p.88-89: el redactor fija en escaleta sus textos definitivos, rótulos (orden y ubicación) y pasos de locutor.
- Libro de Estilo 6.1.2 pp.88-89: informativos en cadena — los centros territoriales se ciñen a la nomenclatura de la escaleta de cadena; si el mismo vídeo se emitió antes en desconexión, el envío a Servicios Centrales lleva el nombre de cadena, «independientemente del método interno que se use».
- Oficio: nombre interno libre; el que ve la cadena, no.
- Avid 1999 p.41: no usar `/ \ : * ? " < > |` en nombres de proyectos, *bins* y usuarios (para portabilidad entre plataformas); opción «Use Windows compatible File Names».
- Avid 1999 pp.126-127: una sola convención de mayúsculas (TAPE/Tape/tape = tres cintas distintas → problemas al digitalizar por lotes, redigitalizar, generar EDL).
- Avid 1999 p.127: esquema de nombres pensado de antemano, según cantidad/complejidad del material de origen.
- Avid 1999 p.127: algunos controladores de edición truncan nombres de cinta a 6 caracteres → riesgo de confundir cintas al generar EDL.
- Avid 1999 p.126: nombres de cinta alfanuméricos (A-Z, 0-9), mayúsculas y minúsculas, máx. 32 caracteres (dato de esa versión y ese campo, no regla general).
- Avid 2010 p.25: ejemplo de nombre de secuencia duplicada — «Sequence_ForMix».
- Oficio (propuesta, no norma de CSRTV): nombre de pieza = el de la escaleta; orden fijo fecha-programa-nombre-versión; fecha AAAA-MM-DD; sin espacios/tildes/caracteres prohibidos; guiones o guiones bajos; una sola convención de mayúsculas; versión numerada o por destino, nunca «final»/«definitiva»/«buena»; nombre del material de origen intocable.

## 3. Trazabilidad
- Definición de oficio: reconstruir de un plano emitido su material, quién lo tocó y en qué versión, y de un material dónde se ha usado. Se apoya en TC, identificadores, metadatos de secuencia y relación entre versiones.
- Libro de Estilo 5.3.3 p.81: el TC es «acuerdo básico entre periodista y cámara»; puede usarse TC real acotado o marcador a 00:00:00 al inicio de cinta, «mejor... sobre todo cuando el material va a ser usado por terceras personas».
- Libro de Estilo 3.17.1.5 p.61: entrevista con dos o más cámaras ENG independientes → «el código de tiempo que se aplicará será idéntico para facilitar el montaje final».
- Oficio: el TC es la dirección de cada cuadro; no se regraba/recodifica el material sin conservar su código original.
- SMPTE ST 377-1:2019 (definiciones): UMID = «Unique Material ID according to SMPTE ST 330»; como Package ID sólo vale el UMID básico de 32 bytes; UMID extendido = 64 bytes (32 básico + 32 de metadatos).
- SMPTE ST 377-1 remite a SMPTE ST 330 (2011) para la estructura interna del UMID — no leída, el tema no la da.
- Oficio: el nombre de fichero puede cambiar y repetirse; el UMID no, y permite reencontrar el material aunque el nombre cambie.
- Avid 2010 p.18: AAF y OMF, «los dos formatos estándar de la industria» para intercambiar composiciones y material entre aplicaciones; el fichero lleva metadatos de edición + material (embebido o enlazado); imagen: material = piezas del puzle, metadatos = instrucciones.
- Avid 2010 p.19: Avid prefiere AAF — más completo, puede embeber/referir MXF (OMF no); p.11: AAF es clave para interoperar con Pro Tools.
- Oficio: mientras el material conserve su identificación, la secuencia exportada reconstruye qué trozo de qué fichero se usó; perdida esa identificación, no.
- EBUCore (EBU Tech 3293 v1.10, 2020) 3.5 pp.18-19: motivos de versión (más corta, otra lengua, con/sin subtítulos, otro soporte); se identifican con relaciones *hasVersion* / *hasSource*, que enlazan las piezas y sus diferencias.
- Oficio: versión original no se sobrescribe (Avid 1999 p.73, *bin* de archivo); cada versión = secuencia distinta con nombre propio; lo que va a cadena = nombre de escaleta de cadena; metadatos de pieza a la base de datos (tarea de ficha; MAM en tema 13; archivo en tema 8).

## 4. Buenas prácticas colaborativas
- ELEMENTS (Filip Milovanovic, 24-01-2023, fuente secundaria): bloqueo de *bins* «first come, first served»; primero en abrir = escritura (candado verde); siguiente = solo lectura, candado rojo, ve la última versión guardada.
- ELEMENTS: fichero .lck se crea al abrir el *bin*; fichero .log con modificaciones; requiere que el almacenamiento lo soporte; no todas las licencias lo incluyen (sí Ultimate/Enterprise/perpetua; no First ni suscripción estándar, dato de 2023).
- Avid *What's New* v2023.3 p.2: «Lock Project Bin» (verde, impide cambios ajenos); «Protect Project Bin» (rojo, solo lectura para todos incluido el dueño, siempre se abre bloqueado); «Unlock Project Bin» (libera, con el *bin* cerrado).
- Oficio: cada montador trabaja en sus *bins*; los compartidos se abren solo para leer/coger material; lo entregado se protege; un *bin* abierto sin necesidad bloquea a los demás.
- Resolve 21 cap.197 p.4329: requisitos — proyecto en Blackmagic Cloud o servidor de bibliotecas configurado (equipo que nunca se apaga/suspende); todos en red; material idealmente en SAN común.
- Resolve 21 p.4330: activación con «File > Multiple User Collaboration»; desactiva auto-conform de *clips*; activa Live Save (no se puede desactivar con colaboración activa, cap.3 p.90).
- Resolve 21 p.4332: modelo «first come, first served»; quien abre *bin*/*timeline*/selecciona clip en Fusion o Color obtiene el bloqueo; los demás ven con insignia de color, sin poder cambiar.
- Resolve 21 pp.4332-4335: *bin* se libera al seleccionar otro; *timeline* se libera al cerrarlo (otros sí pueden moverlo de *bin*); clip en Fusion/Color se libera al seleccionar otro (compositor y colorista simultáneos, bloqueos separados).
- Resolve 21 p.4332: cambios «checked in» al liberarse; cada colaborador refresca (icono circular) para verlos.
- Resolve 21 pp.4334-4335: «Lock/Unlock Bins» a mano; Opción-clic abre en solo lectura (insignia de ojo); «Lock/Unlock Timeline».
- Resolve 21 pp.4338-4339: dividir el programa en «reels», un *timeline* por *bin*; si dos deben tocar el mismo *timeline*, duplicar en *bin* propio, avisar por chat, comparar con «Compare With Current Timeline»; ayudantes y montadores se reparten *bins*.
- Oficio (comparando ambos programas): el primero que llega escribe, los demás leen; cada uno trabaja en sus propios *bins*.
- Avid Knowledge Base (act. 11-08-2023): compartir proyecto/*bin* entre versiones — comprobar compatibilidad de formatos/transcodificar; complementos de terceros instalados en ambos equipos; limitar efectos no soportados en la versión antigua; disponer de todo el material (local, transcodificado, enlazado, plantillas de títulos) o el proyecto «may not open properly»; copia de seguridad antes de compartir/migrar.
- Avid KB: en secuencias solo de cortes, clips/subclips/secuencia son casi idénticos entre versiones; lo delicado son efectos, complementos y material.
- Avid 2010 p.25: entrega a sonido — dos carpetas («To Audio Editor» / «From Audio Editor»); se entrega un duplicado con nombre propio (Sequence_ForMix), no la secuencia de trabajo; intercambio en AAF.
- Libro de Estilo 6.1: avisar de cualquier cambio a todos los afectados (canales de coordinación, tema 9).

## Aplicación práctica: organizar una pieza de informativo
- Supuesto de oficio, 10 pasos: abrir proyecto desde plantilla → *bin* por origen (tarjeta 1/2, archivo) → *bin* de selección (totales/recursos) → secuencia con nombre de escaleta sin variantes (Libro Estilo 6.1.1) → guardado manual tras cambios (Avid, *Attic*) → duplicar para versión corta/redes, original al *bin* de archivo y protegida (EBUCore, no sobrescribir) → si va a cadena, nombre de escaleta de cadena (6.1.2) → si hay mezcla, duplicado «para mezcla» en AAF → meter título/versión/autor/destino en base de datos (tarea de ficha) → avisar de cambios (6.1).
- Errores típicos de examen práctico (oficio): secuencia «final» repetida; vídeo renombrado que ya no casa con la escaleta; material regrabado sin TC; dos montadores sobre el mismo *bin* sin bloqueo; versión corta recortando la secuencia emitida en vez de un duplicado.

## Lo que este tema no da
- Sistema de edición/almacenamiento compartido de CSRTV, convención de nombres o plantilla propia: no consta publicado.
- Copias automáticas de la versión vigente de Media Composer (la guía leída es de 1999).
- Menús de otros programas (Premiere, etc.); de Resolve solo caps. 3 y 197.
- Estructura interna del UMID: SMPTE ST 330, no leída.
- Proyectos/*bins*/*timeline*/códecs/*proxies*/exportación → tema 3. Ingesta/verificación/archivo → tema 8. Coordinación → tema 9. MAM/plantillas → tema 13. Urgencia/versionado bajo presión → tema 14.
