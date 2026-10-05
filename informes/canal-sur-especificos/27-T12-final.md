# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`.
Revisados sólo los pasajes que lista `27-T12-remate.md`, comparando la copia previa al remate con el
tema actual. Fuentes releídas el 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»).
Copia previa a esta fase: scratchpad `27t12-antes-5bis.md`. Ficheros tocados: el tema y este informe.

## Comprobado y correcto

- **1.3, ventaja 1**: títulos de IT 4.2.1, 4.2.2 y 4.2.3 literales (BOE-A-2007-15820, líneas 2401, 2422, 2442).
- **5.2, primer guion**: IT 3.4.4 ap. 2, tramo en negrita continuo y literal (línea 2337).
- **3.2, RITE**: IT 1.2.4.3.2 (THM-C2, C4 y C5 con humedad relativa, líneas 1475-1482); IT 1.2.4.3.3
  ap. 2-4 e IDA-C4 / IDA-C6 literales (líneas 1484-1508).
- **3.2, WIKA IN 00.17 (11/2020)**: Pt100/Pt1000 100 y 1.000 Ω a 0 °C, PTC, IEC 60751; fórmulas AA, A, B;
  intervalos B y AA bobinados; dos hilos (250 mm, no aconsejable con Pt100 A/AA, normal con Pt1000),
  tres (versión normal, ~30 m), cuatro (laboratorio, calibración, A/AA, 1.000 m).
- **WIKA TE 15.01 (03/2025)**: salida lineal, límites 3,8 y 20,5 mA, fallo < 3,6 / > 20,5 mA por NE43,
  vigilancia de rotura y cortocircuito, fábrica Pt100 tres hilos 0-150 °C.
- **TDK (enero 2018)**: definición IEC 60539, 2-6 %/K, unas diez veces los metales.
- **Siemens QAA20 (30-07-2014)**: Pt 100 y Pt 1000 clase B, NTC 10k, pasivos, cable según controlador, montaje.
- **Siemens Symaro (2016, 0-92162-en)**: magnitudes, montajes, LG-Ni1000, salidas, alimentación AC 24 V /
  DC 13,5-35 V, rangos ajustables, NDIR, CO2/VOC/T/HR, ventilación según demanda, presión (aire, líquidos,
  gases, refrigerantes, presostato diferencial), caudal (sensores, detectores, velocidad).
- Aritmética del escalado: 25 °C; 12,5 °C; 3 bar; 13,6 mA. Correcta.
- Antecedentes: «esa sonda», «la misma hoja», «ese catálogo», «el T15 citado», «ese "y similares"»,
  «esa evolución» tienen todos su antecedente.

## Corregido (error 9 y error 1)

1. **Siglas, NAMUR**: «la organización que publica las recomendaciones NE» no consta en ninguna fuente
   leída (las hojas sólo dicen «NAMUR NE43», «NE89», «NE21:2012»). Ahora: «la sigla con la que las hojas
   de los fabricantes citan las especificaciones NE 21, NE 43 y NE 89».
2. **3.2, transmisor T15 y «Lo que este tema no da»**: «la recomendación NAMUR NE 43» → «la NAMUR NE 43»
   (la palabra «recomendación» no está en la fuente).
3. **3.2, tabla NTC**: TDK no dice que la resistencia nominal se dé a 25 °C, sino que la tolerancia de
   resistencia se fija «for one temperature point, which is usually 25 °C». Reescrito así. «"NTC 10k"
   nombra la de 10 kΩ» queda marcado como oficio (la hoja QAA20 sólo da el nombre).
4. **«Lo que este tema no da»**: decía que los termopares «sólo se nombran», pero el tema no los nombra
   en ningún otro sitio. Ahora: «Los termopares (el tema no los trata) y las sondas LG-Ni1000 (sólo se nombran)».

## Lentes

- `refutar_prosa.py`: 0 negritas rotas; siglas «sin presentar» las mismas que vio el remate (falsos positivos).
- `indice.py`: 12.814 palabras, 37 epígrafes; índice sin cambios de rótulo.

Resultado: el tema queda cerrado.
