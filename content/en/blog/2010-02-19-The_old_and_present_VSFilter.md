---
title: 'The old and present: VSFilter'
contributors:
  - jfs
date: 2010-02-19T23:06:00.011000Z
lastmod: 2010-02-20T00:22:52.883000Z
weight: 50
tags:
  - old-post
  - as5
  - vsfilter
  - history
  - future
  - subtitle formats
---

A short while ago, yet another fork of the VSFilter subtitle renderer has surfaced, introducing more extensions. Let it be clear immediately: **Aegisub will not support any new extensions to the ASS subtitle format.** We strongly urge you to not use any extensions, and as for why, please read on.

Let's start with the history of the ASS subtitle format: In 2004, Gabest made the Guliverkli project open source under the GPL license. This corresponds to the version 2.23 of VSFilter, or VobSub as it was better known as then. By this time, the ASS format was essentially already in its final form, no real extensions ever came up then. That's more than 5 years ago. Around 2006-2007, the Guliverkli project mostly died off, almost no more development happened. However, a few patches started to crop up. In 2008, we made a fork for Aegisub, and ended up applying those existing patches, fixing a bunch of bugs and, unfortunately, also adding some new features. Very soon the Guliverkli2 project is forked off the Guliverkli project, and includes patches for all parts of it. The Aegisub patches are ported to Guliverkli2. Some more development happens, the Aegisub fork is abandoned in favour of Guliverkli2. The MPC-HC (Media Player Classic Home Cinema) project pops up, as a second fork of Guliverkli. They import most all the Guliverkli2 patches too, as well as add many major new features to Media Player Classic. Now, a new, fourth fork of VSFilter appears, and it has several new extensions.

The important part of the history is in the very beginning: The ASS subtitle format was essentially finalised in 2004. In retrospect, it was wrong to ever extend it, because it creates fragmentation. We regularly receive support requests from people who can't make VirtualDub render their subtitles correctly. The reason? They use TextSub 2.23, the version from 2004, which is clearly still in distribution from some sites. This only shows that changing and extending a standard after it has been finalised is a really poor idea, because old software will always be around.

We, as developers of Aegisub, have discussed the situation with the MPC-HC developers and the main libass developer, and all agree that extending the ASS format, or supporting any new extensions, is a bad idea, for the reasons of fragmentation of standards and backwards compatibility, and we strongly recommend staying away from any extensions to the ASS format. This in fact also includes the extensions introduced in 2008, namely: `\blur`, `\be` with parameter over 1, `\fax`, `\fay`, `\iclip`, `\xbord`, `\ybord`, `\xshad`, `\yshad`. — None of those tags are compatible with the 2004 versions of VSFilter, and if you use them, you have a great risk that your subtitles will just look wrong for some viewers.

Another thing we agree on is that the ASS subtitle format is in general bad and has many problems, and that the only solution is to draft and implement a new subtitle format, using our experience with subtitles and knowledge of how other projects for new subtitle formats have failed, to make a good subtitle format that supports what subtitlers want and need, is usable and editable and is supported across all relevant platforms.

For now, we have just one request: **Please do not use any extensions to the ASS subtitle format.**
