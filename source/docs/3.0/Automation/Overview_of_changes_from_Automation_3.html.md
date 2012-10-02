To put it short, the changes from Automation 3 to Automation 4 are huge, almost
everything has been completely redesigned and rewritten. You should however
find that many things still work the same, and the rest work better, hopefully.

## Architectural changes  ##
These are the changes in how the scripting engine integrates with Aegisub,
i.e. how scripts are loaded and managed and not as much what happens when they
are running.

Actually, what is called Automation 4 is only the architecture described here.
When you use Automation 4 to run scripts written in Lua (and are not Automation
3 scripts) it's called Automation 4 Lua.

Automation 4 now supports "plugging in" script functionality in several
different places. Each different kind of functionality a script can support is
called a "feature". Currently this really only means the export filters
supported by Automation 3 and then macros. Export filters appear in the Export
dialogue and are intended for large batch-operations. Macros appear in the
Automation menu and are intended for smaller tasks.

Macro features can retrieve the current selection in the subtitle grid, modify
the subtitles in-line and change the selection upon return. They can also set
one or more Undo points. Last but not least, they can show dialogue boxes to
get more information from the user.

Finally, one script file can provide more than one feature, also more than one
of each kind of supported feature. A script file can also provide no features
at all, though that's not very useful.

## The Lua scripting engine  ##
The probably single biggest and most important change from Automation 3 to
Automation 4 Lua is that the Lua version has been upgraded from 5.0 to 5.1.
While there are a large number of changes between the two versions, the perhaps
most important for writing Automation 4 Lua scripts is the modulo operator that
has finally been introduced into the language. You can see more details at [the
Lua homepage](http://www.lua.org/versions.html).

The rest of the changes to Lua scripting interface can best be summed up as:
Give as much control as possible to the script and don't do any unrequested
data generation.

In more detail, these are the main points of the changes from Automation 3 to
Automation 4 Lua. They are discussed in more detail below.

* No more a fixed entry point; script entry points are instead defined with
  `register_xxx` functions
* Direct manipulation of the subtitle file rather than manipulating a large Lua
  table
* Much more direct control over the entire execution process
* Various changes in the data structures used
* More complete Unicode support in include files
* More advanced layout calculations in karaskel include file

You no longer need to name your functions anything specific. Instead, you tell
Aegisub what your entry point functions are called. What you do is register
each feature you want, using the `aegisub.register_macro` and
`aegisub.register_filter` functions. (Exception: If you use the [[karaoke
skeleton functions|Automation/Lua/Modules/karaskel.lua#karaokeskeletons]] you
do need to follow some specific naming schemes and should not register any
features.)

Instead of getting a huge table with all lines in the subtitle file, Automation
4 Lua provides your script with a "user data object" you can use to get, save
and replace lines in the subtitle file with. (This object is usually called the
_subs object_.) Using this subs object you can not only get the dialogue lines
in the subtitle file, but also manipulate the style lines and the Script Info
section. On the other hand, you are no longer given a _styles_ or _meta_ table
directly, but the karaskel include has [[a
function|Automation/Lua/Modules/karaskel.lua#karaskel.collect_head]] to extract
that information.

As a result of the direct manipulation of the subtitle file you can now do, you
also have much more control over what happens when during script execution.
Automation 3 always split the script execution up in three phases: Generate
input, run processing, read output. Using the subs object you can instead
intermix those three phases freely, or just do as usual. This is especially
convenient for macros, since they only need to touch the lines they actually
modify, rather than needing to import the entire file and having it re-read by
Aegisub when done. The skeletons provided by karaskel.lua can to an extent
automate managing the execution process.

The data structures used have also been changed to better support the more
complete subtitle file representation and to better reflect the philosophy of
doing as little as possible before requested. For example, the karaoke data
tables that were an inherent part of the line data structure in Automation 3
are no longer automatically generated, instead you use a separate function to
have them generated. If you use karaskel, you will however not need to worry
about that. The actual changes are too many to list here.

A new _[[unicode.lua|Automation/Lua/Modules/unicode.lua]]_ include file has
been introduced. This file provides a much more clean and usable interface for
manipulating UTF-8 encoded text than the old `next_utf_char` and `utf_len`
functions.

Last but not least, the text layout algorithms used in karaskel have been
improved a lot and now, among other things, support sub-pixel positioned text,
proper handling of inter-syllable spaces and an advanced furigana layout
algorithm. The furigana layout algorithm also produces data structures so
similar to syllable structures you can in effect use exactly the same code to
produce effects for both main syllables and furigana.

[[!template id=Automation_navbox]]
