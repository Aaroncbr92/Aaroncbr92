# 34 · T16 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/16-proteccion-de-datos-privacidad-imagenes.md`.
Entrada: `34-T16-refutacion.md` (0 graves, 2 menores, 5 lagunas) y `34-T16-preguntas.md` (10 enteras, 2 a medias, 3 no).

**Amplía contenido nuevo: sí.** Por eso toca la fase 5 bis sobre los pasajes que se listan abajo.

## Fuente releída

Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004), `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`,
leído el 24-09-2026: 9.1.4, 9.1.8, 9.4.2.1, 9.5.2 (entero), 9.7 (párrafos 1 y 2), 9.9, 9.9.1 y 9.9.2.
Nota: `documento.py seccion` no encuentra esos rótulos en este `.txt`; se localizaron con `grep -n` y se leyó
solo el tramo correspondiente. El texto usa la ligadura «ﬁ», así que `refutar_documento.py` marca como no
literales las citas que llevan «fi». Se volvió a pasar la lente con una copia en la que «ﬁ» se cambió por «fi»,
y todas las negritas nuevas salen literales.

## Comprobación de cada punto

| Punto | ¿Confirmado en la fuente? | Aplicado |
|---|---|---|
| M1 remisión «que se ven a continuación» | Sí: la LO 1/1982 está antes (§4) y la LO 2/1984 se remite al tema 1 | Sí |
| M2 9.9 abarca menores, víctimas, testigos protegidos y fuerzas de seguridad | Sí, es literal | Sí, en §6 con remisión desde §5 y §4 |
| L1 9.5.2 párrafos 3 y 4 (detenidos, personas públicas) | Sí | Sí, en §8 |
| L2 9.9 (ardid y cámara oculta, primeros planos) y 9.9.2 | Sí. Precisión: los «planos cortos» son del 9.9, no del 9.9.2 | Sí, subepígrafe nuevo en §4 |
| L3 9.4.2.1 (entrevistas a menores) | Sí | Sí, en §5 |
| L4 9.1.8, 9.1.4 y 9.5.2 párrafo 2 | Sí. El 9.1.8 trae la errata «si así o solicita», así que se da en redonda. Se añade también el cierre del 9.9.2 (autorización para la imagen detallada de la víctima) | Sí, en §6 y §7 |
| L5 9.7 párrafo 2 (hospital) | Sí | Sí, en §3 |

El informe de refutación no se equivocó en ningún punto. Solo hay que corregir la ubicación de los «planos
cortos» en L2: van en el 9.9, que es donde los pone el tema.

## Pasajes cambiados

1. **Portada**: Extensión 9.000 → 9.746 palabras.
2. **«Qué se puede preguntar»**: se añade la cámara oculta, los primeros planos de heridos, la entrevista a menores, la grabación en un hospital y la identidad de un detenido.
3. **Índice**: nueva entrada «La pauta del Libro de estilo sobre imágenes», que regenera `indice.py`.
4. **§3, tras la cita del 9.7**: se añade el segundo párrafo (intimidad del enfermo y «siempre solicitaremos autorización para grabar imágenes…»).
5. **§4, nuevo `### La pauta del Libro de estilo sobre imágenes`**: el 9.9 (ardid y cámara oculta con autorización de la Dirección de Informativos; planos cortos de muertos y heridos; personas en riesgo, con remisión al §6) y el 9.9.2 (distancia, primer plano y edición).
6. **§5 «La pauta del Libro de estilo»**: se añade el 9.4.2.1 (abstención e intervención obligatoria sobre imagen y sonido) y la remisión al 9.9.
7. **§6, final**: la frase recortada del 9.9 se sustituye por la cita literal completa. Se añade el 9.5.2, párrafo 2 (víctimas y testigos acogidos, paradero secreto).
8. **§7, párrafo nuevo al final**: el 9.1.8, el 9.1.4, la remisión al 9.7 y el cierre del 9.9.2.
9. **§8 «Cómo se pondera»**: se añade la lista con el 9.5.2 sobre detenidos y personas públicas.
10. **§8 «Lo que la LOPDGDD no hace»**: la remisión queda así: «…leyes de protección del honor y audiovisual (epígrafes 4 y 5; la rectificación de la LO 2/1984, en el tema 1)».

Se han releído todos los pasajes cambiados. Cada remisión tiene delante su antecedente: «se cita literal en
el epígrafe 6», «en el mismo 9.5.2» (con el 9.5.2 en la frase anterior) y «9.7, en el epígrafe 3».

## Preguntas tras el remate

4, 11, 12, 13 y 14 pasan a contestarse **enteras** con el tema. Resultado: 15 de 15. No se ha recortado ninguna pregunta.

## Lentes

- `indice.py`: 9.746 palabras, 27 epígrafes, índice regenerado.
- `refutar_prosa.py`: 0 hallazgos.
- `refutar_documento.py` contra el Libro de estilo (con «ﬁ» normalizada): todas las negritas nuevas son literales.
- `negritas.py` con LOPDGDD, LO 1/1982, LO 1/1996, LO 1/2004, Ley 13/2022, Ley 10/2018, CE, Reglamento y Libro de estilo: 109 cotejadas. Los 6 «no está» son considerandos del Reglamento, que no están en el volcado del articulado. Los 6 «atribuidas a otro artículo» son falsos positivos: el tema cita el artículo correcto (1, 22, 83, 66, 14, CE 20). Nada nuevo, y todo es anterior al remate.

## Ficheros tocados

- El tema 16.
- Este informe.
- `…/scratchpad/remate.py` y `le.txt`, fuera del repositorio.
