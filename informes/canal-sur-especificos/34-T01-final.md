# 34 · T01 · Revisión del remate (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/01-derecho-informacion-libertad-expresion.md`.
Alcance: sólo los pasajes que lista `34-T01-remate.md`.

## Fuentes releídas (todas el 24-09-2026)

- LO 1/1982: `boe.py precepto BOE-A-1982-11196 asegundo` (vigente y a 01-01-1985) y `acuarto`; XML de la API del BOE, bloque `asegundo` (las `<strong>` abarcan de «o, por imperativo del artículo 71…» a «…suplicatorios.»).
- LO 2/1984: `aquinto`, `asexto`.
- Reglamento (UE) 2024/1083: `DOUE-L-2024-80523.md`, arts. 4 y 29; HTML del BOE (considerandos, definición de «Carta»); `DOUE-L-2024-81538.md` y `DOUE-Z-2026-70010.md` (cabecera y bloque «Análisis»).
- STC 27/2020, `BOE-A-2020-4112_STC-27-2020.txt`: sumario, antecedente 2.a y 2.d.
- Libro de estilo, `libro-de-estilo-333233b.txt`, 2.3.2.11 y 2.3.2.13; tema 04 (4.3.6 *off the record*) y tema 14 (Normativa: arts. 2, 6, 8.1, 18 y 29 del Reglamento).

## Confirmado sin cambios

Art. 2.Dos LO 1/1982 (literal, «hubiere», tres redacciones, inciso anulado = todo lo añadido por la LO 3/1985); art. 4.3 y 4.4 LO 1/1982; arts. 5 párr. 3 y 6 LO 2/1984 (literales y cifra de siete días hábiles); art. 4.2 del Reglamento y su aplicación desde 8-2-2025 (art. 29.b); art. 4.3 desde 8-8-2025; lista a)-c), 4.4 a)-d) literal, 4.5 (tres/cinco años, subsidiariedad); 4.8 literal; «sendas fotografías», «abierto y accesible al público», BOE núm. 83; 2.3.2.11 literal entero; remisiones a temas 4 y 14.

## Corregido (comprobado en la fuente)

| Pasaje | Error | Corrección |
|---|---|---|
| Ficha «Redacción» y Trazabilidad (Reglamento) | 9/3: «dos correcciones de errores». `DOUE-Z-2026-70010` no es corrección: su «Análisis» dice «Rango: Otros», ELI C/2026/901, dictada «de conformidad con el art. 18.1»; son las directrices de la Comisión sobre el art. 18. La única corrección (17-10-2024) toca el art. 5.1. | Dicho así en ficha y Trazabilidad. |
| §5 art. 4.4 | 5: «la Carta» sin presentar. | Añadido que es la Carta de los Derechos Fundamentales de la UE (el Reglamento la define así en sus considerandos). |
| §5 art. 4.6 | Glosa imprecisa («programas espía», «autoridad judicial o independiente»). | Medidas de vigilancia de la letra b) e instalación de programas de la c); «autoridad decisoria independiente e imparcial». |
| §5 art. 4.8 | Antecedente: «esas mismas personas» quedaba lejos de su referente. | Nombradas: prestadores, personal editorial y quien pueda disponer de la información. |
| §3 STC 27/2020 | Antecedente: con dos fotos, «la condena por la fotografía» era ambiguo. | «la fotografía del demandante» (antecedente 2.d). |
| Normativa | Título del Reglamento incompleto. | Añadido «y se modifica la Directiva 2010/13/UE». |
| Ficha Extensión | 6.059 | 6.123 (`len(tema.cuerpo().split())`). |

## Lentes

`refutar_prosa.py`: 0.

## Fuera de mi tema (no tocado)

- `fuentes/canal-sur/DOUE-L-2024-80523.md` y `DOUE-Z-2026-70010.md` (generados por `doue.py`) rotulan como «corrección de errores» las directrices C/2026/901: conviene corregir `doue.py`, y revisar el tema 14 si repite el rótulo.
- La cabecera añadida a mano en `BOE-A-2020-4112_STC-27-2020.txt` sigue diciendo núm. 84 (ya avisado en el remate).

Ficheros tocados: el tema 01 y este informe.
