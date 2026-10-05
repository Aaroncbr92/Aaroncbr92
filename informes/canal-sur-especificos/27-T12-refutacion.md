# Refutación · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Fase 4. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`
(11.522 palabras según `wc -w`, ficha a 11.000). Fuentes releídas el 05-10-2026 (reloj del sistema;
el encargo dice «hoy es 24-09-2026»). No corrijo: sólo informo.

Ficheros tocados: este informe y `27-T12-preguntas.md`. El tema no se ha modificado.

## Alcance

- Exactitud: todo lo normativo y lo literal de la guía del IDAE, salvo los pasajes listados en
  «Copiado de RTVE sin cambios» de `27-T12-redaccion.md` (1.1, 1.2, 1.4, 2.2, 2.3, 3.1, 3.2, 7.5),
  que no se re-verifican. «Copiado del común»: nada.
- Cobertura: el tema entero contra el enunciado del punto 12.
- No releídas aquí (web, ya cotejadas en verificación): ISO 16484-5:2026 (ficha y muestra iTeh),
  Modbus V1.1b3, glosario NIST y knx.org. No tengo copia local; quedan como en la verificación.

## Comprobado en la fuente, sin hallazgo

- RITE (BOE-A-2007-15820; última redacción vigente 01-07-2021, `redacciones.tsv`): art. 2.1, 12.3,
  25.3; IT 1.2.4.3.1 ap. 1 y 3; IT 1.2.4.3.5 ap. 1 (290 kW, «deberán», a-c, UNE-EN 15232-1), 2
  («podrán») y 3 (cuatro citas); IT 1.2.4.4 ap. 2-7; IT 1.2.4.5.1 ap. 1 y 5; IT 1.3.4.1.2.2 p) i.;
  IT 2.1 (pruebas de puesta en servicio) e IT 2.3.4 ap. 1-4; IT 3.3 pie de tabla 3.1 (2 años, con su
  salvedad); IT 3.4.2 tabla 3.3 (3 m / m, «la primera al inicio de la temporada», pérdidas de
  presión «en plantas enfriadas por agua»); IT 3.4.4 ap. 2 (cinco años); IT 3.4.5 (5 años, 1.000 m²,
  «apartado 2 de la I.T. 3.8.1.2»); IT 3.6 ap. 2; IT 3.7 a), b), e); IT 4.3.4 párrafo 2; apéndice 1
  (definición y cuatro niveles, literales); apéndice 2 (título de la UNE-EN ISO 16484-3).
- RIPCI (BOE-A-2017-6606): anexo I, sección 1.ª, punto 7: las dos frases literales; bloque `s1-2`
  vigente desde 10-05-2025 (BOE-A-2025-7190), como dice la ficha.
- Guía IDAE: operaciones 48-97 del «Control DDC (Computerizado)», número, texto y frecuencia de
  todas las citadas (50, 52-55, 57, 60-64, 66, 68, 71-73, 75-78, 80, 82, 83, 85 bis, 86-88,
  90-94, 97); 37, 39 y 42 bajo «Control por autómata electrónico» de la familia 23; el 85
  repetido; sólo 86-88 son mensuales en esa gama (la afirmación «la más alta» se sostiene);
  clave «2 A»; apartado 5.3.1 literal (y «acordarse previamente con la propiedad o el usuario»);
  ficha técnica (tipos «neumática, electromecánica, electrónica, DDC»), claves ED…CT, «Alarma alta
  temperatura en sala de informática»; frase de datos nominales.

## Hallazgos de exactitud

Graves: 0.

Menores: 2.

1. **Error 6 (salvedad omitida), epígrafe 5.2.** «la empresa mantenedora sigue la evolución del
   consumo y de la energía aportada, desglosada por uso». La IT 3.4.4 ap. 2 dice «**con el mayor
   nivel de desagregación posible por uso (calefacción, refrigeración y agua caliente
   sanitaria), así como del consumo de agua en función de los dispositivos de medida
   disponibles**». El tema convierte en absoluto lo que la norma condiciona a lo posible y omite el
   consumo de agua. Propuesta: «con el mayor nivel de desagregación posible por uso (calefacción,
   refrigeración y agua caliente sanitaria), y también la del consumo de agua».
2. **Error 9 leve (glosa imprecisa), epígrafe 1.3, ventaja 1.** «Es decir, de las inspecciones de
   calefacción, de aire acondicionado y de la instalación completa». Los títulos del RITE son: IT
   4.2.1 «Inspecciones de los sistemas de calefacción, ventilación y agua caliente sanitaria»; IT
   4.2.2 «Inspección de los sistemas de las instalaciones de aire acondicionado y ventilación»; IT
   4.2.3 «Inspección de la instalación térmica completa». Propuesta: dar los tres títulos completos.
   (De paso: el primer párrafo de la IT 4.3.4 exime también por contrato de rendimiento energético;
   el tema no lo necesita, pero «Dos ventajas reglamentarias de tenerlo» no lo contradice.)

## Cobertura del enunciado

Las seis rúbricas (BMS/SCADA, sensores, alarmas, históricos, telemedida, actuación ante avisos)
tienen epígrafe propio, en el orden del enunciado. Quince preguntas (`27-T12-preguntas.md`): 12
enteras, 1 a medias, 2 no.

Lagunas (se amplía el tema, en 3.2 o en un 3.x nuevo), todas en «sensores»:

1. **Tipos de sensor y su principio** (preg. 9 y 10). El tema trata el punto, la señal y el
   contraste, pero no qué sensores hay: temperatura (sondas de resistencia Pt100/Pt1000, NTC,
   termopar), humedad, presión y presión diferencial, caudal, calidad del aire (CO2), presencia,
   nivel, fuga de agua, transformadores de intensidad. Es lo primero que un tribunal pregunta del
   rótulo «sensores». Cada dato con fuente (norma UNE-EN 60751 para Pt100, si se lee; documentación
   de fabricante; el control de la calidad del aire que exija el RITE, si se cita, se lee antes en
   su IT o se remite al tema 10).
2. **Escalado de la señal 4-20 mA / 0-10 V** (preg. 8, a medias). Falta la relación lineal entre
   la señal y la magnitud (valor = mín + (I − 4)/16 × rango) y un ejemplo; el tema ya nombra el
   «escalado mal configurado» como causa de error (3.3) sin explicarlo. Es oficio y así debe
   decirse.

## Otras observaciones (no son hallazgos)

- Extensión: 11.522 palabras con `wc -w` frente a «11.000» de la ficha (`indice.py` dio 10.994 en
  verificación; la diferencia es de método de recuento). Si el remate amplía, actualizar la ficha.
- ISO 16484-5:2026 (agosto de 2026) es anterior a la convocatoria; citarla como vigente es correcto.
