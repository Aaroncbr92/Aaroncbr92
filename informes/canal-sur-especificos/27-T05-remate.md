# Puesto 27 · Oficial Técnico Electricista · Tema 5 · Fase 5, remate

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas). Tema:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/05-puestas-a-tierra-y-equipotencialidad.md`.
Entrada: `27-T05-refutacion.md` (graves 0, menores 3, lagunas 3) y `27-T05-preguntas.md`.

Ficheros tocados: el tema y este informe.

## Fuente releída

RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md`,
leído el 05-10-2026: ITC-BT-05, 6.2; ITC-BT-18, 11; ITC-BT-19, 2.9; ITC-BT-24, 4.3; ITC-BT-26,
3.2 a 3.4; ITC-BT-27, 2.2.

## Correcciones (las tres menores, todas confirmadas en la fuente)

1. **5.3, ITC-BT-18, 11.** «Las masas … no están unidas» pasa a la letra: «**Se verificará que las
   masas puestas a tierra en una instalación de utilización, así como los conductores de protección
   asociados a estas masas o a los relés de protección de masa, no están unidas …**».
2. **1.7, ITC-BT-27, 2.2.** Añadida la salvedad del volumen 3 con cabina de ducha prefabricada. El
   informe de refutación cortaba la frase: la fuente sigue con «**, por ejemplo un dormitorio.**», y
   así se ha copiado.
3. **4.1, ITC-BT-05, 6.2.** Completada la definición de defecto grave con su segunda frase («**También
   se incluye dentro de esta clasificación …**»). El enlace siguiente pasa a «Por eso un conductor de
   protección cortado …».

## Ampliaciones (las tres lagunas)

1. **1.6, ITC-BT-26, 3.3** (pregunta 4). Nueva lista literal de los puntos de puesta a tierra, a) a e).
   Corrección al informe de refutación: el 3.4 no conecta las líneas principales a todos esos puntos,
   sino «**Al punto o puntos de puesta a tierra indicados como a) en el apartado 3.3**»; se ha copiado
   así.
2. **6.3, ITC-BT-24, 4.3** (pregunta 13). Párrafo bajo la tabla con las condiciones a), b) y c): 2 m,
   reducible a 1,25 m fuera del volumen de accesibilidad; obstáculos no conectados ni a tierra ni a las
   masas; ensayo de 2.000 V y fuga no superior a 1 mA. Incluye la condición previa literal de «paredes
   aislantes».
3. **7.3, regla 4, ITC-BT-19, 2.9** (pregunta 14). Añadida la regla literal de las corrientes de fuga.
   Por coherencia, la entradilla de 7.3 («Ninguna de estas reglas es del REBT») pasa a «Estas reglas son
   práctica de oficio compatible con el REBT; del reglamento sólo es el límite de fugas que se cita en
   la 4».

Con lo añadido, las preguntas 4, 13 y 14 se contestan enteras con el tema: 15 de 15.

## Otros retoques

- 1.7, tabla: «a partir de la lista del 3.3» pasa a «de la ITC-BT-18, 3.3», porque 1.6 ahora cita
  también el 3.3 de la ITC-BT-26.
- Trazabilidad: ITC-BT-26 «1, 3.1, 3.2, 3.3 y 3.4».
- Ficha: extensión «Unas 13.400 palabras» (medida por `indice.py`: 13.418).
- Siglas no usadas (MBTP, ID, IP2X, PE): se dejan; no es error.

## Pasajes cambiados (para la fase 5 bis)

1.6 (lista del 3.3 y frase del 3.4) · 1.7 (salvedad ITC-BT-27 y tabla) · 4.1 (definición de defecto
grave) · 5.3 (primer párrafo del apartado 11) · 6.3 (párrafo nuevo bajo la tabla) · 7.3 (entradilla
y regla 4) · Trazabilidad · ficha.

Antecedentes releídos: «El mismo apartado» (2.2 de la ITC-BT-27), «El apartado 3.4» y «el apartado
3.3» (ITC-BT-26), «punto a)» (ITC-BT-24, 4.3), «El límite» (el de las fugas de la regla 4): todos
tienen delante su antecedente.

## Lentes

- `indice.py`: 37 epígrafes, sin epígrafes nuevos; índice sin cambios.
- `negritas.py` (REBT + guía INSST): 273 negritas (257 antes); 4 «no están», las mismas de antes
  (dos rótulos de plantilla, una cita del RD 337/2014 y la definición del INSST entrecomillada, de
  fuentes no pasadas o con comillas tipográficas). Todas las negritas nuevas están en la fuente.
- `refutar_exactitud.py`: 19 «no literales» (18 antes): ruido de la herramienta, que busca artículos
  y no apartados de ITC; la nueva la encuentra `negritas.py`.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos.

## Resultado

Tres correcciones de letra y tres ampliaciones con cita literal. **Amplió contenido**: toca 5 bis.
