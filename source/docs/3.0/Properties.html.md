The **script properties** are some headers and other options that affect the entire script in various ways. They can be accessed from the _File menu_ -> _Properties_.

<center>[[img/Properties.png]]</center>

The properties are:

* **Title**, **Original script**, **Translation**, **Editing**, **Timing**, **Synch point**, **Updated by** and **Update details** - These are for informational purposes only and do not affect rendering in any way.
* **Resolution** - The virtual resolution of the script. Unlike the informational headers, this **does** effect rendering in several ways. It's recommended to set this to the same as the video resolution, or an even multiple thereof. It affects:

  * All coordinates (for margins, <tt>\pos</tt>, <tt>\move</tt>, vector drawing etc) are given in script resolution pixels.
  * All font sizes are scaled according to the script resolution.
  * If _scale border and shadow_ (see below) is enabled, all border and shadow values are given in script resolution pixels (if it is disabled they are in video resolution pixels instead).
  * Do however note that in a rather confusing manner, the script resolution does **not** affect the aspect ratio of any text, although it does affect the aspect ratio of vector drawings.

  <div></div>
* **Wrap style** - Controls how the subtitle renderer will break lines that are too long to fit on one line. The modes are:

  * 0 - The default mode. "Smart" wrapping; if a line is too long to fit on a line by itself, breaks it into two roughly evenly long lines, but prefers the top line to be wider. <tt>\N</tt> (note capital N) can be used to insert a manual linebreak.
  * 1 - Inserts a linebreak when the line reaches the edges of the frame (minus margins); i.e. if it's just one word too long to fit on a line by itself, you get the last word all by itself on the bottom line. Almost never useful. As with 0, <tt>\N</tt> can be used for manual linebreaks.
  * 2 - No automatic linewrapping at all; if a line is too long to fit inside the video frame, it will just continue outside the frame. <tt>\n</tt> and <tt>\N</tt> can be used to insert manual linebreaks.
  * 3 - Same as mode 0, but prefers the bottom line to be wider.

  <div></div>
* **Collision** - Determines how overlapping lines should be handled. In "normal" mode, the first line will stay where it is and the second one drawn above it. In "reverse" mode, the first line will be moved upwards and the second drawn under it.
* **Scale border and shadow** - Controls how outline and shadow widths are drawn. If disabled, they are given in video resolution pixels (meaning that using the script with a higher resolution video will make all borders/shadows look thinner). If enabled, they are given in script resolution pixels instead (meaning that outlines and shadows will look the same no matter the resolution). The latter is usually what you want.
<div></div>


