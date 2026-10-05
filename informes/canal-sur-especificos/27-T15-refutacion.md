# Refutación · Oficial Técnico Electricista (27) · Tema 15 · Trabajos en instalaciones eléctricas

Fase 4 (no corrige). Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/15-trabajos-en-instalaciones-electricas.md`.
Preguntas: `27-T15-preguntas.md`. Fecha del encargo: 24-09-2026; fuentes leídas el 05-10-2026 (reloj del
sistema). Ninguna norma citada tiene más de una redacción (RD 614/2001 desde 21-08-2001; RD 171/2004 desde
30-04-2004; RSP art. 22 bis desde 29-06-2006), así que la diferencia de fechas no cambia nada.

Ficheros tocados: este informe y `27-T15-preguntas.md`. Script temporal en el scratchpad. El tema no se ha tocado.

**Resumen: 0 graves, 5 menores, 2 lagunas.** Preguntas: 12 enteras, 1 a medias, 2 no.

## Alcance

- Saltado, según `27-T15-redaccion.md`: «Copiado del común» (6.1, art. 24 LPRL) y el cuerpo literal de 6.2 a
  6.5 copiado del 32-T14. Los pasajes adaptados de 6.2, 6.4 y 6.5 y todo 6.6 sí se han mirado. «Copiado de
  RTVE sin cambios»: nada declarado.
- Exactitud: RD 614/2001 releído entero (arts. 1 a 6, df 1.ª y 3.ª, anexos I a VI, tabla 1 celda a celda);
  guía INSST 2020 (todas las citas, cotejo normalizado sin guiones blandos ni saltos de línea: **todas
  literales**; las «NO ESTÁ» de `negritas.py` son falsos negativos por cortes de página); RD 171/2004 (df,
  entrada en vigor a los tres meses de 31-01-2004); REBT ITC-BT-29 ap. 4 («técnico competente»: confirmado).
- Cobertura: el tema entero contra el enunciado.

## Lentes

- `negritas.py` (RD 614/2001, guía, RSP, RD 171/2004, REBT): 327 negritas; 47 «NO ESTÁ» = rótulos, texto
  copiado del común (LPRL) o citas de la guía partidas por el PDF (comprobadas con cotejo propio: literales);
  10 «¿ART.?» = texto copiado de 6.2-6.4 o la cita del 2.2 b) bien presentada (falsos positivos).
- `refutar_exactitud.py`: 44 citas, 6 «no literales», todas falsos positivos (citas de la guía o números de
  epígrafe leídos como artículos). `refutar_modo.py`: 0. `refutar_prosa.py`: 0.

## Hallazgos de exactitud

| # | Epígrafe | Error | Qué dice el tema | Qué dice la fuente | Propuesta |
| --- | --- | --- | --- | --- | --- |
| 1 | Portada, «Fuente» | 9 | «Guía técnica del INSST … (4.ª edición, 2020)» | La guía no dice «4.ª»; la verificación ya lo corrigió en 1.1 y en trazabilidad («edición de septiembre de 2020, la cuarta según su histórico»), pero no en la portada | Igualar la portada: «edición de septiembre de 2020» |
| 2 | 1.4, cuadro «quién puede hacer qué», fila «Trabajo en proximidad cuando las medidas no bastan» | 6 | BT: «Autorizado, o bajo la vigilancia de uno», igual que en AT | Anexo V.A.2.2: «**La vigilancia no será exigible cuando los trabajos se realicen fuera de la zona de proximidad o en instalaciones de baja tensión.**» El texto de 4.4 lo dice; el cuadro no, y lo contradice | Añadir en la celda BT: «la vigilancia no es exigible en BT (V.A.2.2)» |
| 3 | 3.5, transformador de intensidad | 6 | Sólo: «Se prohíbe la apertura de los circuitos conectados al secundario estando el primario en tensión…» | Anexo II.B.4.1, párr. 2, empieza: «**Para trabajar sin tensión en un transformador de intensidad, o sobre los circuitos que alimenta, se dejará previamente sin tensión el primario.**» | Añadir esa frase antes de la prohibición (pregunta 2, a medias) |
| 4 | 4.3, último párrafo | 6 | «aunque se invada la zona de peligro “solamente por un instante”, la operación se transformaría en “trabajo en tensión” o en “trabajo en proximidad”» | La guía reparte: se transforma en trabajo en tensión **si tuviera que ocuparse** la zona de peligro, y en trabajo en proximidad **si pudiera invadirse accidentalmente** (coincide con el art. 4.6 y sus «apartados 5 ó 7») | Dar el criterio: ocupar → tensión (anexo III); poder invadir accidentalmente → proximidad (anexo V) |
| 5 | 3.5, condensadores | redacción | «*Condensadores (B.3)*, cuando **«cuya capacidad y tensión permitan…»**» | La frase no se sostiene gramaticalmente («cuando cuya») | «… en instalaciones con condensadores **«cuya capacidad y tensión permitan…»**» |

Confirmado sin cambios (muestra): arts. 1 a 6; definiciones 1, 3 a 15; tabla 1 entera y sus notas; la
interpolación a 25 kV (77/63/127/300); las cinco etapas, su párrafo final y A.2; II.B.1 a B.4 (salvo el
hallazgo 3); III.A, III.B, III.C; IV.A y IV.B; V.A, V.B.1, V.B.2; VI.A y VI.B; la entrada en vigor
(21-08-2001, dos meses tras el BOE de 21-06-2001); la df 1.ª (INSHT, guía no vinculante); las citas de la
guía sobre la decisión de trabajar en tensión, el certificado de experiencia («debería indicarse»), la
desconexión, el neutro, el bloqueo, las señales, la verificación (obligatoria antes y después sólo en AT),
UNE-EN 61243-3, la inducción por antenas, la secuencia BT de puesta a tierra y su retirada, los EPI, las
tres salidas de la quinta etapa, el permiso en AT y el boletín. 6.6: la fila de la distribuidora estira algo
la guía (que pone el deber de aviso en la empresa responsable de la línea y las medidas en los centros
receptores), pero no la contradice; sin hallazgo.

## Cobertura del enunciado

| Rúbrica del enunciado | Dónde | Juicio |
| --- | --- | --- |
| Trabajos en instalaciones eléctricas | 1.1 a 1.5 | Completa |
| Consignación | 2.1 a 2.4 | Completa (término de oficio declarado) |
| Cinco reglas de oro | 3.1 a 3.5 | Completa, salvo hallazgo 3 |
| Trabajos en tensión o proximidad | 4.1 a 4.6 | **Laguna 1 y 2** |
| Permisos de trabajo | 5.1 a 5.3 | Completa (no hay modelo oficial; declarado) |
| Coordinación de actividades empresariales | 6.1 a 6.6 | Completa |

## Lagunas (se amplía el tema)

1. **Métodos de trabajo en tensión** (pregunta 9, no). La guía del INSST, en sus comentarios al anexo
   III.A.2, distingue tres: **a potencial** (sobre todo líneas y transporte de AT), **a distancia** (AT en la
   gama media, con pértigas) y **en contacto** con guantes aislantes y herramientas con recubrimiento aislante
   (sobre todo BT y la gama baja de AT), y pide procedimientos específicos por tipo de trabajo, escritos en
   AT. Es el método que usaría el puesto en BT y una pregunta clásica de «trabajos en tensión». Ampliar 4.2
   con un párrafo y su cita literal.
2. **EPI y equipos para trabajos en tensión: clases de guantes aislantes** (pregunta 10, no). El tema los
   declara «no leídos», pero están en la misma guía ya usada: tabla 2 de EPI frente al choque eléctrico
   (UNE-EN 60903 guantes; clase 00 hasta 500 V c.a. / 750 V c.c.; clase 0 hasta 1 kV c.a. / 1,5 kV c.c.;
   clases 1 a 4 para AT; UNE-EN 50365 cascos; UNE-EN 60900 herramientas manuales hasta 1000 V c.a.). Ampliar
   4.2 (o 3.4) con lo mínimo para BT y retirar la línea correspondiente de «Lo que este tema no da».

## Preguntas

12 enteras, 1 a medias (2: hallazgo 3), 2 no (9 y 10: lagunas 1 y 2). Detalle en `27-T15-preguntas.md`.
