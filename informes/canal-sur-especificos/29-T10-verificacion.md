# Puesto 29 · Tema 10 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 05/06-10-2026 en sus volcados
de `fuentes/canal-sur/informatico/web/` (`v-*.txt`, `nist-sp800-125.txt`, `nist-sp800-145.txt`),
descargados el 05-10-2026 con URL y fecha en cabecera; no se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/10-virtualizacion-de-sistemas-y-escritorios.md`.

## Método

- Copiado del común: nada (según `29-T10-redaccion.md`).
- Copiado de RTVE sin cambios: comprobado sólo que es literal, por script contra
  `temas/tecnica-informatica/17-…md` (§ 5) y `temas/tese/12-…md` (§ 6), sin las negritas: la frase
  en una línea, la tabla de tipos de hipervisor, las cuatro ventajas, la frase máquina
  virtual/contenedor (sin «El contenedor arranca en segundos y aísla menos», quitada a propósito), la
  fila de KVM sobre IP y su párrafo. Todo literal. No se ha re-verificado.
- Todo lo demás: cada una de las 293 negritas se buscó **en la fuente a la que el tema la atribuye**
  (script nuevo que dice en qué fichero aparece cada cita, no sólo si aparece en alguno), y se leyó
  cada página entera para ver el contexto, las salvedades y lo dicho en redonda. Con los nueve
  errores delante.
- Lentes (ENCARGO, tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` 30
  epígrafes, el índice no cambia. No proceden `negritas.py`, `refutar_exactitud.py` ni
  `refutar_modo.py`. Literalidad tras las correcciones: 294 citas, 0 no halladas.

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 1 cita cruzada | § 1, ediciones de Hyper-V | «las dos coinciden: «El rol Hyper-V no se puede instalar en … Home»», pero la frase está en una tercera página («Instalar Hyper-V»), no en las de requisitos ni de presentación | Se atribuye a la página de instalación, y se dice que esa da Pro o Enterprise, como la de requisitos |
| 2 | 1 / 6 | § 1, puntos de control, y caso práctico | «Una instantánea no es una copia de seguridad completa…» se daba como algo dicho de todos los puntos de control; Microsoft lo dice del **estándar** | Se atribuye al punto de control estándar en los dos sitios |
| 3 | 6 salvedad | § 1, contenedores (tabla) | «Se ejecuta en la misma versión del sistema operativo que el host» sin su paréntesis: con el aislamiento de Hyper-V, versiones anteriores | Añadida |
| 4 | 6 | § 1, qué es virtualizar | El NIST da el aislamiento de cada invitado «así como un posible acceso a recursos compartidos, como ficheros del anfitrión»; se había cortado | Añadido en redonda |
| 5 | 6 | § 1, requisitos | La SLAT no hace falta para instalar sólo las herramientas de administración (página de requisitos) | Añadido |
| 6 | 9 sin fuente | § 1, requisitos | «son los que se comprueban en la BIOS o UEFI cuando una máquina virtual no arranca»: sin apoyo, y la RAM no se comprueba en la BIOS | Sustituido por: la virtualización asistida y la DEP se activan en la BIOS o UEFI (lo dice la página) |
| 7 | 6 | § 2, NLA | Omitía que, con clientes antiguos sin NLA, puede hacer falta deshabilitarla temporalmente | Añadido |
| 8 | 6 | § 2, puerto RDP | Por el Editor del Registro, la página manda reiniciar el equipo | Añadido |
| 9 | 3 recuento | § 2, Aplicación de Windows | Lista de plataformas sin Meta Quest, que la página incluye | Añadido |
| 10 | 9 | § 2, modelos de RDS | «Trabajadores del conocimiento que necesitan un Windows cliente», paráfrasis que perdía «aislamiento de aplicaciones» | Sustituido por la cita literal |
| 11 | 6 | § 3, Espacio aislado | «cerrarlo elimina todo» sin la nota de la página: desde Windows 11 22H2 los datos sobreviven a los reinicios hechos dentro | Añadido |
| 12 | 9 | § 3, App-V | «Microsoft recomienda pasar a…»; la página dice «Te recomendamos que consultes…» | «Microsoft remite a» |
| 13 | 5 sigla / 6 | § 3, App Attach | CimFS sin presentar; los tres formatos de imagen son para MSIX y Appx | Presentada la sigla y precisado |
| 14 | 6 | § 4, IaaS (NIST) | Faltaba «and possibly limited control of select networking components (e.g., host firewalls)» | Añadido en redonda |
| 15 | 6 | § 4, agrupación de recursos | «el cliente no sabe»; el NIST dice «generally has no control or knowledge» | «por lo general» |
| 16 | 9 | § 4, híbrido | Daba la nube híbrida del NIST como definición formal de «lo propio + nube»; el NIST habla de infraestructuras **de nube**, y el propio tema dice que un CPD no es nube privada sin las cinco características | Precisado: esa suma es uso común, no definición del NIST |
| 17 | 3 | Lo que este tema no da | «una página la incluye y otra no» (Education); son dos las que no | Corregido |
| 18 | 5 | Trazabilidad | «GPU-P» sin presentar | «particiones de GPU» |
| 19 | — | Trazabilidad | Faltaban fechas de actualización que las páginas sí muestran | Añadidas: «Instalar Hyper-V» 2025-05-26, puntos de control 2025-08-15, App Attach 2026-08-26, responsabilidad compartida 2026-08-24, Citrix 2026-06-22 |

## Confirmado sin cambios (muestra de lo que se comprobó en redonda)

Autores y fechas de las dos SP del NIST; recuentos 5/3/4 del NIST; las ocho filas de la matriz de
responsabilidad; puerto 3389 y ejemplo 3390; reglas TCP y UDP del cortafuegos; seis roles de RDS y
TCP 443; Server Core con `-IncludeManagementTools`; Datacenter; ediciones de Windows 365 (Business
hasta 300 puestos, Flex hasta tres equipos, agentes en versión preliminar); 1:1 en Enterprise,
Business y Government; retirada de AVD clásico el 30-09-2026 y migración a Azure Resource Manager;
fin del soporte extendido de MDOP el 14-04-2026; tipos de paquete de App Attach; registro a
petición por defecto; Azure Local por núcleo físico; ediciones del Espacio aislado; WorkSpaces
Personal y Pool; título de la página de Citrix. El «*sic*» de «REDES virtuales» y de «Windows
Novedades» no se puede contrastar con la versión inglesa (no descargada); se deja como nota de
traducción.

## Lo que no se pudo confirmar

Nada quitado: todo dato afirmado quedó con fuente o se corrigió. Siguen como oficio declarado (no
es cita ni se presenta como norma): la comparación KVM sobre IP / Escritorio remoto, los tres
escalones, los cuadros de síntesis y el caso práctico. La «Movilidad … se restaura como un fichero»
es RTVE sin cambios y ya figura en la Trazabilidad como sin apoyo directo.

## Pasajes cambiados

Los 19 de la tabla (41 líneas del diff). Releídos: cada «la de instalación», «la misma página»,
«por ese camino» tiene su antecedente delante. Extensión: 11.407 palabras de cuerpo (`indice.py`),
dentro de las 11.500 aproximadas de la ficha.

## Otros ficheros tocados

Ninguno, salvo este informe. Copia del tema antes de verificar y scripts de comprobación, en el
scratchpad de la sesión (fuera del proyecto).
