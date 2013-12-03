The `unicode` module contains some basic functions for working with UTF-8
encoded text. All of the `unicode` functions assume that the input is a
well-formed UTF-8 string (which should be the case for any strings supplied by
Aegisub, but may not be the case for files you read yourself).

Import this module with `local unicode = require 'aegisub.unicode'`{:.language-lua}.

## Iterators

{::function name='codepoints' synopsis='for codepoint = unicode.codepoints(str) do ... end'}
Returns an iterator function for looping over all code points in the given UTF-8 encoded string.
For each iteration of the loop, `codepoint` will contain a number representing the next code point in the string.
{:/function}

{::function name='chars' synopsis='for char = unicode.chars(str) do ... end'}
Returns an iterator function for looping over all characters in the given UTF-8 encoded string.
For each iteration of the loop, `char` will contain a string representing the next character in the string.
This string may be (much) more than one byte long.

See [Forms of Unicode](http://www.icu-project.org/docs/papers/forms_of_unicode/)
for an overview of the difference between code points and characters.
{:/function}

{::function name='words' synopsis='for word = unicode.words(str) do ... end'}
Returns an iterator function for looping over all words in the given UTF-8 encoded string.
{:/function}

{::function name='lines' synopsis='for line = unicode.lines(str) do ... end'}
Returns an iterator function for looping over all lines in the given UTF-8 encoded string.
Both Unix and Windows newlines are supported.
{:/function}

## Case Conversion

{::function name='to_upper' synopsis='uppercased = unicode.to_upper(str)'}
Convert a string to uppercase.
Unlike Lua's built-in `string.upper`, this supports non-ASCII characters.
{:/function}

{::function name='to_lower' synopsis='lowercased = unicode.to_lower(str)'}
Convert a string to lowercase.
Unlike Lua's built-in `string.lower`, this supports non-ASCII characters.
{:/function}

{::function name='fold_case' synopsis='lowercased = unicode.to_lower(str)'}
Perform Unicode case folding.
This is similar to converting to lowercase, but is locale-insensitive and is lossier.
Case folding should be used for case-insensitive string comparisons.
{:/function}

## Misc

{::function name='width' synopsis='width = unicode.width(string, index=1)'}
Returns the number of bytes occupied by the UTF-8 encoded code point starting
at position `index` in `string`. The character pointed to is assumed to be a
prefix byte (i.e. the first byte of the code point).

The `index` parameter is optional and defaults to 1 (one) when left out,
meaning the width of the first character in `string` will be returned.
{:/function}

{::function name='len' synopsis='length = unicode.len(str)'}
Get the length in code points of the given UTF-8 encoded string.

Be aware that this function does not run in constant time, but in linear time
(O(N)) proportional to the number of Unicode code points in `str`.
{:/function}

{::function name='codepoint' synopsis='val = unicode.codepoint(str)'}
Read the first unicode codepoint from `str` as a number.
{:/function}
