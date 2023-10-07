---
title: Propiedades de guión
menu:
  docs:
    parent: miscellaneous
weight: 7300
---

Las **propiedades de guión** son unas cabeceras y otras opciones que afectan el guión entero de varias maneras. Se pueden acceder a través del menú _Archivo_ -> _Propiedades_.

![Propiedades](/img/3.2/Properties.png#center)

Las propiedades son:

- **Título**, **Guión original**, **Traducción**, **Edición**, **Sicronización**, **Punto de sinc**, **Cambiado por** y **Detalles de cambios** - Estas son solo de propósitos informacionales y no afectan el renderizado de ninguna manera. Fíjelas en valores apropiados si a uno le parecen útiles.

- **Resolución**, **Matriz YCbCr**, **Escala de contorno y sombra** - Consulte la página [Resolución de guión]({{<relref path="Script_Resolution" lang="en">}}) para el significado de estas opciones.

- **Estilo de salto** - Controla cómo el renderizador de subtítulos mete saltos en renglones demasiado largos como para caber en una sola línea. Los modos son:

  - 0 - El modo por defecto. Salto "inteligente"; si un renglón es demasiado largo como para caber en una línea por sí sola, se divide en dos líneas más o menos uniformes, pero prefiere que la línea superior sea más ancha. `\N` (N mayúscula) se puede usar para insertar un salto de línea manual.
  - 1 - Inserta un salto de línea cuando el renglón llega a los bordes del marco (menos márgenes); es decir, si es solo una palabra demasiado larga para caber en una línea por sí sola, la última palabra se baja sola a la línea inferior. Casi nunca es útil. Al igual que con 0, `\N` se puede utilizar para saltos de línea manuales.
  - 2 - Sin ajuste de línea automático; si un renglón es demasiado largo para caber dentro del marco del video, simplemente continuará fuera del marco. `\n` y `\N` se pueden usar para insertar saltos de línea manuales.
  - 3 - Igual que el modo 0, pero prefiere que la línea inferior sea más ancha. Tenga en cuenta que durante mucho tiempo la implementación de esto por parte de VSFilter tuvo errores y, a veces, insertaba líneas en blanco adicionales o tenía líneas con una sola palabra.

El modo de salto debería ser 0 siempre.
Modo 2 a veces es útil para renglones largos que se deslizan con animación o tienen saltos manuales, pero es mejor ajustarlo a nivel renglón con la etiqueta [\\q]({{<relref path="ASS_Tags#\\q" lang="en">}}).
