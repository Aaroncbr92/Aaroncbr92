# Puesto 34 · Tema 4 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/04-fuentes-informativas-verificacion.md`. Copia previa en la carpeta temporal de la sesión (`t04-antes-verif.md`).

## Fuentes releídas (todas el 24-09-2026)

- Libro de Estilo de Canal Sur (2004), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 4.3 a 4.3.7 (ll. 2330-2600), 9.9.1 (l. 6241), portadilla (1.ª ed., marzo 2004), índice (páginas).
- Orden PCM/1030/2020, `fuentes/canal-sur/BOE-A-2020-13663.md`: preámbulo, firma, apartado 1 (definición COM (2018) 236), estructura (sector privado), 4 «Niveles» y anexo I (niveles 1 y 2).
- Carta ética mundial de la FIP, `fuentes/informacion/FIP_carta-etica.txt`: arts. 3, 5, 6, 14 y nota final (Túnez, 12-VI-2019, completa la Declaración de 1954). **Copiado de RTVE: verificado.**
- Resolución PE 25-XI-2020, `fuentes/informacion/PE_resolucion-25-11-2020.txt`: título, DO, apartados 34 y 35. **Copiado de RTVE: verificado.**
- STC 6/1988: texto completo descargado hoy de hj.tribunalconstitucional.es (resolución 947). Pasaje literal; pertenece al FJ 5 del texto íntegro (no sólo del extracto); Sala Primera; BOE núm. 31, de 5-2-1988.
- Barot, «Verifying Images», cap. 4 del *Verification Handbook*, descargado hoy de datajournalism.com.
- CE art. 20.1.d y rúbrica del art. 9 LGCA (fuera de lo copiado del común).

No re-verificado: art. 9.1 LGCA (copiado del común).

## Correcciones

| # | Error | Pasaje | Antes | Ahora |
|---|---|---|---|---|
| 1 | 9 | 5, principio 2 | EXIF: «cámara, fecha y, a veces, coordenadas GPS» | El capítulo cita marca/modelo, fecha y hora (con cautela: ajuste de fábrica, huso horario) y dimensiones; las redes borran casi todos los metadatos. El GPS sólo sale para servicios de localización de redes. Sigla GPS quitada |
| 2 | 9 | 5, «La referencia»; trazabilidad | «la referencia profesional más citada»; «editado por Craig Silverman» | «Una referencia profesional publicada»; el editor no consta en las páginas leídas: quitado |
| 3 | 6 | 6, Resolución PE | «Describe la desinformación como amenaza» | «la amenaza potencial» (ap. 34), literal |
| 4 | 6 | 6, plataformas | «la eliminación de contenidos ilícitos es necesaria» | «destaca la importancia de eliminar rápidamente los contenidos ilícitos» (ap. 35) |
| 5 | 6 | 3, «Dentro de la casa» | el editor «está obligado a guardar secreto» | añadida la condición: «si se trata de fuentes que merezcan su ocultación» |
| 6 | 8 | 3, «Decir de dónde viene» | «también debe indicarse fehacientemente» parecía de 4.3.5 | es de 4.3: añadida la cita |
| 7 | 9 | 1, fuentes digitales | la carta «añade a la declaración de 1954» la cautela | no se ha leído la de 1954: «trae una cautela» |
| 8 | 9 | ficha; «De dónde sale» | Libro de Estilo «único publicado» | «único publicado que se ha localizado» (sólo consta que no se ha localizado otro) |
| 9 | 6 | 2, versiones contradictorias | «aceptar ni descartar ninguna» | «aceptar o descartar por completo una de ellas», como la fuente; atribuida la jerarquía al criterio del periodista |
| 10 | 1 | 6, Orden PCM | cita del sector privado sin ubicación | «en los niveles 1 y 2 (anexo I)» |
| 11 | — | siglas | «PCM es el prefijo del ministerio que la firma» (y el informe de redacción decía que el ministerio no está en el volcado) | La firma sí está en el volcado: se da la ministra firmante; PCM queda como prefijo del número |
| 12 | forma | varios | 23 rótulos en negrita que no son literales (tipos de fuente, «Dato», traducciones de los cuatro principios, «Veracidad no es exactitud total»…) | En redonda (negrita = literal) |

Añadido de la fuente: la regla de cierre del capítulo de Barot («don’t use the image!» si queda duda). Normativa y trazabilidad: Resolución PE, apartados 34 y 35 y título completo; STC, FJ 5 comprobado en el texto íntegro.

## Confirmado sin cambios

Todas las citas del Libro de Estilo 4.3-4.3.7 y 9.9.1 (literales; «mas» sin tilde y «ó» como en el original); páginas 68-75; Bradlee (seis reglas, primeras frases literales); definición de desinformación y «amenazas a los procesos democráticos»; cuatro niveles; Consejo de Seguridad Nacional (6-X-2020); arts. 3, 5, 6 y 14 FIP; pasaje de la STC; cuatro principios de Barot, las cinco preguntas, búsqueda inversa y el caso Sandy («un mes antes»); desmentido presentado como costumbre de oficio.

## Lentes

- `negritas.py` (LE, LGCA, Orden PCM, FIP, PE, STC, Barot, CE): tras el cambio 12, los «no está» restantes son ligaduras del PDF (ﬁ/ﬂ) y citas con «>» de cita partida, comprobadas a mano, más «Enunciado del programa» y «Qué se puede preguntar».
- `refutar_exactitud.py`: 18 «no literales», todos falsos positivos (lee los apartados 4.3.x del Libro de Estilo como «art. 4» de las leyes).
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: índice sin cambios; 4.356 palabras (ficha: «4.400 aprox.», se mantiene).

## Discrepancias con el encargo o el informe de redacción

- El informe de redacción dice que el nombre del ministerio firmante no está en el volcado de la Orden PCM: sí está (firma de la Ministra de la Presidencia, Relaciones con las Cortes y Memoria Democrática).

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.
