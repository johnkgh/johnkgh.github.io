# johnkgh.github.io

This is a static site built using Jekyll and deployed on Github Pages.

The theme is based directly off of [aweekj/kiko-now](https://github.com/aweekj/kiko-now).

You can build and serve this site locally by invoking `bundle exec jekyll serve`.

## Workflow

I export PNG photos from whatever software (currently Apple Photos.app) then compress them using ImageMagick:
```
magick a.png -resize 1200x a.jpg
magick a.jpg -quality 80 a.jpg
mogrify -strip a.jpg
```

For git management, this repo makes heavy use of interactive rebasing to
* keep the changes to the website itself older in the history since it'll change less ideally
* keep everything about an outing confined to a single independent commit
* keep those outings ordered by date so that more recent history changes as little as possible ideally

So when working, use `git commit --fixup <SHA>` liberally to edit older commits, then `git rebase --interactive --autosquash c9665c3` to clean up the history. Merge conflicts should be rare since the changes are meticuously independent from each other (especially posts).
