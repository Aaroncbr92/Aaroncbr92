# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`.
Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Ficheros tocados: el tema y este
informe. Copia previa del tema en el directorio de trabajo (`t14/tema-antes-remate.md`).

Resultado: **4 menores aplicados, 5 lagunas cubiertas ampliando el tema** (ninguna pregunta
recortada). **Hay contenido nuevo: pasa a 5 bis.** Extensión: de unas 9.400 a 10.941 palabras
(`indice.py`); la portada pasa de «8.500» a «11.000 palabras aproximadamente».

## Fuentes releídas para cada corrección (todas el 25-09-2026)

Copias de texto del directorio de trabajo, las mismas de verificación y refutación: UIT-R BS.775-4
(recomienda 2, 3, 6, 7, 8; notas 4-5; anexos 3, 4 —tabla 2 completa—, 5 y 7 con su apéndice 1, § 6
y § 7); UIT-R BS.1770-5 (anexo 4 y su apéndice 1); EBU Tech 3343-2023 (§ 4.2); EBU Technical Review
2009-Q1; Dolby ED2 Technology Brief; guía del Dolby Atmos Renderer v3.0 (§ 24.3.3 y glosario).
Cada cita en negrita nueva se cotejó por script contra el texto de su fuente: 35 de 35 casan.

## Hallazgos: todos confirmados en la fuente

1. **Cita cruzada (1)**. Confirmado: la BS.1770-5 no contiene «2076»; cita la BS.2051 y la BS.2127
   («ITU-R ADM Renderer (IAR)», apéndice 1 del anexo 4). BS.2076 sustituida por BS.2127 en «Lo que
   este tema no da»; añadida a «Recomendaciones técnicas que el tema cita» y a «Trazabilidad».
2. **Pantalla no transparente (6)**. Confirmado en el recomienda 2, cuarto guion. Tabla «La
   colocación de los altavoces»: fila «Altura de los frontales» completada con «This implies an
   acoustically transparent screen»; filas nuevas «Central con pantalla no transparente» y «Altura
   de los envolventes»; frase de aplicación al control de televisión.
3. **In-Sync (6)**. Confirmado en la *Technical Review*. «El retardo de un cuadro»: añadida la cita
   «The decode delay must be compensated…» y una frase en la aplicación práctica (compensar en el
   punto de decodificación si llegó en sincronía; nada si llegó adelantado).
4. **5.0 (6)**. Confirmado en Tech 3343 § 4.2. «El canal LFE»: añadida la frase «This is typically
   the case … action movies».

## Lagunas: ampliadas

1. **Compatibilidad con receptores (P10)**. «La compatibilidad descendente como requisito»: párrafo
   con el recomienda 6 y tabla del anexo 3 (*simulcast*, matrices A/B/T/Q1/Q2, las dos vías para
   receptores de bajo coste). «Qué es y dónde se hace»: recomienda 7. «La saturación del downmix y
   el upmix»: recomienda 8 y tabla de pautas del anexo 5 (mono al central o a L y R con −3 dB,
   estéreo sin central, envolventes apagados sin señal, decorrelación, canal de datos).
2. **Envolvente mono y tabla 2 (P7, P9)**. «El mono y el envolvente mono»: la tabla de los dos
   sentidos de «mono» dice que la MS se reproduce por los dos envolventes; párrafo nuevo con el
   recomienda 3 y S = 0,7071 LS + 0,7071 RS. «Los coeficientes de la UIT»: filas 2/1, 3/1 y 2/2,
   reglas que se leen en la tabla y la advertencia del anexo 4 («will depend on other factors…»).
   «La colocación de los altavoces»: fila de la nota 5.
3. **Calibración del LFE (P6)**. «El canal LFE»: párrafo del anexo 7 (ruido rosa, medidor de banda
   ancha frente a selectivo, +10 dB en emisión) y aplicación práctica.
4. **LFE de Dolby E frente a AC-3 (P13)**. «El LFE no es el subgrave»: párrafo del apéndice 1 del
   anexo 7, § 6, con el riesgo mayor en PCM lineal y aplicación práctica.
5. **Emisión del audio inmersivo**. Fuente ya leída, no nueva: ED2 Brief («For emission, Dolby ED2
   can be transcoded into … Dolby Digital Plus with Dolby Atmos or Dolby AC-4») y guía del Renderer
   (§ 24.3.3, códecs de entrega TrueHD y Dolby Digital Plus, núcleo compatible, reglas Pro Logic IIx
   o Lo/Ro). «Dolby ED2: el Dolby E inmersivo»: dos párrafos y una tabla. «Lo que este tema no da»:
   declarado que las especificaciones de Dolby Digital Plus, AC-4 y TrueHD no se han leído, ni las
   ecuaciones de la tabla 1 del anexo 3.

## Otros pasajes cambiados

- Siglas de entrada: Dolby Digital Plus, Dolby AC-4 y Dolby TrueHD.
- «Qué se puede preguntar»: conversión ascendente de la UIT, métodos de compatibilidad del anexo 3,
  códecs de emisión del inmersivo, calibración del LFE.
- «Trazabilidad»: filas de BS.775-4, BS.1770-5, Tech 3343, Technical Review, ED2 y Atmos
  ampliadas con lo nuevo.

## Antecedentes y lentes

Releídos los pasajes cambiados: «El mismo apéndice» remite al apéndice 1 del anexo 7, nombrado en
el párrafo anterior; «El mismo documento» (ED2), al Technology Brief del epígrafe; «La
recomendación advierte», a la BS.775 de la tabla anterior; «Y añade» (5.0), a la Tech 3343 de la
frase previa. Lentes (tema técnico sin norma legal): `indice.py` regenera el índice (38 epígrafes,
sin cambios de estructura) y `refutar_prosa.py` da 0 hallazgos.
