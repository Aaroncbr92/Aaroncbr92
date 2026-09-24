# T10 · Comprobación independiente del remate · Protección de datos de carácter personal

Hecha por un agente distinto del que remató y se comprobó a sí mismo (`T10-remate.md`,
`T10-refutacion-final.md`). Alcance: sólo los diez pasajes que lista el remate, sus antecedentes y
las lentes automáticas. Fuentes leídas el 24-09-2026: `DOUE-L-2016-80807` (y sus correcciones de
2018 y 2021: ninguna toca los arts. 7, 35, 77, 79, 82 ni el 83.4.a), `BOE-A-2018-16673` (el
art. 77 también a fecha 21-12-2022 con `boe.py --fecha`), `BOE-A-2014-7534`; considerandos, en la
página del BOE del Reglamento.

## Correcciones

| # | Dónde | Qué decía | Qué dice | Fuente | Gravedad |
|---|---|---|---|---|---|
| 1 | Regla nemotécnica del régimen sancionador (l. ~1360), **introducida por el propio remate (H1)** | «…del artículo 8, que el 83.4.a) incluye junto con los artículos 11 y 25 a 43)» | «…junto con los artículos 11, 25 a 39, 42 y 43)» | RGPD 83.4.a): «a tenor de los artículos 8, 11, 25 a 39, 42 y 43». Los arts. 40 y 41 (códigos de conducta) no están en esa letra | Cambia la respuesta (el propio cuadro de la línea 1351 lo decía bien: el remate se contradijo) |
| 2 | Recursos, responsabilidad e indemnización (l. ~665), **ampliación del remate** | «(artículo 79.1), ante los tribunales del Estado miembro del establecimiento del responsable o encargado, o de la residencia habitual del interesado» | Pasa a 79.2 con su rótulo y añade la salvedad: salvo que el responsable o encargado sea una autoridad pública de un Estado miembro que actúe en ejercicio de sus poderes públicos | RGPD 79.2, segunda frase: «a menos que el responsable o el encargado sea una autoridad pública de un Estado miembro que actúe en ejercicio de sus poderes públicos» | Induce a error (salvedad omitida y atribuida al 79.1; pertinente para una entidad pública como la RTVA) |

Nota: los dos cambios aparecen ya en el commit `4dcebbb` (12:51), hecho por otra sesión mientras
esta trabajaba; el reajuste de la línea partida del nº 2 queda en el árbol de trabajo.

## Pasajes del remate comprobados sin hallazgo

- Art. 7.1 y 7.3 RGPD (l. ~449): literales y resumen fiel.
- Art. 77.1 y 82.1 RGPD (l. ~660): literales.
- Art. 72.1.d) LOPDGDD (l. ~1295): literal.
- Art. 35.3.a) RGPD (l. ~891): literal en lo citado.
- Art. 88 LOPDGDD, tabla (l. ~2037): fiel a 88.2 y 88.3.
- Art. 44 LOPDGDD (l. ~1016): literal; la frase quitada no vuelve.
- Ley 1/2014, tabla (l. ~2059): el cuerpo cita sólo 43, 45 y 48; comprobados 43 y 45 contra la fuente.
- «diecisiete bloques» (l. ~283 y ~2107): son diecisiete los bloques del `.redacciones.tsv` con más
  de una redacción o añadidos después de 2018.
- Art. 77.3 LOPDGDD (l. ~1405): literal, y es cierto que no cambió en 2023 (idéntico a fecha
  21-12-2022).
- Antecedentes: «retirarlo» (7.3), «Esas acciones» (79.2), «esa vía administrativa» y «el apartado 3 /
  el apartado 2» tienen delante su referente.

## `negritas.py`, una a una

Con los 22 volcados que cita el tema y `fusion-csrtv-boja-219-2015.txt`: **216 negritas, 12 NO ESTÁ y
19 ¿ART.?** (lo mismo con todos los volcados y documentos de `fuentes/canal-sur/`). No se reproducen
las cifras de 37 y 14 del encargo; con sólo RGPD + LOPDGDD salen 81 y 11, y con 14 normas, 23 y 15:
cualquier cifra por encima de 12 es falta de fuentes pasadas.

NO ESTÁ (12), ninguna es un error:
- Rótulos (2): «Enunciado del programa», «Aplicación y entrada en vigor».
- Considerandos del RGPD, que el volcado no trae (8): 1 (TFUE 16.1), 4, 32, 65 y 153 (cuatro citas).
  **Comprobados los ocho, literales y con el número correcto, en la página del BOE del Reglamento.**
- Reglamento (UE) 2025/2518, arts. 1 y 37 (2): fuente no pasada; EUR-Lex no responde desde aquí. Lo leyó
  la verificación (fase 3); queda sin comprobar de nuevo.

¿ART.? (19), ninguna es un error: el tema las atribuye bien y la herramienta se ancla en otro número
de la misma frase. CE: rótulo de la sección 1.ª (art. 18 → 81) y dos del art. 1 LOPDGDD que nombran
el 18.4. LOPDGDD: 23 (nombra el 40 RGPD), 48 (nombra el 23 Ley 40/2015), 50 ×2 (nombra el 15 RGPD),
64.3 (nombra el 83.2), 75 (nombra el 60 RGPD), 77.2 (nombra el 72), RGPD 83.7 (nombra el 58).
LO 7/2021 art. 58 ×5 (nombran los arts. 11, 13, 30). LO 2/1984 art. 4 (nombra el 3; «dias» sin
tilde es así en la fuente). Ley 13/2022: 83.1 (nombra el 95) y 158 (está en el 66 de la Ley 10/2018
y en el tema se atribuye bien).

## `refutar_prosa.py` = 1

LORTAD: falso positivo; la sigla la presenta la propia cita («la Ley Orgánica 5/1992, “conocida como
LORTAD”»), que está literal en el preámbulo de la LOPDGDD.

## Lentes

| Lente | Tramos | Resultado |
|---|---|---|
| `negritas.py` (22 volcados + Acuerdo de fusión) | 216 negritas | 12 NO ESTÁ, 19 ¿ART.?: falsos positivos (arriba) |
| `refutar_prosa.py` | tema entero | 1, falso positivo |
| `refutar_modo.py` (22 volcados) | tema entero | 2, los mismos del remate (otra norma con la misma numeración) |
| `indice.py` | tema entero | 24 997 palabras, 33 epígrafes, sin aviso |
| Pasajes del remate releídos contra la fuente | 10 | 2 correcciones |
