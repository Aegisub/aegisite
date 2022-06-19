---
title: utils.lua
menu:
  docs:
    parent: lua-modules
weight: 6262
---

The Automation 4 Lua include file `utils.lua` contains various support functions to aid writing Lua scripts.
There is no general theme for the file.

## Usage

Import this module with {{< lua `util = require 'aegisub.util'` >}}

## Table functions

Duplicating tables in various ways is a common task.
`util` provides some functions to handle the most common cases.

### copy

Synopsis: {{< lua `newtable = util.copy(oldtable)` >}}

Makes a shallow copy of the table passed as parameter.
Shallow here means that it does not dive into contained tables and copy those as well.
For example, if `oldtable.st` refers to a table, `newtable.st` will refer to the same table, and changes made to `newtable.st` will also be reflected in `oldtable.st` and vice versa.

### deep_copy

Synopsis: {{< lua `newtable = util.deep_copy(oldtable)` >}}

Makes a deep copy of the table passed as parameter.
While this function attempts to handle circular references and not do infinite recursion on them, it might not work in all cases.
You will rarely need to use this function.
If you think you need to do a deep copy, consider your task an extra time.

## Colour functions

It is often useful to do various transformations on colour data. Several
functions for this are included.

### ass_color

Synopsis: {{< lua `colorstring = util.ass_color(r, g, b)` >}}

Makes an ASS colour string in the form `&HBBGGRR` from the given `r`, `g` and `b` arguments.

Warning: The arguments are not checked for range.
Values outside the 0..255 range will produce garbage output.

### ass_alpha

Synopsis: {{< lua `alphastring = util.ass_alpha(a)` >}}

Makes an ASS alpha string in the form `&HAA&` from the given `a` argument.

Does not check input range.

### ass_style_color

Synopsis: {{< lua `colorstring = util.ass_style_color(r, g, b, a)` >}}

Makes an ASS colour string suitable for use in Style definitions, i.e. in format `&HAABBGGRR`.

Does not check input range.

### extract_color

Synopsis: {{< lua `r, g, b, a = util.extract_color(colorstring)` >}}

Extracts colour components from a colour string. Several formats of colour strings are recognised:

- Style definition: `&HAABBGGRR`
- Inline override: `&HBBGGRR&`
- Alpha override: `&HAA&`
- HTML with alpha: `#RRGGBBAA`

Note that this function always returns four numbers when passed a valid colour string.
Unused values (depends on the format of the colour string) are assigned 0 (zero).
If an unrecognised colour string is passed, `nil` is returned.

{{<example-box>}}

```lua
r, g, b, a = extract_color("&H7F&")
```

`r`, `g`, and `b` will be 0; `a` will be 127.
{{</example-box>}}

### alpha_from_style

Synopsis: {{< lua `alphastring = util.alpha_from_style(coloralphastring)` >}}

Returns the alpha part of a colour string, as an alpha override string, i.e. `&HAA&` format.
This function is a composition of `extract_color` and `ass_alpha`.

### color_from_style

Synopsis: {{< lua `colorstring = util.color_from_style(coloralphastring)` >}}

Returns the colour part of a colour string, as a colour override string, i.e. `&HBBGGRR&` format.
This function is a composition of `extract_color` and `ass_color`.

### HSV_to_RGB

Synopsis: {{< lua `r, g, b = util.HSV_to_RGB(h, s, v)` >}}

Transforms a colour given in Hue, Saturation, Value space into Red, Green, Blue space.

`h` is given in degrees.
The nominal range is 0..359; values outside this range will be translated into it.
Input range of `s` and `v` are 0..1.
These are not range checked.
Output range of `r`, `g` and `b` are 0..255.

## String functions

Because the Lua standard `string` library is fairly limited, a few additional helper functions are provided.
See also [unicode]({{< relref "unicode" >}}).

### string.trim

Synopsis: {{< lua `outstring = util.trim(instring)` >}}

Removes all space characters at the start and end of the input string, and returns the transformed string.

Warning: This function is not UTF-8 safe.
It uses the Lua regex `%s` class to match spaces, which in some legacy encodings will result in it also matching some prefix bytes in UTF-8 encoded text.

### string.headtail

Synopsis: {{< lua `head, tail = util.headtail(instring)` >}}

Splits a string by first space-sequence into a "head" and a "tail", similar to the handling of linked lists in several functional languages.

If `instring` does not contain any space characters it returns `instring, ""`.

### string.words

Synopsis: {{< lua `for word in util.words(instring) do ... end` >}}

Returns an iterator function for use in a `for` loop, to loop over all the words in the string using `string.headtail` semantics.

## Numeric functions

Functions to handle various operations on numbers.

### clamp

Synopsis: {{< lua `outval = util.clamp(inval, min, max)` >}}

Clamps `inval` to be in range `min`..`max`.

### interpolate

Synopsis: {{< lua `outval = util.interpolate(t, a, b)` >}}

Interpolates between `a` and `b`.
`t` is the time variable in range 0..1.
Values outside this range are clamped.

### interpolate_color

Synopsis: {{< lua `outcolor = util.interpolate_color(t, color1, color2)` >}}

Interpolate between `color1` and `color2` with `t` as time variable in range 0..1.
`color1`, `color2` and `outcolor` are colour strings, and `outcolour` will be in colour override format.

### interpolate_alpha

Synopsis: {{< lua `outalpha = util.interpolate_alpha(t, alpha1, alpha2)` >}}

Similar to `interpolate_color`, but interpolates alpha values instead.
Also works on colour strings, and will return an alpha override string.
