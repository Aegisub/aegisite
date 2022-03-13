---
title: Why rendering \k and \kf effects is fast in VSFilter
contributors:
  - jfs
date: 2008-07-20T22:23:00.012000+01:00
lastmod: 2008-07-22T01:18:34.155000+01:00
weight: 50
tags:
  - old-post
  - vsfilter
  - vsfilter internals
  - karaoke
  - optimisation
---

*This is a repost of something I wrote earlier [on the AnimeSuki forums](http://forums.animesuki.com/showpost.php?p=1629372&postcount=72), in relation to a discussion of how much CPU time various kinds of karaoke effects take to render.*

This discussion only covers TextSub (VSFilter), I don't know what other renderers do and their use is still very limited. Also, everything that goes for \\k also goes for \\kf, \\K and \\ko. They use the same rendering technique.
This will also explain a funny "artifact" some karaokers might have seen when using \\kf with vertical karaoke.

First, while TextSub does have a function that should tell whether a line is animated or not (presumably so it could avoid re-rendering static lines for every frame) that function is empty, it just says "return true;", so every line is always considered animated, no matter what's in it.

Next, the way \\k effects are handled is using a "switchpoints" algorithm.
TextSub renders (up to) three different single-channel 6-bit bitmaps for each line, fill, border and shadow. (Border is Shadow minus Fill. Shadow is Fill "expanded" to give an outline.)
When the subtitle is to be painted onto the video, TextSub builds a list of switchpoints for each line component. A switchpoint has two parts: Colour (which includes alpha) and end-coordinate. The end-coordinate is which pixel index on the scanline the colour is valid up till.
(When a line has a vector-\\clip, the vector drawing is rendered as a fourth 6-bit image which is used to mask the other layers while painting.)

When there is no \\k effect, there is only one switchpoint for each component, which has the colour of it and the end-coordinate set to infinity (actually 0xFFFFFFFF).
When there is a \\k effect, the current position of the highlight is calculated for the frame, and a switchpoint is added at the right coordinate. This is very fast to calculate. The pixel size of every syllable is already known (because the rasteriser breaks the line into "words" at every change in formatting - \\k tags are formatting) and for \\kf effects, getting the position within the syllable is a matter of simple linear interpolation between the endpoints of the syllable.

Now for painting an actual component.
For every scanline of the component, loop over each switchpoint. For each switchpoint, paint its colour to the video frame, using the component as mask and optionally also masking with a vector-\\clip mask. When the endpoint of a switchpoint is reached, do the same for the next switchpoint, continuing where the previous one left off.
This is repeated for every scanline of the component. Also very fast.
(The case of just a single switchpoint, ie. no \\k effect, is questionably optimised by removing the switchpoints-loop. I think this in practice only saves a few hundred or maybe thousand machine instructions in total for each component, but I haven't checked the actual code.)

For the reason why \\k effects don't rotate when you use \\frz (and family): They are scanline-based and the switchpoints are assumed to always be on the same coordinate on every scanline. The switchpoints can't change between scanlines for the same component.

This should explain why \\k effects are fast to render, unlike many \\t-based effects. Using purely \\k-based karaoke effects is safe to do when softsubbing, any modern CPU should be able to render it, since it doesn't really take any more CPU than rendering static lines.
