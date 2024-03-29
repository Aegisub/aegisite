---
title: 附件管理器
menu:
  docs:
    parent: miscellaneous
weight: 7500
---

附件管理器允许你把字体或者图片附在字幕脚本文件中(通过将它们编码为文本)。有时候用于多人共同工作的脚本上，这样生成的字幕文件和字体是一个整体，免去了小伙伴之间单独传输字体文件的麻烦。然而它的功能有限并且容易引起问题。

## 概览

![Attachment_list](/img/3.2/zh/Attachment_list.png#center)

窗口的按钮功能不言自明。两个"附加 ..."
按钮用来添加附件，"提取"用来提取已有的附件到单独的文件，"删除"会从字幕文件中删除附件。

## 局限性和缺点

### 支持的格式

SSA 格式只支持把一些特定的文件格式转化为附件。字体方面，只有.ttf得到了支持。图片方面.bmp, .gif, .ico, .jpg 和 .wmf得到了支持(并不支持.png)。SSA只有这一种方式添加附件，这个方法是很有用的。

### 兼容性问题

许多 SSA/ASS 编辑器会忽略或直接剔除附件。 原始的SubStation Alpha (v4.08)
会兼容得很好，但对于SSA文件。Sabbu(字幕软件)
会无法识别，同时会在你保存文件的时候剔除附件。大多数的其他字幕编辑器程序或忽略附件或崩溃。

一个值得注意的例外是mkvmerge，它会将附件文件在混流的过程中转化成Matroska附件。如果你再从MKV文件中提取字幕流，附件会被从字幕脚本中剔除，但是MKV文件中仍然存储着附件。

### 大小

不幸的是，存储二进制数据为文本 (顺带一提，是UUEncoding的变种)
不是十分有效率的。带附件的文件比起单独的文件会占用更多的空间。

### 速度

Aegisub 的 撤销系统会记录对当前读取文件进行的每一个操作。
通常情况下撤销操作的速度是比较快的，但是有关附件的撤销操作会极大地拖慢这个速度(由于较大的文件体积)。
