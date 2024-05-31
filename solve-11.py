# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 11: Boxed In ---"
  input = "input-11.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Area:
  def __init__(self, corners):
    self.lx, self.ly, self.ux, self.uy = [int(n) for n in corners.split(",")]
  def __repr__(self):
    return f"{self.lx},{self.ly},{self.ux},{self.uy}"
  def overlaps(self, a):
    return self.lx <= a.ux and a.lx <= self.ux and self.ly < a.uy and a.ly <= self.uy
  def tiles(self):
    s = set()
    for x in range(self.lx, self.ux):
      for y in range(self.ly, self.uy):
        s.add((x,y))
    return s

def hasOverlap(a, areas):
  for aa in areas:
    if aa != a and aa.overlaps(a):
      return True
  return False

def solve(lines):
  areas = []
  for l in lines[1:]:
    areas.append(Area(l))
  tiles = set()
  for a in areas:
    if hasOverlap(a, areas):
      tiles |= a.tiles()
  print("Solution:", len(tiles))

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
