---
title: Editing Subtitles
menu:
  docs:
    parent: working-with-subtitles
weight: 3000
---

La edición de subtítulos es para qué sirve sirve Aegisub. Esta página trata de edición básica de renglones de subtítulos; para más información de tipografía de subtítulos, véase [tipografía]({{< relref path="Typesetting" lang="en" >}}). Para más información acerca de cronometrar renglones de subtítulos, véase [trabajar con audio]({{< relref path="Audio" lang="en" >}}).

## Abrir subtitles

En el menú _Archivo_ hay cuatro opciones que se relacionan con abrir o crear subtítulos:

Nuevos subtítulos
: Crear un nuevo guión en blanco (cierra el archivo actual).

Abrir subtítulos
: Abrir un archivo de subtítulos existente o importar subtítulos desde un [archivo contenedor Matroska](http://www.matroska.org).

Abrir subtítulos con charset
: Abre subtítulos pero le permite elegir el arreglo de caracteres (character set) que Aegisub usará para interpretar el archivo. Típicamente no se necesita, pero si se tiene un archivo de charset inusual, Aegisub de vez en cuando lo puede malinterpretar.

Abrir subtítulos desde video
: Abrir subtítulos multiplexados en el archivo de video actualmente abierto. Esta opción actualmente solo funciona con archivos de video Matroska.

Abrir [subtítulos autoguardados]({{< relref path="Autosave" lang="en" >}})
: Abrir un archivo creado por la función de autoguardado de Aegisub. Útil si Aegisub se cae a la vez que uno tenía cambios sin guardar, o si solo se quiere abrir una versión más antigua de un archivo.

Cuando se abre un archivo de subtítulos que no se reconoce como Unicode, Aegisub intentará adivinar con qué arreglo de caracteres de ha codificado. Si no está seguro, le pedirá que escoja entre dos o más alternativas probables. Si el resultado se ve revuelto mal o incorrecto de alguna manera, intente volver a abrirlo con otro arreglo de caracteres.

### Formatos soportados

Aegisub maneja la lectura de los formatos de subtítulos a continuación:

- Advanced Substation Alpha, alias SSA v4+ (.ass)
- Substation Alpha v4 (.ssa)
- [SubRip](http://zuggy.wz.cz/) Text (.srt)
- MPEG4 Timed Text (manejo limitado en el mejor caso; roto en el peor), alias
  ISO/IEC 14496-17, MPEG-4 Part 17 or simplemente TTXT (.ttxt)
- MicroDVD (.sub)
- Simple texto "guión diálogo" formateado (vea abajo)

### Importar subtítulos desde MKV

Importar subítulos directamente desde archivos Matroska se puede hacer. Se soportan los siguientes CodecID:

- S_TEXT/UTF8 (SRT)
- S_TEXT/ASS (ASS/SSA v4+)
- S_TEXT/SSA (SSA v4)

### Importar guiones de texto sin formato (plain text)

Aegisub también soporta la importación de guiones de texto sin formato "formato diálogo". Por ejemplo:

```plaintext
Actor 1: Pues, sí comprendo su habla, pero yo como comprenden pocos extranjeros.
         ¿Por qué no habla entonces en la Lengua común,
         según es típico en el Occidente, si desea una respuesta?
# TL check: Arriba parece ser una cita de Señor de los anillos, lo busco luego
Actor 2: ¿De qué locuras estás hablando?
```

Este resultará en cinco renglones de subtítulos, uno siendo comentario. Los primeros tres tendrán el campo de actor como "Actor 1", y el quinto lo tendrá como "Actor 2" (el actor del renglón de comentario estará en blanco).

Cuando se abre un archivo con la extensión .txt, Aegisub le pedirá qué caracteres debe usar como separador de actor e inicio de comentario, respectivamente. En el ejemplo arriba, el separador de actor es el dos puntos ("`:`") e inicio de comentario el gato ("`#`").

## Editar subtítulos

Edición de subtítulos en Aegisub se hace en dos áreas: la caja edición de subtítulos (en donde se ingresa y edita texto) y la cuadrícula de subtítulos. Cambios realizados tanto en la caja edición como la cuadrícula por lo general modifican todos los renglones seleccionados, y no solo el renglón que aparece en la caja edición.

### La caja edición de subtítulos

![subs_edit_box](/img/3.2/subs_edit_box.png)

La caja edición es sencillamente una zona en que editar texto sin formato, con una cantidad de controles asociados.
Son:

1. Marcar el renglón como comentario. Renglones de comentario no aparecerán en el video.
1. El [estilo]({{< relref lang="en" path="Styles" >}}) usado en este renglón.
1. El actor hablando en este renglón. No tiene efecto real en la muestra de subtítulos pero puede ser útil para propósitos de edición.
1. Efecto para este renglón. Har un par de efectos predefinidos que pueden ser aplicados con este campo, pero compatibilidad con renderizadores es inconsistente y usar [etiquetas manuales]({{< relref lang="en" path="ASS_Tags" >}}) es casi siempre más recomendable. Este campo se usa comunmente como metadatos para scripts automatizadas.
1. El número de caracteres en el renglón más largo del subtítulo.
1. Capa para el renglón. Si fija posiciona con una [etiqueta manual]({{< relref lang="en" path="ASS_Tags" >}}) para que dos o más renglones se muestran encima uno del otro, este campo controla cuál se dibuja dónde; números de capa mayores se dibujan encima de menores.
1. Momento de inicio del renglón.
1. Momento de fin del renglón.
1. Duración del renglón. Si se modifica, el momento final será cambiado como resultado.
1. Márgen izquierda del renglón. 0 significa usar el márgen especificado en el estilo.
1. Márgen derecha del renglón. 0 significa usar el márgen especificado en el estilo.
1. Márgen vertical del renglón. 0 significa usar el márgen especificado en el estilo.
1. Inserta una etiqueta manual **negritas** (`\b1`) en la posición del cursor. Si el texto ya está en negritas, inserta una etiqueta de cierre correspondiente (`\b0`).
1. Inserta una etiqueta manual _cursiva_ (`\i1`) en la posición del cursor. Si el texto ya está en cursiva, inserta una etiqueta de cierre correspondiente (`\i0`).
1. Inserta una etiqueta manual _subrayado_ (`\u1`) en la posición del cursor. Si el texto ya está subrayado, inserta una etiqueta de cierre correspondiente (`\u0`).
1. Inserta una etiqueta manual ~~tachado~~ (`\s1`) en la posición del cursor. Si el texto ya está tachado, inserta una etiqueta de cierre correspondiente (`\s0`).
1. Abre una ventana de elegir tipografía e inserta una etiqueta de nombre de fuente tipográfico (`\fnFontName`) con el nombre de fuente elegido, además de las elegidas etiquetas de efectos.
1. Abre el [paleta de colores]({{< relref path="Colour_Picker" lang="en" >}}) y le permite escoger un color; luego inserta una etiqueta manual de color principal (`\c`) con el color en la posición del cursor.
1. Abre la [paleta de colores]({{< relref path="Colour_Picker" lang="en" >}}) y le permite escoger un color; luego inserta una etiqueta manual de color secundario (`\2c`) con el color en la posición del cursor.
1. Abre la [paleta de colores]({{< relref path="Colour_Picker" lang="en" >}}) y le permite escoger un color; luego inserta una etiqueta manual de color de borde (`\3c`) con el color en la posición del cursor.
1. Abre la [paleta de colores]({{< relref path="Colour_Picker" lang="en" >}}) y le permite escoger un color; luego inserta una etiqueta manual de color de sombra (`\4c`) con el color en la posición del cursor.
1. Pasar al siguiente renglón, creando uno nuevo al final del archivo cuando necesario. Ojo que a diferencia de versiones previas de Aegisub, cambios no necesitan ser entregados con este botón.
1. Cambiar la vista entre tiempos/momentos y cuadros. Note que esto no afecta cómo los tiempos son realmente guardados en el guión.

#### Mostrar original

Habilitar la opción "Mostrar Original" cambia la caja edición al siguiente modo:

![subs_edit_box_original](/img/3.2/subs_edit_box_original.png)

La mitad superior de la caja edición es solo lectura, y enseña el texto que el renglón actualmente seleccionado tenía cuando por primera vez se seleccionó. Esta puede ser útil para traducir, o también sólo para editar subtítulos.

Revertir
: Reemplaza el texto de renglón con el texto enseñado en la caja superior. Es una manera sencilla de deshacer todos los cambios que se hicieron en el renglón si se cambia de idea.

Borrar
: Borrar el renglón.

Borrar texto
: Borrar el texto del renglón pero dejar en su lugar todas las etiquetas manuales. Puede ayudar con traducir letreros sobreescritos a otro idioma.

Insertar original
: Insertar el texto original del renglón en la posición del cursor.

#### Menú contexto

Si hace clic derecho en cualquier parte de la caja edición, aparece el menú siguiente:

![Subs_Edit_Context](/img/3.2/Subs_Edit_Context.png)

Seleccionar todo, copiar, cortar y pegar se portan todos igual que uno esperaría.

Corrector ortográfico
: Si se hace clic derecho en una palabra que se ha detectado como mal escrito, el corrector ortográfico sugerirá unos alternativos probables. Se puede también fijar cuál idioma usará para la corrección en este menú, o agregar palabras que no reconoce pero que uno sabe que son correctos al diccionario. Para más información acerca de la corrección ortográfica en Aegisub, véase la página del [Corrector de ortografía]({{< relref path="Spell_Checker" lang="en" >}}).

Tesauro
: Sugiere palabras alternativas similares a la palabra resaltada.

Dividir renglón
: Divide el renglón dos nuevos a la posición del cursor. "Preservar tiempos" mantiene la sincronía del renglón original para ambos renglones nuevos. "Estimar tiempos" intenta adivinar dónde/cuándo está la división basado en la longitud del texto a cada costado del cursor. "En cuadro de video" hace que la primera mitad del renglón termine en el cuadro anterior, y que la segunda mitad empiece en el cuadro actual. 

### Cuadrícula de subtítulos

![Subs_grid](/img/3.2/Subs_grid.png)

La cuadrícula de subtítulos enseña todos los renglones (comentarios y demás) en el archivo entero.

Algunos controles comunes:

- Para mover renglones arriba o abajo en la lista, selecciónelos, pulse la tecla `alt` a la vez que las teclas de mover arriba o abajo.
- Para selecionar múltiples renglones, pulse o `ctrl` o `shift`/`mayús` y haga clic. Ctrl-clic selecciona uno o más renglones por click; Mayús-clic selecciona todos los renglones entre el primero y último cliqueados.
- Para cambiar el renglón activo enseñado en la caja de edición sin cambiar la selección, pulse `alt` y haga clic en el nuevo renglón.
- Para ordenar todas las filas de la cuadrícula, abra el menú _Subtítulo_, y bajo _Ordenar renglones_ seleccione el cambio en que ordenarlas.
- Para cambiar la manera en que [etiquetas manuales]({{<relref path="ASS_Tags" lang="en">}}) se muestran en la cuadrícula, haga clic en el botón "ojear modos de ocultar etiquetas" en la barra herramientas.

![Subs_grid_tags](/img/3.2/Subs_grid_tags.png)

Los renglones tienen diferentes (configurables) colores representando cosas diferentes; véase la [sección cuadrícula de subtítulos de la página de opciones]({{<relref path="Options#General\_-.3E_Subtitles_grid" lang="en">}}) para detalles acerca de qué significan los colores.

Por defecto, las columnas siguientes son visibles:

**\#**
: El número de renglón.

Inicio
: El tiempo inicio del renglón.

Fin
: El tiempo fin del renglón.

Estilo
: El estilo usado en este renglón.

Texto
: El texto del renglón (este es lo que se verá en el video).

Las siguientes columnas serán vistas si cualquier renglón del guión las usa:

L
: La capa del renglón (véase arriba).

Actor
: El actor hablando durante el renglón.

Efecto
: El efecto de este renglón.

Izquierda
: El márgen izquierda.

Derecha
: El márgen derecha.

Vert
: El márgen vertical.

Se puede también hacer clic-derecho en la primera fila de la cuadrícula (la con los nombres de columna) para seleccionar manualmente cuáles se quiere ver.

Clic-derecho en cualquier otra fila en la cuadrícula le abre el menú siguiente
(muchas de las opciones están también disponibles en otros menúes):

![grid_context_menu](/img/3.2/grid_context_menu.png)

Insertar (antes/después)
: Inserts a new empty line before or after the selected line. The new line
  will be timed start at 0:00:00.00 and go to 0:00:05.00.

Insertar en momento de video (antes/después)
: Same as the above, but the new line will be timed to start at the current
  video frame. Not enabled unless you have video loaded.

Duplicar
: Duplicates the selected line(s).

Dividir renglones antes del cuadro actual
: Duplicate the selected line(s), set the end time of the original line
  to the frame before the current video frame, and set the start time of
  the copy to the current video frame. Useful for frame-by-frame
  typesetting and for splitting a line at a scene change to let it move
  down if it collided with a no-longer-visible line. Only enabled if you
  have video loaded.

Dividir renglones después del cuadro actual
: As above, but it splits off the portion of the line after the current
  frame rather than the potion before the current frame, for when doing
  frame-by-frame typesetting from the last to the first frame of a line.

Dividor (por karaoke)
: Splits the line into one new line per syllable, as delimited by karaoke
  override tags (`\k` and its relatives). The timing of the first line will
  start at the original line's start time and end at that time plus the
  length of the first syllable; the following lines will start at the end of
  the previous and last for the duration of the syllable.

Intercambiar
: Swaps the places (in the grid) of two selected lines.

Unir (mantener primero)
: Joins two or more lines, discarding the text of all but the first. The
  new line will be timed to start at the first line's start time and end at
  the last line's end time. Only enabled if you have more than one line
  selected.

Unir (concatenar)
: Same as above, but concatenates the text of all selected lines instead. A
  space is inserted between the texts of each source line.

Unir (como karaoke)
: Does the inverse of _Split (by karaoke)_, i.e.  the same as _Join
  (concatenate)_ but inserts `\k` tags with the timing of each source line in
  the joined line.

Hacer tiempos continuos (cambar inicio/cambiar fin)
: Modifies the timing of the selected lines so that the end time of each
  line is the same as the start time of the next line. Change start/change
  end determines whether the function changes the end time or the start time
  of each line. Only  enabled when you have more than one line selected.

Recombinar renglones
: Given two or more lines with the same text being partially present in all
  of them, creates one line per text fragment instead. This is mostly useful
  for correcting subs ripped from DVDs, which frequently look something like
  this:

  ![Recombine_01](/img/3.2/Recombine_01.png)

  After recombine lines, the result is:

  ![Recombine_02](/img/3.2/Recombine_02.png)

Crear corte de audio
: Saves a segment of the loaded audio corresponding to the timing of the
  selected lines (starting at the earliest start time and ending at the
  latest end time) as an uncompressed WAV file. Only enabled if you have
  audio loaded.

Cortar/Copiar/Pegar
: Cuts/copies/pastes entire lines. Note that the lines are copied as plain
  text and can be copied and pasted freely between text editors, chat
  programs, web browsers, other instances of Aegisub etc.

Pegar renglones encima...
: Open the [Paste Over]({{< relref path="Paste_Over" lang="en" >}}) dialog.

Eliminar
: Deletes the selected lines.
