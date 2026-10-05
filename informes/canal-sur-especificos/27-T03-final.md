# Puesto 27 · Oficial Técnico Electricista · Tema 3 · Fase 5 bis

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/03-cuadros-electricos-aparamenta-y-protecciones.md`.
Alcance: sólo los pasajes que lista `27-T03-remate.md`, cotejados con el `diff` contra la copia previa
al remate (`27t03-antes-remate.md`, scratchpad). Copia previa a esta fase: `27t03-antes-5bis.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (el encargo fija «hoy» en 24-09-2026).

**Resultado: 3 correcciones menores aplicadas; 0 graves.** El remate es, en lo demás, fiel a sus
fuentes y cada remisión tiene su antecedente.

## Fuentes releídas (05-10-2026)

| Fuente | Pasajes cotejados |
|---|---|
| RD 842/2002 (`fuentes/canal-sur/BOE-A-2002-18099.md`, redacción única): ITC-BT-17, 1.2; ITC-BT-24, 3.2; ITC-BT-34, 1; ITC-BT-47, 5 | Tabla de códigos IP del REBT (1.4); cita de la ITC-BT-34, 1 (3.2), literal; cita entera de la ITC-BT-47, 5 (6.1), literal palabra por palabra |
| Schneider Electric, *Electrical Installation Guide* (wikitexto en `fuentes/canal-sur/tecnica/schneider-eig/` y figuras E66 y E67 en PNG, vistas como imagen) | E66-E70 (1.4); «Practical values…» (2.1); H28 y notas A y B (2.3); «Types of RCDs» y F52 (3.3); «Elementary switching devices», H5, H10 y fusibles (4 y 5.1); N83 (5.1); J18 y características del SPD (9.4) |
| INSST, guía de riesgo eléctrico (`.txt`, líneas 33-34) | «Edición: Madrid, septiembre 2020», sin ordinal: correcto en 7 y en Trazabilidad |

## Datos confirmados

- 1.4: estructura del código IP (0-6/X, 0-9/X, A-D, H/M/S/W), regla de la X, tabla de cada cifra,
  letra adicional, IK00 = 0 J, IK07 ≤ 2 J, IK10 ≤ 20 J (IEC 62262), recomendación IP 30 / IK07 para
  salas técnicas «salvo reglamentación del país». Códigos del REBT bien situados (IP 30 e IK07 en
  ITC-BT-17, 1.2; IP XXB, IP4X/IP XXD e IP2X en ITC-BT-24, 3.2).
- 2.1: las tres condiciones; tiempo convencional de 1 o 2 h; I2 < 1,45 In en automáticos; k2 1,6-1,9;
  k3 = k2/1,45; 1,31 (< 16 A) y 1,10 (≥ 16 A). Ejemplo: 27/1,10 = 24,5 A, cuadra.
- 2.3: B 3-5 In, C 5-10 In, D 10-20 In; nota de 50 In y Schneider 10-14 In; nota B (industriales);
  Ir = In en domésticos. Lectura C16 = 80-160 A, B16 = 48-80 A, D16 = 160-320 A, cuadra.
- 3.3: AC, F (10 mA de continua lisa superpuesta; no dispara con corrientes de choque), B (50 Hz a
  1 kHz), «muñecas rusas», usos típicos, origen de la continua lisa y fila 7 de la F52 (sólo B).
- 4: letras g/a y G/M; gG, aM, gM, gI; cartuchos domésticos hasta 100 A; aM con relé térmico como lo
  más usado; gM con dos valores y relé aparte; 1,25 In / 1,6 In en 1 h para 16 < In ≤ 63 A.
- 5.1: AC-1 a AC-4 con plugging e inching (notas A y B de N83); ejemplo 150 A AC-3 (1.200 A / 1.500 A,
  cos φ 0,35); discontactor limitado a 8 o 10 In.
- 9.4: tipos 1, 2, 3 con ondas 10/350, 8/20 y 1,2/50 + 8/20; usos; tipo 1 + 2; Uc, Up (bajo la
  tensión soportada de las cargas, coherente con ITC-BT-23, 3.2, citada antes), In 8/20 µs 19 veces,
  Iimp, Imax.
- Siglas nuevas presentadas todas en la entrada; Normativa, Lo que este tema no da y Trazabilidad
  coherentes con el cuerpo.

## Correcciones aplicadas (comprobadas en la fuente)

1. **1.4, fila IP 30** (error 9, matiz). Decía «ninguna protección especificada contra el agua»; la
   figura E67 da para la segunda cifra 0 «non-protected», que no es lo mismo que «no especificada»
   (eso es la X). Ahora: «sin protección contra el agua (segunda cifra 0)».
2. **2.3, cierre de la lectura para el examen** (error 9). «Es la razón de que la curva B se use en
   líneas largas, donde la corriente de defecto es baja»: no consta en ninguna página leída de la
   guía. Es deducción de oficio coherente con la tabla anterior; se marca «(oficio)».
3. **5.1, última frase** (error 9). Decía «Los interruptores y seccionadores tienen sus propias
   categorías de empleo, de la IEC 60947-3». La figura H5 de la guía da categorías sólo para
   interruptores («LV AC switches»), y del seccionador dice que «no rated values for these functions
   are given in standards». Ahora: «Los interruptores tienen sus propias categorías de empleo…».

## Antecedentes

Releídos todos los de la lista del remate y los de los pasajes corregidos: «Esa norma UNE» (2.1) →
UNE 20.460-4-43; «la misma guía» → Schneider citada en el mismo epígrafe; «Dos matices de la misma
tabla» → tabla de márgenes; «Esa norma» (3.3) → UNE-EN 62423; «ese apartado» (6.1) → ITC-BT-47, 5;
«el dato del epígrafe 2.1» (4) → I2 ≤ 1,45 Iz; «Lo que de esa norma explica» (9.4) → UNE-EN 61643-11,
nombrada justo antes; «El reparto en cascada del epígrafe 9.2» → existe en 9.2. Ninguno roto.

## Lentes

- `indice.py`: 17.032 palabras, 40 epígrafes (portada «Unas 17.000», válida).
- `refutar_prosa.py`: 0 hallazgos.

## Ficheros tocados

El tema y este informe. Nada más.
