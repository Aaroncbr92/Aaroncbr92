# Puesto 08 · Tema 9 · Fase 5 · Remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`.
Entradas: `08-T09-refutacion.md` (H1-H4, L1) y `08-T09-preguntas.md` (P10 «no»).

## Fuentes releídas (24-09-2026)

- EBU Tech 3335 (agosto de 2014), § 4.4 «Contrast handling», texto completo del apartado.
- EBU R 118 v2 (abril de 2017), § 1.1 «Critical testing criteria».

## Correcciones: comprobadas y aplicadas (las cinco se confirman en la fuente)

| Id | Epígrafe | Antes | Después | Comprobación |
|---|---|---|---|---|
| H1 | Color · La colorimetría de referencia | «…que el mismo error en el verde, y de que el ruido suela verse antes en el azul (oficio).» | «…que el mismo error en el verde (se deduce de los coeficientes).» | Los coeficientes (BT.601/709/2020) no explican el ruido del azul; se quita la inferencia |
| H2 | Exposición · El margen de exposición | «**the effective dynamic range will be reduced by about 1 stop per 6dB…**» | «**If the noise level is particularly high, then the effective dynamic range will be reduced by about 1 stop per 6dB of video noise level increase.**» y la consecuencia práctica pasa a «cuando el ruido ya es alto, subir ganancia… (se deduce de la segunda cita, que pone esa condición)» | Tech 3335 § 4.4, frase completa |
| H3 | Foco · El punto dulce y la difracción | «unos dos o tres pasos por debajo de la abertura máxima» | «cerrando unos dos o tres pasos desde la abertura máxima» | Redacción; sin cambio de dato (oficio) |
| H4 | Calidad · Qué se mide… | «(R 118 v2), y fija cinco criterios de medida, a los que suma el códec de grabación:» | «(R 118 v2, § 1.1). Habla de «**five areas that are specific to the actual camera and (where applicable) to the on-board codec**», pero su lista tiene seis entradas y empieza por el códec; aquí se ordenan con el códec al final:» | R 118 § 1.1: seis viñetas, *Codec* la primera |

## Laguna ampliada (L1, P10)

Epígrafe «Exposición · Las altas luces: el *knee*»: párrafo nuevo tras los valores de la Sony Z200,
con cinco citas literales de Tech 3335 § 4.4: punto de *knee* manual entre 80 % y 90 % para los
tonos de piel (curva ITU.709, cámara sin curvas de tipo cine); el 14 % superior de la señal ≈ 1 paso
y la pendiente baja gana al menos otro; poco contraste: curva BBC0.4 o ITU.709 y recorte de blancos
≤ ~104 %; directo o *as-live* con curvas de tipo cine: no superar el 100 %; ajuste con diente de
sierra interno y monitor de forma de onda. La pregunta P10 queda contestada entera sin tocarla.
Trazabilidad: fila de Tech 3335 ampliada con «ajuste recomendado del *knee* y del recorte de blancos».

Cada negrita nueva se ha cotejado, normalizando espacios, contra el texto de la fuente: todas literales.
Antecedentes releídos: «la segunda cita» sigue refiriéndose a la viñeta de los 6 dB; «El mismo
documento» del párrafo nuevo tiene delante Tech 3335.

## Lentes

- `indice.py`: 10.581 palabras de cuerpo, 48 epígrafes, índice regenerado sin cambios de rúbrica.
- `refutar_prosa.py`: 0 hallazgos.
- Sin lentes de normas: tema técnico sin norma jurídica.

## Resultado

Correcciones aplicadas: 4 (H1-H4); rechazadas: 0. Ampliación de contenido nuevo: **sí** (L1),
así que toca la fase 5 bis sobre el párrafo nuevo del *knee* y los pasajes de H2 y H4.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe.
