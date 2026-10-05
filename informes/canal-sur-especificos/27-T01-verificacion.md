# Puesto 27 · Oficial Técnico Electricista · Tema 1 · Fase 3, verificación

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas). Tema verificado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/01-instalaciones-electricas-de-baja-tension-magnitudes-potencia-y-cargas.md`
(10.014 palabras según `indice.py` tras las correcciones; 9.867 antes).

Ficheros tocados: sólo el tema y este informe. Los demás ficheros del puesto que `git status` da
como modificados (temas 06, 07, 08, 14, 15) no son de esta fase.

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` (volcado el 05-10-2026) | 05-10-2026 | Art. 2.1 (2 redacciones; vigente desde 01-07-2021, BOE-A-2021-6879); art. 4.1, 4.2, 4.4, 4.5 y art. 16.1, 16.2 (1 redacción, desde 18-09-2003) |
| Mismo volcado, ITC-BT-09, 14, 15, 19, 43, 44, 47, 52 | 05-10-2026 | Cada cita y cada cifra, con su apartado y rótulo; redacción de cada ITC (única salvo ITC-BT-52: 3 redacciones, vigente desde 16-06-2022, BOE-A-2022-9848) |
| API de legislación consolidada del BOE, metadatos de BOE-A-2002-18099 | 05-10-2026 | `fecha_actualizacion` 20251218: confirma la «última actualización 18/12/2025» del tema |
| RTVE `temas/teitse/01` y `temas/teitse/05` | 05-10-2026 | Cotejo de literalidad de lo listado como «Copiado de RTVE sin cambios» |

## Lo copiado de RTVE sin cambios: sólo literalidad

Cotejo mecánico (texto normalizado: sin negritas, en minúscula, sin cortes de línea) de cada frase
y fila de los pasajes listados en `27-T01-redaccion.md` contra teitse/01 y teitse/05. Todo literal.
Las únicas frases no literales dentro de esos epígrafes son las que el propio informe de redacción
declara adaptadas o nuevas (1.2 primera frase, 2.1 segunda tabla, 2.3 remisión al epígrafe 7, 3.4
consecuencia y vocabulario «del oficio», 4.1 frase de entrada, 7.3 «y da la caída en la tensión
entre fases» y fórmulas con la potencia, 8.3 «aunque las tres estén perfectamente equilibradas»).
No se re-verificó su contenido.

Hallazgo tipográfico en esos pasajes y en los adaptados: quedaban mayúsculas enfáticas de RTVE que la
redacción dijo haber pasado a minúscula («factor DE potencia», «Y DE LA longitud», «camino DE ida Y
vuelta», «cargas NO lineales», «NO se anulan»). Pasadas a minúscula.

## Verificación de lo demás (normas, adaptado y redacción nueva)

`negritas.py` contra el volcado: 47 negritas cotejadas (43 antes); 2 «no están», rótulos de la
plantilla; 0 atribuidas a otro artículo. `refutar_exactitud.py` y `refutar_modo.py`: 0 hallazgos.
`refutar_prosa.py`: 0. Como `negritas.py` no ancla en apartados de ITC, cada cita se buscó con
`grep -n` y se leyó con el rótulo del apartado que la contiene: todas en el apartado que dice el tema.

Todos los cálculos rehechos (3.2, 3.3, 4.2, 5, 6.2, 7.2, 7.3, 7.4, 7.5, 8.2, 8.4): cuadran. γ = 48
se presenta como dato supuesto, no como valor de norma (7.4 y «Lo que este tema no da»).

## Correcciones aplicadas (comprobadas en la fuente antes de aplicarlas)

1. **Error 3, recuento** (Trazabilidad, ITC-BT-19): los «cuatro párrafos» del 2.2.2 se daban como
   «límites, compensación, transformador propio, neutro». En el BOE la compensación está dentro del
   primero y el tercero es el del número de aparatos simultáneos. Corregido, y añadida la cita del
   tercer párrafo en la lectura 3 del epígrafe 7.2 (literal, línea 4701 del volcado).
2. **Error 6, salvedad omitida** (8.1, ITC-BT-52): el apartado 3.1 es «Instalación en aparcamientos
   de viviendas unifamiliares»; la frase del reparto entre fases sólo está ahí. Añadido el ámbito
   y el rótulo literal, también en Trazabilidad.
3. **Error 9 / atribución** (8.1, ITC-BT-43 2.6): «Fuera de la instalación interior» no lo dice la
   norma (es una ITC de receptores). Sustituido por el rótulo literal del apartado.
4. **Error 9** («Lo que este tema no da»): «un proyecto de reforma del REBT anunciado para 2026 por
   colegios profesionales» procedía de una presentación de COGITI que no se cita en Trazabilidad ni
   se ha releído. Quitado; queda sólo lo confirmado: ninguna reforma publicada después del
   18/12/2025.
5. **Física mal dicha** (5): «julios (vatio por segundo)» → «un vatio durante un segundo, W·s»;
   tabla «KW / KWh» → «kW / kWh».
6. **7.5, motores**: «eso cambia la corriente que entra en las fórmulas» sugería que el 125 % es
   para caída de tensión; la ITC-BT-47, apartado 3, lo fija «con objeto de que no se produzca en
   ellos un calentamiento excesivo». Reformulado con esa cita; Normativa y Trazabilidad añaden el
   apartado 3.
7. **6.3, lectura 4**: «resistencias o reactancias de descarga» → «de descarga a tierra», como dice
   la ITC-BT-43 2.7.
8. **Error 5**: kVA y kvar presentados en las siglas.
9. Normativa y Trazabilidad: añadido ITC-BT-19 2.2.3 (la remisión a la UNE 20.460-5-523 que el
   tema ya usaba en «Lo que este tema no da»). Extensión de la portada: «Unas 10.000 palabras».

Pasajes cambiados releídos: cada «ese apartado», «el mismo apartado» y «ellos» tiene antecedente
(en 7.5 se escribió «de los conductores de conexión» para que «ellos» lo tenga).

## Sin cambios, comprobado

Artículo 2.1, 4 y 16 y sus fechas; tabla del art. 4.1; ITC-BT-09 (3 y 8), 14, 15, 19 (2.2.1, 2.2.2,
2.2.4, 2.5), 43 (2.6, 2.7), 44 (3.1, 3.2), 47 (3.1, 3.2): literales y en su apartado; «podrán» y
«deberá» como en el BOE (error 4: ninguno); erratas del BOE conservadas («deforma», «energí a»,
«debidas cargas»); ninguna redacción derogada.
