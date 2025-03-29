import os
import math
import sys
import random

from PIL import Image

tileset_name = sys.argv[1]

try:
    w = int(sys.argv[2])
except:
    w = 40

try:
    h = int(sys.argv[3])
except:
    h = 25



coords = [
[8,3],[9,3],[10,3],[11,3],
[8,4],[9,4],[10,4],[11,4],
[8,5],[9,5],[10,5],[11,5],
[8,6],[9,6],[10,6],[11,6],
]

source_path = '../Graphics/Atlases/Gameplay/tilesets/iambad/waldmo/'
out_path = 'outputs/tiles'

tilefile = os.path.join(source_path, f'{tileset_name}.png')
tilestyle = os.path.join(out_path, f'{tileset_name}_{w}_{h}.png')

tileset = Image.open(tilefile)

tiles = []
for x,y in coords:
    ntile = tileset.crop([x*8, y*8, (x+1)*8, (y+1)*8])
    tiles.append(ntile)

styleimg = Image.new('RGBA', [w*8,h*8])

for x in range(w):
    for y in range(h):
        ntile = random.choice(tiles)
        styleimg.paste(ntile, [x*8, y*8])

styleimg.save(tilestyle)

