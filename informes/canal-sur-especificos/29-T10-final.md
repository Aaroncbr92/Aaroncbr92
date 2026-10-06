# Puesto 29 · Tema 10 · Revisión de los pasajes del remate (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Sólo se revisan los pasajes listados en
`29-T10-remate.md` (M1, M2, L1-L4, siglas, portada, «Qué se puede preguntar», «Lo que este tema no da»
y la tabla nueva de «Trazabilidad»). Todas las fuentes, releídas el 06-10-2026 en
`fuentes/canal-sur/informatico/web/`.

## Comprobación dato a dato

| Pasaje | Fuente (línea del volcado) | Resultado |
|---|---|---|
| M1 cuarta viñeta NIST | nist-sp800-125.txt l. 398-399 | Literal, mismo párrafo |
| M2 VirtualPC | nist-sp800-125.txt l. 454 | Literal |
| L1 Xen tipo 1 | v-xen.txt l. 94 | Literal |
| L1 ESXi tipo 1 | v-ibm-hyp.txt l. 156 | Literal |
| L1 KVM/Hyper-V/vSphere tipo 1; Workstation/VirtualBox tipo 2 | v-redhat-hyp.txt l. 468, 478 | Literal |
| L1 dominio 0, DomU, PV | v-xen.txt l. 110, 118, 146; «primera máquina», l. 120 («first VM started by the system») | Literal / sostenido |
| L1 KVM híbrido (AWS) | v-aws-hyp.txt l. 417 | Literal |
| L3 cliente ligero (AWS, IBM, NIST) y agente de conexión | v-aws-vdi.txt l. 461; v-ibm-hyp.txt l. 145, 147; nist-sp800-145.txt l. 168 | Literal |
| L2 HDX | v-citrix-hdx.txt l. 1769 | Literal |
| L2 fichero y pila ICA | v-citrix-tech.txt l. 1945, 1947 | Literal |
| L2 transporte adaptable, EDT, caída a TCP, puertos | v-citrix-edt.txt l. 1765-1779, 1840-1870 | Corregido (C1) |
| L2 Horizon multiprotocolo; Blast TCP/UDP, vGPU | v-omnissa-arch.txt l. 929, 939 | Literal |
| L4 DaaS IBM, AWS (gestionado vs DaaS), Citrix híbrido | v-ibm-hyp.txt l. 139; v-aws-vdi.txt l. 423-437; v-citrix-daas.txt l. 1288 | Literal; regla de test corregida (C2) |
| Trazabilidad: fechas de página | Xen 13-02-2024 (l. 961); Red Hat 03-01-2023 (l. 434); Citrix 06-09-2025, 22-04-2026, 15-09-2025, 24-06-2026 (l. 1759); Omnissa 2026-06-24 (l. 1915) | Correctas |

## Correcciones aplicadas (comprobadas en la fuente)

- **C1 (error 6, salvedad omitida; error 5)**: los puertos 2598/1494/443 son, en la fuente, reglas de
  entrada **UDP para conexiones internas** al host de sesión, y el 443 es «HDX Direct or VDA SSL». Se
  dice «en las conexiones internas … tráfico entrante por UDP en los puertos … y 443 (HDX Direct o
  conexión cifrada)». No se usa «VDA» ni «SSL» para no meter siglas sin presentar.
- **C2 (error 9, sin fuente)**: «pagado por suscripción» en la regla de test del DaaS no está en IBM,
  AWS ni Citrix. Queda «servido y gestionado por un proveedor desde la nube».

## Antecedentes

Releídos los pasajes cambiados: «tabla de ejemplos, más arriba», «epígrafe 2», «citado en el PC
virtual», «la misma tabla de Microsoft» y «esa capa» tienen antecedente. Todas las siglas nuevas
(DaaS, ICA, HDX/Blast/PCoIP, ESXi, IBM, EDT desarrollada en el texto, UDP/TCP) están presentadas.

## Lentes

`refutar_prosa.py`: 0 hallazgos tras las correcciones. Índice sin cambios (no se tocan rúbricas).

## Otros ficheros tocados

Sólo el tema y este informe.
