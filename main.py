import argparse
import os
import shutil

from pathlib import Path
from typing import List
from scripts.renderer.renderer import Renderer
from scripts import render_create_maze, render_create_maze2, render_create_maze3, render_rose_maze, render_rose2

scripts: List[Renderer] = [
  render_create_maze.RenderMaze(40),
  render_create_maze2.RenderMaze2(100),
  render_create_maze3.RenderMaze3(100),
  render_rose_maze.RenderRose(),
  render_rose2.RenderRose2(),
]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('name', type=str)
parser.add_argument('render', type=int)

args = parser.parse_args()

target = None
for script in scripts:
  if script.title == args.name:
    target = script

if target is None:
  print(f'cannot found target {args.name}')
else:
  if args.render == 1:
    Path(f'./images/{target.title}').mkdir(parents=True, exist_ok=True)
    for (index, frame) in enumerate(target.render()):
      if frame == None:
        break
      print(f'./images/{target.title}/{index:0>4d}.png')
      frame.save(f'./images/{target.title}/{index:0>4d}.png')
    os.system(f'ffmpeg -y -framerate 24 -i ./images/{target.title}/%04d.png -pix_fmt yuv420p {target.title}.mp4')
    shutil.rmtree(f'./images/{target.title}')
  else:
    for (index, frame) in enumerate(target.render()):
      pass
