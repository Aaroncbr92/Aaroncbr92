# Puesto 29 · Tema 1 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real del
sistema, como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/01-sistemas-de-informacion-y-arquitectura-de-ordenadores.md`.
Material: `29-investigacion-A-hardware.md` (§ Tema 1, y § 4.1-4.2 para USB y Thunderbolt); RTVE
`temas/tecnica-informatica/17-arquitectura-de-ordenadores-y-virtualizacion.md` y
`temas/gestion-administrativa/08-ofimatica.md` (fila 29/1 de `informes/canal-sur-reuso/informatica.tsv`:
40 %, «actualizar: no»).

## Fuentes releídas y fecha

Todas el 05-10-2026. Las de la investigación se releyeron en sus copias de
`fuentes/canal-sur/informatico/web/` antes de citar: `bourgeois-isbb-2019.txt` (cap. 1, 2 y comienzo
del 3), `ms-win11-requirements.txt`, `ms-win10-lifecycle.txt`, `ms-copilot-pc-npu.txt`,
`usbif-data-performance-language-2024.txt`, `usbif-usb32-language.txt`, `usbif-usb4-language.txt`,
`usbif-original-logo-2024.txt`, `usbif-usb4.txt`, `usbif-charger-pd.txt`, `usbif-typec.txt`,
`intel-tb5-press.txt`, `thunderbolt-tech.txt`, `nvme-about.txt`.

Nuevas en esta fase (huecos de la investigación: von Neumann sin fuente; ley de Moore mal dada por
Bourgeois):

| Fuente | Copia | Qué se leyó |
|---|---|---|
| J. von Neumann, *First Draft of a Report on the EDVAC*, 30-6-1945, texto OCR de Internet Archive (ejemplar Smithsonian) | `fuentes/canal-sur/informatico/web/vonneumann-edvac-1945.txt` | Portada y § 2.1-2.9. El PDF del MIT (web.mit.edu/STS.035) es imagen sin texto; el OCR tiene erratas, así que sólo se citan en negrita los trozos limpios (CA, CC, I, «entire memory as one organ»); M y O van en redonda con su apartado |
| Intel, «Moore's Law», newsroom, 18-9-2023 | `fuentes/canal-sur/informatico/web/intel-moores-law.txt` | Página completa |

Comprobación de literalidad por script (comillas tipográficas, guiones y saltos normalizados): las
116 negritas «…» del tema aparecen tal cual en las fuentes. Dos se corrigieron en la comprobación (una
cita de Bourgeois partida por salto de página, pasada a redonda; la de USB 3.2, partida en tres citas
por las viñetas del PDF).

## Qué se hizo

Cuatro rúbricas en el orden del enunciado: elementos del sistema de información (características y
funciones); arquitectura de ordenadores; componentes internos; tecnologías actuales del puesto. 31
epígrafes; `indice.py`: 7.406 palabras. `refutar_prosa.py`: 0 hallazgos (7 siglas sin presentar en la
primera pasada, corregidas; se quitó la cita de Wi-Fi 6E, llena de siglas sin valor para el tema).
Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. Ficha
escrita a mano (los temas de Canal Sur no están en `portadas.tsv`).

Negrita = literal de la fuente (inglés, con glosa en redonda). Lo copiado de RTVE va en redonda (RTVE
lo tenía en negrita sin ser cita), como en los temas 5-10 del puesto.

Decisiones frente al material:

- Lo propio de RTVE fuera: preguntas 11 y 52, «respuesta oficial», marcas ✔, § 6 «Los datos que el
  examen ha preguntado», remisiones a temas de Técnica de Equipos, «el examen se detiene en la cuarta».
  RTVE 17 § 4 (almacenamiento) y § 5 (virtualización) no entran: son de los temas 3 y 10. RTVE GA 08
  § 3-6 tampoco (sistemas operativos, almacenamiento, amenazas: temas 3, 5, 6 y 14); de § 5 sólo la
  tríada confidencialidad-integridad-disponibilidad.
- Avisos de la investigación respetados: la ley de Moore de Bourgeois («integrated circuits») no se
  copia; se da la de Intel. Lo datado de Bourgeois (Core i7/i9, cuatro generaciones DDR, USB 3.1) no
  entra. DDR5, PCIe y ESU de Windows 10 se declaran en «Lo que este tema no da».
- «Características»: sin fuente que dé lista; el tema deduce cuatro rasgos de las definiciones y lo
  dice, y añade la tríada CIA (RTVE GA 08 § 5.1).
- Hueco nuevo detectado y declarado: las fuentes leídas no atan cada velocidad de USB4 a su versión
  1.0 o 2.0 (la investigación daba 80 Gbit/s = USB4 v2 por inferencia). La tabla dice «USB4, sobre
  cables certificados para 80 Gbit/s».
- Requisitos de Windows 11: el tema 6 los da en castellano (es-es); aquí se citan de la página en
  inglés leída en esta fase y se remite al 6 para la instalación. No es copia del tema 6 (no está
  cerrado).
- Aplicación práctica añadida: cálculo de bus de direcciones (2^16, 2^32), diagnóstico de lentitud por
  RAM o disco (oficio declarado) y caso de paso a Windows 11 (razonamiento de oficio sobre cifras de
  Microsoft).

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata sistemas de información,
arquitectura ni componentes.

## Copiado de RTVE sin cambios

Pasajes copiados literal, palabra por palabra, de temas marcados sin actualizar. Únicos cambios: se
quita la negrita (RTVE no citaba fuente) y la marca ✔ de las respuestas oficiales. El verificador sólo
comprueba que son literales (comprobado ya por script en esta fase: todos aparecen en el tema).

| Origen | Pasaje | Dónde va |
|---|---|---|
| RTVE TI 17 § 1 | Tabla «Bloque / Qué hace» (cuatro filas: unidad aritmético-lógica, unidad de control, memoria principal, entrada y salida) | § 2 «El modelo de von Neumann» |
| RTVE TI 17 § 1 | Párrafo «Y el rasgo que define ese modelo: los datos y el programa comparten memoria. La alternativa —memorias separadas para uno y otro— existe y se usa en microcontroladores, pero el ordenador de propósito general sigue el primero.» | ídem |
| RTVE TI 17 § 2 | Frase «La clasificación es de tres cajones y se decide por el sentido en que va la información:», tabla «Clase / Qué hace / Ejemplos» (tres filas, sin ✔), párrafos «La regla que la contesta sin dudar: …» y «Y el aviso que evita el error más común: …» | § 3 «Puertos, entrada y salida» |
| RTVE TI 17 § 3 | Tabla «Generación / Tecnología / Años, aproximados» (cinco filas, sin ✔) y párrafo «El atajo de memoria que ordena las cuatro primeras: …» | § 2 «Las generaciones de ordenadores» |
| RTVE GA 08 § 1 | Párrafo «Hardware es el conjunto de componentes físicos de un sistema informático. Se ordena en cinco funciones:» y tabla «Función / Qué hace / Ejemplos» (cinco filas) | § 2 «Hardware y software» |
| RTVE GA 08 § 1 | Párrafo «La distinción que más se pregunta es memoria frente a almacenamiento. … un equipo con poco disco no cabe.» | § 3 «La memoria» |
| RTVE GA 08 § 2 | Párrafo «Software es el conjunto de programas, procedimientos y documentación que hacen funcionar el hardware. Se clasifica en tres capas:», las tres viñetas y el párrafo «Por su licencia se distingue …» | § 2 «Hardware y software» |
| RTVE GA 08 § 5.1 | Las tres viñetas «Confidencialidad / Integridad / Disponibilidad» | § 1 «Características» (la frase que las introduce es nueva) |

Adaptado de RTVE (no literal; sí se verifica):

- RTVE TI 17 § 1, buses: «Los tres buses que unen los bloques: el de datos, el de direcciones y el de
  control. Con *n* líneas de direcciones se direccionan 2 elevado a *n* posiciones.» Se quitaron «, ya
  vistos en el tema 7 del específico de Técnica de Equipos» y «, que es la misma potencia de dos de las
  máscaras de red del tema 2». La tabla de qué lleva cada bus y el ejemplo de cálculo son nuevos.
- RTVE TI 17 § 3: «Las cinco generaciones, con la tecnología que las define:» (quitado «, que es la
  lista entera que hay que llevar»); «La quinta generación no tiene una definición pacífica: se
  enuncia por su objetivo y no por una tecnología concreta.» (reescrito; quitado «y por eso el examen
  se detiene en la cuarta»).

## Ficheros tocados

- Creados: el tema y este informe.
- Añadidas dos copias de fuente en `fuentes/canal-sur/informatico/web/`: `vonneumann-edvac-1945.txt` e
  `intel-moores-law.txt` (con cabecera URL y fecha de lectura). Descargas de trabajo (PDF del EDVAC,
  HTML) en el directorio temporal de la sesión, fuera del repositorio.
- Ningún otro fichero modificado.

## Preguntas de control (10, tipo test)

Repartidas por las cuatro rúbricas; teoría y aplicación práctica. Se contestan con el tema.

1. **Sistema de información · elementos.** De los cinco componentes de un sistema de información según
   Bourgeois, ¿cuáles son tecnología? a) hardware, software y personas; b) hardware, software y datos;
   c) software, datos y procesos; d) hardware, comunicaciones y procesos. → b. § 1 «Los cinco
   componentes». **Entera.**
2. **Sistema de información · funciones.** Según la definición de Laudon y Laudon, las funciones de un
   sistema de información son: a) recoger, procesar, almacenar y distribuir; b) diseñar, programar,
   probar e implantar; c) cifrar, firmar, sellar y archivar; d) capturar, comprimir, transmitir y
   borrar. → a. § 1 «Qué es un sistema de información» y «Funciones». **Entera.**
3. **Sistema de información · características.** El componente que se ha propuesto añadir a los cinco
   clásicos, porque aun siendo hardware y software es hoy un rasgo esencial, es: a) la nube; b) la
   comunicación en red; c) la seguridad; d) el usuario final. → b. § 1 «El sexto componente». **Entera.**
4. **Arquitectura.** El rasgo que define la arquitectura de von Neumann es: a) memorias separadas para
   datos e instrucciones; b) datos y programa en la misma memoria; c) varios procesadores en paralelo;
   d) ausencia de unidad de control. → b. § 2 «El modelo de von Neumann». **Entera** (también la
   alternativa de memorias separadas en microcontroladores).
5. **Arquitectura · aplicación práctica.** Un procesador con un bus de direcciones de 20 líneas puede
   direccionar: a) 20 posiciones; b) 400 posiciones; c) 1.048.576 posiciones; d) 2.097.152 posiciones.
   → c (2^20). § 2 «Los buses». **Entera** (fórmula 2 elevado a *n* y dos ejemplos resueltos).
6. **Arquitectura · generaciones.** Los circuitos integrados definen la: a) primera; b) segunda; c)
   tercera; d) cuarta generación. → c. § 2 «Las generaciones de ordenadores». **Entera.**
7. **Arquitectura · ley de Moore.** Según Intel, la ley de Moore establece que: a) la velocidad de
   reloj se duplica cada año; b) el número de transistores de un circuito integrado se duplica cada dos
   años; c) el número de circuitos integrados por chip se duplica cada dos años; d) el precio de la
   memoria se reduce a la mitad cada 18 meses. → b (en 1965 predijo cada año; en 1975 lo revisó a dos).
   § 2 «La ley de Moore». **Entera.**
8. **Componentes internos.** ¿Cuál de estas afirmaciones es correcta? a) la RAM conserva los datos al
   apagar el equipo; b) un SSD tiene platos giratorios; c) la RAM es volátil y el tipo de módulo DDR que
   admite un equipo depende de la placa base; d) NVMe es un tipo de memoria RAM. → c. § 3 «La memoria»
   y «El almacenamiento interno». **Entera.** (Variante de periféricos: la pantalla táctil es de entrada
   y salida, el monitor corriente de salida, § 3 «Puertos, entrada y salida». **Entera.**)
9. **Tecnologías del puesto · aplicación práctica.** Un equipo con procesador de 64 bits y dos núcleos a
   3 GHz, 8 GB de RAM, 120 GB libres y UEFI con arranque seguro, pero sin TPM 2.0, no puede instalar
   Windows 11 porque le falta: a) memoria; b) espacio en disco; c) el módulo TPM 2.0; d) un procesador
   de cuatro núcleos. → c. § 4 «El suelo del puesto» y «Aplicación práctica». **Entera.**
10. **Tecnologías del puesto.** Con la especificación USB PD 3.1, la potencia máxima que puede entregar
    un cable USB Type-C completo es: a) 60 W; b) 100 W; c) 140 W; d) 240 W. → d (antes, 100 W). § 4 «Un
    solo puerto para todo». **Entera.**

Resultado: 10 de 10 enteras; no hizo falta ampliar. Otras que el tema también contesta: fecha de fin
de soporte de Windows 10 (14-10-2025); umbral de NPU de los equipos Copilot+ (más de 40 TOPS); nombre
al público de USB 3.2 Gen 2 («USB 10Gbps»); velocidad de Thunderbolt 4 (40 Gbit/s) y 5 (80, hasta 120
con Bandwidth Boost); qué componentes deciden la velocidad del equipo y en qué unidad se miden; bit,
byte y tamaño de palabra; software libre frente a gratuito.
