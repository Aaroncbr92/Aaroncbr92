# Grafista (15) · Tema 6 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/06-escenarios-virtuales-realidad-aumentada-pantallas-videowalls-tiempo-real.md`.
Entradas: `15-T06-refutacion.md` (0 graves, 4 menores, 1 laguna) y `15-T06-preguntas.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe (descargas de trabajo en el scratchpad, fuera del repositorio).

**Se amplió contenido nuevo** (L1, unas 330 palabras, y M3): hace falta la fase 5 bis sobre los pasajes 3, 4 y 5.

## Fuentes releídas para comprobar cada corrección (29-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| Epic, *In-Camera VFX Overview* (UE 5.8; volcado local de Realizador) | M3: «The outer frustum remains static…» y «Using a green screen only in the camera's FOV…», literales |
| Epic, *In-Camera VFX Best Practices in Unreal Engine* (UE 5.8, descargada) | L1: las nueve citas, literales; además «Try to keep it at 1 material per asset», «Automatic LODs can produce assets with a softer, indistinct look», el ejemplo 128x256 / 256x256 / 8080x8080 y «We strongly recommend you run performance tests on a regular basis» (paráfrasis) |
| Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output» (descargada) | M2: «Contains Alpha: Defines if this output channel provides key information on the associated key output connector.», literal, bajo «Key Properties» |
| Vizrt, *Viz Engine Administrator Guide* 5.2, «Dual Channel Mode» (descargada) | M2: la cita del doble canal y la del control externo siguen literales; «open the two Viz Engine consoles» sostiene «desde sus consolas» |

Ninguna corrección del informe resultó equivocada; las cinco se aplicaron.

## Pasajes cambiados

1. **Portada, «Fuente»** (M4 y L1): Epic añade *In-Camera VFX Best Practices*; Chyron pasa a «páginas de *PRIME CG* y *About Chyron*, y nota de prensa de PRIME 5.3».
2. **Siglas de entrada** (M1): fuera CGI, PGM, PVW y «fr», que no se usan en el cuerpo (comprobado con grep). Entran «FPS en la documentación de Epic Games» junto a fps y LOD (*level of detail*), que usa el pasaje nuevo.
3. **§1 «La pared de LED: frustum interior y exterior»** (M3): tras la definición del exterior, la cita «The outer frustum remains static…» con su traducción; tras la tarjeta SDI, la razón del croma sólo en el frustum interior («Using a green screen only in the camera's FOV…») y que el exterior sigue dando luz y reflejos.
4. **§1, epígrafe nuevo «Preparar la escena para que el motor la dibuje a tiempo»** (L1), tras «Lo que hace el grafista en un escenario virtual»: las dos preocupaciones de Epic; el objetivo de 48-72 fps en 4K con la salvedad del 2-3x y las pruebas periódicas; niveles de detalle y LOD hechos a mano; materiales y llamadas de dibujo; texturas en potencias de 2 (con el ejemplo de la fuente); luz precalculada frente a trazado de rayos; aprobación de lo optimizado por quien firma el aspecto. Se dice como oficio que valga también para un decorado de croma, porque la guía es de pared de LED. Índice regenerado.
5. **§5 «Qué hace un sistema de grafismo», párrafo tras la tabla** (M2): relleno y llave se apoyan ahora en «Contains Alpha» (5.4, propiedad de la salida) y el texto aclara que no hace falta un modo especial. El doble canal queda como lo que es: dos salidas de programa, que exigen dos tarjetas. «En ese modo, el motor puede gobernarse…» tiene delante su antecedente, el doble canal, y lo dice la misma página. Se quitó una glosa mía («cada una con su relleno y su llave») porque la fuente, «(fill and key on two channels)», no la sostiene sin ambigüedad.
6. **Trazabilidad**: fila nueva para *In-Camera VFX Best Practices* (29-09-2026); el párrafo de oficio añade la extensión de esos criterios al croma.

Releídos los pasajes 3, 4 y 5: todo «esa página», «la misma casa», «en ese modo» tiene delante su antecedente.

## Lentes

Es un tema técnico sin normas, así que sólo se pasan `indice.py` y `refutar_prosa.py`.
- `indice.py`: índice regenerado, con 12.741 palabras en 48 epígrafes. Avisa «sin portada: es un esquema», pero la portada está (líneas 3-13). Parece que el tema no figura en `portadas.tsv`. El aviso es de la herramienta y no del tema, y no se ha tocado.
- `refutar_prosa.py`: da 4 avisos de siglas, que son nombres de producto y de empresa (AMD, NVIDIA, PRIME, CAMIO) ya presentados como tales. No hay relleno, repeticiones ni negritas rotas.

## Preguntas afectadas

Pregunta 2 (antes a medias) y preguntas 14 y 15 (antes no): ahora se contestan enteras con el tema.
