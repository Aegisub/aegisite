A module for interacting with the Aegisub application and UI.

{::type name='Command'}
A table which represents a command that can be invoked by the user via a
hotkey, a menu entry, or a toolbar button.

All of the function fields are called with a single argument (the current project context).
Except for the `run` function, this project context is immutable and trying to modify it will result in an error.
Functions for all of the fields except `run` are called very often and MUST run quickly.
Taking a millisecond on a large file is enough to cause noticeable delays.

#### Required

{::field name='name' type='string'}
Name of the command.
Need to figure out what sort of naming scheme to use (automatic prefix akin to old thing? leave it up to the author to make names unique?)
{:/field}

{::field name='display_text' type='string<br>function'}
User-visible name of this command.
This should be short (try to keep to a few words) and in command tense (i.e. "Do stuff", not "Does stuff").
If this is a function, it will be invoked with whenever the value is needed.
{:/field}

{::field name='run' type='function'}
The actual command processing function to run when the command is invoked.
{:/field}

#### Optional

{::field name='icon' type='?'}
Optional. Icon for the command. Maybe a filename? Base64 encoded png?
{:/field}

{::field name='menu_text' type='string<br>function'}
Text to show for this command in a menu.
This should be identical to `display_text` except for the addition of an accelerator key.
If it is not present `display_text` will be used for the menu text.
If this is a function, it will be invoked with whenever the value is needed.
{:/field}

{::field name='help_text' type='string<br>function'}
Help text shown for the command in the status bar when the user hovers the mouse over the menu item.
This should be a concise description of what the command does.
Try to keep it to at most 60 characters, as anything more than will fit is pointless.
If this is a function, it will be invoked with whenever the value is needed.
{:/field}

{::field name='validate' type='function'}
Function to call to determine whether or not the command can be run.
If it returns a falsey value (`nil` or `false`), any hotkeys for this command will be ignored, and it will be disabled (greyed out) in menus.
You do not need to perform the same validation in the processing function.
{:/field}

{::field name='is_active' type='function'}
Function to call to determine whether or not to display a check mark next to the command's menu entries.
{:/field}
{:/type}

{::type name='Subtitle Format'}
A table which represents a reader and/or writer for a subtitle format.

The example functions for this section describe a reader/writer for a tab-separated list of start time, end time, and line text, all in the ASS format.
The sample format has the following modules imported:

{::template name='luabox'}
local io = require 'aegisub.io'
local re = require 'aegisub.re'
local subtitles = require 'aegisub.subtitles'
local unicode = require 'aegisub.unicode'
{:/template}

#### Required
{::field name='name' type='string'}
I'm not sure what this is actually used for.
{:/field}

#### Required for Reader
{::field name='read_file' type='function'}
A function which reads a file in this reader's format.
It is passed an absolute path to a file and the file encoding to use, and should return an aegisub.subtitles.File object.

{::template name='luabox'}
local function read_file(reader, path, encoding)
  local ret = subtitles.File.create_default()
  local file = io.open(path, encoding)
  local splitter = re.compile('\t')

  for line in unicode.lines(file) do
    local fields = splitter:split(line)
    if #fields == 3 then
      file.append(file.Dialogue{start=fields[1],
                                end=fields[2],
                                text=fields[3]})
    else
      error(subtitles.BadFormatError('Invalid line: ' .. line))
    end
  end

  return ret
end
{:/template}
{:/field}

{::field name='read_extensions' type='function'}
A function which returns a table of file extensions, without leading dots, which this reader can read.

{::template name='luabox'}
local function read_extensions(reader)
  return ['tsv']
end
{:/template}
{:/field}

#### Optional for Reader
{::field name='can_read_file' type='function'}
A function which checks if this reader can read a file.
It is passed an absolute path to a file and the file encoding to use, and should return a boolean indicating whether the file is in this reader's format.
If not supplied, it is assumed that a reader can read any file with one of its extensions.
This only needs to check if the file is in the format supported by this reader, and not necessarily whether it's a valid file of that format.

{::template name='luabox'}
-- This is the default behavior if you do not supply this function
local function can_read_file(reader, path, encoding)
  for _, extension in ipairs(reader:read_extensions()) do
    if unicode.iends_with(path, '.' .. extension) then
      return true
    end
  end
end
{:/template}
{:/field}

#### Required for Writer
{::field name='write_file' type='function'}
A function which writes a file in this writer's format.
It is passed a file to write, an absolute path to write to, and the file encoding to use.

{::template name='luabox'}
local function write_file(writer, subs, path, encoding)
  local file = io.open(path, encoding, 'w')
  for _, line in ipairs(subs.dialogue)
    file:write_line(string.format('%s\t%s\t%s',
                                  line.start_time,
                                  line.end_time,
                                  line.text))
end
{:/template}
{:/field}

{::field name='write_extensions' type='function'}
A function which returns a table of file extensions, without leading dots, which this writer can write.

{::template name='luabox'}
local function write_extensions(writer)
  return ['tsv']
end
{:/template}
{:/field}

#### Optional for Writer
{::field name='can_write_file' type='function'}
A function which checks if a given path corresponds to this writer.
It is passed an absolute path to a file should return a boolean indicating whether the file's name suggests it is in this writer's format.
If not supplied, it simply checks if the file has one of this writer's extensions.

This is used to infer the subtitle format to use based on the extension the user gives the file rather than forcing the user to always pick one.
You will probably not need to ever override this function.

{::template name='luabox'}
-- This is the default behavior if you do not supply this function
local function can_write_file(writer, path, encoding)
  for _, extension in ipairs(writer:write_extensions()) do
    if unicode.iends_with(path, '.' .. extension) then
      return true
    end
  end
end
{:/template}
{:/field}

{::field name='can_save_file' type='function'}
A function which reports if a subtitles file can be losslessly saved in this writer's format.

If a user opens a subtitles file in a non-ASS format, Aegisub does not limit the user to the functionality supported by that format.
When they try to resave that file, Aegisub calls this function to check if the user has used functionality not supported by the format.
If they have, Aegisub asks them to save the file as ASS and use Export if they want to save the file in the original format.

You only need to implement this function if you support both reading and writing your format.
By default, this checks for the following:

1. Has the user customized the styles?
2. Has the user attached any files?
3. Has the user used any override tags?

If you support a mapping some override tags to your format, you should override this function to instead check for tags other than those.

{::template name='luabox'}
local function can_save_File(writer, subs)
  if #subs.attachments then return false end

  for _, style in ipairs(subs.styles) do
    if not style.is_default() then
      return false
    end
  end

  -- Actor and effect aren't considered very important
  -- so the default function doesn't bother checking
  -- for them.
  for _, line in ipairs(subs.dialogue) do
    if line.actor:len() ~= 0 or line.effect:len() ~= 0 then
      return false
    end
  end

  return true
end
{:/template}
{:/field}



{:/type}

{::function name='register_command' synopsis='app.register_command(command)'}
{:/function}

{::function name='register_subtitle_format' synopsis='app.register_subtitle_format(format)'}
{:/function}
