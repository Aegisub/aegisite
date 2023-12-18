---
title: Editar estilos
menu:
  docs:
    parent: typesetting
weight: 4200
---

Un **style** en formato ASS es un conjunto de reglas de estilo tipográfico que se aplica a las líneas de diálogo. Los parámetros de estilo se pueden anular con
[etiquetas manuales]({{<relref path="ASS_Tags">}}); los estilos existen para que no hay que especificar todas las etiquetas en cada línea.

## El gestor de estilos

La herramienta de gestión de estilos de Aegisub (que se accede desde el menú Subtítulos) proporciona diversos medios para organizar, guardar y editar estilos. Se ve así:

![Style_manager](/img/3.2/Style_manager.png#center)

Como puede ver, la ventana está dividida en dos mitades. La mitad derecha muestra todos los estilos actualmente accesibles desde el guion actualmente cargado; la izquierda representa un almacén de estilo. Aegisub utiliza almacenes de estilo para permitir guardar estilos e importarlos rápidamente en guiones. Uno puede tener tantos almacenes como quiera; algunos prefieren mantener todos sus estilos en un mismo almacén, otros clasifican sus estilos por fuente, por serie o por orden alfabético. El menú desplegable en la parte superior le permite elegir qué almacen ver.

En la parte inferior de la ventana hay dos conjuntos de botones casi idénticos; uno para el almacén y otro para el guion actual. Los botones son:

Nuevo
: Crear un nuevo estilo, o en el almacén o en el guion actual.

Editar
: Editar el estilo seleccionado usando el editor de estilos (véase abajo).

Copiar
: Crear una copia del estilo seleccionado y abrir su editor de estilo.

Borrar
: Eliminar los estilos seleccionados.

Copiar al guion y copiar al almacén
: Copiar estilos seleccionados entre el almacén y el guion actual.

Importar desde guion
: Importar uno o varios estilos desde otro guion hasta el actual.

Al presionar Ctrl-C en el gestor de estilos se copiarán los estilos seleccionados al portapapeles como cadena de texto. Esto también funciona al revés; se puede copiar una o más líneas de estilo desde otro programa y usar Ctrl-V (pegar) dentro del gestor de estilos, lo cual los insertará en el guion actual.

## El editor de estilo

Al presionar el botón "Editar" o hacer doble clic en el nombre de un estilo, aparecerá el editor de estilo, que le permite modificar todos los parámetros disponibles. **Ojo**: algunos de los parámetros que están disponibles como etiquetas manuales (ej. `\be`) _no_ están disponibles como parámetros de estilo; por la otra mano, algunos parámetros que están disponibles en el editor de estilos (ej. la opción de contorno "cuadro opaco") _no_ están disponibles para etiquetas manuales. Este es una desafortunada y a veces molesta limitación del formato.

Volviendo al editor de estilos:

![Editor de estilos](/img/3.2/Style_editor.png#center)

Nombre de estilo
: El nombre del estilo. No se puede tener dos estilos con el mismo nombre en el mismo guion.

Fuente
: Esta sección controla la configuración de fuente tipográfica. El menú desplegable le permite elegir el tipo de letra (cualquier fuente instalada en su sistema aparecerá en esta lista) y el número de la derecha controla el tamaño en puntos. Las casillas de opciones abajo configuran los parámetros negrita/cursiva/subrayado/tachado.

Colores
: Esto controla los cuatro colores del texto (primario, secundario, contorno y sombra). El significado de cada uno de ellos es el siguiente:

   **Primario:**
   El color principal de "relleno" del cuerpo del texto.

   **Secundario:**
   Color de relleno secundario, utilizado para efectos de karaoke (consulte `\k` y sus parecidos en la [página de etiquetas manuales]({{<relref path="ASS_Tags#\k">}})).

   **Contorno:**
   El color del borde del texto.

   **Sombra**
   El color de la sombra, que se muestra debajo del texto principal y desplazado por el ancho de la sombra definido a la derecha.

   Los cuatro cuadros de colores le muestran el color actual de cada uno de los cuatro colores de texto; al hacer clic en ellos se abre el [selector de color]({{<relref path="Colour_Picker" lang="en">}}).

Márgenes
: Controla qué tan cerca de los bordes del marco de video estará el texto posicionado (y por lo tanto también cuándo se activará el salto de línea automático; pero tenga en cuenta que no hay opción para la justificación del texto). Cada valor (izquierda, derecha, vertical) se proporciona en píxeles de resolución de guion (consulte [propiedades de guion] ({{<relref path="Properties">}})). Para alineaciones (`\an`) 1-3, el margen vertical es relativo al pie del marco de video; para 4-6 no tiene ningún significado, y para 7-9 es relativo a la cima del marco de video.

Alineación
: Controla la alineación del texto. Los números corresponden a los argumentos a la etiqueta `\an`. Las alineaciones 1, 4 y 7 están al ras a la izquierda; 3, 6 y 9 están al ras a la derecha; 2, 5 y 8 están centrados. 1, 2 y 3 son "subtítulos" (es decir, dibujados abajo en el marco); 4, 5 y 6 son "títulos intermedios" (es decir, centrados verticalmente en el marco); 7, 8 y 9 son "sobretítulos" (es decir, dibujados arriba en el marco). Tenga en cuenta que no existe tal cosa como la alineación justificada; esta es una limitación del formato.

Contorno
: Controla el grosor (y el estilo) del contorno (borde) y el desplazamiento de la sombra.

   - Para el contorno, el número es el grosor del borde en píxeles de guion si ScaledBorderAndShadow está habilitado (consulte [propiedades del guion]({{<relref path="Properties">}})); si está deshabilitado el grosor se da en píxeles de video en cambio. Fijarlo en 0 desactiva el contorno.
   - La sombra, por otro lado, es una copia del texto principal, desplazada hacia abajo derecha por la distancia especificada. La distancia está en píxeles de guion si ScaledBorderAndShadow está habilitado y, en caso contrario, en píxeles de vídeo. Fijarlo en 0 desactiva la sombra.
   - Finalmente, la casilla de opción etiquetada como "Cuadro opaco" controla si el contorno debe dibujarse como se describe arriba (lo que sucede si no está habilitada), o reemplazado por un cuadro delimitador de fondo opaco. Tenga en cuenta que la representación de los contornos de cuadros opacos se quiebra cuando la escala de fuente es diferente a 100%.

Otro
: Esta sección tiene varios otros parámetros enumerados:

   Escala X/Y
   : Controla el estirado del texto en dirección horizontal (X) y vertical (Y) respectivamente. El valor se da como porcentaje, así que 100 significa que no se estira nada. No se debería usar esto para el ajuste de tamaño de texto; utilice mejor el valor de punto en la zona Fuente, ya que ese utiliza información indicativa de la fuente misma.

   Rotación
   : Controla la rotación del texto. El valor es el ángulo de rotación en grados (360 grados en un círculo completo) y puede ser negativo o mayor que 360 (establecerlo en 360, 720, etc. es lo mismo que configurarlo en 0, excepto por cuando están involucradas las [transformaciones animadas]({{<relref path="ASS_Tags#\t">}})).

   Espaciado:
   : Controla el espacio horizontal entre letras. 0 significa que se usan los valores predeterminados del tipo de letra. Puede ser negativo para menos espacio o positivo para más. El valor es la brecha adicional en píxeles entre cada carácter; si estos son píxeles de guion o píxeles de video no está definido con precisión.

   Codificación:
   : Controla qué página de códigos se utiliza para mapear puntos de código a glifos. No tiene nada que ver con la codificación de texto del guion. Esto es sólo significativo en Windows usando VSFilter, donde se usa para que algunas fuentes antiguas (particularmente japonesas) sin asignaciones Unicode debidas se rendericen adecuadamente. En otros sistemas y renderizadores, Freetype2 proporciona el mapeo adecuado. Si no entendió ni una palabra de lo anterior, finja como que esta configuración no exista, ya que rara vez es importante.

   Vista previa:
   : Muestra una vista previa de cómo se verá el texto usando los parámetros de estilo actuales. El campo de texto le permite ingresar texto de muestra para ensayar de vista previa y el cuadro coloreado controla el color de fondo.
   