# Verificación · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`
(10.994 palabras tras la verificación, 37 epígrafes; ficha a «11.000»). Fuentes releídas el
05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»).

Ficheros tocados: el tema y este informe. En el scratchpad: copia previa del tema (`t12.bak`) y dos
guiones de cotejo literal (`lit.py`, `lit2.py`).

## Lentes

- `negritas.py` contra RITE, RIPCI, guía IDAE, Modbus V1.1b3, muestra EN ISO 16484-5:2026 y KNX:
  132 negritas; 7 no casan: los dos rótulos de forma y cinco literales web, comprobados en su URL
  (abajo). 0 atribuidas a otro artículo.
- `refutar_exactitud.py` (RITE + RIPCI): 7 «no literales» que son falsos positivos: la lente ancla en
  el «artículo 11», «artículo 3», etc. que aparece cerca, pero las citas son de IT; `negritas.py` las
  encuentra literales y las he situado a mano en su IT (abajo).
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 6 siglas ED…CT, presentadas en la propia cita
  literal (no es error). `indice.py`: índice correcto.

## Copiado de RTVE sin cambios: sólo literalidad

Cotejo automático (párrafo y fila de tabla, sin negritas) contra
`temas/ing-tec-industrial/13-control-automatizado-de-instalaciones.md`: los pasajes listados en 1.1,
1.2, 1.4, 2.2, 2.3, 3.1, 3.2 y 7.5 son literales, incluidas las frases de entrada sueltas («Cuatro
niveles…», «Ésta es la parte…», «El lazo de control clásico…», «El «punto» es la unidad…»). No
re-verificados. Lo adaptado (separación de sistemas, reserva de puntos, entradas de señales y
protocolos, tendencia a red de datos, limitación/rotación, entrada y cierre de 7.5) es oficio
declarado, sin cifras ni normas; nada que quitar.

## Comprobado en la fuente (confirmado)

- RITE (BOE-A-2007-15820, volcado 05-10-2026; última redacción en el .tsv 01-07-2021,
  BOE-A-2021-4572): art. 2.1, 12.3, 25.3; IT 1.2.4.3.1 ap. 1 y 3; IT 1.2.4.3.5 ap. 1 (290 kW,
  «deberán», letras a-c, UNE-EN 15232-1), 2 («podrán») y 3; IT 1.2.4.4 ap. 2-7 (70 kW, 20 kW,
  arrancadas); IT 1.2.4.5.1; IT 1.3.4.1.2.2 p) i.; IT 2.3.4 ap. 1-4; IT 3.3 pie de tabla 3.1
  (2 años); IT 3.4.2 tabla 3.3; IT 3.4.4 ap. 2 (cinco años); IT 3.4.5; IT 3.6 ap. 2; IT 3.7 a), b),
  e); IT 4.3.4; apéndice 1 (definición y cuatro niveles); apéndice 2 (UNE-EN 15232-1:2018 y UNE-EN
  ISO 16484-3:2006 con sus títulos).
- RIPCI (BOE-A-2017-6606): anexo I, sección 1.ª, apartado 1 («Sistemas de detección y de alarma de
  incendios»), punto 7: las dos frases literales. Sección 1 en redacción de BOE-A-2025-7190
  (10-05-2025); la modificación de 04-09-2025 sólo toca el anexo III.
- Guía IDAE (2007, ATECYR/AMICYF, ISBN 978-84-96680-06-7): operaciones 37, 39, 42 (autómata) y 48-97
  (DDC), número, texto y frecuencia uno a uno; el 85 repetido; secciones A-G (puesto central,
  controladores distribuidos, unidades terminales, alarmas, integraciones, telegestión); ficha de la
  familia 23, seis columnas ED…CT, puntos del ejemplo («Varios»); apéndice III (M, T, 2 A, A);
  apartado 5.3.1 (procedimiento diario); 5.4 (datos nominales).
- Modbus V1.1b3 (26-04-2012): §1.1 (definición, petición/respuesta, puerto 502, TCP/IP y serie por
  cable, fibra o radio) y §4.3 (cuatro tablas).
- EN ISO 16484-5:2026 (muestra iTeh): octava edición 2026-08, sustituye a EN ISO 16484-5:2022; tipos
  de objeto, capítulo 13 y AcknowledgeAlarm, MS/TP, anexos J y U. Objeto («The purpose…»): ficha de
  iTeh, leída el 05-10-2026, literal.
- NIST CSRC, glosario «SCADA» (SP 800-82r3): literal, incluido «delays, data integrity». El NIST la
  toma de otro diccionario: el tema dice ahora que la «recoge», no que la «define».
- knx.org/explore-knx/what-is-knx: las dos expresiones, literales.

## Correcciones aplicadas

1. Error 1 (cita cruzada), 1.3: «protocolo abierto (epígrafe 2.3)» → 2.2, donde están los protocolos.
2. Error 8 (precepto mal numerado): el tema citaba «IT 1.2.4.3.5.1», «IT 1.2.4.3.5.2»,
   «IT 1.2.4.3.1.3», «IT 2.3.4.4» e «IT 3.4.4.2», numeraciones que el RITE no tiene (él escribe
   «apartado 1 de la IT 1.2.4.3.5», IT 4.3.4). Cambiadas a «apartado N de la IT X» en 1.3, 2.2,
   2.4, 4.1, 4.3, 5.2, 5.3, 6.1, 7.1, normativa y trazabilidad.
3. Error 6/9, 5.2 (IT 3.4.5): «su exhibición en un sitio visible es obligatoria sólo en…» mezclaba
   dos frases. La norma: la información «estará disponible en un sitio visible…» y su «publicidad»
   es obligatoria en los recintos del «apartado 2 de la I.T. 3.8.1.2» (sic en el RITE; se avisa) de
   más de 1.000 m².
4. Error 6, 2.3: IT 1.2.4.5.1 ap. 5 permite justificar el incumplimiento por dificultad; añadido.
5. Error 6, 6.1: la ampliación a 2 años exige seguridad y eficiencia garantizadas; añadido.
6. Error 6, 5.1: las pérdidas de presión de la tabla 3.3 son sólo «en plantas enfriadas por agua»;
   y la primera medida, al inicio de la temporada. Añadido.
7. Error 9, 2.4: clave «2.A» = «dos veces al año o dos veces por temporada» (no «por temporada»).
8. Error 9, 7.2: el procedimiento se acuerda «con la propiedad o el usuario»; la cita, cortada a
   media frase, lleva ahora «[…]».
9. Error 5: siglas presentadas y nunca usadas (E/S, PMP, IEC) quitadas.
10. Ficha: añadidos IT 3.6, IT 3.7 y el apéndice 2, que el tema cita; extensión 11.000.

## Sin cambios, a la vista del refutador

- «Apartado 1.7» del anexo I, sección 1.ª, del RIPCI: es el punto 7 del apartado 1; la forma se
  mantiene igual que en el tema 11.
- Lo de oficio (prioridades, histéresis, pasos, casos, conflictos) va declarado como tal; no se ha
  encontrado en ello cifra ni nombre de norma sin fuente.
