# Productor/a (puesto 32) · Tema 12 · Fase 5, rematar

Tema: `temas/canal-sur-especificos/32-productor-a/12-gestion-documental-y-trazabilidad.md`.
Entrada: `32-T12-refutacion.md` (4 hallazgos menores, 4 lagunas) y `32-T12-preguntas.md`.
«Hoy» del encargo: 24-09-2026. Fuentes releídas el 25-09-2026 (ningún precepto citado cambió entre
ambas fechas).

Ficheros tocados: el tema 12 y este informe. `indice.py` se corrió una vez sin argumentos (sobre
todos los temas del `.tsv`) por error y otra sobre el tema 12; fuera de la carpeta del puesto 32 no
cambió nada (`git status`); los cambios que `git` muestra en los temas 01-11 y 13-15 del puesto 32
son de otros agentes, no de este remate.

**Amplía contenido nuevo: sí** (cuatro lagunas con norma). Procede la fase 5 bis sobre los pasajes
3, 5, 6, 7 y 8.

## Fuentes releídas

| Fuente | Precepto | Fecha de lectura | Resultado |
|---|---|---|---|
| Ley 7/2011 (BOE-A-2011-18654), `boe.py precepto` | 11, 18, 31, 38, 43, 71 | 25-09-2026 | Una redacción, salvo el 31 (dos: la vigente es de la DF 3.1 de la Ley 1/2014, vigencia 30-06-2015) |
| LCSP (BOE-A-2017-12902), volcado local del 25-09-2026 | 37, 120.1, 335 | 25-09-2026 | Una redacción (desde 09-03-2018) |
| Libro de estilo de Canal Sur TV (2004), `libro-de-estilo-333233b.txt`, l. 2713-2718 | 4.4.4, punto 6 | 25-09-2026 | Confirma la salvedad |

## Correcciones de la refutación

| Nº | Propuesta | Comprobación en la fuente | Aplicada |
|---|---|---|---|
| 1 | Salvedad del 4.4.4.6 | Correcta: la fuente abre con «En la medida de lo posible, las propuestas e intercambios…» | Sí |
| 2 | Añadir «la nulidad» al 335.2 | Correcta | Sí, con la enumeración literal completa |
| 3 | «registros externos» | Correcta: el perfil de contratante y el portal no son registros | Sí |
| 4 | Extensión 12.700 | `indice.py` mide ahora 13.695 | Sí: «13.700» |

Matiz a la refutación: su laguna 2 y la pregunta 5 nombran la «Comisión Andaluza de Valoración y
Acceso a los Documentos» para el 31.3.a. Desde el 30-06-2015 el artículo 31 la llama **«Comisión
Andaluza de Valoración de Documentos»**; los artículos 38.2 y 43.5 conservan el nombre antiguo. El
tema da ahora los dos nombres y explica por qué. La pregunta no se toca: su opción correcta sigue
siendo identificable.

## Pasajes cambiados

1. **«Quién lleva los papeles»**: la cita del 4.4.4, punto 6, se da entera desde «En la medida de lo
   posible, las propuestas e intercambios de información entre periodistas, técnicos y
   productores…», presentada como extensión de la regla del 4.4 a todo intercambio.
2. **«Dónde queda constancia pública del contrato»**, entrada: «Hay cuatro sitios fuera de la casa
   donde queda constancia de él:».
3. **Mismo epígrafe, punto 4 (335.2)**: «las modificaciones, prórrogas o variaciones de plazos, las
   variaciones de precio y el importe final, la nulidad y la extinción normal o anormal».
4. **Ficha**: Extensión 13.700; en «Fuente», LCSP con los artículos 37 y 120.
5. **«Los documentos de la RTVA son documentos públicos»**, viñeta nueva «Eliminación»: art. 31.3.a
   y 31.3.c (literal), nombre vigente y anterior de la Comisión, art. 71.b (literal, con su
   remisión al 18) y la aplicación al cierre de un programa (pregunta 13).
6. **«El ciclo de vida»**, tras la tabla: arts. 38.2, 38.4, 43.3 y 43.5 (literales) y la nota sobre
   el nombre de la Comisión (preguntas 4 y 13).
7. **«Qué hace que un documento sirva de prueba»**: art. 11.1 literal, requisito de validez
   (pregunta 6).
8. **«Cuándo existe el contrato»**, párrafo inicial: art. 37.1 literal y los supuestos del 120.1
   (literal); «Sobre esa base, dos preceptos…» enlaza con lo que seguía (pregunta 9).
9. **«Normativa que el tema invoca»**: Ley 7/2011 con 11.1, 31.3.a y c, 38.2 y 4, 43.3 y 5, 71.b;
   LCSP con 37.1 y 120.1.
10. **«Lo que este tema no da»**: se quita «qué plazos de conservación tiene fijados» del «no consta
    publicado» y se sustituye por una viñeta: no se ha localizado si la Comisión (31.3.c) ha dictado
    plazos para las series de producción de la RTVA; en su defecto, el 38.2.
11. **«Trazabilidad»**: filas de la Ley 7/2011 y de la LCSP ampliadas.

Relectura de antecedentes: «esa letra», «ese procedimiento», «esos plazos», «esa base» y «la misma
ley» tienen su antecedente inmediato; la remisión «véase "Los documentos de la RTVA son documentos
públicos"» apunta a un epígrafe anterior que existe.

## Lentes (sobre el tema entero; fuentes: Ley 7/2011, LCSP, Libro de estilo)

- `negritas.py`: ninguna de las negritas nuevas falla, salvo la del punto 6 del Libro de estilo,
  por las ligaduras «ﬂ» y «ﬁ» del `.txt` («ﬂuidez», «ﬁnal»); cotejada a ojo, literal. Los siete
  «¿ART. 28?» son falsos positivos previos (el 116 cita el 28). Los «NO ESTÁ» restantes son citas de
  fuentes que no se pasaron (convenio, Cámara, Ley 39/2015, etc.), ya verificadas.
- `refutar_exactitud.py`: nada en los pasajes nuevos; las 36 «no literales» son de normas no pasadas.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 1, previo («TAS», que es parte del nombre de la Orden, no una sigla).
- `indice.py`: índice regenerado; 13.695 palabras, 50 epígrafes.

## Preguntas tras el remate

Las 15 quedan enteras con el tema: 4 (38.2 y 43.3), 5 (31.3.a y 71.b), 6 (11.1), 9 (37.1) y 13
(31.3.a y 71.b) pasan de «no» o «a medias» a «entera».
