# T04 · Redacción · Ley 13/2022 y Ley 10/2018

Tema: `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md`. Punto 4 del temario común de
Canal Sur. Fase 2 (redactar), un solo agente. Fecha de trabajo y de lectura de todos los
preceptos: **24-09-2026**, sobre los volcados de `fuentes/canal-sur/` (`BOE-A-2022-11311`,
`BOE-A-2018-15240`, `BOE-A-2005-655`, y `BOE-A-2007-5825` para los arts. 69 y 210 del Estatuto),
más `boe.py precepto` / `--fecha` para las redacciones anteriores de la Ley 10/2018 y la API de
datos abiertos del BOE para las tablas de la DT 1.ª (el volcado las pierde) y la DT 2.ª de la Ley
13/2022.

## Estructura

Portada, siglas, enunciado literal, párrafo inicial, índice vacío; `##` de identificación (título
= primera parte literal del enunciado: naturaleza, estructura, objeto, ámbito, carácter básico,
reformas, relación entre las dos leyes, autoridades); después una `##` por rúbrica en el orden del
enunciado (Principios de la comunicación audiovisual · Pluralismo · Protección de menores ·
Accesibilidad · Servicio público), cada una con `### En la Ley 13/2022` y `### En la Ley 10/2018`;
cierre con Normativa, Lo que este tema no da y Trazabilidad. La fila Extensión queda con el
marcador `EXTENSION` para `indice.py`, como en el tema 9.

## Qué reutilicé del tema de RTVE (`temas/general/07-ley-13-2022.md`)

Literal o casi, releído en la redacción vigente: bloque de identificación (166 arts., DF 8.ª,
derogación), tabla de la DF 9.ª (pasada a pasado: el capítulo de accesibilidad ya rige), art. 1,
DF 6.ª; tabla de los doce artículos del título I y párrafos de los arts. 6, 7, 9, 10, 12, 14 y
15; puntos de los arts. 35, 36, 78 y 79; capítulo I del título VI (arts. 95, 97-98, 99 con su
tabla de franjas y las salvedades de juego, 100); tabla de cuotas de accesibilidad y la frase «el
servicio público carga con el triple de horas…»; arts. 50-53, 56, 58-61, 62-66 del título III, la
tabla mandato-marco/contrato-programa y el aviso del «error típico»; art. 33 («el privado puede;
el público debe, y gratis»); art. 118 (6 % y 70 %).

## Qué corregí de RTVE (comprobado en la fuente)

Los que marcaba la investigación (su informe dice «seis», pero lista siete; los siete se
comprobaron y se corrigieron):

1. **Art. 15.2**: nueve características (a-i), no seis; añadidas g), h), i).
2. **Art. 15.5**: «códigos de conducta de ámbito europeo **o internacional**».
3. **Múltiplex**: los límites de dos y uno están en el **art. 35.5**, no en el 24.
4. **Art. 54.3.a**: seis objetivos, no cinco (falta el 6.º, información veraz previo contraste); y
   se aclara que el 54.3 es solo del mandato-marco estatal.
5. **Art. 102**: noticiarios, infantil, etc., son contenido obligado de las horas de **lengua de
   signos**; las audiodescritas deben incluir películas y series (102.1.c y 2.c).
6. **Art. 103**: lengua de signos no es «—», sino «incorporación gradual» de los programas de mayor
   interés (103.1.c).
7. **Art. 33**: quitado el «must offer» (no está en la ley); añadidos el derecho a los datos de
   consumo y el párrafo del catálogo (acuerdo previo).

Otros que encontré al releer RTVE contra la fuente:

- **Rúbrica del título VI**: RTVE lo llama «Protección del usuario»; su rúbrica literal es
  «**Obligaciones de los prestadores del servicio de comunicación audiovisual televisivo**».
- Art. 99.6 (y 83.4): faltaba la salvedad de operadores designados «**o por la correspondiente
  legislación autonómica**».
- Art. 98.2: faltaban «las organizaciones representativas de los usuarios de los medios».
- Art. 4: faltaban el 4.1 y las tres leyes orgánicas del 4.3; «religión o creencias, opiniones
  políticas o de cualquier otro tipo».
- Art. 5 y 9.1: resúmenes de RTVE sustituidos por el literal (5.2 omitía los ámbitos
  territoriales y el servicio público; 9.1, el pluralismo y la libre formación de opinión).
- Art. 6.4 y 61: RTVE ponía en negrita paráfrasis («informe ANUAL…», «nuevo servicio es el no
  incluido…»); sustituidas por el literal.
- Art. 78.3: RTVE dejaba «límites adicionales»; se dan las cifras (un tercio; 40 %) y el 78.4.
- Art. 50: faltaba «según lo dispuesto en el artículo 53».
- Varias negritas de RTVE que no eran literales se pasaron a cita literal o a redonda (arts. 35.2,
  36, 53.4, 62, 64, 72.3, 73…). Hice además una pasada automática de todas las negritas de 4 o más
  palabras contra las fuentes; lo que queda sin casar son rótulos de párrafo, fechas y nombres de
  normas.

## Errores o huecos de los informes de investigación

- **Ninguna cifra de los dos informes resultó errónea** al comprobarla en la fuente. Se verificaron
  en particular: 229 bloques y reparto 210/4/15; arts. 67-71 = capítulo V; 17 ámbitos del 15.4;
  15 letras del art. 2.1 de la Ley 10/2018; horas **diarias** de la DT 1.ª y del art. 9 de 2018;
  cadenas de los arts. 7, 8, 9, 31, 32, 41, 44 y 46.
- **Matiz añadido**: el art. 32.d) de 2018 hablaba de responsabilidad **solidaria** (no la
  subsidiaria del 99.5 estatal).
- **Matiz añadido sobre el Estatuto**: la investigación cita solo el 210.1 («gestión directa»). Leído
  el art. 210 entero, el apartado 2 permite concesiones de gestión indirecta «sin perjuicio» del 1,
  y el 3 dice que la Junta gestionará directamente un servicio. Por eso el tema no dice que el
  Estatuto «imponga» la gestión directa: dice que la impone el art. 46.1 de la Ley 10/2018
  invocando el 210.
- **No usé** la afirmación de que el DL 3/2024 «adapta la ley a la Ley 13/2022» como propósito del
  decreto (no he leído su texto); el tema describe lo observable: sustituyó remisiones y suprimió
  reglas.
- Añadí preceptos que los informes no daban y que están en la fuente: DT 4.ª de la Ley 13/2022
  (umbrales de 2 M€, 2 % y 1 % para la exención del 101.4), DF 7.ª.dos (actualización de cifras),
  arts. 153.5 y 155.4, art. 2.10.c), infracciones 157.9/11/12 y 158.7-14/17; de la Ley 10/2018,
  arts. 10, 31.1.l) (30 segundos por hora), 31.2, 35 (50 % obra andaluza, con su cadena), 37.c),
  54.3 y el art. 69.1 del Estatuto.

## Qué dejé fuera y por qué

- **Arts. 67-71** (capítulo V del título III, estatal y RTVE, no básico por la DF 6.ª): solo se
  nombran para decir que no obligan a Canal Sur. Fuera también los once extremos del
  contrato-programa estatal (55.3) salvo su mención, y el detalle del 61.2-3.
- Lo de RTVE sin encaje en Canal Sur: el apartado sobre la fecha de corte de 2022, la Guía de
  Igualdad de RTVE, las DF 3.ª y 4.ª (Leyes 17/2006 y 8/2009), catálogo de acontecimientos, Plan
  Estratégico, sanciones y prescripción en general, obra europea salvo el art. 118, comunicaciones
  comerciales salvo el art. 124: fuera del enunciado.
- De la Ley 10/2018, lo que no toca las rúbricas: Administración audiovisual y Registro,
  comunitarios y privados (salvo DA 3.ª), inspección y sanción (salvo arts. 66.3, 73.a y 78.3).
- **Art. 4 de la Ley 1/2004** (funciones del Consejo Audiovisual): no se estudia; va a «Lo que este
  tema no da», porque tras la STC 40/2025 el BOE lo muestra «(Anulado)» y ninguna norma leída dice
  qué texto rige. Las funciones del Consejo solo se citan cuando están en la Ley 10/2018.
- Criterios de la DT 2.ª de la Ley 13/2022: la API solo da las categorías (apta, +7, +12, +16, +18,
  X); los criterios no se ven. Van a «Lo que este tema no da».

## Puntos abiertos, declarados y no resueltos

En notas en cursiva dentro del cuerpo y en «Lo que este tema no da»: STC 40/2025 y art. 4 de la
Ley 1/2004; recurso 3473-2024 contra el DL 3/2024 (verificado en el BOE: providencia de
17-06-2024, `BOE-A-2024-12561`); fecha jurídica de entrada en vigor de los arts. 39 y 94 (se
nombran los RD 1138/2023 y 444/2024, verificados por título, sin dar fecha de vigencia);
convalidación de los decretos-leyes; remisión colgada del art. 48.2 al art. 21.3 suprimido;
articulación de la DT 1.ª y el art. 31.1.h) con el art. 9 ya sin cifras y el art. 102.2 estatal.

## Palabras finales

**18.375 palabras** (`wc -w` del fichero entero, con tablas, portada y cierre). Escrito con
margen, como pide el encargo; la verificación y la refutación pueden recortar prosa.

## Ficheros tocados

- Creado `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md`.
- Creado este informe, `informes/canal-sur-comun/T04-redaccion.md`.
- Nada más. No toqué `fuentes/` (las lecturas de redacciones anteriores y de la API se hicieron a la
  salida estándar o a la carpeta temporal de la sesión).
