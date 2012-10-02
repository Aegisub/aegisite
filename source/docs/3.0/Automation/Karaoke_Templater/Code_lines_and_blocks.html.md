Code lines and blocks in Karaoke Templater allows you to create advanced effects by incorporating small snippets of Lua code. This can range from simple mathematical expressions adding two numbers to complex functions that for example could generate various shapes in cycling colours.

Both code lines and code blocks are run in a separate semi-closed execution environment, meaning they are mostly undisturbed by the primary Lua environment the Karaoke Templater script itself runs in. For an overview of what variables are available in the code line/block execution environment see: [[Code execution environment|Automation/Karaoke_Templater/Code_execution_environment]].


## Code lines  ##


A code line is a special kind of template line. Instead of using the `template` keyword in the Effect field it uses the `code` keyword. A code line contains only Lua code and does not by itself produce any lines in the resulting file.

The two primary uses of code lines are:

* Defining/updating variables for use later in templates
* Defining functions for use later in templates

<div></div>

For example, if you need a random number, but also need to use it twice in one template, you can use a code line to first generate the number and store it to a variable, then use that variable in your template line.

Another example could be defining a function that produces a random colour.


### Classes of code lines  ###


Like there's multiple classes of template lines there's also multiple classes of code lines. Some of them are the same, and some only exist for one or the other.

You specify the class of the code line in the Effect field after the `code` keyword. The possible classes are:

**once**
> Code lines in the `once` class are run exactly one time, before any templates are applied. This is usually the best place to define functions and general tables of values you need to look up later.
> This is the default class, if you don't specify a class for a code line it's automatically in the `once` class.

**line**
> Code lines in the `line` class are run when a new line is encountered. They are run once per line. They are run interspersed with `line`/`pre-line` templates in the order they appear. (There are no "pre-line" code lines.)

**syl**
> Code lines in the `syl` class are run when a new syllable is encountered. They run once per syllable. They are run interspersed with `syl` templates.

**furi**
> Code lines in the `furi` class are run when a new furigana syllable is encountered. They run once per furigana syllable.  They are run interspersed with `furi` templates.

You _cannot_ have templates with `char` or `multi` modifiers run per-character/per-highlight interspersed with code lines. This is a limitation of the execution model. This may or may not change in later versions of Karaoke Templater.


## Code blocks  ##


A code block is a block of Lua code within a template line. Code blocks are used to insert more complex things than can be expressed with [[inline variables|Automation/Karaoke_Templater/Inline_variables]].

Code blocks are required to be single Lua expressions, since a `return` statement is automatically prepended to the code. This means you (among other things) can't do assignments or use `if` statements within code blocks, you must use a code line if you want to do any of those things. (There is a way to do basic conditionals in code blocks though, see below.)

You create a code block by surrounding the code by exclamation marks, like this:

    {\t($start,**!syl.start_time+20!**,\bord0)}

It is possible to use inline variables within code blocks. They are expanded before the code block is parsed, so to the Lua interpreter the inline variables look like regular constants.


### Hints for using code blocks  ###


Most simple mathematical expressions work just like you'd expect them to. Operator precedence rules are those of regular arithmetic.

A code block should always return a string or numeric value, if it returns a boolean, a table or something else it might cause a warning and the resulting line containing the wrong output.

To create simple conditionals within code blocks you can use the `and` and `or` operators to chain values and conditions. For example:

    {\k**!(syl.duration>100) and "f" or ""!**$kdur}

If the syllable duration is longer than 100 ms the first sub-expression is true, and the code block returns <tt>"f"</tt>, otherwise the entire `and` expression is false, and the right-hand argument of the `or` expression is returned.

In Lua, `and` binds stronger than `or` meaning that `and` expressions are evaluated first. In the above expression the effective grouping is like this: `((syl.duration > 100) and "f") or ""`

[[!template id=Automation_navbox]]

