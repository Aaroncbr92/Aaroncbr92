# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`.
Alcance: sólo los 15 pasajes que lista `27-T18-remate.md`, § 3 (cotejados con el diff contra la copia previa del
remate).
Fecha de lectura de las fuentes: 05-10-2026, por el reloj del sistema (el encargo fija «hoy» en 24-09-2026; las
fuentes no cambiaron entre las dos fechas).

**Resultado: 3 correcciones menores, aplicadas después de comprobarlas en la fuente. No hay ningún error grave.
Todo lo demás se confirma.**

## Correcciones

| N.º | Pasaje | Error | Fuente | Cambio |
|---|---|---|---|---|
| 1 | 4.2, definición 3.3.14 de BIM (negrita) | Al literal le faltaba la remisión «(3.2.8)», y la definición de gemelo digital del 4.1 sí conserva las suyas | Vista previa de la ISO 19650-1:2018, 3.3.14: «use of a shared digital representation of a built asset (3.2.8) to facilitate…» | Se añade «(3.2.8)» |
| 2 | 6.1, tabla LFP/NMC, fila «Peligrosidad comparada» | Decía «celdas cilíndricas». Esa palabra no está en la fuente, y la revisión no es de ensayos propios: es un resumen de otros estudios (error 9) | Su y otros, PMC13359442: «A review of calorimetric analyses from multiple studies summarizes the TR characteristics of commercial 18650 LIBs» | «Una revisión de análisis calorimétricos de varios estudios con celdas comerciales 18650, citada por la segunda revisión, da…» |
| 3 | 2.6, viñeta de las clases LoRaWAN | «Un sensor de pila […] espera a que él hable» era una generalización: la clase B también vale con pila y recibe a horas programadas (error 6, salvedad omitida) | LoRa Alliance: en clase A, «downlink communication must be buffered at the network server until the next uplink event». En clase B, «the additional power consumption is low enough to still be valid for battery powered applications» | Se dice «en clase A» y se añade la salvedad de la clase B |

## Comprobado sin cambios

- **2.1** (ISO/IEC 30141). El prólogo de la ed. 2.0, 2024-08, dice «subcommittee 41: Internet of Things and Digital
  Twin, of ISO/IEC joint technical committee 1». El epígrafe 4.1 nombra el mismo subcomité.
- **2.6**:
  - LoRaWAN: los cinco literales están en la página de la LoRa Alliance. También lo están la clase A como clase
    por defecto con dos ventanas de recepción y la clase C con «up to ~50mW».
  - 3GPP, «Standardization of NB-IOT completed» (21-06-2016). Se ha releído hoy y contiene la definición,
    «Release 13 (LTE Advanced Pro)» y la congelación en junio de 2016.
  - 3GPP, «The Cellular Internet of Things» (09-10-2017). Se ha releído hoy en
    https://www.3gpp.org/news-events/3gpp-news/c-iot y la frase del espectro con licencia es literal.
  - MQTT 5.0 (OASIS, 07-03-2019): la definición, los contextos M2M/IoT y las tres QoS son literales. Las glosas
    («puede duplicarse») se ajustan a la norma.
  - Las remisiones a 2.2 y 2.5 existen. El 2.5 dice que el equipo de comunicaciones va al SAI.
- **3.5** (ISO 29821:2018):
  - El título, TC 108/SC 5, la definición 3.1 (>20 kHz) y los «acoustic events» están en la norma.
  - En la tabla 1 figuran Switchgear, Transformers, Insulators, Junction boxes y Circuit breaker.
  - Son literales el arco antes de la termografía (4.3), la frase de 50/60 Hz, el sensor de contacto frente a la
    descarga parcial y el acoplamiento magnético (5.4), el sensor parabólico (5.3), los rodamientos lentos (4.3)
    y los equipos portátiles frente a los fijos.
  - La norma de 2018 se retiró el 16-04-2026 y la sustituye la ISO 29821:2026, según el catálogo de ISO y de
    DIN Media.
  - Es cierto que el tema 9 sólo nombra los ultrasonidos para las fugas, y ningún otro tema los trata.
- **4.2**: la definición 3.3.9 de AIM es literal. La ficha de AENOR confirma: 2019-07-03, En Vigor, corregida el
  2020-06-24, idéntica a la EN ISO y a la ISO 19650-1:2018.
- **5.4**: el art. 3.1 del RD 56/2016 tiene redacción única. El sujeto y el 85 % son literales.
- **6.1**:
  - Atribuciones correctas: «frequently used and studied», «olivine», «Ni-rich… highest thermal reactivity» y
    «safest» son de Yang y otros. La tendencia de peligrosidad, la propagación, el humo blanco y la llama son de
    Su y otros.
  - Volumen 13, 2026, e76502 y los doi son correctos.
  - El anexo VI, parte A, punto 7, recoge la «composición química». El anexo V, punto 11, recoge la «Emisión de
    gases».
- **6.6**: el art. 61.1 del Reglamento (UE) 2023/1542 es literal.
- **7.1**: el art. 2.2 del RD 244/2019 (redacción única) es literal, título del RD 1955/2000 incluido.
- **7.11**: el art. 4 está en su redacción vigente (BOE-A-2026-6544). Sin excedentes no tiene límite de potencia.
  El límite de 100 kW sólo es el 4.2.a).ii.
- **Portada, siglas, «Qué se puede preguntar», «Normativa», «Lo que no da», «Trazabilidad»**: concuerdan con el
  cuerpo.

## Antecedentes

Todos tienen delante su antecedente:

- «La segunda exclusión» (7.1): tabla con dos exclusiones.
- «Su artículo 61.1» (6.6).
- «Una de ellas» (6.1).
- «esa edición» (3.5).
- «Las dos primeras» (2.6).
- «la misma norma» (4.2).
- «la segunda revisión», texto nuevo de la corrección 2: las dos se presentan justo antes.

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 15.005 palabras y 58 epígrafes.

## Ficheros tocados

El tema y este informe.
