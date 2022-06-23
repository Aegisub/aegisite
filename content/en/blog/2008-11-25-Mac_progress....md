---
title: Mac progress...?
slug: mac-progress
contributors:
  - jfs
date: 2008-11-25T01:41:00.004000Z
lastmod: 2008-11-25T01:55:34.392000Z
weight: 50
tags:
  - old-post
  - experimental builds
  - mac
aliases:
  - /blog/2008/11/mac-progress.html
---

We get asked "what about the mac version?" once in a while and yes, it's the eternal problem.

Aegisub can build on Mac and it can run, but unfortunately it's quite hard to make it useful, not to mention the numerous GUI bugs and glitches.

Tonight I managed to make my first running build of Aegisub for PPC (G4/G5) architecture which was (of course) the first thing people started screaming for when I put out my first Intel builds some time last year!

**So far this build is essentially useless!** It can't load video, can't load audio, has no Automation support, the libass build can't render anything (because Fontconfig is misconfigured) and even the PCM WAV audio provider that otherwise always works, won't. (The PCM WAV problem is due to endianness.)

If you really want to try it anyway, here's a download link: [aegisub-mac-r2486-stripped.zip](http://jfs.itcamefromjapan.net/aegisub/aegisub-mac-r2486-stripped.zip).

**Remember:** You have no right to complain about this build. I know it's horrible and useless and I'll try to make something better. This is just a proof of concept, it *is* (still) possible to get Aegisub on Mac and PPC.

Also, while it *does* run on Intel machines, it's quite slow, especially during startup, as it's not a Universal binary but a PPC-only one. Of course it's also possible to make an Intel version and it shouldn't be a major problem to lipo them together, I just haven't bothered to try yet.

There's no ETA for the next useful version. (But oh, by the way, I have added a new script to the SVN repository. It's called `make-app-bundle.sh` and can create Application bundles. Quite useful if you're building for Mac yourself! Yes I used it for this build.)
