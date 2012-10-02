The `clipboard` module supplies functions for reading from and writing to
the clipboard.

## Usage ##
Import this module with `require "clipboard"`.

### clipboard.get() ###
Synopsis: `text = clipboard.get()`

Get the current contents of the clipboard as a string. Returns `nil` if the
clipboard does not currently contain text of if an error occurs.

### clipboard.get() ###
Synopsis: `clipboard.set(new_text)`

Set the clipboard contents to a string. Returns true if the clipboard could
be set, and false if an error occurred.

[[!template id=Automation_navbox]]
