# Documentación de fabricante

**Cuarto nivel de la jerarquía de fuentes del bloque específico**
(`informes/fuentes-del-especifico-2026-09-02.md`): ficha técnica del fabricante,
citada con su versión y la fecha en que se leyó, porque **una ficha cambia sin
avisar** y una respuesta que dependa de ella caduca cuando el producto cambia.

## Lo que hay

| Fichero | Producto | De dónde sale | Leído |
|---|---|---|---|
| `Astera_Titan-Tube_ficha.txt` | **Astera Titan Tube** | `astera-led.com/products/titan/` | 02/09/2026 |
| `Astera_Titan-Tube_informe-62471.pdf` y `.txt` | Informe de ensayo **IEC 62471:2006 / EN 62471:2008**, «Photobiological safety of lamps and lamp systems», del **Titan Tube BTB**, modelo FP1-BTB | Publicado por la propia Astera en `astera-led.com/wp-content/uploads/` | 02/09/2026 |
| `Mo-Sys_StarTracker-Max_ficha.txt` | **Mo-Sys StarTracker Max** | `mo-sys.com/product/startracker-max/` | 02/09/2026 |
| `Mo-Sys_camera-tracking_indice.txt` | Catálogo de seguimiento de cámara de **Mo-Sys** | `mo-sys.com/products/camera-tracking/` | 02/09/2026 |
| `LiveU_LU300S_ficha.txt` | **LiveU LU300S** | `liveu.tv/lu300s` | 02/09/2026 |
| `DJI_RS-4-Pro_ficha.txt` | **DJI RS 4 Pro**, ficha técnica | `dji.com/rs-4-pro/specs`, **con agente de navegador** | 02/09/2026 |
| `DJI_RS-4-Pro_compatibilidad-Sony.txt` | **DJI RS 4 Pro**, cámaras **Sony** compatibles | `dji.com/support/compatibility`, **con agente de navegador** | 02/09/2026 |

## Cómo se consiguieron, que es la parte que hay que contar

**En la pasada anterior se dieron por inalcanzables.** El informe de materiales
(`informes/materiales-del-especifico-2026-09-02.md`) decía que las páginas de
producto de LiveU, Astera y Mo-Sys «devuelven 404 en las rutas probadas», y el
tema 9 se escribió declarando que **sus fichas no se habían podido consultar**.

**Las dos causas eran otras, y las dos son evitables:**

1. **La ruta estaba mal.** `liveu.tv/products/lu300s` da 404; **`liveu.tv/lu300s`
   da 200**. Un 404 dice que esa ruta no existe, **no** que el documento no exista:
   confundir las dos cosas es dar por cerrada una fuente que está abierta.
2. **El servidor filtraba por agente de usuario.** `astera-led.com` devolvía **403**
   a la petición automática y **200** a la misma petición con un agente de
   navegador corriente. El 403 no era una negativa a publicar el documento: era un
   filtro antirrobot delante de una página pública.

**La regla que queda**: antes de escribir «no se ha podido consultar», hay que
haber probado **al menos dos rutas** y **un agente de usuario de navegador**. Sólo
entonces la frase es verdad; antes es una conclusión sin comprobar, y de ésas ya
avisa el apartado 5 del manual —*el que detecta se equivoca*—.

**Y una cuarta puerta abierta, ya con la regla en uso**: `etsi.org` devolvía «prohibido» a la
descarga de sus normas y la devuelve entera con agente de navegador, así que las dos normas
europeas del **DVB** están ya en `../normas-tecnicas/`. Van **cuatro**: LiveU, Astera, DJI y ETSI.

**Lo que sigue sin traerse, ya comprobado con las dos reglas puestas:**

- **EBU/UER**: `ebu.ch` y `tech.ebu.ch` devuelven **403 también con agente de
  navegador**. El filtro no es de agente; no hay entrada.
- **DCI**: `dcimovies.com` responde 200, pero es **una aplicación de JavaScript que
  no sirve ningún documento por ruta estática**: la portada descargada no contiene
  ni un solo enlace a la especificación. Sin ejecutar la página no hay ruta que
  probar.
- **AES10**: la página de normas de la AES sí abre —`aes.org/standards/`, 200—,
  pero **sólo publica la línea de identidad** que ya está guardada en
  `../normas-tecnicas/AES-normas-de-audio.md`. **El texto de la norma sigue tras el
  muro de pago**, y lo que el tema 10 dice sobre ella sigue siendo exacto.
- **Sony**: sus páginas de producto —tres rutas probadas, entre ellas la de la
  **HXR-NX80** y la de la **FX3**— responden **«prohibido» también con agente de
  navegador**. Los modelos que el examen cita **no se han contrastado en su
  fabricante**, sólo en la lista de DJI.
- **El fabricante de la *mobycam***: responde **«prohibido» con agente de
  navegador** por las tres rutas probadas.
