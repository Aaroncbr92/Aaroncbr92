# 29-T16 · Redacción · Operador/a Informático · Prevención de riesgos laborales aplicada al puesto

Fecha: 05-10-2026. Tema escrito: `temas/canal-sur-especificos/29-operador-a-informatico/16-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md` (17.030 palabras según `indice.py`).
No se ha tocado ningún otro fichero del repositorio.

## Discrepancia con el encargo (manda la fuente)

- El encargo dice que el tema es «parecido» al 34-20; `AGRUPACION.tsv` (línea 175) lo marca **idéntico** (1,00) y el
  enunciado es palabra por palabra el del 34-20 y el del 32-15. Base usada: el **32-15 (Productor/a)**, que el encargo
  da por cerrado y que ya incorpora el epígrafe 1 del 34-20 sin cambios (comprobado con `diff`) y además el apartado
  «El puesto … en el convenio». Se reescribió sólo lo propio del puesto, y se amplió lo que el puesto pide
  (riesgo eléctrico, cargas, guardias, ratón/teclado).
- El investigador cita el RD 487/1997 como lo trae el 27-19; al montar la trazabilidad se detectó que su identificador
  es **BOE-A-1997-8670** (BOE-A-1997-8668 es el RD 485/1997, señalización). Corregido en el tema.
- RTVE (`prl-especifico.md`, apartado 9.8) cita el art. 2.6 del REBT **sin su salvedad** («siempre que su fuente de
  energía sea autónoma…»): error 6. En el tema va completa.

## Copiado del común

Literal de temas cerrados de Canal Sur (no se re-verifica):

Del **32-15 (Productor/a)**:
- Epígrafe 1 entero (arts. 14, 15, 17 a 22 y 29 de la Ley 31/1995), con su entradilla.
- Epígrafe 2: «Los riesgos generales: las cuatro disciplinas preventivas» (texto; la tabla es nueva), «La organización
  preventiva de la RTVA» (cambio único: «tocan al productor/a» → «tocan al operador/a informático»).
- Epígrafe 2, «Otros riesgos del puesto»: los párrafos del ET art. 36.4, NTP 318, NTP 443 y NTP 502 (cambio único en
  el sujeto de «Que afecten al …»; el ejemplo final de estrés y el cierre de turnos son nuevos).
- Epígrafe 3: «La norma: el RD 488/1997» (salvo el párrafo de la letra d) y la frase final del art. 29.4 del convenio,
  adaptados), «El anexo» (salvo la última frase del apartado 3, nueva), «La colocación de la pantalla», «Los riesgos,
  según la Guía Técnica» (salvo el ejemplo de carga mental, nuevo), «Ergonomía y TME».
- Epígrafe 4 entero salvo: se quitó la frase de la insolación y el rayo aplicada a exteriores; el párrafo de
  ejemplo in itinere/misión y la última frase de «Las medidas preventivas» son nuevos.
- Epígrafe 5: «El Real Decreto 773/1997» entero; arranque de «Las medidas preventivas del puesto, en resumen».

Del **27-19 (Oficial Técnico Electricista)**, cerrado (redacción, verificación, refutación, remate, final):
- «El riesgo eléctrico»: «La norma: RD 614/2001», «Qué es el riesgo eléctrico (anexo I.1)» con el párrafo de la
  letra c) y las baterías de SAI, «La regla: sin tensión (artículo 4.2)» con su tabla y el párrafo de condiciones del
  4.3, las definiciones 13 a 15 del anexo I y la frase «Todo trabajador cualificado…», «Formación (artículo 5)».
- «La manipulación de cargas»: desde «Las cargas: RD 487/1997» hasta «…que el real decreto nombra en su título.»

## Copiado de RTVE sin cambios

Ninguno. Lo tomado de RTVE se ha adaptado y releído en la fuente (se verifica):
- `temas/prl/prl-especifico.md` 3.6 (ratón no está en el anexo; Guía «habrá de conjugar…»; EN ISO 9241-410:2008):
  releído en `fuentes/prl-especifico/guia-tecnica-pvd.txt` l. 1309-1322; añadido ISO/TS 9241-411:2012 y la «ñ» (RD
  564/1993), l. 1298-1306. Guía PVD, portátiles, l. 326-335.
- `temas/prl/prl-especifico.md` 9.8 (anexo I.5 del RD 614/2001; REBT art. 2.1 y 2.6): releído con
  `boe.py precepto BOE-A-2002-18099 a2` (redacción vigente desde 01-07-2021, BOE-A-2021-6879; los apartados 1 y 6 no
  cambian) y `fuentes/canal-sur/BOE-A-2001-11881.md` l. 138.
- `temas/enfermeria/20-equipos-de-proteccion-individual.md`: no se usó; el RD 773/1997 viene del 32-15.

## Nuevo (pasa por el ciclo)

- «El puesto de operador/a informático en el convenio»: ficha 1324100 (X Convenio, anexo III, BOJA 240 pág. 189;
  `x-convenio-rtva-boja-240-2014.txt` l. 6786-6808), art. 45 nivel B04 (l. 1526-1542), anexo II plantilla (l. 2946-2951).
- «Los riesgos específicos del operador/a informático»: tabla tarea→riesgo (lectura del tema, declarada como tal).
- Párrafos propios en «El riesgo eléctrico» («Lo que esto significa para el puesto», «Baja y muy baja tensión»).
- Aplicación de cargas al puesto (servidores, monitores, baterías SAI).
- «Las guardias»: art. 50.11 del convenio (l. 1737-1745), literal.
- «Teclado y ratón (Guía Técnica)»; introducción del epígrafe 3; letra d) del art. 1 ampliada con la Guía.
- EPI: art. 30 del convenio (del 32-15) + anexo III del RD 773/1997 (filas cráneo y pies con «Manipulación de
  cargas…»; `fuentes/canal-sur/BOE-A-1997-12735.md` l. 279-291 y 401-404).
- Tabla de medidas, Normativa, «Lo que este tema no da» y Trazabilidad, rehechas.

Fuentes leídas el 05-10-2026. Huecos declarados: evaluación de riesgos del puesto, riesgos de CPD, guardias/turnos
del puesto, plan de prevención, relación de EPI.

## Preguntas tipo test (comprobadas contra el tema)

1. Según el art. 29.2 de la Ley 31/1995, ante una situación que entrañe riesgo, el trabajador debe informar de
   inmediato a: a) la Inspección; b) el Comité de Seguridad y Salud; **c) su superior jerárquico directo y a los
   trabajadores designados o, en su caso, al servicio de prevención**; d) el delegado sindical. — Entera (epígrafe 1, art. 29; epígrafe 2).
2. El derecho del trabajador a interrumpir su actividad ante riesgo grave e inminente está en: a) art. 14; **b) art.
   21.2**; c) art. 29.1; d) art. 22. — Entera.
3. La función básica del puesto de operador informático (código 1324100) en el X Convenio es: **a) implantar y
   administrar sistemas informáticos de carácter horizontal y sistemas específicos para la producción**; b) velar por
   el cumplimiento de la ley de prevención; c) dirigir el centro de proceso de datos; d) mantener las instalaciones
   eléctricas. — Entera (y que la ficha no le encarga tareas preventivas ni enumera riesgos).
4. El art. 29.4 del X Convenio fija para el trabajo en PVD: **a) diez minutos por cada hora de trabajo continuado, no
   acumulables**; b) quince minutos cada dos horas; c) cinco minutos por hora, acumulables; d) lo que diga el RD
   488/1997. — Entera.
5. Según el RD 614/2001, conectar y desconectar un equipo en baja tensión con material concebido para el público:
   a) exige trabajador cualificado; **b) es una operación elemental que puede hacerse en tensión, por el procedimiento
   del fabricante y verificando antes el buen estado del material**; c) exige las cinco etapas; d) está prohibido. — Entera.
6. Las baterías de un SAI, según el anexo I del RD 614/2001: **a) son instalación eléctrica aunque no estén conectadas
   a la red**; b) no son instalación eléctrica; c) sólo si superan 50 V; d) sólo en alta tensión. — Entera. (Variante:
   la «muy baja tensión» del REBT llega a 50 V CA y 75 V CC y cita las redes informáticas: entera.)
7. El RD 488/1997 excluye los portátiles: a) siempre; b) nunca; **c) siempre y cuando no se utilicen de modo continuado
   en un puesto de trabajo**; d) si su pantalla es menor de 15". — Entera (con el comentario de la Guía).
8. ¿Cuál no es requisito de diseño para evitar TME en el puesto de pantalla? a) asiento de altura regulable; b)
   reposapiés a disposición de quien lo desee; c) teclado inclinable e independiente; **d) mantener limpia la pantalla
   y evitar reflejos**. — Entera (epígrafe 3, TME; el ratón, en «Teclado y ratón»).
9. Según la Guía técnica del INSST de manipulación de cargas, el peso máximo en condiciones ideales para hombres de 20
   a 45 años es: a) 15 kg; b) 20 kg; **c) 25 kg**; d) 40 kg. Y para un operador que monta un servidor en un armario,
   ¿qué hay que hacer primero según el art. 3 del RD 487/1997? **Evitar la manipulación manual con medios mecánicos**.
   — Entera.
10. El accidente que sufre el operador al desplazarse por encargo de la empresa a un centro territorial para reparar un
    equipo es: a) in itinere; **b) en misión, accidente de trabajo**; c) no laboral; d) sólo laboral si ocurre en el
    centro. Y el plus de guardia localizable del convenio: si se llama al trabajador, la convocatoria mínima es de
    **cuatro horas**. — Entera (epígrafe 4; epígrafe 2, «Las guardias»).

Las diez se contestan enteras con el tema; no ha hecho falta ampliar más.
