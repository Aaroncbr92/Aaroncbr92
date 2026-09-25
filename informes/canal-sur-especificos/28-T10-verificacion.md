# Puesto 28 · Operador/a de Sonido · Tema 10 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/10-sonorizacion.md`. Fecha de trabajo y de
lectura de todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).

## Copiado de RTVE sin cambios: sólo literalidad

Script (párrafo, fila o elemento de lista, sin `**` ni ✔, espacios normalizados, ¿subcadena del RTVE
10 + RTVE 04?), pasado antes y después de corregir: los nueve bloques listados en la redacción son
literales (tablas de piezas, cajas, sensibilidad, cruce, sala y decisiones; los tres puntos de la
directividad; los párrafos de la sensibilidad, del cruce, de la cuenta 38 − 4 y del atajo; puntos 1,
3, 4 y 5 de las cinco maneras). No se re-verificó su contenido. «Copiado del común»: ninguno.

Nota al coordinador: el bloque literal «Y la parte que la pregunta mide de verdad…» conserva «la
pregunta», de sabor RTVE (examen). Se lee como genérico tras «El caso tipo»; no se toca por ser
literal listado.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| Shure/Frank, AL1174 (`shure-pag.txt`) | todas las citas por script + cifras a mano (NAG 70/49/21; PAG 20, 22, 16, 24; NOM; erratas «NOW» y «11 dB») | todo confirmado |
| Ureda, JAES 52(5), 2004 (`line-array-theory.txt`) | citas por script (dos con guion de corte de línea, literales) + ejemplo 4 m/8 kHz/100 m | confirmado; atribución de la cita de 1963 corregida |
| Crown FAQ, https://www.crownaudio.com/en-US/faq_categories/1, descargada hoy | las diez citas (incluido el paralelo mono, que la redacción avisaba reconstruido) | todas literales; «No todos los modelos admiten los dos modos» confirmado (CE, CP660, D y K no hacen paralelo mono) |
| TI AN-1497, SNAA034A (`ti-snaa034a.txt`) | citas + contexto | citas literales; paráfrasis del filtro corregida |
| Shure, guía de antenas (`shure-antenna.txt`) | citas + contexto | literales; contexto de los 3 dB corregido |
| RTVE 10 y 04 (pasajes adaptados) | cotejo | fieles; RTVE los declara oficio |
| Temas 1, 2, 3 y 5 del puesto (remisiones) | grep | una remisión falsa (tema 1) corregida |

Cálculos rehechos: 340/5 = 68 Hz; 340/2000 = 0,17 m; 97 + 10 log 400 = 123; 20 log 32 = 30,1 → 93;
×4 = +6 dB; 25 ft = 7,62 m; 10 log 10 = 10; 24 − 3 = 21. Todos bien.

## Correcciones aplicadas (error del catálogo)

1. **9 · Impedancias** «4, 8 o 16 ohmios, las habituales» sin fuente → «TI da como típicos de los
   altavoces 4 u 8 ohmios» (TI: 4/8 Ω altavoces, 16/32 Ω auriculares).
2. **3/9 · «la suma de las cargas colgadas de un canal»**: en paralelo la impedancia no se suma, baja
   → «la impedancia resultante…», con apoyo de Crown (mínimos por modelo y modo).
3. **9 · Clases**: «Sus clases (A, B, AB, C y D) se definen por qué parte del ciclo conduce» → la D
   no se define por ángulo de conducción sino por conmutar (así lo dice también el tema 2).
4. **6/9 · TI, PWM «que un filtro devuelve a audio»**: la nota es precisamente sobre amplificadores
   *sin* filtro; se dice filtro paso bajo de salida o, en los filterless, el propio altavoz como paso
   bajo (TI, líneas 139-156).
5. **6 · Crown 1,4 V = +4 dBu**: se mantiene la cita y se añade la salvedad de cálculo (+4 dBu ≈
   1,23 V; 1,4 V ≈ +5,1 dBu). **Aviso**: el tema 2 del puesto cita lo mismo sin salvedad; no lo he
   tocado (fuera de mi tema).
6. **9 · «impedancia muy baja»** → «baja» (Crown: «Low output impedance»).
7. **1 · Cita de 1963**: es de Klepper y Steele, citada por Ureda → nombrados (texto y Trazabilidad).
8. **9 · Campo lejano «como una fuente puntual»** (inferencia sin frase de Ureda) → «la misma caída
   que da la ley del cuadrado inverso», que el tema sí sostiene con Shure.
9. **6 · 3 dB del combinador pasivo «que Shure da en general»**: en la fuente va en antenas de varias
   salas; para IEM Shure sólo pide contar las pérdidas del pasivo → corregido; salvedad también en
   Trazabilidad.
10. **9 · Mezclador automático «abre sólo cuando detecta voz por encima del fondo»**: Shure describe
    umbral en la mayoría y comparación con el fondo en los más nuevos → corregido.
11. **9 · «Shure respalda los dos primeros puntos»**: Shure respalda acercar el micrófono, alejar el
    altavoz y los componentes direccionales (límite de 6 dB); no «apuntar a los nulos» → corregido.
12. **Propio de RTVE** · Linkwitz-Riley «el nombre que se pregunta» (pregunta 38 del examen RTVE) →
    «que conviene conocer».
13. **9 · Omnis acoplan «en graves»**: DPA (tema 3) dice «lower mid-range or bass» → «medios graves
    o graves».
14. **6 · «el público es el mayor absorbente»**: la fuente (RTVE 04 y tema 1) dice «de un teatro» →
    salvedad repuesta.
15. **1 · Remisión falsa** en «Lo que este tema no da»: velocidad exacta y efecto de precedencia
    remitidos al tema 1, que declara no darlos → «sin fuente leída».
16. **9 · Oficio no declarado en Trazabilidad**: lo heredado de RTVE (que RTVE declara oficio) no
    constaba → fila «Oficio, sin fuente publicada leída».

Extensión de la ficha actualizada a 7.750 palabras (`indice.py`: 7.763). Pasajes cambiados releídos:
cada «la nota» (de TI), «esas pérdidas», «la segunda equivalencia» tiene antecedente delante.

## Avisos de la redacción, resueltos

Crown sin volcado → cotejado en la web hoy, literal. 1,4 V/+4 dBu → salvedad (5). Ureda «como fuente
puntual» → (8). 3 dB del pasivo → (9). «4, 8 o 16 ohmios» → (1). Lazo «llega a uno» → confirmado en
el tema 5 del puesto (oficio de ese tema).

## Lentes

Tema técnico sin norma: `refutar_prosa.py` → 1 hallazgo («NOW», errata literal explicada; se deja);
`indice.py` → sin cambios de epígrafes. `negritas.py`/`refutar_*` de normas no aplican.

## Otros ficheros tocados

Ninguno fuera del tema y este informe. Descarga temporal de la FAQ de Crown en el scratchpad (no en el
repositorio).
