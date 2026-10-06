# Puesto 29 · Tema 15 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/15-normativa-tecnica-de-administracion-electronica-e-interoperabilidad.md`.
Fecha de la verificación y de la lectura de todas las fuentes: 06-10-2026 (encargo fechado 24-09-2026). Las
tablas `.redacciones.tsv` y la cadena de `boe.py precepto` confirman que ninguna fuente cambió después del
02-04-2025: el texto es el mismo el 24-09-2026.

## Qué se ha hecho

- **Copiado del común** (2 pasajes): sólo comprobado con `grep` que son literales en
  `temas/canal-sur-comun/02-estatuto-autonomia-andalucia.md` (l. 1946-1948, art. 54.1 Ley 9/2007) y
  `05-ley-18-2007-rtva.md` (l. 360-363, Primero.3). Literales. El resumen sobre el art. 5 de la Ley 18/2007
  (agencia pública empresarial, personalidad jurídica propia) cuadra con el tema 5 del común (l. 252-258).
- **Copiado de RTVE sin cambios**: ninguno (la redacción lo declara). Lo adaptado de RTVE (8 pasajes) se ha
  verificado como el resto.
- Todo lo demás, releído en su fuente: Ley 39/2015 (arts. 2, 9, 10, 14, 16, 17, 26, 27, 43, 70, DDU), Ley
  40/2015 (arts. 2, 38-46, 155-158), RD 203/2021 (arts. 1, 2, 3, 5, 26, 27, 29, 37, 39, 47, 50, 51, 54, 55,
  60-62), ENI (arts. 1, 3, 4, 8-18, 20-29, DA 1.ª en sus cuatro redacciones, DA 2.ª, DT 1.ª y 2.ª, anexo), ENS
  (arts. 1-3, 5-13, 28, 31, 33-35, 38, 39, 41, DA 2.ª, DDU, anexos I y II), NTI de Documento electrónico,
  Digitalización, Expediente, Catálogo de estándares, Firma y sello 2016 y SICRES4.
- Relación de NTI publicadas: comprobada contra la API de legislación consolidada del BOE (búsqueda por título
  «Norma Técnica de Interoperabilidad», 06-10-2026): 14 resoluciones, 12 sin vigencia agotada; fechas y
  títulos coinciden con el cuadro. BOE-A-2024-22935 = Real Decreto 1125/2024, de 5 de noviembre (API de
  metadatos del BOE, 06-10-2026).
- Lentes: `negritas.py` (13 fuentes): 334 negritas, 0 no encontradas, 16 «atribuidas a otro artículo», todas
  falsos positivos por proximidad, revisadas una a una. `refutar_exactitud.py`: 145 citas, 20 «no
  literales» = los mismos falsos positivos y las citas del común. `refutar_modo.py`: 0. `refutar_prosa.py`:
  4 siglas (AAAA, BES, EPES, ID), explicadas en el tema por su contenido; se dejan. No se cambió ningún rótulo:
  el índice sigue valiendo.

## Correcciones aplicadas (con su error del catálogo)

1. **Error 7/9, DA 1.ª del ENI**: el tema decía que las letras m) a v) se añadieron «en 2021 y 2024». Con
   `boe.py --fecha`: la redacción de 2011 tenía a)-l); la de 02-04-2021 (RD 203/2021) ya trae m)-v) con la ñ;
   la de 07-11-2024 sólo cambia el ministerio del apartado 2 (diff de las dos redacciones). Corregido.
2. **Error 6, ministerios**: «las dos disposiciones reformadas en 2024 ya nombran al Ministerio para la
   Transformación Digital…»; cierto en el apartado 2, pero el apartado 3 de la DA 1.ª del ENI sigue nombrando
   al de Asuntos Económicos. Añadida la salvedad.
3. **Error 3, remisiones del ENI a la Ley 11/2007**: faltaban el art. 11.3.b y la DT 2.ª. Añadidos.
4. **Error 6, art. 46.1 Ley 40/2015**: omitía «salvo cuando no sea posible»; y el artículo habla de
   almacenar, no de «conservación». Corregido.
5. **Error 6, art. 18.1 ENI**: «la aplican obligatoriamente» sin la salvedad de no aplicación justificada y
   autorizada por la Secretaría General de Administración Digital. Añadida.
6. **Error 6, art. 9.2.c Ley 39/2015**: faltaba la previa comunicación a la Secretaría General de
   Administración Digital. Añadida.
7. **Error 6, art. 157.2 Ley 40/2015**: faltaba la condición para declarar fuentes abiertas. Añadida.
8. **Error 6, art. 13.5 ENS** (y caso práctico): el POC se designa «salvo por causa justificada y
   documentada». Añadido en los dos sitios.
9. **Error 6, NTI de expediente V.5**: la red preferente es para la actuación automatizada. Añadido.
10. **Error 9/6, NTI de firma**: IV.1.5 el periodo de precaución es facultativo («podrá establecer»);
    IV.3.2 el sello se aplica a las referencias, no a «todo»; II.5.3.d el formato XML/ASN.1 se exige a la
    política particular; «Por defecto, el perfil mínimo» → «El perfil mínimo». Corregidos.
11. **Error 9, Catálogo**: «XAdES, CAdES y PAdES (abiertos), XML-DSig y CMS (admitidos)» sugería una diferencia
    que no existe: los cinco son abiertos y «Admitido». Reescrita la fila. Añadido que el catálogo agrupa
    texto e imagen en una sola categoría («Imagen y/o texto»), lo que además respalda poner PDF/A entre los
    formatos de imagen del caso práctico.
12. **Error 9, art. 43.1 Ley 40/2015**: «fuera de esos casos» → «sin perjuicio de lo previsto en los
    artículos 38, 41 y 42», como dice la ley.
13. **Error 8 menor, art. 16.5 Ley 39/2015**: dice «presentados de manera presencial», no «en papel».
14. **Error 9, afirmaciones sobre examen**: no hay exámenes anteriores; quitados «que son lo primero que se
    pregunta», «una regla que se pregunta» (×2), «las que se preguntan», «la diferencia que se pregunta» y
    «la que más se aplica en la práctica».
15. **Ficha y normativa**: la ficha citaba como estudiado el art. 28 del Reglamento (no se usa): ahora sólo
    el 27. Quitado el art. 37 del Reglamento y el 40 del ENS de «Normativa que el tema invoca» (no se citan).
    Quitada la sigla PAGe, presentada y nunca usada.
16. **Trazabilidad**: añadidas al «oficio sin norma» las dos funciones clásicas del registro y la tríada
    clásica (adaptadas de RTVE, sin fuente normativa).
17. «Las dos normas cierran con la misma garantía» → «Los dos artículos» (9.2 y 10.2).

Releídos los pasajes cambiados: cada «la», «uno», «esa política» tiene su antecedente.

## Confirmado sin cambios (muestra de lo no trivial)

23 letras de la DA 1.ª (14 + ñ + 8); 9 metadatos mínimos del documento + 3 condicionales, ID de 30
caracteres; metadatos del expediente; 200 ppp; 15 requisitos del art. 12.6 y 7 principios del art. 5 del ENS;
categorías del anexo I 4.1; auditoría cada dos años, prórroga de tres meses, 31.6; 38.1; 33.2 y 33.7;
redacciones vigentes del cuadro «Normativa» (arts. 9 y 10 Ley 39 desde 30-06-2022, 155 Ley 40 desde
06-11-2019, art. 27 RD 203/2021 desde 02-04-2025, arts. 9, 11, 14, 16-18 y anexo del ENI desde 02-04-2021);
erratas «N11», «PMG», «BebM» y estado ausente de SHA; los dos pasajes de sustitución (firma 2016, SICRES4);
deducción RTVA/CSRTV presentada como deducción, no como dato.

## Ficheros tocados

- Editado: el tema 15 (41 líneas cambiadas; 16.184 palabras por `wc`).
- Creado: este informe. Copia previa del tema en el scratchpad (fuera del repositorio).
