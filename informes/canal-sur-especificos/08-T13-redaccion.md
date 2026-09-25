# Puesto 08 · Tema 13 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`
(≈7.240 palabras según `indice.py`; 5 epígrafes `##` en el orden del enunciado —mochilas, enlaces,
*streaming*, señales IP, coordinación con control— precedidos de «Producción móvil y transmisión»,
más normas técnicas, huecos y trazabilidad; 23 `###`). Escrito por partes, guardando cada `##`.
Índice con `indice.py`. `refutar_prosa.py`: queda 1 aviso no aplicable (IP en el título, antes del
bloque de siglas; igual que en el tema 3). Sin norma jurídica: no proceden las lentes de norma.
Agrupación: 8/13 «nuevo». Reúso RTVE (imagen-iluminacion.tsv): 60 %.

## Fuentes (leídas por mí el 24-09-2026)

- **Libro de estilo de Canal Sur** (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`):
  Introducción; 4.4 (l. 2619), 4.4.1 (l. 2640), 4.4.4 paso 2 (l. 2684-2688); 5.6 (l. 3012);
  8.1 punto 6 (l. 4039); 8.3 (l. 4136); 8.3.2 (l. 4179, 4196).
- **Contrato-programa 2024-2026** (`contrato-programa-2024-2026-boja-245-2023.txt`): puntos 45 y 46
  (apartado 3.5, l. 1288-1325) y punto 103 (apartado 3.19, l. 2089).
- **UIT-R SNG.770-2** (`fuentes/normas-tecnicas/UIT-R_SNG.770-2.txt`): considerando g) (l. 140-144),
  recomienda 8 y 9 (l. 198-203), anexo 1, 1.1 (l. 225).
- **SMPTE ST 2110-10:2022** (`.txt` local): introducción (l. 146-163), cl. 1 (l. 166-171), 6.3
  (l. 361), 7.2 (l. 403-415), 8.5 (l. 697). **ST 2110-20:2022** cl. 1 (l. 138). **ST 2110-30:2025**
  cl. 1 (l. 80-83) y portada «Revision of SMPTE ST 2110-30:2017». Índice ST 2110 (local).
- **SRT**: README y `API-socket-options.md` del repositorio Haivision (descargados con curl) y
  draft-sharabayko-srt-01 (texto IETF: cabecera, resumen, 1.1, 1.2, tabla 2). El estado «expirado /
  Independent Submission» se toma de la investigación (datatracker), no releído por mí.
- **NMOS** (`specs.amwa.tv/nmos/`) y **NDI** («What is NDI», «Discovery & Registration»): WebFetch
  (extractor que resume; citas entrecomilladas por el extractor, no cotejadas en HTML).
- **LiveU LU800** (`fuentes/fabricantes/LiveU_LU800_ficha.txt`) y **ATEM** (manual es, l. 1461,
  2674, 7645).

## Copiado del común

Literal de temas cerrados de Canal Sur (no se re-verifica):

- De `34-redactor-a/10-coberturas-en-directo.md`, § 6 «Con los equipos técnicos: cómo llega la
  señal»: la tabla de cinco vías y las viñetas *Satélite* y *Mochila*, en «Enlaces · Las vías de la
  contribución». La frase de entrada es mía (la original se dirigía al redactor).
- De `34-redactor-a/14-periodismo-digital-multiplataforma.md`: el párrafo «Quién lo organiza: según
  el punto 46…» hasta «…mediante acuerdos», en «*Streaming* · El *streaming* en Canal Sur». La frase
  que lo precede (antecedente: cláusula tercera, apartado 3.5) es mía y cotejada; lo he releído
  igualmente en el BOJA.

## Copiado de RTVE (adaptado: se verifica)

Quitadas la negrita de énfasis, las respuestas oficiales, los números de pregunta, las tablas de
opciones falsas y los «datos que el examen ha preguntado»:

- `informacion-grafica/09` § 1 (tabla de caminos y distinción directo/diferido), § 2 (qué permite
  y qué no la mochila; retardo), § 3 (vías de conexión; quitado el distractor ETT).
- `realizacion/16` § 5 (sólo la aritmética imagen/ms y la regla «todo se retrasa hasta el más
  lento»; quitado el caso de la pregunta 34) y § 8 (definición y tabla de modos de *streaming*;
  quitado IPS/DTV como distractores).
- No se usan § 4-6 de IG/09 (robotizadas y realidad aumentada: temas 3 y 4) ni el resto de
  realización/16.

## Nuevo

Todo lo de LE-CS, Contrato-programa (punto 103), SNG.770-2 (considerando g, recomienda 8),
ST 2110, PTP, NMOS, NDI, SRT, LU800 (ficheros, producción remota, canales de coordinación),
tabla de canales cámara-control, procedimiento y supuesto práctico (oficio declarado).

## Avisos para verificación

1. El tema 3 (no cerrado) contiene texto casi igual en «Cómo sale la señal», «La prueba de la
   señal» y «La coordinación con el control desde la mochila»; aquí no se ha copiado de él, sino de
   las fuentes y de 34/10.
2. Fechas de aprobación de ST 2110-10 (28-03-2022) y -20 (14-12-2022) y «revisa la de 2017» de la
   -10: tomadas de la investigación (URL de la biblioteca SMPTE); comprobar.
3. La ficha LU800: «the lowest latency» sale de la frase «…reliability with the lowest latency».
4. La cita del Libro de estilo 8.1 punto 6 la da el tema 34/10 como «8.1.6»; aquí «8.1, punto 6»
   (es el punto 6 de la lista de 8.1).

## Ficheros tocados

- Escrito: el tema 13 y este informe. Temporales de SRT en el scratchpad (fuera del repositorio).

## Diez preguntas tipo test y comprobación

1. (Mochilas) ¿Qué afirmación NO es correcta sobre una mochila? a) aprovecha la capacidad de las
   redes móviles; b) permite emitir en directo en zonas con cobertura; c) reduce costes;
   **d) garantiza transmisiones 100 % estables y sin retardo con poca cobertura**. → Entera
   («Lo que una mochila no promete»).
2. (Mochilas) ¿Por qué vías se conecta una mochila? **Tarjetas de telefonía, wifi y cable de red**.
   → Entera («Por dónde se conecta»).
3. (Mochilas, práctica) El retorno de audio del periodista en un directo con mochila se da en:
   **N-1, sin su propia voz**. → Entera («El retardo…» y «Los canales…»).
4. (Enlaces) Según UIT-R SNG.770-2, el terminal DSNG debe poder manejarlo un equipo de: **no más de
   dos personas en un tiempo razonablemente corto (p. ej., 1 h)**. → Entera.
5. (Enlaces) La contribución es: **el transporte de la señal hacia el centro de producción para
   seguir trabajando con ella**. → Entera (tabla contribución/distribución).
6. (*Streaming*) El modo más adecuado para distribuir un directo por Internet: **la transmisión por
   secuencias**, no la descarga progresiva. → Entera.
7. (*Streaming*) SRT: **protocolo abierto sobre UDP con ARQ; no es norma ni RFC de la IETF**. → Entera.
8. (Señales IP) En la familia SMPTE ST 2110, el audio PCM lo transporta la parte: **ST 2110-30**
   (el vídeo sin comprimir, la -20; no existe la -50). → Entera.
9. (Señales IP) El reloj común de ST 2110 se distribuye con: **PTP, IEEE 1588-2008, perfil
   ST 2059-2**; y NMOS IS-07 es **«Event & Tally»**. → Entera.
10. (Coordinación, práctica) Según el Libro de estilo de Canal Sur, el equipo que debe prever todo
    en un directo es el **coordinado de producción, realización, enlaces e informativos**, y un
    retraso fuera del centro se comunica **a los editores**; y a 25 fps, dos imágenes de retardo
    son **80 ms**. → Entera («Quién coordina…», «Qué pide la casa», «El retardo…»).

Resultado: las diez se contestan enteras con el tema; no ha hecho falta ampliar.
