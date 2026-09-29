# Tema 4 del específico de Realizador/a · Organización del control de realización: mezclador, CCU, grafismo, sonido, iluminación, prompter, servidores y comunicaciones

**Siglas**: RTVA · CSRTV · RD · RA · UC/RP/CR/MF/CE (IMS077_3, INCUAL) · LE · CCU · PGM · PVW · DSK · DVE · GPI · SDI · PL · IFB · N-1 · NRCS · MOS · MAM · DMX512 · XLR · EBU · ANSI.

Esqueleto para repasar, no resumen: fuente delante de cada línea; «oficio» = sin norma; «no consta» = sin documento publicado.

<!-- indice -->
Organización · 1 Mezclador · 2 CCU · 3 Grafismo · 4 Sonido · 5 Iluminación · 6 Prompter · 7 Servidores · 8 Comunicaciones · Aplicación práctica
<!-- /indice -->

## Organización del control de realización

- Ninguna norma regula el control; RTVA sólo publica quién hace qué (convenio X, BOJA 240, 10/12/2014, anexo III). Equipos y salas de CSRTV: no consta.
- Oficio: control = donde se realiza; plató = donde se rueda; estudio = ambos + camerinos, almacén, acceso de decorados.
- RD 1680/2011, 0910, RA 4: configuración de medios del control; 4.a diagrama de equipos y conexiones (control, plató, unidad móvil, continuidad). Norma de enseñanza.
- Controles (oficio): realización, imagen, sonido, iluminación (del estudio); central y continuidad (de la casa). IMS077_3, UC0217_3 y MF0217_3 apdo. 4 los nombran aparte.
- RD 1680/2011, 0910, contenidos: mezcladores, generadores de sincronismos, matrices o «patch–pannel», preselectores, cámaras y CCU, reproductores y grabadores, tituladoras, «sistemas de autocúe», escenografía virtual. 0905 RA 6: equipos auxiliares.
- Cadena (oficio): cámara → caja de plató (panel de conectores en pared) → CCU → control central → mezclador → programa; retorno inverso; cable único con alimentación, intercom, piloto y datos.
- No opera el realizador (oficio): sincronismos, matriz, multipantalla. 0905 RA 6.b: multipantalla (mosaico con nombre y piloto).
- Fichas convenio (código, p.):
  - Realizador 5351000 p.196: «Diseñar, coordinar, supervisar y dirigir la realización»; «Diseñar y coordinar todos los elementos técnicos-artísticos». LE 6.5 (p.92): «responsable máximo de la corrección de la imagen y de la calidad de la emisión». Pide, juzga, responde (oficio). Tema 3.
  - Ayudante de Realización 5353000 p.111; Ayudante Técnico Mezclador 5352000 p.115; Técnico Electrónico 5342100 p.209 y Oficial 5342101 p.186 (idénticas): «Realizar el control de cámaras.»; Operador de Sonido 5212207 p.188; Iluminador 5341112 p.132; Capataz 5341210 p.117; Eléctrico 5341211 p.126; Iluminador Superior 5341111 p.133; Grafista 5345100 p.129; Operador Montador de Vídeo 5212206 p.190; Editor de Continuidad 5302010 p.125.
  - «La presente definición no constituye una lista cerrada de funciones». Sin ficha de prompter ni titulador; operador en CSRTV: no consta.

## 1. Mezclador

- Oficio: conmutar, mezclar, combinar (key). Ficha 5352000: «Mezclar y crear efectos especiales con distintas fuentes de video.»; «Programar los generadores de efectos y mesa de mezclas»; comprobar sincronía de fuentes.
- Oficio, módulos: bus PGM, bus PVW/preset, transición (CUT, AUTO, T-bar), keyers, DSK (normalmente dos: mosca y rótulos), memorias, auxiliares.
- RD 1680/2011, 0905, RA 5: c) entradas a buses; d) salidas y destinos de PGM, PVW y auxiliares; e) transiciones, cortinillas, DVE, croma, luminancia o DSK. Tema 9.
- Salidas (oficio): PGM/PP con mosca y rótulos; PVW; limpia (sin DSK, para quien reemite); auxiliares; multipantalla.
- Auxiliar: manual ATEM (Blackmagic), salidas SDI con cualquier fuente, «muy similares a las salidas de una matriz de conmutación». RA 6.c: enrutamientos en matrices, switcher o preselectores.
- Sincronía (oficio): imágenes en fase; generador de sincronismos; genlock; sincronizador de cuadro con retardo (retardo diferencial arrastra el sonido). ATEM: resincronizador en cada entrada, automático si no hay sincronía. Black burst y tri-level: tema 9; sincronía: tema 11.
- GPI (oficio): contacto seco, un pulso sin datos; arranca un servidor en el mismo fotograma. Piloto, a la inversa; ATEM: relés por «cierre de contacto».

## 2. CCU

- Oficio: alimenta la cámara, procesa y sincroniza su señal, ajuste remoto (diafragma, negros, balance de blancos, ganancia, matriz, detalle); un panel por cámara.
- RD 1680/2011: 0910 RA 4.f (cámaras, unidades de control, ajustes); 0905 RA 5.b (monitor de imagen, forma de onda, vectorscopio, rasterizador).
- Control de imagen (oficio): iguala cámaras; operador = encuadre, foco, movimiento; panel remoto = diafragma, color, obturación, negro, ganancia. Sin ficha «control de imagen»: fichas 5342100 y 5342101.
- IMS077_3, MF0217_3, CE1.5: verificar ajuste de cámara por control de imagen, sonido ajustado, mezclador preparado.
- Instrumentos (oficio): forma de onda = luminancia; vectorscopio = tono y saturación; histograma = niveles. UC0216_3: «monitor en forma de onda, vectorscopio, monitores de vídeo». Cámara y óptica: tema 8.
- Retornos (oficio): de cámara (visor), de plató, de auxiliar (decorado), intercom; configurables; viajan por la CCU.
- ATEM: «permite controlar unidades URSA Mini y Blackmagic Studio Camera mediante la señal SDI de retorno.»
- IMS077_3, UC0217_3, RP3 «Operar con equipos auxiliares en el control de realización, atendiendo a las instrucciones del realizador»; CR3.2: envío de vídeo a plató según escaleta y realizador.

## 3. Grafismo

- Oficio: titulador = rótulos con señal de llave (relleno + llave); hoy también escenografía virtual, datos en tiempo real, RA. Frente a postproducción: tiempo real.
- Vizrt, *Viz Pilot Edge User Guide* 3.5: Template Builder (diseño); plantillas rellenadas como data elements, movidas a la escaleta, guardadas en Viz Pilot para redacción y control.
- Ficha 5345100: «Diseñar y realizar y todo tipo de imagen gráfica»; «Realizar escenarios virtuales»; no lanza rótulos.
- LE 6.1.2 (p.89): rótulos «con su orden y ubicación precisa» en escaleta.
- RD 1680/2011, 0905, RA 6: d) opciones gráficas y almacenamiento, señal incrustada; e) rótulos y claquetas, salida al mezclador. 0910 RA 4.g: escenografía virtual con cámaras y mezclador.
- IMS077_3, UC0217_3: CR3.1 tituladora comprobada con técnicos; CR3.5 paginación a solicitud de dirección o realización; CR2.5 lanzamiento en los códigos de tiempo del parte de emisión. Paginar = páginas numeradas en orden de escaleta (oficio).
- Rotulación, RA, decorados, pantallas: tema 12.

## 4. Sonido

- Oficio: tres familias sin mezclar (programa; retornos: N-1, IFB, monitores; intercom); el retorno no lleva la propia voz.
- RD 1680/2011, 0910, RA 4: c) líneas de entrada a la mesa y envíos a control y estudio; e) «audio sigue vídeo» (sonido se abre y cierra con su imagen) y audio embebido (dentro del SDI). Audio sigue vídeo: controles pequeños; con mesa y operador, se mezcla aparte (oficio).
- LE 6.5 (p.92): «la realización es territorio profesional de los técnicos… su criterio no puede soslayarse»; equipo «en estrecha simbiosis con editores y productores».
- Ficha 5212207: «Analizar los objetivos y criterios establecidos en el guión técnico o escaleta, con el director o realizador.»; «controlar el tráfico de señales de audio»; «Realizar la captación, registro, edición, tratamiento y reproducción del sonido.»
- Planos sonoros, microfonía, N-1, sincronía: tema 11.

## 5. Iluminación

- Ubicación de la mesa en Canal Sur: no consta. Ficha 5341112: «Manejar los pupitres de iluminación durante la realización del programa.»; visionar por cámaras.
- Ficha 5341111: «Crear y definir el estilo de luz de los programas.»; diseño; «Realizar pruebas y ensayos de programas.»
- Fichas 5341210 «Manejar los pupitres de iluminación.» y 5341211 «Mantener el estado de iluminación durante los programas.»; sólo 5341112 dice «durante la realización». Quién se sienta: no consta.
- RD 1680/2011, 0910, RA 1.d: mesas de luces y dimmers; RA 4.d incluye «control de iluminación».
- DMX512, ANSI E1.11-2024 (aprobada 25-04-2024):
  - 1.1: datos entre controladores y equipos, incluidos dimmers; cable fuera de alcance.
  - 1.2: ANSI/TIA/EIA-485A-1998, equilibrada; XLR de 5 polos o bornes; paquetes de hasta 513 slots, el primero START Code.
  - 3.45 y 3.36: universo = enlace de una sola fuente; slot 0 START Code; slots 1 a 512 de datos.
  - 8.6: 512 slots por enlace; más, varias líneas.
  - 1.3: no es red de todo el recinto. 3.37: luminarias automáticas, Slot Footprint mayor que uno.
- IMS077_3, MF0217_3, CE1.7: observar continuidad de actuación, iluminación, ambiente y acción. Tema 10.

## 6. Prompter

- Teleprompter = aparato; Autocue = marca (desde 1955). RD 1680/2011, 0910: «sistemas de autocúe». IMS077_3, MF0217_3, CE1.5: velocidad de lectura adecuada al presentador.
- Autocue (fabricante, no norma):
  - Beamsplitter: 70% pasa, 30% refleja («broadcast standard 70:30 glass»); ninguna norma la fija.
  - Imagen invertida en el monitor; cue marker a 1/4 desde arriba (recomendación).
  - Hand controller (operadores con cable y rueda; presentadores inalámbrico); foot controller.
  - Tally light propio (la capucha tapa el de la cámara).
  - Talent feedback monitor bajo el del prompter.
  - Blank screen (barridos); slugline (título no leído); top (inicio).
  - Counterbalance weight.
  - NRCS/NCS manda la escaleta al programa del prompter. Cambios en directo: tema 6.
- Operador de prompter en CSRTV: no consta.

## 7. Servidores

- Oficio: disco que graba y reproduce a la vez (varias señales, repetición, cámara lenta, listas, emisión, catalogar); no corrige color.
- RD 1680/2011, 0905, RA 6: a) equipos auxiliares, servidores y sistemas virtuales de redacción y edición; f) magnetoscopios y discos duros, etiquetar; g) grabar para repetición. Contenidos: «máster, señal sin incrustaciones y cámaras masterizadas».
- IMS077_3, UC0217_3: CR2.3 lanzamiento al primer fotograma con imagen visible; CR2.4 repeticiones en monitores de plató, duración y velocidad; CR3.3 grabadores auxiliares (planos alternativos); CR3.4 programa a grabadores; CR2.2: tema 6.
- Ficha 5212206: «Grabar, emitir y reproducir videos para programas en todo tipo de eventos y producciones con selección alternativa a la realización.» Reparto con asistencia: no consta.
- LE 6.1.1 (p.88): «Son inadmisibles los cambios en la identificación de un vídeo [...] El nombre de una noticia en escaleta debe respetarse por obligación.»
- MOS (mosprotocol.com): protocolo entre NCS y servidores de vídeo, audio, imágenes fijas y generadores de caracteres; «allows integration of diverse NCS and MOS equipment». Sistema de CSRTV: no consta. MAM: temario Operador/a Montador/a de Vídeo; códecs: tema 14.
- Continuidad (oficio): cortinillas, mosca, autopromociones, publicidad, enlaces. Ficha 5302010: «Realizar la continuidad de la emisión siguiendo las pautas de la escaleta de continuidad.»; puntualidad; «Coordinar la emisión de programas en directo con los realizadores / productores respectivos.» CR2.6: hora de entrada, publicidad, cuenta atrás y parciales a continuidad y equipo.

## 8. Comunicaciones

- RD 1680/2011, 0910, RA 4.d: intercomunicación entre nueve puestos: realización, cámaras, regiduría, mesa de audio, reproducción y grabación de vídeo, control de cámaras, control de iluminación, grafismo, conexiones exteriores. Prompter no figura.
- EBU Tech 3347 § 1.2: intercom entre dos estudios (matrix-to-matrix), estudio y OB van, estudio remoto, VoIP interno, reportero (matrix-to-phone / softphone); nombra «intercom matrices» sin definirlas.
- Oficio: línea compartida (todos se oyen; cámaras) vs matriz (punto a punto; realizador). Clear-Com: partyline analógica de 2 hilos, «the path is the same for both talk and listen»; «camera operators on a camera PL». 2 y 4 hilos, IP: tema 11.
- Confidente (oficio): escucha permanente sin pulsar; no cierra las demás; no es grabar, conferenciar ni silenciar.
- Panel del realizador (oficio): un punto por cada puesto del RA 4.d + continuidad + IFB. Señal internacional: sin continuidad (tema 3).
- Clear-Com: sin diseño estándar de intercom de cámaras entre fabricantes; camera isolate: comunicación privada del video operator o director técnico con un cámara sin interferir con los demás y el director.
- IFB, Clear-Com: «simplex intercom for sending a program feed and interrupt (cue) audio… for a talent». Intercom = dúplex, equipo, nunca al aire; IFB = simplex, presentador o reportero, PGM o N-1 con órdenes. Tema 11.
- Piloto (oficio): en cámara, multipantalla (rojo PGM, verde PVW) y plató. ATEM: CALL hace parpadear la luz piloto. Ventanas: piloto en todas las que contribuyen.
- IMS077_3, UC0216_3, CR5.2: comunicación control-estudio «de forma permanente y con la inmediatez necesaria».
- LE 6.1 (p.88): cambio de escaleta «inmediata y simultáneamente, a todas las personas y departamentos afectados». LE 8.3: «La improvisación no tiene cabida como elemento de trabajo». Órdenes e incidencias: tema 6; presión: tema 18.

## Aplicación práctica

- Orden (oficio): 1 escaleta y fuentes (ficha 5351000); 2 entradas y multipantalla (0905 RA 5.c, 6.b); 3 salidas: PGM, limpia, un auxiliar por retorno, pantalla y grabador (RA 5.d, 6.c); 4 transiciones y memorias (RA 5.e); 5 pactar con control de cámaras e iluminador superior (fichas 5342100, 5341111); 6 vídeos y titulador (CR3.5; LE 6.1.1); 7 prompter y retornos (CE1.5; CR3.2); 8 intercom, IFB, piloto (0910 RA 4.d); 9 continuidad (ficha 5302010; CR2.6).
- Casos (oficio): exterior = entrada fija sincronizada + IFB con N-1; sin mosca = limpia; presentador ve conexión = retorno desde auxiliar; cámara 3 no casa = control de cámaras; cámara 2 sola = aislamiento; oír a la ayudante = confidente; vídeo ausente = buscar por nombre de escaleta; barrido con prompter = pantalla en blanco.
