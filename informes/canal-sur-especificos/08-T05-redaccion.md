# Puesto 08 · Tema 5 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/05-iluminacion-basica.md`
(≈7.300 palabras; 6 epígrafes `##` de cuerpo —introducción, temperatura de color, contraste, sombras,
luz natural, luz artificial, en el orden del enunciado— + recomendaciones citadas, huecos,
trazabilidad; 27 `###`). Índice regenerado con `indice.py`; `refutar_prosa.py`: 2 avisos de «siglas»
(PXW, PUB), que son códigos de producto de fabricante, no siglas: sin cambio. Sin normas jurídicas:
no proceden las lentes automáticas de norma.

Nota de proceso: al empezar esta fase el tema ya estaba escrito y guardado por epígrafes en el
commit 310dc00 (misma fecha), sin informe de redacción. Lo he releído entero contra el enunciado, el
material de investigación y los tres temas de RTVE; sólo he añadido una frase (luz de día más rica en
azules que el tungsteno, en «Qué es») para cubrir la pregunta 1 de abajo.

## Fuentes

- `08-investigacion-A-imagen.md` § Tema 5 y § 9.4-9.5: EBU Tech 3355 (valor 50, dos lecturas,
  salvedad sobre Ra/Qa), Blackmagic URSA Broadcast G2 (parpadeo, obturación, cebra, 25→50 fps),
  UIT-R BT.2020-2 (frecuencia de trama e iluminación), Canon XF605 (preajustes, 2.000-15.000 K).
- Citas del tema que no están en la investigación A y hay que verificar en su fuente: Sony
  *PXW-Z200/HXR-NX800 Help Guide* (HVL-LBPC, Power/Rec Link, preajustes →3200K…→6300K, Tint −99 a
  +99, pasos por encima de 5.600 K, Flicker Reduce), ficha del Astera Titan Tube (lm, CRI/TLCI ≥96,
  RGBMintAmber) e informe IEC 62471 (Exempt Group, 29-05-2026), coordenadas D65 de BT.709-6/BT.2020-2.

## Copiado del común

- Ninguno. El enunciado no pide ninguna norma que desarrolle `temas/canal-sur-comun/`.

## Copiado de RTVE (a verificar; oficio y cálculo, sin precepto que releer)

Literal en lo sustancial, quitado lo propio de RTVE (respuestas oficiales, «datos que el examen ha
preguntado», avisos de reparto, negritas de énfasis):
- `informacion-grafica/07`: equipo ligero, ceferino, mired y sus dos cuentas, CTO/CTB, interior con
  ventana, relación de contraste y pasos (ejemplo 16:1 desde f/8), fantasma de Pepper.
- `informacion-grafica/01`: magnitudes fotométricas, temperatura de color, ley inversa del cuadrado.
- `realizacion/08`: qué decide la luz, dos cifras de luz día (5.500/D65), geles, tres puntos,
  contraste y relleno, dura/suave, aparatos (Fresnel), accesorios (bandera, velo, rejilla),
  interiores y exteriores. Se dejó fuera la luz negra/ultravioleta (no la pide el enunciado).

## Otros ficheros tocados

Sólo el tema 5 (una frase y el índice) y este informe.

## Preguntas tipo test de comprobación (contestadas sólo con el tema)

1. La luz de día, frente a la de tungsteno, tiene: a) más rojos; b) más riqueza en azules; c) la
   misma composición; d) más verdes. → b. «Qué es». **Entera** (tras añadir la frase).
2. ¿Qué valor en mired corresponde a la temperatura de color más alta? a) 370; b) 312; c) 250;
   d) 166. → d. «El mired» (escala inversa). **Entera.**
3. Un filtro CTB: a) baja la temperatura de color; b) sube la temperatura de color; c) quita verde;
   d) sólo quita luz. → b. «Los filtros de conversión». **Entera.**
4. La referencia de «luz día» para iluminar es: a) 3.200 K; b) 4.300 K; c) 5.500-5.600 K;
   d) 6.500 K. → c; D65 es el blanco de la señal (x = 0,3127, y = 0,3290). «La luz de día y el
   blanco D65». **Entera.**
5. El rostro mide f/8; para un fondo a 16:1, el fondo debe medir: a) f/16; b) f/2,8; c) f/2;
   d) f/4. → c. «Medir el contraste en pasos». **Entera.**
6. Para disminuir el contraste de iluminación se: a) sube la principal; b) sube el relleno;
   c) pone una bandera en el lado de sombra; d) sube el contraluz. → b. «Bajar o subir el
   contraste». **Entera.**
7. La dureza de una sombra depende sobre todo de: a) la potencia; b) la temperatura de color; c) el
   tamaño aparente de la fuente vista desde el sujeto; d) el tipo de lámpara. → c. «Luz dura y luz
   suave». **Entera.**
8. Un bastidor de alambre cubierto de tela negra es: a) un velo; b) una rejilla; c) una bandera;
   d) un pulmón. → c. «Los accesorios que controlan la sombra». **Entera.**
9. Interior con ventana: para igualar la intensidad de los focos con la de la ventana se pone:
   a) CTB en los focos; b) CTO en los focos; c) densidad neutra en la ventana; d) CTB en la ventana.
   → c. «Interior con ventana». **Entera.**
10. Si una luz se aleja al doble de distancia, para mantener la iluminancia hay que: a) duplicar la
    intensidad; b) cuadruplicar; c) no cambia nada; d) reducirla a la mitad. → b. «La ley inversa del
    cuadrado». **Entera.**

Otras cubiertas en la relectura (sin numerar): índice que mide la fidelidad de color para cámara
(TLCI, EBU Tech 3355, 50 como frontera); parpadeo con LED y obturación a 1/50 o 1/100 en red de
50 Hz, *Flicker Reduce*; bajar el regulador en tungsteno baja la temperatura de color; posición del
sol como contraluz con rebotador en exterior; luz principal «frontal y cruzada».

Resultado: 10 de 10 enteras.
