# Puesto 30 · Tema 11 · Remate

Fase 5 · Rematar. Fecha de trabajo y de todas las lecturas: 25-09-2026 (el encargo fija «hoy» en
24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/11-accesibilidad-subtitulos-audiodescripcion-lectura-facil-plataformas.md`.
Entrada: `30-T11-refutacion.md` (5 hallazgos menores, 2 lagunas, 1 opcional) y `30-T11-preguntas.md`
(12 enteras, 1 a medias, 2 no).

**Se amplió contenido nuevo** (dos subepígrafes en § 2 y el punto 95 del Contrato-programa): procede
la fase 5 bis sobre los pasajes 3, 5 y 6 de la lista.

## 1. Hallazgos: comprobación en la fuente y decisión

| # | Hallazgo | Fuente releída (25-09-2026) | Decisión |
| --- | --- | --- | --- |
| 1 | Fila de emisión lineal omite LSE del punto 93 | CP, `contrato-programa-2024-2026-boja-245-2023.txt`, líneas 1939-1950 | Aplicado. El informe acortaba la cita: el punto 93 sigue con **«y de aquellos otros programas cuya posesión de derechos de explotación lo permita»**; se añade entera. También se suma la audiodescripción «conforme a la Ley 18/2007» |
| 2 | Fila de informativos omite LSE del punto 12 | CP, líneas 757-764 | Aplicado, literal |
| 3 | «Dos cuentas» no concilia 2,5 s con «unos tres segundos» | Guía de Burgos, ya en la tabla del tema | Aplicado: frase que distingue mínimo de lectura y permanencia de la guía |
| 4 | Falta el punto 95 del CP | CP, líneas 1955-1964 | Aplicado. El punto 95 dice además **«se podrán establecer estipulaciones en contratos»** conforme al Código de Autorregulación del art. 105 LGCA; se recoge con su «podrán» |
| 5 | Portada «Fuente» incompleta | Tema, «Normativa que el tema invoca» | Aplicado: UNE 153102:2018 EX y UNE 139804, más las fuentes nuevas |
| Opc. | CAA, recomendación 3, «un esfuerzo para ganar en accesibilidad…» | `caa-guia-discapacidad-2025.txt`, líneas 153-156 | Aplicado, frase entera |

## 2. Lagunas: ampliación con fuente

**Pregunta 14 (subtitulado en directo).** Fuente: Oncins, E., «Evolución de la accesibilidad en los
medios y formación de nuevos perfiles profesionales», *Magazin* 27 (2019), pp. 91-102, Universidad de
Sevilla (descargado a `fuentes/canal-sur/montador/web/us-oncins-magazin27.pdf/.txt`, p. 96, líneas
268-290). Confirma: rehablado como técnica más usada por las televisiones (citando EBU 2019), definición
de Eugeni, y «estenotipia, la velotipia u otros sistemas de teclado rápido». La pregunta 14 pasa a
**entera**. No confirmado y declarado: retardo del directo y valores de la UNE 153010 para el directo
(el PDF del CESyA *Diferentes técnicas de producción de subtítulos en la TDT* da 404).

**Pregunta 15 (subtítulo cerrado en la TDT).** Fuentes: CESyA, *Los subtítulos en la TDT* (folleto,
2010; `web/cesya-subtitulos-tdt-folleto-2010.pdf/.txt`), que da los dos tipos, teletexto y DVB; y
ETSI EN 300 743 V1.6.1 (2018-10), cláusula 1 «Scope» (`fuentes/canal-sur/montador/etsi/en300743v010601.pdf/.txt`,
líneas 414-419). La pregunta 15 pasa a **entera**. Declarado: qué tipo emite hoy Canal Sur (el dato
del folleto es de 2010). Se quitó, por no constar en la fuente, «el heredado de la televisión
analógica» y «junto al vídeo y al audio».

Resultado de las preguntas tras el remate: **15 enteras**.

## 3. Pasajes cambiados

1. Siglas de entrada: + ETSI y DVB.
2. «Qué se puede preguntar»: + técnica del directo y teletexto/DVB.
3. § 2 «Los criterios de la UNE 153010…», párrafo «Dos cuentas»: frase final nueva (hallazgo 3).
4. § 2, nuevo `### En diferido y en directo` (laguna 1).
5. § 2, nuevo `### Cómo llega el subtítulo cerrado al televisor en la TDT` (laguna 2).
6. § 5 «Qué norma rige cada salida», filas de emisión lineal e informativos (hallazgos 1 y 2).
7. § 5 «Mantener la accesibilidad…», párrafo «Y dos de contratación» con el punto 95 (hallazgo 4).
8. § 5 «Redes sociales…»: segunda cita de la recomendación 3 del CAA (opcional).
9. Portada: «Fuente» (hallazgo 5) y «Extensión» (9.500 → 10.400 palabras).
10. «Normativa que el tema invoca»: + ETSI EN 300 743.
11. «Lo que este tema no da»: + teletexto/DVB en Canal Sur; + retardo y UNE para el directo.
12. «Trazabilidad»: + CP puntos 12, 93 y 95; Oncins; folleto CESyA; ETSI EN 300 743.

Relectura de antecedentes: «ese mismo artículo» (Oncins, nombrado en el párrafo anterior), «el
folleto» (nombrado en el mismo subepígrafe), «el punto 95» (tras el 43, mismo párrafo): correctos.

## 4. Lentes

- `indice.py`: 10.432 palabras, 35 epígrafes; índice regenerado con los dos subepígrafes nuevos.
- `negritas.py` (CP, CAA, Oncins, folleto, ETSI, Burgos, LGCA, LAA, Ley 11/2023): todas las negritas
  nuevas están en su fuente. Los 49 «no está» y 3 «otro artículo» son del § 1 copiado del común, de
  fuentes en línea (AENOR, revista UNE) o de fuentes no pasadas (RDLeg, RD 1112/2018); no afectan a lo
  cambiado.
- `refutar_exactitud.py` (LGCA, LAA, Ley 11/2023): los «no literales» son citas del CP, la Carta y el
  RD 1112/2018 atribuidas por la lente a artículos de esas leyes; falsos positivos.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 1 (ETSI sin presentar) → corregido; ahora 0.

## 5. Ficheros tocados

- El tema 11 del puesto 30.
- Este informe.
- Fuentes nuevas descargadas: `fuentes/canal-sur/montador/web/us-oncins-magazin27.{pdf,txt}`,
  `fuentes/canal-sur/montador/web/cesya-subtitulos-tdt-folleto-2010.{pdf,txt}`,
  `fuentes/canal-sur/montador/etsi/en300743v010601.{pdf,txt}`.
