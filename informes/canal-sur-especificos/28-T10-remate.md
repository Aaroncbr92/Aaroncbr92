# Puesto 28 · Operador/a de Sonido · Tema 10 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/10-sonorizacion.md`. Fecha de trabajo y
de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Parte de
`28-T10-refutacion.md` y `28-T10-preguntas.md`.

**Resultado: sí se amplió contenido nuevo** (laguna L1, modos puente/paralelo). Procede la fase 5 bis
sobre los pasajes 4 y 1-3 de abajo.

## Fuentes releídas antes de aplicar

| Fuente | Qué | Resultado |
|---|---|---|
| TI AN-1497 (`fuentes/canal-sur/sonido/fabricantes/ti-snaa034a.txt`), líneas 86-98 y 147-150 | «linear classes»; «90% efficient amplifier at 1W output dissipates 100mW»; «DC resistance, typically 4Ωor 8Ω» | los tres hallazgos del informe, confirmados |
| Crown FAQ (copia de texto de la verificación, 25-09-2026, scratchpad `crown.txt`; la web da 403 hoy) | «Should I use Bridge Mono or Parallel Mono?» | literal completo leído; confirma L1 |
| Shure/Frank AL1174 (`shure-pag.txt`), línea 303 | «arc far apart» | errata de escaneo confirmada |

## Pasajes cambiados

1. **Hallazgo 1 · «Impedancia del altavoz»**: «(TI da como típicos de los altavoces 4 u 8 ohmios)» →
   «(TI da como típica de los altavoces una resistencia en continua de 4 u 8 ohmios)».
2. **Hallazgo 2 · «La etapa de potencia y sus clases»**: «Sus clases lineales (A, B, AB y C) se
   definen» → «Las clases A, B, AB y C se definen». El antecedente de «la D» sigue delante.
3. **Hallazgo 3 · mismo epígrafe**: tras el ejemplo de TI se añade «La cifra es redondeada: por
   cálculo, para entregar 1 W al 90 % entran unos 1,11 W y se disipan unos 111 mW.» (1/0,9 = 1,111;
   1,111 − 1 = 0,111 W.)
4. **L1 (ampliación) · «Los modos de funcionamiento»**, nuevo párrafo tras la tabla: cuándo conviene
   cada modo, con las citas literales de Crown «Generally, the deciding factor to this dilemma is the
   total speaker load impedance you wish to drive.», «the most power available when driving 8 or
   4-ohm loads», «Parallel Mono can be used when driving lower impedance loads» y «the power is
   distributed equally to all three speakers»; en redonda, los mínimos por gama (puente: Micro-Tech y
   Macro-Tech a 8 o 4 ohmios, Power-Tech y Com-Tech a 8 o más; paralelo: 1 ohmio en Micro/Macro-Tech,
   2 en Power/Com-Tech) y la ventaja con un número impar de cajas (tres). Todo leído en la FAQ. La
   frase «No todos los modelos admiten los dos modos…» queda detrás.
5. **Observación 4 · «Cobertura»**: «if they are far apart» → «if they arc [sic: are] far apart»,
   para ser literal y coherente con las otras erratas señaladas.
6. **Trazabilidad**: fila de Crown amplía el uso (cómo se conecta cada modo y cuándo conviene); fila
   de TI añade la resistencia en continua típica; fila de Shure añade la errata «arc».
7. **Ficha**: Extensión 7.750 → 8.000 palabras (el recuento pasa de 7.763 a 7.991).

Releídos los pasajes: «cada uno», «su mayor ventaja», «las tres» tienen su antecedente inmediato.

## No aplicado

- Observaciones 5 y 6: resumen correcto y aviso ya hecho; sin cambio.
- Pregunta 15 (Linkwitz-Riley): sigue como hueco declarado; no hay fuente leída que lo dé. No se
  recorta la pregunta.
- Tema 2, línea 199 («la C, la más alta de las lineales»): fuera de mi tema, sin tocar; se avisa.

## Lentes

Tema técnico sin norma. `indice.py`: 7.991 palabras, 45 epígrafes (sin cambio de epígrafes; el tema
no está en el `.tsv` de portadas, así que la ficha se ajustó a mano). `refutar_prosa.py`: 2 avisos,
ambos falsos positivos (AB es nombre de clase, no sigla; «NOW» es la errata ya señalada).

## Otros ficheros tocados

Sólo el tema y este informe (copia previa del tema en el scratchpad, `t10-antes.md`).
