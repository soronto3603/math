import argparse

from copy import deepcopy
from pydoc import render_doc
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import time


class RenderFloodFill:
  title = 'flood_fill'
  def __init__(self, width = 512, height= 512,alpha= 2.5):
    random.seed('hyper-cloud')
    self.alpha = alpha
    self.width = width
    self.height = height

    self.map = [[None for j in range(self.width)] for i in range(self.width)]
    self.visited = [[False for j in range(self.width)] for i in range(self.width)]
    self.visited[self.height // 2][self.width // 2]
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = [(self.height // 2, self.width // 2, (120, 120, 120) )]
    count = 1
    while len(q) > 0:
      random.shuffle(q)
      node = q.pop()

      if (count % 10000 == 0):
        c = 0
        for i in range(self.height):
          for j in range(self.width):
            if self.map[i][j] != None:
              c = c + 1
        print(c / self.width / self.height * 100, '%')

      y, x, color = node
      self.map[y][x] = color

      random.shuffle(directions)
      for [y2, x2] in directions:
        
        if y2 + y < 0 or y2 + y >= self.height:
          continue

        if x2+ x < 0 or x2 + x >= self.width:
          continue

        if self.map[y2 + y][x2 + x] == None and self.visited[y2 + y][x2 + x] == False:
          q.append((y2 + y, x2 + x, self.transformColor(color)))
          self.visited[y2 + y][x2 + x] = True
          count = count + 1
      
  def transformColor(self, color):
    _color = list(deepcopy(color))
    # randomIndex = round(random.random() * 2)
    # randomValue = self.alpha if random.random() >= 0.5 else -self.alpha
    # _color[randomIndex] = _color[randomIndex] + randomValue

    _color[0] = _color[0] + (self.alpha if random.random() >= 0.1 else -self.alpha)
    _color[1] = _color[1] + (self.alpha if random.random() >= 0.1 else -self.alpha)
    _color[2] = _color[2] + (self.alpha if random.random() >= 0.1 else -self.alpha)
    return tuple(_color)

  def render(self):
    print('render...')
    image = Image.new('RGB', [self.width, self.height])
    data = image.load()

    for x in range(image.size[0]):
      for y in range(image.size[1]):
        data[x,y] = tuple([round(color) for color in self.map[y][x]])

    image.save(f'flood_fill_{time.time()}.png')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('width', type=int)
parser.add_argument('height', type=int)
# parser.add_argument('alhpa', type=float)

args = parser.parse_args()

renderer = RenderFloodFill(args.width, args.height, 1.4)
renderer.render()

