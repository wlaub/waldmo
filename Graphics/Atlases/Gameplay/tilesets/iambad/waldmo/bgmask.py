import sys
import random

from PIL import Image

mask_file = sys.argv[1]

mask = Image.open(mask_file)
mask = mask.getchannel('R')

for filename in ['brightblue.png']:
    base = filename.split('.')[0]
    outfile = f'{base}_bg.png'

    base_image = Image.open(filename)
    base_image.putalpha(mask)
    base_image.show()
