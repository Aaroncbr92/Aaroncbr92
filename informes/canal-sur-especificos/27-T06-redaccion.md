# Puesto 27 · Oficial Técnico Electricista · Tema 6 · Fase 2, redacción

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas). Tema escrito:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/06-alumbrado-interior-exterior-y-de-emergencia.md`
(11.800 palabras según `indice.py`; 5 rúbricas en el orden del enunciado, 23 epígrafes `###`).

Ficheros tocados: sólo el tema y este informe. Copias de trabajo de los DB del CTE (PDF y `.txt`)
en el scratchpad de la sesión, fuera del repositorio.

Material: `27-investigacion-B-alimentacion-instalaciones.md` § 6.1-6.5 (y § 11.2-11.4 para el RIPCI);
RTVE `teitse/08` § 2-4, `ing-tec-industrial/12` § 3, `prl/prl-especifico` § 12.

Lentes pasadas al cerrar: `negritas.py` contra los seis textos (317 negritas; 2 «no están», ambas
rótulos de la plantilla; 2 «otro artículo», falsos avisos: «Locales de pública concurrencia» está
también en la ITC-BT-05, 4.1.b, y «modificación de importancia» en el art. 2.3.c del RD 1890/2008,
que es lo que el tema cita); `refutar_prosa.py`: 0 hallazgos.

## Fuentes releídas en esta fase

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), `boe.py precepto` ib-28, ib-44, ib-9, ib-5, a2-2 | 05-10-2026 | ITC-BT-09, 28 y 44: redacción única (vig. 18-09-2003). Art. 20: vig. 23-05-2010 (BOE-A-2010-8190). ITC-BT-05: vig. 30-06-2015 (BOE-A-2014-13681), 4.1.b y g, 4.2 |
| RD 1890/2008 (BOE-A-2008-18634), arts. 1, 2, 4, 5, 12; ITC-EA-02, 04, 05, 06 | 05-10-2026 | Redacción única (vig. 01-04-2009) salvo ITC-EA-02 (2.ª redacción vig. 10-08-2022, sólo la nota del RDL 14/2022) |
| RD 486/1997 (BOE-A-1997-8669), art. 8 y anexo IV | 05-10-2026 | Redacción única (vig. 23-07-1997); apartados 1 a 6 enteros |
| RD 314/2006 (BOE-A-2006-5515), art. 2 | 05-10-2026 | Redacción vig. 28-06-2013 (Ley 8/2013) |
| RD 513/2017 (BOE-A-2017-6606), anexo I s. 1.ª ap. 15, anexo II ap. 8, art. 22 | 05-10-2026 | Redacción vig. 10-05-2025 (BOE-A-2025-7190); ap. 15 y ap. 8 idénticos en la redacción anterior (`--fecha 20250101`) |
| DB SUA consolidado «14 junio 2022», codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf | 05-10-2026 | SUA 4, apartados 1 y 2 enteros, pasado a texto con `documento.py` |
| DB HE consolidado «14 Junio 2022», codigotecnico.org/pdf/Documentos/HE/DBHE.pdf, y página AhorroEnergia.html | 05-10-2026 | HE 3 entero y definiciones del anejo A |

## Correcciones y decisiones (manda la fuente)

1. **Pendiente de la investigación resuelto (DB HE):** la «versión 22 diciembre 2023» de la web es el
   «DB-HE C Documento con comentarios del Ministerio»; el DB vigente sigue siendo el de 14-VI-2022
   (RD 450/2022).
2. **Exigencia del HE 3:** la investigación citaba la Parte I, 15.4 («ajustar su funcionamiento a la
   ocupación real»). El tema cita el apartado 2 de la sección HE 3, que dice «ajustar el encendido a
   la ocupación real de la zona». Leído en el PDF.
3. **Añadido a la investigación:** la ITC-BT-28, apartado 3, «La alimentación del alumbrado de
   emergencia será automática con corte breve» (0,5 s), y la frase de 3.1 sobre la carga desde el
   suministro exterior. La investigación no los recogía.
4. **Añadido a la investigación:** nota (5) de la tabla 3.1-HE3 («no se incluye las instalaciones de
   iluminación necesarias para las retransmisiones televisadas»), útil para el puesto.
5. **Salvedad del RD 486/1997 que el RTVE omitía (error 6):** «estos límites no serán aplicables en
   aquellas actividades cuya naturaleza lo impida» (anexo IV.3). Se añade.
6. **RTVE teitse/08 § 4:** «Un quirófano y un control de emisión piden el segundo [reemplazamiento]».
   La ITC-BT-28 sólo obliga al reemplazamiento en hospitales (3.3.2); el tema dice que en un control
   de continuidad es decisión de proyecto.
7. **RTVE teitse/08, trazabilidad:** decía que los niveles del alumbrado de emergencia están «en el
   Código Técnico». También están en la ITC-BT-28, 3.1.1-3.1.3. El tema da los dos.
8. **NBE-CPI-96** citada por la ITC-BT-28, 3.3.1: se deja como salvedad (derogada por el CTE; hoy
   DB SI 1), sin corregir la ITC. Derogación comprobada: RD 314/2006, disposición derogatoria
   única, 1.g (`boe.py precepto BOE-A-2006-5515 ddunica`, redacción única, leída 05-10-2026).
9. **ITC-BT-44, apartado 1:** la investigación entrecomillaba «el alumbrado exterior recogido…»; el
   texto dice «al alumbrado exterior recogido…». Corregida la cita.

## Qué se quitó por propio de RTVE o sin fuente

- Referencias a preguntas del examen RTVE, a «este proyecto», al «apartado 7 del manual» y a otras
  ocupaciones (prl § 12); «Es el único reglamento del anexo que protege el cielo nocturno»
  (ing-tec-industrial/12 § 3, referido al anexo RTVE).
- ing-tec-industrial/12 § 3: «el de baja tensión del tema 7 mide sólo por potencia» (no comprobado).
- teitse/08 § 3: la tabla «qué tecnología cumple cada categoría» (conmutación estática, etc.), oficio
  sin fuente; queda sólo la lectura de que un grupo no da el corte breve.
- La tabla de pública concurrencia de teitse/08 § 2 se sustituye por citas literales del apartado 1.

## Copiado del común

Ninguno. El único pasaje cerrado de Canal Sur sobre la materia (tema 18 de Ayudante de Realización,
lista de iluminación del RD 486/1997 en el contexto de pantallas) resume el anexo IV en una frase; el
tema 6 cita el anexo IV directamente del BOE, entero en lo que usa.

## Copiado de RTVE sin cambios

Ninguno. Los tres temas RTVE de este tema están marcados «actualizar: sí» y todo lo aprovechable cita
norma, así que no cabe la exención. Lo reutilizado, **adaptado y para verificar**:

- prl-especifico § 12: cita del art. 8 RD 486/1997; tabla del anexo IV (negritas recolocadas sobre lo
  literal); «Dónde se mide» (ahora cita); regla de duplicar (ahora cita literal); cita del anexo IV.4
  (literal); comentario de la letra b) y del estroboscópico (reescrito); preferencia por la luz
  natural (ahora cita).
- ing-tec-industrial/12 § 3: cita del art. 1.1 RD 1890/2008; «Dos finalidades…»; art. 1.2 (ahora
  literal); tablas de ámbito, tipos, aplicación y art. 4 (con citas literales añadidas); art. 5;
  exclusiones; párrafo «Ese "o luminarias"…» (reescrito).
- teitse/08 § 2-4: cita de la ocupación (1 persona / 0,8 m²) y su excepción; cita de las categorías
  de conmutación; cuatro condiciones de las fuentes (ahora literales); umbral del 70 %; distinción
  «seguridad para irse, reemplazamiento para quedarse»; tres subtipos (ahora con su definición
  literal); autónomo frente a fuente central (ahora con definiciones literales).

## Preguntas tipo test de comprobación (10)

Respuesta correcta en negrita; a la derecha, dónde la contesta el tema. Las diez se contestan
enteras con el tema; no ha hecho falta ampliar.

1. (Interior, teoría) Según el anexo IV del RD 486/1997, el nivel mínimo de iluminación en zonas
   donde se ejecuten tareas con exigencias visuales altas es: a) 200 lux; **b) 500 lux**; c) 1.000
   lux; d) 300 lux. — Epígrafe 1.2.
2. (Interior, teoría) Según el DB SUA 4, la iluminancia mínima del alumbrado normal en zonas de
   circulación interiores, salvo aparcamientos, medida a nivel del suelo, es: a) 50 lux; b) 20 lux;
   **c) 100 lux**; d) 200 lux. — Epígrafe 1.4.
3. (Luminarias, práctica) Un circuito alimenta 10 lámparas de descarga de 100 W sin datos de
   fabricante. La carga mínima prevista según la ITC-BT-44 es: a) 1.000 VA; **b) 1.800 VA**; c) 1.111
   VA; d) 2.000 VA. — Epígrafe 2.1.
4. (Exterior, teoría) En el cuadro de un alumbrado exterior, la ITC-BT-09 fija para los diferenciales
   una sensibilidad máxima de: a) 30 mA con tierra ≤ 300 Ω; **b) 300 mA con tierra ≤ 30 Ω**; c) 500
   mA con tierra ≤ 30 Ω; d) 1 A con tierra ≤ 5 Ω. — Epígrafe 1.5.
5. (Eficiencia, práctica) Una sala de 250 m² con 2.000 W de lámparas más equipos y Em = 400 lux
   tiene un VEEI de: a) 0,8; **b) 2,0**; c) 5,0; d) 8,0 W/m² por cada 100 lux. — Epígrafe 3.1 (fórmula)
   y 3.2.
6. (Eficiencia, teoría) Una instalación de alumbrado exterior de 7 kW debe llevar, según la
   ITC-EA-04: a) fotocélula; **b) reloj astronómico o encendido centralizado**; c) interruptor manual
   únicamente; d) detector de presencia. — Epígrafe 3.4.
7. (Seguridad, práctica) En una zona de alto riesgo con 400 lux de alumbrado normal, el alumbrado
   de seguridad debe dar como mínimo: a) 15 lux; b) 5 lux; **c) 40 lux**; d) 1 lux. — Epígrafe 4.2.
8. (Seguridad, teoría) Según el DB SUA 4, el alumbrado de emergencia de las vías de evacuación debe
   alcanzar el 50 % del nivel requerido y el 100 % al cabo de: **a) 5 s y 60 s**; b) 0,5 s y 15 s;
   c) 1 s y 10 s; d) 15 s y 1 hora. — Epígrafe 4.3.
9. (Seguridad, práctica) Con fuente central, una misma línea de alumbrado de emergencia puede
   alimentar como máximo, según la ITC-BT-28: a) 10 puntos de luz; **b) 12 puntos de luz,
   protegida con automático de 10 A como máximo**; c) 12 puntos con automático de 16 A; d) un tercio
   de las lámparas del local. — Epígrafe 4.5.
10. (Mantenimiento y reposición, teoría) Según la ITC-EA-06, las mediciones eléctricas y
    luminotécnicas del plan de mantenimiento de un alumbrado exterior las realiza, y el registro se
    guarda: a) el titular, dos años; b) un organismo de control, diez años; **c) un instalador
    autorizado en baja tensión, al menos cinco años**; d) cualquier subcontrata, un año. — Epígrafe 5.2.
