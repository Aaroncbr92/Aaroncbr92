# Productor/a (puesto 32) · Tema 8 · Verificación

Fase 3. Tema: `temas/canal-sur-especificos/32-productor-a/08-produccion-de-exteriores-retransmisiones-eventos-e-informativos.md`
(11.745 palabras tras la verificación; 61 epígrafes). Fecha de trabajo y de lectura de todas las
fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026). Copia previa en el scratchpad (`v08/32T08-antes-verif.md`).

Ficheros tocados: el tema y este informe. Auxiliares, fuera del repositorio (scratchpad `v08/`):
`lit.py` (cotejo de literalidad), volcados de BOE-A-2003-23514 y BOE-A-2024-11377, texto consolidado
del Reglamento (UE) 2019/947 (EUR-Lex), páginas de la DGT y de la Cámara de Comercio en texto.

## 1. Copiado sin re-verificar: comprobación de literalidad

`lit.py`, línea a línea (sin negritas en lo de RTVE, espacios normalizados): los 17 pasajes de
«Copiado del común» y los 11 de «Copiado de RTVE sin cambios» son literales. Resultado: 28/28 OK.
Tampoco se re-verificaron por dentro (encargo). Sólo se ha retocado el marco de uno (ver 3.12).

## 2. Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| Libro de estilo (txt del PDF, 1.ª ed., marzo 2004): 4.4-4.4.4, 8.3-8.3.4, 8.4 | lectura directa, pp. 75-78 y 116-119 | Todas las citas nuevas o adaptadas, literales y bien atribuidas. `negritas.py` no encuentra 4.4.4 inicial por el salto de página: comprobada a mano |
| RGC (BOE-A-2003-23514): art. 55.1; anexo II arts. 2 (sección 1.ª), 34 y 35 (sección 4.ª, redacción BOE-A-2026-12035, vig. 06-06-2026) | `boe.py precepto` | Literales correctos. Salvedades añadidas (3.3) |
| RD 517/2024 (BOE-A-2024-11377): arts. 8, 40, 53-58, 60 | `boe.py precepto` | Literales correctos; sección 3.ª cap. VI anulada por STS 19-06-2025 (BOE-A-2025-14308), confirmada. Salvedades añadidas (3.5, 3.6) |
| Reglamento (UE) 2019/947, arts. 3, 4, 5, 14 | EUR-Lex, consolidado 02019R0947-20250501 (último de la lista «ALL») | Arts. 3, 5.1, 5.2, 14.1 y 14.5 sin cambios (▼B): el pasaje de RTVE coincide. Aviso 3 de redacción, resuelto |
| RD 393/2007 (volcado local) y RD 524/2023 (BOE-A-2023-14679, d. derogatoria única) | volcado y `boe.py` | Norma 3.1 y anexo I 1.d y 2.g literales. **Norma derogada** (3.4) |
| DGT, «Rodajes audiovisuales» | curl directo, texto íntegro | Frase literal confirmada; competencia: sólo interurbanas y travesías (3.1) |
| ADA, «Documentación de rodajes» | curl falla (conexión reiniciada); lector web | Las dos frases de ayuntamientos y DGT, «Espacios Naturales» y «Menores», confirmadas. Costa y patrimonio: tercera redacción distinta (3.2) |
| ADA, «Ordenanzas y tasas» | no releída (curl falla) | Frases de la investigación, sin cambio; pendiente de abrir en navegador |
| Cámara de Comercio, cuaderno ATA (`/comercio-exterior/cuaderno-de-admision-temporal-de-mercancias-ata`) | curl directo | Tres literales confirmados; «Emitimos el cuaderno ATA» sostiene que lo expiden las Cámaras |
| UIT-R SNG.770-2 | txt local | El párrafo adaptado (considerando c) cuadra |
| X Convenio, art. 39 (BOJA) | txt | Rótulo «Seguro de vida e invalidez» correcto |
| Títulos y fechas de RD 1428/2003, 517/2024, 393/2007, 171/2004, 524/2023, Ley 13/2022, Ley 13/1999 | BOE, XML del sumario | Correctos |

## 3. Correcciones aplicadas (con el error del catálogo)

1. **DGT (9)**: «y las autoridades locales en las vías urbanas» no está en la página: quitado. Se
   citan literales el órgano y la regla de interurbanas y travesías; «sede electrónica» → «en línea».
   Añadido a «Lo que este tema no da». Fila de la tabla de coordinación ajustada.
2. **ADA, costa y patrimonio (9)**: el lector web devolvió hoy «Autorizaciones de uso u ocupación del
   dominio público marítimo terrestre» y «Autorización del uso de espacios en bienes inmuebles del
   ámbito de la cultura y el patrimonio histórico», distintos de los de la redacción y de la
   investigación. Sin literal fiable: pasan a redonda, con aviso en la entrada de la tabla.
3. **RGC anexo II art. 2 (6)**: añadidos los informes del titular de la vía y de las Jefaturas
   (vinculantes si se oponen o condicionan, 2.2) y la resolución en 10 días hábiles con silencio
   **positivo** (2.4, literal), en contraste con el art. 35. «La pide el organizador» → «se tramita a
   solicitud de la organización» (el art. 2 no nombra al solicitante). Supuesto 3 ajustado. Rótulo
   de 34.2.d precisado (es una de las afecciones del 34.2).
4. **RD 393/2007 (7)**: derogado por el RD 524/2023 con efectos de 11-07-2023; la nota del BOE dice
   que la Norma Básica «continuará aplicándose hasta tanto sea aprobado el nuevo instrumento». Buscado
   en el BOE (2023-2026): no aparece. Dicho en el texto, la portada, la normativa, la trazabilidad y
   «Lo que este tema no da». El tema lo daba como «Vigente el 24/09/2026».
5. **RD 517/2024 art. 40.3.b y 40.4 (6)**: añadidos la distancia de 30 m de la clase C2 (< 4 kg,
   reducible a 5 m con baja velocidad) y la exención o reducción que pueden dar el órgano
   competente o el titular (40.4).
6. **RD 517/2024 arts. 8 y 60.1 (9/6)**: «seguro» → «póliza de seguro u otra garantía financiera»;
   nombrado el Reglamento (CE) 785/2004 y la excepción del resto de operaciones < 20 kg; la cita del
   60.1 cortaba la frase: añadido «con las que le correspondan por su Estatuto».
7. **Reglamento (UE) 2019/947 art. 14.5 (6)**: faltaba la letra b (en la «específica», registro con
   cualquier masa); «la única salvo del artículo» (errata) quitado; «una cámara de televisión nunca
   lo está» → salvo juguete conforme con la Directiva 2009/48/CE.
8. **Art. 4.1.c del Reglamento (6)**: la «abierta» no permite volar sobre concentraciones de
   personas. Añadido (literal) y llevado al Supuesto 1, que daba la procesión como posible en
   «abierta»: ahora es «específica», con autorización de AESA.
9. **Portada**: normas citadas completas (arts. 4 del Reglamento; 8 y 60 del RD 517/2024);
   redacción del Reglamento (consolidado a 01-05-2025) y de la Norma Básica; extensión 11.700.
10. **Libro de estilo**: 8.3.4 sigue en p. 119: trazabilidad «pp. 116-119». «Por lo que ocurre fuera
    del plató» (la cita incluye el plató) → «buena parte de ella ocurre fuera del plató».
11. **Qué se puede preguntar**: «cuánto vale un cuaderno ATA» era ambiguo (la página da un precio,
    205 €, que el tema no usa) → «cuánto tiempo es válido».
12. **Convenio, art. 39 (marco)**: «añade:» seguido de «Y compromiso…» no casaba; el marco dice ahora
    que el artículo da una póliza colectiva de vida e invalidez, y sigue la frase copiada, intacta.
13. RD 171/2004 con su título en la tabla de normativa.

## 4. Lentes

- `negritas.py` (RGC, RD 517/2024, RD 393/2007, Ley 13/2022, Libro NFKC, UIT-R, DGT, ATA, Reglamento
  consolidado, Carta, Convenio, Ley 18/2007): 88 negritas; 16 «no están», todas explicadas: rótulos
  (4), webs de la ADA confirmadas con lector (6), Libro con salto de página o con ligadura «ﬁ» en
  texto copiado del común (3), supuestos (3). Una «mal atribuida» (34.4 junto al 35) es falso positivo.
- `refutar_modo.py` (RGC, RD 517/2024, RD 393/2007): 0 hallazgos.
- `refutar_prosa.py`: 1 (la Carta 16.3 en portada y trazabilidad: aceptable).
- `indice.py`: 11.745 palabras, 61 epígrafes; índice sin cambios de rúbricas.

## 5. Pendiente para el coordinador

- La página de la ADA no se deja descargar desde aquí; las frases de «Ordenanzas y tasas» no se han
  podido releer. Conviene abrirla en navegador.
- La tabla de 16.1-16.3 de la Carta y la dieta de rodaje son del común: no tocadas.
- Cero cambios en las 28 piezas copiadas.
