---
title: unicode.lua
menu:
  docs:
    parent: lua-modules
weight: 6263
---

The `unicode` module for Automation 4 Lua contains various helper functions for working with UTF-8 encoded text.

## Usage

Import this module with {{< lua `unicode = require 'aegisub.unicode'` >}}.

## unicode.charwidth

Synopsis: {{< lua `width = unicode.charwidth(instring, index=1)` >}}

Returns the number of bytes occupied by the UTF-8 encoded code points starting at position `index` in `instring`.
The character pointed to is assumed to be a prefix byte (i.e. the first byte of the code points).

The `index` parameter is optional abd defaults to 1 (one) when left out, meaning the width of the first character in `instring` will be returned.

## unicode.chars

Synopsis: {{< lua `for char in unicode.chars(instring) do ... end` >}}

Returns an iterator function for looping over all code points in the given UTF-8 encoded string.
For each iteration of the loop, `char` will contain a string representing the next code point in the string. This string may be more than one byte long.

## unicode.len

Synopsis: {{< lua `length = unicode.len(instring)` >}}

Determine the length in code points of the given UTF-8 encoded string.

Be aware that this function does not run in constant time, but in linear time (O(N)) proportional to the number of Unicode code points in `instring`.

## unicode.codepoint

Synopsis: {{< lua `val = unicode.codepoint(instring)` >}}

Read the first unicode codepoint from `instring`.

## unicode.to_upper_case

Synopsis: {{< lua `upper = unicode.to_upper_case(instring)` >}}

Convert a string to upper case.
This function handles accents, non-latin scripts, and the like.

## unicode.to_lower_case

Synopsis: {{< lua `lower = unicode.to_lower_case(instring)` >}}

Convert a string to lower case.
This function handles accents, non-latin scripts, and the like.

## unicode.to_fold_case

Synopsis: {{< lua `folded = unicode.to_fold_case(instring)` >}}

Convert a string to fold case.
This is similar to lower case, but is locale-insensitive and gives better results for case-insensitive comparisons.
