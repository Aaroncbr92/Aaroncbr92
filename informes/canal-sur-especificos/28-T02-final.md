# Puesto 28 · Operador/a de Sonido · Tema 2 · Fase 5 bis, revisión final

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/02-electricidad-y-electronica-aplicada-al-audio.md`.
Alcance: sólo los pasajes que lista `28-T02-remate.md`.

## Fuentes (leídas el 25-09-2026)

| Fuente | Copia | Uso |
|---|---|---|
| DPA, «Electromagnetic interference: EMC, RFI immunity and CMRR» | `fuentes/canal-sur/sonido/fabricantes/dpa-emc-rfi-cmrr.txt` | Párrafo CMRR (4.2) |
| Rane, RaneNote 151 | `fuentes/canal-sur/sonido/fabricantes/rane-note151.txt` | Párrafo masa en estrella (5.2) |
| Rane, RaneNote 110 (ranecommercial.com/legacy/note110.html, bajada con curl a la carpeta temporal de la sesión) | sin copia en `fuentes/` | Para comprobar el antecedente de «Rane añade» (5.2) |

## Cotejo pasaje a pasaje

| Pasaje | Resultado |
|---|---|
| 4.2, CMRR: 6 negritas DPA | Las 6 son literales (una aparición cada una). Contexto correcto: el 65 dB es del previo MMP-A de DPA («un previo suyo»); «cable, equipo que envía y que recibe» está en la fuente. |
| 4.2, «Exige que» | La fuente dice «It is important that». **Corregido**: «Para eso es importante que» (el verbo era más fuerte que la fuente, error 4). |
| 5.2, masa en estrella: 5 negritas RaneNote 151 | Las 5 son literales. La paráfrasis (división analógica/digital; la escuela del jack de entrada es la más razonable para equipos desbalanceados y balanceados con jack de 1/4" y clavija mono) coincide con la fuente. Antecedente: «la misma nota de Rane» sigue a la cita de la RaneNote 151. Bien. |
| 5.2, «Rane añade…» (párrafo anterior, que ahora va detrás del pasaje nuevo) | **Antecedente roto por la inserción.** La cita «also guarantees the best possible protection from RFI…» no está en la RaneNote 151; está en la RaneNote 110 (comprobado en la página publicada). Detrás del párrafo nuevo se leía como si fuera de la 151. **Corregido**: «La otra nota, la RaneNote 110, añade que…». La Trazabilidad ya atribuía la RFI a la 110. |
| 2.3, apunte Crown 1,4 V / +4 dBu | Cálculo rehecho: 0,775 × 10^(4/20) = 1,228 V; 20·log(1,4/0,775) = +5,14 dBu. «epígrafe 2.1» define el dBu. Bien. |
| 1.5, fila C «Más alto que A, B y AB» | Sin fuente de fabricante; la Trazabilidad declara las clases A, B, AB y C como oficio. Se deja así. |
| 3.2, remisión a 4.4 y 5.3 | 4.4 remite a la DI y a los transformadores de aislamiento; 5.3 trata el transformador de aislamiento. Bien. |
| Siglas (EMI, CMRR, EBU, MADI, Dante) | Presentadas antes de su primer uso; desarrollos correctos. Bien. |
| Portada, «Qué se puede preguntar», Trazabilidad | Coherentes con los pasajes nuevos (DPA para el CMRR, fila de la RaneNote 151 con masa en estrella). Bien. |

## Resultado

Dos correcciones (un antecedente roto por la inserción y un verbo más fuerte que la fuente). Ningún
dato quitado. El tema queda cerrado.

## Otros ficheros tocados

Sólo el tema 02 y este informe. La copia de la RaneNote 110 se quedó en la carpeta temporal de la
sesión, no en `fuentes/`.
