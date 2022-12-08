---
layout: post
title: "A Breakup Letter to Vim"
date: 2018-05-13
tags: programming text-editing
---

I'm always impressed whenever someone demonstrates a certain level of proficiency with either Vim or Emacs.
They're considered "editors of a lifetime" for a reason - and it's the same reason why I must break up with Vim in particular.

I rather enjoy the idea of doing all of my work in the terminal, or maybe a single application that becomes an extension of my mind.
Vim has been that tool for a nontrivial amount of time in my so-far brief programming career.
Yet on reflection, I think I lose a lot more than I gain from using Vim.

So at this point, I have to ask: what exactly is Vim buying me?

<!-- more -->

* Fingers on the homerow philosophy?
  * Sure, I'll lose fractions of seconds to take my fingers off of `hjkl` to use the arrow keys, but I don't think it's that much of a drain on productivity, especially when you're handy with the option key to move by words.
  And I daresay that the mouse *is* faster in *some* contexts.
  I swear, I think the image that Vim/Emacs guys have of those who don't use their tools is that of a chimp holding down the arrow key to get to the word that he/she desires, or of a sloth clumsily using the mouse to highlight some text.
  Maybe I won't be as fast as a graybeard, but I'm no slouch on the keyboard either, even without the homerow niceties.

* Editing with motions?
  * Sure, I'll miss my favorite command `ciw` along with the whole family, but again, it's not so bad with the aid of the option key.
  I don't think it's so much worse to go the end of the a word with option+arrow and do option+delete.
  Again, I won't be mouth-breathing while holding down the delete key to delete whole words or entire lines; I'll still stay sharp with regards to editing text.

* Macros?
  * While they're certainly more powerful, I've been able to do pretty much everything that I could have done with macros with Sublime Text/VSCode multicursors.
  Actually, I'm probably able to do them faster by spamming Cmd+D (or Cmd+Shift+L for all occurrences) complimented with the WYSIWYG principle and a consistent undo behavior.
  Contrasting that with vim, where I have to start recording a macro, be meticulous with each action I'm executing, verify my ending cursor position, stop recording, hopefully not overrwrite the macro I just recorded, and then finally apply it.
  This process goes awry about half of the time anyways, so I end up thinking about how I can use the `.` command instead of macros, which is only more cognitive load for a task that should be mindless.
  Invoking Cmd+D *is* mindless, and has never broken my train of thought.
  As a contrived example, try **I**nserting and **A**ppending some text in the lines with the word "vim" in this markdown file; it's trivial with multicursors.

* Buffers, panes, and tabs?
  * This was never a compelling reason to stick with vim for me.
  Working with multiple files has always been a bit of a nuisance, especially with the lack of a built-in fuzzy finder (netrw isn't good enough) and a project-wide grep.
  Some people really like working with buffers, so I put it on the list.
  Most sane editors take care of this for you with flying colors, so I think this is kind of a moot point for vim.

Alright, forget all of that - what about the main selling point: the infinite customizability of an editor like vim or emacs?
And herein lies our final philosophical disagreement on this matter.

Customization is supposed to be a good thing, and I'm always going to agree with that.
More choice = more power.
When it comes at the expense of sane defaults however, even I have to object.
Even avid vimmers must agree with some of this, seeing as they remap `Y` to `y$` and `.` in visual mode for multiline application, and download a bunch of Tim Pope's plugins.
I just think more things work out of the box.
I ask without disrespect, whether if that's too much to expect?

Without sane defaults and out-of-the-box power, we toil at molding our tools to do what should have been accomplished a generation ago, and thus we've reinvented the wheel so many times.
We continually churn through poor documentation, hacky and outdated fixes, and poorly maintained plugins that don't play nicely with each other in order to keep this editor relevant in the modern age.
In an age where modern editors can fluently traverse large codebases, have intelligent autocompletion, can jump to definitions, execute debugging capabilities, and more.
Vim enthusiasts may argue that plugins accomplish some of this, but in my opinion, they're never as well executed as the native features in modern editors.
Some people love the process of wiring these hacks together, but I finally have to come out and say that I've had enough.

The truth is, I dislike configuring stuff, but not because I hate doing it; I actually like doing it too much and that's the problem.
I spend way too much time implementing unnecessary functionality under the guise that this would somehow make me more efficient, and I'm never satisfied.
There's always one more thing that I have to fix with the metaphorical duct tape and WD-40, wasting time that I could have actually spent working or solving problems.

Maintaining my configuration file, trying out new plugins, and god forbid, writing vimscript functions and testing them, end up being a huge drain on productivity.
I've realized that there will never come a point where I'm going to stop modifying my vimrc almost daily and be done with it for an extended period of time.
It will instead continue growing into a huge mess, with a bunch of hodgepodge solutions pasted together from online sources, and some self documentation to try and explain why I did xyz, however many months/years ago.

The thing I'm losing by switching away from vim are some seconds here and there while I edit a file.
Of course, those seconds will add up to minutes, and then hours.
But the time I spend doing all this other busywork to want to do what I want it to do are on the order of minutes, which add up to hours, and days much more quickly.
I find that Vim is spectacular at handling the 90% of the work I do, but I think it really falls short in that crucial 10%, and that's where I'll be losing time playing catchup with editors that have already solved these problems in a robust way.

I've found that the only antidote for me is to use something like Visual Studio Code, which has a lot of sensible default settings and behaviors.
An editor should, by default, come with a fuzzy file finder, project grep, quick and easy file explorer, capability to comment/uncomment code of any language, git integration, etc.
It's 2018 for goodness' sake.

I also *like* the fact that there's one way to do things through its idiot-proof json configuration file.
Having an option item to toggle on and off is actually a boon for me in lowering the mental resources that I would otherwise allocate in figuring out what the difference is between `syntax on` and `syntax enable` in vim for example.
This lack of choice in doing `"files.trimFinalNewlines": true` in VSCode also beats deciphering some community answer on the internet for an equivalent vim solution like `:command! RemoveNewLines execute %s/\($\n\s*\)\+\%$//e` (which doesn't even behave like I want it to, so I would have to test and tweak it some more).

Again, let me emphasize that this is a problem with **me**.
I truly envy the people who can make little configuration edits here and there and not be completely engrossed with making them all day.
It's completely on me that I'm focusing less on actually building cool things with code, and instead trying to maximally optimize how text editing should be done.
I recognize that I'm not that sort of person to touch and go a vimrc file at all.
I'll become obsessed with tweaking it to no real end or purpose if I'm being honest with myself.
I can't recall how many hours I've lost optimizing my vim workflow.
While it's not too common, my experience of being much too anal about my configurations is similar to others who have tapped out from using vim, even after using it for many years.

So I'll be sticking with Visual Studio Code for now.
Don't get me wrong, I want to hate this editor - but it's got everything I need.
I still dislike the fact that
* it regularly shows up as an application that's using significant energy
* it's owned by Microsoft

I'll suck it up over the increased power usage.
The latter point is what I'm really worried about.
My feeling on this matter is that VSCode will try to be for text editing what Google Chrome was for web browsing in that we'll be blown away with how good it is, only for Microsoft to then screw us over in some form or another.
The little research I've done on their telemetry policy doesn't help much either.

And if this is the case, that Microsoft does have nefarious intentions later on, I will gracefully part ways with it.
Or even if Microsoft is really vying for VSCode to be the best text editor without any other motives, and as much I love using VSCode, I know it'll eventually lose its place next to tools of the future.
In either case, I can accept switching to the next editor as thousands have previously done from TextMate to Sublime Text to VSCode.
I think embracing this realization is better than resisting the future and being unable to adapt to change.
We'll miss a ton of cool features these new editors may introduce if we fight tooth and claw to force the tools of an older generation to continue in the modern age.

Right now, there are promising upcomers that I'm looking forward to, like [Oni](https://github.com/onivim/oni), [Xray](https://github.com/atom/xray) (GitHub's second attempt at an editor) and [Xi](https://github.com/google/xi-editor).
I'm particularly interested in how the Xi turns out, given that it's not built with Javascript, and that some of the tools built with Rust thus far have been impressively fast, like [ripgrep](https://github.com/BurntSushi/ripgrep) and [fd](https://github.com/sharkdp/fd).
And we should be rooting for these editors, not diminishing them.
If they make our lives easier, then we win right?

Anyways, for now, I think it's best for me to switch away from vim or emacs, lest I get sucked back into the rabbit hole that many have voluntarily chosen to go down.
I will definitely miss some part of sharpening my tools on a languid afternoon.
While I'll certainly be losing a few fractions of seconds here and there that I could have saved with vim, I just gained a whole lot of time spending it with an editor that has most of everything I could want out of the box.

So it's time that I retire from my short career in yak-shaving, and part with these "editors of a lifetime" for good.
Who knows if I'll even be in this industry for that long?
A lifetime is the longest thing you'll experience.
Vim and emacs will have their place, but I won't be with them extensively[^1] any longer.
What's most important is that I'll be able to allocate my time more effectively to do the things I care about.

Thanks for all you've given me.
I'll continue to see you in large files or over ssh.
For now, so long vim!


> It's not that we have a short time to live, but that we waste much of it. Life is long enough, and it's been given to us in generous measure for accomplishing the greatest things, if the whole of it is well invested. But when life is squandered through soft and careless living, and when it's spent on no worthwhile pursuit, death finally presses and we realize that the life which we didn't notice passing has passed away. So it is: the life we are given isn't short but we make it so; we're not ill provided but we are wasteful of life.

\- Lucius Annaeus Seneca, On the Shortness of Life
