# Tema 14 del específico de Operador/a de Sonido · Audio multicanal, Dolby, 5.1, estéreo, mono, downmix y compatibilidad

**Siglas**: RTVA; CSRTV; UIT/ITU-R; UER/EBU; SMPTE; RDD; AES; AES3; SDI; MADI; PCM; DAW; HDTV; DVB; LFE; LU/LUFS; Lo/Ro; Lt/Rt.

Esqueleto para repasar, no resumen: cada línea remite al dato del tema, no lo sustituye.

<!-- indice --><!-- /indice -->

## Audio multicanal

- Sistema universal BS.775-4 (12/2022): 3 frontales + 2 traseros + LFE opcional = 5.1 (resumen BS.775).
- HDTV debe ser compatible con estéreo y mono (BS.775, considerandos).
- Jerarquía de sistemas compatibles útil para intercambio y up/downmix (BS.775, considerandos).
- Notación UIT delanteros/traseros: 1/0 mono; 2/0 estéreo; 3/0; 2/1; 3/1; 2/2; 3/2 = 5.1 sin LFE (BS.775 tabla 2).
- Notación de puntos horizontal.LFE.altura (2.0, 5.1, 7.1, 7.1.2, 5.1.4): convención de oficio, no cifra de la BS.775.
- 5.1.4: 5 horizontales + 1 LFE + 4 de altura, encima no detrás; son canales, no objetos (cálculo/oficio).
- Más canales: UIT-R BS.2051, citada por BS.1770-5; no desarrollada.
- Canal: señal fija por altavoz, decide el mezclador. Objeto: señal + coordenadas, decide el decodificador (oficio).
- Ventaja objetos: misma mezcla se adapta a distinta sala (oficio).
- BS.1770-5 anexo 4: mide audio basado en objetos o mixto canal/objeto.
- Dolby Atmos: combina canales y objetos; rasgo distintivo = objetos en 3D, también sobre el oyente (Guía Dolby Atmos Renderer v3.0).
- Cama (*bed*): lo que no se mueve, en canales fijos; objeto: lo que viaja (Guía Renderer).
- Cama de la configuración básica = 7.1.2, diez canales (Guía Renderer).
- Objetos: hasta 118 mono, o combinación mono/stereo hasta 118 (Guía Renderer).
- Entradas de la estación de trabajo: hasta 128 (64 a 96 kHz) (Guía Renderer).
- 10 (cama) + 118 (objetos) = 128 entradas (cálculo). Cifras de la guía v3.0 (2018), no comprobadas en versiones posteriores.

## Dolby

- Familia de Dolby Laboratories, no un formato (oficio).
- Dos papeles: Dolby E = transporte interno de producción; Dolby Digital (AC-3) = emisión al público (UER *TechReview* 2009-Q1).
- Problema: AES3 = 2 canales/par; 5.1 = 3 pares; equipo de 1 par no admite 5.1 (oficio).
- Dolby E: hasta 8 canales + metadatos en 1 par AES3, en tramas alineadas con vídeo, editable/conmutable sin ruido (UER *TechReview*).
- Definición UER: flujo profesional, no emisión ni consumidor, reducción de datos ligera (UER *TechReview*).
- Hasta 10 ciclos de codificación-decodificación conservando calidad subjetiva (SMPTE RDD 19-2011, documento registrado, no norma).
- Hasta 8 señales en 1 solo flujo AES3 (RDD 19).
- Dolby Digital: hasta 6 canales (UER *TechReview*).
- Trama algo más corta que el cuadro de vídeo → banda de guarda = punto de conmutación (UER *TechReview*; RDD 19: intervalo vertical).
- Progresivo 50/60 fps: Dolby E sincroniza hasta 30 fps; conmuta sólo cada 2 cuadros progresivos, en banda de guarda (RDD 19).
- Retardo: codificar y decodificar añaden 1 cuadro cada uno (40 ms a 25 Hz) (*TechReview*).
- Entrega In-Sync: retardo se compensa al decodificar, con retardo de vídeo equivalente (UER *TechReview*).
- Entrega Advanced: audio adelantado 1 cuadro; tras decodificar queda en sincronía (UER *TechReview*).
- Equipos «Dolby-E-aware» añaden su propio cuadro de retardo → doble retardo de vídeo si se suma otro aparte (UER *TechReview*).
- Prohibido sobre el par codificado: cambiar ganancia, convertir muestreo, ecualizar, partir la trama → corrupción, silencio o chasquido (UER *TechReview*).
- Cortar sí, en la banda de guarda; mezclar no, sin decodificar-procesar-codificar (UER *TechReview*).
- Dolby E transporta metadatos que luego usa Dolby Digital: continuidad estudio-hogar (UER *TechReview*).
- Metadatos AC-3: *dialnorm*, *dynrng*, niveles de downmix de central y envolventes (Tech 3343).
- *dialnorm* −27 = valor de fábrica; −31 = mínimo del sistema → sospechosos, revisar (Tech 3343).
- Recomendación: descartar metadatos externos salvo plena confianza (Tech 3343).
- Dolby ED2: extensión inmersiva del Dolby E, que no lleva Atmos ni información de sonoridad/metadatos ampliados (doc. Dolby ED2).
- ED2 compatible hacia atrás con equipos que dejan pasar/decodifican Dolby E (doc. ED2).
- Hasta 16 canales, 8 por subflujo, 1 par AES3/SDI por subflujo → 2 pares para los 16 (doc. ED2; cálculo).
- ED2 no es códec de emisión; se transcodifica a Dolby Digital Plus con Atmos o Dolby AC-4 (doc. ED2).
- Códecs de entrega (Guía Renderer): Dolby TrueHD sin pérdidas, con versión 7.1 y downmix 5.1/2.0 compatibles con decodificadores TrueHD antiguos.
- Dolby Digital Plus: objetos renderizados a núcleo 5.1/7.1 compatible con decodificadores antiguos; proceso con pérdidas (Guía Renderer).
- Downmix del núcleo: 5.1 con Pro Logic IIx o Lo/Ro; estéreo con ecuaciones estándar de 2 canales (Guía Renderer).

## 5.1

- 5 señales de referencia: L, R, C delante; LS, RS lado/detrás; LFE opcional (BS.775 punto 3).
- Si limita la capacidad, LS+RS pueden fundirse en MS o suprimirse (BS.775 punto 3) → formatos 3/1, 3/0.
- Anexo 2: compatibilidad descendente hasta estéreo/mono es obligatoria («shall be maintained»); mezcla en directo practicable.
- Colocación (BS.775 punto 2): L/R a ±30° en arco de 60°; central al frente, retardo si más cerca; envolventes 100°-120°, sin precisión exacta; envolventes no más cerca que frontales salvo retardo; altura frontal = oídos, pantalla transparente; no transparente → central encima/debajo de imagen; altura envolventes menos crítica; >2 traseros: 60°-150°, simétricos y equiespaciados (nota 4); LS a todos los izquierdos, RS a todos los derechos, menos ganancia cada uno (nota 5).
- LFE: banda limitada hasta 120 Hz nominal; en intercambio internacional y en emisión de TV no debe superar los 120 Hz (BS.775 puntos 4-5).
- Margen preciso: 20-120 Hz (BS.775 anexo 7).
- Grabación con −10 dB de desplazamiento; reproducción compensa con +10 dB; excepción DVD-Audio/SACD sin desplazamiento (BS.775 anexo 7).
- LFE no lleva todo el grave del programa; a menudo fuera del downmix a 2 canales; complemento, no componente esencial (BS.775 anexo 7).
- TV en general no necesita usar el LFE (BS.775 anexo 7).
- Nombre alternativo en otras normas: «low frequency enhancement» (BS.775 anexo 7).
- Tech 3343: LFE excluido de la medida de sonoridad; opción 5.0 si no hace falta margen extra en graves, salvo películas de acción.
- Calibración: ruido rosa a +10 dB dentro de la banda <120 Hz, medido con medidor selectivo en frecuencia, no de banda ancha (BS.775 anexo 7).
- LFE ≠ subgrave: LFE es un canal de la mezcla; el subgrave es un altavoz que extiende la respuesta de otro (BS.775 anexo 7, apéndice 1).
- Gestión de graves doméstica redirige al subgrave los graves de los canales principales (BS.775 apéndice 1).
- AC-3: LFE de 120 Hz y +10 dB; los otros 5 canales, banda completa (BS.775 apéndice 1).
- LFE de Dolby E admite más alta frecuencia que el de AC-3 → llega filtrado paso bajo al público (BS.775 apéndice 1).
- Con PCM lineal, LFE de banda completa → más riesgo de incompatibilidad (BS.775 apéndice 1).

## Estéreo

- Estéreo = 2/0 de la BS.775; compatibilidad exigida hasta estéreo (BS.775).
- Disposición de referencia: L/R en extremos de un arco de 60°, ±30° (BS.775 punto 2).
- Central en 5.1 = centro fantasma del estéreo; al bajar, se reparte a L/R con 0,7071 (−3 dB) cada uno (BS.775 tabla 2; centro fantasma = oficio).
- Correlador de fase (RTW): determina compatibilidad mono de señal estéreo; también revela mala colocación de micrófonos.
- Escala del correlador: −1 a +1; mezclas estéreo normales entre 0,3 y 0,7 (orientación fabricante RTW, no norma).

## Mono

- Mono = 1/0 de la BS.775; último peldaño de la jerarquía (BS.775).
- Envolvente mono (MS): LS+RS fundidos, se envía a los dos altavoces LS y RS (BS.775 punto 3).
- MS calculado desde 3/2: S = 0,7071 LS + 0,7071 RS (BS.775 tabla 2).
- Downmix a mono: C = 0,7071 L + 0,7071 R + 1,0000 C + 0,5000 LS + 0,5000 RS; LFE fuera de la ecuación (BS.775 tabla 2, anexo 4).
- 0,7071 ≈ −3 dB; 0,5 ≈ −6 dB (cálculo).
- Suma a mono = suma de señales; en contrafase se restan o cancelan (oficio).
- Comprobación: escuchar en mono con el botón de la mesa y mirar el correlador; fase/polaridad se resuelve en origen (oficio).

## Downmix

- Downmix = mezcla reducida (5.1 a estéreo o mono); en producción (manual) o en receptor, según metadatos (Tech 3343).
- BS.775 punto 7: capacidad de downmix antes de la transmisión o en el receptor, con las ecuaciones de la tabla 2.
- Coeficientes a estéreo (3/2 origen): L = 1,0000 L + 0,7071 C + 0,7071 LS; R = 1,0000 R + 0,7071 C + 0,7071 RS (BS.775 tabla 2, anexo 4).
- Reglas de la tabla: el central sin altavoz central va a L/R a 0,7071; los envolventes sin traseros van a su lado a 0,7071; con un solo trasero se suman en S a 0,7071 cada uno (BS.775 tabla 2).
- El efecto real depende también de las leyes de panorámica y las características del micrófono (BS.775 tabla 2, nota).
- Sin metadatos fiables, la UER toma como partida los coeficientes de BS.775-2: frontales 0 dB, C/LS/RS −3 dB (Tech 3343).
- Lo/Ro: combina los canales directamente con los coeficientes de downmix (Tech 3343).
- Lt/Rt: suma a mono los envolventes con desfase de ±90°, mejor compatibilidad con matrices tipo Dolby Pro Logic (Tech 3343).
- UER recomienda Lo/Ro por defecto («Preferred Downmix Method»): Lt/Rt es más impredecible en sonoridad y altera más el sonido (Tech 3343).
- Sonoridad del downmix depende de: método, coeficientes, contenido central/envolventes, correlación entre canales, limitación de seguridad (Tech 3343).
- Coeficientes posibles citados: +3, +1,5, 0, −1,5, −3, −4,5, −6 dB (Tech 3343).
- BS.1770 pesa los envolventes +1,5 dB en 5.1; el downmix por defecto los baja −3 dB → diferencia sistemática de 4,5 dB (Tech 3343).
- Con divergencia total del central, downmix estéreo puede sonar hasta 3 LU más que la mezcla envolvente (Tech 3343).
- Un 5.1 a −23 LUFS no garantiza downmix a −23 LUFS: medir cada versión entregada (Tech 3343/oficio).
- Dolby Digital: coeficientes iniciales gruesos (−3/−4,5/−6 dB central); Extended BSI y DVB TS 101 154 dan pasos finos; decodificadores antiguos usan los gruesos del perfil 1 (Tech 3343).
- Evitar saturación del downmix con procesador de dinámica antes, no con reducción estática de nivel (Tech 3343).
- Un upmix nunca debe sustituir a una mezcla multicanal discreta original (Tech 3343).
- BS.775 punto 8/anexo 5: conversión ascendente antes de transmisión o en receptor.
- Pautas anexo 5: mono con 3 frontales → sólo central; mono con 2 → L/R con −3 dB; estéreo con 3 frontales → sólo L/R, sin central; sin señal envolvente → envolventes no se activan; una señal envolvente en varios altavoces → decorrelación y atenuación; canal de datos transmite periódicamente el modo de transmisión.

## Compatibilidad

- Compatibilidad descendente obligatoria hasta estéreo y mono (BS.775 anexo 2, «shall be maintained»).
- Punto 6: compatibilidad, si se necesita, con receptores existentes y de bajo coste, métodos del anexo 3.
- Anexo 3: *simulcast* (servicio 2/0 en paralelo al 3/2, discontinuable después) o matrices de compatibilidad (L/R llevan A/B compatibles; canales extra T, Q1, Q2; menos datos añadidos).
- Receptor de bajo coste con matriz: sólo necesita A/B; en sistema 3/2 discreto, combina con ecuaciones del anexo 4 (tabla 2), downmix antes de la síntesis del decodificador.
- Tres planos de compatibilidad (oficio): canales (downmix, escucha, correlador); transporte (Dolby E en 1 par AES3; ED2 compatible hacia atrás); receptores (metadatos correctos; decodificador antiguo usa coeficientes gruesos del perfil 1).
- Comprobación: correlador multicanal RTW asegura que la mezcla suene bien reducida a estéreo/mono; medir sonoridad de cada versión entregada.
- Producir señal multicanal compatible (oficio, 7 puntos): 1) monitorización 5.1 calibrada (colocación BS.775); 2) central = diálogo en TV; 3) LFE con criterio: nada esencial sólo ahí, en TV no suele hacer falta, opción 5.0 sin margen extra; 4) comprobar downmix (escucha, correlador, sonoridad); 5) cuidar metadatos: *dialnorm*, *dynrng*, niveles de downmix y método preferido Lo/Ro, vigilar −27/−31; 6) respetar transporte Dolby E: no tocar ganancia/muestreo/ecualización, decodificar-mezclar-recodificar, compensar retardo una vez; 7) no sustituir el original con un upmix.
