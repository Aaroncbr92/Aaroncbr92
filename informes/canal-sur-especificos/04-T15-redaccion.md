# 04 · Ayudante de Producción · Tema 15 · Redacción (fase 2)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/15-herramientas-ofimaticas-y-aplicaciones-de-gestion.md`
(9.802 palabras de cuerpo; 41 epígrafes; índice generado con `indice.py`; `refutar_prosa.py`: 1
hallazgo, falso positivo: «BUSCAR» es nombre de función de Excel, no sigla). Fecha de corte:
24-09-2026. Lecturas propias de esta fase: 06-10-2026 (fecha del sistema). Material:
`04-investigacion-C-gestion-prl.md` §2; Operador/a Informático T11, T12 y T15; Redactor/a T03; RTVE
`gestion-administrativa/11`, `12` y `gestion/30`.

Ficheros tocados: el tema (nuevo) y este informe. Montado por partes en el scratchpad (cinco partes,
una por bloque de rúbricas) y ensamblado con un script que copia por número de línea los pasajes
literales, de modo que la copia es byte a byte.

**Aviso al coordinador.** El encargo daba como base sólo RTVE. Existe un tema cerrado de Canal Sur que
cubre casi todo lo que RTVE ofrecía, ya actualizado: Operador/a Informático T11 «Herramientas
colaborativas y ofimática Microsoft 365» (`29-T11-final.md`), además de T12 (bases de datos) y T15
(ENS). Por la regla 2 del encargo («reutilizar antes de escribir») se ha copiado de ahí y no de RTVE.
Los temas de RTVE tienen la fila `actualizar = sí` en `produccion-informacion.tsv` y están atados a
versiones ya fuera de soporte (Office 2019, fin de soporte ampliado 15-10-2025; Teams 1.6.00.376,
cliente clásico retirado; los «eventos en directo» de Teams que describe RTVE T12 están retirados).
Si los pasajes de Operador/a no deben contar como cerrados para este puesto, tienen que pasar por
verificación.

## Fuentes releídas hoy (06-10-2026)

- Cámara de Cuentas, fiscalización RTVA-CSRTV 2018 (`camara-cuentas-fiscalizacion-rtva-csrtv-2018-boja-36-2021.txt`):
  puntos 99, 205, 227, nota 41 y apartado 9.2.1 (Comité TIC, funciones a) a j) y presidencia).
  Coinciden con la investigación. Se añade la frase del 227 sobre falta de inversiones.
- RD 311/2022, arts. 1 y 2 (`boe.py`, redacción única, vig. 05-05-2022); Ley 40/2015, art. 2 (`boe.py`,
  redacción única, vig. 02-10-2016).
- Soporte de Microsoft (descarga con curl y paso a texto, cotejo de cada negrita con grep; no
  extracción asistida): «Conceptos básicos de las bases de datos», «Conceptos básicos del diseño de una
  base de datos», «¿Qué es el Autoguardado?», «Crear o programar una cita», «Compartir y acceder a un
  calendario con permisos de edición o delegado en Outlook», «Usar segmentaciones para filtrar datos»,
  «Filtrar datos de una tabla o un rango en Excel», «Filtrar valores únicos o quitar valores
  duplicados», «Utilice el formato condicional…», «Crear una tabla dinámica…».
- Correcciones a la investigación: la frase confusa sobre listas que señalaba §2.1 no se usa; en su
  lugar va la de la página («Muchas bases de datos comienzan como una lista…»). La de coautoría de §2.2
  ya estaba en Operador/a T11 y se copia de allí.
- **RTVE desfasado**: la cita de RTVE `gestion/30` §5.3 «las casillas de verificación de las tablas
  dinámicas en la que quiere…» ya no está en la página; se sustituye por la redacción de hoy («puede usar
  esa misma segmentación…», «Las segmentaciones solo se pueden conectar…», «Conexiones de informe»).
- Discrepancia anotada, no corregida (copiado del común): Operador/a T11 cita «Puede ver cuando estoy
  ocupado» (página de calendario de solo lectura); la página de permisos de edición/delegado dice hoy
  «Puede ver si estoy ocupado». Son páginas distintas; el tema copia la de T11 literal.

## Copiado del común

Literal de temas cerrados de Canal Sur (no se reverifica). Entre corchetes, el cambio.

De `29-operador-a-informatico/11-herramientas-colaborativas-y-ofimatica-microsoft-365.md` (líneas del original):
- 167-178 «Por qué no se estudia Office 2019 ni el Teams clásico» [se deja fuera el párrafo 180-182, que
  nombraba PowerPoint; se sustituye por un párrafo propio que nombra Word, Excel, Outlook, Teams y Access].
- 213-225 «Qué herramienta para qué: usos».
- 624-706: cuerpo de «Excel» (libros, referencias, funciones, errores, gestión y análisis de datos),
  bajo el epígrafe «Libros, hojas, fórmulas y funciones».
- 229-255 «Vínculos en lugar de adjuntos» y «Los tres tipos de vínculo» (sin los «Tres matices»).
- 460-468: cuerpo de «Dónde acaba cada archivo de Teams», bajo el título «Dónde queda lo que se
  comparte por Teams».
- 917-941 «Coautoría y Autoguardado» [quitado el párrafo 943-944, que remitía al «epígrafe 4»; se
  reescribe con «(más abajo)»].
- 578-605: el apartado de control de cambios de Word, bajo el título «El control de cambios de Word».
- 739-763 y 777-805: cuerpo de «Outlook» (entorno, responder y reenviar, reglas, respuestas
  automáticas, libreta, .pst, atajos y la trampa de Ctrl+F) [sin el bullet del calendario, que va a
  Agenda].
- 764-776: bullet «Compartir el calendario», en «Compartir la agenda: ver, editar, delegar».
- 946-958 «Teams en Outlook» (en Agenda).
- 571-577: bullet «Combinar correspondencia» (en Bases de datos).

De `29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`:
- 178-185: tabla de nombre corriente y formal (tabla/relación, fila/tupla, columna/atributo).

De `29-operador-a-informatico/15-normativa-tecnica-de-administracion-electronica-e-interoperabilidad.md`:
- La cita del artículo 1.2 del RD 311/2022 (sin la glosa sobre dimensiones, que remitía al anexo I);
  releída igualmente hoy con `boe.py`.

De `34-redactor-a/03-organizacion-redaccion-audiovisual.md`:
- 257-261: bullet del Libro de estilo 4.4 y 4.4.4, punto 6 (peticiones por escrito).

## Copiado de RTVE sin cambios

Ninguno. Los tres temas de RTVE están marcados para actualizar (`actualizar = sí`) y atados a
versiones concretas; lo útil ya estaba actualizado en Operador/a T11. Lo único tomado de RTVE es la
primera cita de la segmentación de datos (`gestion/30-excel-avanzado.md`, líneas 286-290), cotejada
hoy con la página y con el resto del párrafo reescrito: se verifica.

## Lo nuevo (pasa por verificación)

Qué herramientas usa la casa; reparto por documento (oficio); filtro, quitar duplicados, formato
condicional, segmentación; hoja de cálculo en producción; Autoguardado e historial de versiones;
documento compartido, correo y agenda en producción; citas, reuniones, avisos; edición y delegado;
bases de datos (Access: definición, tablas, registros, campos, claves, relaciones, objetos, consultas);
base de datos en producción; ERP SAP y Comité TIC; ENS art. 2.1 y Ley 40/2015 art. 2.2; pautas de
usuario; aplicación práctica (9 casos); «no da»; trazabilidad.

## Preguntas de control (10), contestadas con el tema

1. Según el Libro de estilo de Canal Sur, las peticiones a producción, salvo urgencia extrema, se
   cursan: a) de viva voz; b) por escrito, por los cauces ofimáticos habituales y con la mayor
   precisión; c) por teléfono; d) por el editor. → **b**. Entera (Herramientas, «Las peticiones a
   producción, por escrito»).
2. En Excel, al copiar la fórmula con `$A1` dos filas abajo y dos columnas a la derecha queda: a) `$A$1`;
   b) `C$1`; c) `$A3`; d) `C3`. → **c**. Entera (tabla de referencias).
3. `CONTARA` cuenta: a) sólo números; b) celdas no vacías, incluidos errores y texto vacío; c) celdas
   vacías; d) celdas que cumplen un criterio. → **b**. Entera.
4. Quitar duplicados, frente a filtrar valores únicos: a) oculta temporalmente; b) elimina
   permanentemente; c) no cambia nada; d) sólo marca con color. → **b**. Entera.
5. ¿Qué vínculo de uso compartido no exige autenticarse? a) Cualquiera; b) Personas de su
   organización; c) Personas específicas; d) ninguno. → **a**. Entera.
6. Un archivo enviado por el chat de Teams se guarda en: a) la carpeta del canal en SharePoint; b) el
   OneDrive para la Empresa de quien lo envía; c) el OneDrive personal; d) el buzón de Exchange. →
   **b**. Entera.
7. El Autoguardado está activado por defecto cuando el archivo está en: a) C:\; b) un servidor de
   archivos; c) OneDrive, OneDrive para la Empresa o SharePoint Online; d) un SharePoint local. →
   **c**; y las versiones entran en el historial cada 10 minutos aproximadamente. Entera.
8. En Outlook, Ctrl+F: a) busca; b) reenvía; c) responde; d) abre el calendario. → **b**. Entera.
9. En el calendario de Outlook, añadir periodicidad a una cita: a) la convierte en reunión; b) cambia
   la pestaña a «Serie de citas»; c) quita el aviso; d) la comparte. → **b** (aviso por defecto, 15
   minutos; el delegado puede programar reuniones y responder en nombre del titular). Entera.
10. En una base de datos, una relación de varios a varios se representa: a) repitiendo filas; b) con
    una clave externa en una de las dos tablas; c) con una tercera tabla de unión que la divide en dos
    relaciones uno a varios; d) no se puede representar. → **c** (y la clave externa es la clave
    principal de otra tabla). Entera.

Comprobación de las rúbricas sin pregunta arriba, también contestadas: sistemas corporativos (el ERP
de la RTVA es SAP, adquirido en 1999, calificado de obsoleto por la Cámara de Cuentas, punto 227;
funciones del Comité TIC; el ENS se aplica a todo el sector público del art. 2 de la Ley 40/2015) y
aplicación práctica (nueve casos). No hubo que ampliar el tema.
