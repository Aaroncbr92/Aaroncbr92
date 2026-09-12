# Esquema · Tema 5 del específico de Edición, Montaje y Procesos Audiovisuales · Soportes, formatos, grabación e ingesta

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio · `[plan]` = plantilla
oficial, **sin documentación de fabricante que la contraste**.

**Siglas**: el formato avanzado de autoría (**AAF**, *advanced authoring format*);
los contenedores de Apple (**MOV**), de la familia MPEG (**MP4**) y de Microsoft (**AVI**), y el
contenedor libre **OGG**; el formato gráfico de intercambio (**GIF**), el mapa de bits (**BMP**),
los gráficos de red portátiles (**PNG**) y el formato del grupo conjunto de expertos en fotografía
(**JPEG**); la lista de decisión de edición (**EDL**, *edit decision list*); el formato de emisión
**IMX**; la cinta lineal abierta (**LTO**, *linear tape open*); el formato de intercambio de
material (**MXF**, *material exchange format*), con sus perfiles operacionales **Op1a** y
**Op1b-Atom**; la modulación por impulsos codificados (**PCM**, *pulse-code modulation*); el disco
profesional de esa misma casa (**XDCAM**); el lenguaje de marcado extensible (**XML**).

**Cabecera.** Enunciado: «2.2. Soportes y formatos · 2.4. Documentación y catalogación de ficheros ·
4.1 a 4.4. Equipos y soportes de grabación, disco óptico y disco duro, ingesta, encapsulado» · **8
preguntas** · **CINCO descansan sólo en la plantilla**: es el punto con más afirmaciones de quinto
nivel de la ocupación.

<!-- indice -->

## Índice

- [Esencia, códec, contenedor y proyecto](#esencia-códec-contenedor-y-proyecto)
- [El AAF](#el-aaf)
- [El MXF y sus perfiles](#el-mxf-y-sus-perfiles)
- [Los formatos de imagen fija](#los-formatos-de-imagen-fija)
- [El XDCAM y sus dos preguntas de catálogo](#el-xdcam-y-sus-dos-preguntas-de-catálogo)
- [El audio del HD422](#el-audio-del-hd422)
- [La LTO](#la-lto)
- [La ingesta](#la-ingesta)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Esencia, códec, contenedor y proyecto

| Concepto | Qué es | Ejemplos |
|---|---|---|
| **Esencia** | **El material en sí** | Cuadros y muestras |
| **Códec** | **Cómo se COMPRIME** | H.264, ProRes, DNxHD, JPEG 2000, PCM |
| **Contenedor** | **Cómo se EMPAQUETA** con sus metadatos | **MXF**, MOV, MP4, AVI |
| **Metadatos** | Datos sobre el material | Van dentro del contenedor |
| **Proyecto** | **Las DECISIONES de montaje**, sin esencia | **AAF**, EDL, XML |

- **LAS CUATRO FILAS SE PREGUNTAN**, y **la confusión entre ellas es el mecanismo de tres de las ocho
  preguntas.**

## El AAF

- **PREGUNTA 14** · **Un AAF permite INTERCAMBIAR MEDIOS DIGITALES Y METADATOS entre distintos
  sistemas, plataformas y aplicaciones.**
- **PARA QUÉ DE VERDAD**: **para sacar un montaje de un programa y meterlo en otro** —a la mezcla de
  sonido, al etalonaje—: **qué clips, en qué orden, con qué cortes, niveles y efectos**, y
  opcionalmente **la esencia**.

| Formato | Qué lleva | Límite |
|---|---|---|
| **EDL** | **Sólo la lista de cortes** | **Una pista de vídeo**; sin efectos |
| **AAF** | **Cortes, pistas, niveles, efectos, metadatos** y puede llevar esencia | El más completo |
| **XML** | Lo mismo, en la variante de cada casa | **No es universal** |

- **LAS TRES FALSAS SON LA MISMA FRASE CON EL VERBO CAMBIADO**: «normalizar la señal para la edición» ·
  «…para la emisión» · «ajustar niveles». **El AAF LLEVA los niveles, NO los ajusta.**
- **LA PALABRA QUE RESUELVE ES «INTERCAMBIAR»**: **el AAF es un vehículo, no una herramienta.**

## El MXF y sus perfiles

| Perfil | Cómo empaqueta | Dónde |
|---|---|---|
| **Op1a** | **TODO en un solo fichero** | **Emisión, intercambio, grabación en cámara** |
| **Op-Atom** | **Un fichero POR PISTA** | **El entorno de edición de Avid** |

- **PREGUNTA 88** · `[plan]` · **XDCAM HD 50i 4:2:2 está encapsulado en MXF Op1a.** Coherente: **lo que
  sale de una cámara es un fichero AUTÓNOMO**, no pistas sueltas.
- **LAS FALSAS**: **DNxHR** = **es CÓDEC, no encapsulado** · **MXF Op1-Atom** = **el contenedor
  correcto con el perfil equivocado: es la trampa buena** · **IMX** = **formato de definición estándar,
  anterior**.

## Los formatos de imagen fija

| Formato | Qué es |
|---|---|
| **GIF** | Imagen, 256 colores, **transparencia BINARIA** |
| **BMP** | Imagen, **sin compresión** |
| **PNG** | Imagen, **sin pérdida, con ALFA COMPLETO**. **El profesional para rótulos** |
| **JPEG** | Imagen, **con pérdida**; **degrada los bordes duros** |
| **OGG** | **NO ES IMAGEN: contenedor multimedia de audio y vídeo** |

- **PREGUNTA 34** · **El que NO es imagen digital es OGG.**
- **POR QUÉ EL PNG EN GRAFISMO**: **es el único que junta compresión sin pérdida y alfa de ocho
  bits**. **El GIF tiene transparencia BINARIA** —opaco o transparente, **sin grados**— y por eso **sus
  bordes salen dentados sobre el vídeo**.

## El XDCAM y sus dos preguntas de catálogo

- **QUÉ ES**: **grabación en DISCO ÓPTICO profesional**, nombrada en el propio anexo. Sustituyó a la
  cinta en informativos.
- **SUS DOS VENTAJAS**: **acceso no lineal** —se salta a cualquier punto **y se vuelca mientras se
  graba**— y **ficheros, no señal**: lo del disco **ya es un MXF con metadatos**, así que **la ingesta
  es una copia**.
- **PREGUNTA 22** · `[plan]` · **Para no perder nada al cambiar de disco, el menú 150 (*rec mode*) va
  en «D.exc».** Falsas: Normal, C.rec, Continuous.
- **PREGUNTA 90** · `[plan]` · **La capacidad del disco citado es de 4 HORAS.** Falsas: 23 minutos, 8
  horas, 95 minutos.
- **LO QUE SÍ SE SOSTIENE**: **el concepto de memoria intermedia durante el cambio de soporte** —el
  grabador sigue escribiendo internamente y vuelca al entrar el disco nuevo— **y la regla de la
  capacidad**: **minutos = capacidad en bits ÷ tasa del formato.** **Un mismo disco da el doble de
  minutos a la mitad de tasa**, y por eso la pregunta especifica el formato.

## El audio del HD422

- **PREGUNTA 20** · `[plan]` · **4 U 8 canales, códec PCM, 24 bits.**
- **QUÉ SIGNIFICA**: **«4 u 8» = el formato admite las dos configuraciones** · **PCM = audio SIN
  COMPRIMIR** · **24 bits ≈ 144 dB de rango dinámico**.
- **POR QUÉ PCM**: **el audio de producción NO se comprime**, porque va a pasar por mezcla,
  ecualización y compresión de dinámica, **y cada paso sobre audio comprimido acumula artefactos**.
- **LA TRAMPA**: la opción «8 canales, PCM, 24 bits» **acierta códec y profundidad y falla en que el
  formato admite DOS configuraciones**. **La correcta es LA MÁS COMPLETA, no la más concreta.**

## La LTO

- **PREGUNTA 21** · **Una LTO es una TECNOLOGÍA DE ALMACENAMIENTO EN CINTA MAGNÉTICA DE ALTA
  CAPACIDAD, POTENTE, ESCALABLE Y ADAPTABLE.**
- **POR QUÉ SIGUE USÁNDOSE**: **el coste por terabyte más bajo** · **una cinta guardada no consume
  nada** · **décadas de vida útil** · **escala por unidades baratas** · **una cinta fuera de la
  biblioteca no está en la red** y no la alcanza un ataque.
- **SU DESVENTAJA, QUE FIJA SU USO**: **acceso SECUENCIAL y lento.** **No es almacenamiento de trabajo:
  es ARCHIVO.**
- **LAS TRES FALSAS**: «láser azul» → **confunde la cinta con el disco óptico** · «capacidad baja y no
  regrabables» → **las dos mitades falsas** · «más de 6 pulgadas de ancho» → **absurdo: la cinta LTO es
  de MEDIA pulgada**.
- **AVISO DE VOCABULARIO**: **«abierta» NO se refiere al carrete**: es **una norma abierta**, fabricada
  por varias casas. **La opción a) juega con ese equívoco.**

## La ingesta

| Forma | Qué es |
|---|---|
| **De fichero** | Copiar lo que ya viene en fichero, **con comprobación de integridad** |
| **En directo** | **Grabar una señal que entra ahora** |
| **Programada** | **Grabar automáticamente en un horario previsto** |

- **PREGUNTA 23** · `[plan]` · **Cuatro opciones de recurrencia: None / Daily / Weekly / Monthly.**
  **Las tres falsas son la misma lista con una o dos entradas quitadas: hay que saber que son CUATRO.**
- **POR QUÉ CUATRO**: **son las cuatro periodicidades de una parrilla** —el informativo de agencia
  todos los días, la tertulia los martes y jueves, el resumen el primer lunes—. **Sin recurrencia,
  alguien tendría que programar cada día a mano.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 14 | Qué es y para qué sirve un AAF | b) Intercambiar medios y metadatos ✔ |
| 20 | Audio en XDCAM HD422/50i | b) 4 u 8 canales, PCM, 24 bits ✔ **·** sólo con la plantilla |
| 21 | Qué es una LTO | b) Cinta magnética de alta capacidad y escalable ✔ |
| 22 | Modo del menú 150 al cambiar de disco | c) D.exc ✔ **·** sólo con la plantilla |
| 23 | Opciones de recurrencia de la ingesta | c) None / Daily / Weekly / Monthly ✔ **·** sólo con la plantilla |
| 34 | Cuál NO es imagen digital | c) OGG ✔ |
| 88 | Encapsulado de XDCAM HD 50i 4:2:2 | c) MXF Op1a ✔ **·** sólo con la plantilla |
| 90 | Capacidad del disco XDCAM citado | b) 4 horas ✔ **·** sólo con la plantilla |

**Las ocho oficiales son correctas** y **cinco descansan sólo en la plantilla**: **las cinco que citan
una máquina, un soporte o un programa por su modelo.** · **Aviso de estudio**: **las tres
conceptuales —14, 21 y 34— se contestan entendiendo la diferencia entre contenedor, códec, proyecto e
imagen fija. Las cinco de catálogo se memorizan.** **No se preparan igual: conviene separarlas.**
