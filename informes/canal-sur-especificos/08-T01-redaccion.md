# Puesto 08 · Tema 1 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/01-camara-sensores-opticas-exposicion.md`
(≈9.700 palabras; 8 epígrafes `##` en el orden del enunciado —cámara, sensores, ópticas, enfoque,
exposición, balance de blancos, ganancia, filtros— + recomendaciones
técnicas, huecos, trazabilidad). Escrito por partes (cámara; sensores; ópticas; enfoque; exposición;
balance-ganancia-filtros; cierre). Índice con `indice.py`; `refutar_prosa.py`: 1 falso positivo
(«PUB», código de catálogo de Canon).

## Fuentes

- Material de `08-investigacion-A-imagen.md` (EBU R 103 v3.0, R 118 v2, Tech 3335; Sony FS5;
  Blackmagic URSA Broadcast G2; Canon XF605), leído por el investigador el 24-09-2026. Citas tomadas
  de ahí sin volver a la fuente (no hay copia local): verificación debe cotejarlas.
- Releído por mí el 24-09-2026 en copia local: Sony *PXW-Z200/HXR-NX800 Help Guide*
  (5-060-574-13(1), 2024; `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt`): foco manual, lupa,
  AF (fase + contraste, zonas, velocidad, sensibilidad, caras), push AF, tiraje automático, diafragma,
  ganancia, obturación, ND (presets y variable, Auto ND, difracción), balance (memorias, preset, ATW),
  estabilizador, cebra, peaking, monitor de señal, píxeles blancos, parpadeo, ficha técnica.
- Nota Fujinon UA22x4.8BERD (18-03-2026; `fuentes/fabricantes/Fujinon_UA22x4.8_nota.txt`), leída el
  24-09-2026: ejemplo de referencia de objetivo (22 × 4,8 ≈ 106 mm).

## Copiado del común

Ninguno. El tema 1 no tiene fila en el común de Canal Sur (`08-args.json`, «comun» sólo para 12, 14,
16 y 17) ni se repite en otro puesto cerrado.

## Copiado de RTVE (a verificar; oficio, sin precepto que releer)

Texto literal, quitada la negrita de énfasis (en Canal Sur la negrita es sólo cita literal) y todo lo
propio de RTVE: «Ésa es la respuesta oficial a la pregunta N», tablas de opciones falsas, «Los datos
que el examen ha preguntado», avisos de reparto y la trazabilidad por «plantilla».
- `informacion-grafica/03`: §1 familias (añadida «y estudio»), §2 cadena fotón-número, §3 CCD/CMOS,
  §4 Bayer y filtro paso bajo, §5 sensor y PdC, §6 curva log y LUT.
- `informacion-grafica/04`: §1 focal, §2 ángulo, §3 número f y velocidad, §4 PdC, §5 círculo e
  hiperfocal, §6 Seidel, §7 bokeh, §8 tiraje, §9 concepto de brida y adaptación, §10 lectura de
  referencia, §11 filtros delanteros, polarizador y razonamiento ND→PdC.
- `informacion-grafica/08`: §1 quién ajusta qué (sin fila DIT), §2 bandera francesa (resumida), §3-4
  levantado de negros y dependencia del nivel (resumidos en «El precio: el ruido»), §5 knee, §6
  ganancia en pasos y orden, §7 balance y tres caminos.

## Discrepancias y quitado

1. **Brida**: RTVE da la B4 como «la mayor de las cuatro» (PL, EF, E). No lo he podido confirmar en
   fuente y recuerdo que PL podría ser mayor; quitada la ordenación y la tabla, declarado en «no da».
2. **Porcentajes −1 %/103 %**: no están en R 103 v3.0; el tema lo advierte.
3. **Método Tech 3335 al 50 % con carta gris**: es de medida de sensibilidad para cámaras log, no
   para exponer; colocado en «Sensibilidad de catálogo».
4. Quitado lo no confirmado: Dual Pixel AF (sólo el nombre), obturador global, blanco HLG en %,
   umbrales TLCI (tema 5), cadencias XF605 (tema 15). RTVE «Normal = el del ojo humano» suavizado a
   «parecido al de la visión humana».
5. Añadido como oficio declarado: ND en pasos (cálculo log₂), 1/50-1/100 con red de 50 Hz, lectura
   de la ficha de sensibilidad, apertura máxima menor en tele.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe (creado el directorio `temas/canal-sur-especificos/08-camara-operador/`).

## Autocomprobación: 10 preguntas tipo test

| Nº | Rúbrica | Pregunta (respuesta) | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Cámara (teoría) | ¿Qué dispositivo convierte las tensiones de cada píxel en código binario? (el conversor analógico-digital) | Entera: «Del fotón al número» |
| 2 | Sensores (teoría) | ¿Qué efecto produce el obturador de persiana de un CMOS con movimiento rápido? (verticales inclinadas, bordes distorsionados, imagen «gelatinosa»; EBU Tech 3335) | Entera: «El obturador de persiana» |
| 3 | Sensores (teoría) | En una máscara de Bayer, ¿qué proporción de filtros es verde y por qué? (la mitad; el ojo toma del verde la mayor parte del brillo) | Entera: «Un sensor con máscara de Bayer…» |
| 4 | Ópticas (práctica) | ¿Qué focal máxima tiene un zoom de referencia 22x4.8? (≈106 mm: relación × focal mínima) | Entera: «Cómo se lee la referencia de un objetivo» |
| 5 | Enfoque (práctica) | Procedimiento de ajuste de tiraje (enfocar en tele sobre punto lejano, ir al angular y corregir con el anillo de tiraje, diafragma abierto) | Entera: «El ajuste de tiraje» |
| 6 | Enfoque (teoría) | ¿Se graba el realce de contornos o la ampliación de la lupa? (no) | Entera: «Las ayudas al enfoque» |
| 7 | Exposición (teoría) | Según EBU R 103 v3.0, ¿a qué límites deben ajustarse los recortadores de cámara en directo y cuál es el rango preferente en 10 bits? (a los del rango preferente; 20-984) | Entera: «Los límites de la señal según la EBU» |
| 8 | Exposición (teoría) | ¿Qué hace el knee? (comprime las altas luces para que quepan en la señal; no cambia la sensibilidad) | Entera: «El knee y las altas luces» |
| 9 | Balance (práctica) | ¿En qué situación falla el balance automático continuo y qué se hace? (color dominante, cielo/mar, o fuentes extremas; balance sobre carta blanca en memoria) | Entera: «El balance automático continuo» y «Cómo se hace» |
| 10 | Ganancia y filtros (práctica) | ¿Cuántos pasos son +12 dB, y cuántos quita un ND 1/64? Para una entrevista en interior con mínima profundidad de campo, ¿qué filtro? (2 pasos; 6 pasos; el ND más denso disponible, abriendo el diafragma) | Entera: «Decibelios y pasos», «La densidad neutra», «El ND para abrir el diafragma» |

Resultado: 10 de 10 enteras; no ha hecho falta ampliar.
