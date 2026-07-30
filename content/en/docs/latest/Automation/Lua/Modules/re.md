---
title: re
menu:
  docs:
    parent: lua-modules
weight: 6266
aliases:
  - /docs/latest/Automation/Lua/Modules/re/
---

The `re` module is a wrapper around boost::regex, intended as a full
replacement for Lua's built in regular expressions. It has two main advantages
over Lua's:

1. Full Unicode support. Lua regular expressions operate on bytes rather than
   characters, which frequently causes problems with multibyte characters.
1. A more powerful and flexible syntax. Properly speaking, Lua does not support
   regular expressions; rather it has a basic pattern matching language that
   supports a small subset of what can be done with regular expressions.
   boost::regex, on the other hand, supports perl-compatible regular
   expressions.

## Usage

Import this module with {{< lua `re = require 'aegisub.re'` >}}.

See [boost.regex's
documentation](https://www.boost.org/doc/libs/1_53_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)
for information about the regular expression syntax. In general any resources
on the web that refer to Perl regular expressions or PCRE will apply to
this module's regular expressions.

### Match Tables

Several of the functions below return Match Tables, which are tables containing
the following fields:

`str` (`string`)
: The text matched by a pattern or capturing expression

`first` (`number`)
: The start index of `str` in the original string which had a regular
  expression applied to it. Note that this index is one-based and is in bytes,
  rather than characters, to match Lua's string indexing.

`last` (`number`)
: The end index of `str` in the original string which had a regular expression
  applied to it. Note that this index is one-based, inclusive, and is in bytes,
  rather than characters, to match Lua's string indexing.

{{<example-box>}}

```lua
>>> re.match("abc", "b")
{
    {
        ["str"] = "b",
        ["first"] = 2,
        ["last"] = 2
    }
}
```

{{</example-box>}}

### Flags

The following flags may be passed to all of the static functions (including
`re.compile`).  Flags must come after all supplied non-flag arguments, but
optional arguments can be skipped.

re.ICASE
: Ignore case when matching.

re.NOSUB:
: Don't set backreferences and capture groups. Can improve performance when
  they aren't needed.

re.NEWLINE_ALT:
: Treat newline characters as the alternation operator `|`.

re.NO_MOD_M:
: `^` and `$` only match the beginning and end of the string rather than newlines.

re.MOD_S:
: Treat newlines as normal characters, matched by `.`.

re.MOD_X:
: Ignore unescaped whitespace in the expression, making it possible to write
  regular expressions that *aren't* write-only.

re.NO_EMPTY_SUBEXPRESSIONS:
: Don't match empty expressions/alternatives.

{{<example-box>}}

```lua
>>> re.match("A", "a")
nil
>>> re.match("A", "a", re.ICASE, re.NOSUB)
{
    {
        ["str"] = "A",
        ["first"] = 1,
        ["last"] = 1
    }
}
```

{{</example-box>}}

### re.compile

Synopsis: {{< lua `expr = re.compile(pattern, [FLAGS])` >}}

Compile a regular expression. Reusing a compiled regular expression is faster
than recompiling it each time it is used, and is usually more readable as well.

`@pattern` (`string`)
: Regular expression to compile.

`expr` (`table`)
: A table with all of the functions listed below, except without the pattern
  and flags arguments.

{{<example-box>}}

```lua
>>> expr = re.compile("a")
>>> expr:split("eat banana")
{
    "e",
    "t b",
    "n",
    "n",
    ""
}
```

{{</example-box>}}

### re.split

Synopsis: {{< lua `chunks = re.split(str, pattern, skip_empty=false, max_splits=0)` >}}

Split the string at each of the occurrences of `pattern`.

`@str` (`string`)
: String to split.

`@pattern` (`string`)
: Regular expression to split the string on. Capturing groups in the pattern
  are ignored.

`@skip_empty` (`boolean`)
: Do not include zero-length chunks in the results.

`@max_splits` (`number`)
: If greater than zero, the maximum numbers of times to split the string (i.e.
  `#chunks` will be at most `max_splits + 1`).

`chunks` (`table`)
: A table containing each of the sections of `str` between the matches of
  `pattern`.

{{<example-box>}}

```lua
>>> re.split("a,,b,c", ",")
{
    "a",
    "",
    "b",
    "c"
}
```

{{</example-box>}}
{{<example-box>}}

```lua
>>> re.split("a,,b,c", ",", true)
{
    "a",
    "b",
    "c"
}
```

{{</example-box>}}
{{<example-box>}}

```lua
>>> re.split("a,,b,c", ",", false, 1)
{
    "a",
    ",b,c",
}
```

{{</example-box>}}

### re.gsplit

Synopsis: {{< lua `iter = re.gsplit(str, pattern, skip_empty=false, max_splits=0)` >}}

Iterator version of `re.split`.

`@str` (`string`)
: String to split.

`@pattern` (`string`)
: Regular expression to split the string on. Capturing groups in the pattern
  are ignored.

`@skip_empty` (`boolean`)
: Do not include zero-length chunks in the results.

`@max_splits` (`number`)
: If greater than zero, the maximum numbers of times to split the string (i.e.
  `#chunks` will be at most `max_splits + 1`).

`iter` (`iterator over strings`)
: An iterator over each of the sections of `str` between the matches of
  `pattern`.

{{<example-box>}}

```lua
>>> for str in re.gsplit("a,,b,c", ",") do
>>>     print(str)
>>> end
a

b
c
```

{{</example-box>}}
{{<example-box>}}

```lua
>>> for str in re.gsplit("a,,b,c", ",", true) do
>>>     print(str)
>>> end
a
b
c
```

{{</example-box>}}
{{<example-box>}}

```lua
>>> for str in re.gsplit("a,,b,c", ",", false, 1) do
>>>     print(str)
>>> end
a
,b,c
```

{{</example-box>}}

### re.find

Synopsis: {{< lua `matches = re.find(str, pattern)` >}}

Find all non-overlapping substrings of `str` which match `pattern`.

`@str` (`string`)
: String to search for the pattern in.

`@pattern` (`string`)
: Pattern to search for. Capturing groups in the pattern are ignored.

`matches` (`table` or `nil`)
: A table of [Match Tables]({{< relref "re#match-tables" >}}) for all matches, or `nil` if
  there were none.

{{<example-box>}}

```lua
>>> re.find("☃☃", ".")
{
    {
        ["str"] = "☃",
        ["first"] = 1,
        ["last"] = 3
    },
    {
        ["str"] = "☃",
        ["first"] = 4,
        ["last"] = 6
    }
}
```
{{</example-box>}}

{{<example-box>}}

```lua
function contains_an_a(str)
    if re.find(str, "a") then
        print("Has an a")
    else
        print("Doesn't have an a")
    end
end
>>> contains_an_a("abc")
Has an a
>>> contains_an_a("def")
Doesn't have an a
```

{{</example-box>}}

### re.gfind

Synopsis: {{< lua `iter = re.gfind(str, pattern)` >}}

Iterate over all non-overlapping substrings of `str` which match `pattern`.

`@str` (`string`)
: String to search for the pattern in.

`@pattern` (`string`)
: Pattern to search for. Capturing groups in the pattern are ignored.

`iter` (`iterator over string, number, number`)
: An iterator which produces three values at each step: a matched string, the
  started index of the match in the source string, and the inclusive end index of
  the match in the source string.

{{<example-box>}}

```lua
>>> for str, start_idx, end_idx in re.gfind("☃☃", ".") do
>>>     print(string.format("%d-%d: %s", start_idx, end_idx, str))
>>> end
1-3: ☃
4-6: ☃
```

{{</example-box>}}

### re.match

Synopsis: {{< lua `matches = re.match(str, pattern)` >}}

Match a pattern against a string. This differs from `find` in that `find`
returns all matches and does not capture subgroups, while this returns only a
single match along with the captured subgroups.

`@str` (`string`)
: String to search for the pattern in.

`@pattern` (`string`)
: Pattern to search for.

`matches` (`table` or `nil`)
: `nil` if the pattern did not match the string. Otherwise, a table containing
  a [Match Table]({{< relref "re#match-tables" >}}) for the full match, followed by a [Match Table]({{< relref "re#match-tables" >}}) for each capturing subexpression in the pattern (if
  any).

{{<example-box>}}

```lua
>>> re.match("{250 1173 380}Help!", "(\\d+) (\\d+) (\\d+)")
{
    {
        ["str"] = "250 1173 380",
        ["first"] = 2,
        ["last"] = 13
    },
    {
        ["str"] = "250",
        ["first"] = 2,
        ["last"] = 4
    },
    {
        ["str"] = "1173",
        ["first"] = 6,
        ["last"] = 9,
    },
    {
        ["str"] = "380",
        ["first"] = 11,
        ["last"] = 13
    }
}
```

{{</example-box>}}

### re.gmatch

Synopsis: {{< lua `iter = re.gmatch(str, pattern)` >}}

Iterator version of [`re.match`]({{< relref "re#rematch" >}}).

`@str` (`string`)
: String to search for the pattern in.

`@pattern` (`string`)
: Pattern to search for.

`matches` (`iterator over table`)
: An iterator which returns a table containing a [Match Table]({{< relref "re#match-tables" >}}) for the full match (if it matched), followed by a
  [Match Table]({{< relref "re#match-tables" >}}) for each capturing subexpression in the pattern
  (if any).

### re.sub

Synopsis: {{< lua `out_str = re.sub(str, pattern, replace, max_count=0)` >}}

Replace each occurrence of `pattern` in `str` with `replace`.

`@pattern` (`string`)
: Pattern to search for.

`@replace` (`string` or `function`)
: Replacement for matches. This may be either a string which is inserted, or a
  function which is called for each match.

  If `replace` is a string, it uses Boost.Regex's Perl-style replacement
  format. `$&` is replaced with the full match. `$1`, `$2`, etc. and `\1`
  through `\9` are replaced with the corresponding captured subexpression.

  If `replace` is a function, it is called for either the entire match (if
  there are no capturing subexpressions), or for each captured subexpression.
  It is passed the match string, start index of the match, and end index of
  the match. If it returns a string, the match is replaced with the return
  value. If it returns anything else, then the source string is left
  unchanged.

`@max_count` (`number`)
: If greater than zero, the maximum number of replacements to make.

`out_str` (`string`)
: The input string, with replacements applied.

{{<example-box>}}
Replace all instances of \\k with \\kf:

```lua
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k", "\\\\kf")
{\kf10}a{\kf15}b{\kf30}c
```

{{</example-box>}}
{{<example-box>}}
Replace all instances of \\k and \\K with \\kf:

```lua
>>> re.sub("{\\K10}a{\\K15}b{\\k30}c", "\\\\k", "\\\\kf", re.ICASE)
{\kf10}a{\kf15}b{\kf30}c
```

{{</example-box>}}
{{<example-box>}}
Add one to each \\k duration:

```lua
function add_one(str)
    return tostring(tonumber(str) + 1)
end
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k(\\d+)", add_one)
{\k11}a{\k16}b{\k31}c
```

{{</example-box>}}
{{<example-box>}}
Consider these examples:

```lua
-- Example 1
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", "\\\\yf")
-- Example 2
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", "\\yf")
-- Example 3
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", function(str) return "\\yf" end)
```

Examples 1 and 3 both produce `{\yf10}a{\yf15}b{\yf30}c`. Example 2
produces `{yf10}a{yf15}b{yf30}c`, without the backslashes.

Why do the number of backslashes differ?

Each quoted Lua string is interpreted by Lua first, so a literal backslash in
the string must be written as `\\`. The resulting pattern is then parsed as a
regular expression. A string replacement is separately parsed using
Boost.Regex's replacement format, while the value returned by a replacement
function is inserted directly.

After Lua interprets the strings above:

- The source string is `{\y10}a{\y15}b{\y30}c`.
- The pattern is `\\y`, which matches the literal text `\y`.
- Example 1's replacement is `\\yf`. The replacement formatter converts `\\`
  to a literal backslash, producing `\yf`.
- Example 2's replacement is `\yf`. In a Boost replacement string, an
  unrecognized escape such as `\y` emits the escaped character without the
  backslash, producing `yf`.
- Example 3's function returns `\yf`. Function results do not pass through the
  replacement formatter, so the backslash is retained.

Lua's long-bracket strings do not process escape sequences. The examples above
can equivalently be written as:

```lua
-- Example 1
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], [[\\yf]])
-- Example 2
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], [[\yf]])
-- Example 3
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], function(str) return [[\yf]] end)
```

{{</example-box>}}
