# Realizador/a (puesto 33) · Tema 14 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo); fuentes releídas en esta sesión, el 29-09-2026
(fecha del sistema). Tema:
`temas/canal-sur-especificos/33-realizador-a/14-formatos-video-resolucion-compresion-hdr-codecs-entregables.md`
(19.612 palabras según `indice.py`, 74 epígrafes; índice sin cambios). Copia previa:
`33t14-antes-verif.md` en el scratchpad.

## Lo copiado: sólo comprobación de literalidad

Por script (`33t14-lit.py` en el scratchpad), bloque a bloque, normalizando espacios y quitando las
negritas en lo de RTVE, contra las líneas que declara el informe de redacción (y su `log.tsv`): 51
bloques, del común (`30/04`, `30/02`, `08/07`, `08/03`) y de RTVE (`realizacion/05`, 310-317,
393-401, 404-410, 413-419, 436-442, 449-457, 458-461). Los 51, literales. Repetido tras las
correcciones: siguen literales. No se ha re-verificado su contenido.

Cotejo con el informe de redacción: los rangos del `log.tsv` coinciden con los declarados en
«Copiado del común» y «Copiado de RTVE sin cambios» (1039-1050 va en dos tramos, 1039-1046 y
1047-1050). Epígrafes 7, 9 y 10 del tema 5 de RTVE, como dice la Trazabilidad: correcto.

Lo adaptado, verificado:

- ST 292-1 (§ 3): **«The total data rate shall be either 1.485 Gb/s or 1.485/1.001 Gb/s»**, literal
  en `smpte/st292-1-2018.txt`, l. 194.
- X400, «Specifications», p. 144: las dos cadenas de la tasa están en la p. 144 del manual
  (`x400.txt`, entre las marcas 144 y 145).
- Remisiones cambiadas: § 3 (profundidad de bits), § 7 (código de tiempo, *proxies*, ficha LOC
  fdd000013), apartado siguiente (R 103), tema 12 (canal alfa, zonas seguras R 95), tema 15 (ST
  2110), tema 13 (mezcla, revisión final, BT.1702): todas tienen el contenido.
- Rótulos y frases de enlace («que se aplica», «En la sala de montaje», «Para la pieza montada», «al
  realizador le importan…», «El archivo de CSRTV…», «Es aritmética.», «Las relaciones más usadas…»):
  sin dato nuevo.

## Fuentes releídas (lo propio del tema)

| Fuente | Fichero | Qué se ha comprobado |
|---|---|---|
| RD 1680/2011 (BOE-A-2011-19599) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | 18 citas literales y su módulo, RA y letra: 0905 RA 1 f) (l. 636) y contenido (l. 685); 0906 RA 2 c) (l. 754); 0907 RA 5 f) y h) (ll. 898, 900), RA 6 enunciado y a)-d) (ll. 901-906), contenidos «Control de calidad del producto» (ll. 958-961); 0910 RA 4 e) (l. 1235), RA 5 d) y e) (ll. 1243-1244), RA 7 a) (l. 1257). Títulos de los módulos. «codecs» y «master» sin tilde, como en el BOE |
| RD 500/2024 (BOE-A-2024-10685) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | Nombra 0905-0910 sólo en listados y en el nuevo anexo III (profesorado, apartado Cuarenta); no cambia los RA citados |
| X Convenio RTVA, BOJA 240/2014 | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Ficha 5351000, p. 196, anexo III: las dos tareas citadas, literales |
| Contrato-programa 2024-2026, BOJA 245/2023 | `…/contrato-programa-2024-2026-boja-245-2023.txt` | Punto 85 (p. 42, apartado 3.16 de la cláusula tercera), punto 101 (p. 47), parte expositiva (p. 11): literales y páginas por las marcas «página 40208/N» |
| Libro de Estilo, 2004 | `…/libro-de-estilo-333233b.txt` | 3.17.1.5, cita del máster partida entre pp. 61 y 62 (ll. 2075-2082): literal |
| EBU, *Quality Control* (01-09-2015) | `qc.txt` del scratchpad | Las seis citas y los cuatro tipos de control |
| Catálogo EBU QC | `r33t14/qcapi.txt` y `qcitems.html` del scratchpad | Los 10 ítems: identificador, nombre y definición casan (incl. «metdata»); pie «All QC Items are published under CC-BY 4.0» |
| YouTube Help 2853702 | `yt2853702.txt` del scratchpad | Tabla de parámetros: todas las cadenas, en su rótulo |
| Sony PXW-Z200 | `z200.txt` del scratchpad | Menú [TC/Media] – [Timecode]: [Preset]/[Regen]/[Clock] y [Rec Run]/[Free Run] |
| Sony PXW-X400 y SMPTE ST 292-1 | `x400.txt`, `smpte/st292-1-2018.txt` | Sólo las dos líneas adaptadas |

Lentes: `negritas.py` con RD, Convenio, Contrato-programa, LE, EBU QC, catálogo y YouTube: 244
cotejadas; entre las «no están», sólo tres en lo propio o adaptado: la ST 292-1 y la X400 (su fuente
no se pasó; comprobadas a mano, arriba) y la del LE partida por página (a mano). El resto son pasajes
copiados del común, cuyas fuentes no se pasaron. `refutar_exactitud.py` y `refutar_modo.py` con el
RD: 0 hallazgos (se cita por módulo, RA y letra). `refutar_prosa.py`: 3, HD, UHD y HDR en el título,
que es el enunciado literal (se presentan en las siglas; no se toca). `indice.py`: 74 epígrafes,
índice correcto.

## Correcciones aplicadas

| # | Pasaje | Error | Antes → ahora | Fuente |
|---|---|---|---|---|
| 1 | § 7, «El código de tiempo», párrafo de los modos | 3 y 6 | Cuatro modos seguidos (Rec Run, Regen, Free Run, Clock), que mezclaban dos ajustes y omitían *Preset* → dos ajustes: arranque (*Preset*, *Regen*, *Clock*) y marcha (*Rec Run*, *Free Run*), «paráfrasis del manual de la Z200, menú [TC/Media] – [Timecode]» | Z200, [Mode] y [Run] |
| 2 | § 5, «El HDR en la realización», fila «Curva» | 9 | HLG «por su compatibilidad con las pantallas SDR» → «por el grado de compatibilidad con las pantallas anteriores que le reconoce la BT.2100-3» (la fuente dice «a degree of compatibility with legacy displays», cita ya en el § 5) | BT.2100-3, en el pasaje copiado |
| 3 | § 5, cierre, RD y HDR | 6 | «el texto del RD 1680/2011 no contiene la expresión» → se añade que sólo nombra el rango dinámico entre los parámetros de productos musicales (0910, RA 7, e)) | RD 1680/2011, l. 1261 |
| 4 | § 8, tabla de YouTube, fila «Audio» | 6 | Faltaba la salvedad → **«(5.1 surround sound audio is only supported for AAC in RTMP/RTMPS)»** | YouTube 2853702 |
| 5 | § 8, control de calidad, informe | 9 | «El cierre, todavía, es una firma» (presente sobre una hoja de 2015) → «según la hoja de 2015, suele ser una firma» (*usually*) | EBU *Quality Control* |
| 6 | Ficha, Extensión | — | 19.500 → 19.600 | `indice.py` |

Releídos los pasajes cambiados: «su» (de la BT.2100-3), «graban» (las cámaras), «la hoja de 2015» y
«la salvedad» tienen su antecedente; nada cambia en lo copiado.

## Comprobado sin hallazgo

- § 1: ficha del convenio, RA 4 e), RA 5 d), RA 2 c) y la lectura de la lista del RA 5 d) contra
  los §§ (exploración §§ 1 y 4; muestreo § 3; códecs § 6; exhibición § 8).
- § 4: Contrato-programa. La discrepancia del texto (7.1 en la p. 11 frente a 7.2 en el punto 101 y
  en la cláusula quinta) está bien tratada: el tema no da el número de artículo.
- § 8: citas del RD; LE 3.17.1.5 (la cita ya dice «en exteriores… en una unidad móvil»); QC y catálogo;
  YouTube; tabla de entregables; remisiones a los temas 4, 13, 15 y 16.
- Cálculos de la aplicación práctica: 100 × 3.600 ÷ 8 = 45.000 MB, × 6 = 270 GB; 1.920 × 1.080 × 2 ×
  10 × 25 ≈ 1.037 Mb/s, ÷ 100 ≈ 10; 10:52:37:12 − 10:00:00:00 = 00:52:37:12; 100/25 = 4, 50/25 = 2;
  3.840 × 2.160 = 8.294.400 = 4 × 2.073.600, y 7.680 × 4.320 = 4 × UHD; 2^10 = 1.024; 64-940 y 20-984.
- Siglas nuevas (RD, TDT, IPTV, DVD, PPD, AFD, QC, RTMP/RTMPS, CC-BY): presentadas y en su fuente.
- Tablas de Normativa y de normas técnicas: casan con lo citado y con las fichas de 30/04 y 30/02.

## Para la refutación

- Queda como oficio declarado: reencuadre UHD→HD, material 4:3 y vertical, muestreo para el croma,
  reparto de márgenes de la R 103 (control de cámaras / sala), tabla del HDR en la realización,
  definición de entregable, tabla de señales grabadas, lista de entregables, supuesto práctico.
- En lo copiado de 30/04 (§ 2, l. 331) queda «el examen puede preguntar por las dos»; no se toca
  (copiado del común).

Ficheros tocados: el tema y este informe. `indice.py` lanzado una vez sin argumento reescribió los
índices de `temas/general/01` a `06` sin cambiar su contenido (`git status` limpio en ellos).
