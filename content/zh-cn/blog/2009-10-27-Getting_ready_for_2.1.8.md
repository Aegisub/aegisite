---
title: Getting ready for 2.1.8
contributors:
  - jfs
date: 2009-10-27T16:58:00.003000Z
lastmod: 2009-10-27T23:36:50.309000Z
weight: 50
tags:
  - old-post
  - future
---

It's been a little over three months since we released 2.1.7 stable, and we are happy to announce that version 2.1.8 is getting closer every day.

After we released 2.1.7 we split Aegisub development into two main branches: The stable branch where we apply bugfixes for the last stable version, and the development trunk where we work on grand new features.

For all of you not using Windows we also have some good news. Aegisub 2.1.8 is well on the way to become the first version we can call stable on Linux, FreeBSD and other UNIX systems. There's only a few build-system issues remaining to fix. (Unfortunately it isn't as well for the Mac version, more on that later in this post.)

More on what you can expect to see in 2.1.8 after the jump.

The perhaps most important bug-fix in 2.1.8 for many people will be for the issue hitting everyone on Windows 7: "Could not lock buffer for filling" when trying to play audio. It turned out to be a really silly problem, but now it's fixed.

Another problem a lot of people have had is opening high-definition video, getting cryptic "Failed seeking video" errors. It turns out this is caused by some very limited OpenGL drivers shipped by Microsoft that can't handle texture images larger than 1024x1024 pixels. If you install a graphics driver directly from your chip manufacturer (usually NVidia, AMD ATI or Intel) you should get a better OpenGL driver, but it can be tricky and might not always be possible. We do have a solution for this in our unstable branch, and if it doesn't break anything else we should get it into the 2.1.8 release.

We also fixed some issues with slow seeking in MKV files and opening files with Unicode filenames in FFmpegSource2, and some bugs in Automation 4 Lua. Notably, the new "relayer" and "restyle" functions in Karaoke Templater didn't actually work, they have been fixed.

There's more minor problems most of you probably haven't bumped into, you can see an overview of everything on the bug tracker: [Milestone 2.1.8 issues](http://devel.aegisub.org/query?group=status&milestone=2.1.8).

There are also some things we'd have loved to get in, but just aren't feasible. Some people have complained that the audio spectrum display is very slow, which is entirely true, but it turns out that fixing it causes an avalanche of other problems to pop up, and it's just such a major undertaking that it will never make it into the 2.1.x series of Aegisub. But you can be assured that there is a major rewrite of things under way, and it's *very* fast!

As mentioned at the beginning, it also seems like we won't be able to get a really stable version for Mac out in the 2.1.x line of Aegisub. The technical reason is that we use wxWidgets 2.8, which has some big problems on Mac in some core areas Aegisub depends on, and we can't switch Aegisub 2.1 to use wxWidgets 2.9 without causing a lot of new bugs to pop up. Our unstable development branch is using wxWidgets 2.9 however, and it's looking very good on Mac, but the changes required to support wxWidgets 2.9 in Aegisub were large enough that they aren't getting into Aegiub 2.1.
