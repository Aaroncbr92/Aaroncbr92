# 4 · Pasarela de pago

## 4.1 La decisión, y por qué no hace falta tomarla del todo

La entrega asume **Stripe como principal y PayPal como secundaria**, porque
WooCommerce las admite a la vez y no obliga a elegir una. Tener las dos no
complica el código: el plugin propio no toca pagos, mira el estado del pedido.

| | Stripe | PayPal |
|---|---|---|
| Comisión (España, tarjeta europea) | ~1,5 % + 0,25 € | ~2,9 % + 0,35 € |
| Experiencia de pago | En tu web, sin salir | Salta a PayPal y vuelve |
| Confianza del comprador que no te conoce | Media | **Alta** |
| Cobro con Bizum / Apple Pay / Google Pay | **Sí** | Parcial |
| Facilidad de reembolso | Alta | Alta |
| Retenciones y bloqueos de cuenta | Raros | Ocurren |

**Recomendación**: empieza con Stripe, y añade PayPal si ves carritos
abandonados en el paso del pago. Bizum, vía Stripe, importa más de lo que
parece para un público español que compra desde el móvil.

Ninguna de las dos ve nunca tus temarios, y **tú nunca ves un número de
tarjeta**: el formulario de Stripe es un `iframe` de Stripe. Eso te saca del
alcance más severo de PCI-DSS, y es una razón de peso para no programar nunca
tú el formulario de pago.

---

## 4.2 Stripe, paso a paso

1. Cuenta en [stripe.com](https://stripe.com) → activa la cuenta con tus datos
   fiscales (NIF, IBAN, actividad).
2. WordPress → Plugins → **WooCommerce Stripe Gateway** (el oficial, de
   Stripe). Ningún otro.
3. WooCommerce → Ajustes → Pagos → Stripe → **Conectar**. Empieza en
   **modo de pruebas**.
4. Activa los métodos: tarjeta, **Bizum**, Apple Pay, Google Pay, y *Link* si
   quieres.
5. **Webhook.** En el panel de Stripe → Desarrolladores → Webhooks → añadir:

   ```
   URL:      https://temarios.example/?wc-api=wc_stripe
   Eventos:  payment_intent.succeeded
             payment_intent.payment_failed
             charge.refunded
             charge.dispute.created
   ```

   Copia el **secreto de firma** (`whsec_…`) y pégalo en los ajustes del
   plugin. Sin esto, un pago que se confirme tarde —una autenticación bancaria
   que el cliente termina en el móvil— **no marca el pedido como pagado**, y el
   cliente paga y no recibe nada. Es el fallo más frecuente y el más caro en
   atención al cliente.

6. **Pruebas obligatorias**, las cuatro:

   | Tarjeta | Debe pasar |
   |---|---|
   | `4242 4242 4242 4242` | Pedido completado, temario en «Mis temarios». |
   | `4000 0025 0000 3155` | Pide autenticación; al superarla, completado. |
   | `4000 0000 0000 9995` | Pedido **fallido**, y **ninguna descarga disponible**. |
   | Reembolso desde el panel de Stripe | El pedido pasa a reembolsado. |

   La tercera es la que de verdad importa: comprueba que un pago rechazado no
   abre nada.

---

## 4.3 Cómo se ata el pago a la descarga

No hay código propio de pagos. La cadena es:

```
Stripe confirma  →  webhook  →  WooCommerce marca el pedido pagado
                                        │
                       woocommerce_payment_complete (tema hijo)
                                        │
                          el pedido pasa a «completado»
                                        │
        toac-tienda.php, en cada descarga, pregunta: ¿hay pedido pagado?
```

La comprobación vive en `toac-tienda.php`:

```php
private function ha_comprado( $usuario_id, $producto_id ) {
    $usuario = get_userdata( $usuario_id );
    // Contra los estados que WooCommerce considera pagados: processing,
    // completed y los que añadan las pasarelas. No contra una lista propia.
    return wc_customer_bought_product( $usuario->user_email, $usuario_id, $producto_id );
}
```

Tres propiedades que se siguen de hacerlo así:

- **Un reembolso completo corta la descarga solo.** El pedido sale de los
  estados pagados y la siguiente petición da 403. No hay que acordarse de nada.
- **Un pago pendiente no abre nada.** «Pendiente» no está entre los pagados.
- **Y el caso que hay que vigilar:** un **reembolso parcial** deja el pedido en
  «completado», así que la descarga sigue abierta. Es lo correcto casi siempre
  —has devuelto parte por una incidencia, no has anulado la venta—, pero si
  algún día devuelves el importe completo, hazlo como reembolso total, no como
  parcial del 100 %.

---

## 4.4 Impuestos

Aquí es donde una tienda de productos digitales se complica de verdad, y
conviene saberlo antes de abrir.

**Vendes servicios prestados por vía electrónica.** Para un consumidor final,
el IVA se devenga **en el país del comprador**, no en España. Un temario
vendido a alguien con dirección en Portugal lleva IVA portugués.

- Por debajo de **10.000 € al año** en ventas transfronterizas B2C dentro de la
  UE, puedes seguir repercutiendo **IVA español**. Con veinticinco temarios y
  un público que es casi todo español, es probable que te quedes ahí años.
- Al pasar ese umbral —o si te acoges voluntariamente— entra la **ventanilla
  única (OSS)**: alta con el **modelo 035** y declaración trimestral con el
  **modelo 369**.
- Hay que **guardar dos pruebas no contradictorias** de dónde está el
  comprador (dirección de facturación y país de emisión de la tarjeta o IP).
  WooCommerce con el módulo de IVA de la UE las guarda; Stripe también las
  registra.

**Configuración en WooCommerce**: Ajustes → General → activar impuestos;
Ajustes → Impuestos → «Los precios incluyen impuestos» → **Sí** (el público
español espera ver el precio final), y dirección fiscal del cliente basada en
la **dirección de facturación**.

**Un punto que hay que consultar y no dar por hecho.** Desde 2020 los libros,
periódicos y revistas en formato electrónico tributan en España al **4 %** en
lugar del 21 %. Si un temario en PDF entra en esa categoría, la diferencia de
precio es enorme. Depende de cómo se califique el producto, y **no es una
decisión que deba tomar tu desarrollador**: pregúntalo a tu asesor fiscal antes
de fijar precios, porque cambia el margen de arriba abajo.

**Facturas.** Plugin *WooCommerce PDF Invoices & Packing Slips*, serie propia,
numeración correlativa sin saltos, y envío automático adjunto al correo de
compra. Consérvalas: son la contabilidad.

Y si todo esto te parece desproporcionado para lo que esperas vender, vuelve a
mirar la **Opción C** de `01-ARQUITECTURA.md` §1.2: un vendedor de registro se
come entre el 5 % y el 10 %, y a cambio esto deja de ser tu problema.

---

## 4.5 Desistimiento: la casilla de la que depende todo

Por defecto, un consumidor tiene **catorce días naturales** para desistir de una
compra a distancia y recuperar su dinero. Aplicado a un PDF, eso significa
descargar el temario y pedir la devolución.

La ley contempla la salida, y es concreta: el derecho de desistimiento **no
aplica** al suministro de contenido digital sin soporte material cuando la
ejecución ha comenzado **con el consentimiento previo y expreso del
consumidor** y con **su conocimiento de que pierde ese derecho**
—artículo 103.m) del texto refundido de la Ley General para la Defensa de los
Consumidores y Usuarios (Real Decreto Legislativo 1/2007)—.

Las tres cosas tienen que ocurrir, y las tres están resueltas en el código:

1. **Consentimiento expreso**: casilla obligatoria en el pago, sin marcar por
   defecto, en `codigo/tema-hijo/functions.php`.
2. **Conocimiento de la pérdida**: el texto de la casilla lo dice con esas
   palabras, no con un enlace a las condiciones.
3. **Prueba**: se guarda `_toac_renuncia_desistimiento` con la fecha y la hora
   en el pedido. Si alguien reclama, ahí está.

```php
add_action( 'woocommerce_review_order_before_submit', function () {
    woocommerce_form_field( 'toac_renuncia', array(
        'type'     => 'checkbox',
        'class'    => array( 'form-row', 'toac-renuncia' ),
        'label'    => 'Solicito la descarga inmediata y reconozco que, una vez '
                    . 'descargado el temario, pierdo el derecho de desistimiento '
                    . 'de catorce días.',
        'required' => true,
    ), WC()->checkout->get_value( 'toac_renuncia' ) );
} );
```

**No es una excusa para no devolver nunca.** Si alguien compra el temario
equivocado y no lo ha descargado, devuélveselo: la tabla `wp_toac_descargas`
te dice en un segundo si lo bajó. Una devolución cuesta menos que una reseña
enfadada, y el registro te protege de quien sí abusa.

---

## 4.6 Fraude y disputas

Un producto digital de 54 € es un objetivo cómodo para tarjetas robadas: no hay
envío, la entrega es instantánea y el titular real reclama semanas después.

- **Stripe Radar** viene activado. Sube la sensibilidad los primeros meses.
- Suscríbete al evento `charge.dispute.created` del webhook y **respóndelo
  siempre**, aunque pierdas: una tasa alta de disputas sin respuesta acaba en
  el cierre de la cuenta.
- Tu mejor prueba en una disputa es el **registro de descargas**: fecha, hora,
  dirección IP y agente. Guárdalo, no lo purgues.
- Si ves varias compras seguidas con tarjetas distintas y el mismo correo, o el
  mismo comprador probando tarjetas, corta y avisa a Stripe.
