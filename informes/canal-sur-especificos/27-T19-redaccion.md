# Puesto 27 · Tema 19 · Redacción

Fase 2 · Redactar. Fecha de trabajo y de lectura de las fuentes nuevas: **05-10-2026** (el encargo fija
«hoy» en 24-09-2026; ninguna norma usada tiene redacción con vigencia entre ambas fechas).

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/19-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`
(20.974 palabras, 42 epígrafes según `indice.py`).

Base: AGRUPACION.tsv marca 27-19 como «parecido» (0,70) al 34-20, que es «idéntico» al 32-15 (Productor/a),
cerrado y verificado. Se ha partido del 32-15 (redacción vigente) y se ha ampliado sólo la rúbrica 2 con
lo que este enunciado pide de más: riesgo eléctrico, altura, espacios confinados, cargas, químicos,
señalización y etiquetado, más el puesto en el convenio (fichas 9311100 y 9311200) y el recurso preventivo.

## Ficheros tocados

- Creado: el tema 19 (ruta arriba) y este informe. Borradores en el scratchpad de la sesión (no en el repositorio).
- No he tocado otros temas ni fuentes. (Los cambios ajenos que muestra `git status` en 27/14, 27/15 y otros informes no son míos.)

## Fuentes leídas (05-10-2026)

| Fuente | Cómo | Para qué |
|---|---|---|
| RD 614/2001 (BOE-A-2001-11881), arts. 1-5, anexos I, II.A, III.A, IV.A, V.A | `boe.py precepto` | Riesgo eléctrico |
| RD 39/1997 (BOE-A-1997-1853), art. 22 bis | `boe.py precepto` | Recurso preventivo; definición de espacio confinado |
| RD 1215/1997 (BOE-A-1997-17824), anexo II 4.2.5 | `boe.py precepto` | Fila «Revisión» de escaleras |
| RD 374/2001 (BOE-A-2001-8436), arts. 4, 5, 6, 9 | `boe.py precepto` | Químicos |
| RD 485/1997 (BOE-A-1997-8668), arts. 1, 2, 4, 5, anexos II, III, VII | `boe.py precepto` | Señalización y etiquetado |
| RD 773/1997 (BOE-A-1997-12735), anexo III | `boe.py precepto` | EPI eléctricos y anticaídas |
| Reglamento CLP (DOUE-L-2008-82637), arts. 2, 17, 20, anexo V; Reglamento (UE) 2024/2865 (DOUE-L-2024-81721), art. 2 | volcados en `fuentes/canal-sur/` | Etiqueta |
| X Convenio RTVA, fichas 9311100 (pág. 185) y 9311200 | `x-convenio-rtva-boja-240-2014.txt` l. 6672-6688 y 4779-4793 | Puesto |
| Informe `27-investigacion-D-mantenimiento.md` §4 | — | Material |

No se pudo abrir: NTP 223 del INSST (recintos confinados), 404 en insst.es. Por eso las medidas de
espacios confinados van declaradas como práctica de oficio.

## Copiado del común

Literal, de temas cerrados de Canal Sur (verificación y refutación lo saltan):

Del tema 32-15 (Productor/a):
- «De dónde sale este tema»: **no** (reescrito para este enunciado).
- Epígrafe 1 entero: «1. Derechos y obligaciones…» con los artículos 14, 15, 17, 18, 19, 20, 21, 22 y 29.
- Epígrafe 2: párrafo inicial de «Los riesgos generales: las cuatro disciplinas preventivas» (la tabla
  y su nota se han reescrito, ver abajo); «La organización preventiva de la RTVA» entero salvo la frase
  indicada abajo.
- Epígrafe 2, «Otros riesgos del puesto»: el texto de ET 36.4, NTP 318, NTP 443 y NTP 502, salvo los
  pasajes indicados abajo.
- Epígrafe 3 entero salvo los cuatro pasajes indicados abajo.
- Epígrafe 4 entero salvo los tres pasajes indicados abajo.
- Epígrafe 5: «El Real Decreto 773/1997» entero.
- Normativa y Trazabilidad: las filas comunes (Ley 31/1995, RD 39/1997 art. 34, RD 488, RD 486, RD 773,
  LGSS, ET, Carta, INSST, NTP, CNSST, Anuario).

Del tema 32-14 (Productor/a):
- «La manipulación de cargas»: art. 2, art. 3.1 y 3.2, cita y tablas de la Guía INSST (2024), tabla del
  anexo en cinco grupos, tabla de la técnica de levantamiento y su párrafo final. Quitado: los ejemplos de
  producción (flight case, decorado) y el párrafo final de producción.
- «Los trabajos en altura»: anexo I.6 y su comentario («Dos cifras…»), 4.1.1, 4.1.6 y las siete filas de
  la tabla de escaleras.

**Pasajes adaptados (no literales; sí se verifican):**
1. Tabla «Disciplina | Riesgos del oficial técnico electricista…» (4 filas nuevas).
2. «La organización preventiva»: «fija tres medidas que tocan a todo el personal» (antes «al productor/a»).
3. «Otros riesgos»: título; primera frase («Ni el estrés ni el trabajo a turnos tienen…»); ejemplo de
   estresores del electricista (cita NTP 318 «responsabilidad», «tareas peligrosas»); cierre con la ficha
   del ayudante y las guardias.
4. Epígrafe 3: párrafo de entrada; frase sobre la letra d) (portátil a pie de instalación); salvedad del
   descanso («una maniobra o una avería en curso»); «programas» (gestión técnica y de mantenimiento);
   ejemplo de carga mental.
5. Epígrafe 4: salvedad del 156.4.a) (cubiertas, torres, centros emisores); distinción in itinere / en
   misión; frase sobre el plan de seguridad vial (avería urgente).
6. Altura: frase introductoria (sin la de producción) y la fila nueva «Revisión» (anexo II 4.2.5, leído en BOE).

## Copiado de RTVE sin cambios

**Nada.** Motivo: la fila 27-19 de `informes/canal-sur-reuso/tecnica.tsv` marca **actualizar = sí**,
el tema cita normas en cada pasaje (el encargo manda verificar lo que cite normas) y las fuentes RTVE
tenían defectos que impiden copiarlas sin tocar:
- teitse/14: define «trabajador cualificado» sin «trabajador autorizado que…» ni los «dos o más años», y
  «jefe de trabajo» como «dirección y vigilancia» (la norma dice «responsabilidad efectiva»); dice que el
  detector se comprueba antes y después en general, cuando el anexo II.A.1.3 lo exige **en alta tensión**;
  y usa la negrita como énfasis, no como literal.
- prl-especifico §8: definición de espacio confinado parafraseada y sin cita; tabla de medidas y «la
  causa más frecuente de muerte» sin fuente (quitados; las medidas quedan como oficio).
- enfermería/02 y medicina/13: su texto de RD 485/1997 y RD 374/2001 coincide con el BOE vigente, pero se
  ha tomado del BOE y reescrito con la convención de negritas de Canal Sur.

Todo lo que viene de RTVE está, pues, reescrito desde el BOE leído el 05-10-2026 y **debe verificarse**:
«La presencia de recursos preventivos», «El riesgo eléctrico», «Los espacios confinados», «Los productos
químicos y su etiquetado», «La señalización», «El puesto… en el convenio», «Los riesgos específicos…» y,
del epígrafe 5, «Los EPI en la RTVA y en el trabajo del oficial técnico electricista» y «Las medidas
preventivas del puesto, en resumen»; además, «Normativa», «Lo que este tema no da» y las filas nuevas de
«Trazabilidad».

## Avisos para verificación

- `negritas.py` sobre lo nuevo: 248 negritas; las «no encontradas» son rótulos, la Guía INSST de cargas
  (copiada de 32-14) y elisiones con […]; los cinco «¿art.?» del CLP son falsos positivos (están en el 17.1).
- CLP: texto no consolidado; sólo comprobado que el 2024/2865 no toca 2.3-2.6, 17, 20; no comprobadas las
  reformas anteriores ni las ATP del anexo V (declarado en el tema).
- Anexo III del RD 773/1997: el volcado aplana la tabla; no se atribuye cada actividad a un EPI concreto,
  sólo al grupo.
- Correspondencias tareas → riesgos y ejemplos (baterías, refrigerantes, arquetas, guardias) son
  aplicación del tema y van dichos como tales.

## Diez preguntas de tribunal y comprobación

| # | Rúbrica | Pregunta | Respuesta | ¿La da el tema? |
|---|---|---|---|---|
| 1 | Derechos | Según el art. 21.2 LPRL, el trabajador puede interrumpir su actividad y abandonar el lugar de trabajo cuando considere que la actividad entraña: a) cualquier riesgo; b) un riesgo muy grave; c) un riesgo grave e inminente para su vida o su salud; d) un riesgo para terceros | c | Entera (art. 21, con la tabla de las tres paralizaciones) |
| 2 | Riesgo eléctrico | La tercera de las cinco etapas del anexo II.A.1 del RD 614/2001 es: a) poner a tierra y en cortocircuito; b) verificar la ausencia de tensión; c) prevenir la realimentación; d) señalizar | b | Entera |
| 3 | Riesgo eléctrico (práctico) | Un oficial autorizado, sin formación acreditada y con un año de experiencia, ¿puede hacer un trabajo en tensión en BT? a) sí, basta la autorización; b) sí, con jefe de trabajo; c) no: los trabajos en tensión exigen trabajador cualificado; d) sí, si es BT | c | Entera (definiciones 13-14 y tabla «Quién puede hacer qué») |
| 4 | Altura | Desde una escalera de mano, ¿a partir de qué altura los trabajos con movimientos peligrosos exigen anticaídas u otras medidas alternativas? a) 2 m; b) 3,5 m; c) 5 m; d) 1 m | b | Entera (tabla de escaleras) |
| 5 | Espacios confinados | La definición reglamentaria de espacio confinado y la obligación de recurso preventivo están en: a) el RD 614/2001; b) el RD 486/1997; c) el art. 22 bis del RD 39/1997; d) no existen | c | Entera |
| 6 | Cargas | Según la Guía técnica del INSST, el peso máximo en condiciones ideales para hombres de 20 a 45 años es: a) 15 kg; b) 20 kg; c) 25 kg; d) 40 kg | c | Entera |
| 7 | Químicos y etiquetado | En la etiqueta CLP, la palabra de advertencia de las categorías más graves es: a) «atención»; b) «peligro», y entonces no aparece «atención»; c) «tóxico»; d) ambas | b | Entera (arts. 2.4 y 20.3) |
| 8 | Señalización | Una señal de obligación es: a) triangular, negro sobre amarillo; b) redonda, blanco sobre azul; c) redonda con banda roja; d) rectangular, blanco sobre verde | b | Entera (tabla anexos II y III) |
| 9 | PVD / in itinere (práctico) | El oficial sufre un accidente de tráfico yendo desde su centro a un centro emisor para reparar una avería: a) in itinere; b) en misión; c) no laboral; d) enfermedad profesional | b | Entera (epígrafe 4, aplicación al puesto y NTP 1090) |
| 10 | EPI | Según el art. 4 del RD 773/1997, los EPI deben utilizarse: a) siempre que haya riesgo; b) cuando los riesgos no hayan podido evitarse o limitarse suficientemente por protección colectiva u organización del trabajo; c) a elección del trabajador; d) sólo en AT | b | Entera (art. 4 y regla de subsidiariedad; aplicación al riesgo eléctrico en el epígrafe 5) |

Las diez se contestan enteras con el tema; no ha hecho falta ampliar. Se comprobaron además, sin
incluirlas en la lista: descanso de diez minutos por hora en pantallas (X Convenio art. 29.4), obligación
4.ª del art. 29.2, función básica del puesto en el convenio, barandilla de 90 cm a más de 2 m y orden de
las medidas del art. 5.2 del RD 374/2001: todas contestadas.
