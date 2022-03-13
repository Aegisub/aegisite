---
title: Kumaji explained
contributors:
  - jfs
date: 2009-02-10T02:59:00.013000Z
lastmod: 2009-02-21T13:30:17.177000Z
weight: 50
tags:
  - old-post
  - vsfilter
  - kumaji
  - future
  - subtitle formats
---

Kumaji is an advanced subtitle rendering engine, in development.

At the time of writing this, Kumaji does not render any subtitles whatsoever and is in general in a very early stage.

There are several reasons I started the Kumaji project, I will try to cover them in this post.

**The name**

First what does "Kumaji" even mean? It's derived from Japanese where it would be written クマジ. If you reverse that, you get ジマク, "jimaku" (字幕), which means subtitles. Also, Kumaji can be understood as 熊字, "bear" + "writing", hence Kumaji has a bear for a mascot! (Lots of people have suggested using Pedobear, this is wrong, I don't want to have that association.)

"Kumaji" should be reasonably easy to pronounce for most people and as far as I know it doesn't have the potential to offend people, like "libass" might have. The name is also format-agnostic like the actual renderer will be.

**The goals**

The key goals are:

1. Portable code without sacrificing compatibility

1. Maintainable and hackable code

1. Speed

1. Flexibility

Portability is the first and foremost goal. All current subtitle renderers have major problems with this. Those that do compile and work on multiple platforms (*libass* and the abandoned *asa*) are strongly tied to details of text and font handling on UNIX-like systems, which means they fail on Windows and Mac platforms because those have much different ways of handling fonts which FontConfig doesn't wrap properly or over-complicates. The result is very sub-optimal. VSFilter depends on not just Win32 (and Wine doesn't implement everything it requires yet) as well as MFC and COM. Perian's subtitle rendrer is Objective-C and entirely dependant on Cocoa text API's. Kumaji will achieve portability by plugging in platform-specific code where appropriate. The motto would be *doing the right thing on each platform, whatever the cost*.

Maintainable and hackable code is important. It must be possible to jump into the code without having a great understanding of the entire system beforehand, and it must be possible to learn good techniques from reading the code. The code must be well-commented or self-explanatory all around. (Portions of the code with poor, little or no explanations should be treated as bugs and reported.) VSFilter is a prime example of how I do not want the code to end up.

Speed is obviously important, to a certain degree. Reasonable subtitle scripts should render in realtime so Kumaji can be used for softsubbing. This may mean writing some critical routines in multiple versions optimised for different systems, using SIMD intrinsics or hand-optimised assembly code. However, good algorithms and data structures still take priority over SIMD and assembly tricks.

Finally, Kumaji must be flexible. It should be possible to implement support for new subtitle formats without providing more than a parser for them. If a format requires special rendering support not present, it must be possible to add that without taking the entire system apart and jeopardising the previous goals. It should also be possible to use Kumaji as a framework to write custom special-purpose renderers. For example, one can imagine creating a Lua interface for Kumaji's internal functions and use that for scripting advanced karaoke effects.

**Help wanted!**

Currently, Kumaji is pretty much my own pet project, but I would really like to have some help. What's needed right now is data structure design. If you want to help I expect you to have some knowledge of digital typography, the intricacies of Unicode complex scripts and the Bidi algorithm, OpenType, as well as general data structure and algorithm design. Or you should be have or be able to take an interest in those topics and read lots and lots about them! (It's interesting stuff, really!)

Kumaji is being written in C++ using just the STL (no TR1 libraries, boost or otherwise) so if you want to help reviewing or writing code you should be familiar with that.

The project is being hosted at SourceForge.net under the name [kumaji](http://sourceforge.net/projects/kumaji/).
