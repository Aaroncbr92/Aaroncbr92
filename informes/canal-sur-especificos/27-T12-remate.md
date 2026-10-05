# Remate · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`.
Entradas: `27-T12-refutacion.md` (2 hallazgos menores, 2 lagunas) y `27-T12-preguntas.md`
(12 enteras, 1 a medias, 2 no). Fuentes leídas el 05-10-2026 (reloj del sistema; el encargo dice
«hoy es 24-09-2026»). Copia previa: scratchpad `27t12-antes-remate.md`.

Ficheros tocados: el tema y este informe. **Amplía contenido nuevo: sí** (procede 5 bis).

## Hallazgos de exactitud: aplicados los dos

1. **Epígrafe 5.2, IT 3.4.4 ap. 2 (error 6).** Comprobado en BOE-A-2007-15820 (línea 2337 del
   volcado): la norma dice «con el mayor nivel de desagregación posible por uso (calefacción,
   refrigeración y agua caliente sanitaria), así como del consumo de agua en función de los
   dispositivos de medida disponibles». Cambiado «desglosada por uso, «**con el fin…**»» por
   «por la instalación térmica «**con el mayor nivel de desagregación posible por uso (…), así
   como del consumo de agua en función de los dispositivos de medida disponibles, con el fin…**»».
   La negrita es ahora un tramo continuo del BOE.
2. **Epígrafe 1.3, ventaja 1 (glosa).** Comprobados los títulos de las IT 4.2.1, 4.2.2 y 4.2.3
   (líneas 2401, 2422 y 2442). Sustituida la glosa por los tres títulos literales, cada uno con su
   IT entre paréntesis. La observación sobre el contrato de rendimiento energético no se aplica
   (el informe dice que el tema no la necesita).

## Lagunas: ampliado el epígrafe 3.2

Rótulo nuevo «3.2 Los sensores y sus señales de campo» (antes «3.2 Las señales de campo»; se
mantiene el número para no romper las remisiones al 3.2 del 4.1 ni al 3.3 desde el tema 18).
Pasajes nuevos, todos dentro del 3.2:

- *Qué sensores hay*: familias por magnitud y montaje; pasivos y activos (alimentación, salidas
  0-10 V y 4-20 mA, rango ajustable). Fuente: catálogo Siemens Symaro (2016) y hoja QAA20 (2014).
- Tabla de sensores de temperatura: Pt100/Pt1000 (100 Ω y 1.000 Ω a 0 °C, coeficiente positivo,
  IEC 60751; WIKA IN 00.17, 11/2020) y NTC (definición de la IEC 60539, 2-6 %/K, unas diez veces
  los metales, tolerancia a 25 °C; TDK/EPCOS, enero de 2018). Responde a la pregunta 9.
- Tolerancias AA, A y B con sus fórmulas e intervalos (WIKA IN 00.17); clase B de las QAA20.
- Tabla de conexión a 2, 3 y 4 hilos con longitudes del fabricante (WIKA IN 00.17) y una
  consecuencia aritmética (Pt1000 frente a Pt100).
- Dónde se monta una sonda de ambiente (hoja QAA20), enlazado con el contraste del 3.3.
- Tabla de los demás sensores (humedad, calidad del aire NDIR CO2/VOC, presión, caudal; presencia,
  fuga, nivel e intensidad como oficio); la columna de usos va declarada como oficio.
- RITE IT 1.2.4.3.3 ap. 2-4: IDA-C4 e IDA-C6 literales y dónde se emplean (líneas 1483-1508); y
  la IT 1.2.4.3.2 (THM-C2, C4, C5 con humedad). Responde a la pregunta 10.
- Salida del transmisor WIKA T15 (TE 15.01, 03/2025): lineal, límites 3,8 y 20,5 mA, fallo por
  debajo de 3,6 o por encima de 20,5 mA según NAMUR NE 43.
- *El escalado*: fórmulas 4-20 mA y 0-10 V (aritmética sobre salida lineal, así declarada),
  ejemplos (12 mA en 0-50 °C = 25 °C; 8 mA = 12,5 °C; 30 °C = 13,6 mA) y el error de rango
  distinto entre transmisor y controlador. Responde a la pregunta 8.

Lo que no pude confirmar y no se escribe: termopares y LG-Ni1000 más allá del nombre; la
adopción UNE de la IEC 60751; las normas IEC 60751, IEC 60539 y NAMUR NE 43 leídas directamente
(se citan a través de las hojas). Declarado en «Lo que este tema no da». Se quitó, antes de
guardar, un «UNE-EN IEC 60751» y una glosa sobre NAMUR que salían de memoria.

## Otros pasajes cambiados

- Siglas de entrada: NTC, NDIR, VOC, CO2, IEC, NAMUR, Ω, kΩ.
- «Qué se puede preguntar»: añadidos tipos de sensor, Pt100, sensores de calidad del aire del
  RITE y escalado.
- Portada: Fuente (IT 1.2.4.3.2 y 1.2.4.3.3; hojas WIKA, TDK, Siemens) y Extensión (12.800).
- Normativa que el tema invoca: IT 1.2.4.3.2 e IT 1.2.4.3.3.
- Lo que este tema no da: punto nuevo sobre termopares, LG-Ni1000 y normas no leídas.
- Trazabilidad: cinco filas nuevas (WIKA IN 00.17, WIKA TE 15.01, TDK, Siemens QAA20, Siemens
  Symaro), todas leídas el 05-10-2026; lista de oficio ampliada.

Releídos los pasajes cambiados: «esa sonda», «la misma hoja», «ese catálogo», «el T15 citado» y
«ese "y similares"» tienen su antecedente en el mismo párrafo o en el anterior.

## Lentes

- `indice.py`: índice regenerado, 12.793 palabras, 37 epígrafes.
- `refutar_prosa.py`: 0 relleno, 0 repetidas, 0 negritas rotas; siglas «sin presentar»: ED, SD,
  SS, EA, SA, CT (se presentan en su propia cita, ya estaban), AA (nombre de clase), DIN (dentro de
  un título en Trazabilidad), THM (rótulo del RITE, ya glosado), WIKA y TDK (marcas).
- `negritas.py` contra RITE y RIPCI: todas las negritas nuevas del RITE encontradas; las «no
  están» son literales de la guía del IDAE (fuera de esos volcados), como antes.
- `refutar_exactitud.py`: 13 citas con paréntesis, 11 «no literales»; las 4 nuevas son los títulos
  de las IT 4.2.x, que la lente lee como «art. 4»: falsos positivos, comprobados a mano. Antes del
  remate: 9 y 7, del mismo tipo.
- `refutar_modo.py`: 0 hallazgos.

## Para la 5 bis

Revisar sólo: epígrafe 1.3 (ventaja 1), epígrafe 3.2 entero, epígrafe 5.2 (primer guion), siglas,
«Qué se puede preguntar», portada, «Normativa», «Lo que este tema no da» y «Trazabilidad».
