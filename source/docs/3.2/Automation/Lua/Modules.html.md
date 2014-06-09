{::options toc_levels="2,3" /}

A number of Lua modules are included with Aegisub.
Some of these, such as [[karaskel.lua]] implement subtitle-specific functionality, while others such as [[re]] fill holes in the Lua standard library.

## Using modules ##
Simply write `modulename = require 'aegisub.modulename'` at the top level of a script.
For example, to include the [[re]] modules, `re = require 'aegisub.re'`.

Note that if you look at older scripts you will probably see several other methods for including modules, such as `include`.
These have been deprecated in favor of following the modern lua module style introduced with Lua 5.2.

To use modules in [[Karaoke Templater|Automation/Karaoke_Templater]], place the require statement in a [[code once|Automation/Karaoke_Templater/Code_lines_and_blocks#classesofcodelines]] line.
Note that `karaskel.lua`, `utils.lua` and `unicode.lua` do not have to be `require`d in [[Karaoke Templater|Automation/Karaoke_Templater]], as they are automatically imported.

## Modules reference ##

[[util]]
: An assorted collection of various utility functions which don't fit into any coherent categories, especially for handling colours.

[[karaskel.lua]]
: The karaoke skeleton is a collection of functions mainly intended to do
text layout of timed karaoke for creating advanced karaoke effects, as well
as a number of other helper functions.

[[unicode]]
: All data passed in and out of Aegisub through the Automation 4 Lua interface are encoded in UTF-8, but Lua doesn't natively provide support for this.
Several helper functions are provided here.

[[cleantags.lua]]
: A function to clean up ASS tags in a line.

[[clipboard]]
: Functions for copying and pasting text.

[[re]]
: Bindings for ICU regular expressions via [boost.regex](http://www.boost.org/doc/libs/1_53_0/libs/regex/doc/html/index.html), which has full Unicode support and more features than Lua's built in regular expression.

{::template name="automation_navbox" /}
