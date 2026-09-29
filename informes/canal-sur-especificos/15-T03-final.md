# Grafista (15) · Tema 3 · Revisión de los pasajes del remate (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/03-grafismo-informativos-programas-deportes-promociones-continuidad-eventos.md`.
Fecha del encargo: 24-09-2026. Fuentes releídas: 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe.

Alcance: los 12 pasajes listados en `15-T03-remate.md`; el resto del tema no se ha revisado.

## Fuentes cotejadas (29-09-2026)

- LGCA, BOE-A-2022-11311 (volcado local; `boe.py precepto` devolvió 404 del BOE): arts. 97, 98 y 99
  leídos enteros; una sola redacción cada uno, aplicable desde el 9-7-2022 (tabla de redacciones).
- *Fonseca* 25 (2022), texto del PDF: pp. 99-100 (Marín, Blanco), tabla de herramientas de LaLiga,
  pp. 106-107 (departamentos, gráfico 1, Resta, Brosel).

## Resultado por pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Términos técnicos (DSK) | Correcto; la glosa se apoya en la cita ATEM del epígrafe 5 |
| 2 | Siglas: Mediacoach | Correcto («sistema de análisis de datos de juego Mediacoach»; «los departamentos implicados … son Mediacoach, Audiovisual, Realización y Grafismo») |
| 3 | Funciones: Marín y Blanco | Correcto. Literales cotejados; la cita de Blanco es paráfrasis de los autores del estudio, y el tema la atribuye al estudio («desarrolla»), bien |
| 4 | Cuatro departamentos | Correcto; «director» y equipo propio (siete personas, Resta) constan; los cuatro rótulos del gráfico 1, literales |
| 5 | Lista de avisos, «abajo» | Correcto; antecedente después, en la sección nueva |
| 6 | Sección de calificación por edades | 98.1, 98.2, 98.4, 98.7, 97, 99.1 y 99.2.c literales. **Tres correcciones** (abajo) |
| 7 | Ficha, Extensión | **Error 3 (recuento)**: decía 9.400; `indice.py` da 10.698 (antes del remate ya daba 10.087 frente a 8.800 declarados). Corregido a 10.700. Los temas 1, 2 y 4 declaran lo que mide la herramienta |
| 8 | Qué se puede preguntar | Correcto |
| 9 | Índice | Correcto (entrada presente) |
| 10 | Normativa | Correcto; «ninguno ha sido modificado» confirmado para 97-99 |
| 11 | Lo que no da | **Corregido**: «los fija el acuerdo» afirmaba el contenido de un acuerdo no leído |
| 12 | Trazabilidad | Correcto |

## Correcciones aplicadas (comprobadas en la fuente)

1. «El aviso de continuidad que la ley sí regula es…» → «Entre los avisos de continuidad, la ley regula
   la calificación por edades.» El «sí» no tenía contraste delante, y «el aviso» único era falso: el
   99.1 regula también la advertencia de contenido perjudicial.
2. «acuerdo de corregulación que firma la Comisión» → «que firmará» (98.2: «firmará»).
3. «Qué símbolos… lo fija el acuerdo de corregulación, no la ley» → «no lo dice la ley, que remite al
   acuerdo de corregulación (98.2)»; igual en «Lo que este tema no da» (error 9: el acuerdo no se leyó).
4. Extensión 9.400 → 10.700 palabras.

## Lentes

`indice.py`: 10.698 palabras, 46 epígrafes (índice sin cambios de rótulos). `refutar_prosa.py`: 0.
No se tocaron negritas.
