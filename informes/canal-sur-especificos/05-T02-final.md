# Fase 5 bis · Ayudante de Realización (05) · Tema 2 · Guion, escaleta y documentación de realización

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/02-guion-escaleta-documentacion.md`.
Hecho el 30-09-2026 (reloj del sistema; el encargo fecha el trabajo el 24-09-2026). Revisados sólo
los cinco pasajes que lista `05-T02-remate.md`.

## Fuentes releídas (30-09-2026)

- INCUAL IMS077_3 (`fuentes/canal-sur/realizador/incual-IMS077_3.txt`, UC0217_3, CR1.5, ll. 301-303).
- RD 1680/2011 (`fuentes/canal-sur/realizador/BOE-A-2011-19599.txt`, módulo 0904, RA 2.a-2.c, ll. 543-545).
- SMPTE ST 2059-1:2021 (`fuentes/canal-sur/sonido/smpte/st2059-1/st2059-1-2021.txt`, 9.1, l. 1297; 9.3.3.2, ll. 1611-1630).
- Tema 14 del mismo puesto (sólo para comprobar la remisión al *drop frame*: ll. 321-324).

## Pasaje por pasaje

| N.º | Pasaje | Comprobación | Resultado |
|---|---|---|---|
| 1 | 2, «El guion de trabajo», pies de salida a vídeo y de vuelta | CR1.5 literal coincide con la negrita; no define los pies, así que el párrafo va, bien, como oficio. «esos dos pies» y «este segundo» tienen antecedente. Coherente con el epígrafe 4 (pie de salida = última frase o acción, oficio) | Correcto |
| 2 | 8, «El código de tiempo y la claqueta» | 9.3.3.2: a 24, 25 y 30 fps, *non-drop frame* «Per SMPTE ST 12-1»; HH = HH24 % 24; FF = resto tras segundos enteros. De ahí 00-24 a 25 fps, 23:59:59:24 como máximo y 00:05:10:25 imposible. Suma 00:00:10:20 + 10 fotogramas = 00:00:11:05 (20+10 = 30 = 1 s + 5): correcta. «lo fija así» tiene antecedente. **Hallazgo**: «a partir de la hora de red» no es lo que dice la fuente (9.1: «calculated from the PTP time») | Corregido: «a partir de la hora del protocolo de tiempo de precisión (*Precision Time Protocol*, PTP)»; sigla presentada, única aparición |
| 3 | 9, tabla de listados, fila «Hojas de desglose y listados generales» | RA 2.b y 2.c dicen «hojas de desglose»; 2.a, «listas coherentes»; ninguno «listados generales». El epígrafe 10 (l. 1204) los trata | Correcto |
| 4 | «Lo que este tema no da»: *drop frame* → tema 14 | El tema 14 lo desarrolla (DF/NDF, ll. 321-324) | Correcto |
| 5 | «Trazabilidad» | Fila ST 2059-1:2021, 9.3.3.2, con título del apartado y contenido exactos; fila «Oficio» ampliada con lo que el cuerpo dice como oficio | Correcto |

Sin negritas nuevas. Hallazgos: 1 (error 9, paráfrasis sin apoyo en la fuente), corregido.

## Ficheros tocados

- El tema 02 (una frase del epígrafe 8, «El código de tiempo y la claqueta») y este informe. Los
  demás cambios del árbol de trabajo no son míos.
