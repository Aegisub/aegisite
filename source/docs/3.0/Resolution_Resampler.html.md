The Resolution Resampler is a built-in tool designed to change the resolution
of the script while transforming all affected tags so it ends up looking the
same. It can also offset all margins (and absolute positions) by a specific
value. Uses include merging two scripts with different resolutions, converting
a script for a 4:3 video to its 16:9 equivalent, and converting between 1:1 and
anamorphic pixel formats.


## Overview  ##
<center>[[img/resolution_resampler.png]]</center>

There are two static boxes in the dialog, "margin offset" and "resolution". The
upper box controls how much you want to increase each margin by. The second box
indicates the final resolution to which the script is resized.

It's important to keep in mind that margin offset happens BEFORE the resolution
is changed, so the values are relative to the current script resolution. If you
check the "symmetrical" checkbox, then the left and right values will be
identical, and the same for top and bottom. Positive values indicate an
increase in margin (that is, subtitles farther from the video border), and
negative values a decrease.

After the margins were offset, the resolution is then resampled to the final
value provided. You can click the "From video" button to copy the actual video
resolution to the two fields. The "Change aspect ratio" check box indicates
whether the horizontal size of subtitles should be affected to conform to the
aspect ratio change. This is useful when converting between anamorphic and 1:1
formats.

## Examples  ##
### 4:3 SD to 16:9 HD  ###
For example, if you have subtitles typeset to a 640x480 video, and want to
apply the same subtitles to a 1280x720 video (which is widescreen, therefore
showing more video on the left and right margins), you would set margin left to
107, while leaving top at 0 and "symmetrical" checked. Then you would set final
resolution to 1280x720 (leave "Change aspect ratio" unchecked), and hit OK.

<center>[[img/Resample_diagram.png]]</center>

The above 107 value for the left/right margins was obtained with the following formula:

    (OrigH * FinalW/FinalH - OrigW)/2

Which results in:

    (480 * 1280/720 - 640)/2 = 107

