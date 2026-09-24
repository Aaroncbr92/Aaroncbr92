# 34 · T16 · Verificación (fase 3)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/16-proteccion-de-datos-privacidad-imagenes.md` (9.000 palabras según `indice.py`; la ficha decía 8.738).

No se ha vuelto a verificar lo que `34-T16-redaccion.md` lista en «Copiado del común». Para saber qué era nuevo, se comparó línea a línea con `temas/canal-sur-comun/10-proteccion-de-datos.md`. Sí se ha verificado lo copiado de RTVE (§4 «Grabar en la calle»).

## Fuentes releídas (todas el 24-09-2026)

- LOPDGDD, `BOE-A-2018-16673.md`: art. 22, con una sola redacción, vigente desde el 07-12-2018. Se buscó «víctima» en todo el texto: solo aparece en la DA 7.ª.2.
- LO 1/2004, `boe.py`: art. 14 y art. 63, cada uno con una redacción.
- LO 1/1982, `BOE-A-1982-11196.md` y `.redacciones.tsv`: arts. 4 y 7 (vigentes desde el 23-12-2010) y art. 8 (una redacción).
- CE, `BOE-A-1978-31229.md`: art. 20.1.d) y 20.4, con una redacción.
- Reglamento, `DOUE-L-2016-80807.md`: el art. 9 está en el capítulo II. En la consulta a ese fichero no salió ningún considerando.
- Libro de estilo de 2004, `libro-de-estilo-333233b.txt`: portada (1.ª ed., marzo de 2004), 9.1, 9.1.2, 9.1.3, 9.2.12.1, 9.2.12.2, 9.4.2, 9.5.2, 9.7, 9.9 y 9.9.1.

## Correcciones aplicadas

1. **§3, LE** (err. 8/6): la regla sobre la enfermedad es el apartado 9.7, y el tema la tenía incompleta. Faltaba el segundo requisito, «sea necesario para entenderlo correctamente». Ahora se cita literal.
2. **§4, intro** (err. 9): «la regla… está sobre todo en» era una opinión. Se reformula: la LO 1/1982 dice cuándo hay intromisión, y la identidad física aparece como elemento del art. 4.1.
3. **§4, art. 22** (RTVE; err. 9/6): «se cita a menudo» no tenía fuente y se quita. Se añade la salvedad del 22.2: la captación puede ser más extensa si lo exige la seguridad de bienes o instalaciones estratégicos o de infraestructuras de transporte, y nunca puede alcanzar el interior de un domicilio. El resto coincide con el texto vigente.
4. **§5, LE 9.4.2** (err. 6): la negrita estaba cortada; se completa con «pero se silenciarán las demás circunstancias». El error se refiere a «padres o parientes», no solo a los padres. Se añade la regla del menor víctima o allegado de un delincuente («no será mencionado»). La frase «más estricto que la ley», que era una valoración, se sustituye.
5. **§6, intro** (err. 9): la afirmación general se limita al Reglamento y a la LOPDGDD y se menciona la DA 7.ª. La DA 7.ª se añade también en «Normativa».
6. **§6, LO 1/1982 4.4** (err. 6/7): falta la remisión en caso de fallecimiento. Se indica que la redacción de los arts. 4 y 7 es la vigente desde el 23-12-2010.
7. **§6, LE** (err. 6): en 9.2.12.2 faltaba «sólo se emitirán con autorización y con un prudente alejamiento profesional» y los detalles de referencia. En 9.2.12.1 no dice «agresor», sino «presunto agresor». En 9.5.2 faltaba la salvedad de la víctima ya adulta. En 9.9.1 son los cámaras quienes no deben asediar, a víctimas de delitos, accidentes de tráfico, hechos cruentos y otros casos. Se añade 9.9: la imagen de víctimas no se emite si hay factor de riesgo.
8. **§7, párrafo final** (err. 6): «pide el consentimiento expreso» daba el consentimiento como única vía. El art. 2.2 excluye también la intromisión autorizada por ley, y quedan además los casos del art. 8.
9. **§8, LE** (err. 6/9): 9.1.2 no dice «no dar datos irrelevantes», sino que estos no acaparen la noticia. En 9.5.2 se añaden los condenados y los familiares o amigos, y se completa la negrita («…para que la noticia sea completa»).
10. **§9, fila de violencia de género**: «hijos o personas a su cargo» se cambia por el literal del 63.1, «descendientes… guarda o custodia».
11. **Ficha y normativa**: título completo del Libro de estilo. Reglamento: se añaden el art. 12 y el considerando 71. LOPDGDD: se añaden el art. 26 y la DA 7.ª. Extensión: 9.000 palabras. Se quita «o LE» de las siglas, porque no se usa.

Confirmado sin cambios: art. 22.1, 22.3 y 22.4 LOPDGDD; LO 1/2004 arts. 14 y 63.1; LO 1/1982 arts. 7.5, 7.6, 7.8 y 8.2; CE 20.1.d) y 20.4; art. 9 del Reglamento en el capítulo II; LE 9.1 («cuyo seguimiento es obligatorio») y 9.1.3; tabla §9, filas añadidas; Trazabilidad (identificadores y edición).

## Lentes

- `negritas.py`, con las 11 fuentes (el LE normalizado con NFKC): 99 negritas cotejadas. Hay 6 «no están», todas considerandos copiados del común; el volcado DOUE no los trae. Hay 6 «mal atribuidas», todas falsas por proximidad: 1.b, 22.4→12, 83.1, 66.3.c, «Y el artículo 14» y 20.4.
- `refutar_exactitud.py`: 15 avisos, falsos positivos. Lee los apartados 9.x del LE como «art. 9» y no reconoce los artículos de la LO 1/1982 escritos con palabras. `negritas.py` los confirma literales.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 26 epígrafes.

## Para la fase 4 / remate

- §8, pasaje del común: «…audiovisual, que se ven a continuación». La LO 1/1982 está antes (§4) y la LO 2/1984 no se trata en este tema. El aviso sigue abierto.
- Doctrina TC/TS: no se ha incluido.

Ficheros tocados: el tema y este informe.
