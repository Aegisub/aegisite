The fonts collector is an automated tool that finds all fonts used in the
current script, scans your system's fonts folder(s) and copies all the
relevant fonts to a destination of your choosing. The dialog box looks like
so:

<center>[[img/fonts_collector.png]]</center>

The collector can perform any of the following actions:

* **Check fonts for availability** - Checks the fonts folder(s) to see if
  you have all the fonts used in the current script, and that all fonts
  contain all of the required glyphs. Do note that for technical reasons, the
  collector can't detect or collect fonts that aren't actually installed (like
  for example fonts temporarily loaded by a Matroska splitter or a font
  viewing program).
* **Copy fonts to folder** - Copies all the fonts used on the current script
  to the given folder.
* **Copy fonts to subtitle file's folder** - Copies all the fonts used on the
  current script to the folder containing the subtitle file. This is
  equivalent to using the above option with the destination set to ?script.
* **Copy fonts to zipped archive** - Copies all the fonts used on the
  current script to a compressed .ZIP archive.

The fonts collector will output diagnostic information about its doings in
the lower half of the window.

