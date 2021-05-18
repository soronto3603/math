import sys
import random
import numpy as np

from typing import List
from PIL import Image, ImageDraw, ImageFont
from scripts.renderer.renderer import Renderer
sys.path.append('../')


WIDTH = 1920
HEIGHT = 1080

class RenderMaze3:
  title = 'render_create_maze3'
  def __init__(self, size = 50):
    self.size = size

    self.cells = []

    self.walls = [(x, y, x + 1, y) for x in range(self.size // 2 - 1) for y in range(self.size // 2 - 1)]
    self.walls.extend([(x, y, x, y + 1) for x in range(self.size // 2) for y in range(self.size // 2 - 1)])
    self.walls.extend([(x, y, x - 1, y) for x in range(1, self.size // 2 - 1) for y in range(self.size // 2 - 1)])
    self.walls.extend([(x, y, x, y - 1) for x in range(self.size // 2 - 1) for y in range(1, self.size // 2 - 1)])
    self.cells = [(x, y) for x in range(self.size // 2) for y in range(self.size // 2)]
    self.V = [(0, 0)]

    self.drawWall = []

  def render(self):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(self.V) < len(self.cells):
      adjacencies = []
      for (x, y) in self.V:
        random.shuffle(directions)
        for (dx, dy) in directions:
          if x + dx < 0 or x + dx >= self.size or y + dy < 0 or y + dy >= self.size or (x + dx, y + dy) in self.V or (x, y, x + dx, y + dy) not in self.walls:
            continue
          adjacencies.append((x, y, x + dx, y + dy))
      (sourceX, sourceY, targetX, targetY) = random.choice(adjacencies)
      self.walls.remove((sourceX, sourceY, targetX, targetY))
      self.drawWall.append((sourceX, sourceY, targetX, targetY))
      self.V.append((targetX, targetY))

      image = Image.new('RGB', (WIDTH, HEIGHT))

      scaledHeight = HEIGHT * 3 / 4
      diffX = (WIDTH - scaledHeight) / 2
      diffY = (HEIGHT - scaledHeight) / 2
      draw = ImageDraw.Draw(image)
      for (sourceX, sourceY, targetX, targetY) in self.drawWall:
        dx = targetX - sourceX
        dy = targetY - sourceY

        draw.rectangle(
          (
            diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
            diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
          ), fill=(255, 255, 255), outline=(255, 255, 255))

      for (x, y) in self.V:
        draw.rectangle(
          (
            diffX + x * 2 * scaledHeight / self.size,
            diffY + y * 2 * scaledHeight / self.size,
            diffX + (x * 2 + 1) * scaledHeight / self.size,
            diffY + (y * 2 + 1) * scaledHeight / self.size,
          ), fill = (255, 255, 255), outline=(255, 255, 255)
        )
      yield image
    for i in range(30):
      image = Image.new('RGB', (WIDTH, HEIGHT))

      scaledHeight = HEIGHT * 3 / 4
      diffX = (WIDTH - scaledHeight) / 2
      diffY = (HEIGHT - scaledHeight) / 2
      draw = ImageDraw.Draw(image)
      for (sourceX, sourceY, targetX, targetY) in self.drawWall:
        dx = targetX - sourceX
        dy = targetY - sourceY

        draw.rectangle(
          (
            diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
            diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
          ), fill=(255, 255, 255), outline=(255, 255, 255))

      for (x, y) in self.V:
        draw.rectangle(
          (
            diffX + x * 2 * scaledHeight / self.size,
            diffY + y * 2 * scaledHeight / self.size,
            diffX + (x * 2 + 1) * scaledHeight / self.size,
            diffY + (y * 2 + 1) * scaledHeight / self.size,
          ), fill = (255, 255, 255), outline=(255, 255, 255)
        )
      yield image


Renderer.register(RenderMaze3)