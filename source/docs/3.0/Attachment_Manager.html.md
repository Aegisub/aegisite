[[!template id=toc depth=2]]

The attachment manager allows you to attach fonts and/or pictures to your
script (by encoding them as text). This is occasionally useful for sharing
fonts between everyone who is working on a script without having to send the
fonts as separate files. However, it is quite limited and is prone to causing
problems.

## Overview  ##
<center>[[img/Attachment_list.png]]</center>

The entire dialogue is fairly self-explanatory. The two "Attach ..." buttons
add attachments, "Extract" extracts existing attachments into separate files,
and "Delete" deletes attachments from the subtitles file.

## Limitations and downsides  ##
### Supported formats  ###
The SSA format specification only allows certain filetypes to be attached. For
fonts, only .ttf is allowed. For pictures, .bmp, .gif, .ico, .jpg and .wmf are
allowed (note the absence of .png). None of the SSA commands which _use_ the
images are implemented in anything but SubStation Alpha, so it is very unlikely
that attaching pictures is actually a useful thing to do.

### Compatibility issues  ###
Many SSA/ASS editors ignore or strip attachments. The original SubStation Alpha
(v4.08) will work fine, but only for real SSA files. Sabbu will complain about
unrecognized fields, and strip the attachments if you save the file. Most other
editors either ignore the attachments or crash when encountering them.

A notable exception is mkvmerge, which will convert the attached files to
Matroska attachments on muxing. If you demux the script again, the attachments
will be stripped from the script, but they're still there as MKV attachments.

### Size  ###
Unfortunately, storing binary data as text (in this case, a variant of
UUEncoding) is not very efficient. The attached files will take considerably
more space as script attachments than they do as separate files.

### Speed ###
Aegisub's undo system makes a complete copy of the loaded file on every change.
Normally this is very fast, but attachments can significantly slow this down
due to the large size.

