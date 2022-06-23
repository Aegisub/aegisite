---
title: 自动保存
menu:
  docs:
    parent: miscellaneous
weight: 7100
---

默认情况下Aegisub每隔固定的时间就会自动保存一份当前正在编辑的字幕文件的备份(如果在这几分钟内有更改文件内容)。这些自动保存的文件可以在
`%APPDATA%\Aegisub\autosave`(Windows系统)目录下找到；
；`~/.aegisub/autosave` 目录下找到(Linux系统)；`~/Library/Application Support/Aegisub/autosave`在(OS X系统)。另外地，这些文件可以从Aegisub的
文件→ 打开自动保存的字幕 项中打开。

![autosave-menu](/img/3.2/autosave-menu.png#center)

![autosave-dialog](/img/3.2/autosave-dialog.png#center)
Aegisub会自动清除autosave文件夹下旧的文件，所以自动备份不应该被用做长期存储文件的方式。
