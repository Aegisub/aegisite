The Automation Manager window is used to view, load and unload
[[Automation]] scripts.

The Automation Manager window is opened from the _Automation_ menu or with
the [[img/Automation-toolbar-icon.png]] toolbar button.

[[img/automation_manager.png]]

## The script list  ##

The main area of the window is a list of all _script files_ loaded. It's
important to remember that one script file can contain several
[[features|Glossary/Automation_script_feature]], for example one script file
can define two [[macros|Glossary/Macro]] and one export filter.

Scripts can be loaded in one of two ways. In the screenshot above, most of
the scripts are _global_ (autoloaded), as indicated by the "G" in the
leftmost column. Global scripts are automatically loaded along with Aegisub.
They are put in one of the [[Automation_autoload_folders]]. You can not
unload global scripts; you must remove them from the autoload directory, and
then rescan the autoload directory.

The last script in the screenshot above is an example of the other type of
script: _local_ scripts, as indicated by the "L". Scripts added manually via
the Add button are local to the subtitle file being worked on, and are
automatically unloaded when the current subtitle files is closed, then
reloaded along with the subtitle file when you reopen it.

Sometimes a script is shown in red in the list. This only happens if the
script could not be loaded for some reason. The reason will usually be shown
in the Description column. If the description of the error is too long to
read, you can select the script and click the Show Info button to see it
all. Scripts failing to load should only happen if you are writing your own
scripts and manage to make a programming error.

## The buttons  ##

There are 6 buttons at the bottom of the Automation Manager window:

* The **Add** button is used to load a local script.
* The **Remove** button is used to unload a local script. It is only
  available when a local script is selected.
* The **Reload** button unloads and reloads the selected script file from
  disk. You can use this to reload scripts you're developing, but also see
  below for other ways to do this.
* The **Show Info** buttons shows detailed information on the selected
  script, as well as the entire Automation system.
* The **Rescan Autoload Dir** button scans the autoload folders to see if
  any scripts have been added or removed since Aegisub was started. All new
  scripts in the autoload directories are then loaded, scripts that have been
  removed are unloaded and all other global scripts are reloaded.
* The **Close** button closes the Automation Manager window.

## Other ways to reload scripts  ##

If you're developing scripts you might find yourself returning to the
Automation Manager often to reload your script. There are also faster ways
to reload scripts though:

* When the [[Export|Exporting]] dialog is opened all local scripts are
  reloaded. You can change this in the [[Options|Automation_options]]
  dialog.
* Hold the Ctrl key and click the Automation toolbar button to rescan the
  autoload folders.
* Hold both the Ctrl and Shift keys and click the Automation toolbar button
  to reload all scripts, also rescanning the autoload folders.
* While there is no default hotkey to reload all scripts, you can add one in
  the [[preferences dialog|Options#hotkeys]].

The Automation Manager won't open when any of there methods are used, but
you will get an error message window if a script failed to load. Note that
you can double-click on the rows in the error dialog for more information.

## For users of Aegisub 1.10 and earlier  ##

You may wonder where several of the functions that were previously in the Automation Manager have gone.

* The **Create** and **Edit** buttons were removed since they never worked
  fully as intended. You're encouraged to instead use your favourite file
  manager or editor to find and open the scripts you want to edit. Creating
  new scripts is also a bit easier since the formal requirements for
  Automation 4 scripts are much looser than for Automation 3 scripts.
  Another otherwise commonly used method to create new scripts is just to
  copy an existing script and edit that instead; the Create button wouldn't
  be much help there either way.
* The **Apply now** button was removed for two reasons. The first and most
  important is that it doesn't fit into the Automation 4 design at all. In
  Automation 3 every script file only did one thing so it was obvious what
  it meant to "apply" it. This isn't the case with Automation 4, one script
  file can have several functions (features), so which of them should be
  applied? The other, and rather minor reason, is that burying the button
  inside a dialog is just not a good place. You would have to cancel out of
  the Automation Manager window to undo the effect of the script if you
  decided you weren't satisfied, just to immediately return to it, reload
  the script and Apply again. The Automation 4 solution to this is to create
  a macro instead. It's available directly from the Automation menu and you
  can easily reload using one of the methods listed above.

[[!template id=Automation_navbox]]
