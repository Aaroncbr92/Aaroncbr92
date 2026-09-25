# Puesto 28 · Operador/a de Sonido · Tema 4 · Fase 5 bis, revisión del remate

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/04-consolas-de-mezcla-analogicas-y-digitales.md`.
Alcance: sólo los pasajes 1 a 7 que lista `28-T04-remate.md`.

## Fuentes releídas (25-09-2026)

- Yamaha, *CL5/CL3/CL1 V5 Reference Manual* (copia de trabajo `cl5_3_1_en_rm_f0.txt`): MIX SEND,
  «6 PRE/POST button» y su NOTE; BUS SETUP window (p. 252, tabla «Bus type / Pre-fader send point»);
  «Adjusting the faders (Calibration function)», p. 279; pasos del Fade, paso 8.
- Avid, *Pro Tools Reference Guide* 2025.12, cap. 55, pp. 1532-1533 (copia `r28t04/pt.txt`): «Trim
  Mode (Pro Tools Ultimate and Studio Software Only)» y «Trim Automation Modes».

## Comprobación, pasaje a pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Previo o posterior al fader, último párrafo | Las dos citas son literales (NOTE del PRE/POST button). Que el punto previo se fija por bus y no por canal lo confirma también la tabla del BUS SETUP (VARI [PRE EQ] / VARI [PRE FADER]). Correcto |
| 2 | Los modos, fila Trim | Las citas «existing track volume...», «When writing automation in Trim mode...» y «Trim mode works in combination...» son literales, p. 1532. La lista de seis versiones coincide con los rótulos de Avid. Ultimate y Studio: confirmado. Correcto |
| 3 | Cómo se distinguen, viñeta Trim | Las citas de Read Trim, Touch Trim, Latch Trim, Write Trim y Trim Off, así como «Pan, mute and plugin automation cannot be trimmed in this manner», son literales. **Laguna**: Touch/Latch Trim aparecía en la lista, pero sin explicar. **Corregido**: se añade la cita «The main Volume Trim fader follows Touch Trim behavior, and Send level Trim faders follow Latch Trim behavior» (p. 1533) |
| 4 | Un caso práctico | Cuadra con las definiciones: Latch Trim escribe desde el toque hasta la parada; Write Trim, desde que arranca la reproducción; Touch Trim deja de escribir al soltar; Write borra. Está declarado como oficio. Correcto |
| 5 | Qué guarda, párrafo nuevo | «the motion of the motor faders» (p. 279) y «The faders will begin to move immediately after Recall occurs, and will reach the values of the recalled scene over the course of the specified fade time» son literales. No afirma nada de otras consolas. Correcto |
| 6 | Trazabilidad | Las filas de Yamaha y Avid cubren lo añadido. Se añade «Touch/Latch Trim» a la lista de versiones de Avid para que cuadre con el pasaje 3 |
| 7 | Ficha, Extensión 9.900 | `indice.py` da 9.908 palabras. Se deja en 9.900 |

## Antecedentes

Todos tienen delante su antecedente: «ese previo» (el envío previo de la frase anterior), «Cada versión
Trim ... su modo» (la tabla de modos), «el Fade» (el epígrafe «La transición: Fade», que va debajo pero
se nombra con su cita propia), «la escena» y el remite a «Analógica frente a digital», que existe.

## Lentes

`indice.py`: 9.908 palabras, 58 epígrafes, sin error. `refutar_prosa.py`: sin relleno, sin frases
repetidas, sin negritas rotas. Las 8 «siglas» que marca son palabras inglesas dentro de citas
literales y ya estaban (BUSS, LOW, MID, NB, NOTE, OMNI, ST, VARI).

## Resultado

Los cinco pasajes con contenido nuevo son exactos y citan su fuente. Hay una corrección menor (se
añade la definición de Touch/Latch Trim y su fila en Trazabilidad). Queda cerrado.

## Otros ficheros tocados

Sólo el tema y este informe.
