# Puesto 27 · Oficial Técnico Electricista · Tema 5 · Fase 3, verificación

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas: las ITC citadas tienen su última redacción en 2003, 2010, 2015 o 2025). Tema
verificado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/05-puestas-a-tierra-y-equipotencialidad.md`
(12.928 palabras según `indice.py` tras las correcciones; 12.655 antes; ficha actualizada a «unas
12.900»; 37 epígrafes, índice sin cambios).

Ficheros tocados: sólo el tema y este informe. Los demás ficheros del puesto que `git status` da como
modificados no son de esta fase.

## Lo copiado: nada que saltar

`27-T05-redaccion.md` lista «Copiado del común: ninguno» y «Copiado de RTVE sin cambios: ninguno»
(teitse/03, teitse/09 y tese/15 están marcados «actualizar: sí»). No había pasajes que cotejar sólo
por literalidad: se verificó el tema entero, incluido todo lo tomado de RTVE (adaptado).

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado del 05-10-2026 y `.redacciones.tsv` | 05-10-2026 | ITC-BT-01: las 17 definiciones citadas y la entrada «masa» completa; ITC-BT-03 (5 redacciones, vig. 04-09-2025, BOE-A-2025-17507), apéndice I, 2.1.2; ITC-BT-05 (vig. 30-06-2015, BOE-A-2014-13681), 2.1, 3, 4.1, 4.2, 6.2; ITC-BT-08 entera; ITC-BT-18 entera (vig. 23-05-2010, BOE-A-2010-8190), incluidas tablas 1 a 5; ITC-BT-19, 2.2.4, 2.3, 2.9; ITC-BT-24 entera (1 a 4.5); ITC-BT-26, 1, 3.1, 3.2, 3.4; ITC-BT-27, 2.2; ITC-BT-28, 2.1; ITC-BT-38, 2.1.3. Redacción única salvo ITC-BT-03, 05 y 18 |
| RD 337/2014 (BOE-A-2014-6084), disposición derogatoria única, con `boe.py precepto` («vigente hoy», 1 redacción, vig. 09-12-2014) | 05-10-2026 | Derogación del RD 3275/1982 y su salvedad |
| INSST, guía técnica de riesgo eléctrico, Madrid, septiembre 2020 (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`, líneas 30-36, 2552-2650) | 05-10-2026 | Tensión de paso (literal, con guion blando en la línea 2619), atribución a la ITC-RAT 01 (línea 2554), cuadro 5 (césped «300 a 500»), frase de las tensiones «tanto menores» (2648) |

## Lentes

- `negritas.py` (REBT, guía INSST, RD 337/2014): 257 negritas; 2 «no están» (los dos rótulos de
  plantilla); 0 atribuidas a otro artículo. Como la lente no ancla en apartados de ITC, cada cita se
  leyó bajo el rótulo de su apartado: todas en el apartado que dice el tema.
- `refutar_exactitud.py`: 18 «no literales», falsos positivos (lee «apartado N» de una ITC como
  «art. N»); cotejadas a mano. `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 37 epígrafes.
- Cálculos rehechos: RA máximas 1.667/800/167/80/50/24 Ω; picas 25 y 250 Ω; anillo 10 Ω; placa
  13,3 Ω; 460 A en TN. Cuadran.

## Correcciones aplicadas (comprobadas en la fuente antes de aplicarlas)

1. **Error 9** (Trazabilidad): «4.ª ed.» de la guía del INSST no consta en el `.txt` (sólo «Edición:
   Madrid, septiembre 2020», NIPO). Quitado.
2. **Error 9** («Lo que no da»): el «proyecto de reforma del REBT anunciado para 2026 por colegios
   profesionales» no tiene fuente guardada ni citada (mismo hallazgo que la verificación del tema 3).
   Sustituido por lo confirmado: ninguna reforma posterior al 18/12/2025.
3. **Error 3, recuento** (4.1): «enumera … cuatro que son de este tema» y luego suma tres más.
   Reescrito: siete defectos que tocan el tema (cuatro + tres). **Error 6**: añadido «con carácter no
   exhaustivo».
4. **Error 3** (5.4): «Tres plazos y tres sujetos», pero el tercer sujeto «no lo precisa» el apartado
   12. Reescrito sin el recuento de sujetos.
5. **Error 6** (6.2, TN): faltaba la salvedad de la UNE 20.460-4-41 para tiempos de interrupción
   mayores. Añadida literal.
6. **Error 6** (6.2, IT segundo defecto): faltaban los tiempos superiores de hasta 5 s y el recurso a
   diferencial por aparato o equipotencial complementaria. Añadidos.
7. **Error 6** (3.4, aislamiento): los ≥ 0,5 MΩ se daban sin la condición de los 100 m de
   canalización de la ITC-BT-19, 2.9. Añadida.
8. **Error 6** (5.3): la derogación del RD 3275/1982 se daba sin «sin perjuicio de su aplicación en
   los términos de la disposición transitoria primera.1». Añadida; RD 337/2014 añadido a Trazabilidad.
9. **Error 6** (1.1): la cita de «masa» se cortaba en «Clase II» y omitía el resto de la frase
   (armaduras de cables, conducciones). Completada; señalada la errata «condiciones» del BOE.
10. **Error 6** (1.3): envolventes de plomo; paráfrasis «poco sensibles a la corrosión» sustituida
    por la letra («que no sean susceptibles de deterioro debido a una corrosión excesiva») y añadida
    la advertencia al usuario.
11. **Error 4/9** (2.2, tabla resumen IT): «Un controlador permanente de aislamiento avisa» como si
    fuera siempre exigible; la ITC-BT-24, 4.1.3 dice «Si se ha previsto». Corregido, con la exigencia
    de la ITC-BT-28 para servicios de seguridad.
12. **Error 9/8** (2.3, ITC-BT-38): la ITC exige **transformadores de aislamiento o de separación de
    circuitos, como mínimo uno por cada quirófano**; el dispositivo de vigilancia va en el cuadro.
    Citado literal con su apartado 2.1.3; Normativa y Trazabilidad ya no dicen «sólo el término».
13. **Error 9** (7.1): «una toma de tierra separada … que no cumpla la independencia del apartado 10
    … no es admisible» no sale de ninguna fuente (y sugería que una independiente sí lo sería).
    Reescrito con lo que dan la ITC-BT-18, 3.3 y 6.
14. **Error 9** (6.2 TT; 7.1 punto 5): la extensión al grupo electrógeno y la razón de unir fases y
    neutro al medir aislamiento eran lectura propia presentada como de la norma. Marcadas como oficio.
15. **Error 6** (5.1): añadida la regla de los dispositivos en serie de la ITC-BT-24, 4.1.2.
16. **Precisión** (5.3): «máxima corriente de defecto del lado de alta tensión» por la letra del
    apartado 11 («máximo valor previsto de la corriente de defecto a tierra (Id) en el centro de
    transformación»).
17. **Precisión** (1.7): lista de la ITC-BT-27, 2.2 completada (desagües; volúmenes 0 a 3);
    «vestuarios de cualquier centro de trabajo» → «de muchos» (oficio, no norma).

## Comprobado sin cambios

Ficha (redacciones y fechas de vigencia, contra `.redacciones.tsv`); siglas; todas las citas de la
ITC-BT-18 (tablas 1 a 5 valor a valor, erratas «5.00», «mas seco», «las corriente» y nota de la fila
sin protección contra la corrosión); ITC-BT-08 entera con los 5 y 2 Ω; ITC-BT-24 (MBTS, IP XXB,
IP4X/IP XXD, 30 mA, tablas 1 y 2, condiciones TN/TT/IT, 50/100 kΩ, 4.4, 4.5); ITC-BT-05 (inspección
de pública concurrencia, 5 años, definición de defecto grave); ITC-BT-03 (seis equipos, 1 mA,
0,1 Ω, «ITC MIE-BT 19»); ITC-BT-19 (colores, 2.3, 2.9); ITC-BT-26 (ámbito, 3.1, 3.2, 3.4); ITC-BT-28,
2.1; tensión de paso de la guía INSST. Lo marcado como oficio (método de las dos picas, pinza,
continuidad, zumbido 50/100 Hz de tese/15, reglas de sala) va declarado como tal y no se atribuye a
norma.

Cero hallazgos de cita cruzada (error 1), ley por reglamento (2), redacción derogada como vigente (7)
o artículo mal (8) en las citas literales. Cada pasaje cambiado se releyó: sus antecedentes («esa
frase», «el mismo apartado») están delante.
