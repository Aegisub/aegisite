---
title: "Four years of Aegisub"
contributors:
- "jfs"
date: 2009-06-17T17:05:00.013+01:00
lastmod: 2009-06-17T17:05:01.016+01:00
weight: 50
tags:
- old-post
- aegisub
- history
- hollowpromises
---
Today it's just about four years since Aegisub was first conceived.

It was on the 17th of June 2005 in a private channel on the ChatSociety IRC network. We were discussing the various problems with making advanced typesetting in ASS subtitles and how poor the tools generally were.

The original name was Visual SSA, and it was originally just intended to be a tool to assist in doing typesetting. Yes, the visual typesetting tools we only got implemented somewhat in the more recent versions was the original *goal* of the program. General-purpose subtitle editing wasn't it.

It wasn't many days into development before video was shown.

[![](http://2.bp.blogspot.com/_mEftAG-ggZo/ShjG2SRC3XI/AAAAAAAAAE0/ZFdM2_SqOlE/s320/aegi_v001.png)](http://2.bp.blogspot.com/_mEftAG-ggZo/ShjG2SRC3XI/AAAAAAAAAE0/ZFdM2_SqOlE/s1600-h/aegi_v001.png)

At that point, showing video was all it did. As things went, basic loading, editing and saving of subtitles was added soon, and the interface started looking a lot like the current versions, but still not quite.

[![](http://2.bp.blogspot.com/_mEftAG-ggZo/ShjHuQxy4hI/AAAAAAAAAE8/YnpD9Jaa1hY/s320/aegi_v010.png)](http://2.bp.blogspot.com/_mEftAG-ggZo/ShjHuQxy4hI/AAAAAAAAAE8/YnpD9Jaa1hY/s1600-h/aegi_v010.png)

The important part here is what's above the subtitle editing area: Where the audio box sits today is space for a toolbox. The intention was to add visual typesetting tools there.

Of course, that never happened, and audio took over that place instead. In fact, the goal turned towards making a replacement for the subtitling program Medusa, which was popular then. (A few people are still using it today!) This is where the name of Aegisub comes from: Aegis is the shield of Athena, upon which Medusa's head was put after she was slain by Perseus.

[![](http://1.bp.blogspot.com/_mEftAG-ggZo/SjgTH1xvlYI/AAAAAAAAAFE/9PpA60JGcQg/s320/aegisub100.jpg)](http://1.bp.blogspot.com/_mEftAG-ggZo/SjgTH1xvlYI/AAAAAAAAAFE/9PpA60JGcQg/s1600-h/aegisub100.jpg)
Development went on, features were added, slowly we got more testers and went towards a relatively stable version. On December 27 2005, version "1.00 beta" was released, just a little more than 6 months after the first idea.

Development continued with regular "beta" releases.

We had the notorious version 1.06 with the "movax bug" in the installer: The installation script had a typo in it, which caused it to, instead of adding Aegisub to Windows' Add/Remove Programs list, clear most of the data for the list. After it was discovered, 1.06a was quickly released fixing just that problem, though several people had already been hit by it.

It was first at version 1.07 we went open source. At this point, development still happened on a private SVN server with no public access, and all bug reports and feature requests were taken on the forum. The source for both 1.07, 1.08 and 1.09 was distributed as part of the installer package, there was still no public repository.

However, soon after 1.09, we moved to a new host for source code repository, which allowed us to open up the repository for anonymous read access. It was also around this time we got a real bug tracker. The 1.10 beta was the first version released under fully open development, that happened on August 7 2006.

[![](http://1.bp.blogspot.com/_mEftAG-ggZo/SjgUeGqelYI/AAAAAAAAAFM/SxWm6n8Eu-g/s320/aegisub110.jpg)](http://1.bp.blogspot.com/_mEftAG-ggZo/SjgUeGqelYI/AAAAAAAAAFM/SxWm6n8Eu-g/s1600-h/aegisub110.jpg)
If you compare the screenshots of 1.00 and 1.10, you'll see not much had changed. There's a large number of changes you first notice when you dive into the menus, of course, but compared to what has changed since then, it's just tiny.

After 1.10, the plan first was to release 1.11, and that should be done before the end of the year. First, things went pretty smooth, but then new huge features started slipping in, they weren't stable, and thus the release slipped. Shortly after the new year passed, we decided the changes were big enough that we'd now call it 2.00 instead.

Now, the rest is almost history, but not quite.

Visual typesetting finally got added, the thing Aegisub (then Visual SSA) was first intended for, and pre-release upon pre-release was put out. In the end we decided there were far too many versions called "2.00 pre-release" to make releasing "2.00 final" feasible without confusing everyone, so we instead decided 2.2.0 would be the first version of Aegisub labelled as "stable", and we would release 2.1.x versions until then.

2.1.6 was released on November 26, 2008, which is soon 7 months ago. The good news: 2.1.7 is almost ready and you can expect it within a few days, and version 2.2.0 should be less than a month away!

[![](http://3.bp.blogspot.com/_mEftAG-ggZo/SjgdbOVkbvI/AAAAAAAAAFU/jj_0DSmg4h0/s320/aegiinstaller.jpg)](http://3.bp.blogspot.com/_mEftAG-ggZo/SjgdbOVkbvI/AAAAAAAAAFU/jj_0DSmg4h0/s1600-h/aegiinstaller.jpg)
The installer for Aegisub 1.00 was 2.82 MB, the installer for Aegisub 2.1.7 on Windows will be close to 24 MB. We've come a long way since that day in June 2005.


