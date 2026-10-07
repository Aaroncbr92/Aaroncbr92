# 04 · Ayudante de Producción · Tema 9 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/09-medios-materiales-de-produccion.md`
(11.627 palabras según `wc` tras la verificación; epígrafes sin cambios, índice no regenerado).
Verificado el 06-10-2026 (el encargo fija «hoy» en 24-09-2026; 06-10-2026 es la fecha de lectura
de cada fuente).

Ficheros tocados: el tema y este informe. Ninguno más.

## Lo copiado: sólo comprobación de literalidad

Script de cotejo por frases y celdas de tabla (sin negritas, espacios normalizados) del tema contra
Productor T6, Productor T12, RTVE `produccion/10` y `produccion/08`.

- **Copiado del común** (Productor T6 y T12): todo lo listado aparece literal. Lo que no casa son
  sólo los cambios declarados («tema 10» → «tema 8» en «Cómo se prevé un medio», remisión final al
  tema 11, párrafo nuevo de UC0208_3, frase nueva del reparto) y un falso negativo del script en la
  cita en bloque de la Cámara (comprobada con `diff`: idéntica). No se ha vuelto a verificar.
- **Copiado de RTVE sin cambios** (`10` §§1-5, `08` §7): literal. No se ha vuelto a verificar.
- **Adaptado de RTVE**: cotejado. Las diferencias son las declaradas (quitadas las remisiones a
  temas 9, 3, 14 y 1 de RTVE). Son oficio, declarado como tal en el tema y en «Trazabilidad».

## Lo nuevo y lo adaptado: verificado en la fuente

| Fuente (leída el 06-10-2026) | Cómo | Resultado |
|---|---|---|
| X Convenio, anexo III: fichas de Ayudante de producción (5212705), Productor/a, Auxiliar de servicios generales, Mozo, J. Dpto. Servicios Generales, J. Sec. Compras, J. Sec. Patrimonio, J. Dpto. Compras y Patrimonio, J. Sec. Gestión administrativa de TV, Ayudante técnico electrónico, Jefe de baja frecuencia, Eléctrico de iluminación, Estilista, Sastra, Decorador, Ayudante de decoración, Operador de sonido de radio, Ayudante de unidades móviles, Conductor polivalente UM | Script que extrae cada ficha por denominación (`x-convenio-rtva-boja-240-2014.txt`) | Cada cita está en la ficha a la que se atribuye; los códigos coinciden. Dos salvedades omitidas (abajo) |
| X Convenio, campos de dirección y departamento | Script sobre las 114 fichas | Todos en blanco: confirmado |
| X Convenio, maquillaje/peluquería/caracterización | grep | Ninguna aparición: confirmado |
| X Convenio, arts. 65, 66 y 67 | lectura de los tres artículos | 65.6, 66.8 y 67.3 literales; una remisión mal hecha (abajo) |
| *Libro de estilo*, 4.4 (l. 2597-2620) y 5.6 (l. 2988-2999); 1.ª ed., marzo de 2004 | lectura | Literales (la ligadura «ﬁ» del .txt explica el «no está» de `negritas.py`) |
| Ley 31/1995, art. 29 | volcado BOE y `.redacciones.tsv` (una redacción, desde 10-02-1996) | 29.2.1.º y 29.3 literales |
| RD 1681/2011, anexo I: 0915 RA 2.c, 2.d, 2.g, 2.h, 3.b, 3.c; 0916 RA 2.a, 2.b, 2.h, 5.f; 0919 RA 1.c, 1.e-1.h y contenidos (l. 712); ocupaciones (l. 77-84) | lectura de cada criterio en su módulo y RA | Literales y bien atribuidos |
| RD 500/2024 (`fuentes/canal-sur/realizador/BOE-A-2024-10685.txt`), arts. primero.Dos.a) (41.º) y séptimo.Uno; anexo XLII | lectura | Ver corrección 1: el tema afirmaba algo erróneo |
| IMS074_3: UC0207_3 CR1.2, CR1.3; UC0208_3 CR2.1-2.4, CR3.3-3.5, CR4.2; UC0209_3 CR1.3, CR2.2, CR2.3; MF0208_3 CE2.7 (l. 920) y contenidos (l. 1106); ocupaciones; cabecera «Orden PCI/797/2019», UC en «Tramitación BOE» | lectura | Literales y bien atribuidos |
| Remisiones a los temas 3, 4, 5, 6, 7, 8, 11, 12, 14 y 17 del puesto | grep | Cada tema trata lo que se le remite (el 17 desarrolla la manipulación manual de cargas y el art. 17 LPRL) |

Cámara de Cuentas y Contrato-programa: sólo en pasajes copiados del común. No se han vuelto a verificar.

## Correcciones aplicadas

1. **Error 7/9 (afirmación falsa sobre la redacción).** El tema decía que el RD 500/2024 modificó
   el RD 1681/2011 «en otros puntos» y que no podía comprobarse si alteró los criterios citados. El
   RD 500/2024 sí modifica el anexo I (art. séptimo.Uno, aplicable al 1681/2011 por el art.
   primero.Dos.a, 41.º), pero sólo para suprimir FOL, EIE y FCT, incluir cinco módulos nuevos y
   renombrar «Proyecto» como «Proyecto intermodular». Los módulos 0915, 0916 y 0919 no cambian, así
   que los criterios citados siguen vigentes. Corregidos la portada («Redacción»), la fila de
   «Normativa» y la de «Trazabilidad». Quitada la entrada de «Lo que este tema no da», que ya no es
   un hueco.
2. **Error 1/8 (remisión mal hecha).** Supuesto 3: «el convenio la califica según su gravedad
   (artículos 65.6, 66 y 67.3)». El 66.8 que da el tema trata del uso propio sin autorización, no de
   la pérdida. Ahora se dice: leve, el pequeño descuido (65.6); muy grave, hacer desaparecer o dañar
   voluntaria o negligentemente con grave perjuicio (67.3).
3. **Error 9 (afirmación que la fuente no sostiene).** «El régimen disciplinario la gradúa en tres
   escalones» (la conservación): la falta grave 66.8 no es de conservación, sino de uso. Ahora dice
   «La conservación y el uso del material… una falta de cada grado sobre el material». Ajustado en
   el mismo sentido «Qué se puede preguntar».
4. **Error 6 (salvedad omitida).** «Las pólizas sobre el inmovilizado las gestiona el J. Sec.
   Patrimonio»: la ficha del J. Dpto. Compras y Patrimonio incluye **«Elaborar condiciones de
   pólizas de Seguros sobre activos fijos y responsabilidad civil y supervisar la gestión de las
   mismas.»** Añadida.
5. **Error 6 (salvedad omitida).** «La compra de material corresponde a Compras»: la ficha del Mozo
   incluye **«comprar pequeño material»**. Añadido entre paréntesis.

Relectura de los pasajes cambiados: cada «ese», «la» y «esas pólizas» tiene delante su antecedente.

## Lentes

- `negritas.py` (convenio, Libro de estilo, LPRL, RD 1681/2011, IMS074_3, Cámara, contrato-programa):
  160 negritas, 15 «no están». Son los 13 rótulos propios del tema y las 2 del Libro de estilo por
  la ligadura (cotejadas a mano). Ninguna atribuida a otro artículo.
- `refutar_exactitud.py` y `refutar_modo.py` con la LPRL: 0 no literales, 0 hallazgos de modo o
  salvedad.
- `refutar_prosa.py`: sólo SSFF. Es un falso positivo: la sigla se presenta en las siglas de entrada.

## Sin cambios, por estar bien

Las 10 preguntas del informe de redacción siguen contestándose con el tema. La pregunta 10 (art.
65.6) no se ve afectada por la corrección 3.
