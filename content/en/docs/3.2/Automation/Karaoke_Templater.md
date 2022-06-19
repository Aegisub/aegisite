---
title: Karaoke Templater
menu:
  docs:
    parent: automation
    identifier: karaoke-templater
weight: 6100
---

**Karaoke Templater** is an [Automation]({{< relref "Automation" >}}) script that ships with Aegisub. Its
primary purpose is to help creating [karaoke effects]({{< relref "../Glossary/Karaoke_effect" >}})
with a specially designed template language. Karaoke Templater is already
installed and ready to use along with Aegisub.

## Tutorials: Introducing Karaoke Templater

- [A simple example]({{< relref "./Karaoke_Templater/Tutorial_1" >}})
- [Using math expressions]({{< relref "./Karaoke_Templater/Tutorial_2" >}})
- [Using multiple template lines](#)
- [More advanced effects with positioned syllables](#)

{{<todo>}}Plan more tutorials. Also actually write those above. {{</todo>}}

## Reference

- [Declaring template and code lines]({{< relref "./Karaoke_Templater/Declaring_template_and_code_lines" >}})
- [Rules for when and in what order templates are run]({{< relref "./Karaoke_Templater/Template_execution_rules_and_order" >}})
- [Template modifiers]({{< relref "./Karaoke_Templater/Template_modifiers" >}})
- [Inline variables (dollar-variables)]({{< relref "./Karaoke_Templater/Inline_variables" >}})
- [Rules for code blocks and code lines]({{< relref "./Karaoke_Templater/Code_lines_and_blocks" >}})
- [Contents of the code block/line execution environment]({{< relref "./Karaoke_Templater/Code_execution_environment" >}})

Also see the [`Automation/Lua/Modules/karaskel.lua`]({{< relref "Lua/Modules/karaskel.lua.md" >}}) section for more
information on what's in the `line` and `syl` variables, and more.

## For users of _multi-template_

If you have used the _multi-template_ script from Aegisub 1.10 you should
recognise several similar concepts in the karaoke templater, but there are also
several pitfalls. Some of them are:

- You no longer declare template lines in the Actor field but in the Effect
  field instead. You can also put much more than just `template` in there. Read
  the tutorials above for an introduction, or the reference below if you feel
  adventurous.
- Instead of using percent-signs to write Lua code blocks you use exclamation
  marks. So write `!$start+$i*30!` instead of `%$start+$i*30%`.
- The `A` global is gone, but `line` and `syl` are directly accessible. The
  escaped Lua code is no longer run in the true global environment but instead
  in its own environment, so clashes between your templates and Karaoke
  Templater itself is much less probable.
- The `return false` hack to cancel execution of a template no longer works.
  Neither does having multi-statement Lua blocks and returning from them in
  general. For the first purpose the `fxgroup` functionality has been
  introduced, and for your multi-statement needs code lines have been
  introduced.
- Instead of working with `newline` and `line` (for being-generated and
  original line) you now work with `line` and `orgline` for being-generated and
  original lines.
- The `retime` function has been introduced to make it much easier to control
  the start and end times of your generated lines.
- Lots of more fancy features. Check the tutorials or read the reference to
  learn about it all.
