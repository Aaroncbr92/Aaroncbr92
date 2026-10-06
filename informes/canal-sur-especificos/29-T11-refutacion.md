# Puesto 29 · Tema 11 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/11-herramientas-colaborativas-y-ofimatica-microsoft-365.md`
(1.019 líneas, 11.614 palabras de cuerpo).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios»: nada (lo tomado de RTVE está adaptado,
  según `29-T11-redaccion.md`). Exactitud sobre todo el tema, por muestreo, centrada en lo que la
  verificación no listó como confirmado y en la redonda.
- Fuentes: los volcados `fuentes/canal-sur/informatico/web/m-*.txt` (descargados el 05-10-2026),
  releídos el **06-10-2026** en los pasajes concretos. Nada descargado de nuevo.
- Lentes (tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` sobre una copia en el
  scratchpad: 38 epígrafes, índice idéntico al del tema. No proceden `negritas.py`,
  `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto: tabla de Archivos a petición (estado, atributo y orden:
Fijado `+p`, Clearpin `-p`, Sin anclar `+u`, `m-fod`), icono de nube azul y círculo verde con marca
blanca, compilación 23.066 (`m-odfod`); clave `CldFlt` `Start`=2; Configuración>Restaurar OneDrive y
30 días (`m-odrestoreall`); «pestaña Compartido» de los archivos de canal y chat (`m-teamsfiles`);
equipos públicos hasta 10 000 miembros, @mención del equipo o canal como ajuste del propietario,
moderación (`m-chov`); estados de presencia, «Ahora vuelvo»/«Vuelvo en seguida» y sus definiciones
(`m-status`); 1000 / 10 000 solo vista con Q&A / 100 000 con complemento, Optimizar para gran
audiencia (activable hasta 1000, forzosa por encima) y su efecto, base del caso práctico 6
(`m-townhall`); atajos de Word en español (Ctrl+B navegación, Ctrl+H Reemplazar, Ctrl+G, Ctrl+Entrar,
Ctrl+N, F7, `m-wordkeys`); atajos del Outlook clásico de la tabla «más usados» (Ctrl+Mayús+M, Alt+S,
Ctrl+E o F3, Ctrl+R, Ctrl+F, Ctrl+Mayús+R, Ctrl+2, Ctrl+M o F9) y del nuevo (Ctrl+N, Ctrl+F, Ctrl+D,
Ctrl+Entrar), cada uno en la pestaña que el tema dice (`m-olkeys`); tres vínculos y sus propiedades
(`m-links`); Outlook.com: POP/IMAP deshabilitado por defecto, OAuth2, `smtp-mail.outlook.com`
(`m-olcom`); 1.048.576 × 16.384 (`m-xllimits`).

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué pasa | Propuesta |
|---|---|---|---|---|---|
| M1 | Menor | 5 sigla sin presentar | Siglas: «MAPI … que Outlook usa sobre HTTP» y ep. 5 «MAPI/HTTP» | HTTP aparece sin desarrollar (sólo se remite al tema 13 en «Lo que este tema no da»). `refutar_prosa.py` no lo detecta porque aparece dentro de la línea de siglas | Presentarlo en la línea de siglas: protocolo de transferencia de hipertexto (HTTP) |

Sin hallazgo en: cita cruzada (1; remisiones a los temas 6, 8, 13 y 14 coherentes con el temario),
ley por reglamento (2, no aplica), recuentos (3: tres canales, tres vínculos, cuatro niveles, tres
escalones, cuatro filas de referencias), «podrá»/«deberá» (4), salvedades (6), redacción superada (7:
Office 2019, Teams clásico, eventos en directo y canal semestral, con fecha), artículo mal (8),
afirmación sin fuente (9: lo que es oficio va declarado como oficio).

## Lente 2 · Cobertura

Las seis rúbricas del enunciado tienen epígrafe propio y en su orden. Quince preguntas en
`29-T11-preguntas.md`: **12 enteras, 1 a medias (11), 2 no (10, 14)**.

| # | Laguna | Rúbrica | Propuesta |
|---|---|---|---|
| L1 | Control de cambios y comentarios de Word (Revisar > Control de cambios, aceptar/rechazar, comparar documentos). Es materia típica de test de Word y del trabajo en equipo sobre un mismo documento | Word; funcionalidades e integración | Leer la página del soporte de Microsoft «Realizar un seguimiento de los cambios en Word» y añadir un párrafo en Word (y una línea en coautoría) |
| L2 | Respuestas automáticas (fuera de la oficina) y uso compartido del calendario / delegación en Outlook: el tema da reglas, atajos y .pst, pero no estas dos funciones de soporte diario | Outlook; integración | Leer «Enviar respuestas automáticas (fuera de la oficina) desde Outlook» y «Compartir un calendario de Outlook» y añadir dos viñetas en Outlook |
| L3 | Qué hace cada función habitual de Excel: el tema lista `SUMA`, `CONTAR`, `CONTARA`, `SI`, `SUMAR.SI`, `CONTAR.SI`… sólo por el nombre, como oficio | Excel | Una tabla breve función/qué hace/ejemplo, con la página de cada función del soporte de Microsoft |

## Recuento

Graves: 0. Menores: 1 (M1). Lagunas: 3 (L1-L3).

## Otros ficheros tocados

Ninguno, salvo este informe y `29-T11-preguntas.md`. Copia del tema para `indice.py`, en el
scratchpad de la sesión (fuera del proyecto).
