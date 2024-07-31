# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 28: Hall of Mirrors ---"
  input = "input-28.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.rstrip() for l in open(file, 'r').readlines()]

class EncryptMap:
  dirMap = {
    ((1,0), "/"):  (0,-1),
    ((1,0), "\\"):  (0,1),
    ((1,0), " "):  (1,0),
    ((-1,0), "/"): (0,1),
    ((-1,0), "\\"): (0,-1),
    ((-1,0), " "): (-1,0),
    ((0,1), "/"):  (-1,0),
    ((0,1), "\\"):  (1,0),
    ((0,1), " "):  (0,1),
    ((0,-1), "/"):  (1,0),
    ((0,-1), "\\"):  (-1,0),
    ((0,-1), " "):  (0,-1)
  }
  flipMap = {
    "\\": "/",
    "/": "\\",
    " ": " "
  }
  def __init__(self, lines):
    self.grid = [[c for c in l] for l in lines]
  def __repr__(self):
    return f"{'\n'.join([''.join(l) for l in self.grid])}"
  def inGrid(self, p):
    x, y = p
    return self.grid[y][x] in "/\\ "
  def get(self, p):
    x, y = p
    return self.grid[y][x]
  def set(self, p, v):
    x, y = p
    self.grid[y][x] = v
  def move(self, p, dir):
    c = self.get(p)
    nd = self.dirMap[(dir, c)]
    np = (p[0] + nd[0], p[1] + nd[1])
    self.set(p, self.flipMap[c])
    return (np, nd)

  def encrypt(self, l):
    sy = self.grid[0].index(l)
    p = (1, sy)
    d = (1, 0)
    while self.inGrid(p):
      p, d = self.move(p, d)
    return self.get(p)

def solve(lines):
  em = EncryptMap(lines)
  m = ""
  for l in "FISSION_MAILED":
    m += em.encrypt(l)
  print("Solution:", m)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
