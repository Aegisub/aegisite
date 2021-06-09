---
title: Script Properties
menu:
  docs:
    parent: Miscellaneous
weight: 720
---

The **script properties** are some headers and other options that affect the
entire script in various ways. They can be accessed from the _File menu_ ->
_Properties_.

[[img/Properties.png]]{: class="center"}

The properties are:

* **Title**, **Original script**, **Translation**, **Editing**, **Timing**, **Synch point**, **Updated by** and **Update details** - These are for informational purposes only and do not affect rendering in any way. Set them to appropriate values if you find them useful.
* **Resolution**, **YCbCr Matrix**, **Scale border and shadow** - See the [[Script Resolution]] page for the meaning of these fields.
* **Wrap style** - Controls how the subtitle renderer will break lines that are too long to fit on one line. The modes are:

  * 0 - The default mode. "Smart" wrapping; if a line is too long to fit on a line by itself, breaks it into two roughly evenly long lines, but prefers the top line to be wider. <tt>\N</tt> (note capital N) can be used to insert a manual linebreak.
  * 1 - Inserts a linebreak when the line reaches the edges of the frame (minus margins); i.e. if it's just one word too long to fit on a line by itself, you get the last word all by itself on the bottom line. Almost never useful. As with 0, <tt>\N</tt> can be used for manual linebreaks.
  * 2 - No automatic linewrapping at all; if a line is too long to fit inside the video frame, it will just continue outside the frame. <tt>\n</tt> and <tt>\N</tt> can be used to insert manual linebreaks.
  * 3 - Same as mode 0, but prefers the bottom line to be wider. Note that for a long time VSFilter's implementation of this was buggy and would sometimes insert extra blank lines or have lines with a single word on them.

The wrapping mode should almost always be zero.
Mode two is sometimes useful for long lines which are scrolled or manually line-broken, but should be set on a per-line basis with the [[\q|ASS_Tags#\q]] tag.

