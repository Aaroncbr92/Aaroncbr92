# Puesto 30 · Tema 4 · Revisión final (fase 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`.
Alcance: sólo los seis pasajes que lista `30-T04-remate.md`.

## Fuentes releídas (25-09-2026, sólo el pasaje)

- SMPTE ST 259:2008 (cl. 1, lín. 103-108); ST 292-1:2018 (cl. 1, lín. 89-91; 8.1.10, lín. 445-447);
  ST 424:2012 (cl. 1, lín. 86-88; lín. 439-440); ST 2082-1:2023 (cl. 1, lín. 89-91; lín. 882-883).
- UIT-R BT.2020-2 (10/2015), texto inglés: considerando d) y e) (lín. 126-136), apartado
  *recomienda* y su nota 1 a pie de página (lín. 153-155 y 181-185).
- SMPTE ST 2110-20:2022, 7.6 (lín. 960-964).
- EBU R 123 (julio de 2009): §§ 1-2, tabla 1 (8a, 8b, 8f), clave, notas generales, notas 1, 2, 3 y 5,
  anexo 2.2; bibliografía [1] y [2].
- EBU Tech 3343-2023: § 4.2, § 7.1 y la remisión a UIT-R BS.775-2 (lín. 948-949).

## Hallazgos y correcciones (todas comprobadas en la fuente antes de aplicarlas)

| Nº | Pasaje | Error | Qué dice la fuente | Corrección |
|---|---|---|---|---|
| 1 | § 11, SDI (pasaje 1) | 6 salvedad / 9 | La ST 259 sólo admite **«Receivers designed to work with lesser signal attenuation»**, y **«are not recommend for new designs»**; «greater or lesser» sólo en ST 292-1, 424 y 2082-1 | «las cuatro … admiten receptores para más o menos atenuación» → la ST 292-1, 424 y 2082-1 sí; la ST 259 sólo para menos y no los recomienda en diseños nuevos |
| 2 | § 2, glosa BT.2020-2 (pasaje 2) | 8 cita mal | La nota 1 es pie de página del apartado *recommends* («should be used1»), no del cuadro 1; la definición de LSDI está en el considerando e) | «nota 1 al cuadro 1» → «nota 1 a pie de página del apartado *recomienda*»; añadido «en su considerando e)» |
| 3 | § 12, pistas (pasaje 5) | 9 | La tabla 1 de la R 123 también trae multicanal codificado (*encoded MCA*) y, en la 8f, Ambisonics de formato B | «El multicanal de sus tablas es el 5.1» → «El multicanal discreto de su tabla 1 es el 5.1 (la tabla también prevé multicanal codificado y Ambisonics de formato B)» |
| 4 | § 12, LFE/5.0 (pasaje 5) | 6 salvedad | Tech 3343 § 4.2: prescindir del LFE **«if there is no need for extra headroom in the low frequency region»** | «si no se necesita» → «si no hace falta margen adicional en los graves» |
| 5 | «Lo que este tema no da» (pasaje 6) | 1 cita cruzada / 9 | La R 123 cita R 48 y SMPTE 2035, no la BS.775; la BS.775-2 la cita la Tech 3343 (coeficientes de *downmix*). «Disposición de los altavoces» no se leyó en fuente | Reescrito: BS.775, citada por la Tech 3343 para los coeficientes de *downmix*; R 48 y SMPTE 2035 (asignación de pistas en grabadores de cinta), citadas por la R 123 |

## Confirmado sin cambios

- Pasaje 1: las cuatro cifras de pérdida («20 dB to 30 dB», «up to 20/30/40 dB») y que sean típicas
  (el alcance de la ST 292-1 dice «typical»; su 8.1.10, «nominal»); el HD-SDI da menos que el SD-SDI.
- Pasaje 2: «large screen digital imagery», la definición de LSDI y las comillas “being there”, literales.
- Pasaje 3: la salvedad KEY está en ST 2110-20, 7.6, y el § 5 del tema la cita entera (lín. 445-446).
- Pasaje 4: 29,97 → 25 pierde unos 4,97 cuadros por segundo (cálculo); no son múltiplo.
- Pasaje 5: título y fecha de la R 123; citas de §§ 1-2, clave, notas generales, notas 1, 2 y 5 y
  anexo 2.2, literales; 8a (notas 1, 2) y 8b (notas 1, 3, 5) con sus pistas bien; Tech 3343 § 4.2 y
  § 7.1 (Lo/Ro por defecto, Lt/Rt), literales.
- Antecedentes: «lo llama» (canal LFE), «la misma recomendación» (BT.2020-2), «En las dos» (8a y 8b),
  «nota 1» (R 123), «esa pérdida típica», todos con antecedente delante.

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 14.291 palabras, 62 epígrafes (sin cambios de rúbrica). Portada: Extensión 14.300.

## Ficheros tocados

El tema y este informe.
