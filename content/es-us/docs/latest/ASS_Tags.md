---
title: Etiquetas manuales ASS
menu:
  docs:
    parent: typesetting
weight: 4400
---

La siguiente es una lista de todas las etiquetas admitidas por el formato Advanced Substation Alpha. Esta es básicamente una versión detallada de `ass-quickref.txt`. Consulte el [tutorial]({{<relref path="Visual_Typesetting" lang="en">}}) para obtener una introducción a la composición tipográfica, utilizando algunas etiquetas básicas.

## Caracteres especiales

Las siguientes etiquetas están escritas en el medio del texto y no dentro de bloques de anulación (es decir, no entre { y }).

{{<tag-def-box title="Salto de línea suave" id="\n">}}\\n{{</tag-def-box>}}
Inserta un salto de línea forzado, pero solo cuando esté en el modo de salto 2. (Ver
[la etiqueta \\q]({{<relref path="ASS_Tags#\q" >}})). Fíjese que es una n minúscula.

En todos los demás modos de salto, esto se reemplaza por un espacio normal. Rara vez (o nunca) es realmente útil. Si no está seguro de si quiere esto o \\N, probablemente quiere \\N.

{{<tag-def-box title="Salto de línea duro" id="\N">}}\\N{{</tag-def-box>}}
Inserta un salto de línea forzado, independientemente del modo de ajuste. Fíjese que es una N mayúscula.

{{<tag-def-box title="Espacio duro" id="\h">}}\\h{{</tag-def-box>}}
Inserta un espacio "duro" que no se rompa. La línea nunca se dividirá automáticamente justo antes ni después de un espacio duro, y los espacios no se colapsan cuando aparecen al principio o al final de una línea dibujada.

## Etiquetas manuales

Las etiquetas manuales, o etiquetas de anulación, deben aparecer dentro de los bloques de anulación, que comienzan con { y terminan con }. Cualquier texto no reconocido dentro de los bloques de anulación se ignora silenciosamente, por lo que también se usan comúnmente para comentarios en línea. No se recomienda mezclar comentarios y etiquetas en el mismo bloque de anulación.

Las etiquetas se dividen en dos categorías generales: aquellas que establecen una propiedad de la línea misma y aquellas que modifican sólo el texto que las sigue. `\pos`, `\move`, `\clip`, `\iclip`, `\org`, `\fade` y `\fad` son de la primera categoría; todas las demás son de la segunda. Las etiquetas de la primera categoría deben aparecer como máximo una vez en una línea y no importa en qué parte de la línea aparezcan. Además, algunas de ellas son mutuamente excluyentes: `\pos` y `\move`; `\clip` y `\iclip`; `\fad` y `\fade`. El resultado de incluir varias instancias de estas etiquetas o etiquetas mutuamente excluyentes variará entre los renderizadores y no se recomienda.

Las etiquetas de la segunda categoría modifican todo el texto después de la etiqueta hasta el final de la línea o hasta que otra etiqueta vuelva a anular la propiedad.

Las etiquetas manuales siempre siguen la misma forma: comienzan con una barra invertida (backslash) \\, luego un nombre, luego el parámetro de la etiqueta después del nombre. Si se omite el parámetro, se utiliza el valor predeterminado del estilo de la línea.

Algunas etiquetas son "complejas" y aceptan más de un parámetro. En estos casos, los parámetros se colocan entre paréntesis con comas entre los parámetros.

**Nota sobre tipografía:**
En esta página, todo lo escrito en _cursiva_ rodeado por `<` corchetes angulares `>` es un parámetro y uno tiene que ingresar un valor en su lugar. Los corchetes angulares no forman parte del valor que debe ingresar. Utilice los ejemplos como guía sobre cómo se deben escribir las etiquetas. En general, se aplican las mismas reglas a todas las etiquetas en cuanto a su apariencia.

{{<tag-def-box title="Cursiva" id="\i">}}
\\i1
\\i0
{{</tag-def-box>}}
Activa o desactiva el texto en _cursiva_. Utilice `\i1` para habilitar la cursiva para el siguiente texto y `\i0` para deshabilitarla nuevamente.

{{<tag-def-box title="Negrita" id="\b">}}
\\b1
\\b0
\\b<i>\<peso></i>
{{</tag-def-box>}}
Activa o desactiva el texto en **negrita**. Utilice `\b1` para habilitar la negrita para el siguiente texto y `\b0` para desactivarla nuevamente.

La versión <code>\\b<i>\<peso></i></code> permite especificar un peso explícito para usar. Tenga en cuenta que la mayoría de las fuentes sólo admiten uno o dos pesos, por lo que rara vez necesitará utilizarlo. Los pesos de las fuentes son múltiplos de 100, de modo que 100 es el más bajo, 400 es "normal", 700 es "negrita" y 900 es el más pesado.

{{<example-box>}}

```ass
No me hace {\b1}ninguna{\b0} gracia.
```

La palabra "no" está escrita en negrita.
{{</example-box>}}

{{<example-box>}}

```ass
{\b100}¿Qué {\b300}tan {\b500}negrita {\b700}se {\b900}alcanza?
```

Las palabras se escriben con cada vez mayor peso. Tenga en cuenta que la mayoría de las fuentes no tienen más de uno o dos pesos diferentes y en ese caso solo podrá ver "sin negrita" y "negrita".
{{</example-box>}}

{{<tag-def-box title="Subrayado" id="\u">}}
\\u1
\\u0
{{</tag-def-box>}}
Activa o desactiva el texto <u>subrayado</u>. Utilice `\u1` para habilitar el subrayado en el siguiente texto y `\u0` para desactivarlo nuevamente.

{{<tag-def-box title="Tachado" id="\s">}}
\\s1
\\s0
{{</tag-def-box>}}
Activa o desactiva el texto <s>tachado</s>. Utilice `\s1` para habilitar el tachado del siguiente texto y `\s0` para desactivarlo nuevamente.

{{<tag-def-box title="Grosor de borde" id="\bord">}}\\bord<i>\<grosor></i>{{</tag-def-box>}}
Cambia el grosor del borde alrededor del texto. Fije el grosor en 0 (cero) para desactivar el borde por completo.

Si "escalar borde y sombra" (consulte [propiedades del guión]({{<relref path="Properties">}})) está habilitado, el valor se proporciona en píxeles de resolución del guión; de lo contrario, se proporciona en píxeles de resolución de vídeo (lo cual significa que el grosor del borde variará según la resolución del vídeo en la que se renderizan los subtítulos).

El valor no se limita a píxeles enteros y puede tener decimales. El grosor del borde no puede ser negativo.

{{<example-box>}}

```plaintext
\bord0
```

Deshabilitar el borde por completo.
{{</example-box>}}
{{<example-box>}}

```plaintext
\bord3.7
```

Establecer el grosor del borde en 3.7 píxeles.
{{</example-box>}}

{{<tag-def-box title="Grosor de borde (extendido)" id="\xbord">}}
\\xbord<i>\<grosor></i>
\\ybord<i>\<grosor></i>
{{</tag-def-box>}}
Utilice las etiquetas `\xbord` `\ybord` para establecer el grosor del borde en las direcciones X y Y por separado. Esto puede ser útil para corregir el tamaño del borde en caso del renderizado anamórfico de subtítulos.

Tenga en cuenta que si usa `\bord` después de `\xbord` o `\ybord` en una línea, las anulará a ambas.

Uno puede establecer el grosor del borde en 0 (cero) en una de las direcciones para desactivar completamente el borde en esa dirección.

{{<tag-def-box title="Distancia de sombra" id="\shad">}}\\shad<i>\<profundidad></i>{{</tag-def-box>}}
Establece la distancia desde el texto para posicionar la sombra. Fijar la profundidad en 0
(cero) desactiva la sombra por completo. Funciona de manera similar a [\\bord]({{<relref path="ASS_Tags#\bord">}}).

La profundidad de la sombra no puede ser negativa con esta etiqueta.

{{<tag-def-box title="Distancia de sombra (extendida)" id="\xshad">}}
\\xshad<i>\<profundidad></i>
\\yshad<i>\<profundidad></i>
{{</tag-def-box>}}
Establece la distancia desde el texto para posicionar la sombra, con las posiciones X y Y configuradas por separado. La sombra solo se desactiva si la distancia X y Y es 0.

Tenga en cuenta que, a diferencia de \\shad, puede establecer la distancia negativa con estas etiquetas para colocar la sombra arriba o izquierda del texto.

{{<tag-def-box title="Bordes borrosos" id="\be">}}
\\be0
\\be1
\\be<i>\<fuerza></i>
{{</tag-def-box>}}
Habilita o deshabilita un efecto de suavizado sutil para los bordes del texto. El efecto no siempre es muy visible, pero en algunos casos puede hacer que el texto se vea mejor. Suele ser más visible en tamaños de texto más pequeños.

Fíjese que esta etiqueta difumina solo los _bordes_ del texto, no todo. Esto significa que si el texto tiene un borde (establecido con [\\bord]({{<relref path="ASS_Tags#\bord">}})) el borde se verá borroso, pero si no hay borde, el texto principal aparecerá borroso.

En la versión extendida, _fuerza_ es la cantidad de veces que se aplica el efecto normal. Tenga en cuenta que en valores altos el efecto degenera hasta la nada y, en general, no es muy útil. Como resultado, para desenfoques fuertes, `\blur` generalmente es más útil. La _fuerza_ tiene que ser un número entero.

{{<tag-def-box title="Bordes borrosos (núcleo gaussiano)" id="\blur">}}\\blur<i>\<fuerza></i>{{</tag-def-box >}}
En general, tiene la misma función que la etiqueta [`\be`]({{<relref path="ASS_Tags#\be">}}), pero utiliza un algoritmo más avanzado que se ve mejor en niveles altos de fuerza. A diferencia de `\be`, la _fuerza_ aquí puede ser no entera. Establezca _fuerza_ en 0 (cero) para desactivar el efecto. Con cuidado, que configurar _fuerza_ demasiado alto puede requerir mucho tiempo de CPU para renderizar.

Tenga en cuenta que esta etiqueta difumina solo los _bordes_ del texto, no todo. Esto significa que si el texto tiene un borde (establecido con [`\bord`]({{<relref path="ASS_Tags#\bord">}})) el borde se verá borroso, pero si no hay borde, el texto principal aparecerá borroso.

{{<tag-def-box title="Nombre de fuente" id="\fn">}}\\fn<i>\<nombre></i>{{</tag-def-box>}}
Establece la fuente que se utilizará para el texto que sigue. No debe haber ningún espacio entre `\fn` y el nombre de la fuente, y tampoco puede poner paréntesis o algo similar alrededor del nombre de la fuente.

{{<example-box>}}

```plaintext
\fnArial
```

El texto que sigue a esta etiqueta estará en fuente Arial.
{{</example-box>}}
{{<example-box>}}

```plaintext
\fnTimes New Roman
```

El texto que sigue a esta etiqueta estará en fuente Times New Roman.
{{</example-box>}}

{{<tag-def-box title="Tamaño de fuente" id="\fs">}}\\fs<i>\<tamaño></i>{{</tag-def-box>}}
Establece el tamaño de la fuente. El tamaño especificado es la altura en píxeles de escritura, por lo que con un tamaño de fuente 40, una línea de texto tiene 40 píxeles de alto. (Nota técnica: en realidad se trata de puntos tipográficos (edición de escritorio), no de píxeles de guión, pero dado que la representación siempre se realiza a 72 DPI (según el estándar de facto), un punto termina siendo exactamente igual a un píxel de resolución de guión).

Sólo puede especificar tamaños de fuente enteros.

{{<example-box>}}

```plaintext
\fs10
```

El siguiente texto será de una fuente de tamaño 10.
{{</example-box>}}

{{<tag-def-box title="Escala de fuente" id="\fscx">}}
\\fscx<i>\<escala></i>
\\fscy<i>\<escala></i>
{{</tag-def-box>}}
Ajusta el tamaño del texto en dirección X (`\fscx` o Y (`\fscy`). La _escala_ dada está en porcentaje, por lo que 100 significa "tamaño original".

Esto no es lo mismo que configurar el tamaño de fuente, ya que configurar el tamaño está sujeto a [sugerencias de fuente](http://en.wikipedia.org/wiki/Font_hinting), mientras que escalar el texto modifica la forma del texto después de la sugerencia. Como resultado, esto siempre debe usarse con `\t` en lugar de `\fs`, ya que la animación de cambio de sugerencias para fuentes muy rara vez es deseable.

Estas etiquetas también afectan a los [dibujos vectoriales]({{<relref path="ASS_Tags#comandos-de-dibujo">}}).

Puede utilizar la escala de fuente para corregir la representación anamórfica y especificar el tamaño del texto con mayor precisión que con [\\fs]({{<relref path="ASS_Tags#\fs">}}).

Tenga en cuenta que las versiones anteriores de VSFitler redondearán abajo las escalas que no sean enteras.

{{<example-box>}}

```plaintext
\fscx150
```

Aumenta el texto un 50% más ancho de lo normal.
{{</example-box>}}
{{<example-box>}}

```plaintext
\fscy50
```

Disminuye el texto a media altura.
{{</example-box>}}
{{<example-box>}}

```plaintext
\fscx200\fscy200
```

Duplica el tamaño del texto.
{{</example-box>}}

{{<tag-def-box title="Espaciado entre letras" id="\fsp">}}\\fsp<i>\<espaciado></i>{{</tag-def-box>}}
Cambia el espacio entre las letras individuales del texto. Puede utilizar esto para separar el texto más visualmente. El _espaciado_ se proporciona en píxeles de resolución de guión.

El espaciado puede ser negativo y tener decimales.

{{<tag-def-box title="Rotación de texto" id="\frx">}}
\\frx<i>\<cantidad></i>
\\fry<i>\<cantidad></i>
\\frz<i>\<cantidad></i>
\\fr<i>\<cantidad></i>
{{</tag-def-box>}}
Gira el texto alrededor del eje X, Y o Z. La etiqueta `\fr` es un atajo para `\frz`.

- El **eje X** corre horizontalmente por la pantalla. Girando sobre él (con valores positivos) provoca un efecto con que la parte superior del texto se mete hacia "adentro" de la pantalla mientras que la parte inferior sale hacia "afuera" de la pantalla.
- El **eje Y** corre verticalmente por la pantalla. Girando sobre él (con positivo valores) hace que el texto gire de modo que la izquierda sale hacia "afuera" de la pantalla, y la derecha se mete hacia "adentro" de la pantalla.
- El **eje Z** corre perpendicular a la pantalla. Girando sobre él (con valores positivos) hace que el texto gire en 2D, en sentido antihorario (como es estándar en las matemáticas).

La _cantidad_ de rotación se da en grados matemáticos, de modo que 360 grados es una rotación completa, y rotar cualquier múltiple de 360 es lo mismo que no rotar. Se permite especificar cantidades de rotación negativas, así como cantidades mayores a 360 grados.

La rotación se realiza alrededor del punto de origen de la línea del subtítulo; esto se define con la etiqueta [\\org]({{<relref path="ASS_Tags#\org">}}).

Estas etiquetas también afectan a [dibujos vectoriales]({{<relref path="ASS_Tags#comandos-de-dibujo">}}).

{{<example-box>}}

```plaintext
\frx45
```

Gira el texto 45 grados por el eje X.
{{</example-box>}}
{{<example-box>}}

```plaintext
freír-45
```

Gira el texto 45 grados en dirección opuesta por el eje Y.
{{</example-box>}}
{{<example-box>}}

```plaintext
\frz180
```

Gira el texto 180 grados por el eje Z, dejándolo patas arriba.
{{</example-box>}}
{{<example-box>}}
Las dos rotaciones siguientes producen el mismo resultado:

```plaintext
\frz-30
\frz330
```

Esto se debe a que 330 grados son 30 grados menos que una rotación completa de 360 grados.
{{</example-box>}}
{{<example-box>}}

```plaintext
\t(\frz3600)
```

Realiza una animación donde el texto realiza 10 revoluciones completas en el eje Z. Consulte también la etiqueta [\\t]({{<relref path="ASS_Tags#\t">}}).
{{</example-box>}}
{{<example-box>}}
Los siguientes pantallazos demuestran el efecto de girar sobre los diferentes ejes:

![Fr_sample01](/img/3.2/Fr_sample01.jpg)

![Fr_sample02](/img/3.2/Fr_sample02.jpg)

![Fr_sample03](/img/3.2/Fr_sample03.jpg)
{{</example-box>}}

{{<tag-def-box title="Cizallamiento de texto" id="\fax">}}
\\fax<i>\<factor></i>
\\fay<i>\<factor></i>
{{</tag-def-box>}}
Realiza una transformación de cizallamiento (corte, transvección) del texto. Un _factor_ de 0 (cero) significa que no hay distorsión.

Por lo general, _factor_ será un número pequeño; es poco probable que los valores fuera del rango -2 a 2 produzcan resultados deseables.

El corte se realiza después de la rotación, en las coordenadas giradas. El sistema de coordenadas utilizado para el corte no se ve afectado por el [origen de rotación]({{<relref path="ASS_Tags#\org">}}).

{{<example-box>}}
![cizallamiento](/img/3.2/shearing.png)
{{</example-box>}}

{{<tag-def-box title="Codificación de fuente" id="\fe">}}\\fe<i>\<id></i>{{</tag-def-box>}}
Configura la codificación de fuente Windows utilizada para seleccionar la tabla de mapeo de fuentes utilizado para traducir puntos Unicode a índices de glifos en la fuente. Para algunas fuentes sin una tabla de mapeo Unicode, esto puede ser necesario para que funcione el texto en ciertos idiomas. Para las fuentes que tienen una tabla de mapeo Unicode, se podría usar para seleccionar variaciones regionales, como elegir el glifo correcto para un ideograma Han que sea diferente en chino simplificado, chino tradicional, japonés y coreano.

Algunos ID de codificación de fuentes comunes son:

- 0 - ANSI, Windows CP-1252 para idiomas de Europa occidental.
- 1 - Predeterminado, depende de la configuración del sistema del usuario, pero también permite que el subsistema de fuentes elija dinámicamente una tabla de mapeo diferente en algunas circunstancias.
- 2 - Símbolo, los puntos de código en el rango 0-255 se traducen a glifos de símbolos definidos por cada fuente, esto se usa para fuentes como Wingdings.
- 128 - Shift-JIS, usado para japonés.
- 129 y 130, respectivamente Hangeul y Johab, dos esquemas de codificación para coreano.
- 134 - GB2312, utilizado para chino simplificado.
- 136 - BIG5, usado para chino tradicional.
- 162 - turco.
- 163 - vietnamita.
- 177 - hebreo.
- 178 - árabe.

{{<todo>}}¿Es eso realmente correcto? {{</todo>}}

Una lista más completa se puede ver en la caja de diálogo del [editor de estilos]({{<relref path="Styles#el-editor-de-estilo">}}).

En archivos ASS almacenados en codificaciones que no son Unicode, esta etiqueta también afecta en qué página de códigos debe interpretarse el texto que le sigue. Aegisub no soporta este uso y es posible que algunos renderizadores tampoco lo admitan. Se recomienda que no confíe en esto y, en su lugar, almacene siempre sus archivos en codificación Unicode. (Aegisub almacena archivos en Unicode UTF-8 por defecto).

{{<tag-def-box title="Establecer color" id="\c">}}
\\c&H<i>\<bb>\<gg>\<rr></i>&
\\1c&H<i>\<bb>\<gg>\<rr></i>&
\\2c&H<i>\<bb>\<gg>\<rr></i>&
\\3c&H<i>\<bb>\<gg>\<rr></i>&
\\4c&H<i>\<bb>\<gg>\<rr></i>&
{{</tag-def-box>}}
Establece el color del siguiente texto. La etiqueta `\c` es una abreviatura de `\1c`.

- `\1c` establece el color de relleno principal.
- `\2c` establece el color de relleno secundario. Esto sólo se usa para pre resaltado en karaoke estándar.
- `\3c` establece el color del borde.
- `\4c` establece el color de la sombra.

Los códigos de color se dan en [hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal) en orden Azul Verde Rojo. Tenga en cuenta que este es el orden opuesto a los códigos de color HTML. Los códigos de color siempre deben comenzar con `&H` y terminar con `&`.

Los botones Seleccionar Color de la barra de herramientas ![pick-color-toolbar-buttons](/img/3.2/pick-color-toolbar-buttons.png) pueden ayudar a seleccionar colores e ingresar los códigos de color.

{{<tag-def-box title="Establecer alfa" id="\alpha">}}
\\alpha&H<i>\<aa></i>
\\1a&H<i>\<aa></i>
\\2a&H<i>\<aa></i>
\\3a&H<i>\<aa></i>
\\4a&H<i>\<aa></i>
{{</tag-def-box>}}
Establece el alfa (transparencia) del texto.

- `\alpha` establece el alfa de todos los componentes a la vez.
- `\1a` establece el alfa del relleno primario.
- `\2a` establece el alfa del relleno secundario. Esto sólo se usa para pre resaltado en karaoke estándar.
- `\3a` establece el alfa del borde.
- `\4a` establece el alfa de la sombra.

Un alfa de 00 (cero) significa opaco/completamente visible, y un alfa de FF (es decir, 255 en decimal) es completamente transparente/invisible.

{{<example-box>}}

```plaintext
\alpha&H80&
```

Fija el alfa de todos los componentes en hexadecimal 80, decimal 128, para que el texto sea 50% transparente en general.
{{</example-box>}}
{{<example-box>}}

```plaintext
\1a&HFF&
```

Fija el alfa de relleno principal en hexadecimal FF, decimal 255, para que resulte efectivamente invisible dejando solo el borde y la sombra.
{{</example-box>}}

{{<tag-def-box title="Alineación de línea" id="\an">}}\\an<i>\<pos></i>{{</tag-def-box>}}
Especifica la alineación de la línea. La alineación define la posición de la línea cuando no hay ni [anulación de posición]({{<relref path="ASS_Tags#\pos">}}) ni [movimiento]({{<relref path="ASS_Tags#\move">}}) en efecto. De lo contrario, especifica el punto de anclaje de posicionamiento y rotación.

La etiqueta `\an` usa valores del "teclado numérico" ("numpad") para _pos_. Es decir, los valores de alineación corresponden a las posiciones de los dígitos en el teclado numérico de cuadrícula:

1. Abajo izquierda
1. Abajo centro
1. Abajo derecha
1. Centro izquierda
1. Centro
1. Centro derecha
1. Arriba izquierda
1. Arriba centro
1. Arriba derecha

{{<tag-def-box title="Alineación de línea (antigua)" id="\a">}}\\a<i>\<pos></i>{{</tag-def-box>}}
Especifica la alineación de la línea utilizando códigos de alineación heredados de SubStation Alpha. Esta etiqueta es compatible pero se considera obsoleta; normalmente uno debe usar `\an` en nuevos guiones, ya que es más intuitivo.

La excepción es que `\a6` debería usarse para la traducción perezosa de signos, porque si uno va a ser holgazán ha de hacerlo bien y ahorrar la letra extra.

Calcule _pos_ de la siguiente manera: use 1 para alineación a la izquierda, 2 para alineación central y 3 para alineación a la derecha. Si quiere títulos abajo, ya está. Para títulos arriba, agregue 4 al número, y para títulos intermedios agregue 8 al número:

- 1: Bajo izquierda
- 2: Bajo centro
- 3: Bajo derecha
- 5: Arriba izquierda
- 6: Arriba centro
- 7: Arriba derecha
- 9: Centro izquierda
- 10: Centro
- 11: Centro derecha

{{<tag-def-box title="Efecto Karaoke" id="\k">}}
\\k<i>\<duración></i>
\\K<i>\<duración></i>
\\kf<i>\<duración></i>
\\ko<i>\<duración></i>
{{</tag-def-box>}}

> _Tenga en cuenta que estas etiquetas por sí solas solo crean algunos efectos muy específicos
> y todos los demás efectos se crean con una combinación de múltiples diferentes
> etiquetas._

La familia de etiquetas `\k` marca los subtítulos para efectos de karaoke especificando la duración de cada sílaba. Coloque una etiqueta `\k` antes de cada sílaba en la línea.

La _duración_ se da en centisegundos, ej. una _duración_ de 100 equivale a 1 segundo. Por lo general, uno no ingresa etiquetas `\k` manualmente, sino que utiliza herramientas de sincronización de karaoke como [modo karaoke de Aegisub]({{<relref path="Tutorials#sincronizar-karaoke">}}).

Las diferentes etiquetas `\k` crean varios efectos:

- `\k`: Antes de resaltar, la sílaba se rellena con el color y alfa secundarios. Cuando comienza la sílaba, el relleno cambia instantáneamente para usar color y alfa primarios.
- `\K` y `\kf`: Estos dos son idénticos. Tenga en cuenta que `\K` es una K mayúscula y es diferente de `\k` minúscula. El relleno de sílaba comienza en color secundario, y cuando comienza la sílaba el relleno cambia de secundario a primario con un barrido de izquierda a derecha, y el barrido termina cuando el tiempo de la sílaba termina.
- `\ko`: Similar a `\k`, excepto que antes de resaltar, el borde/contorno de la sílaba se elimina y aparece instantáneamente cuando comienza la sílaba.

_Nota: Hay una etiqueta de karaoke adicional, `\kt`, que es muy diferente a las demás. Rara vez es útil y Aegisub no soporta esa etiqueta; por lo tanto no está documentada._

{{<tag-def-box title="Estilo de salto" id="\q">}}\\q<i>\<estilo></i>{{</tag-def-box>}}

Determina cómo se aplica el salto de línea a la línea de subtítulo. Los siguientes \_estilo_s están disponibles:

- 0: Ajuste inteligente, hace que cada línea sea aproximadamente igual de larga, pero con la línea superior más ancha cuando el ancho igualado es imposible. Sólo `\N` fuerza los saltos de línea.
- 1: Ajuste de final de línea, completa la mayor cantidad de texto posible en una línea y luego salta a la siguiente línea. Sólo `\N` fuerza los saltos de línea.
- 2: Sin ajuste, las líneas anchas se extenderán más allá de los bordes de la pantalla. Tanto `\n` como `\N` fuerzan saltos de línea.
- 3: Salto/ajuste inteligente, similar al estilo 0, pero las líneas inferiores se hacen más anchas.

{{<tag-def-box title="Restablecer estilo" id="\r">}}\\r<br>\\r<i>\<estilo></i>{{</tag-def-box>}}
Restablece el estilo. Esto cancela todas las anulaciones de estilo vigentes, incluidas
[animaciones]({{<relref path="ASS_Tags#\t">}}), para todo el texto siguiente.

La primera forma que no especifica un _estilo_ restablecerá al estilo definido para toda la línea, mientras que el segundo formulario, que especifica el nombre de un _estilo_, establecerá el estilo en ese estilo específico.

{{<example-box>}}

```ass
-Hey\N{\rAlternate}-Huh?\N{\r}-Who are you?
```

Suponiendo que el estilo de línea actual es "Default", primero tiene "Hey" en el estilo predeterminado y luego sigue en la siguiente línea "Huh?" en el estilo "Alternate", y en la tercera línea el estilo se restablece a "Default" para "Who are you?"
{{</example-box>}}

{{<tag-def-box title="Fijar posición" id="\pos">}}\\pos(<i>\<X></i>,<i>\<Y></i>){{</tag-def-box>}}
Establece la posición de la línea. Las coordenadas _X_ y _Y_ deben ser números enteros y se proporcionan en el sistema de coordenadas de resolución de guión. El significado de _X_ y _Y_ cambia ligeramente dependiendo de la [alineación]({{<relref path="ASS_Tags#\an">}}).

La alineación de la línea de subtítulo se utiliza como punto de anclaje para la posición. Es decir, cuando tiene una línea con alineación arriba-izquierda, la esquina superior izquierda del subtítulo se coloca en las coordenadas dadas a `\pos`, y para la alineación abajo-centro, el centro inferior del subtítulo se coloca en las coordenadas dadas.

{{<example-box>}}
Las siguientes capturas de pantalla demuestran la forma de que la alineación afecta el posicionamiento. La cruz verde señala el punto (320,240) en el vídeo.

![Pos_sample01](/img/3.2/Pos_sample01.jpg)
![Pos_sample02](/img/3.2/Pos_sample02.jpg)
![Pos_sample03](/img/3.2/Pos_sample03.jpg)
{{</example-box>}}

{{<tag-def-box title="Movimiento" id="\move">}}
\\move(<i>\<x1</i>>,<i>\<y1</i>>,<i>\<x2</i>>,<i>\<y2</i> >)
\\move(<i>\<x1</i>>,<i>\<y1</i>>,<i>\<x2</i>>,<i>\<y2</i> >,<i>\<t1</i>>,<i>\<t2</i>>)
{{</tag-def-box>}}
La etiqueta `\move` funciona de manera similar a [`\pos`]({{<relref path="ASS_Tags#\pos">}}) en que posiciona la línea de subtítulo, la diferencia es que `\ move` hace que el subtítulo se mueva.

Las dos versiones de `\move` se diferencian en que una hace que el movimiento se produzca durante toda la duración del subtítulo, mientras que la otra especifica el tiempo durante el cual se produce el movimiento.

Las coordenadas _x1_, _y1_, _x2_ y _y2_ se dan en el sistema de coordenadas de resolución del guión, como `\pos`. El subtítulo comienza en el punto (_x1_,_y1_) y se mueve con velocidad constante por lo que termina en (_x2_,_y2_).
[Alineación]({{<relref path="ASS_Tags#\an">}}) influye en las coordenadas de movimiento de la misma manera que influye en las coordenadas `\pos`.

En la segunda versión, los tiempos _t1_ y _t2_ se dan en milisegundos (milésimas de segundo) y son relativos a la hora de inicio del subtítulo. Por ejemplo, un valor _t1_ de 1500 significa que el movimiento comienza 1,5 segundos (un segundo y medio) después de que la línea haya aparecido en pantalla. Cuando especificas tiempos para el movimiento, la posición del subtítulo es la siguiente:

1. Antes de _t1_, el subtítulo está fijado en el punto (_x1_,_y1_). 
1. Entre _t1_ y _t2_, el subtítulo se mueve con velocidad constante desde (_x1_,_y1_) a (_x2_,_y2_). 
1. Después de _t2_ el subtítulo está fijado en el punto (_x2_,_y2_).

Tenga en cuenta que es permitido que _t1_ y _t2_ especifiquen tiempos mayores que la duración de la línea, pero puede que no sea muy útil hacerlo. Especificar _t1_ y _t2_ como 0 (cero) es lo mismo que usar la primera versión de
`\ mover`; el movimiento se producirá desde el inicio de la línea hasta el fin de la línea.

Hay algunas cosas que con **`\move` no se pueden hacer**:

- No es posible realizar movimientos a velocidad no constante. El movimiento no puede, por ejemplo, comience lento y termine rápido.
- Sólo puede haber una etiqueta o de posicionamiento o de movimiento en una línea. Poniendo ambos una `\pos` y una `\move` en una misma línea no funcionarán. Tampoco funciona colocar dos o más etiquetas `\move` en una sola línea.

Si necesita hacer cualquiera de esos dos, deberá dividir el movimiento en segmentos que se realizan en líneas de subtítulos separadas. (Cómo hacer esto está fuera del alcance de esta página).

{{<example-box>}}

```plaintext
\move(100,150,300,350)
```

Cuando aparece la línea en la pantalla, el subtítulo está en (100,150). Mientras se ve el subtítulo, este se mueve a velocidad constante de manera que llegará al punto (300,350) al mismo tiempo que desaparece.
{{</example-box>}}
{{<example-box>}}

```plaintext
\move(100,150,300,350,500,1500)
```

La línea aparece en (100,150). Después de que la línea haya aparecido durante medio segundo (500 milisegundos), comienza a moverse hacia (300,350), de modo que llegará al punto un segundo y medio (1500 milisegundos) después de que la línea apareció por primera vez en la pantalla.
{{</example-box>}}

{{<tag-def-box title="Origen de rotación" id="\org">}}\\org(<i>\<X></i>,<i>\<Y></i> ){{</tag-def-box>}}
Establece el punto de origen utilizado para [rotación]({{<relref path="ASS_Tags#\frx">}}). Esto afecta a todas las rotaciones de la línea. Las coordenadas _X_ e _Y_ se proporcionan en píxeles de resolución de secuencia de comandos de números enteros.

Cuando no hay una etiqueta `\org` en una línea, el origen de rotación es implícitamente el mismo que el [punto de anclaje de posición]({{<relref path="ASS_Tags#\pos">}}). Esto significa que el origen de la rotación se moverá si la línea se mueve y no hay un origen establecido con `\org`. Tenga en cuenta que _no_ puede animar la etiqueta `\org`, está limitado a un origen fijo si la usa.

Si el origen de la rotación se coloca en el punto de fuga en una escena 3D, las rotaciones 3D de la línea de subtítulo producirán la perspectiva correcta para coincidir con la escena.

Es perfectamente posible (y en ocasiones útil) colocar el punto de origen muy fuera de la imagen real; si está lo suficientemente lejos, al realizar pequeñas rotaciones calculadas adecuadamente parecerá que el texto se mueve a lo largo de una línea recta (o casi recta) a través de la imagen. Esto es algo difícil de controlar, pero se puede utilizar para solucionar las limitaciones de formato con \\move, como la incapacidad de realizar movimientos acelerados o varios movimientos por línea.

Puede haber como máximo una etiqueta `\org` en una sola línea, si se pone más de una en una sola línea, solo se usa la primera.

{{<example-box>}}

```plaintext
\org(320,240)
```

Fija el origen de rotación en el punto (320,240).
{{</example-box>}}
{{<example-box>}}

```plaintext
\org(10000,0)
```

Colocar el origen de rotación en un punto lejano le permite utilizar una ligera
`\frz` rotaciones para producir efectos de "salto"; el texto se moverá hacia arriba o hacia abajo sin que parezca girar.
{{</example-box>}}

{{<tag-def-box title="Desvanecimiento" id="\fad">}}\\fad(<i>\<entrada></i>,<i>\<salida></i>) {{</tag-def-box>}}
Produce un efecto de aparición y desaparición gradual. Los tiempos de _entrada_ y _salida_ se dan en milisegundos; es decir, 1000 significa un segundo. Puede especificar _entrada_ o _salida_ como 0 (cero) para no tener ningún efecto de desvanecimiento en ese extremo.

Agregar un efecto de desvanecimiento no extiende la duración de la línea, sino que se usa el inicio o el final del tiempo visible de la línea para el efecto de desvanecimiento. Por esta razón, debes tener cuidado de que _entrada_+_salida_ no sea mayor que la duración de la línea. Por ejemplo, para una línea que aparece durante 4 segundos, la suma de _entrada_+_salida_ no debe ser mayor que 4000.

{{<example-box>}}

```plaintext
\fad(1200,250)
```

Aparece gradualmente la línea en los primeros 1,2 segundos que está visible y se desvanece durante el último cuarto de segundo visible.
{{</example-box>}}

{{<tag-def-box title="Desvanecimiento (complejo)" id="\fade">}}\\fade(<i>\<a1</i>>,<i>\<a2</i>>,<i>\<a3</i>>,<i>\<t1</i>>,<i>\<t2</i>>,<i>\<t3</i>> ,<i>\<t4</i>>){{</tag-def-box>}}
Realice un desvanecimiento de cinco partes utilizando tres valores alfa _a1_, _a2_ y _a3_ y cuatro tiempos _t1_, _t2_, _t3_ y _t4_.

Los valores alfa se dan en _decimal_ y están entre 0 y 255, siendo 0 completamente visible y 255 invisible. Los valores de tiempo se dan en milisegundos después del inicio de la línea. Se requieren los siete parámetros.
(Para los efectos de desvanecimiento más comunes, la etiqueta [`\fad`]({{<relref path="ASS_Tags#\fad">}}) funciona bien.)

- Antes de _t1_, la línea tiene alfa _a1_.
- Entre _t1_ y _t2_ la línea transiciona de alfa _a1_ a alfa _a2_.
- Entre _t2_ y _t3_ la línea tiene alfa _a2_ constantemente.
- Entre _t3_ y _t4_ la línea se desvanece de alfa _a2_ a alfa _a3_.
- Después de _t4_ la línea tiene alfa _a3_.

{{<example-box>}}

```plaintext
\fade(255,32,224,0,500,2000,2200)
```

Comienza invisible, se materializa hasta volverse casi totalmente opaco y luego se desvanece hasta volverse casi totalmente invisible. El primer desvanecimiento comienza cuando comienza la línea y dura 500 milisegundos. El segundo desvanecimiento comienza a los 1500 milisegundos más tarde y dura 200 milisegundos.
{{</example-box>}}

{{<tag-def-box title="Transformación animada" id="\t">}}
\\t(<i>\<estilos></i>)
\\t(<i>\<acel></i>,<i>\<estilos></i>)
\\t(<i>\<t1</i>>,<i>\<t2</i>>,<i>\<estilos></i>)
\\t(<i>\<t1</i>>,<i>\<t2</i>>,<i>\<acel></i>,<i>\<estilos></i>)
{{</tag-def-box>}}

Realiza una transformación gradual y animada de un estilo a otro. Los _estilos_ son otras etiquetas manuales como se especifica en esta referencia. Sólo un conjunto limitado de etiquetas manuales se pueden animar con `\t`:

| Fuente | Geometría | Otros efectos |
| ------- | -------- | ------------- |
| \\fs | \\fscx | \\bord |
| \\fsp | \\fscy | \\xbord |
| \\c | \\frx | \\ybord |
| \\1c | \\fry | \\shad |
| \\2c | \\frz | \\xshad |
| \\3c | \\fr | \\yshad |
| \\4c | \\fax | \\clip |
| \\alpha | \\fay | \\iclip |
| \\1a | | \\be |
| \\2a | | \\blur |
| \\3a | | |
| \\4a | | |

_Nota: Para `\clip` y `\iclip`, solo se pueden animar las versiones rectangulares. Las versiones de dibujos vectoriales no se pueden animar._

_Nota: Mezclar `\clip` y `\iclip` en etiquetas `\t` tiene resultados no deseados._

Los parámetros _t1_ y _t2_ especifican el intervalo de tiempo para realizar la transformación. En las versiones sin _t1_ y _t2_ la transformación se realiza a lo largo de toda la línea. Los tiempos se dan en milisegundos y son relativos a la hora de inicio de la línea. (Para el resto de la descripción de `\t`, se supone que _t1_ y _t2_ están especificados, o implícitamente ser respectivamente 0 y la duración de la línea).

El parámetro _acel_ se puede utilizar para hacer que la animación no sea lineal y, en su lugar, siga una curva exponencial. Un parámetro _acel_ de 1 (uno) hace que la velocidad de la animación sea lineal. Un valor entre 0 y 1 hace que la animación comience rápido y termine lento. Un valor mayor que 1 hace que la animación comience lentamente y termine rápido. (Para los amantes de las matemáticas, la función es _y_ = _x_ con _x_ ∈ \[0;1\] = (_t_-_t1_)/(_t2_-_t1_), siendo _t_ la hora actual.)

Antes de _t1_, el estilo es el que especifican todas las etiquetas antes de la etiqueta `\t`. Después de _t2_, el estilo es como todas las etiquetas antes de la etiqueta `\t` y se anula aún más por las _anulaciones de estilo_ dadas. Entre _t1_ y _t2_ el estilo se anima gradualmente entre esos dos puntos, siguiendo la función de aceleración descrita anteriormente.

{{<example-box>}}

```ass
{\1c&HFF0000&\t(\1c&H0000FF&)}¡Hola!
```

El texto comienza en azul, pero desvanece hacia el rojo, por lo que es completamente rojo cuando termina la línea.
{{</example-box>}}
{{<example-box>}}

```ass
{\an5\t(0,5000,\frz3600)}Uiii
```

Hace que el texto gire 10 veces, en sentido antihorario, con una duración de 5 segundos.
{{</example-box>}}
{{<example-box>}}

```ass
{\an5\t(0,5000,0.5,\frz3600)}Uiii
```

Igual que el anterior, pero comenzará rápido y disminuirá, aún haciendo las 10 rotaciones en 5 segundos.
{{</example-box>}}
{{<example-box>}}

```ass
{\an5\fscx0\fscy0\t(0,500,\fscx100\fscy100)}¡Bú!
```

El texto comienza con un tamaño cero, es decir, invisible, y luego crece hasta alcanzar el 100% del tamaño tanto en la dirección X como en la Y.
{{</example-box>}}

{{<tag-def-box title="Clip (rectángulo)" id="\clip">}}
\\clip(<i>\<x1</i>>,<i>\<y1</i>>,<i>\<x2</i>>,<i>\<y2</i> >)
\\iclip(<i>\<x1</i>>,<i>\<y1</i>>,<i>\<x2</i>>,<i>\<y2</i> >)
{{</tag-def-box>}}
Define un rectángulo para recortar la línea; solo la parte de la línea que está dentro del rectángulo será visible. La etiqueta `\iclip` tiene el efecto contrario: define un rectángulo donde no se ve la línea.

Las coordenadas _x1_, _y1_, _x2_ y _y2_ se dan en píxeles de resolución de guión y son relativas a la esquina superior izquierda del vídeo. Las coordenadas deben ser números enteros, no hay posibilidad de utilizar coordenadas no enteras. (Aumentar la resolución del guión no aumentará la precisión; el recorte siempre ocurre en los límites de los píxeles del video).

{{<example-box>}}

```plaintext
\clip(0,0,320,240)
```

Suponiendo una resolución de guión de 640x480, solo es visible la parte de la línea dentro del cuadrante superior izquierdo.
{{</example-box>}}
{{<example-box>}}

```plaintext
\iclip(0,0,320,240)
```

Similar a lo anterior, pero la parte de la línea dentro del cuadrante superior izquierdo está oculta.
{{</example-box>}}
{{<example-box>}}
Ejemplo de `\clip(0,0,704,245)` en un vídeo de 704x480:

![Clip_sample01](/img/3.2/Clip_sample01.jpg)
{{</example-box>}}

{{<tag-def-box title="Clip (dibujo vectorial)" id="\clip-vector">}}
\\clip(<i>\<comandos de dibujo></i>)
\\clip(<i>\<escala></i>,<i>\<comandos de dibujo></i>)
\\iclip(<i>\<comandos de dibujo></i>)
\\iclip(<i>\<escala></i>,<i>\<comandos de dibujo></i>)
{{</tag-def-box>}}
Usa la forma definida como dibujo vectorial para mostrar selectivamente (`\clip`) u ocultar (`\iclip`) partes de la línea.

Los _comandos de dibujo_ son comandos de dibujo como los que se usan con la etiqueta `\p`. Las coordenadas se dan en píxeles de resolución de guión y son relativas a la esquina superior izquierda del video.

Si la _escala_ no se especifica, se supone que es 1 (uno), lo que significa que las coordenadas corresponden directamente a los píxeles. La _escala_ funciona de la misma manera que la _escala_ para los dibujos `\p`.

A diferencia del clip rectangular, el clip de dibujo vectorial _no_ puede animarse con `\t`. Si necesita animar un clip de dibujo vectorial, debe crear varias líneas de subtítulos similares, cada una con su propio "cuadro" de la animación de recorte.

{{<example-box>}}

```plaintext
\clip(1,m 50 0 b 100 0 100 100 50 100 b 0 100 0 0 50 0)
```

Muestra solo la parte de la línea dentro del pseudocírculo definido.
{{</example-box>}}

## Etiquetas de dibujo

Advanced Substation Alpha también admite algunas etiquetas de dibujo avanzadas que le permiten dibujar con gráficos vectoriales. Cierta familiaridad con los vectores y los splines hará que la comprensión de esto sea mucho más sencilla.

### \\p\<0/1/..> - Alternar modo de dibujo

Establecer esta etiqueta en 1 o superior habilita el modo de dibujo. El texto después de esta etiqueta se interpretará como instrucciones de dibujo y no como texto realmente visible. Establecer esto en cero desactiva el modo de dibujo, restaurando el comportamiento normal. Al activarlo, el valor puede ser cualquier número entero mayor que cero y se interpretará como la escala, en modo `2^(valor-1)`. Esto se hace para permitir una precisión de subpíxeles. Ej:

```plaintext
\p1
```

(Permite dibujar con coordenadas normales)

```plaintext
\p0
```

(Desactiva el dibujo)

```plaintext
\p2
```

(Permite dibujar y la resolución se duplica. Por lo tanto, dibujar hasta 200 200 en realidad llegará a 100 100)

```plaintext
\p4
```

(Permite dibujar y la resolución es 8 veces mayor (`2^(4-1)`). Por lo tanto, dibujar a 400,400 en realidad llegará a 50,50)

### \\pbo<y> - Desplazamiento de línea base

Define el desplazamiento de la línea base para el dibujo. Esto es básicamente un desplazamiento Y para todas las coordenadas. ej:

```plaintext
\pbo-50
```

(Dibuja todo lo especificado 50 píxeles arriba)

```plaintext
\pbo100
```

(Dibuja todo lo que se especifica a 100 píxeles por debajo)

## Comandos de dibujo

Estos comandos deben aparecer en una etiqueta \\clip (versión vectorial) o entre \\p1 y \\p0, fuera de los bloques de anulación. Por ejemplo (tomado directamente de las especificaciones de ASS):

- Cuadrado:

   ```ass
   {\p1}m 0 0 l 100 0 100 100 0 100{\p0}
   ```

- Cuadrado redondeado:

   ```ass
   {\p1}m 0 0 s 100 0 100 100 0 100 c{\p0}
   ```

(c es igual a "p 0 0 100 0 100 100" en este caso)

- Círculo (casi):

   ```ass
   {\p1}m 50 0 b 100 0 100 100 50 100 b 0 100 0 0 50 0{\p0}
   ```

(tenga en cuenta que la segunda 'b' es opcional aquí)

Los comandos de dibujo utilizan el color primario para el relleno y el color de contorno para los bordes. También muestran sombra. La idea de dibujo vectorial es que hay un "cursor" invisible (considérelo como el puntero del ratón en un programa de dibujo, o como un lápiz que se mueve a través de la imagen) en el cuadro de video, y usted le indica que se mueva a otras posiciones. A medida que se mueve, dibuja el área detrás de él, y cuando cierras la línea formada, la rellena con el color primario.

### m \<x> \<y> - Mover

Mueve el cursor a x,y. Si tiene una forma abierta, se cerrará automáticamente, ya que el programa asume que ahora está dibujando una forma nueva e independiente. Todas las rutinas de dibujo deben comenzar con este comando.

### n \<x> \<y> - Mover (sin cerrar)

Mueve el cursor a x,y, sin cerrar la forma actual.

### l \<x> \<y> - Línea

Dibuja una línea desde la posición actual del cursor hasta x,y y luego mueve el cursor allí.

### b \<x1> \<y1> \<x2> \<y2> \<x3> \<y3> - Curva de Bézier cúbica

Dibuja una curva de Bézier cúbica (tercer grado) desde la posición del cursor hasta (x3,y3), utilizando (x1,y1) y (x2,y2) como puntos de control. Consulte el [artículo en Wikipedia] (http://en.wikipedia.org/wiki/B%C3%A9zier_curve) para más información sobre las curvas de Bézier. En esta imagen tomada de ese artículo, P0 es la posición del cursor, P1 es x1,y1, P2 es x2,y2 y P3 es x3,y3:

![Bézier](/img/3.2/Bezier.png)

Tenga en cuenta que la curva comienza en P0, se dirige hacia P1 y luego llega a P3 viniendo de la dirección de P2.

### s \<x1> \<y1> \<x2> \<y2> \<x3> \<y3> .. \<xN> \<yN> - B-spline cúbico

Dibuja un b-spline uniforme cúbico (de tercer grado) hasta el punto N. Este debe contener al menos 3 coordenadas (y es, en ese caso, lo mismo que b). Básicamente, esto le permite encadenar varias curvas cúbicas de Bézier. Consulta este otro artículo en Wikipedia para más información.

### p \<x> \<y> - Extender b-spline

Extiende el b-spline a x,y. Esto es esencialmente lo mismo que agregar otro par de coordenadas al final de s.

### c - Cerrar b-spline

Cierra el b-spline.

_Nota: La [herramienta de composición tipográfica de clip vectorial]({{<relref path="Visual_Typesetting#vectorial-clip" lang="en">}}) solo admite los comandos m, l y b, y puede dañar los dibujos que usan los otros comandos._
