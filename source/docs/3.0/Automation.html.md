The name **Automation** covers the entire scripting functionality of Aegisub.

## About Automation  ##
The single purpose of Automation is — as the name implies — to automate various
aspects of subtitle creation and editing. To date this has mainly been for
creating [[karaoke effects|Glossary/Karaoke_effect]] but Aegisub 2 introduces
[[Automation 4|Sidebar/History_of_Automation]] which also allows creating more
general purpose [[macros|Glossary/Macro]] and also changing the style
definitions and other meta data for the subtitles.

Some of the goals of Automation:

* Macros to automate complex subtitle editing tasks
* Export filters to generate complex effects from simpler input
  * Karaoke effects
  * Translation note boxes
* Probably several yet-undiscovered uses

## Using Automation  ##
Aegisub comes with several Automation scripts already packaged and ready to
use. This includes the advanced **[[Karaoke_Templater]]** script (which covers
everything _simple-k-replacer_, _line-per-syllable_ and _multi-template_ did in
Automation 3) and a **[[collection of macros|Included_macros]]** to
simplify some editing tasks.

Aegisub almost always has several Automation scripts loaded at a time. You can
see what scripts are loaded, and load/unload more from the
**[[Automation/Manager]]** window.

All Automation scripts also present themselves in Aegisub in one way or
another. Some appear as [[macros in the Automation
menu|Running_macros]] and others appear as [[filters in the Export
dialog|Exporting]]. Some scripts even appear in both places.

## Automation for programmers  ##
Automation supports scripts in [Lua 5.1](http://www.lua.org). Other languages
used to be supported, but no one used them.

There is several example scripts included with Aegisub to give you a head start
on writing your own ones. A word of warning: Unless you are an experienced
programmer the _kara-templater.lua_ script is a very bad place to start!

The Automation 3 scripting interface used in Aegisub 1.10 and earlier is no
longer supported. If you have previous experience with writing Automation 3
scripts, there is an **[[overview_of_changes_from_Automation_3]]**.

### Future goals  ###
In future versions of Aegisub (perhaps 3.1), Automation will be replaced with a
backwards-compatible scripting interface to the full capabilities of Aegisub,
rather than being limited to merely manipulating subtitle files.

[[!template id=Automation_navbox]]
