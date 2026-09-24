# 34 · T02 · Verificación (fase 3)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/02-mision-informativa-radiotelevision-publica-autonomica.md` (8.420 palabras tras la verificación, 31 epígrafes).

Alcance: lo que no está bajo «Copiado del común» en `34-T02-redaccion.md` (detectado cotejando línea a línea el tema con `temas/canal-sur-comun/*.md`) y lo copiado de RTVE (art. 2.10 LGCA). El texto copiado del común no se ha releído.

## Fuentes leídas (todas el 24-09-2026)

- Ley 13/2022 (`BOE-A-2022-11311`, volcado): arts. 2.1-2.4, 2.10, 9, 50-54, 56 y disposición derogatoria. Sin modificaciones en todo el texto (`redacciones.tsv`).
- Ley 18/2007 (`BOE-A-2008-1185`): arts. 2, 4 y exposición de motivos (redacción de 2019).
- Ley 10/2018 (`BOE-A-2018-15240`): arts. 2, 3 (redacción DL 3/2024), 44, 45 y rúbricas del título V, cap. I.
- Ley 7/2010 (`BOE-A-2010-5292`, `boe.py precepto … dd`): disposición derogatoria.
- Carta 2024-2029 (BOJA 247/2023, texto volcado): EM, arts. 4, 8.1, 13.4, 15.1, 24.2.a.
- Libro de Estilo (RTVA, 1.ª ed., marzo 2004): créditos, Introducción, 1.1, 1.2, 1.5, 2.5.4.

## Correcciones aplicadas

| # | Error | Pasaje | Qué decía | Qué dice ahora |
|---|---|---|---|---|
| 1 | 8 artículo mal | Responsabilidad editorial; Normativa; Trazabilidad | «Ley 10/2018, artículo 3.1.k)» (operador de televisión) | 3.2.k): la definición está en el apartado 2 del art. 3 (definiciones del cine y el fomento); el 3.1.k es «servicio privado de carácter comercial». El informe de redacción también se equivocaba |
| 2 | 9 sin fuente | Idem | «Esa ley está derogada» | Derogada por la Ley 7/2010, disposición derogatoria, 6 (leída); añadida a Normativa y Trazabilidad |
| 3 | 3 recuento / contradicción interna | «Cómo está hecho»; Responsabilidad editorial | Sólo la responsabilidad editorial tiene definición legal | También el servicio público (LGCA 50, LAA 44.1, L 18/2007 4.2, la tabla del propio tema) |
| 4 | 9 | Ley 10/2018, entrada | «dedica al servicio público los artículos 2.2 y 44 a 51» | El capítulo I del título V («El servicio público audiovisual en Andalucía») llega al 54 (52-54: local, universidades); se dice qué artículos interesan |
| 5 | 4 podrá/deberá | Ley 13/2022, entrada | «deja a las Comunidades Autónomas su prestación» | «permite … acordar su prestación (53.2)» (el 53.2 dice «podrán acordar») |
| 6 | cita imprecisa | Diversidad social | «siete principios del artículo 52» | «siete valores esenciales» (literal del 52) |
| 7 | cita imprecisa | Diversidad social | «45, fines 3.º y 4.º» | «45.3 y 45.4» (la ley numera «3.», «4.») |
| 8 | 7 redacción | Portada | Sin mención de la EM de la Ley 18/2007 | La EM (citada en Neutralidad) está en la redacción de la Ley 2/2019 |
| 9 | forma | Lo que este tema no da | Rótulos propios en negrita | En redonda (negrita = literal) |

## Confirmado sin cambios

- Art. 2.10 LGCA (de RTVE, con la letra d añadida): cuatro supuestos, literales correctos. Art. 2.1-2.4: literales; el fallo de RTVE en 2.2 («tanto… como») sigue corregido.
- «Neutralidad» sale una sola vez en el articulado de la Ley 18/2007 (4.1.g); la otra, en la EM (cita literal correcta).
- LGCA 9.1, 50, 51.b y d, 52 (siete valores), 54.3.a.3.º (mandato-marco estatal), 56.2.
- LAA 2.1: quince letras (a-ñ); 2.1.h literal; 44.1 literal (tabla).
- Ley 18/2007 4.1.b, 4.2, 4.3.c, f y h: literales.
- Carta: art. 4 «Principio de neutralidad tecnológica»; 13.4, nueve principios con neutralidad; neutralidad en la EM; 8.1.m y r; 15.1; 24.2.a (producción financiada); no aparece «independencia editorial».
- Libro de Estilo: Introducción, 1.1, 1.2, 1.5 y 2.5.4, literales; edición y fecha.

## Lentes

- `refutar_prosa.py`: 0. `indice.py`: regenerado (31 epígrafes).
- `negritas.py` (3 leyes, EAA, Carta, Libro): los «NO ESTÁ» que quedan son rúbricas y títulos del texto copiado del común, «Qué se puede preguntar» / «Cómo está hecho» y el 1.5 del Libro partido por salto de página (comprobado a mano).
- `refutar_exactitud.py`: las no literales son falsos anclajes (cita de Carta/Libro, que no son fuentes de la herramienta; rúbrica de capítulo; tabla con varias leyes) o texto del común.
- `refutar_modo.py`: 1 hallazgo, falso: la salvedad es del art. 9 de la Ley 10/2018, no del 9 de la Ley 13/2022 que cita el tema.

## Pendiente para refutar

- La afirmación de portada «la Carta no ha sido modificada» procede del común (no se ha buscado una modificación posterior).

Ficheros tocados: el tema y este informe.
