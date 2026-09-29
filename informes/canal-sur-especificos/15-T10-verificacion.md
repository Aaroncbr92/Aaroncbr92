# Grafista (15) · Tema 10 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/10-accesibilidad-contraste-legibilidad-tamano-lectura-facil-subtitulos-pictogramas-diseno-inclusivo.md`
(16.161 palabras de cuerpo, 51 epígrafes tras la verificación). Fecha de trabajo del encargo: 24-09-2026;
fuentes releídas el 29-09-2026 (fecha del sistema). Copia previa: scratchpad `15t10v/antes-verif.md`.

Ficheros tocados: el tema y este informe. Nota: al comprobar su uso, `indice.py` se lanzó una vez sin
argumentos y reescribió `temas/general/01` a `04` antes de cortarse; `git status` confirma que su
contenido no cambió (sólo la fecha de modificación). Después se pasó sólo sobre el tema.

## 1. Pasajes copiados: sólo se comprobó que son literales (no se re-verifican)

Cotejo con script (espacios normalizados; en RTVE, quitadas `**` y ✔), bloque a bloque y frase a frase:

- **Copiado del común** (Montador/a 11 y Realizador/a 16), los 15 pasajes listados: **literales**. Los
  cortes y las frases de entrada que el redactor declaró como nuevos son los únicos fragmentos que no
  casan: «Ese desarrollo ya existe…» (29 bis), «Es la razón de que las versiones para redes…» (Burgos),
  «Ninguna norma leída obliga…», «Y una recomendación técnica de la guía (6.2)…», «Las notas y los
  anexos que sirven al grafismo:», «Lo que consta de Canal Sur, según la misma guía:». Se verificaron
  como texto nuevo.
- **Copiado de RTVE sin cambios** (`diseno-grafico/05` y `08`): Frutiger (las dos frases), filas
  Tracking, Interlineado, Cuerpo y Ancho, la tabla «Requisito / Qué exige» y la frase del faldón gris:
  **literales**.

## 2. Lo verificado en su fuente (29-09-2026)

| Fuente | Resultado |
|---|---|
| RD 1112/2018 (`boe.py`, BOE-A-2018-12699, arts. 2, 3, 5 y 6; 1 redacción, vigente desde 20-09-2018) | 2.1.d), 3.4.e), 5.1, 5.2, 6.1, 6.3 y 6.4: literales. Título y fecha, correctos |
| Ley 39/2015, art. 2.2 a) y b) (1 redacción) | Literales (la b) se cita cortada antes de «, que quedarán sujetas…»; no afecta a lo que se afirma) |
| Contrato-programa, punto 92 (BOJA 245, 26-XII-2023) | Invoca el RD 1112/2018 para webs y aplicaciones: correcto. Carta BOJA 247, 28-XII-2023: correcto |
| Decisión 2021/1339 (`doue.py`, DOUE-L-2021-81136) | 11-08-2021; inserta la V3.2.1 (2021-03); suprime la fila 1 con efecto desde el 12-02-2022. Que esa fila era la V2.1.2 lo confirma la página de la Comisión «Web Accessibility Directive — standards and harmonisation» |
| Ficha AENOR UNE-EN 301549:2022 (WebFetch, URL …-n0068037) | En vigor; edición 2022-01-05; «Idéntica EN 301549:2021»: correcto |
| AccessibleEU, noticia de 07-09-2026 (WebFetch) | WCAG 2.2 en lugar de 2.1 para webs, programas y documentos; «the current reference remains EN 301 549 v3.2.1 (2021)», basada en WCAG 2.1 AA: literal. Título del PDF de ETSI «EN 301 549 V4.1.1 (2026-09)» (resultado de búsqueda): confirmado |
| WCAG 2.2, `wcag22.txt` (W3C Recommendation 12 December 2024) | Todas las citas, literales; niveles de los 14 criterios, correctos; fórmula con 0,04045. Tabla de contrastes recalculada: 19,56; 4,54; 4,48; 4,00; 2,44; 1,61, correcta. Cuentas del final (4,57; 0,183; 0,30; espaciado 30/40/2,4/3,2), correctas |
| UIT-R BT.709-6, 3.1 y 3.2 | Coeficientes y señales con precorrección: correcto |
| LGCA 101.1.d) y estructura (cap. II del título VI = arts. 101-109) | Correcto |
| RDLeg 1/2013 art. 2 k), l), m) (2 redacciones, vigente la de la Ley 6/2022) | Literales |
| LAA art. 9.2 y 9.4 (3 redacciones; vigente la de 17-02-2024, Decreto-ley 3/2024, de 6 de febrero) | Literales |
| RD 707/2026, volcado vigente a 02-01-2027 | Arts. 1, 3 b) i) j) k) l), 4.2.a), 5.1.a) y 5.2, 6.1 y 6.3, 7.2 e) y g), DA 2.ª, DF 8.ª; «Dado el 2 de septiembre de 2026», publicado 03-09-2026: literales salvo lo corregido abajo |
| Libro de estilo (1.ª ed., marzo de 2004), 3.7.1, 3.16, 6.5.2 y «Siglas y acrónimos. Recomendaciones básicas» | Literales (el texto lleva ligaduras «ﬁ»/«ﬂ»); una salvedad añadida abajo |
| Autismo España (29-06-2026), Revista UNE n.º 68 (abril de 2024), Plena Inclusión | Citas, números de norma y años, correctos |
| ARASAAC: Aula Abierta y paquete JS de arasaac.org (vuelto a descargar) | Las cuatro cadenas de licencia, literales |
| Guía del CNLSE: fondo homogéneo y sin brillo, azul oscuro para sordociegos, 1/6 (CENELEC y Ofcom) | Correcto (texto propio de la lista «Lo que todo eso significa…») |

## 3. Correcciones aplicadas (cada una comprobada antes en la fuente)

1. **Error 9 · §5 «El Reglamento…».** «Desarrolla el artículo 29 bis del RDLeg 1/2013»: el RD 707/2026 no
   cita el 29 bis. Pasa a: lo aprueba en cumplimiento de la DA 2.ª de la Ley 6/2022 y su objeto es
   **«desarrollar las condiciones básicas de accesibilidad cognitiva, su exigencia y aplicación»**
   (art. 1), las del 29 bis, «aunque el real decreto no cita ese artículo».
2. **Error 4/6 · §5, art. 3.j).** «Su norma de referencia: UNE-ISO 24495-1»: la fuente dice «se recomienda
   seguir las pautas… de la norma UNE-ISO 24495-1». Pasa a «Y, como en la i), recomienda seguir las
   pautas de…».
3. **Error 6 · §5 «Lectura fácil y grafismo».** El Libro de estilo manda desglosar la sigla «cuando sea
   imprescindible»; añadida la salvedad.
4. **Error 9 · §7, DA 2.ª.** El Real Patronato no propone el catálogo por sí mismo: «creará un grupo de
   trabajo técnico y especializado con el objetivo de proponer…». Corregido.
5. **Error 6/4 · §8 «La imagen de las personas».** «El reglamento pide, para los pictogramas de
   señalización, un tratamiento igualitario del género»: es un criterio del art. 7.2.e) entre los que
   las Administraciones «podrán» aplicar en su planificación urbanística, y habla de «pictogramas y
   señalizaciones». Reescrito con la salvedad y el artículo (el §7 ya lo decía bien).
6. **Error 9 · §8 «Movimiento y destellos».** Llamar a la epilepsia fotosensible «el caso más grave» del
   control de estímulos sensoriales es lectura propia: se declara como tal.
7. **Negrita = literal.** Rótulos propios en negrita pasados a cursiva: *Quién.*, *Qué exige.*, *Cómo se
   presume que se cumple.*, *Qué deja fuera.*, *La televisión queda fuera por remisión.*, *El subtítulo
   que sí hace el grafista.*, *Desde el origen.*, *Sin adaptación.*; «no está en vigor», a redonda.
8. **Trazabilidad y Normativa.** RD 1112/2018: añadido el art. 3. RD 707/2026: añadidos el artículo único
   y el art. 1 del reglamento.

Pasajes cambiados releídos: cada «lo aprueba», «ese artículo», «como en la i)» tiene su antecedente.

## 4. Lentes

- `negritas.py` (corpus de fuentes + BOE): los «no está» y «otro artículo» restantes son pasajes copiados
  (fuentes en PDF con guiones, no incluidas) o artefactos de concatenar fuentes; ninguno en texto nuevo.
- `refutar_prosa.py`: un aviso, «AENOR» sin desarrollar: se presenta como el catálogo de las normas; es
  una marca, no una sigla que haya que desarrollar (el tema cerrado de Montador hace lo mismo). Se deja.
- `indice.py` sobre el tema: 51 epígrafes, índice sin cambios.

## 5. Queda para refutar

- Extensión (16.000 palabras) alta para siete rúbricas; el recorte posible lo señala el redactor
  (6.1 del CNLSE y tabla de cuotas).
- «AENOR» en las siglas: decidir si se desarrolla.
