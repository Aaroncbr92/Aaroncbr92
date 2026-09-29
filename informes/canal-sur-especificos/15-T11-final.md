# Grafista (15) · Tema 11 · Fase 5 bis (revisión de lo cambiado en el remate)

Tema: `temas/canal-sur-especificos/15-grafista/11-derechos-autor-bancos-imagenes-tipografias-licencias-imagen-atribucion.md`.
Alcance: sólo los pasajes que lista `15-T11-remate.md`, localizados con `diff` contra la copia previa
al remate (scratchpad `15t11-antes-remate.md`). Fecha del encargo: 24-09-2026; fuentes leídas el
29-09-2026 (fecha de sistema). Copia previa a esta fase: scratchpad `15t11-antes-5bis.md`.

## Ficheros tocados

- El tema (4 cambios, abajo).
- Este informe.

## Comprobación, dato a dato

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| Getty, uso compartido RF (viñeta y fila del epígrafe 7) | `www_gettyimages_com_eula.txt`, «Sharing and Storage Restrictions for RF Content» | Literal y completo |
| Getty, IA: alcance, excepción (i)/(ii), entrenamiento indirecto, «Social Media & AI Tool Termination» (viñeta y dos filas) | Misma fuente, «No Machine Learning…» y «Termination» | Literal; paráfrasis fieles |
| Ley de Marcas, arts. 4, 31, 34.1, 34.2.a-c, 34.3.e-f, 37.1.a-c, 37.2 | `boe.py --fecha 20260924`, BOE-A-2001-23093: 4, 34, 37 en redacción RDL 23/2018 (vig. 14-01-2019); 31 original | Literal; portada y Trazabilidad coinciden con la cadena de redacciones |
| TRLPI arts. 14, 35.1, 146 (citados en los pasajes nuevos) | BOE-A-1996-8930 vigente a 24-09-2026 | Correcto; 35.1 está en el epígrafe 4 |
| ® y TM ausentes de la Ley de Marcas | `grep` en el volcado: 0 y 0 | Confirmado |
| CC material adaptado, música sincronizada, 2(a)(4) | BY-NC 4.0 es (sección 1 y 2); BY-ND en, «timed relation» | Literal |
| CC NC: 2(a)(1), definición, 2(b)(3) | BY-NC 4.0 es | Literal (el volcado trae «NoComercial , a»: artefacto) |
| CC ND: 2(a)(1) y 3(a)(1) | BY-ND 4.0 en; numeración confirmada en el HTML de creativecommons.org (párrafo dentro de `s3a1`) | Correcto |
| Aviso sobre la traducción española de BY-ND | BY-ND 4.0 es, línea 241 («solamente para fines NoComerciales») y 162 (nombra la BY-NC-SA) | Confirmado |
| CC SA 3(b)(1); 2(b)(1)-(2) | BY-NC-SA 4.0 es; BY-NC 4.0 es | Literal |
| CC0 secciones 2, 3, 4 | CC0 1.0 es | Literal |
| OMPI, «¿TM o ®?», n.º 900.1S, 2019, ISBN | `ompi-pub-900-1-es.txt` | Literal; salvedad incompleta (ver 2) |
| Antecedentes: «Ley de Marcas», «arriba» (ARASAAC), «el mismo párrafo», «(epígrafe 3/4/5)», «tema 12», licencia delante de cada sección | El tema | Todos tienen antecedente |

## Correcciones aplicadas (comprobadas en la fuente)

1. **Siglas, CC0** (error 9, leve). Decía «la renuncia de Creative Commons al dominio público»: quien
   renuncia es el titular, no Creative Commons. Ahora: «la dedicación al dominio público de Creative
   Commons, con la que el titular renuncia a sus derechos de autor y conexos» (CC0 1.0 es, secciones 2 y
   pie «CC0 de Dedicación al Dominio Público»).
2. **Epígrafe 6, OMPI** (error 6, salvedad omitida). La advertencia de la guía dice que no refleja el
   punto de vista «de los Estados miembros ni el de la Secretaría de la OMPI»; se añade «ni el de su
   Secretaría».
3. **Epígrafe 3, art. 37.1.b** (concordancia con la fuente). «de indicaciones descriptivas «relativos
   a…»» pasa a «de signos o indicaciones «relativos a…»», como dice el artículo.

Sin hallazgos en Getty, Ley de Marcas, textos CC ni cuadros.

## Lentes

`refutar_prosa.py`: 0. `indice.py` (tema 11): 52 epígrafes, índice sin cambios. Extensión: ~19.000.
