
This page describes various technical details about how Karaoke Templater
(_kara-templater_) works and will try to explain why various things work as
they do and why some things can't and won't work.

Most of this is technical details you don't need to know to use kara-templater,
but if you see some behaviour you don't understand this page might explain it.

## Concepts  ##
These are some terms and concepts used throughout the description. The names
are close to or the same as those used in the actual script.

**`tenv`**
: The **t**emplate **env**ironment, or [code execution environment]({{< relref "./Code_execution_environment" >}}).

**`varctx`**
: The inline **var**iable **c**on**t**e**x**t, the storage for the actual
values of the [inline variables]({{< relref "./Inline_variables" >}}).

**`template`**
: The basic "execution unit" of kara-templater, a template is essentially a
mini-program compiled and executed by kara-templater.

**`code template`**
: A template that runs a chunk of Lua code but doesn't produce output.
(Declared with the _code_ keyword.)

**`output template`**
: A template that produces output lines from some karaoke data input. (Declared
with the _template_ keyword.)

**`code line`**
: A line in the subtitle that defines a code template.

**`template line`**
: A line in the subtitle file that defines an output template, or part of one.
(One _line_ class output template can span multiple template lines.)

**`class`**
: A class is a kind of template. There's four basic classes, _once_, _line_,
_syl_ and _furi_, the first only available for code templates.

**`modifier`**
: Modifiers affect how and when templates are executed.

**`template text** or just **text`**
: The "text" part of a template, either the Lua code in a code template or the
template code in output templates. _line_ class output templates also have a
_pre-line text_.

## Startup  ##
The first thing kara-templater does is simply use
[karaskel]({{< relref "../Lua/Modules/karaskel.lua.md" >}}) to collect some basic
information on the subtitle file. It always passes `true` for
_generate_furigana_ in the `karaskel.collect_head` function, meaning that
[furigana]({{< relref "Furigana_karaoke" >}}) styles are always generated, unless they already
exist.

It then collects all template lines in the file.

### Collecting, parsing and compiling templates  ###
Every line in the file is visited and checked for being a template line, i.e.
be a comment and have the first word in the Effect field be _code_ or
_template_.

The details aren't important here, but every modifier name found in the Effect
field either sets a flag in the template or a value corresponding to the
parameter given to the modifier.

When a named _line_ class template lines is encountered, first it's checked if
there is already a _line_ class template with that name. If there isn't one, a
new one is created with that name and initialised with the given modifiers. If
there is already one with that name, _the text of the template line is appended
to the current text of the template_ and modifiers present in the new template
line but not in the current template are added to the template. Modifiers
cannot be removed from templates in this way or any other way. The text of
_pre-line_ template lines is added to the _pre-line text_ of the template
rather than the regular text.

The templates of different classes are each put in their own "bucket", so for
example _line_ and _syl_ templates are not kept together.

### Clean-up  ###
After all templates have been collected etc., all old and no longer needed
lines are deleted from the subtitle file. This mainly includes lines with _fx_
in the Effect field, as those are assumed to have been generated in a previous
run of kara-templater, so they should be replaced in this new run.

### Initialising the _tenv_  ###
The last thing done before starting actually running the templates is
initialising the runtime environment for the templates. Basically, as much as
possible before any templates are run, is put into _tenv_. See [Code execution environment]({{< relref "./Code_execution_environment" >}}) for more
details on what's in there. (Basically everything but `line`, `orgline`, `syl`
and `basesyl`.)

## Run _once_ templates  ##
All templates in the _once_ class are executed first. Nothing truly exciting
happens here, the main thing that can happen is that some more things are added
to _tenv_.

## Iterate through karaoke lines in file  ##
Every non-template line in the file is now run through and has all templates attempted applied in order.

* If a line is a comment and its Effect field doesn't contain `Karaoke` it is
  skipped immediately.
* If a line is not a comment and its Effect field contains anything else that
  `Karaoke` or nothing (is blank) it is skipped immediately.
* Kara-templater attempts to match all templates against all other lines.

Each line that hasn't been rejected by the above points is now run through all
templates in three steps.

First, all _line_ class templates are attempted matched against the line and
then run on the line. See below for a definition of when a template matches a
line.

Next, all syllables on the line are run through in order and for each, all
_syl_ class templates are attempted matched against the line and then run on
the syllable.

Finally, all furigana syllables on the line are run through in order, for each
every _furi_ class template is attempted matched against the line and then run
on the furigana syllable.

It is important to note that the syllables and furigana syllables looped
through are the parsed-stored syllables, not multi-highlight virtual syllables,
not per-character virtual syllables and not a combination.

{::template name="examplebox"}
Assume there are three `syl` class templates: A, B and C.

* A is a regular template with neither _multi_ nor _char_ modifier.
* B has the _multi_ modifier but not _char_.
* C has both the _char_ and _multi_ modifiers.

Now these templates are applied against a line with 2 syllables. This happens in order:

* Syllable 1 is picked.
    * Template A is matched against the line. It matches.
        * Template A is applied on syllable 1.
    * Template B is matched against the line. It matches.
        * Syllable 1 is split into multi-highlight pseudo-sylables 1.1 and 1.2
        * Template B is applied on pseudo-syllable 1.1.
        * Template B is applied on pseudo-syllable 1.2.
    * Template C is matched against the line. It matches.
        * Syllable 1 is split into per-character pseudo-syllables 1.a and 1.b
        * Syllable 1.a and 1.b are further split into per-character pseudo-sylables 1.a1, 1.a2, 1.b1 and 1.b2.
        * Template C is applied on pseudo-syllable 1.a1.
        * Template C is applied on pseudo-syllable 1.a2.
        * Template C is applied on pseudo-syllable 1.b1.
        * Template C is applied on pseudo-syllable 1.b2.
    * Syllable 2 is picked.
        * Processing proceeds similar to syllable 1.

Also see later down for more details on multi-highlight and per-character pseudo-syllables.
{:/}

If any template matches at any time during the three steps above the (original)
line is marked as "timed karaoke" and is then made into a comment with
`karaoke` in the Effect field.

### Matching a template against a line  ###
Templates are always matched against a line, not against a syllable or
otherwise.

* If the template has the _fxgroup_ modifier and the fxgroup named is disabled,
  the template never matches anything.
* If the template has the _all_ modifier it always matches any line.
* If the template has the same Style as a line, it matches the line.
* Otherwise the template does not match the line.

## Applying _line_ class templates  ##
{{<todo>}} write this {{</todo>}}

## Applying _syl_ and _furi_ class templates  ##
{{<todo>}} write this {{</todo>}}

## Old mid-level description  ##
<pre>Main kara-templater process:
1. Collect header
   1. Find all header information, primarily PlayResX and PlayResY
   2. Find all styles
   3. Generate furigana styles for styles missing them
2. Collect templates and delete existing "fx" lines
3. Initialise tenv
   1. Add "string", "math" and "_G" references
   2. Add "tenv" self-reference
   3. Add "retime" function
   4. Add empty "fxgroup" table
4. Run every "code once" template
5. For every pre-existing dialogue line in subtitle file:
   a. If Effect field start with "code" or "template":
      1. Skip line
   b. Else:
      1. If Effect field is not empty and not "karaoke":
         a. Skip line
      2. If Effect field is empty and line is a Comment:
         a. Skip line
      3. Preprocess line with karaskel
      4. Initialise varctx
      5. Reset tenv
         1. Set "orgline" to input line
         2. Set "line", "syl" and "basesyl" to nil
      6. For every "line" template:
         If template matches line style or template is "all":
         Repeat this "template.loops" number of times:
         1. Set "tenv.j" to loop counter
         2. a. If template is a code line:
               1. Set "tenv.line" to input line
               2. Run code
            b. Else:
               1. Produce output line as copy of input line
               2. Set "tenv.line" to output line
               3. Initialise output line Layer to template Layer
               4. Initialise output line Text to empty
               5. If template has pre-line:
                  1. Run pre-line template
                  2. Append result to output Text
               6. a. If template has regular line:
                     For every syllable in input line:
                     1. Set "tenv.syl" to syllable
                     2. Update varctx for syllable
                     3. Run line template
                     4. Append result to output Text
                     5. If "notext" is not set:
                        a. If "keeptags" is set:
                           1. Append "syl.text" to output Text
                        b. Else:
                           1. Append "syl.text_stripped" to output Text
                  b. Else:
                     a. If "keeptags" is set:
                        1. Append "syl.text" to output Text
                     b. Else:
                        1. Append "syl.text_stripped" to output Text
               7. Set Effect field of output line to "fx"
               8. Append output line to subtitle file
      7. For every main syllable in line:
         For every "syl" template:
         If template matches line style or template is "all":
         If template is not in a disabled fxgroup:
         1. Set "tenv.syl" to syllable
         2. Update varctx for syllable
         3. If syllable inlinefx does not match template inlinefx:
            1. Skip syllable
         4. If template has "noblank" set and syllable is blank:
            1. Skip syllable
         5. If template is "char":
            1. Create "charsyl" as copy of syllable
            2. Set "tenv.basesyl" to current "tenv.syl"
            3. Set "tenv.syl" to "charsyl"
            4. For every Unicode character in syllable:
               1. Calculate virtual syllable characteristics for "charsyl"
               2. Update varctx for "charsyl"
               3. Continue syllable processing for the virtual syllable (from 5.b.7.6.)
         6. If template is "multi":
            1. Create "hlsyl" as copy of syllable
            2. Unless "tenv.basesyl" already exists, set it to "hlsyl"
            3. Set "tenv.syl" to "hlsyl"
            4. For every highlight on syllable:
               1. Calculate virtual syllable characteristics for "hlsyl"
               2. Update varctx for "hlsyl"
               3. Continue syllable processing for the virtual syllable (from 5.b.7.7.)
         7. a. If template is a code line:
               1. Set "tenv.line" to input line
               2. Run code
            b. Else:
               Repeat this "template.loops" number of times:
               1. Set "tenv.j" to loop counter
               2. Create output line
               3. Set output line Style to virtual syllable style
               4. Set output line Layer to template layer
               5. Set "tenv.line" to output line
               6. Run template
               7. Set output line Text to result
               8. a. If "keeptags" is set:
                     1. Append "syl.text" to output line Text
                  b. If "notext" is not set:
                     1. Append "syl.text_stripped" to output line Text
                  c. Otherwise nothing is appended
               9. Set output line Effect to "fx"
              10. Append output line to subtitle file
      8. For every furigana part in line:
         Same process as for main syllables (5.b.7.)
      9. If any non-code templates were applied to the line:
         1. Set input line to Comment
         2. Set input line Effect field to "karaoke"
         3. Store modified input line back to subtitle file

Running a code line:
1. Compile line text to a Lua function
2. If compilation failed, report error
3. Set compiled function's environment to tenv
4. Repeat this "template.loops" number of times:
   1. Set "tenv.j" to loop counter
   2. Run compiled function
   3. If an error occurred, report it

Running a single template:
1. Set result text to template
2. If there is a varctx:
   For every match of "$([a-zA-Z_]+)" in result text:
   1. Lowercase the captured name
   2. a. If the captured name is a field in varctx:
         1. Replace match in result text with value from varctx
      b. Else:
         1. Report warning
         2. Keep match as-is in result text
3. For every match of "!(.-)!" in result text:
   1. Append "result " to captured code
   2. Compile captured code to a Lua function
   3. If compilation failed, report error
   4. Set compiled function's environment to tenv
   5. Run compiled function
      a. If compiled function produced an error:
         1. Report error
         2. Leave match in result text
      b. Else:
         1. Replace match with result of running the function</pre>

{{<todo>}}Turn this into something more reasonable? {{</todo>}}

{::template name="automation_navbox" /}
