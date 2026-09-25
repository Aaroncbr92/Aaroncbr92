# Puesto 08 · Tema 5 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/05-iluminacion-basica.md`.
Tema técnico sin norma jurídica: lentes `refutar_prosa.py` (3 avisos de siglas: PXW, PUB, URSA, códigos
de producto, sin cambio) e `indice.py` (índice sin cambios de rúbrica). Copiado del común: ninguno.

## Fuentes releídas (todas el 24-09-2026)

- Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 (copia local).
- Astera, ficha del Titan Tube e informe IEC 62471 n.º 2602T58190E-SF, 2026-05-29 (copias locales).
- UIT-R BT.709-6 (06/2015) y BT.2020-2 (10/2015), edición en español (copias locales).
- EBU Tech 3355, marzo 2017 (tech.ebu.ch, descargada).
- Blackmagic, *URSA Broadcast G2 Installation and Operation Manual*, noviembre 2021 (markertek, descargado).
- Canon XF605, especificaciones PUB. DIE-0559-000B (global.canon, descargado).
- Temas RTVE informacion-grafica/01 y 07, realizacion/08 (origen de lo copiado).

## Confirmado literal

Todas las citas de Sony (HVL-LBPC, Power/Rec Link, pre-lighting, 2000K-15000K, Tint −99/+99, pasos
de 20 K y «Values above [5600K]…», parpadeo, Flicker Reduce), Astera (lm, CRI/TLCI ≥96, RGBMintAmber,
Typical values, Exempt Group), UIT-R (D65 0,3127/0,3290; frecuencia de trama e iluminación), EBU
(valor 50, dos lecturas, salvedad, sin sentido absoluto), Blackmagic (25→50 fps, cebra, parpadeo) y
Canon (preajustes, 2.000-15.000 K, «approximate»). Cálculos rehechos: mired, −134 mired, ≈45 mired
>22.000 K, ley inversa del cuadrado, 16:1 = 4 pasos (f/8→f/2), 4:1 = 2 pasos.

## Correcciones

1. Error 9 (copiado de RTVE): tabla de temperaturas de color con cifras sin fuente (vela 1.800 K,
   doméstica 2.700 K, amanecer 3.000-4.000 K, cielo cubierto 6.500-7.500 K, sombra 8.000-10.000 K,
   HMI 5.600 K). Las dos fuentes RTVE no coinciden entre sí (cielo cubierto 6.500-7.500 frente a
   7.000-10.000) ni con tablas web. Sustituida por los preajustes publicados (Blackmagic 3.200/4.000/
   4.500/5.600/6.500 K, Canon, Sony log 5.500 K), con cita literal. Quitadas también de «La luz
   natural cambia» y de las etiquetas de la tabla de mired. Hueco declarado en «Lo que no da».
2. Error 9: «D65 = 6.500 K» sin fuente; ahora sostenido con la tabla «Daylight radiators» de la EBU
   Tech 3355 (6500 K → 0.312787, 0.329205).
3. Error 8/9: Sony «en modo estándar» → «modo de grabación personalizada (Custom)», como dice la guía.
4. Error 6: parpadeo de Blackmagic sacado del apartado de cadencias altas; añadida la salvedad de que
   las obturaciones sin parpadeo pueden no bastar; 1/50-1/100 pasa de «evita» a «suele evitar».
   Flicker Reduce viene de fábrica en 60 Hz. BT.2020-2: «entre otras consideraciones».
5. Error 9: «el regulador en LED no mueve el color» rebajado a «en principio; depende del aparato».
6. Error 5: IEC y EN presentadas en siglas.
7. Trazabilidad, oficio y extensión (7.600) ajustados.

## Otros ficheros tocados

Ninguno, salvo este informe.
