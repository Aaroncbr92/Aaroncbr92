# 04 · Ayudante de Producción · Tema 8 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/08-apoyo-a-la-contratacion-y-relacion-con-proveedores.md`
(11.810 palabras tras la verificación; 34 epígrafes, sin cambios de rúbrica). Verificado el 06-10-2026.

Ficheros tocados: el tema y este informe. Ninguno más.

## Lo copiado: sólo comprobación de literalidad

Script de cotejo por frases y celdas de tabla (sin negritas, espacios normalizados) del tema contra
Productor T10 (`32-productor-a/10-contratacion-de-servicios-suministros-y-colaboraciones.md`).

- **Copiado del común**: todos los pasajes listados en `04-T08-redaccion.md` aparecen literales en
  Productor T10. Las frases que no coinciden son exactamente los cambios declarados por el redactor
  (Mesa sin el 326, Cámara sin 3.1.g/3.2.b, «rúbrica siguiente», 131.2 recortado, 217.2 sin la
  cita larga, «Las palabras de la ley», «descripción del encargo», frases añadidas para el
  ayudante). No se han vuelto a verificar.
- **Copiado de RTVE sin cambios**: ninguno (el redactor lo declara así; no hay nada que cotejar).

## Lo nuevo y lo adaptado: verificado en la fuente

Fuentes leídas hoy (06-10-2026):

| Fuente | Cómo | Resultado |
|---|---|---|
| RD 1619/2012, arts. 4, 6, 7, 11, 15 | `boe.py precepto` (vig. 01-07-2021, 07-12-2023, 07-12-2023, 01-01-2014, 01-01-2018); 6.5 comprobado ausente a 01-01-2023 («añadido en 2023», correcto) | Citas literales; tres salvedades omitidas (abajo) |
| Ley 25/2013, arts. 2, 3, 4 | `boe.py precepto` (2 y 3 únicos, 17-01-2014; 4 vig. 14-06-2015) | Literales; una afirmación sobre CSRTV matizada |
| ET, art. 42.1 | `boe.py precepto` (vig. 31-12-2021) | Literal |
| LCSP, arts. 64, 71, 198 | `boe.py precepto` (64 y 198 únicos; 71 vig. 22-08-2024, 7 redacciones) | Una cita no literal (64.2) y una salvedad (71.1.d) |
| LCSP, fechas de la portada | `BOE-A-2017-12902.redacciones.tsv`, los 41 artículos citados | Coinciden todas (21, 22, 318: 01-01-2026; 29, 168: 01-01-2023; 71; 217; 118; 215; resto originales) |
| X Convenio, ficha 5212705, pág. 110 | `x-convenio-rtva-boja-240-2014.txt` | Objeto, diez tareas, las cinco citadas y la cláusula de lista abierta: literales |
| Libro de estilo, 4.4.4 punto 9 | `libro-de-estilo-333233b.txt`, líneas 2733-2739 | Literal; está bajo 4.4.4 |
| Tema 17 del puesto y tema 9 del común | grep | Remisión cruzada errónea (abajo) |

## Correcciones aplicadas

1. Error 9 (cita no literal). «Conflictos de intereses»: «puede influir» entre comillas; el 64.2
   dice «pueda influir en el resultado». Corregido.
2. Error 6. 71.1.d) LCSP: la letra incluye también, para empresas de 50 o más trabajadores, la
   reserva del 2 % para personas con discapacidad y el plan de igualdad, acreditados con la
   declaración responsable del 140. Añadido.
3. Error 9. «régimen especial de las agencias de viajes (n), que es la que llevan muchos billetes y
   hoteles comprados a través de agencia»: sin fuente. Quitado; queda «cuando se aplica ese régimen
   especial».
4. Error 6 y antecedente. 6.4 del Reglamento de facturación: la cita omitía «A efectos de lo
   dispuesto en el artículo 97.Uno de la Ley del Impuesto», y «a esos efectos» no tenía
   antecedente. Restituida la cita entera; en la tabla de «Cómo se comprueba», «a efectos del 6.4».
5. Error 3/6. 7.1: la lista de lo que lleva la simplificada omitía la letra i) (menciones de 6.1
   j a p). Añadida.
6. Error 6. 15.1: omitía «sin perjuicio de lo establecido en el apartado 6». Restituido, con el
   15.6 (el canje de una simplificada correcta por una completa no es rectificativa), que toca de
   lleno los tickets del ayudante.
7. Error 9. «CSRTV ... no es Administración Pública» se afirmaba para la Ley 25/2013, cuya remisión
   es al TRLCSP derogado. Ahora se atribuye a la Cámara y se extiende a CSRTV la misma salvedad.
8. Error 6. 198.4: «Los intereses corren sólo si...» chocaba con la frase siguiente; reformulado
   como inicio del cómputo, y completada la cita («sin que la Administración haya aprobado la
   conformidad, si procede, y efectuado el correspondiente abono»).
9. Error 1 (cita cruzada). La coordinación de actividades empresariales se remitía al tema 17, que
   dice expresamente que no la da y la remite al tema 9 del común (art. 24 Ley 31/1995). Corregido
   en «La documentación del proveedor» y en «Lo que este tema no da».
10. «Trazabilidad»: añadidos el art. 64 a los releídos hoy y la relectura del punto 9 del 4.4.4.

Sin corregir, por correctos: cálculos de los supuestos (1.200 × 20 = 24.000; 1 de marzo a 15 de
abril supera 30 días y un mes); remisiones a los temas 5, 9 y 14 del puesto y al tema 5 del común.

## Lentes

- `negritas.py` (LCSP, RD 1619/2012, Ley 25/2013, ET, Ley 18/2007, convenio, Libro, Cámara): 158
  cotejadas; 14 «no está» (los mismos de la redacción: rótulos, supuestos, Libro 4.4.4 partido por
  salto de página, Reglamento de la Mesa, texto original del 118); 3 «otro artículo» falsos (26.1.b
  y 318.b en tabla; el 15.6 por «Ese apartado 6», que tiene antecedente en el 15.1).
- `refutar_exactitud.py`: 61 citas con artículo; 5 «no literales», todas falsas (las tres
  anteriores, la Cámara leída como 132 y «normas de derecho privado», que es del 319.1 y viene del
  común).
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 34 epígrafes, índice sin cambios.

## Avisos que siguen abiertos (declarados en el tema)

- Exigibilidad del 6.5 (QR, VERI*FACTU); RTVA como Administración para la Ley 25/2013 y su punto de
  entrada; reducción andaluza de plazos (198.8); RTVA como empresario a efectos del 11.1; «propia
  actividad» del art. 42 ET. Ninguno se afirma.
- La portada da 11.500 palabras aproximadamente; el tema tiene 11.810.
