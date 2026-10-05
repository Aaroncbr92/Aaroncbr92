# Redacción · Oficial Técnico Electricista (27) · Tema 8 · Instalaciones eléctricas en centros de producción audiovisual, CPD, centros emisores y UM

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/08-instalaciones-electricas-en-centros-audiovisuales-cpd-emisores-y-um.md`
(10.507 palabras según `indice.py`, 50 epígrafes). Material: `27-investigacion-B-alimentacion-instalaciones.md`
(§8 entero). Reuso RTVE (50 %, actualizar: no): `teitse/07` §7, `teitse/08` §6, `teitse/12` §6,
`tese/17` §4, `tese/15` §4. Fecha declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy
es 24-09-2026»). Escrito por partes (cabecera; 1-3; 4-7; 8-10; 11; cierre), guardando cada una.

Lentes corridas: `indice.py` (índice generado); `refutar_prosa.py` (1 hallazgo: «CPD» en el título
del tema, antes de las siglas; igual que en los temas 6 y 7, se deja); `negritas.py` contra
BOE-A-2002-18099 y BOE-A-2016-4442 (95 negritas cotejadas; las 14 que no están son rótulos y las
citas de AENOR y TÜV NORD, que no son del BOE; las 3 «atribuidas a otro artículo» son falsos
positivos: el artículo que nombra el tema al lado es el correcto, 2 y 19).

Ficheros tocados: el tema (nuevo) y este informe. El volcado de BOE-A-2016-4442 se hizo en el
scratchpad, no en `fuentes/`.

## Estructura

Epígrafes en el orden del enunciado: primero los siete lugares (1 centros de producción; 2
estudios; 3 salas de control; 4 CPD; 5 racks; 6 centros emisores; 7 UM), luego las cuatro
exigencias (8 continuidad; 9 redundancia; 10 ruido eléctrico; 11 CEM); normativa; lo que no da;
trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- RD 186/2016 (`boe.py precepto BOE-A-2016-4442`): art. 1, 2 (vig. 25-06-2024), 3 (vig.
  30-05-2026), 4, 5, 6, 7, 18, 19 y anexo I. Lo nuevo frente a la investigación: art. 6, 7.2
  (marcado CE del fabricante), 18.1 y 18.2 (precauciones de instalación; restricción residencial)
  y el párrafo de exención del 19.1 (arts. 6-12 y 14-18 no obligatorios para un aparato hecho
  para una instalación fija concreta). Confirmado que las «buenas prácticas documentadas» están
  en el 19.1, párrafo cuarto.
- ITC-BT-18 (redacción vigente desde 23-05-2010, RD 560/2010): apdos. 5, 6, 7, 10 y 11. Nuevo.
- ITC-BT-19: 2.2.2, 2.4, 2.5. ITC-BT-20: 2.1 y 2.1.1 (el 3 cm está en 2.1.1; la separación
  MBTS/MBTP, en 2.1 «Prescripciones Generales»). Coinciden con la investigación.
- ITC-BT-23 entera: apdos. 1, 2.1, 2.2, 3, 3.2, tabla 1. Nuevo.
- ITC-BT-28: apdos. 1, 2, 4 y 5. ITC-BT-34 (título y campo) e ITC-BT-29 (título). ITC-BT-44, 3.1.
- UNE-EN 50600 y TÜV NORD: de la investigación (8.3), sin releer.
- RD 299/2016 (exposición a campos): `boe.py` devolvió 404; no se cita, se remite al tema 19.

## Avisos para el verificador

- ITC-BT-19 2.2.2 dice «debidas cargas» (sin «a»); se cita literal con «(«debidas cargas», así en el BOE.)».
- 1.2: que un plató con público caiga en la ITC-BT-28 por la cláusula de más de 100 personas, y que
  la UM sea «instalación móvil» del RD 186/2016, van como lectura de aplicación, no como texto.
- 2.1: la lectura «escenario» = plató, declarada como lectura.
- 11.4: que a la UM se le aplique el régimen de aparatos y no el del anexo I.2 es lectura del art. 3.2.
- 10.2: la suma de los armónicos múltiplos de tres en el neutro va como física de circuitos, sin
  fuente leída. Si el verificador lo exige con fuente, se puede dejar sólo la cita del REBT.
- Quitado del reuso por no confirmado: la fila «aparcamiento ... proyecto sin límite de potencia
  si tiene ventilación forzada» de teitse/08 §6 (ITC-BT-04 no releída); se deja sólo lo de la
  ITC-BT-28 (más de 5 vehículos).

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur, y `27-args.json` no
marca repetición para el tema 8.

## Copiado de RTVE sin cambios

Sólo se han quitado las negritas y las mayúsculas de énfasis (en RTVE son de énfasis, no de
literal de fuente). Ninguno cita norma. Comprobado por script (texto normalizado contenido en el
fichero RTVE).

De `teitse/07` §7 (en 1.1):
- La fila «Flexibilidad» de la tabla de tres exigencias.
- Reglas 1 («Separar los circuitos de fuerza … no debe verse en la señal.») y 3 («Dejar reserva: …
  obliga a una obra.»).

De `teitse/08` §6 (en 1.2):
- «la pregunta correcta ante cualquier instalación no es «¿qué dice el reglamento?», sino «¿qué
  instrucción particular le alcanza?». Aplicar sólo la general a un local que tiene la suya es el
  error de proyecto más caro del oficio.»

De `teitse/12` §6 (en 4.2):
- La tabla de las cuatro decisiones (cuatro filas).
- «Pedirle horas a una batería … y el escenario hay que escribirlo.»

De `tese/17` §4 (en 7.2):
- Los tres pasos numerados («Se cuentan los contactos…», «Se mira la intensidad…», «Se mira la
  posición de la chaveta y el color…»).
- Filas «2 polos más tierra (3P)» y «3 polos más tierra (4P)» de la tabla de la familia.
- «La comprobación previa obligada es que haya conductor de protección y que el diferencial de
  cabecera actúe.»

De `tese/15` §4 (en 10.3):
- Filas 50 Hz, 100 Hz, silbido agudo y siseo de banda ancha de la tabla de frecuencias.
- «si el zumbido cambia al tocar o mover los cables de señal, es un bucle de masa; si no cambia, es
  la fuente.»

Adaptado (se verifica): el resto de la tabla de teitse/07 §7 y su regla 2 (quitadas remisiones a
los temas 2, 11 y 12 de RTVE); el párrafo de la autonomía de teitse/12 §6 («este temario declara
como suya», «temas 11 y 12»); la tabla de emplazamientos de teitse/08 §6, rehecha sobre la
ITC-BT-28, 29 y 34 releídas; la fila 4P de tese/17 (quitada la marca ✔ de la pregunta de RTVE), su
párrafo de aviso (quitada la remisión al «epígrafe 2») y su entrada («La pregunta 6…», quitada);
la fila «crujido» de tese/15 (quitado «del epígrafe anterior»), la regla de diagnóstico reescrita y
la respuesta a la pregunta 29 de RTVE, quitada.

## Preguntas de control (10, contestadas sólo con el tema)

1. Según la ITC-BT-19, los dispositivos de protección de cada circuito estarán coordinados y serán
   selectivos con: a) los del cuadro secundario siguiente; b) **los dispositivos generales de
   protección que les precedan**; c) el interruptor de control de potencia; d) los del SAI.
   → b. Tema 1.3 y 8.3. Entera.
2. En un local de pública concurrencia, las líneas de alumbrado de las dependencias con público se
   disponen de modo que el corte de una no afecte a más de: a) la mitad; b) **la tercera parte**;
   c) la cuarta parte; d) un 15 % de las lámparas. → b. Tema 2.1 (ITC-BT-28, 4.d). Entera.
3. Un plató de 400 m² útiles no incluido en las listas de la ITC-BT-28, ¿le alcanza esa
   instrucción? a) No, sólo a cines y teatros; b) **Sí: 400/0,8 = 500 personas, más de 100**; c) Sólo
   si tiene más de 300 personas; d) Sólo si tiene suministro de socorro. → b. Tema 1.2. Entera.
4. Los ordenadores y equipos electrónicos muy sensibles de una sala de control pertenecen a la
   categoría de sobretensión: a) IV; b) III; c) II; d) **I, con 1,5 kV de tensión soportada a
   impulsos en 230/400 V**. → d. Tema 3.1. Entera.
5. La serie UNE-EN 50600 define para el sistema eléctrico de un CPD: a) tres niveles Tier; b)
   **cuatro clases de disponibilidad, de una sola vía (AC1) a varias vías tolerantes a fallos salvo
   en mantenimiento (AC4)**; c) dos clases, N y 2N; d) cinco categorías de conmutación. → b. Tema
   4.1 y 9.2. Entera.
6. (Práctica) Un rack con dos PDU A/B lleva cada una al 70 % de su capacidad. Si cae la rama A:
   a) no pasa nada, los equipos tienen dos fuentes; b) **la rama B tendría que llevar el 140 % y
   se dispara o cae: cada rama no debe pasar en normal de la mitad**; c) el STS reparte la carga;
   d) salta el diferencial de la rama A. → b. Tema 5.1. Entera.
7. Un centro emisor alimentado por una línea aérea de conductores desnudos: a) está en situación
   natural; b) **se considera necesaria protección contra sobretensiones de origen atmosférico en el
   origen de la instalación**; c) sólo necesita pararrayos; d) la ITC-BT-23 no se le aplica por ser
   equipo radioeléctrico. → b. Tema 6.1. Entera.
8. (Práctica) La acometida de una UM que requiere tres fases, neutro y conductor de protección a
   400 V se hace con un conector industrial: a) azul de 3 polos; b) rojo de 4 polos; c) **rojo de 5
   polos (4 polos más tierra)**; d) amarillo de 5 polos. → c. Tema 7.2. Entera.
9. (Práctica) Aparece un zumbido de 50 Hz en un control que cambia al mover los cables de señal.
   Lo más probable y la actuación correcta: a) condensador de filtrado; cambiar la fuente; b) **bucle
   de masa; comprobar que los equipos unidos por señal comparten referencia de tierra y buscar un
   neutro unido a tierra aguas abajo, sin cortar nunca el conductor de protección**; c) ruido
   térmico; bajar la ganancia; d) armónicos; reducir el neutro. → b. Tema 10.3 y 5.2. Entera.
10. Según el Real Decreto 186/2016, la conformidad de una instalación fija y su mantenimiento es
    responsabilidad de: a) el instalador autorizado; b) el fabricante de cada aparato; c) **el
    propietario y, en su caso, el titular de la instalación**; d) la comunidad autónoma. → c. Tema
    11.3. Entera.

Reparto: centros de producción y continuidad (1), estudios (2, 3), salas de control (4), CPD (5),
racks (6), centros emisores (7), UM (8), ruido (9), CEM (10); redundancia en 5 y 6. Las diez se
contestan enteras con el tema; no ha hecho falta ampliar. Otras que el tema también contesta y
quedan para la fase 4: N+1 frente a 2N (9.1), qué prevalece en una tierra a la vez funcional y de
protección (5.2), sección del neutro con cargas no lineales (10.2), los 3 cm de la ITC-BT-20 y por
qué no son de CEM (10.4), definición de inmunidad (11.1) y exclusión de los equipos radioeléctricos
(11.1).
