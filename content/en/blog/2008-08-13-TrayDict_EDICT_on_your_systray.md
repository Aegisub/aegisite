---
title: 'TrayDict: EDICT on your systray'
contributors:
  - Unknown
date: 2008-08-13T23:29:00.002000+01:00
lastmod: 2008-08-13T23:45:20.794000+01:00
weight: 50
tags:
  - old-post
  - kanji
  - katakana
  - hiragana
  - utility
  - traydict
  - dictionary
  - edict
  - japanese
  - roomaji
aliases:
  - /blog/2008/08/traydict-edict-on-your-systray.html
---

A while ago, I posted about [Kanamemo](/blog/kanamemo-a-tool-for-the-apprentice-weeaboo/), a tool that I made to help me learn Hiragana and Katakana. Another tool that I've made to help me in the learning of the Japanese language was TrayDict:

![](/img/blog/old/traydict.png)

TrayDict is a very simple application that sits on your systray until you bring it up with WinKey+Z. Then it lets you type a word in Kanji, Kana, Rōmaji or English, and it will search for it in EDICT (or any of the other supported dictionaries), returning every match, ordered by relevance.
The catch is: it's a complete hack. I made it in just a few days, without worrying at all about how well it'd work - I just wanted a tool for personal use. Even though I'm posting the link to it here, here are some things that you'll have to keep in mind:

1. It has a bug that prevents Windows from shutting down as long as it's running. Right click on it on systray and choose "Exit" to terminate it.
1. There are no options at all. The shortcut is WinKey+Z, and that can't be changed. You can also bring it up/down via systray.
1. This is no longer maintained, so don't bother sending bug reports and/or suggestions.

For a long time, I've been meaning to rewrite it, with less bugs, more customization, support for regular expressions, rendering with HTML+CSS, Kanji information, etc... But, alas, I wanted to use HTML to render this, and my experience with Trident, Gecko and WebKit were all catastrophic, so I've lost some interest. But maybe, if there is a demand for it, I'll pick this project up again.

Anyway, here is the Win32 binary: [Link](http://www.malakith.net/amz/aegisub/traydict.rar)
The source is available [here](https://github.com/Aegisub/traydict), but the HEAD is completely broken (result of my experimentation with Gecko), so you'll have to dig the repository for an older version.
