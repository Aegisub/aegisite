---
title: 运行宏
menu:
  docs:
    parent: automation
weight: 6400
---

[自动化]({{< relref "Automation" >}})的[宏]({{< relref "../Glossary/Macro" >}})是以选项的形式出现在自动化菜单中的。

![automation_menu](/img/3.2/automation_menu.png)

通常可以使用自动化菜单中的，在分隔线前的第一个选项来打开[自动化脚本管理器]({{< relref "./Manager" >}})窗口。

分隔线以下是所有已加载宏的列表。在上面示例图中共加载了七个宏。第三个，[卡拉OK模版执行器]({{< relref "Karaoke_Templater" >}})是不可用状态，因为这个宏不能在当前的字幕文件里运行，这是因为当前字幕文件中没有卡拉OK模版行。其它的宏也可能因其他一些原因而不可用。第四个宏在[选项对话框]({{< relref "Options#hotkeys" >}})中设置了快捷键。

如果想运行一个宏，只需在自动化菜单中点击一个即可。一些宏可能还会找你要一些参数信息，还有些只会作用于所选的字幕行。当你从网上下到一个宏之后，一定要记得看一下附带的说明。
