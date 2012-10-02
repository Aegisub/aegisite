This page describes the **subtitle file interface** use in Automation 4 Lua
scripts to manipulate subtitle files.

There is one special object (the **subtitles** user data object) which has a
number of functions, and a number of table formats defined.

## The subtitles object  ##
Most Automation 4 Lua feature functions are passed a **subtitles object** when
called. This object is used to obtain data from and manipulate the subtitles
the feature is being applied on.

A subtitles object can have two special properties depending on the context it
is created for:

**Read-only**
: Some feature functions must not be allowed to modify the subtitle file at
all. This includes for example [[macro validation
functions|Automation/Lua/Registration#macrovalidationfunction]] and [[export
filter configuration panel
providers|Automation/Lua/Registration#_export_filter_configuration_panel_provider]],
because this would be outside user expectations.

**Allow undo points**
: Only [[macro processing
functions|Automation/Lua/Registration#macroprocessingfunction]] can set undo
points, as it makes no sense to do so at any other time.

To allow the most flexibility, the subtitles object represents a complete ASS
format file, line by line, including all meta-lines such as section headers and
semicolon comments.

The subtitles object supports the following operations:

* Retrieve number of lines
* Read line
* Append line (to end of file)
* Insert line (at arbitrary position in file)
* Replace line
* Delete line
* Create undo point

These operations are described in detail below. In all operation synopses and
examples, `subtitles` is used for name of the subtitles object being operated
on.

### Retrieve number of lines  ###
Synopsis:

* `num_lines = #subtitles`
* `num_lines = subtitles.n`

This operation retrieves the total number of lines in the subtitle file
currently. This number only changes by using the other operations on the
subtitle object. It cannot change spontaneously during the execution of a
script.

**`num_lines`** (`number`)
: Number of lines in the subtitle file.

The first syntax is the preferred one, per normal Lua 5.1 coding style.

### Read line  ###
Synopsis: `line = subtitles[i]`

This retrieves the indexed line and creates a new table object with data about
it.

**`line`** (`table`)
: Table with data about the retrieved line.

**`i`** (`number`)
: Index into the subtitles file of the line number to retrieve. This is
one-based, i.e. the first line in the file has index 1.

Aegisub internally stores the subtitle file as a linked list, which means that
random access is slow, but sequential access is fast. While Automation 4 Lua
presents the subtitles as if it was an array, it internally maintains a cursor
used to optimise for sequential access. It is faster to access a line with an
index close to the one you last accessed than to access one further away. It is
always fast to access lines near the beginning or end of the file.

### Append line  ###
Synopsis:

* `subtitles[0] = line`
* `subtitles.append(line)`
* `subtitles.append(line1, line2, ...)`

Append one or more lines to the end of the subtitles file. In the first syntax,
it is the number 0 (zero) used for index. (Setting index 0 causes an append
operation.)

The third syntax supports appending multiple lines with one single operation.

**`line`** (`table`)
: The line object table to append to the subtitles file.

The latter function-call syntax is preferred for readability. The table index
setting syntax is slightly faster.

Appending a line always runs in constant time, and does not move the cursor
otherwise used to optimise sequential access.

### Insert line  ###
Synopsis:
* `subtitles[-i] = line`
* `subtitles.insert(i, line)`
* `subtitles.insert(i, line1, line2, ...)`

Inserts one or more lines into the subtitles file before the numbered line. In
the first syntax, you supply a negative index. E.g. to insert a line before
line 5 you supply index -5 (negative 5.)

Inserting lines will move lines after the inserted lines to move down in index,
such that old indexes will no longer be valid.

**`i`** (`number`)
: Index to insert before.

**`line`** (`table`)
: The line object table to insert into the subtitles file.

The latter function-call syntax is preferred for readability. The table index
setting syntax is slightly faster.

Inserting lines uses the list cursor and will move it.

### Replace line  ###
Synopsis: `subtitles[i] = line`

Delete the indexed line and insert the given line in its stead.

**`i`** (`number`)
: The line index to replace at.

**`line`** (`table`)
: The line object table to replace with.

Replacing lines uses the list cursor and will move it.

### Delete line  ###
Synopsis:

* `subtitles[i] = nil`
* `subtitles.delete(i)`
* `subtitles.delete(i1, i2, ...)`
* `subtitles.deleterange(first, last)`

Remove one or more from the subtitles file. All lines after the deleted line(s)
will move up to fill the deleted indexes, so old indexes will no longer be
valid.

The third syntax supports deleting multiple indexed lines in one call. The
indexes given must all be correct for the subtitle file's state before any
lines are deleted.

The fourth syntax deletes a range of lines, both indexed lines inclusive.

**`i`** (`number`)
: Index of the line to delete.

**`first`** (`number`)
: Index of the first line of the range to delete.

**`last`** (`number`)
: Index of the last line of the range to delete.

Deleting lines uses the list cursor and will move it.

### Creating an undo point  ###
Synopsis: `aegisub.set_undo_point(description)`

You should always create an undo point at the end of any macro which made
changes to the subtitles object. If you do not, one will automatically be set
for you, but in future versions of Aegisub this may change to rolling back any
changes made instead.

You can set multiple undo points in a single macro, but it is rarely a good
idea to.

Only available in macro processing functions, as it doesn't make sense anywhere
else either.

**`description`** (`string`)
: Text to appear in the Edit menu for the Undo and Redo items to describe the
action that can be undone.

This is not really a function in the subtitles object, but it is still closely
tied to it.

## Line data tables  ##
When you read lines from the subtitle file object they will always be one of a
few classes of lines, and when you write lines back to the subtitle file they
must also follow the format of one of those classes.

The line data objects are regular Lua tables with some specific fields defined.

Here's a list of the different classes of lines:

**`clear`**
: A blank line. These are normally stripped by Aegisub's ASS parser, but they
can potentially show up when importing non-ASS files, or if you add them via a
macro.

**`comment`**
: A line starting with a semicolon. Usually ignored and only useful for storing
unimportant metadata, as they're often stripped.

**`head`**
: A section heading in the file, such as `[Script Info]`

**`info`**
: A key/value pair in the Script Info section of the file

**`format`**
: A Format line in the file. Ignored by nearly everything as VSFilter never
implemented support for them.

**`style`**
: a regular style definition line

**`dialogue`**
: A dialogue line, which may or may not be a comment. These are the lines you
see in the grid in Aegisub.

**`unknown`**
: An unknown kind of line.

There's three fields that always exist in all line data tables:

**`class`** (`string`)
: The name of the class of line this is, see the list above.

**`raw`** (`string`)
: The raw text of the line, from first to last character on the physical line.

**`section`** (`string`)
: Which section of the file the line belongs to. If the line is placed before
the first section heading, this field is `nil`.

### `clear` class  ###
This class doesn't define any additional fields.

### `comment` class  ###
This class defines one additional field:

**`text`** (`string`)
: The text that follows the semicolon. Basically the same as the `raw` field
with the first character chopped off.

### `head` class  ###
The `head` class doesn't define any additional fields, but the `section` field
contains the name of the new section started.

### `info` class  ###
This class defines two additional fields:

**`key`** (`string`)
: The part of the line before the first colon, with leading and trailing spaces
removed.

**`value`** (`string`)
: Everything after the first colon on the line, also with leading and trailing
spaces removed.

### `format` class  ###
This class doesn't define any additional fields.

### `style` class  ###
This class defines a large number of additional fields. It's usually processed
by the _karaskel_ and modified a bit by that. See the _karaskel.lua_ section on
[[style tables|Automation/Lua/Modules/karaskel.lua#styletable]] for more
information about this class.

### `dialogue` class  ###
This class defines a large number of additional fields. It's usually processed
by the _karaskel_ and has many calculated fields added by that. See the
_karaskel.lua_ section on [[dialogue line
tables|Automation/Lua/Modules/karaskel.lua#dialoguelinetable]] for more
information on this class.

### `unknown` class  ###
No additional fields are defined by this class, due to its nature. This might
be things like files embedded into the subtitles. You shouldn't try to work
with these lines unless you really know what you're doing. Deleting, modifying
and inserting `unknown` lines has undefined consequences. (That means, even if
it works today it might not work tomorrow or in the next version of Aegisub.)

[[!template id=Automation_navbox]]
