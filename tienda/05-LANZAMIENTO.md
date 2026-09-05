# 5 · Legal, precios y lanzamiento

## 5.1 Lo que hay que publicar antes de cobrar el primer euro

No es formalismo: sin esto la tienda es sancionable, y Google exige los enlaces
para aprobar la pantalla de consentimiento de OAuth (fase 4).

| Página | Qué tiene que decir | De dónde sale |
|---|---|---|
| **Aviso legal** | Nombre y apellidos o razón social, NIF, domicilio, correo de contacto. La LSSI obliga a que sean localizables sin registrarse. | Tus datos. |
| **Política de privacidad** | Quién es el responsable, qué datos tratas (correo, nombre, dirección de facturación, registro de descargas), con qué base jurídica, cuánto los conservas, con quién los compartes —**Stripe, Google y tu proveedor de correo son cesionarios y hay que nombrarlos**— y cómo se ejercen los derechos. | Plantilla + revisión. |
| **Política de cookies** | Qué cookies pones y para qué. Con banner de **consentimiento previo**: nada de analítica antes de aceptar. | Plugin de consentimiento. |
| **Condiciones generales de venta** | Qué se vende, precio con impuestos, forma de pago, **entrega inmediata por descarga**, licencia de uso personal e intransferible, y la **renuncia al desistimiento** de `04-PAGOS.md` §4.5. | Redactado propio. |
| **Resolución de litigios** | Enlace a la plataforma europea de resolución de litigios en línea. | Enlace de la Comisión Europea. |

Dos avisos que valen su peso:

- **La plantilla genérica no vale tal cual.** La tuya tiene que nombrar a
  Stripe, a Google y al proveedor de correo, y describir el registro de
  descargas. Eso no viene en ninguna plantilla.
- **Una revisión de un abogado cuesta menos que una sanción**, y menos que
  reescribir las condiciones cuando ya hay doscientos clientes que aceptaron
  otras.

Y en la licencia, escribe explícitamente lo que ya hace el código: **cada PDF
va sellado con el nombre y el correo del comprador**. Decirlo antes de vender
es lo que lo convierte en disuasorio; decirlo después es una sorpresa
desagradable y un problema de protección de datos.

---

## 5.2 Precios

Los del CSV son una propuesta, calculada por tramos de páginas en
`herramientas/catalogo.py` (constantes `TRAMOS` y `PRECIO_GENERAL`):

| Volumen | Páginas | Precio |
|---|---:|---:|
| Temario general | 259 | **34 €** |
| Específico corto (≤ 180 pp) | 135–166 | **44 €** |
| Específico medio (181–260 pp) | 182–259 | **54 €** |
| Específico largo (> 260 pp) | 261–578 | **64 €** |

Con **pack general + específico al −15 %**, aplicado solo en el carrito por el
tema hijo. La combinación típica —general + su específico— sale entonces entre
66 € y 83 €.

**Cómo mirar si están bien.** No compares con un PDF suelto: compara con lo que
cuesta una academia de oposiciones, que son cientos de euros al mes. Un temario
verificado contra fuente oficial, con las preguntas reales de las convocatorias
anteriores y con actualizaciones incluidas, no compite con un apunte de
segunda mano; compite con el tiempo que el opositor tardaría en construirlo.

Tres decisiones de precio que sí importan:

- **No pongas el general muy barato.** Es la puerta de entrada, pero si vale 9 €
  el catálogo entero se lee como material de saldo.
- **Cuidado con el descuento de lanzamiento.** Quien compra a 30 € no vuelve a
  comprar a 54. Si haces oferta, ponle fecha de fin y cúmplela.
- **Los tramos son por páginas, no por valor.** El de Medicina tiene 578
  páginas y ninguna pregunta de examen; el de Sonido, 207 y 134 preguntas.
  Repásalos a mano antes de publicar: el algoritmo no sabe cuál cuesta más de
  escribir.

---

## 5.3 Antes de abrir

Marca las diecisiete. La numeración remite a las fases de
`02-IMPLANTACION.md`.

**Que nadie llegue a un fichero** (fase 3)
- [ ] `curl -I https://…/temarios_privados/libros/libro-sonido.pdf` → 403 o 404
- [ ] `curl -I https://…/wp-content/uploads/…/libro-sonido.pdf` → 403 o 404
- [ ] En «Mis temarios», copiar el enlace de descarga, esperar 11 minutos y
      abrirlo → devuelve al panel con aviso, no el PDF
- [ ] Ese mismo enlace, pegado en la sesión de **otra cuenta** → 403

**Que el dinero y la entrega vayan juntos** (fases 5 y 7)
- [ ] Compra real con tarjeta propia, de principio a fin, y reembolso después
- [ ] Pago rechazado (`4000 0000 0000 9995`) → sin descarga
- [ ] Tras el reembolso total, la descarga da 403
- [ ] El correo de compra llega a Gmail, a Outlook y a una cuenta corporativa,
      **y no a la carpeta de no deseado**
- [ ] La factura se adjunta y lleva numeración correlativa

**Que el acceso funcione** (fase 4)
- [ ] Alta con Google desde el móvil, en incógnito
- [ ] Segundo acceso con la misma cuenta → **entra en el mismo usuario**, no
      crea otro
- [ ] Cancelar en la pantalla de Google → vuelve con un aviso, no con un error

**Que no se filtre una sesión** (fase 9)
- [ ] Dos navegadores, dos cuentas, `/mi-cuenta` a la vez → cada uno ve lo suyo
- [ ] Un usuario cliente que intente entrar en `/wp-admin` → va a «Mi cuenta»
- [ ] `/?author=1` → redirige a la portada

**Que se pueda recuperar** (fase 10)
- [ ] Copia restaurada en el sitio de pruebas y arrancando

---

## 5.4 Las primeras semanas

**Los tres primeros pedidos, míralos enteros.** Pedido, correo, factura,
descarga y registro. Los fallos raros salen ahí y no en las pruebas.

**Qué medir**, y sólo esto al principio:

| Número | Dónde | Qué te dice |
|---|---|---|
| Visitas a la ficha → clics en «Ver muestra» | Analítica | Si la ficha convence. |
| Clics en la muestra → compras | Analítica + Woo | **El número clave.** Si la gente mira la muestra y no compra, el problema es el precio o la muestra. |
| Carritos abandonados en el pago | WooCommerce | Fricción en la pasarela. |
| Descargas por comprador | `wp_toac_descargas` | Uso real y cuentas compartidas. |
| Correos de soporte por pedido | Tu bandeja | Si sube de 0,2, algo de la tienda no se entiende. |

**Mantenimiento mensual**, media hora:

1. Actualizar WordPress, WooCommerce y los plugins. Antes, copia de seguridad.
2. Revisar la consulta de cuentas compartidas de `03-PDFS.md` §3.7.
3. Comprobar que la copia semanal fuera de Hostinger existe y pesa lo que debe.
4. Mirar si alguna norma de los temarios ha cambiado. Si ha cambiado:
   regenerar el volumen (`03-PDFS.md` §3.6) y **avisar a los compradores**.

Ese último punto es el que sostiene el negocio. Un temario de oposiciones vale
lo que vale su fecha, y ahí es donde un PDF pirata de hace tres convocatorias
no puede competir contigo.
