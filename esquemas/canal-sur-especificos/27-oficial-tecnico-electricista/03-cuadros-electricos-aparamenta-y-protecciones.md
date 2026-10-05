# Tema 3 del específico de Oficial Técnico Electricista · Cuadros eléctricos, aparamenta y protecciones: automáticos, diferenciales, fusibles, contactores, relés, seccionadores, selectividad y protección frente a sobretensiones

**Siglas**: REBT, ITC-BT, INSST, IGA, ID, DPS, SAI, TT, TN, IT, PE, CPN, IP, IK, NA, NC; Ib, In, Iz, IΔn, Ia, Zs, RA, U0, U, Icc, Im, Ir, I2, k3; Iimp, Imax, Uc, Up.

Esqueleto para repasar, no resumen: delante de cada línea, la fuente o el precepto; sin precepto, oficio o guía Schneider.

<!-- indice -->
- 1. Cuadros y aparamenta
- 2. Automáticos
- 3. Diferenciales
- 4. Fusibles
- 5. Contactores
- 6. Relés
- 7. Seccionadores
- 8. Selectividad
- 9. Protección frente a sobretensiones
<!-- /indice -->

## 1. Cuadros y aparamenta

- Art. 16.3 RD 842/2002: protecciones contra sobreintensidades, sobretensiones, agentes externos, contactos directos e indirectos. Oficio: instalación (magnetotérmico, fusible) ≠ personas (diferencial).
- ITC-BT-01: aparamenta = protección, control, seccionamiento, conexión; poder de corte = intensidad que corta bajo tensión de restablecimiento determinada; de cierre = la que establece bajo tensión dada.
- ITC-BT-01: sobreintensidad = superior a valor asignado (conductor: admisible); sobrecarga sin fallo; cortocircuito franco = impedancia despreciable.
- ITC-BT-01 corte omnipolar = todos los activos; simultáneo, o no (neutro conecta antes, desconecta después). No define seccionador ni relé.
- ITC-BT-17 1.1: generales cerca de la entrada de la derivación individual (industrial o comercial: próximo a una puerta); pública concurrencia: no accesibles al público; 1,4 a 2 m viviendas; comerciales mínimo 1 m.
- ITC-BT-17 1.2: posición vertical. Mínimo: IGA omnipolar, manual, sobrecarga y cortocircuito, independiente del ICP; diferencial general (indirectos, salvo ITC-BT-24); corte omnipolar por circuito; DPS si fuese necesario. Un diferencial por circuito exime del general; en serie, selectividad.
- ITC-BT-17 1.3: IGA poder de corte suficiente para el punto, mínimo 4.500 A; demás resisten el cortocircuito del punto.
- ITC-BT-28 4: cuadro general junto a acometida, sin acceso del público, separado de incendio o pánico con elementos a prueba de incendios y puertas no propagadoras; placa junto a cada interruptor; receptores >16 A desde cuadro general o secundarios; conexionado no propagador. RTVA/CSRTV: no consta.
- ITC-BT-17 1.2: envolventes UNE 20.451 y UNE-EN 60.439-3, mínimo IP 30 e IK07. ITC-BT-02: UNE-EN 60529, serie 61439.
- Schneider (IEC 60529): IP + cifras + letra A-D + suplementaria H, M, S, W; X si no se especifica. Sólidos: 1 ≥50 mm; 2 ≥12,5; 3 ≥2,5; 4 ≥1,0; 5 polvo; 6 estanco. Acceso: 1 mano; 2 dedo; 3 herramienta; 4-6 alambre. Agua: 1 goteo; 2 goteo 15°; 3 pulverización; 4 salpicaduras; 5-6 chorro; 7-8 inmersión; 9 alta presión.
- IP 30: ≥2,5 mm, herramienta, sin agua. IP2X: 12,5 mm, dedo. IP4X: 1,0 mm. IP XXB: dedo. IP XXD: alambre. IK (IEC 62262): IK00 (0 J) a IK10 (20 J); IK07 = 2 J.
- ITC-BT-24 3.2: activas en envolvente o tras barrera mínimo IP XXB; superiores horizontales accesibles IP4X o IP XXD; abrir con llave o herramienta, o sin tensión hasta recolocar, o con segunda barrera IP2X o IP XXB.
- ITC-BT-19 2.2.4: neutro azul claro; protección verde-amarillo; fases marrón o negro (gris si tres).
- ITC-BT-19 2.6 separación (omnipolar salvo neutro TN-C): fusibles; seccionadores; interruptores >3 mm o equivalente; bornes sólo en derivación.
- ITC-BT-19 2.7 corte en carga en una maniobra: origen, principales, cuadros secundarios, receptor, mando (salvo tarificación), acumuladores, salida de generadores (letras a, b, c, i, j de diez; a exceptúa relojes, rectificadores telefónicos ≤500 VA). Dispositivos: interruptores manuales; fusibles manuales u otro con poder de corte y cierre independiente del operador; clavijas ≤16 A.
- ITC-BT-19 2.7 omnipolares: cuadro general y secundarios; circuitos (salvo TN-C, TN-S con neutro a tierra); receptores >1.000 W; lámparas de descarga, autotransformadores, tubos de descarga en alta tensión.

## 2. Automáticos

- ITC-BT-22 1.1 (y art. 15.3: compañías dan el cortocircuito): sobrecarga, cortocircuito, descarga atmosférica. a) automático omnipolar con curva térmica o fusibles calibrados. b) protección en el origen, capacidad de corte según el punto; derivados con su sobrecarga y un general para cortocircuitos.
- Schneider cap. G: Ib ≤ In ≤ Iz; I2 ≤ 1,45 Iz; poder de corte ≥ Icc trifásica. Automático: basta Ib ≤ In ≤ Iz. Fusible: In ≤ Iz/k3; k3 1,31 gG <16 A, 1,10 desde 16 A. Ejemplo: Ib 20, Iz 27: 25 A; gG ≤24,5 A.
- ITC-BT-01: automático establece, mantiene e interrumpe corrientes de servicio y las anormalmente elevadas. Oficio: térmico bimetal (sobrecarga); magnético bobina (cortocircuito, instantáneo).
- ITC-BT-02: UNE-EN 60898-1 (doméstico); 60947-2 (industrial); 61009-1 (AD, con sobreintensidades); 61008-1 (ID).
- Curvas (Schneider cap. H, IEC 60898): B 3 In ≤ Im ≤ 5 In (líneas largas); C 5-10 In (general); D 10-20 In (motores, transformadores); D: IEC hasta 50 In, Schneider 10-14 In. Industriales: umbral del fabricante. C 16 A: 80-160 A.
- ITC-BT-52 6.3: recarga, omnipolar, curva C. Oficio: Icc 6 kA exige IGA ≥6 kA.
- ITC-BT-22 1.2: nota 3, neutro no se corta antes que las fases y se conecta a la vez o antes; notas 1 y 5, neutro sin detección si lo protege el de fases y su corriente es netamente inferior a su admisible; armónicos de orden tres pueden impedirlo.

## 3. Diferenciales

- ITC-BT-01: ID abre contactos al alcanzar la corriente diferencial un valor dado; residual = suma algebraica de instantáneos de todos los activos. Oficio: no detecta fase-neutro aguas abajo.
- ITC-BT-24 3.5: IΔn ≤30 mA = medida complementaria ante fallo de otra o imprudencia; requiere una de 3.1 a 3.4 (aislamiento, barreras o envolventes, obstáculos, alejamiento). Contra indirectos sí es principal.
- Sensibilidades: alta ≤30 mA; media 300 mA cabecera (oficio); ITC-BT-34 3.2: ≤500 mA en instalaciones temporales (recomendación), 3.1: público 30 mA; ITC-BT-52 6.1: 30 mA, clase A.
- ITC-BT-09 4: alumbrado exterior, máximo 300 mA y tierra ≤30 Ω; 500 mA con ≤5 Ω; 1 A con ≤1 Ω.
- Clases: AC senoidales (IEC 60755); A senoidales y continuas pulsantes (ITC-BT-24 3.5); F = A + varias frecuencias, 10 mA continua lisa (IEC 62423); B = además continuas lisas, 50 a 1.000 Hz; B cumple F, A y AC. Usos: A electrónica monofásica; F variadores monofásicos; B trifásico, fotovoltaica. S = tiempo (oficio). ITC-BT-24 3.5: clase A si no senoidales (radiología intervencionista); REBT no prohíbe AC.
- ITC-BT-24 4.1: límite 50 V; 24 V alumbrado público (ITC-BT-09, 10). TT, 4.1.2: RA × Ia ≤ U; RA = tierra + conductores de protección de masas; Ia = IΔn; fusibles y automáticos sólo con RA muy baja. U 50 V: 30 mA ≈1.667 Ω; 300 mA ≈167 Ω; 1 A = 50 Ω; 24 V y 300 mA: 80 Ω.
- TN, 4.1.1: Zs × Ia ≤ U0; 0,4 s a 230 V; 0,2 s a 400 V; 0,1 s >400 V. TN-C: no diferencial. TN-C-S con diferencial: sin CPN aguas abajo; PE-CPN aguas arriba.
- IT, 4.1.3: primer defecto sin corte imperativo, controlador con señal acústica o visual. Segundo: masas por grupos como TT (neutro sin tierra); interconectadas como TN: 2 × Zs × Ia ≤ U (neutro no distribuido), 2 × Zs’ × Ia ≤ U0 (distribuido), tabla 2.
- ITC-BT-19 2.9: fugas, en conjunto y por circuito, no superiores a la sensibilidad. Botón de prueba: mecanismo, no tierra (oficio).

## 4. Fusibles

- ITC-BT-01: interrumpe por fusión cuando la intensidad sobrepasa un valor durante un tiempo; oficio: se destruye, uno por fase (ITC-BT-47 4). ITC-BT-22 1.1: sobrecarga y cortocircuito si calibrado. ITC-BT-19 2.6 separación; 2.7 carga sólo si manual y poder de corte y cierre independiente del operador. ITC-BT-02: UNE-EN 60269-1.
- Schneider cap. H: g toda la gama, a parcial; G uso general, M motores. gG: sobrecarga y cortocircuito. aM: motores, con térmico. gM: motores, relé aparte. gI: no doméstico.
- gG (IEC 60269-1): >16 A hasta 63 A, no funde en 1 h con 1,25 In; funde en ≤1 h con 1,6 In (I2).
- Sustitución (oficio): idéntico en calibre, tamaño, clase y poder de corte; semiconductores: designaciones no confirmadas.

## 5. Contactores

- ITC-BT-01 contactos abiertos en reposo: no manual, única posición de reposo (abierto), maniobras frecuentes con cargas y sobrecargas normales. Con apertura automática: electromagnético con relés.
- Oficio: maniobra, no protege; bobina, principales, auxiliares NA y NC.
- IEC 60947-4-1 (Schneider caps. N, H): AC-1 no inductivas; AC-2 motores de anillos; AC-3 jaula, arranque y desconexión en marcha; AC-4 jaula, contracorriente e impulsos. 150 A AC-3 corta 8 In (1.200 A), establece 10 In (1.500 A), cos φ 0,35. Discontactor: poder de corte 8-10 In.
- Marcha-paro: marcha NA, auxiliar NA en paralelo, paro NC en serie; sin tensión no rearranca (ITC-BT-47). Inversión: dos contactores permutan dos fases, enclavados.
- Enclavamiento eléctrico (NC de cada uno en serie con la bobina del otro) y mecánico, ambos; cerrar los dos = cortocircuito.

## 6. Relés

- ITC-BT-01 no define relé; lo nombra en el contactor con apertura automática (oficio: manda abrir, no corta).
- ITC-BT-47 4: motores contra cortocircuitos y sobrecargas en todas las fases, cubriendo falta de una fase; estrella-triángulo en ambas conexiones.
- ITC-BT-47 5: falta de tensión con corte automático si el arranque espontáneo puede causar accidentes o perjudicar (UNE 20.460-4-45); un dispositivo para varios motores del mismo local si suma ≤10 kW o cada uno vuelve al estado inicial; arranque automático preestablecido: no se exige, se excluye el accidente.
- Oficio: térmico regulado a la placa, NC en serie con bobina. ITC-BT-47 3.1: línea de un motor 125 %.
- Oficio: relé diferencial con toroidal separado. Controlador permanente de aislamiento (IT): avisa sin cortar (ITC-BT-24 4.1.3). ITC-BT-28 2.1: en IT, señal acústica o visual.

## 7. Seccionadores

- INSST 2020: seccionadores abren y cierran con corriente despreciable, sin cargas; interruptores, corrientes normales y sobrecarga en servicio. ITC-BT-19 2.6: separación omnipolar; no figura en 2.7. UNE-EN IEC 60947-3.
- Oficio: no se maniobra en carga; abrir interruptor y luego seccionador.
- RD 614/2001 anexo IV B.1: prever maniobras erróneas (abrir seccionadores en carga, cerrar en cortocircuito); sin protección frente a arco si hay alejamiento u obstáculos. A.1: maniobras, mediciones, ensayos y verificaciones, sólo autorizados.
- INSST: enclavamientos contra apertura con carga, resguardos, accionamiento a distancia.

## 8. Selectividad

- Oficio: abre sólo la protección inmediatamente aguas arriba. Art. 16.2: subdividir. ITC-BT-19 2.4: protecciones coordinadas y selectivas con las generales que las preceden.
- ITC-BT-17 1.2: diferenciales en serie, selectividad. ITC-BT-24 4.1.1 (TN): temporizados (tipo S) en serie; 4.1.2 (TT): máximo 1 s. ITC-BT-34 3.2: 500 mA selectivos con terminales. ITC-BT-52 6.1: selectivo o retardado. ITC-BT-28 4.d): corte no afecta a más de la tercera parte de las lámparas.
- Oficio, tipos: amperimétrica; cronométrica; energética; lógica; total o parcial; con SAI o grupo, Icc menor (temas 7, 8).
- Oficio: diferencial de arriba menos sensible y retardado; TT, RA 20 Ω: 300 mA S, 6 V ≤50 V.

## 9. Protección frente a sobretensiones

- ITC-BT-23 1: transitorias (atmosféricas, conmutaciones, defectos); nivel según isoceraúnico, acometida, proximidad MT/BT. Sólo 230/400 V c.a., no señales (tema 8). 3: rayo directo no se trata.
- ITC-BT-23 2.2, tabla 1 (1,2/50; 230/400 V; 400/690 y 1000 V): IV 6/8 kV, origen (contadores, telemedida); III 4/6 kV, instalación fija (armarios, aparamenta, canalizaciones); II 2,5/4 kV (electrodomésticos); I 1,5/2,5 kV (ordenadores, electrónicos), protección fuera del equipo.
- ITC-BT-23 4: soportada no inferior a tabla 1; menor sólo en natural con riesgo aceptable o controlada protegida. 2.1: cascada basta, media, fina (oficio: IV, III, I).
- ITC-BT-23 3.1: natural = no precisa; red subterránea completa o línea aérea aislada con pantalla a tierra en ambos extremos. 3.2: controlada = línea aérea de conductores desnudos o aislados, protección en el origen; por decisión (continuidad, valor). ITC-BT-17 1.2: DPS si fuese necesario.
- ITC-BT-23 3.2: nivel de protección (ITC-BT-01: cresta más elevada en bornes) inferior a la soportada de la categoría; III <4 kV; I <1,5 kV.
- ITC-BT-23 3.2 conexión: TT o IT, cada conductor (neutro incluido) y tierra; TN-S, cada fase y PE; TN-C, cada fase y neutro.
- Schneider cap. J: tipo 1 10/350 µs, Iimp, edificios con protección contra el rayo; tipo 2 8/20 µs, Imax, cada cuadro; tipo 3 1,2/50 µs, cargas sensibles. Uc máxima de servicio continuo; Up bajo la soportada; In 8/20 µs, ≥19 veces. 
- ITC-BT-52 6.4: DPS sin protección propia lleva la del fabricante aguas arriba; equipo lejano, DPS adicional coordinado; temporales máximo 440 V fase-neutro; ITC-BT-02: UNE-EN IEC 63052. ITC-BT-09 4: DPS si los equipos lo precisan.
