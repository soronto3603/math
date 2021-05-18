from PIL import Image, ImageDraw
import os

from color import ColorScaler

WIDTH = 1024
HEIGHT = 1152

OUTPUT_PATH = './images'
scaler = ColorScaler('#0A2F51', '#DEEDCF')
if not os.path.exists(OUTPUT_PATH):
  os.makedirs(OUTPUT_PATH)

def drawFractal(drawer, x1, y1, x2, y2, it):
  if (it > MAX_IT):
    drawTriangle(drawer, x1, y1, x2, y2)
    return

  if (x2 - x1 < 1 or y2 - y1 < 1):
    drawTriangle(drawer, x1, y1, x2, y2)
    return

  if (x1 > WIDTH and x2 > WIDTH):
    return

  if (y1 > HEIGHT and y2 > HEIGHT):
    return

  if (x1 < 0 and x2 < 0):
    return

  if (y1 < 0 and y2 < 0):
    return

  # drawTriangle(drawer, x1, y1, x2, y2, scaler.getNextColor())
  drawFractal(drawer, x1 + (x2 - x1) / 4, y1, x1 + (x2 - x1) * 3 / 4, (y1 + y2) / 2, it + 1)
  drawFractal(drawer, x1, y1 + (y2 - y1) / 2, x1 + (x2 - x1) / 2, y2, it + 1)
  drawFractal(drawer, x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2, x2, y2, it + 1)


def drawTriangle(drawer, x1, y1, x2, y2, color = 'white'):
  drawer.line([(x1, y2), (x2, y2)], fill = color, width = 1)
  drawer.line([(x2, y2), ((x1 + x2) / 2, y1)], fill = color, width = 1)
  drawer.line([((x1 + x2) / 2, y1), (x1, y2)], fill = color, width = 1)

MAX_IT = 100
MARGIN = 10

image = Image.new('RGB', (WIDTH, HEIGHT))
drawer = ImageDraw.Draw(image)

for i in range(1000):
  print(f'[iter{i}]')
  zoom = 1 + i / 100

  point = {
    'x': WIDTH / 1.9,
    'y': HEIGHT / 4,
  }
  # reset
  drawer.rectangle((0, 0, WIDTH, HEIGHT), fill=(0, 0, 0, 0))

  drawFractal(
    drawer,
    -(WIDTH * zoom - WIDTH) * point['x'] / WIDTH,
    -(HEIGHT * zoom - HEIGHT) * point['y'] / HEIGHT,
    WIDTH * zoom,
    HEIGHT * zoom,
    0)

  image.save(OUTPUT_PATH + f'/triangle{i:03d}.png', 'png')
  # image.show()

os.system('ffmpeg -y -framerate 24 -i images/triangle%03d.png -pix_fmt yuv420p output.mp4')
os.system('open output.mp4')
