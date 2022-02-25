---
title: Autosave
menu:
  docs:
    parent: Miscellaneous
weight: 715
---

By default Aegisub automatically saves a backup copy of every subtitle file you
open, along with another copy every minute (if any changes have been made in
the last minute). These copies can be found in %APPDATA%\Aegisub\autosave on
Windows, ~/.aegisub/autosave on Linux, and ~/Library/Application
Support/Aegisub/autosave on OS X. In addition, they can be browsed directly
within Aegisub at File → Open Autosaved File...

![autosave-menu](/img/3.2/autosave-menu.png){: class="center"}

![autosave-dialog](/img/3.2/autosave-dialog.png){: class="center"}

Aegisub automatically cleans up old files in the autosave directory, so the
automatic backups should not be used for long-term storage of files.
