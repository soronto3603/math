import numpy as np
import random
import os
import sys
sys.path.append('../')

from scripts.renderer.renderer import *
from PIL import Image, ImageDraw, ImageFont

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

CELL = 2
PATH = 1
WALL = 0

WIDTH = 1920
HEIGHT = 1080


class RenderMaze:
  title = 'render_create_maze'
  def __init__(self, size = 100):
    self.size = size

    self.maze = np.zeros((self.size, self.size))
    for row in range(self.size):
      for column in range(self.size):
        if row % 2 == 0 and column % 2 == 0:
          self.maze[row][column] = CELL

    self.visited = np.zeros((self.size // 2, self.size // 2))
    self.visited.fill(False)

    self.q = [(0, 0)]
    self.visited[0][0] = True

    self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    self.stepCount = 0
    self.latestCell = None

  def render(self):
    while(len(self.q) > 0):
      self.stepCount += 1
      (x, y) = self.q.pop()

      random.shuffle(self.directions)
      for direction in self.directions:
        (vx, vy) = direction

        if x + vx < 0 or x + vx >= self.size // 2 or y + vy < 0 or y + vy >= self.size // 2:
          continue

        if self.visited[y + vy][x + vx]:
          continue

        self.q.append((x, y))
        self.maze[y * 2][x * 2] = PATH
        self.maze[y * 2 + vy][x * 2 + vx] = PATH
        self.maze[(y + vy) * 2][(x + vx) * 2] = PATH
        self.latestCell = ((x + vx) * 2, (y + vy) * 2)

        self.visited[y + vy][x + vx] = True
        self.q.append((x + vx, y + vy))
        break

      image = Image.new('RGB', (WIDTH, HEIGHT))

      scaledHeight = HEIGHT * 3 / 4
      diffX = (WIDTH - scaledHeight) / 2
      diffY = (HEIGHT - scaledHeight) / 2
      draw = ImageDraw.Draw(image)
      for row in range (self.size):
        for column in range(self.size):
          if (self.maze[row][column] == PATH):
            (latestX, latestY) = self.latestCell
            if latestX == column and latestY == row:
              draw.rectangle((diffX + row * scaledHeight / self.size, diffY + column * scaledHeight / self.size, diffX + (row + 1) * scaledHeight / self.size, diffY + (column + 1) * scaledHeight / self.size), fill=(255, 40, 109), outline=(255, 40, 109))
            elif (column // 2, row // 2) in self.q:
              draw.rectangle((diffX + row * scaledHeight / self.size, diffY + column * scaledHeight / self.size, diffX + (row + 1) * scaledHeight / self.size, diffY + (column + 1) * scaledHeight / self.size), fill=(144, 144, 144), outline=(144, 144, 144))
            else:
              draw.rectangle((diffX + row * scaledHeight / self.size, diffY + column * scaledHeight / self.size, diffX + (row + 1) * scaledHeight / self.size, diffY + (column + 1) * scaledHeight / self.size), fill=(255, 255, 255), outline=(255, 255, 255))
      yield image

Renderer.register(RenderMaze)
