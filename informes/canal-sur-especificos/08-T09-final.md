# Puesto 08 · Tema 9 · Fase 5 bis · Revisión de los pasajes rematados

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`.
Alcance: sólo los pasajes que lista `08-T09-remate.md` (H1-H4 y la ampliación L1 del *knee*).

## Fuentes releídas (24-09-2026)

- EBU Tech 3335 (agosto de 2014), § 4.4 «Contrast handling», completo.
- EBU R 118 v2 (abril de 2017), parte «Recommends that», § 1.1 y nota del § 1.3.

## Pasaje por pasaje

| Id | Resultado |
|---|---|
| H1 (colorimetría) | Correcto. La deducción (un error en el azul pesa menos en la luminancia que en el verde) se sigue de los coeficientes de la tabla; la frase del ruido azul ya no está |
| H2 (margen de exposición) | Cita literal y completa (§ 4.4). La consecuencia práctica conserva la condición «cuando el ruido ya es alto»; «la segunda cita» tiene su antecedente en la lista |
| H3 (punto dulce) | Correcto. Cambio sólo de redacción; sigue marcado como «(oficio)» |
| H4 (criterios R 118) | **Corregido.** El remate atribuyó al § 1.1 la cita «according to their technical specifications… EBU Tech 3335». Esa frase está en la parte dispositiva («Recommends that»), no en el § 1.1 (error 8). Ahora cita esa parte, y el § 1.1 se asigna a «five areas…», que sí está ahí. El recuento de seis entradas con el códec en primer lugar se confirma. Fila *Codec* (error 6): «que sólo cuenta si graba a bordo» pasa a «en las cámaras de sistema sólo cuenta si graban a bordo», porque la fuente dice «does not apply to system cameras unless on-board recording in used» |
| L1 (*knee*) | Las cinco citas son literales (80-90 %, 14 % ≈ 1 paso, 104 %, 100 % en directo o *as-live*, diente de sierra y forma de onda), y cada una está en la rama que le corresponde (curva ITU.709 sin curvas de tipo cine / con curvas de tipo cine). **Corregido:** «pide lo contrario, no comprimir» era una glosa. Se sustituye por el texto de la fuente: «en las que el contraste de la escena «**is effectively expanded**»». El antecedente de «El mismo documento» es Tech 3335 |

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 10.599 palabras, 48 epígrafes; ninguna rúbrica ha cambiado.

## Resultado

Cinco pasajes revisados y tres correcciones aplicadas, todas comprobadas en la fuente: la ubicación de la cita de R 118, la salvedad de la fila *Codec* y la glosa del poco contraste. No queda nada pendiente.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.
