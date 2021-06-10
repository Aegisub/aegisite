In [the previous tutorial]({{< relref "./Tutorial_1" >}}) we saw how to use the basic features of Karaoke Templater to make simple karaoke effects. We'll continue where we left off here, by expanding on the basics from last tutorial.

{{<todo>}}make and insert screenshots {{</todo>}}


## Preparations  ##

As before, you'll still need some timed karaoke and a video to preview the effects. I won't go into further details with that here.


## Adding a fadeout  ##

To recap, here's the effect from the end of last tutorial:

    {\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)}

We'll add a fadeout effect to this now, having each syllable fade out _after_ it has been sung, not while. We'll have to do a little maths to make this: Start the fadeout at `$end` and have it continue until `$end+200`, ie. have it fade out for 200 milliseconds after the syllable.

Change the template to this:

    {\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)\t($end,!$end+200!,\alpha&HFF&)}

Then try applying templates again. You should see the old effect happen as usual, but this time afterwards, each syllable fades out.

The magic in this is the exclamation marks here: `!$end+200!`

When you have a pair of exclamation marks like that, everything in between them is treated as an _expression_ (actually a very small Lua program, but don't worry about that yet.) Here we use an expression to take the end-time of the syllable and add 200 to it, getting a new number. The end result is that the <tt>\t</tt> fadeout effect lasts from `$end` and until 200 milliseconds later.


## Tweaking the grow/shrink effect  ##

Maybe you think the growing-shrinking effect looks a bit odd, switching right in the middle. It might look better if it was at the maximum height earlier, and used more time shrinking back to normal. Well, that can be changed:

    {\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,!$start+$dur*0.3!,\fscy120)\t(!$start+$dur*0.3!,$end,\fscy100)}

With this, the growing-part will only take the first three-tenths of the syllable duration, and the shrinking the rest. We used one new variable here, `$dur`. This is the duration of the syllable in milliseconds, just like `$kdur` is the duration in centiseconds. (We could actually just as well just have used `$kdur` here, and then multiplied by 3 instead of 0.3.)

Note that I removed the fadeout from here, it's just to make the line shorter and easier to read. You can add it back if you want.

Hopefully this tutorial has given you some more ideas of what you can do. In [the next one](#) we'll add another layer to the effect by using multiple templates!

