Import this module with `local audio = require 'aegisub.audio'`{:.language-lua}.

{::type name='File'}
{::template name='luabox'}
>>> file = audio.File.open('audio.mp3')
>>> file.provider
{:/template}

### Class Methods
{::function name='open' synopsis='file, error = audio.File.open(filename, track=0)'}
Open an audio file.

{::arg name='filename' type='string'}
The absolute path to the file to open, or a dummy audio URI.
The dummy audio URI format is currently undocumented due to that it's mostly unimplemented.
{:/arg}
{::arg name='track' type='int<br>function'}
The track number to open.
0 (the default) opens the first audio track; other numbers open the track at that index.

Alternatively, you can pass a function which will be called if there are multiple audio tracks to choose between.
This function is passed the table of track names for audio tracks in the file, and must either return an index in that table to open or `nil` to cancel.
If you simply want to ask the user, you can pass [`audio.prompt_for_track`](#prompt_for_track).
{:/arg}
{::return name='file' type='audio.File'}
The audio file, or `nil` if an error occured.
{:/return}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
One and only one of `file` and `error` will be non-`nil`.
{:/return}
{:/function}

### Fields
All fields are read-only.

{::field name='channels' type='int'}
Number of audio channels.
Will currently always be 1 due to that Aegisub automatically downmixes all audio to mono.
This may change in the future.
{:/field}
{::field name='sample_count' type='int'}
Number of audio samples in one channel of the file.
{:/field}
{::field name='bytes_per_sample' type='int'}
Bytes for one sample of one channel.
Will currently always be 2 due to that Aegisub automatically converts all audio to 16-bit signed.
This may change in the future.
{:/field}
{::field name='filename' type='string'}
Absolute path of the file (or dummy audio URI used).
{:/field}

### Methods
{::function name='get_data' synopsis='data = file.get_data(start, count)'}
Get a block of audio data.
If `start` or `start + count` are out-of-bounds, the missing portions of the audio will be zero-filled.

{::arg name='start' type='int'}Sample offset to begin reading from.{:/arg}
{::arg name='count' type='int'}Number of samples to read.{:/arg}
{::return name='data' type='uint8_t[]'}ffi array of sample data.{/:return}
{:/function}
{:/type}

### Functions

{::function name='prompt_for_track' synopsis='track_num = audio.prompt_for_track(tracks)'}
Ask the user to pick an audio track from several options.
This is the default behavior when a user opens an audio file with multiple audio tracks via the UI.
{::arg name='tracks' type='table'}Table of strings containing track names{:/arg}
{::return name='track_num' type='int'}Index of chosen track in `tracks` or `nil` if user cancelled.{:/return}
{:/function}
