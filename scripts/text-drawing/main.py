import string
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 5
ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']

target = Image.open('200.jpg').convert('L')
imageWidth, imageHeight = target.size

fnt = ImageFont.truetype('NanumGothic-Regular.ttf', FONT_SIZE)

def modify(image, buckets=25):
  initial_pixels = list(image.getdata())
  new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
  return ''.join(new_pixels)

pixels = modify(target)
lenPixels = len(pixels)
newImage = [pixels[index : index + imageWidth] for index in range(0, lenPixels, imageWidth)]

image = Image.new(mode = 'L', size = (imageWidth, imageHeight))
draw = ImageDraw.Draw(image)
for row in range(imageHeight // FONT_SIZE):
  for col in range(imageWidth // FONT_SIZE):
    draw.text((row * FONT_SIZE, col * FONT_SIZE), newImage[row][col], fnt = fnt, fill = (255))
image.show()
f = open('img2.txt', 'w')
f.write('\n'.join(newImage))
f.close()





# pixels = list(image.getdata())

# with open('123.jpg', 'r+') as f:
  # image.save(f, 'JPEG')