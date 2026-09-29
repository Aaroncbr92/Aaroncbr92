# Grafista (15) · Tema 1 · Revisión final (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/01-diseno-grafico-television-radio-visual-web-redes-plataformas.md`.
Fecha del encargo: 24-09-2026; fuentes leídas el 29-09-2026 (fecha de sistema).
Alcance: sólo los pasajes que lista `15-T01-remate.md`, localizados con `diff` contra la copia previa
(`scratchpad/15t01-antes-remate.md`).

**Ficheros tocados**: el tema y este informe.

## Cotejo de los pasajes cambiados

| Pasaje | Fuente | Resultado |
|---|---|---|
| Portada (Fuente, Redacción, Extensión 9.400) | índice: 9.433 palabras | Correcto |
| Siglas: quitadas IU, UX, PNG, JPEG, SVG | — | Correcto; pero el epígrafe nuevo trae «UI» en cita (error 5): **corregido**, sigla añadida |
| M1: 4:5 retirado (l. 186, redes, «Una identidad…», tabla, «Lo que no da») | — | Coherente en los cinco sitios |
| M2: negativos «no consta» | — | Correcto |
| M4: 1.4.11, excepción de controles | `wcag22.txt` l. 532 | Literal exacto; rótulo «Tres precisiones (dos definiciones y una exención)» cuadra con la lista (contraste, texto grande, logotipo) |
| M5: radio visual, literal completado | remate lo comprobó en `radiovision.txt` | Traducción fiel |
| HbbTV: definición, «most powerful…», «call-to-action», «may provide…», botones, cuatro usos, «In general no.» | `hbbtv-org-overview.txt` l. 11, 15, 26, 27, 37-40, 83 | Todos literales; «la asociación que desarrolla la especificación»: l. 30 («developed under the umbrella of the HbbTV Association») |
| Tabla Android TV: 3 m, d-pad, foco, 16:9, 5 %, overscan, tipografía, aparato compartido | `android-tv-design-for-tv.txt` l. 178-188; `android-tv-layouts.txt` l. 10, 26-53, 79; `android-tv-typography.txt` l. 13, 18 | Todos literales; fechas de actualización (08-05-2023, 09-05-2025, 06-07-2026) correctas; las cifras 48/27 y 58/28 dp, efectivamente contradictorias, no se copian |
| Apertura del epígrafe: «pone en la misma lista la plataforma OTT Canal Sur Más… y los servicios HbbTV (puntos 45 y 46)» | Contrato-programa, BOJA 245/2023, puntos 45 y 46 | **Impreciso**: la lista del punto 46 dice «plataformas de streaming OTT» y HbbTV; Canal Sur Más y sus aplicaciones para smartTV están en el punto 45. **Corregido**: cada dato a su punto; literal HbbTV comprobado |
| «Para una pieza de vídeo o de imagen…» (acotación) | oficio | Correcto |
| Trazabilidad (dos filas) y lista de oficio | — | Correcto |

## Antecedentes

- «(punto 46)… (punto 45; los dos, arriba)»: remiten a «El servicio público digital de Canal Sur» (l. 557), que
  va antes y trata los dos puntos. Correcto.
- «(epígrafe anterior)» en «Una identidad, muchas salidas»: el epígrafe anterior es «Plataformas OTT y televisión
  conectada». Correcto.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 9.433 palabras, 38 epígrafes.

## Resultado

2 correcciones menores (sigla UI; atribución a los puntos 45 y 46). Ningún dato sin fuente. Tema cerrado.
