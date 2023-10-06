# johnkgh.github.io

This is a static site built using Jekyll and deployed on Github Pages.

The theme is based directly off of [aweekj/kiko-now](https://github.com/aweekj/kiko-now) (`c9665c3` on Sep 21, 2019).

Generally, most of these pictures on this site are resized to a width of 1200px compressed with 80% quality. Double the site's max-width is probably overkill (though higher detail and 2x optimzed for retina displays), and 80% seems to have the best results for blue sky gradients (with the biggest size efficiency gains). Trying to keep the average photo size around 300KB and under 700KB.

ImageMagick commands:
```
magick a.jpeg -resize 1200x a.jpeg
magick a.jpeg -quality 80 a.jpeg
mogrify -strip a.jpeg
```
