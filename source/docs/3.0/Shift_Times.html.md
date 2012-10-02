The **shift times** tool is a batch processor for timestamps; it adjusts the
start/end timestamps of many subtitle lines at once in various ways. It is
located under _Timing_ -> _Shift Times_.

It looks like this:

<center>[[img/shift_times.png]]</center>

The left part of the window contain the options.

### Shift by ###

These controls decide in which direction and by how much each timestamp will
be modified.

* **Time** - How much you want to adjust each timestamp, in
  hours:minutes:seconds.centiseconds.
* **Frames** - If you have video loaded, you can specify the adjustment time
  as a number of frames instead. Note that shifting by zero frames will snap
  the timestamps to the frame times without doing any shifting.
* **Forward** or **Backward** - controls in which direction the timestamps
  are adjusted.

### Affect ###

These controls decide what lines will be processed.

* **All rows** - Applies the time shifting to all lines in the script.
* **Selected rows** - Applies the time shifting only to the selected lines.
* **Selection onward** - Applies the time shifting to the first selected
  line and all lines below it (in the grid).

### Times ###

These controls decide what timestamps will be processed.

* **Start and End times** - Both start and end times of the affected lines
  will be modified by the given amount.
* **Start times only** - Only the start times of the affected lines will be
  modified. Note that this makes the lines longer (if you shift backwards)
  or shorter (if you shift forwards) and can even make them have a duration
  of zero.
* **End times only** - Only the end times of the affected lines will be
  modified. Note that this makes the lines longer (if you shift forwards) or
  shorter (if you shift backwards) and can even make them have a duration of
  zero.

Note that if a line is shifted so that its start or end time stamp would be
negative, that timestamp is zeroed instead. This can be used to clear all
timings from an entire script, by shifting backwards by longer than the
latest timestamp in the script.

### Load from history ###

This is a history of all time shiftings you have done since last time you
cleared the shift history (with the clear button). The format is a number of
fields separated by commas. The fields are:

* Filename of the script (e.g. "example.ass")
* Shift amount and direction (e.g. "0:00:05.00 forward")
* What times were affected, "s" for start, "e" for end, "s+e" for both
  What rows were affected; "sel start-end" for selections, "all" for all
  rows (e.g. "sel 1-40")

To load the settings from a history entry simply double-click it.
