[[!template id=toc depth=2]]

The `re` module is a wrapper around wxRegex, intended as a full replacement for
Lua's built in regular expressions. It has two main advantages over Lua's:

1. Full Unicode support. Lua regular expressions operate on bytes rather than
    characters, which frequently causes problems with multibyte characters.
2. A more powerful and flexible syntax. Lua's regular expressions are fairly
    minimal (out of necessity; [PCRE](http://www.pcre.org/) is larger than all
    of Lua combined). wxRegex on the other hand, uses Henry Spencer's regex
    library.

## Usage ##
Import this module with `require "re"`.

See [wx's
documentation](http://docs.wxwidgets.org/trunk/overview_resyntax.html) for
information about the regular expression syntax. Note that Aegisub uses
*advanced regular expressions* (ARE).

### Match Tables ###
Several of the functions below return Match Tables, which are tables containing
the following fields:

**`str`** (`string`)
: The text matched by a pattern or capturing expression

**`first`** (`number`)
: The start index of `str` in the original string which had a regular
expression applied to it. Note that this index is one-based and is in bytes,
rather than characters, to match Lua's string indexing.

**`last`** (`number`)
: The end index of `str` in the original string which had a regular expression
applied to it. Note that this index is one-based, inclusive, and is in bytes,
rather than characters, to match Lua's string indexing.

[[!template id=Examplebox data="""
    >>> re.match("b", "abc")
    {
        {
            ["str"] = "b",
            ["first"] = 2,
            ["last"] = 2
        }
    }
"""]]

### Flags ###
The following flags may be passed to all of the static functions (including
`re.compile`).  Flags must come after all supplied non-flag arguments, but
optional arguments can be skipped.

re.ICASE
:   Ignore case when matching.

re.NOSUB:
:   Don't set backreferences and capture groups. Can improve performance when
they aren't needed.

re.NEWLINE:
:   Treat newlines as normal characters, matched by '.'.

[[!template id=Examplebox data="""
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
"""]]

### re.compile ###
Synopsis: `expr = re.compile(pattern, [FLAGS])`

Compile a regular expression. Reusing a compiled regular expression is faster
than recompiling it each time it is used, and is usually more readable as well.

**`@pattern`** (`string`)
: Regular expression to compile.

**`expr`** (`table`)
: A table with all of the functions listed below, except without the pattern
and flags arguments.

[[!template id=Examplebox data="""
    >>> expr = re.compile("a")
    >>> expr:split("banana")
    {
        "b",
        "n",
        "n"
    }
"""]]

### re.split ###
Synopsis: `chunks = re.split(pattern, str, skip_empty=false, max_splits=0)`

Split the string at each of the occurrences of `pattern`.

**`@pattern`** (`string`)
: Regular expression to split the string on. Capturing groups in the pattern
are ignored.

**`@str`** (`string`)
: String to split.

**`@skip_empty`** (`boolean`)
: Do not include zero-length chunks in the results.

**`@max_splits`** (`number`)
: If greater than zero, the maximum numbers of times to split the string (i.e.
`#chunks` will be at most `max_splits + 1`).

**`chunks`** (`table`)
: A table containing each of the sections of `str` between the matches of
`pattern`.

[[!template id=Examplebox data="""
    >>> re.split(",", "a,,b,c")
    {
        "a",
        "",
        "b",
        "c"
    }
"""]]
[[!template id=Examplebox data="""
    >>> re.split(",", "a,,b,c", true)
    {
        "a",
        "b",
        "c"
    }
"""]]
[[!template id=Examplebox data="""
    >>> re.split(",", "a,,b,c", false, 1)
    {
        "a",
        ",b,c",
    }
"""]]

### re.gsplit ###
Synopsis: `iter = re.gsplit(pattern, str, skip_empty=false, max_splits=0)`

Iterator version of re.split.

**`@pattern`** (`string`)
: Regular expression to split the string on. Capturing groups in the pattern
are ignored.

**`@str`** (`string`)
: String to split.

**`@skip_empty`** (`boolean`)
: Do not include zero-length chunks in the results.

**`@max_splits`** (`number`)
: If greater than zero, the maximum numbers of times to split the string (i.e.
`#chunks` will be at most `max_splits + 1`).

**`iter`** (`iterator over strings`)
: An iterator over each of the sections of `str` between the matches of
`pattern`.

[[!template id=Examplebox data="""
    >>> for str in re.gsplit(",", "a,,b,c") do
    >>>     print str
    >>> end
    a

    b
    c
"""]]
[[!template id=Examplebox data="""
    >>> for str in re.gsplit(",", "a,,b,c", true) do
    >>>     print str
    >>> end
    a
    b
    c
"""]]
[[!template id=Examplebox data="""
    >>> for str in re.gsplit(",", "a,,b,c", false, 1) do
    >>>     print str
    >>> end
    a
    ,b,c
"""]]

### re.find ###
Synopsis: `matches = re.find(pattern, str)`

Find all non-overlapping substrings of `str` which match `pattern`.

**`@pattern`** (`string`)
: Pattern to search for. Capturing groups in the pattern are ignored.

**`@str`** (`string`)
: String to search for the pattern in.

**`matches`** (`table` or `nil`)
: A table of [[Match Tables|re#matchtables]] for all matches, or `nil` if
there were none.

[[!template id=Examplebox data="""
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
"""]]
[[!template id=Examplebox data="""
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
"""]]

### re.gfind ###
Synopsis: `iter = re.gfind(pattern, str)`

Iterate over all non-overlapping substrings of `str` which match `pattern`.

**`@pattern`** (`string`)
: Pattern to search for. Capturing groups in the pattern are ignored.

**`@str`** (`string`)
: String to search for the pattern in.

**`iter`** (`iterator over string, number, number`)
: An iterator which produces three values at each step: a matched string, the
started index of the match in the source string, and the inclusive end index of
the match in the source string.

[[!template id=Examplebox data="""
    >>> for str, start_idx, end_idx in re.gfind(".", "☃☃") do
    >>>     print string.format("%d-%d: %s", start_idx, end_idx, str)
    >>> end
    1-3: ☃
    4-6: ☃
"""]]

### re.match ###
Synopsis: `matches = re.match(pattern, str)`

Match a pattern against a string. This differs from `find` in that `find`
returns all matches and does not capture subgroups, while this returns only a
single match along with the captured subgroups.

**`@pattern`** (`string`)
: Pattern to search for.

**`@str`** (`string`)
: String to search for the pattern in.

**`matches`** (`table` or `nil`)
: `nil` if the pattern did not match the string. Otherwise, a table containing
a [[Match Table|re#matchtables]] for the full match, followed by a [[Match
Table|re#matchtables]] for each capturing subexpression in the pattern (if
any).

[[!template id=Examplebox data="""
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
"""]]

### re.gmatch ###
Synopsis: `iter = re.gmatch(pattern, str)`

Iterator version of [[`re.match`|re#re.match]].

**`@pattern`** (`string`)
: Pattern to search for.

**`@str`** (`string`)
: String to search for the pattern in.

**`matches`** (`iterator over table`)
: An iterator which returns a table containing a [[Match
Table|re#matchtables]] for the full match (if it matched), followed by a
[[Match Table|re#matchtables]] for each capturing subexpression in the pattern
(if any).

### re.sub ###
Synopsis: `out_str, rep_count = re.sub(pattern, replace, str, max_count=0)`

Replace each occurrence of `pattern` in `str` with `replace`.

**`@pattern`** (`string`)
: Pattern to search for.

**`@replace`** (`string` or `function`)
: Replacement for matches. This may be either a string which is inserted, or a
    function which is called for each match.

    If `replace` is a string, it may contain references to the matches. `&` and
    `\0` are replaced with the full match, and `\<number>` is replaced with the
    appropriate captured subexpression.

    If `replace` is a function, it is called for either the entire match (if
    there are no capturing subexpressions), or for each captured subexpression.
    It is passed the match string, start index of the match, and end index of
    the match. If it returns a string, the match is replaced with the return
    value. If it returns anything else, then the source string is left
    unchanged.

**`@max_count`** (`number`)
: If greater than zero, the maximum number of replacements to make.

**`out_str`** (`string`)
: The input string, with replacements applied.

**`rep_count`** (`number`)
: The number of replacements that were made.

[[!template id=Examplebox data="""
Replace all instances of \k with \kf:

    >>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k", "\\kf")
    {\kf10}a{\kf15}b{\kf30}c
"""]]
[[!template id=Examplebox data="""
Replace all instances of \k and \K with \kf:

    >>> re.sub("{\\K10}a{\\K15}b{\\k30}c", "\\\\k", "\\kf", re.ICASE)
    {\kf10}a{\kf15}b{\kf30}c

"""]]
[[!template id=Examplebox data="""
Add one to each \k duration:

    function add_one(str)
        return tostring(tonumber(str) + 1)
    end
    >>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k(\[[:digit:]]+)", add_one)
    {\k11}a{\k16}b{\k31}c
"""]]

[[!template id=Automation_navbox]]
