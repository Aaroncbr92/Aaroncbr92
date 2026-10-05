# Refutación · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Fase 4. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`
(1.131 líneas, unas 13.100 palabras). No corrijo: listo hallazgos para el remate.

**Alcance de la exactitud**: el informe de redacción declara «Nada» en «Copiado del común» y en «Copiado
de RTVE sin cambios», así que la exactitud se ha mirado en el tema entero. La cobertura también.

Ficheros tocados: este informe y `27-T18-preguntas.md`. El tema, no.

Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo fija «hoy» en
24-09-2026; las redacciones citadas son las mismas en las dos fechas: la última reforma aplicada, el
RDL 7/2026, rige desde el 22-03-2026).

## Fuentes releídas

- RD 244/2019 (`boe.py precepto`): arts. 2, 3, 4 y 5 vigentes; art. 3 con `--fecha 20260301` (párrafo
  de 2.000 m); art. 14 en el volcado (bloque `a1-6`, redacción única). `redacciones.tsv`: arts. 2, 5 y
  14 con una sola redacción.
- REBT, ITC-BT-40, apartados 2 y 4.3-4.3.1 (volcado, líneas 8275-8306).
- RITE (volcado): IT 1.2.4.3.5, IT 1.2.4.4 (apartados 1-8), IT 2.3.4, nota de la IT 3.3, IT 4.2.1-4.2.3
  (rótulos), IT 4.3.1-4.3.4, apéndice 1 (definiciones y niveles); `redacciones.tsv` (apéndice 1 del RD
  178/2021; IT 2 original).
- RD 56/2016, art. 3 entero (redacción única).
- Reglamento (UE) 2023/1542 (volcado): art. 3.1 puntos 13, 15, 25, 27 y 28; arts. 12, 13, 14, 61.1,
  77-78 (rótulos), 95 y 96; anexos V (rótulos 1-11 y texto del 6), VI parte A y VII.
- Informe de investigación D, entrada de ISO/IEC 30141 (sólo para ver qué se leyó de esa norma).

## Lentes automáticas

- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (5 fuentes): 166 negritas, 19 «NO ESTÁ» y 2 «otro artículo»: las mismas que ya cotejó
  a mano el verificador (rótulos, fichas de catálogo y vista previa ISO, redacción anterior del
  3.g.iii); los dos «otro artículo» son falsos positivos (anexo V tras el art. 96 en el volcado; el
  14.1 citado en 3.4). Sin hallazgo nuevo.
- `refutar_modo.py`: 0 hallazgos.

## Lente 1 · Exactitud

**Graves: 0.** Todas las cifras, fechas y literales de riesgo releídos están bien: 100 kW, 500 m,
5 MW/5.000 m y su redacción anterior (2.000 m), 800 VA, 30 mA, 100 kVA, 70/20 kW, 290 kW, 2 años,
5 kg, 2 kWh, 18-08-2024/2025/2026 y 18-02-2027, los once rótulos del anexo V, los diez parámetros del
anexo VII, los diez datos del anexo VI parte A de los que se citan cuatro, el 4.5 a)-c) y el 4.7, el
5.6 y el 5.7, el 14.2-14.4, la exención de la IT 4.3.4 y el apartado 8 de la IT 1.2.4.4 con su modo.

**Menores: 6.**

1. **2.1 · error 9 (afirmación sin fuente).** «Es norma de la ISO y la IEC (comité conjunto JTC 1/SC 41)»
   para la **ISO/IEC 30141**. Lo leído de esa norma (ficha AENOR y alcance de la vista previa, según
   investigación y verificación) no incluye el comité; el SC 41 sólo está confirmado para la ISO/IEC
   30173 (vista previa y committee.iso.org/81442). Además «JTC» no se presenta como sigla (error 5).
   Propuesta: quitar el paréntesis o confirmarlo en el prólogo de la vista previa de la 30141.
2. **7.1 · error 6 (salvedad omitida).** Art. 2.2 del RD 244/2019: la exclusión de los grupos de
   emergencia se hace **«de acuerdo con las definiciones del artículo 100 del Real Decreto 1955/2000»**.
   El tema la reproduce sin esa remisión, y apoya en ella una lectura de oficio («el uso decide el
   régimen»). Propuesta: añadir la remisión.
3. **6.6 · error 6.** Art. 61.1: las organizaciones de responsabilidad del productor obligan sólo
   **«de haber sido designadas con arreglo al artículo 57, apartado 1»**. El tema dice «los productores
   (o sus organizaciones de responsabilidad del productor)» sin la condición. Además el nombre literal
   es «organizaciones competentes en materia de responsabilidad del productor».
4. **5.4 · error 6.** «El Real Decreto 56/2016 obliga a las grandes empresas a una auditoría energética
   cada cuatro años»: el art. 3.1 dice **«grandes empresas o grupos de sociedades incluidos en el ámbito
   de aplicación del artículo 2»** y que cubra **«al menos, el 85 por ciento del consumo total de
   energía final»**. Se remite el detalle al tema 16, pero la frase recorta el sujeto. Propuesta: «las
   grandes empresas o grupos de sociedades del artículo 2».
5. **Portada · error 3 (recuento que no cuadra).** «Fuente» da el Reglamento (UE) 2023/1542 con
   «artículos 3, 12, 13, 14, 61 y 96», y el tema usa también el **95** (6.2) y lo lista en «Normativa»;
   el RITE figura con «IT 1.2.4.3.5, IT 1.2.4.4, IT 2.3.4 e IT 4.3.4», sin la **nota de la IT 3.3** (5.3)
   ni el **apéndice 1** (1.2, 2.4), que sí están en «Normativa» y en «Redacción que se estudia».
6. **7.11 · precisión.** Fila «Más de 100 kW de inversores → Fuera de la compensación: con excedentes no
   acogida». Por el art. 4.1-4.2, con más de 100 kW también cabe la modalidad **sin excedentes**; la
   fila sólo es cierta si se quiere verter. Propuesta: «Si se quiere verter, con excedentes no acogida
   (o sin excedentes, con antivertido)».

Sin hallazgo, comprobado: la historia del art. 3.g).iii y del 4.5.b) (avisos 1 de redacción y
verificación); la titularidad y responsabilidad del art. 5.2-5.4; la tabla de compensación del 14.3
(incluido el PVPC parafraseado en redonda); el modo de verbos de la IT 1.2.4.4.8; el art. 95 (deroga
la Directiva 2006/66/CE con efecto 18-08-2025, con disposiciones transitorias); la salvedad del 12.2.a)
y la del 4.3 de la ITC-BT-40, ya añadidas por el verificador. Las remisiones a los temas 7, 12, 13 y 16
no se han reabierto (las comprobó el verificador).

## Lente 2 · Cobertura del enunciado

Las siete materias del enunciado tienen epígrafe propio y en su orden: sensorización IoT (2),
mantenimiento predictivo (3), gemelo digital de instalaciones (4), telegestión energética (5),
baterías (6), autoconsumo (7) y automatización de edificios (8). La parte normativa (autoconsumo,
baterías, RITE) está muy completa. La parte tecnológica, que es la que un tribunal de oficio también
pregunta, tiene huecos.

Quince preguntas en `27-T18-preguntas.md`: **11 enteras, 2 a medias, 2 no**.

**Lagunas: 4** (se amplía el tema; cada dato, con su fuente):

1. **IoT · comunicaciones de los sensores (pregunta 2, no).** El tema dice que los sensores IoT son
   «a menudo inalámbricos, con batería propia», pero no nombra ninguna tecnología de comunicación
   (redes de área amplia y baja potencia como LoRaWAN o NB-IoT; protocolos de mensajería como MQTT), y
   el tema 12 tampoco trata los inalámbricos. Fuentes a buscar: especificación de la LoRa Alliance,
   3GPP para NB-IoT, OASIS para MQTT. Bastan unas líneas y una tabla.
2. **Predictivo · ultrasonidos y descargas parciales (pregunta 5, a medias).** El tema da termografía,
   análisis de red, aislamiento y vibración, pero no la inspección por ultrasonidos ni la detección de
   descargas parciales, técnica habitual en cuadros y celdas. Fuente a buscar: la norma ISO de
   monitorización de condición por ultrasonidos (serie ISO 29821) o la documentación de un fabricante
   de instrumentos. No figura en ningún tema del puesto salvo, en climatización, el tema 9.
3. **Gemelo digital · BIM (pregunta 6, a medias).** El tema no nombra el modelado de información de
   construcción (BIM) ni su relación con el gemelo, que es la pregunta más previsible del epígrafe 4
   («¿un modelo BIM es un gemelo digital?»). Fuente a buscar: UNE-EN ISO 19650 (ficha de catálogo) y la
   definición de la ISO/IEC 30173 ya leída. Basta una fila en la tabla de 4.2.
4. **Baterías · químicas de litio (pregunta 11, no).** La tabla de 6.1 trata el ion litio como una sola
   química; no distingue litio-ferrofosfato (LFP) de níquel-manganeso-cobalto (NMC), que es la
   diferencia que decide el riesgo de embalamiento en un almacenamiento estacionario. Fuente a buscar:
   documentación técnica de fabricante o manual universitario; lo que no se confirme, no se escribe.

## Para el remate

- Corregir los seis menores (pasajes 2.1, 7.1, 6.6, 5.4, portada y 7.11) contra las fuentes citadas.
- Las cuatro lagunas piden **ampliar** (remate con Opus, y 5 bis sobre lo ampliado). Ninguna exige
  norma obligatoria: son fuente técnica, y lo que sólo sea costumbre de oficio debe decirse como tal.
- Sigue pendiente lo que dejó la verificación: la fecha efectiva de la etiqueta del art. 13.1 (acto de
  ejecución del 13.10) y que `indice.py` no procesa el tema (falta su fila en `portadas.tsv`).
