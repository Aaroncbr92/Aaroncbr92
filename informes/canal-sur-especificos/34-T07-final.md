# 34 · T07 · Revisión del remate (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/07-redaccion-audiovisual-television.md`.
Alcance: sólo los pasajes que cambió el remate (lista de `34-T07-remate.md`), identificados con `diff`
contra la copia previa `T07-34-antes-remate.md` de la carpeta temporal.

## Fuentes releídas (24-09-2026)

| Fuente | Cómo |
|---|---|
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004) | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`, `grep -n` / `sed -n`; página por la marca de página del volcado |
| Manfredi Díaz, A. (2010), «Escribir para televisión. La imagen manda», pp. 129-145 | `manfredi.txt` (carpeta temporal, del PDF de idUS); páginas por las marcas «!138»…«!145» (cada marca abre su página) |
| Ficha idUS hdl.handle.net/11441/74192 | Leída en línea: autor «Manfredi Díaz, Antonio», Reig García (Ed.), *La dinámica periodística: perspectiva, contexto, métodos y técnicas*, pp. 129-145, Sevilla, Asociación Universitaria Comunicación y Cultura, 2010, ISBN 9788493760007: coincide con «Trazabilidad» |

## Pasajes revisados

| # | Pasaje | Fuente | Resultado |
|---|---|---|---|
| 1 | § 1 «Imágenes falsas y música» | LE 3.2.2, p. 46 | Literal. Antecedentes bien |
| 2 | § 2, tabla, salidilla | LE, p. 116 | Literal |
| 3 | § 4, lengua extranjera | LE 3.7.1, p. 52 | Literal y en el orden de la fuente; «método» remite al desglose. Bien |
| 4 | § 6, atribución en reportaje y crónica | LE 3.5, p. 49 | Literal; el texto está en 3.5 (no en 3.5.1), como cita el tema |
| 5 | § 7, «Tópicos» | LE 3.6.1, p. 50 | Literal |
| 6 | § 9, nuevo subepígrafe (Manfredi) | pp. 138, 139-140, 143, 144 | Citas literales y páginas correctas. **Un error corregido** (abajo) |
| 7 | § 11, «Vídeo recortable» | LE 3.2.1, p. 45 | Literal; «Es muy recomendable» + «que escribamos…» salta un inciso («en una noticia básica o en cualquier formato…») sin cambiar el sentido. Bien |
| 8 | § 11, «Versiones» | LE 3.15, pp. 56-57 | Literal; «Si se prevé…» parafrasea «También puede preverse… que un vídeo sea emitido»; «entonces» tiene antecedente |
| 9 | Portada, «no da», «Trazabilidad» | Ficha idUS | Bien, con dos retoques (abajo) |

## Correcciones aplicadas (comprobadas en la fuente)

1. **§ 9, viñeta del espacio de trabajo** (error 1, antecedente). El tema decía «En el mismo espacio de
   trabajo», como si fuera el de iNews. En Manfredi (p. 139) «El espacio de trabajo de este sistema»
   es el de **iNews Instinct**, herramienta que Avid lanzó en 2005 para que los periodistas creen piezas
   con texto y vídeo «sin la necesidad de aprender una aplicación profesional de edición no lineal»;
   el párrafo de iNews viene después. Reescrita la viñeta nombrando iNews Instinct.
2. **Trazabilidad**, fila del Libro de estilo: «Todo el tema salvo lo atribuido a RTVE» → «… a RTVE y a
   Manfredi» (recuento/alcance que ya no cuadraba).
3. **Portada, Extensión**: 5.033 palabras (recuento de `indice.py` tras la corrección; lo puse a mano,
   porque `indice.py` no reescribe esta portada).

## Nada más que objetar

- «iNews, de Avid»: el apartado 7 de Manfredi es «El ejemplo de Avid» y describe iNews dentro de él. Se admite.
- Dato de Avid en Canal Sur: fechado en 2010 en el tema y en «no da». Bien.

## Lentes

- `indice.py`: 5.033 palabras, 30 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.

Ficheros tocados: el tema (§ 9, Trazabilidad, portada) y este informe.
