# Puesto 30 · Tema 11 · Fase 5 bis (revisión de lo rematado)

Fecha de trabajo y de todas las lecturas: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).
Alcance: sólo los 12 pasajes que lista `30-T11-remate.md`, § 3. Todos se contrastaron con su fuente.

## Comprobación por pasaje

| # | Pasaje | Fuente releída | Resultado |
| --- | --- | --- | --- |
| 1 | Siglas ETSI, DVB | ETSI EN 300 743, portada | Correcto |
| 2 | «Qué se puede preguntar» | El propio tema | Cubierto por § 2 |
| 3 | «Dos cuentas» | Guía de Burgos (tabla del tema, líneas 456-489) | Cálculo correcto (74/15 ≈ 4,9 s; 37/15 ≈ 2,5 s); cita «unos tres segundos» literal |
| 4 | En diferido y en directo | Oncins, *Magazin* 27, p. 96 (txt, líneas 262-287) | Las tres citas son literales; la atribución a UER/EBU 2019 del rehablado, correcta; la glosa del rehablado sigue la definición de Eugeni que da el artículo. Antecedente «ese mismo artículo»: correcto |
| 5 | Subtítulo cerrado en la TDT | Folleto CESyA (txt y PDF renderizado); ETSI EN 300 743 V1.6.1, cláusula 1 (líneas 414-419) | Citas literales. ETSI: CLUT e ISO/IEC 13818-1, correctos. **Corregido**: el folleto no lleva fecha impresa; «2010» sale sólo de los metadatos del PDF (creación 18-01-2010). Se dice así en el cuerpo y en Trazabilidad |
| 6 | Tabla de salidas, filas lineal e informativos | Contrato-programa, BOJA 245/2023, puntos 12 (líneas 757-764) y 93 (1939-1950) | Literales y completos |
| 7 | Punto 43 y punto 95 | CP, línea 1274 y 1955-1964 | Literales; «podrán» respetado. **Corregido**: la lectura propia final («no se rehace desde cero en casa») no tenía apoyo; queda «la tiene que poner a disposición de Canal Sur la productora» (el punto 95 dice «se obligarán a poner a disposición») |
| 8 | CAA, recomendación 3, segunda cita | `caa-guia-discapacidad-2025.txt`, líneas 153-156 | Literal |
| 9 | Portada: Fuente y Extensión | Tema | Correcto (10.474 palabras según `indice.py`) |
| 10 | Normativa: ETSI EN 300 743 | ETSI | Correcto |
| 11 | «Lo que este tema no da» | — | Correcto |
| 12 | Trazabilidad | Folleto CESyA | **Corregido**: «Madrid, 2010» no consta en el folleto. Ahora: sin fecha impresa; PDF de enero de 2010; logotipos del CESyA, de la Universidad Carlos III de Madrid y del Real Patronato sobre Discapacidad (comprobados en la imagen del PDF) |

## Lentes tras corregir

- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 10.474 palabras, 35 epígrafes.

## Ficheros tocados

- `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/11-accesibilidad-subtitulos-audiodescripcion-lectura-facil-plataformas.md` (3 correcciones: líneas 543, 556, 757 y 953).
- Este informe. Renders del folleto en el scratchpad (fuera del repositorio).

---

# Segunda ronda (revisión del remate de la segunda refutación)

Fecha de trabajo y de las lecturas: 25-09-2026 (encargo fechado 24-09-2026). Alcance: los 6 pasajes
de la segunda ronda de `30-T11-remate.md`.

| # | Pasaje | Fuente releída | Resultado |
| --- | --- | --- | --- |
| 1 | § 3 «Audiosubtítulos o subtítulos hablados» | Oncins, txt l. 319-340; Ley 11/2023, anexo I, IV b) 2.º (`BOE-A-2023-11022.md`, l. 2406) | Las tres citas de Oncins, literales; «subtítulos hablados» en la Ley 11/2023, correcto; antecedentes «citado en el epígrafe 2», «El mismo artículo», «(epígrafe 5)», correctos. **Corregido (error 9)**: «Son los subtítulos leídos en voz alta» no consta en ninguna fuente leída (ni Oncins, ni Ley 11/2023, ni Directiva 2018/1808, cdo. 23): quitado y declarado en «Lo que este tema no da». **Corregido (fecha)**: «los da en 2019» era inexacto; el número es de invierno de 2019, pero el artículo se recibió el 21-12-2020 y se aceptó el 24-03-2021 (txt, l. 14-15; cita webs consultadas en 2021). Sigue siendo anterior a la LGCA vigente |
| 2 | § 4 «Lectura fácil y vídeo», cita de Oncins | Oncins, txt l. 349-352 | Literal; antecedente correcto |
| 3 | «Qué se puede preguntar» | Tema | **Ajustado**: «qué son los audiosubtítulos y a quién sirven» → «a quién sirven los audiosubtítulos», coherente con la corrección 1 |
| 4 | «Lo que este tema no da»: audiosubtítulos en CSRTV | — | Correcto; + definición técnica de los audiosubtítulos no hallada |
| 5 | Trazabilidad: CP puntos 92 y 94; fila de Oncins | CP, l. 1907-1912 y 1952-1955 | Correctos (92: HbbTV y «botón rojo»; 94: «tenderán progresivamente», art. 104.1 LGCA). Fila de Oncins: + fechas de recepción y aceptación |
| 6 | Portada, «Extensión» 10.700 | `indice.py` | 10.736 palabras, 36 epígrafes: se mantiene |

Lentes tras corregir: `refutar_prosa.py` 0 hallazgos.

Ficheros tocados: el tema 11 del puesto 30 (§ 3 audiosubtítulos, «Qué se puede preguntar», «Lo que
este tema no da», Trazabilidad) y este informe.
