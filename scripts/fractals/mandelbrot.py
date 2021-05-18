from multiprocessing import Pool
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

SIZE = 1024
ZOOM_DELTA = 0.01
ITER = 3000
POINT = (74 / 1000, 499 / 1000)

def mandelbrot(Re, Im, max_iter):
  c = complex(Re, Im)
  z = 0.0j
  for i in range(max_iter):
    z = z*z + c
    if(z.real*z.real + z.imag*z.imag) >= 4:
      return i
  return max_iter


def renderFrame(i, size = SIZE, zoomDelta = ZOOM_DELTA, iter = ITER, point = POINT):
  print(f'iter{i:0>4d}')
  zoom = 1 + i * i * zoomDelta
  result = np.zeros([size, size])
  for row_index, Re in enumerate(np.linspace(-2 + 3 * (1 - 1 / zoom) * point[0], 1 - 3 * (1 - 1 / zoom) * (1 - point[0]), num = size)):
      for column_index, Im in enumerate(np.linspace(-1 + 2 * (1 - 1 / zoom) * point[1], 1 - 2 * (1 - 1 / zoom) * (1 - point[1]), num = size)):
          result[row_index, column_index] = mandelbrot(Re, Im, 100)

  im = Image.fromarray(result.T)
  im = im.convert('L')
  im = im.convert('P', palette = Image.ADAPTIVE, colors = 32)
  im.putpalette([
    0, 2, 0,
    255, 170, 0,
    237, 255, 255,
    32, 107, 203,
    0, 7, 100,
  ])
  im.save(f'images/mandelbrot{i:0>4d}.png')

def render(size = SIZE, zoomDelta = ZOOM_DELTA, iter = ITER, point = POINT):
  with Pool(8) as p:
    p.map(renderFrame, [i for i in range(iter)])

def toVideo():
  os.system('ffmpeg -y -framerate 24 -i images/mandelbrot%04d.png -pix_fmt yuv420p output.mp4')
  os.system('open output.mp4')

if __name__ == '__main__':
  render()
  toVideo()