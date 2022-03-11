---
title: "Don't use \\fad on fades to black"
contributors:
- "Unknown"
date: 2008-12-21T01:01:00.011Z
lastmod: 2008-12-21T01:31:55.795Z
weight: 50
tags:
- old-post
- tag tips
- vsfilter
- tips
- ass
- typesetting
---
Dear typesetters,

I have seen this countless times. Every time, it has bothered me. Please, don't do it anymore.

When the screen fades to black (or white, or any other solid colour, for that matter), DON'T use the \fad tag to fade the text along with it. When you use \fad, you're making the text translucent, and not darker. The result is that it will blend with the background - including all the usual associated bugs if you have borders and shadows - and get somewhat darker because the background itself is getting darker - it just won't get as dark as it SHOULD be, and the visual effect is that the text is getting brighter, relative to the background.

| ![](/img/blog/old/fade0.png) | ![](/img/blog/old/fade1.png) | ![](/img/blog/old/fade2.png) |
| --- | --- | --- |
| Original | With \fad | With \t(\c) |




As you can see above, the CORRECT way to deal with this is by using \t to animate the colour (all relevant ones) to black (or whichever colour the screen is fading to). Also note that the background can be seen through the text in the \fad() case, which is not the correct behavior.

Keep in mind, though, \t(\c) is significantly slower than \fad() on VSFilter, so you might have softsub issues, depending on how complex is your text.
