This page describes how a template line or code line is declared.


* Template lines and code lines are always marked Comment.

<div></div>


* The first space-separated word in the Effect field determines whether a line is a template line, a code line, a timed karaoke line, a styled karaoke line or something otherwise undetermined.

<div></div>


* If the first word in the Effect field is `template`, the line is a template line.

<div></div>


* If the first word in the Effect field is `code`, the line is a code line.

<div></div>


* If the Effect field is exactly equal to `fx`, the line is a styled karaoke line. Styled karaoke lines are deleted during execution of Karaoke Templater.

<div></div>


* If the Effect field is `Karaoke`, `karaoke` or empty, the line is a timed karaoke line.

<div></div>


* If the Effect field contains anything else, the line is an undetermined type and is not touched by Karaoke Templater.

<div></div>

Template lines and code lines can have additional text after the `template` or `code` keywords. This text is parsed as a series of space-separated words and is called modifiers. See [[Template modifiers|Automation/Karaoke_Templater/Template_modifiers]] for more information on this.

[[!template id=Automation_navbox]]

