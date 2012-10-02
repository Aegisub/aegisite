The Automation 4 Lua scripting engine is based on the version 5.1 series of
[the Lua scripting language](http://www.lua.org).

This manual will not deal with the Lua language itself nor the standard
libraries shipping with Lua, but only the additional functions and data
structures provided by the Aegisub Automation 4 Lua interface. Please see
[the Lua 5.1 manual](http://www.lua.org/manual/5.1/) for details on the
language itself and its standard libraries.

## General overview of the organisation of Automation 4 Lua  ##
The smallest legal Automation 4 Lua script is an empty file, but that won't
be able to do anything interesting.

There's a number of global variables a script can set to provide
information about itself. This information will be displayed in the
[[Automation/Manager]] window: `script_name`, `script_description`,
`script_author` and `script_version`.

Automation 4 Lua implements both of the currently defined "features" of
Automation 4: Macro and Export Filter. One script (one file) can define
zero, one or many of each of those features. For example, the Karaoke
Templater script defines one macro and one export filter.

When an Automation 4 Lua script is loaded, its top-level code is executed
once. You can put variable initialisations and such at the top level, but
what you usually will do is define some of the script information globals,
import some modules, write some functions that do the script's work and
then call the feature registration functions. This is described on the
**[[Registration|Automation/Lua/Registration]]** page.

When the user activates a feature from the Aegisub interface (such as by
selecting a macro from the Automation menu) the registered script function
is run. One of the parameters passed to the function is a _subtitles
object_, the primary interface to the subtitle data the script will
manipulate. To some extent, the subtitles object works as an
integer-indexed array, but it exposes some special interfaces to add,
remove and modify subtitle lines. The subtitles object allows you to access
every line in the subtitle file, including headers, style definitions,
dialogue lines and comment lines. This is described on the **[[Subtitle
file interface|Automation/Lua/Subtitle_file_interface]]** page.

Automation 4 Lua also provides a number of helper functions in the core API
for getting information on e.g. the video frame timestamps and how large a
piece of text will be when rendered with a given style.

Most things that can be implemented in clean Lua code, i.e. that don't
depend directly on Aegisub internal data structures, have been implemented
outside the core API as [[Lua modules|Modules]]. While it is possible to write
Automation 4 Lua scripts without using the provided standard include files
you will find that for anything but the simplest scripts you will need some
of the functions provided by the includes.

## The Automation 4 Lua core API  ##
Automation 4 Lua provides various APIs that can be grouped in these general
categories.

[[Script and feature registration|Automation/Lua/Registration]]
: Deals with advertising what features a script provides and a few other
script meta data.

[[Subtitle file interface|Automation/Lua/Subtitle_file_interface]]
: Deals with use of the _subtitles_ object, the principal way of accessing
and modifying the subtitle data.

[[Progress reporting and debug output|Automation/Lua/Progress_reporting]]
: providing feedback to the user while a script is running, outputting
hints and warnings to the user and printing debug information.

[[Displaying dialogue boxes and getting user input|Automation/Lua/Dialogs]]
: requesting user input during macro execution by dialogue boxes and
providing a configuration interface for export filters.

[[Miscellaneous APIs|Automation/Lua/Miscellaneous_APIs]]
: for e.g. getting the rendered size of text and getting video frame rate
information.

[[!template id=Automation_navbox]]
