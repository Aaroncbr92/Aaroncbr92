# Verificación · Oficial Técnico Electricista (27) · Tema 9 · Climatización y frío industrial

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/09-climatizacion-y-frio-industrial-en-edificios-y-salas-tecnicas.md`
(15.679 palabras tras la verificación, 48 epígrafes). Fecha declarada: el encargo dice «hoy es
24-09-2026»; el reloj del sistema y los volcados del BOE dicen 05-10-2026. Todas las fuentes se
releyeron el **05-10-2026**.

Ficheros tocados: el tema y este informe. En el scratchpad, extractos de trabajo (IT 1, IT 3,
apéndice 1, IF-14, IF-17, arts. 20-28 del RSIF).

## Alcance

«Copiado del común»: nada. «Copiado de RTVE sin cambios»: nada (el redactor declara que todo lo de
RTVE está adaptado y cita normas). No había, por tanto, pasajes que comprobar sólo por literalidad:
se ha verificado el tema entero.

## Fuentes releídas (05-10-2026)

- RSIF, BOE-A-2019-15228 consolidado: arts. 1, 2, 4-9, 18, 20, 21, 22, 26, 27, 28 y 29 (con
  `boe.py precepto`); IF-14 entera (redacción vigente desde el 10-05-2025); IF-17 1.1, 1.5.1, 1.6,
  2.3, 2.4, 2.5 entera. Cadena de redacciones: sólo cambian, de lo citado, el art. 9 (01-07-2021) y la
  IF-14 (10-05-2025); la IF-02 (no reproducida) tiene redacción de 19-08-2026, como dice el tema.
- RITE, BOE-A-2007-15820: arts. 1, 2 y 26; IT 1.1.4.1 a 1.1.4.3.3; IT 1.2.4.3.2-3; IT 1.2.4.5.1-2;
  IT 3 entera; apéndice 1. Aviso de «reforma cruzada» en IT 3 (versión publicada el 02-08-2022 por el
  RDL 14/2022, sin fecha de vigencia): leída con la API, su texto es idéntico al vigente salvo una nota
  «Véase» que remite al art. 29 del RDL. Los 21 °C/26 °C del tema son los vigentes.
- RDL 14/2022, BOE-A-2022-12925: art. 29 y DF 17.ª (la vigencia «hasta el 1 de noviembre de 2023»
  rige para los apartados uno y cuatro del art. 29; el uno es el de 19/27 °C).
- Reglamento (UE) 2024/573 (texto DOUE): arts. 3, 4, 5, 6, 7, 8, 11, 13, 37; anexos I, IV (7, 8, 9)
  y VI.
- Guía IDAE: portada (autores, fecha), nota del «último borrador», familias 6, 9, 11, 12, leyenda.
- Tarjeta ASHRAE TC 9.9 (copia del redactor en el scratchpad).

Lentes: `negritas.py` (421 cotejadas; 4 no están: rótulos, «t CO2-eq» y la cita del RDL 14/2022,
leída aparte; 5 «atribuidas a otro artículo», falsos positivos: letras del art. 18 confundidas con
sus números y «bombas de calor» del art. 5.2 UE). `refutar_modo.py`: 0. `refutar_exactitud.py`: 82
«no literales», todos ruido (apartados de IF y artículos del reglamento europeo leídos como artículos
del RSIF/RITE); cada uno se cotejó a mano arriba. `refutar_prosa.py`: 1 (la «GF» ya justificada por
el redactor). `indice.py`: índice correcto.

## Correcciones aplicadas

| # | Error | Dónde | Qué había | Qué hay |
|---|---|---|---|---|
| 1 | 1 cita cruzada | 1.3 | «El RSIF clasifica… por la potencia eléctrica de los compresores (2.4)» | (2.3): los niveles están en 2.3; 2.4 es la sala de máquinas |
| 2 | 6 salvedad omitida | 2.3 | Art. 8 sin su último párrafo | Añadido literal: los sistemas indirectos con primario de equipos compactos, sea cual sea el refrigerante, se consideran de nivel 1 y se rigen por la IF-20 |
| 3 | 6 salvedad omitida | 1.1 | Art. 2 sin el apartado 5 | Añadido literal (IF-20 para sistemas indirectos cerrados con primario compacto y secundario sólo de agua, si no se manipula el circuito refrigerante) |
| 4 | 6 salvedad omitida | 3.1 | «un refrigerante L2 o L3 sube la instalación a nivel 2 aunque sea pequeña» | Añadidas las dos excepciones (art. 2.2 y art. 8, último párrafo) |
| 5 | 6 salvedad omitida | 2.3 | Comunicación del art. 21 | Añadido que la comunidad **podrá sustituir** la comunicación por declaración responsable |
| 6 | 6 salvedad omitida | 4.6 | Enfriamiento gratuito obligatorio > 70 kW sin más | Añadida la IT 1.2.4.5.1.5 (podrá justificarse el incumplimiento) |
| 7 | 6 salvedad omitida | 7.5 | Registro del art. 7 «durante al menos cinco años» | Añadido «salvo que se guarde en una base de datos de las autoridades» (7.2) |
| 8 | 9 sin fuente | Ficha, 5.4, «Lo que no da», Trazabilidad | ASHRAE «4.ª edición» y «existe una edición posterior» | La tarjeta sólo dice «2015 Thermal Guidelines»; se cita así y se dice que no se ha comprobado si hay revisión posterior |
| 9 | 9 sin fuente | Trazabilidad | Guía IDAE «documento reconocido del RITE publicado por el Ministerio» | Quitado: la guía no lo dice (sólo autores, IDAE, serie, ISBN, febrero 2007) |
| 10 | 9 sin fuente | 6.5 | «el titular con personal propio en las condiciones del RITE» | Comprobado y anclado: RITE art. 26.1 y 26.8 (empresas mantenedoras habilitadas o personal de plantilla con declaración responsable); art. 26 añadido a ficha, normativa y trazabilidad |
| 11 | prosa | 7.5 | «debe **alerte al operador…**» (agramatical) | «un sistema **que alerte…**» |
| 12 | 9 | 7.5 | «Es la aparamenta de SF6… centro de transformación propio» | Marcado como lectura de aplicación |
| 13 | ficha | Portada | RSIF sin art. 21; RITE sólo art. 2 | RSIF arts. 20 a 22; RITE arts. 1, 2 y 26; extensión 15.700 |

## Comprobado y conforme (sin cambios)

Todas las negritas en su precepto; las tablas de los arts. 2, 6, 7, 8, 18 (17 letras, a-q), 26, 27,
28.2, 29 del RSIF; IF-14 1.1-1.3, 2.1-2.6, 3.1-3.3 (once operaciones de 2.2, frecuencias de 1.2.6);
IF-17 1.1, 1.5.1, 1.6, 2.3.u, 2.4.c, 2.5.1-2.5.3.5; RITE: definiciones del apéndice 1, IDA/ODA/AE,
tablas 1.4.1.1, 1.4.2.1/3/4/5, 2.4.3.1, 2.4.3.2, tablas 3.1 y 3.3 de la IT 3, IT 3.4.2, 3.5.2,
3.6.2, IT 3.8 entera; UE: definiciones del art. 3, arts. 4.1, 4.5, 5.1-5.6, 6.1-6.4, 7.1, 8.1, 8.6,
11.1, 13.3-13.5 y 13.7, 37.1 y 37.5, PCG de los cinco HFC (anexo I), anexo IV 7.b/7.d/9.a/b/c/e con
sus fechas (incluida la corrección del redactor: 9.c es 2029), anexo VI (0,02 y 0); IDAE: familias,
compresores, tareas y frecuencias de las familias 6, 9 y 12, leyenda m/M/2.A/A, autores y fecha;
ASHRAE: 18-27 °C (A1-A4), 15-32 °C (A1), textos de «Recommended» y de la clase A1. Aritmética:
1,5 × 675 = 1,01; 8 × 675 = 5,4; 40 × 1.430 = 57,2 t CO2-eq; 60 × 0,55 = 33; 20 × 12,5 = 250.
Remisiones internas (2.1, 3.3, 4.4, 6.2-6.6, 7.1-7.5) apuntan a su epígrafe. Las lecturas y el oficio
están declarados como tales.

## Hallazgos que no se corrigen

- Art. 7.2 RSIF tiene una tercera regla (local de categoría genérica distinta: la más restrictiva)
  que el tema no recoge; no altera nada de lo afirmado.
- Anexo IV, punto 8 (autónomos y monobloque): el tema sólo da los puntos 7 y 9; es selección, no error.
- IT 1.1.4.1.2: la tabla asume velocidad de aire baja (< 0,1 m/s); omisión menor.
