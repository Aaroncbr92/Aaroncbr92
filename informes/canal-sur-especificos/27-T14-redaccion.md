# Redacción · Oficial Técnico Electricista (27) · Tema 14 · Medidas eléctricas e instrumentación

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/14-medidas-electricas-e-instrumentacion.md`
(13.068 palabras según `indice.py`, 44 epígrafes). Material: `27-investigacion-A-electrico.md` (§0,
§1, §6, §7, §9). Reuso RTVE (95 %, actualizar: no): `teitse/09` §4-§6 y `teitse/01` §5. Fecha
declarada de lectura: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»). Escrito
por partes (cabecera; 1; 2-3; 4; 5; 6-7; cierre), guardando cada una.

Lentes corridas: `indice.py` (índice generado; la portada es manual, como en los temas 3 y 8);
`refutar_prosa.py` (4 siglas sin presentar, corregidas: LED y los nombres de fabricante; 0 al final);
`negritas.py` contra BOE-A-2002-18099, BOE-A-2001-11881 y las cinco fuentes técnicas (187 negritas;
11 «no está»: 2 rótulos de forma —«Enunciado del programa», «Qué se puede preguntar»—, 3 rótulos
que se han pasado a redonda/cursiva, 1 cita corregida a su letra —FLIR, «desaparezca … cámara
termográfica»—, 4 citas del INSST que sí son literales pero el `.txt` corta las palabras con guion
blando U+00AD + salto, comprobado a mano, y 1 de AEMC con la ligadura «ﬁ» del PDF normalizada a «fi»).

## Ficheros tocados

- El tema (nuevo) y este informe.
- `fuentes/canal-sur/tecnica/`, nuevos (PDF descargado + `.txt` de `documento.py texto`):
  `fluke-abc-seguridad-mediciones-2003`, `circutor-manual-comprobador-diferenciales-cdb`,
  `aemc-entendiendo-pruebas-resistencia-tierra-2003`, `flir-guia-termografia-mantenimiento-2011`.

## Estructura

Epígrafes en el orden del enunciado: 1 la rúbrica general (quién mide, instrumentos de la ITC-BT-03,
medir en tensión o sin ella, categorías de medida, comprobador de instalaciones: continuidad, bucle
y diferenciales, que el tema 3 remitía aquí); 2 multímetro; 3 pinza; 4 telurómetro; 5 medidor de
aislamiento; 6 analizador de redes; 7 termografía básica; normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- REBT (volcado `fuentes/canal-sur/BOE-A-2002-18099.md`): ITC-BT-01 (corriente de fuga); ITC-BT-03,
  apéndice I entero (vig. 04-09-2025, RD 770/2025; el 2.1.2 y 2.2 coinciden con la investigación);
  ITC-BT-05, 1-4 (vig. 30-06-2015); ITC-BT-18, 3.3, 7-12 y tablas (vig. 23-05-2010); ITC-BT-19, 2.9
  entero; ITC-BT-24, 3.5, 4.1, 4.1.1 y 4.1.2.
- RD 614/2001: anexo I (8, 10, 13, 14), anexo II B.3 y B.4.1, anexo IV entero, anexo V B.1.
- Guía INSST 2020: comentarios al anexo IV y a la verificación de ausencia de tensión.
- Fuentes técnicas nuevas (ninguna estaba en la investigación, que dejó CAT y termografía como «no
  confirmado»): Fluke 2003 (categorías de medida), manual Circutor CDB (comprobador de diferenciales),
  AEMC 2003 (método del 62 %, pinza de tierra, Wenner), FLIR 2011 (termografía).

## Avisos para el verificador

- **Corrección al RTVE**: la fila del megóhmetro de `teitse/09` §4 dice «la instalación tiene que
  estar sin tensión y los receptores desconectados». La ITC-BT-19, 2.9, manda medir el aislamiento
  a tierra **dejando, en principio, todos los receptores conectados**, y desconectarlos sólo para la
  medida entre conductores. La fila se ha rehecho (5.1) y el 5.2 lo explica.
- Quitado del RTVE por no confirmado: «el neutro de la distribuidora» en el aviso 1 de la medida de
  tierras (en TT la tierra de la instalación no está unida al neutro); «Es el que usa un organismo
  de control» (fila del comprobador); la referencia a «la instrucción de puesta a tierra dedica un
  apartado a la revisión» se ha sustituido por la cita del apartado 12 de la ITC-BT-18.
- ITC-BT-03: «ITC MIE-BT 19» es numeración antigua; se cita tal cual con aviso.
- RD 614/2001, anexo II, B.4.1 (secundario de transformadores de intensidad) está bajo el título
  **Trabajos en transformadores y en máquinas en alta tensión**: se cita con esa salvedad (error 6).
- ITC-BT-18, 12, «mas» sin tilde: así en el BOE, avisado en el pie de la cita.
- AEMC: la fuente escribe «desde X a Y» donde quiere decir «desde X a Z»; se cita la parte segura y
  se avisa de la errata. Las cifras de AEMC (2.4 kHz, 5 A) son de sus modelos 3711/3731 y así se
  presentan.
- Fluke es de 2003; la IEC 61010 ha tenido ediciones posteriores. Por eso no se reproduce la tabla
  de transitorios de ensayo por categoría, sólo la clasificación y las reglas de elección.
- Circutor: el manual no da los tiempos máximos normativos de disparo; el tema no los da (UNE-EN
  61008-1/61009-1 no leídas). Los 300 ms/40 ms que circulan en la web no se han usado.
- La FLIR es de 2011 (© en la p. 2); la cifra de 30 mK y la precisión ±2 %/±2 °C son de esa fecha y
  de ese fabricante, y así se dicen.
- Aritmética propia, sin cita de norma: RA máxima (50/0,03 ≈ 1.667 Ω, etc.), resistividad desde una
  pica (ρ = R·L), regla de los 100 m (0,5/3 ≈ 0,17 MΩ), rigidez (2·400+1000 = 1.800 V).

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur, y `27-args.json` no marca
repetición para el tema 14.

## Copiado de RTVE sin cambios

Sólo se han quitado las negritas y las mayúsculas de énfasis (en RTVE son de énfasis, no de literal
de fuente). Ninguno cita norma. Comprobado por script (texto normalizado contenido en el fichero
RTVE y en el tema).

De `teitse/09` §4 (en 1.3, 2.1, 3.1, 4.1, 6.1 y 7.1):
- «antes de medir hay que decidir si se mide en tensión o sin tensión, y si es sin tensión, hay que
  aplicar las cinco reglas de oro. La comprobación de ausencia de tensión es, ella misma, una medida
  en tensión.» (en 1.3, con «Antes» en mayúscula inicial).
- La tabla «Medida | Estado de la instalación» (dos filas: megóhmetro sin tensión y descargada;
  termografía y análisis de red en carga) y el párrafo «La razón: … mal planificado.» (1.3).
- Filas de la tabla de equipos: polímetro (2.1), pinza amperimétrica (3.1), telurómetro (4.1),
  analizador de redes (6.1), cámara termográfica (7.1).

De `teitse/09` §5 (en 4.1, 4.3 y 4.5):
- «Qué se mide: la resistencia entre el electrodo y el terreno lejano, … se disipe.» (4.1).
- Filas 2 a 5 de la tabla del método (4.3).
- «Y la regla que hace válida la medida, … demasiado cerca.» (4.3).
- «La alternativa sin picas: … electrodo único y aislado.» (4.5).

De `teitse/01` §5 (en 1.4, 2.1, 2.2, 2.3, 3.1, 3.2 y 3.3):
- «Antes de medir hay que saber qué se va a medir y con qué categoría de medida está clasificado el
  instrumento. Un polímetro de categoría insuficiente … transitorio.» (1.4).
- Fila «Polímetro o multímetro | Tensión, corriente, resistencia, continuidad y a veces frecuencia y
  capacidad» (2.1).
- Tabla voltímetro/amperímetro y el párrafo «Y el error que la regla previene, … se produce es un
  arco.» (2.2).
- Párrafo «El valor que muestra un instrumento en alterna, … la única lectura fiable.» (2.3).
- Tabla de los tres rasgos de la pinza (3.1) y tabla de tecnologías (3.2).
- Párrafo «El último rasgo tiene una aplicación directa … hace saltar un diferencial.» (3.3).

Adaptado (se verifica): fila del megóhmetro (5.1, rehecha sobre la ITC-BT-19); fila 1 del método de
tierras (4.3, con la cita del apartado 3.3 de la ITC-BT-18); aviso 1 de la medida de tierras (4.4,
quitado «el neutro de la distribuidora»); aviso 2 (4.4, con la cita del apartado 12); el párrafo del
valor admisible (4.1, rehecho sobre la ITC-BT-18, 9, y la ITC-BT-24, 4.1.2, con «300 mA» en cifra);
la frase del histórico de `teitse/09` §6 y la del aislamiento de devanados de §7 (5.6).

## Preguntas tipo test (10, contestadas sólo con el tema)

1. Según el Real Decreto 614/2001, las mediciones en una instalación de baja tensión pueden
   realizarlas: a) cualquier trabajador con formación básica; b) **trabajadores autorizados**;
   c) sólo trabajadores cualificados; d) sólo una empresa instaladora habilitada. → b. Tema 1.1
   (anexo IV, A.1). Entera.
2. (Analizador de redes) En el cuadro de una sala de equipos, el analizador da cos φ = 0,98 y
   factor de potencia = 0,80. Ampliar la batería de condensadores: a) lo corrige hasta 1; b) **no lo
   corrige: la diferencia se debe a la corriente deformada (armónicos), y los condensadores
   corrigen el desfase, no la deformación**; c) lo corrige si se instala junto a la carga; d) no hace
   falta, porque cos φ y factor de potencia son siempre iguales. → b. Tema 6.2 (y tema 1, 6.1).
   Entera.
3. Para medir en el cuadro general de un edificio, junto al origen de la instalación, el multímetro
   debe ser, según la clasificación de la IEC 61010 que recoge el fabricante: a) CAT I; b) CAT II;
   c) CAT III de 1000 V es siempre suficiente; d) **CAT IV**. → d. Tema 1.4. Entera.
4. Un polímetro de valor medio rectificado mide la corriente de un circuito de fuentes conmutadas:
   a) lee bien porque la red es de 50 Hz; b) **la lectura es falsa por defecto; hace falta un
   instrumento de verdadero valor eficaz**; c) lee de más; d) sólo falla en continua. → b. Tema
   2.3. Entera.
5. (Práctica) Para medir la corriente de descarga de la batería de un SAI sin abrir el circuito
   se usa una pinza: a) de transformador de corriente; b) **de efecto Hall**; c) de fugas; d) de
   tierra. → b. Tema 3.2. Entera.
6. (Práctica) Con la pinza de fugas abrazando juntos fase y neutro de un circuito en servicio se
   leen 22 mA, y el circuito está protegido por un diferencial de 30 mA que salta a veces al
   conectar equipos. Lo correcto es: a) cambiar el diferencial por uno de 300 mA; b) **hay una
   corriente de fuga cercana a la sensibilidad; se baja por el circuito midiendo cada derivación y,
   si son fugas legítimas de fuentes conmutadas, se reparten los equipos en más circuitos**; c) la
   pinza está mal porque debe dar la suma de las dos corrientes; d) medir con el megóhmetro en
   tensión. → b. Tema 3.3 (e ITC-BT-19, 2.9). Entera.
7. En un esquema TT con diferencial de 300 mA y tensión de contacto límite de 50 V, la resistencia
   máxima RA es aproximadamente: a) 1.667 Ω; b) 800 Ω; c) **167 Ω**; d) 37 Ω. → c. Tema 4.1
   (ITC-BT-24, 4.1.2). Entera.
8. Según la ITC-BT-18, la comprobación de la puesta a tierra por personal técnicamente competente
   se hace: a) cada cinco años; b) **al menos anualmente, en la época en que el terreno esté más
   seco**; c) sólo al dar de alta la instalación; d) cada diez años. → b. Tema 4.4. Entera. (Y la
   regla de los cinco años para poner al descubierto los electrodos.)
9. En una instalación de 230/400 V de menos de 100 m, con circuitos de equipos electrónicos, la
   medida de aislamiento: a) 250 V c.c., ≥ 0,25 MΩ, receptores siempre desconectados; b) **500 V
   c.c., ≥ 0,5 MΩ, con fases y neutro de los circuitos electrónicos unidos entre sí durante la
   medida**; c) 1000 V c.a. durante un minuto; d) 2U + 1000 V en continua. → b. Tema 5.1 y 5.3.
   Entera. (La c/d confunden con la rigidez, 5.5.)
10. (Termografía) Un técnico hace la termografía de un cuadro con la puerta de cristal cerrada y la
   sala parada por la noche. La inspección: a) es válida si ajusta bien la emisividad; b) **no vale:
   sin carga no hay punto caliente, y el cristal refleja la radiación térmica como un espejo**;
   c) es válida si la cámara tiene 640 x 480 píxeles; d) sólo falla en metales oxidados. → b. Tema
   1.3, 7.2 y 7.3. Entera.

Cobertura de las rúbricas: general y seguridad de la medida (1, 3), multímetro (4), pinza (5, 6),
telurómetro (7, 8), medidor de aislamiento (9), analizador de redes (2), termografía (10); teoría
(1, 3, 4, 7, 8, 9) y aplicación práctica (2, 5, 6, 10). Se comprobó además, fuera de las diez: «¿Qué
resolución exige la ITC-BT-03 al medidor de fugas? → mejor o igual que 1 mA» (1.2 y 3.3, entera) y
«¿Qué separa el analizador de la empresa básica del de la especialista?» (6.1, entera). Ninguna
pregunta obligó a ampliar el tema.
