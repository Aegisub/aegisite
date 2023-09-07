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

La caja edición es sencillamente una zona en que editar texto sin formato un una cantidad de controles asociados.
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
1. Inserta una etiqueta manual **negrita** (`\b1`) en la posición del cursor. Si el texto ya está en negritas, inserta una etiqueta de cierre correspondiente (`\b0`).
1. Inserta una etiqueta manual _cursiva_ (`\i1`) en la posición del cursor. Si el texto ya está en cursiva, inserta una etiqueta de cierre correspondiente (`\i0`).
1. Inserta una etiqueta **subrayo** (`\u1`) en la posición del cursor. Si el texto ya está subrayado, inserta una etiqueta de cierre correspondiente (`\u0`).
1. Inserts an strikeout override tag (`\s1`) at the cursor position. If the
   text is already italic, inserts a corresponding closing tag (`\s0`).
1. Brings up a font selection window and inserts a font face name tag
   (`\fnFontName`) with the given font name, as well as the chosen effect
   tags.
1. Brings up the [color picker]({{< relref path="Colour_Picker" lang="en" >}}) and lets you choose a
   color; then inserts a primary color override tag (`\c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref path="Colour_Picker" lang="en" >}}) and lets you choose a
   color; then inserts a secondary color override tag (`\2c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref path="Colour_Picker" lang="en" >}}) and lets you choose a
   color; then inserts an outline color override tag (`\3c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref path="Colour_Picker" lang="en" >}}) and lets you choose a
   color; then inserts a shadow color override tag (`\4c`) with the chosen
   color at the cursor position.
1. Move to the next line, creating a new one at the end of the file if
   needed. Note that unlike in previous versions of Aegisub, changes do
   not need to be committed using this button.
1. Changes display between times and frames. Note that this does not change
   how times are actually stored in the script.

#### Mostrar original

Checking the Show Original box switches the edit box to the following mode:

![subs_edit_box_original](/img/3.2/subs_edit_box_original.png)

The top half of the edit box is read-only, and show the text that the currently
selected line had when it was first selected. This can be useful for
translating subtitles into another language, or just for editing subtitles.

Revert
: Replace the text of the line with the text shown in the upper box. A simple
  way to undo all the changes you made to the line if you change your mind.

Clear
: Clear the line.

Clear Text
: Clear the text of the line, but leave all override tags in place. Can help
  with translating typeset signs to another language.

Insert Original
: Insert the original text of the line at the cursor position.

#### Menú contexto

If you right-click anywhere in the edit box, you get the following menu:

![Subs_Edit_Context](/img/3.2/Subs_Edit_Context.png)

Select all, copy, cut and paste all do what you'd expect them to.

Spell checker
: If you right-click on a word that has been detected as misspelled,
  the spell checker will suggest some likely alternative. You can also
  set which language it will use for checking from this menu, or add
  words that it doesn't recognize but you know to be correctly spelled to
  the dictionary. For more information on spell checking in Aegisub, see
  the [Spell Checker]({{< relref path="Spell_Checker" lang="en" >}}) page.

Thesaurus
: Suggests alternative words similar to the highlighted word.

Split line
: Splits the line into two new lines at the cursor position. Preserve
  times keeps the old line's timing for both lines. Estimate times tries
  to guess where the split is based on the length of the text on each
  side of the cursor. At video frame makes the first half of the line end
  on the previous frame, and the second half start on the current frame.

### Cuadrícula de subtítulos

![Subs_grid](/img/3.2/Subs_grid.png)

The subtitles grid shows all lines (comments and otherwise) in the entire
file.

Some common controls:

- To move lines up or down in the grid, select them, hold down the Alt key
  and press the up- or down-arrow keys.
- To select multiple lines, hold down either Ctrl or Shift and click.
  Ctrl-click selects one more line per click; Shift-click selects all the
  lines between the first clicked and the last clicked.
- To change the active line shown in the edit box without changing the
  selection, hold down alt and click on the new line.
- To sort all lines in the grid, open the _Subtitle_ menu, and under _Sort
  Lines_ select the field to sort the lines on.
- To change the way [override tags]({{< relref path="ASS_Tags" lang="en" >}}) are displayed in the grid,
  click the "cycle through tag hiding modes" button on the toolbar.

![Subs_grid_tags](/img/3.2/Subs_grid_tags.png)

The lines have different (configurable) colors representing different
things; see the [subtitles grid section of the options page]({{< relref lang="en" path="Options#General\_-.3E_Subtitles_grid" >}}) for details on what the colors
mean.

By default, the following columns are visible:

**\#**
: The line number.

Start
: The start time of the line.

End
: The end time of the line.

Style
: The style used for this line.

Text
: The text of the line (this is what will be displayed on the video).

The following columns will be displayed if any line in the script uses them:

L
: The layer of the line (see above).

Actor
: The actor speaking the line.

Effect
: The effect for this line.

Left
: The left margin.

Right
: The right margin.

Vert
: The vertical margin.

You can also right-click the top line of the grid (the one with the column
names) to manually select which columns you want to be visible.

Right-clicking any other line in the grid gives you the following menu
(many of the options are also available in other menus):

![grid_context_menu](/img/3.2/grid_context_menu.png)

Insert (before/after)
: Inserts a new empty line before or after the selected line. The new line
  will be timed start at 0:00:00.00 and go to 0:00:05.00.

Insert at video time (before/after)
: Same as the above, but the new line will be timed to start at the current
  video frame. Not enabled unless you have video loaded.

Duplicate
: Duplicates the selected line(s).

Split lines before current frame
: Duplicate the selected line(s), set the end time of the original line
  to the frame before the current video frame, and set the start time of
  the copy to the current video frame. Useful for frame-by-frame
  typesetting and for splitting a line at a scene change to let it move
  down if it collided with a no-longer-visible line. Only enabled if you
  have video loaded.

Split lines after current frame
: As above, but it splits off the portion of the line after the current
  frame rather than the potion before the current frame, for when doing
  frame-by-frame typesetting from the last to the first frame of a line.

Split (by karaoke)
: Splits the line into one new line per syllable, as delimited by karaoke
  override tags (`\k` and its relatives). The timing of the first line will
  start at the original line's start time and end at that time plus the
  length of the first syllable; the following lines will start at the end of
  the previous and last for the duration of the syllable.

Swap
: Swaps the places (in the grid) of two selected lines.

Join (keep first)
: Joins two or more lines, discarding the text of all but the first. The
  new line will be timed to start at the first line's start time and end at
  the last line's end time. Only enabled if you have more than one line
  selected.

Join (concatenate)
: Same as above, but concatenates the text of all selected lines instead. A
  space is inserted between the texts of each source line.

Join (as karaoke)
: Does the inverse of _Split (by karaoke)_, i.e.  the same as _Join
  (concatenate)_ but inserts `\k` tags with the timing of each source line in
  the joined line.

Make times continuous (change start/change end)
: Modifies the timing of the selected lines so that the end time of each
  line is the same as the start time of the next line. Change start/change
  end determines whether the function changes the end time or the start time
  of each line. Only  enabled when you have more than one line selected.

Recombine lines
: Given two or more lines with the same text being partially present in all
  of them, creates one line per text fragment instead. This is mostly useful
  for correcting subs ripped from DVDs, which frequently look something like
  this:

  ![Recombine_01](/img/3.2/Recombine_01.png)

  After recombine lines, the result is:

  ![Recombine_02](/img/3.2/Recombine_02.png)

Create audio clip
: Saves a segment of the loaded audio corresponding to the timing of the
  selected lines (starting at the earliest start time and ending at the
  latest end time) as an uncompressed WAV file. Only enabled if you have
  audio loaded.

Cut/Copy/Paste
: Cuts/copies/pastes entire lines. Note that the lines are copied as plain
  text and can be copied and pasted freely between text editors, chat
  programs, web browsers, other instances of Aegisub etc.

Paste Lines Over...
: Open the [Paste Over]({{< relref path="Paste_Over" lang="en" >}}) dialog.

Delete
: Deletes the selected lines.
