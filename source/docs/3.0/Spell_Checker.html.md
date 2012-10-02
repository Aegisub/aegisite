To help you with quality assurance of your subtitle scripts, Aegisub
features a complete spell checker. It uses the Hunspell library, which is
based on OpenOffice.org's MySpell, which means it's at least as good as one
you'd find in a sophisticated word processing program. It can be found in
the _Subtitles_ menu -> _Spell Checker_. It also spell-checks as you type
and can to some degree be controlled from the subtitle edit box's
right-click menu (see [[editing subtitles|Editing_Subtitles]]).

### The spell checker dialog ###
<center>[[img/spell_checker.png]]</center>

The spell checker dialog will go through all misspelled words it can find in
your script. The area in the lower left of the box displays suggestions to
replace the misspelled word with; to the right there are a number of
buttons:

* **Skip Comments** - ignore misspelled words in commented out lines.
* **Replace** - replaces the found misspelled word with the chosen
  replacement. Note that the list box can be double-clicked to do this as
  well.
* **Replace All** - replaces _all instances_ of the found misspelled word
  _in the entire script_ with the chosen replacement.
* **Ignore** - ignores _this instance_ of the misspelled word.
* **Ignore All** - ignores _all instances_ of this word.
* **Add to dictionary** - adds the found word to the dictionary so it will
  not be detected as misspelled again. Note that it is currently not possible
  to remove words added from within Aegisub.

At the bottom of the dialog box there is a dropdown box to choose the spell
checker language.

### Dictionaries ###
Aegisub comes with a US English dictionary. Installers for many other
languages are available [on our
website](http://ftp.aegisub.org/pub/releases/dictionaries/). If we don't
supply a dictionary for your language, check [Mozilla's set of
dictionaries](https://wiki.mozilla.org/L10n:Dictionaries), or simply Google
for "hunspell <i>&lt;language&gt;</i> dictionary".
