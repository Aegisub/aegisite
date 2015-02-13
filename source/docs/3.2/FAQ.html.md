{::options toc_levels="2,3" /}

Aegisub常见问题解答 —— 不一定适合其他地方。

### 卡拉OK特效？ ###

参阅[[卡拉OK模版教程|Automation/Karaoke_Templater/Tutorial_1]]。

### 我能用Aegisub制作DVD字幕吗？ ###

不能直接做，不过有个不错的程序
[MaestroSBT](http://sourceforge.net/projects/maestrosbt/)，可以把SSA字幕转为VOBSubs。
它确实有很多关于标签和其他方面的限制， so reading its manual first is
advised. Also note that it does not accept ASS - only SSA. You can use
Aegisub's File -> Export... dialog to save real SSA files.

### Does Aegisub allow saving to SRT? ###

Yes, but only if it means that no information will be lost. In other
words, if you have any override tags that aren't \1c, \b, or \i,
Aegisub won't allow saving directly to SRT. However, you can still
export to SRT by using the File -> Export... dialog box. Just uncheck
all the checkboxes (clean script info, VFR transform etc.).

### I've found a bug!? ###

Report it on the [bug tracker](http://devel.aegisub.org/). Please
include as many details as possible in your report! Remember that if a
bug is not on the bug tracker, it _does not exist_ as far as we are
concerned.

### Why doesn't Aegisub have &lt;feature X&gt;? &lt;Program Y&gt; has it! ###

Quite possibly because we didn't know you wanted it. Request it on the
[bug tracker](http://devel.aegisub.org/) and see what happens.

### Where can I find more information and/or get help? ###

For Aegisub-related stuff, the [forums](http://forums.aegisub.org) and
the [IRC channel](irc://irc.rizon.net/aegisub) are good places to ask
questions. The Aegisub [devel wiki](http://devel.aegisub.org) also
contains some more obscure information not included in the manual for
various reasons, and so does the forums.  For general video-related
questions, [Doom9.org](http://www.doom9.org) and [its
forums](http://forum.doom9.org) is generally the place to go.

### Are there any VSFilter bugs I should know about? ###

In one word: [yes](http://asa.diac24.net/VSFilter#BUGS).
