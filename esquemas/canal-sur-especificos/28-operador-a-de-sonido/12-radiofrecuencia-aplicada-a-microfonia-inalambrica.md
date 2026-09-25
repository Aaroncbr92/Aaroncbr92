# Tema 12 del específico de Operador/a de Sonido · Radiofrecuencia aplicada a microfonía inalámbrica

**Siglas**: RTVA; CSRTV; CNAF; UN; CEPT; ERC/REC 70-03; ETSI; EN; UE; PMSE; TDT; PPDR; DECT; p.r.a.; p.i.r.e.; RF; AF; RFI; IM; LO; FI/IF; AM; FM; PM; QPSK; QAM; OFDM; RSSI; GSM; IEM; BNC.

Esqueleto para repasar, no resumen: cada línea manda a su epígrafe del tema.

<!-- indice --><!-- /indice -->

## Radiofrecuencia aplicada a microfonía inalámbrica (fundamentos)

- Cálculo: λ (m) = 300 / f (MHz). Shure, 500 MHz → λ/4 ≈ 15 cm (tabla del tema).
- Shure: antena de VHF no vale para UHF, y viceversa.
- Modulación: AM → amplitud; FM → frecuencia (inalámbrico analógico); PM → fase (base de las digitales); QPSK/QAM/OFDM → digitales.
- Ruido eléctrico es de amplitud: por eso la FM lo recorta y la AM no.
- CNAF, nota UN-17: FM de radiodifusión, banda 87,5-108 MHz.
- CNAF (Orden TDF/732/2026, BOE núm. 173, de 17-VII-2026): base, art. 85 Ley 11/2022, espectro dominio público del Estado. Vigente desde el 18-VII-2026; deroga la Orden ETD/1449/2021.
- Bandas de micrófonos (notas UN del CNAF):
  - UN-36: 470-694 MHz (TDT); 50 mW p.r.a.; uso común secundario, sin protección; sólo recintos/eventos temporales; cesa si interfiere a la TV.
  - UN-151: 821,5-832 MHz; PMSE; uso común; ref. ETSI EN 300 422; supletoria ERC/REC 70-03 anexo 10.
  - UN-118: 863-865 MHz; uso doméstico/interior; máx. 10 mW; EN 301 357, EN 300 220, EN 300 422.
  - UN-119: 1785-1805 MHz; profesional, interior; 20 mW p.i.r.e. (50 mW junto al cuerpo).
  - UN-48: 1785-1804,8 MHz; PMSE sin protección; 1785-1800 MHz reservada al Estado (Servicio Fijo) hasta 1-I-2030.
  - UN-95/UN-105: 5 canales VHF (174,100/174,300/175,500/176,300/179,300 MHz); 50 mW p.r.a.; canal máx. 200 kHz; canales 4-5 con más potencia requieren título habilitante.
  - UN-127: 6 canales 188-195 MHz; interior; 50 mW p.r.a.
  - UN-81: 5 canales de 30 MHz (31,500/31,750/37,850/38,300/38,550 MHz); 50 mW; canal máx. 25 kHz; canales 2-3 domésticos, 50 μW.
- Salvedades del CNAF: 1785-1805 (UN-119) vs 1785-1804,8 (UN-48), dos cifras literales sin armonizar. UN-151: texto 821,5-832 MHz, rótulo del cuadro 823-832 MHz (DPA da 823-832 para Europa).
- CNAF sin nota de micrófonos en 1880-1900 MHz (DECT, UN-49) ni en 2,4 GHz.
- UN-17: micro-transmisores de audio, 50 nW, uso común, sin protección.
- UN-105: 10 canales de ayudas auditivas, 174,050-174,500 MHz cada 50 kHz, 2 mW p.r.a.; comparten frecuencia con canales 1-2 de UN-95.
- Uso común = sin asignación previa, dentro de la nota. Secundario/sin protección = si otro servicio molesta, el micro no reclama; si el micro molesta, cesa. Título habilitante = autorización (caso canales 4-5 VHF >50 mW). Interior de recintos: UN-118, UN-119, UN-127 no valen al aire libre.
- CNAF: dos medidas de potencia, p.r.a. y p.i.r.e.; el tema no da la relación entre ellas.
- Disposición adicional 2.ª de la orden: usos temporales/experimentales, autorizados por el Secretario de Estado de Telecomunicaciones, si no causan perturbación.
- Por qué no hay micrófonos por encima de 694 MHz: nota UN-153, banda 700 MHz (694-790 MHz) desde 31-X-2020 a banda ancha inalámbrica (RD-ley 23/2020, art. 12; Decisión UE 2017/899); bloques 698-703/753-758 y 733-736/788-791 MHz a PPDR. Sobre 862 MHz, sistemas terrenales de comunicaciones electrónicas.
- Receptor: LO + FI (ejemplo Shure, FI típica 10,7 MHz) — el LO es una pequeña emisora, puede interferir a otro receptor cercano. Silenciador (squelch): sin él, ruido blanco sin señal; tipos: umbral (puede necesitar reajuste), de ruido (normalmente no), de tono (abre sólo con RF + tono; hace silencioso encender/apagar). Subir el silenciador reduce alcance; bajarlo lo puede aumentar con más ruido. Etapa de entrada: circuito no lineal, origen de la intermodulación.

## Antenas

- Tipos (Shure): cuarto de onda omnidireccional (necesita plano de tierra; no para montaje remoto sin amplificador o plano de tierra); media onda omnidireccional (no necesita plano de tierra, apta para remoto; 3 dB teóricos sobre la de cuarto, rara vez se nota); direccional (yagi o log-periódica; hasta 10 dB de ganancia y 30 dB de rechazo).
- Yagi: apenas se usa, ancho de banda estrecho (un canal de TV). Log-periódica: más ancho de banda, elementos verticales, mínimo 15 m del emisor.
- Regla Shure: para antena remota, siempre media onda o direccional.
- Colocación: visión directa; altura sobre el público (≥2 m); orientación según la del emisor (45° con emisores de mano móviles; nunca horizontal); fuera de bastidores metálicos; separación entre las dos antenas de un receptor: ¼ de onda mínimo (≈40 cm VHF, ≈10 cm UHF), ventaja hasta una onda completa; distancia emisor-receptor ≥5 m, emisor-emisor ≥1 m (15 m con direccionales). DPA: mínimo 30 cm y media onda para diversidad (tema 3).
- Diversidad (combate el multitrayecto): usar 2 antenas, separación ≥¼ onda. Tipos: combinación pasiva (no es diversidad verdadera); diversidad de fase (activa, ruido de conmutación posible); conmutación de antenas (sin cancelación, alcance de una antena); conmutación de receptores (buena protección, más cara); combinación de receptores (sin ruido de conmutación, +3 dB S/N).
- Cable y conectores: 50 Ω de baja pérdida (75 Ω, pérdida extra <1 dB); conector BNC. Pérdida aceptable 3-5 dB; por encima, amplificador de antena obligatorio; ganancia neta <10 dB; exceso de amplificación sobrecarga el receptor (cortes, «bleed»).
- Distribución de antena: 2 receptores → repartidor pasivo (≈3 dB por división, máx. un reparto); 3-5 → distribución activa; >5 → maestro/esclavo, no más de 2 niveles en cascada. Repartidor pasivo: riesgo de que un receptor «vea» la tensión de otro.
- Combinación: varias antenas para un receptor (varias salas) → combinador pasivo, ≥3 dB de pérdida. Varios emisores (IEM) a una antena: 2 → combinador pasivo; >2 → combinador activo (4-8 emisores); combinadores activos nunca se cascadean entre sí (unión con uno pasivo).

## Coordinación de frecuencias

- Dos pasos (Shure): elegir banda (CNAF); elegir frecuencia dentro de la banda (física, cálculo, normativa).
- Número finito de sistemas simultáneos por banda; fabricantes dan grupos precalculados y programas propios para casos complejos.
- Una frecuencia por micrófono: dos emisores en la misma no se pueden demodular a la vez → efecto captura (la señal más fuerte se impone) o ninguna se oye bien.
- Banda/grupo/canal: banda = margen de RF; grupo = canales calculados por el fabricante para no interferirse; canal = frecuencia dentro del grupo. Dos emisores del mismo inalámbrico doble, mismo grupo (contraintuitivo: no «separarlos todo lo posible»). El grupo vale sólo dentro de una marca/serie; entre marcas o con IEM, coordinación con programa.
- Separación mínima entre canales: 300 kHz a 1,5 MHz según selectividad del receptor; cada sistema nuevo debe guardar esa distancia con todos los anteriores.
- Intermodulación (IM): aparece en circuitos no lineales del propio equipo, por cercanía entre emisores o de emisores a receptores. Se cuidan sólo los órdenes impares; relevantes, 3.º y 5.º orden.
  - Fórmulas 2 emisores: IM1 = 2f1 − f2; IM2 = 2f2 − f1; con F = f2 − f1: IM1 = f1 − F; IM2 = f2 + F. Ejemplo Shure: f1=180, f2=190 MHz → IM1=170, IM2=200 MHz.
  - 3 emisores: productos f1+f2−f3, f1−f2+f3, f2+f3−f1. Ejemplo Shure (200/195/187 MHz) → 208/192/182 MHz.
  - 5.º orden de 2 emisores: normalmente débil, salvo proximidad extrema; de 3 emisores, en general sin importancia.
  - Margen recomendado: 250 kHz entre cualquier producto de 3.er orden y cualquier frecuencia de trabajo.
  - Caso de cálculo propio (TDT): 606,0/606,8 MHz → IM1=605,2, IM2=607,6 MHz; un tercero equiespaciado en 607,6 cae sobre IM2 (trampa clásica); 607,2 MHz cumple separación y deja ≥0,4 MHz a los productos de 2 y 3 emisores.
- Frecuencias internas: LO de un receptor puede entrar en otro cercano (ejemplo Shure: receptor en 200,7 MHz, LO en 190,0 MHz). Frecuencia imagen: a 2×FI del canal (ejemplo, 179,3 MHz con FI 10,7). Espurias del emisor de cristal: armónicos de la frecuencia del cristal (ejemplo, 180 MHz con multiplicador ×9, cristal 20 MHz → espurias en 160/200, 140/220 MHz); no las dan los emisores sintetizados. Margen recomendado en los tres casos: 250 kHz.
- Banda de TDT (470-694 MHz): coordinar exige antes saber qué canales de TV están ocupados en la zona y excluirlos (UN-36); canal de TV europeo, 8 MHz; el plan cambia de ciudad a ciudad.
- Procedimiento de sistema grande: explorar el espectro con los equipos del evento encendidos → descartar TDT ocupada y portadoras → calcular con programa (separación + 250 kHz de IM, incluidos IEM y frecuencias internas) → programar y comprobar. Receptores modernos: reajuste automático a frecuencia libre.
- Comprobación previa (Pre-Show, resumen Shure): pilas ok → receptores encendidos sin emisores (poca/ninguna RF) → emisores uno a uno, comprobar receptor correcto a ≥5 m → todos los emisores a la vez (≥5 m de antenas, ≥1 m entre sí) → escucha fija por sistema → escucha por toda la zona sistema a sistema → escucha con todos los sistemas encendidos.

## Interferencias

- Origen y remedio (tabla Shure resumida): misma frecuencia → una frecuencia por micro, no encender lo que no se usa; canales muy cercanos → respetar 300 kHz-1,5 MHz; intermodulación → recalcular, 250 kHz, separar emisores; frecuencias internas → separar receptores, 250 kHz; TV (470-694 MHz) → excluir canal ocupado, cesar si el micro interfiere; equipos digitales → RFI de banda ancha, alejar receptores/antenas varios pies, en bastidor receptores arriba y digitales abajo; móviles GSM → zumbido/chirrido en conexión o datos, apagarlos cerca; reguladores de iluminación y reactancias → zumbido/hum, alejar; exceso de amplificación de antena → ganancia neta <10 dB; cuerpo y metal → absorben/bloquean RF, antena de petaca libre y separada, antenas fuera de bastidores.
- Multitrayecto: cancelación cuando la onda directa e indirecta llegan con amplitud parecida y fase opuesta; síntomas de menos a más: «noise-up» → «hits» → corte total. Más severo en UHF (zonas de corte más pequeñas y juntas) que en VHF. Remedio: diversidad.
- Los cinco problemas de un montaje (síntesis de oficio): frecuencias libres → explorar y planificar; intermodulación → plan que evite combinaciones; desvanecimiento → diversidad; reparto de antenas → distribuidor; alcance → antena direccional + cable de baja pérdida.
- Diagnóstico (guía de averías Shure, resumen): sin audio ni RF → pila/frecuencia/multitrayecto/alcance; RF sin audio → mute o fallo de fuente; distorsión sin pico → pila baja; distorsión con pico → ganancia de entrada o salida excesiva; ruido con audio bajo → ganancia insuficiente o RFI; ruido con RF baja → subir silenciador; ruido con audio y RF normales → RFI muy fuerte, localizar o cambiar frecuencia; intermitente a distancia → acercar, más ganancia de antena, menos pérdida de cable; intermitente por multitrayecto/obstáculos → diversidad, recolocar, bajar silenciador. Con varios sistemas: distorsión sin pico en varios → misma frecuencia; distorsión con emisores juntos → IM entre emisores; ídem cerca de antenas → IM emisor-receptor; un emisor activa dos receptores → frecuencias iguales/cercanas, armónicos, imagen o IM.
- Durante el programa (reglas Shure): revisar pilas; receptores silenciados hasta que su emisor esté activo; no encender lo que sobra; cortar audio con el mute del emisor, no con el encendido; visión directa y distancias (≥5 m emisor-antena, ≥1 m entre emisores); al terminar, silenciar salidas antes de apagar emisores. Razón: un receptor abierto sin emisor capta lo que haya en su canal; encender/apagar en directo da un golpe de ruido.
- Normativa que el tema invoca: Orden TDF/732/2026 (preámbulo, DA 2.ª, derogatoria, entrada en vigor, notas UN citadas); Ley 11/2022, art. 85 (sólo como la cita el preámbulo).
- Lo que este tema no da: plan de frecuencias ni equipos de RTVA/CSRTV; texto de ERC/REC 70-03, Decisión (UE) 2025/105 y EN 300 422; relación p.r.a./p.i.r.e.; canales de TDT por provincia andaluza; funcionamiento del sistema inalámbrico, formas de emisor, WMAS, petaca, pilas y procedimiento rápido de grupos (tema 3); conectores/cables de audio y vídeo (tema 11); intercom y retornos (tema 8); IEM como sistema de escucha (tema 10); radiodifusión FM/DAB+, RDS; modelos concretos de equipos y programas de coordinación.
