# Puesto 28 · Operador/a de Sonido · Tema 2 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/02-electricidad-y-electronica-aplicada-al-audio.md`.

## Pasajes copiados: sólo comprobación de literalidad

Script de cotejo frase a frase y celda a celda (sin `**` ni ✔, espacios normalizados) contra RTVE
`sonido/01` y `sonido/11`.

- **Copiado del común**: ninguno (lo dice el informe de redacción).
- **Copiado de RTVE sin cambios**: todas las frases y celdas listadas son subcadena de su fuente. Seis
  sólo lo son sin distinguir mayúsculas (1.4 «El interruptor diferencial compara…»; 3.4 paso 3; 3.5
  «Un cable de micrófono y un cable AES3…»; 4.2 párrafo de la señal en oposición; 6.2 «El ruido no
  guarda relación…»; 7.5 tabla y párrafo «La diferencia de fondo…»): el redactor bajó a minúscula
  las versalitas de énfasis de RTVE (CUADRADO, NO, POLARIDAD OPUESTA, DIFERENCIA). Literales. No se
  re-verifican.
- Pasajes no listados pero literales de RTVE (tabla del multímetro 3.6, frase de la THD del 0,1 %):
  literales; la del 0,1 % figuraba como «adaptada» y no lo está.

## Fuentes releídas

| Fuente | Fecha de lectura | Resultado |
|---|---|---|
| RD 2032/2009, BOE-A-2010-927, `boe.py precepto` bloque `cii` (vig. 30-04-2020, BOE-A-2020-4707) | 25-09-2026 | Tabla 3: filas del voltio (W/A), faradio (C/V) y ohmio (V/A) literales. Publicación: BOE núm. 18, de 21-01-2010 (dato ya comprobado en la verificación del tema 1) |
| Rane, RaneNotes 110, 124, 135, 151, 155 y 169 (ranecommercial.com/legacy/noteNNN.html) | 25-09-2026 | 50 citas literales (las de 151 y 155 venían «a través del informe»: releídas). Fechas de redacción/revisión de la Trazabilidad, correctas. Paráfrasis conformes: −0,04 dB, «thanks to Mr. Ohm» (impedancia y tensión bajas, corriente alta), DI como forma de aislar, «too costly» = «caros», malla a chasis «at each end», AES-2id-2006 y +3 dBFS |
| DPA Mic University (autor E. Bøgh Brixen en las cuatro páginas): phantom, especificaciones, 10+ statements, polaridad | 25-09-2026 | 20 citas literales; Neumann 1966/NRK, 150 dB en los labios con 1 y 10 mV/Pa, IEC 60268-4 citada en la página de especificaciones, «dynamic microphones behave a little differently» conformes |
| Schoeps, «Phantom Power P48/P12» | 25-09-2026 | 6 citas literales; P12 como fantasma a 12 V, conforme |
| Crown, FAQ (crownaudio.com/en-US/faq_categories/1) | 25-09-2026 | 4 citas literales (sensibilidad 0,775/1,4 V/26 dB, amortiguamiento, calibre, pines XLR/TRS) |
| Texas Instruments, AN-1497 (SNAA034A, 2006, rev. 2013), volcado local | 25-09-2026 | 3 citas literales (78 %, 30-40 %, 90 %, PWM) |

Cálculos rehechos, correctos: √(0,001 × 600) = 0,775 V; 20 log 2 ≈ 6 dB; +20 dBu = 7,75 V;
+4 dBu + 12/20 dB = +16/+24 dBu; 24 Ω y 2,67 Ω; 8 ∥ 4 = 2,67 Ω. Remisiones a los temas 1, 3, 4, 10,
11, 13 y 16: esos temas tratan lo remitido.

## Hallazgos y correcciones aplicadas

1. **Error 8/7 (publicación y redacción).** Normativa: «BOE núm. 21, de 24/01/2010» → núm. 18, de
   21/01/2010; «Vigente el 21/12/2022» (fecha de corte de RTVE) → vigente el 24/09/2026, capítulo II
   en la redacción en vigor desde el 30/04/2020. Mismo cambio en la portada y en Trazabilidad, que
   además decía leída «en el texto del temario de RTVE»: ahora, en el BOE consolidado.
2. **Error 6 (salvedad omitida).** RaneNote 124 da los 6 dB balanceado/desbalanceado para «many
   (most?)» procesadores y exceptúa **las salidas con transformador y las de acoplamiento cruzado**.
   Añadida la salvedad en 2.4; el punto 3 de 4.2 («Una salida balanceada activa entrega 6 dB más»)
   pasa a «Muchas…; no las de transformador ni las de acoplamiento cruzado».
3. **Error 9.** 1.5, fila de la clase D, «Casi todas las etapas de potencia actuales de
   sonorización»: venía de RTVE sin fuente; TI no lo dice. Queda «Etapas de potencia en las que el
   rendimiento manda», y la clase D como conmutación se declara oficio en Trazabilidad.
4. **Error 9 (menor).** 3.2: «3.4 kΩ, muy por encima de la impedancia de salida de un micrófono
   profesional» no estaba en DPA así; se sustituye por lo que DPA dice en ese mismo pasaje (carga de 5
   a 10 veces la impedancia de la fuente; con 100 Ω, al menos 500-1.000 Ω; con *phantom* no es
   problema).
5. **Error 9 (menor).** 7.4, «en un reparto pasivo… sólo una debe dar la phantom»: sin fuente de
   fabricante (viene del tema 11 de RTVE, oficio). Correcto; se añade a la lista de oficio. Idem el
   papel del par trenzado en 4.2.
6. **Precisión.** 2.1: «la AES define» → «un documento informativo de la AES (AES-2id-2006)», que es
   lo que Rane cita. Portada: faltaba la RaneNote 155 en la lista. Trazabilidad: quitado «a través del
   informe de investigación» (todo releído en su fuente).

Pasajes cambiados releídos: sin «ese artículo»/«dicha» colgantes; cada «epígrafe N» apunta bien.
Sin hallazgo pero comprobado: aviso 1 del redactor (−10 dBV como máximo doméstico, no nominal) está
bien dicho.

## Lentes

`negritas.py` (RD vigente, seis RaneNotes, cuatro páginas DPA, Schoeps, Crown, TI): 93 negritas; 8
«no está», todas falsas alarmas revisadas a mano (rótulos del tema, citas con «…», y en RaneNote 169
la llamada de nota «1» entre «rms» y «level»). `refutar_exactitud.py` y `refutar_modo.py` (RD): 0
hallazgos (la primera deja 1 cita «sin comprobar» por artículo fuera de fuente: el tema no cita
artículos; falsa alarma). `refutar_prosa.py`: 0. `indice.py`: 8.133 palabras, 39 epígrafes; «sin
portada» porque no hay fila en `portadas.tsv` (no tocado).

## Otros ficheros tocados

Sólo el tema y este informe. Descargas de trabajo en el directorio temporal de la sesión.
