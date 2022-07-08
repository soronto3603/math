#%%
import math
import numpy as np
import math
import plotly.graph_objects as go
import colorsys

from typing import List
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

size = 1000
TWO_PI = 2 * math.pi

#%%
def rotate(origin, point, angle):
  ox, oy = origin
  px, py = point

  qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
  qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
  return qx, qy

def line(array, point1, point2):
  x1, y1 = point1
  x2, y2 = point2

  if (x2 - x1 == 0):
    slope = 0
  else:
    slope = (y2 - y1) / (x2 - x1)

  b = (y1 - x1 * slope)
  fn = lambda x: x * slope + b
  for i in range(min(x2, x1), min(x2, x1) + abs(x2 - x1)):
    array[round(fn(i))][i] = 1

#%%


#%%
datas = []

# for iter in range(2.5, 9):
# for iter in range(50):
for iter in range(21):
  # iter /= 10
  array = np.zeros((size, size))
  countPoint = 50

  origin = (0, 0)
  circlePoints = []
  for i in range(countPoint):
    x, y = rotate(origin, (-size / 2, 0), math.radians(360 / countPoint * i))
    circlePoints.append((round(y + size / 2) - 1, round(x + size / 2) - 1))
    array[round(y + size / 2) - 1, round(x + size / 2) - 1] = 1

  for (index, circlePoint) in enumerate(circlePoints):
    line(array, circlePoint, circlePoints[round(index * iter) % countPoint])

  datas.append({
    'index': iter,
    'value': np.count_nonzero(array == 1),
  })
  # im = Image.fromarray(array * 255)
  # im.show()

#%%
edges = []
for i in range(len(datas)):
  if i == 0 or i == len(datas):
    continue

  if (datas[i]['value'] > sum([i['value'] for i in datas]) / len(datas) * 1.05
  or datas[i]['value'] < sum([i['value'] for i in datas]) / len(datas) * 0.95):
    edges.append(datas[i])
# %%
fig = px.line(datas, x='index', y='value')
fig.add_trace(go.Scatter(mode="markers", x=[i['index'] for i in edges], y=[i['value'] for i in edges], name=""))
fig.show()
# %%
images = []
for iter in [i['index'] for i in edges]:
  array = np.zeros((size, size))
  countPoint = 100

  origin = (0, 0)
  circlePoints = []
  for i in range(countPoint):
    x, y = rotate(origin, (-size / 2, 0), math.radians(360 / countPoint * i))
    circlePoints.append((round(y + size / 2) - 1, round(x + size / 2) - 1))
    array[round(y + size / 2) - 1, round(x + size / 2) - 1] = 1

  for (index, circlePoint) in enumerate(circlePoints):
    line(array, circlePoint, circlePoints[round(index * iter) % countPoint])

  datas.append({
    'index': iter,
    'value': np.count_nonzero(array == 1),
  })
  # im = Image.fromarray(array * 255)
  # im.show()
  images.append(array * 255)
# %%
WIDTH, HEIGHT = 4096, 2160
image = Image.new('RGB', (WIDTH, HEIGHT))

npImages = np.array(images[20:50])
for i in range(30):
  x = i % 4
  y = i // 4
  im = Image.fromarray(npImages[i])
  image.paste(im, (round(WIDTH * x / 4), round(HEIGHT * y / 7)))

image.save('text.png')
# %%
WIDTH, HEIGHT = 4096, 2160

image = Image.new('RGB', (WIDTH, HEIGHT))

for i in range(len(images)):
  img = Image.fromarray(images[i]).resize((round(WIDTH / 5), round(HEIGHT / 5))).convert('RGB')
  pixels = img.load()

  x = i % 5
  y = i // 5
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      if pixels[i,j] == (0, 0, 0):
        pixels[i,j] = (255, 255, 255)
      else:
        pixels[i,j] = (32, 29, 155)
  image.paste(img, (round(WIDTH * x / 5), round(HEIGHT * y / 5)))
image.save('123.png')
# %%
