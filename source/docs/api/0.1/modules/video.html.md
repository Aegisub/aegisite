Import this module with `local video = require 'aegisub.video'`{:.language-lua}.

{::type name='VideoFile'}
A `VideoFile` is a read-only table of [`VideoFrame`](#videoframe) objects.
As with all lua tables, it is one-indexed and the number of frames can be read with `#file`.

{::template name='luabox'}
-- This opens a file named video.mkv, prints the frame count, and then
-- prints the timestamp and the min and max value of each color of each
-- frame.
local file = video.open('/path/to/video.mkv')
print("Number of frames:", #file)
for i, frame in ipairs(file) do
    print("PTS:", file.timecodes.time_at_frame(i))

    local min = frame.data[0]
    local max = frame.data[0]
    for y in 1 to frame.height do
        for x in 1 to frame.width do
            local pixel = frame.data[(y - 1) * frame.pitch + x - 1]
            if pixel.r < min.r then min.r = pixel.r end
            if pixel.g < min.g then min.g = pixel.g end
            if pixel.b < min.b then min.b = pixel.b end
            if pixel.a < min.a then min.a = pixel.a end
            if pixel.r > max.r then max.r = pixel.r end
            if pixel.g > max.g then max.g = pixel.g end
            if pixel.b > max.b then max.b = pixel.b end
            if pixel.a > max.a then max.a = pixel.a end
        end
    end

    print("min:", min.r, min.g, min.b, min.a)
    print("max:", max.r, max.g, max.b, max.a)
end
{:/template}

### Fields
All fields are read-only.

{::field name='width' type='int'}Width of the video in pixels.{:/field}
{::field name='height' type='int'}Height of the video in pixels.{:/field}
{::field name='keyframes' type='table'}
Table of int frame numbers which are keyframes.
{:/field}
{::field name='timecodes' type='Timecodes'}The video's timecodes/frame rate.{:/field}
{::field name='filename' type='string'}
Absolute path of the file (or dummy video URI used).
{:/field}
{:/type}

{::type name='Timecodes'}
{::function name='time_to_frame' synopsis="frame_number = fps:time_to_frame(time, rounding='EXACT'"}
Convert a time in milliseconds to a frame number.

{::arg name='time' type='number'}
Time in milliseconds.
Times outside the well-defined range (i.e. negative or after the end of the video) are legal and are handled as sensibly as possible.
{:/arg}
{::arg name='rounding' type='string'}
Rounding mode to use.
Must be one of 'EXACT', 'START', or 'END'.
EXACT gives the frame visible at the given time.
START gives the first frame which a line starting at the given time will be visible on.
END gives the last frame which a line ending at the given time will be visible on.

In general you should use START or END when converting the start or end times of a subtitle line to frame numbers, and EXACT for most other purposes.
{:/arg}
{:/function}

{::function name='frame_to_time' synopsis="time = fps:frame_to_time(frame_number, rounding='EXACT'"}
Convert a frame number to a type in milliseconds

{::arg name='frame_number' type='int'}
A frame number.
Frames outside the well-defined range (i.e. negative or after the end of the video) are legal and are handled as sensibly as possible.
{:/arg}
{::arg name='rounding' type='string'}
Rounding mode to use.
Must be one of 'EXACT', 'START', or 'END'.
EXACT gives the exact start time of a video frame.
START gives a time which a subtitle line should begin at to be first visible on the given frame.
END gives a time which a subtitle line should end at to be last visible on the given frame.

In general you should use START or END when setting the start or end times of a subtitle line, and EXACT for most other purposes.
{:/arg}
{:/function}

{::function name='write' synopsis="error = fps:write(filename)"}
Write the timecodes to a v2 timecodes file.

{::arg name='filename' type='string'}
The absolute path to write the keyframes to.
The directory must exist and the file must be writable.
{:/arg}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
{:/return}
{:/function}
{:/type}

{::type name='Frame'}
### Fields
{::field name='data' type='Pixel[]'}
A row-major array of [Pixels](#pixel) in the video frame.
As this is a C array, it is zero-indexed, not one-indexed.
{:/field}
{::field name='width' type='int'}The width of the video frame in pixels{:/field}
{::field name='height' type='int'}The height of the video frame in pixels{:/field}
{::field name='flipped' type='boolean'}
If true, the first row of data is for the bottom of the image rather than the top.
{:/field}
{::field name='pitch' type='int'}
The stride of the rows in the array.
This is often equal to `width`, but may be greater than `width` if there is padding at the end of the rows.
It will never be less than `width`
{:/field}
{:/type}

{::type name='Pixel'}
A single RGBA pixel in a video frame.
Note that this is a ffi struct, not a Lua table.

### Fields
{::field name='r' type='uint8_t'}Red channel{:/field}
{::field name='g' type='uint8_t'}Green channel{:/field}
{::field name='b' type='uint8_t'}Blue channel{:/field}
{::field name='a' type='uint8_t'}Alpha channel. 0 is opaque.{:/field}
{:/type}

### Functions
{::function name='open' synopsis='file, error = video.open(filename, track=0)'}
Open an video file.

{::arg name='filename' type='string'}
The absolute path to the file to open, or a dummy video URI.
{:/arg}
{::arg name='track' type='int<br>function'}
The track number to open.
0 (the default) opens the first video track; other numbers open the track at that index.

Alternatively, you can pass a function which will be called if there are multiple video tracks to choose between.
This function is passed the table of track names for video tracks in the file, and must either return an index in that table to open or `nil` to cancel.
If you simply want to ask the user, you can pass [`video.prompt_for_track`](#prompt_for_track).
{:/arg}
{::return name='file' type='video.File'}
The video file, or `nil` if an error occured or the user cancelled the loading.
{:/return}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
{:/return}
{:/function}

{::function name='prompt_for_track' synopsis='track_num = video.prompt_for_track(tracks)'}
Ask the user to pick an video track from several options.
This is the default behavior when a user opens an video file with multiple video tracks via the UI.
{::arg name='tracks' type='table'}Table of strings containing track names{:/arg}
{::return name='track_num' type='int'}Index of chosen track in `tracks` or `nil` if user cancelled.{:/return}
{:/function}

{::function name='read_keyframes' synopsis='keyframes, error = video.read_keyframes(filename)'}
Read a list of keyframes from a keyframe file.
Currently supported formats are Aegisub's keyframe format and xvid, divx, x264 and ffmpeg first-pass stats files.

{::arg name='filename' type='string'}
The absolute path to the keyframes file to open.
{:/arg}
{::return name='keyframes' type='table'}
A table of int frame numbers which are keyframes, or `nil` if an error occured.
The table may be empty.
{:/return}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
One and only one of `keyframes` and `error` will be non-`nil`.
{:/return}
{:/function}

{::function name='write_keyframes' synopsis='error = video.write_keyframes(keyframes, filename)'}
Write a keyframes table to a file in Aegisub's keyframe format.

{::arg name='keyframes' type='table'}
Table of frame numbers to write to the file.
{:/arg}
{::arg name='filename' type='string'}
The absolute path to write the keyframes to.
The directory must exist and the file must be writable.
{:/arg}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
{:/return}
{:/function}

{::function name='read_timecodes' synopsis='timecodes, error = video.read_timecodes(filename)'}
Read timecodes from an override file.
Currently supported formats are v1 and v2 Matroska timecodes.

{::arg name='filename' type='string'}
The absolute path to the timecodes file to open.
{:/arg}
{::return name='timescodes' type='Timecodes'}
A [Timecodes](#timecodes) object or `nil` if an error occured.
{:/return}
{::return name='error' type='string'}
The error message, or `nil` if no error occured.
One and only one of `timecodes` and `error` will be non-`nil`.
{:/return}
{:/function}
