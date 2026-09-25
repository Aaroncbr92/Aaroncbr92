# Puesto 30 · Tema 11 · Redacción

Fase 2 · Redactar. Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026; las lecturas de
esta fase se hicieron el 25-09-2026 y así se declaran). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/11-accesibilidad-subtitulos-audiodescripcion-lectura-facil-plataformas.md`.

Material: `30-investigacion-C-derechos-plataformas.md` (§ Tema 11); tema cerrado 34/17; RTVE
`produccion/11` y `general/07`.

## Avance

- [x] Portada, siglas, enunciado, qué se puede preguntar
- [x] Epígrafe 1 (herramientas RTVE + 34/17 §3 y §6)
- [x] Epígrafe 2 Subtítulos (propio, UBU)
- [x] Epígrafe 3 Audiodescripción (propio, UBU)
- [x] Epígrafe 4 Lectura fácil (propio: RDLeg 1/2013, LAA 9.4, ficha AENOR y Revista UNE vía informe C)
- [x] Epígrafe 5 Versiones para plataformas (propio + RTVE produccion/11 § 8)
- [x] Aplicación práctica, Normativa, No da, Trazabilidad
- [x] Índice (`indice.py`), extensión (9.492 palabras de cuerpo), `refutar_prosa.py`: 0 hallazgos
  (la sigla «EX» se presentó tras el primer pase)

## Copiado del común

Todo de `temas/canal-sur-especificos/34-redactor-a/17-accesibilidad-igualdad-diversidad.md`, literal
(misma letra y misma negrita), en el epígrafe 1 del tema. Verificación y refutación lo saltan.

| Pasaje en el tema 30/11 | Origen en 34/17 (líneas del fichero a 25-09-2026) |
| --- | --- |
| § 1 «En la Ley 13/2022», con «Artículo 101», «Artículos 102 a 104», «Artículos 105 a 109» (incluidos actualización de cifras, radio y sonoro a petición, infracciones) | § 3, líneas 364-484 |
| § 1 «En la Ley 10/2018»: principios, art. 6, «Artículo 9» (con la tabla de redacciones), «Disposición transitoria primera» completa, «Las obligaciones del artículo 31.1» | § 3, líneas 485-590 (se omite «Publicidad, fomento y control») |
| § 1 «La Ley 18/2007», «Los informativos», «La programación en general» y la tabla de fichas AENOR de UNE 153010:2012 y 153020:2005 | § 6, líneas 885-948 (se omiten la entradilla de § 6, que remite a su epígrafe 3, y la frase final «Su contenido técnico no se ha leído y este tema no lo da», que aquí ya no es cierta) |

## Copiado de RTVE sin cambios

De `temas/produccion/11-tratamiento-de-imagen-y-sonido.md` (tema técnico sin norma, oficio). Misma
letra; **sólo se ha quitado la negrita**, que en RTVE es énfasis y en Canal Sur marcaría literal de
fuente. El verificador sólo comprueba que es literal.

| Pasaje en el tema 30/11 | Origen |
| --- | --- |
| § 1 «Las herramientas»: frase «La accesibilidad de los contenidos es hoy una parte…» y tabla Herramienta / Para quién / Cómo se produce | produccion/11 § 9, líneas 253-260 |
| § 5 «El máster para cada destino»: frase «El máster es el resultado final…», tabla de especificaciones y párrafo «Y la regla que ordena todo…» | produccion/11 § 8, líneas 229-245 |

Quitado por propio de RTVE o por no sostenerse: la pregunta 63 y la «innovación de RTVE en 2021»
(sin fuente institucional); la frase «el reconocimiento automático de voz es la única técnica que
produce subtítulos al ritmo de quien habla» (afirmación sin fuente); el enlace del máster con la
conservación del art. 156.2 LGCA (tema 16 de RTVE, fuera del enunciado).

`temas/general/07-ley-13-2022.md` (cap. II del título VI): **no se copia nada**; lo absorbe 34/17,
más completo y en redacción vigente (el tema RTVE estudia la redacción de 21/12/2022).

## Redactado nuevo (sí pasa por verificación)

- § 2 Subtítulos, § 3 Audiodescripción y § 5 «La ventana de lengua de signos»: citas de la guía de la
  Universidad de Burgos, releídas en `fuentes/canal-sur/montador/web/ubu-guia-material-multimedia-accesible.txt`
  el 25-09-2026. **Páginas**: se usan las impresas en la guía (el número va en la cabecera de cada
  página): definición p. 3; abiertos/cerrados p. 4; requisitos visuales pp. 4-5; colores p. 5;
  temporales y sonoros p. 6; identificación pp. 6-7; audiodescripción pp. 7-9; UNE 139804 pp. 9-11.
  *Aviso para el tema 7*: allí se cita abiertos/cerrados en «pp. 4-5» y los requisitos en «pp. 5-6»;
  según esta paginación son p. 4 y pp. 4-6. No lo he tocado (fuera de mi tema).
- Nuevo respecto del informe C: la UNE 139804 (lengua de signos en redes informáticas) por la guía de
  Burgos; la LAA art. 31.1.i) literal; la LGCA art. 104.1.b) («debida prominencia»); el Contrato-programa
  punto 43 (contenidos contratados accesibles); el Consejo Audiovisual de Andalucía, *Recomendaciones
  para el tratamiento informativo de la discapacidad* (2025), recomendación 3 (texto alternativo en
  redes; lenguaje claro), en `fuentes/canal-sur/documentos/caa-guia-discapacidad-2025.txt`. Comprobado
  que la Carta 2024-2029 y el Contrato-programa no contienen «lectura fácil» (grep, 0 resultados).
- § 4 Lectura fácil: RDLeg 1/2013 arts. 2.k) y 29 bis releídos con `boe.py` (25-09-2026); LAA 9.4
  literal releído en el volcado. **Ficha AENOR de UNE 153101/153102 y citas de la Revista UNE n.º 4:
  tomadas del informe C sin releer** (no hay copia local): el verificador debe cotejarlas.
- § 5: RD 1112/2018 art. 3 releído con `boe.py`; Ley 11/2023 art. 2, anexo I secc. IV b), anexo VII
  def. 40 y DF 18.ª releídos en el volcado.
- Oficio declarado: uso de abierto/cerrado por destino, zona del subtítulo y rótulos, partir en el
  corte, pista propia de AD, revisión tras remontar, tabla de accesibilidad por destino, supuesto.

## Ficheros tocados

Sólo el tema y este informe. Ninguno más (no se añadió fila a `herramientas/portadas.tsv`: los temas
del puesto 30 no la tienen).

## Diez preguntas tipo test, contestadas con el tema

| # | Pregunta (respuesta) | Rúbrica | Dónde la contesta | ¿Entera? |
| --- | --- | --- | --- | --- |
| 1 | Porcentaje mínimo de programas subtitulados del servicio público televisivo lineal en abierto (LGCA 102.2): a) 80 %; b) **90 %**; c) 100 %; d) 75 % | Accesibilidad / subtítulos | § 1, tabla de cuotas | Sí |
| 2 | En el servicio a petición, subtitulado mínimo y régimen de audiodescripción y signos: **30 %; incorporación gradual con la debida prominencia en el catálogo** | Versiones para plataformas | § 1 tabla; § 5 (104.1.b) | Sí |
| 3 | Diferencia entre subtítulo abierto y cerrado: **el abierto va incrustado y el usuario no lo controla; el cerrado se activa a voluntad** | Subtítulos | § 2 «Abiertos y cerrados» | Sí |
| 4 | Según la síntesis de la UNE 153010, máximo de caracteres por línea: a) 32; b) **37**; c) 42; d) 45 | Subtítulos (teoría) | § 2, tabla visual | Sí |
| 5 | Combinación de colores más legible y a quién se asigna: **amarillo sobre negro, al personaje principal** | Subtítulos | § 2 «Colores» | Sí |
| 6 | Cómo se llaman los espacios donde se insertan las unidades descriptivas de la audiodescripción: **huecos de mensaje** (y la norma: UNE 153020:2005) | Audiodescripción | § 3 «Qué es»; § 1 tabla AENOR | Sí |
| 7 | Qué norma reconoce el derecho de las personas con discapacidad intelectual a programas subtitulados según métodos de lectura fácil: **LAA, art. 9.4**; norma técnica de lectura fácil: **UNE 153101:2018 EX**, para documentos | Lectura fácil | § 4 | Sí |
| 8 | Qué excluye el art. 3.3 del RD 1112/2018: **los contenidos multimedia en directo y pregrabados de las webs y apps de los prestadores del servicio público de radiodifusión** | Versiones para plataformas | § 5 «Webs y aplicaciones» | Sí |
| 9 | Un programa emitido con subtítulos pasa a la OTT: qué precepto obliga a mantener su accesibilidad: **LAA art. 31.1.i)** (y, para contenidos de terceros, LGCA art. 105) | Plataformas (aplicación práctica) | § 5 «Mantener la accesibilidad»; supuesto, punto 2 | Sí |
| 10 | Supuesto: subtítulo de dos líneas llenas a la velocidad recomendada; ¿cuánto tiempo necesita y cumple el máximo?: **74 caracteres a 15 c/s ≈ 5 s; dentro del máximo de 6 s** | Subtítulos (aplicación práctica) | § 2 cuentas; supuesto, punto 4 | Sí |

Resultado: las diez se contestan enteras con el tema; no ha hecho falta ampliar.
