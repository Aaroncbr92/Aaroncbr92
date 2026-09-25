# Puesto 08 · Tema 13 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`
(7.823 palabras con `wc`). No se corrige: sólo se informa. Leídos sólo `ENCARGO.md`, el enunciado
del puesto 08 y los informes de redacción y verificación del T13 (no `metodo/`).

Saltado por «Copiado del común» (informe de redacción): tabla de cinco vías y viñetas *Satélite* y
*Mochila* de «Enlaces · Las vías de la contribución», y el párrafo de los puntos 45-46 del
Contrato-programa.

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Qué se ha cotejado | Resultado |
|---|---|---|
| Libro de estilo CSTV (`libro-de-estilo-333233b.txt`), l. 112-136, 2614-2622, 2638-2643, 2680-2690, 3010-3014, 4036-4046, 4134-4142, 4176-4198 | Introducción, 4.4, 4.4.1, 4.4.4 paso 2, 5.6, 8.1 punto 6, 8.3, 8.3.2 | Todas las citas literales y bien atribuidas; ver M2 |
| Contrato-programa (BOJA 245/2023), l. 8-16, 1286-1292, 2040-2048, 2085-2103 | Título del Acuerdo, 3.5, 3.19, punto 103 | Punto 103 literal y completo; ver M3 |
| UIT-R SNG.770-2 (`.txt`), l. 120-236, 315-325 | Considerandos c), e), g); recomienda 8 y 9; anexo 1, 1.1 y 2.2.1 | Literales; glosas correctas |
| SMPTE ST 2110-10:2022 (l. 1-8, 146-172, 355-376, 400-416, 694-700), -20:2022 (l. 1-5, 136-140), -30:2025 (l. 1-5, 78-84); índice local ST 2110 | Introducción, 1, 6.3, 6.4, 7.2, 8.5; fechas y revisiones; títulos de partes | Literales; ver M1 |
| LiveU LU800 (`LiveU_LU800_ficha.txt`) | Las once citas | Literales |
| Manual ATEM es (l. 1458-1464, 2672-2678, 7643-7647) | N-1, piloto, CALL | Literales |
| SRT: `API-socket-options.md` y README (GitHub, curl), draft-sharabayko-srt-01 (ietf.org, curl) | 120 ms con asterisco (lo modifica `SRTO_TRANSTYPE`), [10..80], definición, «Informational», «Expires: 11 March 2022», UDP, ARQ, *listener/caller*, *rendezvous*, AES-128/192/256 | Conformes |
| NMOS y NDI (HTML descargado por el verificador en el scratchpad) | Definición NMOS, IS-04 e IS-07 | Conformes (no se re-descargó NDI) |

## Exactitud

Graves: 0.

Menores: 3.

| # | Error | Dónde | Qué pasa | Propuesta |
|---|---|---|---|---|
| M1 | 6 salvedad omitida | «Redundancia y límites de paquete», viñeta «Tamaño de paquete» | La cita de 6.3 («**The Standard UDP Size Limit shall be 1460 octets.**») es literal, pero la misma cláusula exceptúa a los emisores que operan conforme al **«optional Extended UDP Size Limit specified in section 6.4»**, que es de **«8960 octets»** (6.4). Tal como está, el lector infiere que 1460 es un tope absoluto (pregunta 12) | Añadir la salvedad y la cifra de 6.4, con su «may» |
| M2 | cita recortada sin marca | «Qué pide la casa», cita de 4.4 | La enumeración sigue en el original («…**contratación de bienes o servicios, edición y postproducción...**»); la cita se cierra en «otras televisiones» sin puntos suspensivos. No cambia el sentido | Cerrar con «…» o «[...]» |
| M3 | título incompleto | «El *streaming* en Canal Sur», rúbrica del apartado 3.19 | El título es **«Compromisos de cobertura por ondas hertzianas terrestres y de distribución de servicios nuevos»**; el tema da sólo la primera línea, y precisamente omite la parte que justifica que el punto 103 (Canal Sur Más) esté ahí | Completar el título |

Sin hallazgo, comprobado: aritmética (40/80/160 ms; 20 ms a 50 fps); «should»/«shall»/«may» de
7.2 y 8.5; cuatro áreas coordinadas (8.3); recuentos de partes ST 2110 (9 + OV + 3 RP; no existe
-50); siglas (sólo el aviso de IP en el título, no aplicable). `refutar_prosa.py`: 1 aviso (el
mismo). Lo declarado como oficio (tablas de caminos, vías, modos de *streaming*, canales,
procedimiento) va marcado como tal; la analogía PTP / generador de sincronismos (final de «El reloj
común») y «el retardo de una mochila no se compensa en el mezclador» son oficio no marcado en la
frase, aunque cubiertos por la lista final de Trazabilidad: no se cuentan.

## Cobertura del enunciado

Los cinco elementos (mochilas, enlaces, *streaming*, señales IP, coordinación con control) tienen
su `##` en el orden del enunciado y se desarrollan. Preguntas: 12 enteras, 1 a medias (M1), 2 no.

Lagunas: 2.

| # | Laguna | Por qué entra en el enunciado | Propuesta (con fuente, sin memoria) |
|---|---|---|---|
| L1 | Enlaces inalámbricos de cámara (transmisor de radiofrecuencia de la cámara a la UM o al control, modulación COFDM) | «Enlaces» en un temario de cámara: es el enlace que lleva el propio operador en deportes y retransmisiones. Ningún tema del puesto lo trata (búsqueda en los 17 temas: sólo inalámbricos de audio y de control de grúa) | Ampliar «Enlaces» con un `###`, apoyado en documentación de fabricante y, para la modulación, en la norma de TDT que define COFDM (ETSI EN 300 744) si se usa para describirla; declarar que el uso de frecuencias es materia de licencia |
| L2 | *Streaming* de distribución hacia plataformas y redes: protocolos de ingesta y entrega (RTMP, HLS) y lo que el cámara configura (URL de ingesta y clave) | «*Streaming*» del enunciado y el propio tema dice que lo grabado también acaba en «la plataforma propia y en redes»; hoy sólo declara el hueco | Ampliar «Dos usos del *streaming*» con los protocolos citados en su fuente primaria (p. ej., RFC 8216 para HLS, informativo; especificación publicada de RTMP) y su estatus |

## Ficheros tocados

Escritos: este informe y `08-T13-preguntas.md`. Descargas de SRT en el scratchpad (fuera del
repositorio). El tema no se ha modificado.
