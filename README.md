dummyimage
==========

Uses [http://dummyimage.com](http://dummyimage.com) to retrieve a set of placeholder images. You tell the script how many images to generate, the minimum and maximum dimensions, what the title overlay should be, and what filetype to generate (png, jpg, gif), and the script creates uniquely colored, sized, and labeled placeholder images. You can also choose to automatically include the dimensions in the title overlay.

## Tips
* If you need images that are at an exact dimension, use the same min/max values. (e.g., `--min 100x100 --max 100x100`)
* You can generate a single image using `-n 1`

## Usage

Please run `python dummyimage.py -h` to see the usage syntax and possible options.

**All options**
<pre>
$ python dummyimage.py -i -t jpg -d ~/Desktop/result/ --min 100x200 --max 300x400 -n 3 -p Slide
Retrieving 1 of 3 : http://dummyimage.com/281x385/77542A/6AB049.jpg&text=Slide+1+281×385
Retrieving 2 of 3 : http://dummyimage.com/236x205/DE0C7B/7B6BC8.jpg&text=Slide+2+236×205
Retrieving 3 of 3 : http://dummyimage.com/122x389/75FF05/934B3C.jpg&text=Slide+3+122×389
</pre>

**Only required options**
<pre>
$ python dummyimage.py -d ~/Desktop/result/ --min 100x200 --max 300x400 -n 3 -p Slide
Retrieving 1 of 3 : http://dummyimage.com/132x363/FA7AC5/05A9E7.png&text=Slide+1
Retrieving 2 of 3 : http://dummyimage.com/155x264/522D6A/F38EB8.png&text=Slide+2
Retrieving 3 of 3 : http://dummyimage.com/121x272/F3F9B7/B7DC24.png&text=Slide+3
</pre>

## Todo
1. Improve readability: foreground and background colors can be too similar on occasion.
1. Error checking
