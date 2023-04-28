"""
make the other directions from the up direction
"""

import os
from PIL import Image

def spike_split(name):
    parts = name.split('_')
    front = '_'.join(parts[:-1])
    direction = parts[-1].split('.')[0]
    if direction[:2] != 'up':
        raise ValueError('nah')
    idx = direction[2:]
    direction = direction[:2]

    return front, direction, idx

for filename_base in os.listdir():
    try:
        front, direction, idx = spike_split(filename_base)
    except Exception as e:
        print(f'{filename_base}: {e}')
        continue
    print(front, direction, idx)

    image = Image.open(filename_base)    
    for new_dir, angle in [('left', 90), ('down',180), ('right', 270)]:
        out = image.rotate(angle)
        outname = f'{front}_{new_dir}{idx}.png'
        print(outname)
        out.save(outname)


