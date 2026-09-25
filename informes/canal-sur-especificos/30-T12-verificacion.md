# Puesto 30 · Tema 12 · Verificación

Fase 3 · Verificar. Fecha de trabajo y de lectura de todas las fuentes: 25-09-2026 (el encargo fija
«hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`.

## 1. Pasajes copiados: sólo comprobación de literalidad

| Pasaje | Comprobación | Resultado |
| --- | --- | --- |
| Común (34/14 § 1, líneas 103-181) → 30/12 líneas 107-185 | `diff` | Idéntico |
| Común: LGCA 2.18 (34/14 351-355) | comparación | Idéntico |
| Común: Manual RTVE 4.1 (fragmento) y 4.3.2-4.3.3 (dos viñetas) | comparación | Idéntico (la tercera viñeta de 34/14 no se copia, como declara la redacción) |
| Común: LGCA 2.13 y 2.20 (34/14 540-547) | comparación | Idéntico desde «Servicio de intercambio…»; entrada propia, declarada |
| Común: arts. 86-93.1 (34/14 573-598) | `diff` | Idéntico |
| Común: «Conservar lo publicado…» (34/14 643-659) | `diff` | Una sola diferencia: «, tema 16», la declarada |
| RTVE sin cambios: identificador (realizacion/18, 109-114) | `diff` quitando `**` | Idéntico |
| RTVE sin cambios: FTP (160-163) y listas de reproducción (169-176) | `diff` quitando `**` | Idéntico |

No se re-verificaron.

## 2. Verificado en fuente (redactado nuevo y adaptado)

- YouTube, answers 6375112, 15424877, 72431 y 1722171 (`fuentes/canal-sur/montador/web/redes/`,
  leídas enteras): todas las citas y cifras de §§ 2, 4, 6 y del supuesto cuadran (relación 16:9,
  relleno, barras, resoluciones; Shorts desde 15-10-2024, hasta tres minutos, cuadrado o vertical;
  música 90/60/30 s; Content ID desde 24-09-2026 para Shorts nuevos de 1 a 3 min; miniaturas
  3840 × 2160 / 2160 × 3840, 640 px, JPG/PNG, 2 MB / 10 MB / 50 MB, 16:9, 9:16, 1:1, 4:5, 30 días;
  codificación MP4, AAC-LC/Opus/Eclipsa, 48 kHz, H.264, perfil alto, GOP cerrado, CABAC, 4:2:0,
  1080i60 → 1080p30, tasas SDR 4K/2K/1080p/720p, audio 128/384/512, BT.709, BT.2020 → BT.709).
- DNR 2026 (resumen, 16-06-2026): 48 mercados, 54 %/51 %, 77 %, −5 pp, 43/34/26/20 %, «less than
  two minutes», 27 % en televisores: literales.
- DaVinci Resolve 21: cap. 41 p. 860; cap. 127 p. 3119; cap. 182 p. 4140 (−23/−14 LUFS); cap. 187
  pp. 4187-4190 (preajustes, casillas, ajustes propios, «Review Before Upload»): literales y bien
  paginados.
- Normas: LGCA art. 9 (BOE-A-2022-11311, redacción única vigente), art. 101.1.g) («gradualmente
  accesibles»); Ley 10/2018 art. 31.1.i) (BOE-A-2018-15240, redacción vigente desde 17-02-2024);
  fechas de las leyes 13/2022 (7 de julio) y 10/2018 (9 de octubre) y RD 444/2024 (30 de abril, por
  el tema 14 de Redactor/a).
- Cálculos de reencuadre (3413; 31,6 % ≈ 32 %; 607,5 ≈ 608): correctos.
- Remisiones a temas 3, 4, 7 y 11 del puesto: existen.

## 3. Correcciones aplicadas

1. § 2, vertical 1080 × 1920 (error 9): el manual no dice que el preajuste de TikTok produzca
   1080 × 1920; fija **1920x1080 HD** y una casilla para entregar en vertical. Reescrito así.
2. § 4, miniaturas de Shorts (error 6): se añade «Por el momento», que la fuente pone delante.
3. § 4, trampa del 4:5 (errores 6 y 9): «pierde su miniatura en los lugares donde más se ve» no
   tiene fuente y omite la salvedad; ahora nombra las tres páginas y dice dónde se sigue viendo la
   personalizada (página de visualización, historial, no móviles).
4. § 4, límite diario (error 4): las faltas de derechos de autor «pueden influir» (no «influyen»); se
   añade que el límite varía por región, país o historial.
5. § 6, tabla, cadencias comunes (error 6): se añade «(también son aceptables otras frecuencias)».
6. § 5, última pauta (error 9): «la duración de la canción puede limitar la de la pieza» no es lo que
   dice la fuente (limita el tiempo de uso de la canción); reescrito con 90/60/30 s.

Releídos los pasajes cambiados: sin antecedentes rotos.

## 4. Lentes

- `negritas.py` (LGCA, Contrato-programa, Carta, Manual de RTVE de medios interactivos, páginas de
  YouTube, DNR, extractos de Resolve): 112 negritas, todas localizadas; 0 mal atribuidas.
- `refutar_exactitud.py` (LGCA): 1 aviso falso — toma «cláusula tercera… punto 29» del
  Contrato-programa por art. 3 LGCA; pasaje copiado del común y literal en el Contrato-programa.
- `refutar_modo.py` (LGCA): 0. `refutar_prosa.py`: 0. `indice.py`: 8.518 palabras, 36 epígrafes.

## 5. Avisos

- Informe de redacción: la tercera viñeta del Manual de RTVE no se copia (correcto, no es error).
- Para el tema 7 (no tocado): sigue pendiente el aviso de la redacción sobre «cap. 56, p. 1214»
  frente a cap. 127, p. 3119 para las guías de redes.
- La ficha dice «8.400 palabras aproximadamente»; ahora son 8.518. No se toca.

## Ficheros tocados

Sólo el tema 12 y este informe.

## Relanzamiento de la fase 3 (25-09-2026)

La orquestación volvió a pedir la fase 3 de este tema. No se rehízo: la verificación ya estaba
completa (arriba) y el tema había pasado después por refutación, remate y fase 5 bis (`30-T12-final.md`);
el fichero del tema no tiene cambios desde el commit b08a902. Comprobación rápida con `diff`: § 1
copiado del común sigue idéntico a 34/14 y «Conservar lo publicado…» difiere sólo en «, tema 16»
(declarado). No se tocó el tema; sólo se añadió esta nota.
