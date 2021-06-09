
A number of Lua modules are included with Aegisub.
Some of these, such as [`karaskel.lua`]({{< relref "karaskel.lua.md" >}}) implement subtitle-specific functionality, while others such as [re]({{< relref "re" >}}) fill holes in the Lua standard library.

## Using modules ##
Simply write `modulename = require 'aegisub.modulename'` at the top level of a script.
For example, to include the [re]({{< relref "re" >}}) modules, `re = require 'aegisub.re'`.

Note that if you look at older scripts you will probably see several other methods for including modules, such as `include`.
These have been deprecated in favor of following the modern lua module style introduced with Lua 5.2.

To use modules in [Karaoke Templater|Automation/Karaoke_Templater]], place the require statement in a [[code once]({{< relref "../Karaoke_Templater/Code_lines_and_blocks#classesofcodelines" >}}) line.
Note that `karaskel.lua`, `utils.lua` and `unicode.lua` do not have to be `require`d in [Karaoke Templater]({{< relref "../Karaoke_Templater" >}}), as they are automatically imported.

## Modules reference ##

[util]({{< relref "Modules/util" >}})
: An assorted collection of various utility functions which don't fit into any coherent categories, especially for handling colours.

[`karaskel.lua`]({{< relref "Modules/karaskel.lua.md" >}})
: The karaoke skeleton is a collection of functions mainly intended to do
text layout of timed karaoke for creating advanced karaoke effects, as well
as a number of other helper functions.

[unicode]({{< relref "Modules/unicode" >}})
: All data passed in and out of Aegisub through the Automation 4 Lua interface are encoded in UTF-8, but Lua doesn't natively provide support for this.
Several helper functions are provided here.

[`cleantags.lua`](#)
: A function to clean up ASS tags in a line.

[clipboard]({{< relref "Modules/clipboard" >}})
: Functions for copying and pasting text.

[re]({{< relref "Modules/re" >}})
: Bindings for ICU regular expressions via [boost.regex](http://www.boost.org/doc/libs/1_53_0/libs/regex/doc/html/index.html), which has full Unicode support and more features than Lua's built in regular expression.

[lpeg](http://www.inf.puc-rio.br/~roberto/lpeg/)
: PEG library for writing parsers.

[luabins](https://github.com/agladysh/luabins)
: A serialization library for saving tables to extradata or config files

[lfs](http://keplerproject.github.io/luafilesystem/)
: Some assorted filesystem functionality not supported by the Lua standard library.

{::template name="automation_navbox" /}
