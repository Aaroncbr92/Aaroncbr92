# Puesto 29 · Tema 10 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/10-virtualizacion-de-sistemas-y-escritorios.md`
(de 11.407 a 12.559 palabras según `indice.py`; 30 epígrafes, sin epígrafes nuevos).

**Amplía contenido nuevo: sí** (L1-L4). Procede la fase 5 bis sobre los pasajes listados abajo.

## Correcciones de exactitud (comprobadas en la fuente antes de aplicarlas)

| # | Comprobación | Aplicada | Pasaje cambiado |
|---|---|---|---|
| M1 | NIST SP 800-125 § 2.1 (`nist-sp800-125.txt`, l. 393-399), releído el 06-10-2026: la cuarta frase («quite dynamic… security boundaries more complex») está en el mismo párrafo | Sí | Ep. 1 «Por qué se virtualiza»: cuarta viñeta, «Entornos que cambian deprisa», con su cita y traducción |
| M2 | NIST SP 800-125 (l. 454): sólo cita VirtualPC como ejemplo de emulación; nada sobre el origen del término | Sí | Ep. 3 «PC virtual»: «El NIST cita un producto antiguo con ese nombre, VirtualPC, como ejemplo de emulación» |

## Lagunas: se amplía el tema (fuentes nuevas, leídas el 06-10-2026)

Volcados nuevos en `fuentes/canal-sur/informatico/web/`: `v-xen.txt`, `v-redhat-hyp.txt`,
`v-ibm-hyp.txt`, `v-aws-hyp.txt`, `v-aws-vdi.txt`, `v-citrix-hdx.txt`, `v-citrix-tech.txt`,
`v-citrix-edt.txt`, `v-citrix-daas.txt`, `v-omnissa-arch.txt`.

| # | Pasaje cambiado | Fuente |
|---|---|---|
| L1 | Ep. 1 «El hipervisor: tipo 1 y tipo 2»: tabla de ejemplos (Xen, ESXi, KVM/Hyper-V/vSphere de tipo 1; VMware Workstation y VirtualBox de tipo 2) y párrafo sobre el dominio 0/DomU de Xen y la paravirtualización | Xen Project Wiki; IBM Think; Red Hat |
| L1 | Ep. 1 «KVM, el hipervisor de Linux»: la última frase («este tema tampoco lo hace») se sustituye por la discrepancia Red Hat (tipo 1) / Amazon (híbrido que tira a tipo 1) | Red Hat; AWS «What is a hypervisor?» |
| L3 | Ep. 3 «Escritorio virtual (VDI)», tras Amazon WorkSpaces: párrafo del cliente ligero (AWS, IBM, NIST «thin client interface») y agente de conexión | AWS «What is VDI?»; IBM; NIST SP 800-145 |
| L2 | Mismo epígrafe: tabla de protocolos de visualización (RDP; HDX sobre ICA, con transporte EDT y puertos 2598/1494/443; Blast, PCoIP y RDP en Horizon 8) | Citrix «HDX», «Technical overview», «Adaptive transport»; Omnissa «Horizon 8 architecture» |
| L4 | Ep. 4 «Cloud: en la nube»: párrafo del DaaS (definición de IBM; sentido estrecho de AWS, que separa WorkSpaces; Citrix DaaS híbrido; Microsoft no lo usa en las páginas leídas) | IBM; AWS «What is VDI?»; Citrix DaaS |

Además: siglas (DaaS, ICA, HDX/Blast/PCoIP, ESXi, IBM), portada (Fuente, Redacción, Extensión),
«Qué se puede preguntar», «Lo que este tema no da» (línea de VMware/Omnissa/Xen reescrita; cliente
cero declarado como no encontrado) y una tabla nueva en «Trazabilidad» con las fuentes añadidas.

## Dónde el informe de refutación no se siguió al pie de la letra

- L1: la documentación de Broadcom/VMware no se descarga en texto (página cargada por JavaScript);
  ESXi se clasifica con IBM y Workstation con Red Hat. El «only type-1 hypervisor that is available as
  open source» de Xen no se cita, porque choca con Red Hat (KVM de tipo 1).
- L2: la página de Omnissa Docs volvió a fallar; se usó la arquitectura de referencia de Omnissa Tech
  Zone. La sigla de PCoIP no se desarrolla: la fuente no lo hace.
- L3: el cliente cero no aparece en ninguna fuente leída; se declara.
- L4: la refutación proponía decir que Windows 365 o AVD son DaaS. Ninguna fuente leída lo dice, y
  AWS distingue su WorkSpaces («fully managed») del DaaS; no se aplica esa equivalencia.
- Se quitó una frase propia del borrador («el cliente de un fabricante no sirve para el escritorio de
  otro») por no tener fuente, y «Horizon, antes de VMware», por lo mismo.

## Lentes

Tema técnico sin norma: `refutar_prosa.py` 0 hallazgos (tras presentar IBM y quitar la mención a la
marca de la vGPU); `indice.py` regenerado, 30 epígrafes, índice sin cambios. No proceden
`negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Pasajes releídos

Cada pasaje cambiado se releyó; las remisiones («tabla de ejemplos, más arriba», «epígrafe 2»,
«citado en el PC virtual») tienen su antecedente en el tema.

## Otros ficheros tocados

Los diez volcados nuevos de `fuentes/canal-sur/informatico/web/` citados arriba y este informe.
