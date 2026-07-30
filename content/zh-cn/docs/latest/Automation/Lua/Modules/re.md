---
title: re
menu:
  docs:
    parent: lua-modules
weight: 6266
---

`re`模块是对 boost::regex 的封装，旨在完全替代 Lua 内置的正则表达式。相比 Lua 的内置正则表达式，它具有两个主要优势：

1. 完整的 Unicode 支持。Lua 正则表达式操作的是字节而非字符，这在使用多字节字符时经常引发问题。
1. 更强大、更灵活的语法。严格来说，Lua 并不支持正则表达式；它只具备一种基础的模式匹配语言，仅支持正则表达式功能的一小部分子集。而 boost::regex 则支持 Perl 兼容的正则表达式。

## 用法

通过 {{< lua `re = require 'aegisub.re'` >}} 导入此模块。

关于正则表达式语法，请参阅 [boost.regex 文档](https://www.boost.org/doc/libs/1_53_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)。通常，网络上任何提及 Perl 正则表达式或 PCRE 的资料均适用于此模块的正则表达式。

### 匹配表（Match Tables）

下文中的几个函数会返回匹配表(以表的形式返回匹配)，表的结构如下：

`str` (`string`)
: 模式或捕获表达式匹配到的文本。

`first` (`number`)
: `str`在源字符串中的起始索引。注意，此索引从 1 开始，且以字节而非字符为单位，以便与 Lua 的字符串索引保持一致。

`last` (`number`)
: `str`在源字符串中的结束索引。注意，此索引从 1 开始、包含结束位置，且以字节而非字符为单位，以便与 Lua 的字符串索引保持一致。

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

### 标志（Flags）

下列标志可传递给所有静态函数（包括 `re.compile`）。标志必须位于所有非标志参数之后，但可选参数可以跳过。

re.ICASE
: 匹配时忽略大小写。

re.NOSUB:
: 不设置反向引用和捕获组。当不需要它们时，可以提高性能。

re.NEWLINE_ALT:
: 将换行符视为交替操作符（the alternation operator）`|`。

re.NO_MOD_M:
: `^`和`$`仅匹配字符串的开始和结束，而不是换行处。

re.MOD_S:
: 将换行符视为普通字符，由`.`匹配。

re.MOD_X:
: 忽略表达式中未转义的空白字符，便于编写可读性更好的正则表达式。

re.NO_EMPTY_SUBEXPRESSION:
: 不匹配空表达式/空分支。

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

语法概要：{{< lua `expr = re.compile(pattern, [FLAGS])` >}}

编译一个正则表达式。重复使用已编译的正则表达式比每次使用时重新编译更快，通常也更具可读性。

`@pattern` (`string`)
: 要编译的正则表达式。

`expr` (`table`)
: 一个包含下文中所有函数的表，但不包含`pattern`和`flags`参数。

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

语法概要：{{< lua `chunks = re.split(str, pattern, skip_empty=false, max_splits=0)` >}}

在每次出现`pattern`的位置拆分字符串。

`@str` (`string`)
: 要拆分的字符串。

`@pattern` (`string`)
: 用于拆分的正则表达式。其捕获组会被忽略。

`@skip_empty` (`boolean`)
: 在结果中不要包含长度为零的分段。

`@max_splits` (`number`)
: 若大于零，表示拆分字符串的最大次数（即`#chunks`最多为`max_splits + 1`）。

`chunks` (`table`)
: 一个表，包含了字符串`str`根据`pattern`每次匹配拆分后的各个部分。

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

语法概要：{{< lua `iter = re.gsplit(str, pattern, skip_empty=false, max_splits=0)` >}}

`re.split`的迭代器版本。

`@str` (`string`)
: 要拆分的字符串。

`@pattern` (`string`)
: 用于拆分的正则表达式。其捕获组会被忽略。

`@skip_empty` (`boolean`)
: 在结果中不要包含长度为零的分段。

`@max_splits` (`number`)
: 若大于零，表示拆分字符串的最大次数（即`#chunks`最多为`max_splits + 1`）。

`iter` (`iterator over strings`)
: 一个迭代器，用于遍历字符串`str`根据模式`pattern`每次匹配拆分后的各个部分。

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

语法概要：{{< lua `matches = re.find(str, pattern)` >}}

查找字符串`str`中所有匹配`pattern`的非重叠子串。

`@str` (`string`)
: 要搜索的字符串。

`@pattern` (`string`)
: 用于搜索的正则表达式。其捕获组将被忽略。

`matches` (`table` 或 `nil`)
: 一个包含所有匹配项（每个匹配项都是一个[匹配表]({{< relref "re#match-tables" >}})）的表，若未找到任何匹配则返回 `nil`。

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
    if re.find(str, "a")
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

语法概要：{{< lua `iter = re.gfind(str, pattern)` >}}

迭代遍历`str`中所有匹配`pattern`的非重叠子串。

`@str` (`string`)
: 要搜索的字符串。

`@pattern` (`string`)
: 用于搜索的正则表达式。其捕获组将被忽略。

`iter` (`iterator over string, number, number`)
: 一个迭代器，每次迭代产生三个值：匹配到的字符串、该匹配在源字符串中的起始索引、匹配在源字符串中的结束索引（结束索引包含结束位置）。

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

语法概要：{{< lua `matches = re.match(str, pattern)` >}}

将模式串`pattern`与字符串进行匹配。与`find`不同，`find`返回所有匹配且不捕获子组，而此函数仅返回单个匹配及其捕获的子组。

`@str` (`string`)
: 要搜索的字符串。

`@pattern` (`string`)
: 用于搜索的正则表达式。

`matches` (`table` 或 `nil`)
: 若未找到任何匹配则返回`nil`。否则，返回一个表，第一项是一个完整匹配的[匹配表]({{< relref "re#match-tables" >}})，随后的项是每个捕获子表达式（如果有）对应的[匹配表]({{< relref "re#match-tables" >}})。

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
        ["str"] = "380"
        ["first"] = 11,
        ["last"] = 13
    }
}
```

{{</example-box>}}

### re.gmatch

语法概要：{{< lua `iter = re.gmatch(str, pattern)` >}}

[`re.match`]({{< relref "re#re.match" >}})的迭代器版本。

`@str` (`string`)
: 要搜索的字符串。

`@pattern` (`string`)
: 用于搜索的正则表达式。

`matches` (`iterator over table`)
: 一个迭代器，用于遍历一个表。该表第一项是一个完整匹配的[匹配表]({{< relref "re#match-tables" >}})，随后的项是每个捕获子表达式（如果有）对应的[匹配表]({{< relref "re#match-tables" >}})。

### re.sub

语法概要：{{< lua `out_str = re.sub(str, pattern, replace, max_count=0)` >}}

将`str`中每次出现的`pattern`替换为`replace`。

`@pattern` (`string`)
: 用于搜索的正则表达式。

`@replace` (`string` 或 `function`)
: 匹配项的替换内容。可以是要插入的字符串，也可以是针对每个匹配调用的函数。

  如果`replace`是字符串，它可以包含对匹配项的引用。`&`和`\0`会被替换为整个模式匹配到的文本，`\<number>`会被替换为相应的捕获子表达式。

  如果`replace`是函数，当模式中没有捕获子表达式时，它将接收整个模式匹配到的文本作为参数进行调用；当存在捕获子表达式时，则为每个捕获的子表达式分别调用。该函数会接收三个参数：匹配到的字符串、匹配在源字符串中的起始索引、匹配在源字符串中的结束索引（结束索引包含结束位置）。如果函数返回一个字符串，则匹配项会被替换为该返回值；如果函数返回任何其他类型的值，则源字符串中对应的部分保持原样不变。

`@max_count` (`number`)
: 如果大于零，表示要进行的最大替换次数。

`out_str` (`string`)
: 替换后的输入字符串。

{{<example-box>}}
替换所有的`\\k`为`\\kf`：

```lua
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k", "\\\\kf")
{\kf10}a{\kf15}b{\kf30}c
```

{{</example-box>}}
{{<example-box>}}
替换所有的`\\k`和`\\K`为`\\kf`：

```lua
>>> re.sub("{\\K10}a{\\K15}b{\\k30}c", "\\\\k", "\\\\kf", re.ICASE)
{\kf10}a{\kf15}b{\kf30}c
```

{{</example-box>}}
{{<example-box>}}
对每个`\\k`的时长加1：

```lua
function add_one(str)
    return tostring(tonumber(str) + 1)
end
>>> re.sub("{\\k10}a{\\k15}b{\\k30}c", "\\\\k(\\d+)", add_one)
{\k11}a{\k16}b{\k31}c
```

{{</example-box>}}

{{<example-box>}}
考虑以下例子：

```lua
-- 例子 1
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", "\\\\yf")
-- 例子 2
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", "\\yf")
-- 例子 3
re.sub("{\\y10}a{\\y15}b{\\y30}c", "\\\\y", function(str) return "\\yf" end)
```

其中，**例子1和例子3是正确的，且输出结果相同。例子2是错误的，可能导致非预期结果**（可能产生非预想的替换结果或者程序抛错，取决于正则引擎的实现）。

为什么几个例子反斜杠的数量会不同？

对于`re`模块，模式字符串`pattern`和替换内容`replace`都需要经过 Lua 转义和正则转义。但如果`replace`是函数，则`replace`仅需 Lua 转义。

在 Lua 字符串字面量中，反斜杠`\`必须写作`\\`，否则会被解释为转义字符（例如`\n`代表换行符）。要表示字面意义的两个字符`\`和`n`，需写为`\\n`。

<br>
在 Lua 解释过程中，上述例子被解释为：

*源字符串（第1个参数）*：`"{\\y10}a{\\y15}b{\\y30}c" → {\y10}a{\y15}b{\y30}c`

*模式串（第2个参数）*：`"\\\\y" → \\y`

*替换内容（第3个参数）*：

 - *例子1*：`"\\\\yf" → \\yf`

 - *例子2*：`"\\yf" → \yf`

 - *例子3（函数内的字符串）*：`"\\yf" → \yf`

<br>
解释后的内容被传递给正则引擎。此时进行了正则转义：

*源字符串*：不进行正则转义。依旧为`{\y10}a{\y15}b{\y30}c`

*模式串*：`\\y → \y`

*替换内容*：

 - *例子1*：`\\yf → \yf`

 - *例子2*：`\yf → ??` （由于`\y`不是有效的单字符正则类（例：字符正则类`\d`代表数字`0-9`），正则引擎可能抛出错误，或忽略`\`而将其视为`yf`）

 - *例子3*：由于是函数，不进行正则转义。函数内的字符串依旧为`\yf`

当然，我们可以用长格式中括号来定义字符串，Lua 不会对这样定义的字符串解释任何转义序列（但还是会正则转义），上面的例子等价于：

```lua
-- 例子 1
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], [[\\yf]])
-- 例子 2
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], [[\yf]])
-- 例子 3
re.sub([[{\y10}a{\y15}b{\y30}c]], [[\\y]], function(str) return [[\yf]] end)
```

{{</example-box>}}
