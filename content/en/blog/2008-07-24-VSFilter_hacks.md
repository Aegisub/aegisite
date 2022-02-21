---
title: "VSFilter hacks"
contributors:
- "jfs"
date: 2008-07-24T15:00:00.006+01:00
lastmod: 2008-07-24T16:38:14.747+01:00
weight: 50
tags:
- old-post
- ass2
- tag tips
- vsfilter
- tips
- ass
---
There's lots of versions of Gabest's VSFilter subtitle renderer around, some people are even still using versions that are several years old and are missing features and bugfixes. There's cases of people still distributing these old versions around, sometimes as part of a package with other software such as [VirtualDub](http://www.virtualdub.org/).

Now it happens that some time in 2006, Gabest seems to have lost interest in working on VSFilter, so nothing has happened from his side, not even bugfixes. Fortunately VSFilter is open source, so we have picked it up and made a [fork](http://en.wikipedia.org/wiki/Fork_%28software_development%29). We have included both some existing bugfixes and improvements that existed as patches, and also made our own bugfixes and further improvements.

I'm going to talk about some of the improvements we have made throughout this post.


![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
First, I'm going to assume you're familiar with most regular ASS override tags, if not you can get a refresher in [our manual](http://aegisub.cellosoft.com/docs/ASS_Tags). Second, not all of these improvements are available in the version of VSFilter we ship with the current release (2.1.2) of Aegisub, but they should all be in the next one (which will be 2.1.3 or 2.2.0, depending on circumstances.)

![Four lines of text, each positioned 0.2 pixels further to the right, showing the effect of sub-pixel positioning](http://www.animereactor.dk/aegisub/blogimg/floatpos-demo.png)Sometimes you need sub-pixel precision when positioning text and drawings. Normally you've only been able to get this by setting the script resolution (PlayResX and PlayResY) to something larger than the video resolution, but the "float \pos" patch changes this. It allows you to use decimal/floating point numbers for positioning lines and gives you up to 1/8th pixel precision.

The image to the left shows four lines of text positioned at different X coordinates. You can see how they move ever so slightly, although not a full pixel.

![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
The tags **\fax** and **\fay** allow you to do *shearing* operations on your text. This is a bit like rotations, except that it's not. They are especially useful for doing perspective correction when you are typesetting signs rotated in 3D.

[![Demonstration of \fax and \fay tags](http://www.animereactor.dk/aegisub/blogimg/faxfay-demo-w400.png)](http://www.animereactor.dk/aegisub/blogimg/faxfay-demo.png)
![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
Shortly before Gabest dropped development of VSFilter, he introduced the "ASS2" format. This isn't very well known, and it only has minor changes over the original ASS format. One of the things was a new karaoke timing tag, **\kt**. While Aegisub can read ASS2 files it can't write them, so if you edit them in Aegisub you will lose some information. It doesn't have support for timing with the \kt tag either, but you can of course still use that and use all the additional features of ASS2 if you edit the file with a text editor.

So what *is* \kt? It's "set absolute timing", it allows you to move both back and forth in time of highlight without highlighting other syllables. It is probably best illustrated with an example:

```
{\kf10}ABC {\kt20\kf10}DEF {\kt10\kf10}GHI
```

When you render this example, you will first see ABC highlight. Then GHI will follow, because its highlight is set to start at time 10 by \kt. Finally, DEF will highlight because its start time was set to 20 by \kt. You can also use \kt to make karaoke syllables overlap in timing.

![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
Originally the **\be** tag (Blur Edges) only allowed blurring to be turned on or off, and was very "weak", the blur effect was hard to notice at all. We have updated it so it supports variable strength blur effects now, and you can also use it with \t to animate the blur strength.

Because \be doesn't look very high at high values we have also introduced the alternate **\blur** tag, which performs the blur effect using a two-pass gaussian blur algorithm. This gives a much nicer and wider blur, especially at high values.

![Demonstration and comparison of \be and \blur tags with different parameters](http://www.animereactor.dk/aegisub/blogimg/be-blur-demo.png)

I will discuss why \be and \blur are "blur edges" effects and not "blur everything" effects tomorrow.

![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
![Demonstration of \xshad and \yshad tags](http://www.animereactor.dk/aegisub/blogimg/xshad-yshad-demo.png)If you've ever wanted the shadow to be positioned differently than just "X down and X right", the **\xshad** and **\yshad** tags are probably just what you want. These work like \shad except that they set only the X or Y displacement. You can even use negative values with them!

![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
![Demonstration of \xshad and \yshad tags](http://www.animereactor.dk/aegisub/blogimg/xbord-ybord-demo.png)Finally there's the **\xbord** and **\ybord** tags. They can be useful for various things, but one of the intentions was to better support anamorphic video: The \xbord and \ybord tags allows you to control the border width in X and Y direction separately. You can even disable border in one direction entirely!

You can also combine this with strong \be or \blur and maybe some shadow for other interesting effects.

![-----](http://www.animereactor.dk/aegisub/blogimg/split-line.png)
Again, remember that many of these tags require a very new version of VSFilter. For example, the \blur tag was only added yesterday..! The next release of Aegisub will ship with a VSFilter version that supports all of them, so if you want to safe you can wait until then. If you're impatient, you can [follow development on the Aegisub forum](http://malakith.net/aegisub/index.php?topic=651.0).


