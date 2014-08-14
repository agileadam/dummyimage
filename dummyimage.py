# -*- coding: utf-8 -*-
import os
import argparse
import random
import urllib2
import sys

parser = argparse.ArgumentParser(description="Uses http://dummyimage.com to \
    to retrieve a set of placeholder images. View README.md for more info.")

parser.add_argument("-i", "--include-dimensions", dest="dimensionsInTitle",
    default=False, action="store_true",
    help="Optional. Include dimensions in title")

parser.add_argument("-t", "--filetype", dest="filetype",
    help="Optional. Output file type without leading period. Use png, jpg, or \
    gif (png is default).", default="png", metavar="FILETYPE")

parser.add_argument("-d", "--directory", dest="targetDirectory", required=True,
    help="Output directory", metavar="DIRECTORY")

parser.add_argument("--min", dest="minDimensions", required=True,
    help="Minimum dimensions?", metavar="WxH")

parser.add_argument("--max", dest="maxDimensions", required=True,
    help="Maximum dimensions?", metavar="WxH")

parser.add_argument("-n", "--num", type=int, dest="numImages", required=True,
    help="How many images to generate.", metavar="INTEGER")

parser.add_argument("-p", "--prefix", dest="prefix", required=True,
    help="Prefix for the images' text overlay. Use Alphas, Numbers, Spaces, \
    Underscores, Spaces, and Hyphens only. Wrap with quotation marks!",
    metavar="\"PREFIX\"")

args = parser.parse_args()

mins = args.minDimensions.split("x")
maxes = args.maxDimensions.split("x")
minWidth = int(mins[0])
maxWidth = int(maxes[0])
minHeight = int(mins[1])
maxHeight = int(maxes[1])

targetDirectory = os.path.expanduser(args.targetDirectory)
if not os.access(targetDirectory, os.W_OK):
    sys.exit("ERROR: Unable to write to output directory.")

i = 0
while i < args.numImages:
    i += 1
    r = lambda: random.randint(0,255)
    bgcolor = "%02X%02X%02X" % (r(),r(),r())
    fgcolor = "%02X%02X%02X" % (r(),r(),r())
    width = random.randint(minWidth, maxWidth)
    height = random.randint(minHeight, maxHeight)
    prefix = args.prefix.replace(" ", "+")
    dimensionsTitle = "" 
    if args.dimensionsInTitle:
        # The character here is not an X, it's a multiplication sign
        dimensionsTitle = "+" + str(width) + "×" + str(height)
    url = "http://dummyimage.com/%dx%d/%s/%s.%s&text=%s+%d%s" % (width,
        height, bgcolor, fgcolor, args.filetype, prefix, i,
        dimensionsTitle)
    r = urllib2.urlopen(url)
    print "Retrieving", i, "of", args.numImages, ":", url
    output = open("%s/%s_%d.%s" % (targetDirectory,
        args.prefix.lower().replace(" ","_"), i, args.filetype), "wb")
    output.write(r.read())
    output.close()

sys.exit()
