# T03 · Refutación (fase 4, modo ahorro: una lectura, dos lentes)

Tema: `temas/canal-sur-comun/03-union-europea.md` (18.452 palabras según la ficha, verificado).
Leídos antes: `ENCARGO.md`, `CICLO.md` (avisos y dos modos ahorro) y `T03-verificacion.md`.
**Fecha de lectura de todos los preceptos: 24-09-2026**, redacción vigente, extraídos uno a uno
(`grep -n -A40`) de `documentos/` (TUE, protocolos, TFUE, Decisión 2013/272, Decreto 189/2026) y de
los volcados de `fuentes/canal-sur/` (Ley 2/1997). No he corregido el tema. Ficheros tocados: este
informe y `T03-preguntas.md`.

## 1. Exactitud normativa

Cotejado de nuevo, con el foco en lo que la verificación no listó o parafraseó: TUE 7 (los tres
escalones y quién propone), 20.1 a 20.4, 31.1 y 31.2 (los cuatro casos), 42.1 a 42.7, 46.2, 48.7
(los cuatro párrafos), 49 y 50.2 a 50.4; TFUE 5, 24, 238.1 a 238.4 y 354; Protocolo n.º 2, art. 7;
Decisión 2013/272, art. 2; Decreto 189/2026, arts. 2.4, 2.6, 6.1 y 8.2. Composición, mayorías,
mandatos, plazos, recuentos y modo verbal cuadran. Dos salvedades mal acotadas:

| # | Dónde | Qué dice el tema | Qué debería decir | Fuente literal | Gravedad |
| --- | --- | --- | --- | --- | --- |
| 1 | TUE, título VI, *Revisión de los Tratados*, guion «Pasarelas (48.7)», primer subguion | «No cabe para decisiones "que tengan repercusiones militares o en el ámbito de la defensa"», colgado de las dos pasarelas (unanimidad → mayoría cualificada y procedimiento legislativo especial → ordinario) | La exclusión solo alcanza a la primera pasarela (paso del Consejo de la unanimidad a la mayoría cualificada); la segunda no la lleva | TUE 48.7, párrafo primero: «…el Consejo Europeo podrá adoptar una decisión que autorice al Consejo a pronunciarse por mayoría cualificada en dicho ámbito o en dicho caso. **El presente párrafo** no se aplicará a las decisiones que tengan repercusiones militares o en el ámbito de la defensa.» El párrafo segundo (procedimiento legislativo especial → ordinario) no tiene esa salvedad | Cambia la respuesta (error 6): la pregunta 8 no se contesta |
| 2 | *El control de subsidiariedad*, Protocolo n.º 2, artículo 7 | «(un cuarto en el espacio de libertad, seguridad y justicia)» | «un cuarto cuando el proyecto se presente sobre la base del artículo 76 del TFUE, relativo al espacio de libertad, seguridad y justicia»: no se aplica a todo proyecto de ese espacio, solo a los del art. 76 | Protocolo n.º 2, 7.2: «Este umbral se reducirá a un cuarto cuando se trate de un proyecto de acto legislativo presentado sobre la base del artículo 76 del Tratado de Funcionamiento de la Unión Europea, relativo al espacio de libertad, seguridad y justicia.» | Menor (error 6) |

## 2. Cobertura

- Las tres rúbricas del enunciado (la segunda con sus dos normas) tienen su epígrafe, en su orden, y
  cada una da lo que anuncia.
- Quince preguntas en `T03-preguntas.md` (UE 4, TUE 4, Carta 3, Junta 4): **14 enteras, 0 a
  medias, 1 no** (la 8, por el hallazgo 1).

## 3. Prosa

| # | Dónde | Qué pasa | Qué debería ser | Gravedad |
| --- | --- | --- | --- | --- |
| 3 | Rúbrica «Tratado de la Unión Europea»: cierre del título I («Salvo el 6 y el 8, todos se han explicado en el epígrafe anterior»), títulos II y III («…en el epígrafe anterior») y tabla del título VI (filas 49 y 50, «explicada en el epígrafe anterior») | «El epígrafe anterior» quiere decir la rúbrica «La Unión Europea», pero desde el título II el epígrafe inmediatamente anterior es el título precedente del TUE: el antecedente queda mal señalado | «en la rúbrica "La Unión Europea"» (o «en el primer bloque del tema») | Menor |

Sin siglas sin presentar ni referencias a ficheros del proyecto.

## 4. Lentes automáticas

| Lente | Fuentes | Resultado |
| --- | --- | --- |
| `refutar_prosa.py` | tema entero | 0 hallazgos |
| `refutar_modo.py` | EAA, Leyes 2/1997, 8/1994 y 2/2014, CE | 2 hallazgos, los dos falsos positivos ya explicados en la verificación (art. 51 y art. 53: colisión de numeración entre la Carta y el EAA; la lente lo avisa) |

`refutar_exactitud.py`, `refutar_citas.py` y `refutar_documento.py` no se han vuelto a correr: el
tema no ha cambiado desde la verificación, que da su cuadro.
