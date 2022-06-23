---
title: clipboard
menu:
  docs:
    parent: lua-modules
weight: 6265
aliases:
  - /docs/latest/Automation/Lua/Modules/clipboard/
---

The `clipboard` module supplies functions for reading from and writing to the clipboard.

## Usage

Import this module with {{< lua `clipboard = require 'aegisub.clipboard'` >}}

### clipboard.get()

Synopsis: {{< lua `text = clipboard.get()` >}}

Get the current contents of the clipboard as a string.
Returns `nil` if the clipboard does not currently contain text or if an error occurs.

### clipboard.get()

Synopsis: {{< lua `clipboard.set(new_text)` >}}

Set the clipboard contents to a string.
Returns true if the clipboard could be set, and false if an error occurred.
