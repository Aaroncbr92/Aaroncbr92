# Puesto 30 · Tema 11 · Verificación

Fase 3 · Verificar. Fecha de trabajo y de todas las lecturas: 25-09-2026 (el encargo fija «hoy» en
24-09-2026). Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/11-accesibilidad-subtitulos-audiodescripcion-lectura-facil-plataformas.md`.

## 1. Pasajes copiados: sólo literalidad

- **Copiado del común** (34/17 § 3, líneas 364-484 y 485-590; § 6, líneas 885-948): `difflib` bloque a
  bloque contra el fichero de 34/17 → 0 diferencias (en el tema, líneas 114-234, 235-340 y 342-405).
  No se re-verifica.
- **Copiado de RTVE sin cambios** (`temas/produccion/11`, líneas 253-260 y 229-245): cada línea, sin
  `**`, está en el tema → literal (sólo se quitó la negrita, como declara la redacción). No se re-verifica.

## 2. Lo verificado en su fuente

| Pasaje | Fuente releída | Resultado |
| --- | --- | --- |
| § 2, § 3, § 5 (ventana LSE), § 5 redes: 62 citas de la guía de Burgos | `fuentes/canal-sur/montador/web/ubu-guia-material-multimedia-accesible.txt`, búsqueda normalizada con la página impresa de cada cita | Todas literales. Páginas correctas (3; 3-4; 4; 4-5; 5; 6; 6-7; 7; 8; 8-9; 9-11). Metadatos del PDF: 30-11-2020 ✓; «Unidad de Atención a la Diversidad» ✓; UNE 139804 «2007» ✓; pensada para vídeos docentes (habla de «profesorado» y «estudiante») ✓. Las comillas internas rectas donde la guía usa “ ” son tipografía, no se tocan |
| § 4 RDLeg 1/2013 art. 2.k) y 29 bis.1-3 | `boe.py precepto BOE-A-2013-12632 a2` y `a2-2` | Literales; 2.k) 2 redacciones, vigente la de BOE-A-2022-5140 (Ley 6/2022, título confirmado en el BOE) desde 02-04-2022; 29 bis, 1 redacción ✓ |
| § 4 LAA art. 9.4 | `boe.py precepto BOE-A-2018-15240 ar-9` | Literal; redacción vigente de 17-02-2024 (Decreto-ley 3/2024) ✓ |
| § 4 «lectura fácil» sólo en la LAA | grep en volcados LGCA, LAA, Ley 18/2007 (BOE-A-2008-1185) | LGCA 0, Ley 18/2007 0, LAA 1 ✓ |
| § 4 fichas AENOR (UNE 153101:2018 EX, 2018-05-03, CTN 153/GT 1, En Vigor; UNE 153102:2018 EX, 2018-12-26, En Vigor) | tienda.aenor.com/p/norma-une-153101-2018-ex-n0060036, descargada hoy | Confirmado |
| § 4 Revista UNE n.º 4 (junio 2018), cinco citas | revista.une.org/4/primera-norma-tecnica-sobre-lectura-facil.html, descargada hoy | Las cinco literales. **Corregido**: firman presidenta **y vicepresidenta** del CTN 153/GT 1, no sólo la presidenta (error 9) |
| § 4 y § 5 CAA, recomendación 3 | `caa-guia-discapacidad-2025.txt` + posición de bloques en el PDF (p. 4: el rótulo «3» encabeza la columna derecha y esos párrafos van debajo) | Dos citas literales y en la recomendación 3 ✓; PDF de 19-11-2025 ✓ |
| § 5 tabla de salidas | LGCA 102.2, 102.3, 104.1.a)-b) (`a1-14`, `a1-16`); Contrato-programa puntos 12, 92, 93, 94; Carta 13.9 | Cifras y citas ✓. **Corregido**: «su accesibilidad "se ampliarán…"» → «sus prestaciones de accesibilidad "se ampliarán…"» (el sujeto del punto 12 es «Las prestaciones de accesibilidad»; concordancia rota) |
| § 5 LGCA 104.1.b), 101.1.g)-h) | `boe.py` `a1-16`, `a1-13` | Literales ✓ |
| § 5 LAA 31.1.i) | `boe.py ar-31` | Literal ✓ |
| § 5 LGCA 105 | `boe.py a1-17` | **Corregido** (error 6, salvedad omitida): «formatos interoperables» → «los formatos interoperables que acuerden los códigos de autorregulación (artículo 108)» |
| § 5 Contrato-programa punto 43 | CP 2024-2026, BOJA 245 de 26-XII-2023 | Literal ✓ |
| § 5 RD 1112/2018 art. 3.3 y 3.4.e), vigencia 20-09-2018 | `boe.py precepto BOE-A-2018-12699 ar-3`; título y fechas en la API del BOE | Literales, 1 redacción ✓ |
| § 5 Ley 11/2023: arts. 2.1.b).4.º y 2.2.b), anexo I secc. IV b) 1.º y 2.º, anexo VII def. 40, DF 18.ª.2, Directiva 2019/882 | `boe.py` `a2`, `ai`, `av-3`, `df-18`, `ti` | Literales ✓. **Corregido** (error 6): la DF 18.ª.2 exceptúa el art. 27.4; añadido «salvo su artículo 27.4» |
| Carta y CP «en BOJA en diciembre de 2023»; «lectura fácil» en ninguno de los dos | cabeceras BOJA 247 (28-XII-2023) y 245 (26-XII-2023); grep | ✓ |
| § 3 oficio: la ley nombra informativos para LSE y no para AD | LGCA 102.2.b)-c) | ✓ |

## 3. Lentes (ENCARGO: el tema cita normas)

Fuentes: LGCA, LAA, Ley 18/2007, Ley 11/2023, RDLeg 1/2013 y RD 1112/2018 (estos dos volcados en el
scratchpad, no en `fuentes/`), Carta, CP, CAA, guía UBU y la revista UNE.

- `negritas.py`: 230 negritas; 32 «no están» y 3 «otro artículo». Todas las del bloque común (saltadas)
  salvo: rótulos del propio tema (como en los demás temas del puesto); «Facilitan el acceso…» (cruza
  el salto de página 3-4, comprobada a mano); fichas AENOR y def. 40 con «[…]» (comprobadas arriba);
  CAA «En los textos…» (ligadura «ﬁ» en el txt). Cero erratas reales.
- `refutar_exactitud.py`: 28 «no literales»; todas en el bloque común (Carta y CP, que la lente
  atribuye a «artículos») salvo la cita del CP punto 12, literal en el CP. Cero hallazgos reales.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos. `indice.py`: sin cambios; 9.510
  palabras.

## 4. Cambios aplicados al tema

1. § 4: «firmado por la presidenta y la vicepresidenta del grupo de trabajo».
2. § 5 tabla, fila de informativos: «sus prestaciones de accesibilidad **«se ampliarán…»**».
3. § 5 «Mantener la accesibilidad»: salvedad de los formatos interoperables acordados en códigos de
   autorregulación (artículo 108; su antecedente, «LGCA, artículo 105», abre la misma viñeta).
4. § 5 Ley 11/2023: «salvo su artículo 27.4».
5. Trazabilidad: fichas AENOR y Revista UNE, leídas directamente hoy (antes «lectura del informe de
   investigación»). Quitada una línea en blanco doble tras la tabla del máster.

Releídos los pasajes cambiados: cada «ese artículo»/«artículo 108» tiene su antecedente delante.
Nada quitado: todo dato fuera de lo copiado se confirmó.

## 5. Ficheros tocados

El tema y este informe. `fuentes/canal-sur/BOE-A-2023-11022.md` aparece modificado en git (sólo la
fecha de volcado, 24 → 25-09-2026): no es de esta fase; no lo
he tocado.
