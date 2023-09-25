---
title: Editing styles
menu:
  docs:
    parent: typesetting
weight: 4200
---

Un **estilo** en formato ASS es un conjunto de reglas de formato tipográfico que se aplica a las líneas de diálogo. Los parámetros de estilo se pueden anular con
[etiquetas manuales]({{<relref path="ASS_Tags" lang=en>}}); los estilos existen para que no hay que especificar todas las etiquetas en cada línea.

## El gestor de estilos

La herramienta de gestión de estilos de Aegisub (a la que se accede desde el menú Subtítulos) proporciona diversos medios para organizar, guardar y editar estilos. Se ve así:

![Style_manager](/img/3.2/Style_manager.png#center)

Como puede ver, la ventana está dividida en dos mitades. La mitad derecha muestra todos los estilos a los que actualmente tiene acceso en su secuencia de comandos actualmente cargada; la izquierda representa un almacenamiento de estilo. Aegisub utiliza almacenamientos de estilo para permitir guarda estilos y los importa rápidamente a scripts. Puedes tener tantos almacenamientos como quieras; Algunas personas prefieren mantener todos sus estilos en uno.
almacenamiento, otros clasifican sus estilos por fuente, por presentación o alfabéticamente. La gota El menú desplegable en la parte superior le permite elegir qué almacenamiento desea ver.

En la parte inferior de la ventana hay dos conjuntos de botones casi idénticos; uno configurado para el almacenamiento y otro para el script actual. Ellos son:

Nuevo
: crea un nuevo estilo, ya sea en el almacenamiento o en el script actual.

Editar
: Edite el estilo seleccionado usando el editor de estilos (ver más abajo).

Copiar
: cree una copia del estilo seleccionado y abra el editor de estilos correspondiente.

Borrar
: elimina los estilos seleccionados.

Copiar al script y copiar al almacenamiento
: Copia los estilos seleccionados entre el almacenamiento y el script actual.

Importar desde script
: Importa uno o más estilos de otro script al actual.

Al presionar Ctrl-C en el administrador de estilos se copiarán los estilos seleccionados al portapapeles como una cadena de texto. Esto también funciona al revés; puedes copiar una o más líneas de estilo de otro programa y presione Ctrl-V (pegar) en el administrador de estilos; esto los insertará en el script actual.

## El editor de estilo

Al presionar el botón "Editar" o hacer doble clic en el nombre de un estilo, aparecerá el editor de estilo, que le permite modificar todos los parámetros disponibles. **Nota**: algunos los parámetros que están disponibles como etiquetas de anulación (es decir, `\be`) _no_ están disponibles como parámetros de estilo; por el contrario, algunos parámetros que están disponibles en el editor de estilos (es decir, la opción de contorno "cuadro opaco") _no_ están disponibles como anulación de estilo. Este es un formato desafortunado y en ocasiones molesto.
limitación.

Para volver al editor de estilos:

![Editor de estilos](/img/3.2/Style_editor.png#center)

Nombre de estilo
: El nombre del estilo. No puedes tener dos estilos con el mismo nombre en el
   mismo guión.

Fuente
: Esta sección controla la configuración de fuente. El menú desplegable le permite elegir
   el tipo de letra (cualquier fuente instalada en su sistema aparecerá en esta lista) y
   el número de la derecha controla el tamaño en puntos. Las casillas de verificación a continuación configuran
   los parámetros negrita/cursiva/subrayado/tachado.

Colores
: Esto controla los cuatro colores del texto (primario, secundario, contorno y sombra).
   El significado de cada uno de ellos es el siguiente:

   **Primario:**
   El color principal de "relleno" del cuerpo del texto.

   **Secundario:**
   Color de relleno secundario, utilizado para efectos de karaoke (consulte `\k` y sus
   familiares en la [página de anulación de etiquetas]({{< relref "ASS_Tags#karaokeeffect" >}})).

   **Contorno:**
   El color del borde del texto.

   **Sombra**
   El color de la sombra, que se muestra debajo del texto principal y
   compensado por el ancho de la sombra definido a la derecha.

   Los cuatro cuadros de colores le muestran el color actual de cada uno de los cuatro textos.
   colores; al hacer clic en ellos se abre el [selector de color]({{< relref "Colour_Picker" >}}).

Márgenes
: controla qué tan cerca de los bordes del cuadro de video estará el texto.
   posicionado (y por lo tanto también cuando se activará el salto de línea automático; pero no
   tenga en cuenta que no hay opción para la justificación del texto). Cada valor (izquierda, derecha,
   vertical) se proporciona en píxeles de resolución de secuencia de comandos (consulte [propiedades de secuencia de comandos] ({{< relref "Propiedades" >}})). Para alineaciones (`\an`) 1-3, el margen vertical es
   relativo a la parte inferior del cuadro de video; para 4-6 no tiene ningún significado,
   y para 7-9 es relativo a la parte superior del cuadro de video.

Alineación
: Controla la alineación del texto. Los números corresponden a los argumentos.
   a la etiqueta `\an`. Las alineaciones 1, 4 y 7 están al ras a la izquierda; 3, 6 y 9 están al ras
   bien; 2, 5 y 8 están centrados. 1, 2 y 3 son "subtítulos" (es decir, dibujados en el
   parte inferior del marco); 4, 5 y 6 son "títulos intermedios" (es decir, ingresados verticalmente en
   el marco); 7, 8 y 9 son "títulos principales" (es decir, dibujados en la parte superior del cuadro). Hacer
   tenga en cuenta que no existe una alineación justificada; este es un formato
   limitación.

Describir
: Controla el grosor (y el estilo) del contorno (borde) y el desplazamiento de la sombra.

   - Para el contorno, el número es el grosor del borde en píxeles de escritura
     si ScaledBorderAndShadow está habilitado (consulte [propiedades del script]({{< relref "Propiedades" >}}));
     si está deshabilitado el espesor se da en píxeles de video en cambio. Configuración
     si se pone a 0 se desactiva el contorno.
   - La sombra, por otro lado, es una copia del texto principal, desplazada hacia abajo y
     hacia la derecha la distancia especificada. La distancia está en píxeles de escritura si
     ScaledBorderAndShadow está habilitado y, en caso contrario, los píxeles de vídeo. Configurarlo en
     0 desactiva la sombra.
   - Finalmente, la casilla de verificación marcada como "Cuadro opaco" controla si el contorno
     debe dibujarse como se describe arriba (lo que sucede si no está marcado), o
     reemplazado por un cuadro delimitador de fondo opaco. Tenga en cuenta que la representación de
     Los contornos de los cuadros opacos se rompen cuando la escala de fuente es diferente a
     100%.

Misceláneas
: Esta sección tiene varios otros parámetros, a saber:

   Escala X/Y
   : controla el texto que se extiende en dirección horizontal (X) y vertical (Y).
     respectivamente. El valor se da en porcentaje, por lo que 100 significa que no se realiza ningún estiramiento.
     hecho. No deberías usar esto para el tamaño de texto normal; utilizar el valor del punto
     en el área Fuente, ya que utiliza información de sugerencias de la fuente.

   Rotación
   : controla la rotación del texto. El valor es el ángulo de rotación en
     grados (360 grados a un círculo completo) y puede ser negativo o mayor que
     360 (establecerlo en 360, 720, etc. es lo mismo que configurarlo en 0, excepto por
     cuando [transformaciones animadas]({{< relref "ASS_Tags#animatedtransform" >}}) están involucradas).

   Espaciado:
   : Controla el espacio horizontal entre letras. 0 significa la fuente
     Se utilizan los valores predeterminados. Puede ser negativo para menos espacio o positivo para más.
     El valor es el espacio adicional en píxeles entre cada carácter; si
     estos son píxeles de secuencia de comandos o píxeles de video que no están bien definidos.

   Codificación:
   : controla qué página de códigos se utiliza para asignar puntos de código a glifos; Tiene
     nada que ver con la codificación de texto real del guión. Esto es sólo
     significativo en Windows usando VSFilter, donde se usa para obtener algunos elementos antiguos
     fuentes (particularmente japonesas) sin asignaciones Unicode adecuadas para renderizar
     adecuadamente. En otros sistemas y renderizadores, Freetype2 proporciona la solución adecuada.
     mapeos. Si no entendiste una palabra de lo anterior, finge esto
     La configuración no existe, ya que rara vez es importante.

   Avance:
   : Muestra una vista previa de cómo se verá el texto usando el estilo actual.
     parámetros. El campo de texto le permite ingresar texto de muestra para obtener una vista previa y
     el cuadro coloreado controla el color del fondo.
