import sys
import random
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

from functools import wraps
from time import time
from typing import List
from PIL import Image, ImageDraw, ImageFont
sys.path.append('../')

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap



UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

CELL = 2
PATH = 1
WALL = 0


WIDTH = 40
HEIGHT = 40

START_POINT = (270, 162)

WIDTH, HEIGHT = (500, 500)

class RenderRose:
  title = 'render_rose_maze'
  def __init__(self, size = 100):
    im = Image.open('rose3.png')
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    self.pixels = pixels

    image = np.zeros((width, height))
    for row in range(height):
      for col in range(width):
        if sum(pixels[row][col]) != 0:
          image[row][col] = 1
    # print(image)
    # image = [
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 0, 1, 1, 0, 0],
    #   [0, 0, 1, 1, 1, 0],
    #   [0, 0, 1, 1, 0, 0],
    #   [0, 0, 1, 1, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    # ]

    # get start point
    # flag = 0
    # for row in reversed(range(height)):
    #   for col in reversed(range(width)):
    #     if pixels[row][col][3] != 0:
    #       print(row, col)
    #       flag+=1

    #   if flag > 10:
    #     break

    self.mask = image
    self.size = len(image)

    image = np.asarray(image)
    startPoint = (240, 366)
    # startPoint = (2, 4)

    self.visited = [startPoint]

    self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    self.pools = []

    x, y = startPoint
    for direction in self.directions:
      (vx, vy) = direction

      if x + vx < 0 or x + vx > self.size or y + vy < 0 or y + vy > self.size:
        continue

      if (x + vx, y + vy) in self.visited:
        continue

      if self.mask[y + vy][x + vx] == 0:
        continue

      self.pools.append((x + vx, y + vy))

  def calcVisited(self):
    while len(self.pools) > 0:
      random.shuffle(self.pools)
      point = self.pools.pop()

      x, y = point
      for direction in self.directions:
        (vx, vy) = direction

        if x + vx < 0 or x + vx > self.size or y + vy < 0 or y + vy > self.size:
          continue

        if (x + vx, y + vy) in self.visited:
          continue

        if self.mask[y + vy][x + vx] == 0:
          continue

        self.pools.append((x + vx, y + vy))
        self.visited.append((x + vx, y + vy))

  def render(self):
    self.calcVisited()
      # image = Image.new('RGB', (WIDTH, HEIGHT))
      # image.paste((250, 240, 241), (0, 0, image.size[0], image.size[1]))
      # draw = ImageDraw.Draw(image)

      # for row in range(self.size):
      #   for col in range(self.size):
      #     if (col, row) in self.visited:
      #       draw.rectangle((row * WIDTH / self.size, col * HEIGHT / self.size, (row + 1) * WIDTH/ self.size, (col + 1) * HEIGHT / self.size), fill=self.pixels[row][col], outline=self.pixels[row][col])
      #       # draw.rectangle((col * WIDTH / self.size, row * HEIGHT / self.size, (col + 1) * WIDTH/ self.size, (row + 1) * HEIGHT / self.size), fill=(255, 40, 109), outline=(255, 40, 109))

      # yield image

    image = Image.new('RGB', (WIDTH, HEIGHT))
    image.paste((250, 240, 241), (0, 0, image.size[0], image.size[1]))
    draw = ImageDraw.Draw(image)
    for path in self.visited:
      x, y = path
      draw.rectangle((x * WIDTH / self.size, y * HEIGHT / self.size, (x + 1) * WIDTH/ self.size, (y + 1) * HEIGHT / self.size), fill=self.pixels[y][x], outline=self.pixels[y][x])
      yield image

    for path in range(1000):
      yield image

    # for path in self.visited:
    #   x, y = path
    #   draw.rectangle((x * WIDTH / self.size, y * HEIGHT / self.size, (x + 1) * WIDTH/ self.size, (y + 1) * HEIGHT / self.size), fill=(250, 240, 241), outline=(250, 240, 241))
    #   yield image

    image2 = Image.new('RGB', (WIDTH, HEIGHT))
    image2.paste((250, 240, 241), (0, 0, image2.size[0], image2.size[1]))
    for path in range(5):
      yield image2

    # image = Image.new('RGB', (WIDTH, HEIGHT))
    # image.paste((250, 240, 241), (0, 0, image.size[0], image.size[1]))
    # draw = ImageDraw.Draw(image)

    # for row in range(self.size):
    #   for col in range(self.size):
    #     if (col, row) in self.visited:
          # print(self.pixels[row][col])
          # draw.rectangle((row * WIDTH / self.size, col * HEIGHT / self.size, (row + 1) * WIDTH/ self.size, (col + 1) * HEIGHT / self.size), fill=self.pixels[row][col], outline=self.pixels[row][col])
          # draw.rectangle((col * WIDTH / self.size, row * HEIGHT / self.size, (col + 1) * WIDTH/ self.size, (row + 1) * HEIGHT / self.size), fill=(255, 40, 109), outline=(255, 40, 109))


    # yield []
