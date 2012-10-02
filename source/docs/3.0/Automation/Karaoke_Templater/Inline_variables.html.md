This page describes the **inline variables** also known as **dollar variables** available in Karaoke Templater.


## How to use inline variables  ##


All inline variables start with a dollar-sign. They only work in template lines, not in code lines. You can, however, use them in code blocks on template lines.

Here is an example of how a template text using inline variables could look:

    {\pos(**$x**,**$y**)\t(**$start**,**$end**,\bord0)}

The highlighted parts are the inline variables in the template.

When a template is applied, the first thing that happens is that all inline variables are found and replaced with their value. Eg. in the above example `$x` and `$y` are replaced with the X and Y coordinates of the syllable the template is being applied to, and `$start` and `$end` are replaced by the start and end times of the syllable.

Case does not matter for inline variables, `$start`, `$START` and `$StArT` all work and give the same result.


### Limitations  ###


Inline variables are not "intelligent", they do the same no matter where you place them or use them, it doesn't "know" what tag it's being used with. Not every variable can be used with success in all places, and the meaning of some are affected by usage of eg. the [[retime|Automation/Karaoke_Templater/Code_execution_environment#retime]] function. In these cases, inline variables may not be appropriate and you need to use code blocks.

Because inline variables have their values determined as the very first thing when a template is applied you can't affect their values in any way.

Using inline variables is an easy way to get started with an effect, but for many advanced effects they might not be the best choice.

All positioning and sizing inline variables (such as `$y`, `$right` and `$width` are rounded to the nearest whole pixel, unlike the values in the internal data structures which you can get in code blocks, they have sub-pixel precision.


## Line and syllable variables  ##


The inline variables exist in both "line" and "syllable" variants. The "line" variants contain information about the entire line being processed, the "syllable" variants contain information about the current syllable being processed.

There are also "automatic" variants of most of the variables, there are either the line or the syllable variant depending on what kind of template they are used in. In pre-line templates the automatic inline variables refer to the line variants, and everywhere else they refer to the syllable variants.


## The variables  ##


The line variables that also exist as automatic variants all start with a lowercase L ("ell") letter, the syllable variants start with the letter S.

| Line variants                  |                                                                                                                                                                          
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
| layer                          | line layer                                                                                                                                                               
| lstart, lend, ldur, lmid       | line start time, end time, duration and midway, all absolute times in milliseconds                                                                                       
| style                          | name of the line style                                                                                                                                                   
| actor                          | name of the line actor                                                                                                                                                   
| margin_l, margin_r             | effective left and right margin (line if nonzero, otherwise style)                                                                                                       
| margin_v, margin_t, margin_b   | effective vertical, top and bottom margin, vertical and top is same                                                                                                      
| syln                           | number of syllables on line                                                                                                                                              
| li                             | line index (first physical line in file is 1)                                                                                                                            
| lleft, lcenter, lright         | line left, horizontal center and right edges, taking margins and alignment into account, rounded to an integer value                                                     
| ltop, lmiddle, lbottom         | line top, vertical middle and bottom edges, taking margins and alignment into account, rounded                                                                           
| lx, ly                         | line x and y position suitable for a \pos command when alignment is not overridden                                                                                       
| lwidth, lheight                | line width and height in pixels, this is rounded and might not match exactly with the positioning variables                                                              
| Syllable variants              |                                                                                                                                                                          
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
| sstart, send, smid             | syllable start, end and midway times relative to start of line, suitable for putting into \t and \move                                                                   
| sdur, skdur                    | syllable duration in milliseconds and centiseconds                                                                                                                       
| si                             | syllable index from start of line                                                                                                                                        
| sleft, scenter, sright         | absolute left, horizontal center and right edges for syllable from left edge of screen, suitable directly for \pos and \move                                             
| sbottom, smiddle, stop         | absolute bottom, vertical middle and top edges for syllable from top edge of screen, suitable directly for \pos and \move, adjusted for furigana positioning if needed   
| sx, sy                         | syllable absolute x and y position in default alignment, suitable for using directly in \pos and \move                                                                   
| swidth, sheight                | syllable width and height in pixelsthis is rounded and might not match exactly with the positioning variables                                                            
| Automatic variants             |                                                                                                                                                                          
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
| start, end, mid                | start and and midway time for line/syllable; absolute for lines and relative for syllables                                                                               
| dur, kdur                      | duration in milliseconds and centiseconds of line/syllable                                                                                                               
| i                              | line or syllable index                                                                                                                                                   
| left, center, right            | left, center and right edges of line/syllable, absolute from left screen edge                                                                                            
| top, middle, bottom            | top middle and bottom edges of line/syllable, absolute from top screen edge                                                                                              
| x, y                           | x and y position of line/syllable when using default alignment                                                                                                           
| width, height                  | width and height of line/syllable in pixels, this is rounded and might not match exactly with the positioning variables                                                  


[[!template id=Automation_navbox]]

