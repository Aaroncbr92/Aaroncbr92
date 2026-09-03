# TESE · Tema 8 · La señal audiovisual: SDI, AES y sincronismos

10 preguntas reales sacadas de los cuadernillos de octubre y noviembre de 2024.
La respuesta es la de la plantilla oficial; donde pone «sin plantilla» es que
no se pudo emparejar.

---

**70_preguntas_tese_a · nº 42 · respuesta: c**

```
42. En  el  interface  SDI  a  10  bits  según  la  norma  SMPTE  259M,  en  los  patrones  de 
referencia temporal EAV y SAV, una de sus cuatro palabras de 10 bits (XYZ) está 
formada por los bits 1FVHP3P2P1P000. ¿Qué función tienen los bits P3P2P1P0?: 
a)   Son bits de paridad de las muestras de la LAD asociada. 
b)   Dan información de la posición de la muestra dentro del frame de video. 
c)   Son bits de protección de errores de los bits FVH. 
d)   Indican el tipo de datos auxiliares insertados en el periodo de borrado.
```

---

**70_preguntas_tese_a · nº 45 · respuesta: d**

```
45. El protocolo PTP, definido por el estándar IEEE 1588, se utiliza para: 
a)   Envío de paquetes. 
b)   Direccionamiento de paquetes. 
c)   Comprimir paquetes. 
d)   Sincronismo de relojes.
```

---

**70_preguntas_tese_a · nº 67 · respuesta: b**

```
67. En el interface HDSDI, ¿Dónde se informa del número de línea dentro del frame de 
video (tanto para Y como para C)? 
a)   A continuación del patrón de sincronización SAV, al inicio de la línea activa, mediante 
dos palabras de 10 bits (LN0 y LN1) que combinadas forman un contador binario de 11 
bits. 
b)   A continuación del patrón de sincronización EAV mediante dos palabras de 10 bits (LN0 
y LN1) que combinadas forman un contador binario de 11 bits. 
c)   Al final de la LAD, mediante dos palabras de 10 bits (LN0 y LN1) que combinadas forman 
un contador binario de 11 bits, anteriores al patrón de sincronización EAV. 
d)   La información se extrae de los bits FVH de cada patrón de sincronización.
```

---

**70_preguntas_tese_a · nº 71 · respuesta: b**

```
71. ¿Qué bit rate tiene una señal de audio AES3 a 48 KHz? 
a)   2,822 Mbps. 
b)   3,072 Mbps. 
c)   5,644 Mbps. 
d)   6,144 Mbps.
```

---

**70_preguntas_tese_a · nº 81 · respuesta: b**

```
81. ¿Qué estándar define el protocolo comúnmente conocido como MADI? 
a)   AES-3. 
b)   AES-10. 
c)   AES-11. 
d)   AES-12.
```

---

**70_preguntas_tese_a · nº 84 · respuesta: b**

```
84. El  interface  SDI  a  10  bits  según  la  norma  SMPTE  259M  (SD),  los  patrones  de 
referencia temporal denominados EAV y SAV están formados por cuatro palabras 
de 10 bits cuyo orden es: 
a)   000 - 3FF - 3FF - XYZ   //   (XYZ = 1FVHP3P2P1P000). 
b)   3FF - 000 - 000 - XYZ  //   (XYZ = 1FVHP3P2P1P000). 
c)   XYZ - 000 - 3FF - 3FF    //   (XYZ = 1FVHP3P2P1P000). 
d)   XYZ - 3FF - 000 - 000    //   (XYZ = 1FVHP3P2P1P000).
```

---

**70_preguntas_tese_a · nº 91 · respuesta: c**

```
91. El protocolo MADI hasta cuantos canales puede transportar en un solo cable: 
a)   16. 
b)   32. 
c)   64. 
d)   128.
```

---

**70_preguntas_tese_a · nº 92 · respuesta: a**

```
92. ¿Qué es el Protocolo NTP? 
a)   Es un protocolo de internet para sincronizar los relojes de los sistemas informáticos. 
b)   Es  un  protocolo  de  internet  para  monitorizar  un  grupo  de  paquetes  en  un  sistema 
informático. 
c)   Es un protocolo temporal para sincronizar audio en un sistema informático. 
d)   Es un protocolo temporal para comprobar la latencia de un sistema informático.
```

---

**71_preguntas_tese_b · nº 8 · respuesta: a**

```
8.- ¿Cuál es el bitrate de una señal AES-10 que transporta señal de audio muestreada a
48000 muestras por segundo?.
a) 125 Mbps
b) Depende de la profundidad de muestra
c) Depende del número de canales que transporte
d) 3,072Mbps
```

---

**71_preguntas_tese_b · nº 20 · respuesta: b**

```
20.- En una unidad móvil, se avería el distribuidor de código de tiempo LTC. Ante la falta de
repuesto para solucionar el problema, disponemos en la instalación de distribuidores de
referencia blackburst, de audio analógico, de SDI y de AES3 que no se están
utilizando.Indicar cuál de estos distribuidores podemos usar para solucionar
momentáneamente la avería hasta que el distribuidor de código de tiempo se repare.
a) Distribuidor de referencia blackburst.
b) Distribuidor de audio analógico.
c) Distribuidor de SDI.
d) Distribuidor de AES3.
```

