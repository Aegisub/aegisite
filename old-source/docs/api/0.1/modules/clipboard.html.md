The `clipboard` module supplies functions for reading from and writing to the clipboard.

Import this module with `local clipboard = require 'aegisub.clipboard'`{:.language-lua}.

{::function name='get' synopsis='text = clipboard.get()'}
Get the current contents of the clipboard as a string.
Returns `nil` if the clipboard does not currently contain text or if an error occurs.
{:/function}

{::function name='set' synopsis='clipboard.set(new_text)'}
Set the clipboard contents to a string.
Returns true if the clipboard could be set, and false if an error occurred.
{:/function}
