# Puesto 30 · Tema 2 · Revisión final (fase 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.
Alcance: sólo los pasajes que lista `30-T02-remate.md`.

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Pasaje del tema | Resultado |
|---|---|---|
| UIT-R BT.709-6, parte 6 (`montador/itu/bt709.txt` l. 820-890; PDF con PyMuPDF: los glifos Symbol U+F0B1 = «±» delante de 350, de 300 y de 2 %) | «La referencia de sincronismo»: cita de la parte 6; 6.1 0/700 mV; 6.2 ±350; 6.3 «Tri-level bipolar»; 6.5 ±300 ± 2 %; 6.6 «Sync on all components»; columnas 60/P a 24/PsF | Todo confirmado y literal |
| SMPTE ST 292-1:2018 (`montador/smpte/st292-1-2018.txt` l. 407, 438-496) | Cita de 8.1.8 (RP 184); tabla 3: B1 10 Hz, B2 100 kHz, B3 «> 1/10 the clock rate», A1 1 UI, A2 0.2 UI, «UI = unit interval»; nota 2 | Confirmado. 8.1 es «Signal Levels and Specifications» del generador: «la salida» es correcto |
| EBU R 68-2000 (`montador/ebu/r068.txt` l. 17-19, 44-48) | 16 bits como parecer («It is of the opinion…»), no en «The EBU recommends» | Confirmado (la parte dispositiva sólo nombra 16 bits en la tabla 1 de códigos) |
| EBU R 128-2023 (`montador/ebu/r128.txt` l. 98-125) | i) ±0.2 LU; j) por debajo de −23.0 LUFS; m) tolerancia ±0.3 dB y salvedad | Confirmado y literal |

## Correcciones aplicadas

1. **Cita cruzada (error 1)**, final de «La referencia de sincronismo»: «El reloj propio del audio
   embebido se ve en el § 2» → «§ 3». El audio síncrono al vídeo (272M, ST 299-1) está en el § 3,
   «La sincronía entre imagen y sonido»; el § 2 no trata el reloj. El remate dio este antecedente
   por bueno: se equivocó.
2. **Antecedente**: «Distingue dos:» → «La tabla distingue dos:», porque la frase anterior tiene por
   sujeto los valores («Se expresan…»), no la ST 292-1.
3. **Trazabilidad, fila R 128**: quitado «en el remate» (referencia al proceso dentro del tema). La
   fecha se mantiene.

Sin otros hallazgos. *Genlock*, *black burst*, UI como duración de un bit y la forma del pulso siguen
declarados como oficio; la RP 184, como no leída.

## Lentes

- `refutar_prosa.py`: 1 aviso, «BC» (falso positivo ya conocido, Y'C'BC'R en cita de la BT.2020).
- Índice: sin cambios de epígrafes; no se regenera. Extensión de la portada sin cambio relevante.

## Ficheros tocados

- El tema y este informe.
