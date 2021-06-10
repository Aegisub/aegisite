---
title: Typesetting Introduction
menu:
  docs:
    parent: Typesetting
    name: Typesetting Introduction
weight: 405
---

Wikipedia's definition of
[typesetting](http://en.wikipedia.org/wiki/Typesetting): "**Typesetting**
involves the presentation of textual material in graphic form on paper or some
other medium." In a subtitling context, this means three things:

* Presenting (a translation of) the spoken dialogue to the viewer in an easily
  readable and visually pleasing form.
* Translating any foreign-language background texts (such as episode titles,
  scene information like time/place and other plot-important writings on things
  in the background) and presenting the translation to the viewer, preferably
  so that it appears that the translation was there all along (yet retaining
  readability).
* Designing other texts (logotypes, karaoke, etc. etc.) that should be
  displayed on the video.

Particularly in the fansub community, the word "typesetting" usually refers to
the second or third of these three.

This page will attempt to give you an introduction to subtitle typesetting.
Unfortunately good taste is hard to teach, but we will do our best.

## Dialogue typesetting ##
The main goal of dialogue typesetting is **legibility**; everything else is
just icing on the cake. There's no point in having subtitles if the viewer
can't read them. Remember that subtitles frequently require quite fast reading,
so ease of recognition is vital. Some guidelines for good legibility:

* Use a plain, uncluttered, no-nonsense typeface. Sans-serif fonts (or if you
  insist on serifs, "slab serif" fonts) are generally preferable, especially at
  low video resolutions, since the serifs tend get blurred out, which naturally
  looks bad. Too thin fonts are also to be avoided. Small caps fonts are bad
  because the ascenders/descenders of  help recognition of words. Using tried
  and trusted faces such as Helvetica, Arial or Verdana is not a bad thing; if
  you want something that looks less "boring" but still readable try a
  sans-serif font of the "humanist" variety, such as Calibri.
* Use a well-defined but not too thick border. The color is important; the
  higher the contrast against the main color the better. The white main
  color/black border combo is well tried and trusted. Shadow is optional; if
  you use it consider setting it to half-transparent black; solid black tends
  to hurt legibility.
* Use big friendly letters with comfortable margins; usually subtitles need to
  be bigger than you think to be easily readable, particularly on a TV screen
  (since the viewing distance on a TV is usually 2-3 meters, compared to
  0.3-0.6m for a computer screen). If you plan on showing your subtitles on a
  TV you also need to take [overscan](http://en.wikipedia.org/wiki/Overscan)
  into account; Aegisub has an overscan mask feature (see [working with video]({{< relref "Video" >}})) that can help you with this. Even if the end result isn't
  going to be viewed on a TV, subtitles which are in the overscan area are
  usually not very readable anyway. Also consider the aspect ratio of the
  video; 16:9 or wider aspect ratios give you the opportunity to have longer
  lines at the expense of vertical space.
* Make sure that no more than two lines of text are visible at a time
  (exceptions can be made at times where there are a lot of people talking at
  the same time). Sometimes you can compress the text horizontally a bit to
  squeeze it in; at other times you just have to split the text block into two
  different lines and display one after the other.

{{<todo>}}examples {{</todo>}}

## "Sign" typesetting ##
Sign typesetting (translating various background text) can usually be
accomplished with ASS, but for more complex effects commercial programs like
Adobe AfterEffects are sometimes used, since the holy grail of sign typesetting
is to make the subtitle look like it's a part of the image that was always
there. How to get there from here will not be discussed in detail on this page
(see the [typesetting tutorial]({{< relref "Visual_Typesetting" >}})), but here are some
pointers:

* Is the sign actually important to the plot? Trying to translate every single
  bit of text displayed on screen will rapidly make you go insane, and the end
  result will often be unreadable anyway.
* Frequently, the text of a plot-important sign (such as a letter) is actually
  read out loud in the dialogue; if this is the case you should consider
  skipping the sign typeset because having both text and dialogue may overload
  the viewer with information. You should not typeset a sign just to show off
  that you're capable of doing so.
* Will you be able to make the translation easily legible? For example, if you
  have very little space available to squeeze it in on, consider putting a
  translation note as a normal "toptitle" instead.

{{<todo>}}images {{</todo>}}

## Further reading ##
The Wikipedia page on [typography](http://en.wikipedia.org/wiki/Typography) has
a lot of useful links and explanation of various typesetting-related terms.
