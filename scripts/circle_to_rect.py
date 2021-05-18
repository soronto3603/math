#%%
import numpy as np
from __future__ import annotations

#%%
class Line:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def intersectLine(self, l: Line):
    return ((l.b - self.b) / (self.a - l.a), self.a * (l.b - self.b) / (self.a - l.a) + self.b)

class Circle:
  def __init__(self, r, point):
    self.r = r
    self.point = point

  def intersectLine(self, l: Line):
    x, y = self.point

l1 = Line(1, 2)
l2 = Line(-1, 0)

print(l1.intersectLine(l2))

# %%
