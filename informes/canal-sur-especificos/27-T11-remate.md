# Remate · Oficial Técnico Electricista (27) · Tema 11 · Protección contra incendios y seguridad en instalaciones

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/11-proteccion-contra-incendios-y-seguridad-en-instalaciones.md`.
Entrada: `27-T11-refutacion.md` (0 graves, 1 menor, 2 lagunas) y `27-T11-preguntas.md` (13 enteras,
1 a medias, 1 no). Fecha de lectura de las fuentes: 05-10-2026 (reloj del sistema; el encargo dice
«hoy es 24-09-2026»; ninguna redacción de las fuentes usadas cambia entre esas fechas).

Ficheros tocados: el tema y este informe. Copia del tema anterior al remate en el scratchpad
(`27t11-antes-remate.md`).

Resultado: **las tres propuestas, comprobadas en la fuente y aplicadas. Se ha ampliado contenido
nuevo (L1, L2)**: pasa a 5 bis.

## Comprobación en la fuente

| # | Fuente leída (05-10-2026) | Resultado |
|---|---|---|
| M1 | Real Decreto 393/2007 (volcado `BOE-A-2007-6237`), anexo I: apartado 1.d) «Edificios cerrados: Con capacidad o aforo igual o superior a 2000 personas…» (actividades **con** reglamentación sectorial); apartado 2.c) «Instalaciones de generación y transformación…» y 2.g) «Todos aquellos edificios…» (**sin** reglamentación sectorial); artículo 2.1, «aplicándose con carácter supletorio» a las del punto 1 | El informe acierta. Aplicado |
| L1 | RIPCI, anexo I, sección 1.ª, apartado 2 (volcado); anexo II, tablas I y II leídas por columnas en la página HTML del BOE consolidado (`act.php?id=BOE-A-2017-6606`, descargada hoy): fila «Sistemas de abastecimiento de agua contra incendios», columnas «Tres meses», «Seis meses», «Año»; la columna «Cinco años» está vacía | El informe acierta en todo: la «Comprobación de la alimentación eléctrica, líneas y protecciones» es semestral y el «estado de carga de baterías y electrolito», anual. Aplicado |
| L2 | RIPCI, anexo I, sección 1.ª, apartado 13.1 y 13.2; anexo II, tablas I y II por columnas (misma página): fila «Sistemas para el control de humos y de calor»; «Cinco años» vacía | El informe acierta. Aplicado |

## Pasajes cambiados

1. **Qué se puede preguntar**: añadido «qué son el sistema de abastecimiento de agua contra
   incendios y los de control de humos y de calor» y «semestral» en la lista de periodicidades.
2. **4.6**, enumeración del RIPCI: añadido «el sistema de abastecimiento de agua contra incendios»
   a la lista de sistemas que regula.
3. **4.6**, nuevo bloque al final («Dos de los sistemas que regula el RIPCI…»), dos viñetas:
   abastecimiento de agua (definición literal del anexo I, apartado 2, y remisión literal a la UNE
   23500; composición del grupo de bombeo, declarada oficio) y control de humos y de calor
   (literal del apartado 13.1, las cuatro estrategias literales, marcado CE de barreras, aireadores
   y extractores según UNE-EN 12101-1, -2 y -3 del apartado 13.2; enlace con las maniobras de 2.5).
4. **4.7**, tabla: fila nueva «Sistema de abastecimiento de agua» (antes de «Sistemas fijos») y
   fila nueva «Control de humos y de calor» (al final), con las operaciones de tres y seis meses
   (tabla I) y anuales (tabla II), literales en negrita las que llevan cifra o parte eléctrica;
   «La tabla II no fija operación quinquenal» en ambas.
5. **4.7**, párrafo nuevo tras la tabla («Lo que toca de lleno al electricista en esas dos
   filas…»): resume la parte eléctrica y recuerda quién puede hacer cada operación (remite a 1.5).
6. **7.2**, «Quién lo necesita» (M1): reordenado. Apartado 2 del anexo (sin reglamentación
   sectorial): letra g) (edificios administrativos) y letra c) (alta tensión); después, «en
   cambio», los edificios cerrados de espectáculos públicos del apartado 1.d), con reglamentación
   sectorial, y la aplicación «con carácter supletorio» del artículo 2.1. Se ha recortado la
   negrita de espectáculos a la parte literal que sigue a «capacidad o aforo».
7. **Portada**, Extensión: 12.900 → 13.600 palabras.
8. **Lo que este tema no da**: añadidas UNE 23500 y la serie UNE-EN 12101 a las normas cuyo
   contenido no se da.
9. **Trazabilidad**: RIPCI anexo I, sección 1.ª, apartados 2 y 13 añadidos; en «oficio», la
   composición habitual del grupo de bombeo y la lectura eléctrica del mantenimiento de las dos
   filas nuevas.

Releídos los pasajes 3, 5 y 6: «esas dos filas» tiene delante la tabla; «en ese mismo grupo» y «a
ellas» tienen delante su antecedente; «Dos de los sistemas de esa lista» se cambió a «Dos de los
sistemas que regula el RIPCI», porque entre la lista y la frase va el párrafo del DB SI.

## Lentes

- `indice.py`: 13.653 palabras, 43 epígrafes; índice sin cambios (no hay epígrafes nuevos).
- `negritas.py` (mismas 13 fuentes que la verificación, con el RIPCI HTML de hoy): 278 negritas
  (259 antes); las 19 nuevas, todas encontradas; «no están» y «¿art.?» idénticos a antes del remate
  (3 y 3, ya explicados en la verificación).
- `refutar_exactitud.py` (RIPCI, RD 393/2007): 32 no literales antes y después; el único cambio es
  que la negrita «igual o superior a 2000 personas…» sale «(art. 2)» en lugar de la de alta
  tensión: falso positivo del mismo tipo (está en el anexo I, 1.d, y `negritas.py` la encuentra).
- `refutar_modo.py`: 0. `refutar_prosa.py`: sin hallazgos, igual que antes.

## Para 5 bis

Revisar sólo los pasajes 3, 4, 5 y 6. Las columnas de las tablas I y II no se distinguen en el
volcado plano: se leen en la tabla HTML del BOE.
