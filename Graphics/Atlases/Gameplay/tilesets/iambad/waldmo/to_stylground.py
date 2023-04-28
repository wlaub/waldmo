import sys
import random

from PIL import Image

tileset_name = sys.argv[1]

coords = [
[8,3],[9,3],[10,3],[11,3],
[8,4],[9,4],[10,4],[11,4],
[8,5],[9,5],[10,5],[11,5],
[8,6],[9,6],[10,6],[11,6],
]

tilefile = f'{tileset_name}.png'
tilestyle = f'{tileset_name}_bg.png'

tileset = Image.open(tilefile)

tiles = []
for x,y in coords:
    ntile = tileset.crop([x*8, y*8, (x+1)*8, (y+1)*8])
    tiles.append(ntile)

styleimg = Image.new('RGBA', [320,200])

for x in range(40):
    for y in range(25):
        ntile = random.choice(tiles)
        styleimg.paste(ntile, [x*8, y*8])

styleimg.save(tilestyle)

