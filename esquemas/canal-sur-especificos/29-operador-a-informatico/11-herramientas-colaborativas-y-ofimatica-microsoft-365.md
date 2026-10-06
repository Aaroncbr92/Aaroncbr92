# Tema 11 del específico de Operador/a Informático · Herramientas colaborativas y ofimática Microsoft 365

**Siglas**: RTVA, CSRTV, BOJA, MFA, B2B, CDN, POP3, IMAP4, SMTP, SSL/TLS, STARTTLS, OAuth 2.0, MAPI, EWS, SCP, PDF, VBA, .pst, GB, TI, Entra ID.

Esqueleto para repasar, no resumen: sin norma; fuente Microsoft Learn/Soporte (leída 05-10-2026; control de cambios, funciones Excel, respuestas automáticas y calendario, 06-10-2026). Fuera: Office 2019, Teams clásico.

<!-- indice -->
<!-- /indice -->

## 1. Microsoft 365: qué es y para qué se usa
- Learn Apps365: versión de Office vía planes Office 365; instalada en local, no web; 32/64 bits, Arm sin 32 bits; mismas directivas de grupo (tema 6). Project y Visio no incluidos.
- Frente a Office sin suscripción: actualiza con frecuencia (mensual); un único paquete; Hacer clic y ejecutar; Office CDN; instala administrador local.
- Licencia: 5 equipos, 5 tabletas, 5 teléfonos. Conectar ≥1 vez cada 30 días; si no, funcionalidad reducida (abrir y ver).
- Learn canales: actual (≥1/mes, sin programación); mensual para empresas (1/mes, segundo martes); empresarial semestral (cargas críticas; características enero y julio, segundo martes; actualizaciones 1/mes).
- Desde julio 2026: semestral con actualizaciones mensuales como el mensual; versiones de características admitidas 1 mes.
- Learn Office 2019: ciclo fijo, fin 15-10-2025. Teams clásico: fin de soporte 01-07-2024, de disponibilidad 01-07-2025.
- Learn Teams-SharePoint: Teams = chat; SharePoint = sitios, contenido, archivos; equipo ligado a sitio(s) SharePoint; membresía en grupo M365; Entra ID = directorio (exige MFA).
- Crear equipo crea: grupo M365; sitio y biblioteca SharePoint; buzón y calendario compartidos Exchange Online; bloc OneNote.
- Grupo M365: propietarios (añaden/quitan), miembros (sin cambiar configuración; invitan por defecto), invitados. Cualquiera crea grupos salvo limitación (entonces no sitios SharePoint, Teams, bibliotecas compartidas).
- Soporte usos: Teams = proyectos, público/privado; SharePoint = equipo/grupo/organización, permisos, externos; OneDrive = individual y de equipo, privado hasta compartir.
- Oficio: borrador en OneDrive; equipo en canal Teams; organización en sitio SharePoint.

## 2. Métodos de compartición de información
- Soporte: vínculos en lugar de adjuntos (OneDrive/SharePoint). Permisos: Puede editar, Puede revisar, Puede ver, No se puede descargar; Copiar vínculo.
- Learn vínculos:
  - Cualquiera: sin autenticar, sin auditoría; revocable y transferible.
  - Personas de su organización: sólo miembros (no invitados); revocable y transferible.
  - Personas específicas: autenticarse como el indicado, dentro o fuera; revocable, NO transferible; aparece en búsqueda.
- Cualquiera: transferible (reenvío), revocable (eliminarlo), secreto.
- Cualquiera no vale en canal compartido (sólo Personas específicas a miembros).
- Vínculo de organización: no da acceso a toda la organización; se canjea al abrirlo; por web, Outlook o chat Teams, canje automático hasta 100; no con grupos ni canales Teams.
- Learn planear (2023-04-07): externo = Entra B2B, habilitado por defecto. Cuatro niveles (más a menos abierto): Cualquiera (sin inicio de sesión); Invitados nuevos y existentes (inicio de sesión o código); Invitados existentes; Solo personas de la organización.
- Sitio nunca más permisivo que la organización; OneDrive nunca más que SharePoint.
- Restricciones: dominios, grupo de seguridad, caducidad de invitado, reautenticación con código, vínculo predeterminado, edición, caducidad de Cualquiera.
- Canal estándar: Cualquiera y Personas específicas hacia fuera si invitados habilitados; canal compartido: sin ajenos no miembros.

## 3. Trabajo en equipo con OneDrive, Teams y SharePoint
- Learn Archivos a petición: por defecto desde compilación 23.066. Estados (`attrib`):
  - Solo en línea: Sin anclar; `+u`; sin espacio, sin conexión no abre.
  - Disponible localmente: Clearpin; `-p`; Liberar espacio lo devuelve.
  - Siempre disponible: Fijado; `+p`; Mantener siempre.
- Orden: de solo en línea a local, antes siempre disponible. Si falta la opción: servicio «Controlador de filtro de archivos en la nube de Windows», `Start` = 2, `HKLM\SYSTEM\CurrentControlSet\Services\CldFlt`.
- Learn carpetas conocidas: escritorio, documentos, imágenes, capturas, rollo de cámara; copia en la nube y acceso multidispositivo. Directiva de grupo, Intune o Registro; preguntar o mover silenciosamente. No con OneDrive en SharePoint Server.
- Soporte restaurar: papelera Windows (no solo en línea ni nube); papelera web 93 días (profesional, salvo cambio) o 30 (personal); Restaurar OneDrive últimos 30 días (Configuración>Restaurar OneDrive; lo posterior va a papelera). Borrado permanente de papelera: irrecuperable.
- SharePoint: usuarios crean sitios de equipo, de comunicación, bibliotecas compartidas OneDrive. Versiones: límites por organización, sitio, biblioteca o cuenta; herencia interrumpible; Word exige OneDrive o SharePoint.
- Equipos: público hasta 10 000 miembros; todos crean. Roles: propietario (copropietarios) y miembros; externos invitados o canal compartido. General no se elimina.
- Canales: estándar (todos; carpeta en sitio común); privado (miembros del canal, sitio propio); compartido (otros equipos u organizaciones, sitio propio).
- Privado: sólo propietario del canal añade/quita; sólo miembros del equipo (invitados incluidos); ven historial; crean miembros o propietario, no invitados; configurable.
- Compartido: sólo propietarios del equipo crean; sólo propietario añade/quita (varios); invitados Entra no, externos por conexión directa B2B; no convertible; restaurable 30 días (equipos eliminados igual).
- Soporte almacenamiento: canal = SharePoint; chat = OneDrive del remitente, sólo la conversación; sin OneDrive personal. Pestaña Archivos: estándar carpeta del sitio primario; privado/compartido biblioteca de su sitio. Permisos del equipo sincronizados; administrar por Teams.
- Mensajes: hilo; @ persona/canal/equipo; anuncio sólo canales; importante = Establecer opciones de entrega; moderadores.
- Presencia: Disponible, Ocupado, No molestar, Ahora vuelvo, Ausente, Sin conexión; Disponible pasa a Ausente al bloquear/inactividad/suspensión; Ocupado con notificaciones; No molestar sin.
- Reunión: roles coorganizador, moderador, asistente; organizador no cambia; coorganizadores no cambian antes del inicio. Compartir pantalla, ventana, PowerPoint, Excel, pizarra; Ceder el control.
- Eventos en directo retirados 30-06-2026 (programados antes: soporte hasta 28-02-2027); eventos de Teams: 1000 con micro/cámara; 10 000 sólo vista con Q&A; 100 000 con complemento. Gran audiencia: activable hasta 1000; obligatoria >1000.

## 4. Word, Excel, PowerPoint y Outlook
- Word: tabla de contenido sobre títulos (faltan por formato), Referencias>tabla de contenido, Actualizar campo; manual no se actualiza. Saltos de sección: Página siguiente, Continuo, Página par o impar.
- Listas: «1.»+espacio numerada; «*»+espacio viñetas.
- Combinar correspondencia: documento principal + campos; orígenes Excel y contactos Outlook; correos con dirección única en Para.
- Control de cambios (Revisar): tachado = eliminación, subrayado = adición; Para todos/Solo míos; vistas Revisión simple (línea roja), Todas las marcas, Sin marcado, El original. Ocultar no quita: Aceptar/Rechazar. Bloqueo con contraseña (Proteger documento): no se desactiva ni se acepta. Comentarios aparte.
- Atajos Word: Ctrl+B Navegación; Ctrl+H reemplazar; Ctrl+G Ir a; Ctrl+Entrar salto de página; Ctrl+N negrita; F7 ortografía.
- Excel: 1.048.576 filas × 16.384 columnas. Relativa por defecto; copiada 2 abajo y 2 derecha: `$A$1`→`$A$1`; `A$1`→`C$1`; `$A1`→`$A3`; `A1`→`C3`. F4 alterna.
- `CONTAR`: números, no vacías/lógicos/texto/errores; `CONTARA`: no vacías, con errores y "". `SUMAR.SI(B2:B5;"Juan";C2:C5)` suma C. Varios criterios: SUMAR.SI.CONJUNTO, CONTAR.SI.CONJUNTO. `PROMEDIO` ignora texto/lógicos/vacías, incluye ceros. SUMA, SI, CONTAR.SI, MAX, MIN, `HOY()` sin argumentos.
- BUSCARV: valor buscado a la izquierda; BUSCARX: cualquier dirección, exacta por defecto, no en Excel 2016/2019.
- Errores: `#¡DIV/0!` divide por cero/vacía; `#¡REF!` celdas eliminadas o pegadas encima; `#N/A` no encuentra (BUSCARX, BUSCARV, BUSCARH, BUSCAR, COINCIDIR); `#¡VALOR!` tipo incorrecto (oficio). `=SI.ERROR(FORMULA();0)`.
- Validación de datos: restringe valores, lista desplegable. Tabla dinámica: Insertar>tabla dinámica; origen con una fila de encabezado; no numéricos a Filas, fecha a Columnas, numéricos a Valores (SUM por defecto); actualizar si cambia origen.
- PowerPoint: vistas Normal, Clasificador, Notas, Esquema (sólo texto), Presentación, Moderador. Patrón: cambios se reflejan en todas las diapositivas; cada tema trae patrón y diseños.
- Animación: un elemento, varias por diapositiva (entrada, salida, énfasis, trayectorias). Transición: al cambiar de diapositiva, una sola. Transformación = transición con aspecto de animación.
- Outlook: clásico con Archivo, nuevo sin. Reglas: nombre, condición, acción (+excepciones); Stop processing more rules; nuevo sin reglas para Gmail/Yahoo/iCloud.
- Respuestas automáticas: una vez por remitente; clásico Archivo>Respuestas automáticas; nuevo Ver>Ver configuración>Cuentas; sin período, desactivar a mano; no con Gmail, Yahoo, POP/IMAP (regla con Outlook abierto).
- Calendario: Puede ver cuando estoy ocupado; títulos y ubicaciones; todos los detalles; ninguno edita (delegación). Atenuado = directiva; añadir ajeno sólo cuentas profesionales o educativas.
- .pst: mensajes, contactos, citas, tareas, notas, diario; nuevo Outlook requiere clásico para abrirlo.
- Atajos clásico: Ctrl+F reenviar; Ctrl+R responder; Ctrl+Mayús+R todos; Ctrl+Mayús+M nuevo; Alt+S enviar; Ctrl+E/F3 buscar; Ctrl+M/F9 comprobar; Ctrl+2 Calendario. Nuevo: Ctrl+F reenviar; Ctrl+Entrar enviar; Ctrl+N nuevo; Ctrl+D responder.

## 5. Configuración del cliente de correo electrónico
- Clásico: Archivo>Agregar cuenta, dirección, Conectar. Nuevo: Vista>Configuración de vista (o Archivo>Información de la cuenta), Cuentas>Sus cuentas, Agregar cuenta, Continuar.
- Learn Detección automática: usuario y contraseña; SCP (AD, tema 8) para equipos del dominio; `https://autodiscover.<smtp-address-domain>/autodiscover/autodiscover.xml`.
- Manual (clásico): Opciones avanzadas>«Permíteme configurar mi cuenta manualmente»>Conectar; normalmente IMAP.
- Learn POP3/IMAP4 (2023-10-31), Exchange Online: POP3 Outlook.office365.com 995 SSL/TLS; IMAP4 Outlook.office365.com 993 SSL/TLS; SMTP Smtp.office365.com 587 STARTTLS. POP/IMAP envían por SMTP.
- Outlook.com: salida smtp-mail.outlook.com 587 STARTTLS; POP/IMAP deshabilitado por defecto; OAuth2.
- Exchange Online: POP3/IMAP4 habilitados; valores predeterminados de seguridad los deshabilitan; sin calendario ni contactos.
- POP3: quita del servidor (configurable), una carpeta local. IMAP4: no quita, varias carpetas, varios equipos.
- Básica (usuario y contraseña en cada solicitud): deshabilitada en todos los inquilinos; rehabilitable hasta 31-12-2022, ya no. SMTP AUTH aún disponible, retirada anunciada.
- Moderna: tokens OAuth 2.0 (vida limitada, no reutilizables), facilita MFA. OAuth para POP/IMAP/SMTP desde 2020; Outlook sin plan para POP/IMAP: usa MAPI/HTTP (Windows) y EWS (Mac).
- Contraseñas de aplicación: un solo uso; IMAP/iCloud; en Exchange Online no sirven sin verificación en dos pasos.
- Quitar cuenta: no la desactiva, sólo contenido local; si es la única, nueva ubicación de datos.

## 6. Funcionalidades e integración con las herramientas colaborativas
- Coautoría: tiempo real con archivo en la nube y suscripción; si no, guardar de vez en cuando. Autoguardado. Deshacer/Rehacer pueden fallar; en Excel ordenar/filtrar cambia la vista de todos; .docm editable.
- Teams en Outlook: integrado en el nuevo, complemento en otros; sin cuenta personal ni POP/IMAP (@gmail.com, @yahoo.com, @icloud.com); exige cuenta de trabajo Exchange.
- Teams: botón OneDrive; Adjuntar archivo (canal SharePoint, chat OneDrive); OneDrive comentarios con @nombre.
- Integración: combinar correspondencia desde Word por correo; tabla dinámica con origen externo; guardar en nube activa coautoría y versiones.
- Casos: archivo por chat no está en canal (OneDrive del remitente); externo = Personas específicas con Puede ver; portátil lleno: Liberar espacio `+u`; borrado: papelera 93 días, ransomware Restaurar OneDrive 30 días; cliente antiguo: básica desactivada, OAuth 2.0, IMAP 993/587; >1000 asistentes = evento solo vista.

## Lo que este tema no da
- Versión y licencias en RTVA/CSRTV; cuota de OneDrive y límites de archivo; administración M365; capacidades por rol en reuniones; .ost; atajos duplicados de Word; Comparar y combinar; OneNote, Planner, Loop, Copilot.
