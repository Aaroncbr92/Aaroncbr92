# Grafista (15) · Tema 6 · Fase 5 bis (revisión de lo que cambió el remate)

Tema: `temas/canal-sur-especificos/15-grafista/06-escenarios-virtuales-realidad-aumentada-pantallas-videowalls-tiempo-real.md`.
Alcance: sólo los seis pasajes que lista `15-T06-remate.md`. Fecha de trabajo del encargo: 24-09-2026;
las fuentes se descargaron de nuevo y se leyeron el 29-09-2026 (fecha de sistema). Descargas en el scratchpad, fuera del repositorio.
Ficheros tocados: el tema y este informe.

## Fuentes releídas (29-09-2026, descarga propia)

| Fuente | Resultado |
|---|---|
| Epic, *In-Camera VFX Overview in Unreal Engine* (UE 5.8) | «This inner frustum represents…», «Content displayed… outer frustum…», «The outer frustum remains static…» y «Using a green screen only in the camera's FOV…»: literales |
| Epic, *Recommended Hardware for In-Camera VFX* (UE 5.8) | «If you plan to use live green-screen compositing, you will need a SDI video card…»: literal |
| Epic, *In-Camera VFX Best Practices in Unreal Engine* (UE 5.8) | Las nueve citas, literales («Level of Detail» es un enlace en el HTML: el texto es literal). Paráfrasis comprobadas: 2-3x, pruebas periódicas, «1 material per asset», LOD automáticos blandos, ejemplo 128x256 / 256x256 / 8080x8080 |
| Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output» | «Contains Alpha: …», literal, bajo «Key Properties» |
| Vizrt, *Viz Engine Administrator Guide* 5.2, «Dual Channel Mode» | Cita del doble canal y del control externo, literales; «open the two Viz Engine consoles» sostiene «desde sus consolas» |

## Hallazgos y correcciones (todas comprobadas en la fuente)

1. **Cita cruzada (error 1), §1 «La pared de LED»**: «la misma página de Epic» seguía a una cita de *Recommended Hardware*, pero la frase del croma sólo en el FOV está en *In-Camera VFX Overview*. Ahora dice «la página de Epic sobre efectos visuales rodados en cámara (*In-Camera VFX Overview*)».
2. **«Deberá» por «podrá» (error 4), §1 «Preparar la escena»**: «la versión optimizada debe aprobarla» no está en la fuente, que dice «When possible, aim to get optimized versions approved…». Ahora pone «Epic aconseja que, cuando se pueda, … la apruebe». La consecuencia se ajusta a la fuente («otherwise optimization may introduce noticeable visual differences»).
3. **Salvedad omitida (error 6), mismo epígrafe**: la cifra de 48-72 fps era **«a benchmark guideline. However, further testing was required on a target device off-stage»**. Se añade que fue una referencia y que después hubo que comprobarla en el equipo de destino, fuera del plató.
4. **Negrita no literal**: los cinco rótulos de la lista nueva («Un objetivo de rendimiento con margen.», etc.) iban en negrita, pero no son texto de la fuente. Ahora van en redonda.
5. **§5, párrafo de Vizrt**: «No hace falta, por tanto, un modo especial» es una deducción y no está en la fuente. Se marca como tal: «se deduce de que sea una propiedad de cada salida; oficio».
6. **Trazabilidad, fila de Vizrt**: no recogía lo que ahora sostiene la 5.4. Se añade «la llave como propiedad de la salida («Contains Alpha», 5.4)».

## Sin cambios

- Portada: la «Fuente» cuadra con la «Trazabilidad».
- Siglas: CGI, PGM, PVW y «fr» no aparecen en el cuerpo. FPS y LOD sí aparecen, y cada una tiene delante su presentación.
- Traducciones entre paréntesis: fieles.
- Antecedentes: «En ese modo» se refiere al doble canal y «la misma casa» (l. 910) a Vizrt; los dos antecedentes son correctos.

## Lentes

- `refutar_prosa.py`: da 4 avisos de nombres de producto ya presentados (los mismos que en el remate) y ninguna negrita rota.
- `indice.py`: 12.792 palabras en 48 epígrafes. El aviso «sin portada» es de la herramienta, porque la portada está.
