from collections.abc import Iterable
from typing import Union
from abc import ABC, abstractmethod
from PIL.Image import Image

class Renderer(ABC):
  @property
  @abstractmethod
  def title(self) -> str:
    pass

  @abstractmethod
  def render(self) -> Iterable[Image]:
    pass
