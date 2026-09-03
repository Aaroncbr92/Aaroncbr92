# Esquema · Realización (Asistencia) 5: la tecnología en el ámbito de la realización

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

<!-- indice -->

## Índice

- [Luz y color](#luz-y-color)
- [Espacios de color](#espacios-de-color)
- [Luminancia](#luminancia)
- [Digitalización](#digitalización)
- [Rango dinámico y HDR](#rango-dinámico-y-hdr)
- [Resolución y aspecto](#resolución-y-aspecto)
- [Compresión](#compresión)
- [TDT](#tdt)
- [Aparatos de medida](#aparatos-de-medida)
- [3D](#3d)

<!-- /indice -->

## Luz y color

**A menor longitud de onda, mayor frecuencia y mayor energía** → azul y violeta, colores fríos.
Un objeto se ve verde porque **absorbe todo el espectro salvo el verde**.
**Cuanto más estrecho es el espectro, más saturado** es el color.
Tres magnitudes: **matiz · saturación · brillo**. El sistema que se ordena por las tres es **Munsell**.

## Espacios de color

Primarios sobre el diagrama CIE 1931. **BT.709** R (0,640; 0,330) G (0,300; 0,600) B (0,150; 0,060).
**BT.2020** R (0,708; 0,292) G (0,170; 0,797) B (0,131; 0,046). Blanco común **D65** (0,3127; 0,3290).
**De menor a mayor amplitud: Rec. 709 · DCI P3 · Rec. 2020 · AP0.** *El AP0 tiene primarios
imaginarios y contiene el visible entero.*

## Luminancia

| Norma | R | G | B |
|---|---|---|---|
| **BT.601** (SD) | 0,299 | **0,587** | 0,114 |
| **BT.709** (HD) | 0,2126 | **0,7152** | 0,0722 |
| **BT.2020** (UHD) | 0,2627 | **0,6780** | 0,0593 |

*El 59-30-11 de la respuesta oficial es el de la BT.601: no es universal.*

## Digitalización

**Muestreo → cuantificación → codificación**, en ese orden.
**4:2:2**: luminancia en cada píxel, C<sub>B</sub> y C<sub>R</sub> cada dos. *Son restas, no sumas.*
**1 bit = imagen monocromática.** **Rango legal de 8 bits: 16 a 235** (en 10 bits, 64 a 940).

## Rango dinámico y HDR

Más rango = **detalle en sombras y en altas luces a la vez**.
**PQ**: referenciado a la pantalla, **pico 10.000 cd/m²**, usa metadatos, no retrocompatible.
**HLG**: referenciado a la escena, retrocompatible, γ = 1,2 para pico nominal de 1.000 cd/m².

## Resolución y aspecto

**4K UHD = 3840 × 2160** (cuatro veces Full HD). DCI 4K = 4096 × 2160. 8K = 7680 × 4320.
**Aspecto = píxeles horizontales ÷ verticales.** **16:9 = 1,77:1**; 4:3 = 1,33:1.
**Letterboxing**: dos franjas negras **horizontales**. **Aliasing**: patrones de interferencia en
detalles finos; los *jaggies* son su manifestación.

## Compresión

**Entropía = información nueva o esencial.** Redundancia = repetida o predecible.
**Interframe** combina varios fotogramas; **intraframe**, cada uno solo.
**MPEG-2 no vale para 4K.** **HEVC (H.265)** es el códec de la emisión UHD en España y llega a 8K.

## TDT

**Ondas hertzianas terrestres, sin cable ni satélite, antenas UHF.**
**OFDM** reparte en portadoras; **QAM** modula cada una en amplitud y fase.
DVB-T (EN 300 744): QPSK, 16-QAM, 64-QAM. DVB-T2 (EN 302 755) añade **256-QAM**.

## Aparatos de medida

**Monitor de forma de onda** → luminancia y nivel de vídeo. **Vectorscopio** → **pureza de los
colores**, en polares. **Osciloscopio digital** → formas de onda y sincronismos. **Rasterizador** →
varias representaciones a la vez, para HD.
*Con señal monocroma el vectorscopio pinta un punto en el centro: no hay vector que comprobar.*

## 3D

**Autoestereoscopia**: sin gafas, por **filtros en la pantalla** —barrera de paralaje o red
lenticular— que entrelazan verticalmente. Con gafas: anaglifo, polarización, obturación LCD.
