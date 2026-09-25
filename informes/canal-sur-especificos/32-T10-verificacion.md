# Productor/a (puesto 32) · Tema 10 · Fase 3, verificar

Tema: `temas/canal-sur-especificos/32-productor-a/10-contratacion-de-servicios-suministros-y-colaboraciones.md`.
Fecha de verificación y de lectura de todas las fuentes: 25-09-2026 (redacción que se estudia: la vigente
el 24-09-2026; ningún precepto citado cambia entre ambas fechas). Ficheros tocados: el tema y este informe.
Temporales en el scratchpad (volcados de la Ley 60/2003, arts. 9, 11 y 43, y de las redacciones vigentes de
los arts. 20, 21, 22, 29, 116, 118, 125, 159, 168, 215, 217 y 318 LCSP; copia del tema antes de corregir).

## Copiado del común: sólo literalidad

Comprobado con grep contra `temas/canal-sur-comun/05`, `06` y `07`: los tres pasajes listados en el informe
de redacción son literales (viñeta de los arts. 26 y 19.2.e de la Ley 18/2007; viñetas 23.2 y 24.3 de la
Carta; denominación del Reglamento de la Mesa de Contratación). No se re-verifican. «Copiado de RTVE sin
cambios»: ninguno declarado; todo lo de RTVE se ha verificado como el resto.

## Método

- Cada negrita (159) contra todas las fuentes con `negritas.py`; las 6 «no están» son 3 rótulos, el salto de
  página del Libro de Estilo (págs. 76-77, literal), la denominación del Reglamento (del común) y el 118.3
  original (leído con `boe.py --fecha 20190101`, literal). Las 4 «atribuidas a otro artículo» son falsos
  positivos (26.1.b en tabla; 318.b; 217.2; 11.3 Ley 60/2003 releído: «solicitar de un tribunal la
  adopción de medidas cautelares»).
- Cada precepto con varias redacciones, leído en la vigente con `boe.py precepto`: fechas de la portada
  confirmadas contra `BOE-A-2017-12902.redacciones.tsv` y la cadena de la Ley 60/2003. BOE-A-2020-1651
  confirmado como el Real Decreto-ley 3/2020 (disp. final primera, «Se da nueva redacción al artículo 118»).
- Todo lo que no es negrita (paráfrasis, números de artículo y apartado, cifras, recuentos, páginas) releído
  en su fuente: LCSP arts. 1, 3, 4, 9, 11, 16, 17, 19-22, 25-29, 62-64, 99-101, 116, 118, 120, 124-126, 131,
  132, 145, 159, 168, 210, 215, 217, 300, 311, 316-319, 326; convenio (art. 24, anexo III), Libro de Estilo
  4.4, contrato-programa (puntos 34 y 43), Cámara (puntos 27, 29-31, 40-45, cuadros 1 y 3, anexo 9.5).
- Recuentos: 8 tareas en la ficha (ocho, correcto); 188/192 = 97,92 %; 117/192 = 60,94 %; 71 contratos por
  22.153.964,71 euros; 24.000 euros de valor estimado en el ejemplo (correcto).

## Correcciones aplicadas (con el error del catálogo)

| # | Pasaje | Error | Qué dice la fuente | Cambio |
|---|---|---|---|---|
| 1 | Ficha del Ayudante de producción, «página 195» (texto y Trazabilidad) | 8 | La ficha está en la pág. 110 del BOJA 240/2014; la 195 es la de Programador | Página 110 |
| 2 | «Libro de Estilo de los Servicios Informativos (2004)» | 8 | Título: *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía* (1.ª ed., marzo 2004); 4.4 trata la producción en informativos | Título corregido |
| 3 | «el mismo apartado cita la contratación de bienes o servicios» | 1 | Está en la introducción del 4.4, no en el 4.4.4 que precede | «la introducción del apartado 4.4» |
| 4 | Tabla RTVA/CSRTV, excepciones del 319.1 | 3 y 6 | Omitía 218 a 228 (racionalización técnica); la modificación es 203 a 205 | Lista completa con artículos |
| 5 | Modificación «artículos 203 a 207, que en CSRTV también se aplican por el 319.1» | 8 | El 319.1 aplica los 203 a 205 | Corregido |
| 6 | 25.2 «supletoriamente, el derecho administrativo» | 6 | «…y, en su defecto, las normas de derecho privado» | Completado |
| 7 | 29.4, cinco años | 6 | El mismo apartado admite excepcionalmente duración mayor | Salvedad añadida |
| 8 | 29.2, preaviso «de al menos dos meses» | 6 | «salvo que en el pliego… se establezca uno mayor»; exceptuados los de duración inferior a dos meses | Salvedad añadida |
| 9 | 99.3, lotes «la regla» | 6 | «Siempre que la naturaleza o el objeto del contrato lo permitan» | Añadido |
| 10 | 99.6, «no lote a lote» | 6 | «salvo… artículos 20.2, 21.2 y 22.2» | Añadido |
| 11 | «Por encima de 216.000 euros, SARA (artículo 317)» | 9 | Umbral «igual o superior» (21.1.b, 22.1.b); el 317 regula preparación y adjudicación | Redactado así |
| 12 | 326.1, mesa de contratación en general | 6 | Sólo en abiertos, abierto simplificado, restringidos, diálogo, licitación con negociación e innovación | Salvedad añadida |
| 13 | 125.1 y la STC 68/2021, «no lo anula» | 9 (alcance) | La nota del BOE declara no conforme con el orden de competencias; su efecto para una entidad autonómica no se ha leído | Hueco declarado (texto y «Lo que no da») |
| 14 | 126.7, «una norma equivalente» | 9 | Norma nacional que transponga europea, internacional, etc., referida al rendimiento | Precisado |
| 15 | 215.2.a), «y a quién» | 9 | «el nombre o el perfil empresarial» | Precisado |
| 16 | 210.4, liquidación | 6 | «en su caso y cuando la naturaleza del contrato lo exija» | Añadido |
| 17 | Contenido de la factura dado como lista cerrada | 9 | La ley remite a normas de desarrollo (118.3), no leídas | Presentado como oficio con la remisión; hueco en «Lo que no da» |
| 18 | «Instrucción 1/2010 y otras de 2015 a 2019» | 9 | El anexo 9.5 de la Cámara lista instrucciones de 2015 a 2018 | 2015 a 2018 |
| 19 | Nota al cuadro nº 1 de la Cámara, cortada tras «principios generales» | 6 | Sigue: «ya sea de forma directa… o para el resto por la transposición… en las disposiciones e instrucciones internas» | Cita completada; se aclara que es de 2018 y qué es el TRLCSP (5) |
| 20 | Trazabilidad de la Cámara | 1 | Muestra de 71 contratos y cuadro 3 en el punto 45; instrucciones en el anexo 9.5 | Añadidos |

Extensión de la portada puesta al día (11.300 palabras). Releídos todos los pasajes cambiados: «el mismo
apartado» (29.4) y los demás antecedentes tienen su referente delante.

## Comprobado sin cambios (muestra de lo que más se presta a error)

Umbrales SARA 5.404.000 / 140.000 / 216.000 / 750.000 (vigentes desde 01-01-2026); contrato menor 15.000
y 40.000, «inferior a»; 29.8; 118.5 (5.000 euros, anticipo de caja fija); 63.4 y su excepción; 159.1 y 159.6
(60.000, salvo prestaciones intelectuales); 168.a).1.º, 2.º y b).1.º; 120 (un mes); 131.2 y 131.3; 318.a) y b);
215 (todos los apartados citados); 217.2 completo; 62.1-2; 210.1-3; 300.1-3; 311.1-5 y 7; 3.1.g-h, 3.2.b,
3.3.d; 9.2; 11 completo; 16.2-3; 19.2.a) y su remisión a la Directiva 2010/13/UE; 26.1.b y 26.2; 27.1-2;
Ley 60/2003, arts. 9.1, 9.3, 11.1, 11.3 y 43; convenio art. 24 (bolsas, acceso, contrataciones; provisión y
promoción en arts. 15 y 18); contrato-programa 34 y 43; Cámara puntos 27, 31, 41, 42, 44 y cuadro 3.

## Lentes (25-09-2026)

`negritas.py`: 159; sin hallazgos reales tras las correcciones. `refutar_modo.py`: 0. `refutar_exactitud.py`
(LCSP): 77 citas, 13 «no literales», todas de otra norma o de tabla; 0 errores. `indice.py`: 11.265 palabras,
40 epígrafes; índice intacto (el aviso «sin portada» es porque el tema no está aún en `portadas.tsv`).

## Avisos al coordinador

- El informe de redacción situaba la ficha del Ayudante de producción en la pág. 195: está en la 110 (manda
  la fuente).
- La STC 68/2021 declara no conforme con el orden de competencias el art. 125.1; si otros temas citan
  preceptos afectados (hay notas en los arts. 41, 46, 52, 58, 72, 82, 122, 154, 177, 185, 187, 212, 242 y
  347), conviene declarar su alcance para entidades autonómicas o leer la sentencia.
