---
title: "Five cool things in Aegisub that people aren't aware of"
contributors:
- "Unknown"
date: 2008-07-23T03:25:00.008+01:00
lastmod: 2008-07-24T04:24:27.700+01:00
weight: 50
tags:
- old-post
- aegisub
- tips
---
One thing that I've noticed while talking to users of Aegisub is that there are a number of features that people just don't realize Aegisub has. Here are five of them:

(Note: these tips apply to version 2.1.2.)

1. **Loading audio from a video file**
If you have a video raw that you're working on, and you're just going to be performing audio timing on it, you don't need to demux the audio from it. Provided that the video is in a format that Aegisub can work with (that is: most files on Windows), you can just go to Audio->Open File and pick the VIDEO file as the audio file to open (you will need to change the open dialog's default filter to show those files). Note that this is different from "Open Audio From Video", that just loads the audio from the currently open video file.

2. **Saving to non-ASS formats**
Aegisub's primary format is ASS (this is due to a few technical reasons, such as avoiding accidental loss of formatting information), so you can't easily save to other formats. But it's not impossible! If you go to File->Export..., you can tell Aegisub to save in other formats, such as SRT, SSA, or Adobe Encore. It's also possible to force the "Save As" dialog to save directly to those formats, if you tell it to use the right extension (i.e., tell it to save as "foo.srt" and it will save as SRT).

3. **Converting framerate with "Export"**
The Export dialog has a "Transform Framerate" filter. If you enable it, it can perform a VFR->CFR conversion on your file (useful for hardsubbing to decimated VFR files). However, it can also do CFR->CFR conversion, that is, "ramp" the file. This can be useful if you have e.g. NTSC subtitles and want to speed them up by 4% for a PAL video. In that case, you would set Input to 23.976 and output to 25.

4. **Saving screenshots**
Often, you might want to share a screenshot of a subtitle with somebody else. Aegisub has tools to help you do just that - right click the video display, and you will have an option to save the current frame as a PNG file, or copy it as an image to the clipboard.

5. **Copying to/from clipboard in plain-text**
If you want to share some lines with somebody over IRC or an IM program, or you want to copy from another file, it might be useful to know that Aegisub performs copy and pasting of lines as raw plain-text. So if you copy lines from Aegisub, you can paste them in any text medium, and vice-versa. The same is valid for Style lines.

