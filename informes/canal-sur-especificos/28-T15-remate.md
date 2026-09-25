# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.
Fecha de trabajo y de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).

Fuentes releídas el 25-09-2026 para cada corrección:
- Audinate, *Dante Controller User Guide* 4.18.x, v1.0, publicada el 6-V-2026 (`dc-latest.txt`):
  «About Transmit Flows» (p. 132), «About Clock Domains» (p. 58), «Sample Rate» pull-up/down
  (pp. 85-86), mensajes de suscripción («Mismatched clock domains»).
- SMPTE ST 2110-30:2025, cl. 7 y tablas 2 y 3.

## Correcciones y lagunas: todas confirmadas en la fuente y aplicadas

| Nº | Hallazgo | Comprobación | Aplicado |
|---|---|---|---|
| 1 (grave) | Multicast «sin cifra» | Cita literal en DC 4.18 p. 132 | Sí |
| 2 (menor) | Salvedad cl. 7 (más canales) | Literal en cl. 7 | Sí |
| L1 | Niveles de receptores | Cl. 7 y tabla 3, cifra a cifra | Sí (ampliación) |
| L2 | = hallazgo 1 | — | Sí |
| L3 | Dominios de reloj por pull-up/down | DC 4.18 p. 58 y pp. 85-86 | Sí (ampliación) |

Ninguna corrección del informe estaba equivocada.

## Pasajes cambiados

1. **Qué se puede preguntar** (párrafo): «cuántos canales lleva un flujo unicast y uno multicast y en
   qué se diferencian»; «qué es el nivel A, cuántos canales admite cada nivel y qué combinaciones debe
   admitir un receptor».
2. **SMPTE ST 2110-30**, párrafo tras la tabla 2: se quita «Manda la norma: 1 a 4 canales en AX y 9 a
   32 en CX» y se sustituye por «No es una contradicción…» con la cita de la cl. 7 («Senders and
   receivers may support more channels…») y la regla de conformidad de emisores («shall», «at least
   one channel count»).
3. **SMPTE ST 2110-30**, nuevo bloque: regla de receptores (cita cl. 7), tabla 3 completa (A, AX, B,
   BX, C, CX con todas sus combinaciones) y «Aplicación práctica» (receptor C admite emisor A y C).
4. **Unicast y multicast**, tabla, celda «Canales por flujo / Multicast»: «La guía no da una cifra» →
   cita «Multicast flows can be configured with up to 64 channels (depending on the Dante device type).»
5. **Unicast y multicast**, tras el aviso de inundación: cita sobre saturación de enlaces de 100 Mbps y
   uso del multicast sólo con motivo.
6. **Las cuentas de ancho de banda**, segundo ejemplo: citas «support up to 4 channels of audio
   simultaneously» y «If you were to then subscribe a fifth audio channel, a second flow would have to
   be created.»
7. **Sincronía entre flujos y con la imagen**, nuevo párrafo: pull-up/down (ejemplo 24→25 fps,
   +4.1667 %), dominios de reloj separados, imposibilidad de intercambiar audio entre dominios (ejemplo
   +4,1667 % y −1 %), hasta cinco dominios con su propio leader, aviso «Mismatched clock domains».
8. **Sincronía entre flujos…**, «Aplicación práctica»: una frase sobre equipos que no se oyen por
   pull-up/down distinto.
9. **Portada**, Extensión: 8.400 → 8.700 palabras.
10. **Trazabilidad**, filas de Audinate y de ST 2110-30: añadidos los datos nuevos.

Relectura de antecedentes: «Ese ajuste» (7) remite al pull-up/down de la frase anterior; «la propia
norma» (2) a la ST 2110-30 del epígrafe; «su propia tabla (tabla 3)» (3) a la norma. Sin remisiones
huérfanas. Ningún pasaje es «Copiado de RTVE sin cambios».

## Lentes

- `indice.py`: sin errores (no hay epígrafes nuevos; el índice no cambia).
- `refutar_prosa.py`: 3 avisos ya existentes antes del remate (IP y PTP en el título, antes de la lista
  de siglas; TRUE dentro de una cita de norma). No se tocan.
- Sin norma legal: no se pasan `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Resultado

**Amplió contenido nuevo** (tabla 3 de receptores y dominios de reloj): procede la fase 5 bis sobre
los pasajes 2, 3, 5, 6 y 7. Preguntas 5, 6 y 12 pasan a contestarse enteras con el tema.

## Ficheros tocados

El tema 15 y este informe. Nada más.
