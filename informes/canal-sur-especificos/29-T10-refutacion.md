# Puesto 29 · Tema 10 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/10-virtualizacion-de-sistemas-y-escritorios.md`
(1.007 líneas, 11.407 palabras de cuerpo).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios» (informe de redacción): la frase en una
  línea, la tabla de tipos de hipervisor, las cuatro ventajas, la frase máquina virtual/contenedor y
  la fila y párrafo del KVM sobre IP. Saltados en exactitud; sí cuentan para cobertura.
- Fuentes: los volcados de la redacción en `fuentes/canal-sur/informatico/web/` (`v-*.txt`,
  `nist-sp800-125.txt`, `nist-sp800-145.txt`, descargados el 05-10-2026), releídos el **06-10-2026**
  sobre los pasajes concretos. Nada descargado de nuevo.
- Lentes (tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` sobre una copia en el
  scratchpad: 30 epígrafes, índice idéntico al del tema. No proceden `negritas.py`,
  `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto (sobre todo la redonda, donde cae el error 9): NIST SP 800-125
§ 2 (reparto y aislamiento con acceso a recursos compartidos, paravirtualización «significantly
faster», hardware virtual con USB y puertos serie y paralelo, emulación y VirtualPC, motivos de la
virtualización de escritorio, datos fuera de la imagen, aplicación en vez de escritorio con el ejemplo
del navegador antiguo); SP 800-145 (pago por uso, clientes ligeros o pesados); `Set-VM
-CheckpointType` y la caída a estándar sólo con `Production`; «Crear punto de control y aplicar» /
«Aplicar» / «No es posible deshacer»; Server Core e `-IncludeManagementTools`; generación 2 con TPM
2.0 virtual y BitLocker; Windows Admin Center y SCVMM; Datacenter; Réplica y RPO de 30 s; Site
Recovery; Azure Local en Hyper-V, RDS y AVD; 1:1 en Enterprise, Business y Government, Flex hasta
tres equipos; Espacio aislado (ediciones Pro, Enterprise, Pro Education/SE, Education; 22H2; red por
defecto; una instancia); aplicación de Windows (Meta Quest, inicio de sesión no necesario para PC
remoto); grupo personal «Uno», amplitud/profundidad; CimFS/VHDX/VHD; RDS en Azure IaaS; columna de
despliegue de MV en la tabla de contenedores y salvedad del aislamiento de Hyper-V; matriz de
responsabilidad (las diez filas de la fuente, agrupadas en seis sin error), responsabilidades que
siempre se conservan, hipervisor a cargo de Microsoft, los cinco fallos de lo local; Docker.

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| M1 | Menor | 3 recuento / 6 salvedad | Ep. 1 «Por qué se virtualiza»: «Los inconvenientes, que el tribunal también puede pedir, los da el NIST:» y tres viñetas | SP 800-125 § 2.1 da un cuarto en el mismo párrafo: **«In some cases, virtualized environments are quite dynamic, which makes creating and maintaining the necessary security boundaries more complex.»** La frase introductoria presenta la lista como la del NIST completa | Añadir la cuarta viñeta (entornos dinámicos, límites de seguridad más difíciles de mantener) con su cita |
| M2 | Menor | 9 sin fuente | Ep. 3 «PC virtual»: «El nombre viene de un producto antiguo que el NIST cita como ejemplo de emulación» | El NIST sólo cita VirtualPC como ejemplo de emulación (**«early versions of VirtualPC allowed users to run the Microsoft Windows OS on the PowerPC processor…»**); no dice nada del origen del término «PC virtual». La salvedad que sigue («que el enunciado lo use en este sentido es interpretación del tema») no cubre la etimología | Cambiar por «El NIST cita un producto antiguo con ese nombre, VirtualPC, como ejemplo de emulación» y dejar la interpretación como está |

Sin hallazgo en: cita cruzada (1), ley por reglamento (2), «podrá»/«deberá» (4), siglas (5; 0 en
`refutar_prosa.py`), redacción derogada (7: AVD clásico y MDOP, con su fecha), artículo mal (8).

## Lente 2 · Cobertura

Las rúbricas del enunciado tienen epígrafe propio y en su orden (sistemas; escritorio remoto; PC
virtual, escritorio virtual, aplicaciones, workspace; on-premise, cloud, híbrido). Quince preguntas en
`29-T10-preguntas.md`: **11 enteras, 2 a medias (2, 10), 2 no (9, 14)**.

| # | Laguna | Rúbrica | Propuesta |
|---|---|---|---|
| L1 | Ejemplos de hipervisor de tipo 1 fuera de Microsoft (VMware ESXi, Xen) y clasificación de VMware Workstation: el tema sólo clasifica Hyper-V y VirtualBox, y declara ESXi como no dado. Es la pregunta de test más típica del bloque (pregunta 2) | Virtualización de sistemas | Leer la documentación de Broadcom/VMware (ESXi «bare-metal hypervisor», Workstation «hosted») y la del proyecto Xen, y añadir una fila de ejemplos a la tabla de tipos |
| L2 | Protocolos de visualización remota distintos de RDP (Citrix HDX/ICA, VMware/Omnissa Blast y PCoIP) | Virtualización de escritorio remoto / escritorio virtual | Una tabla breve con protocolo y fabricante, leída en documentación de Citrix y Omnissa (la de Omnissa falló en texto; probar otra página) |
| L3 | Cliente ligero (*thin client*) y cliente cero como dispositivo de acceso a la VDI: el tema lo roza (NIST «thin or thick», Windows 365 Link) sin definirlo | Escritorio virtual | Definirlo con fuente (NIST o documentación de fabricante) en «Escritorio virtual» o en «Virtualizar el escritorio» |
| L4 | El término DaaS (escritorio como servicio), habitual para Windows 365, AVD o WorkSpaces; el tema sólo da SaaS/IaaS/PaaS | Modos de despliegue: cloud | Añadir el término con fuente (Microsoft, AWS o Citrix lo usan) en «Cloud: en la nube», diciendo que no es un modelo del NIST |

## Recuento

Graves: 0. Menores: 2 (M1, M2). Lagunas: 4 (L1-L4).

## Otros ficheros tocados

Ninguno, salvo este informe y `29-T10-preguntas.md`. Copia del tema para `indice.py`, en el
scratchpad de la sesión (fuera del proyecto).
