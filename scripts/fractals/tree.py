import math, colorsys
import os
from PIL import Image, ImageDraw

left_spread = 17 + 5
right_spread = 17
WIDTH, HEIGHT = 2048, 576
maxd = 24
len = 8.0

OUTPUT_PATH = './images'
if not os.path.exists(OUTPUT_PATH):
  os.makedirs(OUTPUT_PATH)

image = Image.new('RGB', (WIDTH, HEIGHT))
drawer = ImageDraw.Draw(image)

def drawTree(x1, y1, angle, depth):
  if depth > 0:
    x2 = x1 + int(math.cos(math.radians(angle)) * depth * len)
    y2 = y1 + int(math.sin(math.radians(angle)) * depth * len)

    (r, g, b) = colorsys.hsv_to_rgb(float(depth) / maxd, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)

    if depth < 5:
      drawer.line([x1, y1, x2, y2], (R, G, B), width = 1)
    else:
      drawer.line([x1, y1, x2, y2], fill = 'white', width = 1)

    drawTree(x2, y2, angle - left_spread, depth - maxd / 10)
    drawTree(x2, y2, angle + right_spread, depth - maxd / 10)

for i in range(1000):
  print(f'[iter{i:03d}]')
  left_spread += 1 * 0.01
  right_spread = right_spread

  drawer.rectangle((0, 0, WIDTH, HEIGHT), fill=(0, 0, 0, 0))

  drawTree(WIDTH / 2, HEIGHT * 0.9, -90, maxd)
  image.save(OUTPUT_PATH + f'/tree{i:03d}.png', 'png')

os.system('ffmpeg -y -framerate 24 -i images/tree%03d.png -pix_fmt yuv420p output.mp4')
os.system('open output.mp4')