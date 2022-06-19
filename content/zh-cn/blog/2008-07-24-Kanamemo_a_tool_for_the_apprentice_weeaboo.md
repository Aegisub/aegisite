---
title: 'Kanamemo: a tool for the apprentice weeaboo'
contributors:
  - Unknown
date: 2008-07-24T03:24:00.006000+01:00
lastmod: 2008-10-16T01:07:57.655000+01:00
weight: 50
tags:
  - old-post
  - kanamemo
  - katakana
  - hiragana
  - utility
  - japanese
---

Back in 2006, when I decided to learn Hiragana and Katakana, I looked around for flashcard programs to help me in my task. After finding that none of them actually worked as I thought that they SHOULD, I decided to roll my own. The result is Kanamemo:

![](/img/blog/old/kanamemo.png)

It works by teaching you Hiragana and/or Katakana (at your choice) by "levels". Each level typically contains 5 different kana. It basically shows you a kana and asks you to enter its Hepburn roomaji transliteration. If you get it right, you get +1 point in it. If you get it wrong, you get -10 to it AND -10 to the one that you confused it with. Once all kana of a given level are at least at level 5 (or so, I don't remember the exact rules), you've learned them and it unlocks the next level.

It also never stops flashing old kana to you, but the probability of a given kana being picked is inversely proportional to how good you are at it - that way, it makes sure that you don't forget the ones that you learned earlier, while focusing on the ones that you struggle with.

I found that it works exceptionally well, and I could learn to read all of Hiragana and Katakana in 2 days, but if you're particularly diligent, you can probably do it in a day.

You can download a Win32 binary for it [here](http://www.malakith.net/amz/aegisub/kanamemo.exe). Please post a comment if you have any trouble with the runtimes (i.e. missing DLL errors, or "application hasn't been installed properly").

The source code for the program has been available at the Aegisub repository for a while. Here's a [link](https://github.com/Aegisub/kanamemo).

I have been meaning to write a similar tool for kanji+words (by mining data from EDICT and KANJIDIC), but my sloth has been preventing me from doing so.

\[EDIT\] If you want to build it natively on Linux, see [this](/blog/2008-10-10-kanamemo_on_linux/).
