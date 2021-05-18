import sys
import random
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

from functools import wraps
from time import time
from typing import List
from PIL import Image, ImageDraw, ImageFont
sys.path.append('../')

class RenderRose2:
  title = 'render_rose2'
  def __init__(self, size = 100):
    im = Image.open('rose3.png')
    width, height = im.size
    pixels = im.load()

    im2 = Image.new('RGBA', (width, height))
    im2.paste((250, 240, 241), (0, 0, width, height))
    pixels2 = im2.load()

    for x in range(width):
      for y in range(height):
        # r, g, b, a = pixels2[x, y]
        # r2, g2, b2, a2 = pixels[x, y]
        # pixels2[x, y] = (r + r2, g + g2, b + b2, a + a2)
        r, g, b, a = pixels[x, y]
        if (r + g + b + a) == 0 or a < 250:
          continue
        print(r, g, b, a)

        if abs(r - 41) < 5 and abs(g - 43) < 5 and abs(b - 41):
          continue

        if pixels[x, y][3] != 0:
          pixels2[x, y] = pixels[x, y]

    im2.show()



  def render(self):
    yield None