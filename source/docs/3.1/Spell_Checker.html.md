To help you with quality assurance of your subtitle scripts, Aegisub
features a complete spell checker. It uses the Hunspell library, which is
based on OpenOffice.org's MySpell, which means it's at least as good as one
you'd find in a sophisticated word processing program. It can be found in
the _Subtitles_ menu -> _Spell Checker_. It also spell-checks as you type
and can to some degree be controlled from the subtitle edit box's
right-click menu (see [[editing subtitles|Editing_Subtitles]]).

### The spell checker dialog ###
[[img/spell_checker.png]]{: class="center"}

The spell checker dialog will go through all misspelled words it can find in
your script. The area in the lower left of the box displays suggestions to
replace the misspelled word with; to the right there are a number of
buttons:

Skip Comments
: Skip over commented lines when looking for misspelled words. Useful
when your comments are mostly things like karaoke scripts or the
original script which you're translating to a new language.

Replace
: Replaces the found misspelled word with the chosen replacement. Note
that the list box can be double-clicked to do this as well.

Replace All
: Replaces _all instances_ of the found misspelled word _in the entire
script_ with the chosen replacement.

Ignore
: Ignore _this instance_ of the misspelled word, but continue to stop
on other places where this misspelling occurs.

Ignore All
: Ignore _all instances_ of this word for this spell-checking session,
but continue to check for it in the future.

Add to dictionary
: Add the found word to the dictionary so it will not be detected as
misspelled again. Note that it is currently not possible to remove
words added from within Aegisub.
{: class="dl-horizontal"}

At the bottom of the dialog box there is a dropdown box to choose the spell
checker language.

### Dictionaries ###
The Windows version of Aegisub comes with a US English dictionary.
Installers for many other languages are available [on our
website](http://www.aegisub.org/downloads/#dictionaries). If we don't
supply a dictionary for your language, check [Mozilla's set of
dictionaries](https://wiki.mozilla.org/L10n:Dictionaries), or simply
Google for "hunspell <i>&lt;language&gt;</i> dictionary".

The OS X version of Aegisub includes all of the dictionaries we have.

On Linux your distribution's package manager should have hunspell
dictionaries. You may need to set the [[dictionary
path|Options#interface]] to the location where they are installed; one
common location is `/usr/share/hunspell`.
