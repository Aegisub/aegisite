---
title: clipboard
menu:
  docs:
    parent: Lua Modules
weight: 6265
---

The `clipboard` module supplies functions for reading from and writing to the clipboard.

## Usage ##
Import this module with `clipboard = require 'aegisub.clipboard'`{:.language-lua}.

### clipboard.get() ###
Synopsis: `text = clipboard.get()`{:.language-lua}

Get the current contents of the clipboard as a string.
Returns `nil` if the clipboard does not currently contain text or if an error occurs.

### clipboard.get() ###
Synopsis: `clipboard.set(new_text)`{:.language-lua}

Set the clipboard contents to a string.
Returns true if the clipboard could be set, and false if an error occurred.
