# Verificación · Oficial Técnico Electricista (27) · Tema 8 · Instalaciones eléctricas en centros audiovisuales, CPD, centros emisores y UM

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/08-instalaciones-electricas-en-centros-audiovisuales-cpd-emisores-y-um.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguna fuente usada cambia entre las dos fechas: la última redacción aplicada, la del
art. 3 del RD 186/2016, rige desde el 30-05-2026).

Ficheros tocados: el tema y este informe. Copia previa del tema en el scratchpad
(`v27t08/t08-antes.md`). Aviso: al empezar copié también el tema a `scratchpad/t08-antes.md`, y ese
nombre pudo pisar una copia previa de otro tema 8 que hubiera allí. No afecta a ningún fichero del
repositorio.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| ITC-BT-18 (`ib-18`, redacción RD 560/2010, BOE-A-2010-8190, vigente desde 23-05-2010) | `boe.py precepto`, apdos. 5, 6, 7, 10, 11 | Literal. En el 11 faltaba la salvedad de la unión de tierras (hallazgo 6) |
| ITC-BT-19 (redacción única) | apdos. 2.2.2, 2.4, 2.5 | Literal («debidas cargas», así en el BOE). Faltaba la salvedad de las instalaciones industriales en 2.2.2 (hallazgo 7) |
| ITC-BT-20 | apdos. 2.1, 2.1.1 | Literal; mal agrupada «calefacción» con los 3 cm (hallazgo 9) |
| ITC-BT-23 | entera | Literal; faltaban dos salvedades (hallazgo 5) |
| ITC-BT-28 | apdos. 1, 2, 4, 5 | Literal; faltaba BD2-BD4 (hallazgo 3) |
| ITC-BT-34 (apdo. 1), ITC-BT-29 (título), ITC-BT-40 (definición de aisladas) | `boe.py precepto` | Bien |
| ITC-BT-44, apdo. 3.1 | `boe.py precepto` | Literal; faltaba la salvedad del coeficiente (hallazgo 4) |
| RD 186/2016: arts. 1, 2 (vig. 25-06-2024), 3 (vig. 30-05-2026), 4, 6, 7, 18, 19, anexo I | `boe.py precepto` | Todo literal y bien atribuido; dos retoques (hallazgos 11 y 12) |
| Ley 21/1992, art. 8 (vig. 24-12-2014, BOE-A-2014-13359) | `boe.py precepto` | Nueva: respalda «norma voluntaria» (hallazgo 8) |
| CTE, parte I, art. 12 (vig. 12-03-2010, BOE-A-2010-4056) | `boe.py precepto` | Nueva: respalda el nombre del DB SUA 8 (hallazgo 10) |
| Ficha AENOR UNE-EN 50600-2-2:2019 | descargada | Título, «En Vigor», 2019-07-01, anula la de 2014, idéntica a EN 50600-2-2:2019: confirmado |
| TÜV NORD, *Whitepaper_EN-50600-171025.pdf* | descargado, `documento.py texto` | Las ocho citas en inglés, literales; la n+1 de la AC3 está en la lista de la 2-2 «Current Version released 2019» |

Cruces internos comprobados en el tema 7: 2.4 (inversor limita la corriente; rectificador
antiguo), 3.1, 3.3, 3.4 y 4.5 existen y dicen lo que se les atribuye.

Lentes: `negritas.py` (106 cotejadas; 3 «no están»: dos rótulos y la cita de TÜV «business» partida
por un guion blando en el PDF; 4 «atribuidas a otro artículo», falsos positivos, todas en el
art. 2 o 19 que nombra el tema), `refutar_exactitud.py` (8 «no literales», falsos positivos: la lente
casa el número de artículo más cercano, y las ocho están comprobadas a mano en su precepto),
`refutar_modo.py` (0), `refutar_prosa.py` (1: «CPD» en el título, se deja igual que en los temas 6
y 7), `indice.py` (10.879 palabras, 50 epígrafes, índice sin cambios).

## Copiado del común

Nada (así lo declara la redacción).

## Copiado de RTVE sin cambios

Comprobado sólo que es literal con un guion que normaliza el texto (sin negritas, sin acentos, sin
puntuación) y busca cada pasaje en `teitse/07`, `teitse/08`, `teitse/12`, `tese/15` y `tese/17`:
los 20 pasajes y filas listados están en RTVE. No se han re-verificado. Lo adaptado (resto de la
tabla de 1.1 y su regla 2, tabla de locales de 1.2, párrafo de la autonomía de 4.2, fila 5P, fila
«crujido», regla de diagnóstico) sí se ha verificado: la tabla de locales, contra la ITC-BT-28, 29 y
34; lo demás va como oficio y así está declarado.

## Hallazgos y correcciones

1. **Error 9** · 1.2: «La cláusula general… es la que más se pregunta». No hay exámenes anteriores. Quitado.
2. **Error 9** · 2.1: «la más preguntable de todas»; y 9.2: «La diferencia que más se pregunta»
   y «(mantenimiento concurrente)», un término que no está en la fuente. Quitados.
3. **Error 6** · 1.2: la cláusula general de la ITC-BT-28 incluye también los locales **BD2, BD3 y BD4,
   según la norma UNE 20.460-3**. Añadido.
4. **Error 6** · 2.2: la ITC-BT-44, 3.1, admite **un coeficiente diferente** del 1,8 si el factor de
   potencia es mayor o igual a 0,9 y se conocen las cargas asociadas. Añadido.
5. **Error 6** · 6.1: faltaba que una línea aérea con conductores aislados y pantalla unida a tierra
   en los dos extremos **se considera equivalente a una línea subterránea** (ITC-BT-23, 3.1), y la
   frase final del 3.2 sobre la conexión de descargadores («**No obstante se permiten otras formas de
   conexión…**»). Añadidas.
6. **Error 6** · 6.2: el apdo. 11 de la ITC-BT-18 permite unir la tierra del edificio y la de
   protección del CT si **Vd = Id * Rt** queda por debajo de la tensión de contacto. Añadido.
7. **Error 6** · 6.2: el 4,5 % y el 6,5 % de la ITC-BT-19, 2.2.2, son **Para instalaciones industriales
   que se alimenten directamente en alta tensión mediante un transformador de distribución propio**.
   Además, «3 % y 5 % de una instalación alimentada en BT desde la red pública» no es lo que dice el
   BOE (3 %/5 % para instalaciones que no son viviendas; 3 % en viviendas). Reescrito, con la lectura
   de aplicación declarada.
8. **Error 9** · 4.1: «norma voluntaria» no tenía fuente. Apoyado en la Ley 21/1992, art. 8.3
   (**cuya observancia no es obligatoria**). Añadido a la ficha, «Normativa» y «Trazabilidad».
9. **Error 9** · 10.4: «calefacción» estaba entre los ejemplos de los 3 cm. La ITC-BT-20, 2.1.1, trata
   aparte los conductos de calefacción, aire caliente, vapor o humo (**distancia conveniente o…
   pantallas calorífugas**). Corregido.
10. **Error 9** · 6.1: el DB SUA 8 se nombraba sin fuente. Confirmado en el CTE, parte I, art. 12.8
    (**Seguridad frente al riesgo causado por la acción del rayo**). Añadido a la ficha, «Normativa» y
    «Trazabilidad».
11. **Error 5/9** · siglas: «Asociación Española de Normalización (AENOR…)» hacía de AENOR la sigla
    de la Asociación. La ficha dice «Tienda AENOR» y «Ratificada por la Asociación Española de
    Normalización». Reescrito.
12. **Error 6** · 11.3: el art. 19.1 añade que esa documentación **incluirá la información mencionada
    en el artículo 7.5 y 6 y en el artículo 9.3**. Añadido. En 11.2, «llevan» se cambia por el literal
    del art. 18.2, **irán acompañados de**.
13. Ficha: la fuente del RD 186/2016 no nombraba los arts. 6 y 7.2, que el tema cita. Completada.

Se han releído todos los pasajes cambiados. Cada «el mismo apartado», «la misma instrucción» y «esa
documentación» tiene su antecedente inmediatamente antes (apdo. 11, ITC-BT-44, apdo. 2.1.1 y
art. 19.1).

Sin hallazgo, comprobado: definiciones del art. 3.1 a), c), d), e), f) y h); art. 3.2 (instalaciones
móviles); arts. 1, 2.1, 2.2.a, 2.3, 4, 6, 7.2, 18.1 y 19.1-19.3; anexo I.1 y I.2; los modos
(«deberán», «podrán», «impondrán»); ITC-BT-28, 4.a-d, f, g y 5.a-d, f; las categorías de
conmutación; la tabla 1 de la ITC-BT-23 (6/4/2,5/1,5 kV); ITC-BT-18, 5, 6, 7 y 10; ITC-BT-19, 2.4 y
2.5; las fechas de redacción de la ficha.

Queda como física de circuitos sin fuente leída (lo señaló el redactor): la suma de los armónicos
múltiplos de tres en el neutro (10.2). Va declarada como tal y la respalda la cita literal de la
ITC-BT-19, 2.2.2. No se ha quitado.
