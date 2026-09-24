# T03 · Remate (fase 5, modo ahorro)

Tema: `temas/canal-sur-comun/03-union-europea.md`. Leídos: `ENCARGO.md`, `CICLO.md` (avisos y los
dos modos ahorro), `T03-refutacion.md`, `T03-preguntas.md`. Los tres hallazgos, comprobados antes
de aplicarlos, extrayendo el artículo con `grep -n -A40` (nunca el volcado entero):
`fuentes/canal-sur/documentos/tue-version-consolidada-doue-c202-2016.txt` (art. 48) y
`fuentes/canal-sur/documentos/tue-tfue-protocolos-doue-c202-2016.txt` (Protocolo n.º 2, art. 7).
Los tres eran correctos; se aplicaron los tres.

## Pasajes cambiados

| # | Dónde | Antes | Después | Comprobación |
| --- | --- | --- | --- | --- |
| 1 | Título VI, *Revisión de los Tratados*, guion «Pasarelas (48.7)» | «No cabe para decisiones "que tengan repercusiones militares o en el ámbito de la defensa"», colgado de las dos pasarelas | Se aclara que la exclusión solo alcanza a la primera pasarela (unanimidad → mayoría cualificada); el segundo párrafo (procedimiento legislativo especial → ordinario) no la lleva | TUE art. 48.7, párrafo primero: «...el Consejo Europeo podrá adoptar una decisión que autorice al Consejo a pronunciarse por mayoría cualificada en dicho ámbito o en dicho caso. El presente párrafo no se aplicará a las decisiones que tengan repercusiones militares o en el ámbito de la defensa.» El párrafo segundo no tiene esa frase |
| 2 | *El control de subsidiariedad*, Protocolo n.º 2, artículo 7 | «(un cuarto en el espacio de libertad, seguridad y justicia)» | «un cuarto cuando el proyecto se presente sobre la base del artículo 76 del TFUE, relativo al espacio de libertad, seguridad y justicia» | Protocolo n.º 2, art. 7.2: «Este umbral se reducirá a un cuarto cuando se trate de un proyecto de acto legislativo presentado sobre la base del artículo 76 del Tratado de Funcionamiento de la Unión Europea, relativo al espacio de libertad, seguridad y justicia.» |
| 3 | Rúbrica «Tratado de la Unión Europea»: cierre del título I, títulos II y III, y tabla del título VI (filas 49 y 50) | «...en el epígrafe anterior» | «...en la rúbrica "La Unión Europea"» (cinco apariciones) | Corrección de antecedente: desde el título II el epígrafe inmediatamente anterior ya no es «La Unión Europea», sino el título precedente del TUE |

Ningún otro pasaje se tocó. Releídos los párrafos que rodean cada cambio: los antecedentes de «esta
exclusión», «el segundo párrafo» y «la rúbrica…» quedan claros.

## Pregunta 8

`T03-preguntas.md`, pregunta 8 (exclusión militar/defensa del art. 48.7): con el pasaje corregido,
el cuerpo del tema ya distingue las dos pasarelas y contesta **a) Solo a la autorización para que el
Consejo pase de la unanimidad a la mayoría cualificada** — entera.

## Lentes automáticas

| Lente | Fuentes | Resultado |
| --- | --- | --- |
| `indice.py` | tema | 18.508 palabras, 34 epígrafes (ficha actualizada de 18.452 a 18.508; sin fila de portada en `portadas.tsv`, aviso normal) |
| `refutar_prosa.py` | tema entero | 0 hallazgos |
| `negritas.py` | TUE, TFUE, Carta, protocolos, tres decisiones UE, EAA, Leyes 2/1997, 8/1994 y 2/2014, RD 2105/1996, Acuerdos 2004 y sus modificaciones de 2011, decretos 9/2026, 189/2026 (y su corrección), 164/1995 y 230/1995 | 389 negritas cotejadas; 15 «NO ESTÁ» y 11 «¿ART. N?», ninguna sobre los tres pasajes tocados. Las «NO ESTÁ» corresponden a citas de páginas institucionales (ue.europa.eu), del instrumento de ratificación de 1985/86, del art. 93 CE y de normas sobre la Conferencia/Acuerdo de la Mesa no incluidas en este cotejo por no ser objeto de este remate; no se investigan aquí, por quedar fuera del alcance de los tres hallazgos encargados |

## Ficheros tocados

`temas/canal-sur-comun/03-union-europea.md` (los tres pasajes y la extensión de la ficha) y este
informe.
