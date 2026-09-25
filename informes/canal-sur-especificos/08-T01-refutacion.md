# Puesto 08 · Tema 1 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/01-camara-sensores-opticas-exposicion.md`
(tras la verificación, ≈9.800 palabras). Copiado del común: ninguno (`08-T01-redaccion.md`), así que se ha
refutado todo. Sólo leídos: `ENCARGO.md`, el enunciado del puesto 08, los informes de redacción y
verificación del T01 y la copia local del Sony *PXW-Z200 Help Guide* (5-060-574-13(1)) y de la nota
Fujinon UA22x4.8BERD, leídas el 24-09-2026. Las recomendaciones EBU no tienen copia en `fuentes/`: sus
citas se dan por cotejadas en la verificación y no se han vuelto a leer.

## Lente 1 · Exactitud

### Graves

1. **SDI y LUT de monitorización (error 9 / 6 salvedad omitida)** — epígrafe «Las curvas logarítmicas y
   el visor»: «La salida SDI lleva la misma señal logarítmica: un monitor conectado ahí verá la misma
   imagen lavada, salvo que el propio monitor aplique una LUT. La interfaz es un transporte, no un
   procesador.» La propia fuente que cita el tema lo contradice: el Z200 Help Guide tiene el ajuste
   «[SDI/HDMI] (PXW-Z200 only) [LUT On] / [LUT Off] … Selects whether to apply a monitor LUT to the SDI and
   HDMI output video» (de fábrica [LUT Off], configurable en modo log), y otro para «LCD/VF/Proxy/Stream».
   Es decir, la cámara sí puede sacar la LUT por SDI. Propuesta: «Por defecto, la salida SDI lleva la
   señal logarítmica, pero muchas cámaras permiten aplicar la LUT de monitor a cada salida por separado
   (la Z200, a SDI/HDMI y a pantalla/visor)»; revisar la tabla «Sin LUT / Con LUT» en consecuencia y
   quitar «La interfaz es un transporte, no un procesador» como argumento.

### Menores

2. **180° y 1/50 (error 6)** — «La obturación»: tras definir 180° como la mitad del cuadro, la cita de
   Tech 3335 («1/50 second for 50 Hz … or 180 degrees for either») deja entender que 180° = 1/50 siempre.
   Sólo lo es a 25 cuadros; a 50p, 180° = 1/100. Añadir la salvedad (cuenta: ángulo/360 × 1/cadencia).
   Provoca la respuesta «a medias» de la pregunta 10.
3. **Montura B4 = prisma de tres sensores (error 9, generalización)** — «La montura y la distancia de
   brida»: «Los objetivos de televisión de 2/3 de pulgada usan la montura B4, detrás de la cual va el
   bloque de prisma de tres sensores». Hay cámaras de un solo sensor con montura B4 (probablemente la
   propia URSA Broadcast G2 que el tema cita; no confirmado en copia local). Propuesta: «detrás de la
   cual suele ir…», o quitar la subordinada si no se confirma.
4. **Adaptación por brida «nunca» (error 6)** — «nunca a uno cuya brida sea más larga»: vale para un
   anillo sin óptica; los adaptadores con óptica correctora existen. Precisar «con un simple anillo» o
   declararlo como oficio con su límite.
5. **Factores de la profundidad de campo (coherencia interna)** — la tabla da tres factores (diafragma,
   focal, distancia) y el razonamiento sensor-PdC dice «El tamaño del sensor no aparece en esa lista»,
   pero el epígrafe siguiente mete el círculo de confusión como criterio de cálculo, que depende del
   formato. No es falso, pero un tribunal que pregunte «factores de la PdC» puede incluir el círculo de
   confusión; conviene mencionarlo en la tabla o en una línea.
6. **Residuos de respuesta de examen y repeticiones (prosa)** — «la palabra que decide es "binario"»
   («Del fotón al número») y la justificación del distractor «obturación» en la hiperfocal vienen de
   corregir preguntas de RTVE; el orden de mandos con poca luz se repite en «Los cuatro mandos» y «La
   ganancia es el último recurso». Recortar sin perder datos.

Comprobado sin hallazgo (en copia local): tiraje automático Z200 (tele, angular, [Auto FB Adjust]),
ATW y sus límites, memorias y preajustes de balance (Custom 3200/4300/5600/6300 K; log 3200/4300/5500 K),
2000-15000 K, ganancia −3/+36 dB, valores de ND 1/4…1/128, AF ([1(Locked On)], [7(Fast)]), lupa ×3/×6,
cebra 0-109 %, difracción y ND, nota Fujinon (4,8-106 mm, 22x). Cuentas: dB/pasos, ND/pasos, 22 × 4,8,
hiperfocal (mitad al infinito). Observación sin corrección: el paso 3 del balance sobre carta dice
«con el diafragma en manual»; la fuente sólo dice «Adjust the brightness» (añadido de oficio inocuo).

## Lente 2 · Cobertura del enunciado

Las ocho rúbricas (cámara, sensores, ópticas, enfoque, exposición, balance de blancos, ganancia y
filtros) están, en su orden. Preguntas: 12 enteras, 1 a medias, 2 no (`08-T01-preguntas.md`).

### Lagunas (a ampliar con fuente, no de memoria)

7. **Extensor óptico del zoom** — el tema nombra el «extensor» entre las letras de la referencia, pero
   no dice qué hace ni cuánto cuesta en luz (pregunta 14). Pregunta previsible en cámara de hombro con
   zoom B4. Buscar en documentación Fujinon/Canon de un zoom con extensor ×2.
8. **Balance de negros** — ausente del epígrafe de balance (pregunta 15); es ajuste clásico de las
   cámaras de hombro y de estudio. Ampliar con un manual de cámara broadcast que lo describa; si no se
   encuentra fuente, declararlo en «Lo que este tema no da».

Sin laguna: detalle/realce electrónico, igualación de cámaras y ruido de compresión quedan remitidos al
tema 9, y la temperatura de color al tema 5, como dice «Lo que este tema no da».

## Lentes automáticas

Tema técnico sin norma: no se pasan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`; la
verificación ya pasó `refutar_prosa.py` e `indice.py` y no se ha tocado el tema.

## Otros ficheros tocados

Ninguno, salvo este informe y `08-T01-preguntas.md`. El tema no se ha modificado.
