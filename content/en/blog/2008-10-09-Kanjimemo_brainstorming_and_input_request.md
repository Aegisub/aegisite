---
title: "Kanjimemo brainstorming and input request"
contributors:
- "Unknown"
date: 2008-10-10T00:48:00.003+01:00
lastmod: 2008-10-11T03:56:18.338+01:00
weight: 50
tags:
- old-post
- kanamemo
- kanji
- katakana
- hiragana
- kanjimemo
- japanese
---
漢字メモ？

*[Text above added to try to attract some attention to this post]*

Ever since I've posted about [Kanamemo](http://www.aegisub.net/2008/07/kanamemo-tool-for-apprentice-weeaboo.html), there have been quite a few requests for a "Kanjimemo", a tool based on the same idea, but for Kanji.

Even before, I had considered writing something like that... But I never started because I couldn't quite figure out all the details on how it'd work. On this post, I'll talk about some of the ideas that I had for it. If you're interested in a "Kanjimemo", please leave your feedback and suggestions in the comments!

**Programming Language**

First of all, I'm not sure which programming language to write it in. At first, I considered C++, since that would be the easiest for me and allow the maximum flexibility, at least as far as PCs are concerned. The problem is that I'm already fairly experienced with C++, and so it wouldn't be much of a learning experience (which is always a plus :)) unless I went for Direct3D.

Then I pondered about Java: with all the cell phones supporting J2ME, it seemed like a good idea - Kanjimemo on the go? Great! The real problem came when I realized that J2ME is *REALLY* limited - you often have less than 1 MB of heap memory available (!) for your application, which makes a program like Kanjimemo almost impossible to implement. I also lack a J2ME-enabled cell phone, so I couldn't even work on a J2ME port right away.

A few other languages crossed my mind. C# is something that I've always wanted to learn, but its cross-platform support is quite bad (I'm looking at you, Mono). It's also much slower than Java. Python is another "to learn" language, but I question the sanity of doing complicated data analysis on such a high level and slow language... Plus all the horrible dependencies. Same goes for Ruby.

So, any thoughts on the "language barrier" might be useful.

**Basics**

On to how the program would ACTUALLY work... Learning kanji is nowhere as easy as learning kana. The problem with kanji is that most of them have multiple (typically two) readings, depending on the word... but some (like 日, one of the most basic kanji) can have many more. So my idea is to have an algorithm that works like this:

1. Select a group of five or so kanji for each level (like Kanamemo)
2. Mine EDICT for all words marked as [Common] that use that kanji
3. Perhaps attempt to extract the pronunciation of your kanji on that word? If that doesn't work, just go with individual words.
4. Create a list of all the different unique pronunciations and associated words.
5. Have the user learn all the unique pronunciations, preferably by using words that contain nothing but that kanji and kana.
6. If there's no word with that kanji by itself, make sure that the user already "learned" all the other kanji in the word displayed.

 Of course, steps 3 and 6 might be very tricky to code. All of this will require mining data from EDICT and possibly KANJIDIC. If it becomes necessary, I might use a SQLite database to store this information.

**Progression**
Progression would work similarly to Kanamemo, with a new set of 5 kanji unlocked with each memorized set. Ideally, the user could choose profiles to control the new kanji: perhaps follow the JLPT progression, or the japanese school system progression, or how common a given kanji is, or a combination of them (i.e. start with all JLPT4 kanji sorted by frequency, then all JLPT3 sorted by frequency, etc). The user should also be able to customize a list of kanji that he wants to learn.

Given this system, it'd be possible to simply consider kana as being kanji, and have the program work in the same way for those, so you'd be entering actual japanese words when learning kana. This has the advantage of making your japanese reading skill progress.

**Multiple fonts**
One problem that I noticed with kanamemo is that it was easy to just memorize the font glyph, as opposed to the more abstract shape of the kana. This could prove to be an issue with kana that are very different depending on how they're written (such as さ and ふ). This program would fix that problem by using different types of fonts (cursive, brush, type) randomly, or perhaps by forcing you to learn all the different variation before progressing.

**Translation**
Since the concept of the program is word-focused, it might feel strange to be learning how to read words without learning what they mean. If you're an anime watcher, then perhaps you already have a relatively big vocabulary of words, but you won't know all of them, and not everyone is an anime watcher. EDICT provides translations, but I'm not sure if just slapping the translations there will do any good... Thoughts on this?

**Voice**
Finally, it might be useful to have someone read the words out loud for you whenever you get them right. I'm not sure how hard it would be to add support for some third-party voice synthesizer, but it might be worth the trouble.

**Other ideas**
Perhaps the program should be designed to look more like a game? A little mascot cheering for you, a scrolling background, some background music? Perhaps this game could have multiple "stages" that you would do in alternating order: First learn to read the kanji, then what the word means, then perhaps a speed typing test? Maybe even a grammar test mode?

**Development**
Of course, what this needs the most right now are IDEAS! If you have any, please share them with us. If you know of somebody who might be interested in this sort of thing, link them to this page! If you want to help with the development itself, drop by IRC and let us know. The idea is that this should be an open, free project.

