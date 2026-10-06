# Tema 1 del específico de Operador/a Informático · Sistemas de información, arquitectura de ordenadores y componentes del equipo

**Siglas**: SI sistema de información; CIO responsable de SI; CPU, ALU, UC; GPU, NPU; RAM, ROM, EEPROM, DDR; E/S; SSD; NVMe, PCIe; NIC; USB, USB PD; UEFI, BIOS; PC (ordenador personal; contador de programa = *program counter*); NAS, SAN; TPM; SoC; WDDM; SLAT; TOPS; RISC, CISC; CPI; ISA; AVR; LTSC; RTVA, CSRTV, BOJA.

Esqueleto para repasar, no resumen: sin norma jurídica; la fuente delante de cada línea; fuentes leídas el 05 y 06-10-2026.

<!-- indice --><!-- /indice -->

## 1. Elementos constitutivos de un sistema de información

- Sin definición legal; manual Bourgeois et al., *Information Systems for Business and Beyond* (2019): las definiciones se fijan en componentes y en papel en la organización.
- Laudon y Laudon 13.ª (2014): componentes relacionados que recogen, procesan, almacenan y distribuyen información para apoyar decisiones y control en una organización.
- Valacich y Schneider 4.ª (2010): hardware, software y redes que las personas construyen y usan para recoger, crear y distribuir datos útiles. Laudon y Laudon 12.ª (2012): recoger, procesar, almacenar, diseminar; decisiones, coordinación, control, análisis, visualización.
- Bourgeois, cinco componentes: hardware, software, datos, personas, procesos; los tres primeros, tecnología; personas y procesos separan los SI de la informática.
- Hardware: parte tangible. Software: instrucciones, intangible; SO y aplicaciones.
- Datos: colección de hechos; sueltos valen poco; en base de datos, herramienta potente.
- Personas: soporte de primera línea, analistas, desarrolladores, hasta el CIO. Procesos: serie de pasos hacia un resultado; fin: mejorar procesos interna y externamente.
- Sexto componente propuesto, comunicación (Bourgeois): primeros PC autónomos; técnicamente hardware y software, pero tan central que es categoría propia.
- Funciones (Laudon): recoger/entrada (teclado, escáner); procesar (hoja, consulta); almacenar (disco, carpeta compartida); distribuir/salida (pantalla, impresora, correo).
- Escalera (Bourgeois): dato (hecho aislado), información (organizado, con sentido), conocimiento (lo que la organización aprende).
- Características (sin lista cerrada en fuente; deducidas): componentes relacionados que funcionan juntos; tecnología + personas + procesos; finalidad organizativa (decisiones, control); datos sin organizar «not very useful».
- Propiedades (oficio, tema 14): confidencialidad, integridad, disponibilidad.

## 2. Arquitectura de ordenadores

- Bourgeois cap. 2: digital = valores discretos, analógico = continuo; binario.
- Bit: uno o cero. Byte: 8 bits; máximo 255 (11111111). Palabra: bits procesados a la vez; primeros PC 8, hoy 64.
- Von Neumann, *First Draft of a Report on the EDVAC*, 30-6-1945, Moore School (Pensilvania), § 2: CA aritmética central (§ 2.2); CC control central (§ 2.3), encadena las operaciones; M memoria (§ 2.5), resultados intermedios, instrucciones, tablas, datos; I entrada (§ 2.7, cuarta parte); O salida (§ 2.8, quinta parte); CA + CC = C (§ 2.6), antecedente de la CPU.
- Rasgo del modelo: toda la memoria como un solo órgano, instrucciones y datos (§ 2.5).
- UCM, *Estructura de Computadores* tema 1 (2011-12): el computador actual sigue siendo von Neumann, máquina secuencial de datos escalares. Cinco características: organización lineal de memoria; palabra de longitud fija; espacio único de direcciones; memoria única para datos e instrucciones; ejecución secuencial salvo ruptura de secuencia.
- Añadidos: interrupciones (interrumpen un programa por señal externa), caché, memoria virtual.
- Harvard: memorias y buses separados (Microchip ATmega328P, apartado 7 «AVR CPU Core»); mientras se ejecuta una instrucción se pre-lee la siguiente.
- Von Neumann: una memoria, propósito general; Harvard: dos, microcontroladores (oficio); eco en el PC: UCM tema 6, cachés independientes de datos e instrucciones frente a unificadas.
- Bus (Bourgeois): conexiones eléctricas entre componentes; velocidad = rapidez × bits a la vez.
- Tres buses (oficio): datos; direcciones (posición o dispositivo); control (lectura, escritura, reloj, interrupciones).
- n líneas = 2^n posiciones: 16 → 65.536; 32 → 4.294.967.296 (4 GiB a un byte); cada línea más duplica.
- Registros: Arm, memoria ultrarrápida para datos temporales; UCM tema 1: ruta de datos = registros + UAL + buses.
- Contador de programa (MIT 6.004, cap. 14): guarda la dirección de la siguiente instrucción; la CPU lo incrementa tras cada una, salvo saltos, llamadas, interrupciones; en interrupción salva en la pila PC y registro de estado RE (UCM tema 8).
- MIT: «fetch/execute loop». Ciclo (Arm), cuatro fases: Fetch trae la siguiente instrucción; Decode interpreta y determina recursos; Execute realiza la operación; Store escribe en memoria o registro.
- Segmentación (*pipelining*): solapa etapas de instrucciones distintas (Arm); UCM tema 4: una etapa de cada una por ciclo.
- Jerarquía (UCM tema 5), de más rápida a más lenta: registros; caché L1, L2, L3; RAM; discos magnéticos; cintas, CD-ROM (externo). Arriba velocidad, abajo capacidad. Interna (CPU): registros, caché, principal; externa (E/S): discos, cintas.
- Caché (UCM tema 6): pequeña y rápida entre CPU y principal; nivel i+1 copia bloques del i con más probabilidad de uso (tema 5); L2 entre L1 y principal..
- Localidad (tema 6): temporal (lo reciente se repite; bucles); espacial (lo próximo se referencia; ejecución en orden, estructuras regulares).
- ISA: interfaz hardware-software (MIT). CISC (UCM tema 1): repertorio complejo y numeroso, muchos direccionamientos y modos de control, reduce distancia con lenguajes de alto nivel; microprogramación. RISC: pocas instrucciones simples y rápidas; el compilador las combina.
- UCM tema 4, CISC / RISC: muchas operaciones básicas, direccionamientos complejos / pocas, simples; largas, formatos diversos, descodificación lenta / formato simple, tamaño fijo, rápida; pocas instrucciones por programa, CPI elevado / muchas, CPI reducido; registros de propósito general limitados / elevados; operandos en registros y memoria (RM y MM) / sólo entre registros (RR), carga/almacenamiento.
- MIT: CISC con longitud variable complica búsqueda y descodificación; RISC popular en los ochenta. Arm: una acción por instrucción, un ciclo; longitud fija, fácil de segmentar; alto rendimiento por vatio en batería.
- Arm = RISC («Advanced RISC Machine», Arm Ltd.); UCM tema 2: 16 registros de 32 bits; común en móviles, tabletas, portátiles, consolas, sobremesa; Snapdragon de Copilot+ es Arm.
- Hardware, cinco funciones (oficio): proceso (CPU); memoria principal (RAM volátil, ROM no volátil); almacenamiento (disco, SSD, flash); entrada; salida.
- Software, tres capas (oficio): sistema (SO, controladores, utilidades); programación (compiladores, intérpretes, entornos); aplicación (ofimática). Bourgeois: SO cargado por el programa de arranque; gestiona recursos de hardware, da interfaz de usuario, plataforma para desarrolladores (tema 5).
- Licencia (oficio): propietario (código no distribuido); libre (usar, estudiar, modificar, redistribuir); freeware, shareware: gratuitos o de prueba, no necesariamente libres.
- Generaciones (años aproximados, oficio): 1.ª válvulas, 1940-mediados cincuenta; 2.ª transistores, hasta los sesenta; 3.ª circuitos integrados, sesenta-primeros setenta; 4.ª microprocesador, desde los setenta; 5.ª paralelo e IA, desde los ochenta, discutida, por objetivo.
- Bourgeois: primera CPU a comienzos de los setenta; Altair 8800, 1975; IBM PC 1981.
- Ley de Moore (Intel, 18-9-2023): transistores de un circuito integrado se duplican cada dos años con coste mínimo; 1965 cada año durante 10 años; revisión de 1975 cada dos. Se duplican transistores, no circuitos ni velocidad; no es ley científica; *Electronics Magazine* vol. 38 n.º 8, 19-4-1965.

## 3. Componentes internos de los equipos microinformáticos

- CPU: «cerebro», ejecuta órdenes del software; Intel y AMD. Reloj en hercios (1 GHz = mil millones de ciclos/s). Núcleos: dual-core 2, quad-core 4; Windows 11 pide al menos dos. Caché: datos frecuentes del programa.
- Placa base: en ella se conectan CPU, memoria y almacenamiento; buena parte del bus; integra NIC, vídeo, sonido (gráfica o red añadida = ampliación).
- RAM (Bourgeois): memoria de trabajo, carga desde el almacenamiento, mucho más rápida que el disco, todo programa en ejecución va a RAM; volátil (sin corriente se pierde); más RAM suele dar más velocidad; módulos DDR, tipo decidido por la placa (incompatibilidad entre generaciones = oficio).
- Memoria frente a almacenamiento: RAM rápida y volátil; almacenamiento lento y persistente.
- ROM no volátil, sólo lectura. Firmware hoy UEFI (Windows 11: UEFI, Secure Boot capable). UEFI/BIOS y arranque seguro: tema 6; mensajes de error: tema 2.
- Disco duro: no volátil. SSD: memoria flash con chips EEPROM, mucho más rápido, más fiable sin partes móviles. NVMe: interfaz y juego de órdenes para almacenamiento sobre PCIe, estándar de hecho de SSD PCIe (NVM Express). Flash, NAS, SAN, recuperación: tema 3.
- NIC: tarjeta de expansión; mediados de los noventa, Ethernet en placa; principios de los 2000, inalámbrica integrada. Averías gráficas y red: tema 2; redes: tema 13.
- Puertos: en la placa, accesibles desde fuera; USB (1996) casi todo; Bluetooth para teclados, altavoces, auriculares. Conectores (USB, RJ45, VGA, DVI, HDMI, DisplayPort): tema 4.
- Periféricos (oficio): entrada (teclado, ratón, escáner, micrófono); salida (monitor, impresora, altavoz); entrada y salida (disco, memoria portátil, NIC, pantalla táctil). Regla: ¿hace las dos cosas? Pantalla táctil sí, monitor no.
- Velocidad (Bourgeois): CPU, placa, RAM, disco duro, sustituibles. CPU: reloj, GHz; bus: MHz; RAM: tasa de transferencia, MB/s; disco duro: tiempo de acceso (ms) y tasa de transferencia (Mbit/s).
- Aplicación (oficio): lento con varios programas = RAM (lo que no cabe va al disco); tarda en arrancar = disco (a SSD, la mejora que más se nota). Medir: tema 2.

## 4. Tecnologías actuales aplicables al puesto de usuario

- Windows 11, mínimos (Microsoft Learn, 14-7-2026): procesador 1 GHz o más, dos o más núcleos, 64 bits compatible o SoC; memoria 4 GB o más; almacenamiento 64 GB disponibles; gráfica DirectX 12 o posterior con WDDM 2.0; firmware UEFI con arranque seguro; TPM 2.0; pantalla HD 720p, 9" o más, 8 bits por canal; internet para actualizaciones (Home: cuenta Microsoft e internet en la primera configuración).
- Funciones que piden más: BitLocker to Go (USB; Pro y superiores); Client Hyper-V (SLAT; Pro y superiores); Teams (cámara, micrófono, altavoz); Windows Hello (cámara IR o huellas; si no, PIN o llave); Snap tres columnas (1920 píxeles efectivos de ancho). Instalación, discos, seguridad: tema 6.
- Windows 10 (Microsoft Learn): fin de soporte 14-10-2025; 22H2 última versión; LTSC con su ciclo. A 24-IX-2026 Home o Pro fuera de soporte; puesto de referencia Windows 11; si no cumple, sustituir o ampliar.
- Copilot+ (Microsoft Learn, 17-11-2025): NPU de más de 40 TOPS; ejecuta en el equipo operaciones de aprendizaje profundo de IA; trabaja con CPU y GPU, Windows 11 asigna cada tarea; umbral 40+ TOPS (billones de operaciones/s); Snapdragon X Elite (Qualcomm, Arm), AMD Ryzen AI 300, Intel Core Ultra 200V; Administrador de tareas muestra la NPU.
- USB-IF: versión = velocidad, Type-C = conector, PD = energía; USB 3.2 sólo define la tasa; no es Type-C, PD ni Battery Charging.
- Cinco velocidades (USB4 y USB 3.2): 80, 40, 20, 10, 5 Gbps; nombres al público «USB 80Gbps», «USB 40Gbps», «USB 20Gbps», «USB 10Gbps», «USB 5Gbps»; nombres técnicos (USB4 Version 2.0/1.0, USB 3.2, SuperSpeed Plus, Enhanced SuperSpeed, SuperSpeed+) no en producto ni cara al consumidor.
- Tabla: 1,5 y 12 Mbit/s Basic-Speed (logo Basic-Speed); 480 Mbit/s USB 2.0 Hi-Speed (logo Hi-Speed); 5 Gbit/s USB 3.2 Gen 1; 10 Gbit/s Gen 2; 20 Gbit/s Gen 2x2 (dos carriles de 10) o USB4 20Gbps; 40 Gbit/s USB4 40Gbps; 80 Gbit/s USB4 con cables certificados para 80 Gbit/s.
- USB 3.2: tres velocidades (Gen 1 5Gbps, Gen 2 10Gbps, Gen 2x2 20Gbps); USB4: dos (20, 40Gbps); página vigente: hasta 80 Gbps. Velocidad por versión 1.0 o 2.0: no atada.
- USB4: basado en Thunderbolt (Intel), dobla el ancho de banda agregado, datos y vídeo simultáneos; compatible con todas las versiones; la conexión se ajusta a la mejor capacidad mutua (USB 3.2: velocidad común más baja).
- Type-C: conector y sentido de cable reversibles. USB PD 3.1 (2021): hasta 240 W con cable Type-C completo; antes 100 W (20 V, 5 A). Sentido no fijo: quien tiene energía (host o periférico) la da; monitor con alimentación carga el portátil mostrando imagen: un cable.
- Thunderbolt (marca de Intel): TB4 siempre 40 Gbps con datos, vídeo y energía; TB5 (Intel, 12-9-2023) 80 Gbps bidireccional, hasta 120 Gbps con Bandwidth Boost; sobre USB4 V2, DisplayPort 2.1, PCIe Gen 4; compatible con anteriores. Conectores: tema 4.
- Caso (2 núcleos a 3 GHz, 8 GB, 120 GB libres, UEFI con arranque seguro desactivado, sin TPM 2.0 activo): cifras sí, modelo compatible por comprobar (tema 6); UEFI sí (exige ser capaz); TPM 2.0 no hasta activarlo. No pasa tal cual; obstáculo el TPM, no la potencia (oficio).

## Lo que este tema no da

- Sin fuente: lista cerrada de características de un SI; DDR5 y PCIe con velocidades (Bourgeois llega a DDR4); alimentación, refrigeración, chipset; registro de instrucción, acumulador; x86 como CISC; coste por bit; USB4 por versión; vatios de Thunderbolt 4 y 5; actualizaciones extendidas de Windows 10; equipos y SO del puesto en RTVA o CSRTV.
- Remite: diagnóstico, BIOS, benchmark, tema 2; almacenamiento, 3; periféricos y conectores, 4; SO, 5; Windows 11, 6; virtualización, 10; seguridad, 14.
