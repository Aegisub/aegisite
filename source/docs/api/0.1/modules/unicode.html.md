The `unicode` module contains some basic functions for working with UTF-8
encoded text. All of the `unicode` functions assume that the input is a
well-formed UTF-8 string (which should be the case for any strings supplied by
Aegisub, but may not be the case for files you read yourself).

Import this module with `local unicode = require 'aegisub.unicode'`{:.language-lua}.

## Functions

{::function name='charwidth' synopsis='width = unicode.charwidth(instring, index=1)'}
Returns the number of bytes occupied by the UTF-8 encoded code point starting
at position `index` in `instring`. The character pointed to is assumed to be a
prefix byte (i.e. the first byte of the code point).

The `index` parameter is optional and defaults to 1 (one) when left out,
meaning the width of the first character in `instring` will be returned.
{:/function}

{::function name='chars' synopsis='for char = unicode.chars(instring) do ... end'}
Returns an iterator function for looping over all code points in the given
UTF-8 encoded string. For each iteration of the loop, `char` will contain a
string representing the next code point in the string (which may be more than
one byte long).
{:/function}

{::function name='len' synopsis='length = unicode.len(instring)'}
Determine the length in code points of the given UTF-8 encoded string.

Be aware that this function does not run in constant time, but in linear time
(O(N)) proportional to the number of Unicode code points in `instring`.
{:/function}

{::function name='codepoint' synopsis='val = unicode.codepoint(instring)'}
Read the first unicode codepoint from `instring` as a number.
{:/function}
