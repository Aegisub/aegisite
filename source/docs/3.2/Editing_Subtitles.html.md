{::options toc_levels="2,3" /}

开发Aegisub是为了编辑字幕. 本页面会讲述字幕中的基本文本编辑; 若想了解更多关于字幕排版的信息, 请看[[排版|Typesetting]].有关字幕时间的编辑，请看[[载入音频|Audio]].

## 打开字幕 ##

在 _文件_ 菜单中, 有四种方式用来打开或创建字幕:

新建字幕
: 建立一个新的,空白的字幕脚本 (同时也会关闭当前文件).

打开字幕
: 打开一个现有的字幕文件，或者从其他容器如[Matroska
container file](http://www.matroska.org)中导入字幕文件.

打开字幕并指定编码
: 打开字幕的同时允许指定编码，Aegisub将以该编码读取字幕文件. 通常不需要这么做,但如果你有不常编码的字幕文件，Aegisub可能会无法正常读取它.

从视频中打开字幕
: 打开封装在视频文件中的字幕. 这个方式目前只在Matroska视频文件中有效.

打开自动保存的字幕 [[自动保存的字幕|Autosave]]
: 打开由Aegisub自动保存功能生成的字幕. 这一项很有用，尤其是编辑字幕忘记保存而Aegisub崩溃时，或者你当想查看字幕文件的历史版本时.
{: class="horizontal-wide"}

当你打开一个不是以Unicode方式编码的字幕文件时, Aegisub将会试图猜测它的编码方式.如无法确认,Aegisub将会要求你从可能的选项中选择编码.如果打开的结果是乱码或者有其他形式的错误,请尝试以其他编码方式重新打开文件.

### 支持的格式 ###
Aegisub支持读取以下字幕格式:

* Advanced Substation Alpha, 也称 SSA v4+ (.ass)
* Substation Alpha v4 (.ssa)
* [SubRip](http://zuggy.wz.cz/) 文本 (.srt)
* MPEG4 Timed Text (最佳可能兼容，也有可能支持不佳而崩溃), 也称
  ISO/IEC 14496-17, MPEG-4 Part 17 or just TTXT (.ttxt)
* MicroDVD (.sub)
* 明显的"对话脚本"格式的文本 (见下方)

### 从MKV中读取字幕 ###
可以直接从Matroska文件中读取字幕.以下CodecIDs被支持:

* S_TEXT/UTF8 (SRT)
* S_TEXT/ASS (ASS/SSA v4+)
* S_TEXT/SSA (SSA v4)

### 导入明显的对话文字 ###
Aegisub也支持导入"对话格式"的文本.例如:

    Actor 1: Well do I understand your speech, yet few strangers do so.
             Why then do you not speak in the Common Tongue,
             as is the custom in the West, if you wish to be answered?
    # TL check: The above seems to be a quote from the lord of the rings, look it up later
    Actor 2: What are you babbling about?

导入该文本将会产生5行字幕,其中一是注释. 前三行说话人被设置为 "Actor 1", 第五行说话人被设置为 "Actor 2" (注释行的说话人栏为空白).

当你直接打开.txt文本的时候, Aegisub会询问用哪个字符作为区分说话注释的
characters it should use as the actor separator and comment starter,
respectively. In the example above, the actor separator is a colon
("`:`") and the comment starter is a hash ("`#`").

## Editing subtitles ##
Editing subtitles in Aegisub is done in two areas: the subtitle edit box (where
you type in or edit text) and the subtitles grid. Changes made in both the
edit box and the grid normally modify all selected lines, and not just the
line displayed in the edit box.

### The subtitles edit box ###
[[img/subs_edit_box.png]]

The edit box is just a plain editing area with a number of associated controls.
They are:

1. Flags the line as a comment. Comment lines will not be displayed on the
    video.
1. The [[style|Styles]] used for this line.
1. The actor speaking this line. Has no actual effect on subtitle display but
    can be useful for editing purposes.
1. Effect for this line. There are a few predefined effects which can be
    applied via this field, but renderer support for them is spotty and using
    [[override tags|ASS_Tags]] is nearly always a better idea. This is commonly
    used as a metadata field for automation scripts.
1. The number of characters on the longest line of this subtitle.
1. Layer for this line. If you override positioning with an [[override
    tag|ASS_Tags]] so that two or more lines are displayed on top of each
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
1. Brings up the [[color picker|Colour_Picker]] and lets you choose a
    color; then inserts a primary color override tag (`\c`) with the chosen
    color at the cursor position.
1. Brings up the [[color picker|Colour_Picker]] and lets you choose a
    color; then inserts a secondary color override tag (`\2c`) with the chosen
    color at the cursor position.
1. Brings up the [[color picker|Colour_Picker]] and lets you choose a
    color; then inserts an outline color override tag (`\3c`) with the chosen
    color at the cursor position.
1. Brings up the [[color picker|Colour_Picker]] and lets you choose a
    color; then inserts a shadow color override tag (`\4c`) with the chosen
    color at the cursor position.
1. Move to the next line, creating a new one at the end of the file if
    needed. Note that unlike in previous versions of Aegisub, changes do
    not need to be committed using this button.
1. Changes display between times and frames. Note that this does not change
    how times are actually stored in the script.

#### Show Original

Checking the Show Original box switches the edit box to the following mode:

[[img/subs_edit_box_original.png]]

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
[[img/Subs_Edit_Context.png]]

Select all, copy, cut and paste all do what you'd expect them to.

Spell checker
: If you right-click on a word that has been detected as misspelled,
the spell checker will suggest some likely alternative. You can also
set which language it will use for checking from this menu, or add
words that it doesn't recognize but you know to be correctly spelled to
the dictionary. For more information on spell checking in Aegisub, see
the [[Spell Checker|Spell_Checker]] page.

Thesaurus
: Suggests alternative words similar to the highlighted word.

Split line
: Splits the line into two new lines at the cursor position. Preserve
times keeps the old line's timing for both lines. Estimate times tries
to guess where the split is based on the length of the text on each
side of the cursor. At video frame makes the first half of the line end
on the previous frame, and the second half start on the current frame.
{: class="dl-horizontal"}

### The subtitles grid ###
[[img/Subs_grid.png]]

The subtitles grid shows all lines (comments and otherwise) in the entire
file.

Some common controls:

* To move lines up or down in the grid, select them, hold down the Alt key
  and press the up- or down-arrow keys.
* To select multiple lines, hold down either Ctrl or Shift and click.
  Ctrl-click selects one more line per click; Shift-click selects all the
  lines between the first clicked and the last clicked.
* To change the active line shown in the edit box without changing the
  selection, hold down alt and click on the new line.
* To sort all lines in the grid, open the _Subtitle_ menu, and under _Sort
  Lines_ select the field to sort the lines on.
* To change the way [[override tags|ASS_Tags]] are displayed in the grid,
  click the "cycle through tag hiding modes" button on the toolbar.

[[img/Subs_grid_tags.png]]

The lines have different (configurable) colors representing different
things; see the [[subtitles grid section of the options
page|Options#General_-.3E_Subtitles_grid]] for details on what the colors
mean.

By default, the following columns are visible:

**#**
: The line number.

Start
: The start time of the line.

End
: The end time of the line.

Style
: The style used for this line.

Text
: The text of the line (this is what will be displayed on the video).
{: class="horizontal-narrow"}

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
{: class="horizontal-narrow"}

You can also right-click the top line of the grid (the one with the column
names) to manually select which columns you want to be visible.

Right-clicking any other line in the grid gives you the following menu
(many of the options are also available in other menus):

[[img/grid_context_menu.png]]

**Insert (before/after)**
: Inserts a new empty line before or after the selected line. The new line
will be timed start at 0:00:00.00 and go to 0:00:05.00.

**Insert at video time (before/after)**
: Same as the above, but the new line will be timed to start at the current
video frame. Not enabled unless you have video loaded.

**Duplicate**
: Duplicates the selected line(s).

**Split lines before current frame**
: Duplicate the selected line(s), set the end time of the original line
to the frame before the current video frame, and set the start time of
the copy to the current video frame. Useful for frame-by-frame
typesetting and for splitting a line at a scene change to let it move
down if it collided with a no-longer-visible line. Only enabled if you
have video loaded.

**Split lines after current frame**
: As above, but it splits off the portion of the line after the current
frame rather than the potion before the current frame, for when doing
frame-by-frame typesetting from the last to the first frame of a line.

**Split (by karaoke)**
: Splits the line into one new line per syllable, as delimited by karaoke
override tags (`\k` and its relatives). The timing of the first line will
start at the original line's start time and end at that time plus the
length of the first syllable; the following lines will start at the end of
the previous and last for the duration of the syllable.

**Swap**
: Swaps the places (in the grid) of two selected lines.

**Join (keep first)**
: Joins two or more lines, discarding the text of all but the first. The
new line will be timed to start at the first line's start time and end at
the last line's end time. Only enabled if you have more than one line
selected.

**Join (concatenate)**
: Same as above, but concatenates the text of all selected lines instead. A
space is inserted between the texts of each source line.

**Join (as karaoke)**
: Does the inverse of _Split (by karaoke)_, i.e.  the same as _Join
(concatenate)_ but inserts `\k` tags with the timing of each source line in
the joined line.

**Make times continuous (change start/change end)**
: Modifies the timing of the selected lines so that the end time of each
line is the same as the start time of the next line. Change start/change
end determines whether the function changes the end time or the start time
of each line. Only  enabled when you have more than one line selected.

**Recombine lines**
: Given two or more lines with the same text being partially present in all
of them, creates one line per text fragment instead. This is mostly useful
for correcting subs ripped from DVDs, which frequently look something like
this:

    [[img/Recombine_01.png]]

    After recombine lines, the result is:

    [[img/Recombine_02.png]]

**Create audio clip**
: Saves a segment of the loaded audio corresponding to the timing of the
selected lines (starting at the earliest start time and ending at the
latest end time) as an uncompressed WAV file. Only enabled if you have
audio loaded.

**Cut/Copy/Paste**
: Cuts/copies/pastes entire lines. Note that the lines are copied as plain
text and can be copied and pasted freely between text editors, chat
programs, web browsers, other instances of Aegisub etc.

**Paste Lines Over...**
: Open the [[Paste Over]] dialog.

**Delete**
: Deletes the selected lines.
