Aegisub uses a simple system for denoting file locations. Most pathnames in
Aegisub can be written starting with special variables that each refer to
specific locations. Note that path specifiers should always have a trailing
slash unless they are the entire path (i.e. ?scripta doesn't work).

* **?data**
:   The location where application data are stored. On Windows this is the
    installation directory (the location of the .exe). On Mac OS X this is
    inside the application bundle. On other POSIX-like systems this is
    `$prefix/share/aegisub/`.

* **?user**
:   The location for user data files, such as configuration
    files, automatic back-ups and some additional things. On Windows this
    `%APPDATA%\Aegisub\`, on Mac OS X this is `$HOME/Library/Application
    Support/Aegisub/` and on other POSIX-like systems this is
    `$HOME/.aegisub/`. In portable mode this is changed to ?data.

* **?temp**
:   The system temp directory. Audio cache and any required temporary
    subtitle files are stored here.

* **?local**
:   The local user settings directory. Cache files which should be
    persisted across runs, such as FFMS2 indexes and the fontconfig cache are
    stored here. %LOCALAPPDATA%\Aegisub on recent versions of Windows, and
    equal to ?user everywhere else.

* **?script**
:   Only defined if a subtitles file is open and saved somewhere, in which
    case it points to the directory the script is in.

* **?video**
:   Only defined if a video file is loaded. Points to the directory the
    video file in is. Do note that this is not a good place to save things with
    dummy video loaded.

* **?audio**
:   Only defined if an audio file is loaded. Points to the directory the
    audio file in is. Do note that this is not a good place to save things with
    dummy audio loaded.
