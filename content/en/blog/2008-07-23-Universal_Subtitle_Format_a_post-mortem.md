---
title: 'Universal Subtitle Format: a post-mortem?'
contributors:
  - Unknown
date: 2008-07-23T01:36:00.011000+01:00
lastmod: 2008-07-23T02:38:21.267000+01:00
weight: 50
tags:
  - old-post
  - as5
  - usf
  - athenasub
  - history
  - xml
  - future
  - subtitle formats
  - ass
  - matroska
aliases:
  - /blog/2008/07/universal-subtitle-format-post-mortem.html
---

The Universal Subtitle Format (USF) was an ambitious project. It was a XML-based subtitle format, supposed to replace the old and problematic community standard, Advanced Substation Alpha (ASS). It was chosen as the default subtitle format for the [Matroska](http://www.matroska.org) multimedia container, and was the primary format of Medusa's unfortunate successor, ChronoSub.

It failed to achieve that goal.

This is what its page on CoreForge has to say:

> The format is based on XML for many reasons: flexibility, human readability, portability, Unicode support, hierarchical system and easier management.

While I can certainly understand "flexibility" and "portability", I don't see why you need XML to have a portable format, or Unicode support. But they go ahead and claim human readability and easier management. Is that supposed to be a joke? It sure is human readable - compared to binary formats. But it's still an incredibly verbose format that no sane person would try to edit by hand. And how is it easier to manage? Only if they mean that it's easier to avoid horribly misshapen subtitle files (you know, the kind of file that's always floating around the community and that VSFilter will happily eat). And what's with "hierarchical system"? It is true, but isn't it also completely irrelevant? Subtitles are NOT intrinsically hierarchical - forcing them to be only complicates matters.

But let's have a look at the format itself. This is a simple "Hello World" in USF:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- DOCTYPE USFSubtitles SYSTEM "USFV100.dtd" -->
<?xml-stylesheet type="text/xsl" href="USFV100.xsl"?>

<USFSubtitles version="1.0">

  <styles>
    <style name="NarratorSpeaking">
      <fontstyle italic="yes" color="#FFEEEE" outline-color="#FF4444"/>
    </style>
  </styles>

  <subtitles>
    <subtitle start="6.100" duration="4.900">
      <text style="NarratorSpeaking">This is a demo of<br/>The Core Media Player<br/>subtitle format</text>
    </subtitle>
    <subtitle start="00:00:11.000" stop="00:00:15.000">
      <text style="NarratorSpeaking">What can be done ?</text>
    </subtitle>
  </subtitles>

</USFSubtitles>
```

The above sample is the "official" sample included with the specs, stripped down to make a suitable "hello world". For comparison, I've re-created the script in ASS:

```plaintext
[Script Info]
ScriptType: v4.00+
PlayResX: 640
PlayResY: 480

[V4+ Styles]
Style: NarratorSpeaking,Arial,20,&H00EEEEFF,&H000000FF,&H004444FF,&H00000000,0,-1,0,0,100,100,0,0,1,2,0,2,10,10,10,0

[Events]
Dialogue: 0,0:00:06.10,0:00:11.00,NarratorSpeaking,,0000,0000,0000,,This is a demo of\NThe Core Media Player\Nsubtitle format
Dialogue: 0,0:00:11.00,0:00:15.00,NarratorSpeaking,,0000,0000,0000,,What can be done ?
```

**Note**: I removed the "Format:" lines from the above file. This is because, to the best of my knowledge, Sabbu is the only program that actually cares about those lines. Neither VSFilter nor Aegisub care if it's there or not, and both will, in fact, ignore it.

For further comparison, this is what the same script would look like in the current draft of AS5:

```plaintext
[AS5]
ScriptType: AS5
Resolution: 640x480

[Styles]
Style: NarratorSpeaking,,\i1\1c#FFEEEE\3c#FF4444

[Events]
Line: 0:00:06.10,0:00:11.00,NarratorSpeaking,,This is a demo of\NThe Core Media Player\Nsubtitle format
Line: 0:00:11.00,0:00:15.00,NarratorSpeaking,,What can be done ?
```

The first thing that we can notice there is that ASS is a much more "compact" format, and USF is more "readable" in the sense that you'll easily know what each thing does if you aren't familiar with the format - unless you are very familiar with the ASS format, the "Style" line should be incomprehensible. ASS is also more "horizontal" - that is, unless you cram things into the same line in USF, ASS will take less lines but those lines will be longer.

Here's the important point: USF is **NOT** designed to be written by hand. It's just too much effort to write all of that, and if you forget to close some tag somewhere, you'll break the entire file, which isn't an issue in an ASS-like format. And this is exactly where the problem is: there is no good editor that supports USF!

Lately, there has been a trend for XML-based subtitle formats. This is probably because XML is relatively easy to parse by a machine, and also because of the "buzz" associated with XML. But let's face it: subtitles are not best modeled by XML. The ASS format is a strange hybrid of an [INI file](http://en.wikipedia.org/wiki/INI_file), a [CSV list](http://en.wikipedia.org/wiki/Comma-separated_values), and [TeX](http://en.wikipedia.org/wiki/TeX), and that works astonishingly well - that's why we have decided to base AS5 on the same combination, although that is a subject for another post.

So here's the situation that USF faced: there was no real editor that could deal with it and nobody wants to write or maintain USF files by hand. Because of that, nobody actually uses USF, so there is no renderer that accepts it. Finally, USF offers very few real benefits over ASS, feature-wise. All in all, it just wasn't interesting to support it, and it faded into oblivion.

But here's an idea: Athenasub (the library that will be the backend of Aegisub 3.x series) will be completely format-agnostic. That would make it feasible to make Aegisub fully support USF, even its fanciest features, except that there is no renderer to display it. Should we bother? Is there still any interest in this format? At the moment, I have little interest in attempting to resurrect it (especially since we have our own plans with AS5), but if there is popular demand for it, I might reconsider. Last time I checked, not even the Matroska team seemed to care much for it anymore.

AS5. USF. And let's not forget Gabest's SSF. Do any of those formats have a future in the community? Or will fansubbers linger to ASS until the rest of their days?
