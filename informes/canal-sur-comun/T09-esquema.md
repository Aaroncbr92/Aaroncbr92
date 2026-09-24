# T09 · Esquema de repaso — Ley 31/1995

Fecha de trabajo: 24/09/2026.

Había un borrador a medias de un agente cortado en `esquemas/canal-sur-comun/09-ley-31-1995.md`
(191 líneas, 4.560 palabras: muy por encima de la horquilla del apartado 9 del manual). Lo he
revisado línea por línea contra `temas/canal-sur-comun/09-ley-31-1995.md` (no contra el esquema
de RTVE, que solo se usó como referencia de formato) y lo he recortado a 158 líneas y 2.395
palabras.

Qué se ha quitado: explicación y contexto (buena parte de la exposición de motivos, que no está
en el formato de referencia; frases de enlace; bullets que se podían fusionar sin perder datos).
Qué no se ha tocado: ningún precepto, cifra, plazo, umbral o fecha del tema. Se ha comprobado
cada dato recortado contra el tema antes de fusionar la frase que lo llevaba.

Verificación:
- `python3 herramientas/indice.py esquemas/canal-sur-comun/09-ley-31-1995.md` → índice generado,
  16 epígrafes.
- `python3 herramientas/refutar_prosa.py esquemas/canal-sur-comun/09-ley-31-1995.md` → 0
  hallazgos.
- `LC_ALL=C.UTF-8 wc -w` → 2.395 palabras (horquilla: unas 2.000). `wc -l` → 158 líneas (horquilla:
  unas 130). Algo por encima de la horquilla de referencia, pero ya no crece con el tamaño del
  tema (el tema tiene 20.190 palabras); no he forzado el recorte por debajo de la cifra a costa de
  quitar dato normativo.

Ficheros tocados: `esquemas/canal-sur-comun/09-ley-31-1995.md` (reescrito), este informe.
