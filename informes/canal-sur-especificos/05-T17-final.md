# Fase 5 bis · Ayudante de Realización (05) · Tema 17 · revisión de los pasajes del remate

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/17-accesibilidad-subtitulado-audiodescripcion-lenguaje-inclusivo.md`.
Alcance: sólo los pasajes que lista `05-T17-remate.md`. Fuentes releídas el 30-09-2026 (reloj del
sistema; el encargo fija «hoy» en 24-09-2026).

## Comprobación dato a dato

| Pasaje | Dato | Fuente | Resultado |
|---|---|---|---|
| Ep. 2, «Subtítulos en lectura fácil» | LAA 9.4, «programas subtitulados según métodos de lectura fácil» | `BOE-A-2018-15240.md` l. 191 | Literal; antecedente «(epígrafe 1)» correcto (cita en «En la Ley 10/2018») |
| Id. | LGCA no usa «lectura fácil» | `BOE-A-2022-11311.md`, grep: 0 | Correcto |
| Id. | RD 707/2026, de 2 de septiembre; BOE 3-IX-2026; DF 8.ª «entrará en vigor el 2 de enero de 2027» | `grafista/BOE-A-2026-18509.vigente-20270102.md` l. 10, 112, 187-188 | Literal |
| Id. | Reglamento art. 3.i) y su remisión a la UNE 153101; 3.k); 6.1 párr. 2.º (corte en «de 8 de mayo») | Id. l. 230, 240, 242, 292-294 | Literal; el título del reglamento consta (l. 112, 202) |
| Id. | UNE 153101:2018 EX, título, 2018-05-03; dos citas de la *Revista de la Normalización Española* n.º 4 | Temas cerrados 30/11 (l. 690-706) y 15/10 (l. 569-586) | Copia literal (sin volcado local de la revista; declarado) |
| Id. | Oncins, «la Lectura Fácil se está convirtiendo en una modalidad de accesibilidad en los medios»; antecedente «(arriba)» | `montador/web/us-oncins-magazin27.txt` l. 351-352; Oncins presentado en «En diferido y en directo» | Literal; antecedente correcto |
| Id. | CAA, recomendación 3, «En los textos informativos… derecho a la información» | `documentos/caa-guia-discapacidad-2025.pdf`, p. 4: el rótulo «3 ACCESIBILIDAD UNIVERSAL» (y=291) precede al párrafo (y=332) en la misma columna | Literal y bien atribuido a la recomendación 3 |
| Id. | Ni Carta ni Contrato-programa dicen «lectura fácil» | Afirmación del remate (grep) | Aceptado |
| Ep. 4, «El subtítulo, literal» | Burgos, «en la medida de lo posible»; Libro de estilo 9.7.3, «en nuestros contenidos»; remisión a «Lo que se dice en plató, arriba» | `ubu-guia-material-multimedia-accesible.txt` l. 264; `libro-de-estilo-333233b.txt` l. 6157-6160 | Literal; antecedente dos viñetas antes, correcto |
| Aplicación práctica, paso 6 | Mismas dos citas; remisiones «(epígrafe 2)» (tabla de Burgos, l. 740 del tema) y «(epígrafe 4)» | Id. | Literal; antecedentes correctos |
| Siglas, «Qué se puede preguntar», portada, índice, Normativa, «Lo que este tema no da», Trazabilidad | EX; RD 707/2026 (arts. 3.i y k, 6.1, DF 8.ª); UNE 153101:2018 EX; filas nuevas | Coinciden con lo comprobado arriba | Correcto |

## Correcciones aplicadas (comprobadas en la fuente)

1. **«En la norma audiovisual la expresión sólo aparece en la ley andaluza»** → «De las dos leyes
   audiovisuales, sólo la andaluza usa la expresión». Motivo: la Ley 11/2023 (`BOE-A-2023-11022.md`),
   que el tema trata como norma de acceso a la televisión, sí dice «criterios de lectura fácil» (para las
   instrucciones de productos, no para programas). La frase original era demasiado amplia (error 9).
   La frase siguiente se aligeró para no repetir: «La LGCA no la usa en ningún artículo, ni fija cuota
   para esa modalidad.»
2. **CAA**: el pasaje nuevo la llama *Recomendaciones para el tratamiento informativo de la
   discapacidad* (2025) y el epígrafe 4 *Guía para el tratamiento informativo…*; son el mismo documento
   (el PDF se titula en metadatos y p. 4 «Recomendaciones para el tratamiento informativo de la
   discapacidad…» y se llama a sí mismo «GUÍA», p. 2). Se añade «(2025; es la Guía del CAA del
   epígrafe 4)» para que no parezcan dos documentos.

## Lentes

- `indice.py`: 19.800 palabras, 44 epígrafes (la «Extensión» de la portada sigue valiendo).
- `refutar_prosa.py`: 1 hallazgo, el mismo conocido (frase repetida literal del común); negritas rotas: ninguna.

## Otros ficheros tocados

Ninguno salvo el tema y este informe.
