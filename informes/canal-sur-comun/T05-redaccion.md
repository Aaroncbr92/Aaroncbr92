# T05 · Redacción · Ley 18/2007 (RTVA)

Tema: `temas/canal-sur-comun/05-ley-18-2007-rtva.md` (14.959 palabras de cuerpo). Punto 5 del
temario común de Canal Sur; enunciado comprobado literal en
`convocatoria/canal-sur/PROGRAMA-COMUN.md`. Fase 2 (redactar), un solo agente, escrito por
partes y guardado sección a sección. **Fecha de trabajo y de lectura de todos los preceptos:
24-09-2026.**

## Material y fuentes

- Investigación: `T05-investigacion-ley-organos.md` y `T05-investigacion-csrtv-control.md`,
  leídos enteros.
- Ley 18/2007: volcado `fuentes/canal-sur/BOE-A-2008-1185.md` leído entero (todos los bloques)
  y su `.redacciones.tsv`. Redacciones anteriores sacadas con `boe.py --fecha` (20100101,
  20140101, 20190601, 20200101) para exposición de motivos y arts. 8, 14, 15, 18 y 20.
  Metadatos y «posteriores» leídos en la API del BOE: publicación BOE núm. 20 de 23-01-2008,
  BOJA núm. 252 de 26-12-2007, vigencia 15-01-2008, tres modificadoras (DL 3/2013 de 19 de
  marzo, Ley 2/2019 de 26 de junio, DL 5/2024 de 21 de mayo).
- Título de la Ley 2/2019 comprobado con `boe_buscar.py`. Convalidación del DL 5/2024
  comprobada en el sumario del BOJA núm. 111/2024 (Resolución de 4-06-2024).
- Estatuto `BOE-A-2007-5825` (arts. 69, 130, 131, 194, 207-217 y rótulos de los títulos VII y
  VIII); título de la LO 2/2007 comprobado en la API. Ley 9/2007 `BOE-A-2007-19819` (54, 68,
  75-77, sección de órganos colegiados = arts. 88-96). TRLGHP `BOE-A-2010-5303` (DA única del
  DLeg, 5.1, 97.1, 98.1). Ley 1/2004 `BOE-A-2005-655` (1, 2, 4, 11, 13). Ley 1/1988
  `BOE-A-1988-8592` (1, 2, 4). Ley 7/2025 `BOE-A-2026-944` (DD única, letra a; título).
- Documentos: Acuerdo de fusión (BOJA 219/2015) leído entero; Reglamento del Parlamento
  consolidado (arts. 46, 188-190 y rótulo del título XIV); Contrato-Programa 2024-2026 (BOJA
  245/2023), sólo el expositivo IV, para confirmar la sociedad única.

## Estructura

Ficha, siglas, enunciado, párrafo de qué se pregunta, índice vacío; `## Identificación de la
ley` (naturaleza, estructura, reformas, remisiones desfasadas); y un `##` por rúbrica en el
orden del enunciado: régimen jurídico básico de CSRTV (RTVA, art. 9, fusión 2015, desajuste con
el art. 9, régimen de sociedad del sector público andaluz, arts. 21-27, arts. 10-12); misión de
servicio público (arts. 1-4 completos, Estatuto, arts. 7-8, arts. 28-34 y DA/DT); organización
(art. 13, quién elige/nombra, mandatos, composición equilibrada, puesta en marcha, organización
de CSRTV); órganos de gobierno (Consejo de Administración, Dirección General, Consejo Asesor,
con composición, elección, mandato, cese, funciones, funcionamiento y redacciones anteriores);
control parlamentario (Estatuto 214, art. 35, Reglamento, cuadro de intervenciones del
Parlamento, y resto del control externo: CAA, Tribunal y Cámara de Cuentas, auditoría).
Cierra con normativa, lo que no da y trazabilidad.

## Puntos abiertos: declarados, no resueltos

1. Art. 9 (dos sociedades) frente a la fusión de 2015 (una, CSRTV): dicho tal cual, con 10.2
   y DA 2.ª. El título del Acuerdo se lee al revés; se da la parte dispositiva (absorbente
   Canal Sur Televisión). Fecha de inscripción y modificaciones posteriores de los estatutos:
   no constan; se dice.
2. «Título VII» de la exposición de motivos frente al Título VIII del Estatuto: dicho como
   desajuste, sin corregir.
3. Art. 4 de la Ley 1/2004 «(Anulado)»: se cita la nota del BOE y la «Redacción anterior»
   (función 14) sin afirmar que rija; no se dan números de función como dato.
4. Remisiones a la Ley 5/1983, a su «artículo 87» (hoy 98.1 TRLGHP, correspondencia por
   contenido, declarada como tal) y a la Ley 4/1986 (derogada por Ley 7/2025).
5. «Voz y voto» de la Dirección General en el Consejo (19.4): no se interpreta.
6. Tipo de agencia pública empresarial (68.1 Ley 9/2007): ninguna fuente lo dice; se dice.
7. Fórmulas de mandato distintas (15.3, 18.2, 20.3-20.4): tabla con cada una literal.
8. Paridad (14.1) no definida; composición equilibrada (DA 3.ª) sí: dicho así.

Las normas internas del Parlamento que citan las notas del Reglamento (2009, 2010, 2013) sólo
se nombran; su contenido no se ha leído.

## Decisiones de forma

- Negrita sólo en citas literales (y en las etiquetas de la ficha, que fija la forma de la
  casa). Las siglas se presentan en redonda, no en negrita como en los temas 4 y 9, para
  cumplir la regla del encargo de este tema.
- El título del tema usa el nombre completo de la RTVA para no estrenar la sigla antes de
  presentarla.
- Índice vacío entre sus marcas; «Extensión» medida con `tema.cuerpo`.

## Comprobaciones

- Script propio (scratchpad, `t05/neg5.py`): cada tramo en negrita, normalizados los
  espacios, buscado como subcadena en el corpus de fuentes (volcados `BOE-A-*`, documentos,
  programa y redacciones anteriores). **226 negritas, 0 no encontradas.**
- `refutar_prosa.py`: 3 avisos. «Redacción anterior (hasta el 27 de junio de 2019)» repetida
  x3: rótulo intencionado en cada órgano. «LGBTI»: parte del nombre oficial del Consejo
  Andaluz LGBTI (art. 20.1.e), no sigla del tema. «RTVA» en el título: corregido.
- `refutar_citas.py`: 0 tramos (el tema no usa bloques de cita `> ` salvo el enunciado).
  `refutar_exactitud.py`: 0 negritas comprobadas, porque ancla en marcadores «**Artículo N**»
  que este tema no usa. Los ceros no significan que miraran: la comprobación real es la del
  script propio y la lectura precepto a precepto. El verificador debe tenerlo en cuenta.

## Ficheros tocados

- `temas/canal-sur-comun/05-ley-18-2007-rtva.md` (nuevo).
- Este informe.
- `fuentes/canal-sur/BOE-A-2026-944.md` y `.redacciones.tsv`: volcado de la Ley 7/2025 con
  `boe.py norma` (identificador comprobado por su título) para la derogación de la Ley 4/1986.
- Ejecuté por error `herramientas/indice.py` sin argumentos: falló en la primera ruta
  (`temas/general/01-…`) antes de escribir; `git status` limpio después, nada modificado.
- Temporales en el scratchpad, en `t05/` (el scratchpad lo comparten otros agentes: uno
  sobrescribió un `negritas.py` que había dejado en la raíz).
