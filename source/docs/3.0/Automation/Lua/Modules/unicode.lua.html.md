The `unicode.lua` include for Automation 4 Lua contains various helper
functions for working with UTF-8 encoded text.


## unicode.charwidth  ##
Synopsis: `width = unicode.charwidth(instring, index=1)`

Returns the number of bytes occupied by the UTF-8 encoded character
starting at position `index` in `instring`. The character pointed to is
assumed to be a prefix byte.

The `index` parameter is optional abd defaults to 1 (one) when left out,
meaning the width of the first character in `instring` will be returned.

## unicode.chars  ##
Synopsis: ` for char = unicode.chars(instring) do ... end`

Returns an iterator function for looping over all characters in the given
UTF-8 encoded string. For each iteration of the loop, `char` will contain a
string representing the next character in the string (which may be more
than one byte long).

## unicode.len  ##
Synopsis: `length = unicode.len(instring)`

Determine the length of the given UTF-8 encoded string.

Be aware that this function does not run in constant time, but in linear
time (O(N)) proportional to the number of Unicode characters in `instring`.


## unicode.codepoint  ##
Synopsis: `val = unicode.codepoint(instring)`

Calculate the Unicode codepoint for the first character in `instring`.

[[!template id=Automation_navbox]]
