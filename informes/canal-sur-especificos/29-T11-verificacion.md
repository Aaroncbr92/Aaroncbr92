# Puesto 29 · Tema 11 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus volcados
de `fuentes/canal-sur/informatico/web/` (`m-*.txt`), descargados el 05-10-2026 con URL y fecha en
cabecera; no se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/11-herramientas-colaborativas-y-ofimatica-microsoft-365.md`.

## Método

- Copiado del común: nada. Copiado de RTVE sin cambios: nada (según `29-T11-redaccion.md`: lo
  tomado de RTVE `gestion-administrativa/11` y `/12` está adaptado). No hubo nada que comprobar
  sólo por diff; se verificó todo el tema.
- Cada una de las 365 negritas se buscó **en la fuente a la que el tema la atribuye** (script que dice
  en qué fichero aparece cada cita): 365 halladas, todas en la página que el tema o la Trazabilidad
  señalan. Se leyó cada página en el pasaje citado y alrededor, para el contexto, las salvedades y lo
  dicho en redonda. Con los nueve errores delante.
- Lentes (ENCARGO, tema técnico sin norma): `refutar_prosa.py` 1 hallazgo tras las correcciones
  (MAPI sin presentar; corregido) y 0 al final; `indice.py` 38 epígrafes, el índice no cambia. No
  proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. Literalidad final: 374 citas,
  0 no halladas.

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 7 redacción superada / 6 | § 1, canales de actualización | El canal semestral se daba con novedades «dos veces al año (enero y julio)», sin el aviso de la misma página: desde julio de 2026 recibe actualizaciones de características mensuales y cada versión se admite un mes | Añadido el aviso con tres citas literales, y que el ritmo semestral es el anterior al cambio |
| 2 | 6 | § 1, tabla de canales | «Equipos que requieren pruebas exhaustivas»: la página dice dispositivos no interactivos o con cargas especializadas o críticas | Precisado en redonda |
| 3 | 9 | § 1, Office 2019 | «Desde entonces no recibe actualizaciones»: la página de ciclo de vida sólo da fechas | «Desde entonces está fuera de soporte» |
| 4 | 6 | § 2, vínculo de la organización | El canje automático hasta 100 sin su salvedad: no vale con destinatarios de grupo ni con mensajes de canal de Teams | Añadida la cita |
| 5 | 6 | § 3, canal compartido | «solo el propietario puede agregar o quitar»: la página admite más de un propietario | Añadido |
| 6 | 9 | § 3, mensajes | «Importante o urgente»: «urgente» sólo está en la URL; el cuerpo de la página sólo trata «Importante» | «Importante» |
| 7 | 9 | § 3, eventos | «Los eventos en directo ya no existen», cuando la cita que sigue da soporte hasta el 28-02-2027 a los programados antes del 30-06-2026 | «están retirados» |
| 8 | 6 / 3 | § 3, eventos | «Por encima de mil se activa Optimizar…»: hasta mil está desactivada pero se puede activar; por encima, activada y no se puede desactivar. Faltaba «levantar la mano» en la lista de capacidades | Añadidos los dos |
| 9 | 9 | § 4, Excel | «Microsoft recomienda ya BUSCARX»: la página dice «Pruebe a usar» | «Microsoft invita a probar» |
| 10 | 6 | § 4, Outlook, «la trampa» | «en Outlook la búsqueda va con Ctrl+E o F3»: eso es del clásico; Ctrl+F reenvía en los dos | Precisado |
| 11 | 6 | § 5, autenticación | Faltaba que la autenticación SMTP ya está deshabilitada en los inquilinos que no la usaban | Añadida la cita |
| 12 | 6 | § 5, autenticación | Se describía la configuración manual IMAP de Outlook clásico junto a la tabla de Exchange Online sin decir que Outlook no admite OAuth para POP/IMAP (se conecta por MAPI/HTTP o EWS), ni que Exchange Online admite OAuth para POP, IMAP y SMTP desde 2020 | Añadido con dos citas |
| 13 | 6 | § 5, contraseñas de aplicación | Omitía que en Exchange Online el desuso de la autenticación básica impide las contraseñas de aplicación con apps sin verificación en dos pasos | Añadido |
| 14 | 9 | § 6, Teams | «el moderador puede tomar el control … si su rol lo permite»: la tabla de roles va con iconos ilegibles; no consta qué rol lo tiene | Reescrito: es una capacidad de la tabla; qué rol la tiene no se pudo leer |
| 15 | 5 | Siglas | MAPI y EWS sin presentar (los traen las correcciones 12) | Presentadas |
| 16 | — | Trazabilidad | Faltaban fechas de actualización y lo que sostienen las citas nuevas | Añadidas: Aplicaciones Microsoft 365 2025-05-20, canales 2026-05-27, POP3 e IMAP4 2023-10-31; filas de canales, eventos y autenticación ampliadas |

## Confirmado sin cambios (muestra de lo que se comprobó en redonda)

Cinco equipos, cinco tabletas y cinco teléfonos; 30 días; Arm sin 32 bits; Hacer clic y ejecutar y
CDN; fechas de Office 2019 (10/15/2025 6:59:59 AM, hora del Pacífico) y del Teams clásico
(01-07-2024 y 01-07-2025); las cuatro cosas que se crean con un equipo; roles del grupo y lo que no
se puede crear si se limita; tabla de usos del soporte; tres vínculos y sus propiedades; cuatro
niveles externos y las dos reglas de jerarquía; estados de Archivos a petición, atributos, órdenes
`attrib`, iconos y clave `CldFlt` `Start`=2; compilación 23.066; carpetas conocidas; papeleras 93 y
30 días y Restaurar OneDrive 30 días; límites de versiones por niveles; 10 000 miembros; roles del
equipo; canal General; reparto de archivos por tipo de canal y de chat; canales privados y
compartidos (creación, miembros, B2B, no conversión, 30 días); estados de presencia; roles de
reunión; retirada de eventos en directo; 1000/10 000/100 000 asistentes; atajos de Word, de Outlook
clásico y del nuevo Outlook (incluida la tabla «más usados» de cada uno); tabla de referencias y F4
(la página escribe «columna mixta» para `$A1`; el tema dice «absoluta» en redonda, que es lo
correcto); 1.048.576 × 16.384; errores y SI.ERROR; tabla dinámica; vistas, patrón y animación frente
a transición; reglas (inglés); .pst; alta de cuenta en los dos Outlook; detección automática y SCP;
tabla de servidores, puertos y cifrado de Exchange Online y de Outlook.com; POP frente a IMAP;
autenticación básica deshabilitada sin vuelta atrás; quitar cuenta; coautoría, .docm, Deshacer y
ordenación en Excel; Teams en Outlook y sus límites (inglés).

## Lo que no se pudo confirmar

Nada nuevo quitado: lo que no tenía apoyo se reescribió (hallazgos 3, 6, 7, 9 y 14). Siguen como
oficio declarado, sin presentarse como cita: los descriptores de Word, Excel y PowerPoint tomados de
RTVE (caracteres y párrafos, plantillas, funciones habituales, `#¡VALOR!`, gráficos, macros,
protección, objetos y multimedia), «sala de espera, grabación y transcripción» en la reunión, la
regla de dónde guardar cada archivo, sitio de equipo frente a sitio de comunicación, los apartados
de integración sin cita y el caso práctico. Todo ello ya figura como oficio en «Lo que este tema no
da» o en la Trazabilidad.

## Pasajes cambiados

Los 16 de la tabla (unas 70 líneas del diff). Releídos: «Esa tabla», «la misma página», «Con ella
activada», «Y la autenticación SMTP», «del apartado anterior» tienen su antecedente delante. El caso
práctico 5 (cliente de terceros por IMAP con OAuth) sigue siendo coherente con la corrección 12.
Extensión: 11.611 palabras de cuerpo (`indice.py`), cerca de las 11.000 aproximadas de la ficha.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe. Copia del tema antes de verificar y scripts de comprobación,
en el scratchpad de la sesión (fuera del proyecto).
