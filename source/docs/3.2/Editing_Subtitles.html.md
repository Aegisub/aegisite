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

当你直接打开.txt文本的时候, Aegisub会分别询问用哪个字符作为区分说话人分隔符或注释开端.上方的例子中,使用了冒号(半角)
("`:`")作为说话人分隔符，用井号作为注释开端 ("`#`").

## 编辑字幕 ##
在Aegisub中有两个区域可用于编辑字幕:字幕编辑框(你打字或者编辑文本的地方)和字幕栏. 在这两处对字幕进行的更改会作用于所有选择的行，不只是出现在字幕编辑框里的那一行.

### 字幕编辑框 ###
[[img/subs_edit_box.png]]

字幕编辑框是直观的编辑区域，它带有一些附属控制功能.
它们是:

1. 将该行设为注释. 注释行不会显示在屏幕上.
1. 该行的[[样式|Styles]].
1. 该行的说话人名. 对字幕显并无影响，但是能方便编辑.
1. 该行的特效.通过该区域可以应用预定义的特效, 但渲染器的支持不够完善，使用
    [[特效标签|ASS_Tags]] 更佳. 多为了使用自动化脚本而用在元数据区域.
1. 在当前字幕行的最长行的字符数.
1. 该行的层次编号. 如果你使用了[[特效标签|ASS_Tags]]将两字幕定位重合到了一块，两行至多行都互相覆盖显示,这个区域控制这些行的    上下关系;层次编号大的行会被“拖”到层次编号小的行上方.
1. 行的开始时间.
1. 行的结束时间.
1. 行的持续时间. 如果你修改这里的数值,行的结束时间会被更改.
1. 该行的左边距. 0意味着使用样式中设置的数值.
1. 该行的右边距. 0意味着使用样式中设置的数值.
1. 该行的垂直边距. 0意味着使用样式中设置的数值.
1. 在光标位置插入“加粗”(Blod)特效标签(`\b1`). 如果文本已经被加粗, 会插入取消加粗的特效标签(`\b0`).
1. 在光标位置插入“斜体”(Italic)特效标签(`\i1`). 如果文本已经是斜体, 会插入取消斜体的特效标签(`\i0`).
1. 在光标位置插入“下划线”(Underline)特效标签(`\u1`). 如果文本已经有下划线, 会插入取消下划线的特效标签(`\u0`).
1. 在光标位置插入“删除线”(Strikeout)特效标签(`\s1`). 如果文本已经有删除线, 会插入取消删除线的特效标签(`\s0`).
1. 打开字体选择窗口，选择字体后插入一个“字体名称”特效标签(`\fnFontName`) ,其他标签也会同时插入.
1. 打开[[取色器|Colour_Picker]]选择颜色后，在光标位置插入插入一个“主要颜色”特效标签(`\c`) .
1. 打开[[取色器|Colour_Picker]]选择颜色后，在光标位置插入插入一个“次要颜色”特效标签(`\2c`) .
1. 打开[[取色器|Colour_Picker]]选择颜色后，在光标位置插入插入一个“边框颜色”特效标签(`\3c`) .
1. 打开[[取色器|Colour_Picker]]选择颜色后，在光标位置插入插入一个“阴影颜色”特效标签(`\c`) .
1. 移动到下一行, 如果需要会创建新的一行.注意，和之前版本的Aegisub不同,更改不需要被提交.
1. 改变时间的定位方式，是以时间为单位还是以帧为单位.注意，更改这项不会影响已经存储在脚本中的时间信息.

#### 显示原始字幕

“显示原始字幕”选项是把字幕编辑变成以下模式的开关:

[[img/subs_edit_box_original.png]]

上半个编辑框是只读的,显示当前行被第一次选中时的原始内容.这个功能在翻译或者编辑字幕时很有用.

还原
: 恢复下半编辑框到上半编辑框的状态.如果你改变主意了，这比撤销更快速的还原方法.

清除
: 清空该行.

清空文本
: 清空该行文本,但会留下所有的特效标签.保留排版方式的同时翻译成另一种语言.

插入原文
: 在光标处插入原文.

#### 背景菜单

如果你在编辑框的任意位置右键单击, 你会看见以下菜单:
[[img/Subs_Edit_Context.png]]

全选、复制、剪切和粘贴，基本功能应有尽有.

拼写检查器
: 如果你在一个可能拼写错了的单词上单击右键,拼写检查器会向你提供一些选项.你也可以在菜单中设置拼写检查语言,或者向字典中添加无法正确识别的单词. 想了解更多有关拼写检查器的信息, 请看
 [[拼写检查器|Spell_Checker]] 页面.

拼写检查器建议
: 提供和以选择单词接近的备选项.

分割行
:在光标处分割行. 保留原计时会生成时间一样的一行.概略计时会按照光标前后字符数量计算分割行.以视频帧会把光标前内容的结束时间设为当前帧的前一帧，光标后内容的开始时间设为当前帧.
{: class="dl-horizontal"}

### 字幕栏 ###
[[img/Subs_grid.png]]

字幕栏显示出所有行 (包括注释行和其他) 在整个文件中.

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
