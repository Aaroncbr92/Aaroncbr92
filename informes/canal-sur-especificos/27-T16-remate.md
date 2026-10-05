# Remate · Oficial Técnico Electricista (27) · Tema 16 · Eficiencia energética y sostenibilidad en instalaciones

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/16-eficiencia-energetica-y-sostenibilidad-en-instalaciones.md`.
Entrada: `27-T16-refutacion.md` (0 graves, 4 menores, 3 lagunas) y `27-T16-preguntas.md`. Fecha del encargo
24-09-2026; fuentes leídas el 05-10-2026 (reloj del sistema).

Ficheros tocados: el tema y este informe. Textos de la UE descargados en el scratchpad (no en `fuentes/`):
CELEX 32024R1364, 32019R1781, 32021R0341 y 32023R0003, de publications.europa.eu (EUR-Lex devolvía 202 vacío).

**Resultado: 4 hallazgos aplicados, 3 lagunas cerradas; se ha ampliado contenido nuevo (≈ 1.850 palabras,
de 14.650 a ≈ 16.500).** Pasa a 5 bis.

## Hallazgos: comprobados en la fuente y aplicados

| # | Comprobación (05-10-2026) | Pasaje cambiado |
| --- | --- | --- |
| 1 | RITE (BOE-A-2007-15820), apéndice 1, entrada «Coeficiente de eficiencia energética de una máquina frigorífica»: define COP y EER; apéndice 1 en redacción vigente desde 01-07-2021 | 4.1: la «definición de oficio» del EER se sustituye por la cita literal (COP y EER) y un ejemplo de COP con datos supuestos. Siglas: EER y COP. Trazabilidad: fuera «la definición del EER» de la lista de oficio |
| 2 | RD 214/2025 (BOE-A-2025-7439), art. 11.5: «…el apartado 2 y 3 y el artículo 12.3 en relación con sus emisiones de gases de efecto invernadero» | 1.2, fila 11.5: cita completa. **Aviso (manda la fuente):** el art. 12 vigente sólo tiene apartados 1 y 2; la remisión al 12.3 no casa. Se dice en el tema entre paréntesis |
| 3 | RITE, IT 3.8.2.1 (párrafo final) e IT 3.8.2.2 | 6.1: añadidas las dos salvedades, en literal |
| 4 | RITE, IT 4.2.3: más de quince años **y** más de 70 kW | 4.2, fila «La instalación completa»: ahora «IT 4.2.3 e IT 4.3.3», con el umbral literal |

## Lagunas: ampliaciones

1. **PUE (pregunta 11)**, epígrafe 3.4. Directiva 2023/1791, anexo VII, letras a) a c) (txt DOUE local),
   y Reglamento Delegado (UE) 2024/1364: art. 1 (500 kW), art. 3.1 (plazos), anexo II letras d) y e)
   (E DC antes del conmutador de transferencia; E IT a la salida de los SAI), anexo III letra a)
   (PUE = E DC / E IT) y mención de WUE, FRE y coeficiente renovable. Ejemplo con datos supuestos
   (1.500/1.000 = 1,5) y lectura de oficio declarada. La consulta SPARQL de la Oficina de Publicaciones
   no da actos modificativos del 2024/1364. «Lo que no da»: la línea del anexo VII se sustituye por el
   desarrollo nacional, la EN 50600-4 y los PUE de la casa.
2. **Motores y variadores (pregunta 12)**, nuevo epígrafe **2.4 Motores y variadores de velocidad**; el
   antiguo 2.4 pasa a 2.5 (índice regenerado; cuatro filas de Trazabilidad renumeradas «2.4 → 2.5»).
   Reglamento (UE) 2019/1781: art. 1, art. 2.1, anexo I secciones 1 (calendario IE3/IE2 desde 01-07-2021,
   IE2 Ex eb y monofásicos e IE4 75-200 kW desde 01-07-2023, en la redacción del Reglamento (UE) 2021/341,
   anexo II), 2 (puntos 1 y 2) y 3 (variadores IE2, −25 % sobre el cuadro 6; la parte 3 no la toca el
   2021/341). El servicio de datos sólo lista además el Reglamento (UE) 2023/3, que corrige la versión
   alemana. **La respuesta de la pregunta 12 (IE3) queda confirmada.** Como oficio declarado: aplicación
   a una sustitución y regulación por velocidad frente a estrangulamiento; la relación cuantitativa
   velocidad-potencia no se da (sin fuente leída).
3. **COP (pregunta 13)**: cerrada con el hallazgo 1.

Otros pasajes tocados por coherencia: portada (Fuente, Redacción que se estudia, Extensión), siglas
(COP, PUE, IE, CA, CEN, CENELEC), «Qué se puede preguntar» (EER/COP, clase IE, PUE), «Normativa que el
tema invoca» (anexo VII de la Directiva; filas nuevas 2024/1364 y 2019/1781; RITE con IT 4.2.3 y
apéndice 1), Trazabilidad (filas nuevas y lista de oficio).

Relectura de antecedentes: «Ese acto delegado» (3.4) tiene delante la cita del anexo VII que lo nombra;
«esos motores» (2.4), el art. 2.1.a; «El mismo anexo» (3.4), el anexo III; «Otras dos salvedades» (6.1),
la de recintos especiales.

## Lentes

- `indice.py`: 16.496 palabras, 36 epígrafes; índice regenerado.
- `refutar_prosa.py`: 0 hallazgos (tras presentar CA y CEN/CENELEC).
- `negritas.py` con RITE, Directiva, 2019/1781, 2021/341, 2024/1364 y art. 11 del RD 214/2025: todas las
  negritas nuevas, «ok»; los 7 «NO ESTÁ» que salen son de pasajes no tocados cuyas fuentes no se pasaron.
- `refutar_exactitud.py` / `refutar_modo.py` contra el RITE: las líneas nuevas que salen son citas de
  otras normas (2019/1781, 2024/1364, RD 214/2025), ya cotejadas con `negritas.py`; falso positivo.

## Para 5 bis

Revisar sólo: 2.4 entero; 3.4 desde «Lo que se publica»; 4.1 (cita del apéndice 1 y ejemplo COP); fila
de la IT 4.2.3 en 4.2; párrafo de salvedades en 6.1; fila 11.5 en 1.2; portada, siglas, Normativa,
«Lo que no da» y Trazabilidad.
