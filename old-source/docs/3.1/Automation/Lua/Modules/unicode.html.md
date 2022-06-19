The `unicode` module for Automation 4 Lua contains various helper functions for working with UTF-8 encoded text.

## Usage ##
Import this module with `unicode = require 'aegisub.unicode'`{:.language-lua}.

## unicode.charwidth  ##
Synopsis: `width = unicode.charwidth(instring, index=1)`{:.language-lua}

Returns the number of bytes occupied by the UTF-8 encoded code points starting at position `index` in `instring`.
The character pointed to is assumed to be a prefix byte (i.e. the first byte of the code points).

The `index` parameter is optional abd defaults to 1 (one) when left out, meaning the width of the first character in `instring` will be returned.

## unicode.chars  ##
Synopsis: `for char in unicode.chars(instring) do ... end`{:.language-lua}

Returns an iterator function for looping over all code points in the given UTF-8 encoded string.
For each iteration of the loop, `char` will contain a string representing the next code point in the string. This string may be more than one byte long.

## unicode.len  ##
Synopsis: `length = unicode.len(instring)`{:.language-lua}

Determine the length in code points of the given UTF-8 encoded string.

Be aware that this function does not run in constant time, but in linear time (O(N)) proportional to the number of Unicode code points in `instring`.


## unicode.codepoint  ##
Synopsis: `val = unicode.codepoint(instring)`{:.language-lua}

Read the first unicode codepoint from `instring`.

{::template name="automation_navbox" /}
