from multiprocessing import Pool
from functools import partial
from PIL import Image, ImageDraw, ImageFont
import math
import os
import colorsys
from subprocess import Popen, PIPE

width, height = 1920, 1080
margin = 10
countPoint = 500

def rotate(origin, point, angle):
  """
  Rotate a point counterclockwise by a given angle around a given origin.

  The angle should be given in radians.
  """
  ox, oy = origin
  px, py = point

  qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
  qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
  return qx, qy

def renderFrame(index):
  alpha = 1 + index / 100
  circleRadius = min(width, height) - margin * 2

  HSV_tuples = [(x * 1.0 / 100, 0.5, 0.5) for x in range(100)]
  RGB_tuples = list(map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples))

  im = Image.new(mode = "RGB", size = (width, height))
  draw = ImageDraw.Draw(im)

  draw.text((50, 50), f'{alpha:2f}', fill=(255, 255, 255, 50), font=ImageFont.truetype("NanumGothicCoding.ttf", 40))

  circlePoints = []
  for i in range(countPoint):
    _x, _y = rotate((0, 0), (circleRadius / 2 * -1, 0), math.radians(360 / countPoint * i))
    draw.ellipse((_x - 1 + width / 2, _y - 1 + height / 2, _x + 1 + width / 2, _y + 1 + height / 2), fill = 'blue' )

    circlePoints.append((_x, _y))

  for (i, point) in enumerate(circlePoints):
    x, y = point
    target = int(i * alpha)
    targetX, targetY = circlePoints[target % len(circlePoints)]
    r, g, b = RGB_tuples[i % 100]
    draw.line((x + width / 2, y + height / 2, targetX + width / 2, targetY + height / 2), fill = (int(r * 255), int(g * 255), int(b * 255), 50))

  print(f'images/mandelbrote-times-table{index:0>4d}.png')
  im.save(f'images/mandelbrote-times-table{index:0>4d}.png')

def render():
  # for i in range(10000):
  #   renderFrame(i)
  with Pool(8) as p:
    p.map(renderFrame, [i for i in range(10000)])
def toVideo():
  os.system('ffmpeg -y -framerate 24 -i images/mandelbrote-times-table%04d.png -pix_fmt yuv420p output.mp4')
  os.system('open output.mp4')

if __name__ == '__main__':
  render()
  toVideo()
