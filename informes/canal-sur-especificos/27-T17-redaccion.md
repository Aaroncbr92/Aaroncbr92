# Redacción · Oficial Técnico Electricista (27) · Tema 17 · Planificación de intervenciones en instalaciones críticas

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/17-planificacion-de-intervenciones-en-instalaciones-criticas.md`
(unas 9.800 palabras según `indice.py`, 44 epígrafes con índice). Material: `27-investigacion-D-mantenimiento.md`
(§0, §1.2, §1.4, §2, §5, §6). Reuso RTVE (20 %, actualizar: no): `teitse/09` §4 y §6, `tese/16` §1 y §2.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguno de los preceptos citados cambió entre ambas fechas). Escrito por partes,
guardando cada una: cabecera; epígrafe 1; 2; 3; 4; 5; 6; 7; 7.6; cierre (normativa, lo que no da,
trazabilidad).

Lentes corridas: `indice.py` (índice generado; portada manual, como en los temas 3, 8, 13 y 14);
`refutar_prosa.py` (1 sigla sin presentar, AENOR: quitada del cuerpo; 0 al final); `negritas.py`
contra BOE-A-2011-7630, BOE-A-1995-24292, BOE-A-1997-17824, BOE-A-1997-1853, BOE-A-2001-11881,
BOE-A-2007-6237, BOE-A-2007-15820, BOE-A-2023-14679, el X Convenio (txt) y la investigación D (para
los títulos de catálogo UNE/ISO): 65 negritas; 5 «no está»: 2 rótulos de forma («Enunciado del
programa», «Qué se puede preguntar») y 3 citas con elisión «[…]» dentro del párrafo copiado del
tema 32-14 (copiado del común; no se re-verifica). 0 atribuidas a otro artículo.

## Ficheros tocados

- El tema (nuevo) y este informe.
- `fuentes/canal-sur/BOE-A-2011-7630.md` y `.redacciones.tsv`: volcado nuevo de la Ley 8/2011
  (`boe.py norma`), para el cotejo de negritas.

## Estructura

Epígrafes en el orden del enunciado: 1 planificación de intervenciones en instalaciones críticas
(qué es crítica, Ley 8/2011 como vocabulario; reparto de tareas según el convenio; ciclo de ocho
fases; definir la intervención y condiciones previas del RD 1215/1997 y del RD 614/2001); 2
análisis de impacto (cinco preguntas, interdependencias, orden de prioridades, redundancia
consumida, ISO 22301/22313 sólo catálogo, ejemplo); 3 ventanas (datos, elección, qué va en
ventana, ensayos con carga, duración y punto de no retorno); 4 coordinación con producción (quién
decide, qué se pacta, recurso preventivo por concurrencia, permisos); 5 comunicación de incidencias
(dos clases, LPRL 29.2.4.º y NBA 3.3.3.c, tres momentos, guardias del convenio, registro); 6 planes
de contingencia (dos niveles, NBA como modelo, vuelta atrás y RITE IT 2.3.4.4, niveles de
redundancia, probar); 7 retorno al servicio (RD 614 anexo II.A.2, RD 1215 art. 4, secuencia de
ocho pasos, cierre, caso completo). La CAE, las cinco reglas, la consignación, N/N+1/2N, las
pruebas de grupo y SAI se remiten a los temas 15, 8 y 7, que ya remitían al 17 la ventana pactada
y el retorno al servicio.

## Fuentes leídas por el redactor (05-10-2026)

Releídas en el BOE consolidado (`boe.py precepto`), no sólo en la investigación:
- Ley 8/2011, art. 2 (redacción única; norma no derogada según metadatos de la API del BOE).
- LPRL, art. 29.2.4.º (redacción única).
- RD 39/1997, art. 22 bis, apartados 1 y 2 (redacción del RD 604/2006, BOE-A-2006-9379).
- RD 1215/1997, art. 4 (redacción única) y anexo II.1.14 (redacción RD 2177/2004).
- RD 614/2001, anexo II, A y A.2 (redacción única).
- RD 393/2007: nota de derogación del bloque «no» (BOE-A-2023-14679); Norma, 3.3.3, 3.6.4 y 3.7;
  anexo II, capítulos 5 a 9.
- RITE, IT 2 (bloque `it2-2`), IT 2.3.4 apartado 4 (redacción única, vigente desde 29-02-2008).
- X Convenio (txt): art. 50.11 (plus por guardia localizable), anexo III, puestos 9311100, 9311200
  y 9300000.
- Fichas de catálogo UNE-EN ISO 22301:2020 y 22313:2020: sólo de la investigación (iso.org/une.org
  dan 403 desde aquí); se citan como metadatos.

## Avisos para el verificador y para el coordinador

- **Corrección a la investigación (manda la fuente).** La investigación (§2.3) dice que el RD
  393/2007, anexo II, está «vigente; sin cambios desde 2022». El BOE consolidado anota: «Norma
  derogada, con efectos de 11 de julio de 2023, por la disposición derogatoria única.2.d) del Real
  Decreto 524/2023 […] No obstante, la Norma Básica continuará aplicándose hasta tanto sea aprobado
  el nuevo instrumento de planificación que la sustituya». El tema lo dice (párrafo copiado del
  tema 32-14, que ya lo había resuelto). **El tema 13 de este puesto cita el RD 393/2007, anexo II,
  capítulo 5, como «redacción única» sin ese aviso** (portada, l. 9-10; 6.2; 9.1): conviene añadirlo
  en su verificación. No lo he tocado.
- La Ley 8/2011 se usa sólo como vocabulario; el tema dice expresamente que no consta que una
  instalación de la RTVA sea infraestructura crítica.
- RD 39/1997, 22 bis.2: la frase citada empieza «la evaluación de riesgos…» dentro de «En el caso al
  que se refiere el párrafo a) del apartado anterior, …»; el tema la introduce con «El mismo
  artículo dispone que, en ese caso,».
- Convenio: «Mantener en condiciones optimas» va sin tilde, como en la fuente.
- 7.2: «trabajadores autorizados» en negrita es literal del anexo II.A del RD 614/2001.
- Ejemplos de estudio declarados como oficio y sin cifras: 2.5 y 7.6 (SAI 2N del control central).
- Extensión: más larga que lo que pedía la investigación («corta»); todo lo que no es norma es
  oficio declarado. Si el coordinador quiere recortar, lo prescindible es 3.2 (elección de la
  ventana) y 7.6, que repite en tabla los epígrafes 2 a 7.

## Copiado del común

Del tema 14 del específico de Productor/a (`32-productor-a/14-prevencion-de-riesgos-laborales-en-la-produccion-audiovisual.md`,
cerrado), literal, en el epígrafe 6.2 del tema:
- El párrafo de la derogación de la NBA, desde «El Real Decreto 393/2007, de 23 de marzo, aprobó la
  Norma Básica de Autoprotección…» hasta «…lo que sigue es, pues, la norma que se sigue aplicando,
  formalmente derogada.» (32-14, «Presencia de público e invitados», l. 945-964, sin la
  cabecera en cursiva).
- El párrafo «El capítulo 6 del anexo II («Plan de actuación ante emergencias») clasifica las
  emergencias…» hasta «…con una periodicidad no superior a tres años.»» (32-14, «El plan de
  actuación en emergencias de la autoprotección», l. 1902-1912).

## Copiado de RTVE sin cambios

Ninguno cita norma. Sólo se han quitado las negritas y las mayúsculas de énfasis (en RTVE son de
énfasis, no de literal de fuente), y en dos pasajes se ha empezado en mitad de la frase original
(«La redundancia existe…» y «El punto caliente…», con la mayúscula inicial). Comprobado por script
(texto normalizado contenido en el fichero RTVE y en el tema).

De `tese/16` §1 (en 2.2):
- «Y la jerarquía que ordena las prioridades cuando fallan dos cosas a la vez: … una continuidad
  parada es un incidente de emisión.»
- Cuatro filas de la tabla de áreas: Continuidades, Controles técnicos y salas técnicas, Estudios,
  Postproducción de vídeo y audio (sin las de Sistemas de redacción y Sonorización, que remitían a
  temas de RTVE).

De `tese/16` §2 (en 2.3, 6.4 y 6.5):
- «La redundancia existe para que la avería no se note. Si se ha invertido … no ha servido para
  nada.» (sin «Y la regla que hay que llevar entendida, porque es la que la pregunta 25 mide:»).
- La tabla de niveles, cabecera y cuatro primeras filas (sin la de «Doble camino permanente», que
  remitía a la norma de redundancia del tema 9 de RTVE).
- «Dónde está la redundancia en una cadena de emisión típica: … se tiene repuesto de lo que sí.»
- «Una redundancia que no se prueba no existe. Una segunda fuente … hasta que caiga la primera.»

De `teitse/09` §4 (en 3.3):
- «El punto caliente y el armónico sólo existen cuando circula corriente. Una termografía hecha con
  la instalación parada no vale para nada, y es un error frecuente en un mantenimiento mal
  planificado.»

De `teitse/09` §6 (en 3.4):
- «Un grupo que arranca en vacío una vez al mes no demuestra nada; … no se sabe si funciona.»

Quitado de RTVE: las preguntas de examen de RTVE, los casos de licencias y versiones, el caso del
disco RAID y toda referencia a temas o exámenes de RTVE.

## Preguntas tipo test (10, contestadas sólo con el tema)

1. (Instalación crítica, teoría) Según la Ley 8/2011, una infraestructura crítica es la
   infraestructura estratégica: a) que figura en el plan de autoprotección; b) **cuyo
   funcionamiento es indispensable y no permite soluciones alternativas, por lo que su
   perturbación o destrucción tendría un grave impacto sobre los servicios esenciales**; c) que
   alimenta un CPD; d) de titularidad pública. → b. Tema 1.1. Entera.
2. (Análisis de impacto, teoría) En la Ley 8/2011, los efectos que una perturbación en una
   instalación produciría en otras instalaciones o servicios se denominan: a) criterios
   horizontales de criticidad; b) zona crítica; c) **interdependencias**; d) análisis de riesgos.
   → c. Tema 2.1. Entera.
3. (Análisis de impacto, aplicación práctica) Se interviene en uno de los dos SAI de un sistema 2N
   que alimenta el control central con equipos de doble fuente. Mientras dura el trabajo: a) la
   carga cae; b) la carga sigue con la misma redundancia; c) **la carga sigue alimentada por el
   otro sistema, pero sin redundancia: un fallo de la vía que queda la tira**; d) no hace falta
   ventana porque nada se apaga. → c. Tema 2.3 y 2.5. Entera.
4. (Ventanas, aplicación práctica) En una ventana en la que se va a reapretar un cuadro general,
   la termografía se hace: a) con el cuadro consignado, después de reapretar; b) **en carga, antes
   de abrir o tocar nada**; c) no se hace en ventana; d) con la instalación parada para no correr
   riesgos. → b. Tema 3.3. Entera.
5. (Ventanas, teoría) Si al llegar al punto de no retorno de una ventana el trabajo no está
   terminado: a) se sigue, y se avisa del retraso; b) se pide ampliar la ventana sobre la marcha;
   c) **se deshace lo hecho y se devuelve la instalación como estaba**; d) se deja la instalación
   en bypass hasta el día siguiente. → c. Tema 3.5 (y 6.3). Entera.
6. (Coordinación con producción, norma) En una ventana trabajan a la vez el personal propio y el
   servicio técnico externo del SAI. La presencia de recursos preventivos es necesaria, según el
   Real Decreto 39/1997, cuando: a) siempre que haya una empresa externa; b) **los riesgos puedan
   verse agravados o modificados por la concurrencia de operaciones diversas que se desarrollan
   sucesiva o simultáneamente y que hagan preciso el control de la correcta aplicación de los
   métodos de trabajo**; c) el trabajo se haga de noche; d) sólo en espacios confinados. → b.
   Tema 4.3. Entera.
7. (Comunicación de incidencias, norma) Ante una situación que entraña un riesgo, el artículo
   29.2.4.º de la LPRL obliga al trabajador a informar de inmediato: a) sólo al servicio de
   prevención; b) sólo a los delegados de prevención; c) **a su superior jerárquico directo, y a
   los trabajadores designados para actividades de prevención o, en su caso, al servicio de
   prevención**; d) a la autoridad laboral. → c. Tema 5.2. Entera.
8. (Comunicación de incidencias, aplicación práctica) Un SAI de continuidad pasa a bypass de
   madrugada y aún no se sabe por qué. Lo correcto es: a) esperar a tener el diagnóstico para no
   alarmar; b) **avisar de inmediato a quien explota la emisión, diciendo lo que se sabe y lo que
   no, y cuándo se volverá a informar**; c) reiniciar el SAI y avisar si no vuelve; d) anotarlo en
   la OT y avisar por la mañana. → b. Tema 5.3 (y 5.1). Entera.
9. (Planes de contingencia, norma) Sobre la Norma Básica de Autoprotección del Real Decreto
   393/2007, señale la correcta: a) está vigente sin cambios; b) **fue derogada por el Real Decreto
   524/2023 con efectos de 11 de julio de 2023, pero se sigue aplicando hasta que se apruebe el
   instrumento que la sustituya; exige simulacros al menos una vez al año y revisar el plan con
   periodicidad no superior a tres años**; c) fue derogada y ya no se aplica; d) exige simulacros
   cada tres años. → b. Tema 6.2. Entera.
10. (Retorno al servicio, norma y práctica) Durante la reposición de la tensión tras un trabajo sin
    tensión: a) la instalación se considera sin tensión hasta que se cierra el último interruptor;
    b) **desde que se suprime una de las medidas adoptadas para trabajar sin tensión, la parte
    afectada se considera en tensión**; c) la reposición la puede hacer cualquier trabajador; d)
    basta con reponer para dar el retorno al servicio por terminado. → b. Tema 7.2 (c falsa: 1.4 y
    7.2, trabajadores autorizados; d falsa: 7.1 y 7.4, comprobación, prueba con carga, redundancia
    repuesta y devolución). Entera.

Todas se contestan enteras con el tema; no ha hecho falta ampliar. (Otras que el tema también
contesta: quién actualiza el programa de un sistema de telegestión según el RITE, IT 2.3.4.4,
en 6.3; qué comprobaciones exige el art. 4.2 del RD 1215/1997 tras transformaciones o accidentes,
en 7.3; convocatoria mínima de una guardia localizable si hay llamada, cuatro horas, en 5.4.)
