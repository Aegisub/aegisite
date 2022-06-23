---
title: Undocumented control
contributors:
  - jfs
date: 2008-09-10T17:27:00.003000+01:00
lastmod: 2008-09-10T17:36:50.052000+01:00
weight: 50
tags:
  - old-post
  - aegisub
  - tips
aliases:
  - /blog/2008/09/undocumented-control.html
---

First, let me apologise for the bad pun in the title up front.

There are a few undocumented/"secret" functions in Aegisub that can be activated by holding the Ctrl key (Command on Mac) while clicking on things. These aren't easter-eggs, just little things you may or may not need at times.

First thing is "play video without ensuring audio synchronisation". This is mainly a debugging function. If you hold the Ctrl key while clicking a Play Video button, a flag is set such that, during that playback, Aegisub doesn't attempt to keep the audio synchronised with the video by regularly seeking the audio if it gets too far away from the actual displayed video frame. This may be useful if you have a slow system that can't handle decoding and displaying some complex video in real-time.

Second is the Automation Manager toolbar button. If you hold Ctrl while clicking that, the Automation Manager will not open, but instead all scripts in the Autoload directories are reloaded instantly. The Autoload directories are also scanned for new scripts. If you hold both Ctrl and Shift while clicking the button, then every Automation script is reloaded. This can be really useful if you're working on a macro script and don't want to open Automation Manager every time you make a small change.

I think there might be some more hidden functions like these I'm forgetting, but those can be saved for another post another day ;)
