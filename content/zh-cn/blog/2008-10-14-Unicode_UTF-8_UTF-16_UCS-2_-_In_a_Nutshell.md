---
title: "Unicode, UTF-8, UTF-16, UCS-2 - In a Nutshell"
contributors:
- "Unknown"
date: 2008-10-14T22:57:00.004+01:00
lastmod: 2008-10-16T04:40:42.208+01:00
weight: 50
tags:
- old-post
- kanji
- aegisub
- katakana
- hiragana
- unicode
---
I have noticed that lots of people have no idea what exactly is the whole "Unicode", "UTF-8", "UTF-16" and "UCS-2" stuff, aside from the fact that it's somehow related to the display of foreign characters. The objective of this post is to briefly explain them and dispel some of the myths associated with them.

Unicode is a coding system used to represent characters from many languages (including Japanese and Chinese) without the need to change your language locale. If you've tried writing Kanji in Medusa, you know what I'm talking about. In Unicode, characters are given an unique number. For example, the capital letter "A" is U+0041 (65 in decimal), and the Hiragana "ふ" is U+3075 (12405 in decimal). Characters are divided into *planes* of 65536 characters for convenience. Almost all common characters are in plane 0 (also known as the Basic Multilingual Plane, or BMP), which goes from code points U+0000 to U+FFFF. All kanji are in planes 0 and 2.

UTF-8, UTF-16 and UCS-2 are simply techniques used to encode those values into text files. Windows helped create a myth that Unicode is UTF-16 by calling UTF-16 "Unicode" in applications such as Notepad - but the fact is that UTF-16 is as much Unicode as UTF-8 is.

UCS-2 (UCS = Universal Character Set) is an old encoding system that can store characters from the BMP by simply writing them as 16-bit values. The advantage of this system is that it's simple and covers most characters, but anything outside the BMP will fail catastrophically. That's why some Kanji have issues with some programs. An interesting consequence of UCS-2 is that it allows the mapping of characters that don't exist, such as the ones reserved for surrogate pairs (see the next paragraph).

UTF-16 (UTF = Unicode Transformation Format) builds on UCS-2. Indeed, for characters on the BMP, UTF-16 is identical to UCS-2; the difference lies in planes above the BMP. UTF-16 is capable of representing characters in planes 1 through 16 (even though no planes above 3 are specified yet) with a surrogate pair, that is, it uses two 16-bit values to store a character. This means that you can't measure the length of a UTF-16 string by counting how many 16-bit values it has!

UTF-8 is similar to UTF-16, but a character can be encoded as anything ranging from 1 to 6 bytes, although no character is mapped to anything that would be over 4 bytes long in UTF-8. Similarly to how UTF-16 is identical to UCS-2 for the BMP, UTF-8 is identical to Western encoding for the ASCII range (U+0000 to U+007F), making it "backwards compatible" with software that isn't Unicode-aware. It also means that text that is mostly composed of ASCII characters (such as, say, ASS subtitles) will be much shorter as UTF-8 than as other Unicode formats. That's why Aegisub uses UTF-8 as its standard format.

Regardless of encoding differences, UTF-8 and UTF-16 can both represent ANY Unicode character. UTF-16 can sometimes be shorter than UTF-8, but that will, in practice, never be the case for ASS subtitles, even if they are entirely written in Japanese/Chinese, due to all the ASCII text involved in the format syntax.

