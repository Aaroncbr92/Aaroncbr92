# Puesto 27 · Oficial Técnico Electricista · Tema 4 · Fase 3, verificación

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas). Tema verificado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/04-canalizaciones-conductores-y-cableado.md`
(13.929 palabras según `indice.py` tras las correcciones, 45 epígrafes; 13.638 antes; ficha
actualizada a «unas 13.900»).

Ficheros tocados: sólo el tema y este informe. Los demás temas del puesto que `git status` da como
modificados no son de esta fase.

## Lo copiado: nada que saltar

`27-T04-redaccion.md` lista «Copiado del común: nada» y «Copiado de RTVE sin cambios: nada» (reuso
teitse/04, 05 y 07 marcado «actualizar: sí» y adaptado). No había pasajes que cotejar sólo por
literalidad: se verificó el tema entero, incluido todo lo tomado de RTVE.

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` | 05-10-2026 | Art. 15.3 (nuevo); ITC-BT-01 (cada definición); ITC-BT-02 (vig. 04-04-2025, BOE-A-2025-6773): cada título citado y notas (4), (7), (10), (12), (20)-(22); ITC-BT-07 leyenda «Tipo de aislamiento» y 2.1.3.1; ITC-BT-14, 3; ITC-BT-15, 3 (incl. caídas b); ITC-BT-17, 1.3; ITC-BT-19, 2.2.1-2.2.4, 2.3, 2.6, 2.10, 2.11; ITC-BT-20 entera con tablas 1 y 2 fila a fila; ITC-BT-21 1.1-4.1 con tablas 1-6 y 8 y filas de 2 y 5; ITC-BT-22, 1.1; ITC-BT-24, 3.2; ITC-BT-27, 3; ITC-BT-28, 4 y 5.b; ITC-BT-30 entera; ITC-BT-44, 3.1; ITC-BT-47 (125 %) |
| Rúbricas «Redacción aplicable» del volcado | 05-10-2026 | Una sola redacción (2002, desde 18-09-2003) en art. 15 y en todas las ITC citadas salvo ITC-BT-02: la ficha es correcta |
| Temas 1, 3 y 8 del puesto (sólo rótulos) | 05-10-2026 | Que existen los epígrafes remitidos: tema 1, 2.4 y 8.3; tema 3, 1.4; tema 8, 7.2, 9.4 y 10.2 |

## Lentes

- `negritas.py` (REBT): 190 negritas; 2 «no están» (rótulos de plantilla); 0 atribuidas a otro
  artículo. Como no ancla en apartados de ITC, cada negrita se localizó con un guion propio (línea
  del volcado) y se leyó bajo el rótulo de su apartado: todas en el apartado que dice el tema.
- `refutar_exactitud.py`: 19 «no literales», falsos positivos (lee «apartado N» de una ITC como
  «art. N»), cotejados a mano. `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 45.
- Recuentos («tres reglas», «cuatro reglas», «nueve pasos», «dos condiciones»…) y cálculos del
  ejemplo de 2.5 (Ib ≈ 51 A; S = 6,25 mm²; tubos de 32 mm en tablas 2 y 5; 95 → 47,5 → 50 mm²):
  cuadran.

## Correcciones aplicadas (comprobadas en la fuente antes de aplicarlas)

1. **Error 1/9** (1.10, prefabricadas): el tema decía que el listado de la ITC-BT-02 «recoge para
   ellas» la serie UNE-EN 61534. La ITC-BT-20 2.2.10 cita UNE EN 60570 (iluminación) y UNE EN
   60439-2 (uso general), y la nota (12) del listado da como referencia actual de esta última la
   **UNE-EN 61439-6** «Conjuntos de aparamenta de baja tensión. Parte 6: Canalizaciones
   prefabricadas». Reescrito; 61534 queda como «además». Normativa y Trazabilidad, con nota (12).
2. **Error 9** (1.4, tabla): fila «Libre de halógenos…: no desprende gases halogenados». El REBT
   exige «emisión de humos y opacidad reducida», no «libre de halógenos»; nada leído lo define.
   Fila renombrada con la expresión del REBT y nota de que la columna «Qué significa» es oficio.
3. **Error 9** (1.3, columna «Rasgo»: PVC y ácido clorhídrico, EPR «muy flexible»): sin fuente;
   declarada como oficio en el tema y en Trazabilidad.
4. **Error 6** (1.5, ITC-BT-27, 3): faltaba la alternativa **o mediante cable bajo tubo aislante
   con conductores aislados de tensión asignada 450/750V**. Añadida, con el apartado.
5. **Error 6** (1.8, tabla 4): +90 ºC sin la nota (1) (precableadas en obra de fábrica, +60 ºC).
   Añadida.
6. **Error 8** (1.9): la frase del número máximo de conductores en canal parecía del 4.1; está en el
   3.2 de la ITC-BT-21. Añadido «(apartado 3.2)».
7. **Error 9** (5.2.4 y «Lo que no da»): «no se ha leído un precepto» sobre tierra de bandejas. La
   ITC-BT-07 2.1.3.1 sí manda unir al conductor de tierra las bandejas de galerías visitables de
   redes subterráneas. Precisado que para instalación interior no hay equivalente en las ITC leídas.
8. **Error 3** (8.2, tabla de la sala de baterías): «Lo que sigue a esos dos puntos» daba 6 de las
   8 exigencias del apartado 7. Añadidas iluminación, aislamiento suplementario de los acumuladores
   y la sustitución fácil de cada elemento (literales).
9. **Error 9 menor** (2.3): «facilita la empresa distribuidora (artículo 15.3)»; el artículo dice
   **compañías suministradoras** y **valores máximos previsibles**. Cita literal; art. 15.3 añadido a
   ficha, Normativa y Trazabilidad.
10. **Error 5 inverso** (siglas): «HD» se presentaba y no se usaba. Quitada.

## Comprobado sin cambios

Definiciones de la ITC-BT-01; tabla 1 de la ITC-BT-20 celda a celda y las tres lecturas de la tabla
2; 2.1 y 2.1.1-2.1.3; tensiones asignadas por sistema (ITC-BT-15, 20, 21, 28); temperaturas de la
ITC-BT-07; reacción al fuego de ITC-BT-14, 15 y 28 4.f; tablas 1, 3, 4, 6 y 8 y filas de las 2 y 5
de la ITC-BT-21; 2,5/3/4/4 veces y «más de 10» en enterrados; registros, cajas, fijaciones, rozas,
montaje al aire; canales 3.1 y 4.1; molduras; 2.2.2-2.2.10; pasos (3); caídas de ITC-BT-19, 14 y
15; secciones mínimas; tabla del conductor de protección y sus reglas; colores; ITC-BT-19 2.6, 2.10
y 2.11; ITC-BT-24 3.2; ITC-BT-30 1-5, 8 y 9; ITC-BT-44 3.1; 125 % (ITC-BT-47) y 1,8 (ITC-BT-44) de
2.5. Las negritas de «baterí as» y «debidas cargas» son así en el BOE.

## Para la refutación

- La tabla 1 de la ITC-BT-19 (Iz) no está en el volcado; el tema lo declara.
- «Sala técnica» como local afecto a servicio eléctrico, y el falso suelo como hueco de la
  construcción, van como lectura, no como texto: comprobar que no se presentan como norma.
