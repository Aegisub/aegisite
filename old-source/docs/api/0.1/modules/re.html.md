The `re` module is a wrapper around boost.regex, intended as a full
replacement for Lua's built in regular expressions. It has two main advantages
over Lua's:

1. Full Unicode support. Lua regular expressions operate on bytes rather than
    characters, which frequently causes problems with multibyte characters.
2. A more powerful and flexible syntax. Properly speaking, Lua does not support
    regular expressions; rather it has a basic pattern matching language that
    supports a small subset of what can be done with regular expressions.
    boost::regex, on the other hand, supports perl-compatible regular
    expressions.

Import this module with `re = require 'aegisub.re'`{:.language-lua}.

See [boost.regex's
documentation](http://www.boost.org/doc/libs/1_53_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)
for information about the regular expression syntax. In general any resources
on the web that refer to Perl regular expressions or PCRE will apply to
this module's regular expressions.

## Data Types

{::type name='MatchTable'}
Several of the functions below return Match Tables containing the match along with information about where in the string the match was found.

{::template name="luabox"}
>>> re.match("b", "abc")
{
    {
        ["str"] = "b",
        ["first"] = 2,
        ["last"] = 2
    }
}
{:/template}

#### Fields
{::field type='string' name='str'}The text matched by a pattern or capturing expression.{:/field}
{::field type='number' name='first'}
The start index of `str` in the original string which had a regular expression
applied to it. Note that this index is one-based and is in bytes, rather than
characters, to match Lua's string indexing.
{:/field}
{::field type='number' name='last'}
The end index of `str` in the original string which had a regular expression
applied to it. Note that this index is one-based, inclusive, and is in bytes,
rather than characters, to match Lua's string indexing.
{:/field}
{:/type}

### Flags ###
The following flags may be passed to all of the static functions (including
`re.compile`).  Flags must come after all supplied non-flag arguments, but
optional arguments can be skipped.

re.ICASE
:   Ignore case when matching.

re.NOSUB:
:   Don't set backreferences and capture groups. Can improve performance when
they aren't needed.

re.NEWLINE_ALT:
:   Treat newline characters as the alternation operator (|).

re.NO_MOD_M:
:   ^ and $ only match the beginning and end of the string rather than newlines.

re.MOD_S:
:   Treat newlines as normal characters, matched by '.'.

re.MOD_X:
:   Ignore unescaped whitespace in the expression, making it possible to write
regular expressions that *aren't* write-only.

re.NO_EMPTY_SUBEXPRESSION:
:   Don't match empty expressions/alternatives.

{::template name="luabox"}
>>> re.match("a", "A")
nil
>>> re.match("a", "A", re.ICASE, re.NOSUB)
{
    {
        ["str"] = "A",
        ["first"] = 1,
        ["last"] = 1
    }
}
{:/template}

## Functions

{::function name='compile' synopsis='expr = re.compile(pattern, [FLAGS])'}
Compile a regular expression. Reusing a compiled regular expression is faster
than recompiling it each time it is used, and is usually more readable as well.

{::arg name='pattern' type='string'}Regular expression to compile.{:/arg}
{::return name='expr' type='table'}
A table with method versions of all of the functions listed below, with the
self argument replacing the pattern argument and no flags arguments
{:/return}

{::template name="luabox"}
>>> expr = re.compile("a")
>>> expr:split("banana")
{
    "b",
    "n",
    "n"
}
{:/template}
{:/function}

{::function name='split' synopsis='chunks = re.split(pattern, str, skip_empty=false, max_splits=0)'}
Split the string at each of the occurrences of `pattern`.

{::arg name='pattern' type='string'}
Regular expression to split the string on. Capture groups in the pattern are
ignored.
{:/arg}
{::arg name='str' type='string'}String to split.{:/arg}
{::arg name='skip_empty' type='boolean'}
Exclude zero-length chunks from the results.
{:/arg}
{::arg name='max_splits' type='number'}
If greater than zero, the maximum numbers of times to split the string (i.e.
`#chunks` will be at most `max_splits + 1`).
{:/arg}
{::return name='chunks' type='table'}
A table containing each of the sections of `str` between the matches of
`pattern`.
{:/return}

{::template name="luabox"}
>>> re.split(",", "a,,b,c")
{
    "a",
    "",
    "b",
    "c"
}
{:/template}
{::template name="luabox"}
>>> re.split(",", "a,,b,c", true)
{
    "a",
    "b",
    "c"
}
{:/template}
{::template name="luabox"}
>>> re.split(",", "a,,b,c", false, 1)
{
    "a",
    ",b,c",
}
{:/template}
{:/function}

{::function name='gsplit' synopsis='iter = re.gsplit(pattern, str, skip_empty=false, max_splits=0)'}
Iterator version of re.split.

{::arg name='pattern' type='string'}
Regular expression to split the string on. Capturing groups in the pattern
are ignored.
{:/arg}
{::arg name='str' type='string'}String to split.{:/arg}
{::arg name='skip_empty' type='boolean'}
Exclude zero-length chunks from the results.
{:/arg}
{::arg name='max_splits' type='number'}
If greater than zero, the maximum numbers of times to split the string (i.e.
`#chunks` will be at most `max_splits + 1`).
{:/arg}
{::return name='iter' type='string iterator'}
An iterator over each of the sections of `str` between the matches of
`pattern`.
{:/return}

{::template name="luabox"}
>>> for str in re.gsplit(",", "a,,b,c") do
>>>     print str
>>> end
a

b
c
{:/template}
{::template name="luabox"}
>>> for str in re.gsplit(",", "a,,b,c", true) do
>>>     print str
>>> end
a
b
c
{:/template}
{::template name="luabox"}
>>> for str in re.gsplit(",", "a,,b,c", false, 1) do
>>>     print str
>>> end
a
,b,c
{:/template}
{:/function}

{::function name='find' synopsis='matches = re.find(pattern, str)'}
Find all non-overlapping substrings of `str` which match `pattern`.

{::arg name='pattern' type='string'}
Pattern to search for. Capturing groups in the pattern are ignored.
{:/arg}
{::arg name='str' type='string'}String to search for the pattern in.{:/arg}
{::return name='matches' type='table or nil'}
A table of [[Match Tables|re#matchtables]] for all matches, or `nil` if
there were none.
{:/return}

{::template name="luabox"}
>>> re.find(".", "☃☃")
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
{:/template}
{::template name="luabox"}
function contains_an_a(str)
    if re.find("a", str)
        print "Has an a"
    else
        print "Doesn't have an a"
    end
end
>>> contains_an_a("abc")
Has an a
>>> contains_an_a("def")
Doesn't have an a
{:/template}
{:/function}

{::function name='gfind' synopsis='iter = re.gfind(pattern, str)'}
Iterate over all non-overlapping substrings of `str` which match `pattern`.

{::arg name='pattern' type='string'}
Pattern to search for. Capturing groups in the pattern are ignored.
{:/arg}
{::arg name='str' type='string'}String to search for the pattern in.{:/arg}
{::return name='iter' type='string, number,<br> number iterator'}
An iterator which produces three values at each step: a matched string, the
start index of the match in the source string, and the inclusive end index of
the match in the source string.
{:/return}

{::template name="luabox"}
>>> for str, start_idx, end_idx in re.gfind(".", "☃☃") do
>>>     print string.format("%d-%d: %s", start_idx, end_idx, str)
>>> end
1-3: ☃
4-6: ☃
{:/template}
{:/function}

{::function name='match' synopsis='matches = re.match(pattern, str)'}
Match a pattern against a string. This differs from `find` in that `find`
returns all matches and does not capture subgroups, while this returns only a
single match along with the captured subgroups.

{::arg name='pattern' type='string'}Pattern to search for.{:/arg}
{::arg name='str' type='string'}String to search for the pattern in.{:/arg}
{::return name='matches' type='table or nil'}
`nil` if the pattern did not match the string. Otherwise, a table containing
a [[Match Table|re#matchtables]] for the full match, followed by a [[Match
Table|re#matchtables]] for each capturing subexpression in the pattern (if
any).
{:/return}

{::template name="luabox"}
>>> re.match("(\d+) (\d+) (\d+)", "{250 1173 380}Help!")
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
        ["str"] = "380"
        ["first"] = 11,
        ["last"] = 13
    }
}
{:/template}
{:/function}

{::function name='gmatch' synopsis='iter = re.gmatch(pattern, str)'}
Iterator version of [[`re.match`|re#re.match]].

{::arg name='pattern' type='string'}Pattern to search for.{:/arg}
{::arg name='str' type='string'}String to search for the pattern in.{:/arg}
{::return name='matches' type='table iterator'}
An iterator which returns a table containing a [[Match
Table|re#matchtables]] for the full match (if it matched), followed by a
[[Match Table|re#matchtables]] for each capturing subexpression in the pattern
(if any).
{:/return}
{:/function}

{::function name='sub' synopsis='out_str, rep_count = re.sub(pattern, replace, str, max_count=0)'}
Replace each occurrence of `pattern` in `str` with `replace`.

{::arg name='pattern' type='string'}
Pattern to search for.
{:/arg}
{::arg name='replace' type='string or function'}
Replacement for matches. This may be either a string which is inserted, or a
function which is called for each match.

If `replace` is a string, it may contain references to the matches. `&` and
`\0` are replaced with the full match, and `\<number>` is replaced with the
appropriate captured subexpression.

If `replace` is a function, it is called for either the entire match (if there
are no capturing subexpressions), or for each captured subexpression. It is
passed the match string, start index of the match, and end index of the match.
If it returns a string, the match is replaced with the return value. If it
returns anything else, then the source string is left unchanged.
{:/arg}
{::arg name='max_count' type='number'}
If greater than zero, the maximum number of replacements to make.
{:/arg}
{::return name='out_str' type='string'}
The input string, with replacements applied.
{:/return}
{::return name='rep_count' type='number'}
The number of replacements that were made.
{:/return}

{::template name="examplebox"}
Replace all instances of \k with \kf:

~~~ lua
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k", "\\kf")
{\kf10}a{\kf15}b{\kf30}c
~~~
{:/template}
{::template name="examplebox"}
Replace all instances of \k and \K with \kf:

~~~ lua
>>> re.sub("{\\K10}a{\\K15}b{\\k30}c", "\\\\k", "\\kf", re.ICASE)
{\kf10}a{\kf15}b{\kf30}c
~~~

{:/template}
{::template name="examplebox"}
Add one to each \k duration:

~~~ lua
function add_one(str)
    return tostring(tonumber(str) + 1)
end
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k(\[[:digit:]]+)", add_one)
{\k11}a{\k16}b{\k31}c
~~~
{:/template}
{:/function}
