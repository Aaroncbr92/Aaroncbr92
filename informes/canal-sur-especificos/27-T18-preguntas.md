# Preguntas · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Fase 4 (refutar). Quince preguntas tipo test de cuatro opciones, de teoría y de aplicación práctica,
contestadas **sólo con el tema** (`temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`).
Distintas de las diez del informe de redacción. Respuesta correcta en negrita; luego el epígrafe que la
da y el veredicto: **entera**, **a medias** o **no**.

Reparto: IoT 2, predictivo 2, gemelo digital 2, telegestión 2, baterías 2, autoconsumo 3,
automatización 2. Aplicación práctica: 3, 6, 8, 10, 12, 13 y 15.

---

1. (IoT · teoría) Según el RITE, los controladores, tanto analógicos como digitales, que manejan los
   elementos del nivel de periferia pertenecen al nivel: a) de unidades de campo; **b) de proceso**;
   c) de comunicaciones; d) de gestión y telegestión.
   — 2.4 (apéndice 1, literal). **Entera.**

2. (IoT · teoría) Para comunicar sensores inalámbricos de baja potencia y largo alcance alimentados
   por pila (por ejemplo, sondas de temperatura repartidas por un centro emisor) se usa típicamente
   una red: a) KNX cableada; b) BACnet/IP; **c) de área amplia y baja potencia (LPWAN, tipo LoRaWAN o
   NB-IoT)**; d) RS-485.
   — El tema dice que la sensorización IoT es «a menudo inalámbrica, con batería propia» (2.2), pero no
   nombra ninguna tecnología ni protocolo de comunicación IoT; el tema 12 tampoco trata los
   inalámbricos. **No.**

3. (IoT · práctica) Se instala un sensor de temperatura en el embarrado de un cuadro general con
   transmisión a una plataforma en la nube. Para el disparo por sobretemperatura, lo correcto es:
   a) que la plataforma ordene la apertura del interruptor; **b) que la decisión de seguridad se tome
   abajo, en la protección o en el controlador local, y la plataforma sirva para la decisión de
   mantenimiento**; c) que el operador la valide por teléfono; d) que la decida el gemelo digital.
   — 2.4, último párrafo (oficio). **Entera.**

4. (Predictivo · teoría) En una instalación eléctrica, la medida predictiva cuyo valor está sobre todo
   en su tendencia, de modo que una caída clara respecto a las anteriores dice más que un valor
   absoluto que todavía cumple, es: a) la tensión de flotación de la batería; **b) la resistencia de
   aislamiento**; c) la potencia contratada; d) la frecuencia de red.
   — 3.2 (último párrafo) y 3.3. **Entera.**

5. (Predictivo · teoría) La técnica predictiva que detecta arcos, efecto corona o descargas parciales
   en cuadros y celdas, incluso con la envolvente cerrada, es: a) la medida de la tensión en flotación;
   b) el registro de horas de funcionamiento; **c) la inspección por ultrasonidos (emisión acústica)**;
   d) la prueba de descarga.
   — El tema da termografía, análisis de red, aislamiento y vibración (3.2, 3.3); no nombra los
   ultrasonidos ni las descargas parciales. Se descartan a), b) y d), pero la c) no se puede
   confirmar con el tema. **A medias.**

6. (Gemelo digital · práctica) La sede tiene un modelo BIM tridimensional del edificio, con sus
   cuadros y líneas, pero sin datos en vivo. Según la definición de la ISO/IEC 30173: a) ya es un
   gemelo digital; **b) es la representación digital, pero no es gemelo digital mientras le falte la
   conexión de datos con la instalación real**; c) es gemelo digital si tiene más de diez años de
   históricos; d) sólo lo es si lo certifica AENOR.
   — 4.2 (tabla, «modelo tridimensional del edificio sin datos en vivo: No, por sí solo»). El tema no
   nombra el BIM ni su relación con el gemelo, y quien no sepa qué es un BIM no puede contestar. **A
   medias.**

7. (Gemelo digital · teoría) Según la nota 1 de la definición 3.1.1 de la ISO/IEC 30173, entre las
   capacidades de un gemelo digital NO figura de forma expresa: a) la simulación; b) la visualización;
   c) la colaboración; **d) la certificación**.
   — 4.1 (nota 1, literal). **Entera.**

8. (Telegestión · práctica) Un CPD tiene una enfriadora de 85 kW de potencia útil nominal en
   refrigeración y bombas de 15 kW. El RITE obliga a registrar: **a) las horas de funcionamiento de la
   enfriadora, pero no las de las bombas**; b) las horas de las bombas y no las de la enfriadora; c) nada, porque es una sala
   técnica; d) sólo el consumo total del edificio.
   — 5.2 (IT 1.2.4.4, apartados 5, 6 y 7: 70 kW para generadores y compresores, 20 kW para motores de
   bombas y ventiladores). **Entera.**

9. (Telegestión · teoría) Según la IT 1.2.4.4.8 del RITE, en un generador de frío de más de 70 kW con
   suministro directo de energía renovable eléctrica, contabilizar la contribución producida por
   instalaciones de autoconsumo es: a) obligatorio siempre; **b) obligatorio sólo si es técnicamente
   viable**; c) potestativo; d) prohibido.
   — 5.2 (apartado 8 y la observación sobre el modo de los verbos). **Entera.**

10. (Baterías · práctica) Se va a retirar la batería de un SAI de 40 kWh de una sala técnica. Según el
    Reglamento (UE) 2023/1542: a) va al contenedor general de residuos metálicos; b) la recoge el
    productor sólo si se le compra una nueva; **c) el productor (o su organización de responsabilidad
    del productor) acepta su devolución gratis y sin obligación de comprar otra ni de habérsela
    comprado a él**; d) la gestiona la distribuidora eléctrica.
    — 6.2 (batería industrial) y 6.6 (artículo 61.1). **Entera.**

11. (Baterías · teoría) Para un sistema estacionario de almacenamiento con baterías de litio, la
    química que se suele preferir por su mayor estabilidad térmica y su menor riesgo de embalamiento
    frente a las de níquel-manganeso-cobalto es: a) plomo-ácido abierta; **b) litio-ferrofosfato
    (LFP)**; c) níquel-cadmio; d) litio-óxido de cobalto.
    — La tabla de químicas (6.1) trata el ion litio como una sola química; el embalamiento térmico sí
    está (6.4), pero no la diferencia entre químicas de litio. **No.**

12. (Autoconsumo · práctica) Un centro de trabajo quiere a la vez su fotovoltaica de cubierta sin
    excedentes y participar en un autoconsumo colectivo a través de la red. Hoy: a) está prohibido,
    un consumidor sólo puede estar en una modalidad; **b) es posible: es la única excepción del
    artículo 4.5.b) del Real Decreto 244/2019**; c) sólo si las dos son sin excedentes; d) sólo si
    la potencia total es inferior a 100 kW.
    — 7.5. **Entera.**

13. (Autoconsumo · práctica) Durante el mantenimiento se detecta que alguien ha puenteado el
    mecanismo antivertido de una instalación sin excedentes. La consecuencia que prevé el Real
    Decreto 244/2019 es que: a) la instalación pasa automáticamente a con excedentes; **b) la
    distribuidora podrá proceder a la interrupción del suministro**; c) se pierde el derecho a
    compensación durante un año; d) ninguna, si la potencia es menor de 100 kW.
    — 7.7 (artículo 5.6). **Entera.**

14. (Autoconsumo · teoría) En la compensación simplificada, el periodo de facturación no podrá ser
    superior a: a) una semana; **b) un mes**; c) dos meses; d) un año.
    — 7.8 (artículo 14.3, literal). **Entera.**

15. (Automatización · práctica) Un edificio no residencial con 320 kW de climatización dispone de un
    sistema que sólo arranca y para los equipos por horario. Respecto de las inspecciones de la
    IT 4.2.1, 4.2.2 y 4.2.3: a) queda exento por tener automatización; **b) no queda exento: la
    exención exige que el sistema cumpla las capacidades a), b) y c) de la IT 1.2.4.3.5.1**; c) queda
    exento si la potencia es inferior a 400 kW; d) queda exento si tiene supervisión remota.
    — 8.1 y 8.4. **Entera.**

---

**Resultado**: **11 enteras, 2 a medias (5 y 6), 2 no (2 y 11)**. Las cuatro que no son enteras son lagunas del tema y se proponen en el informe de
refutación.
