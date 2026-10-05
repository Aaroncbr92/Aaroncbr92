# Tema 17 del específico de Oficial Técnico Electricista · Planificación de intervenciones en instalaciones críticas

**Siglas**: RTVA, CSRTV, SAI, STS (conmutador estático de transferencia), CPD, PDU, RAID, BMS, OT, LPRL, NBA, RITE, IT, REBT, UNE, EN, ISO; SSFF = sociedades filiales.

Esqueleto para repasar, no resumen: lo no marcado como norma es oficio.

<!-- indice -->

## Índice

- [Planificación](#planificación-de-intervenciones-en-instalaciones-críticas)
- [Análisis de impacto](#análisis-de-impacto)
- [Ventanas de mantenimiento](#ventanas-de-mantenimiento)
- [Coordinación con producción](#coordinación-con-producción)
- [Comunicación de incidencias](#comunicación-de-incidencias)
- [Planes de contingencia](#planes-de-contingencia)
- [Retorno al servicio](#retorno-al-servicio)
- [Huecos declarados](#huecos-declarados)

<!-- /indice -->

## Planificación de intervenciones en instalaciones críticas

- Sin norma en radiotelevisión: casi todo oficio.
- Crítica = su fallo corta servicio que no puede pararse o pone en peligro personas.
- Ley 8/2011, art. 2: a) servicio esencial; d) infraestructuras estratégicas; e) críticas = indispensables, **no permite soluciones alternativas**, grave impacto en servicios esenciales.
- Ley 8/2011, art. 4: Catálogo Nacional, Ministerio del Interior. RTVA catalogada: no consta.
- Convenio X RTVA (BOJA 240, 10/12/2014), anexo III, puesto 9311100: revisiones y mantenimiento generales; reparaciones; montaje de nuevos sistemas y verificar puesta en marcha; mantener en condiciones óptimas; mantener, operar, explotar e inspeccionar instalaciones RTVA y SSFF.
- Anexo III, puesto 9300000 (jefe Explotación y Mantenimiento): elaborar e implantar Plan de Mantenimiento; coordinar y supervisar colaboradores externos y contratas; asegurar disponibilidad de servicios básicos. Fichas no cerradas.
- Jefatura decide y coordina contratas; oficial prepara, ejecuta, devuelve.
- Ciclo de 8 fases (oficio): definir; analizar impacto; elegir ventana; coordinar; preparar contingencia; ejecutar (tema 15); retornar; cerrar. Correctivo urgente: fases 2, 5, 6, 7 comprimidas.
- Definir = OT con gama (tema 13) + esquema actualizado + procedimiento de maniobra + lista de comprobaciones de retorno.
- RD 1215/1997, anexo II, 1.14: mantenimiento con peligro tras parar o desconectar, comprobar inexistencia de energías residuales peligrosas, evitar puesta en marcha o conexión accidental; si no puede pararse, medidas para hacerlo seguro o fuera de zonas peligrosas (eléctrica: tensión o proximidad, tema 15).
- RD 614/2001, anexo II, A: dejar sin tensión y reponerla, trabajadores autorizados; alta tensión, cualificados.

## Análisis de impacto

- Cinco preguntas: qué deja de funcionar; qué servicio cae (esquema a servicios); cuánto tiempo (trabajo, maniobra, reposición, rearranque); qué redundancia queda; qué puede salir mal.
- Ley 8/2011, art. 2.h, criterios horizontales de criticidad: 1 personas (víctimas, heridos graves, salud pública); 2 económico; 3 medioambiental; 4 público y social (pérdida y grave deterioro de servicios esenciales).
- Art. 2.j, interdependencias: efectos sobre otras instalaciones o servicios; propio sector y otros; local, autonómico, nacional, internacional. Ejemplos: climatización apaga equipos por temperatura; red de datos deja sin BMS (tema 12).
- Prioridades (oficio): antena; lo que lo estará en horas; lo recuperable. Áreas: continuidades (nunca paran); controles y salas técnicas; estudios; postproducción.
- Escala: edición, con la sala; estudio, con producción; continuidad o controles sólo con carga por otro camino o emisión en otra cadena o centro (existencia no consta).
- Redundancia consumida: N, carga cae; N+1, queda N sin reserva; 2N, queda un camino. Ventana en redundante = riesgo aumentado; vigilar vía que queda (SAI, BMS).
- Redundancia existe para que la avería no se note; cortar carga = mal diseño: bypass que corta, carga de una entrada en 2N, PDU que alimenta ambas fuentes (tema 8, 8.4).
- UNE-EN ISO 22301:2020 (SGCN, requisitos; ISO 22301:2019; Modificación 1 2024 cambio climático); UNE-EN ISO 22313:2020 (directrices). Sólo ficha; contenido no leído; RTVA con SGCN no consta.
- Ejemplo 2.5: baterías SAI A, control central 2N; dos conversores de una entrada en STS. Servicio caído: ninguno si rama B aguanta; redundancia: ninguna; riesgos: STS no transfiere, B sobrecargada, alarma latente en SAI B, SAI A no vuelve a inversor.
- Decisiones: carga real de B y estado de SAI B (tema 7); probar STS o aceptar corte; ventana de menor emisión; no cerrar hasta SAI A en inversor y rama A alimentando.

## Ventanas de mantenimiento

- Costumbre, sin norma. Intervalo pactado con quien explota el servicio con instalación parada, degradada o sin redundancia.
- Cinco datos: inicio (maniobra, no trabajo); fin (devuelta y comprobada); alcance; punto de no retorno; responsables (ejecuta, autoriza, a quién se avisa).
- Elección: parrilla (madrugada, sin directos, emisión enlatada desde reserva); producción (sin grabación; nunca víspera de directo: elecciones, retransmisiones); meteorología y red (no con tormentas en centro emisor ni cortes de distribuidora); personas (conocedoras, fabricante disponible).
- Tareas: en carga, sin ventana (termografía, análisis de red, alarmas, históricos); parada (aislamiento, reapriete, sustitución de aparamenta, limpieza de cuadros); ensayos de fuentes de socorro (grupo, SAI, STS), ventana pactada.
- Punto caliente y armónico sólo con corriente; termografía antes de abrir.
- Grupo en vacío no demuestra nada: probar transferencia. Prueba con carga, banco de cargas, descarga SAI: tema 7 (7.1, 7.2).
- Ensayo = intervención: impacto, ventana, vuelta atrás (reponer red), retorno (retransferencia, grupo en automático).
- Duración hacia atrás: comprobaciones previas; maniobra de salida; trabajo con margen; reposición y pruebas; vuelta atrás.
- Punto de no retorno: si sólo queda tiempo de deshacer, se deshace.

## Coordinación con producción

- Propone mantenimiento; acepta quien responde del servicio. Procedimiento y firma por emisión: no constan.
- Se pacta por escrito: fecha, inicio, fin, punto de no retorno; servicios en lenguaje de servicio («estudio 3 sin climatización»); riesgo residual; lo que hace producción (emisión a reserva, no grabar, guardar, apagar ordenadamente); contingencia y quién aborta; interlocutores localizables; cómo se comunica avance y final.
- Aviso a todos los dependientes; confirmar antes de empezar.
- Externas: LPRL art. 24 y RD 171/2004 (información, instrucciones, medios, persona coordinadora), tema 15, epígrafe 6.
- RD 39/1997, art. 22 bis.1.a): recursos preventivos si concurrencia de operaciones sucesivas o simultáneas agrava o modifica riesgos y hace preciso controlar la aplicación de métodos de trabajo; 22 bis.2: evaluación identifica esos riesgos.
- Permiso de trabajo: con riesgo eléctrico o concurrencia; en baja tensión buena práctica, no obligación expresa del RD 614/2001 (tema 15, epígrafe 5).
- NBA (RD 393/2007), 3.3.3, mínimos: a) precauciones; b) permisos especiales de trabajo; c) comunicación de anomalías o incidencias al titular; d) programa de mantenimiento de lo que genera riesgo (cap. 5 anexo II); e) de lo que protege (cap. 5).

## Comunicación de incidencias

- Servicio (a quien explota y a quien coordina mantenimiento) y seguridad (superior directo y organización preventiva, LPRL art. 29). Ambas: primero personas, impedir acceso a lo que está en tensión y señalizar (tema 13, 5.1).
- Ley 31/1995, art. 29.2.4.º: informar de inmediato al superior jerárquico directo y a trabajadores designados o servicio de prevención de cualquier situación que, a su juicio, entrañe, por motivos razonables, riesgo.
- NBA 3.3.3.c). Paralización ante riesgo grave e inminente: tema 19, epígrafe 1.
- Incidencia de servicio: sin norma ni procedimiento RTVA publicado.
- Tres momentos: inicial inmediato (qué, dónde, desde cuándo, servicio, acción, próximo aviso); seguimiento (cambio de riesgo, al instante); cierre (restablecido y comprobado, pendientes: p. ej. redundancia sin reponer).
- Reglas: avisar antes de saber la causa; decir lo que se sabe y lo que no; escalar si no hay respuesta, supera lo previsto o puede afectar a emisión.
- Convenio, anexo III, puesto 9311200 (Ayudante Técnico Electricista): guardias con el oficial para averías imprevistas. Art. 50.11: guardia voluntaria en descanso o festivos, plus por día de guardia, llamado o no, horas del llamado compensadas como extraordinarias; si es llamado, mínimo cuatro horas; localizador a distancia.
- Imprevista: prioridades en tema 7, 8.1; ayuda lo preparado: esquema, procedimiento, repuestos (tema 13, 7), lista de llamadas.
- Registro: qué, cuándo, servicio y duración, causa (no síntoma), hecho, pendiente. OT de correctivo (tema 13) + afección al servicio.

## Planes de contingencia

- Dos: de la instalación (red, grupo, SAI, climatización: maniobras, avisos, deslastre, apagado ordenado; revisado al cambiar); de la intervención (cómo se deshace, quién aborta; una por intervención). Grupo y SAI: tema 7, epígrafe 8.
- NBA, RD 393/2007, 23 de marzo. RD 524/2023, 20 de junio, disp. derogatoria única 2.d): derogada con efectos de 11/07/2023; sigue aplicándose hasta nuevo instrumento (nota del BOE; ap. 3 no nombra la NBA); disp. final primera: máximo cuatro años para adaptarla; art. 12: Directriz Básica de Planificación de Autoprotección. A 25/09/2026 no localizada sustituta.
- Anexo II, cap. 6, emergencias por tipo de riesgo, gravedad, ocupación y medios humanos; procedimientos: a) detección y alerta; b) alarma (quién avisa; centro de coordinación de Protección Civil); c) respuesta; d) evacuación y/o confinamiento; e) primeras ayudas; f) ayudas externas.
- 3.6.4: simulacros, al menos una vez al año, evaluando resultados. 3.7: vigencia indeterminada, revisión al menos cada tres años.
- Cap. 5: mantenimiento preventivo de riesgo (control) y protección (operatividad); cuadernillo de hojas numeradas de operaciones e inspecciones. Cap. 7.1 notificación. Cap. 9: 9.2 sustitución de medios; 9.3 ejercicios y simulacros.
- Lección: clasificar por tipo y gravedad; quién avisa y decide; qué en cada caso; mantener medios; ensayar. Obligación RTVA: no consta.
- Vuelta atrás: estado inicial (aparatos, ajustes, parámetros, fotos); lo retirado, conservado hasta el retorno; configuración y programa anteriores guardados; repuesto en sala; fuente alternativa (grupo, provisional, emisión a reserva); criterio para abortar (alarma en vía que queda, punto de no retorno, daño imprevisto) y quién.
- RITE (RD 1027/2007), IT 2.3.4.4: control, mando, gestión o telegestión por tecnología de la información; mantenimiento y actualización de versiones por personal cualificado o el suministrador. Oficio: ventana y versión anterior guardada.
- Niveles: repuesto en almacén; reserva fría; reserva caliente; redundancia interna (dos fuentes, ventiladores, RAID). Saber el nivel de cada elemento crítico: dice cuánto dura la incidencia.
- Se duplica lo que no puede parar (alimentación con SAI y grupo, matrices, servidor, enlace al centro emisor); repuesto de lo que sí.
- Redundancia no probada no existe; ensayos en ventana (3.4); procedimiento ensayado con quien lo ejecutaría, revisado al cambiar la instalación.

## Retorno al servicio

- Devolver instalación comprobada, redundancia repuesta, producción avisada. Sin norma con ese nombre.
- RD 614/2001, anexo II, A.2 (tema 15, 2.4): reposición tras retirar trabajadores no indispensables y recoger herramientas y equipos. Pasos: 1.º retirada de protecciones adicionales y señalización de zona; 2.º puesta a tierra y en cortocircuito; 3.º desbloqueo y/o señalización de dispositivos de corte; 4.º cierre de circuitos. Trabajadores autorizados. Suprimida una medida inicial, se considera en tensión la parte afectada.
- Reposición por escalones, aguas arriba a abajo, sin cerrar de golpe lo que cuelga de SAI o grupo (punta; bypass); avisar al operador.
- RD 1215/1997, art. 4.1: comprobación inicial tras instalación y antes de primera puesta en marcha; nueva tras montaje en nuevo emplazamiento. 4.2: adicionales ante transformaciones, accidentes, fenómenos naturales, falta prolongada de uso. 4.3: personal competente. 4.4: documentadas, a disposición de la autoridad laboral, conservadas toda la vida útil.
- Aparamenta sustituida, cuadro ampliado, equipo tras avería grave = transformación: criterio de oficio.
- REBT (tema 2): verificaciones previas a puesta en servicio y documentación de modificaciones.
- Secuencia: 1 zona despejada; 2 comprobación en frío (aislamiento, tema 14); 3 reposición; 4 funcional (SAI a inversor, grupo en automático, alarmas BMS); 5 prueba con carga; 6 redundancia repuesta (STS ve dos fuentes, nada en bypass); 7 devolución aceptada por quien autorizó; 8 vigilancia reforzada (alarmas, temperaturas, termografía en carga).
- Paso 6, el más olvidado: cree tener 2N y tiene N (tema 8, 9.4). Hasta aceptación, responsabilidad de quien paró.
- Cierre: OT (hecho, repuestos, medidas, duración real); esquema actualizado; comprobaciones documentadas (RD 1215/1997, 4.4); lecciones si salió mal o casi.
- Caso 7.6 (SAI A): batería vieja no sale hasta el final; batería sin interruptor que la deje sin tensión (tema 7, 8.4). Si SAI B alarma, parar y emisión a reserva; batería nueva defectuosa: montar la vieja si fue por capacidad y no por seguridad, o SAI A en bypass y comunicar rama A sin protección. OT con fecha de batería nueva.

## Huecos declarados

- Sin definición normativa de ventana, análisis de impacto, plan de contingencia ni retorno: oficio.
- No leídos (de pago): UNE-EN ISO 22301, 22313, UNE-EN 50110-1.
- No confirmados: RTVA como infraestructura crítica; Directiva (UE) 2022/2557; plan de autoprotección (anexo I NBA) y norma andaluza.
- No constan: procedimientos RTVA de ventanas e incidencias, planes, emisión de reserva, guardias más allá del convenio.
