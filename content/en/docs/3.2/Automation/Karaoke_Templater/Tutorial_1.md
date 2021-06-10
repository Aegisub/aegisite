Welcome to the first tutorial in using Karaoke Templater to create [karaoke effects]({{< relref "../../Glossary/Karaoke_effect" >}}). We'll start out with something simple and
then continue on to more advanced effects throughout the series.

## Finding Karaoke Templater  ##

You can run Karaoke Templater in two different ways. For now we'll just
concentrate on one of them.

Look under the Automation menu in Aegisub.

![Automation-menu-kara-templater-gray](/img/3.2/Automation-menu-kara-templater-gray.png)

You should see the option called _Apply karaoke template_, though it will be
unavailable. This is what you'll select to use the "templates" we'll be writing
throughout these tutorials. Right now it's unavailable because you haven't
entered any templates. We'll get to that in a moment.

If you don't have the _Apply karaoke template_ option, your Aegisub
installation is either incomplete or damaged. You need to repair your
installation in that case, to be able to use Karaoke Templater.

But there is something else to make sure of first.

## Getting timed karaoke  ##

Karaoke Templater can do many things for you, but it can't guess the lyrics for
your song, or how they're synchronised with the music. You'll have to time the
lyrics yourself, or get someone else to do it. You can learn how to time
karaoke at the [Karaoke_Timing_Tutorial]({{< relref "Karaoke_Timing_Tutorial" >}}).

We'll call song lyrics with basic karaoke timing (\k timing), but no other
special effects, for _timed karaoke_. When an effect has been applied to the
karaoke we'll call it _styled karaoke_.

If you don't have any song to work with here are two lines from a song. You
can select them in your browser, select _Edit_→_Copy_, then go to Aegisub and
select _Edit_→_Paste_, to get them into Aegisub.

    Dialogue: 0,0:00:01.85,0:00:09.06,Default,,0000,0000,0000,,{\k97}shi{\k41}ta{\k0} {\k20}no{\k10} {\k30}u{\k80}e{\k53} {\k23}a{\k21}ma{\k39}ku{\k7}  {\k24}to{\k24}ke{\k31}ru{\k0} {\k37}wa{\k23}ta{\k92}gu{\k69}mo
    Dialogue: 0,0:00:09.28,0:00:16.21,Default,,0000,0000,0000,,{\k79}ki{\k61}su{\k0} {\k9}o{\k0} {\k37}shi{\k98}te{\k40}  {\k23}ku{\k25}ro{\k40}i{\k0} {\k28}tsu{\k19}ba{\k51}sa{\k0} {\k11}no{\k0} {\k34}shi{\k138}ta

Either way you have some karaoke timed lyrics now, so we can start.

### Load a video  ###

You don't need to load any audio, but it can be a good idea to have some video
open. If you don't have any video files ready you can use, select _Video_→_Use
dummy video_ and just say OK. It's not a very interesting video you will get,
but it will show you how the subtitles and the effect we're creating will look.

## Writing a _k-replacer_ style template  ##

Now we have everything else set up it's time to make the actual template.
First, here's how to add it. The explanation of what every part means will
follow.

1. Select the very first subtitle line in the file.
1. Select _Subtitles_→_Insert Lines_→_Before Current_ to get a new line before it. This will become our karaoke template line. It doesn't _need_ to be first, but it usually makes it easier to keep track of for yourself.
1. Make sure the newly created line has the same _style_ as your timed karaoke.
1. Click the _Comment_ check box for the new line. It should change colour in the subtitle grid.
1. Find the _Effect_ field, it's to the right of the _Style_ and _Actor_ fields. Put the text "`template line`" into it. (Without the quotes!) Press the _Enter_ key on your keyboard to save the Effect field.
1. Finally, enter this text for the main text of your template line. Finish off with _Enter_ again. `{\r\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)}`

{{<todo>}}Insert a screenshot of how it should look after the steps. {{</todo>}}

Now look at the _Automation_ menu again. If you made the template line
correctly, _Apply karaoke template_ will now be available. If it isn't review
the steps above again.

Select _Apply karaoke templates_ and watch Karaoke Templater do its work.

{{<todo>}}Another screenshot, this time after applying templates. {{</todo>}}

If you have a video open you can view the effect right now, inside Aegisub.

Also notice how the template line was left in place, and the timed karaoke was
changed to comment lines and had _karaoke_ filled into their Effect fields.
Karaoke Templater preserves your timed karaoke in the styled karaoke so you
won't lose it. But it also has another function...

## Extending the effect a bit  ##

Continuing right on from above, now try doing this:

1. Change the text of the template line to: `{\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)}`
1. Apply templates again

{{<todo>}}More screenshot {{</todo>}}

Karaoke Templater re-used the commented out timed karaoke and changed the
styled karaoke to match the new effect instead. You can also try changing the
commented out timed karaoke and apply templates again.

Like this, you can work gradually on your effect and preview it as you go.

## So what does it all mean?  ##

To finish off this first part of the tutorial, here's what each part means.
This is not the full explanation of everything, but it should be plenty for
now.

 *  _Template lines_ are lines in the subtitle file marked in a special way.
     They must always be Comment lines, and the first word in their Effect
     field must be `template`.
 *  There are several kinds of template lines. We only used one in this
    tutorial, this template line type, or _template class_, is called a _line
    template_. Yes, it might be a bit confusing. It's called this because it
    creates one line of styled karaoke from one line of timed karaoke. The
    second word in the Effect field of a template line tells what template
    class it is.  For line templates, this is `line`.
 *  So, the `template line` text in the Effect field means this is a
    _template line_ of _line class_.
^
 *  A template only does something to timed karaoke lines that have the same
    Style as the template line.
^
 *  Styled karaoke produced by Karaoke Templater all has `fx` in the Effect
    field. This is used as a reminder for Karaoke Templater that this line
    should be replaced, if templates are applied once again.
^
 *  The main text for a template line is called the _template text_. In
    _line_ templates, every \k tag is replaced with the template text.
 *  Template text can use several _variables_. These are short words that
    start with a dollar-sign, like `$start`, `$end`, `$mid` and `$kdur`.
    Variables are replaced with the information they store for every syllable
    that's replaced.
     *  `$start` gets replaced with the start time of the syllable. This is
        in milliseconds from the start of the line, ie. a time code suitable
        for putting into the \t, \move and \fade tags.
     *  Similarly, `$end` is the end time of the syllable, also in
        milliseconds.
     *  A bit more special is `$mid`, this is the _midway time_ of the
        syllable, the time right in the middle of `$start` and `$end`. Here, we
        used it to grow each syllable taller the first half of its duration,
        and back to normal height for the second half. Also in milliseconds.
     *  The `$kdur` variable, however is in centiseconds. This is the
        original time from the \k tag, and is almost only useful for putting
        back into a \k tag, like we did here.

With this knowledge, you should already be able to create lots of effects. You
may also want to refer to the page on [ASS override tags]({{< relref "ASS_Tags" >}}).

You can also [continue to the next tutorial]({{< relref "./Tutorial_2" >}}), where we'll look at how to
do math with variables to get more variation.

