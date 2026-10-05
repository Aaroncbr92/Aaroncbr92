# 5 bis · Oficial Técnico Electricista (27) · Tema 16 · Eficiencia energética y sostenibilidad en instalaciones

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/16-eficiencia-energetica-y-sostenibilidad-en-instalaciones.md`.
Entrada: lista de pasajes de `27-T16-remate.md`; diff del remate obtenido contra la copia previa
(`t16-antes.md` del scratchpad). Fecha del encargo 24-09-2026; fuentes leídas el 05-10-2026 (reloj del sistema).
Ficheros tocados: el tema y este informe.

**Resultado: 4 correcciones (1 dato desactualizado, 2 salvedades omitidas, 1 antecedente) y 1 retoque de
prosa. El resto de los pasajes cambiados se confirma en su fuente.**

## Fuentes releídas (05-10-2026)

- RITE, BOE-A-2007-15820 consolidado (`fuentes/canal-sur/`): apéndice 1 (redacción desde 01-07-2021),
  IT 1.2.4.4 (apdo. 6, 20 kW), IT 3.8.2, IT 4.2.3, IT 4.3.3.
- RD 214/2025, BOE-A-2025-7439 consolidado: arts. 11.5 y 12 (sólo dos apartados: confirmado el aviso).
- Reglamento (UE) 2019/1781 (CELEX 32019R1781) y Reglamento (UE) 2021/341, anexo II (CELEX 32021R0341),
  DOUE; Reglamento (UE) 2023/3 (sólo corrige la versión alemana: confirmado).
- Reglamento Delegado (UE) 2024/1364 (CELEX 32024R1364), DOUE L de 17-05-2024: arts. 1, 3.1; anexo II d) y e); anexo III.
- Directiva (UE) 2023/1791, anexo VII (texto en español de la Oficina de Publicaciones).

## Correcciones aplicadas (comprobadas en la fuente)

| # | Pasaje | Error | Fuente | Cambio |
|---|---|---|---|---|
| 1 | 2.4, documentación del motor | 7 (redacción superada): «Desde el 1 de julio de 2021» es la redacción original de la parte 2; el Reglamento (UE) 2021/341 (anexo II, 1.b.2) la sustituye: desde 01-07-2021 para los motores de la parte 1 a) y desde 01-07-2023 para los de la parte 1 b) i) («Ex eb» y monofásicos). El remate decía que sólo usaba el 2021/341 para la sección 1 | 32021R0341, anexo II | Fecha doble, con mención del 2021/341. La cita de la eficiencia nominal sigue siendo literal en ambas redacciones |
| 2 | 2.4, ámbito de los variadores | 6: faltaba la tercera condición del art. 2.1.b | 32019R1781, art. 2.1.b.iii | Añadido **«una única tensión de salida CA»** |
| 3 | 3.4, E IT | 6: faltaba la vía para centros sin SAI | 32024R1364, anexo II e), párr. 2 | Añadida, en literal |
| 4 | 6.1, «pueden acogerse a ella» | Antecedente: tras insertar las dos salvedades nuevas, «ella» apuntaba a la IT 3.8.2.2 | — | «a la salvedad de la IT 3.8.2.3» |
| 5 | 4.1, ejemplos | Prosa: «datos supuestos» repetido dos veces seguidas | — | «Y una enfriadora…» |

## Confirmado sin cambios

Portada y siglas; «Qué se puede preguntar»; 1.2, fila 11.5 (literal, y el aviso sobre el art. 12.3 es
correcto); 2.4: art. 1, art. 2.1.a, calendario de la sección 1 en la redacción del 2021/341, sección 3
(IE2 y −25 % sobre el cuadro 6; la parte 3 no la modifica el 2021/341), fecha y DO de ambos reglamentos,
remisión al epígrafe 3.1 (20 kW, IT 1.2.4.4.6); 3.4: anexo VII a) a c) literal, art. 33.3 de la Directiva
como base del 2024/1364 (considerando de apertura), 500 kW, plazos del art. 3.1, «año natural anterior»,
E DC (punto de medida y generadores aparte), PUE = E DC / E IT, WUE, FRE y coeficiente renovable;
4.1: cita del apéndice 1; 4.2: IT 4.2.3 (quince años **y** más de 70 kW) e IT 4.3.3; 6.1: IT 3.8.2.1
párrafo final (cita truncada antes de «establecidas en la I.T. 1.1.4.1.2…», sin alterar el sentido) e
IT 3.8.2.2; Normativa, «Lo que no da» y Trazabilidad (renumeración 2.4 → 2.5 coherente con el contenido
del antiguo 2.4). Antecedentes «Ese acto delegado», «esos motores», «El mismo anexo»: correctos.

## Lentes (tras las correcciones)

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 16.577 palabras, 36 epígrafes (la extensión de la portada, «unas 16.500», sigue valiendo).
- `negritas.py` con RITE, 2019/1781, 2021/341, 2024/1364, Directiva 2023/1791 y RD 214/2025: todas las
  negritas de los pasajes revisados, «ok»; la fila 11.5 sale como «atribuida al art. 12» por contener
  «artículo 12.3»: falso positivo (está en el art. 11.5). Los «NO ESTÁ» restantes son de pasajes no
  tocados por el remate (RAEE, residuos, gases fluorados), cuyas fuentes no se pasaron.

Tema cerrado.
