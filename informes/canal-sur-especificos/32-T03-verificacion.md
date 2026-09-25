# Productor/a (puesto 32) · Tema 3 · Verificación

Fase 3. Tema: `temas/canal-sur-especificos/32-productor-a/03-plan-de-produccion.md`.
Fuentes releídas el 25-09-2026 («hoy» del encargo: 24-09-2026; las locales no cambian entre ambas
fechas). Ficheros tocados: el tema y este informe; en el scratchpad, fuera del repositorio, copia del
tema antes de verificar y el Libro de estilo normalizado NFKC.

## Lo copiado: sólo comprobación de literalidad

- «Copiado del común»: ninguno (según la redacción).
- «Copiado de RTVE sin cambios» (13 pasajes): cotejados por script, frase a frase y fila a fila de
  tabla, contra `realizacion/03`, `produccion-asistencia/06` y `produccion/01` sin negritas.
  **Todos literales.** Única frase no hallada, «Puestos en orden, los papeles de una producción se
  explican:», es la entrada de la tabla reescrita (el origen la tiene dentro del párrafo
  introductorio que la redacción dice haber quitado); conector, sin dato. No se re-verifican.
- Adaptado de RTVE (6 pasajes): cotejados con su origen; los cambios son los declarados (quitar
  «respuesta oficial», «por sus siglas inglesas», «las cuatro» → «todo el plan»). Son oficio y así
  van declarados en el tema. Correcto.

## Verificado en la fuente (correcto)

- Convenio (`x-convenio-rtva-boja-240-2014.txt`): ficha 5331000 Productor/a (pág. 194), objeto y 8
  tareas; ficha 5212705 Ayudante de producción: plan de producción, citaciones, archivo, seguimiento
  técnico y presupuestario. «Plan de producción» sólo aparece en esas dos fichas: el convenio no lo
  define (como dice el tema).
- Libro de estilo (Primera edición, marzo de 2004, © RTVA): 4.4 (tres citas), 4.4.1 Operatividad
  (tres), 4.4.2 Rendimiento (tres), 4.4.3 Economía (dos), 4.4.4 puntos 1, 2, 3, 4, 6, 7, 8, 9 y 10.
  Numeración y rótulos correctos.
- Contrato-programa (BOJA 245, 26-12-2023): 3.24 «Planificación estratégica», punto 127, dentro de la
  cláusula TERCERA; las cinco citas literales y son finalidades del punto.
- Cámara de Cuentas (BOJA 36, 23-02-2021): §155 (dos frases), recomendación 306 («En relación con la
  fiscalización operativa»), alegación nº 19 al punto 46 (págs. 291-292), lista de documentos y del
  «Plan de Trabajo inicial»; RPA = Registro de Programas Audiovisuales (abreviaturas del informe).
- Revista AENOR núm. 352, octubre 2019 (WebFetch 25-09-2026): definición de riesgo, pasos (alcance,
  contexto y criterios; identificación; análisis y evaluación; tratamiento; comunicación y consulta,
  seguimiento y revisión transversales). Tabla del tema correcta.
- Remisiones a otros temas (modalidades de la Carta en tema 1; preferencia por lo propio del Libro en
  tema 2): comprobado que esos temas las dan.

## Correcciones aplicadas

1. **Error 9** (AENOR, tratamiento por nivel): el artículo dice «aquellos riesgos tolerables o
   aceptables serán registrados; los tolerables, pero no inocuos, serán monitorizados; y los
   inaceptables serán tratados específicamente». El tema decía «los aceptables se registran, los
   tolerables se vigilan». Corregido.
2. **Error 9** (AENOR, desviación): «negativa (una amenaza)» no está; el artículo dice negativo «en su
   visión más tradicional del riesgo». Corregido.
3. **Error 9** («versión española de la norma internacional ISO 31000»): no lo dice el artículo.
   Confirmado en la ficha de la norma en tienda.aenor.com (25-09-2026): «Gestión del riesgo.
   Directrices», equivalencia «Idéntica ISO 31000:2018», en vigor. Reescrito con ese dato y añadida la
   fuente a Trazabilidad (une.org devolvió 403).
4. **Error 9** («revista de la entidad de normalización española»): la Revista AENOR no es la del
   organismo de normalización (hoy UNE). → «un artículo de la Revista AENOR».
5. **Error 8/9** (§155 como «Conclusión»): el §155 está en el apartado 6, Fiscalización operativa
   («Del análisis realizado al Contrato Programa como herramienta de gestión y control, se han
   detectado las siguientes incidencias»), no en el 7 de Conclusiones. Corregido en el texto y en
   Trazabilidad.
6. **Error 9** (medios ajenos): «cuando el programa lo hace una productora… el control es de Canal
   Sur» excedía la ficha («tanto si se realiza con medios propios como ajenos»). → «cuando se hace con
   medios ajenos, presupuesto y memoria son suyos, y el plan que los sostiene tiene que existir igual
   (oficio)». Igual que la corrección 4 de 32-T02.
7. Precisión: el Contrato-programa es entre «el Consejo de Gobierno de la Junta de Andalucía» y la
   RTVA (título del Acuerdo de 19-12-2023). Portada ajustada.

Releídos los pasajes cambiados: cada antecedente («el mismo artículo», «la norma») sigue delante.

## Lentes

- `negritas.py` (Libro NFKC, convenio, Contrato-programa, CCA): 62 cotejadas; 4 «no están» (3 rótulos
  de plantilla y la cita de AENOR, verificada en la web); 0 mal atribuidas.
- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 7.876 palabras, 45 epígrafes (índice regenerado).
- `refutar_exactitud.py` y `refutar_modo.py`: no aplican; el tema no cita preceptos de una norma con
  articulado (sólo nombra la Ley de Prevención de Riesgos Laborales, sin artículos).

## Pendiente / avisos

- Dos líneas del tema quedaron largas tras la edición (Advertencia sobre las fuentes y §155); sólo
  formato.
- La pregunta 8 del informe de redacción sigue siendo válida (la cita de AENOR no cambia).
