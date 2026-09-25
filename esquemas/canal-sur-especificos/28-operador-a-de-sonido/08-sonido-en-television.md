# Tema 8 del específico de Operador/a de Sonido · Sonido en televisión

**Siglas**: RTVA; CSRTV; UER/EBU; UIT/ITU; RDSI/ISDN; RTC/PSTN; IP; RTP; UDP; VoIP; SDI; GPIO; dB; dBFS; dBTP; LU; LUFS; MSL; SPL; dBC; LFE; PML; IFB; N-1; PL; CCU; UM/OB; XLR; DC; AKA.

Esqueleto para repasar, no resumen: cada línea remite al dato del tema, no lo sustituye.

<!-- indice --><!-- /indice -->

## Las tres familias del control

- Programa (al espectador), retornos (N-1, IFB, monitores plató), intercomunicación (equipo) — nunca mezcladas (oficio).
- Tech 3347 § 1.1: intercom conecta estudios, reportero y UM en tiempo real.
- Tech 3347 § 1.2: 3 tipos de señal — pure intercom (dúplex/conferencia); mix-minus (semidúplex o vuelta de dúplex) = N-1; commentary feed (semidúplex o ida de dúplex).
- Contribución = hacia el centro, calidad alta, mínimo retardo; distribución/emisión = hacia el espectador (oficio).
- Control central = matriz que encamina, sincroniza, adapta y vigila señales exteriores (oficio).

## Intercom

- Dos arquitecturas: línea compartida (todos se oyen a la vez, típica de cámaras) y matriz con paneles (realización) (oficio).
- Clear-Com (partyline, feb-2018): partyline = 2 hilos, mismo camino ida/vuelta; siempre dúplex; no privada. Ejemplo: cámaras en PL.
- Cableado Clear-Com XLR: pin 2 = DC ±15V; pin 3 = audio dúplex; pin 1 = masa. Propio de este fabricante, no generalizable.
- 4 hilos: todo circuito empieza a 4 hilos (auricular/micro separados); matriz, códec, mayoría de equipos así (Clear-Com).
- Híbrido: convierte 2↔4 hilos; calidad = atenuación transhíbrida; ajuste = nulling; digitales con auto-nulling (Clear-Com).
- Mala separación → la voz vuelve por la escucha → riesgo de oscilación/«howling» (Clear-Com); mismo problema que resuelve el N-1.
- Híbrido también interfaz con telefonía (Clear-Com); híbrido telefónico de radio = tema 7.
- Matriz: central del intercom, conecta paneles, PL, cámaras, teléfono, IP (Tech 3347, sin definirla).
- Confidente: escucha permanente de un punto sin pulsar tecla; distinto de grabar, conferenciar y silenciar-salvo-uno (oficio).
- Puntos de un panel según usuario (oficio); señal internacional: no se emite, se entrega; sin canal de continuidad propio.
- IP sustituye ISDN/PSTN (Tech 3347 § 1.1); RTP sobre UDP obligatorio (§ 2.2); interfaz en matriz, periférico, externo o software (§ 1.3).
- Códecs (§ 3): G.711 y G.722 obligatorios (64 kbit/s); Speex y G.729 recomendados. G.722 muestrea a 16 kHz (Tech 3326).
- Retardo: EBU no lo fija (§ 1.5); encuesta, no requisito: <100 ms remoto, <50 ms interno; remite a UIT-T G.114 (no leída).

## IFB

- Clear-Com (16-03-2021): IFB = intercom simplex que manda programa + interrupción (cue) para que el talento escuche.
- 3 elementos (Clear-Com): Program Audio (lo pone el operador); Interrupt/Cue Audio (orden de realización/regidor); Dip or Mute control (baja o corta programa al interrumpir).
- Equipo: auricular, caja externa de volumen propio, fuente de programa, puesto de control (Clear-Com).
- IFB ≠ intercom: IFB es simplex, sólo lo lleva presentador/reportero/comentarista; nunca sale al aire, pero el presentador sí, y depende de lo que oye (oficio).
- Escucha del control (Clear-Com): altavoces de sala se silencian/atenúan al activarse el IFB, evita que el programa de sala entre por el micro del que interrumpe. Mismo principio que el DIM (tema 4).
- 3 usos (Clear-Com): entradas al presentador de plató; realizador con reporteros y presentador; deportes, muchos canales de IFB en campo y cabinas.
- Reportero exterior con retardo → oye N-1 (siguiente epígrafe); mezcla del presentador la fija cada producción (oficio).

## Retornos

- Retorno = todo lo que el control devuelve para oír/trabajar: programa o N-1 por IFB, monitores de plató, retorno de cámaras (oficio).
- N-1: mezcla sin la propia señal del receptor (N fuentes → N-1); evita que se oiga a sí mismo con eco del enlace (oficio).
- Cada envío auxiliar tiene su propio N-1; varias conexiones = varias N-1 distintas (oficio).
- Tech 3347 § 1.2: mix-minus = vía única (semidúplex) o vuelta de comunicación dúplex.
- N-1 no quita el retardo, quita la señal insoportable con ese retardo; no quita órdenes (intercom); no evita acople de plató (oficio).
- Retorno de programa (ST, estéreo): para quien NO está en antena. N-1: para quien SÍ está en antena (oficio).
- Montaje del N-1: envío/bus con todas las fuentes menos la del oyente; previo al fader = no se mueve con él; posterior = sigue la mezcla (tema 4).
- Soundcraft: envíos posteriores → «foldback mix levels will alter with every input fader change».
- Yamaha (CL V5): función Mix Minus quita un canal específico de los buses MIX/MATRIX automáticamente.
- Conexión redundante (2 líneas): cada retorno debe quitar las DOS líneas si ambas llevan la misma voz, o la voz vuelve por la no quitada (oficio).
- Comprobación práctica: abrir la línea de reserva como si fuera a antena y preguntar al reportero si se oye a sí mismo; repetir con la principal (oficio).
- ATEM: salidas SDI con modo N-1 propio; silencia el audio de una entrada en el retorno para que el presentador no se distraiga con su voz retrasada.
- Retorno del plató: altavoces para público/presentadores y monitores de músicos, envíos previos (oficio); problema inverso al N-1: realimentación si micros abiertos apuntan a los altavoces (mínimo del micro = tema 3; filtro de acople = temas 5 y 10).

## Mezcla para emisión

- Mezcla para emisión = salida de programa hacia continuidad y difusión; única familia que oye el espectador y que cumple R 128 (oficio).
- Directo: una sola vez, sin corregir después; grabado: se revisa antes de entregar (oficio).
- R 128 aplicada por Tech 3343-2023: objetivo −23 LUFS; tolerancia postproducción ±0,2 LU (desde R 128 revisión 3, 2020); tolerancia directo ±1,0 LU («challenging... a matter of luck»); pico verdadero máximo −1 dBTP en producción.
- Ley 13/2022 art. 121.4: «El nivel sonoro de las comunicaciones comerciales audiovisuales no puede ser superior al nivel medio del programa que le precede» — prohibición, sin unidad ni método.
- Art. 121.1: comunicación comercial = publicidad, patrocinio, televenta, emplazamiento de producto y autopromoción.
- Práctica que cumple el 121.4: normalizar en torno a −23 LUFS (oficio); § 9.1: género muy citado por molestia; BCAP (UK) y CALM Act (EEUU) legislan sobre ello.
- Contenido corto (≤2 min, típico <60 s), R 128 s1 vía § 9.1: sonoridad −23,0 LUFS; pico −1 dBTP; MSL −18,0 LUFS (+5,0 LU); rango de sonoridad no aplicable. MSL = máximo de corto plazo (3 s); recomendado, no impuesto.
- Excepción § 9.1: fondos/sonidos bajos intencionados, por debajo del objetivo, identificados.
- Tech 3343 § 2.4/3.2: mezclar «only by ear» con ganancia de escucha fija; si antes se mezclaba a −20 LUFS, subir la escucha 3 dB (§ 3.1).
- Escucha de referencia (§ 8.2): 73 dBC SPL, ruido 500-2.000 Hz a −23 LUFS, ponderación C lenta; entre altavoces ≤1 dB (frontales <0,5 dB); LFE +10 dB sobre banda equivalente de canal principal.
- Deportes (§ 3.5.1): goles en últimos 15 min disparan la integrada; comentaristas algo por debajo, p. ej. −24 LUFS.
- Espectáculos (§ 3.5.2): público tan importante como el presentador; en musical manda la música; zona cómoda ±3/−5 LU.
- Procesador de sonoridad de seguridad (§ 2.4): con contenido conforme, Bypass o sólo limitador de pico, por GPIO o red de control.
- En directo puede «harmonizar la fuente»; aviso literal: «Don't produce loudness sausage!».
- Tono de alineación (§ 8.1 / R 68): 1 kHz a −18 dBFS, en medidor de pico; PML de −9 dBFS de BS.645 obsoleto con el pico verdadero.
- Comprobación de salida (oficio): alineación (tono −18 dBFS hasta control central); escucha calibrada fija; medidor a cero al empezar; limitador a −1 dBTP; estéreo/mono (temas 13-14); cada N-1 e IFB probado.

## Coordinación con realización

- Libro de estilo (6.5, p. 92): realización, territorio de los técnicos; el realizador responde máximo de la imagen y la calidad de emisión; participa con editores y productores.
- El realizador pide, juzga y responde del sonido de emisión sin operarlo; el operador ejecuta y responde de la corrección técnica (oficio).
- Reparto (oficio): realizador = contenido/forma; productor = medios (dinero, tiempo, contratos, permisos); coordinador de estudio = agenda de plató, no gasto; equipo técnico = ejecución, no autoriza jornadas.
- Medios → producción; contenido → realización (oficio).
- Libro de estilo (8.3): «La improvisación no tiene cabida»; equipo coordinado (producción, realización, enlaces, informativos) prevé todo lo planificable, con «la interrupción del sonido de retorno» como ejemplo de eventualidad.
- Libro de estilo (8.1, punto 6): directos pactados entre productor, cámara, técnicos de enlace, presentador, edición, realizador (lista abierta, «…»); sonido no figura por nombre, pero le alcanza como técnico involucrado (lectura del texto). Le toca conocer: quién interviene, vía de cada conexión, retorno de cada uno, músicas/vídeos con sonido, quién da paso (oficio); todo, si es posible, en la escaleta.
- Libro de estilo (8.3.2): «Terminado el directo, en la despedida sólo habla el presentador» — micro del reportero se cierra al retomar el presentador, retorno se mantiene hasta que el control da la conexión por terminada (oficio).
- Oficio, sin norma: se anticipa y se ejecuta (aviso + orden); se confirma por intercom sin discutir en directo; se sigue la imagen (tema 6); se avisan incidencias con la solución si la hay.
- Procedimiento del directo (oficio): preparación (escaleta, mesa, escenas, buses N-1/IFB, intercom); prueba (tono, micrófonos, cada conexión); ensayo (escucha fija, guardar escena); en antena (mezcla, medidor, retornos); incidencia (reserva, aviso); final (retornos hasta cierre, anota sonoridad e incidencias).
- Supuesto práctico (oficio, con fuentes citadas): presentador con 2 micros de corbata, uno abierto (tema 6); N-1 del reportero sin mochila ni reserva (misma voz); IFB con interrupción y atenuación de escucha (Clear-Com); intercom con realización y control central; prueba previa de nivel, retorno y retardo; en antena −23 LUFS ±1 LU directo, pico ≤−1 dBTP; si cae la mochila entra la reserva con retorno ya preparado; despedida sólo la habla el presentador.

## Cámaras

- Operador de estudio con auriculares de intercom; órdenes de realizador y control de imagen (ATEM, puesta en marcha Constellation 8K).
- Retorno de cámara = imagen de programa devuelta al visor/monitor; en ATEM también gobierna la cámara (URSA Mini, Studio Camera) por la SDI de retorno.
- Audio del retorno en modo N-1 (remite a «Retornos»); fuera de plató cambian los caminos, no los canales (oficio).
- Cámara en calle (oficio): piloto por mochila o cable; retorno por mochila/receptor/teléfono con audio en N-1; intercom por mochila/cable/teléfono; control remoto por red si el equipo lo permite.
- Piloto (tally), ATEM: enciende luz roja para saber que está al aire; botón CALL hace parpadear el piloto para llamar la atención del cámara.
- Intercom de cámaras: normalmente todos en una PL con el realizador (Clear-Com, ejemplo camera PL); sin diseño común entre fabricantes.
- Aislamiento de cámara (Clear-Com): control de imagen o director técnico habla en privado con un cámara para ajuste/mantenimiento sin interferir en la comunicación de los demás.
- Conexión CCU-matriz, 3 reglas Clear-Com: mejor 4 hilos (sin híbrido) que 2; interfaz individual por cámara (en paralelo empeora la impedancia de la PL); conector de 3 polos de la CCU es PL de 2 hilos (+/hot, −/cold) con el común como masa, no 3 hilos reales.
- Sonido de cámaras: micrófono capta ambiente; viaja embebido en SDI, se desembebe para la mesa (tema 11); cada cámara es una fuente más, con su canal (oficio; reparto del Libro de estilo = tema 6).

## Lo que este tema no da

- Intercom, consolas, códecs y procedimientos concretos de CSRTV en sus controles, UM y centros territoriales: no consta en documento publicado.
- Matriz/panel en documentación de fabricante: no leída; lo dado es oficio.
- Fraseología de órdenes y protocolos de ensayo realización-sonido: sin norma, costumbre de oficio.
- Cableado de intercom de otros fabricantes y de cada fabricante de cámaras: sin diseño común.
- UIT-T G.114 y UIT-R BS.645: citadas por la EBU, no leídas; R 128 s1: sólo lo que recoge la Tech 3343.
- Cómo vigila la autoridad audiovisual el nivel sonoro de publicidad: no lo dice el art. 121, sin documento localizado.
