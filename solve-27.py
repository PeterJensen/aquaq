# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 27:  ---"
  input = "input-27.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else open(file, 'r').read().split("\n")

class Grid:
  def __init__(self, lines):
    self.lines = [l for l in lines if len(l) > 0]
    self.dims = (len(self.lines[0]), len(self.lines))
  def __repr__(self):
    return f"{"\n".join(self.lines)}"
  def get(self, p):
    x, y = p
    if x in range(self.dims[0]) and y in range(self.dims[1]):
      return self.lines[y][x]
    else:
      return " "
  def neighbors(self, p):
    px, py = p
    if self.get(p) != " ":
      for n in [(px-1, py), (px+1, py), (px, py-1), (px, py+1)]:
        x, y = n
        if x in range(self.dims[0]) and y in range(self.dims[1]) and self.get(n) != " ":
          yield (x, y)
  def allPos(self):
    for x in range(self.dims[0]):
      for y in range(self.dims[1]):
        yield (x, y)
  def numNeighbors(self, p):
    nn = 0
    for n in self.neighbors(p):
      nn += 1
    return nn

def findHeads(grid):
  heads = set()
  for p in grid.allPos():
    if grid.numNeighbors(p) == 1:
      heads.add(p)
  return heads

def getNextDir(grid, p, dir):
  if dir != None:
    dirRev = (-dir[0], -dir[1])
  else:
    dirRev = None
  for np in grid.neighbors(p):
    d = (np[0] - p[0], np[1] - p[1])
    if dir == None or d != dirRev:
      return d
  return None

def getWord(grid, head, dir):
  w = ""
  p = head
  pp = None
  while True:
    l = grid.get(p)
    if l == " ":
      break
    else:
      w += l
      pp = p
      p = (p[0] + dir[0], p[1] + dir[1])
  return w, pp
  
def words(grid, head):
  p = head
  dir = None
  while True:
    dir = getNextDir(grid, p, dir)
    if dir == None:
      return
    w, ep = getWord(grid, p, dir)
    yield (w, ep)
    p = ep

def wordValue(w):
  val = 0
  for l in w:
    val += ord(l) - ord("a") + 1
  return val*len(w)

def solve(lines):
  grid = Grid(lines)
  heads = findHeads(grid)
  ends = []
  sum = 0
  for h in heads:
    if h not in ends:
      for w, ep in words(grid, h):
        print(w)
        sum += wordValue(w)
      ends.append(ep)
  print("Solution:", sum)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
