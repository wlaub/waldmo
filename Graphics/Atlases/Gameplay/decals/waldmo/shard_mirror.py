
import os
import glob

from PIL import Image, ImageOps

files = glob.glob('shard_*.png')
outdir = '../../mirrormasks/waldmo'


for infile in files:
    im = Image.open(infile)

#    im = ImageOps.grayscale(im)
#    im = ImageOps.invert(im)
    pixels = im.load()

    for y in range(im.height):
        for x in range(im.width):
            pixel = pixels[x,y]
            val = (pixel[0]+pixel[1]+pixel[2])/(3*255)
            a = 255-int(val*255)
            b = int((1-val)*pixel[3])
            pixels[x,y] = (a,a,a,b)

    outfile = os.path.join(outdir, infile)
    im.save(outfile)

    decal_name = infile.split('.')[0]

    decal_string = f"""  <decal path="waldmo/{decal_name}">
    <mirror />
  </decal>"""
    print(decal_string)


