---
title: Automation Overview
menu:
  docs:
    parent: Automation
weight: 610
---

The name **Automation** covers the entire scripting functionality of Aegisub.

## About Automation
The single purpose of Automation is — as the name implies — to automate various aspects of subtitle creation and editing.
This was originally used mainly for creating [karaoke effects]({{< relref "Glossary/Karaoke_effect" >}}), but over time it has expanded in scope to support more general purpose [macros]({{< relref "Glossary/Macro" >}}) which add arbitrary new functionaly to Aegisub.

Some of the goals of Automation:

* Macros to automate complex subtitle editing tasks
* Export filters to generate complex effects from simpler input
  * Karaoke effects
  * Translation note boxes
* Probably several yet-undiscovered uses

## Using Automation
Aegisub comes with several Automation scripts already packaged and ready to use.
This includes the advanced **[Karaoke_Templater]({{< relref "Karaoke_Templater" >}})** script and a **[collection of macros]({{< relref "Included_macros" >}})** to simplify some editing tasks.

Aegisub almost always has several Automation scripts loaded at a time.
You can see what scripts are loaded, and load/unload more from the **[Automation/Manager]({{< relref "Automation/Manager" >}})** window.

All Automation scripts also present themselves in Aegisub in one way or another.
Some appear as [macros in the Automation menu]({{< relref "Running_macros" >}}) and others appear as [filters in the Export dialog]({{< relref "Exporting" >}}).
Some scripts even appear in both places.

## Automation for programmers  ##
Automation uses [LuaJIT 2.0](http://luajit.org/) compiled in [Lua 5.2 mode](http://www.lua.org/manual/5.2/).
[MoonScript](http://www.moonscript.org) is natively supported (and in fact parts of the Aegisub libraries are written in it).

There are several example scripts included with Aegisub to give you a head start on writing your own ones.
A word of warning: Unless you are an experienced programmer the _kara-templater.lua_ script is a very bad place to start!
