# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 4, preguntas tipo test

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`.
Fecha: 25-09-2026. Quince preguntas de cuatro opciones, teoría (T) y aplicación práctica (P), repartidas
por las siete rúbricas del enunciado. Clave marcada en negrita. Cada una se contesta **sólo con el
tema**; la fuente de la clave se da cuando el tema no la tiene.

Resultado: **8 enteras, 1 a medias, 6 no**.

1. (T · Audio multicanal) La versión vigente de la UIT-R BS.775 el 24-IX-2026 es: a) BS.775-2 (2006);
   b) BS.775-3 (2012); **c) BS.775-4 (2022)**; d) BS.775-5 (2023).
   → **Entera**: «Qué es un sistema multicanal».

2. (P · Audio multicanal) Una escucha 5.1.4 tiene: a) 5 frontales, 1 subgrave y 4 traseros; **b) 5
   canales en el plano horizontal, 1 de baja frecuencia y 4 de altura**; c) 5 canales y 4 objetos;
   d) 5 canales, 1 LFE y 4 envolventes mono.
   → **Entera**: «Cómo se nombra un formato».

3. (P · 5.1) Según la BS.775-4, los altavoces envolventes se colocan: a) a ±30°; b) a ±90° exactos;
   **c) entre 100° y 120° desde el frente, sin que haga falta precisión**; d) a ±150°.
   → **Entera**: «La colocación de los altavoces».

4. (P · 5.1) En un control con pantalla que no es acústicamente transparente, la BS.775-4 pide que el
   altavoz central: a) se retrase respecto a los laterales; **b) se sitúe inmediatamente encima o
   debajo de la imagen**; c) se suprima y se use el centro fantasma; d) se ponga a la altura de los
   envolventes.
   → **No**. El tema sólo da la altura ideal de los frontales («a la altura de los oídos»). Fuente:
   BS.775-4, recomienda 2, cuarto guion («This implies an acoustically transparent screen. Where a
   non-acoustically transparent screen is used, the centre loudspeaker should be placed immediately
   above or below the picture. The height of side/rear loudspeakers is less critical»).

5. (T · 5.1) El canal LFE, según la BS.775-4, se graba: a) sin desplazamiento; **b) con −10 dB, que la
   reproducción compensa con +10 dB**; c) con +10 dB, que la reproducción compensa con −10 dB;
   d) con −3 dB, como el central en el downmix.
   → **Entera**: «El canal LFE».

6. (P · 5.1) Al calibrar la escucha con ruido rosa, el LFE se mide con un sonómetro de banda ancha y
   no da +10 dB sobre los demás canales. Según la BS.775-4: a) hay que subir el LFE hasta leer +10 dB;
   **b) es lo esperable por su banda limitada: los +10 dB se miden dentro de su banda de menos de
   120 Hz, con un medidor selectivo en frecuencia**; c) el LFE se calibra a 0 dB en televisión;
   d) hay que activar la gestión de graves.
   → **No**. Fuente: BS.775-4, anexo 7 («if the acoustic level produced by the LFE pink noise is
   measured with a wideband sound pressure level meter, the reading will not measure +10 dB …
   should measure +10 dB within its < 120 Hz bandwidth when measured with a frequency selective
   meter»).

7. (T · Mono) En la BS.775-4, cuando se usa envolvente mono (MS), esa señal: a) va a un único
   altavoz trasero central; **b) se envía a los dos altavoces LS y RS**; c) se suma al central;
   d) se descarta en la reproducción.
   → **No**. El tema dice que LS y RS se funden en una señal, no cómo se reproduce. Fuente:
   BS.775-4, recomienda 3 («In the case of mono surround, the MS signal is fed to both LS and RS
   loudspeakers»).

8. (T · Estéreo · Downmix) En el downmix de 3/2 a 2/0 de la BS.775-4, el central entra en cada lado
   con: a) 1,0; **b) 0,7071**; c) 0,5; d) 0.
   → **Entera**: «Los coeficientes de la UIT».

9. (T · Downmix · Mono) En la tabla 2 de la BS.775-4, al bajar un 3/2 a 3/1, la señal envolvente S
   es: a) LS + RS; **b) 0,7071 LS + 0,7071 RS**; c) 0,5 LS + 0,5 RS; d) 0,7071 C + 0,5 LS + 0,5 RS.
   → **No**. El tema da sólo los destinos 1/0, 2/0 y 3/0. Fuente: BS.775-4, anexo 4, tabla 2
   (filas 2/1 y 3/1: «S = … 0.7071 0.7071»; 2/2 conserva LS y RS a 1,0).

10. (T · Compatibilidad) Para que un servicio 2/0 ya existente pase a 3/2 sin dejar fuera a los
    receptores existentes, la BS.775-4 (anexo 3) identifica: a) sólo el downmix en el receptor;
    b) el upmix en emisión; **c) el *simulcast* del servicio 2/0 junto al 3/2, o las matrices de
    compatibilidad**; d) el Dolby E en un par AES3.
    → **No**. El tema no cita el anexo 3 ni el recomienda 6. Fuente: BS.775-4, anexo 3, § 1
    («simulcasting operation» y «compatibility matrices», con la ventaja de cada uno).

11. (P · Dolby) Un programa llega con el Dolby E «In-Sync Encoded». Según la *Technical Review* de la
    UER: a) no hace falta compensar nada; **b) el retardo de decodificación se compensa en el lugar
    donde se decodifica, con un retardo de vídeo equivalente**; c) el audio llega un cuadro
    adelantado; d) se compensa en el codificador de emisión.
    → **A medias**. El tema define «In-Sync» como «en sincronía con el vídeo» y avisa de la doble
    compensación, pero no dice dónde ni cómo se compensa. Fuente: EBU Technical Review 2009-Q1
    («The decode delay must be compensated for at the decode site by the use of an equivalent video
    delay»).

12. (P · Dolby) Hay que meter una voz en off en un programa que llega en Dolby E: a) se mezcla sobre el
    par bajando su ganancia; b) se ecualiza el par; **c) se decodifica, se mezcla en PCM y se vuelve a
    codificar**; d) se inserta en la banda de guarda.
    → **Entera**: «Lo que no se le puede hacer a una señal Dolby E».

13. (P · Dolby · Compatibilidad) En una cadena Dolby E → Dolby AC-3, se mete en el LFE del Dolby E una
    señal de banda ancha. Según la BS.775-4: a) llega igual a casa, porque el Dolby E conserva la
    calidad; **b) llegará filtrada paso bajo al espectador, porque la respuesta del LFE en Dolby E no
    es la del AC-3**; c) el AC-3 la reparte a los canales principales; d) la descarta el Dolby E.
    → **No**. Fuente: BS.775-4, anexo 7, adjunto 1, § 6 «Dolby E LFE and Dolby AC-3 LFE».

14. (T · Downmix) Método de downmix que la UER recomienda por defecto: **a) Lo/Ro, porque el Lt/Rt es
    aún menos predecible en sonoridad y altera el sonido**; b) Lt/Rt, por la compatibilidad con
    matriz; c) Lt/Rt, porque desfasa 180° los envolventes; d) ninguno.
    → **Entera**: «Por qué la UER recomienda Lo/Ro».

15. (P · Compatibilidad · Downmix) Un 5.1 medido a −23 LUFS se entrega también en estéreo: a) el
    downmix estará a −23 LUFS; **b) hay que medir el downmix: entre otras razones, los envolventes
    pesan +1,5 dB en la medida y bajan −3 dB en el downmix por defecto (4,5 dB de diferencia)**;
    c) se baja el nivel global del downmix de forma fija; d) se hace un upmix.
    → **Entera**: «El downmix y la sonoridad» y «La saturación del downmix y el upmix».
