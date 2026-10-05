# Puesto 27 · Oficial Técnico Electricista · Tema 3 · Fase 3, verificación

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas). Tema verificado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/03-cuadros-electricos-aparamenta-y-protecciones.md`
(14.191 palabras según `indice.py` tras las correcciones; 13.847 antes; ficha actualizada a «unas
14.200»).

Ficheros tocados: sólo el tema y este informe. Los demás ficheros del puesto que `git status` da
como modificados no son de esta fase.

## Lo copiado: nada que saltar

`27-T03-redaccion.md` lista «Copiado del común: ninguno» y «Copiado de RTVE sin cambios: ninguno»
(teitse/03 y teitse/04 están marcados «actualizar: sí»). No había pasajes que cotejar sólo por
literalidad: se verificó el tema entero, incluido todo lo tomado de RTVE.

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` | 05-10-2026 | Art. 15.3, 16.2, 16.3 (1 redacción); ITC-BT-01 (cada definición citada, y que no hay entrada de seccionador ni de relé); ITC-BT-02 (vig. 04-04-2025, BOE-A-2025-6773): cada título de norma citado y la nota (7); ITC-BT-09, 4 (nuevo); ITC-BT-17 entera; ITC-BT-19 2.2.4, 2.4, 2.6, 2.7, 2.9; ITC-BT-22 entera con notas; ITC-BT-23 entera con tabla 1; ITC-BT-24 3.2, 3.5, 4.1-4.1.3 con tablas 1 y 2; ITC-BT-28 1, 2.1, 4; ITC-BT-34 1, 3.1, 3.2; ITC-BT-47 3.1, 4, 5; ITC-BT-52 6.1-6.4 (vig. 16-06-2022, BOE-A-2022-9848). Redacción de cada bloque: única salvo ITC-BT-02 y 52 |
| API de legislación consolidada del BOE, metadatos de BOE-A-2002-18099 | 05-10-2026 | `fecha_actualizacion` 20251218: confirma la «última actualización 18/12/2025» |
| RD 614/2001 (BOE-A-2001-11881), anexo IV | 05-10-2026 | A.1 y B.1 (1 redacción, desde 21-08-2001) |
| INSST, guía técnica de riesgo eléctrico, 2020 (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`, líneas 4561-4625) | 05-10-2026 | Las 2 negritas que `negritas.py` no encuentra por los guiones blandos: literales. Medidas frente a la maniobra errónea |

## Lentes

- `negritas.py` (REBT, RD 614/2001, guía INSST): 192 negritas; 4 «no están» (2 rótulos de
  plantilla; 2 citas de la guía con guiones blandos, cotejadas a mano: literales); 0 atribuidas a
  otro artículo. Como no ancla en apartados de ITC, cada cita se buscó con `grep -n` y se leyó bajo
  el rótulo de su apartado: todas en el apartado que dice el tema.
- `refutar_exactitud.py`: 29 «no literales», todos falsos positivos (lee «apartado 3.2» de una ITC
  como «art. 3»); cotejadas a mano. `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 40
  epígrafes.
- Cálculos rehechos (3.4 RA máximas 1.667/167/50/80 Ω; 460 A en TN; 8.3 6 V ≤ 50 V; 9.4): cuadran.

## Correcciones aplicadas (comprobadas en la fuente antes de aplicarlas)

1. **Error 9 y error 3, el informe de redacción se equivocó** (3.2, «Lo que este tema no da»;
   decisión 3 de la redacción): el tema decía que el REBT «no fija» 300 mA y que «sólo fija los 30 mA
   y los 500 mA». La ITC-BT-09, apartado 4 (alumbrado exterior), fija **como máximo de 300 mA** con
   tierra ≤ 30 Ω, y admite 500 mA o 1 A con tierra ≤ 5 Ω y ≤ 1 Ω (la redacción dijo haber buscado «300 mA»
   sin resultado; `grep -n '300 \?mA'` lo da en la línea 3721 del volcado).
   Añadida la cita literal en 3.2, corregida la fila «Media» de la tabla y la viñeta de «Lo que no
   da» (que además ya no dice «sólo»: 30 mA aparece en muchas ITC); ITC-BT-09 añadida a ficha,
   Normativa y Trazabilidad.
2. **Error 9** («Lo que no da», 3.3 y 9.3): el «proyecto de reforma del REBT anunciado para 2026 por
   colegios profesionales (diferenciales AC, DPS obligatorio)» procede de una presentación de COGITI
   no guardada en fuentes ni citada en Trazabilidad. Quitado su contenido y las dos remisiones; queda
   lo confirmado: ninguna reforma publicada después del 18/12/2025 (mismo criterio que la
   verificación del tema 1).
3. **Error 6, salvedad omitida** (1.5, ITC-BT-19 2.7 a): añadidas las excepciones de la letra a)
   (relojes, rectificadores telefónicos ≤ 500 VA, mando o control ligado a la seguridad).
4. **Error 6** (3.4, ITC-BT-24 4.1.1): los tiempos 0,4/0,2/0,1 s se daban sin la salvedad de la UNE
   20.460-4-41 para tiempos mayores. Añadida.
5. **Error 6/9** (3.4, IT): «el segundo defecto se corta con las condiciones del TT o del TN»
   simplificaba: TT **salvo que el neutro no debe ponerse a tierra**, o TN con **2 x Zs x Ia ≤ U** /
   **2 x Zs’ x Ia ≤ U0** y tabla 2. Sustituido por lo literal.
6. **Error 6** (1.1): «la ITC-BT-17 los exige por separado en todo cuadro general» omitía el «salvo
   que la protección… se efectúe mediante otros dispositivos». Corregido.
7. **Error 6** (5.2): la falta de tensión se pide si el rearranque puede «provocar accidentes, **o
   perjudicar el motor**». Añadido.
8. **Error 6** (6.1): el 125 % de la ITC-BT-47 es del apartado 3.1 «Un solo motor». Precisado.
9. **Error 6** (6.2): la ITC-BT-28 2.1 exige el controlador de aislamiento sólo **en el esquema IT**.
   Precisado.
10. **Error 9** (3.5): el rearme automático del REBT no es sólo «recarga en vía pública»: ITC-BT-52 6.1
    también nombra aparcamientos públicos y estaciones de movilidad eléctrica, y la ITC-BT-09 4 los
    de **reenganche automático**. Corregido. «La solución que el apartado sugiere» → «que se
    desprende del apartado» (la ITC-BT-19 2.9 no sugiere nada).
11. **Error 9** (4): «consecuencia que el REBT recoge en motores… Por eso…» atribuía al REBT un
    razonamiento sobre fusibles que no hace. Reescrito como oficio + exigencia de la ITC-BT-47.
12. **Error 9** (3.2): «Es el caso de… un plató abierto al público» no consta en la ITC-BT-34;
    sustituido por su campo de aplicación literal (apartado 1). «Dos valores más que el REBT impone
    con su número» (el segundo no era un número) → «Otros dos lugares donde el REBT fija la
    sensibilidad».
13. **Error 9** (9.1): «que el REBT no regula» y «no es materia del REBT» iban más allá de la fuente,
    que sólo dice que la ITC-BT-23 no lo contempla/trata. Ajustado. En 9.3 se añade la ITC-BT-09 4
    (**cuando los equipos instalados lo precisen**) como otro caso de protección contra
    sobretensiones fuera de la ITC-BT-23.
14. **Precisiones menores**: 1.4 «envolventes de los cuadros generales» → «de los cuadros» (literal de
    la ITC-BT-17 1.2); 1.4, la tapa que se abre a mano incumple sólo si no hay corte enclavado ni
    segunda barrera (las otras dos opciones de la ITC-BT-24 3.2); 2.4, la cita del neutro es literal
    de la nota (1), no de la (5), que lo dice como «salvo que…»; 7, la guía habla de seccionadores
    «de puesta a tierra **y en cortocircuito**».

Releídos los pasajes cambiados: cada «ese apartado», «la instrucción», «el mismo apartado» tiene su
antecedente delante («tabla 2» se precisó como «de ese apartado 4.1.3»).

## Confirmado sin cambios

Todo lo demás: las 10 decisiones de la redacción (salvo la 3, véase corrección 1), incluidas las
erratas del BOE conservadas («instalació n», «deforma», «esta», «kv»), la entrada duplicada del
contactor de contactos cerrados en la ITC-BT-01, la coma de B.1.1.ª del RD 614/2001 y la ausencia de
seccionador y relé en la ITC-BT-01. Lo declarado como oficio se mantiene como oficio.

## Para la refutación

- La pregunta 4 de comprobación (167 Ω) y la 9 (1 s) siguen contestándose; conviene añadir una sobre
  la ITC-BT-09 (300 mA / 30 Ω; 500 mA / 5 Ω; 1 A / 1 Ω).
- No se ha comprobado si otras ITC no citadas (25, 27, 30, 40…) piden selectividad diferencial; el
  tema no lo afirma.
