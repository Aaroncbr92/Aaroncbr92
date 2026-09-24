# Puesto 08 · Tema 9 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`
(≈10.000 palabras; 7 epígrafes `##` en el orden del enunciado —foco, exposición, color,
estabilidad, ruido, compresión, continuidad— precedidos de uno general, «La calidad técnica de
imagen», y seguidos de recomendaciones, huecos y trazabilidad). Escrito por partes (portada y
general; foco; exposición; color; estabilidad y ruido; compresión y continuidad; cierre). Índice con
`indice.py`; `refutar_prosa.py`: 0 hallazgos tras presentar SDI, LCD y PLUGE.

## Fuentes

- Material de `08-investigacion-A-imagen.md` (EBU R 103 v3.0, R 118 v2, Tech 3335, Tech 3355;
  UIT-R BT.709-6, BT.2020-2, BT.2100-3; Sony FS5; Blackmagic URSA Broadcast G2), leído por el
  investigador el 24-09-2026. Citas tomadas de ahí sin volver a la fuente (no hay copia local):
  verificación debe cotejarlas.
- Releído por mí el 24-09-2026 en copia local:
  - Sony *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024;
    `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt`): puntos blancos y parpadeo (ll. 259-270),
    monitor de señal (9540-9545), SteadyShot (8814-8836), archivos de escena y menú [Paint/Look]
    (13429-13800: Knee, Black, Detail, Matrix, Multi Matrix), [Noise Suppression] y [Flicker Reduce]
    (12571-12630), conversión HDR→SDR en visor (≈9555).
  - Libro de estilo de Canal Sur (1.ª ed., marzo 2004;
    `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`): 5.1 (p. 79), 5.2 trípode (p. 80),
    6.3.4 armonía (p. 91), 6.4 *raccord* y 6.5 realización (p. 92).
  - Panasonic *AVC-Intra FAQ* (`fuentes/fabricantes/Panasonic_AVC-Intra_FAQ.txt`, pregunta 2):
    intracuadro frente a *Long GoP*. Documento comercial sin fecha; el tema lo advierte.

## Copiado del común

Ninguno. El tema 9 no tiene fila en el común de Canal Sur (`08-args.json`, «comun» sólo para 12,
14, 16 y 17) ni se repite en otro puesto (`AGRUPACION.tsv`: «nuevo»). No se ha copiado de otros
temas del puesto 08 (el 1 y el 2 no están cerrados); el solapamiento con el tema 1 (R 103, *knee*,
ganancia) se ha redactado desde las fuentes y el tema 9 remite al 1 para los mandos.

## Copiado de RTVE (a verificar; oficio, sin precepto que releer)

Texto literal, quitada la negrita de énfasis (en Canal Sur la negrita es sólo cita literal) y todo lo
propio de RTVE: «Ésa es la respuesta oficial a la pregunta N», tablas de opciones falsas, «Los datos
que el examen ha preguntado», avisos de vocabulario de plató y trazabilidad por «plantilla».
- `informacion-grafica/08`: §1 quién ajusta qué (tabla y reparto), §3 levantado y gamma de negros,
  §4 detalle y dependencia del nivel, §5 *knee*, §6 ganancia en pasos y orden, §7 balance, tres
  caminos y aviso del ATW.
- `informacion-grafica/02`: §3 profundidad de bits (condensado), §4 submuestreo, §6 tabla de
  coeficientes de luminancia, §8 instrumentos y lectura del vectorscopio, §10 funciones del monitor
  (sin ALAC), §11 señales de prueba (condensado).
- `informacion-grafica/04`: §6 Seidel, §8 tiraje.
- `realizacion-tv/14`: §2 regla del RCP (una frase), §3 ganancia y ruido, §4 regla del color
  complementario y tabla, §5 *blooming*/*smear*/*moiré* (sin «perla»), §7 punto dulce, §11
  estabilización pasiva/activa.
- `realizacion-tv/12`: §4 muestreo (sólo la idea), §5 transformada del coseno y recuantificación.

## Discrepancias y quitado

1. Porcentajes −1 %/103 %: no están en R 103 v3.0; el tema lo advierte.
2. RTVE da los coeficientes BT.601/709/2020 «verificados»; no los he releído (no hay copia local de
   las recomendaciones): verificación debe cotejarlos.
3. RTVE dice que el material de incrustación se graba «en 4:2:2 como mínimo»: dejado como oficio.
4. Quitado lo no confirmado: blanco HLG en %, umbrales TLCI, igualación con CCU, obturador global,
   filas de la tabla 1 de R 118 no comprobadas (H.264 2J «15/12»). Quitadas por mí dos frases de
   oficio sin apoyo (aviso a entrevistados con rayas; *flash* sobre CMOS).
5. Oficio declarado añadido: defectos de compresión visibles, efecto del ruido y del movimiento
   sobre el códec, remedios de continuidad, balance de negros, temblor en tele.
6. Sony Z200: la frecuencia de [Flicker Reduce] viene de fábrica a [60Hz]; el tema avisa de ponerla
   a 50 Hz en España (deducción de la red de 50 Hz, declarada).

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.

## Autocomprobación: 10 preguntas tipo test

| Nº | Rúbrica | Pregunta (respuesta) | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Calidad (teoría) | ¿Cuál de estos NO es uno de los criterios de EBU R 118 para clasificar cámaras: ruido, sensibilidad, latitud, temperatura de color? (temperatura de color) | Entera: «Qué se mide cuando se habla de calidad» |
| 2 | Foco (teoría) | Con mucha luz, ¿por qué no conviene cerrar el diafragma a f/22 y qué se hace? (difracción; meter ND y dejar el diafragma en zona intermedia) | Entera: «El punto dulce y la difracción» |
| 3 | Foco (práctica) | La imagen enfocada en tele se ablanda al abrir al angular: ¿qué se ajusta y cómo? (tiraje: enfocar en tele sobre punto lejano, ir al angular y corregir con el anillo de tiraje, diafragma abierto) | Entera: «El ajuste de tiraje» |
| 4 | Exposición (teoría) | Según EBU R 103 v3.0, ¿cuál es el rango preferente en 10 bits y a qué límites se ajustan los recortadores en directo? (20-984; a los del rango preferente) | Entera: «Los límites de la señal según la EBU» |
| 5 | Exposición (teoría) | Según EBU Tech 3335, ¿cuánto margen dinámico se pierde por cada 6 dB de aumento del ruido? (un paso) | Entera: «El margen de exposición» |
| 6 | Color (práctica) | Si se hace el balance de blancos sobre un vaquero azul claro, ¿cómo sale la imagen? ¿Qué submuestreo conviene para un croma? (más cálida; 4:2:2 mínimo, mejor 4:4:4) | Entera: «El balance de blancos», «Profundidad de bits y submuestreo» |
| 7 | Estabilidad (práctica) | Grabando en trípode bajo LED con red de 50 Hz: ¿qué se hace con el estabilizador y qué obturación evita el parpadeo? (apagarlo; 1/50 o 1/100) | Entera: «El estabilizador de la cámara», «El parpadeo» |
| 8 | Ruido (práctica) | Imagen bien diafragmada con una sombra ruidosa: ¿qué parámetro ayuda? ¿Qué S/N pide la EBU a una HD Tier 1? (dependencia del nivel; mejor que −48 dB a 0 dB de ganancia) | Entera: «El realce de detalle y el ruido», «Cómo se mide» |
| 9 | Compresión (teoría) | ¿Qué distingue un códec intracuadro de uno *Long GoP* según EBU R 118? (el intracuadro procesa cada cuadro por separado, sin compresión temporal; el *Long GoP* comprime a través de varios cuadros y ahorra más flujo) | Entera: «Intracuadro y *Long GoP*» |
| 10 | Continuidad (teoría y práctica) | ¿Qué diferencias prohíbe el aspecto técnico del *raccord* del Libro de estilo de Canal Sur, y qué ajuste automático conviene evitar para cumplirlo? (color, brillo, contraste, tono, luz, altura de planos, calidad de la imagen; el balance automático continuo) | Entera: «La continuidad técnica», «La continuidad con una sola cámara» |

Resultado: 10 de 10 enteras; no ha hecho falta ampliar.
