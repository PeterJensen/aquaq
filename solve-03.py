# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 03: Short walks ---"
  input = "input-03.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Grid:
  def __init__(self):
    self.positions = [
      "  ##  ",
      " #### ",
      "######",
      "######",
      " #### ",
      "  ##  "
    ]
    self.dims = (len(self.positions[0]), len(self.positions))
  def move(self, pos, dir):
    x, y = pos
    if dir == 'U' and y-1 >= 0 and self.positions[y-1][x] == '#':
      return (x, y-1)
    elif dir == 'D' and y+1 < self.dims[1] and self.positions[y+1][x] == '#':
      return (x, y+1)
    elif dir == 'L' and x-1 >= 0 and self.positions[y][x-1] == '#':
      return (x-1, y)
    elif dir == 'R' and x+1 < self.dims[0] and self.positions[y][x+1] == '#':
      return (x+1, y)
    return (x, y)

def solve(lines):
  grid = Grid()
  pos = (2, 0)
  sum = 0
  for c in lines[0]:
    pos = grid.move(pos, c)
    sum += pos[0] + pos[1]
  print("Solution:", sum)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
