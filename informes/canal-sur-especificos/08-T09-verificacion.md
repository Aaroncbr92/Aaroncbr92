# Puesto 08 · Tema 9 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`
(≈10.300 palabras tras la verificación).

## Fuentes releídas (todas el 24-09-2026)

Descargadas a la carpeta temporal de la sesión y pasadas a texto con `documento.py texto` (no quedan en el repositorio):
- EBU R 103 v3.0 (tech.ebu.ch/docs/r/r103.pdf), EBU R 118 v2 (r118.pdf), EBU Tech 3335 (tech3335.pdf), EBU Tech 3355 (tech3355.pdf).
- UIT-R BT.709-6, BT.2020-2, BT.601-7 y BT.2100-3 (02/2025), PDF en inglés de itu.int (la copia local de las tres primeras está en español; de la BT.2100 sólo existe la -1 en local).
- Sony *PXW-FS5 Operating Guide* 4-581-849-11(1) (copia de ats.emory.edu); Blackmagic *URSA Broadcast G2*, noviembre de 2021 (copia de markertek.com).
Copias locales: Sony PXW-Z200 Help Guide 5-060-574-13(1); Panasonic AVC-Intra FAQ; Libro de estilo de Canal Sur (2004).

Método: script que busca cada cita en negrita (normalizada) en todas las fuentes. Resultado: todas localizadas y en la fuente atribuida. La única que no aparece es la de *black-stretch*, por un fallo de extracción del salto de línea («black-\nstretch»); comprobada en el PDF. Luego he leído el contexto de cada cita y de cada dato no literal (secciones, páginas, valores de fábrica, tablas).

## Copiado del común

Ninguno (según el informe de redacción). No se ha saltado nada.

## Correcciones (error del catálogo)

1. **Levantado y gamma de negros (copiado de RTVE, IG/08 §3), errores 9 y 6.** La tabla «sólo en luminancia / sólo levanta frente a RGB / bidireccional» y la idea de que «comprimir los negros no tiene sentido» no tienen apoyo en ninguna fuente. Además las contradicen Tech 3335 § 4.4 («Black-stretch (and black-press)… black-press conceals it») y la FS5 ([BLACK GAMMA] de «–7 (maximum black compression) to +7 (maximum black stretch)»). En RTVE procedía de una respuesta oficial de examen, que en Canal Sur no sirve de fuente. **Quitado**, y el epígrafe se ha reescrito con Tech 3335 (pareja stretch/press, más ruido, mejor en cámara que en posproducción) y con la FS5. «Levantar los negros sube el ruido» pasa de oficio a Tech 3335.
2. **R 118, HD Tier 1 «10-bit», error 6.** La tabla 2 da «10-bit» como procesado mínimo, pero el § 2.7 dice «10-bit processing preferred». Ahora el tema da las dos cosas, y la frase del submuestreo («la EBU pide 4:2:2 y 10 bits») queda matizada.
3. **R 118, tabla 6 (S/N), errores 4 y 6.** El tema decía «fija mínimos», pero la columna de notas los da como orientación («Guidance only»; «For guidance however…»). Corregido, con la cita.
4. **R 118, límite del 33 %, error 9.** Se ha quitado «precisamente porque se nota al mezclarlo», porque la recomendación no da esa razón. También se ha ajustado el sujeto: son las cadenas las que «usually limit».
5. **R 103, error 9.** «Recortar mal es peor que no recortar» no está en la fuente. Ahora dice: la señal que excede el rango total se recorta, y ese recorte tiene el efecto citado. «El recorte mal hecho» pasa a «el recorte».
6. **Tech 3355, error 9 y error 6.** El tema decía «La EBU creó el TLCI», pero el TLCI parte del trabajo de Sproson y Taylor y el de la EBU es el TLCI-2012. Se ha añadido la cautela de la fuente («appears to represent»). «No se arregla con el balance» pasa a «no corregible para televisión». Se ha añadido «do not form hard definitions» a la escala de multicámara.
7. **Tech 3335, error 8.** La cita del *videolook* estaba en el § 4 y es del § 4.3. La obturación nominal es la del procedimiento de medida del § 2.9.1, y así se dice.
8. **Sony Z200, archivos de escena, error 6.** Faltaba el aviso de que el archivo no reproduce del todo los ajustes y de que la imagen cambia entre modelos. Añadido literal.
9. **Tiraje.** El «cuándo» y el método eran oficio. Ahora se apoyan en Blackmagic URSA Broadcast G2 (al montar y al cambiar objetivo). El golpe y la temperatura siguen como oficio.
10. **Hueco y trazabilidad.** He leído la tabla 1 de R 118 entera, así que el hueco dice ahora que las filas no reproducidas están en la propia tabla. Coeficientes de luminancia cotejados con BT.601-7, BT.709-6 y BT.2020-2 (quitada la nota «no se han vuelto a leer»). Secciones de R 118 y Tech 3335 completadas. FS5 [BLACK GAMMA] y Blackmagic (tiraje) añadidos.

## Confirmado sin cambios (muestra de lo cotejado)

Tabla 1 de R 103 (16 valores); umbral del 1 %; recortadores en directo; PLUGE y 0-700 mV (anexo 2); no aparecen −1 %/103 % en la v3.0. Niveles, resoluciones UHD y tasas de R 118 (Intra 100/200 y 50/75; H.264 25/35; MPEG-2 UHD «Not to be used»). Cifras de Tech 3335 § 2.4 y § 4.4. Primarios, D65, 16/235 y 64/940 de BT.709-6; primarios de BT.2020-2, y BT.2100-3 con esos mismos primarios; nota 10a, PQ/HLG y BT.814. Valores y ajustes de fábrica de la Z200 (*knee*, *black*, *detail*, *noise suppression* On/Mid, *flicker* Off/60 Hz, SteadyShot). Libro de estilo: 5.1 p. 79, 5.2 p. 80, 6.3.4 p. 91, 6.4 y 6.5 p. 92.

## Lo copiado de RTVE, oficio sin fuente, que se mantiene declarado

Reparto de puestos, monitor de referencia, Seidel, punto dulce («dos o tres pasos», oficio), *blooming*/*smear*/*moiré*, balance y regla del complementario, submuestreo, estabilización pasiva/activa, DCT. Nada contradice lo leído.

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` da 0 hallazgos; `indice.py` sin cambios en el índice (48 epígrafes). He releído los pasajes cambiados: cada «el mismo documento», «ese manual» y «la propia recomendación» tiene su antecedente.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.
