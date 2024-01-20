import sys
import random

from PIL import Image, ImageChops

mask_file = sys.argv[1]

mask = Image.open(mask_file)
mask = mask.getchannel('R')

files = {
'darkblue',
'brightblue',
'vividblue',
'darkyellow',
'brightyellow',
'vividyellow',
'emptyred',
'brightred',
'vividred',
'sinisterred',
'darkblack',
'brightblack',
'vividblack2',
'darkwhite',
'brightwhite',
'subduedpurp',
'vividpurp',
'xtremepurp',
'tamewhite',
'tameyellow',
}

files = {'vividblack3'}

for filename in files:
#    base = filename.split('.')[0]
    base=filename
    filename+='.png'
    outfile = f'{base}_bg.png'

    base_image = Image.open(filename)
    base_mask = base_image.getchannel('A')
    base_mask = ImageChops.multiply(base_mask, mask)
    base_image.putalpha(base_mask)
#    base_image.show()
    base_image.save(outfile)
