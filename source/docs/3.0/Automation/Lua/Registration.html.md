**Registration** covers presenting your [[Automation 4 Lua|Lua]]
script to Aegisub, providing information about it and registering what
_features_ it provides.

## Features explained  ##

One of the primary concepts in Automation 4 is the _feature_. A feature is
something a script makes available for Aegisub to call back in response to a
user action.

A feature is not a plain callback. Rather, it's usually a set of several
callback functions as well as some information on how they should be
presented to the user in the GUI.

One feature is the **macro**. A macro is presented as an item in the
Automation menu. A macro has a name (the title show in the menu), a
description (the text shown on the status bar when hovering over the menu
item), a processing function (the function called when the user selects the
menu item) and an optional validation function (determines whether the macro
can even do any work in the current state.)

Another feature is the **export filter**. The export filter is presented in
the [[Export|Exporting]] dialogue and can be applied during an export
operation. Export filters also have a name, description, processing function
and then an optional configuration panel provider. The configuration panel
provider is a function that returns a configuration dialogue definition
structure which will be displayed in the Export dialogue when the export
filter is enabled. The settings filled into the configuration panel are
passed to the processing function when it is run.

## Script information globals  ##

A script can set a few global variables to provide metadata about the script
to Aegisub. The information given with these variables are displayed in the
[[Automation/Manager]] dialogue and the Script Info dialogue.

* **script_name** (string) - Name of the script. This should be short.
* **script_description** (string) - Description of the purpose of the
  script. Shouldn't be too long either.
* **script_version** (string or number) - Version number/name of the script.
  This is freeform; no specific meaning is assigned to this.
* **script_author** (string) - Author credits for the script.

All of these are optional; a script does not have to provide any of these.
If no script name is given, the file name is used instead for display
purposes.

## Registration functions  ##

The registration functions are the functions provided by Automation 4 Lua
you can call to make a feature available to Aegisub. You will usually call
these in the top level, at the very bottom of your script.

### aegisub.register_macro  ###

Synopsis: `aegisub.register_macro(name, description, processing_function, validation_function)`

Register a macro feature.

* **name** (string) - The name displayed on the Automation menu. This should
  be very short, try three words or less, and should be in command tense.
* **description** (string) - The description displayed on the status bar
  when the user hovers the mouse over the menu item. This should be a
  concise description of what the macro does. Try to keep it at most 60
  characters.
* **processing_function** (function) - The function that is called when the
  user selects the menu item. This must be a function with the [[macro
  processing function API|Automation/Lua/Registration#macroprocessingfunction]].
* **validation_function** (function, optional) - This function is called to
  determine whether the menu item should be available to the user or not.
  (Grayed out or not.) If no validation function is provided the macro is
  always available. This function must follow the [[macro validation
  function API|Automation/Lua/Registration#macrovalidationfunction]].

### aegisub.register_filter  ###

Synopsis: `aegisub.register_filter(name, description, priority, processing_function, configuration_panel_provider)`

Register an export filter feature.

* **name** (string) - The name displayed in the export filters list. The
  name should be rather short.
* **description** (string) - The description displayed in the description
  box when the user highlights the export filter in the Export dialogue.
* **priority** (number) - Determines the initial ordering of export filter
  application. Filters with higher priority are applied earlier than filters
  with lower priority. The user can change the filter application order in
  the Export dialogue. Priorities of the Aegisub built in export filters:

  * Transform Framerate = 1000 (karaoke effects should have higher priority
    than this)
  * Clean Script Info = 0 (your script might depend on the information
    cleaned by this)
  * Fix Styles = -5000 (should almost always run last)

* **processing_function** (function) - The function that is called when the
  user initiates the export operation. This must be a function with the
  [[export filter processing function
  API|Automation/Lua/Registration#exportfilterprocessingfunction]].
* **configuration_panel_provider** (function, optional) - A function that
  provides a configuration panel for the export filter. If this function is
  not provided the export filter will not have a configuration panel. This
  function must follow the [[export filter configuration panel provider
  API|Automation/Lua/Registration#exportfilterconfigurationpanelprovider]].

## Feature callback functions  ##

These are the callback functions you provide to the registration functions.

### Macro processing function  ###

Signature: `process_macro(subtitles, selected_lines, active_line)`

Macro processing functions passed to
[[`aegisub.register_macro`|Automation/Lua/Registration#aegisub.register_macro]]
must have this signature. The name `process_macro` is a placeholder for your
own function name.

* **subtitles** (user data) - The [[subtitles
  object|Automation/Lua/Subtitle_file_interface]] you use to manipulate
  the subtitles with.
* **selected_lines** (table) - An array with indexes of the selected lines.
  The values in this table are line indexes in the _subtitles_ object at its
  initial state. Only `dialogue` class lines can ever be selected.
* **active_line** (number) - The line that is currently available for
  editing in the subtitle editing area. This is an index into the
  _subtitles_ object. This line will usually also be selected, but this is
  not a strict requirement.

**Return value:**
The macro processing function can return up to two values: a new
`selected_lines` table containing indices of the lines to select after the
macro returns, and an index of the line to make the new `active_line`. If
set, the new active line index must be one of the lines in the new
`selected_lines` table.

### Macro validation function  ###

Signature: `validate_macro(subtitles, selected_lines, active_line)`

Macro validation functions passed to
[[`aegisub.register_macro`|Automation/Lua/Registration#aegisub.register_macro]]
must have this signature. The name `validate_macro` is a placeholder for
your own function name.

**Important, execution time:** Validation functions should always run very
fast. Do as little work as possible inside this function, because it is run
every time the user pulls open the Automation menu, and every millisecond
you spend in `validate_macro` is one millisecond delay in opening the menu.
Consider that the user might have very large files open. Don't block the UI.


* **subtitles** (user data) - The [[subtitles
  object|Automation/Lua/Subtitle_file_interface]] for the current subtitle
  file. This is **read-only**. You cannot modify the subtitles in the
  validation function, and attempting to do so will cause a run-time error.
* **selected_lines** (table) - An array with indexes of the selected lines.
  The values in this table are line indexes in the _subtitles_ object at its
  initial state. Only `dialogue` class lines can ever be selected.
* **active_line** (number) - The line that is currently available for
  editing in the subtitle editing area. This is an index into the
  _subtitles_ object.

**Return value:**
Boolean, `true` if the macro can run given the current
state of _subtitles_, _selected_lines_ and _active_line_, `false` if it can
not.

In addition to the primary return value, the validation function can return
a string. If it does, the description of the macro is set to the string.
This is intended for reporting information to the user about why the macro
cannot be run, but there may be more uses for it.

### Export filter processing function  ###

Signature: `process_filter(subtitles, settings)`

Export filter processing functions passed to
[[`aegisub.register_filter`|Automation/Lua/Registration#aegisub.register_filter]]
must have this signature. The name `process_filter` is a placeholder for
your own function name.

You do not have to worry about undo issues with export filters. You always
work on a copy of the subtitle file.

* **subtitles** (user data) - The [[subtitles
  object|Automation/Lua/Subtitle_file_interface]] you use to manipulate
  the subtitles with. This is a copy of the open subtitles file, so
  modifying this subtitles object does not modify the open file and will
  only affect the exported file.
* **settings** (table) - Configuration settings entered into the
  configuration panel or an empty table if there is no configuration panel.
  See the page on [[configuration
  dialogues|Automation/Lua/Dialogs]] for more information
  on the format of this table.

**Return value:**
Nothing.

### Export filter configuration panel provider  ###

Signature: `get_filter_configuration_panel(subtitles, old_settings)`

Export filter configuration panel providers passed to
[[`aegisub.register_filter`|Automation/Lua/Registration#aegisub.register_filter]]
must have this signature. The name `get_filter_configuration_panel` is a
placeholder for your own function name.

**Important, execution time:**
This function is called automatically when
the user opens the Export dialogue, and Aegisub blocks until it returns with
a configuration panel. Consider that the user might have a very large file
open, and that every millisecond spent creating your configuration dialogue
is one more millisecond the user has to wait for the Export dialogue to
open. Don't block the UI.

* **subtitles** (user data) - The [[subtitles
  object|Automation/Lua/Subtitle_file_interface]] for the current subtitle
  file. This is **read-only**. You cannot modify the subtitles in the filter
  configuration provider. Attempting to modify the subtitles will cause a
  run-time error.
* **old_settings** (table) - Previous configuration settings entered into
  the configuration panel, if any. When an Automation 4 export filter is
  run, any configuration settings are automatically stored to the original
  file. If any stored settings exist for this filter, they are passed as
  _old_settings_ so you can use them as a base for filling in defaults.

**Return value:**
A configuration dialogue table. See the page on
[[configuration dialogues|Automation/Lua/Dialogs]] for
more information on the format of this table.

[[!template id=Automation_navbox]]


