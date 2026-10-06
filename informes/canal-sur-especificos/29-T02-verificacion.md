# Puesto 29 · Tema 2 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en las copias de
`fuentes/canal-sur/informatico/web/` (descargadas el 05-10-2026).

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/02-diagnostico-mantenimiento-y-reparacion-de-equipos-microinformaticos.md`.

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios»: nada (según `29-T02-redaccion.md`). Por
  tanto se verificó **todo** el tema.
- Tema técnico sin norma jurídica: lentes `refutar_prosa.py` (0 hallazgos) e `indice.py` (10.693
  palabras, 33 epígrafes). No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.
- Literalidad: script propio sobre las 189 negritas «…» contra las 26 fuentes normalizadas: 186 aparecen
  tal cual; las 3 restantes (smartctl, SMART y Pre-fail) sí son literales, pero la fuente es troff y
  lleva marcas `\fB…\fP` en mitad de la frase. Comprobado a mano (smartctl-man.txt, líneas 44-46 y
  1241-1262).
- Datos en redonda: se releyó cada uno en su fuente (AMI, HP, Lenovo, smartctl, chkdsk, sfc, códigos
  del Administrador de dispositivos, PnPUtil, TDR, ipconfig, ping, MemTest86 (2 páginas), UCM, SPEC
  2026/2017, Cinebench, 3DMark, PassMark, CrystalDiskMark, winsat). Se rehicieron los cálculos (`time`
  y MIPS/MFLOPS): cuadran.

## Correcciones aplicadas (error del catálogo entre paréntesis)

1. AMI: faltaba el alcance que declara el propio documento, **«covers AMIBIOS products released before
   May 2002»** (Core 8.00.04). Se añade: «tres límites» en lugar de dos (6, 3).
2. AMI: los puntos de control en pantalla no los activan todos los equipos («not all computers… enable
   this feature»): se añade la salvedad (6).
3. Lenovo, pila: «normally requires no charging or maintenance»; faltaba «normalmente» (6).
4. Lenovo, electricidad estática: «para descargar la bolsa y el cuerpo» → «reduce la electricidad
   estática» (9).
5. Lenovo: «Todas las sustituciones empiezan igual» → «Las sustituciones…» (3). Algunas, como la del
   disco de 2,5″ o la del procesador, remiten a otro procedimiento.
6. Lenovo, Wi-Fi: «pantalla metálica» no consta. Se añade la desconexión y reconexión de antenas, que
   sí figuran (9, 6). Se quita «si la red integrada falla, la pieza afectada es la placa base»: es una
   deducción sin fuente (9).
7. smartctl: `-a` da **«a large amount of»** información, no «toda» (9). `select`: se quita «útil cuando
   se sospecha de una zona» (sin fuente) y se pone lo que sí dice el manual: hasta cinco rangos (9).
8. MemTest86, martilleo: «antes de que se refresque» no consta; la fuente habla de fugas de carga en las
   filas vecinas (9). «Hace dos pasadas» → «puede hacer»: la segunda sólo se lanza si la primera da
   error (6). ECC: «recomienda» → «probablemente se pasaría» (4).
9. MemTest86, remedios: «subir tensiones» → «subir la tensión de la RAM», que es lo que dice la fuente (9).
10. Memoria, señal 3: «exigen descartar la memoria antes de culpar a otra pieza» no tiene fuente. Se
    sustituye por lo que dice PassMark de los errores intermitentes (9).
11. Código 10: el mensaje es el genérico; si existe *FailReasonString*, se muestra ese (6).
12. Código 28 tras la actualización: «porque» → «con frecuencia porque… quedó fuera de la migración» (6).
13. PnPUtil: `/drivers` existe desde Windows 10 versión 2004, no desde la 1903 (8).
14. UCM: «cuando la máquina aún no existe» → «no está disponible» (9).
15. «Pasa casi siempre por los controladores» → «pasa también» (9, generalización sin fuente).
16. Trazabilidad: se añade la fecha de la página de winsat (04-05-2023).

Releídos los pasajes cambiados: cada referencia tiene su antecedente; «tres límites» y su enumeración
cuadran.

## Confirmado sin cambios (muestra de lo que más riesgo tenía)

Puerto 80h; pitidos 1/3/6/7/8 y su remedio; códigos suprimidos en la revisión 1.8 (17-05-2006);
corrección del de 6 pitidos en la 1.9; pitidos del bloque de arranque; familias HP; reglas FRU/CRU;
SMART (24 h, 1-253, 1-254, 0-255, FAILING_NOW/In_the_past, duración de las pruebas corta y larga,
NVMe 7.4, cada cuatro horas); chkdsk (parámetros, inclusiones, códigos de salida 0-3, HDD/SSD, Visor de
eventos, fecha 26-05-2025); TDR de 2 s; ping (4 / 32 bytes / 4000 ms); SPEC CPU 2026 (52 pruebas)
y 2017 (43 pruebas, retirada el 03-11 y el 17-11-2026); pesos de los MFLOPS 1/4/8; ejemplo de `time`.

## Ficheros tocados

- Modificado: el tema (correcciones arriba).
- Creado: este informe.
- Copia previa en el scratchpad de la sesión (no en el repositorio).
