import sys
import random
import numpy as np

from typing import List
from PIL import Image, ImageDraw, ImageFont
from scripts.renderer.renderer import Renderer
sys.path.append('../')


WIDTH = 1920
HEIGHT = 1080

class RenderMaze2:
  title = 'render_create_maze2'
  def __init__(self, size = 50):
    self.size = size

    self.walls = [(x, y, x + 1, y) for x in range(self.size // 2 - 1) for y in range(self.size // 2 - 1)]
    self.walls.extend([(x, y, x, y + 1) for x in range(self.size // 2) for y in range(self.size // 2 - 1)])
    self.cell_sets = [set([(x, y)]) for x in range(self.size // 2) for y in range(self.size // 2)]

    self.drawWall = []
    self.lastDrawingLength = 0
    self.lastWall = None

  def render(self):
    walls_copy = self.walls[:]
    random.shuffle(walls_copy)

    for wall in walls_copy:
      set_a = None
      set_b = None

      for s in self.cell_sets:
        if (wall[0], wall[1]) in s:
          set_a = s
        if (wall[2], wall[3]) in s:
          set_b = s

      if set_a is not set_b:
        self.cell_sets.remove(set_a)
        self.cell_sets.remove(set_b)
        self.cell_sets.append(set_a.union(set_b))
        self.walls.remove(wall)
        self.drawWall.append(wall)
        self.lastWall = wall

      if self.lastDrawingLength != len(self.drawWall):
        self.lastDrawingLength = len(self.drawWall)
      else:
        continue

      image = Image.new('RGB', (WIDTH, HEIGHT))

      scaledHeight = HEIGHT * 3 /4
      diffX = (WIDTH - scaledHeight) / 2
      diffY = (HEIGHT - scaledHeight) / 2
      draw = ImageDraw.Draw(image)
      for (sourceX, sourceY, targetX, targetY) in self.drawWall:
        dx = targetX - sourceX
        dy = targetY - sourceY

        if self.lastWall[0] == sourceX and self.lastWall[1] == sourceY and self.lastWall[2] == targetX and self.lastWall[3] == targetY:
          draw.rectangle(
          (
            diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
            diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
          ), fill=(255, 40, 109), outline=(255, 40, 109))
        else:
          draw.rectangle(
          (
            diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
            diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
            diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
          ), fill=(255, 255, 255), outline=(255, 255, 255))
      for set in self.cell_sets:
        if len(set) < 2:
          continue
        for (x, y) in list(set):
          draw.rectangle(
            (
              diffX + x * 2 * scaledHeight / self.size,
              diffY + y * 2 * scaledHeight / self.size,
              diffX + (x * 2 + 1) * scaledHeight / self.size,
              diffY + (y * 2 + 1) * scaledHeight / self.size,
            ), fill = (255, 255, 255), outline=(255, 255, 255)
          )
      yield image

    image = Image.new('RGB', (WIDTH, HEIGHT))

    scaledHeight = HEIGHT * 3 /4
    diffX = (WIDTH - scaledHeight) / 2
    diffY = (HEIGHT - scaledHeight) / 2
    draw = ImageDraw.Draw(image)
    for (sourceX, sourceY, targetX, targetY) in self.drawWall:
      dx = targetX - sourceX
      dy = targetY - sourceY

      if self.lastWall[0] == sourceX and self.lastWall[1] == sourceY and self.lastWall[2] == targetX and self.lastWall[3] == targetY:
        draw.rectangle(
        (
          diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
          diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
          diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
          diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
        ), fill=(255, 40, 109), outline=(255, 40, 109))
      else:
        draw.rectangle(
        (
          diffX + (sourceX * 2 + dx) * scaledHeight / self.size,
          diffY + (sourceY * 2 + dy) * scaledHeight / self.size,
          diffX + (sourceX * 2 + dx + 1) * scaledHeight / self.size,
          diffY + (sourceY * 2 + dy + 1) * scaledHeight / self.size,
        ), fill=(255, 255, 255), outline=(255, 255, 255))
    for set in self.cell_sets:
      if len(set) < 2:
        continue
      for (x, y) in list(set):
        draw.rectangle(
          (
            diffX + x * 2 * scaledHeight / self.size,
            diffY + y * 2 * scaledHeight / self.size,
            diffX + (x * 2 + 1) * scaledHeight / self.size,
            diffY + (y * 2 + 1) * scaledHeight / self.size,
          ), fill = (255, 255, 255), outline=(255, 255, 255)
        )
    yield image


Renderer.register(RenderMaze2)