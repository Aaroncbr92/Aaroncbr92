# Puesto 08 · Tema 9 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`
(estado en disco a esa fecha, tras la verificación). No corrijo: listo hallazgos para el remate.

## Alcance y método

- «Copiado del común»: ninguno (informe de redacción), así que no se salta nada.
- Tema técnico sin norma jurídica: sin lentes de normas. Lente propia: script que normaliza y busca
  cada cita en negrita en las fuentes (resultado: **todas** localizadas; sólo quedan fuera los tres
  rótulos de estructura «Redacción que se estudia», «Enunciado del programa», «Qué se puede preguntar»).
- Fuentes releídas el 24-09-2026 para contexto, cifras y secciones: EBU R 103 v3.0 (anexos 1 y 2,
  tabla 1); EBU R 118 v2 (§ 1.1-1.3.1, tablas 1, 2 y 6, § 2.7, 2.9, 3.1.1-3.1.5); EBU Tech 3335
  (índice, § 2.4, 2.9, 2.9.1, 4.3, 4.4); EBU Tech 3355 (§ 1.5.2); UIT-R BT.601-7, BT.709-6,
  BT.2020-2 (copias locales) y BT.2100-3 (nota 10a); Sony PXW-Z200 Help Guide (Knee, Black, Detail,
  Noise Suppression, Flicker Reduce, SteadyShot); Blackmagic URSA Broadcast G2 (tiraje); Libro de
  estilo de Canal Sur (páginas 79, 80, 91 y 92 comprobadas contra los folios del texto).

## Confirmado

Tabla 1 de R 103 (16 valores), umbral del 1 %, recortadores al rango preferente, legalizadores,
PLUGE y 0-700 mV (anexo 2). R 118: seis niveles HD/SP y cuatro UHD con sus resoluciones, 33 % (§ 2.9),
2J como «relaxation», bits y 4:2:2 de la tabla 2 y del § 2.7, S/N de la tabla 6 y sus notas, ganancia
negativa, § 3.1.3-3.1.5, tasas 100/200, 50/75 y H.264 25/35, MPEG-2 UHD «Not to be used». Tech 3335:
Lmax/Lmin y margen de 1-3 pasos (§ 2.4), 7,5 pasos, 1 paso por 6 dB, 12-13 pasos y *black-stretch*
(§ 4.4), *videolook* (§ 4.3), obturador de persiana (§ 2.9) y obturación nominal (§ 2.9.1). Primarios,
D65, 16/235 y 64/940 (BT.709-6); primarios BT.2020-2; coeficientes de luminancia de las tres
recomendaciones; nota 10a de BT.2100-3. Sony Z200: *knee* 75-109 %, 90 %, ±99, Auto Knee y Setting
[On] en SDR; negros ±99,0; detalle ±7; *crispening* 0-7; Noise Suppression [On]/[Mid];
Flicker Reduce [Off] y [60Hz]. Tiraje: método del manual de Blackmagic coincide con los pasos del tema.

## Hallazgos de exactitud

**H1 (menor, error 9, oficio mal razonado).** «Color · La colorimetría de referencia»: «Ésa es la
razón de que un error en el canal azul se note mucho menos […] y de que el ruido suela verse antes en
el azul». El peso bajo del azul en la luminancia explica lo primero, pero no lo segundo (si acaso,
haría el ruido azul *menos* visible en la luminancia). Que el canal azul sea el más ruidoso no se
deduce de los coeficientes. Proponer: quitar «y de que el ruido suela verse antes en el azul» o
separarlo como oficio sin ese «Ésa es la razón».

**H2 (menor, error 6, salvedad omitida).** «Exposición · El margen de exposición»: la cita de
Tech 3335 § 4.4 empieza en «the effective dynamic range will be reduced…», pero la frase original
arranca con la condición «**If the noise level is particularly high, then** the effective dynamic
range will be reduced by about 1 stop per 6dB of video noise level increase». Proponer: incluir la
condición en la cita (o marcar el corte con […] y decirla en redonda). Afecta también a la
«consecuencia práctica» del párrafo siguiente.

**H3 (menor, redacción).** «El punto dulce y la difracción»: «unos dos o tres pasos por debajo de la
abertura máxima» es ambiguo (en número f el punto dulce está *por encima*). Proponer: «cerrando unos
dos o tres pasos desde la abertura máxima». Oficio, sin cambio de dato.

**H4 (menor, error 3 aparente, sólo aviso).** «Qué se mide…»: el tema dice que R 118 «fija cinco
criterios de medida, a los que suma el códec». La fuente (§ 1.1) dice «five areas that are specific
to the actual camera and (where applicable) to the on-board codec» y lista seis viñetas, con el códec
en primer lugar. La lectura del tema es razonable; conviene sólo añadir que la lista de la fuente
tiene seis viñetas y empieza por el códec, para que un recuento no despiste.

Sin hallazgos graves: ninguna cita falsa, ningún valor de tabla erróneo, ninguna sección mal
atribuida.

## Cobertura del enunciado

«Foco, exposición, color, estabilidad, ruido, compresión y continuidad»: los siete elementos tienen
epígrafe `##` propio y en el orden del enunciado. Preguntas en `08-T09-preguntas.md`: 14 enteras,
0 a medias, 1 no.

**L1 (laguna, se amplía).** El tema describe el *knee* sólo con oficio y con los valores de fábrica
de la Sony Z200, pero Tech 3335 § 4.4 (fuente ya citada) da el ajuste recomendado: «Set the knee
function on (manual knee) and the knee point to between 80% and 90%. This will ensure that skin tones
remain in the normal part of the gamma curve.», y además «set white clipping to not greater than
about 104%» para el bajo contraste y, en directo o «as-live», «always use curves that do not exceed
100%». Son datos de norma técnica que el tribunal puede preguntar (P10) y que casan con «Las altas
luces: el *knee*». Proponer: añadir esas tres citas en ese epígrafe, con § 4.4.

## Resumen

Graves: 0. Menores: 4 (H1-H4). Lagunas: 1 (L1).

## Otros ficheros tocados

Ninguno, salvo `08-T09-preguntas.md` y este informe.
