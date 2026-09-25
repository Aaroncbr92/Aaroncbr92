# Puesto 30 · Tema 10 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/10-derechos-autor-imagen-musica-archivo-creditos-terceros.md`.
Material: `30-investigacion-C-derechos-plataformas.md` (§ Tema 10); Cámara T12 (08/12, cerrado); RTVE
`produccion-asistencia/02`, `produccion/02`, `diseno-grafico/13`.

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| TRLPI, volcado `fuentes/canal-sur/BOE-A-1996-8930.md` (+ `.redacciones.tsv`) | arts. 1-3, 5-7, 9, 10, 14, 15, 17-21, 26, 28, 30-33, 35-37 bis, 39, 40 bis, 41, 43, 45, 50, 51, 86-90, 92, 93, 105, 108, 110, 113, 114, 116, 120-122, 124-128, 138, 140, 144-147, 153, 163, 164, 166, 167 | 25-09-2026 |
| RDL 24/2021, `boe.py precepto BOE-A-2021-17910` | a6-8 (art. 66), a7-2 (art. 70), a7-5 (art. 73): una redacción cada uno, vigente desde 04-11-2021 | 25-09-2026 |
| Ley 10/2018, volcado `BOE-A-2018-15240.md` | art. 20 (una redacción, desde 17-10-2018) | 25-09-2026 |
| Carta 2024-2029 (txt local) | arts. 24.2.a y 27 | 25-09-2026 |
| Contrato-programa 2024-2026 (txt local) | 3.22, puntos 120-122 | 25-09-2026 |
| X Convenio (txt local) | ficha 5212206, p. 190 | 25-09-2026 |
| Libro de estilo 2004 (txt local) | 3.2.2 (p. 46), 3.10 (p. 53), 9.2.12.4 (pp. 130-131), anexo Código FAPE punto 12 (p. 470) | 25-09-2026 |
| CC BY 4.0, legalcode.es (descargado con curl) | sección 3(a)(1) y (2) | 25-09-2026 |
| BOE-A-2020-10489 (txt del BOE, curl) | fecha de la autorización de SEDA, objeto estatutario, interesados | 25-09-2026 |

## Qué se hizo

Tema escrito por epígrafes en ocho partes guardadas una a una (`p00`-`p07` en el scratchpad) y montado
con un script que inserta los pasajes de Cámara T12 por número de línea, para que la copia sea literal
byte a byte; índice generado con la regla de anclajes de GitHub. Estructura: «De dónde sale» (con la
ficha del puesto), las seis rúbricas en el orden del enunciado, tabla de aplicación práctica,
normativa, «Lo que este tema no da» y trazabilidad. Extensión ≈ 14.000 palabras.
`refutar_prosa.py`: 0 hallazgos (tras presentar OTT y URI, que sólo aparecen en citas).
`negritas.py` contra TRLPI, Ley 10/2018, LO 1/1982, LO 1/1996, LGCA, Ley 18/2007, CE, Carta,
Contrato-programa, convenio, Libro de estilo (ligaduras normalizadas), CC BY, SEDA y RDL 24/2021:
182 negritas, 4 «no están»: tres del art. 681 LECrim (pasaje copiado de 08/12; no hay volcado local de
la LECrim) y la de 9.2.12.4, partida por un salto de página en el txt (comprobada a mano). Los 6
«atribuidas a otro artículo» son falsos positivos de proximidad (cada cita lleva su artículo en el
texto).

**Correcciones y matices a la investigación:**

- 10.0 dice que los arts. 65-72 y 74-80 del RDL no se comprobaron: el tema sólo usa 66.6, 70 y 73, los
  tres leídos (una redacción).
- 10.2: la investigación no citaba la Ley 10/2018, art. 20.2 (protección especial de los archivos de la
  RTVA, gestión por personal propio, supervisión de la Consejería, dotación específica). Leído y
  añadido; es la base legal que la Carta, art. 27.1, invoca.
- 10.2 atribuye a 163.4 y 164.1 que son «nuevo, no está en RTVE»: correcto.
- La investigación proponía 36.3 y 93.2 sólo implícitamente; el tema los aplica al archivo.
- Añadido del Libro de estilo, no previsto por la investigación: 3.2.2 (música y rótulo
  «reconstrucción»), 3.10 (música en cierres; coleo para créditos), 9.2.12.4 (música en malos tratos),
  anexo FAPE punto 12.
- RTVE `produccion/02` § 8 aporta un caso útil (película antigua en una noticia) que se adapta, sin la
  referencia al examen de RTVE, como fila de la tabla práctica. `diseno-grafico/13` no aporta nada
  jurídico que no esté en `produccion-asistencia/02` o en 08/12.
- Lista de entidades de gestión: se reintentó cultura.gob.es; falla el certificado TLS. No se usa la
  lista; sólo SEDA con su resolución.

## Copiado del común

Pasajes copiados literal de Cámara Operador T12
(`temas/canal-sur-especificos/08-camara-operador/12-derechos-de-imagen-privacidad-menores-victimas.md`,
cerrado). No se re-verifican.

| Pasaje en 08/12 (líneas) | Dónde va en este tema (líneas) |
|---|---|
| «El marco: Constitución, ley audiovisual y normas de la RTVA» y «La Ley Orgánica 1/1982», epígrafes completos (96-166) | 2 · 431-501 |
| «Fallecidos y tutela judicial», epígrafe completo (207-239) | 2 · 503-535 |
| «La imagen como dato personal», desde el rótulo hasta «(artículo 17.3.a).» (241-257); se omite la frase final «El epígrafe 5 explica…», que remite a un epígrafe que aquí no existe | 2 · 537-553 |
| «La imagen y los datos de los menores en los medios», cuerpo completo sin el rótulo (355-399) | 2 · «Menores y víctimas», 557-601 |
| «La LECrim: víctimas que no se graban nunca», primeros párrafos hasta el final de la cita del 681.3 (533-554) | 2 · «Menores y víctimas», 603-624 |
| 9.9.2, desde «En el proceso posterior de selección y edición…» hasta «…la muerte o el sufrimiento.» (765-783) | 2 · «Lo que el Libro de estilo pone en la edición», 640-658 |
| 9.9.1, viñeta «Archivo» (745-749) | 4 · «El archivo en la pieza», 912-916 |

También literales de 08/12, dentro de frases propias: la cita de 9.9 «La imagen de menores de edad…»
(08/12, 469-471) y el inciso de 9.9.2 «está obligado a captar los hechos, con prudencia, con cierta
distancia física y profesional» (08/12, 759-760).

## Copiado de RTVE sin cambios

Ninguno. El ENCARGO reserva esta lista a pasajes técnicos de temas sin actualizar; los tres temas de
RTVE de este encargo son jurídicos y todo lo que se toma de ellos cita normas, así que va a la lista
siguiente y se verifica. Además, el formato de RTVE usa negrita de énfasis, que en Canal Sur sólo marca
lo literal: ningún pasaje podía copiarse sin tocar.

## Tomado de RTVE (sí se verifica)

De `produccion-asistencia/02` (redacción 21-12-2022; TRLPI sin cambios desde 31-03-2022, comprobado
en el `.redacciones.tsv`), con la negrita reducida a lo literal, sin remisiones a sus epígrafes y sin
lo propio de RTVE (§ 15, exámenes; «hueco» de normativa interna de RTVE):

- § 1.1 (arts. 1-3) → 1 «Qué protege la ley».
- § 2.1 (arts. 5-6) → 1 «Quién es autor».
- § 3, tabla del art. 14 → 1 «El derecho moral» (textos de cada facultad ajustados al literal).
- § 4.1-4.4 (arts. 17-21, tabla del 20.2 reducida a c, e, f, g, i) → 1 «Los derechos de explotación».
- § 6 (arts. 26, 28, 30, 41) → 1 «Cuánto duran» y «El derecho moral».
- § 7.3 (arts. 33 y 35) y § 7.2 (art. 32.1) → 6.
- § 7.4 (art. 37 bis) → 4 «Obras huérfanas».
- § 7.5 (arts. 39 y 40 bis) → 6.
- § 8.1-8.4 (arts. 43, 45, 50, 51) → 1 «Ceder y licenciar» y «La obra hecha en la casa».
- § 9.1-9.4 (arts. 86-88, 92, 93) → 1 «La obra audiovisual».
- § 10.1-10.5 (arts. 105, 108, 110, 113, 114, 116, 120-128) → 1 y 3; tabla obra fotográfica / mera
  fotografía.
- § 11 (arts. 138 y 140) → 1 «Si se infringe».
- § 12 (arts. 145, 146, 147) → 3 y 5.
- § 4.3 (art. 36.3) → 4.
- § 14.2 (arts. 66.6, 70, 73 RDL 24/2021) → 6 «Plataformas» y «Parodia y pastiche».

De `produccion/02` § 8: la idea del caso de la película antigua (fila de la tabla del epígrafe 7), sin
la pregunta de examen.

Nuevo sobre RTVE y la investigación (se verifica entero): arts. 7, 9.1, 15.1, 31.1, 163-167, 153,
Ley 10/2018 art. 20, Carta 24 y 27, Contrato-programa 120-122, ficha 5212206, Libro de estilo 3.2.2,
3.10, 9.2.12.4 y anexo FAPE, CC BY 4.0, SEDA.

## Para el verificador

Todo lo que no está en «Copiado del común» se verifica. Lecturas del tema que son deducción del texto
y se dicen como tales: que la cita del 32.1 no ampara un informativo (fines docentes o de
investigación); que capturar la emisión de otra cadena es fijarla (126.1.a); que un medio que publica
sus piezas pueda o no acogerse al 73.2 (el tema no lo resuelve); cómo casan 33.1 y 126 (no se
resuelve). Oficio declarado: «hoja o relación de músicas». No se afirma quién declara la música en la
RTVA.

## Ficheros tocados

- Creado: el tema 10 (ruta arriba).
- Creado: este informe.
- Scratchpad (fuera del repositorio): partes del tema, `ccby.txt`, `seda.txt`, extractos del RDL.
- Ningún otro fichero del repositorio.

## Diez preguntas tipo test (comprobación de cobertura)

Contestadas sólo con el tema. Resultado: las diez, enteras. Una laguna previa (película antigua en una
noticia, que enlaza plazos y el art. 35.1) se cerró añadiendo una fila a la tabla del epígrafe 7 antes
de redactar las preguntas.

1. **Según el art. 1 TRLPI, la propiedad intelectual de una obra corresponde al autor:** a) desde su
   inscripción en el Registro; b) por el solo hecho de su creación; c) desde su divulgación; d) desde
   que se antepone el símbolo ©.
   → **b**. Tema: 1, «Qué protege la ley y desde cuándo»; 5, «Los símbolos de reserva». Entera.
2. **Son autores de la obra audiovisual (art. 87):** a) el director-realizador, el productor y el
   montador; b) el director-realizador, los autores del argumento, la adaptación, el guion o los
   diálogos, y los de la música creada especialmente para ella; c) todos los que intervienen en ella;
   d) el productor y el guionista.
   → **b**. Tema: 1, «La obra audiovisual». Entera.
3. **En una obra audiovisual producida para su emisión, ¿qué modificaciones de la versión definitiva se
   presumen autorizadas?** a) ninguna; b) cualquiera que decida la cadena; c) las estrictamente
   exigidas por el modo de programación del medio, sin perjuicio del derecho a la integridad; d) sólo
   el doblaje.
   → **c** (art. 92.2). Tema: 1, «La obra audiovisual». Entera.
4. **No es intromisión ilegítima en la propia imagen (art. 8.2 LO 1/1982):** a) emitir el rostro de un
   viandante convertido en protagonista; b) la información gráfica de un suceso público en la que la
   persona aparece como meramente accesoria; c) usar su imagen en una promoción; d) grabarlo en su vida
   privada.
   → **b**. Tema: 2, «La Ley Orgánica 1/1982». Entera.
5. **La utilización de la imagen de un menor en los medios que pueda menoscabar su honra o reputación
   es intromisión ilegítima:** a) salvo consentimiento de sus padres; b) salvo que sea mayor de
   catorce años; c) incluso si consta el consentimiento del menor o de sus representantes legales;
   d) sólo si hay denuncia del Fiscal.
   → **c** (art. 4.3 LO 1/1996). Tema: 2, «Menores y víctimas». Entera.
6. **La remuneración por el uso de un fonograma publicado con fines comerciales para la comunicación
   pública:** a) la cobran sólo los autores; b) es equitativa y única, para artistas y productores de
   fonogramas, repartida por partes iguales a falta de acuerdo, y excluye la puesta a disposición del
   art. 20.2.i); c) la cobra el productor, que decide si paga a los artistas; d) sólo se debe en
   plataformas a la carta.
   → **b** (arts. 108.4 y 116.2). Tema: 3, «Remuneraciones que genera la emisión». Entera.
7. **Salvo acuerdo, los usuarios deben facilitar a la entidad de gestión la información sobre la
   utilización de los derechos en:** a) treinta días; b) noventa días; c) seis meses; d) un año.
   → **b** (art. 167.1), con cláusula de penalización obligatoria (167.6). Tema: 3, «Lo que las
   entidades deben al usuario…». Entera.
8. **Los organismos públicos de radiodifusión pueden usar como obras huérfanas las obras audiovisuales y
   fonogramas producidos por ellos y que figuren en sus archivos hasta:** a) el 31-12-1995; b) el
   31-12-2002 inclusive; c) el 01-01-2015; d) sin límite de fecha.
   → **b** (art. 37 bis.4.b). Tema: 4, «Obras huérfanas». Entera.
9. **En las copias de los fonogramas, el símbolo que puede anteponerse al nombre del productor es:**
   a) © con el lugar y año de divulgación; b) (p) indicando el año de la publicación; c) ® con el año
   de registro; d) ninguno, porque la ley no prevé símbolos.
   → **b** (art. 146). Tema: 5, «Los símbolos de reserva». Entera.
10. **(Práctica) Montas una noticia sobre el concierto de anoche con un fragmento de la actuación. ¿Qué
    lo ampara y qué pauta de la casa rige la música?** a) el derecho de cita del art. 32.1, sin
    límite; b) el art. 35.1, sólo en la medida que lo justifique la finalidad informativa, y el Libro
    de estilo admite la música porque es la referencia noticiosa principal; c) nada: hace falta siempre
    licencia de la entidad; d) la libertad de panorama del art. 35.2.
    → **b**. El 32.1 exige fines docentes o de investigación. Tema: 6, «El límite del informativo» y
    «Por qué la cita no es el límite…»; 3, «Lo que el Libro de estilo dice de la música»; tabla del
    epígrafe 7. Entera.
