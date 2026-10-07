# Tema 15 del específico de Ayudante de Producción · Herramientas ofimáticas y aplicaciones de gestión aplicadas a la producción

**Siglas**: RTVA, CSRTV, BOJA, SGBD, ERP, TIC, SGSI, LOPD, ENS, VBA.

Esqueleto para repasar, no resumen: el detalle y las citas literales están en el tema.

<!-- indice -->

Herramientas · Hojas de cálculo · Documentos compartidos · Correo · Agenda · Bases de datos · Sistemas corporativos · Lo que este tema no da

<!-- /indice -->

## Herramientas ofimáticas y aplicaciones de gestión aplicadas a la producción

- Ningún documento publicado dice qué paquete usan RTVA y CSRTV; se describe Microsoft (oficio).
- Soporte Microsoft: Office 2019, ciclo de vida fijo, fin ampliado 15-10-2025 (10/15/2025 6:59:59 AM, hora Pacífico).
- Soporte Microsoft: Teams clásico, fin de soporte 1-7-2024; fin de disponibilidad 1-7-2025.
- Guía Microsoft: SharePoint = equipo/grupo/organización, permisos sólidos, externos; OneDrive = individual y de equipo, privado hasta compartir; Teams = equipo, conversar, archivos, llamadas; equipos públicos o privados.
- Oficio: borrador, OneDrive; equipo, canal de Teams (SharePoint por debajo); toda la organización, sitio de SharePoint.
- Oficio: una sola versión viva y un responsable; hoja para gastos, dietas e inventario; documento compartido para escaleta, plan y citaciones; correo para peticiones; agenda para reuniones y reservas; BD para invitados; ERP para pedidos, facturas y contabilidad; contratos, aplicativos jurídicos fuera del ERP.
- Libro de estilo 4.4: peticiones a producción, salvo urgencia extrema, «por escrito, a través de los cauces ofimáticos habituales, y con la mayor precisión».
- Libro de estilo 4.4.4 p.6: propuestas entre periodistas, técnicos y productores nunca de viva voz sino con constancia; acuerdo final obligatorio para todos.

## Hojas de cálculo

- Excel: libro > hojas > celdas (A1); rango A1:B10; máximo 1.048.576 filas x 16.384 columnas.
- Excel: referencia por defecto relativa; al copiar cambia. Copiada 2 abajo y 2 a la derecha: $A$1 queda $A$1; A$1 queda C$1; $A1 queda $A3; A1 queda C3.
- Excel: F4 cambia entre tipos de referencia. Toda fórmula empieza por =.
- Excel: SUMA suma; PROMEDIO media (ignora texto, lógicos y vacías; cuenta ceros); CONTAR números; CONTARA no vacías (incluye error y ""); ni una ni otra cuentan vacías.
- Excel: SI; SUMAR.SI(rango;criterio;[rango_suma]); CONTAR.SI; MAX; MIN; HOY() sin argumentos; con varios criterios, SUMAR.SI.CONJUNTO y CONTAR.SI.CONJUNTO.
- Excel: BUSCARV, valor buscado a la izquierda del devuelto; BUSCARX, cualquier dirección, exacta por defecto, no en Excel 2016 ni 2019.
- Errores Excel: #¡DIV/0! división por cero o celda 0/vacía; #¡REF! celda no válida (eliminada o pegada encima); #N/A no encuentra lo buscado (BUSCARX, BUSCARV, BUSCARH, BUSCAR, COINCIDIR); #¡VALOR! tipo de dato incorrecto (oficio).
- SI.ERROR(FORMULA();0) oculta el error.
- Excel: ordenar, autofiltro; formato condicional; macros VBA; protección de celdas, hoja y libro.
- Excel, validación de datos: restringe tipo o valores en celda, p. ej. lista desplegable.
- Excel, tabla dinámica: origen en columnas con una sola fila de encabezado; Insertar>tabla dinámica; no numéricos a Filas, fecha/hora a Columnas, numéricos a Valores; por defecto SUM; si cambia el origen, actualizar.
- Excel, filtro: oculta temporalmente; en tabla, controles automáticos; se borra el filtro para ver todo.
- Excel, duplicados: filtrar únicos oculta; quitar duplicados elimina permanentemente; duplicado = todos los valores de una fila idénticos a otra; compara lo visible (8/03/2006 y 8 de marzo de 2006, únicos); antes filtrar únicos o formato condicional.
- Excel, segmentación de datos: botones para filtrar tablas o tablas dinámicas; indica el estado del filtrado; sirve a varias tablas dinámicas con el mismo origen; Segmentación > Conexiones de informe.
- Oficio: dietas, cuantías en celda aparte con referencia absoluta (temas 6 y 14); en libro compartido, filtrar u ordenar cambia la vista a todos.

## Documentos compartidos

- Microsoft 365: vínculos en lugar de adjuntos (documento en OneDrive o SharePoint); evita conciliar versiones.
- Teams soporte, permisos: Puede editar, Puede revisar, Puede ver, No se puede descargar; Copiar vínculo.
- Vínculo Cualquiera: no autentica, no auditable; clave secreta revocable y transferible.
- Vínculo Personas de su organización: sólo miembros (no invitados); autentica; revocable y transferible.
- Vínculo Personas específicas: internos y externos; autentica como el usuario indicado; revocable y no transferible.
- Cualquiera: transferible (se reenvía), revocable (se elimina el vínculo), secreto (no se adivina).
- Teams, archivos del canal: SharePoint del equipo, pestaña Compartido; del chat: OneDrive para la Empresa del emisor, sólo los del chat; el OneDrive que se ve en Teams no es el personal.
- Coautoría (tiempo real): archivo en la nube + versión con suscripción; sin suscripción se edita a la vez pero hay que guardar para ver cambios. Abrir en el escritorio desde el vínculo. Deshacer/Rehacer pueden fallar. .docm admite coautoría.
- Autoguardado: suscriptores de Excel, Word y PowerPoint; guarda cada pocos segundos.
- Autoguardado activo por defecto en OneDrive, OneDrive para la Empresa y SharePoint Online; desactivado en SharePoint local, servidor de archivos, otra nube, ruta local (C:\) o archivo sin guardar. Sin él, sigue la Autorrecuperación.
- Autoguardado activo: cambios en el archivo original.
- Historial de versiones: versión al primer cambio, luego ocasionalmente, cada 10 minutos aproximadamente; nombre del archivo > Historial de versiones > Abrir versión > Restaurar.
- Word, control de cambios (Revisar): marca autores; eliminaciones tachado, adiciones subrayado; colores por autor; Para todos / Solo míos; desactivar deja de marcar pero las marcas siguen.
- Word, vistas: Revisión simple (línea roja en margen); Todas las marcas; Sin marcado; El original. Ocultar no quita: hay que Aceptar o Rechazar (uno a uno o todos).
- Word: panel de revisiones, resumen con número de marcas y comentarios; bloqueo con contraseña (Revisar > Proteger > Proteger documento): no se desactiva ni se acepta/rechaza; comentarios ya no forman parte del control de cambios.

## Correo

- Outlook: clásico (pestaña Archivo) y nuevo (sin ella); entorno: correo, calendario, Personas, tareas, notas.
- Responder, al remitente; responder a todos, también a los demás; reenviar, a alguien nuevo con adjuntos.
- Reglas: nombre, condición y acción (al menos tres), con excepciones; Stop processing more rules; nuevo Outlook no admite reglas para cuentas de terceros.
- Respuestas automáticas: un mensaje por persona; programables; distintos para internos y externos. Clásico Archivo > Respuestas automáticas; nuevo Ver > Ver configuración > Cuentas > Respuestas automáticas. Sin período, desactivar a mano. Hacia fuera, a todo (boletines, spam): limitar a contactos. No compatibles con Gmail, Yahoo, POP o IMAP (clásico: regla con Outlook abierto).
- .pst: mensajes, contactos, citas, tareas, notas, diario; copia de seguridad o elementos antiguos; nuevo Outlook, abrirlos exige el clásico.
- Atajos Outlook clásico: reenviar Ctrl+F; responder Ctrl+R; responder a todos Ctrl+Mayús+R; nuevo Ctrl+Mayús+M; enviar Alt+S; buscar Ctrl+E o F3; comprobar Ctrl+M o F9; Calendario Ctrl+2.
- Nuevo Outlook: reenviar Ctrl+F; enviar Ctrl+Entrar; nuevo mensaje o evento Ctrl+N; página española, responder Ctrl+D. Trampa: Ctrl+F reenvía, no busca.

## Agenda

- Outlook: agenda = calendario. Cita: sin invitados ni recursos; se convierte en reunión con Invitar a asistentes.
- Nueva cita: Ctrl+N en Calendar, Ctrl+Mayús+A en otra carpeta; Responder con reunión desde un correo.
- Mostrar como: Libre, Trabajando en otro lugar, Provisional, Ocupado, Fuera de la oficina.
- Periodicidad: Diaria, Semanal, Mensual, Anual; la pestaña Cita pasa a Serie de citas.
- Aviso: por defecto 15 minutos antes; Ninguno lo desactiva.
- Teams en Outlook: integrado o complemento según versión (nuevo Outlook, integrado); no con cuenta personal ni POP/IMAP.
- Compartir calendario (Inicio > Compartir calendario): Puede ver cuando estoy ocupado (sólo disponibilidad); Puede ver títulos y ubicaciones; Puede ver todos los detalles. Ninguno permite cambiar.
- Atenuada: directiva del administrador o TI. Añadir calendario ajeno directo: sólo cuentas profesionales o educativas.
- Puede editar: ver y cambiar el calendario.
- Delegado: edita, programa reuniones y responde en su nombre. Límites: sólo cuenta profesional o educativa de Microsoft 365 o Exchange Online; sólo calendario principal; no editor ni delegado a ajenos a la organización.

## Bases de datos

- Access, base de datos: herramienta para recopilar y organizar información; listas grandes traen redundancias; pasar a SGBD (DBMS), p. ej. Access.
- Base de datos = conjunto de datos; SGBD = programa. Tres tablas = una base de datos. Extensiones .accdb (anteriores .mdb).
- Tabla: filas y columnas, sin redundancias (cada empleado una vez). Registro = fila; campo = columna, un elemento de información, con tipo (texto, fecha u hora, número).
- Modelo relacional: tabla = relación; fila = tupla; columna = atributo.
- Clave principal: identifica cada fila; sin duplicados (no usar nombres); siempre con valor; valor que no cambia; a menudo número único arbitrario.
- Clave externa = clave principal de otra tabla.
- Uno a varios (proveedor-productos): clave del lado «uno» como columna en «varios».
- Varios a varios (pedidos-productos): tercera tabla (de unión) con dos relaciones uno a varios.
- Uno a uno: misma clave principal en ambas, o clave de una como externa en la otra; valorar combinarlas.
- Primer principio: la información duplicada es perjudicial. Normalización = aplicar las reglas al diseño.
- Objetos: formulario (escribir y editar datos, controlar la interacción); informe (formato, resumen, presentación; datos actuales); consulta (recuperar datos con criterios); macro (lenguaje simplificado); módulo (VBA).
- Consulta de selección, recupera; de acción, crea tablas, agrega, actualiza o elimina; en consultas actualizables los cambios van a las tablas.
- Combinar correspondencia (Word): documento principal con campos de combinación; orígenes habituales, hojas de Excel y contactos de Outlook; cartas, correos (un destinatario en Para), sobres, etiquetas, directorios.
- Oficio: la agenda de invitados es tratamiento de datos personales (tema 10 del común).

## Sistemas corporativos

- Informe 2018, nota 41: ERP = conjunto de sistemas que integra los procesos más relevantes; un solo programa con base de datos centralizada (dato único); puede tener módulos independientes.
- Informe 2018, puntos 226 y 227: ERP del grupo, marca comercial SAP, adquirido en 1999; sin inversiones ni mejoras desde adquisición (ninguna desde 2012); obsoleto; contabilidad analítica fuera del módulo SAP.
- Informe 2018, punto 99: no se obtuvo listado íntegro de contratos de 2018; no hay conexión entre SAP y los aplicativos de servicios jurídicos.
- Informe 2018, punto 205: porcentaje de servicio público calculado fuera de SAP, con hojas de cálculo.
- Salvedad: situación de 2018; no consta renovación posterior.
- Comité TIC de RTVA y CSRTV (informe 9.2.1; Disposición nº 4, 7-4-2016, sustituida el 25-10-2019 por la Disposición nº 6, texto vigente no publicado); lo preside el Director/a Gerente.
- Comité TIC, funciones a) plan anual de proyectos y revisar ejecución; b) correspondencia procesos informáticos y de negocio; c) proponer política de seguridad; d) aprobar procedimientos del SGSI y proponer auditorías; e) revisar normativa de seguridad y LOPD; f) roles y responsabilidades de seguridad; g) aprobar procedimientos de identidades, perfiles y accesos y designar responsables de altas y bajas; h) nombrar responsable de seguridad de la información; i) nombrar Comité de seguridad de la información; j) otras cuestiones.
- RD 311/2022 art. 1.2: ENS = principios básicos y requisitos mínimos para proteger información y servicios; acceso, confidencialidad, integridad, trazabilidad, autenticidad, disponibilidad, conservación.
- RD 311/2022 art. 2.1: aplica a todo el sector público (art. 2 Ley 40/2015; art. 156.2).
- Ley 40/2015 art. 2: sector público institucional; a) organismos públicos y entidades de derecho público; b) entidades de derecho privado vinculadas o dependientes (apartado 2).
- RD 311/2022 art. 2.3: también a sistemas de entidades del sector privado que presten servicios o provean soluciones al sector público por relación contractual, con política de seguridad (art. 12); pliegos con requisitos de conformidad con el ENS para contratistas.
- Salvedad: no consta en qué letra del art. 2.2 encajan RTVA (agencia pública empresarial) y CSRTV (S.A.), ni política de seguridad conforme al ENS.

## Lo que este tema no da

- No constan: paquete, correo, agenda y aplicaciones de RTVA y CSRTV; Disposición nº 6 (25-X-2019); política ENS; letra del art. 2.2 Ley 40/2015.
- Fuera del enunciado: PowerPoint, POP/IMAP, administración de OneDrive, SharePoint y Teams, Excel avanzado, SQL. Dietas y gastos, temas 6 y 14; documentación y cierre, tema 5; datos personales, tema 10 del común.
