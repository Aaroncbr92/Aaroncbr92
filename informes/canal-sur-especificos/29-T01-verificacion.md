# Puesto 29 · Tema 1 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/01-sistemas-de-informacion-y-arquitectura-de-ordenadores.md`.
Copia previa en el directorio temporal de la sesión (`29t01-antes-verif.md`).

## Fuentes y fecha de lectura

Releídas el 06-10-2026 sobre las copias de `fuentes/canal-sur/informatico/web/` (descargadas el
05-10-2026): `bourgeois-isbb-2019.txt` (portada, créditos, cap. 1, cap. 2 completo, cap. 3 en lo
citado), `vonneumann-edvac-1945.txt` (portada y § 2.1-2.9), `intel-moores-law.txt`,
`ms-win11-requirements.txt` (completa, «Last updated 2026-07-14»), `ms-win10-lifecycle.txt`,
`ms-copilot-pc-npu.txt` («Last updated 2025-11-17»), `usbif-data-performance-language-2024.txt` (y
metadatos del PDF: modificado 22-01-2024), `usbif-original-logo-2024.txt` (© 2000-2024),
`usbif-usb32-language.txt`, `usbif-usb4-language.txt`, `usbif-usb4.txt`, `usbif-charger-pd.txt`,
`usbif-typec.txt`, `intel-tb5-press.txt` (12-09-2023), `thunderbolt-tech.txt`, `nvme-about.txt`.

Nueva: ficha del ejemplar en Internet Archive (`archive.org/metadata/firstdraftofrepo00vonn`), leída
el 06-10-2026 y guardada en `fuentes/canal-sur/informatico/web/vonneumann-edvac-1945-ficha.txt`. El
OCR no deja leer «Moore School» en la portada; la ficha lo da como editor
(«Philadelphia : Moore School of Electrical Engineering, University of Pennsylvania»).

## Método

1. Literalidad: script que normaliza comillas, guiones, ™/® y saltos y busca cada negrita «…»
   (troceada por […]) en las fuentes: **116 fragmentos, 0 sin encontrar** (antes y después de
   corregir).
2. Prosa en redonda, tablas, glosas, fechas y Trazabilidad: releídas en su pasaje con los nueve
   errores delante.
3. Lentes (tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` 7.402 palabras, 31
   epígrafes.

## Copiado del común / de RTVE sin cambios

Nada del común. Los ocho pasajes «Copiado de RTVE sin cambios» se comprobaron sólo por literalidad
(script que compara el texto sin negritas ni ✔ con RTVE TI 17 y GA 08): todos aparecen tal cual
(la única diferencia, «Disco duro ✔,», es la marca quitada). No se re-verifican. Lo adaptado
(buses, frase de las cinco generaciones, la quinta generación) sí se verificó.

## Hallazgos y correcciones (12)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | Siglas: desarrollo de EDVAC (*Electronic Discrete Variable Automatic Computer*) | No está en el OCR ni en la ficha: quitado; queda «la calculadora EDVAC» |
| 2 | 9 | § 1: «El puesto de Operador/a Informático está precisamente en la primera línea […]: el soporte al usuario» | Funciones del puesto que no constan en documento publicado: frase quitada |
| 3 | 9 | § 2 bit: «La mayoría de los aparatos trabaja con dos valores» | Bourgeois: **«Many electronic devices»**: «Muchos aparatos» |
| 4 | 9 | § 2 von Neumann: «el rasgo que da nombre al modelo» | El informe no nombra así el modelo: «el rasgo que define el modelo» |
| 5 | 9 | § 2 buses (oficio): bus de direcciones «sólo sale de la CPU» | Absoluto sin fuente (otros dueños del bus, p. ej. acceso directo a memoria): quitado «sólo sale de la CPU» |
| 6 | 9 | § 2: «lo que dice Bourgeois de la primera CPU en un chip» | Bourgeois dice **«the first CPU was created in the early 1970s»**, y que las primeras CPU eran placas grandes; «en un chip» no es suyo: «la primera CPU, de comienzos de los setenta» |
| 7 | 9 | § 2: «el primer microordenador comercial que cita» | Fuente: **«the first microcomputer»**: quitado «comercial» |
| 8 | 9 | § 3: «(un teléfono, una tableta)» como ejemplos de la fuente | Bourgeois dice sólo **«Almost every digital device»**: quitados |
| 9 | 6 | § 4: Client Hyper-V sin su salvedad | Añadido literal **«This feature is available in Windows Pro editions and greater.»** |
| 10 | 6 | § 4 Windows 10: «ya está fuera de soporte» | La página da el fin del soporte ordinario; el programa de actualizaciones extendidas no se ha leído (ya en «Lo que este tema no da»): añadida la salvedad |
| 11 | 9 | § 4 tabla USB: «USB 2.0 y anteriores, Basic-Speed» | La guía de logos sólo dice **«Basic-Speed (12 Mbps or 1.5 Mbps)»**: queda «Basic-Speed» |
| 12 | 1 | Trazabilidad: tríada CIA «(con fuente en el tema 14)» | El tema 14 la da también sin cita: «desarrolladas, también sin cita, en el tema 14» |

Además, sin ser error: quitadas de las siglas HDD e IoT, que el tema no usa. Trazabilidad de von
Neumann: añadidos § 2.6 (C = CA + CC, que el tema afirma) y la ficha de Internet Archive.

## Confirmado sin cambios (muestra de lo comprobado)

Ediciones y años de Laudon (13.ª 2014, 12.ª 2012) y Valacich-Schneider (4.ª 2010); autores, edición
del 1-8-2019, Saylor y CC BY-NC 4.0 de Bourgeois; cap. 1-3 con sus títulos; partes CA, CC, M, I, O
en § 2.2, 2.3, 2.5, 2.7, 2.8 y fecha 30-6-1945; tabla de velocidad (GHz, MHz, MB/s, ms, Mbit/s);
DDR hasta DDR4; Bluetooth de corto alcance; requisitos de Windows 11 y Home con cuenta Microsoft;
PIN o llave para Windows Hello; Windows 10 14-10-2025, 22H2, LTSC; NPU 40 TOPS, Snapdragon X Elite
Arm, Ryzen AI 300, Core Ultra 200V; USB 3.2 Gen 2x2 = dos carriles de 10 Gbit/s; nombres al
público; PD 3.1 240 W; Thunderbolt 4/5; NVMe; aritmética 2^16, 2^20, 2^32, 255.

## Ficheros tocados

- Tema 1 (12 correcciones) y este informe.
- Añadido `fuentes/canal-sur/informatico/web/vonneumann-edvac-1945-ficha.txt` (cabecera URL y fecha).
- Ningún otro.
