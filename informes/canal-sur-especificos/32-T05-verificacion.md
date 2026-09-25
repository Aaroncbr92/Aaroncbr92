# Productor/a (puesto 32) · Tema 5 · Verificación

Fase 3. Tema: `temas/canal-sur-especificos/32-productor-a/05-gestion-de-recursos-humanos-y-condiciones-de-prestacion.md`.
Fuentes releídas el 25-09-2026 (el encargo fija «hoy» en el 24-09-2026; mismas fuentes). Ficheros
tocados: el tema y este informe.

## Copiado (sólo comprobación de literalidad)

Cotejo automático párrafo a párrafo contra `temas/canal-sur-comun/07-x-convenio-colectivo.md`,
`temas/produccion/05-equipos-humanos.md`, `temas/produccion/14-el-presupuesto.md` y
`temas/gestion/06-tiempo-de-trabajo.md`:

- **Copiado del común**: todos los pasajes listados son literales (arts. 3, 10, 11, 12, 14, 21.3.B-C,
  24, 41, 50, 51, 53; DA 2.ª y 7.ª; DT 1.ª y 7.ª y sus tablas; arts. 6, 7). Diferencias sólo de
  arranque, sin cambio de dato: art. 34 («El artículo 34 del convenio obliga a la empresa a dar…»
  por «La empresa da…»); art. 1 y DA 5.ª, fragmentos entrecomillados idénticos al común. No se
  re-verifican.
- **Copiado de RTVE sin cambios**: literales las dos tablas y las tres frases listadas. No se
  re-verifican.

## Verificado en la fuente

| Pasaje | Fuente | Resultado |
| --- | --- | --- |
| Fichas de Productor/a (5331000, pág. 194, ocho tareas) y Ayudante (5212705, pág. 110) | BOJA 240/2014, l. 6916-6947, 4687-4716 | Correcto |
| Nivel B03 del Productor/a y B04 del Ayudante | BOJA 240/2014, l. 1451-1541 | Correcto |
| Anexo II: 26+9 Sevilla, 1×6 centros, 2+1 Málaga = 44; ninguno en Algeciras, Jerez, Madrid | BOJA 240/2014, l. 3140-4380 | Correcto |
| Art. 1, 6, 9.3 y 9.5, 12.a (Dirección) | BOJA 240/2014, l. 170-241, 267-275 | Correcto |
| Art. 21.3.1, 3.3 (treinta días), 3.7, 3.8, B, C | BOJA 240/2014, l. 541-641 | Dos salvedades omitidas (ver abajo) |
| Art. 50.11, 51.4, 53 entero (pág. 78-79), plus de pernocta | BOJA 240/2014, l. 1737-1840 | Correcto; salvedad del plus omitida en un pasaje |
| Art. 14 (no pacta obligatoriedad) | BOJA 240/2014 | Correcto; la conclusión «son voluntarias» se marca como lectura del tema |
| Párrafo de cabecera de las transitorias; rúbrica «pernota» | BOJA 240/2014, l. 2332-2340, 2596 | Correcto |
| DA 2.ª (lectura para el productor) | BOJA 240/2014, l. 2236-2280 | Inferencia sin apoyo (ver abajo) |
| Libro de Estilo 4.4, 4.4.1, 4.4.2, 4.4.4.2; 1.ª ed. marzo 2004; pág. 75-77 | `libro-de-estilo` .txt, l. 2597-2690 | Correcto (las dos «no está» de `negritas.py` son la ligadura «ﬁ») |
| Cámara 2018: puntos 162, 235, 236, 250, 252, 253; anexo 9.1 | BOJA 36/2021, l. 2870-4439, 10174-10179 | Citas correctas; dos «único/más reciente» sin fuente |
| Contrato-programa, cláusula tercera, punto 68 | BOJA 245/2023, l. 1656-1660 | Correcto |
| Convocatoria: Granada 1, Jaén 1, Sevilla 12; Reglamento Mesa 12-03-2026 | BOJA 186/2026, l. 611-799, 64, 104 | Correcto |
| ET 34.1-6, 34.8, 34.9 (RDL 5/2023, vig. 30-06-2023) | `boe.py precepto a34` | Correcto; salvedad del 34.8 omitida |
| ET 35, 36 (redacción única 2015) | `boe.py` a35, a36 | Correcto |
| ET 37.1-2 (vig. 03-03-2025, Ley 6/2024) | `boe.py` a37 | Correcto |
| ET 40.1, 40.6, 40.7 (vig. 22-08-2024) | `boe.py` a40 | 40.6 correcto; 40.7 con salvedad omitida; consultas son 40.2 |

## Correcciones aplicadas (cada una comprobada en la fuente)

1. **Portada, Fuente** (error 9): quitada la «Ley 7/2024», que el tema no usa en ningún pasaje.
2. **Cámara, entrada** (error 9): «El único diagnóstico publicado» → «El diagnóstico publicado… que
   recoge este tema». Lo mismo en «Centros y desconexiones»: «más reciente» → «que recoge este tema».
3. **ET 34.3, glosa** (error 6): «indisponible» → «indisponible para el convenio» (el 34.3 sólo impide
   al convenio tocarlo; el 34.7 permite ampliaciones y limitaciones por el Gobierno).
4. **ET 34.8** (error 6): añadida la condición de las personas dependientes («no puedan valerse por
   sí mismas por razones de edad, accidente o enfermedad») y el deber de justificar la petición.
5. **Horas extraordinarias**: «son voluntarias» marcado «(lectura del tema)»; el art. 14 no dice
   nada sobre la voluntariedad.
6. **Tabla salida/desplazamiento/traslado** (error 6 y 8): el permiso en el domicilio de origen, «si
   pasa de tres meses»; traslado, «artículos 40.1 y 40.2 del ET» (las consultas son del 40.2).
7. **Art. 21.3.8** (error 4/6): los criterios son los que «**se procurará atender**», no obligatorios.
   **Art. 21.3.1**: «Antes de imponerlo» (antecedente dudoso) → «Antes de adoptar los criterios del
   traslado forzoso», añadida «y, en su caso, la de concurso».
8. **ET 40.7** (error 6): «el ET sólo da a los representantes…» → añadido que permite al convenio o al
   acuerdo en consultas fijar prioridades para otros colectivos, como mayores de determinada edad.
9. **Plan de viaje** (error 6): el plus de pernocta sólo si se pernocta fuera de Andalucía y la
   jornada se prolonga más de dos horas (art. 53.4).
10. **DA 2.ª, lectura para el productor** (error 9): quitado «que no están libres para otra producción
    mientras la hacen» (la DA dice que lo hacen «adicionalmente a las funciones propias de su
    puesto») y «no una ampliable a demanda»; «centros pequeños» → los cinco centros que nombra la DA.
11. **Málaga** (precisión): «único centro territorial con productor de radio» → «con plaza de
    Productor/a de radio (CSR) en el anexo II» (Algeciras y Jerez tienen Presentador/a productor/a).
12. **Trazabilidad**: añadido el art. 1 a los pasajes copiados del común.

Pasajes cambiados releídos: cada remisión («ese artículo», «el apartado B», «esos centros») tiene su
antecedente.

## Lentes

- `negritas.py` (convenio, ET, Libro de Estilo, Cámara, contrato-programa, convocatoria, común 07):
  183 negritas; 4 «no está»: dos rótulos («Qué se puede preguntar.», «Advertencia…») y dos del Libro
  de Estilo por la ligadura «ﬁ» (literales). 1 «¿art. 22?»: la definición de trabajo nocturno, que es
  del art. 36, como dice el tema (falso positivo).
- `refutar_exactitud.py` (ET, Ley 3/2012): las «no literales» son citas del convenio con «(art. N)»
  del convenio, no del ET; la de menores es del 34.3, como dice el texto (falso positivo).
- `refutar_modo.py` (ET): dos avisos; el del 35.2 ya lo recoge el tema («salvo lo previsto en el
  apartado 3»); el del 37 es de permisos, fuera del tema.
- `refutar_prosa.py`: tres siglas «sin presentar»: CSR (presentada en la misma frase), ESTRUC (rótulo
  literal del anexo II) y RAI (el tema ya declara que el informe no la desarrolla). Sin cambios.
- `indice.py`: índice correcto; 11.717 palabras de cuerpo.

## Sin confirmar (se mantiene declarado en el tema)

Cuantías vigentes del Decreto 54/1989; qué jornada aplica hoy la RTVA; acuerdos de la COMVI y pactos
de trabajo; normas internas de citación, partes, desplazamientos y dietas; plantilla y estructura de
2026. Tampoco se decide si la remisión del art. 21.3.B alcanza al preaviso de treinta días del 3.3
(el tema da los dos textos; es correcto así).
