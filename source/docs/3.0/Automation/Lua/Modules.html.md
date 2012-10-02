[[!template id=toc depth=2]]

A number of Lua modules are included with Aegisub. Some of these, such as
[[karaskel.lua]] implement subtitle-specific functionality, while others
such as [[re]] fill holes in the Lua standard library.

## Using modules ##
Simply write `require "modulename"` at the top level of a script. For
example, to include the [[re]] modules, `require "re"`.

In previous versions of Aegisub, `include` was used, but this is now
deprecated as it suffers from several limitations.

To use modules in [[Karaoke Templater|Automation/Karaoke_Templater]],
place the require statement in a [[code
once|Automation/Karaoke_Templater/Code_lines_and_blocks#classesofcodelines]]
line. Note that `karaskel.lua`, `utils.lua` and `unicode.lua` do not have
to be `require`d in [[Karaoke Templater|Automation/Karaoke_Templater]], as
they are automatically imported.

## Modules reference ##

[[utils.lua]]
: An assorted collection of various utility functions which don't fit into
any coherent categories, especially for handling colours.

[[karaskel.lua]]
: The karaoke skeleton is a collection of functions mainly intended to do
text layout of timed karaoke for creating advanced karaoke effects, as well
as a number of other helper functions.

[[unicode.lua]]
: All data passed in and out of Aegisub through the Automation 4 Lua
interface are encoded in UTF-8, but Lua doesn't natively provide support
for this. A number of helper functions are provided here.

[[cleantags.lua]]
: A function to clean up ASS tags in a line.

[[clipboard]]
: Functions for copying and pasting text.

[[re]]
: Bindings for
[wxRegex](http://docs.wxwidgets.org/trunk/overview_resyntax.html), which
has full Unicode support and more features than Lua's built in regular
expression.

[[!template id=Automation_navbox]]
