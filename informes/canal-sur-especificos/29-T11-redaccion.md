# Puesto 29 · Tema 11 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación y en los temas 5 a 10). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/11-herramientas-colaborativas-y-ofimatica-microsoft-365.md`.
Material: `29-investigacion-C-datos-redes-seguridad.md` (§ Tema 11). Fila de
`informes/canal-sur-reuso/informatica.tsv`: RTVE `gestion-administrativa/11` y `/12`, 45 %,
«actualizar: sí».

## Avance

- Fuentes descargadas (páginas de Microsoft Learn y del soporte de Microsoft, prefijo `m-`).
- Ficha, siglas, enunciado, «qué se puede preguntar» y epígrafe 1 (Microsoft 365: Aplicaciones frente a Office sin suscripción, canales, Office 2019 y Teams clásico, piezas, usos) guardados. Literalidad: 64 citas en negrita, todas halladas.
- Epígrafe 2 (compartición: vínculos frente a adjuntos, tres tipos de vínculo, cuatro niveles de uso compartido externo, restricciones, Teams) guardado. Literalidad: 106 citas acumuladas, todas halladas.
- Epígrafe 3 (OneDrive: Archivos a petición, carpetas conocidas, recuperación; SharePoint: sitios, bibliotecas, versiones; Teams: equipos, canales y permisos, dónde van los archivos, mensajes, chats y estado, reuniones y eventos) guardado. Primera pasada: 13 negritas de RTVE que no eran cita (rótulos y énfasis), pasadas a cursiva o redonda. Literalidad: 201 citas acumuladas, todas halladas.
- Epígrafe 4 (Word, Excel, PowerPoint y Outlook) guardado. Literalidad: 292 citas acumuladas, todas halladas.
- Epígrafe 5 (cliente de correo: alta automática y detección automática, configuración manual, servidores y puertos de Exchange Online, POP frente a IMAP, autenticación básica y moderna, quitar cuenta) guardado. Fila .ost suprimida (sin fuente leída). Literalidad: 345 citas acumuladas, todas halladas.
- Epígrafe 6 (coautoría y Autoguardado, Teams en Outlook, archivos de Office en Teams/OneDrive/SharePoint, integración entre aplicaciones, caso práctico de seis supuestos), «Lo que este tema no da» y «Trazabilidad» guardados. Índice generado con `indice.py` (38 epígrafes; ficha escrita a mano, el tema no está en `portadas.tsv`). Literalidad final: 365 citas en negrita, 0 no halladas. `refutar_prosa.py`: 4 siglas sin presentar (AUTH, GB, ID, SUM), presentadas; quitadas de la lista de siglas seis que el tema no usaba (TI, EWS, AD DS, LDAP, MAPI, IU); 0 hallazgos. Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Fuentes leídas y fecha

Todas el 05-10-2026, descargadas como texto con URL y fecha en cabecera en
`fuentes/canal-sur/informatico/web/` (nuevas, prefijo `m-`): de Microsoft Learn
`m-m365apps`, `m-channels365`, `m-o2019life`, `m-teamsclassic`, `m-tsp`, `m-teamsov`, `m-chov`,
`m-privch`, `m-sharedch`, `m-groups`, `m-live`, `m-townhall`, `m-links`, `m-collab`, `m-fod`,
`m-kfm`, `m-spintro`, `m-versions`, `m-popimap`, `m-autod`, `m-basicauth`; del soporte de Microsoft
`m-collabtso`, `m-worktog`, `m-teamsfiles`, `m-sharefiles`, `m-odfod`, `m-odrestore`,
`m-odrestoreall`, `m-important`, `m-announce`, `m-status`, `m-roles`, `m-present`, `m-toc`,
`m-sections`, `m-bullets`, `m-merge`, `m-wordkeys`, `m-xlrefs`, `m-xllimits`, `m-vlookup`,
`m-xlookup`, `m-na`, `m-ref`, `m-div0` (inglés) y `m-div0es`, `m-valid`, `m-pivot`, `m-pptviews`,
`m-master`, `m-anim`, `m-olkeys`, `m-rules` (redirigida al inglés), `m-pstost`, `m-addacct`,
`m-olcom`, `m-coauth`, `m-versioning`, `m-addin` (redirigida al inglés). Descargas fallidas, que no
se usan: `m-newoutlook` y `m-syncov` (44 palabras, sólo el aviso de autorización).

Comprobación de literalidad por script (`scratchpad/t11check.py`, el de T10 con las fuentes `m-*`,
tolerante sólo a la mayúscula o minúscula inicial de la cita): 365 citas en negrita, 0 no halladas.

## Qué se hizo

Seis epígrafes en el orden del enunciado: 1 Microsoft 365 y sus usos (Aplicaciones Microsoft 365
frente a Office sin suscripción, canales de actualización, por qué no Office 2019 ni Teams clásico,
piezas —Teams, SharePoint, equipo, grupo, Entra ID—, qué herramienta para qué); 2 métodos de
compartición (vínculos frente a adjuntos, tres tipos de vínculo, cuatro niveles externos,
restricciones); 3 trabajo en equipo con OneDrive (Archivos a petición con `attrib`, carpetas
conocidas, tres escalones de recuperación), SharePoint (sitios, bibliotecas, versiones) y Teams
(equipos, canales, permisos, dónde van los archivos, mensajes, presencia, reuniones y eventos); 4
Word, Excel, PowerPoint y Outlook; 5 configuración del cliente de correo (alta automática, detección
automática, configuración manual, tabla de Exchange Online, POP frente a IMAP, autenticación básica y
moderna, contraseñas de aplicación, quitar cuenta); 6 funcionalidades e integración (coautoría,
Autoguardado, Teams en Outlook, archivos de Office en Teams, caso práctico).

Decisiones y salvedades (manda la fuente):

- Versiones: no se estudia Office 2019 (fin de soporte ampliado 15-10-2025, hora del Pacífico) ni el
  Teams clásico (no disponible desde 01-07-2025). Se dice en el epígrafe 1.
- Eventos en directo de Teams: **retirados el 30-06-2026** (página de Microsoft Learn). RTVE los
  daba como vigentes; el tema los da como retirados y explica los eventos que los sustituyen.
- Archivos de canal: RTVE decía que «lo que se sube a un canal queda en la biblioteca de ese canal,
  no en la del equipo entero». No cuadra con la fuente: el canal estándar es una carpeta de la
  biblioteca del sitio del equipo; sólo los privados y compartidos tienen sitio propio. Corregido.
- Roles de reunión: RTVE daba organizador, moderador y asistente; la fuente añade el coorganizador.
  Corregido.
- Atajos: RTVE decía que «en casi todas las aplicaciones Ctrl + F abre la búsqueda». En Word en
  español la página de Microsoft da **Ctrl+B** para el panel de Navegación; en Outlook clásico la
  búsqueda es Ctrl+E o F3. Corregido. La página española del nuevo Outlook da **Ctrl+D** para
  responder (se da atribuido a esa página). La tabla de «más usados» de Word en español tiene
  duplicados (Ctrl+A y Ctrl+U con dos acciones cada uno): se declara en «Lo que este tema no da».
- Canal privado: RTVE decía que se identifica por un icono de candado; no consta en la página leída.
  Quitado.
- Investigación: daba el servidor SMTP de Outlook.com (`smtp-mail.outlook.com`) y faltaban los de
  Exchange Online; se leyó la página de Exchange Online (Outlook.office365.com 995/993 SSL/TLS;
  Smtp.office365.com 587 STARTTLS) y se releyó la de Outlook.com. La frase cortada de la
  investigación sobre OneDrive y SharePoint se completó en la fuente: «la configuración de OneDrive
  no puede ser más permisiva que la configuración de SharePoint».
- Página de BUSCARV: su título en español es «Función CONSULTAV», pero el cuerpo habla de BUSCARV;
  se usa BUSCARV y se marca *sic* en la Trazabilidad.
- El .ost no se afirma (la página leída sólo trata el .pst); fila suprimida.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata Microsoft 365 ni ofimática.

## Copiado de RTVE sin cambios

Nada. Los dos temas de RTVE (`gestion-administrativa/11` y `/12`) están marcados «actualizar: sí»
en `informatica.tsv`, así que lo que se toma de ellos es **adaptado** y debe pasar la verificación
entera. Para que el verificador lo localice, lo tomado de RTVE (copiado o casi literal, sin la
negrita de énfasis de RTVE, porque aquí negrita es cita):

| Pasaje de RTVE | Dónde va | Cambio |
|---|---|---|
| `/11` § 11.1: caracteres y párrafos; estilos; secciones; listas y esquemas; tablas y objetos; plantillas; combinar correspondencia; personalización; gestión de ficheros | § 4, Word | «índice» → «tabla de contenido»; secciones y listas con cita; combinar correspondencia reescrito con la página de Microsoft |
| `/11` § 11.2: libros, hojas y celdas; referencias; fórmulas y funciones; errores; gestión y análisis | § 4, Excel | referencias con la tabla de Microsoft y F4; errores con cita; quitado `#¡VALOR!` como cita (va como oficio); quitada la remisión al «punto 30 del temario de Gestión» |
| `/11` § 11.3: vistas, patrón, objetos, multimedia, animación frente a transición | § 4, PowerPoint | vistas y patrón con cita; tabla de animación y transición nueva |
| `/11` § 11.4: entorno, responder y reenviar, reglas, libreta, tabla de atajos y «la trampa» | § 4, Outlook | tabla de atajos releída (Outlook clásico); «la trampa» corregida (ver arriba) |
| `/12` § 1: equipo, canal, pestañas | § 3, Teams | «Cada canal tiene su propia carpeta…» corregido |
| `/12` § 2: tabla de tipos de canal, tres citas de canales privados (releídas: literales en `m-privch`), «Tres consecuencias…» | § 3, Tipos de canal | tabla con columna de almacenamiento; quitado el candado |
| `/12` § 3: publicación, menciones, anuncio, formato | § 3, Mensajes | anuncio e importante con cita; quitado «emojis, reacciones» |
| `/12` § 4: chat, llamadas, estado | § 3, Chats | estado con cita; «almacenamiento personal» → «OneDrive para la Empresa» |
| `/12` § 5: reunión, evento en directo, compartir pantalla, compartir documentos | § 3, Reuniones; § 6 | roles con coorganizador; eventos en directo retirados; ceder el control con cita |

Quitado por propio de RTVE: versión 1.6.00.376 y «Office Profesional Plus 2019» como versión de
estudio, los epígrafes «Los datos que el examen ha preguntado», los números de pregunta, el
cuadernillo `23_preguntas_gea`, la remisión al punto 30 de Gestión y la Trazabilidad de RTVE.

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/m-*.txt` (nuevos). Ningún fichero existente modificado.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; (AP) = aplicación práctica. Todas se contestan enteras
con el tema; no ha hecho falta ampliarlo después de escribirlas.

1. (Usos) Con una sola licencia, Aplicaciones Microsoft 365 se puede instalar: a) en un equipo; b) en
   hasta cinco equipos, y además en cinco tabletas y cinco teléfonos; c) en equipos ilimitados si
   están en el dominio; d) sólo en la versión web. → **b**; y si no se conecta en 30 días pasa a
   funcionalidad reducida. § 1. Entera.
2. (Métodos de compartición) El vínculo que concede acceso sin autenticarse y cuyos accesos no se
   pueden auditar es: a) Personas específicas; b) Personas de su organización; c) Cualquiera; d)
   ninguno. → **c**. § 2. Entera.
3. (Compartición, AP) El administrador fija SharePoint en «Invitados existentes». ¿Puede dejar
   OneDrive en «Cualquiera»? a) Sí, son independientes; b) no: OneDrive no puede ser más permisivo
   que SharePoint; c) sí, si lo pide el propietario del sitio; d) sólo para carpetas. → **b**. § 2.
   Entera.
4. (OneDrive, AP) Para que una carpeta sincronizada esté siempre disponible sin conexión se usa: a)
   `attrib +u`; b) `attrib -p`; c) `attrib +p`; d) `attrib +h`. → **c** (Fijado). § 3, OneDrive.
   Entera.
5. (Teams, AP) Un archivo enviado en un chat de Teams se guarda en: a) la carpeta del canal General;
   b) el sitio de SharePoint del equipo; c) el OneDrive para la Empresa de quien lo envía, compartido
   sólo con los del chat; d) el OneDrive personal del destinatario. → **c**. § 3. Entera.
6. (Teams/SharePoint) Sobre los canales: a) todos tienen su propio sitio de SharePoint; b) los
   estándar comparten el sitio del equipo, con una carpeta por canal, y privados y compartidos tienen
   sitio propio; c) sólo los compartidos tienen sitio; d) los privados guardan en OneDrive. → **b**;
   y el compartido sólo lo crean los propietarios del equipo. § 3. Entera.
7. (Word y Excel) Se copia una fórmula con `A$1` dos celdas hacia abajo y dos hacia la derecha: a)
   `A$1`; b) `C$1`; c) `$A3`; d) `C3`. → **b**; F4 alterna los tipos. § 4, Excel. Entera. (Y en
   Word, el salto de sección que permite cambiar el número de columnas en la misma página es el
   Continuo: § 4, Word.)
8. (PowerPoint y Outlook) ¿Cuál es correcta? a) Una diapositiva puede tener varias transiciones; b)
   en el Outlook clásico Ctrl+F busca; c) una diapositiva admite una sola transición y varias
   animaciones, y en el Outlook clásico Ctrl+F reenvía; d) el patrón de diapositivas sólo afecta a la
   primera. → **c**. § 4. Entera.
9. (Configuración del cliente de correo, AP) Configuración IMAP de un buzón de Exchange Online: a)
   outlook.office365.com, 993, SSL/TLS, y salida smtp.office365.com, 587, STARTTLS; b) 143 sin
   cifrar; c) 995 para IMAP; d) basta autenticación básica. → **a**; la autenticación básica está
   deshabilitada en todos los inquilinos. § 5. Entera.
10. (Funcionalidades e integración) Para coautoría en tiempo real en Word hace falta: a) enviar el
    archivo adjunto; b) guardarlo en OneDrive o SharePoint y usar una versión con suscripción a
    Microsoft 365; c) Office 2019 con macros; d) una cuenta POP. → **b**; y para programar reuniones
    de Teams desde Outlook, las cuentas POP/IMAP no sirven. § 6. Entera.
