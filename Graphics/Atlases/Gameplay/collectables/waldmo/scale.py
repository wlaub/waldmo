import os
from PIL import Image

for filename_base in os.listdir():
    base, ext = os.path.splitext(filename_base)
    if ext != '.png': continue
    idx = int(base[-4:])
    image = Image.open(filename_base)
    out = image.resize([20,20])
    out = out.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    out.save(f'collectable{idx:02}.png')


