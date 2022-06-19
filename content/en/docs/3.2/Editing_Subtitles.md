---
title: Editing Subtitles
menu:
  docs:
    parent: working-with-subtitles
weight: 3000
---

Editing subtitles is what Aegisub is made for. This page will deal with basic
text editing of subtitle lines; for more information on the typography of
subtitles, see [typesetting]({{< relref "Typesetting" >}}). For information on the timing of
subtitle lines, see [working with audio]({{< relref "Audio" >}}).

## Opening subtitles

In the _File_ menu, there are four menu choices that relate to opening or
creating subtitles:

New subtitles
: Create a new, blank script (i.e. close the current file).

Open subtitles
: Open an existing subtitles file or import subtitles from a [Matroska
  container file](http://www.matroska.org).

Open subtitles with charset
: Opens subtitles but lets you choose what character set Aegisub will
  use to interpret the file. Usually not needed, but if you have a file
  in an unusual charset Aegisub will occasionally misdetect it.

Open subtitles from video
: Open the subtitles muxed into the currently open video file. This
  currently only works with Matroska video files.

Open [Autosaved Subtitles]({{< relref "Autosave" >}})
: Open a file created by Aegisub's autosave. Useful if Aegisub crashes when you
  had unsaved changes or just if you want to open an older version of a file.

When you open a subtitles file that is not detected as Unicode, Aegisub will
attempt to guess what character set it is encoded with. If it is unsure, it
will ask you to choose from two or more likely alternatives. If the result
looks garbled or otherwise incorrect, try reopening it with another character
set.

### Supported formats

Aegisub supports reading the following subtitle formats:

- Advanced Substation Alpha, also known as SSA v4+ (.ass)
- Substation Alpha v4 (.ssa)
- [SubRip](http://zuggy.wz.cz/) Text (.srt)
- MPEG4 Timed Text (limited support at best; broken at worst), also known as
  ISO/IEC 14496-17, MPEG-4 Part 17 or just TTXT (.ttxt)
- MicroDVD (.sub)
- Plain "dialog script" formatted text (see below)

### Importing subtitles from MKV

Loading subtitles directly from Matroska files can also be done. The following
CodecIDs are supported:

- S_TEXT/UTF8 (SRT)
- S_TEXT/ASS (ASS/SSA v4+)
- S_TEXT/SSA (SSA v4)

### Importing plain text scripts

Aegisub also supports importing "dialogue-formatted" plain text scripts. For example:

```plaintext
Actor 1: Well do I understand your speech, yet few strangers do so.
         Why then do you not speak in the Common Tongue,
         as is the custom in the West, if you wish to be answered?
# TL check: The above seems to be a quote from the lord of the rings, look it up later
Actor 2: What are you babbling about?
```

This will result in five subtitle lines, one being commented out. The first
three will have the actor field set to "Actor 1", and the fifth will have it
set to "Actor 2" (the comment line's actor field will be blank).

When you open a file with the extension .txt, Aegisub will ask you about what
characters it should use as the actor separator and comment starter,
respectively. In the example above, the actor separator is a colon
("`:`") and the comment starter is a hash ("`#`").

## Editing subtitles

Editing subtitles in Aegisub is done in two areas: the subtitle edit box (where
you type in or edit text) and the subtitles grid. Changes made in both the
edit box and the grid normally modify all selected lines, and not just the
line displayed in the edit box.

### The subtitles edit box

![subs_edit_box](/img/3.2/subs_edit_box.png)

The edit box is just a plain editing area with a number of associated controls.
They are:

1. Flags the line as a comment. Comment lines will not be displayed on the
   video.
1. The [style]({{< relref "Styles" >}}) used for this line.
1. The actor speaking this line. Has no actual effect on subtitle display but
   can be useful for editing purposes.
1. Effect for this line. There are a few predefined effects which can be
   applied via this field, but renderer support for them is spotty and using
   [override tags]({{< relref "ASS_Tags" >}}) is nearly always a better idea. This is commonly
   used as a metadata field for automation scripts.
1. The number of characters on the longest line of this subtitle.
1. Layer for this line. If you override positioning with an [override tag]({{< relref "ASS_Tags" >}}) so that two or more lines are displayed on top of each
   other, this field controls which one is drawn where; higher layer numbers
   are drawn on top of lower ones.
1. Start time for the line.
1. End time for the line.
1. Duration for the line. If you modify this field, the end time will be
   modified as a result.
1. Left margin for this line. 0 means use the margin specified in the
   style.
1. Right margin for this line. 0 means use the margin specified in the
   style.
1. Vertical margin for this line. 0 means use the margin specified in the
   style.
1. Inserts a bold override tag (`\b1`) at the cursor position. If the text
   is already bold, inserts a corresponding closing tag (`\b0`).
1. Inserts an italics override tag (`\i1`) at the cursor position. If the
   text is already italic, inserts a corresponding closing tag (`\i0`).
1. Inserts an underline override tag (`\u1`) at the cursor position. If the
   text is already italic, inserts a corresponding closing tag (`\u0`).
1. Inserts an strikeout override tag (`\s1`) at the cursor position. If the
   text is already italic, inserts a corresponding closing tag (`\s0`).
1. Brings up a font selection window and inserts a font face name tag
   (`\fnFontName`) with the given font name, as well as the chosen effect
   tags.
1. Brings up the [color picker]({{< relref "Colour_Picker" >}}) and lets you choose a
   color; then inserts a primary color override tag (`\c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref "Colour_Picker" >}}) and lets you choose a
   color; then inserts a secondary color override tag (`\2c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref "Colour_Picker" >}}) and lets you choose a
   color; then inserts an outline color override tag (`\3c`) with the chosen
   color at the cursor position.
1. Brings up the [color picker]({{< relref "Colour_Picker" >}}) and lets you choose a
   color; then inserts a shadow color override tag (`\4c`) with the chosen
   color at the cursor position.
1. Move to the next line, creating a new one at the end of the file if
   needed. Note that unlike in previous versions of Aegisub, changes do
   not need to be committed using this button.
1. Changes display between times and frames. Note that this does not change
   how times are actually stored in the script.

#### Show Original

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

#### Context menu

If you right-click anywhere in the edit box, you get the following menu:

![Subs_Edit_Context](/img/3.2/Subs_Edit_Context.png)

Select all, copy, cut and paste all do what you'd expect them to.

Spell checker
: If you right-click on a word that has been detected as misspelled,
  the spell checker will suggest some likely alternative. You can also
  set which language it will use for checking from this menu, or add
  words that it doesn't recognize but you know to be correctly spelled to
  the dictionary. For more information on spell checking in Aegisub, see
  the [Spell Checker]({{< relref "Spell_Checker" >}}) page.

Thesaurus
: Suggests alternative words similar to the highlighted word.

Split line
: Splits the line into two new lines at the cursor position. Preserve
  times keeps the old line's timing for both lines. Estimate times tries
  to guess where the split is based on the length of the text on each
  side of the cursor. At video frame makes the first half of the line end
  on the previous frame, and the second half start on the current frame.

### The subtitles grid

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
- To change the way [override tags]({{< relref "ASS_Tags" >}}) are displayed in the grid,
  click the "cycle through tag hiding modes" button on the toolbar.

![Subs_grid_tags](/img/3.2/Subs_grid_tags.png)

The lines have different (configurable) colors representing different
things; see the [subtitles grid section of the options page]({{< relref "Options#General\_-.3E_Subtitles_grid" >}}) for details on what the colors
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
: Open the [Paste Over]({{< relref "Paste_Over" >}}) dialog.

Delete
: Deletes the selected lines.
