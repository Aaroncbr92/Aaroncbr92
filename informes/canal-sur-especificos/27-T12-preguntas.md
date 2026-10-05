# Preguntas · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Fase 4 (refutación). Quince preguntas tipo test de cuatro opciones, contestadas **sólo con el
tema** (`temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`).
Distintas de las diez del informe de redacción. Clave: entera / a medias / no.

1. Según el apéndice 1 del RITE, el sistema de automatización y control de edificios apoya el
   funcionamiento eficiente, económico y seguro de las instalaciones mediante controles
   automatizados y: a) sustituyendo su gestión manual; b) facilitando su gestión manual; c)
   prohibiendo su gestión manual; d) delegando su gestión en la empresa mantenedora.
   **b**. Epígrafe 1.1 — **entera**.
2. En los niveles del RITE, los buses de comunicación, drivers y redes pertenecen al nivel: a) de
   unidades de campo; b) de proceso; c) de comunicaciones; d) de gestión y telegestión.
   **c**. Epígrafe 1.4 — **entera**.
3. Según el RIPCI, la gestión de las señales del sistema de comunicación de la alarma de incendio
   está controlada, en cualquier caso, por: a) el sistema de gestión técnica del edificio; b) el
   equipo de control e indicación (e.c.i.); c) el puesto de control de seguridad física; d) la
   empresa mantenedora. **b**. Epígrafe 1.1 — **entera**.
4. Modbus sobre TCP/IP utiliza el puerto reservado: a) 47808; b) 80; c) 502; d) 161.
   **c**. Epígrafe 2.2 — **entera**.
5. En el modelo de datos de Modbus, las «Coils» son: a) bits de sólo lectura; b) bits de lectura y
   escritura; c) palabras de 16 bits de sólo lectura; d) palabras de 16 bits de lectura y
   escritura. **b**. Epígrafe 2.2 — **entera**.
6. En BACnet (ISO 16484-5), el tipo de objeto que guarda el registro de tendencias de un punto es:
   a) Notification Class; b) Schedule; c) Trend Log; d) Binary Value.
   **c**. Epígrafes 2.2 y 5.1 — **entera**.
7. En un lazo de regulación, la acción que elimina la desviación permanente es la: a)
   proporcional; b) integral; c) derivativa; d) todo-nada. **b**. Epígrafe 2.3 — **entera**.
8. (Aplicación práctica) Una sonda de temperatura con salida 4-20 mA y rango 0-50 °C entrega
   12 mA. El controlador debe mostrar: a) 12 °C; b) 20 °C; c) 25 °C; d) 30 °C.
   **c**. Epígrafe 3.2 — **a medias**: el tema dice que el cero está en 4 mA y cita el «escalado»
   (3.3), pero no da la conversión lineal entre corriente y magnitud.
9. Una sonda de temperatura de resistencia de platino Pt100 tiene, a 0 °C, una resistencia de:
   a) 10 Ω; b) 100 Ω; c) 1.000 Ω; d) 10.000 Ω. **b**. — **no**: el tema sólo habla de «sondas de
   resistencia» (3.2), sin tipos (Pt100, Pt1000, NTC, termopar).
10. (Aplicación práctica) Para regular el caudal de aire exterior de una sala según la calidad del
    aire interior, el sensor que el sistema de gestión suele emplear mide: a) la temperatura de
    impulsión; b) la concentración de CO2; c) la presión diferencial del filtro; d) la humedad
    exterior. **b**. — **no**: el tema menciona el «control por ocupación» (2.3) pero no los
    sensores de calidad del aire ni los de presencia como tecnología.
11. (Aplicación práctica) El sistema manda arrancar una bomba y, pasado el tiempo previsto, no
    recibe su contacto de marcha. Es una alarma: a) de umbral; b) de equipo; c) por discrepancia;
    d) informativa. **c**. Epígrafe 4.1 — **entera**.
12. Según la guía técnica de mantenimiento del IDAE, la simulación de alarmas y la comprobación de
    su notificación en el control computerizado se recomienda: a) mensual; b) trimestral; c) dos
    veces al año; d) anual. **a**. Epígrafe 4.4 — **entera**.
13. El RITE exige un dispositivo que registre las horas de funcionamiento en las bombas y
    ventiladores cuyo motor tenga una potencia eléctrica mayor que: a) 5 kW; b) 20 kW; c) 70 kW;
    d) 290 kW. **b**. Epígrafe 5.1 — **entera**.
14. (Aplicación práctica) El puesto central muestra desde hace horas el mismo valor de un
    analizador de red integrado por bus, sin ninguna alarma. La operación de la guía del IDAE que
    detecta este fallo es: a) la verificación del cambio de horario; b) la comprobación de los
    tiempos de refresco; c) la evaluación de la obsolescencia del hardware; d) la comprobación del
    arranque del puesto central tras un fallo de tensión. **b**. Epígrafe 6.2 — **entera**.
15. (Aplicación práctica) Hay que sustituir el contactor de una UTA que el sistema de gestión puede
    arrancar a distancia. Además de consignar en campo, el técnico debe: a) nada más, la
    consignación en campo basta; b) dejar el punto fuera de servicio o en manual local también en
    el puesto central y señalizarlo en los dos sitios; c) apagar el servidor del puesto central;
    d) rearmar la alarma desde el puesto. **b**. Epígrafe 7.3 (paso 5) — **entera**.

## Recuento

Entera: 12 (1-7, 11-15). A medias: 1 (8). No: 2 (9, 10).

Cobertura por rúbrica del enunciado: BMS/SCADA (1, 2, 4-7), sensores (8, 9, 10), alarmas (3, 11,
12), históricos (6, 13), telemedida (14), actuación ante avisos (15). Las tres respuestas
incompletas caen en «sensores»: el tema trata el punto, la señal y el contraste, pero no la
tecnología de los sensores.
