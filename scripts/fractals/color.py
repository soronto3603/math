colors = [
  '#0A2F51',
  '#DEEDCF',
]

class ColorScaler:
  def __init__(self, minColor, maxColor):
    self.minColor = int(minColor[1: 3], 16), int(minColor[3: 5], 16), int(minColor[5: 7], 16)
    self.maxColor = int(maxColor[1: 3], 16), int(maxColor[3: 5], 16), int(maxColor[5: 7], 16)

    self.iter = min(self.maxColor[0] - self.minColor[0], self.maxColor[1] - self.minColor[1], self.maxColor[2] - self.minColor[2])
    self.rd = (self.maxColor[0] - self.minColor[0]) / self.iter
    self.gd = (self.maxColor[1] - self.minColor[1]) / self.iter
    self.bd = (self.maxColor[2] - self.minColor[2]) / self.iter
    self.currentIter = 0
  def getNextColor(self):
    index = self.currentIter % self.iter

    r = hex(int(self.minColor[0] + index * self.rd))
    r = r[2: len(r)]
    if len(r) == 1:
      r = '0' + r

    g = hex(int(self.minColor[1] + index * self.gd))
    g = g[2: len(g)]
    if len(g) == 1:
      g = '0' + g

    b = hex(int(self.minColor[2] + index * self.bd))
    b = b[2: len(b)]
    if len(b) == 1:
      b = '0' + b

    self.currentIter += 1

    return f'#{r}{g}{b}'

  def getColorByIndex(self, _index):
    index = _index % self.iter

    r = hex(int(self.minColor[0] + index * self.rd))
    r = r[2: len(r)]
    if len(r) == 1:
      r = '0' + r

    g = hex(int(self.minColor[1] + index * self.gd))
    g = g[2: len(g)]
    if len(g) == 1:
      g = '0' + g

    b = hex(int(self.minColor[2] + index * self.bd))
    b = b[2: len(b)]
    if len(b) == 1:
      b = '0' + b

    self.currentIter += 1

    return f'#{r}{g}{b}'

if __name__ == '__main__':
  scaler = ColorScaler(colors[0], colors[1])
  scaler.getNextColor()
