---
title: Running macros
menu:
  docs:
    parent: Automation
weight: 650
---

[Automation]({{< relref "Automation" >}}) [macros]({{< relref "../Glossary/Macro" >}}) appear as options in the Automation
menu.

![automation_menu](/img/3.2/automation_menu.png)

The first option in the Automation menu, before the separator, always opens
the [Automation/Manager]({{< relref "./Manager" >}}) window.

Below the separator is a list of all macros loaded. In the example above
seven macros are loaded. The third, [Karaoke_Templater]({{< relref "Karaoke_Templater" >}}) is unavailable
though, because the macro has determined it can't be run on the subtitles.
In this case, because the subtitle file has no karaoke templates. Other
macros might be unavailable for other reasons. The fourth has had a hotkey
set in the [preferences dialog]({{< relref "Options#hotkeys" >}})

To run a macro, just select it from the Automation menu. Some macros might
ask you for more information, and some work only on the selected subtitle
lines. Always remember to read the documentation that came with macros you
downloaded from the Internet.
