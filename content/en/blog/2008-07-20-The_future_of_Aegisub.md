---
title: The future of Aegisub
contributors:
  - Unknown
date: 2008-07-20T17:12:00.007000+01:00
lastmod: 2008-07-22T01:20:17.173000+01:00
weight: 50
tags:
  - old-post
  - as5
  - aegisub
  - osx
  - linux
  - athenasub
  - future
  - unix
aliases:
  - /blog/2008/07/future-of-aegisub.html
---

Greetings to all readers, and welcome to our new blog!

I'm Rodrigo Monteiro (a.k.a. amz) and I've founded the Aegisub project together with Niels Hansen (jfs). Although I've written a good portion of all the code, lately real life has decided to get in my way and I haven't been contributing much - which is part of the reason why development has been slow.

But, to get to the point, this is what we're planning for the future of Aegisub:

1. We want a stable 2.2.0 release ASAP. Nobody should be using 1.10 anymore.
1. We want proper Linux, \*BSD and OS X support. Although those three platforms work to varying degrees, Aegisub still works better in Windows.
1. A major infrastructure review, which will decouple all the subtitle parsing and manipulation into an external library tentativelly named Athenasub.
1. Implement even more features!
1. AS5.

I think that we're very close to point #1, and that depends mostly on jfs finishing the manual. On the UNIX front, we have verm porting the program to accomplish #2, but we still need more C++ developers to work on the actual features that don't work too well there - TheFluff has been trying to fix LAVC support, which is very problematic.

Point #3 is largely my responsibility. Athenasub will be a standalone C++ library that will load, manipulate and write subtitle files in many formats (all that Aegisub supports now, plus new formats, including image-based). It will probably also support some form of script similar to Avisynth, which could be used to edit individual subtitles from command line or do whole batches at once. While the library itself is coming along nicely, integrating it into Aegisub will be extremely difficult, but will hopefully make the program more stable and easier to understand (source-wise). It will also warrant a major version change, so look forward for that in 3.1.x.

Point #4 includes all those features that we've always wanted but never got around implementing... gradient and blur visual typesetting tools, a bleed checker, a script analyzer (that will search for any potential issues and display all of them in a list, with support for automation plugins), a character counter, and a few others.

Point #5 is probably the farthest in the future. AS5 is a subtitles format that is intended to replace the Advanced Substation Alpha (ASS) format, by adding many critical new features while overall simplifying the format. A draft specification is available [here](https://spaceboyz.net/svn/aegisub/trunk/specs/as5/as5.pdf), but beware that it will certainly change much before it sees the light of day.

This is all that I can think of now. Perhaps jfs will have some more to say regarding his plans for the future of the program. Either way, I intend to detail those points more carefully in posts to come, so stay tuned.
