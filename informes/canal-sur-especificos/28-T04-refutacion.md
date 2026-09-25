# Puesto 28 · Operador/a de Sonido · Tema 4 · Fase 4, refutación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/04-consolas-de-mezcla-analogicas-y-digitales.md`.
Sólo se ha leído, no se ha corregido nada.

## Alcance

- **Exactitud**: todo menos lo que `28-T04-redaccion.md` lista como «Copiado del común» (bloque de
  alineación de Cámara) y «Copiado de RTVE sin cambios» (nueve pasajes). Lo adaptado de RTVE y lo
  nuevo, sí.
- **Cobertura**: el tema entero frente al enunciado del punto 4 (BOJA núm. 186, anexo V, puesto
  2.28): «Consolas de mezcla analógicas y digitales: niveles, entradas, salidas, buses, auxiliares,
  grupos, matrices, automatización y escenas».

## Fuentes releídas (25-09-2026)

- Yamaha, *CL5/CL3/CL1 V5 Reference Manual* (copia de trabajo `cl5_3_1_en_rm_f0.txt` en el scratchpad).
- Soundcraft, *The Soundcraft Guide to Mixing* (copia de trabajo en el scratchpad).
- Yamaha / D. Gould, *Get on the Bus* (copia de trabajo `bus.txt` en el scratchpad).
- Avid, *Pro Tools Reference Guide* 2025.12: descargado de nuevo hoy de resources.avid.com y pasado a
  texto con `documento.py texto`; cap. 55 «Automation».
- EBU R 68-2000 y EBU Tech 3343-2023 (`fuentes/normas-tecnicas/`).

Método: script que saca cada cita en negrita **«…»**, la parte por «[...]» y busca cada trozo en las
seis fuentes normalizadas. 117 citas; 110 casan por script; las 7 restantes (procedimiento PFL de
Soundcraft, R 68, Tech 3343 § 8.1, canal MATRIX, Mix Minus, contenido de escena, entrada de la
matriz) son listas con viñetas o cortes de línea en «STEREO/ MONO» y «MIX/ MATRIX»: comprobadas a
mano, literales. Después, lectura de cada afirmación en redonda que se apoya en fuente (cifras,
modos, alcances).

## Exactitud: conforme

Conforme en la fuente: los diez bloques del canal CL y su orden (con el aviso sobre LEVEL/DCA 1-16,
cuya descripción en el manual es la de un efecto: es así en el manual); DIGITAL GAIN; puntos de
inserción (PRE EQ, PRE FADER, POST ON) y de salida directa (cuatro); compensación de ganancia y uso
de la ganancia digital; puntos de escucha PFL/AFL/POST PAN del canal de entrada; modos ST/MONO y LCR
elegidos canal a canal, mando CSR; FIXED/VARI y MATRIX siempre VARI; botón PRE/POST por canal
emisor; SENDS ON FADER; Mix Minus; órdenes y atenuador de órdenes; oscilador (senoide o ruido rosa)
y su finalidad; dieciséis DCA, DCA de salidas desde CL V3.0, DCA guardados con la escena; ocho grupos
de silencio para entradas y salidas; escenas 000-300, 000 de sólo lectura, contenido de la escena,
Recall Safe con su salvedad, Focus y Fade; *Get on the Bus* (envíos, matriz, órdenes, subgrupo, VCA,
«in most mixing consoles»); Pro Tools (Off, Read, Write, Touch, Latch, Touch/Latch, «After Write
Pass, Switch To», Latch en mandos giratorios, Trim relativo, sólo volumen y envíos, Touch/Latch y
Trim sólo en Ultimate y Studio); R 68 (1:8, 18,06 dB; «the only reliable method…»); Tech 3343 § 8.1.
Cálculos (−3 + 4 = 1; 40 + 3 − 5 = 38): correctos. Remisiones a los temas 1, 2 y 5 comprobadas: el
tema 1 tiene «Polaridad no es fase»; el tema 2, la ganancia «all at once at the input mic stage»; el
tema 5, «Por qué 18 dB de reserva».

## Hallazgos

### Graves

Ninguno.

### Menores

1. **Error 6 (salvedad omitida) · «Previo o posterior al fader: la regla», último párrafo.** El
   tema dice que en la CL «el punto del envío se elige canal a canal» y sigue: «Y en previo se puede
   elegir además **«PRE EQ (immediately before the EQ) or PRE FADER (immediately before the
   fader)»**». El manual lo pone **por bus**, no por canal: «If the PRE/POST button is on, you can
   also select PRE EQ (immediately before the EQ) or PRE FADER (immediately before the fader) **for
   each MIX/MATRIX bus**. This setting is made in the BUS SETUP window». Tal como está, el lector
   entiende que también PRE EQ/PRE FADER se elige canal a canal (pregunta 8, a medias). Propuesta:
   añadir «para cada bus MIX/MATRIX, en la ventana BUS SETUP» con la cita.
2. **Error 6 (salvedad omitida) · «Los modos» (fila Trim) y «Un caso práctico».** Avid: «Trim mode
   works in combination with the other Automation modes (Read, Touch, Latch, Touch/Latch, and Write)»,
   y describe Trim Off, Read Trim, Touch Trim, Latch Trim y Write Trim. El tema presenta Trim como un
   modo más, al lado de Read o Touch, y el caso dice «se pone la pista en Trim» sin decir con qué modo
   se combina (pregunta 13, a medias). Propuesta: añadir la cita de la combinación a la fila Trim y, en
   el caso, decir en qué modo de Trim se hace el pase (p. ej., Touch Trim o Latch Trim, con lo que Avid
   dice de cada uno), comprobándolo en el cap. 55.

### Observaciones (sin cambio obligado)

- Varias citas cortan la frase de la fuente sin «[...]» al final (Touch: sigue «at a rate determined
  by the AutoMatch and Touch Timeout settings»; Latch: sigue «of the automation pass by changing the
  Automation mode to Read or Touch»; punto de inserción CL: sigue «(immediately after the [ON] key)»).
  No cambian el sentido.
- «Las órdenes van a los buses que se elijan […], nunca al programa (oficio)»: el «nunca» es fuerte
  para una costumbre de oficio; el manual sólo dice «to the desired bus». Podría decirse «no al
  programa, salvo que se quiera» o dejarse como está, declarado.

## Cobertura

Las nueve materias del enunciado tienen rúbrica propia, en su orden, más la del título. Resultado
de las 15 preguntas (`28-T04-preguntas.md`): **12 enteras, 2 a medias (8 y 13, por los menores 1 y
2), 1 no (15)**.

### Laguna

1. **Faders motorizados (analógicas y digitales / escenas).** El tema dice que la escena guarda
   **«the position of the top panel faders»**, pero no explica cómo quedan los faders físicos al
   recuperarla: en la CL son motorizados (el manual habla de «the motion of the motor faders» en
   «Adjusting the faders (Calibration function)», p. 279). Es la pieza que une la memoria de escena
   con la superficie de control y una pregunta de test esperable. Ampliar con una o dos frases en
   «Analógica frente a digital» o en «Qué guarda», con la cita del manual CL; la afirmación general
   sobre otras consolas, sólo si se encuentra fuente.

## Lentes

Tema técnico sin norma legal: no aplican `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.
`refutar_prosa.py` e `indice.py` ya los pasaron redacción y verificación; no hay cambios desde entonces.

## Nota sobre el reuso

El redactor midió en torno a un 8 % de texto literal de RTVE (15 % con lo adaptado), no el 75 % que
se suponía: casi todo el tema es material nuevo de Yamaha, Soundcraft y Avid.

## Otros ficheros tocados

`informes/canal-sur-especificos/28-T04-preguntas.md` y este informe. Copia de trabajo del manual de
Pro Tools en el scratchpad (`r28t04/`). El tema no se ha tocado.
