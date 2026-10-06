# Puesto 29 · Tema 10 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación y en los temas 5 a 9). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/10-virtualizacion-de-sistemas-y-escritorios.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 10). `AGRUPACION.tsv`: tema 10 «nuevo». Fila de
`informes/canal-sur-reuso/informatica.tsv`: RTVE `tecnica-informatica/17` y `tese/12`, 20 %,
«actualizar: no».

## Avance

- Ficha, siglas, enunciado, «qué se puede preguntar» y epígrafe 1 (virtualización de sistemas: definición, ventajas e inconvenientes, tipo 1 y 2, Hyper-V requisitos/instalación/funciones, puntos de control, KVM, MV frente a contenedor) guardados. Comprobación de literalidad: 99 citas en negrita halladas tal cual.
- Epígrafe 2 (virtualización de escritorio remoto: local o remoto, RDP en un equipo, RDS con roles y modelos, KVM sobre IP) guardado. Literalidad: 165 citas acumuladas, todas halladas.
- Epígrafe 3 (modelos: advertencia de vocabulario, PC virtual en sus dos lecturas, escritorio virtual con AVD y FSLogix, virtualización de aplicaciones con RemoteApp/App-V/App Attach, workspace virtual, cuadro) guardado. Literalidad: 239 citas acumuladas, todas halladas.
- Epígrafe 4 (modos de despliegue: NIST, on-premise, cloud con matriz de responsabilidades, híbrido, cuadro, caso práctico), «Lo que este tema no da» y «Trazabilidad» guardados. Índice generado con `indice.py`. Literalidad final: 293 citas en negrita, todas halladas.

## Fuentes leídas y fecha

Todas el 05-10-2026, descargadas como texto con URL y fecha en cabecera en
`fuentes/canal-sur/informatico/web/` (nuevas, prefijo `v-`): `v-hyperv`, `v-hypervwin` (redirige a
la misma página que `v-hyperv`), `v-hypervreq`, `v-hypervenable`, `v-checkpoints`, `v-kvm`,
`v-vbox`, `v-contvm`, `v-docker`, `v-rds`, `v-rdenable`, `v-rdpport`, `v-winapp`, `v-avd`,
`v-avdterm`, `v-w365`, `v-sandbox`, `v-fslogix`, `v-appv`, `v-appattach`, `v-azlocal`,
`v-sharedresp`, `v-awsws`, `v-citrixdocs`; y los PDF del NIST `nist-sp800-145.pdf` y
`nist-sp800-125.pdf` con su `.txt` (`documento.py texto`). La ficha del CSRC del NIST se consultó el
mismo día: ambas publicaciones figuran como publicadas (enero y septiembre de 2011) sin aviso de
retirada. Descargas fallidas, conservadas pero no usadas: `v-citrix.txt` (página de Citrix Tech
Zone bloqueada por Cloudflare, 3 palabras) y `v-omnissa.txt` (página de Omnissa Horizon que sólo
sirve el menú).

Huecos de la investigación cubiertos con fuente: puerto RDP 3389 (`v-rdpport`); hipervisor tipo 1
y 2 con fuente (NIST SP 800-125 para *bare metal*/alojado; VirtualBox para la numeración; Microsoft
para Hyper-V tipo 1); frase de RTVE sobre contenedores (Microsoft «Contenedores frente a máquinas
virtuales»); Docker releído en su página (antes sólo vía resumen). Huecos que siguen (declarados en
el tema): definición neutral de «PC virtual» y «workspace virtual»; VMware ESXi y Omnissa Horizon;
herramientas de KVM; clasificación IaaS/PaaS de AVD; la cita de Citrix Tech Zone de la
investigación no se pudo releer y no se usa (se usa en su lugar la de StoreFront Cloud, leída).

Comprobación de literalidad por script (`scratchpad/t10check.py`, el de T08 con las fuentes `v-*` y
`nist-*`, normaliza espacios, comillas, apóstrofos y acentos graves): 293 citas en negrita, 0 no
halladas. En la primera pasada fallaron 2 rótulos en negrita que no eran cita (pasados a cursiva).
`refutar_prosa.py`: 7 siglas sin presentar (DISM, GB, IP, PC, QEMU, TI, USB) y una negrita partida
por salto de línea que dejaba una línea empezando por guion (se pasó a tabla); corregidas, 0
hallazgos. Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`. `indice.py`: 30 epígrafes; ficha escrita a mano (el tema no está en
`portadas.tsv`).

## Qué se hizo

Cuatro epígrafes en el orden del enunciado: 1 virtualización de sistemas (definición NIST,
hipervisor, ventajas e inconvenientes, tipo 1 y 2, Hyper-V requisitos, ediciones, instalación y
funciones, puntos de control, KVM, MV frente a contenedor y Docker); 2 virtualización de escritorio
remoto (local frente a remoto, Escritorio remoto de un equipo con ediciones, puerto, NLA y
clientes, RDS con roles y modelos, KVM sobre IP); 3 modelos de virtualización (PC virtual en dos
lecturas con Espacio aislado y Windows 365, escritorio virtual con RDS, AVD y FSLogix,
virtualización de aplicaciones con RemoteApp, App-V y App Attach, workspace virtual, cuadro); 4
modos de despliegue (NIST completo, on-premise, cloud con matriz de responsabilidad, híbrido con
Azure Local y Site Recovery, cuadro, caso práctico).

Decisiones:

- «PC virtual» y «workspace virtual»: sin definición normativa; el tema da las dos lecturas de PC
  virtual (MV local y PC en la nube) y una interpretación declarada de workspace apoyada en tres
  fabricantes (Microsoft, Amazon, Citrix).
- «Híbrido» en RDS (sesión + VDI) se separa expresamente del despliegue híbrido del enunciado.
- KVM hipervisor y KVM sobre IP se separan en las siglas, en el epígrafe 1 y en el 2.
- Desajuste de fuentes señalado: ediciones de Windows 11 con Hyper-V (una página incluye Education,
  otra no); se dan las dos y lo común (Home no).
- Vigencia: AVD clásico se retira el 30-09-2026 (posterior al 24-09-2026 del encargo y anterior a
  la lectura); MDOP/App-V fuera de soporte extendido desde el 14-04-2026. Se dicen con su fecha.
- Fecha de lectura (05-10-2026) posterior a la del encargo (24-09-2026), como en los temas 5 a 9.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata virtualización.

## Copiado de RTVE sin cambios

Los dos temas de RTVE están marcados «actualizar: no». Pasajes técnicos copiados literal, sin
cambiar una palabra; único cambio, de formato: quitada la negrita, porque RTVE no citaba fuente y
en este tema negrita es cita. Se declaran como oficio en la Trazabilidad del tema.

| Pasaje en RTVE | Dónde va en el tema |
|---|---|
| `tecnica-informatica/17` § 5: «La idea, en una línea: un solo equipo físico ejecuta varias máquinas completas, cada una con su propio sistema operativo, gracias a una capa que reparte el soporte físico entre ellas.» | § 1, «Qué es virtualizar» |
| `tecnica-informatica/17` § 5: «Los dos tipos de esa capa:» y la tabla «Tipo / Dónde se instala / Para qué» entera (dos filas) | § 1, «El hipervisor: tipo 1 y tipo 2» |
| `tecnica-informatica/17` § 5: «Qué gana una organización con ello, que es lo preguntable:» y la lista de cuatro ventajas (aprovechamiento, aislamiento, movilidad, instantáneas) | § 1, «Por qué se virtualiza» |
| `tecnica-informatica/17` § 5: «Y el contraste con los contenedores, porque el sector los confunde: una máquina virtual lleva su propio sistema operativo completo; un contenedor comparte el núcleo del anfitrión y sólo empaqueta la aplicación y sus dependencias.» Se omite la frase siguiente («El contenedor arranca en segundos y aísla menos.»): lo de los segundos no se confirmó en fuente y el aislamiento se da con la cita de Microsoft | § 1, «Máquinas virtuales y contenedores» |
| `tese/12` § 6: la fila de la tabla «KVM sobre IP / Llevar el teclado, el vídeo y el ratón de un ordenador por la red, para manejarlo desde otro sitio» (cabecera de la tabla cambiada de «Asunto del enunciado / Qué es, en una línea» a «Qué es / Qué hace») y el párrafo «Y por qué el KVM sobre IP importa: permite sacar los ordenadores de la sala de realización y dejarlos en el centro de proceso de datos, quedando en el puesto sólo el teclado, el monitor y el ratón. Menos calor y menos ruido en la sala, y el mantenimiento se hace sin entrar en el plató.» | § 2, «KVM sobre IP» |

Quitado por propio de RTVE: «Es lo último que el enunciado pide y lo que más ha cambiado la sala de
servidores.», los números de pregunta y la tabla de respuestas oficiales, el aviso de estudio y la
Trazabilidad de RTVE («Ninguna documentación de fabricante se ha consultado»), que aquí ya no vale.
Nada del resto de `tese/12` (VLAN, ACL, TRUNK) entra en este enunciado.

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/v-*.txt` (26 volcados nuevos) y `nist-sp800-125.{pdf,txt}`,
  `nist-sp800-145.{pdf,txt}` (nuevos). Ningún fichero existente modificado.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; (AP) = aplicación práctica. Todas se contestan enteras
con el tema; no ha hecho falta ampliarlo.

1. (Virtualización de sistemas) El hipervisor que se instala directamente sobre el hardware, sin
   sistema operativo anfitrión, y que se usa sobre todo en servidores es: a) de tipo 2 o alojado,
   como VirtualBox; b) de tipo 1, nativo o *bare metal*, como Hyper-V; c) un emulador de hardware;
   d) un motor de contenedores. → **b** (la emulación es un tipo de virtualización alojada). § 1,
   «El hipervisor: tipo 1 y tipo 2». Entera.
2. (Virtualización de sistemas, AP) Un técnico quiere activar Hyper-V en un portátil con Windows 11
   Home y procesador con SLAT: a) basta `Enable-WindowsOptionalFeature -Online -FeatureName
   Microsoft-Hyper-V -All`; b) hay que descargar Hyper-V de Microsoft; c) no puede: el rol no se
   instala en Home; d) basta activar Intel VT en la UEFI. → **c**. § 1, «Hyper-V: requisitos e
   instalación». Entera.
3. (Virtualización de sistemas, AP) Antes de actualizar una MV de Hyper-V se crea un punto de control
   sin cambiar la configuración. ¿Qué tipo se crea y qué no guarda? a) Estándar; no guarda los
   discos; b) de producción; no guarda el estado de la memoria; c) de producción; no guarda los
   discos; d) estándar; no guarda la memoria. → **b** (producción es el predeterminado y usa
   instantáneas de volumen). § 1, «Puntos de control». Entera.
4. (Escritorio remoto, AP) Se cambia el puerto de escucha del Escritorio remoto de `pc1.contoso.com`
   al 3390. ¿Qué es correcto? a) El puerto por defecto era el 443 y no hay que tocar el
   cortafuegos; b) era el 3389, hay que añadir una regla de entrada para el 3390 y conectar a
   `pc1.contoso.com:3390`; c) era el 3389 y el cliente lo detecta solo; d) era el 3390. → **b**. § 2,
   «Escritorio remoto de un equipo: RDP». Entera.
5. (Escritorio remoto) En RDS, el rol que permite el acceso RDP cifrado desde redes externas por HTTPS
   (TCP 443) sin abrir puertos RDP internos es: a) Agente de conexión; b) Acceso web; c) Puerta de
   enlace (*RD Gateway*); d) Host de sesión. → **c**. § 2, tabla de roles de RDS. Entera.
6. (PC virtual) Sobre Windows 365, ¿cuál es correcta? a) Es IaaS y el administrador crea cada
   máquina; b) es SaaS, crea el PC en la nube al asignar la licencia y, salvo en Flex, la relación es
   1:1; c) es multisesión como RDSH; d) sólo funciona desde Windows 365 Link. → **b**. § 3, «PC
   virtual». Entera.
7. (Escritorio virtual, AP) Usuarios de un grupo de hosts agrupado de Azure Virtual Desktop pierden
   su configuración al iniciar sesión otro día. La causa y el remedio: a) el grupo es personal;
   pasarlo a agrupado; b) en un grupo agrupado pueden caer en otro host cada vez; guardar los
   perfiles en FSLogix; c) falta la puerta de enlace; d) la sesión estaba desconectada. → **b**. § 3,
   «Escritorio virtual (VDI)». Entera.
8. (Virtualización de aplicaciones) ¿Cuál es cierta? a) App-V es la tecnología que Microsoft
   recomienda hoy; b) App Attach instala las aplicaciones en la imagen del host; c) App Attach
   permite ejecutar varias versiones de la misma aplicación a la vez en el mismo host de sesión; d)
   RemoteApp sólo existe en grupos de hosts personales. → **c** (App-V está en retirada; RemoteApp,
   sólo en agrupados). § 3, «Virtualización de aplicaciones» y tabla de términos de AVD. Entera.
9. (Workspace virtual) En Azure Virtual Desktop, el «área de trabajo» (*workspace*) es: a) una
   colección de MV registradas como hosts de sesión; b) una agrupación lógica de grupos de
   aplicaciones, sin la cual el usuario no ve lo publicado; c) el escritorio personal de cada
   usuario; d) el recurso SMB de los perfiles. → **b** (a es el grupo de hosts). § 3, «Escritorio
   virtual» y «Workspace virtual». Entera.
10. (Modos de despliegue) Según el NIST: a) la nube tiene cuatro características, tres modelos de
    servicio y cinco de despliegue; b) la nube privada siempre está en las instalaciones de la
    organización; c) la nube híbrida es la composición de dos o más infraestructuras distintas que
    siguen siendo entidades únicas, unidas por tecnología que permite portar datos y aplicaciones; d)
    la nube pública está en las instalaciones del cliente. → **c** (cinco, tres y cuatro; la privada
    puede estar «on or off premises»). § 4, «La nube según el NIST». Entera.
