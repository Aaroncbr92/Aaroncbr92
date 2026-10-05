# Tema 5 del específico de Oficial Técnico Electricista · Puestas a tierra y equipotencialidad: esquemas de conexión, mediciones, continuidad, resistencia de tierra, protección de personas y compatibilidad con equipos sensibles

**Siglas**: REBT, ITC-BT, CP, CPN, TT, TN, TN-S, TN-C, TN-C-S, IT, MBTS, ID, CT, IP, RA, Ia, IΔn, Id, Zs, U0, U, UL, ρ.

Esqueleto para repasar, no resumen: lo que falta se estudia en el tema. Fuente: RD 842/2002; «of.»: oficio.

<!-- indice -->
- 1. Puestas a tierra y equipotencialidad
- 2. Esquemas de conexión
- 3. Mediciones
- 4. Continuidad
- 5. Resistencia de tierra
- 6. Protección de personas
- 7. Compatibilidad con equipos sensibles
<!-- /indice -->

## 1. Puestas a tierra y equipotencialidad

- ITC-BT-18, 1: objeto: limitar tensión de masas, asegurar protecciones, reducir riesgo de avería. 2: unión directa «sin fusibles ni protección alguna»; sin diferencias de potencial peligrosas; paso de corrientes de defecto y de rayo.
- ITC-BT-01: tierra (potencial 0 convencional); masas: partes metálicas accesibles, excepto clase II, armaduras de cables y conducciones de agua/gas; parte que sólo se energiza vía una masa, no es masa; resistencia de puesta a tierra = V/I.
- 3.1 electrodos: barras, tubos, pletinas, conductores desnudos, placas, anillos/mallas, armaduras de hormigón (no pretensadas), otras apropiadas. Profundidad ≥ 0,50 m. Cu clase 2 UNE 21.022. No valen canalizaciones de otros servicios; envolventes de plomo sí, con permiso del propietario.
- 3.2 tabla 1 (tierra enterrado): protegido corrosión y mecánicamente: según 3.4; protegido corrosión, sin protección mecánica: 16 mm² Cu / 16 acero galvanizado; sin protección corrosión: 25 Cu / 50 hierro. Nunca < CP.
- 3.3 borne principal: tierra, CP, equipotencial principal, tierra funcional. Dispositivo de medida: accesible, desmontable con útil, seguro, continuo.
- 3.4 CP: unen masas. Sección tabla 2 (= ITC-BT-19, 2.3) o UNE 20.460-5-54, 543.1.1: S ≤ 16 → Sp = S; 16 < S ≤ 35 → 16; S > 35 → S/2. No normalizado → superior; otro material → conductividad equivalente; común → mayor fase.
- 3.4 fuera de canalización: Cu 2,5 mm² con protección mecánica, 4 mm² sin ella. Agua, gas, estructuras no son CP/CPN; envolventes de fábrica y canalizaciones prefabricadas sí.
- ITC-BT-19, 2.2.4: CP verde-amarillo; neutro azul claro; fases marrón/negro; gris.
- ITC-BT-18, 4: con sobreintensidad, CP en la misma canalización o inmediata. 5: tierra funcional; 6: ambas → prevalece protección.
- ITC-BT-18, 7 CPN: sólo TN; CP ≥ 10 mm² Cu/Al fijo, sin diferencial en la parte común; excepción 4 mm² Cu concéntrico, conexiones duplicadas; aislado a la tensión más alta. Separados neutro y protección, prohibido reunirlos aguas abajo; bornes/barras separados; CPN al borne del CP.
- ITC-BT-26, 3.1: edificio nuevo: anillo cerrado de Cu desnudo en cimentación, picas si hace falta, malla entre edificios próximos; ≥ 1 hierro principal por zapata; soldadura aluminotérmica o autógena. 3.2: se conectan masas importantes, gasóleo, calefacción, agua, gas, antenas.
- ITC-BT-26, 3.3 puntos: patios de luces, contadores, ascensores, caja general de protección, locales de servicios. 3.4 líneas principales: Cu, ≥ 16 mm²; no tuberías, cubiertas, bandejas ni canales.
- ITC-BT-18, 8: principal ≥ mitad del CP mayor, mínimo 6 mm², reducible a 2,5 si Cu (condición no consta en el BOE); suplementario masa-elemento ≥ mitad del CP de la masa; por elementos no desmontables, conductores o ambos.
- ITC-BT-27, 2.2: baños, equipotencial local en volúmenes 1, 2, 3. ITC-BT-05, 6.2: falta de equipotenciales: defecto grave.

## 2. Esquemas de conexión

- ITC-BT-08, 1: protecciones dependen del esquema. T 1ª: alimentación directa a tierra; I: aislada o por impedancia; T 2ª: masas a tierra propia; N: masas al punto de alimentación a tierra; S = neutro y protección separados; C: combinados (CPN).
- 1.1 TN: alimentación a tierra, masas a ese punto por CP. TN-S separados en todo; TN-C combinados en todo; TN-C-S combinados en parte. Defecto franco: cortocircuito, bucle todo metálico.
- 1.2 TT: alimentación a tierra, masas a toma separada; defecto menor que cortocircuito pero peligroso.
- 1.3 IT: sin punto directo a tierra, masas a tierra; primer defecto sin tensiones peligrosas (sin conexión o impedancia); no distribuir neutro.
- 1.4: a) red pública (neutro a tierra) alimentando directamente: TT; b) desde CT de abonado, cualquiera de los tres; c) IT en parte, con transformadores adecuados.
- ITC-BT-28, 2.1: servicios de seguridad, IT con controlador permanente (señal acústica o visual).
- ITC-BT-08, 2 (red TN): R neutro ≤ 5 Ω; global ≤ 2 Ω.

## 3. Mediciones

- ITC-BT-03, apéndice I, 2.1.2 (equipos mínimos): telurómetro; medidor de aislamiento (remite a ITC MIE-BT 19; vigente ITC-BT-19, 2.9); medidor de fugas ≤ 1 mA; verificador de disparo de diferenciales (característica intensidad-tiempo); verificador de continuidad; medidor de bucle ≤ 0,1 Ω, medición independiente o compensación de cables.
- Telurómetro (of.): separar electrodo por el dispositivo; dos picas alineadas (corriente lejos, tensión en medio); inyectar corriente, medir tensión, R = V/I. Pica de tensión en zona de potencial nulo (si al moverla la lectura cambia, picas cerca).
- Avisos: sin separar se mide el paralelo (resistencia global), menor y falso; cuenta el caso más seco (ITC-BT-18, 12). Cerrar el dispositivo y comprobar continuidad. Registrar fecha, terreno, valor; R creciente: corrosión o conexión floja.
- Of.: bucle Zs comprueba Zs × Ia ≤ U0; verificador de ID mide tiempo de disparo (botón de prueba sólo mecanismo, tema 3). Instrumentos: tema 14.
- Aislamiento, ITC-BT-19, 2.9, tabla 3: ≤ 500 V nominal, ensayo 500 V c.c., ≥ 0,5 MΩ; conjunto ≤ 100 m (si excede, fraccionar); respecto a tierra y entre conductores; con electrónica, fases y neutro unidos.

## 4. Continuidad

- ITC-BT-18, 3.4: ningún aparato en el CP (conexiones desmontables con útil para ensayos); masas no en serie (salvo envolventes de fábrica y canalizaciones prefabricadas); conexiones accesibles (salvo cajas selladas con relleno o no desmontables con juntas estancas); CP protegidos contra daños mecánicos, químicos, electroquímicos y esfuerzos electrodinámicos.
- ITC-BT-19, 2.3: uniones soldadas sin ácido o apriete por rosca, accesibles, inoxidables, antidesapriete; CP no común a tensiones distintas; canalización móvil con CP dentro.
- ITC-BT-05, 6.2, defectos graves (no exhaustivo): falta de continuidad de CP; R de tierra elevada respecto a las medidas; defecto de conexión de CP a masas preceptivas; sección insuficiente de CP; falta de equipotenciales requeridas; sin medidas contra contactos indirectos; falta de identificación de neutro y protección. Defecto grave: sin peligro inmediato, puede serlo al fallar la instalación.
- Comprobación (of.): sin tensión; verificador entre borne principal (o barra del cuadro) y cada masa y equipotenciales; compensar cables; valor bajo; alto o inestable: conexión floja o cortada;. En tensión: bucle alto o abierto: CP defectuoso.

## 5. Resistencia de tierra

- ITC-BT-18, 9: R en cualquier circunstancia previsible ≤ valor especificado; tensiones de contacto ≤ 24 V en local o emplazamiento conductor, ≤ 50 V en los demás.
- ITC-BT-24, 4.1.2 (TT): RA × Ia ≤ U; RA = tierra + CP de masas; Ia = IΔn; U: 50, 24 V u otras; RA ≤ U/IΔn. Máximos 50 V / 24 V: 30 mA: 1.667 / 800 Ω; 300 mA: 167 / 80 Ω; 1 A: 50 / 24 Ω; manda el ID menos sensible.
- ITC-BT-18, 9: R depende de dimensiones, forma y ρ (varía por punto y profundidad). Tabla 3 (Ω·m, orientación): pantanosos unidades a 30; humus 10-150; arcilla plástica 50; arena silícea 200-3.000; pedregoso desnudo 1500-3.000; calizas 1.000-5.000; granitos y gres 1.500-10.000.
- Tabla 4: fértiles y terraplenes húmedos 50; terraplenes poco fértiles 500; pedregosos, arenas secas 3.000.
- Tabla 5: placa R = 0,8 ρ/P; pica R = ρ/L; conductor horizontal R = 2 ρ/L (P perímetro, L longitud).
- ITC-BT-18, 10: tomas independientes si una no pasa de 50 V respecto a potencial cero cuando por la otra circula la máxima corriente de defecto.
- 11: masas de utilización y CP no unidas a la tierra de masas del CT. Sin control del 10, independientes si: a) sin canalización metálica conductora entre zonas; b) distancia ≥ 15 m (ρ < 100 Ω·m; terreno muy malo, fórmula en imagen, no consta); c) CT en recinto aislado o, contiguo/interior, sin unión metálica con los locales. Unir sólo si Vd = Id × Rt < tensión de contacto máxima aplicada; remite a MIE-RAT 13, 1.1 (RD 3275/1982), derogado por RD 337/2014 (DDU, salvo DT 1ª.1).
- 12: comprobación al dar de alta por Director de Obra o empresa instaladora; al menos anual, personal técnicamente competente, terreno más seco, midiendo R y reparando con urgencia; al menos cada 5 años, si el terreno no conserva electrodos, descubrir electrodos y conductores de enlace.
- ITC-BT-05, 4.1: pública concurrencia, inspección cada 5 años revisa tierra (tema 2).

## 6. Protección de personas

- ITC-BT-01: directo: contacto con partes activas; indirecto: con partes en tensión por fallo de aislamiento. ITC-BT-24: directos: aislamiento, barreras/envolventes, obstáculos, alejamiento, complemento ID ≤ 30 mA. Indirectos: corte automático, clase II, locales no conductores, equipotencial local no a tierra, separación eléctrica.
- ITC-BT-24, 2: MBTS protege de directos e indirectos. 3.2: IP XXB mínimo; superficies horizontales superiores IP4X o IP XXD. 3.5: ID ≤ 30 mA complementaria, no completa (tema 3).
- 4.1: límite convencional 50 V c.a.; menos en casos (24 V alumbrado público, ITC-BT-09, 10).
- 4.1.1 TN: Zs × Ia ≤ U0. Tabla 1: U0 230 V: 0,4 s; 400 V: 0,2 s; > 400 V: 0,1 s. Fusibles, automáticos, diferenciales; TN-C sin diferencial; TN-C-S con diferencial, sin CPN aguas abajo y CP al CPN aguas arriba.
- 4.1.2 TT: RA × Ia ≤ U; sobreintensidad de tiempo inverso: disparo ≤ 5 s, o instantáneo; selectividad con diferenciales «S», ≤ 1 s; neutro (o una fase) de cada generador/transformador a tierra (grupo, tema 7).
- 4.1.3 IT: ningún activo a tierra; masas a tierra individual o por grupos; primer defecto sin corte, RA × Id ≤ UL; controlador: señal acústica o visual. Segundo defecto: masas por grupos: TT sin neutro a tierra; interconectadas: TN: neutro no distribuido 2 × Zs × Ia ≤ U; distribuido 2 × Zs' × Ia ≤ U0.
- IT tabla 2 (neutro no distribuido / distribuido): 230/400 V 0,4 / 0,8 s; 400/690 V 0,2 / 0,4 s; 580/1000 V 0,1 / 0,2 s. UNE 20.460-4-41: hasta 5 s. Si no se cumple con sobreintensidad: ID por aparato o equipotencial complementaria.
- 4.2 clase II: doble o reforzado, sin tierra de protección. 4.3 no conductor: sin CP; paredes y suelos ≥ 50 kΩ (hasta 500 V) o 100 kΩ (> 500 V); paredes aislantes y: a) ≥ 2 m (1,25 m fuera del volumen de accesibilidad); b) obstáculos; c) aislamiento ≥ 2.000 V, fuga ≤ 1 mA.
- 4.4 equipotencial local sin tierra, ni directa ni por masas o elementos. 4.5 separación: transformador de aislamiento; un aparato, masas sin CP; varios, equipotenciales aislados sin tierra.
- ITC-BT-01: tensión de contacto (entre partes accesibles a la vez), de defecto (entre masas, masa y elemento, masa y tierra de referencia), de puesta a tierra; choque eléctrico. Tensión de paso: no la define el REBT; INSST (ITC-RAT 01): puntos del terreno a 1 m; menor con menor R.

## 7. Compatibilidad con equipos sensibles

- ITC-BT-18, 5: tierra funcional correcta y fiable; 6: con protección, prevalece la protección; 3.3: tierra funcional al mismo borne principal; 7: no reunir neutro y protección aguas abajo (of.: zumbido).
- ITC-BT-19, 2.3: CP distinto por cada sistema de protección en instalaciones próximas. 2.9: aislamiento con electrónica, fases y neutro unidos.
- El REBT no regula tierras limpias, de señal ni independientes; toda tierra técnica va al borne principal. CEM y rack: tema 8.
- Zumbido (of.): 50 Hz: red (fuente o bucle de masa); 100 Hz: rizado del rectificador (fuente). Cambia al mover cables: bucle de masa.
- Bucle de tierra (of.): cable apantallado y dos caminos a tierra, 50 Hz por la malla; causas: fugas en CP largos, neutro a tierra aguas abajo, protección floja.
- Sala técnica (of.): una referencia de tierra por área, CP en estrella a la barra del cuadro; equipotencializar racks, bandejas, falso suelo; circuitos sensibles separados de fuerza, iluminación y clima, con transformador de aislamiento propio; repartir cargas de fuente conmutada (fugas, disparo del ID).
- Nunca cortar el CP ni usar adaptador sin tierra: incumple ITC-BT-18, 6; «falta de continuidad de los conductores de protección» (ITC-BT-05, 6.2).
