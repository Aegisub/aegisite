  **样式** 在ASS格式中是指一套固定的字幕排版方案。样式可以在单独的行里被
[[特效标签|ASS_Tags]]覆写;由于样式的存在，你不必再单独为每一行进行排版。

## 样式管理器 ##

Aegisub的样式管理器工具 (字幕菜单下可找到) 提供了多种多样的方式以便组织保存和编辑字幕样式，它看起来是这个样子:

[[img/Style_manager.png]]{: class="center"}

如你所见, 窗口被分为两半。右半窗口显示的是目前脚本所有可用的样式;左半窗口显示的是样式库中的样式。样式库的存在是为了方便您从其他字幕文件中快速导入样式到当前字幕文件中。 你想建立多少个样式库就可以建多少个（译者注：目前版已知bug，样式库名称不能含有中文）; 一些人喜欢把他们使用的样式都存在一个样式库中,其他人喜欢按照字体、外观或者首字母顺序存储样式库。 通过顶部的下拉菜单可以切换样式库，样式库内容显示在左半窗口。

在底部有两排几乎一样的按钮;一排用于样式库，一排用于当前脚本。它们是:

新建
: 新建样式,在样式库或当前脚本中皆可.

编辑
: 在样式编辑器(见下方)编辑已选择的样式。

复制
: 建立已选样式的副本，同时会打开样式编辑器窗口.

删除
: 删除已选的样式(可多选).

复制到当前脚本和复制到样式库
: 在当前脚本和样式库之间复制已选的样式。

从脚本中导入
: 从其它脚本中导入样式到当前脚本。

在样式管理器中按 Ctrl-C 会复制已选的样式(可多选)到剪切板（文本形式）。你可以在另一个脚本的样式管理器按 Ctrl-V (粘贴)，此举会导入你刚才复制的样式到当前脚本。

## 样式编辑器 ##

按"编辑"按钮或双击一个样式的名称，会打开样式编辑器窗口,在这里你可以调整所有可调节的参数. **注意**: 一些参数是以特效标签的形式存在的 (如 `\be`) ，它们 _并不是_ 样式参数;反过来, 一些样式编辑器中的参数也_没有_相应的特效标签相对应 (如"不透明背景"边框选项)。这是一个不幸且偶然的缺陷。

接着说样式编辑器:

[[img/Style_editor.png]]{: class="center"}

样式名称
: 样式的名称. 在一栏中两个样式的名称不能重复.

字体
: 这部分控制着字体。下拉菜单允许你选择系统中所有已经安装的字体，右边的数字用于控制字的大小(字号)。下方的复选框可以调节加粗/斜体/下划线/删除线参数。

Colors
: This controls the four text colors (primary, secondary, outline and shadow).
The meaning of each of them is as follows:

    Primary
    : The main "fill" color of the body of the text.

    Secondary
    : Secondary fill color, used for karaoke effects (see `\k` and its
    relatives on the [[override tags page|ASS_Tags#karaokeeffect]]).

    Outline
    : The border color of the text.

    Shadow
    : The color of the shadow, which is displayed under the main text and
    offset by the shadow width defined to the right.
    {: .horizontal-narrow }

    The four colored boxes show you the current color for each of the four text
    colors; clicking on them opens the [[color picker|Colour_Picker]].

Margins
: Controls how close to the borders of the video frame the text will be
positioned (and hence also when automatic line breaking will kick in; but do
note that there is no option for text justification). Each value (left, right,
vertical) is given in script resolution pixels (see [[script
properties|Properties]]). For alignments (`\an`) 1-3, the vertical margin is
relative to the bottom of the video frame; for 4-6 it doesn't have any meaning,
and for 7-9 it is relative to the top of the video frame.

Alignment
: Controls the alignment of the text. The numbers correspond to the arguments
to the `\an` tag. Alignments 1, 4 and 7 are flush left; 3, 6 and 9 are flush
right; 2, 5 and 8 are centered. 1, 2 and 3 are "subtitles" (i.e. drawn at the
bottom of the frame); 4, 5 and 6 are "midtitles" (i.e.  entered vertically on
the frame); 7, 8 and 9 are "toptitles" (i.e. drawn at the top of the frame). Do
note that there is no such thing as a justified alignment; this is a format
limitation.

Outline
: Controls the outline (border) thickness (and style) and the shadow offset.

  * For the outline, the number is the thickness of the border in script pixels
    if ScaledBorderAndShadow is enabled (see [[script properties|Properties]]);
    if it is disabled the thickness is given in video pixels instead. Setting
    it to 0 disables the outline.
  * The shadow on the other hand is a copy of the main text, shifted down and
    to the right the specified distance. The distance is in script pixels if
    ScaledBorderAndShadow is enabled, and video pixels otherwise. Setting it to
    0 disables shadow.
  * Finally, the check box marked "Opaque box" controls whether the outline
    should be drawn as described above (which happens if it is unticked), or
    replaced by an opaque background bounding box. Note that the rendering of
    Opaque box outlines is broken when the font scale is anything other than
    100%.

Miscellaneous
: This section has various other parameters, namely:

    Scale X/Y
    : Controls text stretching in the horizontal (X) and vertical (Y) direction
    respectively. The value is given in percent, so 100 means no stretching is
    done. You should not use this for normal text sizing; use the point value
    in the Font area instead since that uses hinting information from the font.

    Rotation
    : Controls rotation of the text. The value is the angle of the rotation in
    degrees (360 degrees to a full circle) and may be negative or larger than
    360 (setting it to 360, 720 etc. is the same as setting it to 0 except for
    when [[animated transforms|ASS_Tags#animatedtransform]] are involved).

    Spacing
    : Controls the horizontal spacing between letters. 0 means the font
    defaults are used. May be negative for less spacing, or positive for more.
    The value is the additional gap in pixels between each character; whether
    these are script pixels or video pixels is not well defined.

    Encoding
    : Controls which codepage is used to map codepoints to glyphs; it has
    nothing to do with the actual text encoding of the script. This is only
    meaningful on Windows using VSFilter, where it is used to get some old
    (particularly Japanese) fonts without proper Unicode mappings to render
    properly. On other systems and renderers, Freetype2 provides the proper
    mappings. If you didn't understand a word of the above, pretend this
    setting doesn't exist, as it is rarely important.

    Preview
    : Shows a preview of what the text will look like using the current style
    parameters. The text field lets you input some sample text to preview, and
    the colored box controls the color of the background.
    {: .horizontal-narrow}
{: .dl-horizontal}
